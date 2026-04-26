---
name: ax-migration-support-operations
description: Use when support managers, ITSM owners, operations teams, service desk leads, monitoring teams, or BAU transition owners need AX to D365FO support model, runbooks, monitoring, alerting, hypercare-to-BAU, or incident categorization.
---

# AX Migration Support Operations

## Purpose

Prepare the post-go-live operating model from migration evidence.

## Outputs

- Support model generator.
- Runbook pack.
- Monitoring and alerting plan.
- Hypercare-to-BAU transition.
- Incident categorization model.

## Command

```powershell
python axmigrate.py stakeholder-pack migration-analysis/sample --stakeholder support --output stakeholder-packs/support
```

## Quality Bar

Every critical process, integration, batch, report, and data flow needs support owner, monitoring signal, runbook, escalation, and SLA expectation.
