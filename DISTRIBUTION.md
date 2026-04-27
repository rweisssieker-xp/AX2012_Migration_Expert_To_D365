# AX to D365FO Migration Expert Distribution

## Package Contents

The distributable package contains:

- `plugins/ax-to-d365fo-migration-expert`
- `.agents/plugins/marketplace.json`
- `INSTALL.md`
- `README.md`
- `docs/`

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
python plugins\ax-to-d365fo-migration-expert\scripts\migration_cli.py doctor
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

## Commerce and Solo Smoke Tests

```powershell
python plugins\ax-to-d365fo-migration-expert\scripts\migration_cli.py commerce-pack migration-analysis\sample --output commerce-packs\sample
python plugins\ax-to-d365fo-migration-expert\scripts\migration_cli.py commerce-readiness migration-analysis\sample --output commerce-readiness\sample
python plugins\ax-to-d365fo-migration-expert\scripts\migration_cli.py solo-init "Sample AX Migration" --output solo-migration
python plugins\ax-to-d365fo-migration-expert\scripts\migration_cli.py solo-run --project "Sample AX Migration" --input plugins\ax-to-d365fo-migration-expert\examples\sample-ax-inventory.csv --output solo-migration
```

## Scope Included

- 92 skills.
- 264 templates.
- 51 Python scripts.
- 25 JSON configs.
- 46 analyzer outputs.
- 380 documented AI/KI feature entries.

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
