# Solo and Master Orchestrator

The Solo/Master-Orchestrator layer is designed for a single plugin user who must drive the migration with maximum AI/KI support. It generates the operating system around the migration: workplan, role substitution, evidence tracking, gates, daily next actions, tests, sign-off, audit binder, hypercare, benefits, stakeholder communication, and master routing to specialized skills.

## What It Can Do

| Capability | Output pattern |
| --- | --- |
| Initialize project | Solo project folder, charter, workplan, role substitution matrix. |
| Run orchestration | Analysis outputs plus project operating artifacts. |
| Route work to skills | Master orchestration plan, skill routing map, action queue, evidence-to-skill matrix. |
| Govern evidence | Evidence completeness matrix, missing stakeholder register, confidence ledger. |
| Control gates | Self-approval gates, external approval pack, blocked decision register. |
| Run daily execution | Daily migration command sheet and next-best-action board. |
| Test the project | Key-user, UAT, regression, process owner validation, test evidence, and sign-off outputs. |
| Manage cutover | War-room board, cutover smoke tests, rollback and communication prompts. |
| Stabilize after go-live | Hypercare command center, incident model, support runbooks, BAU transition. |
| Protect value | Benefits realization, value tracker, waste hunter, scope defense, drift detector. |

## Master-Orchestrator Synonyms

The master agent can be described as:

- Master-Orchestrator
- Migration Command Agent
- AI Migration Brain
- Autonomous Migration Controller
- Migration Control Tower
- Program Copilot
- Delivery Orchestrator
- Skill Router
- Evidence Gatekeeper
- Go-Live Commander

## Typical Solo Flow

```powershell
python .\axmigrate.py solo-init "Contoso AX Migration" --output solo-migration
python .\axmigrate.py solo-run --project "Contoso AX Migration" --input plugins\ax-to-d365fo-migration-expert\examples\sample-ax-inventory.csv --output solo-migration
python .\axmigrate.py solo-orchestrate solo-migration\contoso-ax-migration --output master-orchestration\contoso
python .\axmigrate.py solo-evidence solo-migration\contoso-ax-migration
python .\axmigrate.py solo-gates solo-migration\contoso-ax-migration
python .\axmigrate.py solo-test-plan solo-migration\contoso-ax-migration
python .\axmigrate.py solo-signoff solo-migration\contoso-ax-migration
```

## Role Coverage

The Solo/Master layer is supported by skills for:

- CEO, board, executive sponsor.
- CIO, CTO, enterprise architecture.
- CISO, security, compliance, audit.
- Project manager, PMO, steering committee.
- Project team members and delivery execution.
- CFO, COO, data governance, integration, QA/testing.
- Enterprise architect, vendor/procurement, legal/compliance, support/ITSM, partner sales.
- Key users, UAT testers, regression testers, process owners, test execution copilot.
- CXP, CRM, Lead Management, Commerce, CSU, POS, POS Offline, Payments, Store Ops, Loyalty, Pricing, Channel Sync, Hardware, PCI, Customer Master, Call Center, Marketplace, Analytics, and Store Training.

## External Approval Boundary

The plugin can generate evidence, recommendations, control packs, and sign-off candidates. It should not self-approve real-world production decisions that require accountable humans or external authorities. Executive go/no-go, security approval, PCI/payment approval, legal approval, audit approval, finance approval, customer acceptance, and production release approval remain external decisions.
