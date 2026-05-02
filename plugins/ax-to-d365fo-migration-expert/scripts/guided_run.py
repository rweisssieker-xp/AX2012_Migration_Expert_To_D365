#!/usr/bin/env python3
"""Run an end-to-end guided migration pass from source input to next actions."""

from __future__ import annotations

import argparse
import json
import subprocess
import sys
from pathlib import Path

from health_snapshot import evidence_score, write_snapshot


ROOT = Path(__file__).resolve().parents[1]
SCRIPTS = ROOT / "scripts"
SUPPORTED_INPUTS = {".csv", ".json", ".xpp", ".xpo", ".txt"}
GATE_FLAGS = [
    "ciso-approval",
    "cutover-rehearsal",
    "finance-reconciliation",
    "uat-signoff",
    "commerce-payments",
    "rollback-plan",
]


def run_script(script: str, args: list[str], log: list[str]) -> None:
    command = [sys.executable, str(SCRIPTS / script), *args]
    log.append("## " + script)
    log.append("```powershell")
    log.append(" ".join(str(item) for item in command))
    log.append("```")
    result = subprocess.run(command, text=True, capture_output=True)
    if result.stdout.strip():
        log.append(result.stdout.strip())
    if result.stderr.strip():
        log.append(result.stderr.strip())
    if result.returncode != 0:
        raise SystemExit(f"{script} failed with exit code {result.returncode}")


def discover_inputs(source: Path) -> list[Path]:
    if source.is_file():
        return [source]
    if not source.exists():
        raise SystemExit(f"Source does not exist: {source}")
    return [path for path in sorted(source.rglob("*")) if path.is_file() and path.suffix.lower() in SUPPORTED_INPUTS]


def is_analysis_folder(source: Path) -> bool:
    markers = ["dashboard.html", "ai-analysis-summary.md", "inventory-normalized.json", "work-items.csv"]
    return source.is_dir() and any((source / marker).exists() for marker in markers)


def ensure_analysis(source: Path, output: Path, log: list[str]) -> Path:
    if is_analysis_folder(source):
        return source
    inputs = discover_inputs(source)
    if not inputs:
        raise SystemExit(f"No supported inventory inputs found under {source}")
    analysis = output / "analysis"
    run_script("analyze_ax_inventory.py", [*(str(path) for path in inputs), "--output", str(analysis)], log)
    return analysis


def load_routes(path: Path) -> list[dict[str, object]]:
    route_path = path / "skill-routing.json"
    if not route_path.exists():
        return []
    try:
        return json.loads(route_path.read_text(encoding="utf-8"))
    except json.JSONDecodeError:
        return []


def unique_commands(routes: list[dict[str, object]]) -> list[str]:
    commands: list[str] = []
    for route in routes:
        for command in route.get("commands", []):
            if command not in commands:
                commands.append(str(command))
    for command in ["evidence-gates", "evidence-vault", "security-scan", "health-snapshot"]:
        if command not in commands:
            commands.append(command)
    return commands


def render_plan(project: str, source: Path, analysis: Path, output: Path, routes: list[dict[str, object]]) -> str:
    route_lines = "\n".join(
        f"- `{route.get('domain')}` -> skills: {', '.join(route.get('skills', []))}; commands: {', '.join(route.get('commands', []))}"
        for route in routes
    ) or "- No routed domain found; use core analysis, governance, and evidence commands."
    return (
        "# Guided Migration Run Plan\n\n"
        f"Project: `{project}`\n\n"
        f"Source: `{source}`\n\n"
        f"Analysis: `{analysis}`\n\n"
        "## Automated Steps\n\n"
        "- Analyze inventory inputs or reuse the supplied analysis folder.\n"
        "- Route project signals to skills, artifacts, and next CLI commands.\n"
        "- Generate evidence gates, governance pack, evidence vault, security scan, memory store, and health snapshot.\n"
        "- Produce a role action inbox and recommended command list.\n\n"
        "## Skill Routing\n\n"
        f"{route_lines}\n\n"
        "## Output Folders\n\n"
        + "\n".join(f"- `{path.name}`" for path in sorted(output.iterdir()) if path.is_dir())
        + "\n"
    )


def render_recommended_commands(analysis: Path, output: Path, routes: list[dict[str, object]]) -> str:
    lines = ["# Recommended Next Commands\n"]
    for command in unique_commands(routes):
        if command == "evidence-gates":
            example = f"python .\\axmigrate.py evidence-gates {analysis} --output {output / 'evidence-gates'}"
        elif command == "health-snapshot":
            example = f"python .\\axmigrate.py health-snapshot {output} --output {output}"
        elif command == "security-scan":
            example = f"python .\\axmigrate.py security-scan {analysis} --output {output / 'security-scan'}"
        elif command == "evidence-vault":
            example = f"python .\\axmigrate.py evidence-vault {analysis} --output {output / 'evidence-vault'}"
        else:
            example = f"python .\\axmigrate.py {command} {analysis} --output {output / command}"
        lines.append(f"- `{command}`\n  `{example}`")
    return "\n".join(lines) + "\n"


def render_role_inbox(routes: list[dict[str, object]]) -> str:
    domains = " ".join(str(route.get("domain", "")) for route in routes).lower()
    items = [
        ("Project Manager", "Review generated plan, assign owners for open evidence, and schedule gate closure."),
        ("CIO / Architect", "Confirm architecture, integration, data migration, and environment risks from routed domains."),
        ("CISO", "Review security scan, privileged access evidence, PCI/payment exposure, and CISO gate status."),
        ("CFO / Finance Lead", "Confirm reconciliation, tax, ledger, settlement, and sign-off evidence."),
        ("QA / Test Lead", "Turn routed workstreams into UAT, regression, smoke, and cutover rehearsal evidence."),
    ]
    if any(token in domains for token in ["commerce", "pos", "crm", "cxp"]):
        items.append(("Commerce / CRM Lead", "Validate customer, channel, POS, CSU, payment, loyalty, and lead-to-cash evidence."))
    if "integration" in domains:
        items.append(("Integration Lead", "Confirm interface ownership, retry/recovery, monitoring, and cutover sequencing."))
    return "# Role Action Inbox\n\n" + "\n".join(f"- **{role}:** {task}" for role, task in items) + "\n"


def render_evidence_strength(source: Path) -> str:
    score, gaps = evidence_score(source)
    status = "Ready" if score >= 75 else "Needs control" if score >= 50 else "Blocked"
    return (
        "# Evidence Strength Score\n\n"
        f"Status: `{status}`\n\n"
        f"Score: `{score}`\n\n"
        "## Gaps\n\n"
        + "\n".join(f"- {gap}" for gap in gaps)
        + "\n"
    )


def render_index(project: str, routes: list[dict[str, object]]) -> str:
    route_cards = "\n".join(
        "<tr>"
        f"<td>{route.get('domain', 'unknown')}</td>"
        f"<td>{route.get('score', 0)}</td>"
        f"<td>{', '.join(route.get('skills', []))}</td>"
        f"<td>{', '.join(route.get('commands', []))}</td>"
        "</tr>"
        for route in routes[:8]
    ) or "<tr><td colspan=\"4\">No routed domain found.</td></tr>"
    links = [
        ("Project Health Snapshot", "project-health-snapshot.html"),
        ("Guided Run Plan", "guided-run-plan.md"),
        ("Recommended Commands", "recommended-commands.md"),
        ("Role Action Inbox", "role-action-inbox.md"),
        ("Evidence Strength Score", "evidence-strength-score.md"),
        ("Analysis Dashboard", "analysis/dashboard.html"),
        ("Evidence Gate Result", "evidence-gates/go-live-gate-result.json"),
        ("Security Scan", "security-scan/security-scan-report.md"),
        ("Office Exports", "exports/"),
    ]
    link_items = "\n".join(f"<a href=\"{href}\">{label}</a>" for label, href in links)
    return (
        "<!doctype html><html lang=\"en\"><head><meta charset=\"utf-8\"><title>Guided Migration Run</title>"
        "<style>body{font-family:Segoe UI,Arial,sans-serif;margin:0;background:#f5f7f9;color:#16202f}"
        "main{max-width:1160px;margin:auto;padding:28px}header{display:flex;justify-content:space-between;gap:20px;align-items:flex-end}"
        "h1{margin:0;color:#173f5f}.grid{display:grid;grid-template-columns:repeat(auto-fit,minmax(220px,1fr));gap:12px;margin:22px 0}"
        "a{display:block;padding:12px 14px;background:#fff;border:1px solid #d9e2ec;border-radius:6px;color:#17446b;text-decoration:none;font-weight:600}"
        "table{width:100%;border-collapse:collapse;background:#fff;border:1px solid #d9e2ec}th,td{text-align:left;padding:10px;border-bottom:1px solid #e7edf3;vertical-align:top}"
        "th{background:#eef3f8}</style></head><body><main>"
        f"<header><div><h1>{project}</h1><p>Guided migration run command center</p></div><a href=\"project-health-snapshot.html\">Open Health Snapshot</a></header>"
        f"<section class=\"grid\">{link_items}</section>"
        "<section><h2>Skill Routing</h2><table><thead><tr><th>Domain</th><th>Score</th><th>Skills</th><th>Commands</th></tr></thead>"
        f"<tbody>{route_cards}</tbody></table></section>"
        "</main></body></html>"
    )


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("source", help="Inventory file/folder or existing analysis folder.")
    parser.add_argument("--project", default="Migration Project")
    parser.add_argument("--output", default="guided-run")
    for flag in GATE_FLAGS:
        parser.add_argument(f"--{flag}", choices=["yes", "no"], default="no")
    args = parser.parse_args()

    source = Path(args.source)
    output = Path(args.output)
    output.mkdir(parents=True, exist_ok=True)
    log: list[str] = ["# Guided Run Log\n"]

    analysis = ensure_analysis(source, output, log)
    orchestration = output / "orchestration"
    gates = output / "evidence-gates"
    governance = output / "governance-pack"
    evidence = output / "evidence-vault"
    security = output / "security-scan"
    memory = output / "memory-store"
    exports = output / "exports"

    run_script("orchestrate_migration.py", [str(analysis), "--output", str(orchestration)], log)
    gate_args = [str(analysis), "--output", str(gates)]
    for flag in GATE_FLAGS:
        gate_args += [f"--{flag}", getattr(args, flag.replace("-", "_"))]
    run_script("evaluate_evidence_gates.py", gate_args, log)
    run_script("generate_governance_pack.py", [str(analysis), "--output", str(governance)], log)
    run_script("generate_evidence_vault.py", [str(analysis), "--output", str(evidence)], log)
    run_script("scan_sensitive_data.py", [str(analysis), "--output", str(security)], log)
    run_script("update_migration_memory_store.py", [str(analysis), "--project", args.project, "--output", str(memory)], log)
    run_script("export_analysis.py", [str(analysis), "--output", str(exports)], log)

    routes = load_routes(orchestration)
    (output / "guided-run-plan.md").write_text(render_plan(args.project, source, analysis, output, routes), encoding="utf-8")
    (output / "recommended-commands.md").write_text(render_recommended_commands(analysis, output, routes), encoding="utf-8")
    (output / "role-action-inbox.md").write_text(render_role_inbox(routes), encoding="utf-8")
    (output / "evidence-strength-score.md").write_text(render_evidence_strength(output), encoding="utf-8")
    (output / "guided-run-log.md").write_text("\n\n".join(log) + "\n", encoding="utf-8")
    write_snapshot(output, output)
    (output / "index.html").write_text(render_index(args.project, routes), encoding="utf-8")

    print(f"Generated guided run into {output.resolve()}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
