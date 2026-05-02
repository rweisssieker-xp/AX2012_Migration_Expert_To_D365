# Configuration

Configuration lives under:

```text
plugins/ax-to-d365fo-migration-expert/config
```

## Files

| File | Purpose |
| --- | --- |
| `alm-release-rules.json` | Alm release rules rules, mappings, thresholds, or routing defaults. |
| `benchmarking-rules.json` | Benchmarking rules rules, mappings, thresholds, or routing defaults. |
| `commerce-cutover-checks.json` | Commerce cutover checks rules, mappings, thresholds, or routing defaults. |
| `commerce-gate-minimum-evidence.json` | Commerce gate minimum evidence rules, mappings, thresholds, or routing defaults. |
| `commerce-readiness-rules.json` | Commerce readiness rules rules, mappings, thresholds, or routing defaults. |
| `commerce-role-skill-map.json` | Commerce role skill map rules, mappings, thresholds, or routing defaults. |
| `commerce-synonyms.json` | Commerce synonyms rules, mappings, thresholds, or routing defaults. |
| `contract-scope-risk-rules.json` | Contract scope risk rules rules, mappings, thresholds, or routing defaults. |
| `country-regulatory-rules.json` | Country regulatory rules rules, mappings, thresholds, or routing defaults. |
| `crm-lead-management-map.json` | Crm lead management map rules, mappings, thresholds, or routing defaults. |
| `d365fo-knowledge-base.json` | D365fo knowledge base rules, mappings, thresholds, or routing defaults. |
| `evidence-vault-rules.json` | Evidence vault rules rules, mappings, thresholds, or routing defaults. |
| `fabric-advisor-rules.json` | Fabric advisor rules rules, mappings, thresholds, or routing defaults. |
| `governance-role-skill-map.json` | Governance role skill map rules, mappings, thresholds, or routing defaults. |
| `governance-synonyms.json` | Governance synonyms rules, mappings, thresholds, or routing defaults. |
| `industry-packs.json` | Industry packs rules, mappings, thresholds, or routing defaults. |
| `integration-resilience-rules.json` | Integration resilience rules rules, mappings, thresholds, or routing defaults. |
| `integrations.json` | Integrations rules, mappings, thresholds, or routing defaults. |
| `intelligence-fabric-rules.json` | Intelligence fabric rules rules, mappings, thresholds, or routing defaults. |
| `license-cost-rules.json` | License cost rules rules, mappings, thresholds, or routing defaults. |
| `migration-cost-model.json` | Migration cost model rules, mappings, thresholds, or routing defaults. |
| `payment-pci-risk-rules.json` | Payment pci risk rules rules, mappings, thresholds, or routing defaults. |
| `portfolio-control-rules.json` | Portfolio control rules rules, mappings, thresholds, or routing defaults. |
| `pos-offline-risk-rules.json` | Pos offline risk rules rules, mappings, thresholds, or routing defaults. |
| `process-twin-rules.json` | Process twin rules rules, mappings, thresholds, or routing defaults. |
| `quality-audit-rules.json` | Quality audit rules rules, mappings, thresholds, or routing defaults. |
| `reconciliation-rules.json` | Reconciliation rules rules, mappings, thresholds, or routing defaults. |
| `regulatory-packs.json` | Regulatory packs rules, mappings, thresholds, or routing defaults. |
| `risk-rules.json` | Risk rules rules, mappings, thresholds, or routing defaults. |
| `scenario-lab-rules.json` | Scenario lab rules rules, mappings, thresholds, or routing defaults. |
| `security-attack-surface-rules.json` | Security attack surface rules rules, mappings, thresholds, or routing defaults. |
| `standard-feature-map.json` | Standard feature map rules, mappings, thresholds, or routing defaults. |
| `technical-debt-rules.json` | Technical debt rules rules, mappings, thresholds, or routing defaults. |
| `training-effectiveness-rules.json` | Training effectiveness rules rules, mappings, thresholds, or routing defaults. |
| `usp-catalog.json` | Usp catalog rules, mappings, thresholds, or routing defaults. |
| `value-realization-rules.json` | Value realization rules rules, mappings, thresholds, or routing defaults. |

## Validation

```powershell
python .\axmigrate.py validate
```
