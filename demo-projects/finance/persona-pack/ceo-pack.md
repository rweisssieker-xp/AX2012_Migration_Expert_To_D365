# CEO Board Pack

## Readiness Score

| Persona | Score | Interpretation |
| --- | --- | --- |
| CEO | 75/100 | Ready |

## Next Actions

- Proceed with gate review and maintain weekly evidence updates.

## Included Evidence

### persona-ceo-summary.md

# CEO Migration Summary

## Executive Position

The migration currently rates **Medium** with a complexity score of **46**. The AI analysis identified **1** scope-reduction candidates, **3** high-risk items, and **8** risk flags.

## CEO Decisions Needed

| Decision | Why it matters |
| --- | --- |
| Approve scope-reduction mandate | Avoid migrating low-value customizations, reports, and historical data. |
| Confirm business standardization appetite | D365FO value depends on process simplification, not legacy recreation. |
| Assign executive owners for unresolved high-risk items | Risk decisions need accountable business leadership. |
| Confirm investment envelope | Current heuristic effort is 30.8 person-days before detailed planning. |

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

The current AI scan estimates **41 effort points** and highlights **1 scope-reduction opportunities**. The recommended path is controlled scope reduction before build commitment.

### ai-value-tracker.md

# AI Migration Value Tracker

| Item | Value lever | Avoidable points | Avoidable days | Indicative value |
| --- | --- | --- | --- | --- |
| DimensionLegacyEditor | Retire Candidate | 7 | 5.2 | 4988 |
| TaxAuditPack | Standard / Power BI Review | 9 | 6.8 | 6412 |

### ai-cost-model.md

# AI Migration Cost Model

| Metric | Value |
| --- | --- |
| Effort points | 41 |
| Base person-days | 30.8 |
| Risk multiplier | 1.15 |
| Adjusted person-days | 35.4 |
| Budget range | 28,555 - 41,993 |

### ai-risk-heatmap.md

# AI Migration Risk Heatmap

| Item | Workstream | Impact | Probability | Risk drivers |
| --- | --- | --- | --- | --- |
| GLTrialBalanceSqlExport | integration | High | High | direct-sql, overlayering |
| LedgerJournalPostOverride | object | High | High | overlayering, posting |
| TaxAuditPack | report | High | High | overlayering, report-rationalization |
| DimensionLegacyEditor | object | Medium | Medium | overlayering |
| LegacyFinanceController | security | Medium | Medium | overlayering |

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
