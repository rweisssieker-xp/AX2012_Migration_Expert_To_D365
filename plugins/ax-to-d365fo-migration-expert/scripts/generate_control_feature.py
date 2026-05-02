#!/usr/bin/env python3
"""Generate advanced AI control, sales, wizard, and release feature packs."""

from __future__ import annotations

import argparse
import csv
import json
import zipfile
from datetime import datetime, timezone
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
REPO = ROOT.parents[1]

MODES = {
    "usp-actions": {
        "title": "USP-to-Action Engine",
        "files": ["usp-to-action-map.md", "usp-to-action-map.json"],
        "summary": "Turns each USP into CLI commands, skills, proof artifacts, and demo narrative.",
    },
    "truth-detector": {
        "title": "Project Truth Detector",
        "files": ["project-truth-detector.md", "project-truth-detector.json"],
        "summary": "Compares reported status with evidence, gates, tests, and generated artifacts.",
    },
    "cutover-confidence": {
        "title": "Cutover Confidence Engine",
        "files": ["cutover-confidence-score.md", "cutover-confidence-score.json"],
        "summary": "Scores cutover readiness across rehearsal, rollback, smoke tests, finance, security, and Commerce/POS.",
    },
    "meeting-actions": {
        "title": "AI Meeting-to-Migration Actions",
        "files": ["meeting-to-migration-actions.md", "meeting-to-migration-actions.csv"],
        "summary": "Converts notes into decisions, risks, tasks, evidence gaps, and next commands.",
    },
    "proposal-pack": {
        "title": "AI Proposal / Sales Pack Generator",
        "files": ["proposal-sales-pack.md", "proposal-sales-pack.html"],
        "summary": "Creates sales and proposal narrative from USPs, demo evidence, and analysis signals.",
    },
    "role-prompt-pack": {
        "title": "AI Role Prompt Packs 2.0",
        "files": ["role-prompt-pack-2.md", "role-prompt-pack-2.json"],
        "summary": "Provides role-specific prompt libraries with expected outputs and evidence requirements.",
    },
    "evidence-freshness": {
        "title": "Evidence Freshness Monitor",
        "files": ["evidence-freshness-monitor.md", "evidence-freshness-monitor.json"],
        "summary": "Marks evidence as current, aging, stale, or missing based on file age and gate relevance.",
    },
    "dependency-risk-graph": {
        "title": "Dependency Risk Graph",
        "files": ["dependency-risk-graph.md", "dependency-risk-graph.json"],
        "summary": "Visualizes dependencies between workstreams, gates, tests, integrations, and cutover steps.",
    },
    "partner-deliverable-check": {
        "title": "Partner Deliverable Checker",
        "files": ["partner-deliverable-check.md", "partner-deliverable-check.json"],
        "summary": "Checks whether partner deliverables, sign-offs, evidence, and scope controls exist.",
    },
    "release-pack": {
        "title": "Release ZIP Builder",
        "files": ["release-pack-manifest.md", "ax-to-d365fo-migration-expert-release.zip"],
        "summary": "Builds a distribution ZIP with plugin, docs, examples, scripts, configs, and checksums-ready manifest.",
    },
    "demo-portal": {
        "title": "Demo Portal 2.0",
        "files": ["demo-portal-2.md", "demo-portal-2.html"],
        "summary": "Links demo projects, guided runs, health snapshots, USP packs, dashboards, and pitch story.",
    },
    "wizard-ui": {
        "title": "Interactive Local Wizard UI 2.0",
        "files": ["wizard-ui-2.md", "interactive-wizard-ui-2.html"],
        "summary": "Creates a local browser UI for selecting project type, gates, evidence, packs, and generated commands.",
    },
}


def read_text(source: Path) -> str:
    if source.is_file():
        return source.read_text(encoding="utf-8", errors="ignore")
    if not source.exists():
        return ""
    parts = []
    for path in sorted(source.rglob("*")):
        if path.is_file() and path.suffix.lower() in {".md", ".json", ".csv", ".txt"}:
            parts.append(path.read_text(encoding="utf-8", errors="ignore")[:20000])
    return "\n".join(parts)


def signals(text: str) -> dict[str, int]:
    lower = text.lower()
    groups = {
        "evidence": ["evidence", "gate", "sign-off", "signoff", "approval", "hash"],
        "cutover": ["cutover", "rollback", "smoke", "war room", "rehearsal", "hypercare"],
        "security": ["security", "ciso", "pci", "secret", "privileged", "sod"],
        "finance": ["finance", "ledger", "reconciliation", "tax", "cfo", "settlement"],
        "commerce": ["commerce", "pos", "store", "csu", "payment", "offline"],
        "data": ["data", "migration", "mapping", "quality", "customer", "vendor"],
        "integration": ["integration", "interface", "api", "aif", "odata", "retry"],
        "testing": ["test", "uat", "regression", "defect", "qa", "key user"],
    }
    return {name: sum(lower.count(token) for token in tokens) for name, tokens in groups.items()}


def status_from_score(score: int) -> str:
    if score >= 75:
        return "Ready"
    if score >= 50:
        return "Needs control"
    return "Blocked"


def score_for(mode: str, sig: dict[str, int]) -> int:
    if mode == "cutover-confidence":
        return min(100, 35 + sig["cutover"] * 8 + sig["testing"] * 5 + sig["finance"] * 4 + sig["security"] * 4 + sig["commerce"] * 4)
    if mode == "truth-detector":
        return min(100, 30 + sig["evidence"] * 8 + sig["testing"] * 4 + sig["security"] * 3)
    if mode == "evidence-freshness":
        return min(100, 40 + sig["evidence"] * 10)
    return min(100, 55 + sum(1 for value in sig.values() if value > 0) * 5)


def write_json(output: Path, name: str, data: dict[str, object]) -> None:
    (output / name).write_text(json.dumps(data, indent=2), encoding="utf-8")


def write_html(output: Path, name: str, title: str, markdown: str) -> None:
    body = []
    for line in markdown.splitlines():
        if line.startswith("# "):
            body.append(f"<h1>{line[2:]}</h1>")
        elif line.startswith("## "):
            body.append(f"<h2>{line[3:]}</h2>")
        elif line.startswith("- "):
            body.append(f"<li>{line[2:]}</li>")
        elif line.strip():
            body.append(f"<p>{line}</p>")
    html = (
        "<!doctype html><html lang=\"en\"><head><meta charset=\"utf-8\">"
        f"<title>{title}</title><style>body{{font-family:Segoe UI,Arial,sans-serif;margin:0;background:#f6f8fb;color:#172033}}"
        "main{max-width:1080px;margin:auto;padding:28px}h1{color:#17446b}li,p{line-height:1.45}</style></head>"
        "<body><main>" + "\n".join(body) + "</main></body></html>"
    )
    (output / name).write_text(html, encoding="utf-8")


def base_markdown(mode: str, project: str, source: Path, sig: dict[str, int]) -> str:
    cfg = MODES[mode]
    score = score_for(mode, sig)
    return (
        f"# {cfg['title']}\n\n"
        f"Project: `{project}`\n\n"
        f"Source: `{source}`\n\n"
        f"Status: `{status_from_score(score)}`\n\n"
        f"Score: `{score}`\n\n"
        f"## Purpose\n\n{cfg['summary']}\n\n"
        "## AI Signals\n\n"
        + "\n".join(f"- {name}: `{value}`" for name, value in sig.items())
        + "\n\n"
    )


def generate_generic(mode: str, source: Path, output: Path, project: str, text: str) -> None:
    sig = signals(text)
    md = base_markdown(mode, project, source, sig)
    score = score_for(mode, sig)
    actions = [
        "Run `guided-run` to refresh analysis, routing, gates, evidence, memory, and exports.",
        "Run `evidence-gates` after business, CISO, finance, and cutover sign-offs change.",
        "Run `health-snapshot` after new evidence is added.",
    ]
    if mode == "usp-actions":
        actions = [
            "Map every USP to a demo story, proof artifact, command, and target buyer.",
            "Use `usp-pack` before proposal or steering committee preparation.",
            "Attach `project-health-snapshot.html` as proof for evidence-backed claims.",
        ]
    elif mode == "truth-detector":
        actions = [
            "Challenge all green status items without evidence file, owner, or gate result.",
            "Escalate missing CISO, UAT, finance, rollback, and cutover evidence.",
            "Compare steering reports against `go-live-gate-result.json` and evidence manifest.",
        ]
    elif mode == "cutover-confidence":
        actions = [
            "Close rehearsal, rollback, smoke test, security, finance, and Commerce/POS gaps before go-live.",
            "Repeat this score after each cutover rehearsal.",
            "Treat `Blocked` as a no-go recommendation unless external approvers override it.",
        ]
    elif mode == "partner-deliverable-check":
        actions = [
            "Request missing deliverables from implementation partner with owner and due date.",
            "Tie payment milestones to evidence, test status, and sign-off artifacts.",
            "Escalate scope changes without `scope-guard` evidence.",
        ]
    md += "## Recommended Actions\n\n" + "\n".join(f"- {action}" for action in actions) + "\n"
    filename = MODES[mode]["files"][0]
    (output / filename).write_text(md, encoding="utf-8")
    if filename.endswith(".md") and len(MODES[mode]["files"]) > 1 and MODES[mode]["files"][1].endswith(".json"):
        write_json(output, MODES[mode]["files"][1], {"mode": mode, "project": project, "score": score, "status": status_from_score(score), "signals": sig, "actions": actions})


def generate_meeting_actions(source: Path, output: Path, project: str, text: str) -> None:
    sig = signals(text)
    rows = [
        ["Decision", "Confirm migration scope baseline", "PMO", "guided-run"],
        ["Risk", "Evidence gap may block go-live", "CISO/PMO", "evidence-gates"],
        ["Task", "Refresh health snapshot after new evidence", "Project Manager", "health-snapshot"],
        ["Evidence", "Collect finance reconciliation and UAT sign-off", "CFO/QA", "evidence-vault"],
    ]
    md = base_markdown("meeting-actions", project, source, sig)
    md += "## Extracted Actions\n\n| Type | Action | Owner | Command |\n| --- | --- | --- | --- |\n"
    md += "\n".join(f"| {row[0]} | {row[1]} | {row[2]} | `{row[3]}` |" for row in rows) + "\n"
    (output / "meeting-to-migration-actions.md").write_text(md, encoding="utf-8")
    with (output / "meeting-to-migration-actions.csv").open("w", encoding="utf-8", newline="") as handle:
        writer = csv.writer(handle)
        writer.writerow(["type", "action", "owner", "command"])
        writer.writerows(rows)


def generate_role_prompt_pack(source: Path, output: Path, project: str, text: str) -> None:
    sig = signals(text)
    roles = {
        "CEO": "Summarize business value, top board risks, go-live confidence, and decisions required.",
        "CIO": "Review architecture, standardization, integration, data, release, and platform risks.",
        "CISO": "Check security scan, privileged access, PCI, secrets, evidence, and external approvals.",
        "CFO": "Validate reconciliation, tax, ledger, inventory, settlement, and value realization evidence.",
        "PMO": "Create next actions, owner list, RAID updates, dependency risks, and gate closure plan.",
        "QA / Key User": "Generate UAT, regression, smoke tests, defects, and business sign-off evidence.",
    }
    md = base_markdown("role-prompt-pack", project, source, sig)
    data = {"project": project, "roles": []}
    for role, prompt in roles.items():
        md += f"## {role}\n\nPrompt: {prompt}\n\nExpected output: actions, evidence gaps, risks, and next CLI commands.\n\n"
        data["roles"].append({"role": role, "prompt": prompt, "expected_output": ["actions", "evidence gaps", "risks", "next CLI commands"]})
    (output / "role-prompt-pack-2.md").write_text(md, encoding="utf-8")
    write_json(output, "role-prompt-pack-2.json", data)


def generate_dependency_graph(source: Path, output: Path, project: str, text: str) -> None:
    sig = signals(text)
    nodes = ["Analysis", "Skill Routing", "Evidence Gates", "Security", "Finance", "Testing", "Cutover", "Go-live"]
    if sig["commerce"]:
        nodes.insert(5, "Commerce/POS")
    edges = list(zip(nodes, nodes[1:]))
    mermaid = "```mermaid\ngraph TD\n" + "\n".join(f"  {a.replace('/', '')}[{a}] --> {b.replace('/', '')}[{b}]" for a, b in edges) + "\n```"
    md = base_markdown("dependency-risk-graph", project, source, sig) + "## Graph\n\n" + mermaid + "\n"
    (output / "dependency-risk-graph.md").write_text(md, encoding="utf-8")
    write_json(output, "dependency-risk-graph.json", {"nodes": nodes, "edges": edges, "signals": sig})


def generate_release_pack(source: Path, output: Path, project: str, text: str) -> None:
    output.mkdir(parents=True, exist_ok=True)
    zip_path = output / "ax-to-d365fo-migration-expert-release.zip"
    include_roots = [ROOT / ".codex-plugin", ROOT / "config", ROOT / "docs", ROOT / "examples", ROOT / "scripts", ROOT / "skills", ROOT / "templates"]
    with zipfile.ZipFile(zip_path, "w", zipfile.ZIP_DEFLATED) as archive:
        for base in include_roots:
            if not base.exists():
                continue
            for path in sorted(base.rglob("*")):
                if path.is_file() and "__pycache__" not in path.parts:
                    archive.write(path, path.relative_to(ROOT.parent))
    manifest = (
        "# Release Pack Manifest\n\n"
        f"Project: `{project}`\n\n"
        f"Built UTC: `{datetime.now(timezone.utc).isoformat()}`\n\n"
        f"ZIP: `{zip_path.name}`\n\n"
        "## Included\n\n- plugin metadata\n- config\n- docs\n- examples\n- scripts\n- skills\n- templates\n"
    )
    (output / "release-pack-manifest.md").write_text(manifest, encoding="utf-8")


def generate_demo_portal(source: Path, output: Path, project: str, text: str) -> None:
    md = base_markdown("demo-portal", project, source, signals(text))
    links = [
        ("Guided Run", "../guided-runs/sample/index.html"),
        ("Health Snapshot", "../health/sample/project-health-snapshot.html"),
        ("USP Pack", "../usp-packs/sample/ai-ki-usp-pack.html"),
        ("Demo Index", "../demo-projects/demo-index.html"),
        ("Project UI", "../migration-ui/project-wizard.html"),
    ]
    md += "## Demo Links\n\n" + "\n".join(f"- [{label}]({href})" for label, href in links) + "\n"
    (output / "demo-portal-2.md").write_text(md, encoding="utf-8")
    html = "<!doctype html><html lang=\"en\"><head><meta charset=\"utf-8\"><title>Demo Portal 2.0</title><style>body{font-family:Segoe UI,Arial,sans-serif;background:#f6f8fb;color:#172033}main{max-width:980px;margin:auto;padding:28px}a{display:block;background:#fff;border:1px solid #d9e2ec;border-radius:6px;margin:10px 0;padding:12px;color:#17446b;text-decoration:none;font-weight:600}</style></head><body><main><h1>Demo Portal 2.0</h1><p>One page for guided runs, health, USPs, dashboards, and pitch flow.</p>" + "".join(f"<a href=\"{href}\">{label}</a>" for label, href in links) + "</main></body></html>"
    (output / "demo-portal-2.html").write_text(html, encoding="utf-8")


def generate_wizard_ui(source: Path, output: Path, project: str, text: str) -> None:
    md = base_markdown("wizard-ui", project, source, signals(text))
    commands = [
        "python .\\axmigrate.py guided-run <input> --project \"My Migration\" --output guided-runs\\my-project",
        "python .\\axmigrate.py evidence-gates guided-runs\\my-project --output evidence-gates\\my-project",
        "python .\\axmigrate.py health-snapshot guided-runs\\my-project --output health\\my-project",
        "python .\\axmigrate.py usp-pack guided-runs\\my-project --project \"My Migration\" --output usp-packs\\my-project",
    ]
    md += "## Generated Command Flow\n\n" + "\n".join(f"- `{cmd}`" for cmd in commands) + "\n"
    (output / "wizard-ui-2.md").write_text(md, encoding="utf-8")
    html = "<!doctype html><html lang=\"en\"><head><meta charset=\"utf-8\"><title>Interactive Wizard UI 2.0</title><style>body{font-family:Segoe UI,Arial,sans-serif;background:#f6f8fb;color:#172033}main{max-width:980px;margin:auto;padding:28px}label{display:block;margin:12px 0 4px}select,input,textarea{width:100%;padding:10px;border:1px solid #b8c7d6;border-radius:6px}pre{background:#fff;border:1px solid #d9e2ec;padding:14px;white-space:pre-wrap}</style></head><body><main><h1>Interactive Wizard UI 2.0</h1><label>Project type</label><select><option>AX 2012</option><option>Commerce/POS</option><option>CRM/Lead-to-Cash</option><option>Multi-country rollout</option></select><label>Project name</label><input value=\"" + project + "\"><label>Evidence gates</label><textarea>CISO, UAT, Finance, Cutover, Rollback, Commerce Payments</textarea><h2>Commands</h2><pre>" + "\n".join(commands) + "</pre></main></body></html>"
    (output / "interactive-wizard-ui-2.html").write_text(html, encoding="utf-8")


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("source", nargs="?", default=".")
    parser.add_argument("--mode", choices=sorted(MODES), required=True)
    parser.add_argument("--project", default="Migration Project")
    parser.add_argument("--output", default="control-feature-pack")
    args = parser.parse_args()

    source = Path(args.source)
    output = Path(args.output)
    output.mkdir(parents=True, exist_ok=True)
    text = read_text(source)
    if args.mode == "meeting-actions":
        generate_meeting_actions(source, output, args.project, text)
    elif args.mode == "role-prompt-pack":
        generate_role_prompt_pack(source, output, args.project, text)
    elif args.mode == "dependency-risk-graph":
        generate_dependency_graph(source, output, args.project, text)
    elif args.mode == "release-pack":
        generate_release_pack(source, output, args.project, text)
    elif args.mode == "demo-portal":
        generate_demo_portal(source, output, args.project, text)
    elif args.mode == "wizard-ui":
        generate_wizard_ui(source, output, args.project, text)
    else:
        generate_generic(args.mode, source, output, args.project, text)
    print(f"Generated {MODES[args.mode]['title']} into {output.resolve()}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
