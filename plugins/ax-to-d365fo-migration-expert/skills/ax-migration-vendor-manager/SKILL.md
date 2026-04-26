---
name: ax-migration-vendor-manager
description: Use when procurement leads, vendor managers, license managers, commercial owners, ISV owners, or sourcing teams need AX to D365FO ISV contract risk, license impact, vendor readiness, third-party replacement, or commercial decision guidance.
---

# AX Migration Vendor Manager

## Purpose

Control ISV, vendor, license, and commercial risks during migration.

## Outputs

- ISV contract risk pack.
- License impact view.
- Vendor readiness checklist.
- Third-party replacement matrix.
- Commercial decision log.

## Command

```powershell
python axmigrate.py stakeholder-pack migration-analysis/sample --stakeholder vendor --output stakeholder-packs/vendor
```

## Quality Bar

Track contract owner, renewal date, D365FO availability, replacement option, data migration impact, support model, and commercial decision deadline.
