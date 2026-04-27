# CIO Architecture View

| Item | Domain | Target pattern | Architecture risk | Effort |
| --- | --- | --- | --- | --- |
| CSUChannelSyncMonitor | integration | Middleware-backed D365FO integration pattern | client-dependency, overlayering | 11 |
| PaymentTerminalConnector | integration | Middleware-backed D365FO integration pattern | overlayering, posting | 11 |
| RetailTransactionHistory | data | Extension/service/data entity redesign | client-dependency, direct-sql | 10 |
| RetailPriceOverride | object | Extension/service/data entity redesign | client-dependency, overlayering | 9 |
| POSOfflineRecoveryForm | object | Form extension plus event handlers | overlayering | 9 |
| LoyaltyLiabilityReport | report | D365FO workspace, SSRS, Power BI, Financial Reporter, or archive | overlayering, report-rationalization | 7 |

## CIO Focus

- Remove unsupported legacy integration patterns.
- Reduce technical debt before cloud migration.
- Sequence high-risk rebuilds through architecture gates.
