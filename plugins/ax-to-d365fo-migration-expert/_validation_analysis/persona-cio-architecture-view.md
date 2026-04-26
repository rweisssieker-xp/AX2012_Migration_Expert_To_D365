# CIO Architecture View

| Item | Domain | Target pattern | Architecture risk | Effort |
| --- | --- | --- | --- | --- |
| AIFCustomerExport | integration | OData, custom service, Business Events, or middleware | aif, overlayering | 11 |
| LegacyTaxAddon | isv | D365FO ISV successor, standard replacement, custom extension, or retire | overlayering | 11 |
| SalesFormLetter_Extension | object | Extension/service/data entity redesign | direct-sql, overlayering, posting, transaction-scope | 11 |
| InventTransHistory | data | Extension/service/data entity redesign | direct-sql, posting | 10 |
| SalesFormLetter_Extension | object | Chain of Command or event handler | overlayering, posting | 9 |
| WarehouseFileDrop | integration | Managed file integration through middleware or recurring data jobs | overlayering | 8 |
| CustTableLegacyCreditCheck | object | Business validation before migration | overlayering | 7 |
| InventAgingCustom | report | D365FO workspace, SSRS, Power BI, Financial Reporter, or archive | overlayering, report-rationalization | 7 |

## CIO Focus

- Remove unsupported legacy integration patterns.
- Reduce technical debt before cloud migration.
- Sequence high-risk rebuilds through architecture gates.
