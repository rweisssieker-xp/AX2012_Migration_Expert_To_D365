# AI Customization Disposition

| Name | Type | Category | Disposition | Target pattern | Risks | Effort | Rationale |
| --- | --- | --- | --- | --- | --- | --- | --- |
| LedgerJournalService | Service | integration | Rebuild | Middleware-backed D365FO integration pattern | overlayering, posting | 7 | Legacy integrations usually need redesign for D365FO operations and monitoring. |
| FR_TaxSettlementBatch | Batch | object | Extend | SysOperation/batch framework alignment | batch, overlayering, posting | 7 | Customization likely needs extension-based migration. |
| UK_VATMakingTaxDigital | Integration | integration | Rebuild | OData, custom service, Business Events, or middleware | aif, overlayering | 7 | Legacy integrations usually need redesign for D365FO operations and monitoring. |
| DE_EInvoiceAdapter | Integration | integration | Rebuild | Middleware-backed D365FO integration pattern | overlayering | 6 | Legacy integrations usually need redesign for D365FO operations and monitoring. |
| US_SalesTaxConnector | Integration | integration | Rebuild | Middleware-backed D365FO integration pattern | integration-modernization | 6 | Legacy integrations usually need redesign for D365FO operations and monitoring. |
| LegacyDataArchive | Report | integration | Rebuild | Middleware-backed D365FO integration pattern | overlayering | 6 | Legacy integrations usually need redesign for D365FO operations and monitoring. |
| LocalLabelExtensions | AOT | integration | Rebuild | Middleware-backed D365FO integration pattern | overlayering | 6 | Legacy integrations usually need redesign for D365FO operations and monitoring. |
| IntercompanyOrderFlow | Class | object | Rebuild | Extension/service/data entity redesign | client-dependency, overlayering | 5 | Unsupported legacy dependency detected. |
| GlobalCustomerMaster | Table | object | Rebuild | Extension/service/data entity redesign | client-dependency, overlayering | 5 | Unsupported legacy dependency detected. |
| VendorBankValidation | Class | object | Extend | Chain of Command or event handler | overlayering | 4 | Customization likely needs extension-based migration. |
| SecurityRoleTemplate | Security | security | Map | D365FO roles, duties, privileges, and SoD review | overlayering | 3 | Security must be mapped rather than technically migrated as-is. |
| CountryRolloutPMO | Process | object | Review | Fit-gap validation required | overlayering | 3 | Insufficient evidence for an automatic recommendation. |
