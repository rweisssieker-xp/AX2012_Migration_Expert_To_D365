# CIO Architecture View

| Item | Domain | Target pattern | Architecture risk | Effort |
| --- | --- | --- | --- | --- |
| LedgerJournalService | integration | Middleware-backed D365FO integration pattern | overlayering, posting | 7 |
| FR_TaxSettlementBatch | object | SysOperation/batch framework alignment | batch, overlayering, posting | 7 |
| UK_VATMakingTaxDigital | integration | OData, custom service, Business Events, or middleware | aif, overlayering | 7 |
| DE_EInvoiceAdapter | integration | Middleware-backed D365FO integration pattern | overlayering | 6 |
| US_SalesTaxConnector | integration | Middleware-backed D365FO integration pattern | integration-modernization | 6 |
| LegacyDataArchive | integration | Middleware-backed D365FO integration pattern | overlayering | 6 |
| LocalLabelExtensions | integration | Middleware-backed D365FO integration pattern | overlayering | 6 |
| IntercompanyOrderFlow | object | Extension/service/data entity redesign | client-dependency, overlayering | 5 |
| GlobalCustomerMaster | object | Extension/service/data entity redesign | client-dependency, overlayering | 5 |
| VendorBankValidation | object | Chain of Command or event handler | overlayering | 4 |
| CountryRolloutPMO | object | Fit-gap validation required | overlayering | 3 |

## CIO Focus

- Remove unsupported legacy integration patterns.
- Reduce technical debt before cloud migration.
- Sequence high-risk rebuilds through architecture gates.
