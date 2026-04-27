#!/usr/bin/env python3
"""Shared Autonomous Governance & Evidence Intelligence generation helpers."""

from __future__ import annotations

import csv
import hashlib
import json
import re
from pathlib import Path


MODE_OUTPUTS = {
    "pack": [
        "autonomous-governance-master-pack.md",
        "contract-scope-risk-pack.md",
        "stakeholder-sentiment-radar.md",
        "migration-evidence-vault-index.md",
        "cutover-rehearsal-scorecard.md",
        "finance-reconciliation-judge.md",
        "license-cost-optimization-pack.md",
        "alm-release-train-plan.md",
        "training-effectiveness-score.md",
        "isv-exit-strategy-pack.md",
        "country-regulatory-pack.md",
        "legacy-archive-strategy.md",
        "hyperautomation-modernization-map.md",
        "board-risk-forecast.md",
        "end-to-end-process-twin.md",
        "meeting-decision-action-log.md",
    ],
    "evidence-vault": ["migration-evidence-vault-index.md", "evidence-freshness-report.md", "go-live-evidence-gap-report.md", "evidence-chain-of-custody.md", "audit-ready-signoff-binder.md"],
    "scope-guard": ["scope-baseline-ledger.md", "change-request-impact-register.md", "contract-scope-risk-pack.md", "commercial-approval-matrix.md"],
    "contract-risk": ["contract-scope-risk-pack.md", "sow-assumption-tracker.md", "commercial-approval-matrix.md", "change-request-impact-register.md"],
    "cutover-rehearsal": ["cutover-rehearsal-plan.md", "cutover-rehearsal-scorecard.md", "cutover-rehearsal-defect-log.md", "cutover-critical-path-variance.md"],
    "reconciliation-judge": ["finance-reconciliation-judge.md", "inventory-reconciliation-judge.md", "customer-vendor-reconciliation-judge.md", "open-transaction-reconciliation-judge.md", "reconciliation-tolerance-matrix.md"],
    "license-cost": ["license-cost-optimization-pack.md", "role-license-mapping.md", "license-overallocation-report.md", "subscription-cost-forecast.md"],
    "alm-release": ["alm-release-train-plan.md", "environment-readiness-gate.md", "release-freeze-calendar.md", "deployment-risk-register.md"],
    "training-readiness": ["training-effectiveness-score.md", "training-adoption-risk-map.md", "role-training-coverage-matrix.md"],
    "isv-exit": ["isv-exit-strategy-pack.md", "isv-transition-risk-register.md", "vendor-termination-checklist.md"],
    "country-regulatory-pack": ["country-regulatory-pack.md", "localization-obligation-map.md", "tax-einvoicing-readiness-gate.md"],
    "archive-strategy": ["legacy-archive-strategy.md", "archive-access-model.md", "archive-retention-evidence.md"],
    "hyperautomation-pack": ["hyperautomation-modernization-map.md", "automation-candidate-backlog.md", "power-platform-opportunity-pack.md"],
    "board-risk": ["board-risk-forecast.md", "executive-go-live-probability.md", "budget-scope-test-risk-trend.md"],
    "process-twin": ["end-to-end-process-twin.md", "process-risk-traceability-map.md"],
    "meeting-copilot": ["meeting-decision-action-log.md", "meeting-to-backlog-bridge.md", "decision-bottleneck-register.md", "stakeholder-sentiment-radar.md"],
}


DOMAINS = {
    "Contract and Scope": ["contract", "sow", "scope", "change request", "commercial", "approval"],
    "Stakeholder Sentiment": ["stakeholder", "resistance", "decision", "meeting", "owner", "alignment"],
    "Evidence Vault": ["evidence", "proof", "sign-off", "audit", "gate", "missing"],
    "Cutover Rehearsal": ["cutover", "rehearsal", "rollback", "critical path", "smoke", "war room"],
    "Reconciliation": ["reconciliation", "balance", "variance", "finance", "inventory", "customer", "vendor"],
    "License and Cost": ["license", "subscription", "cost", "budget", "role", "user"],
    "ALM Release": ["alm", "release", "deploy", "environment", "build", "freeze"],
    "Training": ["training", "adoption", "key user", "uat", "learning", "readiness"],
    "ISV Exit": ["isv", "vendor", "addon", "contract", "replacement", "termination"],
    "Country Regulatory": ["country", "tax", "e-invoicing", "retention", "privacy", "localization"],
    "Archive Strategy": ["archive", "history", "retention", "readonly", "legacy", "reporting"],
    "Hyperautomation": ["automation", "logic apps", "power automate", "fabric", "dataverse", "api"],
    "Board Risk": ["board", "forecast", "probability", "budget", "scope", "risk"],
    "Process Twin": ["lead-to-cash", "order-to-cash", "procure-to-pay", "process", "twin", "traceability"],
    "Meeting Copilot": ["meeting", "minutes", "agenda", "action", "decision", "backlog"],
}


def read_source(source: Path) -> str:
    if source.is_file():
        return source.read_text(encoding="utf-8", errors="ignore")
    parts = []
    if source.exists():
        for path in sorted(source.rglob("*")):
            if path.is_file() and path.suffix.lower() in {".md", ".json", ".csv", ".txt", ".xpp", ".xpo"}:
                parts.append(path.read_text(encoding="utf-8", errors="ignore"))
    return "\n".join(parts)


def score_domain(text: str, keywords: list[str]) -> tuple[int, str]:
    lower = text.lower()
    hits = sum(1 for keyword in keywords if keyword.lower() in lower)
    blockers = len(re.findall(r"\b(blocked|missing|critical|overdue|unapproved|failed|variance|risk)\b", lower))
    value = max(20, min(100, 52 + hits * 9 - min(blockers, 30)))
    status = "Blocked" if value < 50 else "Ready" if value >= 75 else "Needs control"
    return value, status


def governance_scores(source: Path) -> dict[str, dict[str, object]]:
    text = read_source(source)
    return {
        domain: {"score": score_domain(text, keywords)[0], "status": score_domain(text, keywords)[1], "keywords": keywords}
        for domain, keywords in DOMAINS.items()
    }


def render_artifact(title: str, source: Path, mode: str) -> str:
    scores = governance_scores(source)
    rows = "\n".join(
        f"| {domain} | {item['score']} | {item['status']} | Generate evidence-backed owner action |"
        for domain, item in scores.items()
    )
    blockers = "\n".join(
        f"- {domain}: {item['status']} at score {item['score']}"
        for domain, item in scores.items()
        if item["status"] == "Blocked"
    ) or "- No domain is automatically blocked from the available evidence."
    return f"""# {title}

## Autonomous Governance Scores

| Domain | Score | Status | AI-KI Next Action |
| --- | --- | --- | --- |
{rows}

## Blocking Signals

{blockers}

## Required Controls

- Contract, scope, commercial impact, and change requests must be traceable.
- Evidence must be current, attributable, and linked to gates.
- Cutover rehearsal defects must be closed or accepted by accountable owners.
- Finance, inventory, customer, vendor, and open transaction reconciliation must have tolerance-based sign-off.
- License, ALM, training, ISV, regulatory, archive, automation, board risk, process twin, and meeting actions must be routed to accountable skills.

## AI-KI USP

This output turns project governance from manual status collection into evidence-driven control: risks, missing proof, decisions, approvals, and next actions are derived from the same migration evidence base.
"""


def write_outputs(source: Path, output: Path, mode: str) -> None:
    output.mkdir(parents=True, exist_ok=True)
    for filename in MODE_OUTPUTS[mode]:
        (output / filename).write_text(render_artifact(filename[:-3].replace("-", " ").title(), source, mode), encoding="utf-8")
    scores = governance_scores(source)
    (output / "governance-readiness.json").write_text(json.dumps(scores, indent=2), encoding="utf-8")
    with (output / "governance-readiness.csv").open("w", encoding="utf-8", newline="") as handle:
        writer = csv.writer(handle)
        writer.writerow(["Domain", "Score", "Status"])
        for domain, item in scores.items():
            writer.writerow([domain, item["score"], item["status"]])
    if mode == "evidence-vault":
        write_evidence_manifest(source, output)


def evidence_files(source: Path) -> list[Path]:
    if source.is_file():
        return [source]
    if not source.exists():
        return []
    suffixes = {".md", ".json", ".csv", ".txt", ".xpp", ".xpo", ".xlsx", ".pptx", ".pdf", ".docx"}
    return sorted(path for path in source.rglob("*") if path.is_file() and path.suffix.lower() in suffixes)


def sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for block in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(block)
    return digest.hexdigest()


def write_evidence_manifest(source: Path, output: Path) -> None:
    rows = []
    hash_lines = []
    for path in evidence_files(source):
        try:
            file_hash = sha256(path)
        except OSError:
            continue
        item = {
            "path": str(path),
            "name": path.name,
            "size_bytes": path.stat().st_size,
            "sha256": file_hash,
            "gate": classify_evidence_gate(path),
            "owner": classify_evidence_owner(path),
        }
        rows.append(item)
        hash_lines.append(f"{file_hash}  {path}")
    (output / "evidence-manifest.json").write_text(json.dumps(rows, indent=2), encoding="utf-8")
    with (output / "evidence-manifest.csv").open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=["path", "name", "size_bytes", "sha256", "gate", "owner"])
        writer.writeheader()
        writer.writerows(rows)
    (output / "evidence-hashes.sha256").write_text("\n".join(hash_lines) + ("\n" if hash_lines else ""), encoding="utf-8")


def classify_evidence_gate(path: Path) -> str:
    text = path.name.lower()
    if any(word in text for word in ["ciso", "security", "pci", "attack"]):
        return "Security/CISO"
    if any(word in text for word in ["reconciliation", "finance", "ledger", "inventory"]):
        return "Finance reconciliation"
    if any(word in text for word in ["cutover", "smoke", "rollback", "rehearsal"]):
        return "Cutover"
    if any(word in text for word in ["uat", "test", "quality"]):
        return "UAT/Test"
    return "General evidence"


def classify_evidence_owner(path: Path) -> str:
    gate = classify_evidence_gate(path)
    return {
        "Security/CISO": "CISO",
        "Finance reconciliation": "Finance owner",
        "Cutover": "Cutover lead",
        "UAT/Test": "QA/Test lead",
    }.get(gate, "PMO")


def run_cli(mode: str, description: str) -> int:
    import argparse

    parser = argparse.ArgumentParser(description=description)
    parser.add_argument("source")
    parser.add_argument("--output", required=True)
    args = parser.parse_args()
    write_outputs(Path(args.source), Path(args.output), mode)
    print(f"Generated {mode} outputs into {Path(args.output).resolve()}")
    return 0
