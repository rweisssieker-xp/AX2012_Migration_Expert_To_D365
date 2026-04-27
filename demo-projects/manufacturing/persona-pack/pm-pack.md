# Project Manager Control Pack

## Readiness Score

| Persona | Score | Interpretation |
| --- | --- | --- |
| PM | 82/100 | Ready |

## Next Actions

- Proceed with gate review and maintain weekly evidence updates.

## Included Evidence

### persona-project-manager-control-view.md

# Project Manager Control View

| Control | Value | Owner | Action |
| --- | --- | --- | --- |
| Complexity | Medium | Program Manager | Track weekly |
| High-risk items | 2 | Workstream leads | Escalate blockers |
| Open decisions | 3 | Steering committee | Decision log |
| Scope reduction candidates | 0 | Business owners | Validate in workshops |

### raid-log.md

# RAID Log

| ID | Type | Item | Description | Owner | Status |
| --- | --- | --- | --- | --- | --- |
| R-001 | Risk | ProdCostRollupCustom | overlayering | Functional / technical lead | Open |
| D-001 | Dependency | ProdCostRollupCustom | Requires architecture/business decision | Functional / technical lead | Open |
| R-002 | Risk | BOMCalcHistory | direct-sql | Functional / technical lead | Open |
| R-003 | Risk | AIFProductionOrderImport | aif, overlayering | Integration lead | Open |
| D-003 | Dependency | AIFProductionOrderImport | Requires architecture/business decision | Integration lead | Open |
| R-004 | Risk | ProdVarianceLegacy | overlayering, report-rationalization | Reporting lead | Open |
| R-005 | Risk | ShopFloorAddon | overlayering | Solution architect | Open |
| D-005 | Dependency | ShopFloorAddon | Requires architecture/business decision | Solution architect | Open |

### raci-matrix.md

# RACI Matrix

| Workstream | Responsible | Accountable | Consulted | Informed |
| --- | --- | --- | --- | --- |
| Integration | Integration lead | Solution architect | Business owner | Program manager |
| Isv | Solution architect | Solution architect | Business owner | Program manager |
| Object | Functional / technical lead | Solution architect | Business owner | Program manager |
| Report | Reporting lead | Solution architect | Business owner | Program manager |

### weekly-status-report.md

# Weekly Status Report

| Area | Status | Comment |
| --- | --- | --- |
| Overall | Amber | Complexity is Medium. |
| Scope | Amber | 0 scope-reduction candidates need validation. |
| Risks | Amber | 7 risk flags detected. |
| Decisions | Amber | High-effort and retire decisions require owner confirmation. |

### steering-committee-pack.md

# Steering Committee Pack

| Metric | Value |
| --- | --- |
| Complexity | Medium |
| Score | 55 |
| High-risk items | 2 |
| Scope reduction candidates | 0 |
| Effort points | 43 |

## Decisions Needed

| ID | Decision | Owner | Due |
| --- | --- | --- | --- |
| DEC-001 | Approve Extend for ProdCostRollupCustom | Functional / technical lead | Next steering |
| DEC-003 | Approve Rebuild for AIFProductionOrderImport | Integration lead | Next steering |
| DEC-005 | Approve ISV Review for ShopFloorAddon | Solution architect | Next steering |

### project-operating-model.md

# Project Operating Model

| Area | Recommendation |
| --- | --- |
| Governance | Weekly delivery review and bi-weekly steering committee. |
| Decision rights | Business owns scope decisions; architecture owns technical patterns; CISO owns security gates. |
| Escalation | Escalate high-risk blockers within 48 hours. |
| Cadence | Daily workstream standups during build/test/cutover windows. |
| Artifacts | Maintain RAID, RACI, decision log, backlog, cutover runbook, and test dashboard. |

### ai-wave-roadmap.md

# AI Migration Wave Roadmap

| Wave | Purpose | Candidate scope |
| --- | --- | --- |
| Wave 0 | Discovery and scope reduction | Inventory, fit-gap, decisions |
| Wave 1 | Standard/configuration and low-risk extensions | ProdCostRollupCustom, ProdVarianceLegacy |
| Wave 2 | Complex rebuilds, integrations, ISVs | BOMCalcHistory, AIFProductionOrderImport, ShopFloorAddon |
| Wave 3 | Data migration, testing, cutover | Trial migrations, UAT, cutover rehearsal, go-live |
