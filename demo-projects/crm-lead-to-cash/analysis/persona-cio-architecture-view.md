# CIO Architecture View

| Item | Domain | Target pattern | Architecture risk | Effort |
| --- | --- | --- | --- | --- |
| AIFLeadToCashSync | integration | OData, custom service, Business Events, or middleware | aif, overlayering | 11 |
| DataverseCustomerExport | integration | Data entity, export, reporting replica, or data lake pattern | direct-sql, overlayering | 11 |
| CustContactLegacyMap | data | Extension/service/data entity redesign | direct-sql, overlayering | 8 |
| OpportunityQuoteBridge | object | Chain of Command or event handler | overlayering | 8 |
| PipelineConversionLegacy | report | D365FO workspace, SSRS, Power BI, Financial Reporter, or archive | overlayering, report-rationalization | 7 |

## CIO Focus

- Remove unsupported legacy integration patterns.
- Reduce technical debt before cloud migration.
- Sequence high-risk rebuilds through architecture gates.
