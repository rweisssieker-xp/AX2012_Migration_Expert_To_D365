# AI Data Entity Mapping

| AX source | Source type | D365FO target candidate | Transformation notes | Reconciliation |
| --- | --- | --- | --- | --- |
| LedgerJournalService | Service | Financial data entity review | Validate mandatory fields, dimensions, references, and legal entity handling. | Record count, balance/quantity check, exception report |
| DE_EInvoiceAdapter | Integration | Data management entity mapping required | Validate mandatory fields, dimensions, references, and legal entity handling. | Record count, balance/quantity check, exception report |
| UK_VATMakingTaxDigital | Integration | Data management entity mapping required | Validate mandatory fields, dimensions, references, and legal entity handling. | Record count, balance/quantity check, exception report |
| US_SalesTaxConnector | Integration | Sales order / customer transaction entity review | Validate mandatory fields, dimensions, references, and legal entity handling. | Record count, balance/quantity check, exception report |
| GlobalCustomerMaster | Table | Customer-related data entity review | Validate mandatory fields, dimensions, references, and legal entity handling. | Record count, balance/quantity check, exception report |
| LegacyDataArchive | Report | Data management entity mapping required | Validate mandatory fields, dimensions, references, and legal entity handling. | Record count, balance/quantity check, exception report |
| LocalLabelExtensions | AOT | Data management entity mapping required | Validate mandatory fields, dimensions, references, and legal entity handling. | Record count, balance/quantity check, exception report |
