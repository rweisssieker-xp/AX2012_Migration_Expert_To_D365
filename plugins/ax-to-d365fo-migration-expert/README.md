# AX to D365FO Migration Expert

Codex plugin for AI-powered Microsoft Dynamics AX 4.0, AX 2009, and AX 2012 migration scope reduction and delivery acceleration targeting Dynamics 365 Finance & Operations.

## Included Skill

- `ax-to-d365fo-migration`: migration assessment, planning, fit-gap, X++ customization disposition, data migration, integration redesign, reporting, testing, cutover, and stabilization guidance.

## Max AI USP Feature List

The main USP is AI-powered migration scope reduction: identify what must move, what D365FO standard can replace, and what should be retired.

Included AI feature areas:

- AI Migration Scope Reducer
- AX Legacy Complexity Score
- Migration Effort Estimator
- Customization Disposition AI
- Code-to-Extension Advisor
- Dead Customization Detector
- Business Process Mining Assistant
- Fit-Gap Generator
- Integration Modernization Advisor
- Report Rationalization AI
- Data Migration Scope Optimizer
- Test Case Generator
- Cutover Simulation
- Migration Risk Radar
- Migration Decision Log
- Role and Security Mapper
- ISV Replacement Advisor
- Executive Migration Briefing
- Migration Backlog Builder
- Workshop Question Generator
- D365FO Target Architecture Advisor
- Compliance and Audit Migration Assistant
- Environment and ALM Planner
- Data Quality Issue Detector
- Post-Go-Live Stabilization Advisor
- AI Business Case and ROI Builder
- Migration Wave Planner
- Dependency Graph Advisor
- D365FO Standard Feature Matchmaker
- Migration Anti-Pattern Detector
- SME Interview Copilot
- RFP / Proposal Accelerator
- Cutover Downtime Estimator
- Training and Change Impact Mapper
- Dual-Run and Reconciliation Planner
- AX Modelstore / AOT Deep Scanner
- X++ Pattern Detector
- Standard Feature Knowledge Base
- Automated Fit-Gap from Evidence
- Migration Dependency Graph
- Data Entity Mapper
- LCS / Azure DevOps Work Item Generator
- Migration Cost Model
- Quality Gate Engine
- Upgrade Path Decision Engine
- Before / After Architecture Generator
- Risk-to-Mitigation Playbooks
- Automated Report Usage Rationalizer
- Process Standardization Advisor
- Migration Command Center Dashboard
- Evidence Confidence Score
- Industry Template Packs
- Multi-Language Migration Pack
- Partner Delivery Methodology
- Migration Anti-Waste Score
- Migration Digital Twin
- What-if Simulator
- AI Migration Negotiator
- Code Refactoring Blueprint Generator
- Migration Test Intelligence
- Cutover War Room Assistant
- Data Quality AI Profiler
- Migration Knowledge Graph
- Scope Creep Detector
- Architecture Decision Record Generator
- AI Prompt Pack for Migration Workshops
- D365FO Extension Pattern Library
- Migration Readiness Interview Bot
- Regulatory / Localization Risk Advisor
- Partner Playbook Generator
- Automated Do Not Migrate Report
- Migration Value Tracker
- Continuous Migration Monitor
- Executive Story Generator
- AX SQL / Modelstore Direct Connector
- Azure DevOps Work Item API Push
- LCS Metadata Connector
- D365FO Metadata / OData Connector
- Usage Telemetry Analyzer
- Extended D365FO Knowledge Base

See `docs/ai-usp-feature-list.md` for detailed feature behavior, inputs, and outputs.

## Included Templates

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
- `templates/command-center-dashboard.md`
- `templates/evidence-confidence-score.md`
- `templates/risk-mitigation-playbook.md`
- `templates/data-entity-mapping.md`
- `templates/quality-gate-engine.md`
- `templates/upgrade-path-decision.md`
- `templates/anti-waste-score.md`
- `templates/before-after-architecture.md`
- `templates/azure-devops-work-items.md`
- `templates/standard-feature-matchmaker.md`
- `templates/industry-template-pack.md`
- `templates/migration-methodology.md`

## Helper Script

Unified CLI:

```bash
python plugins/ax-to-d365fo-migration-expert/scripts/migration_cli.py analyze \
  plugins/ax-to-d365fo-migration-expert/examples/sample-ax-inventory.csv \
  --output migration-analysis/contoso
```

Create a new customer/project workspace from the templates:

```bash
python plugins/ax-to-d365fo-migration-expert/scripts/create_migration_workspace.py "Contoso AX Migration"
```

The script writes files under `migration-workspaces/<project-name>/`.

Analyze AX inventory CSV/JSON files and generate AI assessment reports:

```bash
python plugins/ax-to-d365fo-migration-expert/scripts/analyze_ax_inventory.py \
  plugins/ax-to-d365fo-migration-expert/examples/sample-ax-inventory.csv \
  --output migration-analysis/contoso
```

Generated reports:

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

See `docs/input-inventory-format.md` for recommended inventory columns.
See `docs/installation-and-usage.md` for setup, analyzer usage, configuration, and tests.

Export analysis to Excel and PowerPoint:

```bash
python plugins/ax-to-d365fo-migration-expert/scripts/migration_cli.py export migration-analysis/contoso --output migration-exports/contoso
```

Validate the plugin:

```bash
python plugins/ax-to-d365fo-migration-expert/scripts/migration_cli.py validate
```

## Typical Prompts

- Assess my Dynamics AX environment and produce a D365FO migration readiness plan.
- Create a migration checklist for AX 2012 customizations, integrations, reports, and data.
- Review this X++ customization and suggest a D365FO extension-based migration approach.
- Analyze this AX inventory export and classify what should be retired, replaced, extended, or rebuilt.

## Publishing Notes

The plugin is usable locally. Before public distribution, replace the `example.org` contact, homepage, repository, privacy, and terms URLs in `.codex-plugin/plugin.json` with real publisher URLs.
