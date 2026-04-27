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

The migration currently rates **Medium** with a complexity score of **73**. The AI analysis identified **0** scope-reduction candidates, **5** high-risk items, and **12** risk flags.

## CEO Decisions Needed

| Decision | Why it matters |
| --- | --- |
| Approve scope-reduction mandate | Avoid migrating low-value customizations, reports, and historical data. |
| Confirm business standardization appetite | D365FO value depends on process simplification, not legacy recreation. |
| Assign executive owners for unresolved high-risk items | Risk decisions need accountable business leadership. |
| Confirm investment envelope | Current heuristic effort is 46.5 person-days before detailed planning. |

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

The current AI scan estimates **62 effort points** and highlights **0 scope-reduction opportunities**. The recommended path is controlled scope reduction before build commitment.

### ai-value-tracker.md

# AI Migration Value Tracker

| Item | Value lever | Avoidable points | Avoidable days | Indicative value |
| --- | --- | --- | --- | --- |
| LoyaltyLiabilityReport | Standard / Power BI Review | 7 | 5.2 | 4988 |

### ai-cost-model.md

# AI Migration Cost Model

| Metric | Value |
| --- | --- |
| Effort points | 62 |
| Base person-days | 46.5 |
| Risk multiplier | 1.15 |
| Adjusted person-days | 53.5 |
| Budget range | 43,181 - 63,502 |

### ai-risk-heatmap.md

# AI Migration Risk Heatmap

| Item | Workstream | Impact | Probability | Risk drivers |
| --- | --- | --- | --- | --- |
| CSUChannelSyncMonitor | integration | High | High | client-dependency, overlayering |
| PaymentTerminalConnector | integration | High | High | overlayering, posting |
| RetailTransactionHistory | data | High | High | client-dependency, direct-sql |
| RetailPriceOverride | object | High | High | client-dependency, overlayering |
| POSOfflineRecoveryForm | object | High | Medium | overlayering |
| LoyaltyLiabilityReport | report | Medium | High | overlayering, report-rationalization |
| StoreManagerLegacyRole | security | Medium | Medium | overlayering |

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
