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

    args = parser.parse_args()
    if args.command == "init":
        return run("create_migration_workspace.py", [args.project, "--output", args.output])
    if args.command in ("analyze", "scan-code", "dashboard"):
        return run("analyze_ax_inventory.py", [*args.inputs, "--output", args.output])
    if args.command == "extract-modelstore":
        return run("extract_modelstore_inventory.py", [args.input, "--output", args.output])
    if args.command == "export":
        return run("export_analysis.py", [args.analysis_dir, "--output", args.output])
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

Doctor:
  python axmigrate.py doctor
""".strip()
    )


if __name__ == "__main__":
    raise SystemExit(main())
