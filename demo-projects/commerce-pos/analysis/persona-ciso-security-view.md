# CISO Security View

| Item | Area | Risk | Control / review | Owner |
| --- | --- | --- | --- | --- |
| RetailPriceOverride | object | client-dependency, overlayering | Remove local/client dependency and review endpoint/security model. | CISO / security lead |
| CSUChannelSyncMonitor | integration | client-dependency, overlayering | Remove local/client dependency and review endpoint/security model. | CISO / security lead |
| RetailTransactionHistory | data | client-dependency, direct-sql | Replace direct data access with governed service/entity pattern. | CISO / security lead |
| StoreManagerLegacyRole | security | overlayering | Map roles, duties, privileges, and SoD controls. | CISO / security lead |
