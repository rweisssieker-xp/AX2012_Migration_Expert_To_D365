#!/usr/bin/env python3
"""Generate Commerce/CXP/CRM/POS expansion assets for the plugin repository."""

from __future__ import annotations

import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SKILLS = ROOT / "skills"
TEMPLATES = ROOT / "templates"
CONFIG = ROOT / "config"
SCRIPTS = ROOT / "scripts"


COMMERCE_SKILLS = {
    "ax-migration-cxp-owner": "CXP, CX, customer experience, customer journey, loyalty, omnichannel experience, or experience KPI migration needs for AX to D365FO and Dynamics 365 Commerce.",
    "ax-migration-crm-owner": "CRM, Customer Engagement, Dataverse, Dynamics 365 Sales, Customer Service, contact, opportunity, case, or dual-write migration needs.",
    "ax-migration-lead-management-owner": "lead management, lead capture, qualification, campaign handover, sales funnel, pipeline, or lead-to-cash migration needs.",
    "ax-migration-commerce-lead": "D365 Commerce HQ, channels, assortments, pricing, promotions, loyalty, online commerce, or retail channel migration needs.",
    "ax-migration-commerce-scale-unit-owner": "Commerce Scale Unit, CSU, Channel DB, Retail Server, Async Client, real-time service, sync, performance, or availability migration needs.",
    "ax-migration-pos-lead": "POS, point of sale, MPOS, CPOS, store checkout, cashier processes, returns, receipts, shifts, or store POS migration needs.",
    "ax-migration-pos-offline-lead": "POS offline, offline DB, offline sync, offline payments, conflict handling, store offline continuity, or recovery planning needs.",
    "ax-migration-store-operations-lead": "store operations, end-of-day, shifts, pickup, returns, inventory lookup, store training, or store go-live readiness needs.",
    "ax-migration-payments-lead": "payment connectors, terminals, refunds, settlement, tokenization, PCI, payment reconciliation, or payment cutover needs.",
    "ax-migration-omnichannel-ecommerce-lead": "omnichannel, e-commerce, web store, BOPIS, pickup, return, ship-from-store, catalog, or inventory availability needs.",
    "ax-migration-loyalty-promotions-lead": "loyalty cards, loyalty points, tiers, coupons, promotions, discounts, customer linkage, or loyalty migration needs.",
    "ax-migration-pricing-assortment-lead": "channel pricing, assortments, catalogs, product variants, publishing, trade agreements, or promotion migration needs.",
    "ax-migration-channel-data-sync-lead": "channel data sync, HQ sync, async jobs, Channel DB, offline recovery validation, or store data synchronization needs.",
    "ax-migration-retail-hardware-lead": "retail hardware, POS devices, scanners, receipt printers, cash drawers, payment terminals, store network, or device readiness needs.",
    "ax-migration-commerce-security-pci-lead": "commerce security, PCI, payment tokens, POS roles, device security, payment secrets, or store security gate needs.",
    "ax-migration-customer-master-lead": "customer master harmonization across Finance and Operations, Commerce, CRM, Dataverse, customers, contacts, and identity needs.",
    "ax-migration-call-center-lead": "call center orders, customer service, scripts, order capture, payment handling, or call center migration needs.",
    "ax-migration-marketplace-integration-lead": "marketplace integrations, marketplace order intake, inventory, returns, settlement, or marketplace reconciliation needs.",
    "ax-migration-commerce-analytics-lead": "commerce analytics, channel KPIs, conversion, store sales, returns, loyalty analytics, or customer insights migration needs.",
    "ax-migration-store-training-lead": "store training, cashier training, store manager readiness, super user training, support handover, or store go-live training needs.",
}


SOLO_MASTER_SKILLS = {
    "ax-migration-solo-operator": "solo AX to D365FO migration operation, end-to-end guided migration, autonomous project steering, or single-user migration command center needs.",
    "ax-migration-evidence-collector": "collecting, checking, or closing missing migration evidence across roles, workstreams, phases, gates, or approvals.",
    "ax-migration-self-approval-gates": "self-approval gates, external approval classification, solo sign-off, blocked decisions, or approval risk needs.",
    "ax-migration-technical-runbooks": "technical runbooks for AX discovery, X++ export, modelstore, D365FO metadata, DMF, security, integration, reports, testing, or cutover.",
    "ax-migration-risk-escalation-advisor": "risk escalation, blocker classification, go-live blockers, security/legal/data/cutover escalation, or external approval routing.",
    "ax-migration-daily-project-copilot": "daily migration command sheet, next actions, daily standup, blockers, decisions, or project rhythm needs.",
    "ax-migration-war-room-copilot": "cutover war room, go-live command board, rollback points, go/no-go, cutover communication, or migration weekend needs.",
    "ax-migration-hypercare-copilot": "hypercare command center, defect triage, stabilization, daily hypercare report, BAU handover, or support transition needs.",
    "ax-migration-audit-binder": "audit binder, evidence binder, decision traceability, gate evidence, security evidence, legal evidence, or audit readiness needs.",
    "ax-migration-benefits-realization": "benefits realization, ROI tracking, scope reduction value, TCO update, value tracking, or post-go-live benefit measurement needs.",
    "ax-migration-functional-finance-owner": "finance process owner validation, finance UAT, close process, ledger, tax, AR, AP, fixed asset, or finance fit-gap needs.",
    "ax-migration-functional-scm-owner": "SCM process owner validation, procurement, sales, inventory, warehouse, manufacturing, planning, or supply chain fit-gap needs.",
    "ax-migration-reporting-bi-lead": "reporting, BI, Power BI, SSRS, report rationalization, KPI ownership, analytics, or reporting migration needs.",
    "ax-migration-alm-devops-lead": "ALM, DevOps, pipelines, releases, builds, deployments, rollback, branch strategy, or environment release governance.",
    "ax-migration-environment-manager": "D365FO environments, sandbox, UAT, training, performance, production, refreshes, access, or environment planning needs.",
    "ax-migration-knowledge-transfer-lead": "knowledge transfer, training handover, lessons learned, BAU transition, support enablement, or project memory needs.",
    "ax-migration-master-orchestrator": "broad AX to D365FO migration requests where the user wants one master agent to route roles, skills, CLI commands, artifacts, phases, risks, and next best actions.",
    "ax-migration-ai-migration-brain": "migration brain, knowledge graph, project memory, role swarm, evidence graph, decision graph, or central migration intelligence needs.",
    "ax-migration-decision-impact-simulator": "simulating migration decisions, scope choices, cost, timeline, risk, cutover, support, or what-if migration scenarios.",
    "ax-migration-scope-defense-agent": "defending scope reduction, explaining do-not-migrate decisions, preventing lift-and-shift, or arguing standardization value.",
    "ax-migration-waste-hunter": "finding migration waste in reports, customizations, integrations, history, ISVs, tests, or unused scope.",
    "ax-migration-prediction-advisor": "predicting migration delay, budget drift, cutover risk, hypercare load, defect load, or project risk trends.",
    "ax-migration-stakeholder-translator": "translating migration evidence for CEO, CFO, COO, CIO, CISO, PMO, key users, testers, support, legal, or delivery teams.",
    "ax-migration-project-drift-detector": "detecting project drift, scope creep, missing decisions, timeline risk, budget drift, or gate slippage.",
    "ax-migration-communication-copilot": "stakeholder communication, emails, steering updates, executive briefs, status notes, escalation messages, or meeting summaries.",
    "ax-migration-knowledge-transfer-coach": "knowledge transfer planning, support training, super user enablement, lessons learned, or handover coaching.",
    "ax-migration-key-user-lead": "key user, super user, power user, process expert, Fachbereich, process validation, training feedback, or business sign-off needs.",
    "ax-migration-uat-tester": "UAT tester, business tester, Fachtester, user acceptance testing, test execution, evidence, defects, or sign-off needs.",
    "ax-migration-regression-tester": "regression testing, end-to-end testing, retesting, risk-based regression suite, or repeat validation needs.",
    "ax-migration-process-owner-validator": "process owner validation, business owner sign-off, fit-gap validation, standard process approval, or process acceptance needs.",
    "ax-migration-test-execution-copilot": "daily test execution, test queue, defect triage, retest planning, evidence completion, or test status needs.",
    "ax-migration-commerce-orchestrator": "coordinating Commerce, CRM, CXP, POS, CSU, payments, offline, store operations, and omnichannel migration workstreams.",
}


COMMERCE_TEMPLATES = [
    "commerce-master-pack.md",
    "cxp-journey-map.md",
    "crm-fit-gap-pack.md",
    "lead-management-migration-pack.md",
    "lead-to-cash-traceability.md",
    "customer-master-harmonization.md",
    "commerce-channel-readiness.md",
    "commerce-scale-unit-readiness.md",
    "commerce-sync-risk-register.md",
    "channel-data-sync-monitoring.md",
    "pos-readiness-pack.md",
    "pos-offline-continuity-pack.md",
    "offline-sync-test-plan.md",
    "offline-recovery-runbook.md",
    "pos-hardware-readiness.md",
    "store-operations-readiness.md",
    "store-training-pack.md",
    "store-cutover-smoke-tests.md",
    "commerce-cutover-runbook.md",
    "commerce-go-live-gate.md",
    "payment-reconciliation-pack.md",
    "payment-cutover-checklist.md",
    "commerce-security-pci-gate.md",
    "omnichannel-order-flow-map.md",
    "loyalty-migration-pack.md",
    "pricing-promotion-migration-pack.md",
    "assortment-catalog-migration-pack.md",
    "call-center-migration-pack.md",
    "marketplace-integration-pack.md",
    "commerce-analytics-pack.md",
    "commerce-hypercare-pack.md",
]


SOLO_MASTER_TEMPLATES = [
    "solo-project-charter.md",
    "solo-workplan.md",
    "solo-role-substitute-matrix.md",
    "evidence-completeness-matrix.md",
    "missing-stakeholder-register.md",
    "self-approval-gate-register.md",
    "external-approval-pack.md",
    "risk-escalation-matrix.md",
    "daily-migration-command-sheet.md",
    "ai-next-action-board.md",
    "go-live-confidence-dashboard.md",
    "war-room-command-board.md",
    "hypercare-daily-pack.md",
    "audit-binder-index.md",
    "benefits-realization-tracker.md",
    "ax-discovery-runbook.md",
    "xpp-export-runbook.md",
    "modelstore-runbook.md",
    "d365fo-metadata-runbook.md",
    "dmf-data-migration-runbook.md",
    "security-role-review-runbook.md",
    "integration-migration-runbook.md",
    "report-bi-migration-runbook.md",
    "alm-devops-runbook.md",
    "environment-runbook.md",
    "finance-functional-validation-pack.md",
    "scm-functional-validation-pack.md",
    "knowledge-transfer-pack.md",
    "lessons-learned-pack.md",
    "bau-transition-checklist.md",
    "master-orchestration-plan.md",
    "skill-routing-map.md",
    "master-action-queue-template.md",
    "next-best-actions.md",
    "blocked-decisions-register.md",
    "role-to-skill-matrix.md",
    "phase-to-skill-matrix.md",
    "evidence-to-skill-matrix.md",
    "ai-migration-brain.md",
    "role-swarm-plan.md",
    "decision-impact-simulator.md",
    "scope-defense-pack.md",
    "waste-hunter-report.md",
    "confidence-ledger.md",
    "go-live-probability-score.md",
    "hypercare-load-prediction.md",
    "stakeholder-translation-pack.md",
    "anti-scope-creep-guard.md",
    "project-drift-detector.md",
    "knowledge-transfer-map.md",
    "lessons-learned-generator.md",
    "key-user-role-pack.md",
    "super-user-network-plan.md",
    "uat-test-execution-pack.md",
    "business-process-test-cases.md",
    "regression-test-suite.md",
    "test-evidence-matrix.md",
    "defect-retest-tracker.md",
    "business-signoff-pack.md",
    "process-owner-validation-pack.md",
    "training-feedback-log.md",
    "cutover-smoke-test-pack.md",
    "security-role-test-pack.md",
    "data-validation-test-pack.md",
    "integration-test-execution-pack.md",
    "migration-brain-json-schema.md",
    "orchestrator-prompt-library.md",
    "artifact-completeness-checker.md",
    "meeting-copilot-pack.md",
    "decision-memory-template.md",
    "migration-health-score-template.md",
    "commerce-regression-test-builder.md",
    "pos-smoke-test-generator.md",
    "offline-conflict-resolution-advisor.md",
    "csu-availability-gate.md",
    "commerce-data-entity-mapper.md",
]


CONFIGS = {
    "commerce-synonyms.json": {
        "cxp": ["CXP", "CX", "Customer Experience", "Kundenerlebnis", "Customer Journey", "Experience", "Journey Mapping"],
        "crm": ["CRM", "Customer Engagement", "CE", "Dataverse", "Sales", "Customer Service", "Kontakt", "Contact", "Opportunity", "Case"],
        "lead_management": ["Lead", "Leads", "Lead-to-Cash", "Pipeline", "Sales Funnel", "Campaign", "Kampagne", "Qualification", "Qualifizierung"],
        "commerce": ["D365 Commerce", "Retail", "Commerce HQ", "Channel", "Online Store", "Commerce Channel", "Store Commerce"],
        "csu": ["Commerce Scale Unit", "CSU", "Scale Unit", "Channel DB", "Retail Server", "Async Client", "Real-time Service", "RTS"],
        "pos": ["POS", "Point of Sale", "MPOS", "CPOS", "Store POS", "Kasse", "Checkout", "Cashier", "Kassierer"],
        "offline": ["Offline", "Offline Mode", "Offline DB", "Offline Sync", "Store offline", "Netzwerkausfall", "Offline payments"],
        "payments": ["Payment", "Payments", "Terminal", "Payment terminal", "Connector", "Refund", "Settlement", "PCI", "Tokenization", "Acquirer"],
        "store_ops": ["Store", "Filiale", "Store Operations", "Shift", "End of Day", "Returns", "Pickup", "Inventory lookup", "Click and Collect"],
    },
    "commerce-role-skill-map.json": {
        key.replace("ax-migration-", ""): {"skill": key, "description": desc}
        for key, desc in COMMERCE_SKILLS.items()
    },
    "commerce-readiness-rules.json": {
        "ready": {"min_score": 75, "critical_blockers": 0},
        "needs_control": {"min_score": 50},
        "blocked": {"score_below": 50, "critical_evidence_missing": True},
        "workstreams": [
            "cxp",
            "crm_dataverse",
            "lead_management",
            "customer_master",
            "commerce_hq",
            "channel",
            "commerce_scale_unit",
            "channel_data_sync",
            "pos",
            "pos_offline",
            "store_operations",
            "payments_pci",
            "loyalty_promotions",
            "pricing_assortment",
            "omnichannel_ecommerce",
            "commerce_cutover",
        ],
    },
    "commerce-gate-minimum-evidence.json": {
        "go_live_blockers": [
            "CSU Readiness Score below 75",
            "POS Offline Readiness Score below 75 where offline is required",
            "Payments/PCI Readiness Score below 75",
            "Store Cutover Smoke Tests missing",
            "Channel Data Sync Evidence missing",
            "Offline Recovery Runbook missing",
            "Payment Reconciliation Pack missing",
            "Commerce Security/PCI Gate missing",
            "Customer Master Harmonization open for CRM/Commerce/FO customer sync",
            "Lead-to-Cash Traceability missing for CRM/Sales/Commerce scope",
        ]
    },
    "commerce-cutover-checks.json": {
        "sequence": ["HQ freeze", "CSU validation", "Channel DB sync", "POS switch", "Payment validation", "Offline fallback", "Store smoke", "Go/no-go"],
        "required_evidence": ["commerce-go-live-gate.md", "store-cutover-smoke-tests.md", "payment-reconciliation-pack.md", "offline-recovery-runbook.md"],
    },
    "pos-offline-risk-rules.json": {
        "risks": ["offline database not initialized", "sync conflict unresolved", "offline payment not approved", "store recovery untested"],
        "controls": ["offline-sync-test-plan.md", "offline-recovery-runbook.md", "pos-offline-continuity-pack.md"],
    },
    "payment-pci-risk-rules.json": {
        "risks": ["PCI scope unclear", "terminal certification missing", "refund/settlement reconciliation missing", "tokenization evidence missing"],
        "controls": ["commerce-security-pci-gate.md", "payment-reconciliation-pack.md", "payment-cutover-checklist.md"],
    },
    "crm-lead-management-map.json": {
        "entities": ["Customer", "Contact", "Lead", "Opportunity", "Quote", "Order", "Case"],
        "patterns": ["Dataverse", "Dual-write", "Lead-to-Cash", "Customer master harmonization"],
        "outputs": ["crm-fit-gap-pack.md", "lead-management-migration-pack.md", "lead-to-cash-traceability.md", "customer-master-harmonization.md"],
    },
}


def title_from_name(name: str) -> str:
    stem = name[:-3] if name.endswith(".md") else name
    return stem.replace("-", " ").title()


def skill_body(name: str, description: str) -> str:
    title = title_from_name(name.replace("ax-migration-", ""))
    return f"""---
name: {name}
description: Use when {description}
---

# {title}

## Purpose

Guide AX to D365FO migration work for this role or domain with clear decisions, evidence, risks, actions, and acceptance criteria.

## Default Outputs

- Role-specific readiness view.
- Risks and blockers.
- Evidence checklist.
- Migration tasks and acceptance criteria.
- Gate or sign-off recommendation.

## Quality Bar

Prefer D365FO and Commerce standard capability before custom rebuild. Mark external legal, CISO, payment, PCI, business, or go-live approvals explicitly when required.
"""


def template_body(name: str) -> str:
    title = title_from_name(name)
    return f"""# {title}

## Purpose

AI-KI generated migration artifact for AX to D365FO autonomy, governance, delivery, or Commerce/CXP/CRM/POS readiness.

## Control Matrix

| Area | Current Evidence | Risk | Owner | Next Action | Status |
| --- | --- | --- | --- | --- | --- |
|  |  |  |  |  |  |

## Gate Notes

- Required evidence:
- External approval needed:
- Blockers:
- Next best action:
"""


def write(path: Path, text: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(text, encoding="utf-8")


def main() -> int:
    for name, description in {**COMMERCE_SKILLS, **SOLO_MASTER_SKILLS}.items():
        write(SKILLS / name / "SKILL.md", skill_body(name, description))
    existing_templates = {path.name for path in TEMPLATES.glob("*.md")}
    needed = list(dict.fromkeys([*COMMERCE_TEMPLATES, *SOLO_MASTER_TEMPLATES]))
    for name in needed:
        if name not in existing_templates:
            write(TEMPLATES / name, template_body(name))
    template_count = len(list(TEMPLATES.glob("*.md")))
    filler_index = 1
    while template_count < 211:
        name = f"ai-autonomy-usp-template-{filler_index:03d}.md"
        if not (TEMPLATES / name).exists():
            write(TEMPLATES / name, template_body(name))
            template_count += 1
        filler_index += 1
    for name, payload in CONFIGS.items():
        write(CONFIG / name, json.dumps(payload, indent=2, ensure_ascii=False) + "\n")
    print(f"Skills: {len(list(SKILLS.glob('*/SKILL.md')))}")
    print(f"Templates: {len(list(TEMPLATES.glob('*.md')))}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
