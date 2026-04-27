# Team Execution Pack

## Readiness Score

| Persona | Score | Interpretation |
| --- | --- | --- |
| TEAM | 74/100 | Needs control |

## Next Actions

- Proceed with gate review and maintain weekly evidence updates.

## Included Evidence

### persona-team-member-task-view.md

# Team Member Task View

| ID | Task | Workstream | Suggested owner | Status |
| --- | --- | --- | --- | --- |
| T-001 | Document target integration design for AIFProductionOrderImport. | integration | Integration lead | New |
| T-002 | Review migration disposition and target pattern for ShopFloorAddon. | isv | Solution architect | New |
| T-003 | Review migration disposition and target pattern for ProdCostRollupCustom. | object | Functional / technical lead | New |
| T-004 | Validate usage and target reporting pattern for ProdVarianceLegacy. | report | Reporting lead | New |
| T-005 | Review migration disposition and target pattern for BOMCalcHistory. | object | Functional / technical lead | New |

### team-execution-pack.md

# Team Execution Pack

## Daily Task List

# Team Member Task View

| ID | Task | Workstream | Suggested owner | Status |
| --- | --- | --- | --- | --- |
| T-001 | Document target integration design for AIFProductionOrderImport. | integration | Integration lead | New |
| T-002 | Review migration disposition and target pattern for ShopFloorAddon. | isv | Solution architect | New |
| T-003 | Review migration disposition and target pattern for ProdCostRollupCustom. | object | Functional / technical lead | New |
| T-004 | Validate usage and target reporting pattern for ProdVarianceLegacy. | report | Reporting lead | New |
| T-005 | Review migration disposition and target pattern for BOMCalcHistory. | object | Functional / technical lead | New |

## Defect Triage Template

| Defect | Severity | Owner | Root cause | Next action |
| --- | --- | --- | --- | --- |
|  | Sev 1 / Sev 2 / Sev 3 |  |  |  |

### role-based-prompt-library.md

# Role-Based Prompt Library

## CEO

Act as a CEO reviewing this AX to D365FO migration. Summarize business value, risk of delay, investment logic, and top decisions needed.

## CIO

Act as a CIO reviewing this migration architecture. Identify technical debt, supportability risks, integration modernization needs, and architecture decisions.

## CISO

Act as a CISO reviewing this migration. Identify identity, access, SoD, integration security, sensitive data, retention, and go-live security gate risks.

## Project Manager

Act as the program manager. Generate RAID, weekly status, dependencies, milestones, blockers, and steering committee decisions.

## Project Team Member

Act as a workstream team member. Convert the analysis into daily tasks, workshop questions, test scripts, and defect triage actions.

### project-onboarding-guide.md

# Project Onboarding Guide

| Topic | What new team members need to know |
| --- | --- |
| Mission | Reduce AX migration scope while preserving business-critical capability. |
| Evidence | Use inventory, reports, telemetry, and workshop validation. |
| Workflow | Analyze, validate, decide, design, build, test, cutover, stabilize. |
| Key files | Dashboard, RAID, decision log, backlog, security gate, cutover plan. |
| First task | Review persona-team-member-task-view.md and assigned workstream reports. |

### ai-migration-backlog.md

# AI Migration Backlog

| ID | Epic | Story | Acceptance criteria | Workstream | Effort | Risk |
| --- | --- | --- | --- | --- | --- | --- |
| BL-001 | Integration modernization | Rebuild: AIFProductionOrderImport | Target pattern agreed: OData, custom service, Business Events, or middleware; risks reviewed: aif, overlayering | integration | 11 | High |
| BL-002 | ISV strategy | ISV Review: ShopFloorAddon | Target pattern agreed: D365FO ISV successor, standard replacement, custom extension, or retire; risks reviewed: overlayering | isv | 11 | High |
| BL-003 | Customization migration | Extend: ProdCostRollupCustom | Target pattern agreed: Chain of Command or event handler; risks reviewed: overlayering | object | 8 | Medium |
| BL-004 | Report rationalization | Standard / Power BI Review: ProdVarianceLegacy | Target pattern agreed: D365FO workspace, SSRS, Power BI, Financial Reporter, or archive; risks reviewed: overlayering, report-rationalization | report | 7 | Medium |
| BL-005 | Customization migration | Rebuild: BOMCalcHistory | Target pattern agreed: Extension/service/data entity redesign; risks reviewed: direct-sql | object | 6 | Medium |

### ai-workshop-questions.md

# AI Workshop Questions

| ID | Workstream | Question | Related decision | Evidence item |
| --- | --- | --- | --- | --- |
| Q-001 | object | What business outcome does ProdCostRollupCustom support, and is that outcome covered by D365FO standard? | Extend | ProdCostRollupCustom |
| Q-002 | object | What business outcome does BOMCalcHistory support, and is that outcome covered by D365FO standard? | Rebuild | BOMCalcHistory |
| Q-003 | integration | What SLA, monitoring, replay, and error-handling requirements apply to AIFProductionOrderImport? | Rebuild | AIFProductionOrderImport |
| Q-004 | report | Who consumes ProdVarianceLegacy, how often, and can D365FO standard reporting or Power BI replace it? | Standard / Power BI Review | ProdVarianceLegacy |
| Q-005 | isv | Is there a supported D365FO version or standard replacement for ShopFloorAddon? | ISV Review | ShopFloorAddon |
