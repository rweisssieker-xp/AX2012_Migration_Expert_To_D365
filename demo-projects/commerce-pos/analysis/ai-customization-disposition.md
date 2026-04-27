# AI Customization Disposition

| Name | Type | Category | Disposition | Target pattern | Risks | Effort | Rationale |
| --- | --- | --- | --- | --- | --- | --- | --- |
| CSUChannelSyncMonitor | Service | integration | Rebuild | Middleware-backed D365FO integration pattern | client-dependency, overlayering | 11 | Legacy integrations usually need redesign for D365FO operations and monitoring. |
| PaymentTerminalConnector | Interface | integration | Rebuild | Middleware-backed D365FO integration pattern | overlayering, posting | 11 | Legacy integrations usually need redesign for D365FO operations and monitoring. |
| RetailTransactionHistory | Table | data | Rebuild | Extension/service/data entity redesign | client-dependency, direct-sql | 10 | Unsupported legacy dependency detected. |
| RetailPriceOverride | Class | object | Rebuild | Extension/service/data entity redesign | client-dependency, overlayering | 9 | Unsupported legacy dependency detected. |
| POSOfflineRecoveryForm | Form | object | Extend | Form extension plus event handlers | overlayering | 9 | Customization likely needs extension-based migration. |
| LoyaltyLiabilityReport | Report | report | Standard / Power BI Review | D365FO workspace, SSRS, Power BI, Financial Reporter, or archive | overlayering, report-rationalization | 7 | Reports should be rationalized before rebuild. |
| StoreManagerLegacyRole | Role | security | Map | D365FO roles, duties, privileges, and SoD review | overlayering | 5 | Security must be mapped rather than technically migrated as-is. |
