# AX Inventory Input Format

`scripts/analyze_ax_inventory.py` accepts CSV or JSON files. It is schema-tolerant, but these columns produce the best output.

## Recommended Columns

| Column | Meaning | Example |
| --- | --- | --- |
| Category | Object, Integration, Report, ISV, Security, Data | Integration |
| ObjectType | AX object or artifact type | Class, Form, Service, Report |
| Name | Object or artifact name | AIFCustomerExport |
| Layer | AX layer, model, or package | CUS |
| Module | Business module or process area | Accounts receivable |
| Usage | Usage evidence or frequency | Daily, High, Low |
| Complexity | Low, Medium, High | High |
| Technology | Technical pattern | AIF, SSRS, Direct SQL |
| BusinessPurpose | Business reason for the artifact | Exports customer updates |

## Example

```powershell
python plugins\ax-to-d365fo-migration-expert\scripts\analyze_ax_inventory.py `
  plugins\ax-to-d365fo-migration-expert\examples\sample-ax-inventory.csv `
  --output migration-analysis\contoso
```

## Generated Reports

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
