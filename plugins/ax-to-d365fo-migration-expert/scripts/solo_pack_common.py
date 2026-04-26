#!/usr/bin/env python3
"""Shared Solo/Master-Orchestrator artifact generation helpers."""

from __future__ import annotations

import csv
import json
import re
import shutil
import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SCRIPTS = ROOT / "scripts"
TEMPLATES = ROOT / "templates"


MODE_OUTPUTS = {
    "evidence": ["evidence-completeness-matrix.md", "missing-stakeholder-register.md"],
    "status": ["migration-health-score.md", "go-live-confidence-dashboard.md", "ai-next-action-board.md"],
    "gates": ["self-approval-gate-register.md", "external-approval-pack.md", "blocked-decisions-register.md"],
    "daily": ["daily-migration-command-sheet.md", "next-best-actions.md"],
    "war-room": ["war-room-command-board.md", "commerce-cutover-runbook.md", "cutover-smoke-test-pack.md"],
    "hypercare": ["hypercare-daily-pack.md", "commerce-hypercare-pack.md", "bau-transition-checklist.md"],
    "audit-binder": ["audit-binder-index.md", "confidence-ledger.md", "decision-memory.md"],
    "benefits": ["benefits-realization-tracker.md", "roi-benefits-realization.md", "tco-model.md"],
    "orchestrate": ["master-orchestration-plan.md", "skill-routing-map.md", "role-to-skill-matrix.md", "phase-to-skill-matrix.md", "evidence-to-skill-matrix.md"],
    "brain": ["ai-migration-brain.md", "role-swarm-plan.md", "migration-brain.json"],
    "next": ["next-best-actions.md", "master-action-queue.csv"],
    "simulate": ["decision-impact-simulator.md"],
    "scope-defense": ["scope-defense-pack.md", "anti-scope-creep-guard.md"],
    "waste-hunter": ["waste-hunter-report.md"],
    "predict": ["go-live-probability-score.md", "hypercare-load-prediction.md"],
    "translate": ["stakeholder-translation-pack.md"],
    "drift": ["project-drift-detector.md"],
    "communicate": ["meeting-copilot-pack.md", "stakeholder-translation-pack.md"],
    "test-plan": ["uat-test-execution-pack.md", "business-process-test-cases.md", "regression-test-suite.md", "test-evidence-matrix.md", "cutover-smoke-test-pack.md"],
    "test-status": ["defect-retest-tracker.md", "test-evidence-matrix.md", "migration-health-score.md"],
    "signoff": ["business-signoff-pack.md", "process-owner-validation-pack.md", "external-approval-pack.md"],
}


PHASES = ["Discover", "Reduce", "Decide", "Design", "Build", "Validate", "Cutover", "Hypercare", "BAU", "Benefits"]
ROLES = ["CEO", "CFO", "COO", "CIO", "CISO", "PMO", "Data", "Integration", "QA", "Key User", "Legal", "Support", "Commerce", "POS", "CRM"]


def normalize_project_name(value: str) -> str:
    cleaned = "".join(ch.lower() if ch.isalnum() else "-" for ch in value.strip())
    parts = [part for part in cleaned.split("-") if part]
    return "-".join(parts) or "migration-project"


def read_text_tree(path: Path) -> str:
    parts = []
    if path.exists():
        for item in sorted(path.rglob("*")):
            if item.is_file() and item.suffix.lower() in {".md", ".json", ".csv", ".xpp", ".xpo", ".txt"}:
                parts.append(item.read_text(encoding="utf-8", errors="ignore"))
    return "\n".join(parts)


def health_scores(text: str) -> dict[str, int]:
    lower = text.lower()
    scores = {}
    for role in ROLES:
        keyword = role.lower().replace(" ", "-")
        hits = lower.count(role.lower()) + lower.count(keyword)
        risks = len(re.findall(r"\b(blocked|critical|missing|risk|external approval|security|legal|cutover)\b", lower))
        scores[role] = max(20, min(100, 55 + hits * 7 - min(risks, 35)))
    return scores


def markdown_for(mode: str, source: Path, extra: str = "") -> str:
    text = read_text_tree(source)
    scores = health_scores(text)
    rows = "\n".join(f"| {role} | {score} | {'Ready' if score >= 75 else 'Needs control' if score >= 50 else 'Blocked'} |" for role, score in scores.items())
    phases = "\n".join(f"| {phase} | Validate evidence, decisions, gates, and next actions | Master Orchestrator |" for phase in PHASES)
    return f"""# {mode.replace('-', ' ').title()}

## Migration Health

| Role / Domain | Score | Status |
| --- | --- | --- |
{rows}

## Phase Control

| Phase | Required Control | Owner |
| --- | --- | --- |
{phases}

## Next Best Actions

- Close missing evidence before gate approval.
- Route blockers to the responsible specialist skill.
- Mark Legal, CISO, business, payment, PCI, and go-live approvals as external when required.
- Keep decisions, evidence, risks, actions, and owners traceable.

## Context

{extra or 'Generated from the current solo migration project or analysis folder.'}
"""


def copy_or_generate(name: str, destination: Path, source: Path, mode: str) -> None:
    template = TEMPLATES / name
    if template.exists() and name not in {"migration-brain.json", "master-action-queue.csv"}:
        body = template.read_text(encoding="utf-8")
        body += "\n\n## Generated Solo Context\n\n" + markdown_for(mode, source)
        destination.write_text(body, encoding="utf-8")
    elif name.endswith(".json"):
        payload = {"mode": mode, "scores": health_scores(read_text_tree(source)), "phases": PHASES, "roles": ROLES}
        destination.write_text(json.dumps(payload, indent=2), encoding="utf-8")
    elif name.endswith(".csv"):
        with destination.open("w", encoding="utf-8", newline="") as handle:
            writer = csv.writer(handle)
            writer.writerow(["Priority", "Role", "Phase", "Action", "Output"])
            for idx, role in enumerate(ROLES[:10], start=1):
                writer.writerow([idx, role, PHASES[idx % len(PHASES)], "Close highest-risk evidence gap", mode])
    else:
        destination.write_text(markdown_for(mode, source), encoding="utf-8")


def generate_mode(source: Path, output: Path, mode: str, extra: str = "") -> Path:
    output.mkdir(parents=True, exist_ok=True)
    files = MODE_OUTPUTS[mode]
    for name in files:
        copy_or_generate(name, output / name, source, mode)
    (output / f"{mode}-summary.md").write_text(markdown_for(mode, source, extra), encoding="utf-8")
    return output


def create_solo_project(project: str, output: Path) -> Path:
    project_dir = output / normalize_project_name(project)
    project_dir.mkdir(parents=True, exist_ok=True)
    for folder in ["inputs", "analysis", "persona-packs", "stakeholder-packs", "questionnaires", "github-issues", "solo-evidence", "solo-gates", "solo-status", "runbooks", "war-room", "hypercare", "audit-binder", "benefits"]:
        (project_dir / folder).mkdir(parents=True, exist_ok=True)
    generate_mode(project_dir, project_dir / "solo-status", "status", "Initial solo project status.")
    generate_mode(project_dir, project_dir / "solo-evidence", "evidence", "Initial evidence checklist.")
    generate_mode(project_dir, project_dir / "solo-gates", "gates", "Initial self-approval and external approval gates.")
    (project_dir / "README.md").write_text(markdown_for("solo project charter", project_dir, f"Project: {project}"), encoding="utf-8")
    return project_dir


def run_script(script: str, args: list[str]) -> None:
    result = subprocess.run([sys.executable, str(SCRIPTS / script), *args], text=True, capture_output=True)
    if result.returncode:
        print(result.stdout)
        print(result.stderr)
        raise SystemExit(result.returncode)


def run_solo(project: str, inputs: list[str], output: Path) -> Path:
    project_dir = create_solo_project(project, output)
    analysis = project_dir / "analysis"
    run_script("analyze_ax_inventory.py", [*inputs, "--output", str(analysis)])
    run_script("generate_persona_pack.py", [str(analysis), "--persona", "all", "--output", str(project_dir / "persona-packs")])
    run_script("generate_stakeholder_pack.py", [str(analysis), "--stakeholder", "all", "--output", str(project_dir / "stakeholder-packs")])
    run_script("create_questionnaire_pack.py", ["--persona", "all", "--output", str(project_dir / "questionnaires")])
    run_script("export_github_issues.py", [str(analysis), "--output", str(project_dir / "github-issues")])
    run_script("generate_commerce_pack.py", [str(analysis), "--output", str(project_dir / "commerce-packs")])
    for mode, folder in [
        ("evidence", "solo-evidence"),
        ("status", "solo-status"),
        ("gates", "solo-gates"),
        ("daily", "daily"),
        ("orchestrate", "master-orchestration"),
        ("brain", "migration-brain"),
        ("war-room", "war-room"),
        ("hypercare", "hypercare"),
        ("audit-binder", "audit-binder"),
        ("benefits", "benefits"),
        ("test-plan", "test-plan"),
        ("signoff", "signoff"),
    ]:
        generate_mode(project_dir, project_dir / folder, mode)
    return project_dir
