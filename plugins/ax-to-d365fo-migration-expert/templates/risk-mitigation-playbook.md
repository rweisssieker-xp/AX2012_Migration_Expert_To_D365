# Risk-to-Mitigation Playbook

| Risk | Trigger | Mitigation | Owner | Gate |
| --- | --- | --- | --- | --- |
| Direct SQL | SQL/ODBC/direct table access | Replace with data entity, service, export, or reporting replica | Technical architect | Design |
| AIF | AIF/Axd services | Redesign with OData, custom service, Business Events, or middleware | Integration architect | Design |
| Overlayering | Legacy layer/model modification | Replace with extension, CoC, or event handler | Technical architect | Build |
| Custom posting | Ledger/inventory/customer/vendor posting logic | Senior architecture and reconciliation review | Solution architect | Design |
| Large history | Full transaction history migration | Archive/reporting strategy and reconciliation plan | Data lead | Data |
