# AX to D365FO Migration Expert

[![Validate Plugin](https://github.com/OWNER/REPO/actions/workflows/validate.yml/badge.svg)](https://github.com/OWNER/REPO/actions/workflows/validate.yml)
![Version](https://img.shields.io/badge/version-0.2.0-blue)
![License](https://img.shields.io/badge/license-MIT-green)

Enterprise AI migration command center for Microsoft Dynamics AX 4.0, AX 2009, and AX 2012 migrations to Dynamics 365 Finance & Operations.

The repository contains a Codex plugin that analyzes AX inventories, X++/XPO/AOT text exports, usage telemetry, modelstore-style extracts, and migration planning inputs. It generates migration scope recommendations, risk reports, dashboards, work items, executive artifacts, and project templates.

## What It Does

- Reduces migration scope by identifying what to migrate, replace, configure, archive, or retire.
- Analyzes CSV, JSON, X++ source, XPO, and AOT text exports.
- Produces 46 analyzer outputs including dashboards, risk heatmaps, effort estimates, cost model, ADRs, Azure DevOps CSV, knowledge graph JSON, CEO/CIO/CISO/PM/team persona packs, RAID, RACI, weekly status, and steering committee artifacts.
- Generates 211 migration project templates.
- Includes 76 Codex skills: end-to-end migration expert plus executive, architecture, security, PMO, delivery, finance, operations, data, integration, QA, legal, vendor, support, partner sales, regulatory, industry, connector, automation, master-orchestrator, solo-operator, key-user/tester, and Commerce/CXP/CRM/POS skills.
- Exports analysis to Excel and PowerPoint.
- Provides connector scaffolding for AX SQL, Azure DevOps, LCS, D365FO metadata/OData, and usage telemetry.
- Adds a Solo/Master-Orchestrator operating model so a single plugin user can generate project control, evidence, gates, daily actions, test plans, sign-off, audit binder, hypercare, and benefits tracking.
- Adds a dedicated Customer & Commerce Experience domain for CXP, CRM/Dataverse, Lead Management, D365 Commerce, CSU, POS, POS Offline, Payments, Store Operations, Omnichannel, Loyalty, Pricing, Assortment, Marketplace, Call Center, Analytics, and Store Training.

## Quick Start

Validate the plugin:

```powershell
python .\axmigrate.py validate
```

Analyze the sample inventory:

```powershell
python .\axmigrate.py analyze `
  plugins\ax-to-d365fo-migration-expert\examples\sample-ax-inventory.csv `
  --output migration-analysis\sample
```

Open the generated dashboard:

```text
migration-analysis\sample\dashboard.html
```

Create a migration workspace:

```powershell
python .\axmigrate.py init "Contoso AX Migration"
```

Check local environment:

```powershell
python .\axmigrate.py doctor
```

Generate persona packs with readiness scores and Office exports:

```powershell
python .\axmigrate.py persona-pack migration-analysis\sample --persona all --office --output persona-packs\sample
```

Generate questionnaires, factory, cutover, hypercare, and partner packs:

```powershell
python .\axmigrate.py questionnaire --persona all --output migration-questionnaires\sample
```

Generate extended stakeholder packs:

```powershell
python .\axmigrate.py stakeholder-pack migration-analysis\sample --stakeholder all --output stakeholder-packs\sample
```

Export GitHub issue Markdown:

```powershell
python .\axmigrate.py github-issues migration-analysis\sample --output github-issues\sample
```

Generate Commerce/CXP/CRM/POS packs:

```powershell
python .\axmigrate.py commerce-pack migration-analysis\sample --output commerce-packs\sample
python .\axmigrate.py commerce-readiness migration-analysis\sample --output commerce-readiness\sample
python .\axmigrate.py commerce-cutover migration-analysis\sample --output commerce-cutover\sample
python .\axmigrate.py commerce-offline-check migration-analysis\sample --output commerce-offline\sample
python .\axmigrate.py commerce-crm-pack migration-analysis\sample --output commerce-crm\sample
python .\axmigrate.py commerce-store-pack migration-analysis\sample --output commerce-store\sample
python .\axmigrate.py commerce-payments-pack migration-analysis\sample --output commerce-payments\sample
python .\axmigrate.py commerce-omnichannel-pack migration-analysis\sample --output commerce-omnichannel\sample
```

Run the Solo/Master-Orchestrator operating system:

```powershell
python .\axmigrate.py solo-init "Contoso AX Migration" --output solo-migration
python .\axmigrate.py solo-run --project "Contoso AX Migration" --input plugins\ax-to-d365fo-migration-expert\examples\sample-ax-inventory.csv --output solo-migration
python .\axmigrate.py solo-orchestrate solo-migration\contoso-ax-migration --output master-orchestration\contoso
python .\axmigrate.py solo-status solo-migration\contoso-ax-migration
python .\axmigrate.py solo-test-plan solo-migration\contoso-ax-migration
python .\axmigrate.py solo-signoff solo-migration\contoso-ax-migration
```

## Repository Map

- `plugins/ax-to-d365fo-migration-expert/` - Codex plugin.
- `plugins/ax-to-d365fo-migration-expert/scripts/` - CLI, analyzer, exporters, connectors, validators.
- `plugins/ax-to-d365fo-migration-expert/templates/` - migration project templates.
- `plugins/ax-to-d365fo-migration-expert/config/` - cost model, rule maps, integrations, knowledge base.
- `plugins/ax-to-d365fo-migration-expert/docs/` - plugin-specific documentation.
- `docs/` - repository-level architecture, configuration, connector, examples, and FAQ docs.
- `.github/` - GitHub Actions and issue/PR templates.

## Current Capability Snapshot

| Area | Current state |
| --- | --- |
| Skills | 76 Codex skills across migration, roles, testing, solo operation, orchestration, connectors, industry/regulatory, and Commerce/CXP/CRM/POS. |
| Templates | 211 templates for assessment, delivery, governance, testing, cutover, hypercare, role packs, solo operation, and Commerce. |
| Scripts | 31 Python scripts including CLI, analyzer, exporters, connectors, validators, Commerce generators, and Solo/Master generators. |
| Configs | 15 JSON configs including cost model, risks, D365FO knowledge, integrations, Commerce readiness/gates, POS offline, PCI, and CRM lead management maps. |
| Analyzer outputs | 46 generated outputs from inventory analysis, including technical, executive, governance, role, dashboard, graph, and backlog artifacts. |
| AI/KI features | 301 documented feature items, including the 260-feature autonomy expansion and Commerce features 261-300. |

## Documentation

- [Docs index](docs/README.md)
- [Architecture](docs/architecture.md)
- [Configuration](docs/configuration.md)
- [Connectors](docs/connectors.md)
- [Examples](docs/examples.md)
- [FAQ](docs/faq.md)
- [Command reference](docs/command-reference.md)
- [Commerce/CXP/CRM/POS](docs/commerce-cxp-crm-pos.md)
- [Solo and Master Orchestrator](docs/solo-master-orchestrator.md)
- [Plugin usage](plugins/ax-to-d365fo-migration-expert/docs/installation-and-usage.md)
- [Input format](plugins/ax-to-d365fo-migration-expert/docs/input-inventory-format.md)
- [AI feature list](plugins/ax-to-d365fo-migration-expert/docs/ai-usp-feature-list.md)
- [Role-based AI-KI USP pack](plugins/ax-to-d365fo-migration-expert/docs/role-based-ai-ki-usp-pack.md)
- [Roadmap](ROADMAP.md)
- [Disclaimer](DISCLAIMER.md)

## Distribution

See [DISTRIBUTION.md](DISTRIBUTION.md) for packaging and install instructions.

## Validation

The main validation command runs JSON checks, unit tests, analyzer smoke tests, template generation checks, and placeholder checks:

```powershell
python .\axmigrate.py validate
```

## Security

Do not commit customer data, credentials, telemetry exports, SQL connection strings, PATs, bearer tokens, or generated analysis outputs. See [SECURITY.md](SECURITY.md).
