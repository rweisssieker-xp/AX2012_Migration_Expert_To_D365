# Team Execution Pack

## Readiness Score

| Persona | Score | Interpretation |
| --- | --- | --- |
| TEAM | 68/100 | Needs control |

## Next Actions

- Reduce high-risk scope before committing delivery baseline.

## Included Evidence

### persona-team-member-task-view.md

# Team Member Task View

| ID | Task | Workstream | Suggested owner | Status |
| --- | --- | --- | --- | --- |
| T-001 | Document target integration design for GLTrialBalanceSqlExport. | integration | Integration lead | New |
| T-002 | Review migration disposition and target pattern for LedgerJournalPostOverride. | object | Functional / technical lead | New |
| T-003 | Validate usage and target reporting pattern for TaxAuditPack. | report | Reporting lead | New |
| T-004 | Validate retirement decision for DimensionLegacyEditor. | object | Functional / technical lead | New |
| T-005 | Map security role/duties for LegacyFinanceController. | security | Security lead | New |

### team-execution-pack.md

# Team Execution Pack

## Daily Task List

# Team Member Task View

| ID | Task | Workstream | Suggested owner | Status |
| --- | --- | --- | --- | --- |
| T-001 | Document target integration design for GLTrialBalanceSqlExport. | integration | Integration lead | New |
| T-002 | Review migration disposition and target pattern for LedgerJournalPostOverride. | object | Functional / technical lead | New |
| T-003 | Validate usage and target reporting pattern for TaxAuditPack. | report | Reporting lead | New |
| T-004 | Validate retirement decision for DimensionLegacyEditor. | object | Functional / technical lead | New |
| T-005 | Map security role/duties for LegacyFinanceController. | security | Security lead | New |

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
| BL-001 | Integration modernization | Rebuild: GLTrialBalanceSqlExport | Target pattern agreed: Data entity, export, reporting replica, or data lake pattern; risks reviewed: direct-sql, overlayering | integration | 11 | High |
| BL-002 | Customization migration | Extend: LedgerJournalPostOverride | Target pattern agreed: Chain of Command or event handler; risks reviewed: overlayering, posting | object | 9 | High |
| BL-003 | Report rationalization | Standard / Power BI Review: TaxAuditPack | Target pattern agreed: D365FO workspace, SSRS, Power BI, Financial Reporter, or archive; risks reviewed: overlayering, report-rationalization | report | 9 | High |
| BL-004 | Customization migration | Retire Candidate: DimensionLegacyEditor | Target pattern agreed: Business validation before migration; risks reviewed: overlayering | object | 7 | Medium |
| BL-005 | Security mapping | Map: LegacyFinanceController | Target pattern agreed: D365FO roles, duties, privileges, and SoD review; risks reviewed: overlayering | security | 5 | Medium |

### ai-workshop-questions.md

# AI Workshop Questions

| ID | Workstream | Question | Related decision | Evidence item |
| --- | --- | --- | --- | --- |
| Q-001 | object | What business outcome does LedgerJournalPostOverride support, and is that outcome covered by D365FO standard? | Extend | LedgerJournalPostOverride |
| Q-002 | object | Can the business confirm that DimensionLegacyEditor is no longer required in the D365FO target scope? | Retire Candidate | DimensionLegacyEditor |
| Q-003 | integration | What SLA, monitoring, replay, and error-handling requirements apply to GLTrialBalanceSqlExport? | Rebuild | GLTrialBalanceSqlExport |
| Q-004 | report | Who consumes TaxAuditPack, how often, and can D365FO standard reporting or Power BI replace it? | Standard / Power BI Review | TaxAuditPack |
| Q-005 | security | Which D365FO duties and privileges should replace LegacyFinanceController, and are there SoD concerns? | Map | LegacyFinanceController |
