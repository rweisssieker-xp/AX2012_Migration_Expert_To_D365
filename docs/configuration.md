# Configuration

Configuration lives under:

```text
plugins/ax-to-d365fo-migration-expert/config
```

## Files

| File | Purpose |
| --- | --- |
| `migration-cost-model.json` | Converts effort points to person-days and budget range. |
| `standard-feature-map.json` | Maps AX terms to D365FO standard capabilities. |
| `d365fo-knowledge-base.json` | Data entities, business events, workspaces, and feature management hints. |
| `risk-rules.json` | Risk-to-mitigation guidance. |
| `industry-packs.json` | Industry-specific focus areas. |
| `integrations.json` | Environment variable names and connector defaults. |

## Cost Model

Tune these fields for your delivery organization:

```json
{
  "hours_per_effort_point": 6,
  "hours_per_day": 8,
  "blended_day_rate": 950,
  "risk_multiplier": {
    "Low": 1.0,
    "Medium": 1.15,
    "High": 1.3,
    "Critical": 1.5
  }
}
```

## Integration Variables

Set only when using real external connectors:

| Variable | Used by |
| --- | --- |
| `AX_SQL_CONNECTION_STRING` | AX SQL connector |
| `AZDO_ORG_URL` | Azure DevOps connector |
| `AZDO_PROJECT` | Azure DevOps connector |
| `AZDO_PAT` | Azure DevOps connector |
| `LCS_BASE_URL` | LCS connector |
| `LCS_BEARER_TOKEN` | LCS connector |
| `D365FO_BASE_URL` | D365FO connector |
| `D365FO_BEARER_TOKEN` | D365FO connector |

## Validation

After configuration changes:

```powershell
python plugins\ax-to-d365fo-migration-expert\scripts\migration_cli.py validate
```

