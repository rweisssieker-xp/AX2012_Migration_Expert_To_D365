# CIO Architecture View

| Item | Domain | Target pattern | Architecture risk | Effort |
| --- | --- | --- | --- | --- |
| AIFProductionOrderImport | integration | OData, custom service, Business Events, or middleware | aif, overlayering | 11 |
| ShopFloorAddon | isv | D365FO ISV successor, standard replacement, custom extension, or retire | overlayering | 11 |
| ProdCostRollupCustom | object | Chain of Command or event handler | overlayering | 8 |
| ProdVarianceLegacy | report | D365FO workspace, SSRS, Power BI, Financial Reporter, or archive | overlayering, report-rationalization | 7 |
| BOMCalcHistory | object | Extension/service/data entity redesign | direct-sql | 6 |

## CIO Focus

- Remove unsupported legacy integration patterns.
- Reduce technical debt before cloud migration.
- Sequence high-risk rebuilds through architecture gates.
