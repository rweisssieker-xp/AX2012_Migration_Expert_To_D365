# AI Migration Risk Radar

| Item | Category | Risk flags | Recommendation | Reason |
| --- | --- | --- | --- | --- |
| RetailPriceOverride | object | client-dependency, overlayering | Rebuild | Unsupported legacy dependency detected. |
| CSUChannelSyncMonitor | integration | client-dependency, overlayering | Rebuild | Legacy integrations usually need redesign for D365FO operations and monitoring. |
| POSOfflineRecoveryForm | object | overlayering | Extend | Customization likely needs extension-based migration. |
| PaymentTerminalConnector | integration | overlayering, posting | Rebuild | Legacy integrations usually need redesign for D365FO operations and monitoring. |
| LoyaltyLiabilityReport | report | overlayering, report-rationalization | Standard / Power BI Review | Reports should be rationalized before rebuild. |
| RetailTransactionHistory | data | client-dependency, direct-sql | Rebuild | Unsupported legacy dependency detected. |
| StoreManagerLegacyRole | security | overlayering | Map | Security must be mapped rather than technically migrated as-is. |
