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
| Validator | Runs repository health checks. |

## Data Flow

```text
AX exports / code / telemetry
  -> analyzer / connector scripts
  -> normalized inventory
  -> AI migration reports
  -> dashboard / Excel / PowerPoint / ADO CSV
```

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

