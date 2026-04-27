# AI Customization Disposition

| Name | Type | Category | Disposition | Target pattern | Risks | Effort | Rationale |
| --- | --- | --- | --- | --- | --- | --- | --- |
| AIFProductionOrderImport | Service | integration | Rebuild | OData, custom service, Business Events, or middleware | aif, overlayering | 11 | Legacy integrations usually need redesign for D365FO operations and monitoring. |
| ShopFloorAddon | Addon | isv | ISV Review | D365FO ISV successor, standard replacement, custom extension, or retire | overlayering | 11 | ISV capability needs product roadmap and licensing validation. |
| ProdCostRollupCustom | Class | object | Extend | Chain of Command or event handler | overlayering | 8 | Customization likely needs extension-based migration. |
| ProdVarianceLegacy | Report | report | Standard / Power BI Review | D365FO workspace, SSRS, Power BI, Financial Reporter, or archive | overlayering, report-rationalization | 7 | Reports should be rationalized before rebuild. |
| BOMCalcHistory | Table | object | Rebuild | Extension/service/data entity redesign | direct-sql | 6 | Unsupported legacy dependency detected. |
