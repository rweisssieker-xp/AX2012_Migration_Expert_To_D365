# AX to D365FO Migration Expert - Operating Handbook

Dieses Handbuch beschreibt den kompletten Projektablauf, die Rollen, die internen/externen Verantwortlichkeiten, die Skills und die wichtigsten Faehigkeiten des Plugins.

## 1. Operating Model

Das Plugin arbeitet als lokales Migration Operating System fuer AX 4.0, AX 2009, AX 2012 und D365 Finance & Operations inklusive Commerce, CRM, POS, Governance, Evidence und Migration Intelligence.

| Ebene | Zweck | Ergebnis |
| --- | --- | --- |
| Master Orchestrator | Eingaben analysieren, passende Skills waehlen, Evidence-Luecken erkennen, naechste Commands vorschlagen. | `orchestration-plan.md`, `skill-routing.json`, `next-commands.ps1` |
| Guided Run | Analyse, Routing, Gates, Evidence, Security, Memory, Export und Health Snapshot in einem Lauf verbinden. | `guided-run-plan.md`, `role-action-inbox.md`, `recommended-commands.md`, `project-health-snapshot.html` |
| Analyzer | AX Inventory, X++, XPO, CSV, JSON und Projektdaten auswerten. | Dashboard, Risks, Backlog, Roadmap, Effort, Role Views |
| Packs | Rollen-, Commerce-, Governance-, Solo- und Intelligence-Artefakte erzeugen. | Markdown, JSON, CSV, XLSX, PPTX |
| Evidence Gates | Kritische Nachweise und externe Freigaben pruefbar machen. | Ready / Needs control / Blocked |
| Memory & Intelligence | Wissen, Benchmarks, Szenarien, Portfolio, Qualitaet und Value Tracking aufbauen. | SQLite, JSONL, Scorecards, Playbooks |
| Demo & UI | Lokale Demo-Projekte, Dashboard und Command UI bereitstellen. | `demo-index.html`, `project-wizard.html` |

## 2. End-to-End Ablauf

### Phase 1: Projektstart

| Schritt | Command | Ergebnis |
| --- | --- | --- |
| Profil waehlen | `python .\axmigrate.py wizard --profile ax2012 --project "Contoso"` | Projektplan und passende Commands |
| Demo erzeugen | `python .\axmigrate.py demo-projects --output demo-projects` | Demo Dashboards und Beispielpacks |
| UI erzeugen | `python .\axmigrate.py project-ui --output migration-ui` | Lokale HTML Command UI |

### Phase 2: Analyse

| Schritt | Command | Ergebnis |
| --- | --- | --- |
| Inventory analysieren | `python .\axmigrate.py analyze <input> --output migration-analysis\sample` | 46 Analyseartefakte |
| Dashboard erzeugen | `python .\axmigrate.py dashboard <input> --output migration-dashboard\sample` | Dashboard 2.0 |
| Datenqualitaet pruefen | `python .\axmigrate.py profile-data <csv>` | Data Quality Report |

### Phase 3: Orchestrierung

| Schritt | Command | Ergebnis |
| --- | --- | --- |
| Gefuehrter Lauf | `python .\axmigrate.py guided-run <input> --project "Contoso" --output guided-runs\contoso` | Analyse, Skills, Gates, Evidence, Security, Memory, Exporte und Health Snapshot |
| Skill Routing | `python .\axmigrate.py orchestrate migration-analysis\sample --output orchestration\sample` | Skills, Evidence Gaps, Next Commands |
| Solo Betrieb | `python .\axmigrate.py solo-run --project "Contoso" --input <input>` | Solo Operating Folder |
| Tagessteuerung | `python .\axmigrate.py solo-daily <source>` | Daily Command Sheet |

### Phase 4: Fachliche und technische Packs

| Bereich | Commands |
| --- | --- |
| Persona/Rollen/USPs | `persona-pack`, `stakeholder-pack`, `questionnaire`, `usp-pack` |
| Commerce/CRM/POS | `commerce-pack`, `commerce-readiness`, `commerce-cutover`, `commerce-offline-check`, `commerce-crm-pack`, `commerce-store-pack`, `commerce-payments-pack`, `commerce-omnichannel-pack` |
| Governance | `governance-pack`, `evidence-vault`, `scope-guard`, `contract-risk`, `cutover-rehearsal`, `reconciliation-judge`, `board-risk` |
| Intelligence | `intelligence-pack`, `migration-memory`, `benchmark`, `portfolio-control`, `scenario-lab`, `quality-audit`, `war-game`, `value-realization` |
| Advanced AI Control | `usp-actions`, `truth-detector`, `cutover-confidence`, `meeting-actions`, `proposal-pack`, `role-prompt-pack`, `evidence-freshness`, `dependency-risk-graph`, `partner-deliverable-check`, `release-pack`, `demo-portal`, `wizard-ui` |

### Phase 5: Evidence, Security, Freigaben

| Schritt | Command | Ergebnis |
| --- | --- | --- |
| Evidence Gate | `python .\axmigrate.py evidence-gates <source> --output evidence-gates\sample` | Go-live Status |
| Evidence Vault | `python .\axmigrate.py evidence-vault <source> --output evidence-vault\sample` | Evidence Index, Manifest, Hashes |
| Security Scan | `python .\axmigrate.py security-scan <source> --output security-scan\sample` | Secrets/PII/Connection String Report |
| Memory Store | `python .\axmigrate.py memory-store <source> --project "Contoso"` | SQLite und JSONL Memory |
| Health Snapshot | `python .\axmigrate.py health-snapshot guided-runs\contoso --output health\contoso` | Kompakter Ready/Needs control/Blocked Projektstatus |

### Phase 6: Export, Reporting, Go-live

| Schritt | Command | Ergebnis |
| --- | --- | --- |
| Office Export | `python .\axmigrate.py export migration-analysis\sample --output migration-exports\sample` | Excel/PPTX Decks und Workbooks |
| Cutover | `cutover-rehearsal`, `commerce-cutover`, `solo-war-room` | Runbooks, Smoke Tests, Rehearsal |
| Hypercare | `solo-hypercare`, `continuous-improvement`, `post-go-live-optimizer` | Hypercare und Optimierungsbacklog |

## 3. Rollenmodell

### Interne Rollen

| Rolle | Aufgabe | Hauptskills |
| --- | --- | --- |
| Solo Operator | Projekt allein steuern und naechste Aktionen ausfuehren. | `ax-migration-solo-operator`, `ax-migration-master-orchestrator` |
| Projektleiter / PMO | Planung, Status, RAID, Abhaengigkeiten, Eskalationen. | `ax-migration-project-manager`, `ax-migration-pmo-negotiator` |
| Fachbereich Finance | Fit-Gap, Tests, Reconciliation, Closing Readiness. | `ax-migration-functional-finance-owner`, `ax-migration-cfo-finance-leadership` |
| Fachbereich SCM | Supply Chain, Warehouse, Manufacturing, Prozesse. | `ax-migration-functional-scm-owner`, `ax-migration-coo-operations` |
| Data Lead | Datenqualitaet, Mapping, Ownership, Evidence. | `ax-migration-data-governance` |
| Integration Lead | Interfaces, APIs, AIF, Retry, Monitoring. | `ax-migration-integration-owner`, `ax-migration-integration-resilience-engineer` |
| QA / Test Lead | UAT, Regression, Defects, Test Evidence. | `ax-migration-qa-lead`, `ax-migration-test-execution-copilot` |
| Key User | Fachliche Tests, Prozessvalidierung, Abnahmevorbereitung. | `ax-migration-key-user-lead`, `ax-migration-uat-tester` |
| Commerce Lead | Commerce HQ, Channels, Stores, POS, Payments. | `ax-migration-commerce-orchestrator`, `ax-migration-commerce-lead` |
| CRM Lead | CRM, Dataverse, Lead-to-Cash, Customer Master. | `ax-migration-crm-owner`, `ax-migration-lead-management-owner` |

### Externe Rollen und Freigaben

| Rolle | Externe Entscheidung | Plugin liefert |
| --- | --- | --- |
| CEO / Board | Business Case, Scope, Go-live Risiko. | Executive Deck, Board Risk Forecast |
| CFO | Budget, Finance Sign-off, Reconciliation Acceptance. | Finance Pack, Reconciliation Judge |
| CIO | Target Architecture, Platform, Integration Strategy. | Architecture Deck, CIO Views |
| CISO | Security, SoD, Secrets, PCI, Go-live Security Gate. | CISO Gate Deck, Security Scan, Attack Surface |
| Legal / Compliance | Datenschutz, Retention, Regulatorik, Vertragsrisiken. | Legal Pack, Regulatory Pack, Evidence Vault |
| Auditor | Audit Trail, Evidence, Nachvollziehbarkeit. | Audit Binder, Evidence Manifest, Hashes |
| ISV / Vendor | Add-on Roadmap, Replacement, Contract Changes. | ISV Exit Pack, Vendor Readiness |
| Microsoft / Platform | LCS, Environments, Production Deployment Windows. | Environment Readiness, ALM Release Train |

### Hybrid Rollen

| Rolle | Intern automatisierbar | Externe Grenze |
| --- | --- | --- |
| Governance Owner | Evidence sammeln, Gates bewerten, Reports erzeugen. | Echte Freigaben bleiben extern. |
| Cutover Lead | Runbook, Rehearsal, Smoke Tests, War Room. | Go-live Entscheidung bleibt extern. |
| Payments Lead | Payment Evidence, Settlement, Refund, Reconciliation. | Provider/PCI Freigabe bleibt extern. |
| Security Lead | Attack Surface, Scan, Gate Material. | CISO Risk Acceptance bleibt extern. |

## 4. Skill Cluster mit Kurzbeschreibung

### Core

| Skill | Kurzbeschreibung |
| --- | --- |
| `ax-to-d365fo-migration` | Kernskill fuer AX 4.0/2009/2012 zu D365FO Analyse, Planung und Umsetzung. |

### Master, Solo, Autonomie

| Skill | Kurzbeschreibung |
| --- | --- |
| `ax-migration-master-orchestrator` | Steuert Skills, Evidence, Aufgaben und naechste Commands. |
| `ax-migration-solo-operator` | Ermoeglicht einer Einzelperson den Betrieb des Projekts. |
| `ax-migration-ai-migration-brain` | Haelt zentrale Projektintelligenz, Kontext und Entscheidungen. |
| `ax-migration-daily-project-copilot` | Erzeugt Tagesplan, Prioritaeten und Kommandozettel. |
| `ax-migration-project-drift-detector` | Erkennt Drift bei Scope, Zeit, Qualitaet und Evidence. |
| `ax-migration-prediction-advisor` | Prognostiziert Blocker, Verzug und Projektrisiken. |
| `ax-migration-decision-impact-simulator` | Simuliert Folgen von Scope-, Zeit-, Budget- und Qualitaetsentscheidungen. |
| `ax-migration-scope-defense-agent` | Verteidigt Scope gegen unkontrollierte Erweiterung. |
| `ax-migration-waste-hunter` | Findet unnoetigen Aufwand, Doppelarbeit und Low-Value Scope. |
| `ax-migration-war-room-copilot` | Unterstuetzt Cutover War Room und Krisensteuerung. |
| `ax-migration-hypercare-copilot` | Steuert Hypercare, Support und Stabilisierung. |
| `ax-migration-benefits-realization` | Verfolgt Nutzen, ROI und Value Delivery. |
| `ax-migration-stakeholder-translator` | Uebersetzt Projektsignale fuer Zielgruppen. |
| `ax-migration-communication-copilot` | Erstellt Kommunikation, Updates und Stakeholder-Nachrichten. |

### Executive, PMO, Delivery

| Skill | Kurzbeschreibung |
| --- | --- |
| `ax-migration-ceo-advisor` | Erstellt CEO-Sicht auf Wert, Risiko und Entscheidungen. |
| `ax-migration-cfo-finance-leadership` | Erstellt CFO-Sicht auf Budget, ROI, Reconciliation und Audit. |
| `ax-migration-cio-architect` | Erstellt CIO-Sicht auf Architektur, Plattform und Modernisierung. |
| `ax-migration-ciso-guardian` | Erstellt Security-, Privacy-, SoD- und CISO-Gate-Sicht. |
| `ax-migration-coo-operations` | Bewertet operative Kontinuitaet und Prozessrisiken. |
| `ax-migration-steering-committee` | Bereitet Steering Entscheidungen und Eskalationen vor. |
| `ax-migration-board-risk-forecaster` | Prognostiziert Board-Risiken und Go-live Confidence. |
| `ax-migration-project-manager` | Erstellt Projektplan, RAID, Status, Milestones und Governance. |
| `ax-migration-pmo-negotiator` | Modelliert Trade-offs zwischen Scope, Budget, Qualitaet und Zeit. |
| `ax-migration-risk-escalation-advisor` | Identifiziert Risiken fuer Eskalation und Steering. |
| `ax-migration-meeting-copilot` | Wandelt Meetings in Entscheidungen, Aktionen und Backlog um. |
| `ax-migration-team-executor` | Wandelt Analyse in konkrete Teamaufgaben um. |

### Functional, Data, Integration, Reporting

| Skill | Kurzbeschreibung |
| --- | --- |
| `ax-migration-functional-finance-owner` | Bewertet Finance Fit-Gap, Tests und Fachabnahme. |
| `ax-migration-functional-scm-owner` | Bewertet SCM, Warehouse, Manufacturing und Supply Chain. |
| `ax-migration-process-owner-validator` | Validiert Prozessverantwortung und Sign-off Bedarf. |
| `ax-migration-process-twin-builder` | Erstellt Prozess-Twins mit Risiken, Tests und Evidence. |
| `ax-migration-data-governance` | Steuert Datenqualitaet, Ownership, Mapping und Evidence. |
| `ax-migration-integration-owner` | Bewertet Schnittstellen, APIs, AIF und Cutover-Abhaengigkeiten. |
| `ax-migration-reporting-bi-lead` | Plant Reporting, BI, Power BI und Analytics Migration. |
| `ax-migration-enterprise-architect` | Bewertet Zielarchitektur, Portfolio und technische Schulden. |
| `ax-migration-environment-manager` | Plant Sandbox, UAT, Training, Production und Refreshes. |
| `ax-migration-technical-runbooks` | Erstellt technische Runbooks fuer Betrieb und Cutover. |
| `ax-migration-hyperautomation-architect` | Identifiziert Automatisierung und Power Platform Chancen. |

### Testing, Training, Knowledge Transfer

| Skill | Kurzbeschreibung |
| --- | --- |
| `ax-migration-qa-lead` | Plant Teststrategie, UAT, Regression und Defect Control. |
| `ax-migration-key-user-lead` | Steuert Key User Readiness und fachliche Validierung. |
| `ax-migration-uat-tester` | Unterstuetzt UAT Execution und Test Evidence. |
| `ax-migration-regression-tester` | Baut Regressionstestabdeckung und Status. |
| `ax-migration-test-execution-copilot` | Erzeugt Testpacks, Status und Defect Follow-up. |
| `ax-migration-training-effectiveness-monitor` | Misst Training, Adoption und Rollenabdeckung. |
| `ax-migration-knowledge-transfer-lead` | Plant Know-how Uebergabe und Supportfaehigkeit. |
| `ax-migration-knowledge-transfer-coach` | Coacht Teams bei Wissensluecken. |
| `ax-migration-knowledge-transfer-examiner` | Prueft, ob Teams nach Go-live arbeitsfaehig sind. |

### Commerce, CRM, POS

| Skill | Kurzbeschreibung |
| --- | --- |
| `ax-migration-commerce-orchestrator` | Steuert Commerce, CRM, POS, Stores und Payments. |
| `ax-migration-commerce-lead` | Verantwortet Commerce HQ, Channels, Pricing und Loyalty. |
| `ax-migration-commerce-scale-unit-owner` | Bewertet CSU, Channel DB, Retail Server und Availability. |
| `ax-migration-channel-data-sync-lead` | Prueft Channel Sync, Async Jobs und Recovery. |
| `ax-migration-pos-lead` | Bewertet POS, Checkout, Returns, Receipts und Shifts. |
| `ax-migration-pos-offline-lead` | Bewertet POS Offline, Sync, Konflikte und Recovery. |
| `ax-migration-store-operations-lead` | Bewertet Store Prozesse, End-of-Day, Pickup und Returns. |
| `ax-migration-store-training-lead` | Plant Store Training fuer Cashier, Manager und Support. |
| `ax-migration-retail-hardware-lead` | Prueft Scanner, Printer, Drawer, Terminals und Store Network. |
| `ax-migration-payments-lead` | Bewertet Payment, Refunds, Settlement und Reconciliation. |
| `ax-migration-commerce-security-pci-lead` | Bewertet PCI, Payment Security, Tokens und Rollen. |
| `ax-migration-commerce-analytics-lead` | Erstellt Commerce KPIs, Channel Reporting und Analytics. |
| `ax-migration-cxp-owner` | Bewertet Customer Journey, Experience und Omnichannel. |
| `ax-migration-crm-owner` | Bewertet CRM, Dataverse, Dual-write und Customer Engagement. |
| `ax-migration-lead-management-owner` | Bewertet Lead Capture, Qualification und Lead-to-Cash. |
| `ax-migration-customer-master-lead` | Harmonisiert Customer Master ueber FO, Commerce und CRM. |
| `ax-migration-call-center-lead` | Bewertet Call Center Order Capture und Service Prozesse. |
| `ax-migration-omnichannel-ecommerce-lead` | Bewertet Web Commerce, BOPIS und Ship-from-store. |
| `ax-migration-marketplace-integration-lead` | Bewertet Marketplace Orders, Returns und Settlement. |
| `ax-migration-loyalty-promotions-lead` | Bewertet Loyalty, Punkte, Coupons und Promotions. |
| `ax-migration-pricing-assortment-lead` | Bewertet Pricing, Assortment, Catalogs und Variants. |

### Governance, Evidence, Compliance

| Skill | Kurzbeschreibung |
| --- | --- |
| `ax-migration-autonomous-governance-orchestrator` | Steuert Governance, Evidence, Contract, Cutover und Reconciliation. |
| `ax-migration-evidence-collector` | Sammelt Evidence, Luecken, Owner und Nachweise. |
| `ax-migration-evidence-vault-manager` | Verwaltet Evidence Vault, Manifest, Hashes und Audit Trail. |
| `ax-migration-self-approval-gates` | Erstellt Selbstpruefungen mit externer Freigabegrenze. |
| `ax-migration-contract-scope-guardian` | Kontrolliert Scope, Change Requests und Contract Impact. |
| `ax-migration-cutover-rehearsal-lead` | Erstellt Cutover Rehearsal, Scorecards und Defect Logs. |
| `ax-migration-reconciliation-judge` | Bewertet Finance, Inventory, Customer, Vendor und Open Transactions. |
| `ax-migration-license-cost-optimizer` | Optimiert Rollen, Lizenzen, Subscriptions und Kosten. |
| `ax-migration-alm-devops-lead` | Plant DevOps, Branching, Build, Release und Deployment. |
| `ax-migration-alm-release-train-controller` | Kontrolliert Release Train, Freeze, Gates und Rollback. |
| `ax-migration-isv-exit-strategist` | Plant ISV Replacement, Exit und Vendor Transition. |
| `ax-migration-vendor-manager` | Kontrolliert Vendor Readiness, Contracts und Dependencies. |
| `ax-migration-legal-compliance` | Bewertet Datenschutz, Retention, Recht und Compliance. |
| `ax-migration-regulatory-pack` | Erstellt Regulatory, GDPR, GoBD und Audit Packs. |
| `ax-migration-regulatory-country-pack-generator` | Erstellt Country, Tax, Localization und E-Invoicing Packs. |
| `ax-migration-legacy-archive-strategist` | Plant Legacy Archive, Retention und Read-only Zugriff. |
| `ax-migration-support-operations` | Plant Supportmodell, Monitoring, ITSM und BAU Uebergang. |
| `ax-migration-partner-sales` | Erstellt Discovery, Proposal, Assessment und Sales Packs. |
| `ax-migration-connector-wizard` | Hilft bei AX SQL, ADO, LCS, D365FO und GitHub Connectors. |
| `ax-migration-github-exporter` | Exportiert Work Items und Risiken als GitHub Issues. |

### Migration Intelligence Fabric

| Skill | Kurzbeschreibung |
| --- | --- |
| `ax-migration-intelligence-fabric-orchestrator` | Steuert Memory, Benchmarks, Portfolio, Szenarien und Value. |
| `ax-migration-migration-memory` | Speichert Lessons, Decisions, Patterns und Projektwissen. |
| `ax-migration-benchmarking-analyst` | Vergleicht Scope, Risk, Effort, Test und Outcome mit Baselines. |
| `ax-migration-peer-comparison-analyst` | Vergleicht Projekte, Wellen, Laender, Stores und Entities. |
| `ax-migration-portfolio-control-tower` | Steuert Multi-Wave, Multi-Country und Legal Entity Rollouts. |
| `ax-migration-rollout-wave-optimizer` | Optimiert Rollout-Sequenz nach Readiness, Risk und Value. |
| `ax-migration-scenario-lab` | Simuliert Strategien, Scope, Kosten, Risiken und Timeline. |
| `ax-migration-delivery-quality-auditor` | Auditiert Artefakte, Backlog, Tests, Gates und Evidence. |
| `ax-migration-quality-maturity-scorer` | Scored Delivery Maturity und Quality Readiness. |
| `ax-migration-technical-debt-liquidator` | Priorisiert technische Schulden und Modernisierungssprints. |
| `ax-migration-fabric-data-product-advisor` | Bewertet Fabric, Lakehouse, Power BI und Data Products. |
| `ax-migration-integration-resilience-engineer` | Bewertet Retry, Replay, Idempotency, Monitoring und Support. |
| `ax-migration-security-attack-surface-mapper` | Kartiert Rollen, APIs, Secrets, POS und Integration Exposure. |
| `ax-migration-sustainability-advisor` | Bewertet Archive, Datenvolumen, Cloud Footprint und ESG. |
| `ax-migration-war-game-master` | Simuliert Failures und erstellt Recovery- und Resilience Plans. |
| `ax-migration-value-realization-engine` | Verfolgt KPIs, Nutzen, Adoption und Value Leakage nach Go-live. |
| `ax-migration-continuous-improvement-lead` | Erstellt Verbesserungs- und Modernisierungsbacklogs. |
| `ax-migration-post-go-live-optimizer` | Identifiziert Optimierungen nach Stabilisierung. |

## 5. Externe Freigabegrenze

Das Plugin bereitet Entscheidungen, Evidence und Empfehlungen vor, ersetzt aber keine echten Freigaben.

| Externe Freigabe | Plugin Vorbereitung |
| --- | --- |
| Go-live | Go-live Gate, Confidence, Board Risk, Cutover Evidence |
| CISO | Security Scan, Attack Surface, SoD, PCI Evidence |
| CFO / Finance | Reconciliation Judge, Finance Pack, Variance Reports |
| Legal / Audit | Evidence Vault, Audit Binder, Regulatory Pack |
| Payment Provider / PCI | Payment Pack, PCI Gate, Settlement Evidence |
| Vendor / ISV | ISV Exit Pack, Vendor Readiness, Contract Risk |
| Microsoft / Platform | Environment Readiness, ALM Release, Connector Checks |

## 6. Betriebs-Checkliste

| Check | Command |
| --- | --- |
| Vollvalidierung | `python .\axmigrate.py validate` |
| Umgebung pruefen | `python .\axmigrate.py doctor` |
| Demo Portal | `python .\axmigrate.py demo-projects --output demo-projects` |
| Project UI | `python .\axmigrate.py project-ui --output migration-ui` |
| Security Scan | `python .\axmigrate.py security-scan <source> --output security-scan\sample` |
| Evidence Vault | `python .\axmigrate.py evidence-vault <source> --output evidence-vault\sample` |
| Memory Store | `python .\axmigrate.py memory-store <source> --project "Contoso"` |
