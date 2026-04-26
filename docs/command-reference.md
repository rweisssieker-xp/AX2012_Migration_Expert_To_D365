# Command Reference

Use the root wrapper from the repository root:

```powershell
python .\axmigrate.py <command> [options]
```

The plugin script can also be called directly:

```powershell
python plugins\ax-to-d365fo-migration-expert\scripts\migration_cli.py <command> [options]
```

## Core Migration Commands

| Command | Purpose |
| --- | --- |
| `init` | Create a migration workspace from all templates. |
| `analyze` | Analyze CSV, JSON, X++, XPO, and AOT-style evidence. |
| `scan-code` | Alias for code-focused X++/XPO/AOT analysis. |
| `dashboard` | Generate analysis including `dashboard.html`. |
| `extract-modelstore` | Normalize AX modelstore-style CSV exports. |
| `export` | Export an analysis folder to Excel and PowerPoint. |
| `profile-data` | Profile CSV data quality. |
| `monitor` | Compare two normalized inventory snapshots. |

## Role, Governance, and Delivery Commands

| Command | Purpose |
| --- | --- |
| `persona-pack` | Generate CEO, CIO, CISO, PM, and team packs with readiness scoring. |
| `questionnaire` | Generate role questionnaires, migration factory, cutover, hypercare, and partner packs. |
| `stakeholder-pack` | Generate CFO, COO, data, integration, QA, enterprise architecture, vendor, legal, support, and partner packs. |
| `github-issues` | Export analyzer work items as GitHub issue Markdown files. |

## Commerce/CXP/CRM/POS Commands

| Command | Purpose |
| --- | --- |
| `commerce-pack` | Generate the full Customer & Commerce Experience master pack. |
| `commerce-readiness` | Generate readiness scores for CXP, CRM, Lead, Customer Master, Commerce HQ, CSU, POS, Offline, Store Ops, Payments, Loyalty, Pricing, Omnichannel, and Cutover. |
| `commerce-cutover` | Generate Store/POS/CSU/Payments/Offline cutover runbook, smoke tests, and go-live gate. |
| `commerce-offline-check` | Generate POS offline continuity, offline sync test, and recovery runbooks. |
| `commerce-crm-pack` | Generate CRM/Dataverse, Lead Management, Lead-to-Cash, and Customer Master packs. |
| `commerce-store-pack` | Generate Store Operations, POS Hardware, and Store Training packs. |
| `commerce-payments-pack` | Generate Payment Reconciliation, PCI/Security Gate, and Payment Cutover packs. |
| `commerce-omnichannel-pack` | Generate Omnichannel Order Flow, Commerce Analytics, and Marketplace Integration packs. |

## Solo/Master-Orchestrator Commands

| Command | Purpose |
| --- | --- |
| `solo-init` | Create a solo migration project operating folder. |
| `solo-run` | Run the full solo orchestration flow from inventory input. |
| `solo-evidence` | Generate evidence completeness outputs. |
| `solo-status` | Generate health, status, next actions, and confidence outputs. |
| `solo-gates` | Generate self-approval and external approval gates. |
| `solo-daily` | Generate the daily migration command sheet. |
| `solo-war-room` | Generate cutover war-room outputs. |
| `solo-hypercare` | Generate hypercare command center outputs. |
| `solo-audit-binder` | Generate audit and evidence binder outputs. |
| `solo-benefits` | Generate benefits realization outputs. |
| `solo-orchestrate` | Generate master-orchestrator plan, routing, evidence-to-skill matrix, and action queue. |
| `solo-brain` | Generate AI migration brain outputs. |
| `solo-next` | Generate next-best-action outputs. |
| `solo-simulate` | Generate decision impact simulations. |
| `solo-scope-defense` | Generate scope defense outputs. |
| `solo-waste-hunter` | Generate waste hunter report. |
| `solo-predict` | Generate prediction outputs. |
| `solo-translate` | Generate stakeholder translation outputs. |
| `solo-drift` | Generate project drift detector outputs. |
| `solo-communicate` | Generate communication copilot outputs. |
| `solo-test-plan` | Generate key-user, UAT, regression, and process owner test planning outputs. |
| `solo-test-status` | Generate test execution status outputs. |
| `solo-signoff` | Generate business sign-off outputs. |

## Connector and Validation Commands

| Command | Purpose |
| --- | --- |
| `ax-sql` | Extract AX SQL/modelstore inventory through ODBC. |
| `push-ado` | Create Azure DevOps work items from analyzer CSV. |
| `fetch-lcs` | Fetch LCS metadata or payloads from a configured endpoint. |
| `fetch-d365fo` | Fetch D365FO metadata or OData payloads from a configured endpoint. |
| `usage-telemetry` | Summarize AX usage telemetry CSV. |
| `validate` | Run JSON, skill, test, analyzer, template, Commerce, Solo, and placeholder checks. |
| `doctor` | Check runtime, optional dependencies, plugin metadata, configs, and connector environment variables. |
| `examples` | Print useful command examples. |
