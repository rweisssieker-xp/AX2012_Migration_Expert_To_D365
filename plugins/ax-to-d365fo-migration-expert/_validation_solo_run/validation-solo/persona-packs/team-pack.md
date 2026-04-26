# Team Execution Pack

## Readiness Score

| Persona | Score | Interpretation |
| --- | --- | --- |
| TEAM | 62/100 | Needs control |

## Next Actions

- Reduce high-risk scope before committing delivery baseline.

## Included Evidence

### persona-team-member-task-view.md

# Team Member Task View

| ID | Task | Workstream | Suggested owner | Status |
| --- | --- | --- | --- | --- |
| T-001 | Document target integration design for AIFCustomerExport. | integration | Integration lead | New |
| T-002 | Review migration disposition and target pattern for LegacyTaxAddon. | isv | Solution architect | New |
| T-003 | Review migration disposition and target pattern for SalesFormLetter_Extension. | object | Functional / technical lead | New |
| T-004 | Review migration disposition and target pattern for InventTransHistory. | data | Data migration lead | New |
| T-005 | Review migration disposition and target pattern for SalesFormLetter_Extension. | object | Functional / technical lead | New |
| T-006 | Document target integration design for WarehouseFileDrop. | integration | Integration lead | New |
| T-007 | Validate retirement decision for CustTableLegacyCreditCheck. | object | Functional / technical lead | New |
| T-008 | Validate usage and target reporting pattern for InventAgingCustom. | report | Reporting lead | New |
| T-009 | Map security role/duties for LegacyWarehouseSupervisor. | security | Security lead | New |

### team-execution-pack.md

# Team Execution Pack

## Daily Task List

# Team Member Task View

| ID | Task | Workstream | Suggested owner | Status |
| --- | --- | --- | --- | --- |
| T-001 | Document target integration design for AIFCustomerExport. | integration | Integration lead | New |
| T-002 | Review migration disposition and target pattern for LegacyTaxAddon. | isv | Solution architect | New |
| T-003 | Review migration disposition and target pattern for SalesFormLetter_Extension. | object | Functional / technical lead | New |
| T-004 | Review migration disposition and target pattern for InventTransHistory. | data | Data migration lead | New |
| T-005 | Review migration disposition and target pattern for SalesFormLetter_Extension. | object | Functional / technical lead | New |
| T-006 | Document target integration design for WarehouseFileDrop. | integration | Integration lead | New |
| T-007 | Validate retirement decision for CustTableLegacyCreditCheck. | object | Functional / technical lead | New |
| T-008 | Validate usage and target reporting pattern for InventAgingCustom. | report | Reporting lead | New |
| T-009 | Map security role/duties for LegacyWarehouseSupervisor. | security | Security lead | New |

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
| BL-001 | Integration modernization | Rebuild: AIFCustomerExport | Target pattern agreed: OData, custom service, Business Events, or middleware; risks reviewed: aif, overlayering | integration | 11 | High |
| BL-002 | ISV strategy | ISV Review: LegacyTaxAddon | Target pattern agreed: D365FO ISV successor, standard replacement, custom extension, or retire; risks reviewed: overlayering | isv | 11 | High |
| BL-003 | Customization migration | Rebuild: SalesFormLetter_Extension | Target pattern agreed: Extension/service/data entity redesign; risks reviewed: direct-sql, overlayering, posting, transaction-scope | object | 11 | High |
| BL-004 | Data migration | Rebuild: InventTransHistory | Target pattern agreed: Extension/service/data entity redesign; risks reviewed: direct-sql, posting | data | 10 | High |
| BL-005 | Customization migration | Extend: SalesFormLetter_Extension | Target pattern agreed: Chain of Command or event handler; risks reviewed: overlayering, posting | object | 9 | High |
| BL-006 | Integration modernization | Rebuild: WarehouseFileDrop | Target pattern agreed: Managed file integration through middleware or recurring data jobs; risks reviewed: overlayering | integration | 8 | Medium |
| BL-007 | Customization migration | Retire Candidate: CustTableLegacyCreditCheck | Target pattern agreed: Business validation before migration; risks reviewed: overlayering | object | 7 | Medium |
| BL-008 | Report rationalization | Standard / Power BI Review: InventAgingCustom | Target pattern agreed: D365FO workspace, SSRS, Power BI, Financial Reporter, or archive; risks reviewed: overlayering, report-rationalization | report | 7 | Medium |
| BL-009 | Security mapping | Map: LegacyWarehouseSupervisor | Target pattern agreed: D365FO roles, duties, privileges, and SoD review; risks reviewed: overlayering | security | 3 | Low |

### ai-workshop-questions.md

# AI Workshop Questions

| ID | Workstream | Question | Related decision | Evidence item |
| --- | --- | --- | --- | --- |
| Q-001 | object | What business outcome does SalesFormLetter_Extension support, and is that outcome covered by D365FO standard? | Extend | SalesFormLetter_Extension |
| Q-002 | object | Can the business confirm that CustTableLegacyCreditCheck is no longer required in the D365FO target scope? | Retire Candidate | CustTableLegacyCreditCheck |
| Q-003 | integration | What SLA, monitoring, replay, and error-handling requirements apply to AIFCustomerExport? | Rebuild | AIFCustomerExport |
| Q-004 | integration | What SLA, monitoring, replay, and error-handling requirements apply to WarehouseFileDrop? | Rebuild | WarehouseFileDrop |
| Q-005 | report | Who consumes InventAgingCustom, how often, and can D365FO standard reporting or Power BI replace it? | Standard / Power BI Review | InventAgingCustom |
| Q-006 | isv | Is there a supported D365FO version or standard replacement for LegacyTaxAddon? | ISV Review | LegacyTaxAddon |
| Q-007 | security | Which D365FO duties and privileges should replace LegacyWarehouseSupervisor, and are there SoD concerns? | Map | LegacyWarehouseSupervisor |
| Q-008 | data | Does InventTransHistory require full history migration, archive access, or only opening balances/open transactions? | Rebuild | InventTransHistory |
| Q-009 | object | What business outcome does SalesFormLetter_Extension support, and is that outcome covered by D365FO standard? | Rebuild | SalesFormLetter_Extension |
