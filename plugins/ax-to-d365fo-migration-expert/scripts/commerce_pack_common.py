#!/usr/bin/env python3
"""Shared Commerce/CXP/CRM/POS pack generation helpers."""

from __future__ import annotations

import csv
import json
import re
from pathlib import Path


WORKSTREAMS = {
    "cxp_journey": ["cxp", "customer experience", "journey", "loyalty", "omnichannel"],
    "crm_dataverse": ["crm", "dataverse", "customer engagement", "contact", "opportunity", "case", "dual-write"],
    "lead_management": ["lead", "pipeline", "sales funnel", "campaign", "qualification", "lead-to-cash"],
    "customer_master": ["customer", "contact", "identity", "master", "dataverse"],
    "commerce_hq": ["commerce", "retail", "channel", "assortment", "pricing", "promotion"],
    "commerce_scale_unit": ["csu", "scale unit", "channel db", "retail server", "async", "real-time service"],
    "pos": ["pos", "point of sale", "mpos", "cpos", "kasse", "checkout", "cashier"],
    "pos_offline": ["offline", "offline db", "offline sync", "offline payments", "store offline"],
    "store_operations": ["store", "filiale", "shift", "end of day", "returns", "pickup", "inventory lookup"],
    "payments_pci": ["payment", "terminal", "refund", "settlement", "pci", "tokenization", "acquirer"],
    "omnichannel_ecommerce": ["e-commerce", "online store", "bopis", "ship-from-store", "click and collect"],
    "loyalty_promotions": ["loyalty", "points", "tiers", "coupon", "promotion", "discount"],
    "pricing_assortment": ["pricing", "assortment", "catalog", "variant", "publishing"],
    "channel_data_sync": ["sync", "channel data", "async job", "hq sync", "channel db"],
    "commerce_cutover": ["cutover", "go-live", "smoke", "rollback", "war room"],
}


PACK_OUTPUTS = {
    "pack": [
        "commerce-master-pack.md",
        "cxp-journey-map.md",
        "crm-fit-gap-pack.md",
        "lead-management-migration-pack.md",
        "lead-to-cash-traceability.md",
        "customer-master-harmonization.md",
        "commerce-channel-readiness.md",
        "commerce-scale-unit-readiness.md",
        "commerce-sync-risk-register.md",
        "channel-data-sync-monitoring.md",
        "pos-readiness-pack.md",
        "pos-offline-continuity-pack.md",
        "offline-sync-test-plan.md",
        "offline-recovery-runbook.md",
        "pos-hardware-readiness.md",
        "store-operations-readiness.md",
        "store-training-pack.md",
        "store-cutover-smoke-tests.md",
        "commerce-cutover-runbook.md",
        "commerce-go-live-gate.md",
        "payment-reconciliation-pack.md",
        "payment-cutover-checklist.md",
        "commerce-security-pci-gate.md",
        "omnichannel-order-flow-map.md",
        "loyalty-migration-pack.md",
        "pricing-promotion-migration-pack.md",
        "assortment-catalog-migration-pack.md",
        "call-center-migration-pack.md",
        "marketplace-integration-pack.md",
        "commerce-analytics-pack.md",
        "commerce-hypercare-pack.md",
    ],
    "cutover": ["commerce-cutover-runbook.md", "store-cutover-smoke-tests.md", "commerce-go-live-gate.md"],
    "offline": ["pos-offline-continuity-pack.md", "offline-recovery-runbook.md", "offline-sync-test-plan.md"],
    "crm": ["crm-fit-gap-pack.md", "lead-management-migration-pack.md", "lead-to-cash-traceability.md", "customer-master-harmonization.md"],
    "store": ["store-operations-readiness.md", "pos-hardware-readiness.md", "store-training-pack.md"],
    "payments": ["payment-reconciliation-pack.md", "commerce-security-pci-gate.md", "payment-cutover-checklist.md"],
    "omnichannel": ["omnichannel-order-flow-map.md", "commerce-analytics-pack.md", "marketplace-integration-pack.md"],
}


def analysis_text(analysis_dir: Path) -> str:
    parts = []
    if analysis_dir.exists():
        for path in sorted(analysis_dir.glob("*")):
            if path.is_file() and path.suffix.lower() in {".md", ".csv", ".json", ".xpp", ".xpo", ".txt"}:
                parts.append(path.read_text(encoding="utf-8", errors="ignore"))
    return "\n".join(parts)


def score(text: str, keywords: list[str]) -> int:
    lower = text.lower()
    hits = sum(1 for keyword in keywords if keyword.lower() in lower)
    risk_hits = len(re.findall(r"\b(blocked|critical|missing|risk|offline|pci|payment|sync)\b", lower))
    return max(20, min(100, 45 + hits * 12 - min(risk_hits, 25)))


def readiness(analysis_dir: Path) -> dict[str, dict[str, object]]:
    text = analysis_text(analysis_dir)
    result = {}
    for name, keywords in WORKSTREAMS.items():
        value = score(text, keywords)
        blocked = value < 50 or (name in {"commerce_scale_unit", "pos_offline", "payments_pci"} and value < 75)
        result[name] = {
            "score": value,
            "status": "Blocked" if blocked else "Ready" if value >= 75 else "Needs control",
            "keywords": keywords,
        }
    return result


def render_artifact(title: str, analysis_dir: Path) -> str:
    scores = readiness(analysis_dir)
    rows = "\n".join(
        f"| {name.replace('_', ' ').title()} | {item['score']} | {item['status']} | Validate evidence and assign owner |"
        for name, item in scores.items()
    )
    return f"""# {title}

## Commerce/CXP/CRM/POS Readiness

| Workstream | Score | Status | Next Action |
| --- | --- | --- | --- |
{rows}

## Gate Rules

- CSU, POS Offline, Payments/PCI, Store Smoke Tests, Channel Sync, Offline Recovery, Payment Reconciliation, Security/PCI, Customer Master, and Lead-to-Cash evidence are go-live critical.
- Mark Commerce go-live as blocked when critical evidence is missing or a critical readiness score is below 75.

## AI-KI Actions

- Generate role-specific questions.
- Convert missing evidence into work items.
- Route blockers to Commerce, POS, Payments, CISO, Legal, Finance, CRM, or Store Operations skills.
"""


def write_outputs(analysis_dir: Path, output: Path, mode: str) -> None:
    output.mkdir(parents=True, exist_ok=True)
    for name in PACK_OUTPUTS[mode]:
        title = name[:-3].replace("-", " ").title()
        (output / name).write_text(render_artifact(title, analysis_dir), encoding="utf-8")
    if mode in {"pack", "cutover", "offline", "crm", "store", "payments", "omnichannel"}:
        data = readiness(analysis_dir)
        (output / "commerce-readiness.json").write_text(json.dumps(data, indent=2), encoding="utf-8")
        with (output / "commerce-readiness.csv").open("w", encoding="utf-8", newline="") as handle:
            writer = csv.writer(handle)
            writer.writerow(["Workstream", "Score", "Status"])
            for key, item in data.items():
                writer.writerow([key, item["score"], item["status"]])


def run_cli(mode: str, description: str) -> int:
    import argparse

    parser = argparse.ArgumentParser(description=description)
    parser.add_argument("analysis_dir")
    parser.add_argument("--output", required=True)
    args = parser.parse_args()
    write_outputs(Path(args.analysis_dir), Path(args.output), mode)
    print(f"Generated {mode} outputs into {Path(args.output).resolve()}")
    return 0
