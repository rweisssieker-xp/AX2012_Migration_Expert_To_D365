---
name: ax-migration-persona-pack-generator
description: Use when generating CEO, CIO, CISO, project manager, team, or all persona packs, readiness scores, PowerPoint decks, Excel workbooks, or role-specific migration deliverables from AX to D365FO analysis outputs.
---

# AX Migration Persona Pack Generator

## Purpose

Generate role-specific deliverables from an existing analysis folder.

## Commands

```powershell
python axmigrate.py persona-pack migration-analysis/sample --persona all --office --output persona-packs/sample
python axmigrate.py persona-pack migration-analysis/sample --persona ciso --output persona-packs/ciso
```

## Outputs

- `<persona>-pack.md`
- `readiness-scores.json`
- `readiness-scores.csv`
- `persona-readiness.xlsx` when `--office` is used
- `persona-readiness-deck.pptx` when `--office` is used

## Quality Bar

Use this after `analyze`. If persona source files are missing, regenerate analysis before trusting scores.
