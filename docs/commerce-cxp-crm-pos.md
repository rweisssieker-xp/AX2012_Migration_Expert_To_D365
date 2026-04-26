# Commerce/CXP/CRM/POS Domain

The Customer & Commerce Experience domain extends the AX to D365FO migration plugin beyond core Finance & Operations. It covers customer journey, CRM/Dataverse, lead management, D365 Commerce, Commerce Scale Unit, POS, offline store operations, payments, loyalty, pricing, assortment, omnichannel, marketplace, call center, analytics, and store training.

## Skills

| Area | Skill |
| --- | --- |
| CXP and customer journey | `ax-migration-cxp-owner` |
| CRM, Dataverse, Customer Engagement | `ax-migration-crm-owner` |
| Lead management and lead-to-cash | `ax-migration-lead-management-owner` |
| Commerce HQ, channels, assortment, pricing | `ax-migration-commerce-lead` |
| CSU, Channel DB, Retail Server, Async Client | `ax-migration-commerce-scale-unit-owner` |
| POS, MPOS/CPOS, checkout, returns, shifts | `ax-migration-pos-lead` |
| POS offline, offline DB, sync, recovery | `ax-migration-pos-offline-lead` |
| Store operations and training | `ax-migration-store-operations-lead` |
| Payments, refunds, settlement, PCI | `ax-migration-payments-lead` and `ax-migration-commerce-security-pci-lead` |
| Omnichannel, e-commerce, BOPIS | `ax-migration-omnichannel-ecommerce-lead` |
| Loyalty and promotions | `ax-migration-loyalty-promotions-lead` |
| Pricing, assortment, catalogs | `ax-migration-pricing-assortment-lead` |
| Channel sync and async jobs | `ax-migration-channel-data-sync-lead` |
| Retail hardware | `ax-migration-retail-hardware-lead` |
| Customer master | `ax-migration-customer-master-lead` |
| Call center | `ax-migration-call-center-lead` |
| Marketplace | `ax-migration-marketplace-integration-lead` |
| Commerce analytics | `ax-migration-commerce-analytics-lead` |
| Store training | `ax-migration-store-training-lead` |
| Commerce orchestration | `ax-migration-commerce-orchestrator` |

## Generated Packs

| Command | Main outputs |
| --- | --- |
| `commerce-pack` | `commerce-master-pack.md` plus all Commerce domain artifacts. |
| `commerce-readiness` | `commerce-readiness.md`, `commerce-readiness.json`, `commerce-readiness.csv`. |
| `commerce-cutover` | `commerce-cutover-runbook.md`, `store-cutover-smoke-tests.md`, `commerce-go-live-gate.md`. |
| `commerce-offline-check` | `pos-offline-continuity-pack.md`, `offline-recovery-runbook.md`, `offline-sync-test-plan.md`. |
| `commerce-crm-pack` | `crm-fit-gap-pack.md`, `lead-management-migration-pack.md`, `lead-to-cash-traceability.md`, `customer-master-harmonization.md`. |
| `commerce-store-pack` | `store-operations-readiness.md`, `pos-hardware-readiness.md`, `store-training-pack.md`. |
| `commerce-payments-pack` | `payment-reconciliation-pack.md`, `commerce-security-pci-gate.md`, `payment-cutover-checklist.md`. |
| `commerce-omnichannel-pack` | `omnichannel-order-flow-map.md`, `commerce-analytics-pack.md`, `marketplace-integration-pack.md`. |

## Readiness Scores

`commerce-readiness` scores:

- CXP Journey Readiness
- CRM/Dataverse Readiness
- Lead Management Readiness
- Customer Master Readiness
- Commerce HQ Readiness
- Channel Readiness
- Commerce Scale Unit Readiness
- Channel Data Sync Readiness
- POS Readiness
- POS Offline Readiness
- Store Operations Readiness
- Payments/PCI Readiness
- Loyalty/Promotions Readiness
- Pricing/Assortment Readiness
- Omnichannel/E-Commerce Readiness
- Commerce Cutover Readiness

Status rules:

| Status | Rule |
| --- | --- |
| Ready | Score is at least 75 and no critical blocker exists. |
| Needs control | Score is 50-74 or noncritical evidence is missing. |
| Blocked | Score is below 50 or critical Payment, POS Offline, CSU, Store Smoke, or CISO evidence is missing. |

## Go-Live Blocking Evidence

Commerce go-live is blocked when any of these are missing or below threshold:

- CSU Readiness Score under 75.
- POS Offline Readiness Score under 75 where stores require offline capability.
- Payments/PCI Readiness Score under 75.
- Store Cutover Smoke Tests.
- Channel Data Sync Evidence.
- Offline Recovery Runbook.
- Payment Reconciliation Pack.
- Commerce Security/PCI Gate.
- Customer Master Harmonization where CRM/Commerce/FO customer sync is in scope.
- Lead-to-Cash Traceability where CRM/Sales/Commerce scope exists.

## Routing Examples

| User request | Routed skills |
| --- | --- |
| `Kasse offline testen` | POS Offline, POS Lead, Store Ops. Payments is added when payments are mentioned. |
| `CSU Sync ist kritisch` | Commerce Scale Unit Owner, Channel Data Sync Lead. |
| `Lead-to-Cash migrieren` | Lead Management Owner, CRM Owner, Customer Master Lead. |
| `Dataverse Customer Sync` | CRM Owner, Customer Master Lead, Integration Owner. |
| `Store Go-live` | Store Ops, POS, POS Offline, Payments, Commerce Cutover. |
| `PCI Payment Terminal` | Payments Lead, Commerce Security PCI Lead, CISO. |
| `Loyalty Punkte migrieren` | Loyalty Promotions Lead, Customer Master Lead. |
| `BOPIS Prozess testen` | Omnichannel E-Commerce Lead, QA/Test Execution. |
