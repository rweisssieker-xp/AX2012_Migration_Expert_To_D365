# Skill Handbook

This handbook lists every Codex skill currently included in the AX to D365FO Migration Expert plugin. It is generated from the real `SKILL.md` files and groups the skills by operating area.

## Current Coverage

| Area | Count |
| --- | ---: |
| Core Migration | 1 |
| Executive, Leadership, PMO | 8 |
| Functional, Data, Integration, QA | 8 |
| Delivery Team, Change, Support, Vendor, Legal | 12 |
| Solo and Master Orchestrator | 21 |
| Key User and Testing | 5 |
| Commerce, CXP, CRM, POS | 21 |
| Autonomous Governance and Evidence | 16 |
| Total | 92 |

## How To Read This Handbook

- **Skill** is the exact folder and frontmatter name.
- **When to use** is the trigger description from the skill.
- **Primary output** summarizes what the skill should produce or influence.
- **CLI relation** shows direct commands where one exists; many skills are used by the master orchestrator rather than called directly.

## Core Migration

| Skill | When to use | Primary output | CLI relation |
| --- | --- | --- | --- |
| `ax-to-d365fo-migration` | Use when planning, assessing, documenting, or executing a migration from Microsoft Dynamics AX 4.0, AX 2009, or AX 2012 to Dynamics 365 Finance & Operations. Applies to upgrade strategy, fit-gap, X++ customization conversion, data migration, integrations, reports, testing, cutover, and stabilization. | End-to-end assessment, scope reduction, migration backlog, risks, dashboard, and delivery artifacts. | `analyze`, `scan-code`, `dashboard`, `init`, `export`, `validate` |

## Executive, Leadership, PMO

| Skill | When to use | Primary output | CLI relation |
| --- | --- | --- | --- |
| `ax-migration-ceo-advisor` | Use when a CEO, board member, executive sponsor, managing director, CFO, COO, or senior business leader needs AX to D365FO migration value, risk, business case, scope reduction, investment, steering, or decision support. | Role-specific leadership pack, decisions, KPIs, risks, value narrative, and next actions. | No direct command; used by orchestration and prompts |
| `ax-migration-cfo-finance-leadership` | Use when a CFO, finance director, controller, audit sponsor, or finance leadership team needs AX to D365FO migration budget control, ROI, TCO, benefits realization, closing readiness, audit readiness, or financial decision support. | Role-specific leadership pack, decisions, KPIs, risks, value narrative, and next actions. | No direct command; used by orchestration and prompts |
| `ax-migration-cio-architect` | Use when a CIO, CTO, enterprise architect, solution architect, IT director, or technical leadership team needs AX to D365FO target architecture, modernization path, integration strategy, technical debt, ALM, environment, or platform decisions. | Role-specific leadership pack, decisions, KPIs, risks, value narrative, and next actions. | No direct command; used by orchestration and prompts |
| `ax-migration-ciso-guardian` | Use when a CISO, security lead, compliance officer, data protection officer, audit lead, risk manager, or security architect needs AX to D365FO migration security, privacy, roles, SoD, controls, evidence, gate readiness, or compliance guidance. | Role-specific leadership pack, decisions, KPIs, risks, value narrative, and next actions. | No direct command; used by orchestration and prompts |
| `ax-migration-coo-operations` | Use when a COO, operations director, supply chain leader, warehouse leader, production leader, or business operations sponsor needs AX to D365FO migration operational continuity, disruption, dual-run, cutover, warehouse, production, or supply chain readiness guidance. | Role-specific leadership pack, decisions, KPIs, risks, value narrative, and next actions. | No direct command; used by orchestration and prompts |
| `ax-migration-partner-sales` | Use when partners, sales teams, solution sellers, consulting leaders, pre-sales architects, or account teams need AX to D365FO discovery workshop kits, assessment offers, proposals, SOWs, pricing assumptions, or client executive pitch packs. | Role-specific leadership pack, decisions, KPIs, risks, value narrative, and next actions. | No direct command; used by orchestration and prompts |
| `ax-migration-project-manager` | Use when a project manager, program manager, PMO, scrum master, delivery lead, workstream lead, or steering coordinator needs AX to D365FO migration planning, status, RAID, RACI, governance, milestones, scope control, backlog, or stakeholder communication. | Role-specific leadership pack, decisions, KPIs, risks, value narrative, and next actions. | No direct command; used by orchestration and prompts |
| `ax-migration-steering-committee` | Use when preparing or running AX to D365FO steering committee, executive review, board update, gate review, decision meeting, escalation session, or stakeholder alignment across CEO, CIO, CISO, PMO, and delivery leads. | Role-specific leadership pack, decisions, KPIs, risks, value narrative, and next actions. | No direct command; used by orchestration and prompts |

## Functional, Data, Integration, QA

| Skill | When to use | Primary output | CLI relation |
| --- | --- | --- | --- |
| `ax-migration-alm-devops-lead` | Use when ALM, DevOps, pipelines, releases, builds, deployments, rollback, branch strategy, or environment release governance. | Workstream pack, validation checklist, risks, owners, test coverage, and evidence outputs. | No direct command; used by orchestration and prompts |
| `ax-migration-data-governance` | Use when data owners, master data managers, data migration leads, data governance teams, or records owners need AX to D365FO data ownership, cleansing, reconciliation, retention, archive, master data, or migration evidence guidance. | Workstream pack, validation checklist, risks, owners, test coverage, and evidence outputs. | No direct command; used by orchestration and prompts |
| `ax-migration-environment-manager` | Use when D365FO environments, sandbox, UAT, training, performance, production, refreshes, access, or environment planning needs. | Workstream pack, validation checklist, risks, owners, test coverage, and evidence outputs. | No direct command; used by orchestration and prompts |
| `ax-migration-functional-finance-owner` | Use when finance process owner validation, finance UAT, close process, ledger, tax, AR, AP, fixed asset, or finance fit-gap needs. | Workstream pack, validation checklist, risks, owners, test coverage, and evidence outputs. | No direct command; used by orchestration and prompts |
| `ax-migration-functional-scm-owner` | Use when SCM process owner validation, procurement, sales, inventory, warehouse, manufacturing, planning, or supply chain fit-gap needs. | Workstream pack, validation checklist, risks, owners, test coverage, and evidence outputs. | No direct command; used by orchestration and prompts |
| `ax-migration-integration-owner` | Use when integration owners, middleware teams, API teams, EDI owners, platform integration leads, or interface workstreams need AX to D365FO interface criticality, modernization, middleware, retry, error handling, reconciliation, or cutover sequencing. | Workstream pack, validation checklist, risks, owners, test coverage, and evidence outputs. | No direct command; used by orchestration and prompts |
| `ax-migration-qa-lead` | Use when QA leads, test managers, UAT coordinators, regression owners, defect managers, or quality workstreams need AX to D365FO test coverage, risk-based testing, UAT, regression suites, defect triage, or quality gate evidence. | Workstream pack, validation checklist, risks, owners, test coverage, and evidence outputs. | No direct command; used by orchestration and prompts |
| `ax-migration-reporting-bi-lead` | Use when reporting, BI, Power BI, SSRS, report rationalization, KPI ownership, analytics, or reporting migration needs. | Workstream pack, validation checklist, risks, owners, test coverage, and evidence outputs. | No direct command; used by orchestration and prompts |

## Delivery Team, Change, Support, Vendor, Legal

| Skill | When to use | Primary output | CLI relation |
| --- | --- | --- | --- |
| `ax-migration-change-adoption` | Use when change managers, training leads, process owners, HR enablement, business readiness teams, or adoption leads need AX to D365FO migration change impact, training, communication, readiness, UAT ownership, or hypercare adoption guidance. | Role-specific delivery guidance, questions, risks, owner actions, and governance artifacts. | No direct command; used by orchestration and prompts |
| `ax-migration-connector-wizard` | Use when setting up, checking, explaining, or troubleshooting AX SQL, Azure DevOps, LCS, D365FO OData/metadata, usage telemetry, GitHub export, or connector environment variables for the migration plugin. | Role-specific delivery guidance, questions, risks, owner actions, and governance artifacts. | No direct command; used by orchestration and prompts |
| `ax-migration-enterprise-architect` | Use when enterprise architects, portfolio architects, capability owners, platform architects, or architecture boards need AX to D365FO capability maps, application portfolio impact, technical debt burn-down, target landscape, or dependency risk guidance. | Role-specific delivery guidance, questions, risks, owner actions, and governance artifacts. | No direct command; used by orchestration and prompts |
| `ax-migration-github-exporter` | Use when exporting AX to D365FO migration backlog, risks, Azure DevOps work item CSV, or analyzer tasks into GitHub issue Markdown files for teams that do not use Azure DevOps. | Role-specific delivery guidance, questions, risks, owner actions, and governance artifacts. | `github-issues` |
| `ax-migration-industry-pack` | Use when tailoring AX to D365FO migration analysis for manufacturing, retail, wholesale, project operations, finance-heavy, warehouse/SCM, public sector, automotive, or other industry-specific migration patterns. | Role-specific delivery guidance, questions, risks, owner actions, and governance artifacts. | No direct command; used by orchestration and prompts |
| `ax-migration-legal-compliance` | Use when legal counsel, compliance leads, privacy officers, records managers, audit teams, or risk owners need AX to D365FO data processing, retention, regulatory obligations, contractual risk, audit evidence, or compliance decision support. | Role-specific delivery guidance, questions, risks, owner actions, and governance artifacts. | No direct command; used by orchestration and prompts |
| `ax-migration-persona-pack-generator` | Use when generating CEO, CIO, CISO, project manager, team, or all persona packs, readiness scores, PowerPoint decks, Excel workbooks, or role-specific migration deliverables from AX to D365FO analysis outputs. | Role-specific delivery guidance, questions, risks, owner actions, and governance artifacts. | `persona-pack` |
| `ax-migration-questionnaire-factory` | Use when creating role-based migration questionnaires, interview guides, migration factory mode, portfolio control, cutover war room packs, hypercare command center, or partner sales accelerator artifacts. | Role-specific delivery guidance, questions, risks, owner actions, and governance artifacts. | `questionnaire` |
| `ax-migration-regulatory-pack` | Use when AX to D365FO migration work needs regulatory, compliance, privacy, audit, DACH, GDPR/DSGVO, GoBD, EU e-invoicing, finance audit, pharma validation, automotive EDI, or public-sector control guidance. | Role-specific delivery guidance, questions, risks, owner actions, and governance artifacts. | No direct command; used by orchestration and prompts |
| `ax-migration-support-operations` | Use when support managers, ITSM owners, operations teams, service desk leads, monitoring teams, or BAU transition owners need AX to D365FO support model, runbooks, monitoring, alerting, hypercare-to-BAU, or incident categorization. | Role-specific delivery guidance, questions, risks, owner actions, and governance artifacts. | No direct command; used by orchestration and prompts |
| `ax-migration-team-executor` | Use when developers, functional consultants, data leads, integration specialists, report builders, testers, security analysts, or project team members need AX to D365FO migration tasks, acceptance criteria, technical actions, workshop outputs, or delivery execution guidance. | Role-specific delivery guidance, questions, risks, owner actions, and governance artifacts. | No direct command; used by orchestration and prompts |
| `ax-migration-vendor-manager` | Use when procurement leads, vendor managers, license managers, commercial owners, ISV owners, or sourcing teams need AX to D365FO ISV contract risk, license impact, vendor readiness, third-party replacement, or commercial decision guidance. | Role-specific delivery guidance, questions, risks, owner actions, and governance artifacts. | No direct command; used by orchestration and prompts |

## Solo and Master Orchestrator

| Skill | When to use | Primary output | CLI relation |
| --- | --- | --- | --- |
| `ax-migration-ai-migration-brain` | Use when migration brain, knowledge graph, project memory, role swarm, evidence graph, decision graph, or central migration intelligence needs. | Solo/Master-Orchestrator control artifacts, gates, evidence, status, sign-off, and runbooks. | `solo-brain` |
| `ax-migration-audit-binder` | Use when audit binder, evidence binder, decision traceability, gate evidence, security evidence, legal evidence, or audit readiness needs. | Solo/Master-Orchestrator control artifacts, gates, evidence, status, sign-off, and runbooks. | `solo-audit-binder` |
| `ax-migration-benefits-realization` | Use when benefits realization, ROI tracking, scope reduction value, TCO update, value tracking, or post-go-live benefit measurement needs. | Solo/Master-Orchestrator control artifacts, gates, evidence, status, sign-off, and runbooks. | `solo-benefits` |
| `ax-migration-communication-copilot` | Use when stakeholder communication, emails, steering updates, executive briefs, status notes, escalation messages, or meeting summaries. | Solo/Master-Orchestrator control artifacts, gates, evidence, status, sign-off, and runbooks. | `solo-communicate` |
| `ax-migration-daily-project-copilot` | Use when daily migration command sheet, next actions, daily standup, blockers, decisions, or project rhythm needs. | Solo/Master-Orchestrator control artifacts, gates, evidence, status, sign-off, and runbooks. | `solo-daily` |
| `ax-migration-decision-impact-simulator` | Use when simulating migration decisions, scope choices, cost, timeline, risk, cutover, support, or what-if migration scenarios. | Solo/Master-Orchestrator control artifacts, gates, evidence, status, sign-off, and runbooks. | `solo-simulate` |
| `ax-migration-evidence-collector` | Use when collecting, checking, or closing missing migration evidence across roles, workstreams, phases, gates, or approvals. | Solo/Master-Orchestrator control artifacts, gates, evidence, status, sign-off, and runbooks. | `solo-evidence` |
| `ax-migration-hypercare-copilot` | Use when hypercare command center, defect triage, stabilization, daily hypercare report, BAU handover, or support transition needs. | Solo/Master-Orchestrator control artifacts, gates, evidence, status, sign-off, and runbooks. | `solo-hypercare` |
| `ax-migration-knowledge-transfer-coach` | Use when knowledge transfer planning, support training, super user enablement, lessons learned, or handover coaching. | Solo/Master-Orchestrator control artifacts, gates, evidence, status, sign-off, and runbooks. | No direct command; used by orchestration and prompts |
| `ax-migration-knowledge-transfer-lead` | Use when knowledge transfer, training handover, lessons learned, BAU transition, support enablement, or project memory needs. | Solo/Master-Orchestrator control artifacts, gates, evidence, status, sign-off, and runbooks. | No direct command; used by orchestration and prompts |
| `ax-migration-master-orchestrator` | Use when broad AX to D365FO migration requests where the user wants one master agent to route roles, skills, CLI commands, artifacts, phases, risks, and next best actions. | Solo/Master-Orchestrator control artifacts, gates, evidence, status, sign-off, and runbooks. | `solo-orchestrate` |
| `ax-migration-prediction-advisor` | Use when predicting migration delay, budget drift, cutover risk, hypercare load, defect load, or project risk trends. | Solo/Master-Orchestrator control artifacts, gates, evidence, status, sign-off, and runbooks. | `solo-predict` |
| `ax-migration-project-drift-detector` | Use when detecting project drift, scope creep, missing decisions, timeline risk, budget drift, or gate slippage. | Solo/Master-Orchestrator control artifacts, gates, evidence, status, sign-off, and runbooks. | `solo-drift` |
| `ax-migration-risk-escalation-advisor` | Use when risk escalation, blocker classification, go-live blockers, security/legal/data/cutover escalation, or external approval routing. | Solo/Master-Orchestrator control artifacts, gates, evidence, status, sign-off, and runbooks. | No direct command; used by orchestration and prompts |
| `ax-migration-scope-defense-agent` | Use when defending scope reduction, explaining do-not-migrate decisions, preventing lift-and-shift, or arguing standardization value. | Solo/Master-Orchestrator control artifacts, gates, evidence, status, sign-off, and runbooks. | `solo-scope-defense` |
| `ax-migration-self-approval-gates` | Use when self-approval gates, external approval classification, solo sign-off, blocked decisions, or approval risk needs. | Solo/Master-Orchestrator control artifacts, gates, evidence, status, sign-off, and runbooks. | `solo-gates` |
| `ax-migration-solo-operator` | Use when solo AX to D365FO migration operation, end-to-end guided migration, autonomous project steering, or single-user migration command center needs. | Solo/Master-Orchestrator control artifacts, gates, evidence, status, sign-off, and runbooks. | `solo-*` |
| `ax-migration-stakeholder-translator` | Use when translating migration evidence for CEO, CFO, COO, CIO, CISO, PMO, key users, testers, support, legal, or delivery teams. | Solo/Master-Orchestrator control artifacts, gates, evidence, status, sign-off, and runbooks. | `solo-translate` |
| `ax-migration-technical-runbooks` | Use when technical runbooks for AX discovery, X++ export, modelstore, D365FO metadata, DMF, security, integration, reports, testing, or cutover. | Solo/Master-Orchestrator control artifacts, gates, evidence, status, sign-off, and runbooks. | No direct command; used by orchestration and prompts |
| `ax-migration-war-room-copilot` | Use when cutover war room, go-live command board, rollback points, go/no-go, cutover communication, or migration weekend needs. | Solo/Master-Orchestrator control artifacts, gates, evidence, status, sign-off, and runbooks. | `solo-war-room` |
| `ax-migration-waste-hunter` | Use when finding migration waste in reports, customizations, integrations, history, ISVs, tests, or unused scope. | Solo/Master-Orchestrator control artifacts, gates, evidence, status, sign-off, and runbooks. | `solo-waste-hunter` |

## Key User and Testing

| Skill | When to use | Primary output | CLI relation |
| --- | --- | --- | --- |
| `ax-migration-key-user-lead` | Use when key user, super user, power user, process expert, Fachbereich, process validation, training feedback, or business sign-off needs. | Test, UAT, regression, process validation, evidence, defect, and sign-off outputs. | No direct command; used by orchestration and prompts |
| `ax-migration-process-owner-validator` | Use when process owner validation, business owner sign-off, fit-gap validation, standard process approval, or process acceptance needs. | Test, UAT, regression, process validation, evidence, defect, and sign-off outputs. | `solo-signoff` |
| `ax-migration-regression-tester` | Use when regression testing, end-to-end testing, retesting, risk-based regression suite, or repeat validation needs. | Test, UAT, regression, process validation, evidence, defect, and sign-off outputs. | `solo-test-plan` |
| `ax-migration-test-execution-copilot` | Use when daily test execution, test queue, defect triage, retest planning, evidence completion, or test status needs. | Test, UAT, regression, process validation, evidence, defect, and sign-off outputs. | `solo-test-status` |
| `ax-migration-uat-tester` | Use when UAT tester, business tester, Fachtester, user acceptance testing, test execution, evidence, defects, or sign-off needs. | Test, UAT, regression, process validation, evidence, defect, and sign-off outputs. | `solo-test-plan`, `solo-test-status` |

## Commerce, CXP, CRM, POS

| Skill | When to use | Primary output | CLI relation |
| --- | --- | --- | --- |
| `ax-migration-call-center-lead` | Use when call center orders, customer service, scripts, order capture, payment handling, or call center migration needs. | Commerce readiness, cutover, store, CRM, POS, payment, offline, or omnichannel artifacts. | No direct command; used by orchestration and prompts |
| `ax-migration-channel-data-sync-lead` | Use when channel data sync, HQ sync, async jobs, Channel DB, offline recovery validation, or store data synchronization needs. | Commerce readiness, cutover, store, CRM, POS, payment, offline, or omnichannel artifacts. | `commerce-readiness` |
| `ax-migration-commerce-analytics-lead` | Use when commerce analytics, channel KPIs, conversion, store sales, returns, loyalty analytics, or customer insights migration needs. | Commerce readiness, cutover, store, CRM, POS, payment, offline, or omnichannel artifacts. | `commerce-*` |
| `ax-migration-commerce-lead` | Use when D365 Commerce HQ, channels, assortments, pricing, promotions, loyalty, online commerce, or retail channel migration needs. | Commerce readiness, cutover, store, CRM, POS, payment, offline, or omnichannel artifacts. | `commerce-*` |
| `ax-migration-commerce-orchestrator` | Use when coordinating Commerce, CRM, CXP, POS, CSU, payments, offline, store operations, and omnichannel migration workstreams. | Commerce readiness, cutover, store, CRM, POS, payment, offline, or omnichannel artifacts. | `commerce-*` |
| `ax-migration-commerce-scale-unit-owner` | Use when Commerce Scale Unit, CSU, Channel DB, Retail Server, Async Client, real-time service, sync, performance, or availability migration needs. | Commerce readiness, cutover, store, CRM, POS, payment, offline, or omnichannel artifacts. | `commerce-*` |
| `ax-migration-commerce-security-pci-lead` | Use when commerce security, PCI, payment tokens, POS roles, device security, payment secrets, or store security gate needs. | Commerce readiness, cutover, store, CRM, POS, payment, offline, or omnichannel artifacts. | `commerce-*` |
| `ax-migration-crm-owner` | Use when CRM, Customer Engagement, Dataverse, Dynamics 365 Sales, Customer Service, contact, opportunity, case, or dual-write migration needs. | Commerce readiness, cutover, store, CRM, POS, payment, offline, or omnichannel artifacts. | `commerce-crm-pack` |
| `ax-migration-customer-master-lead` | Use when customer master harmonization across Finance and Operations, Commerce, CRM, Dataverse, customers, contacts, and identity needs. | Commerce readiness, cutover, store, CRM, POS, payment, offline, or omnichannel artifacts. | No direct command; used by orchestration and prompts |
| `ax-migration-cxp-owner` | Use when CXP, CX, customer experience, customer journey, loyalty, omnichannel experience, or experience KPI migration needs for AX to D365FO and Dynamics 365 Commerce. | Commerce readiness, cutover, store, CRM, POS, payment, offline, or omnichannel artifacts. | `commerce-pack` |
| `ax-migration-lead-management-owner` | Use when lead management, lead capture, qualification, campaign handover, sales funnel, pipeline, or lead-to-cash migration needs. | Commerce readiness, cutover, store, CRM, POS, payment, offline, or omnichannel artifacts. | `commerce-crm-pack` |
| `ax-migration-loyalty-promotions-lead` | Use when loyalty cards, loyalty points, tiers, coupons, promotions, discounts, customer linkage, or loyalty migration needs. | Commerce readiness, cutover, store, CRM, POS, payment, offline, or omnichannel artifacts. | No direct command; used by orchestration and prompts |
| `ax-migration-marketplace-integration-lead` | Use when marketplace integrations, marketplace order intake, inventory, returns, settlement, or marketplace reconciliation needs. | Commerce readiness, cutover, store, CRM, POS, payment, offline, or omnichannel artifacts. | No direct command; used by orchestration and prompts |
| `ax-migration-omnichannel-ecommerce-lead` | Use when omnichannel, e-commerce, web store, BOPIS, pickup, return, ship-from-store, catalog, or inventory availability needs. | Commerce readiness, cutover, store, CRM, POS, payment, offline, or omnichannel artifacts. | `commerce-*`, `commerce-omnichannel-pack` |
| `ax-migration-payments-lead` | Use when payment connectors, terminals, refunds, settlement, tokenization, PCI, payment reconciliation, or payment cutover needs. | Commerce readiness, cutover, store, CRM, POS, payment, offline, or omnichannel artifacts. | `commerce-payments-pack` |
| `ax-migration-pos-lead` | Use when POS, point of sale, MPOS, CPOS, store checkout, cashier processes, returns, receipts, shifts, or store POS migration needs. | Commerce readiness, cutover, store, CRM, POS, payment, offline, or omnichannel artifacts. | `commerce-store-pack` |
| `ax-migration-pos-offline-lead` | Use when POS offline, offline DB, offline sync, offline payments, conflict handling, store offline continuity, or recovery planning needs. | Commerce readiness, cutover, store, CRM, POS, payment, offline, or omnichannel artifacts. | `commerce-offline-check` |
| `ax-migration-pricing-assortment-lead` | Use when channel pricing, assortments, catalogs, product variants, publishing, trade agreements, or promotion migration needs. | Commerce readiness, cutover, store, CRM, POS, payment, offline, or omnichannel artifacts. | No direct command; used by orchestration and prompts |
| `ax-migration-retail-hardware-lead` | Use when retail hardware, POS devices, scanners, receipt printers, cash drawers, payment terminals, store network, or device readiness needs. | Commerce readiness, cutover, store, CRM, POS, payment, offline, or omnichannel artifacts. | No direct command; used by orchestration and prompts |
| `ax-migration-store-operations-lead` | Use when store operations, end-of-day, shifts, pickup, returns, inventory lookup, store training, or store go-live readiness needs. | Commerce readiness, cutover, store, CRM, POS, payment, offline, or omnichannel artifacts. | `commerce-store-pack` |
| `ax-migration-store-training-lead` | Use when store training, cashier training, store manager readiness, super user training, support handover, or store go-live training needs. | Commerce readiness, cutover, store, CRM, POS, payment, offline, or omnichannel artifacts. | `commerce-store-pack` |

## Autonomous Governance and Evidence

| Skill | When to use | Primary output | CLI relation |
| --- | --- | --- | --- |
| `ax-migration-alm-release-train-controller` | Use when migration work needs ALM, release train, code freeze, deployments, environments, build gates, and release readiness. | Autonomous governance/evidence artifacts with Ready, Needs control, or Blocked signals. | `alm-release` |
| `ax-migration-autonomous-governance-orchestrator` | Use when migration work needs autonomous governance orchestration, evidence routing, gates, contracts, risks, meetings, and board control. | Autonomous governance/evidence artifacts with Ready, Needs control, or Blocked signals. | `governance-pack` |
| `ax-migration-board-risk-forecaster` | Use when migration work needs board risk forecast, go-live probability, budget risk, test risk, scope risk, and executive trends. | Autonomous governance/evidence artifacts with Ready, Needs control, or Blocked signals. | `board-risk` |
| `ax-migration-contract-scope-guardian` | Use when migration work needs contract, scope, SOW, change request, commercial guardrails, approval paths, and scope creep prevention. | Autonomous governance/evidence artifacts with Ready, Needs control, or Blocked signals. | `scope-guard`, `contract-risk` |
| `ax-migration-cutover-rehearsal-lead` | Use when migration work needs cutover rehearsals, dress rehearsals, critical path variance, runbook defects, and rollback readiness. | Autonomous governance/evidence artifacts with Ready, Needs control, or Blocked signals. | `cutover-rehearsal` |
| `ax-migration-evidence-vault-manager` | Use when migration work needs evidence vault, go-live evidence, audit binder, freshness, traceability, and missing proof control. | Autonomous governance/evidence artifacts with Ready, Needs control, or Blocked signals. | `evidence-vault` |
| `ax-migration-hyperautomation-architect` | Use when migration work needs Power Platform, Logic Apps, Fabric, Dataverse, APIs, automation candidates, and modernization backlog. | Autonomous governance/evidence artifacts with Ready, Needs control, or Blocked signals. | `hyperautomation-pack` |
| `ax-migration-isv-exit-strategist` | Use when migration work needs ISV exit, vendor replacement, contract termination, add-on retirement, and transition risk. | Autonomous governance/evidence artifacts with Ready, Needs control, or Blocked signals. | `isv-exit` |
| `ax-migration-legacy-archive-strategist` | Use when migration work needs legacy archive strategy, history retention, read-only access, audit retrieval, and reporting archive. | Autonomous governance/evidence artifacts with Ready, Needs control, or Blocked signals. | `archive-strategy` |
| `ax-migration-license-cost-optimizer` | Use when migration work needs D365FO, Commerce, CRM, role, user, subscription, license, cost, and budget optimization. | Autonomous governance/evidence artifacts with Ready, Needs control, or Blocked signals. | `license-cost` |
| `ax-migration-meeting-copilot` | Use when migration work needs meeting agenda, minutes, decisions, actions, RAID updates, owner tracking, and decision memory. | Autonomous governance/evidence artifacts with Ready, Needs control, or Blocked signals. | `meeting-copilot` |
| `ax-migration-process-twin-builder` | Use when migration work needs end-to-end process twin, lead-to-cash, order-to-cash, procure-to-pay, plan-to-produce, and risk traceability. | Autonomous governance/evidence artifacts with Ready, Needs control, or Blocked signals. | `process-twin` |
| `ax-migration-reconciliation-judge` | Use when migration work needs finance, inventory, customer, vendor, open transaction, and tolerance-based reconciliation sign-off. | Autonomous governance/evidence artifacts with Ready, Needs control, or Blocked signals. | `reconciliation-judge` |
| `ax-migration-regulatory-country-pack-generator` | Use when migration work needs country regulatory packs, localization, tax, e-invoicing, retention, audit, and privacy obligations. | Autonomous governance/evidence artifacts with Ready, Needs control, or Blocked signals. | `country-regulatory-pack` |
| `ax-migration-stakeholder-sentiment-radar` | Use when migration work needs stakeholder sentiment, resistance, decision bottlenecks, alignment risk, and change fatigue. | Autonomous governance/evidence artifacts with Ready, Needs control, or Blocked signals. | `meeting-copilot` |
| `ax-migration-training-effectiveness-monitor` | Use when migration work needs training effectiveness, adoption, key user readiness, learning gaps, and role readiness. | Autonomous governance/evidence artifacts with Ready, Needs control, or Blocked signals. | `training-readiness` |

## Coverage Check

- Skills documented here: `92`.
- This should match the validator target in `plugins/ax-to-d365fo-migration-expert/scripts/validate_plugin.py`.
- If a new skill is added, update this handbook, the role-based USP pack if relevant, and the docs index.
