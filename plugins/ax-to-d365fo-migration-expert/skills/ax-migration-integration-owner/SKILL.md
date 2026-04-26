---
name: ax-migration-integration-owner
description: Use when integration owners, middleware teams, API teams, EDI owners, platform integration leads, or interface workstreams need AX to D365FO interface criticality, modernization, middleware, retry, error handling, reconciliation, or cutover sequencing.
---

# AX Migration Integration Owner

## Purpose

Modernize and control integration migration from AX to D365FO.

## Outputs

- Interface criticality matrix.
- API modernization backlog.
- Middleware target design.
- Retry and error-handling pack.
- Integration cutover sequence.

## Command

```powershell
python axmigrate.py stakeholder-pack migration-analysis/sample --stakeholder integration --output stakeholder-packs/integration
```

## Quality Bar

Include authentication, monitoring, replay, reconciliation, error ownership, operational support, and rollback behavior for every critical interface.
