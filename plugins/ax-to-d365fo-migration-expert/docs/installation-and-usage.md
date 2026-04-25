# Installation and Usage

## Local Plugin

The plugin is repo-local under:

`plugins/ax-to-d365fo-migration-expert`

The marketplace entry is:

`.agents/plugins/marketplace.json`

## Create a Project Workspace

```powershell
python plugins\ax-to-d365fo-migration-expert\scripts\create_migration_workspace.py "Contoso AX Migration"
```

This creates a project folder under `migration-workspaces\contoso-ax-migration` with all templates.

## Analyze Inventory

CSV/JSON inventory:

```powershell
python plugins\ax-to-d365fo-migration-expert\scripts\analyze_ax_inventory.py `
  plugins\ax-to-d365fo-migration-expert\examples\sample-ax-inventory.csv `
  --output migration-analysis\contoso
```

X++ / XPO / AOT text:

```powershell
python plugins\ax-to-d365fo-migration-expert\scripts\analyze_ax_inventory.py `
  plugins\ax-to-d365fo-migration-expert\examples\sample-xpp-class.xpp `
  plugins\ax-to-d365fo-migration-expert\examples\sample-aot-export.xpo `
  --output migration-analysis\code-scan
```

## Unified CLI

```powershell
python plugins\ax-to-d365fo-migration-expert\scripts\migration_cli.py init "Contoso AX Migration"
python plugins\ax-to-d365fo-migration-expert\scripts\migration_cli.py analyze plugins\ax-to-d365fo-migration-expert\examples\sample-ax-inventory.csv --output migration-analysis\contoso
python plugins\ax-to-d365fo-migration-expert\scripts\migration_cli.py scan-code plugins\ax-to-d365fo-migration-expert\examples\sample-xpp-class.xpp --output migration-analysis\code
python plugins\ax-to-d365fo-migration-expert\scripts\migration_cli.py dashboard plugins\ax-to-d365fo-migration-expert\examples\sample-ax-inventory.csv --output migration-dashboard\contoso
python plugins\ax-to-d365fo-migration-expert\scripts\migration_cli.py profile-data data-export.csv --output data-quality-profile.md
python plugins\ax-to-d365fo-migration-expert\scripts\migration_cli.py ax-sql --output ax-modelstore.csv --dry-run
python plugins\ax-to-d365fo-migration-expert\scripts\migration_cli.py push-ado migration-analysis\contoso\ai-azure-devops-work-items.csv --dry-run
python plugins\ax-to-d365fo-migration-expert\scripts\migration_cli.py fetch-lcs --path / --output lcs.json --dry-run
python plugins\ax-to-d365fo-migration-expert\scripts\migration_cli.py fetch-d365fo --path /data/$metadata --output d365-metadata.xml --dry-run
python plugins\ax-to-d365fo-migration-expert\scripts\migration_cli.py usage-telemetry ax-usage.csv --object-column Object --output usage-summary.csv
python plugins\ax-to-d365fo-migration-expert\scripts\migration_cli.py validate
```

## Integration Environment Variables

Direct integrations are configured through `config/integrations.json` and environment variables:

- `AX_SQL_CONNECTION_STRING`
- `AZDO_ORG_URL`
- `AZDO_PROJECT`
- `AZDO_PAT`
- `LCS_BASE_URL`
- `LCS_BEARER_TOKEN`
- `D365FO_BASE_URL`
- `D365FO_BEARER_TOKEN`

Use `--dry-run` before calling external systems.

## Modelstore CSV Normalization

```powershell
python plugins\ax-to-d365fo-migration-expert\scripts\migration_cli.py extract-modelstore `
  modelstore-export.csv `
  --output normalized-inventory.csv
```

The extractor expects a CSV with fields such as `ElementType`, `Name`, `Layer`, `Model`, `Module`, `Path`, or similar. It writes the analyzer's standard inventory CSV format.

## Export Excel and PowerPoint

```powershell
python plugins\ax-to-d365fo-migration-expert\scripts\migration_cli.py export migration-analysis\contoso --output migration-exports\contoso
```

Outputs:

- `migration-analysis.xlsx`
- `migration-executive-deck.pptx`

## Important Outputs

- `dashboard.html`: browser-friendly command center.
- `ai-command-center-dashboard.md`: KPI dashboard.
- `ai-customization-disposition.md`: retire / extend / rebuild recommendations.
- `ai-risk-mitigation-playbooks.md`: risk-to-action guidance.
- `ai-cost-model.md`: effort points to person-day and budget range.
- `ai-standard-feature-matches.md`: D365FO standard feature candidates.
- `ai-dependency-graph.md`: Mermaid dependency graph.
- `ai-azure-devops-work-items.csv`: importable delivery backlog starter.

## Configuration

Adjust these files to fit your delivery model:

- `config/migration-cost-model.json`
- `config/standard-feature-map.json`
- `config/risk-rules.json`
- `config/industry-packs.json`

## Tests

```powershell
python -m unittest discover plugins\ax-to-d365fo-migration-expert\tests
```

Full validation:

```powershell
python plugins\ax-to-d365fo-migration-expert\scripts\validate_plugin.py
```
