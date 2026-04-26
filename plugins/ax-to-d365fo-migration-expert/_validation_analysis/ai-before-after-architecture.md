# AI Before / After Architecture

| Domain | Before AX | After D365FO |
| --- | --- | --- |
| Application | Dynamics AX legacy environment | Dynamics 365 Finance & Operations cloud environment |
| Integrations | AIFCustomerExport, WarehouseFileDrop | OData, custom services, Business Events, middleware, managed files |
| Reporting | InventAgingCustom | D365FO workspaces, SSRS, Power BI, Financial Reporter, archive |
| Data | InventTransHistory | Data entities, recurring data jobs, archive/reporting store |
| Security | AX groups/roles | D365FO roles, duties, privileges, SoD controls |
| ALM | Layer/model deployment | Packages, build validation, release pipeline, environment governance |
