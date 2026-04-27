# AI Migration Risk Radar

| Item | Category | Risk flags | Recommendation | Reason |
| --- | --- | --- | --- | --- |
| LedgerJournalService | integration | overlayering, posting | Rebuild | Legacy integrations usually need redesign for D365FO operations and monitoring. |
| DE_EInvoiceAdapter | integration | overlayering | Rebuild | Legacy integrations usually need redesign for D365FO operations and monitoring. |
| FR_TaxSettlementBatch | object | batch, overlayering, posting | Extend | Customization likely needs extension-based migration. |
| UK_VATMakingTaxDigital | integration | aif, overlayering | Rebuild | Legacy integrations usually need redesign for D365FO operations and monitoring. |
| US_SalesTaxConnector | integration | integration-modernization | Rebuild | Legacy integrations usually need redesign for D365FO operations and monitoring. |
| IntercompanyOrderFlow | object | client-dependency, overlayering | Rebuild | Unsupported legacy dependency detected. |
| GlobalCustomerMaster | object | client-dependency, overlayering | Rebuild | Unsupported legacy dependency detected. |
| VendorBankValidation | object | overlayering | Extend | Customization likely needs extension-based migration. |
| SecurityRoleTemplate | security | overlayering | Map | Security must be mapped rather than technically migrated as-is. |
| LegacyDataArchive | integration | overlayering | Rebuild | Legacy integrations usually need redesign for D365FO operations and monitoring. |
| CountryRolloutPMO | object | overlayering | Review | Insufficient evidence for an automatic recommendation. |
| LocalLabelExtensions | integration | overlayering | Rebuild | Legacy integrations usually need redesign for D365FO operations and monitoring. |
