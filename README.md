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
- Generates 264 migration project templates.
- Includes 92 Codex skills: end-to-end migration expert plus executive, architecture, security, PMO, delivery, finance, operations, data, integration, QA, legal, vendor, support, partner sales, regulatory, industry, connector, automation, master-orchestrator, solo-operator, key-user/tester, Commerce/CXP/CRM/POS, and autonomous governance/evidence intelligence skills.
- Exports analysis to Excel and PowerPoint.
- Provides connector scaffolding for AX SQL, Azure DevOps, LCS, D365FO metadata/OData, and usage telemetry.
- Adds a Solo/Master-Orchestrator operating model so a single plugin user can generate project control, evidence, gates, daily actions, test plans, sign-off, audit binder, hypercare, and benefits tracking.
- Adds a dedicated Customer & Commerce Experience domain for CXP, CRM/Dataverse, Lead Management, D365 Commerce, CSU, POS, POS Offline, Payments, Store Operations, Omnichannel, Loyalty, Pricing, Assortment, Marketplace, Call Center, Analytics, and Store Training.
- Adds an Autonomous Governance & Evidence Intelligence layer for contract/scope guard, stakeholder sentiment, evidence vault, cutover rehearsal, reconciliation judge, license/cost, ALM release, training readiness, ISV exit, country regulatory packs, archive strategy, hyperautomation, board risk, process twin, and meeting copilot.
- Adds productized onboarding with `wizard` command plans, `demo-projects`, sample dashboards, and stronger dashboard skill-routing/evidence signals.

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

Generate a guided command plan and demo dashboards:

```powershell
python .\axmigrate.py wizard --profile commerce --project "Contoso Retail Migration" --output migration-wizard\commerce
python .\axmigrate.py wizard --profile multi-country --project "Contoso Global Rollout" --output migration-wizard\multi-country
python .\axmigrate.py demo-projects --output demo-projects
```

Run the autonomous router, evidence gates, and Migration Intelligence Fabric:

```powershell
python .\axmigrate.py orchestrate migration-analysis\sample --output orchestration\sample
python .\axmigrate.py evidence-gates migration-analysis\sample --ciso-approval yes --cutover-rehearsal yes --finance-reconciliation yes --uat-signoff yes --rollback-plan yes --output evidence-gates\sample
python .\axmigrate.py intelligence-pack migration-analysis\sample --output intelligence-pack\sample
python .\axmigrate.py migration-memory migration-analysis\sample --output migration-memory\sample
python .\axmigrate.py benchmark migration-analysis\sample --output benchmark\sample
python .\axmigrate.py portfolio-control migration-analysis\sample --output portfolio-control\sample
python .\axmigrate.py scenario-lab migration-analysis\sample --output scenario-lab\sample
python .\axmigrate.py quality-audit migration-analysis\sample --output quality-audit\sample
python .\axmigrate.py war-game migration-analysis\sample --output war-game\sample
python .\axmigrate.py value-realization migration-analysis\sample --output value-realization\sample
python .\axmigrate.py memory-store migration-analysis\sample --project "Contoso AX Migration" --output migration-memory-store\sample
python .\axmigrate.py security-scan migration-analysis\sample --output security-scan\sample
python .\axmigrate.py project-ui --output migration-ui
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
| Skills | 112 Codex skills across migration, roles, testing, solo operation, orchestration, connectors, industry/regulatory, Commerce/CXP/CRM/POS, governance/evidence intelligence, and Migration Intelligence Fabric. |
| Templates | 325 templates for assessment, delivery, governance, testing, cutover, hypercare, role packs, solo operation, Commerce, evidence, rehearsal, reconciliation, ALM, training, archive, board risk, process twin, and intelligence fabric outputs. |
| Scripts | 75 Python scripts including CLI, analyzer, exporters, connectors, validators, Commerce generators, Solo/Master generators, governance generators, intelligence generators, documentation generator, wizard, evidence gates, router, memory store, security scanner, local UI, and demo project generator. |
| Configs | 35 JSON configs including cost model, risks, D365FO knowledge, integrations, Commerce readiness/gates, POS offline, PCI, CRM lead management, evidence, scope, reconciliation, license, ALM, training, country regulatory, process twin, benchmarking, portfolio, scenario, quality, integration resilience, security, and value rules. |
| Analyzer outputs | 46 generated outputs from inventory analysis, including technical, executive, governance, role, dashboard, graph, and backlog artifacts. |
| AI/KI features | 530 documented feature items, including solo autonomy, Commerce features, autonomous governance/evidence intelligence, wizard automation, evidence gates, Dashboard 2.0, stronger Office exports, strict validation, Migration Intelligence Fabric, memory store, evidence hashes, security scanning, local UI, and demo portal. |

## Documentation

- [Docs index](docs/README.md)
- [Architecture](docs/architecture.md)
- [Configuration](docs/configuration.md)
- [Connectors](docs/connectors.md)
- [Examples](docs/examples.md)
- [FAQ](docs/faq.md)
- [Command reference](docs/command-reference.md)
- [Skill handbook](docs/skill-handbook.md)
- [Migration operating handbook](docs/migration-operating-handbook.md)
- [Commerce/CXP/CRM/POS](docs/commerce-cxp-crm-pos.md)
- [Solo and Master Orchestrator](docs/solo-master-orchestrator.md)
- [Autonomous Governance & Evidence Intelligence](docs/autonomous-governance-evidence.md)
- [Migration Intelligence Fabric](docs/migration-intelligence-fabric.md)
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
