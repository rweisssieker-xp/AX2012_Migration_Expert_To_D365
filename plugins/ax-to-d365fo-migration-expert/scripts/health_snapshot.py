#!/usr/bin/env python3
"""Generate a compact project health snapshot from a guided run or analysis folder."""

from __future__ import annotations

import argparse
import json
from pathlib import Path


def load_json(path: Path, default):
    try:
        return json.loads(path.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError):
        return default


def find_file(root: Path, name: str) -> Path | None:
    if root.is_file() and root.name == name:
        return root
    if not root.exists():
        return None
    direct = root / name
    if direct.exists():
        return direct
    matches = sorted(root.rglob(name))
    return matches[0] if matches else None


def evidence_score(root: Path) -> tuple[int, list[str]]:
    manifest_path = find_file(root, "evidence-manifest.json")
    if not manifest_path:
        return 25, ["Evidence manifest is missing."]
    manifest = load_json(manifest_path, [])
    if not manifest:
        return 35, ["Evidence manifest exists but has no evidence files."]
    with_hash = sum(1 for item in manifest if item.get("sha256"))
    with_owner = sum(1 for item in manifest if item.get("owner"))
    with_gate = sum(1 for item in manifest if item.get("gate"))
    score = int((with_hash + with_owner + with_gate) / (len(manifest) * 3) * 100)
    gaps = []
    if with_hash < len(manifest):
        gaps.append("Some evidence files have no hash.")
    if with_owner < len(manifest):
        gaps.append("Some evidence files have no owner.")
    if with_gate < len(manifest):
        gaps.append("Some evidence files have no gate mapping.")
    return max(0, min(100, score)), gaps or ["Evidence manifest is complete enough for audit review."]


def security_status(root: Path) -> tuple[str, int]:
    report_path = find_file(root, "security-scan-report.json")
    report = load_json(report_path, {}) if report_path else {}
    findings = report.get("findings", []) if isinstance(report, dict) else []
    if not report_path:
        return "Needs control", 0
    return ("Blocked" if findings else "Ready", len(findings))


def gate_status(root: Path) -> tuple[str, list[str]]:
    gate_path = find_file(root, "go-live-gate-result.json")
    gate = load_json(gate_path, {}) if gate_path else {}
    if not gate:
        return "Needs control", ["Evidence gate result is missing."]
    answers = gate.get("answers", {})
    missing = [key for key, value in answers.items() if value is False]
    return gate.get("status", "Needs control"), missing


def route_summary(root: Path) -> list[str]:
    route_path = find_file(root, "skill-routing.json")
    routes = load_json(route_path, []) if route_path else []
    if not routes:
        return ["No automatic skill routing found."]
    return [f"{item.get('domain', 'unknown')} ({item.get('score', 0)})" for item in routes[:5]]


def overall_status(gate: str, security: str, evidence: int) -> str:
    if "Blocked" in (gate, security) or evidence < 50:
        return "Blocked"
    if "Needs control" in (gate, security) or evidence < 75:
        return "Needs control"
    return "Ready"


def next_actions(status: str, missing_gates: list[str], evidence_gaps: list[str], security_findings: int) -> list[str]:
    actions = []
    if missing_gates:
        actions.append("Close missing gate evidence: " + ", ".join(missing_gates[:5]) + ".")
    if security_findings:
        actions.append(f"Review and resolve {security_findings} security scan finding(s).")
    if evidence_gaps and "complete enough" not in evidence_gaps[0]:
        actions.append(evidence_gaps[0])
    if status == "Ready":
        actions.append("Prepare external sign-off meeting with generated evidence pack.")
    actions.append("Run `python .\\axmigrate.py guided-run <input> --project <name> --output <folder>` after evidence changes.")
    return actions[:5]


def render_markdown(source: Path) -> str:
    evidence, evidence_gaps = evidence_score(source)
    security, security_findings = security_status(source)
    gate, missing_gates = gate_status(source)
    status = overall_status(gate, security, evidence)
    routes = route_summary(source)
    actions = next_actions(status, missing_gates, evidence_gaps, security_findings)
    return (
        "# Project Health Snapshot\n\n"
        f"## Overall Status\n\n`{status}`\n\n"
        "## Signals\n\n"
        f"- Evidence strength: `{evidence}`\n"
        f"- Gate status: `{gate}`\n"
        f"- Security status: `{security}` with `{security_findings}` finding(s)\n"
        f"- Skill routing: {', '.join(routes)}\n\n"
        "## Top Actions\n\n"
        + "\n".join(f"- {action}" for action in actions)
        + "\n\n## Evidence Gaps\n\n"
        + "\n".join(f"- {gap}" for gap in evidence_gaps)
        + "\n"
    )


def render_html(markdown: str) -> str:
    lines = markdown.splitlines()
    body = []
    for line in lines:
        if line.startswith("# "):
            body.append(f"<h1>{line[2:]}</h1>")
        elif line.startswith("## "):
            body.append(f"<h2>{line[3:]}</h2>")
        elif line.startswith("- "):
            body.append(f"<li>{line[2:]}</li>")
        elif line.strip():
            body.append(f"<p>{line}</p>")
    return (
        "<!doctype html><html lang=\"en\"><head><meta charset=\"utf-8\"><title>Project Health Snapshot</title>"
        "<style>body{font-family:Segoe UI,Arial,sans-serif;margin:0;background:#f4f7fa;color:#172033}"
        "main{max-width:980px;margin:auto;padding:28px}h1{color:#17446b}h2{margin-top:28px}"
        "p,li{font-size:15px;line-height:1.45}code{background:#eef3f8;padding:2px 5px;border-radius:4px}</style></head>"
        "<body><main>" + "\n".join(body) + "</main></body></html>"
    )


def write_snapshot(source: Path, output: Path) -> None:
    output.mkdir(parents=True, exist_ok=True)
    markdown = render_markdown(source)
    (output / "project-health-snapshot.md").write_text(markdown, encoding="utf-8")
    (output / "project-health-snapshot.html").write_text(render_html(markdown), encoding="utf-8")


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("source")
    parser.add_argument("--output", default="health-snapshot")
    args = parser.parse_args()
    write_snapshot(Path(args.source), Path(args.output))
    print(f"Generated health snapshot into {Path(args.output).resolve()}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
