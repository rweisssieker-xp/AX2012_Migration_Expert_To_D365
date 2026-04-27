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
| T-001 | Document target integration design for LedgerJournalService. | integration | Integration lead | New |
| T-002 | Review migration disposition and target pattern for FR_TaxSettlementBatch. | object | Functional / technical lead | New |
| T-003 | Document target integration design for UK_VATMakingTaxDigital. | integration | Integration lead | New |
| T-004 | Document target integration design for DE_EInvoiceAdapter. | integration | Integration lead | New |
| T-005 | Document target integration design for US_SalesTaxConnector. | integration | Integration lead | New |
| T-006 | Document target integration design for LegacyDataArchive. | integration | Integration lead | New |
| T-007 | Document target integration design for LocalLabelExtensions. | integration | Integration lead | New |
| T-008 | Review migration disposition and target pattern for IntercompanyOrderFlow. | object | Functional / technical lead | New |
| T-009 | Review migration disposition and target pattern for GlobalCustomerMaster. | object | Functional / technical lead | New |
| T-010 | Review migration disposition and target pattern for VendorBankValidation. | object | Functional / technical lead | New |
| T-011 | Map security role/duties for SecurityRoleTemplate. | security | Security lead | New |
| T-012 | Review migration disposition and target pattern for CountryRolloutPMO. | object | Functional / technical lead | New |

### team-execution-pack.md

# Team Execution Pack

## Daily Task List

# Team Member Task View

| ID | Task | Workstream | Suggested owner | Status |
| --- | --- | --- | --- | --- |
| T-001 | Document target integration design for LedgerJournalService. | integration | Integration lead | New |
| T-002 | Review migration disposition and target pattern for FR_TaxSettlementBatch. | object | Functional / technical lead | New |
| T-003 | Document target integration design for UK_VATMakingTaxDigital. | integration | Integration lead | New |
| T-004 | Document target integration design for DE_EInvoiceAdapter. | integration | Integration lead | New |
| T-005 | Document target integration design for US_SalesTaxConnector. | integration | Integration lead | New |
| T-006 | Document target integration design for LegacyDataArchive. | integration | Integration lead | New |
| T-007 | Document target integration design for LocalLabelExtensions. | integration | Integration lead | New |
| T-008 | Review migration disposition and target pattern for IntercompanyOrderFlow. | object | Functional / technical lead | New |
| T-009 | Review migration disposition and target pattern for GlobalCustomerMaster. | object | Functional / technical lead | New |
| T-010 | Review migration disposition and target pattern for VendorBankValidation. | object | Functional / technical lead | New |
| T-011 | Map security role/duties for SecurityRoleTemplate. | security | Security lead | New |
| T-012 | Review migration disposition and target pattern for CountryRolloutPMO. | object | Functional / technical lead | New |

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
| BL-001 | Integration modernization | Rebuild: LedgerJournalService | Target pattern agreed: Middleware-backed D365FO integration pattern; risks reviewed: overlayering, posting | integration | 7 | Medium |
| BL-002 | Customization migration | Extend: FR_TaxSettlementBatch | Target pattern agreed: SysOperation/batch framework alignment; risks reviewed: batch, overlayering, posting | object | 7 | Medium |
| BL-003 | Integration modernization | Rebuild: UK_VATMakingTaxDigital | Target pattern agreed: OData, custom service, Business Events, or middleware; risks reviewed: aif, overlayering | integration | 7 | Medium |
| BL-004 | Integration modernization | Rebuild: DE_EInvoiceAdapter | Target pattern agreed: Middleware-backed D365FO integration pattern; risks reviewed: overlayering | integration | 6 | Medium |
| BL-005 | Integration modernization | Rebuild: US_SalesTaxConnector | Target pattern agreed: Middleware-backed D365FO integration pattern; risks reviewed: integration-modernization | integration | 6 | Medium |
| BL-006 | Integration modernization | Rebuild: LegacyDataArchive | Target pattern agreed: Middleware-backed D365FO integration pattern; risks reviewed: overlayering | integration | 6 | Medium |
| BL-007 | Integration modernization | Rebuild: LocalLabelExtensions | Target pattern agreed: Middleware-backed D365FO integration pattern; risks reviewed: overlayering | integration | 6 | Medium |
| BL-008 | Customization migration | Rebuild: IntercompanyOrderFlow | Target pattern agreed: Extension/service/data entity redesign; risks reviewed: client-dependency, overlayering | object | 5 | Medium |
| BL-009 | Customization migration | Rebuild: GlobalCustomerMaster | Target pattern agreed: Extension/service/data entity redesign; risks reviewed: client-dependency, overlayering | object | 5 | Medium |
| BL-010 | Customization migration | Extend: VendorBankValidation | Target pattern agreed: Chain of Command or event handler; risks reviewed: overlayering | object | 4 | Low |
| BL-011 | Security mapping | Map: SecurityRoleTemplate | Target pattern agreed: D365FO roles, duties, privileges, and SoD review; risks reviewed: overlayering | security | 3 | Low |
| BL-012 | Customization migration | Review: CountryRolloutPMO | Target pattern agreed: Fit-gap validation required; risks reviewed: overlayering | object | 3 | Low |

### ai-workshop-questions.md

# AI Workshop Questions

| ID | Workstream | Question | Related decision | Evidence item |
| --- | --- | --- | --- | --- |
| Q-001 | integration | What SLA, monitoring, replay, and error-handling requirements apply to LedgerJournalService? | Rebuild | LedgerJournalService |
| Q-002 | integration | What SLA, monitoring, replay, and error-handling requirements apply to DE_EInvoiceAdapter? | Rebuild | DE_EInvoiceAdapter |
| Q-003 | object | What business outcome does FR_TaxSettlementBatch support, and is that outcome covered by D365FO standard? | Extend | FR_TaxSettlementBatch |
| Q-004 | integration | What SLA, monitoring, replay, and error-handling requirements apply to UK_VATMakingTaxDigital? | Rebuild | UK_VATMakingTaxDigital |
| Q-005 | integration | What SLA, monitoring, replay, and error-handling requirements apply to US_SalesTaxConnector? | Rebuild | US_SalesTaxConnector |
| Q-006 | object | What business outcome does IntercompanyOrderFlow support, and is that outcome covered by D365FO standard? | Rebuild | IntercompanyOrderFlow |
| Q-007 | object | What business outcome does GlobalCustomerMaster support, and is that outcome covered by D365FO standard? | Rebuild | GlobalCustomerMaster |
| Q-008 | object | What business outcome does VendorBankValidation support, and is that outcome covered by D365FO standard? | Extend | VendorBankValidation |
| Q-009 | security | Which D365FO duties and privileges should replace SecurityRoleTemplate, and are there SoD concerns? | Map | SecurityRoleTemplate |
| Q-010 | integration | What SLA, monitoring, replay, and error-handling requirements apply to LegacyDataArchive? | Rebuild | LegacyDataArchive |
| Q-011 | object | What business outcome does CountryRolloutPMO support, and is that outcome covered by D365FO standard? | Review | CountryRolloutPMO |
| Q-012 | integration | What SLA, monitoring, replay, and error-handling requirements apply to LocalLabelExtensions? | Rebuild | LocalLabelExtensions |
