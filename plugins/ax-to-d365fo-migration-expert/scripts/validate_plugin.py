#!/usr/bin/env python3
"""Validate the AX to D365FO migration plugin."""

from __future__ import annotations

import json
import subprocess
import sys
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


def main() -> int:
    for path in [ROOT / ".codex-plugin" / "plugin.json", *list((ROOT / "config").glob("*.json"))]:
        assert_json(path)

    run([sys.executable, "-m", "unittest", "discover", str(ROOT / "tests")])
    analysis = ROOT / "_validation_analysis"
    workspace = ROOT / "_validation_workspace"
    run([sys.executable, str(ROOT / "scripts" / "analyze_ax_inventory.py"), str(ROOT / "examples" / "sample-ax-inventory.csv"), str(ROOT / "examples" / "sample-xpp-class.xpp"), "--output", str(analysis)])
    run([sys.executable, str(ROOT / "scripts" / "create_migration_workspace.py"), "Validation", "--output", str(workspace)])

    report_count = len(list(analysis.glob("*")))
    template_count = len(list((workspace / "validation").glob("*.md")))
    if report_count != 31:
        raise SystemExit(f"Expected 31 analysis outputs, got {report_count}")
    if template_count != 52:
        raise SystemExit(f"Expected 52 templates, got {template_count}")

    for base in (analysis, workspace):
        if base.exists():
            for child in sorted(base.rglob("*"), reverse=True):
                child.unlink() if child.is_file() else child.rmdir()
            base.rmdir()

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
