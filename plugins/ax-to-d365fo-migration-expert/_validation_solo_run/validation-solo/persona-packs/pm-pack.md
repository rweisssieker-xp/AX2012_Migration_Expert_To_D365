# Project Manager Control Pack

## Readiness Score

| Persona | Score | Interpretation |
| --- | --- | --- |
| PM | 80/100 | Ready |

## Next Actions

- Reduce high-risk scope before committing delivery baseline.

## Included Evidence

### persona-project-manager-control-view.md

# Project Manager Control View

| Control | Value | Owner | Action |
| --- | --- | --- | --- |
| Complexity | High | Program Manager | Track weekly |
| High-risk items | 5 | Workstream leads | Escalate blockers |
| Open decisions | 7 | Steering committee | Decision log |
| Scope reduction candidates | 1 | Business owners | Validate in workshops |

### raid-log.md

# RAID Log

| ID | Type | Item | Description | Owner | Status |
| --- | --- | --- | --- | --- | --- |
| R-001 | Risk | SalesFormLetter_Extension | overlayering, posting | Functional / technical lead | Open |
| D-001 | Dependency | SalesFormLetter_Extension | Requires architecture/business decision | Functional / technical lead | Open |
| R-002 | Risk | CustTableLegacyCreditCheck | overlayering | Functional / technical lead | Open |
| R-003 | Risk | AIFCustomerExport | aif, overlayering | Integration lead | Open |
| D-003 | Dependency | AIFCustomerExport | Requires architecture/business decision | Integration lead | Open |
| R-004 | Risk | WarehouseFileDrop | overlayering | Integration lead | Open |
| D-004 | Dependency | WarehouseFileDrop | Requires architecture/business decision | Integration lead | Open |
| R-005 | Risk | InventAgingCustom | overlayering, report-rationalization | Reporting lead | Open |
| R-006 | Risk | LegacyTaxAddon | overlayering | Solution architect | Open |
| D-006 | Dependency | LegacyTaxAddon | Requires architecture/business decision | Solution architect | Open |
| R-007 | Risk | LegacyWarehouseSupervisor | overlayering | Security lead | Open |
| R-008 | Risk | InventTransHistory | direct-sql, posting | Data migration lead | Open |
| D-008 | Dependency | InventTransHistory | Requires architecture/business decision | Data migration lead | Open |
| R-009 | Risk | SalesFormLetter_Extension | direct-sql, overlayering, posting, transaction-scope | Functional / technical lead | Open |
| D-009 | Dependency | SalesFormLetter_Extension | Requires architecture/business decision | Functional / technical lead | Open |

### raci-matrix.md

# RACI Matrix

| Workstream | Responsible | Accountable | Consulted | Informed |
| --- | --- | --- | --- | --- |
| Data | Data migration lead | Solution architect | Business owner | Program manager |
| Integration | Integration lead | Solution architect | Business owner | Program manager |
| Isv | Solution architect | Solution architect | Business owner | Program manager |
| Object | Functional / technical lead | Solution architect | Business owner | Program manager |
| Report | Reporting lead | Solution architect | Business owner | Program manager |
| Security | Security lead | Solution architect | Business owner | Program manager |

### weekly-status-report.md

# Weekly Status Report

| Area | Status | Comment |
| --- | --- | --- |
| Overall | Amber | Complexity is High. |
| Scope | Amber | 1 scope-reduction candidates need validation. |
| Risks | Amber | 16 risk flags detected. |
| Decisions | Amber | High-effort and retire decisions require owner confirmation. |

### steering-committee-pack.md

# Steering Committee Pack

| Metric | Value |
| --- | --- |
| Complexity | High |
| Score | 96 |
| High-risk items | 5 |
| Scope reduction candidates | 1 |
| Effort points | 77 |

## Decisions Needed

| ID | Decision | Owner | Due |
| --- | --- | --- | --- |
| DEC-001 | Approve Extend for SalesFormLetter_Extension | Functional / technical lead | Next steering |
| DEC-002 | Approve Retire Candidate for CustTableLegacyCreditCheck | Functional / technical lead | Next steering |
| DEC-003 | Approve Rebuild for AIFCustomerExport | Integration lead | Next steering |
| DEC-004 | Approve Rebuild for WarehouseFileDrop | Integration lead | Next steering |
| DEC-006 | Approve ISV Review for LegacyTaxAddon | Solution architect | Next steering |
| DEC-008 | Approve Rebuild for InventTransHistory | Data migration lead | Next steering |
| DEC-009 | Approve Rebuild for SalesFormLetter_Extension | Functional / technical lead | Next steering |

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
| Wave 0 | Discovery and scope reduction | CustTableLegacyCreditCheck, LegacyWarehouseSupervisor |
| Wave 1 | Standard/configuration and low-risk extensions | SalesFormLetter_Extension, InventAgingCustom |
| Wave 2 | Complex rebuilds, integrations, ISVs | AIFCustomerExport, WarehouseFileDrop, LegacyTaxAddon, InventTransHistory, SalesFormLetter_Extension |
| Wave 3 | Data migration, testing, cutover | Trial migrations, UAT, cutover rehearsal, go-live |
