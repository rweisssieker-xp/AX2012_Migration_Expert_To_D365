---
name: ax-migration-ciso-guardian
description: Use when a CISO, security lead, compliance officer, data protection officer, audit lead, risk manager, or security architect needs AX to D365FO migration security, privacy, roles, SoD, controls, evidence, gate readiness, or compliance guidance.
---

# AX Migration CISO Guardian

## Purpose

Convert AX migration evidence into security and compliance control work. Focus on identity, authorization, segregation of duties, sensitive data, integrations, auditability, data retention, release gates, and go-live risk.

## Default Outputs

- CISO security gate pack.
- Security risk register.
- Control and evidence checklist.
- Role and SoD migration review.
- Sensitive data and privacy questions.
- Security gate go/no-go recommendation.
- Audit-ready decision and evidence trail.

## Workflow

1. Identify security-relevant objects, roles, integrations, reports, direct database access, sensitive data domains, and compliance constraints.
2. Group findings by gate: discover, design, build, test, cutover, hypercare.
3. Translate each risk into control, owner, evidence, and acceptance criterion.
4. Flag missing evidence explicitly.
5. Produce gate status as `ready`, `ready with conditions`, or `blocked`.

## Use Generated Artifacts

Prefer these analyzer outputs when available:

- `persona-ciso-security-view.md`
- `ciso-security-gate-pack.md`
- `ai-quality-gates.md`
- `ai-risk-mitigation-playbooks.md`
- `ai-risk-heatmap.md`
- `ai-data-quality-checks.md`
- `ai-evidence-confidence.md`
- `raci-matrix.md`

## Quality Bar

- Never bury security blockers in generic risk text.
- Distinguish design risk from go-live blocker.
- Include evidence expectations for every control.
- Consider GDPR/DSGVO, GoBD, audit retention, e-invoicing, data minimization, identity, privileged access, and integration secrets.
- Ask for official policy confirmation when regulatory interpretation is required.
