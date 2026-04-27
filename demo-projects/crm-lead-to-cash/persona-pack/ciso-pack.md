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
| AIFLeadToCashSync | integration | aif, overlayering | Review authentication, replay, monitoring, and least privilege for new integration. | CISO / security lead |
| CustContactLegacyMap | data | direct-sql, overlayering | Replace direct data access with governed service/entity pattern. | CISO / security lead |
| DataverseCustomerExport | integration | direct-sql, overlayering | Replace direct data access with governed service/entity pattern. | CISO / security lead |
| SalesManagerLegacyRole | security | overlayering | Map roles, duties, privileges, and SoD controls. | CISO / security lead |

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
| AIFLeadToCashSync | integration | aif, overlayering | Review authentication, replay, monitoring, and least privilege for new integration. | CISO / security lead |
| CustContactLegacyMap | data | direct-sql, overlayering | Replace direct data access with governed service/entity pattern. | CISO / security lead |
| DataverseCustomerExport | integration | direct-sql, overlayering | Replace direct data access with governed service/entity pattern. | CISO / security lead |
| SalesManagerLegacyRole | security | overlayering | Map roles, duties, privileges, and SoD controls. | CISO / security lead |

### ai-quality-gates.md

# AI Migration Quality Gates

| Gate | Required evidence | Exit criteria | Current status |
| --- | --- | --- | --- |
| Readiness Gate | Inventory, scope, risks | No critical unknowns | On track |
| Design Gate | Fit-gap, target architecture, decisions | High-risk designs approved | At risk |
| Build Gate | Backlog, estimates, dependencies | Build scope baselined | Proposed |
| Data Gate | Mappings, quality checks, reconciliation | Trial migration criteria approved | Proposed |
| UAT Gate | Test cases, roles, data, defects | Business acceptance criteria approved | Proposed |
| Cutover Gate | Runbook, rollback, smoke tests | Go/no-go criteria met | Proposed |

### ai-risk-mitigation-playbooks.md

# AI Risk-to-Mitigation Playbooks

| Risk | Mitigation playbook | Owner | When |
| --- | --- | --- | --- |
| aif | Redesign AIF services using OData, custom services, Business Events, or middleware. | Technical architect | Discovery / Solution design |
| direct-sql | Replace direct SQL with data entities, custom services, export patterns, or reporting replicas. | Technical architect | Discovery / Solution design |
| overlayering | Replace overlayered behavior with extensions, Chain of Command, and event handlers. | Technical architect | Discovery / Solution design |
| report-rationalization | Validate usage and replace with standard reports, workspaces, Power BI, or archive access. | Reporting lead | Discovery / Solution design |

### ai-evidence-confidence.md

# AI Evidence Confidence Score

| Item | Recommendation | Confidence | Reason | Missing evidence |
| --- | --- | --- | --- | --- |
| AIFLeadToCashSync | Rebuild | High | Inventory row contains strong classification evidence. | none |
| CustContactLegacyMap | Rebuild | High | Inventory row contains strong classification evidence. | none |
| OpportunityQuoteBridge | Extend | High | Inventory row contains strong classification evidence. | none |
| DataverseCustomerExport | Rebuild | High | Inventory row contains strong classification evidence. | none |
| PipelineConversionLegacy | Standard / Power BI Review | High | Inventory row contains strong classification evidence. | none |
| SalesManagerLegacyRole | Map | High | Inventory row contains strong classification evidence. | none |
