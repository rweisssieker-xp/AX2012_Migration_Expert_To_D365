---
name: ax-migration-data-governance
description: Use when data owners, master data managers, data migration leads, data governance teams, or records owners need AX to D365FO data ownership, cleansing, reconciliation, retention, archive, master data, or migration evidence guidance.
---

# AX Migration Data Governance

## Purpose

Turn migration data findings into ownership, cleansing, reconciliation, archive, and governance work.

## Outputs

- Data ownership RACI.
- Data cleansing backlog.
- Data reconciliation pack.
- Master data governance pack.
- Archive and retention decision pack.

## Command

```powershell
python axmigrate.py stakeholder-pack migration-analysis/sample --stakeholder data --output stakeholder-packs/data
```

## Quality Bar

Every data issue needs owner, rule, source, target, validation method, reconciliation check, and cutover implication.
