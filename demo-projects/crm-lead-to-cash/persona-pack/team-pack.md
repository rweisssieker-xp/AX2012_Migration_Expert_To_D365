# Team Execution Pack

## Readiness Score

| Persona | Score | Interpretation |
| --- | --- | --- |
| TEAM | 63/100 | Needs control |

## Next Actions

- Reduce high-risk scope before committing delivery baseline.

## Included Evidence

### persona-team-member-task-view.md

# Team Member Task View

| ID | Task | Workstream | Suggested owner | Status |
| --- | --- | --- | --- | --- |
| T-001 | Document target integration design for AIFLeadToCashSync. | integration | Integration lead | New |
| T-002 | Document target integration design for DataverseCustomerExport. | integration | Integration lead | New |
| T-003 | Review migration disposition and target pattern for CustContactLegacyMap. | data | Data migration lead | New |
| T-004 | Review migration disposition and target pattern for OpportunityQuoteBridge. | object | Functional / technical lead | New |
| T-005 | Validate usage and target reporting pattern for PipelineConversionLegacy. | report | Reporting lead | New |
| T-006 | Map security role/duties for SalesManagerLegacyRole. | security | Security lead | New |

### team-execution-pack.md

# Team Execution Pack

## Daily Task List

# Team Member Task View

| ID | Task | Workstream | Suggested owner | Status |
| --- | --- | --- | --- | --- |
| T-001 | Document target integration design for AIFLeadToCashSync. | integration | Integration lead | New |
| T-002 | Document target integration design for DataverseCustomerExport. | integration | Integration lead | New |
| T-003 | Review migration disposition and target pattern for CustContactLegacyMap. | data | Data migration lead | New |
| T-004 | Review migration disposition and target pattern for OpportunityQuoteBridge. | object | Functional / technical lead | New |
| T-005 | Validate usage and target reporting pattern for PipelineConversionLegacy. | report | Reporting lead | New |
| T-006 | Map security role/duties for SalesManagerLegacyRole. | security | Security lead | New |

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
| BL-001 | Integration modernization | Rebuild: AIFLeadToCashSync | Target pattern agreed: OData, custom service, Business Events, or middleware; risks reviewed: aif, overlayering | integration | 11 | High |
| BL-002 | Integration modernization | Rebuild: DataverseCustomerExport | Target pattern agreed: Data entity, export, reporting replica, or data lake pattern; risks reviewed: direct-sql, overlayering | integration | 11 | High |
| BL-003 | Data migration | Rebuild: CustContactLegacyMap | Target pattern agreed: Extension/service/data entity redesign; risks reviewed: direct-sql, overlayering | data | 8 | Medium |
| BL-004 | Customization migration | Extend: OpportunityQuoteBridge | Target pattern agreed: Chain of Command or event handler; risks reviewed: overlayering | object | 8 | Medium |
| BL-005 | Report rationalization | Standard / Power BI Review: PipelineConversionLegacy | Target pattern agreed: D365FO workspace, SSRS, Power BI, Financial Reporter, or archive; risks reviewed: overlayering, report-rationalization | report | 7 | Medium |
| BL-006 | Security mapping | Map: SalesManagerLegacyRole | Target pattern agreed: D365FO roles, duties, privileges, and SoD review; risks reviewed: overlayering | security | 5 | Medium |

### ai-workshop-questions.md

# AI Workshop Questions

| ID | Workstream | Question | Related decision | Evidence item |
| --- | --- | --- | --- | --- |
| Q-001 | integration | What SLA, monitoring, replay, and error-handling requirements apply to AIFLeadToCashSync? | Rebuild | AIFLeadToCashSync |
| Q-002 | data | Does CustContactLegacyMap require full history migration, archive access, or only opening balances/open transactions? | Rebuild | CustContactLegacyMap |
| Q-003 | object | What business outcome does OpportunityQuoteBridge support, and is that outcome covered by D365FO standard? | Extend | OpportunityQuoteBridge |
| Q-004 | integration | What SLA, monitoring, replay, and error-handling requirements apply to DataverseCustomerExport? | Rebuild | DataverseCustomerExport |
| Q-005 | report | Who consumes PipelineConversionLegacy, how often, and can D365FO standard reporting or Power BI replace it? | Standard / Power BI Review | PipelineConversionLegacy |
| Q-006 | security | Which D365FO duties and privileges should replace SalesManagerLegacyRole, and are there SoD concerns? | Map | SalesManagerLegacyRole |
