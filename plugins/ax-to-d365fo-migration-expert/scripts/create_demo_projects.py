#!/usr/bin/env python3
"""Generate ready-to-open demo projects for the migration plugin."""

from __future__ import annotations

import argparse
import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SCRIPTS = ROOT / "scripts"

DEMOS = {
    "finance": ROOT / "examples" / "ax2009-finance-inventory.csv",
    "manufacturing": ROOT / "examples" / "ax2012-r3-manufacturing-inventory.csv",
    "commerce-pos": ROOT / "examples" / "ax2012-retail-commerce-pos-inventory.csv",
    "crm-lead-to-cash": ROOT / "examples" / "ax2012-crm-lead-to-cash-inventory.csv",
}


def run(script: str, args: list[str]) -> None:
    result = subprocess.run([sys.executable, str(SCRIPTS / script), *args], text=True, capture_output=True)
    if result.returncode:
        print(result.stdout)
        print(result.stderr)
        raise SystemExit(result.returncode)


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", default="demo-projects")
    args = parser.parse_args()
    root = Path(args.output)
    root.mkdir(parents=True, exist_ok=True)
    dashboard_rows = []
    for name, source in DEMOS.items():
        demo = root / name
        analysis = demo / "analysis"
        run("analyze_ax_inventory.py", [str(source), "--output", str(analysis)])
        run("generate_persona_pack.py", [str(analysis), "--persona", "all", "--output", str(demo / "persona-pack")])
        run("generate_governance_pack.py", [str(analysis), "--output", str(demo / "governance-pack")])
        if name == "commerce-pos":
            run("generate_commerce_pack.py", [str(analysis), "--output", str(demo / "commerce-pack")])
            run("generate_commerce_cutover.py", [str(analysis), "--output", str(demo / "commerce-cutover")])
        if name == "crm-lead-to-cash":
            run("generate_commerce_crm_pack.py", [str(analysis), "--output", str(demo / "commerce-crm-pack")])
        dashboard_rows.append(f"| {name} | `{source.name}` | [{name} dashboard](./{name}/analysis/dashboard.html) |")
    (root / "README.md").write_text(
        "# Demo Projects\n\n"
        "| Demo | Input | Dashboard |\n| --- | --- | --- |\n"
        + "\n".join(dashboard_rows)
        + "\n\nEach demo includes analysis, persona, and governance outputs. Commerce and CRM demos include their domain packs.\n",
        encoding="utf-8",
    )
    print(f"Generated demo projects into {root.resolve()}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
