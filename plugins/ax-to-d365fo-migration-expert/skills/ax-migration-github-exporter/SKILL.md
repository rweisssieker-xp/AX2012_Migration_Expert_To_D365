---
name: ax-migration-github-exporter
description: Use when exporting AX to D365FO migration backlog, risks, Azure DevOps work item CSV, or analyzer tasks into GitHub issue Markdown files for teams that do not use Azure DevOps.
---

# AX Migration GitHub Exporter

## Purpose

Create GitHub issue Markdown files from analyzer work items.

## Command

```powershell
python axmigrate.py github-issues migration-analysis/sample --output github-issues/sample
```

## Input

Requires `ai-azure-devops-work-items.csv` in the analysis folder.

## Quality Bar

Review generated issues before bulk import. Add labels, milestones, and assignees according to the target repository process.
