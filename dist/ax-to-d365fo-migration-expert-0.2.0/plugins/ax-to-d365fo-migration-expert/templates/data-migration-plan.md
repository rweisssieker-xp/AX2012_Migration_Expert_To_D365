# D365FO Data Migration Plan

## 1. Data Scope

| Data domain | Source tables / objects | Target entity | Migration method | Volume | Owner |
| --- | --- | --- | --- | --- | --- |
| Configuration |  |  | Data management / Manual / Package |  |  |
| Master data |  |  | Data management / DMF / Integration |  |  |
| Open transactions |  |  | Data management / Custom |  |  |
| History |  |  | Archive / Reporting / Load |  |  |
| Attachments |  |  | Document management |  |  |

## 2. Migration Cycles

| Cycle | Purpose | Data scope | Environment | Entry criteria | Exit criteria |
| --- | --- | --- | --- | --- | --- |
| Trial 1 | Validate mappings |  |  |  |  |
| Trial 2 | Validate volume and timing |  |  |  |  |
| Dress rehearsal | Validate cutover |  |  |  |  |
| Production | Go-live migration |  |  |  |  |

## 3. Reconciliation

| Check | Source | Target | Tolerance | Owner |
| --- | --- | --- | --- | --- |
| Record counts |  |  |  |  |
| Financial balances |  |  |  |  |
| Inventory quantities |  |  |  |  |
| Open AR/AP |  |  |  |  |

