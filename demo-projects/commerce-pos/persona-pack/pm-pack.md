# Project Manager Control Pack

## Readiness Score

| Persona | Score | Interpretation |
| --- | --- | --- |
| PM | 83/100 | Ready |

## Next Actions

- Proceed with gate review and maintain weekly evidence updates.

## Included Evidence

### persona-project-manager-control-view.md

# Project Manager Control View

| Control | Value | Owner | Action |
| --- | --- | --- | --- |
| Complexity | Medium | Program Manager | Track weekly |
| High-risk items | 5 | Workstream leads | Escalate blockers |
| Open decisions | 5 | Steering committee | Decision log |
| Scope reduction candidates | 0 | Business owners | Validate in workshops |

### raid-log.md

# RAID Log

| ID | Type | Item | Description | Owner | Status |
| --- | --- | --- | --- | --- | --- |
| R-001 | Risk | RetailPriceOverride | client-dependency, overlayering | Functional / technical lead | Open |
| D-001 | Dependency | RetailPriceOverride | Requires architecture/business decision | Functional / technical lead | Open |
| R-002 | Risk | CSUChannelSyncMonitor | client-dependency, overlayering | Integration lead | Open |
| D-002 | Dependency | CSUChannelSyncMonitor | Requires architecture/business decision | Integration lead | Open |
| R-003 | Risk | POSOfflineRecoveryForm | overlayering | Functional / technical lead | Open |
| D-003 | Dependency | POSOfflineRecoveryForm | Requires architecture/business decision | Functional / technical lead | Open |
| R-004 | Risk | PaymentTerminalConnector | overlayering, posting | Integration lead | Open |
| D-004 | Dependency | PaymentTerminalConnector | Requires architecture/business decision | Integration lead | Open |
| R-005 | Risk | LoyaltyLiabilityReport | overlayering, report-rationalization | Reporting lead | Open |
| R-006 | Risk | RetailTransactionHistory | client-dependency, direct-sql | Data migration lead | Open |
| D-006 | Dependency | RetailTransactionHistory | Requires architecture/business decision | Data migration lead | Open |
| R-007 | Risk | StoreManagerLegacyRole | overlayering | Security lead | Open |

### raci-matrix.md

# RACI Matrix

| Workstream | Responsible | Accountable | Consulted | Informed |
| --- | --- | --- | --- | --- |
| Data | Data migration lead | Solution architect | Business owner | Program manager |
| Integration | Integration lead | Solution architect | Business owner | Program manager |
| Object | Functional / technical lead | Solution architect | Business owner | Program manager |
| Report | Reporting lead | Solution architect | Business owner | Program manager |
| Security | Security lead | Solution architect | Business owner | Program manager |

### weekly-status-report.md

# Weekly Status Report

| Area | Status | Comment |
| --- | --- | --- |
| Overall | Amber | Complexity is Medium. |
| Scope | Amber | 0 scope-reduction candidates need validation. |
| Risks | Amber | 12 risk flags detected. |
| Decisions | Amber | High-effort and retire decisions require owner confirmation. |

### steering-committee-pack.md

# Steering Committee Pack

| Metric | Value |
| --- | --- |
| Complexity | Medium |
| Score | 73 |
| High-risk items | 5 |
| Scope reduction candidates | 0 |
| Effort points | 62 |

## Decisions Needed

| ID | Decision | Owner | Due |
| --- | --- | --- | --- |
| DEC-001 | Approve Rebuild for RetailPriceOverride | Functional / technical lead | Next steering |
| DEC-002 | Approve Rebuild for CSUChannelSyncMonitor | Integration lead | Next steering |
| DEC-003 | Approve Extend for POSOfflineRecoveryForm | Functional / technical lead | Next steering |
| DEC-004 | Approve Rebuild for PaymentTerminalConnector | Integration lead | Next steering |
| DEC-006 | Approve Rebuild for RetailTransactionHistory | Data migration lead | Next steering |

### project-operating-model.md

# Project Operating Model

| Area | Recommendation |
| --- | --- |
| Governance | Weekly delivery review and bi-weekly steering committee. |
| Decision rights | Business owns scope decisions; architecture owns technical patterns; CISO owns security gates. |
| Escalation | Escalate high-risk blockers within 48 hours. |
| Cadence | Daily workstream standups during build/test/cutover windows. |
| Artifacts | Maintain RAID, RACI, decision log, backlog, cutover runbook, and test dashboard. |

### ai-wave-roadmap.md

# AI Migration Wave Roadmap

| Wave | Purpose | Candidate scope |
| --- | --- | --- |
| Wave 0 | Discovery and scope reduction | StoreManagerLegacyRole |
| Wave 1 | Standard/configuration and low-risk extensions | POSOfflineRecoveryForm, LoyaltyLiabilityReport |
| Wave 2 | Complex rebuilds, integrations, ISVs | RetailPriceOverride, CSUChannelSyncMonitor, PaymentTerminalConnector, RetailTransactionHistory |
| Wave 3 | Data migration, testing, cutover | Trial migrations, UAT, cutover rehearsal, go-live |
