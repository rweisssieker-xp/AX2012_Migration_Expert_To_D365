# AI Before / After Architecture

| Domain | Before AX | After D365FO |
| --- | --- | --- |
| Application | Dynamics AX legacy environment | Dynamics 365 Finance & Operations cloud environment |
| Integrations | LedgerJournalService, DE_EInvoiceAdapter, UK_VATMakingTaxDigital, US_SalesTaxConnector, LegacyDataArchive, LocalLabelExtensions | OData, custom services, Business Events, middleware, managed files |
| Reporting | Legacy reports not inventoried | D365FO workspaces, SSRS, Power BI, Financial Reporter, archive |
| Data | Legacy data domains not inventoried | Data entities, recurring data jobs, archive/reporting store |
| Security | AX groups/roles | D365FO roles, duties, privileges, SoD controls |
| ALM | Layer/model deployment | Packages, build validation, release pipeline, environment governance |
