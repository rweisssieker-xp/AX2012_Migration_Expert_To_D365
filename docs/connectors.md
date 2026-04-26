# Connectors

The plugin includes connector scaffolding for real enterprise integrations. All connectors support safe configuration and should be tested with dry-run first.

## AX SQL / Modelstore

Purpose: extract modelstore-style inventory rows from AX SQL Server.

```powershell
$env:AX_SQL_CONNECTION_STRING = "Driver={ODBC Driver 17 for SQL Server};Server=...;Database=...;Trusted_Connection=yes;"
python plugins\ax-to-d365fo-migration-expert\scripts\migration_cli.py ax-sql --output ax-modelstore.csv --dry-run
```

Remove `--dry-run` only after the query and connection string are verified.

## Azure DevOps

Purpose: push analyzer-generated work item CSV into Azure DevOps.

```powershell
$env:AZDO_ORG_URL = "https://dev.azure.com/your-org"
$env:AZDO_PROJECT = "your-project"
$env:AZDO_PAT = "..."
python plugins\ax-to-d365fo-migration-expert\scripts\migration_cli.py push-ado migration-analysis\sample\ai-azure-devops-work-items.csv --dry-run
```

## LCS

Purpose: fetch metadata or API payloads from a configured LCS endpoint.

```powershell
$env:LCS_BASE_URL = "https://..."
$env:LCS_BEARER_TOKEN = "..."
python plugins\ax-to-d365fo-migration-expert\scripts\migration_cli.py fetch-lcs --path / --output lcs.json --dry-run
```

## D365FO Metadata / OData

Purpose: fetch D365FO metadata or OData payloads.

```powershell
$env:D365FO_BASE_URL = "https://your-environment.operations.dynamics.com"
$env:D365FO_BEARER_TOKEN = "..."
python plugins\ax-to-d365fo-migration-expert\scripts\migration_cli.py fetch-d365fo --path /data/$metadata --output d365-metadata.xml --dry-run
```

## Usage Telemetry

Purpose: summarize usage evidence from CSV logs.

```powershell
python plugins\ax-to-d365fo-migration-expert\scripts\migration_cli.py usage-telemetry ax-usage.csv --object-column Object --output usage-summary.csv
```

## Security Notes

- Keep secrets in environment variables.
- Do not commit output from customer systems.
- Run dry-run before any write operation.
- Sanitize data before opening GitHub issues.

