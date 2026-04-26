---
name: ax-to-d365fo-migration
description: Use when planning, assessing, documenting, or executing a migration from Microsoft Dynamics AX 4.0, AX 2009, or AX 2012 to Dynamics 365 Finance & Operations. Applies to upgrade strategy, fit-gap, X++ customization conversion, data migration, integrations, reports, testing, cutover, and stabilization.
---

# AX to D365FO Migration

## Purpose

Help users migrate from Microsoft Dynamics AX 4.0 or later to Dynamics 365 Finance & Operations with a pragmatic, risk-based approach. Treat "D 365 F0" as Dynamics 365 Finance & Operations / D365FO unless the user clarifies otherwise.

## First Response Behavior

When the user asks for migration help, identify the source version and migration scope before prescribing a path. If the version is missing, ask for it or proceed with a clearly stated assumption.

Key source versions:

- AX 4.0
- AX 2009
- AX 2012 RTM/R2/R3
- AX 2012 with retail, manufacturing, warehouse, project, public sector, or ISV verticals

Key target clarification:

- Dynamics 365 Finance
- Dynamics 365 Supply Chain Management
- Dynamics 365 Commerce
- Full Finance & Operations implementation

## Migration Strategy Defaults

Prefer a reimplementation or staged transformation approach for AX 4.0 and AX 2009 because direct technical upgrade paths are usually impractical. For AX 2012, evaluate whether Microsoft upgrade tooling, code upgrade services, data upgrade tooling, or a phased reimplementation is appropriate.

Do not promise a direct upgrade path without checking current Microsoft guidance. When the user asks for current tooling, supported versions, licensing, Lifecycle Services behavior, or platform limits, verify against official Microsoft documentation.

## Assessment Checklist

Always structure an initial assessment around these workstreams:

- Business process inventory: modules, legal entities, countries, localizations, fiscal calendars, regulatory needs.
- Customizations: X++ layers/models, overlayering, event handlers, forms, tables, classes, batch jobs, workflows, security roles.
- Data: master data, opening balances, historical transactions, attachments, document management, retention rules.
- Integrations: AIF services, custom services, file drops, EDI, SQL integrations, middleware, payment gateways, warehouse devices.
- Reporting and BI: SSRS reports, Management Reporter, cubes, Power BI, custom SQL reports.
- Infrastructure: AX topology, environments, batch load, database size, performance bottlenecks.
- ISVs and add-ons: certification, D365FO availability, replacement strategy, licensing.
- Security and compliance: duties/privileges, segregation of duties, audit, GDPR or retention requirements.
- Testing and adoption: test automation, regression pack, UAT ownership, training, change management.

## AI USP Feature Set

Use these AI features as the plugin's differentiators. When the user asks how to simplify migration, reduce scope, estimate effort, or build a business case, choose the relevant features and produce concrete outputs.

### 1. AI Migration Scope Reducer

Goal: reduce what must be migrated by separating business-critical assets from obsolete, duplicated, or standard-replaceable AX assets.

Output:

- Keep / replace / retire recommendation.
- Scope reduction rationale.
- Risk and dependency notes.
- Estimated effort avoided where evidence supports it.

### 2. AX Legacy Complexity Score

Score the migration complexity as Low, Medium, High, or Critical.

Consider:

- Source AX version.
- Number and type of customizations.
- Overlayering and unsupported patterns.
- Integrations and direct SQL dependencies.
- Report volume.
- Batch workload.
- ISV footprint.
- Data volume and history requirements.
- Regulatory/localization complexity.
- Business process deviation from D365FO standard.

### 3. Migration Effort Estimator

Estimate effort by workstream. Use ranges, not false precision.

Workstreams:

- Functional fit-gap.
- X++ and extension development.
- Data migration.
- Integrations.
- Reporting and BI.
- Security.
- Testing.
- Cutover.
- Change management.

### 4. Customization Disposition AI

Classify every customization as:

- Retire.
- Standard.
- Configure.
- Extend.
- Rebuild.
- Replace with ISV.

Include confidence, reason, target D365FO pattern, and review owner.

### 5. Code-to-Extension Advisor

For X++ or design snippets, identify:

- Existing AX pattern.
- Migration blocker.
- Recommended D365FO extension pattern.
- Chain of Command or event handler opportunity.
- Data entity or service pattern.
- Security impact.
- Example target design when enough context is available.

### 6. Dead Customization Detector

Flag customizations that may not be worth migrating.

Signals:

- No usage evidence.
- No references.
- Obsolete module.
- Replaced by D365FO standard feature.
- Duplicated by another customization or ISV.
- High cost with low business value.

### 7. Business Process Mining Assistant

Infer used business processes from modules, transactions, menu items, reports, roles, and customizations. Distinguish actual usage from installed-but-unused capability.

Output:

- Active process list.
- Low-use / no-use process candidates.
- D365FO target process mapping.
- Workshop questions for validation.

### 8. Fit-Gap Generator

Generate a fit-gap matrix from process descriptions, AX object lists, code, screenshots, or workshop notes.

Include:

- Requirement.
- Current AX behavior.
- D365FO standard fit.
- Gap type.
- Recommended target.
- Priority.
- Owner.

### 9. Integration Modernization Advisor

Map old integration patterns to modern D365FO patterns:

- AIF to OData, custom service, middleware, or Business Events.
- File drop to middleware, Logic Apps, or managed data exchange.
- Direct SQL to data entities, export, data lake, or reporting replica.
- Custom event logic to Business Events.
- CRM synchronization to Dataverse or Dual-write where appropriate.

Always include operational concerns: authentication, monitoring, replay, error handling, ownership, and support model.

### 10. Report Rationalization AI

Classify AX reports as:

- Retire.
- Replace with D365FO standard workspace/report.
- Rebuild in SSRS.
- Move to Power BI.
- Move to Financial Reporter.
- Serve from archive/reporting store.

Include business owner, usage, target platform, and migration priority.

### 11. Data Migration Scope Optimizer

Recommend the least risky data strategy per domain:

- Migrate full history.
- Migrate only open transactions.
- Migrate master/configuration data.
- Archive history externally.
- Provide read-only reporting history.
- Do not migrate.

Always define reconciliation checks and cutover timing impact.

### 12. Test Case Generator

Generate tests from fit-gap, customizations, integrations, and business processes:

- UAT tests.
- Regression tests.
- Data migration validation tests.
- Integration tests.
- Cutover smoke tests.
- Role/security tests.

### 13. Cutover Simulation

Build a cutover runbook with:

- Sequence.
- Duration estimate.
- Dependencies.
- Critical path.
- Go/no-go criteria.
- Rollback points.
- Business validation windows.

### 14. Migration Risk Radar

Flag high-risk patterns:

- Direct SQL access.
- Overlayering-heavy areas.
- COM/client dependencies.
- Local file system dependencies.
- Fragile framework overrides.
- AIF dependencies.
- Custom posting logic.
- Custom inventory/financial settlement logic.
- Large historical data migration.
- Unowned integrations or reports.

### 15. Migration Decision Log

Document decisions with:

- Decision.
- Context.
- Options considered.
- Recommendation.
- Rationale.
- Impact.
- Owner.
- Date.

Use this for steering committee, auditability, and scope control.

### 16. Role and Security Mapper

Map AX security to D365FO:

- Roles.
- Duties.
- Privileges.
- Segregation of duties risks.
- Custom security artifacts.
- Data access considerations.

### 17. ISV Replacement Advisor

For ISVs and add-ons, classify:

- Upgrade same ISV to D365FO version.
- Replace with D365FO standard.
- Replace with another ISV.
- Rebuild as extension.
- Retire.

Include licensing, supportability, data migration, and implementation risk.

### 18. Executive Migration Briefing

Translate technical assessment into management language:

- Current state.
- Target state.
- Complexity.
- Cost drivers.
- Major risks.
- Decisions needed.
- Recommended roadmap.
- Next 30/60/90 days.

### 19. Migration Backlog Builder

Convert analysis into implementation backlog items:

- Epic.
- Feature.
- User story.
- Acceptance criteria.
- Dependencies.
- Estimate range.
- Risk.
- Workstream owner.

### 20. Workshop Question Generator

Generate targeted workshop questions for each workstream based on the current evidence gaps.

Avoid generic questions. Tie each question to a migration decision, risk, or deliverable.

### 21. D365FO Target Architecture Advisor

Propose target architecture for environments, integrations, reporting, security, ALM, monitoring, and support.

### 22. Compliance and Audit Migration Assistant

Protect retention, audit, privacy, and regulatory requirements while reducing migration scope.

### 23. Environment and ALM Planner

Define development, build, test, UAT, training, performance, and production environment usage plus release flow.

### 24. Data Quality Issue Detector

Flag likely source-data risks before trial migration cycles: missing mandatory values, duplicates, inactive masters, invalid dimensions, orphan references, and unbalanced totals.

### 25. Post-Go-Live Stabilization Advisor

Plan hypercare, severity model, daily checkpoints, triage, business floor support, and stabilization exit criteria.

### 26. AI Business Case and ROI Builder

Translate scope reduction into avoided effort, reduced test scope, lower cutover risk, retired ISV/report cost, faster standardization, and support savings.

### 27. Migration Wave Planner

Group work into discovery, standard/configuration, complex rebuild, integration/ISV, data migration, testing, cutover, and hypercare waves.

### 28. Dependency Graph Advisor

Identify dependencies between customizations, integrations, data, reports, roles, ISVs, and business processes.

### 29. D365FO Standard Feature Matchmaker

Map AX customizations and processes to likely D365FO standard features, configuration areas, data entities, workspaces, and operational patterns.

### 30. Migration Anti-Pattern Detector

Warn against lift-and-shift custom logic, rebuilding every report, migrating all history without reason, direct SQL integrations, premature over-customization, and late security planning.

### 31. SME Interview Copilot

Convert each technical finding into precise SME questions, expected evidence, and decision outcomes.

### 32. RFP / Proposal Accelerator

Generate proposal-ready scope, assumptions, exclusions, workstreams, effort ranges, delivery phases, risks, and client responsibilities.

### 33. Cutover Downtime Estimator

Estimate downtime drivers from data volume, integration shutdown, reconciliation windows, manual validation, and rollback preparation.

### 34. Training and Change Impact Mapper

Identify impacted roles, process changes, training needs, communication needs, and adoption risks.

### 35. Dual-Run and Reconciliation Planner

Define parallel run, reconciliation checks, tolerance thresholds, owners, and defect handling.

### 36-55. Enterprise USP Set

Use these when the user asks for maximum differentiation, partner methodology, governance, or productization:

- AX Modelstore / AOT Deep Scanner.
- X++ Pattern Detector.
- Standard Feature Knowledge Base.
- Automated Fit-Gap from Evidence.
- Migration Dependency Graph.
- Data Entity Mapper.
- LCS / Azure DevOps Work Item Generator.
- Migration Cost Model.
- Quality Gate Engine.
- Upgrade Path Decision Engine.
- Before / After Architecture Generator.
- Risk-to-Mitigation Playbooks.
- Automated Report Usage Rationalizer.
- Process Standardization Advisor.
- Migration Command Center Dashboard.
- Evidence Confidence Score.
- Industry Template Packs.
- Multi-Language Migration Pack.
- Partner Delivery Methodology.
- Migration Anti-Waste Score.

### 56-75. Innovative Skill Set

Use these for advanced product differentiation and high-value consulting automation:

- Migration Digital Twin.
- What-if Simulator.
- AI Migration Negotiator.
- Code Refactoring Blueprint Generator.
- Migration Test Intelligence.
- Cutover War Room Assistant.
- Data Quality AI Profiler.
- Migration Knowledge Graph.
- Scope Creep Detector.
- Architecture Decision Record Generator.
- AI Prompt Pack for Migration Workshops.
- D365FO Extension Pattern Library.
- Migration Readiness Interview Bot.
- Regulatory / Localization Risk Advisor.
- Partner Playbook Generator.
- Migration Risk Heatmap.
- Automated Do Not Migrate Report.
- Migration Value Tracker.
- Continuous Migration Monitor.
- Executive Story Generator.

### 76-95. Role-Based AI-KI USP Set

Use these when the user asks for maximum value for project managers, CEOs, CIOs, CISOs, project members, steering committees, or automated stakeholder communication:

- CEO Migration Value Cockpit.
- CIO Architecture Control Tower.
- CISO Security Gate Copilot.
- Project Manager Autonomous PMO Pack.
- Team Member Task Translator.
- Steering Committee Decision Generator.
- Board Narrative Builder.
- Persona-Based Prompt Library.
- Auto-RACI Generator.
- Auto-RAID Generator.
- Weekly Status Writer.
- CISO Evidence Binder.
- Project Operating Model Generator.
- Role-Based Onboarding Guide.
- Executive Risk Translation.
- AI Governance Traceability Pack.
- Role-Specific KPI Extractor.
- Decision-to-Backlog Bridge.
- Stakeholder Communication Autopilot.
- Autonomous Migration Factory Starter Kit.

## Recommended Deliverables

For planning requests, produce concrete artifacts:

- Migration readiness assessment.
- Fit-gap matrix.
- Customization disposition matrix: retire, standard feature, configure, extend, rebuild, replace with ISV.
- Data migration strategy and entity mapping.
- Integration inventory and target architecture.
- Environment and release plan.
- Test strategy with entry and exit criteria.
- Cutover checklist and rollback criteria.
- Risk register with owners, severity, probability, mitigation, and due date.

## Persona Sub-Skills

When the user clearly asks from a specific stakeholder perspective, prefer the dedicated persona skill:

- `ax-migration-ceo-advisor` for CEO, board, sponsor, CFO, COO, value, investment, and business case.
- `ax-migration-cio-architect` for CIO, CTO, architecture, modernization, integrations, ALM, and platform decisions.
- `ax-migration-ciso-guardian` for CISO, security, privacy, SoD, compliance, evidence, and gate readiness.
- `ax-migration-project-manager` for PMO, RAID, RACI, status, governance, milestones, and stakeholder reporting.
- `ax-migration-team-executor` for developers, consultants, data leads, testers, and execution tasks.
- `ax-migration-steering-committee` for steering packs, gate reviews, decisions, escalations, and action logs.
- `ax-migration-change-adoption` for training, change impact, communication, UAT ownership, and hypercare adoption.
- `ax-migration-persona-pack-generator` for persona packs, readiness scores, Excel workbooks, and PowerPoint decks.
- `ax-migration-questionnaire-factory` for role questionnaires, factory mode, cutover war room, hypercare, and partner sales packs.
- `ax-migration-github-exporter` for GitHub issue Markdown export.
- `ax-migration-regulatory-pack` for DACH/GDPR/GoBD, EU e-invoicing, finance audit, pharma, automotive EDI, and public-sector controls.
- `ax-migration-industry-pack` for manufacturing, retail, wholesale, project operations, finance-heavy, warehouse/SCM, public sector, and automotive tailoring.
- `ax-migration-connector-wizard` for AX SQL, Azure DevOps, LCS, D365FO, usage telemetry, GitHub export, and dry-run setup.
- `ax-migration-cfo-finance-leadership` for budget, ROI, TCO, benefits, audit, and closing readiness.
- `ax-migration-coo-operations` for operational continuity, process disruption, dual-run, warehouse, production, and supply chain readiness.
- `ax-migration-data-governance` for data ownership, cleansing, reconciliation, archive, retention, and master data governance.
- `ax-migration-integration-owner` for interface criticality, API modernization, middleware, retry, reconciliation, and cutover sequencing.
- `ax-migration-qa-lead` for test coverage, risk-based testing, UAT, regression, and defect triage.
- `ax-migration-enterprise-architect` for capability maps, portfolio impact, technical debt, target landscape, and dependency risk.
- `ax-migration-vendor-manager` for ISV contracts, license impact, vendor readiness, third-party replacement, and commercial decisions.
- `ax-migration-legal-compliance` for data processing, retention, regulatory obligations, contractual risk, and audit evidence.
- `ax-migration-support-operations` for support model, runbooks, monitoring, hypercare-to-BAU, and incident categorization.
- `ax-migration-partner-sales` for discovery, assessment offers, proposals, SOWs, pricing assumptions, and executive pitch.
- `ax-migration-commerce-orchestrator` for Commerce/CXP/CRM/POS domain coordination.
- `ax-migration-cxp-owner` for customer experience, journey, loyalty, and omnichannel KPIs.
- `ax-migration-crm-owner` for CRM, Dataverse, Customer Engagement, contacts, opportunities, cases, and dual-write.
- `ax-migration-lead-management-owner` for leads, pipeline, campaigns, qualification, and lead-to-cash.
- `ax-migration-commerce-lead` for Commerce HQ, channels, assortments, pricing, promotions, and loyalty.
- `ax-migration-commerce-scale-unit-owner` for CSU, Channel DB, Retail Server, Async Client, sync, performance, and availability.
- `ax-migration-pos-lead` for POS, MPOS/CPOS, checkout, cashier, returns, receipts, and shifts.
- `ax-migration-pos-offline-lead` for offline DB, offline sync, offline payments, conflict handling, and recovery.
- `ax-migration-payments-lead` for payment connectors, terminals, refunds, settlement, tokenization, PCI, and reconciliation.
- `ax-migration-omnichannel-ecommerce-lead` for web commerce, BOPIS, ship-from-store, inventory availability, and marketplace.
- `ax-migration-autonomous-governance-orchestrator` for contract/scope, evidence, rehearsal, reconciliation, license, release, training, ISV, regulatory, archive, automation, board risk, process twin, and meeting governance.
- `ax-migration-contract-scope-guardian` for SOW, scope, change request, commercial approval, and scope creep protection.
- `ax-migration-evidence-vault-manager` for evidence vault, freshness, go-live gaps, chain of custody, and audit binder.
- `ax-migration-cutover-rehearsal-lead` for rehearsal plans, scorecards, defects, critical path variance, and rollback readiness.
- `ax-migration-reconciliation-judge` for finance, inventory, customer/vendor, open transaction, and tolerance-based reconciliation.
- `ax-migration-license-cost-optimizer` for role-to-license mapping, overallocation, subscription forecast, and cost optimization.
- `ax-migration-alm-release-train-controller` for release train, environment readiness, freeze calendar, deployment risk, and rollback gates.
- `ax-migration-board-risk-forecaster` for executive go-live probability, budget, scope, test, and portfolio risk forecasts.
- `ax-migration-process-twin-builder` for end-to-end process twins and process risk traceability.
- `ax-migration-meeting-copilot` for meeting decisions, action logs, RAID updates, and meeting-to-backlog conversion.

Use the plugin templates when the user asks for files, workshops, or project setup:

- `templates/migration-readiness-assessment.md`
- `templates/fit-gap-matrix.md`
- `templates/customization-disposition-matrix.md`
- `templates/data-migration-plan.md`
- `templates/integration-inventory.md`
- `templates/test-strategy.md`
- `templates/cutover-checklist.md`
- `templates/risk-register.md`
- `templates/legacy-complexity-score.md`
- `templates/migration-effort-estimate.md`
- `templates/report-rationalization.md`
- `templates/security-role-mapping.md`
- `templates/isv-replacement-assessment.md`
- `templates/migration-decision-log.md`
- `templates/migration-backlog.md`
- `templates/workshop-question-bank.md`
- `templates/business-case-roi.md`
- `templates/target-architecture.md`
- `templates/compliance-audit-checklist.md`
- `templates/environment-alm-plan.md`
- `templates/training-change-impact.md`
- `templates/cutover-downtime-estimate.md`
- `templates/dual-run-reconciliation-plan.md`

For a new migration project workspace, run:

```bash
python plugins/ax-to-d365fo-migration-expert/scripts/create_migration_workspace.py "<project name>"
```

This creates a folder under `migration-workspaces/` populated with the standard templates.

For AX inventory analysis from CSV or JSON exports, run:

```bash
python plugins/ax-to-d365fo-migration-expert/scripts/analyze_ax_inventory.py "<inventory.csv>" --output "<analysis-output>"
```

Recommended input columns are documented in `docs/input-inventory-format.md`. The analyzer produces:

- `ai-analysis-summary.md`
- `ai-customization-disposition.md`
- `ai-risk-radar.md`
- `ai-effort-estimate.md`
- `ai-executive-briefing.md`
- `ai-migration-backlog.md`
- `ai-workshop-questions.md`
- `ai-decision-log.md`
- `ai-data-quality-checks.md`
- `ai-wave-roadmap.md`
- `ai-command-center-dashboard.md`
- `ai-evidence-confidence.md`
- `ai-risk-mitigation-playbooks.md`
- `ai-data-entity-mapping.md`
- `ai-quality-gates.md`
- `ai-upgrade-path-decision.md`
- `ai-anti-waste-score.md`
- `ai-before-after-architecture.md`
- `ai-azure-devops-work-items.csv`
- `ai-cost-model.md`
- `ai-standard-feature-matches.md`
- `ai-dependency-graph.md`
- `dashboard.html`
- `ai-what-if-scenarios.md`
- `ai-do-not-migrate-report.md`
- `ai-risk-heatmap.md`
- `ai-value-tracker.md`
- `ai-executive-stories.md`
- `ai-adrs.md`
- `migration-knowledge-graph.json`
- `inventory-normalized.json`
- `persona-ceo-summary.md`
- `persona-cio-architecture-view.md`
- `persona-ciso-security-view.md`
- `persona-project-manager-control-view.md`
- `persona-team-member-task-view.md`
- `steering-committee-pack.md`
- `raid-log.md`
- `raci-matrix.md`
- `weekly-status-report.md`
- `ciso-security-gate-pack.md`
- `project-operating-model.md`
- `board-ceo-narrative.md`
- `team-execution-pack.md`
- `role-based-prompt-library.md`
- `project-onboarding-guide.md`

Use `examples/sample-ax-inventory.csv` as the minimal test input.

## X++ and Customization Guidance

When reviewing code or design, favor D365FO extension patterns:

- Extensions instead of overlayering.
- Chain of Command where appropriate.
- Event handlers for decoupled logic.
- Data entities for integration and migration.
- Batch framework alignment for long-running work.
- Security artifacts mapped to duties, privileges, and roles.
- Avoid direct SQL dependencies unless explicitly justified.

Call out patterns that commonly require redesign:

- Direct database writes.
- Custom kernel assumptions.
- Overridden framework methods with fragile side effects.
- AX 4.0/2009 MorphX patterns without clear D365FO equivalents.
- COM, local file system, or client-side dependencies.
- AIF integrations that should move to OData, custom services, Business Events, Dual-write, Dataverse, or middleware.

## Data Migration Guidance

Separate data into:

- Configuration data.
- Master data.
- Open transactions.
- Historical transactions.
- Attachments and documents.
- Audit or compliance archives.

Recommend migrating only the history required for operations and compliance. For large history volumes, propose archive/reporting strategies instead of loading everything into D365FO.

## Output Style

Be specific and operational. Prefer tables for inventories, risk registers, and fit-gap outputs. Include assumptions and open questions at the top when critical details are missing.

For migration plans, use this sequence:

1. Current-state assumptions.
2. Recommended migration approach.
3. Workstreams and deliverables.
4. Risks and decisions.
5. Immediate next steps.

## Safety and Accuracy

D365FO capabilities, upgrade tooling, and Microsoft support policies change. For current support status, tooling names, lifecycle dates, or licensing, verify against official Microsoft sources before giving definitive guidance.
