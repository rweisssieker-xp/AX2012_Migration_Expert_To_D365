---
name: ax-migration-reconciliation-judge
description: Use when migration work needs finance, inventory, customer, vendor, open transaction, and tolerance-based reconciliation sign-off.
---

# ax-migration-reconciliation-judge

## Purpose

Use this skill to turn AX to D365FO migration evidence into autonomous governance outputs for finance, inventory, customer, vendor, open transaction, and tolerance-based reconciliation sign-off.

## Inputs

- Analyzer output folders.
- Meeting notes, status reports, decisions, risks, issues, assumptions, and evidence files.
- Contract, scope, test, cutover, reconciliation, license, ALM, training, regulatory, archive, and process inputs where available.

## Outputs

- Role-specific recommendations.
- Missing evidence and blocker lists.
- Gate status with owner and next action.
- Backlog-ready actions with acceptance criteria and evidence expectations.

## Operating Rules

- Treat legal, security, finance, audit, PCI, payment, customer, and production go-live approvals as external human approvals.
- Mark items as blocked when critical evidence is missing.
- Prefer scope reduction, standard D365FO capability, clean governance, and auditable decisions over uncontrolled migration growth.
