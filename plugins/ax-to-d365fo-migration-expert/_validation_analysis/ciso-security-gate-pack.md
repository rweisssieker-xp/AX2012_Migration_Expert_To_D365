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
| AIFCustomerExport | integration | aif, overlayering | Review authentication, replay, monitoring, and least privilege for new integration. | CISO / security lead |
| LegacyWarehouseSupervisor | security | overlayering | Map roles, duties, privileges, and SoD controls. | CISO / security lead |
| InventTransHistory | data | direct-sql, posting | Replace direct data access with governed service/entity pattern. | CISO / security lead |
| SalesFormLetter_Extension | object | direct-sql, overlayering, posting, transaction-scope | Replace direct data access with governed service/entity pattern. | CISO / security lead |
