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
| Complexity | Medium | Program Manager | Track weekly |
| High-risk items | 2 | Workstream leads | Escalate blockers |
| Open decisions | 4 | Steering committee | Decision log |
| Scope reduction candidates | 0 | Business owners | Validate in workshops |

### raid-log.md

# RAID Log

| ID | Type | Item | Description | Owner | Status |
| --- | --- | --- | --- | --- | --- |
| R-001 | Risk | AIFLeadToCashSync | aif, overlayering | Integration lead | Open |
| D-001 | Dependency | AIFLeadToCashSync | Requires architecture/business decision | Integration lead | Open |
| R-002 | Risk | CustContactLegacyMap | direct-sql, overlayering | Data migration lead | Open |
| D-002 | Dependency | CustContactLegacyMap | Requires architecture/business decision | Data migration lead | Open |
| R-003 | Risk | OpportunityQuoteBridge | overlayering | Functional / technical lead | Open |
| D-003 | Dependency | OpportunityQuoteBridge | Requires architecture/business decision | Functional / technical lead | Open |
| R-004 | Risk | DataverseCustomerExport | direct-sql, overlayering | Integration lead | Open |
| D-004 | Dependency | DataverseCustomerExport | Requires architecture/business decision | Integration lead | Open |
| R-005 | Risk | PipelineConversionLegacy | overlayering, report-rationalization | Reporting lead | Open |
| R-006 | Risk | SalesManagerLegacyRole | overlayering | Security lead | Open |

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
| Risks | Amber | 10 risk flags detected. |
| Decisions | Amber | High-effort and retire decisions require owner confirmation. |

### steering-committee-pack.md

# Steering Committee Pack

| Metric | Value |
| --- | --- |
| Complexity | Medium |
| Score | 65 |
| High-risk items | 2 |
| Scope reduction candidates | 0 |
| Effort points | 50 |

## Decisions Needed

| ID | Decision | Owner | Due |
| --- | --- | --- | --- |
| DEC-001 | Approve Rebuild for AIFLeadToCashSync | Integration lead | Next steering |
| DEC-002 | Approve Rebuild for CustContactLegacyMap | Data migration lead | Next steering |
| DEC-003 | Approve Extend for OpportunityQuoteBridge | Functional / technical lead | Next steering |
| DEC-004 | Approve Rebuild for DataverseCustomerExport | Integration lead | Next steering |

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
| Wave 0 | Discovery and scope reduction | SalesManagerLegacyRole |
| Wave 1 | Standard/configuration and low-risk extensions | OpportunityQuoteBridge, PipelineConversionLegacy |
| Wave 2 | Complex rebuilds, integrations, ISVs | AIFLeadToCashSync, CustContactLegacyMap, DataverseCustomerExport |
| Wave 3 | Data migration, testing, cutover | Trial migrations, UAT, cutover rehearsal, go-live |
