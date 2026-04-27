# Migration Wizard Plan

## Profile

`multi-country`

## Focus

- Konzernrollout
- Legal entities
- Localization
- Tax
- Wave planning
- Portfolio control

## Commands

```powershell
python .\axmigrate.py analyze plugins/ax-to-d365fo-migration-expert/examples/ax2012-multi-country-rollout-inventory.csv --output migration-wizard\multi-country/contoso-global-rollout/analysis
```
```powershell
python .\axmigrate.py country-regulatory-pack migration-wizard\multi-country/contoso-global-rollout/analysis --output migration-wizard\multi-country/contoso-global-rollout/country-regulatory-pack
```
```powershell
python .\axmigrate.py portfolio-control migration-wizard\multi-country/contoso-global-rollout/analysis --output migration-wizard\multi-country/contoso-global-rollout/portfolio-control
```
```powershell
python .\axmigrate.py scenario-lab migration-wizard\multi-country/contoso-global-rollout/analysis --output migration-wizard\multi-country/contoso-global-rollout/scenario-lab
```
```powershell
python .\axmigrate.py board-risk migration-wizard\multi-country/contoso-global-rollout/analysis --output migration-wizard\multi-country/contoso-global-rollout/board-risk
```
```powershell
python .\axmigrate.py governance-pack migration-wizard\multi-country/contoso-global-rollout/analysis --output migration-wizard\multi-country/contoso-global-rollout/governance-pack
```
```powershell
python .\axmigrate.py evidence-vault migration-wizard\multi-country/contoso-global-rollout/analysis --output migration-wizard\multi-country/contoso-global-rollout/evidence-vault
```
