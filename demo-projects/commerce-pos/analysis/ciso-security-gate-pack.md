# CISO Security Gate Pack

| Gate | Evidence | Timing | Status |
| --- | --- | --- | --- |
| Identity and access | Roles/duties mapped | Required before UAT | Open |
| SoD | Segregation of duties reviewed | Required before UAT | Open |
| Integrations | Auth, secrets, monitoring, replay reviewed | Required before SIT | Open |
| Sensitive data | GDPR/DSGVO and retention reviewed | Required before data migration trial | Open |
| Go-live | Privileged access and emergency access reviewed | Required before cutover | Open |

## Security Items

# CISO Security View

| Item | Area | Risk | Control / review | Owner |
| --- | --- | --- | --- | --- |
| RetailPriceOverride | object | client-dependency, overlayering | Remove local/client dependency and review endpoint/security model. | CISO / security lead |
| CSUChannelSyncMonitor | integration | client-dependency, overlayering | Remove local/client dependency and review endpoint/security model. | CISO / security lead |
| RetailTransactionHistory | data | client-dependency, direct-sql | Replace direct data access with governed service/entity pattern. | CISO / security lead |
| StoreManagerLegacyRole | security | overlayering | Map roles, duties, privileges, and SoD controls. | CISO / security lead |
