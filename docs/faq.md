# FAQ

## Is this a direct AX upgrade tool?

No. It is a migration assessment, scope reduction, planning, and delivery-acceleration plugin. It can analyze evidence and produce artifacts, but it does not perform a Microsoft-supported technical upgrade by itself.

## Which AX versions are covered?

The skill is written for AX 4.0, AX 2009, and AX 2012, including AX 2012 R2/R3 scenarios.

## What input formats are supported?

- CSV
- TSV
- JSON
- X++ text
- XPO
- AOT text exports
- Modelstore-style CSV exports
- Usage telemetry CSV

## Does it connect directly to AX SQL?

Yes, via the `ax-sql` connector, but only when `AX_SQL_CONNECTION_STRING` is configured. Use `--dry-run` first.

## Does it create Azure DevOps work items?

Yes, via the `push-ado` connector. It requires `AZDO_ORG_URL`, `AZDO_PROJECT`, and `AZDO_PAT`. The analyzer also produces `ai-azure-devops-work-items.csv`.

## Does it call LCS or D365FO APIs?

It includes generic HTTP connector scaffolding for LCS and D365FO/OData endpoints. Real use requires valid URLs and bearer tokens.

## Are recommendations final decisions?

No. Recommendations include evidence and confidence signals. Business owners, architects, and steering committees should validate high-impact decisions.

## Can one person run a migration project with this plugin?

The plugin is designed to support a solo operator with generated plans, role substitution, evidence checks, master-orchestrator routing, daily actions, test planning, sign-off, audit binder, hypercare, and benefits tracking. It does not remove the need for external approvals where real governance is required, such as executive, security, finance, audit, legal, customer, payment, or production go-live sign-off.

## Does the plugin cover Commerce, CRM, CXP, POS, and offline store scenarios?

Yes. The Customer & Commerce Experience domain covers CXP, CRM/Dataverse, Lead Management, D365 Commerce HQ, Commerce Scale Unit, Channel DB, POS, POS Offline, Payments/PCI, Store Operations, Loyalty, Pricing, Assortment, Omnichannel, Marketplace, Call Center, Analytics, and Store Training.

## Does it cover governance beyond technical migration?

Yes. The Autonomous Governance & Evidence Intelligence layer covers contract/scope guardrails, stakeholder sentiment, evidence vault, cutover rehearsal, reconciliation judge, license/cost optimization, ALM release train, training readiness, ISV exit, country regulatory packs, archive strategy, hyperautomation, board risk forecast, process twin, and meeting copilot outputs.

## What is the Migration Intelligence Fabric?

It is the documented next USP backlog after the current 380-feature implementation. It proposes Features 381-500 for migration memory, benchmarking, portfolio control, scenario simulation, delivery quality audit, technical debt liquidation, Fabric/data product modernization, integration resilience, security attack surface, sustainability, PMO negotiation, knowledge transfer, migration war games, value realization, and continuous improvement.

## When is Commerce go-live blocked?

Commerce go-live is blocked when critical evidence is missing for CSU readiness, POS Offline readiness where offline is required, Payments/PCI, Store Smoke Tests, Channel Data Sync, Offline Recovery, Payment Reconciliation, Commerce Security/PCI, Customer Master Harmonization, or Lead-to-Cash Traceability.

## Can generated analysis be committed?

Usually no. Generated analysis may contain customer data. Keep it out of version control unless it is sanitized sample data.

## How do I validate everything?

```powershell
python plugins\ax-to-d365fo-migration-expert\scripts\migration_cli.py validate
```

For local runtime and optional dependency checks:

```powershell
python .\axmigrate.py doctor
```

## Where do I change cost assumptions?

Edit:

```text
plugins/ax-to-d365fo-migration-expert/config/migration-cost-model.json
```
