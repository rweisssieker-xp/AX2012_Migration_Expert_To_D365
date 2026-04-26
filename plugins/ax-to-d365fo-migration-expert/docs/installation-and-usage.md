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

From the repository root, the shorter wrapper is also available:

```powershell
python .\axmigrate.py validate
python .\axmigrate.py doctor
python .\axmigrate.py examples
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
- Persona and governance outputs: `persona-ceo-summary.md`, `persona-cio-architecture-view.md`, `persona-ciso-security-view.md`, `persona-project-manager-control-view.md`, `persona-team-member-task-view.md`, `steering-committee-pack.md`, `raid-log.md`, `raci-matrix.md`, `weekly-status-report.md`, `ciso-security-gate-pack.md`, `project-operating-model.md`, `board-ceo-narrative.md`, `team-execution-pack.md`, `role-based-prompt-library.md`, and `project-onboarding-guide.md`.

## Persona, Stakeholder, and Questionnaire Packs

```powershell
python .\axmigrate.py persona-pack migration-analysis\contoso --persona all --office --output persona-packs\contoso
python .\axmigrate.py stakeholder-pack migration-analysis\contoso --stakeholder all --output stakeholder-packs\contoso
python .\axmigrate.py questionnaire --persona all --output migration-questionnaires\contoso
python .\axmigrate.py github-issues migration-analysis\contoso --output github-issues\contoso
```

## Commerce/CXP/CRM/POS Packs

```powershell
python .\axmigrate.py commerce-pack migration-analysis\contoso --output commerce-packs\contoso
python .\axmigrate.py commerce-readiness migration-analysis\contoso --output commerce-readiness\contoso
python .\axmigrate.py commerce-cutover migration-analysis\contoso --output commerce-cutover\contoso
python .\axmigrate.py commerce-offline-check migration-analysis\contoso --output commerce-offline\contoso
python .\axmigrate.py commerce-crm-pack migration-analysis\contoso --output commerce-crm\contoso
python .\axmigrate.py commerce-store-pack migration-analysis\contoso --output commerce-store\contoso
python .\axmigrate.py commerce-payments-pack migration-analysis\contoso --output commerce-payments\contoso
python .\axmigrate.py commerce-omnichannel-pack migration-analysis\contoso --output commerce-omnichannel\contoso
```

Commerce packs cover CXP, CRM/Dataverse, Lead Management, Customer Master, Commerce HQ, CSU, Channel DB, Channel Sync, POS, POS Offline, Payments/PCI, Store Operations, Store Training, Loyalty, Pricing, Assortment, Omnichannel, Call Center, Marketplace, Analytics, and Commerce Hypercare.

## Solo/Master-Orchestrator Packs

```powershell
python .\axmigrate.py solo-init "Contoso AX Migration" --output solo-migration
python .\axmigrate.py solo-run --project "Contoso AX Migration" --input plugins\ax-to-d365fo-migration-expert\examples\sample-ax-inventory.csv --output solo-migration
python .\axmigrate.py solo-orchestrate solo-migration\contoso-ax-migration --output master-orchestration\contoso
python .\axmigrate.py solo-evidence solo-migration\contoso-ax-migration
python .\axmigrate.py solo-status solo-migration\contoso-ax-migration
python .\axmigrate.py solo-gates solo-migration\contoso-ax-migration
python .\axmigrate.py solo-daily solo-migration\contoso-ax-migration
python .\axmigrate.py solo-war-room solo-migration\contoso-ax-migration
python .\axmigrate.py solo-hypercare solo-migration\contoso-ax-migration
python .\axmigrate.py solo-audit-binder solo-migration\contoso-ax-migration
python .\axmigrate.py solo-benefits solo-migration\contoso-ax-migration
python .\axmigrate.py solo-test-plan solo-migration\contoso-ax-migration
python .\axmigrate.py solo-test-status solo-migration\contoso-ax-migration
python .\axmigrate.py solo-signoff solo-migration\contoso-ax-migration
```

The Solo/Master layer supports a single user with project operating artifacts, evidence completeness, self-approval gates, external approval packs, master routing, daily actions, scope defense, waste hunting, predictions, stakeholder communication, test planning, test status, sign-off, audit binder, benefits tracking, cutover, and hypercare.

## Autonomous Governance & Evidence Intelligence Packs

```powershell
python .\axmigrate.py governance-pack migration-analysis\contoso --output governance-packs\contoso
python .\axmigrate.py evidence-vault migration-analysis\contoso --output evidence-vault\contoso
python .\axmigrate.py scope-guard migration-analysis\contoso --output scope-guard\contoso
python .\axmigrate.py contract-risk migration-analysis\contoso --output contract-risk\contoso
python .\axmigrate.py cutover-rehearsal migration-analysis\contoso --output cutover-rehearsal\contoso
python .\axmigrate.py reconciliation-judge migration-analysis\contoso --output reconciliation\contoso
python .\axmigrate.py license-cost migration-analysis\contoso --output license-cost\contoso
python .\axmigrate.py alm-release migration-analysis\contoso --output alm-release\contoso
python .\axmigrate.py training-readiness migration-analysis\contoso --output training-readiness\contoso
python .\axmigrate.py isv-exit migration-analysis\contoso --output isv-exit\contoso
python .\axmigrate.py country-regulatory-pack migration-analysis\contoso --output country-regulatory\contoso
python .\axmigrate.py archive-strategy migration-analysis\contoso --output archive-strategy\contoso
python .\axmigrate.py hyperautomation-pack migration-analysis\contoso --output hyperautomation\contoso
python .\axmigrate.py board-risk migration-analysis\contoso --output board-risk\contoso
python .\axmigrate.py process-twin migration-analysis\contoso --output process-twin\contoso
python .\axmigrate.py meeting-copilot migration-analysis\contoso --output meeting-copilot\contoso
```

These commands convert the same migration evidence into contract/scope control, evidence vaults, cutover rehearsal proof, reconciliation sign-off, license cost optimization, ALM release gates, training readiness, ISV exit, country regulatory packs, archive strategy, hyperautomation backlog, board risk forecast, process twin traceability, and meeting-to-backlog actions.

## Configuration

Adjust these files to fit your delivery model:

- `config/migration-cost-model.json`
- `config/standard-feature-map.json`
- `config/risk-rules.json`
- `config/industry-packs.json`
- `config/regulatory-packs.json`
- `config/commerce-role-skill-map.json`
- `config/commerce-synonyms.json`
- `config/commerce-readiness-rules.json`
- `config/commerce-gate-minimum-evidence.json`
- `config/commerce-cutover-checks.json`
- `config/pos-offline-risk-rules.json`
- `config/payment-pci-risk-rules.json`
- `config/crm-lead-management-map.json`
- `config/governance-role-skill-map.json`
- `config/governance-synonyms.json`
- `config/evidence-vault-rules.json`
- `config/contract-scope-risk-rules.json`
- `config/reconciliation-rules.json`
- `config/license-cost-rules.json`
- `config/alm-release-rules.json`
- `config/training-effectiveness-rules.json`
- `config/country-regulatory-rules.json`
- `config/process-twin-rules.json`

## Tests

```powershell
python -m unittest discover plugins\ax-to-d365fo-migration-expert\tests
```

Full validation:

```powershell
python plugins\ax-to-d365fo-migration-expert\scripts\validate_plugin.py
```

Doctor check:

```powershell
python .\axmigrate.py doctor
```
