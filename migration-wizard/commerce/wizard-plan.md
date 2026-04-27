# Migration Wizard Plan

## Profile

`commerce`

## Focus

- Commerce
- CSU
- POS Offline
- Payments
- Store Operations

## Commands

```powershell
python .\axmigrate.py analyze plugins/ax-to-d365fo-migration-expert/examples/ax2012-retail-commerce-pos-inventory.csv --output migration-wizard\commerce/contoso-retail-migration/analysis
```
```powershell
python .\axmigrate.py commerce-pack migration-wizard\commerce/contoso-retail-migration/analysis --output migration-wizard\commerce/contoso-retail-migration/commerce-pack
```
```powershell
python .\axmigrate.py commerce-readiness migration-wizard\commerce/contoso-retail-migration/analysis --output migration-wizard\commerce/contoso-retail-migration/commerce-readiness
```
```powershell
python .\axmigrate.py commerce-cutover migration-wizard\commerce/contoso-retail-migration/analysis --output migration-wizard\commerce/contoso-retail-migration/commerce-cutover
```
```powershell
python .\axmigrate.py commerce-offline-check migration-wizard\commerce/contoso-retail-migration/analysis --output migration-wizard\commerce/contoso-retail-migration/commerce-offline-check
```
```powershell
python .\axmigrate.py commerce-payments-pack migration-wizard\commerce/contoso-retail-migration/analysis --output migration-wizard\commerce/contoso-retail-migration/commerce-payments-pack
```
```powershell
python .\axmigrate.py governance-pack migration-wizard\commerce/contoso-retail-migration/analysis --output migration-wizard\commerce/contoso-retail-migration/governance-pack
```
