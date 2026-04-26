---
name: ax-migration-qa-lead
description: Use when QA leads, test managers, UAT coordinators, regression owners, defect managers, or quality workstreams need AX to D365FO test coverage, risk-based testing, UAT, regression suites, defect triage, or quality gate evidence.
---

# AX Migration QA Lead

## Purpose

Convert migration scope and risk into test strategy, coverage, UAT, regression, and defect control.

## Outputs

- Test coverage matrix.
- Risk-based test prioritization.
- UAT pack.
- Regression suite generator.
- Defect triage model.

## Command

```powershell
python axmigrate.py stakeholder-pack migration-analysis/sample --stakeholder qa --output stakeholder-packs/qa
```

## Quality Bar

Trace tests to risks, business processes, customizations, integrations, data migration, security roles, and cutover smoke checks.
