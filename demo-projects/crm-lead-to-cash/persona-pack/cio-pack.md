# CIO Architecture Pack

## Readiness Score

| Persona | Score | Interpretation |
| --- | --- | --- |
| CIO | 61/100 | Needs control |

## Next Actions

- Reduce high-risk scope before committing delivery baseline.

## Included Evidence

### persona-cio-architecture-view.md

# CIO Architecture View

| Item | Domain | Target pattern | Architecture risk | Effort |
| --- | --- | --- | --- | --- |
| AIFLeadToCashSync | integration | OData, custom service, Business Events, or middleware | aif, overlayering | 11 |
| DataverseCustomerExport | integration | Data entity, export, reporting replica, or data lake pattern | direct-sql, overlayering | 11 |
| CustContactLegacyMap | data | Extension/service/data entity redesign | direct-sql, overlayering | 8 |
| OpportunityQuoteBridge | object | Chain of Command or event handler | overlayering | 8 |
| PipelineConversionLegacy | report | D365FO workspace, SSRS, Power BI, Financial Reporter, or archive | overlayering, report-rationalization | 7 |

## CIO Focus

- Remove unsupported legacy integration patterns.
- Reduce technical debt before cloud migration.
- Sequence high-risk rebuilds through architecture gates.

### ai-before-after-architecture.md

# AI Before / After Architecture

| Domain | Before AX | After D365FO |
| --- | --- | --- |
| Application | Dynamics AX legacy environment | Dynamics 365 Finance & Operations cloud environment |
| Integrations | AIFLeadToCashSync, DataverseCustomerExport | OData, custom services, Business Events, middleware, managed files |
| Reporting | PipelineConversionLegacy | D365FO workspaces, SSRS, Power BI, Financial Reporter, archive |
| Data | CustContactLegacyMap | Data entities, recurring data jobs, archive/reporting store |
| Security | AX groups/roles | D365FO roles, duties, privileges, SoD controls |
| ALM | Layer/model deployment | Packages, build validation, release pipeline, environment governance |

### ai-upgrade-path-decision.md

# AI Upgrade Path Decision

| Factor | Assessment |
| --- | --- |
| Complexity rating | Medium |
| Rebuild / ISV review count | 3 |
| Scope reduction candidates | 0 |
| Recommended approach | Hybrid or reimplementation-led approach |
| Required validation | Confirm source AX version, Microsoft-supported tooling, data volume, and customization inventory. |

### ai-dependency-graph.md

# AI Migration Dependency Graph

```mermaid
graph TD
  N_AIFLeadToCashSync["AIFLeadToCashSync"]
  N_module_CRM["CRM"] --> N_AIFLeadToCashSync
  N_AIFLeadToCashSync --> N_risk_aif["Risk: aif"]
  N_AIFLeadToCashSync --> N_risk_overlayering["Risk: overlayering"]
  N_AIFLeadToCashSync --> N_gate_integration["Integration workstream"]
  N_CustContactLegacyMap["CustContactLegacyMap"]
  N_module_Customer_Master["Customer Master"] --> N_CustContactLegacyMap
  N_CustContactLegacyMap --> N_risk_direct_sql["Risk: direct-sql"]
  N_CustContactLegacyMap --> N_risk_overlayering["Risk: overlayering"]
  N_CustContactLegacyMap --> N_gate_data["Data workstream"]
  N_OpportunityQuoteBridge["OpportunityQuoteBridge"]
  N_module_Sales["Sales"] --> N_OpportunityQuoteBridge
  N_OpportunityQuoteBridge --> N_risk_overlayering["Risk: overlayering"]
  N_DataverseCustomerExport["DataverseCustomerExport"]
  N_module_Dataverse["Dataverse"] --> N_DataverseCustomerExport
  N_DataverseCustomerExport --> N_risk_direct_sql["Risk: direct-sql"]
  N_DataverseCustomerExport --> N_risk_overlayering["Risk: overlayering"]
  N_DataverseCustomerExport --> N_gate_integration["Integration workstream"]
  N_PipelineConversionLegacy["PipelineConversionLegacy"]
  N_module_CRM["CRM"] --> N_PipelineConversionLegacy
  N_PipelineConversionLegacy --> N_risk_overlayering["Risk: overlayering"]
  N_PipelineConversionLegacy --> N_risk_report_rationalization["Risk: report-rationalization"]
  N_PipelineConversionLegacy --> N_gate_report["Report workstream"]
  N_SalesManagerLegacyRole["SalesManagerLegacyRole"]
  N_module_Sales["Sales"] --> N_SalesManagerLegacyRole
  N_SalesManagerLegacyRole --> N_risk_overlayering["Risk: overlayering"]
```

### ai-adrs.md

# Architecture Decision Records

| ID | Decision | Context | Decision | Status |
| --- | --- | --- | --- | --- |
| ADR-001 | Disposition for AIFLeadToCashSync | Legacy integrations usually need redesign for D365FO operations and monitoring. | Rebuild | Proposed |
| ADR-002 | Disposition for CustContactLegacyMap | Unsupported legacy dependency detected. | Rebuild | Proposed |
| ADR-003 | Disposition for OpportunityQuoteBridge | Customization likely needs extension-based migration. | Extend | Proposed |
| ADR-004 | Disposition for DataverseCustomerExport | Legacy integrations usually need redesign for D365FO operations and monitoring. | Rebuild | Proposed |
