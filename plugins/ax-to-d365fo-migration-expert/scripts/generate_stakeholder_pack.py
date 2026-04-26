#!/usr/bin/env python3
"""Generate extended stakeholder packs for AX to D365FO migration programs."""

from __future__ import annotations

import argparse
import csv
import json
import re
from pathlib import Path


STAKEHOLDERS = {
    "cfo": {
        "title": "CFO Finance Leadership Pack",
        "focus": ["budget", "ROI", "TCO", "benefits realization", "audit", "closing readiness"],
        "outputs": ["budget-control-pack.md", "roi-benefits-realization.md", "tco-model.md", "audit-closing-readiness.md"],
    },
    "coo": {
        "title": "COO Operations Continuity Pack",
        "focus": ["operational continuity", "process disruption", "dual-run", "warehouse", "production", "supply chain"],
        "outputs": ["operational-continuity-pack.md", "process-disruption-radar.md", "dual-run-operating-model.md"],
    },
    "data": {
        "title": "Data Governance Pack",
        "focus": ["data ownership", "cleansing", "reconciliation", "master data", "archive", "retention"],
        "outputs": ["data-ownership-raci.md", "data-cleansing-backlog.md", "data-reconciliation-pack.md", "archive-retention-decision-pack.md"],
    },
    "integration": {
        "title": "Integration Owner Pack",
        "focus": ["interface criticality", "API modernization", "middleware", "retry", "reconciliation", "cutover sequence"],
        "outputs": ["interface-criticality-matrix.md", "api-modernization-backlog.md", "integration-cutover-sequence.md"],
    },
    "qa": {
        "title": "QA and Testing Pack",
        "focus": ["test coverage", "risk-based testing", "UAT", "regression", "defect triage"],
        "outputs": ["test-coverage-matrix.md", "risk-based-test-prioritization.md", "uat-pack.md", "defect-triage-model.md"],
    },
    "enterprise-architect": {
        "title": "Enterprise Architect Pack",
        "focus": ["capability map", "application portfolio", "technical debt", "target landscape", "dependency graph"],
        "outputs": ["capability-map.md", "application-portfolio-impact.md", "technical-debt-burndown.md", "target-landscape-blueprint.md"],
    },
    "vendor": {
        "title": "Procurement and Vendor Manager Pack",
        "focus": ["ISV contracts", "license impact", "vendor readiness", "third-party replacement", "commercial decisions"],
        "outputs": ["isv-contract-risk-pack.md", "license-impact-view.md", "vendor-readiness-checklist.md", "third-party-replacement-matrix.md"],
    },
    "legal": {
        "title": "Legal and Compliance Pack",
        "focus": ["data processing", "retention", "regulatory obligations", "contract risk", "audit evidence"],
        "outputs": ["data-processing-register.md", "regulatory-obligation-matrix.md", "contractual-risk-checklist.md", "audit-evidence-binder.md"],
    },
    "support": {
        "title": "Support and ITSM Operations Pack",
        "focus": ["support model", "runbooks", "monitoring", "hypercare to BAU", "incident categories"],
        "outputs": ["support-model-generator.md", "runbook-pack.md", "monitoring-alerting-plan.md", "hypercare-to-bau-transition.md"],
    },
    "partner-sales": {
        "title": "Partner Sales and Consulting Pack",
        "focus": ["discovery", "assessment offer", "proposal", "SOW", "pricing assumptions", "executive pitch"],
        "outputs": ["discovery-workshop-kit.md", "assessment-offer-generator.md", "proposal-sow-generator.md", "client-executive-pitch-pack.md"],
    },
}


def read_all(analysis_dir: Path) -> str:
    parts = []
    for path in sorted(analysis_dir.glob("*.md")):
        parts.append(path.read_text(encoding="utf-8", errors="ignore"))
    return "\n".join(parts)


def score_for(text: str, focus: list[str]) -> int:
    lower = text.lower()
    hits = sum(1 for item in focus if item.lower() in lower)
    risk_hits = len(re.findall(r"\b(high|critical|blocked|missing|risk|gap)\b", lower))
    return max(10, min(100, 40 + hits * 10 - min(risk_hits, 30)))


def render_pack(analysis_dir: Path, key: str) -> tuple[str, int]:
    cfg = STAKEHOLDERS[key]
    text = read_all(analysis_dir)
    score = score_for(text, cfg["focus"])
    lines = [
        f"# {cfg['title']}",
        "",
        "## Readiness",
        "",
        "| Stakeholder | Score | Status |",
        "| --- | --- | --- |",
        f"| {key} | {score}/100 | {'Ready' if score >= 75 else 'Needs control' if score >= 50 else 'At risk'} |",
        "",
        "## Focus Areas",
        "",
        *[f"- {item}" for item in cfg["focus"]],
        "",
        "## Required Outputs",
        "",
        *[f"- {item}" for item in cfg["outputs"]],
        "",
        "## Decision and Action Matrix",
        "",
        "| Topic | Decision Needed | Owner | Evidence | Next Action |",
        "| --- | --- | --- | --- | --- |",
    ]
    for item in cfg["focus"]:
        lines.append(f"| {item} | Validate migration impact and control approach | {key} owner | Analysis pack | Assign action |")
    lines.extend([
        "",
        "## AI-KI Automation",
        "",
        "Use this pack to translate migration evidence into stakeholder-specific decisions, risks, backlog items, controls, and communication.",
    ])
    return "\n".join(lines) + "\n", score


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("analysis_dir")
    parser.add_argument("--stakeholder", choices=[*STAKEHOLDERS.keys(), "all"], default="all")
    parser.add_argument("--output", default="stakeholder-packs")
    args = parser.parse_args()

    analysis_dir = Path(args.analysis_dir)
    output = Path(args.output)
    output.mkdir(parents=True, exist_ok=True)
    keys = list(STAKEHOLDERS) if args.stakeholder == "all" else [args.stakeholder]
    scores = {}
    for key in keys:
        body, score = render_pack(analysis_dir, key)
        scores[key] = score
        (output / f"{key}-stakeholder-pack.md").write_text(body, encoding="utf-8")
    (output / "stakeholder-readiness.json").write_text(json.dumps(scores, indent=2), encoding="utf-8")
    with (output / "stakeholder-readiness.csv").open("w", encoding="utf-8", newline="") as handle:
        writer = csv.writer(handle)
        writer.writerow(["Stakeholder", "Score"])
        writer.writerows([[key, score] for key, score in scores.items()])
    print(f"Generated stakeholder packs into {output.resolve()}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
