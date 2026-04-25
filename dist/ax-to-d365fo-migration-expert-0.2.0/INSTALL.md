# AX to D365FO Migration Expert Distribution

## Package Contents

The distributable package contains:

- `plugins/ax-to-d365fo-migration-expert`
- `.agents/plugins/marketplace.json`
- `INSTALL.md`

## Install Into Another Repo

Copy the package contents into the target repo root so the layout becomes:

```text
<repo-root>/
  .agents/
    plugins/
      marketplace.json
  plugins/
    ax-to-d365fo-migration-expert/
      .codex-plugin/
        plugin.json
      skills/
      scripts/
      templates/
      docs/
      config/
      examples/
      tests/
```

## Validate

From the target repo root:

```powershell
python plugins\ax-to-d365fo-migration-expert\scripts\migration_cli.py validate
```

## First Run

```powershell
python plugins\ax-to-d365fo-migration-expert\scripts\migration_cli.py analyze `
  plugins\ax-to-d365fo-migration-expert\examples\sample-ax-inventory.csv `
  --output migration-analysis\sample
```

Open:

```text
migration-analysis\sample\dashboard.html
```

## External Integrations

For real external calls, configure environment variables:

- `AX_SQL_CONNECTION_STRING`
- `AZDO_ORG_URL`
- `AZDO_PROJECT`
- `AZDO_PAT`
- `LCS_BASE_URL`
- `LCS_BEARER_TOKEN`
- `D365FO_BASE_URL`
- `D365FO_BEARER_TOKEN`

Use dry-run first:

```powershell
python plugins\ax-to-d365fo-migration-expert\scripts\migration_cli.py ax-sql --output ax-modelstore.csv --dry-run
python plugins\ax-to-d365fo-migration-expert\scripts\migration_cli.py push-ado migration-analysis\sample\ai-azure-devops-work-items.csv --dry-run
```
