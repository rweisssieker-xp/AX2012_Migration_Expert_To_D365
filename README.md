# AX to D365FO Migration Expert

[![Validate Plugin](https://github.com/OWNER/REPO/actions/workflows/validate.yml/badge.svg)](https://github.com/OWNER/REPO/actions/workflows/validate.yml)
![Version](https://img.shields.io/badge/version-0.2.0-blue)
![License](https://img.shields.io/badge/license-MIT-green)

Enterprise AI migration command center for Microsoft Dynamics AX 4.0, AX 2009, and AX 2012 migrations to Dynamics 365 Finance & Operations.

The repository contains a Codex plugin that analyzes AX inventories, X++/XPO/AOT text exports, usage telemetry, modelstore-style extracts, and migration planning inputs. It generates migration scope recommendations, risk reports, dashboards, work items, executive artifacts, and project templates.

## What It Does

- Reduces migration scope by identifying what to migrate, replace, configure, archive, or retire.
- Analyzes CSV, JSON, X++ source, XPO, and AOT text exports.
- Produces 31 analyzer outputs including dashboards, risk heatmaps, effort estimates, cost model, ADRs, Azure DevOps CSV, and knowledge graph JSON.
- Generates 52 migration project templates.
- Exports analysis to Excel and PowerPoint.
- Provides connector scaffolding for AX SQL, Azure DevOps, LCS, D365FO metadata/OData, and usage telemetry.

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

## Repository Map

- `plugins/ax-to-d365fo-migration-expert/` - Codex plugin.
- `plugins/ax-to-d365fo-migration-expert/scripts/` - CLI, analyzer, exporters, connectors, validators.
- `plugins/ax-to-d365fo-migration-expert/templates/` - migration project templates.
- `plugins/ax-to-d365fo-migration-expert/config/` - cost model, rule maps, integrations, knowledge base.
- `plugins/ax-to-d365fo-migration-expert/docs/` - plugin-specific documentation.
- `docs/` - repository-level architecture, configuration, connector, examples, and FAQ docs.
- `.github/` - GitHub Actions and issue/PR templates.

## Documentation

- [Docs index](docs/README.md)
- [Architecture](docs/architecture.md)
- [Configuration](docs/configuration.md)
- [Connectors](docs/connectors.md)
- [Examples](docs/examples.md)
- [FAQ](docs/faq.md)
- [Plugin usage](plugins/ax-to-d365fo-migration-expert/docs/installation-and-usage.md)
- [Input format](plugins/ax-to-d365fo-migration-expert/docs/input-inventory-format.md)
- [AI feature list](plugins/ax-to-d365fo-migration-expert/docs/ai-usp-feature-list.md)
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
