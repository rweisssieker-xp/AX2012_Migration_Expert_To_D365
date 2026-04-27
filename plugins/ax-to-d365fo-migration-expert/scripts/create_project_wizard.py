#!/usr/bin/env python3
"""Create a guided migration command plan for common project profiles."""

from __future__ import annotations

import argparse
import json
from pathlib import Path


PROFILES = {
    "finance": {
        "input": "plugins/ax-to-d365fo-migration-expert/examples/ax2009-finance-inventory.csv",
        "focus": ["Finance", "Tax", "Security", "Reconciliation", "Audit"],
        "commands": ["analyze", "persona-pack", "stakeholder-pack", "governance-pack", "reconciliation-judge", "evidence-vault", "board-risk"],
    },
    "manufacturing": {
        "input": "plugins/ax-to-d365fo-migration-expert/examples/ax2012-r3-manufacturing-inventory.csv",
        "focus": ["Manufacturing", "SCM", "AIF", "ISV", "Shop floor"],
        "commands": ["analyze", "stakeholder-pack", "solo-orchestrate", "isv-exit", "process-twin", "cutover-rehearsal"],
    },
    "commerce": {
        "input": "plugins/ax-to-d365fo-migration-expert/examples/ax2012-retail-commerce-pos-inventory.csv",
        "focus": ["Commerce", "CSU", "POS Offline", "Payments", "Store Operations"],
        "commands": ["analyze", "commerce-pack", "commerce-readiness", "commerce-cutover", "commerce-offline-check", "commerce-payments-pack", "governance-pack"],
    },
    "crm": {
        "input": "plugins/ax-to-d365fo-migration-expert/examples/ax2012-crm-lead-to-cash-inventory.csv",
        "focus": ["CRM", "Dataverse", "Lead-to-Cash", "Customer Master", "Sales"],
        "commands": ["analyze", "commerce-crm-pack", "process-twin", "evidence-vault", "reconciliation-judge"],
    },
    "solo": {
        "input": "plugins/ax-to-d365fo-migration-expert/examples/sample-ax-inventory.csv",
        "focus": ["Solo Operator", "Master Orchestrator", "Evidence", "Gates", "Testing", "Sign-off"],
        "commands": ["solo-init", "solo-run", "solo-orchestrate", "solo-evidence", "solo-gates", "solo-test-plan", "solo-signoff"],
    },
}


def command_lines(profile: str, project: str, output: str) -> list[str]:
    slug = "".join(ch.lower() if ch.isalnum() else "-" for ch in project).strip("-") or "migration-project"
    data = PROFILES[profile]
    analysis = f"{output}/{slug}/analysis"
    lines = []
    for command in data["commands"]:
        if command == "analyze":
            lines.append(f"python .\\axmigrate.py analyze {data['input']} --output {analysis}")
        elif command == "solo-init":
            lines.append(f"python .\\axmigrate.py solo-init \"{project}\" --output {output}/{slug}/solo")
        elif command == "solo-run":
            lines.append(f"python .\\axmigrate.py solo-run --project \"{project}\" --input {data['input']} --output {output}/{slug}/solo")
        elif command.startswith("solo-"):
            lines.append(f"python .\\axmigrate.py {command} {output}/{slug}/solo/{slug} --output {output}/{slug}/{command}")
        else:
            lines.append(f"python .\\axmigrate.py {command} {analysis} --output {output}/{slug}/{command}")
    return lines


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--profile", choices=sorted(PROFILES), required=True)
    parser.add_argument("--project", default="Contoso AX Migration")
    parser.add_argument("--output", default="migration-wizard")
    args = parser.parse_args()

    target = Path(args.output)
    target.mkdir(parents=True, exist_ok=True)
    lines = command_lines(args.profile, args.project, args.output)
    payload = {"profile": args.profile, "project": args.project, "focus": PROFILES[args.profile]["focus"], "commands": lines}
    (target / "wizard-plan.json").write_text(json.dumps(payload, indent=2), encoding="utf-8")
    (target / "wizard-plan.md").write_text(
        "# Migration Wizard Plan\n\n"
        f"## Profile\n\n`{args.profile}`\n\n"
        "## Focus\n\n" + "\n".join(f"- {item}" for item in PROFILES[args.profile]["focus"]) + "\n\n"
        "## Commands\n\n" + "\n".join(f"```powershell\n{line}\n```" for line in lines) + "\n",
        encoding="utf-8",
    )
    print(f"Generated wizard plan into {target.resolve()}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
