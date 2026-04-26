# Architecture

## Overview

The repository is organized as a repo-local Codex plugin plus supporting GitHub and distribution files.

```text
repo root
  .agents/plugins/marketplace.json
  plugins/ax-to-d365fo-migration-expert
    .codex-plugin/plugin.json
    skills/
    scripts/
    templates/
    config/
    docs/
    examples/
    tests/
```

## Main Components

| Component | Purpose |
| --- | --- |
| Skill | Guides Codex behavior for AX to D365FO migration work. |
| Analyzer | Reads inventory/code inputs and generates migration reports. |
| Templates | Blank project artifacts for delivery teams. |
| Config | Cost model, rules, integration settings, and knowledge base. |
| Connectors | Optional scripts for AX SQL, Azure DevOps, LCS, D365FO, and telemetry. |
| Exporters | Produce Excel and PowerPoint outputs from analysis folders. |
| Persona and stakeholder generators | Produce CEO, CIO, CISO, PMO, team, CFO, COO, data, integration, QA, legal, vendor, support, and partner packs. |
| Commerce generators | Produce Customer & Commerce Experience artifacts for CXP, CRM, Lead Management, Commerce HQ, CSU, POS, POS Offline, Payments, Store Ops, Omnichannel, Loyalty, Pricing, Marketplace, Call Center, and Analytics. |
| Solo/Master-Orchestrator generators | Produce single-user project operating artifacts, evidence gates, master routing, daily command sheets, tests, sign-off, audit binder, hypercare, and benefits tracking. |
| Validator | Runs repository health checks. |

## Data Flow

```text
AX exports / code / telemetry
  -> analyzer / connector scripts
  -> normalized inventory
  -> AI migration reports
  -> dashboard / Excel / PowerPoint / ADO CSV
  -> persona / stakeholder / solo / commerce generators
  -> gates / runbooks / test packs / executive and team artifacts
```

## Domain Model

| Domain | What it controls |
| --- | --- |
| Legacy AX evidence | AX 4.0, AX 2009, AX 2012 inventories, X++/XPO/AOT text, modelstore-style exports, telemetry, reports, integrations, roles, ISVs, and modules. |
| Migration analysis | Scope reduction, standard fit, complexity, effort, risks, dependencies, data entity candidates, cost, quality gates, backlog, and dashboards. |
| Role operating model | Persona-specific decision and execution artifacts for executives, architecture, security, PMO, team, finance, operations, QA, legal, vendors, support, and partners. |
| Customer & Commerce Experience | CXP, CRM/Dataverse, lead-to-cash, customer master, D365 Commerce, CSU, POS, POS offline, payments, store operations, loyalty, pricing, omnichannel, marketplace, call center, and analytics. |
| Solo/Master autonomy | A single user can initialize, run, govern, test, gate, communicate, sign off, and track a migration using generated artifacts and master-orchestrator routing. |

## Design Principles

- Keep external credentials in environment variables.
- Prefer dry-run before calling external systems.
- Keep analyzer inputs schema-tolerant.
- Keep recommendations evidence-rated.
- Generate delivery artifacts that can be reviewed by humans.

## Key Scripts

| Script | Role |
| --- | --- |
| `migration_cli.py` | Unified command entrypoint. |
| `analyze_ax_inventory.py` | Main analyzer and report generator. |
| `create_migration_workspace.py` | Copies templates into a project workspace. |
| `export_analysis.py` | Exports analysis to XLSX/PPTX. |
| `validate_plugin.py` | Runs validation checks. |
| `connect_ax_sql.py` | Direct AX SQL extraction via ODBC. |
| `push_azure_devops.py` | Creates Azure DevOps work items from CSV. |
| `generate_commerce_pack.py` | Generates the full Commerce/CXP/CRM/POS master pack. |
| `generate_commerce_readiness.py` | Generates Commerce readiness scores in Markdown, JSON, and CSV. |
| `generate_commerce_cutover.py` | Generates Commerce cutover runbooks, store smoke tests, and go-live gates. |
| `generate_solo_artifacts.py` | Generates Solo/Master-Orchestrator artifacts, gates, tests, status, and sign-off packs. |
| `run_solo_migration.py` | Runs the solo migration orchestration flow from inputs into a project operating folder. |
