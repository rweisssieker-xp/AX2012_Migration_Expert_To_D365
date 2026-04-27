# AI Migration Risk Radar

| Item | Category | Risk flags | Recommendation | Reason |
| --- | --- | --- | --- | --- |
| ProdCostRollupCustom | object | overlayering | Extend | Customization likely needs extension-based migration. |
| BOMCalcHistory | object | direct-sql | Rebuild | Unsupported legacy dependency detected. |
| AIFProductionOrderImport | integration | aif, overlayering | Rebuild | Legacy integrations usually need redesign for D365FO operations and monitoring. |
| ProdVarianceLegacy | report | overlayering, report-rationalization | Standard / Power BI Review | Reports should be rationalized before rebuild. |
| ShopFloorAddon | isv | overlayering | ISV Review | ISV capability needs product roadmap and licensing validation. |
