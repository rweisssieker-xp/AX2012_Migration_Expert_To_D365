#!/usr/bin/env python3
"""Create a guided migration command plan for common project profiles."""

from __future__ import annotations

import argparse
import json
from pathlib import Path


PROFILES = {
    "ax40": {
        "input": "plugins/ax-to-d365fo-migration-expert/examples/sample-ax-inventory.csv",
        "focus": ["AX 4.0", "Legacy code", "Data cleanup", "Process redesign", "Security redesign"],
        "commands": ["analyze", "profile-data", "stakeholder-pack", "governance-pack", "debt-liquidator", "evidence-vault", "quality-audit"],
    },
    "ax2009": {
        "input": "plugins/ax-to-d365fo-migration-expert/examples/ax2009-finance-inventory.csv",
        "focus": ["AX 2009", "Finance", "Tax", "Reconciliation", "Legacy integrations"],
        "commands": ["analyze", "persona-pack", "stakeholder-pack", "governance-pack", "reconciliation-judge", "evidence-vault", "board-risk"],
    },
    "ax2012": {
        "input": "plugins/ax-to-d365fo-migration-expert/examples/ax2012-r3-manufacturing-inventory.csv",
        "focus": ["AX 2012", "Modelstore", "Custom code", "Data entities", "LCS readiness"],
        "commands": ["analyze", "stakeholder-pack", "solo-orchestrate", "process-twin", "cutover-rehearsal", "intelligence-pack"],
    },
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
        "commands": ["analyze", "commerce-pack", "commerce-readiness", "commerce-cutover", "commerce-offline-check", "commerce-payments-pack", "evidence-gates", "governance-pack"],
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
    "pos": {
        "input": "plugins/ax-to-d365fo-migration-expert/examples/ax2012-retail-commerce-pos-inventory.csv",
        "focus": ["POS", "Offline DB", "Payment terminals", "Store hardware", "Cashier smoke tests"],
        "commands": ["analyze", "commerce-store-pack", "commerce-offline-check", "commerce-payments-pack", "commerce-cutover", "evidence-gates"],
    },
    "multi-country": {
        "input": "plugins/ax-to-d365fo-migration-expert/examples/ax2012-multi-country-rollout-inventory.csv",
        "focus": ["Konzernrollout", "Legal entities", "Localization", "Tax", "Wave planning", "Portfolio control"],
        "commands": ["analyze", "country-regulatory-pack", "portfolio-control", "scenario-lab", "board-risk", "governance-pack", "evidence-vault"],
    },
    "corporate-rollout": {
        "input": "plugins/ax-to-d365fo-migration-expert/examples/ax2012-multi-country-rollout-inventory.csv",
        "focus": ["Konzernrollout", "Template rollout", "Wave governance", "Value realization", "Board reporting"],
        "commands": ["analyze", "portfolio-control", "rollout-wave-optimizer", "scenario-lab", "value-realization", "board-risk"],
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
        elif command == "profile-data":
            lines.append(f"python .\\axmigrate.py profile-data {data['input']} --output {output}/{slug}/data-quality-profile.md")
        elif command == "evidence-gates":
            lines.append(f"python .\\axmigrate.py evidence-gates {analysis} --output {output}/{slug}/evidence-gates")
        elif command == "rollout-wave-optimizer":
            lines.append(f"python .\\axmigrate.py portfolio-control {analysis} --output {output}/{slug}/portfolio-control")
        else:
            lines.append(f"python .\\axmigrate.py {command} {analysis} --output {output}/{slug}/{command}")
    return lines


def choose_profile() -> str:
    names = sorted(PROFILES)
    print("Migration Wizard Profile:")
    for idx, name in enumerate(names, start=1):
        print(f"  {idx}. {name} - {', '.join(PROFILES[name]['focus'][:3])}")
    raw = input("Profilnummer oder Profilname: ").strip()
    if raw.isdigit() and 1 <= int(raw) <= len(names):
        return names[int(raw) - 1]
    if raw in PROFILES:
        return raw
    raise SystemExit(f"Unknown profile: {raw}")


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--profile", choices=sorted(PROFILES))
    parser.add_argument("--project", default="Contoso AX Migration")
    parser.add_argument("--output", default="migration-wizard")
    args = parser.parse_args()

    if not args.profile:
        args.profile = choose_profile()

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
