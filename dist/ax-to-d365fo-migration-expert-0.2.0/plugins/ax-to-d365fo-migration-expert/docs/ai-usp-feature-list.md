# Max AI USP Feature List

## Core Positioning

The plugin is an AI-powered AX to D365FO migration scope reducer and delivery accelerator.

It simplifies migration by converting AX evidence into decisions:

- What must be migrated.
- What D365FO standard can replace.
- What should be configured instead of customized.
- What should be retired.
- What is risky and needs senior review.
- What artifacts the project team needs next.

## Feature 1: AI Migration Scope Reducer

Purpose: reduce cost, timeline, and go-live risk by minimizing unnecessary migration scope.

Inputs:

- AX object inventory.
- X++ customization list.
- Module/process inventory.
- Integration inventory.
- Report list.
- Usage evidence.
- Workshop notes.

Outputs:

- Scope reduction matrix.
- Keep / replace / retire decisions.
- Effort avoided estimate.
- Risk impact.
- Business validation questions.

USP: turns migration from "move everything" into "move only what creates value."

## Feature 2: AX Legacy Complexity Score

Purpose: produce an executive-ready migration complexity rating.

Inputs:

- Source version.
- Customization volume.
- Integration count.
- Report count.
- ISV footprint.
- Database size.
- Data history requirements.
- Localization and compliance scope.

Outputs:

- Overall complexity: Low / Medium / High / Critical.
- Score by workstream.
- Top complexity drivers.
- Mitigation plan.

USP: gives leadership an early, structured view of migration difficulty.

## Feature 3: Migration Effort Estimator

Purpose: estimate effort ranges by workstream without pretending to know exact numbers too early.

Outputs:

- Effort by workstream.
- Confidence level.
- Assumptions.
- Missing evidence.
- Decision dependencies.

Recommended workstreams:

- Functional fit-gap.
- X++ development.
- Data migration.
- Integrations.
- Reporting.
- Security.
- Testing.
- Cutover.
- Change management.

USP: accelerates proposal, planning, and budget conversations.

## Feature 4: Customization Disposition AI

Purpose: classify each customization into the correct target strategy.

Categories:

- Retire.
- Standard.
- Configure.
- Extend.
- Rebuild.
- Replace with ISV.

Outputs:

- Classification.
- Reason.
- Confidence.
- D365FO target pattern.
- Review owner.
- Risk.

USP: automates one of the most expensive expert tasks in AX migrations.

## Feature 5: Code-to-Extension Advisor

Purpose: help convert legacy X++ designs into supportable D365FO extension patterns.

Detects:

- Overlayering.
- Direct SQL.
- Framework overrides.
- Form-level business logic.
- Batch issues.
- Posting modifications.
- Client-side dependencies.

Outputs:

- Recommended extension pattern.
- Chain of Command opportunity.
- Event handler opportunity.
- Data entity or service design.
- Security considerations.
- Example target approach.

USP: helps teams avoid unsupported or fragile migration designs.

## Feature 6: Dead Customization Detector

Purpose: identify customizations that likely should not be migrated.

Signals:

- No references.
- No recent usage.
- Obsolete process.
- Replaced by standard D365FO.
- Duplicate capability.
- High complexity and low business value.

Outputs:

- Retire candidate list.
- Evidence.
- Business validation owner.
- Expected scope reduction.

USP: directly reduces project size.

## Feature 7: Business Process Mining Assistant

Purpose: infer real business process usage from AX evidence.

Inputs:

- Modules.
- Transactions.
- Menu items.
- Roles.
- Reports.
- Customizations.
- Batch jobs.

Outputs:

- Active processes.
- Rarely used processes.
- D365FO target process mapping.
- Workshop validation questions.

USP: separates actual business use from historical system baggage.

## Feature 8: Fit-Gap Generator

Purpose: convert AX behavior, notes, and object evidence into fit-gap deliverables.

Outputs:

- Requirement.
- Current AX behavior.
- D365FO standard fit.
- Gap type.
- Recommendation.
- Priority.
- Owner.

USP: turns discovery material into a structured migration backlog.

## Feature 9: Integration Modernization Advisor

Purpose: move old AX integration architecture to modern D365FO patterns.

Mappings:

- AIF to OData, custom service, Business Events, or middleware.
- File drop to managed integration or Logic Apps.
- Direct SQL to data entities or reporting replica.
- Custom event logic to Business Events.
- CRM sync to Dataverse or Dual-write where appropriate.

Outputs:

- Target integration pattern.
- Authentication model.
- Monitoring approach.
- Error handling.
- Replay strategy.
- Operational owner.

USP: modernizes architecture instead of copying fragile legacy integrations.

## Feature 10: Report Rationalization AI

Purpose: reduce reporting migration scope.

Classifications:

- Retire.
- Replace with D365FO standard.
- Rebuild in SSRS.
- Move to Power BI.
- Move to Financial Reporter.
- Serve from archive/reporting store.

USP: prevents unnecessary report rebuilds.

## Feature 11: Data Migration Scope Optimizer

Purpose: minimize data migration risk and downtime.

Strategies:

- Full history migration.
- Open transactions only.
- Master/configuration only.
- External archive.
- Read-only reporting history.
- No migration.

Outputs:

- Data domain recommendation.
- Rationale.
- Reconciliation checks.
- Cutover timing impact.
- Compliance considerations.

USP: reduces one of the highest-risk migration workstreams.

## Feature 12: Test Case Generator

Purpose: create practical tests from migration scope.

Generated test types:

- UAT.
- Regression.
- Data validation.
- Integration.
- Security role.
- Cutover smoke.

USP: makes test coverage traceable to migration decisions.

## Feature 13: Cutover Simulation

Purpose: create and stress-test a go-live runbook.

Outputs:

- Sequence.
- Dependencies.
- Duration estimates.
- Critical path.
- Go/no-go criteria.
- Rollback points.
- Validation windows.

USP: makes go-live risk visible before go-live weekend.

## Feature 14: Migration Risk Radar

Purpose: detect technical and delivery risks early.

Risk patterns:

- Direct SQL.
- AIF dependencies.
- Overlayering-heavy areas.
- COM/client dependencies.
- Custom posting logic.
- Custom inventory logic.
- Large history migration.
- Unowned reports or integrations.
- Weak reconciliation plan.

USP: catches hidden migration risk before it becomes a project delay.

## Feature 15: Migration Decision Log

Purpose: keep migration decisions traceable.

Captures:

- Decision.
- Context.
- Options.
- Recommendation.
- Rationale.
- Impact.
- Owner.
- Date.

USP: supports steering committee, audit, and scope control.

## Feature 16: Role and Security Mapper

Purpose: structure security migration from AX to D365FO.

Outputs:

- AX role inventory.
- D365FO target role.
- Duties.
- Privileges.
- SoD risks.
- Custom security impact.

USP: reduces late security surprises during UAT.

## Feature 17: ISV Replacement Advisor

Purpose: handle old AX add-ons and vertical solutions.

Recommendations:

- Upgrade same ISV.
- Replace with D365FO standard.
- Replace with another ISV.
- Rebuild as extension.
- Retire.

USP: makes old add-on dependency decisions explicit.

## Feature 18: Executive Migration Briefing

Purpose: translate technical evidence into management decisions.

Outputs:

- Current state.
- Target state.
- Complexity.
- Cost drivers.
- Key risks.
- Decisions needed.
- Roadmap.
- Next 30/60/90 days.

USP: bridges technical migration work and executive steering.

## Feature 19: Migration Backlog Builder

Purpose: turn assessment outputs into implementation work.

Outputs:

- Epic.
- Feature.
- User story.
- Acceptance criteria.
- Dependencies.
- Estimate range.
- Risk.
- Workstream owner.

USP: converts assessment into execution.

## Feature 20: Workshop Question Generator

Purpose: generate targeted workshop questions from evidence gaps.

Outputs:

- Question.
- Workstream.
- Why it matters.
- Related decision.
- Required evidence.
- Owner.

USP: shortens workshops and focuses SMEs on decisions.

## Feature 21: D365FO Target Architecture Advisor

Purpose: propose the target landscape for environments, integrations, analytics, security, and operations.

Outputs:

- Environment strategy.
- Integration architecture.
- Reporting architecture.
- Security architecture.
- ALM and release flow.
- Monitoring and support model.

USP: connects migration decisions to a maintainable future-state architecture.

## Feature 22: Compliance and Audit Migration Assistant

Purpose: ensure regulatory and audit requirements are not lost during scope reduction.

Outputs:

- Retention requirements.
- Audit evidence requirements.
- Sensitive data domains.
- Archive strategy.
- Security control mapping.

USP: enables scope reduction without losing compliance coverage.

## Feature 23: Environment and ALM Planner

Purpose: define how D365FO environments and release processes support the migration.

Outputs:

- Environment list.
- Purpose per environment.
- Build/deploy path.
- Test data approach.
- Release governance.

USP: avoids environment chaos during parallel migration workstreams.

## Feature 24: Data Quality Issue Detector

Purpose: identify source data risks before migration cycles.

Detects:

- Missing mandatory fields.
- Inactive or duplicate master data.
- Invalid dimensions.
- Unbalanced financial data.
- Orphaned references.
- Obsolete codes.

USP: reduces failed loads and reconciliation delays.

## Feature 25: Post-Go-Live Stabilization Advisor

Purpose: plan support after go-live.

Outputs:

- Hypercare model.
- Support triage categories.
- Daily checkpoint agenda.
- Defect severity model.
- Stabilization exit criteria.

USP: improves adoption and operational continuity after cutover.

## Feature 26: AI Business Case and ROI Builder

Purpose: convert migration simplification into business value.

Outputs:

- Avoided rebuild effort.
- Reduced testing scope.
- Retired report or ISV cost.
- Lower cutover risk.
- Faster standardization opportunities.
- Executive value summary.

USP: helps justify migration decisions in financial and steering language.

## Feature 27: Migration Wave Planner

Purpose: sequence migration delivery into manageable waves.

Outputs:

- Wave 0 discovery and scope reduction.
- Wave 1 standard/configuration and low-risk extensions.
- Wave 2 complex rebuilds, integrations, and ISVs.
- Wave 3 data migration, testing, cutover, hypercare.

USP: turns assessment into an executable roadmap.

## Feature 28: Dependency Graph Advisor

Purpose: reveal hidden dependencies before planning build work.

Dependencies:

- Customization to table.
- Integration to data entity.
- Report to business process.
- Security role to process.
- ISV to data migration.
- Cutover task to validation owner.

USP: prevents blocked workstreams and late surprises.

## Feature 29: D365FO Standard Feature Matchmaker

Purpose: map AX custom functionality to likely D365FO standard capabilities.

Outputs:

- Candidate D365FO feature.
- Configuration area.
- Fit confidence.
- Required validation.
- Residual gap.

USP: reduces custom build by checking standard fit first.

## Feature 30: Migration Anti-Pattern Detector

Purpose: warn when teams recreate legacy AX problems in D365FO.

Anti-patterns:

- Lift-and-shift custom logic.
- Rebuilding every report.
- Migrating all history without a business reason.
- Direct SQL integrations.
- Over-customizing before fit-gap validation.
- Leaving security until UAT.

USP: protects the D365FO target from becoming a cloud copy of legacy AX debt.

## Feature 31: SME Interview Copilot

Purpose: turn technical findings into business validation questions.

Outputs:

- Question.
- Why it matters.
- Required evidence.
- Decision to make.
- Suggested owner.

USP: shortens workshops and improves decision quality.

## Feature 32: RFP / Proposal Accelerator

Purpose: produce proposal-ready migration content.

Outputs:

- Scope.
- Assumptions.
- Exclusions.
- Workstreams.
- Effort ranges.
- Delivery phases.
- Risks.
- Client responsibilities.

USP: turns discovery evidence into sales and delivery material.

## Feature 33: Cutover Downtime Estimator

Purpose: identify drivers of go-live downtime.

Drivers:

- Data export/import duration.
- Reconciliation windows.
- Integration shutdown and restart.
- Manual validation.
- Rollback preparation.

USP: gives leadership early visibility into go-live constraints.

## Feature 34: Training and Change Impact Mapper

Purpose: connect migration decisions to business change.

Outputs:

- Impacted roles.
- Process changes.
- Training topics.
- Adoption risk.
- Communication needs.

USP: prevents migration from being treated as only a technical project.

## Feature 35: Dual-Run and Reconciliation Planner

Purpose: define how AX and D365FO outputs will be compared before go-live.

Outputs:

- Parallel run scope.
- Reconciliation checks.
- Tolerance thresholds.
- Owners.
- Defect handling.

USP: improves confidence before production cutover.

## Feature 36: AX Modelstore / AOT Deep Scanner

Purpose: prepare for deeper automated discovery from AX modelstore exports, XPO files, AOT object lists, and SQL-based inventories.

USP: reduces manual inventory preparation.

## Feature 37: X++ Pattern Detector

Purpose: detect legacy code patterns such as overridden methods, transaction blocks, direct SQL, RunBaseBatch, AIF, COM/WinAPI, NumberSeq, and posting logic.

USP: acts like a technical migration architect for code review.

## Feature 38: Standard Feature Knowledge Base

Purpose: map AX processes and customizations to likely D365FO standard features, workspaces, data entities, APIs, and Business Events.

USP: build less, configure more.

## Feature 39: Automated Fit-Gap from Evidence

Purpose: generate fit-gap entries from customizations, reports, roles, integrations, modules, usage, and process notes.

USP: accelerates discovery-to-backlog conversion.

## Feature 40: Migration Dependency Graph

Purpose: expose dependencies between objects, tables, reports, integrations, roles, ISVs, data, and cutover tasks.

USP: improves sequencing and prevents blocked work.

## Feature 41: Data Entity Mapper

Purpose: propose AX source to D365FO data entity candidates, transformations, mandatory field checks, and reconciliation checks.

USP: makes data migration actionable earlier.

## Feature 42: LCS / Azure DevOps Work Item Generator

Purpose: convert analysis into importable delivery work items.

USP: hands assessment output directly to delivery execution.

## Feature 43: Migration Cost Model

Purpose: convert effort points into person-day and budget ranges using configurable role mix and rate assumptions.

USP: accelerates business case and proposal creation.

## Feature 44: Quality Gate Engine

Purpose: define readiness, design, build, data, UAT, and cutover quality gates.

USP: makes migration governance repeatable.

## Feature 45: Upgrade Path Decision Engine

Purpose: recommend upgrade-led, hybrid, or reimplementation-led migration paths based on version, complexity, and risk.

USP: prevents choosing the wrong migration approach.

## Feature 46: Before / After Architecture Generator

Purpose: describe AX current architecture and D365FO target architecture side by side.

USP: improves executive and architecture communication.

## Feature 47: Risk-to-Mitigation Playbooks

Purpose: attach repeatable mitigation plans to common risks like direct SQL, AIF, overlayering, ISVs, custom posting, and large history.

USP: moves from risk detection to remediation planning.

## Feature 48: Automated Report Usage Rationalizer

Purpose: use report usage evidence to retire, replace, rebuild, or move reports to Power BI/Financial Reporter/archive.

USP: reduces hidden reporting migration effort.

## Feature 49: Process Standardization Advisor

Purpose: identify where adapting to D365FO standard process can remove customizations.

USP: supports business transformation instead of technical copy.

## Feature 50: Migration Command Center Dashboard

Purpose: summarize complexity, scope reduction, high-risk items, low-confidence recommendations, and gate status.

USP: creates visible product value from analysis.

## Feature 51: Evidence Confidence Score

Purpose: score every AI recommendation as high, medium, or low confidence and state missing evidence.

USP: makes AI recommendations auditable and safe for governance.

## Feature 52: Industry Template Packs

Purpose: tailor assessment to manufacturing, retail, wholesale, project, public sector, finance-heavy, or warehouse-heavy migrations.

USP: moves beyond generic AX migration advice.

## Feature 53: Multi-Language Migration Pack

Purpose: support German/English, executive/technical wording, and steering committee-ready outputs.

USP: fits DACH and international migration programs.

## Feature 54: Partner Delivery Methodology

Purpose: package the repeatable method as Discover, Reduce, Decide, Design, Build, Validate, Cutover, Stabilize.

USP: turns the skill into a consulting product.

## Feature 55: Migration Anti-Waste Score

Purpose: quantify unnecessary migration scope such as unused reports, low-value customizations, all-history migration, duplicate integrations, and old ISVs.

USP: strong sales message: find and remove waste from migration scope.

## Feature 56: Migration Digital Twin

Simulates current AX state, target D365FO state, workstreams, risks, dependencies, and scope-reduction effects before execution.

## Feature 57: What-if Simulator

Compares baseline, scope-reduced, archive-history, report-rationalized, phased, and rebuild-heavy migration scenarios.

## Feature 58: AI Migration Negotiator

Creates evidence-based arguments for scope discussions and steering committee decisions.

## Feature 59: Code Refactoring Blueprint Generator

Turns legacy X++ findings into extension patterns, refactoring steps, risks, and test cases.

## Feature 60: Migration Test Intelligence

Prioritizes tests by risk coverage, customization impact, cutover criticality, and role coverage.

## Feature 61: Cutover War Room Assistant

Provides live cutover checklist, blocker log, decision points, rollback timer inputs, and communication prompts.

## Feature 62: Data Quality AI Profiler

Profiles CSV data for nulls, duplicates, distinct counts, and migration-readiness concerns.

## Feature 63: Migration Knowledge Graph

Exports machine-readable nodes and edges for objects, processes, reports, integrations, data, risks, and decisions.

## Feature 64: Scope Creep Detector

Compares new requests to baseline scope and flags incremental effort, risk, and approval needs.

## Feature 65: Architecture Decision Record Generator

Generates ADR-ready records for major migration decisions.

## Feature 66: AI Prompt Pack for Migration Workshops

Provides role/workstream-specific prompts for fit-gap, integration, data, reporting, cutover, and steering workshops.

## Feature 67: D365FO Extension Pattern Library

Documents CoC, event handler, table/form extension, data entity, service, Business Event, SysOperation, and security mapping patterns.

## Feature 68: Migration Readiness Interview Bot

Structures missing-evidence questions and converts answers into readiness actions.

## Feature 69: Regulatory / Localization Risk Advisor

Highlights GDPR/DSGVO, GoBD, e-invoicing, tax localization, retention, and audit concerns.

## Feature 70: Partner Playbook Generator

Creates consulting delivery assets such as proposal structure, SOW assumptions, RACI, governance, and steering pack.

## Feature 71: Migration Risk Heatmap

Maps impact and probability by workstream and risk driver.

## Feature 72: Automated Do Not Migrate Report

Lists items that should be retired, replaced, archived, or validated before migration.

## Feature 73: Migration Value Tracker

Tracks avoided effort and indicative savings from scope reduction.

## Feature 74: Continuous Migration Monitor

Compares inventory snapshots and reports added, removed, and changed migration scope.

## Feature 75: Executive Story Generator

Creates CFO, CIO, COO, and Program Manager storylines from the same migration evidence.
