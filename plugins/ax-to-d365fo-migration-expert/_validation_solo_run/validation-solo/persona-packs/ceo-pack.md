# CEO Board Pack

## Readiness Score

| Persona | Score | Interpretation |
| --- | --- | --- |
| CEO | 74/100 | Needs control |

## Next Actions

- Proceed with gate review and maintain weekly evidence updates.

## Included Evidence

### persona-ceo-summary.md

# CEO Migration Summary

## Executive Position

The migration currently rates **High** with a complexity score of **96**. The AI analysis identified **1** scope-reduction candidates, **5** high-risk items, and **16** risk flags.

## CEO Decisions Needed

| Decision | Why it matters |
| --- | --- |
| Approve scope-reduction mandate | Avoid migrating low-value customizations, reports, and historical data. |
| Confirm business standardization appetite | D365FO value depends on process simplification, not legacy recreation. |
| Assign executive owners for unresolved high-risk items | Risk decisions need accountable business leadership. |
| Confirm investment envelope | Current heuristic effort is 57.8 person-days before detailed planning. |

## Board-Level Message

The migration should be governed as a business simplification and risk-reduction program, not only as an ERP technical move.

### board-ceo-narrative.md

# Board / CEO Narrative

## Why Migrate

The AX estate carries technical and operational risk that increases cost, slows change, and limits supportability.

## Why Now

D365FO migration is an opportunity to retire low-value scope, standardize processes, modernize integrations, and improve security governance.

## Risk of Doing Nothing

Legacy customizations, direct integrations, aging reports, and unclear data history requirements will continue to increase operational risk.

## Investment Logic

The current AI scan estimates **77 effort points** and highlights **1 scope-reduction opportunities**. The recommended path is controlled scope reduction before build commitment.

### ai-value-tracker.md

# AI Migration Value Tracker

| Item | Value lever | Avoidable points | Avoidable days | Indicative value |
| --- | --- | --- | --- | --- |
| CustTableLegacyCreditCheck | Retire Candidate | 7 | 5.2 | 4988 |
| InventAgingCustom | Standard / Power BI Review | 7 | 5.2 | 4988 |
| LegacyTaxAddon | ISV Review | 11 | 8.2 | 7838 |

### ai-cost-model.md

# AI Migration Cost Model

| Metric | Value |
| --- | --- |
| Effort points | 77 |
| Base person-days | 57.8 |
| Risk multiplier | 1.3 |
| Adjusted person-days | 75.1 |
| Budget range | 60,623 - 89,152 |

### ai-risk-heatmap.md

# AI Migration Risk Heatmap

| Item | Workstream | Impact | Probability | Risk drivers |
| --- | --- | --- | --- | --- |
| AIFCustomerExport | integration | High | High | aif, overlayering |
| LegacyTaxAddon | isv | High | Medium | overlayering |
| SalesFormLetter_Extension | object | High | High | direct-sql, overlayering, posting, transaction-scope |
| InventTransHistory | data | High | High | direct-sql, posting |
| SalesFormLetter_Extension | object | High | High | overlayering, posting |
| WarehouseFileDrop | integration | Medium | Medium | overlayering |
| CustTableLegacyCreditCheck | object | Medium | Medium | overlayering |
| InventAgingCustom | report | Medium | High | overlayering, report-rationalization |
| LegacyWarehouseSupervisor | security | Low | Medium | overlayering |

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
