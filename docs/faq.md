# FAQ

## Is this a direct AX upgrade tool?

No. It is a migration assessment, scope reduction, planning, and delivery-acceleration plugin. It can analyze evidence and produce artifacts, but it does not perform a Microsoft-supported technical upgrade by itself.

## Which AX versions are covered?

The skill is written for AX 4.0, AX 2009, and AX 2012, including AX 2012 R2/R3 scenarios.

## What input formats are supported?

- CSV
- TSV
- JSON
- X++ text
- XPO
- AOT text exports
- Modelstore-style CSV exports
- Usage telemetry CSV

## Does it connect directly to AX SQL?

Yes, via the `ax-sql` connector, but only when `AX_SQL_CONNECTION_STRING` is configured. Use `--dry-run` first.

## Does it create Azure DevOps work items?

Yes, via the `push-ado` connector. It requires `AZDO_ORG_URL`, `AZDO_PROJECT`, and `AZDO_PAT`. The analyzer also produces `ai-azure-devops-work-items.csv`.

## Does it call LCS or D365FO APIs?

It includes generic HTTP connector scaffolding for LCS and D365FO/OData endpoints. Real use requires valid URLs and bearer tokens.

## Are recommendations final decisions?

No. Recommendations include evidence and confidence signals. Business owners, architects, and steering committees should validate high-impact decisions.

## Can generated analysis be committed?

Usually no. Generated analysis may contain customer data. Keep it out of version control unless it is sanitized sample data.

## How do I validate everything?

```powershell
python plugins\ax-to-d365fo-migration-expert\scripts\migration_cli.py validate
```

## Where do I change cost assumptions?

Edit:

```text
plugins/ax-to-d365fo-migration-expert/config/migration-cost-model.json
```

