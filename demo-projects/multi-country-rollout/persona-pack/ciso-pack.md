# CISO Security Gate Pack

## Readiness Score

| Persona | Score | Interpretation |
| --- | --- | --- |
| CISO | 72/100 | Needs control |

## Next Actions

- Reduce high-risk scope before committing delivery baseline.

## Included Evidence

### persona-ciso-security-view.md

# CISO Security View

| Item | Area | Risk | Control / review | Owner |
| --- | --- | --- | --- | --- |
| UK_VATMakingTaxDigital | integration | aif, overlayering | Review authentication, replay, monitoring, and least privilege for new integration. | CISO / security lead |
| IntercompanyOrderFlow | object | client-dependency, overlayering | Remove local/client dependency and review endpoint/security model. | CISO / security lead |
| GlobalCustomerMaster | object | client-dependency, overlayering | Remove local/client dependency and review endpoint/security model. | CISO / security lead |
| SecurityRoleTemplate | security | overlayering | Map roles, duties, privileges, and SoD controls. | CISO / security lead |

### ciso-security-gate-pack.md

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
| UK_VATMakingTaxDigital | integration | aif, overlayering | Review authentication, replay, monitoring, and least privilege for new integration. | CISO / security lead |
| IntercompanyOrderFlow | object | client-dependency, overlayering | Remove local/client dependency and review endpoint/security model. | CISO / security lead |
| GlobalCustomerMaster | object | client-dependency, overlayering | Remove local/client dependency and review endpoint/security model. | CISO / security lead |
| SecurityRoleTemplate | security | overlayering | Map roles, duties, privileges, and SoD controls. | CISO / security lead |

### ai-quality-gates.md

# AI Migration Quality Gates

| Gate | Required evidence | Exit criteria | Current status |
| --- | --- | --- | --- |
| Readiness Gate | Inventory, scope, risks | No critical unknowns | On track |
| Design Gate | Fit-gap, target architecture, decisions | High-risk designs approved | On track |
| Build Gate | Backlog, estimates, dependencies | Build scope baselined | Proposed |
| Data Gate | Mappings, quality checks, reconciliation | Trial migration criteria approved | Proposed |
| UAT Gate | Test cases, roles, data, defects | Business acceptance criteria approved | Proposed |
| Cutover Gate | Runbook, rollback, smoke tests | Go/no-go criteria met | Proposed |

### ai-risk-mitigation-playbooks.md

# AI Risk-to-Mitigation Playbooks

| Risk | Mitigation playbook | Owner | When |
| --- | --- | --- | --- |
| aif | Redesign AIF services using OData, custom services, Business Events, or middleware. | Technical architect | Discovery / Solution design |
| batch | Align to SysOperation and D365FO batch operations with monitoring and retry behavior. | Technical architect | Discovery / Solution design |
| client-dependency | Remove COM, ActiveX, WinAPI, local file, and client-side dependencies. | Technical architect | Discovery / Solution design |
| integration-modernization | Define SLA, monitoring, replay, authentication, and support ownership. | Workstream lead | Discovery / Solution design |
| overlayering | Replace overlayered behavior with extensions, Chain of Command, and event handlers. | Technical architect | Discovery / Solution design |
| posting | Run senior architecture review for financial/inventory posting changes and reconciliation impact. | Solution architect / finance lead | Discovery / Solution design |

### ai-evidence-confidence.md

# AI Evidence Confidence Score

| Item | Recommendation | Confidence | Reason | Missing evidence |
| --- | --- | --- | --- | --- |
| LedgerJournalService | Rebuild | Medium | Inventory row supports a recommendation but needs workshop validation. | usage, business purpose |
| DE_EInvoiceAdapter | Rebuild | Medium | Inventory row supports a recommendation but needs workshop validation. | usage, business purpose |
| FR_TaxSettlementBatch | Extend | Medium | Inventory row supports a recommendation but needs workshop validation. | usage, business purpose |
| UK_VATMakingTaxDigital | Rebuild | Medium | Inventory row supports a recommendation but needs workshop validation. | usage, business purpose |
| US_SalesTaxConnector | Rebuild | Medium | Inventory row supports a recommendation but needs workshop validation. | usage, business purpose |
| IntercompanyOrderFlow | Rebuild | Medium | Inventory row supports a recommendation but needs workshop validation. | usage, business purpose |
| GlobalCustomerMaster | Rebuild | Medium | Inventory row supports a recommendation but needs workshop validation. | usage, business purpose |
| VendorBankValidation | Extend | Medium | Inventory row supports a recommendation but needs workshop validation. | usage, business purpose |
| SecurityRoleTemplate | Map | Medium | Inventory row supports a recommendation but needs workshop validation. | usage, business purpose |
| LegacyDataArchive | Rebuild | Medium | Inventory row supports a recommendation but needs workshop validation. | usage, business purpose |
| CountryRolloutPMO | Review | Medium | Inventory row supports a recommendation but needs workshop validation. | usage, business purpose |
| LocalLabelExtensions | Rebuild | Medium | Inventory row supports a recommendation but needs workshop validation. | usage, business purpose |
