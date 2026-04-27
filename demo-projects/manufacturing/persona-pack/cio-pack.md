# CIO Architecture Pack

## Readiness Score

| Persona | Score | Interpretation |
| --- | --- | --- |
| CIO | 66/100 | Needs control |

## Next Actions

- Reduce high-risk scope before committing delivery baseline.

## Included Evidence

### persona-cio-architecture-view.md

# CIO Architecture View

| Item | Domain | Target pattern | Architecture risk | Effort |
| --- | --- | --- | --- | --- |
| AIFProductionOrderImport | integration | OData, custom service, Business Events, or middleware | aif, overlayering | 11 |
| ShopFloorAddon | isv | D365FO ISV successor, standard replacement, custom extension, or retire | overlayering | 11 |
| ProdCostRollupCustom | object | Chain of Command or event handler | overlayering | 8 |
| ProdVarianceLegacy | report | D365FO workspace, SSRS, Power BI, Financial Reporter, or archive | overlayering, report-rationalization | 7 |
| BOMCalcHistory | object | Extension/service/data entity redesign | direct-sql | 6 |

## CIO Focus

- Remove unsupported legacy integration patterns.
- Reduce technical debt before cloud migration.
- Sequence high-risk rebuilds through architecture gates.

### ai-before-after-architecture.md

# AI Before / After Architecture

| Domain | Before AX | After D365FO |
| --- | --- | --- |
| Application | Dynamics AX legacy environment | Dynamics 365 Finance & Operations cloud environment |
| Integrations | AIFProductionOrderImport | OData, custom services, Business Events, middleware, managed files |
| Reporting | ProdVarianceLegacy | D365FO workspaces, SSRS, Power BI, Financial Reporter, archive |
| Data | Legacy data domains not inventoried | Data entities, recurring data jobs, archive/reporting store |
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
  N_ProdCostRollupCustom["ProdCostRollupCustom"]
  N_module_Manufacturing["Manufacturing"] --> N_ProdCostRollupCustom
  N_ProdCostRollupCustom --> N_risk_overlayering["Risk: overlayering"]
  N_BOMCalcHistory["BOMCalcHistory"]
  N_module_Manufacturing["Manufacturing"] --> N_BOMCalcHistory
  N_BOMCalcHistory --> N_risk_direct_sql["Risk: direct-sql"]
  N_AIFProductionOrderImport["AIFProductionOrderImport"]
  N_module_Manufacturing["Manufacturing"] --> N_AIFProductionOrderImport
  N_AIFProductionOrderImport --> N_risk_aif["Risk: aif"]
  N_AIFProductionOrderImport --> N_risk_overlayering["Risk: overlayering"]
  N_AIFProductionOrderImport --> N_gate_integration["Integration workstream"]
  N_ProdVarianceLegacy["ProdVarianceLegacy"]
  N_module_Manufacturing["Manufacturing"] --> N_ProdVarianceLegacy
  N_ProdVarianceLegacy --> N_risk_overlayering["Risk: overlayering"]
  N_ProdVarianceLegacy --> N_risk_report_rationalization["Risk: report-rationalization"]
  N_ProdVarianceLegacy --> N_gate_report["Report workstream"]
  N_ShopFloorAddon["ShopFloorAddon"]
  N_module_Manufacturing["Manufacturing"] --> N_ShopFloorAddon
  N_ShopFloorAddon --> N_risk_overlayering["Risk: overlayering"]
```

### ai-adrs.md

# Architecture Decision Records

| ID | Decision | Context | Decision | Status |
| --- | --- | --- | --- | --- |
| ADR-001 | Disposition for ProdCostRollupCustom | Customization likely needs extension-based migration. | Extend | Proposed |
| ADR-002 | Disposition for AIFProductionOrderImport | Legacy integrations usually need redesign for D365FO operations and monitoring. | Rebuild | Proposed |
| ADR-003 | Disposition for ShopFloorAddon | ISV capability needs product roadmap and licensing validation. | ISV Review | Proposed |
