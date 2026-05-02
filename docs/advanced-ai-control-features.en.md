# Advanced AI Control Features

This document describes the 12 advanced AI control features added on top of the guided run, health snapshot, and USP pack. Each feature has a direct CLI command, generated artifacts, and validator coverage.

## Commands

| Feature | Command | Main Outputs | Purpose |
| --- | --- | --- | --- |
| USP-to-Action Engine | `usp-actions` | `usp-to-action-map.md`, `usp-to-action-map.json` | Converts USPs into concrete skills, commands, proof artifacts, and demo narrative. |
| Project Truth Detector | `truth-detector` | `project-truth-detector.md`, `project-truth-detector.json` | Compares claimed project status with available evidence, gates, tests, and artifacts. |
| Cutover Confidence Engine | `cutover-confidence` | `cutover-confidence-score.md`, `cutover-confidence-score.json` | Scores go-live confidence from rehearsal, rollback, smoke tests, finance, security, and Commerce/POS signals. |
| AI Meeting-to-Migration Actions | `meeting-actions` | `meeting-to-migration-actions.md`, `meeting-to-migration-actions.csv` | Converts notes into decisions, risks, tasks, evidence gaps, owners, and next commands. |
| AI Proposal / Sales Pack Generator | `proposal-pack` | `proposal-sales-pack.md`, `proposal-sales-pack.html` | Creates a sales-ready migration narrative from USPs, demos, health, and analysis signals. |
| AI Role Prompt Packs 2.0 | `role-prompt-pack` | `role-prompt-pack-2.md`, `role-prompt-pack-2.json` | Generates role-specific prompts for CEO, CIO, CISO, CFO, PMO, QA, and key users. |
| Evidence Freshness Monitor | `evidence-freshness` | `evidence-freshness-monitor.md`, `evidence-freshness-monitor.json` | Classifies evidence as current, aging, stale, or missing based on project signals. |
| Dependency Risk Graph | `dependency-risk-graph` | `dependency-risk-graph.md`, `dependency-risk-graph.json` | Visualizes workstream, gate, test, integration, and cutover dependencies. |
| Partner Deliverable Checker | `partner-deliverable-check` | `partner-deliverable-check.md`, `partner-deliverable-check.json` | Checks partner deliverables, scope control, evidence, milestones, and sign-offs. |
| Release ZIP Builder | `release-pack` | `release-pack-manifest.md`, `ax-to-d365fo-migration-expert-release.zip` | Builds a distributable plugin ZIP and release manifest. |
| Demo Portal 2.0 | `demo-portal` | `demo-portal-2.md`, `demo-portal-2.html` | Links guided runs, health snapshots, USP packs, demo dashboards, and pitch story. |
| Interactive Local Wizard UI 2.0 | `wizard-ui` | `wizard-ui-2.md`, `interactive-wizard-ui-2.html` | Provides a local HTML command builder for project type, gates, evidence, packs, and commands. |

## Example

```powershell
python .\axmigrate.py truth-detector guided-runs\sample --project "Contoso AX Migration" --output truth\sample
python .\axmigrate.py cutover-confidence guided-runs\sample --project "Contoso AX Migration" --output cutover-confidence\sample
python .\axmigrate.py demo-portal guided-runs\sample --project "Contoso AX Migration" --output demo-portal\sample
```

## Operating Model

These commands are designed to make the plugin behave less like a report generator and more like a migration control system. They reuse local project evidence and generated artifacts to produce stronger decision support for leadership, PMO, security, finance, delivery, testing, partners, and sales.
