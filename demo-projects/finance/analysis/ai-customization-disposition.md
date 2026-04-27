# AI Customization Disposition

| Name | Type | Category | Disposition | Target pattern | Risks | Effort | Rationale |
| --- | --- | --- | --- | --- | --- | --- | --- |
| GLTrialBalanceSqlExport | Interface | integration | Rebuild | Data entity, export, reporting replica, or data lake pattern | direct-sql, overlayering | 11 | Legacy integrations usually need redesign for D365FO operations and monitoring. |
| LedgerJournalPostOverride | Class | object | Extend | Chain of Command or event handler | overlayering, posting | 9 | Customization likely needs extension-based migration. |
| TaxAuditPack | Report | report | Standard / Power BI Review | D365FO workspace, SSRS, Power BI, Financial Reporter, or archive | overlayering, report-rationalization | 9 | Reports should be rationalized before rebuild. |
| DimensionLegacyEditor | Form | object | Retire Candidate | Business validation before migration | overlayering | 7 | Low usage suggests scope reduction opportunity. |
| LegacyFinanceController | Role | security | Map | D365FO roles, duties, privileges, and SoD review | overlayering | 5 | Security must be mapped rather than technically migrated as-is. |
