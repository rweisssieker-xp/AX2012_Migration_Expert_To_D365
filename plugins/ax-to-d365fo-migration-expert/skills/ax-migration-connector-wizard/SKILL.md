---
name: ax-migration-connector-wizard
description: Use when setting up, checking, explaining, or troubleshooting AX SQL, Azure DevOps, LCS, D365FO OData/metadata, usage telemetry, GitHub export, or connector environment variables for the migration plugin.
---

# AX Migration Connector Wizard

## Purpose

Guide connector setup and validation for migration automation.

## Commands

```powershell
python axmigrate.py doctor
python axmigrate.py ax-sql --output ax-inventory.csv --dry-run
python axmigrate.py push-ado migration-analysis/sample/ai-azure-devops-work-items.csv --dry-run
python axmigrate.py fetch-lcs --path / --output lcs.json --dry-run
python axmigrate.py fetch-d365fo --path /data/$metadata --output metadata.xml --dry-run
python axmigrate.py github-issues migration-analysis/sample --output github-issues/sample
```

## Quality Bar

Never print or commit secrets. Prefer dry-run first. Use `doctor` to show which optional environment variables are missing.
