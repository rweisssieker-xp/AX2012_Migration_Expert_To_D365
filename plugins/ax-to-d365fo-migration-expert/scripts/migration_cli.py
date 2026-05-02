#!/usr/bin/env python3
"""Unified CLI for the AX to D365FO migration plugin."""

from __future__ import annotations

import argparse
import importlib.util
import json
import os
import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
REPO_ROOT = ROOT.parents[1]
SCRIPTS = ROOT / "scripts"


def run(script: str, args: list[str]) -> int:
    return subprocess.call([sys.executable, str(SCRIPTS / script), *args])


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    sub = parser.add_subparsers(dest="command", required=True)

    init = sub.add_parser("init", help="Create a migration workspace from templates.")
    init.add_argument("project")
    init.add_argument("--output", default="migration-workspaces")

    analyze = sub.add_parser("analyze", help="Analyze CSV/JSON/X++/XPO inventory inputs.")
    analyze.add_argument("inputs", nargs="+")
    analyze.add_argument("--output", default="migration-analysis")

    scan = sub.add_parser("scan-code", help="Alias for analyze focused on X++/XPO/AOT text.")
    scan.add_argument("inputs", nargs="+")
    scan.add_argument("--output", default="migration-code-analysis")

    dashboard = sub.add_parser("dashboard", help="Generate analysis including dashboard.html.")
    dashboard.add_argument("inputs", nargs="+")
    dashboard.add_argument("--output", default="migration-dashboard")

    extract = sub.add_parser("extract-modelstore", help="Normalize AX modelstore CSV exports.")
    extract.add_argument("input")
    extract.add_argument("--output", required=True)

    export = sub.add_parser("export", help="Export analysis folder to XLSX and PPTX.")
    export.add_argument("analysis_dir")
    export.add_argument("--output", default="migration-exports")

    persona = sub.add_parser("persona-pack", help="Generate CEO/CIO/CISO/PM/team persona packs and readiness scores.")
    persona.add_argument("analysis_dir")
    persona.add_argument("--persona", choices=["ceo", "cio", "ciso", "pm", "team", "all"], default="all")
    persona.add_argument("--output", default="persona-packs")
    persona.add_argument("--office", action="store_true")

    questionnaire = sub.add_parser("questionnaire", help="Generate role questionnaires, migration factory, cutover, hypercare, and partner packs.")
    questionnaire.add_argument("--persona", choices=["ceo", "cio", "ciso", "pm", "team", "change", "all"], default="all")
    questionnaire.add_argument("--output", default="migration-questionnaires")

    github_issues = sub.add_parser("github-issues", help="Export analyzer work items as GitHub issue Markdown files.")
    github_issues.add_argument("analysis_dir")
    github_issues.add_argument("--output", default="github-issues")

    stakeholder = sub.add_parser("stakeholder-pack", help="Generate extended CFO/COO/data/integration/QA/legal/support/vendor/partner stakeholder packs.")
    stakeholder.add_argument("analysis_dir")
    stakeholder.add_argument("--stakeholder", choices=["cfo", "coo", "data", "integration", "qa", "enterprise-architect", "vendor", "legal", "support", "partner-sales", "all"], default="all")
    stakeholder.add_argument("--output", default="stakeholder-packs")

    usp_pack = sub.add_parser("usp-pack", help="Generate AI/KI USP positioning, proof, and differentiation pack.")
    usp_pack.add_argument("source", nargs="?", default=".")
    usp_pack.add_argument("--project", default="Migration Project")
    usp_pack.add_argument("--output", default="usp-packs")

    commerce_commands = {
        "commerce-pack": ("generate_commerce_pack.py", "Generate full Commerce/CXP/CRM/POS pack.", "commerce-packs"),
        "commerce-readiness": ("generate_commerce_readiness.py", "Generate Commerce readiness scores.", "commerce-readiness"),
        "commerce-cutover": ("generate_commerce_cutover.py", "Generate Commerce cutover runbook and go-live gate.", "commerce-cutover"),
        "commerce-offline-check": ("generate_commerce_offline_check.py", "Generate POS offline continuity and recovery pack.", "commerce-offline"),
        "commerce-crm-pack": ("generate_commerce_crm_pack.py", "Generate CRM, Dataverse, Lead-to-Cash, and Customer Master pack.", "commerce-crm"),
        "commerce-store-pack": ("generate_commerce_store_pack.py", "Generate Store Operations, POS hardware, and training pack.", "commerce-store"),
        "commerce-payments-pack": ("generate_commerce_payments_pack.py", "Generate payments, PCI, settlement, and reconciliation pack.", "commerce-payments"),
        "commerce-omnichannel-pack": ("generate_commerce_omnichannel_pack.py", "Generate omnichannel, e-commerce, analytics, and marketplace pack.", "commerce-omnichannel"),
    }
    for command, (_, help_text, default_output) in commerce_commands.items():
        commerce = sub.add_parser(command, help=help_text)
        commerce.add_argument("analysis_dir")
        commerce.add_argument("--output", default=default_output)

    governance_commands = {
        "governance-pack": ("generate_governance_pack.py", "Generate autonomous governance master pack.", "governance-packs"),
        "evidence-vault": ("generate_evidence_vault.py", "Generate migration evidence vault.", "evidence-vault"),
        "scope-guard": ("generate_scope_guard.py", "Generate scope guard outputs.", "scope-guard"),
        "contract-risk": ("generate_contract_risk.py", "Generate contract and commercial risk outputs.", "contract-risk"),
        "cutover-rehearsal": ("generate_cutover_rehearsal.py", "Generate cutover rehearsal outputs.", "cutover-rehearsal"),
        "reconciliation-judge": ("generate_reconciliation_judge.py", "Generate reconciliation judge outputs.", "reconciliation-judge"),
        "license-cost": ("generate_license_cost.py", "Generate license and cost optimization outputs.", "license-cost"),
        "alm-release": ("generate_alm_release.py", "Generate ALM and release train outputs.", "alm-release"),
        "training-readiness": ("generate_training_readiness.py", "Generate training readiness outputs.", "training-readiness"),
        "isv-exit": ("generate_isv_exit.py", "Generate ISV exit strategy outputs.", "isv-exit"),
        "country-regulatory-pack": ("generate_country_regulatory_pack.py", "Generate country regulatory pack.", "country-regulatory"),
        "archive-strategy": ("generate_archive_strategy.py", "Generate legacy archive strategy.", "archive-strategy"),
        "hyperautomation-pack": ("generate_hyperautomation_pack.py", "Generate hyperautomation pack.", "hyperautomation-pack"),
        "board-risk": ("generate_board_risk.py", "Generate board risk forecast.", "board-risk"),
        "process-twin": ("generate_process_twin.py", "Generate end-to-end process twin.", "process-twin"),
        "meeting-copilot": ("generate_meeting_copilot.py", "Generate meeting copilot outputs.", "meeting-copilot"),
    }
    for command, (_, help_text, default_output) in governance_commands.items():
        governance = sub.add_parser(command, help=help_text)
        governance.add_argument("source")
        governance.add_argument("--output", default=default_output)

    intelligence_commands = {
        "intelligence-pack": ("generate_intelligence_pack.py", "Generate Migration Intelligence Fabric master pack.", "intelligence-pack"),
        "migration-memory": ("generate_migration_memory.py", "Generate reusable migration memory and decision patterns.", "migration-memory"),
        "benchmark": ("generate_benchmark.py", "Generate benchmark scorecard and outlier report.", "benchmark"),
        "portfolio-control": ("generate_portfolio_control.py", "Generate portfolio control tower and wave optimization.", "portfolio-control"),
        "scenario-lab": ("generate_scenario_lab.py", "Generate scenario simulation and strategy comparison.", "scenario-lab"),
        "quality-audit": ("generate_quality_audit.py", "Generate delivery quality audit and paper readiness detection.", "quality-audit"),
        "debt-liquidator": ("generate_debt_liquidator.py", "Generate technical debt liquidation plan.", "debt-liquidator"),
        "fabric-advisor": ("generate_fabric_advisor.py", "Generate Fabric, Lakehouse, Power BI and data product advisory outputs.", "fabric-advisor"),
        "integration-resilience": ("generate_integration_resilience.py", "Generate integration resilience and observability pack.", "integration-resilience"),
        "attack-surface": ("generate_attack_surface.py", "Generate security attack surface and privileged access map.", "attack-surface"),
        "sustainability": ("generate_sustainability.py", "Generate cloud footprint and sustainability assessment.", "sustainability"),
        "pmo-negotiator": ("generate_pmo_negotiator.py", "Generate scope, budget, quality trade-off negotiation pack.", "pmo-negotiator"),
        "knowledge-transfer-exam": ("generate_knowledge_transfer_exam.py", "Generate knowledge transfer and support readiness exam.", "knowledge-transfer-exam"),
        "war-game": ("generate_war_game.py", "Generate migration failure simulation and war-game plan.", "war-game"),
        "value-realization": ("generate_value_realization.py", "Generate post-go-live value realization tracker.", "value-realization"),
        "continuous-improvement": ("generate_continuous_improvement.py", "Generate continuous improvement backlog and modernization roadmap.", "continuous-improvement"),
    }
    for command, (_, help_text, default_output) in intelligence_commands.items():
        intelligence = sub.add_parser(command, help=help_text)
        intelligence.add_argument("source")
        intelligence.add_argument("--output", default=default_output)

    orchestrate = sub.add_parser("orchestrate", help="Automatically route input to skills, evidence gaps, artifacts, and next CLI commands.")
    orchestrate.add_argument("source")
    orchestrate.add_argument("--output", default="orchestration")

    gates = sub.add_parser("evidence-gates", help="Generate interactive go-live evidence gates and status.")
    gates.add_argument("source", nargs="?", default=".")
    gates.add_argument("--output", default="evidence-gates")
    for gate_name in ["ciso-approval", "cutover-rehearsal", "finance-reconciliation", "uat-signoff", "commerce-payments", "rollback-plan"]:
        gates.add_argument(f"--{gate_name}", choices=["yes", "no"], default="no")

    memory_store = sub.add_parser("memory-store", help="Persist migration memory into local SQLite and JSONL files.")
    memory_store.add_argument("source")
    memory_store.add_argument("--project", default="Migration Project")
    memory_store.add_argument("--output", default="migration-memory-store")

    security_scan = sub.add_parser("security-scan", help="Scan files for secrets, connection strings, and common PII patterns.")
    security_scan.add_argument("source")
    security_scan.add_argument("--output", default="security-scan")
    security_scan.add_argument("--fail-on-findings", action="store_true")

    project_ui = sub.add_parser("project-ui", help="Generate local HTML UI for wizard, gates, router, memory, and security commands.")
    project_ui.add_argument("--output", default="migration-ui")

    guided_run = sub.add_parser("guided-run", help="Run analysis, skill routing, gates, evidence, security, memory, exports, and health snapshot in one pass.")
    guided_run.add_argument("source")
    guided_run.add_argument("--project", default="Migration Project")
    guided_run.add_argument("--output", default="guided-run")
    for gate_name in ["ciso-approval", "cutover-rehearsal", "finance-reconciliation", "uat-signoff", "commerce-payments", "rollback-plan"]:
        guided_run.add_argument(f"--{gate_name}", choices=["yes", "no"], default="no")

    health_snapshot = sub.add_parser("health-snapshot", help="Generate a compact Markdown and HTML project health snapshot.")
    health_snapshot.add_argument("source")
    health_snapshot.add_argument("--output", default="health-snapshot")

    control_commands = {
        "usp-actions": ("USP-to-Action Engine", "usp-actions"),
        "truth-detector": ("Project Truth Detector", "truth-detector"),
        "cutover-confidence": ("Cutover Confidence Engine", "cutover-confidence"),
        "meeting-actions": ("AI Meeting-to-Migration Actions", "meeting-actions"),
        "proposal-pack": ("AI Proposal / Sales Pack Generator", "proposal-pack"),
        "role-prompt-pack": ("AI Role Prompt Packs 2.0", "role-prompt-pack"),
        "evidence-freshness": ("Evidence Freshness Monitor", "evidence-freshness"),
        "dependency-risk-graph": ("Dependency Risk Graph", "dependency-risk-graph"),
        "partner-deliverable-check": ("Partner Deliverable Checker", "partner-deliverable-check"),
        "release-pack": ("Release ZIP Builder", "release-pack"),
        "demo-portal": ("Demo Portal 2.0", "demo-portal"),
        "wizard-ui": ("Interactive Local Wizard UI 2.0", "wizard-ui"),
    }
    for command, (help_text, _) in control_commands.items():
        control = sub.add_parser(command, help=f"Generate {help_text}.")
        control.add_argument("source", nargs="?", default=".")
        control.add_argument("--project", default="Migration Project")
        control.add_argument("--output", default=command)

    solo_init = sub.add_parser("solo-init", help="Create a solo migration project operating folder.")
    solo_init.add_argument("project")
    solo_init.add_argument("--output", default="solo-migration")

    solo_run = sub.add_parser("solo-run", help="Run full solo migration orchestration from inventory inputs.")
    solo_run.add_argument("--project", required=True)
    solo_run.add_argument("--input", action="append", required=True, dest="inputs")
    solo_run.add_argument("--output", default="solo-migration")

    solo_commands = {
        "solo-evidence": ("evidence", "Generate solo evidence completeness outputs."),
        "solo-status": ("status", "Generate solo migration health/status outputs."),
        "solo-gates": ("gates", "Generate self-approval and external approval gates."),
        "solo-daily": ("daily", "Generate daily migration command sheet."),
        "solo-war-room": ("war-room", "Generate cutover war-room outputs."),
        "solo-hypercare": ("hypercare", "Generate hypercare command center outputs."),
        "solo-audit-binder": ("audit-binder", "Generate audit and evidence binder outputs."),
        "solo-benefits": ("benefits", "Generate benefits realization outputs."),
        "solo-orchestrate": ("orchestrate", "Generate master-orchestrator plan and routing outputs."),
        "solo-brain": ("brain", "Generate AI migration brain outputs."),
        "solo-next": ("next", "Generate next-best-action outputs."),
        "solo-simulate": ("simulate", "Generate decision impact simulation outputs."),
        "solo-scope-defense": ("scope-defense", "Generate scope defense outputs."),
        "solo-waste-hunter": ("waste-hunter", "Generate waste hunter report."),
        "solo-predict": ("predict", "Generate prediction outputs."),
        "solo-translate": ("translate", "Generate stakeholder translation outputs."),
        "solo-drift": ("drift", "Generate project drift detector outputs."),
        "solo-communicate": ("communicate", "Generate communication copilot outputs."),
        "solo-test-plan": ("test-plan", "Generate key-user/UAT/regression test plan outputs."),
        "solo-test-status": ("test-status", "Generate test execution status outputs."),
        "solo-signoff": ("signoff", "Generate business sign-off outputs."),
    }
    for command, (_, help_text) in solo_commands.items():
        solo = sub.add_parser(command, help=help_text)
        solo.add_argument("source")
        solo.add_argument("--output")
        if command == "solo-translate":
            solo.add_argument("--role", default="")
        if command == "solo-communicate":
            solo.add_argument("--audience", default="")

    profile = sub.add_parser("profile-data", help="Profile CSV data quality.")
    profile.add_argument("input")
    profile.add_argument("--output", default="data-quality-profile.md")

    monitor = sub.add_parser("monitor", help="Compare two inventory-normalized.json snapshots.")
    monitor.add_argument("baseline")
    monitor.add_argument("current")
    monitor.add_argument("--output", default="inventory-change-monitor.md")

    axsql = sub.add_parser("ax-sql", help="Extract AX SQL/modelstore inventory through ODBC.")
    axsql.add_argument("--query")
    axsql.add_argument("--output", required=True)
    axsql.add_argument("--dry-run", action="store_true")

    azdo = sub.add_parser("push-ado", help="Create Azure DevOps work items from analyzer CSV.")
    azdo.add_argument("work_items_csv")
    azdo.add_argument("--dry-run", action="store_true")

    lcs = sub.add_parser("fetch-lcs", help="Fetch LCS metadata/payload from configured endpoint.")
    lcs.add_argument("--path", default="/")
    lcs.add_argument("--output", required=True)
    lcs.add_argument("--dry-run", action="store_true")

    d365 = sub.add_parser("fetch-d365fo", help="Fetch D365FO metadata/OData payload from configured endpoint.")
    d365.add_argument("--path", default="/data/$metadata")
    d365.add_argument("--output", required=True)
    d365.add_argument("--dry-run", action="store_true")

    usage = sub.add_parser("usage-telemetry", help="Summarize AX usage telemetry CSV.")
    usage.add_argument("input")
    usage.add_argument("--object-column", default="Object")
    usage.add_argument("--output", default="usage-telemetry-summary.csv")

    sub.add_parser("validate", help="Run plugin validation checks.")
    sub.add_parser("doctor", help="Check local runtime, optional dependencies, config, and environment.")
    sub.add_parser("examples", help="Print useful example commands.")

    wizard = sub.add_parser("wizard", help="Generate a guided project command plan for a migration profile.")
    wizard.add_argument("--profile", choices=["ax40", "ax2009", "ax2012", "commerce", "crm", "finance", "manufacturing", "multi-country", "corporate-rollout", "pos", "solo"])
    wizard.add_argument("--project", default="Contoso AX Migration")
    wizard.add_argument("--output", default="migration-wizard")

    demos = sub.add_parser("demo-projects", help="Generate ready-to-open demo projects and dashboards.")
    demos.add_argument("--output", default="demo-projects")

    args = parser.parse_args()
    if args.command == "init":
        return run("create_migration_workspace.py", [args.project, "--output", args.output])
    if args.command in ("analyze", "scan-code", "dashboard"):
        return run("analyze_ax_inventory.py", [*args.inputs, "--output", args.output])
    if args.command == "extract-modelstore":
        return run("extract_modelstore_inventory.py", [args.input, "--output", args.output])
    if args.command == "export":
        return run("export_analysis.py", [args.analysis_dir, "--output", args.output])
    if args.command == "persona-pack":
        cmd = [args.analysis_dir, "--persona", args.persona, "--output", args.output]
        if args.office:
            cmd += ["--office"]
        return run("generate_persona_pack.py", cmd)
    if args.command == "questionnaire":
        return run("create_questionnaire_pack.py", ["--persona", args.persona, "--output", args.output])
    if args.command == "github-issues":
        return run("export_github_issues.py", [args.analysis_dir, "--output", args.output])
    if args.command == "stakeholder-pack":
        return run("generate_stakeholder_pack.py", [args.analysis_dir, "--stakeholder", args.stakeholder, "--output", args.output])
    if args.command == "usp-pack":
        return run("generate_usp_pack.py", [args.source, "--project", args.project, "--output", args.output])
    if args.command in commerce_commands:
        script, _, _ = commerce_commands[args.command]
        return run(script, [args.analysis_dir, "--output", args.output])
    if args.command in governance_commands:
        script, _, _ = governance_commands[args.command]
        return run(script, [args.source, "--output", args.output])
    if args.command in intelligence_commands:
        script, _, _ = intelligence_commands[args.command]
        return run(script, [args.source, "--output", args.output])
    if args.command == "orchestrate":
        return run("orchestrate_migration.py", [args.source, "--output", args.output])
    if args.command == "evidence-gates":
        cmd = [args.source, "--output", args.output]
        for gate_name in ["ciso_approval", "cutover_rehearsal", "finance_reconciliation", "uat_signoff", "commerce_payments", "rollback_plan"]:
            cmd += [f"--{gate_name.replace('_', '-')}", getattr(args, gate_name)]
        return run("evaluate_evidence_gates.py", cmd)
    if args.command == "memory-store":
        return run("update_migration_memory_store.py", [args.source, "--project", args.project, "--output", args.output])
    if args.command == "security-scan":
        cmd = [args.source, "--output", args.output]
        if args.fail_on_findings:
            cmd += ["--fail-on-findings"]
        return run("scan_sensitive_data.py", cmd)
    if args.command == "project-ui":
        return run("create_project_ui.py", ["--output", args.output])
    if args.command == "guided-run":
        cmd = [args.source, "--project", args.project, "--output", args.output]
        for gate_name in ["ciso_approval", "cutover_rehearsal", "finance_reconciliation", "uat_signoff", "commerce_payments", "rollback_plan"]:
            cmd += [f"--{gate_name.replace('_', '-')}", getattr(args, gate_name)]
        return run("guided_run.py", cmd)
    if args.command == "health-snapshot":
        return run("health_snapshot.py", [args.source, "--output", args.output])
    if args.command in control_commands:
        _, mode = control_commands[args.command]
        return run("generate_control_feature.py", [args.source, "--mode", mode, "--project", args.project, "--output", args.output])
    if args.command == "solo-init":
        return run("create_solo_project.py", [args.project, "--output", args.output])
    if args.command == "solo-run":
        cmd = ["--project", args.project, "--output", args.output]
        for item in args.inputs:
            cmd += ["--input", item]
        return run("run_solo_migration.py", cmd)
    if args.command in solo_commands:
        mode, _ = solo_commands[args.command]
        cmd = [args.source, "--mode", mode]
        if args.output:
            cmd += ["--output", args.output]
        if getattr(args, "role", ""):
            cmd += ["--role", args.role]
        if getattr(args, "audience", ""):
            cmd += ["--audience", args.audience]
        return run("generate_solo_artifacts.py", cmd)
    if args.command == "profile-data":
        return run("profile_data_quality.py", [args.input, "--output", args.output])
    if args.command == "monitor":
        return run("monitor_inventory_changes.py", [args.baseline, args.current, "--output", args.output])
    if args.command == "ax-sql":
        cmd = ["--output", args.output]
        if args.query:
            cmd += ["--query", args.query]
        if args.dry_run:
            cmd += ["--dry-run"]
        return run("connect_ax_sql.py", cmd)
    if args.command == "push-ado":
        cmd = [args.work_items_csv]
        if args.dry_run:
            cmd += ["--dry-run"]
        return run("push_azure_devops.py", cmd)
    if args.command == "fetch-lcs":
        cmd = ["--path", args.path, "--output", args.output]
        if args.dry_run:
            cmd += ["--dry-run"]
        return run("fetch_lcs_metadata.py", cmd)
    if args.command == "fetch-d365fo":
        cmd = ["--path", args.path, "--output", args.output]
        if args.dry_run:
            cmd += ["--dry-run"]
        return run("fetch_d365fo_metadata.py", cmd)
    if args.command == "usage-telemetry":
        return run("analyze_usage_telemetry.py", [args.input, "--object-column", args.object_column, "--output", args.output])
    if args.command == "validate":
        return run("validate_plugin.py", [])
    if args.command == "doctor":
        return doctor()
    if args.command == "examples":
        print_examples()
        return 0
    if args.command == "wizard":
        cmd = ["--project", args.project, "--output", args.output]
        if args.profile:
            cmd += ["--profile", args.profile]
        return run("create_project_wizard.py", cmd)
    if args.command == "demo-projects":
        return run("create_demo_projects.py", ["--output", args.output])
    return 2


def doctor() -> int:
    checks = [
        ("Python", sys.version.split()[0]),
        ("Plugin root", str(ROOT)),
        ("Version", read_version()),
        ("openpyxl", module_status("openpyxl")),
        ("python-pptx", module_status("pptx")),
        ("pyodbc", module_status("pyodbc")),
        ("plugin.json", "OK" if (ROOT / ".codex-plugin" / "plugin.json").exists() else "Missing"),
        ("config", "OK" if (ROOT / "config").exists() else "Missing"),
    ]
    for name, value in checks:
        print(f"{name}: {value}")
    integration_cfg = json.loads((ROOT / "config" / "integrations.json").read_text(encoding="utf-8"))
    for section in integration_cfg.values():
        for key, env_name in section.items():
            if key.endswith("_env"):
                print(f"{env_name}: {'set' if os.environ.get(env_name) else 'not set'}")
    return 0


def read_version() -> str:
    version_file = REPO_ROOT / "VERSION"
    return version_file.read_text(encoding="utf-8").strip() if version_file.exists() else "unknown"


def module_status(name: str) -> str:
    return "OK" if importlib.util.find_spec(name) else "missing"


def print_examples() -> None:
    print(
        """
Validate:
  python axmigrate.py validate

Analyze sample inventory:
  python axmigrate.py analyze plugins/ax-to-d365fo-migration-expert/examples/sample-ax-inventory.csv --output migration-analysis/sample

Scan X++ / XPO:
  python axmigrate.py scan-code plugins/ax-to-d365fo-migration-expert/examples/sample-xpp-class.xpp --output migration-analysis/code

Create workspace:
  python axmigrate.py init "Contoso AX Migration"

Export Excel/PPTX:
  python axmigrate.py export migration-analysis/sample --output migration-exports/sample

Generate persona packs with readiness scores:
  python axmigrate.py persona-pack migration-analysis/sample --persona all --office --output persona-packs/sample

Generate questionnaires, factory, cutover, hypercare, and partner packs:
  python axmigrate.py questionnaire --persona all --output migration-questionnaires/sample

Export GitHub issue Markdown:
  python axmigrate.py github-issues migration-analysis/sample --output github-issues/sample

Generate extended stakeholder packs:
  python axmigrate.py stakeholder-pack migration-analysis/sample --stakeholder all --output stakeholder-packs/sample

Generate Commerce/CXP/CRM/POS pack:
  python axmigrate.py commerce-pack migration-analysis/sample --output commerce-packs/sample

Generate Commerce readiness:
  python axmigrate.py commerce-readiness migration-analysis/sample --output commerce-readiness/sample

Generate Commerce cutover and offline packs:
  python axmigrate.py commerce-cutover migration-analysis/sample --output commerce-cutover/sample
  python axmigrate.py commerce-offline-check migration-analysis/sample --output commerce-offline/sample

Generate autonomous governance and evidence intelligence:
  python axmigrate.py governance-pack migration-analysis/sample --output governance-packs/sample
  python axmigrate.py evidence-vault migration-analysis/sample --output evidence-vault/sample
  python axmigrate.py scope-guard migration-analysis/sample --output scope-guard/sample
  python axmigrate.py cutover-rehearsal migration-analysis/sample --output cutover-rehearsal/sample
  python axmigrate.py reconciliation-judge migration-analysis/sample --output reconciliation/sample
  python axmigrate.py board-risk migration-analysis/sample --output board-risk/sample

Generate a guided command plan:
  python axmigrate.py wizard --profile commerce --project "Contoso Retail Migration" --output migration-wizard/commerce

Generate demo projects and dashboards:
  python axmigrate.py demo-projects --output demo-projects

Run solo migration operating system:
  python axmigrate.py solo-run --project "Contoso AX Migration" --input plugins/ax-to-d365fo-migration-expert/examples/sample-ax-inventory.csv --output solo-migration

Generate master-orchestrator status:
  python axmigrate.py solo-orchestrate solo-migration/contoso-ax-migration --output master-orchestration/sample

Doctor:
  python axmigrate.py doctor
""".strip()
    )


if __name__ == "__main__":
    raise SystemExit(main())
