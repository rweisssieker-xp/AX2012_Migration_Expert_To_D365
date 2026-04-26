#!/usr/bin/env python3
"""Generate Governance/Evidence Intelligence assets for the plugin."""

from __future__ import annotations

import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]


SKILLS = {
    "ax-migration-contract-scope-guardian": "contract, scope, SOW, change request, commercial guardrails, approval paths, and scope creep prevention",
    "ax-migration-stakeholder-sentiment-radar": "stakeholder sentiment, resistance, decision bottlenecks, alignment risk, and change fatigue",
    "ax-migration-evidence-vault-manager": "evidence vault, go-live evidence, audit binder, freshness, traceability, and missing proof control",
    "ax-migration-cutover-rehearsal-lead": "cutover rehearsals, dress rehearsals, critical path variance, runbook defects, and rollback readiness",
    "ax-migration-reconciliation-judge": "finance, inventory, customer, vendor, open transaction, and tolerance-based reconciliation sign-off",
    "ax-migration-license-cost-optimizer": "D365FO, Commerce, CRM, role, user, subscription, license, cost, and budget optimization",
    "ax-migration-alm-release-train-controller": "ALM, release train, code freeze, deployments, environments, build gates, and release readiness",
    "ax-migration-training-effectiveness-monitor": "training effectiveness, adoption, key user readiness, learning gaps, and role readiness",
    "ax-migration-isv-exit-strategist": "ISV exit, vendor replacement, contract termination, add-on retirement, and transition risk",
    "ax-migration-regulatory-country-pack-generator": "country regulatory packs, localization, tax, e-invoicing, retention, audit, and privacy obligations",
    "ax-migration-legacy-archive-strategist": "legacy archive strategy, history retention, read-only access, audit retrieval, and reporting archive",
    "ax-migration-hyperautomation-architect": "Power Platform, Logic Apps, Fabric, Dataverse, APIs, automation candidates, and modernization backlog",
    "ax-migration-board-risk-forecaster": "board risk forecast, go-live probability, budget risk, test risk, scope risk, and executive trends",
    "ax-migration-process-twin-builder": "end-to-end process twin, lead-to-cash, order-to-cash, procure-to-pay, plan-to-produce, and risk traceability",
    "ax-migration-meeting-copilot": "meeting agenda, minutes, decisions, actions, RAID updates, owner tracking, and decision memory",
    "ax-migration-autonomous-governance-orchestrator": "autonomous governance orchestration, evidence routing, gates, contracts, risks, meetings, and board control",
}


TEMPLATES = [
    "autonomous-governance-master-pack.md",
    "contract-scope-risk-pack.md",
    "change-request-impact-register.md",
    "sow-assumption-tracker.md",
    "scope-baseline-ledger.md",
    "commercial-approval-matrix.md",
    "stakeholder-sentiment-radar.md",
    "resistance-risk-map.md",
    "decision-bottleneck-register.md",
    "migration-evidence-vault-index.md",
    "evidence-freshness-report.md",
    "go-live-evidence-gap-report.md",
    "evidence-chain-of-custody.md",
    "audit-ready-signoff-binder.md",
    "cutover-rehearsal-plan.md",
    "cutover-rehearsal-scorecard.md",
    "cutover-rehearsal-defect-log.md",
    "cutover-critical-path-variance.md",
    "finance-reconciliation-judge.md",
    "inventory-reconciliation-judge.md",
    "customer-vendor-reconciliation-judge.md",
    "open-transaction-reconciliation-judge.md",
    "reconciliation-tolerance-matrix.md",
    "license-cost-optimization-pack.md",
    "role-license-mapping.md",
    "license-overallocation-report.md",
    "subscription-cost-forecast.md",
    "alm-release-train-plan.md",
    "environment-readiness-gate.md",
    "release-freeze-calendar.md",
    "deployment-risk-register.md",
    "training-effectiveness-score.md",
    "training-adoption-risk-map.md",
    "role-training-coverage-matrix.md",
    "isv-exit-strategy-pack.md",
    "isv-transition-risk-register.md",
    "vendor-termination-checklist.md",
    "country-regulatory-pack.md",
    "localization-obligation-map.md",
    "tax-einvoicing-readiness-gate.md",
    "legacy-archive-strategy.md",
    "archive-access-model.md",
    "archive-retention-evidence.md",
    "hyperautomation-modernization-map.md",
    "automation-candidate-backlog.md",
    "power-platform-opportunity-pack.md",
    "board-risk-forecast.md",
    "executive-go-live-probability.md",
    "budget-scope-test-risk-trend.md",
    "end-to-end-process-twin.md",
    "process-risk-traceability-map.md",
    "meeting-decision-action-log.md",
    "meeting-to-backlog-bridge.md",
]


CONFIGS = {
    "governance-role-skill-map.json": {
        "contract_scope": {"skill": "ax-migration-contract-scope-guardian", "commands": ["scope-guard", "contract-risk"]},
        "evidence": {"skill": "ax-migration-evidence-vault-manager", "commands": ["evidence-vault"]},
        "cutover_rehearsal": {"skill": "ax-migration-cutover-rehearsal-lead", "commands": ["cutover-rehearsal"]},
        "reconciliation": {"skill": "ax-migration-reconciliation-judge", "commands": ["reconciliation-judge"]},
        "orchestrator": {"skill": "ax-migration-autonomous-governance-orchestrator", "commands": ["governance-pack"]},
    },
    "governance-synonyms.json": {
        "contract_scope": ["contract", "vertrag", "sow", "scope", "umfang", "change request", "cr", "commercial", "freigabe"],
        "evidence": ["evidence", "nachweis", "audit", "sign-off", "go-live proof", "gate evidence"],
        "cutover_rehearsal": ["cutover rehearsal", "dress rehearsal", "probe", "generalprobe", "rollback test"],
        "reconciliation": ["reconciliation", "abgleich", "tolerance", "finance balance", "inventory balance"],
        "meeting": ["meeting", "protokoll", "minutes", "agenda", "decision", "action item"],
    },
    "evidence-vault-rules.json": {
        "freshness_days": 14,
        "critical_evidence": ["CISO", "Finance", "UAT", "Cutover", "Reconciliation", "Payments", "Commerce", "Legal"],
        "blocked_when_missing": ["go_live_approval", "security_gate", "reconciliation_signoff", "cutover_rehearsal_scorecard"],
    },
    "contract-scope-risk-rules.json": {
        "scope_creep_keywords": ["new requirement", "also migrate", "must include", "not in scope", "late request"],
        "requires_change_request": ["new integration", "new report", "new legal entity", "new country", "new channel"],
        "commercial_impact": ["budget", "timeline", "resources", "contract", "license"],
    },
    "reconciliation-rules.json": {
        "domains": ["finance", "inventory", "customer", "vendor", "open transactions", "tax", "loyalty"],
        "default_status": {"pass": "Ready", "variance": "Needs control", "missing": "Blocked"},
    },
    "license-cost-rules.json": {
        "license_domains": ["D365FO", "Commerce", "CRM", "Dataverse", "Team Members", "Operations Activity"],
        "risk_signals": ["overallocated", "unmapped role", "shared account", "inactive user", "premium connector"],
    },
    "alm-release-rules.json": {
        "gates": ["build", "deploy", "smoke", "regression", "code freeze", "release approval"],
        "blocked_when_missing": ["environment readiness", "rollback plan", "release owner", "deployment evidence"],
    },
    "training-effectiveness-rules.json": {
        "signals": ["attendance", "assessment score", "uat defects", "repeat defects", "process questions", "sign-off"],
        "blocked_when": ["key user not trained", "critical role missing", "training below threshold"],
    },
    "country-regulatory-rules.json": {
        "countries": ["DE", "AT", "CH", "FR", "NL", "BE", "ES", "IT", "UK", "US", "CA", "PL", "SE", "NO", "DK"],
        "obligations": ["tax", "e-invoicing", "audit retention", "privacy", "localization", "payments", "reporting"],
    },
    "process-twin-rules.json": {
        "processes": ["lead-to-cash", "order-to-cash", "procure-to-pay", "plan-to-produce", "record-to-report", "hire-to-retire"],
        "nodes": ["process", "role", "data", "integration", "report", "test", "risk", "evidence", "decision"],
    },
}


WRAPPERS = {
    "generate_governance_pack.py": ("pack", "Generate autonomous governance master pack."),
    "generate_evidence_vault.py": ("evidence-vault", "Generate migration evidence vault."),
    "generate_scope_guard.py": ("scope-guard", "Generate scope guard outputs."),
    "generate_contract_risk.py": ("contract-risk", "Generate contract and commercial risk outputs."),
    "generate_cutover_rehearsal.py": ("cutover-rehearsal", "Generate cutover rehearsal outputs."),
    "generate_reconciliation_judge.py": ("reconciliation-judge", "Generate reconciliation judge outputs."),
    "generate_license_cost.py": ("license-cost", "Generate license and cost optimization outputs."),
    "generate_alm_release.py": ("alm-release", "Generate ALM and release train outputs."),
    "generate_training_readiness.py": ("training-readiness", "Generate training readiness outputs."),
    "generate_isv_exit.py": ("isv-exit", "Generate ISV exit strategy outputs."),
    "generate_country_regulatory_pack.py": ("country-regulatory-pack", "Generate country regulatory pack."),
    "generate_archive_strategy.py": ("archive-strategy", "Generate legacy archive strategy."),
    "generate_hyperautomation_pack.py": ("hyperautomation-pack", "Generate hyperautomation pack."),
    "generate_board_risk.py": ("board-risk", "Generate board risk forecast."),
    "generate_process_twin.py": ("process-twin", "Generate end-to-end process twin."),
    "generate_meeting_copilot.py": ("meeting-copilot", "Generate meeting copilot outputs."),
}


def write_skill(name: str, focus: str) -> None:
    directory = ROOT / "skills" / name
    directory.mkdir(parents=True, exist_ok=True)
    text = f"""---
name: {name}
description: Use when migration work needs {focus}.
---

# {name}

## Purpose

Use this skill to turn AX to D365FO migration evidence into autonomous governance outputs for {focus}.

## Inputs

- Analyzer output folders.
- Meeting notes, status reports, decisions, risks, issues, assumptions, and evidence files.
- Contract, scope, test, cutover, reconciliation, license, ALM, training, regulatory, archive, and process inputs where available.

## Outputs

- Role-specific recommendations.
- Missing evidence and blocker lists.
- Gate status with owner and next action.
- Backlog-ready actions with acceptance criteria and evidence expectations.

## Operating Rules

- Treat legal, security, finance, audit, PCI, payment, customer, and production go-live approvals as external human approvals.
- Mark items as blocked when critical evidence is missing.
- Prefer scope reduction, standard D365FO capability, clean governance, and auditable decisions over uncontrolled migration growth.
"""
    (directory / "SKILL.md").write_text(text, encoding="utf-8")


def write_template(name: str) -> None:
    title = name[:-3].replace("-", " ").title()
    text = f"""# {title}

## Purpose

AI-KI generated governance artifact for autonomous AX to D365FO migration control.

## Inputs

| Input | Evidence Needed | Owner |
| --- | --- | --- |
| Current state | Analyzer outputs, meeting notes, decisions, risks, and evidence | Master Orchestrator |
| Target state | D365FO, Commerce, CRM, data, integration, security, and process design evidence | Workstream owner |
| Approval state | Sign-off, gate, audit, legal, security, finance, and business approval evidence | Accountable approver |

## AI-KI Assessment

| Area | Status | Risk | Missing Evidence | Next Action |
| --- | --- | --- | --- | --- |
| Scope | Needs control | Unapproved scope growth can increase cost and timeline | Scope baseline and change log | Validate with PMO and sponsor |
| Evidence | Needs control | Gate decisions may be unsupported | Fresh evidence and owner | Update evidence vault |
| Go-live | Needs control | Cutover or reconciliation proof may be incomplete | Rehearsal and sign-off | Route to responsible skill |

## Automation Outputs

- Decision-ready summary.
- Blocker list.
- Owner and due date proposal.
- Backlog-ready actions.
- Gate recommendation.
- Evidence checklist.

## Go/No-Go Logic

- `Ready`: required evidence is current, owners are assigned, and no critical blocker exists.
- `Needs control`: evidence is incomplete but not go-live critical.
- `Blocked`: required external approval, reconciliation, cutover, security, legal, finance, or production evidence is missing.
"""
    (ROOT / "templates" / name).write_text(text, encoding="utf-8")


def write_wrapper(filename: str, mode: str, description: str) -> None:
    text = f"""#!/usr/bin/env python3
from governance_pack_common import run_cli

if __name__ == "__main__":
    raise SystemExit(run_cli("{mode}", "{description}"))
"""
    (ROOT / "scripts" / filename).write_text(text, encoding="utf-8")


def main() -> int:
    for name, focus in SKILLS.items():
        write_skill(name, focus)
    for name in TEMPLATES:
        write_template(name)
    for name, payload in CONFIGS.items():
        (ROOT / "config" / name).write_text(json.dumps(payload, indent=2), encoding="utf-8")
    for filename, (mode, description) in WRAPPERS.items():
        write_wrapper(filename, mode, description)
    print(f"Generated {len(SKILLS)} skills, {len(TEMPLATES)} templates, {len(CONFIGS)} configs, {len(WRAPPERS)} scripts.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
