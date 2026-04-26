#!/usr/bin/env python3
"""Validate the AX to D365FO migration plugin."""

from __future__ import annotations

import json
import subprocess
import sys
import tempfile
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]


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


def main() -> int:
    for path in [ROOT / ".codex-plugin" / "plugin.json", *list((ROOT / "config").glob("*.json"))]:
        assert_json(path)
    skill_files = sorted((ROOT / "skills").glob("*/SKILL.md"))
    if len(skill_files) != 76:
        raise SystemExit(f"Expected 76 skills, got {len(skill_files)}")
    for path in skill_files:
        assert_skill(path)

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
        run([sys.executable, str(ROOT / "scripts" / "analyze_ax_inventory.py"), str(ROOT / "examples" / "sample-ax-inventory.csv"), str(ROOT / "examples" / "sample-xpp-class.xpp"), "--output", str(analysis)])
        run([sys.executable, str(ROOT / "scripts" / "create_migration_workspace.py"), "Validation", "--output", str(workspace)])
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

        report_count = len(list(analysis.glob("*")))
        template_count = len(list((workspace / "validation").glob("*.md")))
        if report_count != 46:
            raise SystemExit(f"Expected 46 analysis outputs, got {report_count}")
        if template_count != 211:
            raise SystemExit(f"Expected 211 templates, got {template_count}")
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
