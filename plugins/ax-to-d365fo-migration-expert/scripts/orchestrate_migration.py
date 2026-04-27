#!/usr/bin/env python3
"""Automatically route migration input to skills, artifacts, evidence gaps, and next CLI commands."""

from __future__ import annotations

import argparse
import json
import re
from pathlib import Path


ROUTES = {
    "commerce": {
        "keywords": ["commerce", "retail", "pos", "store", "csu", "channel", "payment", "loyalty", "offline"],
        "skills": ["ax-migration-commerce-orchestrator", "ax-migration-commerce-lead", "ax-migration-pos-lead", "ax-migration-payments-lead"],
        "commands": ["commerce-pack", "commerce-readiness", "commerce-cutover"],
        "evidence": ["CSU readiness", "POS smoke tests", "Payment/PCI evidence", "Store cutover smoke tests"],
    },
    "crm": {
        "keywords": ["crm", "dataverse", "lead", "opportunity", "case", "customer master", "dual-write"],
        "skills": ["ax-migration-crm-owner", "ax-migration-lead-management-owner", "ax-migration-customer-master-lead"],
        "commands": ["commerce-crm-pack", "process-twin"],
        "evidence": ["Lead-to-Cash traceability", "Customer master harmonization", "Dual-write decision"],
    },
    "governance": {
        "keywords": ["evidence", "gate", "approval", "ciso", "audit", "scope", "contract", "reconciliation", "cutover"],
        "skills": ["ax-migration-autonomous-governance-orchestrator", "ax-migration-evidence-vault-manager", "ax-migration-reconciliation-judge"],
        "commands": ["governance-pack", "evidence-vault", "evidence-gates", "reconciliation-judge"],
        "evidence": ["External approvals", "Evidence freshness", "Reconciliation sign-off", "Cutover rehearsal result"],
    },
    "solo": {
        "keywords": ["solo", "alone", "alleine", "master", "orchestrator", "next action", "signoff"],
        "skills": ["ax-migration-master-orchestrator", "ax-migration-solo-operator", "ax-migration-ai-migration-brain"],
        "commands": ["solo-orchestrate", "solo-evidence", "solo-gates", "solo-test-plan", "solo-signoff"],
        "evidence": ["Role substitution", "Self-approval gate", "External approval boundary", "Test evidence"],
    },
    "fabric": {
        "keywords": ["memory", "benchmark", "portfolio", "scenario", "quality", "war game", "value realization", "continuous improvement"],
        "skills": ["ax-migration-intelligence-fabric-orchestrator", "ax-migration-migration-memory", "ax-migration-scenario-lab"],
        "commands": ["intelligence-pack", "migration-memory", "benchmark", "scenario-lab", "war-game", "value-realization"],
        "evidence": ["Benchmark baseline", "Scenario assumptions", "Portfolio wave data", "Post-go-live KPI baseline"],
    },
}


def read_text(source: Path) -> str:
    if source.is_file():
        return source.read_text(encoding="utf-8", errors="ignore")
    parts = []
    if source.exists():
        for path in sorted(source.rglob("*")):
            if path.is_file() and path.suffix.lower() in {".md", ".json", ".csv", ".txt", ".xpp", ".xpo"}:
                parts.append(path.read_text(encoding="utf-8", errors="ignore"))
    return "\n".join(parts)


def route(text: str) -> list[dict[str, object]]:
    lower = text.lower()
    results = []
    for domain, cfg in ROUTES.items():
        hits = [kw for kw in cfg["keywords"] if kw in lower]
        if hits:
            results.append({"domain": domain, "score": min(100, 40 + len(hits) * 12), "hits": hits, **{k: cfg[k] for k in ("skills", "commands", "evidence")}})
    if not results:
        cfg = ROUTES["governance"]
        results.append({"domain": "general", "score": 50, "hits": [], **{k: cfg[k] for k in ("skills", "commands", "evidence")}})
    return sorted(results, key=lambda item: int(item["score"]), reverse=True)


def render_markdown(routes: list[dict[str, object]], source: Path) -> str:
    rows = "\n".join(f"| {r['domain']} | {r['score']} | {', '.join(r['skills'])} | {', '.join(r['commands'])} |" for r in routes)
    evidence = "\n".join(f"- {r['domain']}: " + ", ".join(r["evidence"]) for r in routes)
    commands = "\n".join(f"python .\\axmigrate.py {cmd} {source} --output orchestration-output\\{cmd}" for r in routes for cmd in r["commands"])
    return f"""# Master Orchestration Plan

## Skill Routing

| Domain | Score | Skills | Commands |
| --- | ---: | --- | --- |
{rows}

## Missing Evidence To Check

{evidence}

## Next CLI Commands

```powershell
{commands}
```
"""


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("source", help="Analysis folder, project folder, or text file.")
    parser.add_argument("--output", default="orchestration")
    args = parser.parse_args()
    source = Path(args.source)
    routes = route(read_text(source))
    output = Path(args.output)
    output.mkdir(parents=True, exist_ok=True)
    (output / "orchestration-plan.md").write_text(render_markdown(routes, source), encoding="utf-8")
    (output / "skill-routing.json").write_text(json.dumps(routes, indent=2), encoding="utf-8")
    next_commands = re.search(r"```powershell\n(.*?)\n```", render_markdown(routes, source), re.S).group(1)
    (output / "next-commands.ps1").write_text(next_commands + "\n", encoding="utf-8")
    print(f"Generated orchestration outputs into {output.resolve()}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
