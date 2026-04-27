# Team Execution Pack

## Readiness Score

| Persona | Score | Interpretation |
| --- | --- | --- |
| TEAM | 61/100 | Needs control |

## Next Actions

- Reduce high-risk scope before committing delivery baseline.

## Included Evidence

### persona-team-member-task-view.md

# Team Member Task View

| ID | Task | Workstream | Suggested owner | Status |
| --- | --- | --- | --- | --- |
| T-001 | Document target integration design for CSUChannelSyncMonitor. | integration | Integration lead | New |
| T-002 | Document target integration design for PaymentTerminalConnector. | integration | Integration lead | New |
| T-003 | Review migration disposition and target pattern for RetailTransactionHistory. | data | Data migration lead | New |
| T-004 | Review migration disposition and target pattern for RetailPriceOverride. | object | Functional / technical lead | New |
| T-005 | Review migration disposition and target pattern for POSOfflineRecoveryForm. | object | Functional / technical lead | New |
| T-006 | Validate usage and target reporting pattern for LoyaltyLiabilityReport. | report | Reporting lead | New |
| T-007 | Map security role/duties for StoreManagerLegacyRole. | security | Security lead | New |

### team-execution-pack.md

# Team Execution Pack

## Daily Task List

# Team Member Task View

| ID | Task | Workstream | Suggested owner | Status |
| --- | --- | --- | --- | --- |
| T-001 | Document target integration design for CSUChannelSyncMonitor. | integration | Integration lead | New |
| T-002 | Document target integration design for PaymentTerminalConnector. | integration | Integration lead | New |
| T-003 | Review migration disposition and target pattern for RetailTransactionHistory. | data | Data migration lead | New |
| T-004 | Review migration disposition and target pattern for RetailPriceOverride. | object | Functional / technical lead | New |
| T-005 | Review migration disposition and target pattern for POSOfflineRecoveryForm. | object | Functional / technical lead | New |
| T-006 | Validate usage and target reporting pattern for LoyaltyLiabilityReport. | report | Reporting lead | New |
| T-007 | Map security role/duties for StoreManagerLegacyRole. | security | Security lead | New |

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
| BL-001 | Integration modernization | Rebuild: CSUChannelSyncMonitor | Target pattern agreed: Middleware-backed D365FO integration pattern; risks reviewed: client-dependency, overlayering | integration | 11 | High |
| BL-002 | Integration modernization | Rebuild: PaymentTerminalConnector | Target pattern agreed: Middleware-backed D365FO integration pattern; risks reviewed: overlayering, posting | integration | 11 | High |
| BL-003 | Data migration | Rebuild: RetailTransactionHistory | Target pattern agreed: Extension/service/data entity redesign; risks reviewed: client-dependency, direct-sql | data | 10 | High |
| BL-004 | Customization migration | Rebuild: RetailPriceOverride | Target pattern agreed: Extension/service/data entity redesign; risks reviewed: client-dependency, overlayering | object | 9 | High |
| BL-005 | Customization migration | Extend: POSOfflineRecoveryForm | Target pattern agreed: Form extension plus event handlers; risks reviewed: overlayering | object | 9 | High |
| BL-006 | Report rationalization | Standard / Power BI Review: LoyaltyLiabilityReport | Target pattern agreed: D365FO workspace, SSRS, Power BI, Financial Reporter, or archive; risks reviewed: overlayering, report-rationalization | report | 7 | Medium |
| BL-007 | Security mapping | Map: StoreManagerLegacyRole | Target pattern agreed: D365FO roles, duties, privileges, and SoD review; risks reviewed: overlayering | security | 5 | Medium |

### ai-workshop-questions.md

# AI Workshop Questions

| ID | Workstream | Question | Related decision | Evidence item |
| --- | --- | --- | --- | --- |
| Q-001 | object | What business outcome does RetailPriceOverride support, and is that outcome covered by D365FO standard? | Rebuild | RetailPriceOverride |
| Q-002 | integration | What SLA, monitoring, replay, and error-handling requirements apply to CSUChannelSyncMonitor? | Rebuild | CSUChannelSyncMonitor |
| Q-003 | object | What business outcome does POSOfflineRecoveryForm support, and is that outcome covered by D365FO standard? | Extend | POSOfflineRecoveryForm |
| Q-004 | integration | What SLA, monitoring, replay, and error-handling requirements apply to PaymentTerminalConnector? | Rebuild | PaymentTerminalConnector |
| Q-005 | report | Who consumes LoyaltyLiabilityReport, how often, and can D365FO standard reporting or Power BI replace it? | Standard / Power BI Review | LoyaltyLiabilityReport |
| Q-006 | data | Does RetailTransactionHistory require full history migration, archive access, or only opening balances/open transactions? | Rebuild | RetailTransactionHistory |
| Q-007 | security | Which D365FO duties and privileges should replace StoreManagerLegacyRole, and are there SoD concerns? | Map | StoreManagerLegacyRole |
