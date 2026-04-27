# Project Manager Control Pack

## Readiness Score

| Persona | Score | Interpretation |
| --- | --- | --- |
| PM | 80/100 | Ready |

## Next Actions

- Proceed with gate review and maintain weekly evidence updates.

## Included Evidence

### persona-project-manager-control-view.md

# Project Manager Control View

| Control | Value | Owner | Action |
| --- | --- | --- | --- |
| Complexity | Medium | Program Manager | Track weekly |
| High-risk items | 3 | Workstream leads | Escalate blockers |
| Open decisions | 4 | Steering committee | Decision log |
| Scope reduction candidates | 1 | Business owners | Validate in workshops |

### raid-log.md

# RAID Log

| ID | Type | Item | Description | Owner | Status |
| --- | --- | --- | --- | --- | --- |
| R-001 | Risk | LedgerJournalPostOverride | overlayering, posting | Functional / technical lead | Open |
| D-001 | Dependency | LedgerJournalPostOverride | Requires architecture/business decision | Functional / technical lead | Open |
| R-002 | Risk | DimensionLegacyEditor | overlayering | Functional / technical lead | Open |
| R-003 | Risk | GLTrialBalanceSqlExport | direct-sql, overlayering | Integration lead | Open |
| D-003 | Dependency | GLTrialBalanceSqlExport | Requires architecture/business decision | Integration lead | Open |
| R-004 | Risk | TaxAuditPack | overlayering, report-rationalization | Reporting lead | Open |
| D-004 | Dependency | TaxAuditPack | Requires architecture/business decision | Reporting lead | Open |
| R-005 | Risk | LegacyFinanceController | overlayering | Security lead | Open |

### raci-matrix.md

# RACI Matrix

| Workstream | Responsible | Accountable | Consulted | Informed |
| --- | --- | --- | --- | --- |
| Integration | Integration lead | Solution architect | Business owner | Program manager |
| Object | Functional / technical lead | Solution architect | Business owner | Program manager |
| Report | Reporting lead | Solution architect | Business owner | Program manager |
| Security | Security lead | Solution architect | Business owner | Program manager |

### weekly-status-report.md

# Weekly Status Report

| Area | Status | Comment |
| --- | --- | --- |
| Overall | Amber | Complexity is Medium. |
| Scope | Amber | 1 scope-reduction candidates need validation. |
| Risks | Amber | 8 risk flags detected. |
| Decisions | Amber | High-effort and retire decisions require owner confirmation. |

### steering-committee-pack.md

# Steering Committee Pack

| Metric | Value |
| --- | --- |
| Complexity | Medium |
| Score | 46 |
| High-risk items | 3 |
| Scope reduction candidates | 1 |
| Effort points | 41 |

## Decisions Needed

| ID | Decision | Owner | Due |
| --- | --- | --- | --- |
| DEC-001 | Approve Extend for LedgerJournalPostOverride | Functional / technical lead | Next steering |
| DEC-002 | Approve Retire Candidate for DimensionLegacyEditor | Functional / technical lead | Next steering |
| DEC-003 | Approve Rebuild for GLTrialBalanceSqlExport | Integration lead | Next steering |
| DEC-004 | Approve Standard / Power BI Review for TaxAuditPack | Reporting lead | Next steering |

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
| Wave 0 | Discovery and scope reduction | DimensionLegacyEditor, LegacyFinanceController |
| Wave 1 | Standard/configuration and low-risk extensions | LedgerJournalPostOverride, TaxAuditPack |
| Wave 2 | Complex rebuilds, integrations, ISVs | GLTrialBalanceSqlExport |
| Wave 3 | Data migration, testing, cutover | Trial migrations, UAT, cutover rehearsal, go-live |
