# AI Customization Disposition

| Name | Type | Category | Disposition | Target pattern | Risks | Effort | Rationale |
| --- | --- | --- | --- | --- | --- | --- | --- |
| AIFLeadToCashSync | Service | integration | Rebuild | OData, custom service, Business Events, or middleware | aif, overlayering | 11 | Legacy integrations usually need redesign for D365FO operations and monitoring. |
| DataverseCustomerExport | Interface | integration | Rebuild | Data entity, export, reporting replica, or data lake pattern | direct-sql, overlayering | 11 | Legacy integrations usually need redesign for D365FO operations and monitoring. |
| CustContactLegacyMap | Table | data | Rebuild | Extension/service/data entity redesign | direct-sql, overlayering | 8 | Unsupported legacy dependency detected. |
| OpportunityQuoteBridge | Class | object | Extend | Chain of Command or event handler | overlayering | 8 | Customization likely needs extension-based migration. |
| PipelineConversionLegacy | Report | report | Standard / Power BI Review | D365FO workspace, SSRS, Power BI, Financial Reporter, or archive | overlayering, report-rationalization | 7 | Reports should be rationalized before rebuild. |
| SalesManagerLegacyRole | Role | security | Map | D365FO roles, duties, privileges, and SoD review | overlayering | 5 | Security must be mapped rather than technically migrated as-is. |
