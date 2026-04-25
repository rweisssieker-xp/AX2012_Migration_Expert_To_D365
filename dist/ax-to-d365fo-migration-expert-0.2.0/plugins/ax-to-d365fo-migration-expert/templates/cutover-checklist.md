# D365FO Cutover Checklist

| Seq | Task | Owner | Duration | Dependency | Status | Rollback note |
| --- | --- | --- | --- | --- | --- | --- |
| 1 | Confirm go/no-go approval |  |  |  | Not started |  |
| 2 | Freeze AX master data changes |  |  |  | Not started |  |
| 3 | Stop AX integrations and batch jobs |  |  |  | Not started |  |
| 4 | Take final AX backup |  |  |  | Not started |  |
| 5 | Export final migration data |  |  |  | Not started |  |
| 6 | Load D365FO configuration and master data deltas |  |  |  | Not started |  |
| 7 | Load opening transactions and balances |  |  |  | Not started |  |
| 8 | Reconcile financial and operational totals |  |  |  | Not started |  |
| 9 | Enable integrations |  |  |  | Not started |  |
| 10 | Smoke test critical business flows |  |  |  | Not started |  |
| 11 | Release users into production |  |  |  | Not started |  |

## Go / No-Go Criteria

| Criterion | Required result | Actual result | Approved by |
| --- | --- | --- | --- |
| Critical reconciliations passed | Yes |  |  |
| Sev 1 defects open | 0 |  |  |
| Sev 2 defects accepted | Yes / No |  |  |
| Business owners approve | Yes |  |  |

