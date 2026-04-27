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
    "multi-country-rollout": ROOT / "examples" / "ax2012-multi-country-rollout-inventory.csv",
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
        if name == "multi-country-rollout":
            run("generate_country_regulatory_pack.py", [str(analysis), "--output", str(demo / "country-regulatory-pack")])
            run("generate_board_risk.py", [str(analysis), "--output", str(demo / "board-risk")])
            run("generate_portfolio_control.py", [str(analysis), "--output", str(demo / "portfolio-control")])
            run("generate_scenario_lab.py", [str(analysis), "--output", str(demo / "scenario-lab")])
        dashboard_rows.append(f"| {name} | `{source.name}` | [{name} dashboard](./{name}/analysis/dashboard.html) |")
    write_demo_index(root, dashboard_rows)
    (root / "README.md").write_text(
        "# Demo Projects\n\n"
        "| Demo | Input | Dashboard |\n| --- | --- | --- |\n"
        + "\n".join(dashboard_rows)
        + "\n\nEach demo includes analysis, persona, and governance outputs. Commerce and CRM demos include their domain packs.\n",
        encoding="utf-8",
    )
    print(f"Generated demo projects into {root.resolve()}")
    return 0


def write_demo_index(root: Path, dashboard_rows: list[str]) -> None:
    cards = []
    for line in dashboard_rows:
        parts = [part.strip() for part in line.strip("|").split("|")]
        if len(parts) >= 3:
            name = parts[0]
            cards.append(
                f"<section><h2>{name}</h2><a href=\"./{name}/analysis/dashboard.html\">Open dashboard</a>"
                f"<p>Analysis, persona and governance outputs are generated under <code>{name}</code>.</p></section>"
            )
    (root / "demo-index.html").write_text(
        "<!doctype html><html lang=\"en\"><head><meta charset=\"utf-8\"><title>AX Migration Demo Index</title>"
        "<style>body{font-family:Segoe UI,Arial,sans-serif;margin:0;background:#f4f7fa;color:#172033}"
        "header{background:#17446b;color:white;padding:24px 32px}main{padding:24px 32px;display:grid;grid-template-columns:repeat(auto-fit,minmax(260px,1fr));gap:16px}"
        "section{background:white;border:1px solid #d9e2ec;border-radius:8px;padding:18px}a{color:#0f5f8f;font-weight:700}</style></head>"
        "<body><header><h1>AX to D365FO Demo Projects</h1><p>Ready-to-open dashboards and generated migration packs.</p></header><main>"
        + "\n".join(cards)
        + "</main></body></html>",
        encoding="utf-8",
    )


if __name__ == "__main__":
    raise SystemExit(main())
