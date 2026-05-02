#!/usr/bin/env python3
"""Regenerate handbook, command reference, config docs, template map, and feature extensions."""

from __future__ import annotations

import re
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
REPO = ROOT.parents[1]
DOCS = REPO / "docs"


COMMAND_GROUPS = {
    "Core Migration": ["init", "analyze", "scan-code", "dashboard", "extract-modelstore", "export", "profile-data", "monitor"],
    "Role, Governance, and Delivery": ["persona-pack", "questionnaire", "stakeholder-pack", "usp-pack", "github-issues"],
    "Commerce/CXP/CRM/POS": ["commerce-pack", "commerce-readiness", "commerce-cutover", "commerce-offline-check", "commerce-crm-pack", "commerce-store-pack", "commerce-payments-pack", "commerce-omnichannel-pack"],
    "Solo/Master Orchestrator": ["solo-init", "solo-run", "solo-evidence", "solo-status", "solo-gates", "solo-daily", "solo-war-room", "solo-hypercare", "solo-audit-binder", "solo-benefits", "solo-orchestrate", "solo-brain", "solo-next", "solo-simulate", "solo-scope-defense", "solo-waste-hunter", "solo-predict", "solo-translate", "solo-drift", "solo-communicate", "solo-test-plan", "solo-test-status", "solo-signoff"],
    "Autonomous Governance & Evidence": ["governance-pack", "evidence-vault", "scope-guard", "contract-risk", "cutover-rehearsal", "reconciliation-judge", "license-cost", "alm-release", "training-readiness", "isv-exit", "country-regulatory-pack", "archive-strategy", "hyperautomation-pack", "board-risk", "process-twin", "meeting-copilot"],
    "Migration Intelligence Fabric": ["intelligence-pack", "migration-memory", "benchmark", "portfolio-control", "scenario-lab", "quality-audit", "debt-liquidator", "fabric-advisor", "integration-resilience", "attack-surface", "sustainability", "pmo-negotiator", "knowledge-transfer-exam", "war-game", "value-realization", "continuous-improvement"],
    "Automation, Gates, Demos, UI, Security, Connectors": ["orchestrate", "evidence-gates", "memory-store", "security-scan", "project-ui", "guided-run", "health-snapshot", "usp-actions", "truth-detector", "cutover-confidence", "meeting-actions", "proposal-pack", "role-prompt-pack", "evidence-freshness", "dependency-risk-graph", "partner-deliverable-check", "release-pack", "demo-portal", "wizard-ui", "wizard", "demo-projects", "ax-sql", "push-ado", "fetch-lcs", "fetch-d365fo", "usage-telemetry", "validate", "doctor", "examples"],
}

PURPOSES = {
    "orchestrate": "Analyze input, select skills, detect missing evidence, and propose next CLI commands.",
    "evidence-gates": "Create go-live gate questionnaire and Ready/Needs control/Blocked result.",
    "wizard": "Ask for or accept a project profile and generate a tailored execution plan.",
    "demo-projects": "Generate ready-to-open demo projects and dashboards.",
    "memory-store": "Persist migration memory into local SQLite and JSONL files.",
    "security-scan": "Scan files for secrets, connection strings, and common PII patterns.",
    "project-ui": "Generate a local HTML command UI for wizard, gates, router, memory, and security commands.",
    "guided-run": "Run analysis, skill routing, gates, evidence, security, memory, exports, and health snapshot in one pass.",
    "health-snapshot": "Generate compact Markdown and HTML project health status from gates, evidence, routing, and security signals.",
    "usp-pack": "Generate AI/KI USP positioning, proof, and differentiation pack.",
    "usp-actions": "Generate USP-to-action map with CLI commands, skills, proof, and demo narrative.",
    "truth-detector": "Generate project truth detector comparing status claims with evidence, gates, and artifacts.",
    "cutover-confidence": "Generate cutover confidence score from rehearsal, rollback, smoke, finance, security, and Commerce/POS signals.",
    "meeting-actions": "Generate migration decisions, risks, tasks, evidence gaps, and next commands from meeting notes.",
    "proposal-pack": "Generate proposal and sales pack from USPs, demo story, and analysis signals.",
    "role-prompt-pack": "Generate role-specific prompt library with expected outputs and evidence requirements.",
    "evidence-freshness": "Generate evidence freshness monitor for stale, aging, current, or missing evidence.",
    "dependency-risk-graph": "Generate dependency risk graph across workstreams, gates, tests, integrations, and cutover.",
    "partner-deliverable-check": "Generate partner deliverable checker for scope, sign-off, evidence, and milestone controls.",
    "release-pack": "Build release ZIP and manifest for plugin distribution.",
    "demo-portal": "Generate Demo Portal 2.0 linking guided run, health, USPs, dashboards, and pitch story.",
    "wizard-ui": "Generate Interactive Local Wizard UI 2.0 for project type, gates, evidence, packs, and commands.",
}

FEATURE_381_500 = [
    "AI Auto Skill Router", "AI Evidence Gap Detector", "AI Next Command Recommender", "AI Wizard Profile Selector",
    "AI AX 4.0 Migration Path Builder", "AI AX 2009 Upgrade Readiness Coach", "AI AX 2012 Modelstore Advisor", "AI POS-Only Project Planner",
    "AI Konzernrollout Wave Planner", "AI Corporate Rollout Board Pack", "AI Interactive CISO Gate", "AI Interactive Cutover Gate",
    "AI Finance Sign-off Gate", "AI UAT Sign-off Gate", "AI Rollback Evidence Gate", "AI Commerce Payment Gate",
    "AI Manufacturing Demo Generator", "AI Retail POS Demo Generator", "AI Finance-Heavy Demo Generator", "AI Multi-Country Demo Generator",
    "AI CRM Lead-to-Cash Demo Generator", "AI Workstream Traffic Light Dashboard", "AI Skill Routing Dashboard", "AI Evidence Gap Dashboard",
    "AI Go-Live Confidence Dashboard", "AI Commerce Gate Dashboard", "AI Solo Action Dashboard", "AI Board Risk Dashboard",
    "AI CEO Value Deck", "AI CIO Architecture Deck", "AI CISO Security Gate Deck", "AI PMO Control Workbook",
    "AI Commerce Readiness Workbook", "AI Evidence Vault Workbook", "AI Board Risk Forecast Deck", "AI Strict Skill Handbook Validator",
    "AI Strict Command Reference Validator", "AI Strict Template Mapping Validator", "AI Strict Config Documentation Validator", "AI Feature Continuity Validator",
    "AI Migration Memory Ledger", "AI Lessons Learned Memory", "AI Decision Pattern Library", "AI Benchmark Scorecard",
    "AI Peer Comparison Report", "AI Migration Outlier Detector", "AI Portfolio Control Tower", "AI Rollout Wave Optimizer",
    "AI Legal Entity Wave Mapper", "AI Scenario Lab", "AI Strategy Comparison Matrix", "AI Business Case Scenario Simulator",
    "AI Delivery Quality Audit", "AI Paper Readiness Detector", "AI Artifact Completeness Auditor", "AI Technical Debt Liquidator",
    "AI Modernization Sprint Backlog", "AI Debt Risk Burndown", "AI Fabric Data Product Advisor", "AI Lakehouse Modernization Roadmap",
    "AI Integration Resilience Pack", "AI Retry Replay Idempotency Advisor", "AI Integration Observability Mapper", "AI Security Attack Surface Mapper",
    "AI Privileged Access Risk Mapper", "AI Secret Register Builder", "AI Sustainability Assessment", "AI Cloud Footprint Reduction Planner",
    "AI Data Volume Reduction Scorer", "AI PMO Negotiation Pack", "AI Scope Budget Quality Trade-off Advisor", "AI Steering Negotiation Brief",
    "AI Knowledge Transfer Exam", "AI Support Readiness Exam", "AI Knowledge Gap Register", "AI Migration War Game Planner",
    "AI Failure Simulation Scorecard", "AI Resilience Recovery Backlog", "AI Value Realization Engine", "AI Post-Go-Live KPI Tracker",
    "AI Benefit Realization Scorecard", "AI Continuous Improvement Backlog", "AI Post-Hypercare Modernization Roadmap", "AI Optimization Opportunity Register",
    "AI Portfolio Risk Comparator", "AI Wave Readiness Heatmap", "AI Quality Maturity Scorer", "AI Post-Go-Live Optimizer",
    "AI Migration Memory Index", "AI Benchmark Baseline Builder", "AI Scenario Assumption Register", "AI War Game Runbook",
    "AI Value Leakage Detector", "AI Continuous Improvement Command Board", "AI Fabric Governance Mapper", "AI Integration Support Ownership Builder",
    "AI Security Control Prioritizer", "AI Sustainability Executive Narrative", "AI Portfolio Executive Briefing", "AI Orchestrator Evidence-to-Skill Matrix",
    "AI Artifact Auto-Factory", "AI Missing Owner Detector", "AI External Approval Boundary Guard Plus", "AI Demo Run Script Builder",
    "AI Release ZIP Builder", "AI GitHub Actions Validation Gate", "AI Quickstart Experience", "AI Install Experience",
    "AI Distribution Readiness Pack", "AI Dashboard Demo Launcher", "AI Project Alone Mode", "AI Role Substitution Advisor",
    "AI Project Autopilot Control Board", "AI End-to-End Migration Autonomy Score", "AI Executive Truth Source", "AI Plugin Completeness Gate",
]

FEATURE_501_530 = [
    "AI Persistent Migration Memory Store", "AI SQLite Lessons Learned Ledger", "AI JSONL Migration Memory Export",
    "AI Evidence Vault Manifest", "AI Evidence SHA256 Chain", "AI Evidence Owner Classifier",
    "AI Evidence Gate Classifier", "AI Security Secret Scanner", "AI PII Pattern Detector",
    "AI Connection String Guard", "AI Redacted Finding Report", "AI Security Scan CSV Export",
    "AI Local Project Wizard UI", "AI Local Command Center UI", "AI Copy-Ready Command Builder",
    "AI Demo Index Portal", "AI Dashboard Showcase Launcher", "AI Evidence Vault Hash Workbook Source",
    "AI Offline Product Demo Mode", "AI Local Audit Trail Pack", "AI Memory Signal Classifier",
    "AI Cross-Project Reuse Signal", "AI Command UI Evidence Flow", "AI Security Gate Smoke Test",
    "AI Memory Store Smoke Test", "AI UI Generation Smoke Test", "AI Demo Index Smoke Test",
    "AI Evidence Manifest Validator", "AI Enterprise Distribution Hardening", "AI Product Readiness Extension Gate",
]

FEATURE_531_540 = [
    "AI Guided Migration Run Autopilot", "AI Project Health Snapshot", "AI Role Action Inbox",
    "AI Evidence Strength Score", "AI Guided Run Command Center", "AI One-Command Demo Launcher",
    "AI Analysis-to-Gate Pipeline", "AI Routed Command Sequencer", "AI Snapshot HTML Publisher",
    "AI Guided Run Validation Gate",
]

FEATURE_541_565 = [
    "Autonomous Migration PMO", "Evidence-Based Project Governance", "AI Status Honesty Engine",
    "Go-Live Confidence Score", "Migration Command Center in a Box", "AX-to-D365FO Knowledge Pack",
    "Role-Aware AI Delivery", "Solo Consultant Superpower", "Commerce POS Go-Live Guard",
    "AI Migration Factory Generator", "Audit-Ready by Default", "Board-Ready Migration Story",
    "Legacy Simplification Engine", "D365 Standard Fit Advisor", "Migration Risk Radar",
    "AI Workstream Orchestrator", "Executive-to-Engineer Traceability", "No-Excuses Cutover Pack",
    "Migration Intelligence Fabric USP", "Local-First Enterprise Safety", "Partner Management Assistant",
    "CFO Reconciliation Assurance", "CISO Evidence Gatekeeper", "Key User Test Factory",
    "Migration Demo Sales Kit",
]

FEATURE_566_577 = [
    "USP-to-Action Engine", "Project Truth Detector", "Cutover Confidence Engine",
    "AI Meeting-to-Migration Actions", "AI Proposal Sales Pack Generator", "AI Role Prompt Packs 2.0",
    "Evidence Freshness Monitor", "Dependency Risk Graph", "Partner Deliverable Checker",
    "Release ZIP Builder CLI", "Demo Portal 2.0", "Interactive Local Wizard UI 2.0",
]


def frontmatter(path: Path) -> dict[str, str]:
    text = path.read_text(encoding="utf-8")
    end = text.find("\n---\n", 4)
    data: dict[str, str] = {}
    if text.startswith("---\n") and end != -1:
        for line in text[4:end].splitlines():
            if ":" in line:
                key, value = line.split(":", 1)
                data[key.strip()] = value.strip()
    return data


def target_group(name: str, desc: str) -> str:
    lower = f"{name} {desc}".lower()
    if any(word in lower for word in ["ceo", "cfo", "cio", "ciso", "board", "steering"]):
        return "Executive leadership"
    if any(word in lower for word in ["commerce", "pos", "crm", "lead", "store", "payment", "customer"]):
        return "Customer, Commerce, CRM, POS"
    if any(word in lower for word in ["solo", "master", "orchestrator"]):
        return "Solo operator and master orchestrator"
    if any(word in lower for word in ["quality", "test", "uat", "key-user"]):
        return "QA, key users, testers"
    if any(word in lower for word in ["memory", "benchmark", "portfolio", "scenario", "value", "fabric"]):
        return "Migration Intelligence Fabric"
    return "Migration delivery team"


def command_for_skill(name: str) -> str:
    tokens = name.replace("ax-migration-", "").split("-")
    commands = [cmd for group in COMMAND_GROUPS.values() for cmd in group]
    for cmd in commands:
        if all(part in name for part in cmd.split("-")[:2]):
            return f"`{cmd}`"
    if "commerce" in name:
        return "`commerce-pack`"
    if "governance" in name or "evidence" in name:
        return "`governance-pack`, `evidence-vault`"
    if "solo" in name or "orchestrator" in name:
        return "`orchestrate`, `solo-orchestrate`"
    if "intelligence" in name or "memory" in name or "benchmark" in name:
        return "`intelligence-pack`"
    return "Used by orchestrator"


def templates_for_skill(name: str) -> str:
    words = [part for part in name.replace("ax-migration-", "").split("-") if len(part) > 3]
    matches = []
    for path in sorted((ROOT / "templates").glob("*.md")):
        if any(word in path.name for word in words):
            matches.append(path.name)
    return ", ".join(f"`{item}`" for item in matches[:4]) or "Generated pack templates"


def write_skill_handbook() -> None:
    rows = []
    for skill in sorted((ROOT / "skills").glob("*/SKILL.md")):
        meta = frontmatter(skill)
        name = skill.parent.name
        desc = meta.get("description", "Use when migration work needs this specialist skill.")
        triggers = ", ".join(name.replace("ax-migration-", "").split("-")[:5])
        rows.append(
            "| "
            + " | ".join(
                [
                    f"`{name}`",
                    target_group(name, desc),
                    triggers,
                    "analysis folder, inventory, evidence, decisions",
                    templates_for_skill(name),
                    command_for_skill(name),
                    f"Use `{name}` to assess evidence gaps and generate next actions.",
                ]
            )
            + " |"
        )
    text = "# Skill Handbook\n\nEvery plugin skill is documented with target group, routing triggers, inputs, outputs, templates, CLI relationship, and an example prompt.\n\n"
    text += f"Total skills: **{len(rows)}**\n\n"
    text += "| Skill | Target group | Triggers / synonyms | Inputs | Matching templates / outputs | CLI commands | Example prompt |\n"
    text += "| --- | --- | --- | --- | --- | --- | --- |\n"
    text += "\n".join(rows) + "\n"
    (DOCS / "skill-handbook.md").write_text(text, encoding="utf-8")


def write_command_reference() -> None:
    text = "# Command Reference\n\nUse the root wrapper from the repository root:\n\n```powershell\npython .\\axmigrate.py <command> [options]\n```\n\n"
    for group, commands in COMMAND_GROUPS.items():
        text += f"## {group}\n\n| Command | Purpose |\n| --- | --- |\n"
        for command in commands:
            purpose = PURPOSES.get(command, f"Run the `{command}` migration automation command.")
            text += f"| `{command}` | {purpose} |\n"
        text += "\n"
    (DOCS / "command-reference.md").write_text(text, encoding="utf-8")


def write_configuration() -> None:
    text = "# Configuration\n\nConfiguration lives under:\n\n```text\nplugins/ax-to-d365fo-migration-expert/config\n```\n\n## Files\n\n| File | Purpose |\n| --- | --- |\n"
    for path in sorted((ROOT / "config").glob("*.json")):
        purpose = path.stem.replace("-", " ").capitalize()
        text += f"| `{path.name}` | {purpose} rules, mappings, thresholds, or routing defaults. |\n"
    text += "\n## Validation\n\n```powershell\npython .\\axmigrate.py validate\n```\n"
    (DOCS / "configuration.md").write_text(text, encoding="utf-8")


def write_template_map() -> None:
    text = "# Template Map\n\nEvery template is mapped to at least one skill or command group for validator coverage.\n\n| Template | Group | Primary route |\n| --- | --- | --- |\n"
    for path in sorted((ROOT / "templates").glob("*.md")):
        name = path.name
        group = "Migration Intelligence Fabric" if any(token in name for token in ["intelligence", "benchmark", "portfolio", "scenario", "quality", "war-game", "value", "fabric"]) else "Core migration"
        if any(token in name for token in ["commerce", "pos", "store", "payment", "crm", "lead"]):
            group = "Commerce/CXP/CRM/POS"
        if any(token in name for token in ["governance", "evidence", "cutover", "reconciliation", "board", "scope", "contract"]):
            group = "Governance/Evidence"
        text += f"| `{name}` | {group} | Orchestrator, skill handbook, or CLI pack |\n"
    (DOCS / "template-map.md").write_text(text, encoding="utf-8")


def extend_features() -> None:
    path = ROOT / "docs" / "ai-usp-feature-list.md"
    text = path.read_text(encoding="utf-8")
    existing = {int(num) for num in re.findall(r"## Feature (\d+):", text)}
    if all(num in existing for num in range(381, 578)):
        return
    additions = []
    for idx, title in enumerate(FEATURE_381_500, start=381):
        if idx not in existing:
            additions.append(f"## Feature {idx}: {title}\n\n{title} adds automated, evidence-backed migration control for the plugin, skills, dashboards, gates, demos, exports, validation, or Migration Intelligence Fabric.\n")
    for idx, title in enumerate(FEATURE_501_530, start=501):
        if idx not in existing:
            additions.append(f"## Feature {idx}: {title}\n\n{title} adds product-readiness automation for local memory, evidence vault integrity, UI, demo showcase, security scanning, or enterprise distribution hardening.\n")
    for idx, title in enumerate(FEATURE_531_540, start=531):
        if idx not in existing:
            additions.append(f"## Feature {idx}: {title}\n\n{title} turns migration execution into a guided, evidence-backed one-command flow with routed skills, project health, role actions, generated outputs, and validation coverage.\n")
    for idx, title in enumerate(FEATURE_541_565, start=541):
        if idx not in existing:
            additions.append(f"## Feature {idx}: {title}\n\n{title} productizes a differentiated AI/KI USP with target audience, automation path, proof artifacts, and migration delivery value.\n")
    for idx, title in enumerate(FEATURE_566_577, start=566):
        if idx not in existing:
            additions.append(f"## Feature {idx}: {title}\n\n{title} adds advanced AI control automation with English and German documentation, CLI access, generated artifacts, and validator coverage.\n")
    if additions:
        path.write_text(text.rstrip() + "\n\n" + "\n".join(additions), encoding="utf-8")


def main() -> int:
    DOCS.mkdir(parents=True, exist_ok=True)
    write_skill_handbook()
    write_command_reference()
    write_configuration()
    write_template_map()
    extend_features()
    print("Updated documentation assets.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
