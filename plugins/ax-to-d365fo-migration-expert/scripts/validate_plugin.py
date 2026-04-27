#!/usr/bin/env python3
"""Validate the AX to D365FO migration plugin."""

from __future__ import annotations

import json
import re
import subprocess
import sys
import tempfile
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
REPO_ROOT = ROOT.parents[1]
EXPECTED_SKILLS = 112
EXPECTED_TEMPLATES = 325
EXPECTED_ANALYSIS_OUTPUTS = 46

CLI_COMMANDS = [
    "init", "analyze", "scan-code", "dashboard", "extract-modelstore", "export", "persona-pack", "questionnaire",
    "github-issues", "stakeholder-pack", "commerce-pack", "commerce-readiness", "commerce-cutover", "commerce-offline-check",
    "commerce-crm-pack", "commerce-store-pack", "commerce-payments-pack", "commerce-omnichannel-pack", "governance-pack",
    "evidence-vault", "scope-guard", "contract-risk", "cutover-rehearsal", "reconciliation-judge", "license-cost",
    "alm-release", "training-readiness", "isv-exit", "country-regulatory-pack", "archive-strategy", "hyperautomation-pack",
    "board-risk", "process-twin", "meeting-copilot", "intelligence-pack", "migration-memory", "benchmark",
    "portfolio-control", "scenario-lab", "quality-audit", "debt-liquidator", "fabric-advisor", "integration-resilience",
    "attack-surface", "sustainability", "pmo-negotiator", "knowledge-transfer-exam", "war-game", "value-realization",
    "continuous-improvement", "orchestrate", "evidence-gates", "solo-init", "solo-run", "solo-evidence", "solo-status",
    "solo-gates", "solo-daily", "solo-war-room", "solo-hypercare", "solo-audit-binder", "solo-benefits", "solo-orchestrate",
    "solo-brain", "solo-next", "solo-simulate", "solo-scope-defense", "solo-waste-hunter", "solo-predict", "solo-translate",
    "solo-drift", "solo-communicate", "solo-test-plan", "solo-test-status", "solo-signoff", "profile-data", "monitor",
    "ax-sql", "push-ado", "fetch-lcs", "fetch-d365fo", "usage-telemetry", "validate", "doctor", "examples", "wizard",
    "demo-projects",
]


def run(args: list[str]) -> None:
    result = subprocess.run(args, cwd=ROOT.parents[1], text=True, capture_output=True)
    if result.returncode:
        print(result.stdout)
        print(result.stderr)
        raise SystemExit(result.returncode)


def assert_json(path: Path) -> None:
    json.loads(path.read_text(encoding="utf-8"))


def assert_skill(path: Path) -> None:
    text = path.read_text(encoding="utf-8")
    if not text.startswith("---\n"):
        raise SystemExit(f"Skill missing YAML frontmatter: {path}")
    end = text.find("\n---\n", 4)
    if end == -1:
        raise SystemExit(f"Skill frontmatter is not closed: {path}")
    frontmatter = text[4:end]
    fields = {}
    for line in frontmatter.splitlines():
        if ":" in line:
            key, value = line.split(":", 1)
            fields[key.strip()] = value.strip()
    expected_name = path.parent.name
    if fields.get("name") != expected_name:
        raise SystemExit(f"Skill name mismatch in {path}: expected {expected_name}, got {fields.get('name')}")
    if not fields.get("description", "").startswith("Use when"):
        raise SystemExit(f"Skill description should start with 'Use when': {path}")


def assert_documentation_coverage(skill_files: list[Path]) -> None:
    handbook = (REPO_ROOT / "docs" / "skill-handbook.md").read_text(encoding="utf-8")
    command_ref = (REPO_ROOT / "docs" / "command-reference.md").read_text(encoding="utf-8")
    config_doc = (REPO_ROOT / "docs" / "configuration.md").read_text(encoding="utf-8")
    template_map = (REPO_ROOT / "docs" / "template-map.md").read_text(encoding="utf-8")

    missing_skills = [path.parent.name for path in skill_files if path.parent.name not in handbook]
    if missing_skills:
        raise SystemExit("Skills missing from handbook:\n" + "\n".join(missing_skills))

    missing_commands = [command for command in CLI_COMMANDS if f"`{command}`" not in command_ref]
    if missing_commands:
        raise SystemExit("CLI commands missing from command reference:\n" + "\n".join(missing_commands))

    missing_configs = [path.name for path in sorted((ROOT / "config").glob("*.json")) if path.name not in config_doc]
    if missing_configs:
        raise SystemExit("Config files missing from configuration docs:\n" + "\n".join(missing_configs))

    missing_templates = [path.name for path in sorted((ROOT / "templates").glob("*.md")) if path.name not in template_map]
    if missing_templates:
        raise SystemExit("Templates missing from template map:\n" + "\n".join(missing_templates))


def assert_feature_numbers() -> None:
    text = (ROOT / "docs" / "ai-usp-feature-list.md").read_text(encoding="utf-8")
    numbers: set[int] = set()
    for match in re.finditer(r"## Feature (\d+):", text):
        numbers.add(int(match.group(1)))
    for match in re.finditer(r"## Features (\d+)-(\d+):", text):
        start, end = int(match.group(1)), int(match.group(2))
        numbers.update(range(start, end + 1))
    expected = set(range(1, 501))
    missing = sorted(expected - numbers)
    extra_gap = sorted(num for num in numbers if num < 1 or num > 500)
    if missing or extra_gap:
        raise SystemExit(f"Feature numbering is not continuous 1-500. Missing={missing[:20]} Extra={extra_gap[:20]}")


def main() -> int:
    for path in [ROOT / ".codex-plugin" / "plugin.json", *list((ROOT / "config").glob("*.json"))]:
        assert_json(path)
    skill_files = sorted((ROOT / "skills").glob("*/SKILL.md"))
    if len(skill_files) != EXPECTED_SKILLS:
        raise SystemExit(f"Expected {EXPECTED_SKILLS} skills, got {len(skill_files)}")
    for path in skill_files:
        assert_skill(path)
    assert_documentation_coverage(skill_files)
    assert_feature_numbers()

    run([sys.executable, "-m", "unittest", "discover", str(ROOT / "tests")])
    with tempfile.TemporaryDirectory(prefix="axmigrate-validation-") as tmp:
        temp_root = Path(tmp)
        analysis = temp_root / "analysis"
        workspace = temp_root / "workspace"
        commerce_outputs = [
            temp_root / "commerce_pack",
            temp_root / "commerce_readiness",
            temp_root / "commerce_cutover",
            temp_root / "commerce_offline",
            temp_root / "commerce_crm",
            temp_root / "commerce_store",
            temp_root / "commerce_payments",
            temp_root / "commerce_omnichannel",
        ]
        solo_project = temp_root / "solo"
        solo_run = temp_root / "solo_run"
        solo_outputs = [
            temp_root / "solo_orchestrate",
            temp_root / "solo_status",
            temp_root / "solo_gates",
            temp_root / "solo_test_plan",
            temp_root / "solo_signoff",
        ]
        governance_outputs = [
            temp_root / "governance_pack",
            temp_root / "evidence_vault",
            temp_root / "scope_guard",
            temp_root / "contract_risk",
            temp_root / "cutover_rehearsal",
            temp_root / "reconciliation_judge",
            temp_root / "license_cost",
            temp_root / "alm_release",
            temp_root / "training_readiness",
            temp_root / "isv_exit",
            temp_root / "country_regulatory",
            temp_root / "archive_strategy",
            temp_root / "hyperautomation",
            temp_root / "board_risk",
            temp_root / "process_twin",
            temp_root / "meeting_copilot",
        ]
        wizard_output = temp_root / "wizard"
        demo_output = temp_root / "demo_projects"
        export_output = temp_root / "exports"
        orchestration_output = temp_root / "orchestration"
        evidence_gate_output = temp_root / "evidence_gates"
        intelligence_outputs = [
            temp_root / "intelligence_pack",
            temp_root / "migration_memory",
            temp_root / "benchmark",
            temp_root / "portfolio_control",
            temp_root / "scenario_lab",
            temp_root / "quality_audit",
            temp_root / "war_game",
            temp_root / "value_realization",
        ]
        run([sys.executable, str(ROOT / "scripts" / "analyze_ax_inventory.py"), str(ROOT / "examples" / "sample-ax-inventory.csv"), str(ROOT / "examples" / "sample-xpp-class.xpp"), "--output", str(analysis)])
        run([sys.executable, str(ROOT / "scripts" / "create_migration_workspace.py"), "Validation", "--output", str(workspace)])
        run([sys.executable, str(ROOT / "scripts" / "export_analysis.py"), str(analysis), "--output", str(export_output)])
        for script, output in [
            ("generate_commerce_pack.py", commerce_outputs[0]),
            ("generate_commerce_readiness.py", commerce_outputs[1]),
            ("generate_commerce_cutover.py", commerce_outputs[2]),
            ("generate_commerce_offline_check.py", commerce_outputs[3]),
            ("generate_commerce_crm_pack.py", commerce_outputs[4]),
            ("generate_commerce_store_pack.py", commerce_outputs[5]),
            ("generate_commerce_payments_pack.py", commerce_outputs[6]),
            ("generate_commerce_omnichannel_pack.py", commerce_outputs[7]),
        ]:
            run([sys.executable, str(ROOT / "scripts" / script), str(analysis), "--output", str(output)])
        run([sys.executable, str(ROOT / "scripts" / "create_solo_project.py"), "Validation Solo", "--output", str(solo_project)])
        run([sys.executable, str(ROOT / "scripts" / "run_solo_migration.py"), "--project", "Validation Solo", "--input", str(ROOT / "examples" / "sample-ax-inventory.csv"), "--input", str(ROOT / "examples" / "sample-xpp-class.xpp"), "--output", str(solo_run)])
        for mode, output in [
            ("orchestrate", solo_outputs[0]),
            ("status", solo_outputs[1]),
            ("gates", solo_outputs[2]),
            ("test-plan", solo_outputs[3]),
            ("signoff", solo_outputs[4]),
        ]:
            run([sys.executable, str(ROOT / "scripts" / "generate_solo_artifacts.py"), str(solo_run), "--mode", mode, "--output", str(output)])
        for script, output in [
            ("generate_governance_pack.py", governance_outputs[0]),
            ("generate_evidence_vault.py", governance_outputs[1]),
            ("generate_scope_guard.py", governance_outputs[2]),
            ("generate_contract_risk.py", governance_outputs[3]),
            ("generate_cutover_rehearsal.py", governance_outputs[4]),
            ("generate_reconciliation_judge.py", governance_outputs[5]),
            ("generate_license_cost.py", governance_outputs[6]),
            ("generate_alm_release.py", governance_outputs[7]),
            ("generate_training_readiness.py", governance_outputs[8]),
            ("generate_isv_exit.py", governance_outputs[9]),
            ("generate_country_regulatory_pack.py", governance_outputs[10]),
            ("generate_archive_strategy.py", governance_outputs[11]),
            ("generate_hyperautomation_pack.py", governance_outputs[12]),
            ("generate_board_risk.py", governance_outputs[13]),
            ("generate_process_twin.py", governance_outputs[14]),
            ("generate_meeting_copilot.py", governance_outputs[15]),
        ]:
            run([sys.executable, str(ROOT / "scripts" / script), str(analysis), "--output", str(output)])

        for script, output in [
            ("generate_intelligence_pack.py", intelligence_outputs[0]),
            ("generate_migration_memory.py", intelligence_outputs[1]),
            ("generate_benchmark.py", intelligence_outputs[2]),
            ("generate_portfolio_control.py", intelligence_outputs[3]),
            ("generate_scenario_lab.py", intelligence_outputs[4]),
            ("generate_quality_audit.py", intelligence_outputs[5]),
            ("generate_war_game.py", intelligence_outputs[6]),
            ("generate_value_realization.py", intelligence_outputs[7]),
        ]:
            run([sys.executable, str(ROOT / "scripts" / script), str(analysis), "--output", str(output)])
        run([sys.executable, str(ROOT / "scripts" / "orchestrate_migration.py"), str(analysis), "--output", str(orchestration_output)])
        run([sys.executable, str(ROOT / "scripts" / "evaluate_evidence_gates.py"), str(analysis), "--ciso-approval", "yes", "--cutover-rehearsal", "yes", "--finance-reconciliation", "yes", "--uat-signoff", "yes", "--rollback-plan", "yes", "--output", str(evidence_gate_output)])

        report_count = len(list(analysis.glob("*")))
        template_count = len(list((workspace / "validation").glob("*.md")))
        if report_count != EXPECTED_ANALYSIS_OUTPUTS:
            raise SystemExit(f"Expected {EXPECTED_ANALYSIS_OUTPUTS} analysis outputs, got {report_count}")
        if template_count != EXPECTED_TEMPLATES:
            raise SystemExit(f"Expected {EXPECTED_TEMPLATES} templates, got {template_count}")
        if not (commerce_outputs[0] / "commerce-master-pack.md").exists():
            raise SystemExit("Commerce pack did not generate commerce-master-pack.md")
        if not (commerce_outputs[1] / "commerce-readiness.json").exists():
            raise SystemExit("Commerce readiness did not generate commerce-readiness.json")
        if not (commerce_outputs[2] / "commerce-go-live-gate.md").exists():
            raise SystemExit("Commerce cutover did not generate commerce-go-live-gate.md")
        if not (commerce_outputs[3] / "offline-recovery-runbook.md").exists():
            raise SystemExit("Commerce offline check did not generate offline-recovery-runbook.md")
        if not (solo_outputs[0] / "master-orchestration-plan.md").exists():
            raise SystemExit("Solo orchestrate did not generate master-orchestration-plan.md")
        if not (solo_outputs[1] / "migration-health-score.md").exists():
            raise SystemExit("Solo status did not generate migration-health-score.md")
        if not (solo_outputs[3] / "uat-test-execution-pack.md").exists():
            raise SystemExit("Solo test plan did not generate uat-test-execution-pack.md")
        if not (governance_outputs[0] / "autonomous-governance-master-pack.md").exists():
            raise SystemExit("Governance pack did not generate autonomous-governance-master-pack.md")
        if not (governance_outputs[1] / "migration-evidence-vault-index.md").exists():
            raise SystemExit("Evidence vault did not generate migration-evidence-vault-index.md")
        if not (governance_outputs[4] / "cutover-rehearsal-scorecard.md").exists():
            raise SystemExit("Cutover rehearsal did not generate cutover-rehearsal-scorecard.md")
        if not (governance_outputs[5] / "finance-reconciliation-judge.md").exists():
            raise SystemExit("Reconciliation judge did not generate finance-reconciliation-judge.md")
        if not (governance_outputs[13] / "board-risk-forecast.md").exists():
            raise SystemExit("Board risk did not generate board-risk-forecast.md")
        if not (export_output / "ceo-migration-value-deck.pptx").exists():
            raise SystemExit("Export did not generate CEO deck")
        if not (export_output / "pmo-control-workbook.xlsx").exists():
            raise SystemExit("Export did not generate PMO workbook")
        if not (intelligence_outputs[0] / "intelligence-fabric-master-pack.md").exists():
            raise SystemExit("Intelligence pack did not generate master pack")
        if not (orchestration_output / "skill-routing.json").exists():
            raise SystemExit("Orchestrator did not generate skill-routing.json")
        if not (evidence_gate_output / "go-live-gate-result.json").exists():
            raise SystemExit("Evidence gates did not generate go-live-gate-result.json")
        run([sys.executable, str(ROOT / "scripts" / "create_project_wizard.py"), "--profile", "multi-country", "--project", "Validation Global", "--output", str(wizard_output)])
        run([sys.executable, str(ROOT / "scripts" / "create_demo_projects.py"), "--output", str(demo_output)])
        if not (wizard_output / "wizard-plan.md").exists():
            raise SystemExit("Wizard did not generate wizard-plan.md")
        if not (demo_output / "commerce-pos" / "analysis" / "dashboard.html").exists():
            raise SystemExit("Demo projects did not generate commerce-pos dashboard.html")
        if not (demo_output / "multi-country-rollout" / "analysis" / "dashboard.html").exists():
            raise SystemExit("Demo projects did not generate multi-country dashboard.html")

    todo_hits = []
    for path in [*ROOT.rglob("*"), ROOT.parents[1] / ".agents" / "plugins" / "marketplace.json"]:
        if path.is_file() and path.suffix.lower() in (".json", ".md", ".py", ".csv", ".xpp", ".xpo"):
            text = path.read_text(encoding="utf-8", errors="ignore")
            placeholder = "[" + "TODO"
            if placeholder in text:
                todo_hits.append(str(path))
    if todo_hits:
        raise SystemExit("TODO placeholders found:\n" + "\n".join(todo_hits))

    print("Plugin validation passed.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
