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
| `regulatory-packs.json` | DACH/GDPR/GoBD, EU e-invoicing, audit, pharma, automotive, and public-sector control packs. |
| `commerce-role-skill-map.json` | Commerce role to skill, artifact, and CLI command routing. |
| `commerce-synonyms.json` | German/English synonyms for CXP, CRM, Commerce, CSU, POS, Offline, Payments, and Store Ops routing. |
| `commerce-readiness-rules.json` | Score rules for Commerce/CXP/CRM/POS workstreams. |
| `commerce-gate-minimum-evidence.json` | Minimum evidence required for Commerce go-live gates. |
| `commerce-cutover-checks.json` | Cutover checks for HQ, CSU, Channel DB, POS, Payments, Offline, and Store Smoke. |
| `pos-offline-risk-rules.json` | POS offline blockers, risks, and recovery controls. |
| `payment-pci-risk-rules.json` | Payment, PCI, terminal, tokenization, and settlement risk rules. |
| `crm-lead-management-map.json` | CRM/Dataverse, lead-to-cash, customer/contact/opportunity/case, dual-write, and customer master mapping. |

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

## Commerce Gate Defaults

Commerce go-live is blocked when critical evidence is missing or readiness is below threshold for CSU, POS Offline, Payments/PCI, Store Smoke Tests, Channel Data Sync, Offline Recovery, Payment Reconciliation, Commerce Security/PCI, Customer Master Harmonization, or Lead-to-Cash Traceability.

Readiness status uses:

| Status | Rule |
| --- | --- |
| Ready | Score is at least 75 and no critical blockers exist. |
| Needs control | Score is 50-74 or noncritical evidence is missing. |
| Blocked | Score is below 50 or critical CSU/POS Offline/Payments/Store Smoke/CISO evidence is missing. |
