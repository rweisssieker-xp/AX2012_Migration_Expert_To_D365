# AI Migration Risk Radar

| Item | Category | Risk flags | Recommendation | Reason |
| --- | --- | --- | --- | --- |
| AIFLeadToCashSync | integration | aif, overlayering | Rebuild | Legacy integrations usually need redesign for D365FO operations and monitoring. |
| CustContactLegacyMap | data | direct-sql, overlayering | Rebuild | Unsupported legacy dependency detected. |
| OpportunityQuoteBridge | object | overlayering | Extend | Customization likely needs extension-based migration. |
| DataverseCustomerExport | integration | direct-sql, overlayering | Rebuild | Legacy integrations usually need redesign for D365FO operations and monitoring. |
| PipelineConversionLegacy | report | overlayering, report-rationalization | Standard / Power BI Review | Reports should be rationalized before rebuild. |
| SalesManagerLegacyRole | security | overlayering | Map | Security must be mapped rather than technically migrated as-is. |
