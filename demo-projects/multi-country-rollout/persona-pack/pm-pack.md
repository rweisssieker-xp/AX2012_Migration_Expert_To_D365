# Project Manager Control Pack

## Readiness Score

| Persona | Score | Interpretation |
| --- | --- | --- |
| PM | 69/100 | Needs control |

## Next Actions

- Reduce high-risk scope before committing delivery baseline.

## Included Evidence

### persona-project-manager-control-view.md

# Project Manager Control View

| Control | Value | Owner | Action |
| --- | --- | --- | --- |
| Complexity | Medium | Program Manager | Track weekly |
| High-risk items | 0 | Workstream leads | Escalate blockers |
| Open decisions | 0 | Steering committee | Decision log |
| Scope reduction candidates | 0 | Business owners | Validate in workshops |

### raid-log.md

# RAID Log

| ID | Type | Item | Description | Owner | Status |
| --- | --- | --- | --- | --- | --- |
| R-001 | Risk | LedgerJournalService | overlayering, posting | Integration lead | Open |
| R-002 | Risk | DE_EInvoiceAdapter | overlayering | Integration lead | Open |
| R-003 | Risk | FR_TaxSettlementBatch | batch, overlayering, posting | Functional / technical lead | Open |
| R-004 | Risk | UK_VATMakingTaxDigital | aif, overlayering | Integration lead | Open |
| R-005 | Risk | US_SalesTaxConnector | integration-modernization | Integration lead | Open |
| R-006 | Risk | IntercompanyOrderFlow | client-dependency, overlayering | Functional / technical lead | Open |
| R-007 | Risk | GlobalCustomerMaster | client-dependency, overlayering | Functional / technical lead | Open |
| R-008 | Risk | VendorBankValidation | overlayering | Functional / technical lead | Open |
| R-009 | Risk | SecurityRoleTemplate | overlayering | Security lead | Open |
| R-010 | Risk | LegacyDataArchive | overlayering | Integration lead | Open |
| R-011 | Risk | CountryRolloutPMO | overlayering | Functional / technical lead | Open |
| R-012 | Risk | LocalLabelExtensions | overlayering | Integration lead | Open |

### raci-matrix.md

# RACI Matrix

| Workstream | Responsible | Accountable | Consulted | Informed |
| --- | --- | --- | --- | --- |
| Integration | Integration lead | Solution architect | Business owner | Program manager |
| Object | Functional / technical lead | Solution architect | Business owner | Program manager |
| Security | Security lead | Solution architect | Business owner | Program manager |

### weekly-status-report.md

# Weekly Status Report

| Area | Status | Comment |
| --- | --- | --- |
| Overall | Amber | Complexity is Medium. |
| Scope | Amber | 0 scope-reduction candidates need validation. |
| Risks | Amber | 18 risk flags detected. |
| Decisions | Amber | High-effort and retire decisions require owner confirmation. |

### steering-committee-pack.md

# Steering Committee Pack

| Metric | Value |
| --- | --- |
| Complexity | Medium |
| Score | 84 |
| High-risk items | 0 |
| Scope reduction candidates | 0 |
| Effort points | 65 |

## Decisions Needed

| ID | Decision | Owner | Due |
| --- | --- | --- | --- |

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
| Wave 0 | Discovery and scope reduction | SecurityRoleTemplate, CountryRolloutPMO |
| Wave 1 | Standard/configuration and low-risk extensions | FR_TaxSettlementBatch, VendorBankValidation |
| Wave 2 | Complex rebuilds, integrations, ISVs | LedgerJournalService, DE_EInvoiceAdapter, UK_VATMakingTaxDigital, US_SalesTaxConnector, IntercompanyOrderFlow, GlobalCustomerMaster, LegacyDataArchive, LocalLabelExtensions |
| Wave 3 | Data migration, testing, cutover | Trial migrations, UAT, cutover rehearsal, go-live |
