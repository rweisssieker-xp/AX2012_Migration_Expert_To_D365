# AI Migration Risk Radar

| Item | Category | Risk flags | Recommendation | Reason |
| --- | --- | --- | --- | --- |
| SalesFormLetter_Extension | object | overlayering, posting | Extend | Customization likely needs extension-based migration. |
| CustTableLegacyCreditCheck | object | overlayering | Retire Candidate | Low usage suggests scope reduction opportunity. |
| AIFCustomerExport | integration | aif, overlayering | Rebuild | Legacy integrations usually need redesign for D365FO operations and monitoring. |
| WarehouseFileDrop | integration | overlayering | Rebuild | Legacy integrations usually need redesign for D365FO operations and monitoring. |
| InventAgingCustom | report | overlayering, report-rationalization | Standard / Power BI Review | Reports should be rationalized before rebuild. |
| LegacyTaxAddon | isv | overlayering | ISV Review | ISV capability needs product roadmap and licensing validation. |
| LegacyWarehouseSupervisor | security | overlayering | Map | Security must be mapped rather than technically migrated as-is. |
| InventTransHistory | data | direct-sql, posting | Rebuild | Unsupported legacy dependency detected. |
