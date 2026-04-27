# Command Reference

Use the root wrapper from the repository root:

```powershell
python .\axmigrate.py <command> [options]
```

## Core Migration

| Command | Purpose |
| --- | --- |
| `init` | Run the `init` migration automation command. |
| `analyze` | Run the `analyze` migration automation command. |
| `scan-code` | Run the `scan-code` migration automation command. |
| `dashboard` | Run the `dashboard` migration automation command. |
| `extract-modelstore` | Run the `extract-modelstore` migration automation command. |
| `export` | Run the `export` migration automation command. |
| `profile-data` | Run the `profile-data` migration automation command. |
| `monitor` | Run the `monitor` migration automation command. |

## Role, Governance, and Delivery

| Command | Purpose |
| --- | --- |
| `persona-pack` | Run the `persona-pack` migration automation command. |
| `questionnaire` | Run the `questionnaire` migration automation command. |
| `stakeholder-pack` | Run the `stakeholder-pack` migration automation command. |
| `github-issues` | Run the `github-issues` migration automation command. |

## Commerce/CXP/CRM/POS

| Command | Purpose |
| --- | --- |
| `commerce-pack` | Run the `commerce-pack` migration automation command. |
| `commerce-readiness` | Run the `commerce-readiness` migration automation command. |
| `commerce-cutover` | Run the `commerce-cutover` migration automation command. |
| `commerce-offline-check` | Run the `commerce-offline-check` migration automation command. |
| `commerce-crm-pack` | Run the `commerce-crm-pack` migration automation command. |
| `commerce-store-pack` | Run the `commerce-store-pack` migration automation command. |
| `commerce-payments-pack` | Run the `commerce-payments-pack` migration automation command. |
| `commerce-omnichannel-pack` | Run the `commerce-omnichannel-pack` migration automation command. |

## Solo/Master Orchestrator

| Command | Purpose |
| --- | --- |
| `solo-init` | Run the `solo-init` migration automation command. |
| `solo-run` | Run the `solo-run` migration automation command. |
| `solo-evidence` | Run the `solo-evidence` migration automation command. |
| `solo-status` | Run the `solo-status` migration automation command. |
| `solo-gates` | Run the `solo-gates` migration automation command. |
| `solo-daily` | Run the `solo-daily` migration automation command. |
| `solo-war-room` | Run the `solo-war-room` migration automation command. |
| `solo-hypercare` | Run the `solo-hypercare` migration automation command. |
| `solo-audit-binder` | Run the `solo-audit-binder` migration automation command. |
| `solo-benefits` | Run the `solo-benefits` migration automation command. |
| `solo-orchestrate` | Run the `solo-orchestrate` migration automation command. |
| `solo-brain` | Run the `solo-brain` migration automation command. |
| `solo-next` | Run the `solo-next` migration automation command. |
| `solo-simulate` | Run the `solo-simulate` migration automation command. |
| `solo-scope-defense` | Run the `solo-scope-defense` migration automation command. |
| `solo-waste-hunter` | Run the `solo-waste-hunter` migration automation command. |
| `solo-predict` | Run the `solo-predict` migration automation command. |
| `solo-translate` | Run the `solo-translate` migration automation command. |
| `solo-drift` | Run the `solo-drift` migration automation command. |
| `solo-communicate` | Run the `solo-communicate` migration automation command. |
| `solo-test-plan` | Run the `solo-test-plan` migration automation command. |
| `solo-test-status` | Run the `solo-test-status` migration automation command. |
| `solo-signoff` | Run the `solo-signoff` migration automation command. |

## Autonomous Governance & Evidence

| Command | Purpose |
| --- | --- |
| `governance-pack` | Run the `governance-pack` migration automation command. |
| `evidence-vault` | Run the `evidence-vault` migration automation command. |
| `scope-guard` | Run the `scope-guard` migration automation command. |
| `contract-risk` | Run the `contract-risk` migration automation command. |
| `cutover-rehearsal` | Run the `cutover-rehearsal` migration automation command. |
| `reconciliation-judge` | Run the `reconciliation-judge` migration automation command. |
| `license-cost` | Run the `license-cost` migration automation command. |
| `alm-release` | Run the `alm-release` migration automation command. |
| `training-readiness` | Run the `training-readiness` migration automation command. |
| `isv-exit` | Run the `isv-exit` migration automation command. |
| `country-regulatory-pack` | Run the `country-regulatory-pack` migration automation command. |
| `archive-strategy` | Run the `archive-strategy` migration automation command. |
| `hyperautomation-pack` | Run the `hyperautomation-pack` migration automation command. |
| `board-risk` | Run the `board-risk` migration automation command. |
| `process-twin` | Run the `process-twin` migration automation command. |
| `meeting-copilot` | Run the `meeting-copilot` migration automation command. |

## Migration Intelligence Fabric

| Command | Purpose |
| --- | --- |
| `intelligence-pack` | Run the `intelligence-pack` migration automation command. |
| `migration-memory` | Run the `migration-memory` migration automation command. |
| `benchmark` | Run the `benchmark` migration automation command. |
| `portfolio-control` | Run the `portfolio-control` migration automation command. |
| `scenario-lab` | Run the `scenario-lab` migration automation command. |
| `quality-audit` | Run the `quality-audit` migration automation command. |
| `debt-liquidator` | Run the `debt-liquidator` migration automation command. |
| `fabric-advisor` | Run the `fabric-advisor` migration automation command. |
| `integration-resilience` | Run the `integration-resilience` migration automation command. |
| `attack-surface` | Run the `attack-surface` migration automation command. |
| `sustainability` | Run the `sustainability` migration automation command. |
| `pmo-negotiator` | Run the `pmo-negotiator` migration automation command. |
| `knowledge-transfer-exam` | Run the `knowledge-transfer-exam` migration automation command. |
| `war-game` | Run the `war-game` migration automation command. |
| `value-realization` | Run the `value-realization` migration automation command. |
| `continuous-improvement` | Run the `continuous-improvement` migration automation command. |

## Automation, Gates, Demos, UI, Security, Connectors

| Command | Purpose |
| --- | --- |
| `orchestrate` | Analyze input, select skills, detect missing evidence, and propose next CLI commands. |
| `evidence-gates` | Create go-live gate questionnaire and Ready/Needs control/Blocked result. |
| `memory-store` | Persist migration memory into local SQLite and JSONL files. |
| `security-scan` | Scan files for secrets, connection strings, and common PII patterns. |
| `project-ui` | Generate a local HTML command UI for wizard, gates, router, memory, and security commands. |
| `wizard` | Ask for or accept a project profile and generate a tailored execution plan. |
| `demo-projects` | Generate ready-to-open demo projects and dashboards. |
| `ax-sql` | Run the `ax-sql` migration automation command. |
| `push-ado` | Run the `push-ado` migration automation command. |
| `fetch-lcs` | Run the `fetch-lcs` migration automation command. |
| `fetch-d365fo` | Run the `fetch-d365fo` migration automation command. |
| `usage-telemetry` | Run the `usage-telemetry` migration automation command. |
| `validate` | Run the `validate` migration automation command. |
| `doctor` | Run the `doctor` migration automation command. |
| `examples` | Run the `examples` migration automation command. |

