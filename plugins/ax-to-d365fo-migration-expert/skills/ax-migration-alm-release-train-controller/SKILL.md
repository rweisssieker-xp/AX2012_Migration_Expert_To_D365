---
name: ax-migration-alm-release-train-controller
description: Use when migration work needs ALM, release train, code freeze, deployments, environments, build gates, and release readiness.
---

# ax-migration-alm-release-train-controller

## Purpose

Use this skill to turn AX to D365FO migration evidence into autonomous governance outputs for ALM, release train, code freeze, deployments, environments, build gates, and release readiness.

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
