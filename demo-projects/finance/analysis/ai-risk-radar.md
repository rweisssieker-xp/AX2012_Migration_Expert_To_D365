# AI Migration Risk Radar

| Item | Category | Risk flags | Recommendation | Reason |
| --- | --- | --- | --- | --- |
| LedgerJournalPostOverride | object | overlayering, posting | Extend | Customization likely needs extension-based migration. |
| DimensionLegacyEditor | object | overlayering | Retire Candidate | Low usage suggests scope reduction opportunity. |
| GLTrialBalanceSqlExport | integration | direct-sql, overlayering | Rebuild | Legacy integrations usually need redesign for D365FO operations and monitoring. |
| TaxAuditPack | report | overlayering, report-rationalization | Standard / Power BI Review | Reports should be rationalized before rebuild. |
| LegacyFinanceController | security | overlayering | Map | Security must be mapped rather than technically migrated as-is. |
