#!/usr/bin/env python3
"""Generate Migration Intelligence Fabric assets."""

from __future__ import annotations

import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]

SKILLS = [
    "ax-migration-intelligence-fabric-orchestrator", "ax-migration-migration-memory", "ax-migration-benchmarking-analyst",
    "ax-migration-portfolio-control-tower", "ax-migration-scenario-lab", "ax-migration-delivery-quality-auditor",
    "ax-migration-technical-debt-liquidator", "ax-migration-fabric-data-product-advisor", "ax-migration-integration-resilience-engineer",
    "ax-migration-security-attack-surface-mapper", "ax-migration-sustainability-advisor", "ax-migration-pmo-negotiator",
    "ax-migration-knowledge-transfer-examiner", "ax-migration-war-game-master", "ax-migration-value-realization-engine",
    "ax-migration-continuous-improvement-lead", "ax-migration-peer-comparison-analyst", "ax-migration-rollout-wave-optimizer",
    "ax-migration-quality-maturity-scorer", "ax-migration-post-go-live-optimizer",
]

TEMPLATES = [
    "intelligence-fabric-master-pack.md", "migration-memory-ledger.md", "lessons-learned-memory.md", "decision-pattern-library.md",
    "benchmark-scorecard.md", "peer-comparison-report.md", "migration-outlier-report.md", "portfolio-control-tower.md",
    "rollout-wave-optimizer.md", "legal-entity-wave-map.md", "scenario-lab-pack.md", "strategy-comparison-matrix.md",
    "business-case-scenario-pack.md", "delivery-quality-audit.md", "paper-readiness-detector.md", "artifact-completeness-audit.md",
    "technical-debt-liquidation-plan.md", "modernization-sprint-backlog.md", "debt-risk-burndown.md", "fabric-advisor-pack.md",
    "data-product-roadmap.md", "lakehouse-powerbi-modernization.md", "integration-resilience-pack.md", "retry-replay-idempotency-checklist.md",
    "integration-observability-map.md", "security-attack-surface-map.md", "privileged-access-risk-map.md", "secret-service-account-register.md",
    "sustainability-assessment.md", "cloud-footprint-reduction-plan.md", "data-volume-reduction-score.md", "pmo-negotiation-pack.md",
    "scope-budget-quality-tradeoff.md", "steering-negotiation-brief.md", "knowledge-transfer-exam.md", "support-readiness-exam.md",
    "kt-gap-register.md", "migration-war-game-plan.md", "failure-simulation-scorecard.md", "resilience-recovery-backlog.md",
    "value-realization-engine.md", "post-go-live-kpi-tracker.md", "benefit-realization-scorecard.md", "continuous-improvement-backlog.md",
    "post-hypercare-modernization-roadmap.md", "optimization-opportunity-register.md", "portfolio-risk-comparator.md",
    "wave-readiness-heatmap.md", "quality-maturity-score.md", "post-go-live-optimization-plan.md", "migration-memory-index.md",
    "benchmark-baseline.json.md", "scenario-assumption-register.md", "war-game-runbook.md", "value-leakage-detector.md",
    "continuous-improvement-command-board.md", "fabric-governance-map.md", "integration-support-ownership.md", "security-control-prioritization.md",
    "sustainability-executive-narrative.md", "portfolio-executive-briefing.md",
]

CONFIGS = {
    "intelligence-fabric-rules.json": {"domains": ["memory", "benchmark", "portfolio", "scenario", "quality", "value"]},
    "benchmarking-rules.json": {"metrics": ["scope", "effort", "risk", "test", "cutover", "hypercare"]},
    "portfolio-control-rules.json": {"wave_drivers": ["risk", "value", "readiness", "country", "legal entity"]},
    "scenario-lab-rules.json": {"scenarios": ["reimplementation", "hybrid", "technical upgrade", "phased rollout", "scope reduced"]},
    "quality-audit-rules.json": {"checks": ["artifact completeness", "test evidence", "gate evidence", "owner clarity"]},
    "technical-debt-rules.json": {"drivers": ["custom code", "direct sql", "old isv", "manual process", "unsupported pattern"]},
    "fabric-advisor-rules.json": {"targets": ["Fabric", "Lakehouse", "Power BI", "Dataverse", "data product"]},
    "integration-resilience-rules.json": {"controls": ["retry", "replay", "idempotency", "monitoring", "queue", "owner"]},
    "security-attack-surface-rules.json": {"surfaces": ["roles", "apis", "secrets", "pos", "integrations", "service accounts"]},
    "value-realization-rules.json": {"kpis": ["adoption", "cost", "cycle time", "automation", "defects", "benefits"]},
}

COMMANDS = {
    "intelligence-pack": ("generate_intelligence_pack.py", "pack"),
    "migration-memory": ("generate_migration_memory.py", "memory"),
    "benchmark": ("generate_benchmark.py", "benchmark"),
    "portfolio-control": ("generate_portfolio_control.py", "portfolio"),
    "scenario-lab": ("generate_scenario_lab.py", "scenario"),
    "quality-audit": ("generate_quality_audit.py", "quality"),
    "debt-liquidator": ("generate_debt_liquidator.py", "debt"),
    "fabric-advisor": ("generate_fabric_advisor.py", "fabric"),
    "integration-resilience": ("generate_integration_resilience.py", "integration"),
    "attack-surface": ("generate_attack_surface.py", "security"),
    "sustainability": ("generate_sustainability.py", "sustainability"),
    "pmo-negotiator": ("generate_pmo_negotiator.py", "pmo"),
    "knowledge-transfer-exam": ("generate_knowledge_transfer_exam.py", "kt"),
    "war-game": ("generate_war_game.py", "wargame"),
    "value-realization": ("generate_value_realization.py", "value"),
    "continuous-improvement": ("generate_continuous_improvement.py", "improvement"),
}


def main() -> int:
    for name in SKILLS:
        d = ROOT / "skills" / name
        d.mkdir(parents=True, exist_ok=True)
        focus = name.replace("ax-migration-", "").replace("-", " ")
        (d / "SKILL.md").write_text(f"---\nname: {name}\ndescription: Use when migration intelligence fabric work needs {focus}, reusable knowledge, benchmarking, portfolio control, scenario simulation, quality audit, resilience, value realization, or continuous improvement.\n---\n\n# {name}\n\nUse this skill to convert migration evidence into Migration Intelligence Fabric outputs for {focus}.\n\n## Outputs\n\n- Evidence-backed score.\n- Risks and missing inputs.\n- Owner actions.\n- Next CLI commands.\n- Reusable migration knowledge.\n", encoding="utf-8")
    for name in TEMPLATES:
        title = name[:-3].replace("-", " ").title()
        (ROOT / "templates" / name).write_text(f"# {title}\n\n## Purpose\n\nMigration Intelligence Fabric artifact for reusable migration knowledge, benchmarking, portfolio control, scenarios, quality, resilience, value realization, or continuous improvement.\n\n## Score\n\n| Area | Status | Evidence | Next Action |\n| --- | --- | --- | --- |\n| Intelligence | Needs control | Source evidence required | Route to responsible skill |\n\n## Output\n\n- Decision summary.\n- Evidence gaps.\n- Risk and value signals.\n- Owner actions.\n", encoding="utf-8")
    for name, payload in CONFIGS.items():
        (ROOT / "config" / name).write_text(json.dumps(payload, indent=2), encoding="utf-8")
    for _, (filename, mode) in COMMANDS.items():
        (ROOT / "scripts" / filename).write_text(f"#!/usr/bin/env python3\nfrom intelligence_fabric_common import run_cli\n\nif __name__ == \"__main__\":\n    raise SystemExit(run_cli(\"{mode}\", \"Generate {mode} intelligence outputs.\"))\n", encoding="utf-8")
    print(f"Generated {len(SKILLS)} skills, {len(TEMPLATES)} templates, {len(CONFIGS)} configs, {len(COMMANDS)} scripts.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
