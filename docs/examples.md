# Examples

## Analyze Sample Inventory

```powershell
python plugins\ax-to-d365fo-migration-expert\scripts\migration_cli.py analyze `
  plugins\ax-to-d365fo-migration-expert\examples\sample-ax-inventory.csv `
  --output migration-analysis\sample
```

Outputs include:

- `dashboard.html`
- `ai-analysis-summary.md`
- `ai-customization-disposition.md`
- `ai-risk-heatmap.md`
- `ai-cost-model.md`
- `ai-do-not-migrate-report.md`
- `migration-knowledge-graph.json`

## Scan X++ / XPO

```powershell
python plugins\ax-to-d365fo-migration-expert\scripts\migration_cli.py scan-code `
  plugins\ax-to-d365fo-migration-expert\examples\sample-xpp-class.xpp `
  plugins\ax-to-d365fo-migration-expert\examples\sample-aot-export.xpo `
  --output migration-analysis\code
```

## Create Delivery Workspace

```powershell
python plugins\ax-to-d365fo-migration-expert\scripts\migration_cli.py init "Contoso AX Migration"
```

## Export Executive Artifacts

```powershell
python plugins\ax-to-d365fo-migration-expert\scripts\migration_cli.py export migration-analysis\sample --output migration-exports\sample
```

Generated files:

- `migration-analysis.xlsx`
- `migration-executive-deck.pptx`

## Profile Data Quality

```powershell
python plugins\ax-to-d365fo-migration-expert\scripts\migration_cli.py profile-data data-export.csv --output data-quality-profile.md
```

## Compare Inventory Snapshots

```powershell
python plugins\ax-to-d365fo-migration-expert\scripts\migration_cli.py monitor baseline\inventory-normalized.json current\inventory-normalized.json --output inventory-change-monitor.md
```

