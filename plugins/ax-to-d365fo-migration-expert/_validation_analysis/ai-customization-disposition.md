# AI Customization Disposition

| Name | Type | Category | Disposition | Target pattern | Risks | Effort | Rationale |
| --- | --- | --- | --- | --- | --- | --- | --- |
| AIFCustomerExport | Service | integration | Rebuild | OData, custom service, Business Events, or middleware | aif, overlayering | 11 | Legacy integrations usually need redesign for D365FO operations and monitoring. |
| LegacyTaxAddon | Addon | isv | ISV Review | D365FO ISV successor, standard replacement, custom extension, or retire | overlayering | 11 | ISV capability needs product roadmap and licensing validation. |
| SalesFormLetter_Extension | Class | object | Rebuild | Extension/service/data entity redesign | direct-sql, overlayering, posting, transaction-scope | 11 | Unsupported legacy dependency detected. |
| InventTransHistory | Table | data | Rebuild | Extension/service/data entity redesign | direct-sql, posting | 10 | Unsupported legacy dependency detected. |
| SalesFormLetter_Extension | Class | object | Extend | Chain of Command or event handler | overlayering, posting | 9 | Customization likely needs extension-based migration. |
| WarehouseFileDrop | Interface | integration | Rebuild | Managed file integration through middleware or recurring data jobs | overlayering | 8 | Legacy integrations usually need redesign for D365FO operations and monitoring. |
| CustTableLegacyCreditCheck | Form | object | Retire Candidate | Business validation before migration | overlayering | 7 | Low usage suggests scope reduction opportunity. |
| InventAgingCustom | Report | report | Standard / Power BI Review | D365FO workspace, SSRS, Power BI, Financial Reporter, or archive | overlayering, report-rationalization | 7 | Reports should be rationalized before rebuild. |
| LegacyWarehouseSupervisor | Role | security | Map | D365FO roles, duties, privileges, and SoD review | overlayering | 3 | Security must be mapped rather than technically migrated as-is. |
