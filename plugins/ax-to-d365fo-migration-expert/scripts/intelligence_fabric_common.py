#!/usr/bin/env python3
"""Shared Migration Intelligence Fabric generators."""

from __future__ import annotations

import csv
import json
from pathlib import Path


MODE_OUTPUTS = {
    "pack": ["intelligence-fabric-master-pack.md", "migration-memory-ledger.md", "benchmark-scorecard.md", "portfolio-control-tower.md", "scenario-lab-pack.md", "delivery-quality-audit.md", "migration-war-game-plan.md", "value-realization-engine.md"],
    "memory": ["migration-memory-ledger.md", "lessons-learned-memory.md", "decision-pattern-library.md"],
    "benchmark": ["benchmark-scorecard.md", "peer-comparison-report.md", "migration-outlier-report.md"],
    "portfolio": ["portfolio-control-tower.md", "rollout-wave-optimizer.md", "portfolio-risk-comparator.md"],
    "scenario": ["scenario-lab-pack.md", "strategy-comparison-matrix.md", "business-case-scenario-pack.md"],
    "quality": ["delivery-quality-audit.md", "paper-readiness-detector.md", "artifact-completeness-audit.md"],
    "debt": ["technical-debt-liquidation-plan.md", "modernization-sprint-backlog.md", "debt-risk-burndown.md"],
    "fabric": ["fabric-advisor-pack.md", "data-product-roadmap.md", "lakehouse-powerbi-modernization.md"],
    "integration": ["integration-resilience-pack.md", "retry-replay-idempotency-checklist.md", "integration-observability-map.md"],
    "security": ["security-attack-surface-map.md", "privileged-access-risk-map.md", "secret-service-account-register.md"],
    "sustainability": ["sustainability-assessment.md", "cloud-footprint-reduction-plan.md", "data-volume-reduction-score.md"],
    "pmo": ["pmo-negotiation-pack.md", "scope-budget-quality-tradeoff.md", "steering-negotiation-brief.md"],
    "kt": ["knowledge-transfer-exam.md", "support-readiness-exam.md", "kt-gap-register.md"],
    "wargame": ["migration-war-game-plan.md", "failure-simulation-scorecard.md", "resilience-recovery-backlog.md"],
    "value": ["value-realization-engine.md", "post-go-live-kpi-tracker.md", "benefit-realization-scorecard.md"],
    "improvement": ["continuous-improvement-backlog.md", "post-hypercare-modernization-roadmap.md", "optimization-opportunity-register.md"],
}


def read_source(path: Path) -> str:
    if path.is_file():
        return path.read_text(encoding="utf-8", errors="ignore")
    parts = []
    if path.exists():
        for item in sorted(path.rglob("*")):
            if item.is_file() and item.suffix.lower() in {".md", ".json", ".csv", ".txt"}:
                parts.append(item.read_text(encoding="utf-8", errors="ignore"))
    return "\n".join(parts)


def score(text: str, mode: str) -> int:
    lower = text.lower()
    hits = sum(lower.count(word) for word in [mode, "risk", "evidence", "decision", "scope", "test", "cutover", "value"])
    return max(25, min(100, 50 + hits))


def render(title: str, source: Path, mode: str) -> str:
    value = score(read_source(source), mode)
    status = "Ready" if value >= 75 else "Needs control" if value >= 50 else "Blocked"
    return f"""# {title}

## Intelligence Score

| Mode | Score | Status |
| --- | ---: | --- |
| {mode} | {value} | {status} |

## AI-KI Findings

- Reuse prior migration memory where available.
- Compare current scope, effort, risk, test and cutover evidence against baselines.
- Route missing evidence to the Master Orchestrator.
- Convert findings into portfolio, scenario, quality, resilience, value, or improvement actions.

## Next Actions

- Validate assumptions.
- Assign owner.
- Add evidence.
- Generate next command pack.
"""


def write_outputs(source: Path, output: Path, mode: str) -> None:
    output.mkdir(parents=True, exist_ok=True)
    for filename in MODE_OUTPUTS[mode]:
        (output / filename).write_text(render(filename[:-3].replace("-", " ").title(), source, mode), encoding="utf-8")
    payload = {"mode": mode, "score": score(read_source(source), mode), "outputs": MODE_OUTPUTS[mode]}
    (output / "intelligence-readiness.json").write_text(json.dumps(payload, indent=2), encoding="utf-8")
    with (output / "intelligence-readiness.csv").open("w", encoding="utf-8", newline="") as handle:
        writer = csv.writer(handle)
        writer.writerow(["Mode", "Score"])
        writer.writerow([mode, payload["score"]])


def run_cli(mode: str, description: str) -> int:
    import argparse
    parser = argparse.ArgumentParser(description=description)
    parser.add_argument("source")
    parser.add_argument("--output", required=True)
    args = parser.parse_args()
    write_outputs(Path(args.source), Path(args.output), mode)
    print(f"Generated {mode} intelligence outputs into {Path(args.output).resolve()}")
    return 0
