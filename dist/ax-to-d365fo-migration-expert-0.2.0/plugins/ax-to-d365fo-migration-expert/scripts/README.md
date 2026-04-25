# AX to D365FO Migration Expert Scripts

This folder contains helper scripts for migration project setup.

## create_migration_workspace.py

Creates a project folder from the standard migration templates:

```bash
python plugins/ax-to-d365fo-migration-expert/scripts/create_migration_workspace.py "Contoso AX Migration"
```

Future script candidates:

- Data entity mapping generators.
- Migration checklist exporters.

## migration_cli.py

Unified entrypoint:

```bash
python plugins/ax-to-d365fo-migration-expert/scripts/migration_cli.py validate
```

Supported commands:

- `init`
- `analyze`
- `scan-code`
- `dashboard`
- `extract-modelstore`
- `export`
- `profile-data`
- `monitor`
- `ax-sql`
- `push-ado`
- `fetch-lcs`
- `fetch-d365fo`
- `usage-telemetry`
- `validate`

## export_analysis.py

Exports an analysis folder to:

- `migration-analysis.xlsx`
- `migration-executive-deck.pptx`

## extract_modelstore_inventory.py

Normalizes AX modelstore-style CSV exports into the analyzer inventory format.

## analyze_ax_inventory.py

Analyzes CSV or JSON inventory exports and generates AI migration assessment reports:

```bash
python plugins/ax-to-d365fo-migration-expert/scripts/analyze_ax_inventory.py `
  plugins/ax-to-d365fo-migration-expert/examples/sample-ax-inventory.csv `
  --output migration-analysis/contoso
```

The script is schema-tolerant and works best with columns such as `Category`, `ObjectType`, `Name`, `Layer`, `Module`, `Usage`, `Complexity`, `Technology`, and `BusinessPurpose`.

It also accepts `.xpp`, `.xpo`, and plain-text AOT exports for lightweight X++ pattern detection.
