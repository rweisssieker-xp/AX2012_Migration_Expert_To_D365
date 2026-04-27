# Master Orchestration Plan

## Skill Routing

| Domain | Score | Skills | Commands |
| --- | ---: | --- | --- |
| governance | 100 | ax-migration-autonomous-governance-orchestrator, ax-migration-evidence-vault-manager, ax-migration-reconciliation-judge | governance-pack, evidence-vault, evidence-gates, reconciliation-judge |
| crm | 88 | ax-migration-crm-owner, ax-migration-lead-management-owner, ax-migration-customer-master-lead | commerce-crm-pack, process-twin |
| commerce | 64 | ax-migration-commerce-orchestrator, ax-migration-commerce-lead, ax-migration-pos-lead, ax-migration-payments-lead | commerce-pack, commerce-readiness, commerce-cutover |
| solo | 64 | ax-migration-master-orchestrator, ax-migration-solo-operator, ax-migration-ai-migration-brain | solo-orchestrate, solo-evidence, solo-gates, solo-test-plan, solo-signoff |
| fabric | 64 | ax-migration-intelligence-fabric-orchestrator, ax-migration-migration-memory, ax-migration-scenario-lab | intelligence-pack, migration-memory, benchmark, scenario-lab, war-game, value-realization |

## Missing Evidence To Check

- governance: External approvals, Evidence freshness, Reconciliation sign-off, Cutover rehearsal result
- crm: Lead-to-Cash traceability, Customer master harmonization, Dual-write decision
- commerce: CSU readiness, POS smoke tests, Payment/PCI evidence, Store cutover smoke tests
- solo: Role substitution, Self-approval gate, External approval boundary, Test evidence
- fabric: Benchmark baseline, Scenario assumptions, Portfolio wave data, Post-go-live KPI baseline

## Next CLI Commands

```powershell
python .\axmigrate.py governance-pack demo-projects\manufacturing\analysis --output orchestration-output\governance-pack
python .\axmigrate.py evidence-vault demo-projects\manufacturing\analysis --output orchestration-output\evidence-vault
python .\axmigrate.py evidence-gates demo-projects\manufacturing\analysis --output orchestration-output\evidence-gates
python .\axmigrate.py reconciliation-judge demo-projects\manufacturing\analysis --output orchestration-output\reconciliation-judge
python .\axmigrate.py commerce-crm-pack demo-projects\manufacturing\analysis --output orchestration-output\commerce-crm-pack
python .\axmigrate.py process-twin demo-projects\manufacturing\analysis --output orchestration-output\process-twin
python .\axmigrate.py commerce-pack demo-projects\manufacturing\analysis --output orchestration-output\commerce-pack
python .\axmigrate.py commerce-readiness demo-projects\manufacturing\analysis --output orchestration-output\commerce-readiness
python .\axmigrate.py commerce-cutover demo-projects\manufacturing\analysis --output orchestration-output\commerce-cutover
python .\axmigrate.py solo-orchestrate demo-projects\manufacturing\analysis --output orchestration-output\solo-orchestrate
python .\axmigrate.py solo-evidence demo-projects\manufacturing\analysis --output orchestration-output\solo-evidence
python .\axmigrate.py solo-gates demo-projects\manufacturing\analysis --output orchestration-output\solo-gates
python .\axmigrate.py solo-test-plan demo-projects\manufacturing\analysis --output orchestration-output\solo-test-plan
python .\axmigrate.py solo-signoff demo-projects\manufacturing\analysis --output orchestration-output\solo-signoff
python .\axmigrate.py intelligence-pack demo-projects\manufacturing\analysis --output orchestration-output\intelligence-pack
python .\axmigrate.py migration-memory demo-projects\manufacturing\analysis --output orchestration-output\migration-memory
python .\axmigrate.py benchmark demo-projects\manufacturing\analysis --output orchestration-output\benchmark
python .\axmigrate.py scenario-lab demo-projects\manufacturing\analysis --output orchestration-output\scenario-lab
python .\axmigrate.py war-game demo-projects\manufacturing\analysis --output orchestration-output\war-game
python .\axmigrate.py value-realization demo-projects\manufacturing\analysis --output orchestration-output\value-realization
```
