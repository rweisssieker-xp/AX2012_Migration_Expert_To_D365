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

## Generate Persona and Stakeholder Packs

```powershell
python .\axmigrate.py persona-pack migration-analysis\sample --persona all --office --output persona-packs\sample
python .\axmigrate.py stakeholder-pack migration-analysis\sample --stakeholder all --output stakeholder-packs\sample
python .\axmigrate.py questionnaire --persona all --output migration-questionnaires\sample
```

## Generate Commerce/CXP/CRM/POS Packs

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

## Run Solo/Master-Orchestrator Flow

```powershell
python .\axmigrate.py solo-init "Contoso AX Migration" --output solo-migration
python .\axmigrate.py solo-run --project "Contoso AX Migration" --input plugins\ax-to-d365fo-migration-expert\examples\sample-ax-inventory.csv --output solo-migration
python .\axmigrate.py solo-orchestrate solo-migration\contoso-ax-migration --output master-orchestration\contoso
python .\axmigrate.py solo-status solo-migration\contoso-ax-migration
python .\axmigrate.py solo-test-plan solo-migration\contoso-ax-migration
python .\axmigrate.py solo-signoff solo-migration\contoso-ax-migration
```

## Generate Autonomous Governance Packs

```powershell
python .\axmigrate.py governance-pack migration-analysis\sample --output governance-packs\sample
python .\axmigrate.py evidence-vault migration-analysis\sample --output evidence-vault\sample
python .\axmigrate.py scope-guard migration-analysis\sample --output scope-guard\sample
python .\axmigrate.py cutover-rehearsal migration-analysis\sample --output cutover-rehearsal\sample
python .\axmigrate.py reconciliation-judge migration-analysis\sample --output reconciliation\sample
python .\axmigrate.py board-risk migration-analysis\sample --output board-risk\sample
python .\axmigrate.py process-twin migration-analysis\sample --output process-twin\sample
python .\axmigrate.py meeting-copilot migration-analysis\sample --output meeting-copilot\sample
```
