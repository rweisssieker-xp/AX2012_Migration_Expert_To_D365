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

The migration currently rates **Medium** with a complexity score of **84**. The AI analysis identified **0** scope-reduction candidates, **0** high-risk items, and **18** risk flags.

## CEO Decisions Needed

| Decision | Why it matters |
| --- | --- |
| Approve scope-reduction mandate | Avoid migrating low-value customizations, reports, and historical data. |
| Confirm business standardization appetite | D365FO value depends on process simplification, not legacy recreation. |
| Assign executive owners for unresolved high-risk items | Risk decisions need accountable business leadership. |
| Confirm investment envelope | Current heuristic effort is 48.8 person-days before detailed planning. |

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

The current AI scan estimates **65 effort points** and highlights **0 scope-reduction opportunities**. The recommended path is controlled scope reduction before build commitment.

### ai-value-tracker.md

# AI Migration Value Tracker

| Item | Value lever | Avoidable points | Avoidable days | Indicative value |
| --- | --- | --- | --- | --- |

### ai-cost-model.md

# AI Migration Cost Model

| Metric | Value |
| --- | --- |
| Effort points | 65 |
| Base person-days | 48.8 |
| Risk multiplier | 1.15 |
| Adjusted person-days | 56.1 |
| Budget range | 45,270 - 66,574 |

### ai-risk-heatmap.md

# AI Migration Risk Heatmap

| Item | Workstream | Impact | Probability | Risk drivers |
| --- | --- | --- | --- | --- |
| LedgerJournalService | integration | Medium | High | overlayering, posting |
| FR_TaxSettlementBatch | object | Medium | High | batch, overlayering, posting |
| UK_VATMakingTaxDigital | integration | Medium | High | aif, overlayering |
| DE_EInvoiceAdapter | integration | Medium | Medium | overlayering |
| US_SalesTaxConnector | integration | Medium | Medium | integration-modernization |
| LegacyDataArchive | integration | Medium | Medium | overlayering |
| LocalLabelExtensions | integration | Medium | Medium | overlayering |
| IntercompanyOrderFlow | object | Medium | High | client-dependency, overlayering |
| GlobalCustomerMaster | object | Medium | High | client-dependency, overlayering |
| VendorBankValidation | object | Low | Medium | overlayering |
| SecurityRoleTemplate | security | Low | Medium | overlayering |
| CountryRolloutPMO | object | Low | Medium | overlayering |

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
