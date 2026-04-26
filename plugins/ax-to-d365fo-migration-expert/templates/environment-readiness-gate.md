# Environment Readiness Gate

## Purpose

AI-KI generated governance artifact for autonomous AX to D365FO migration control.

## Inputs

| Input | Evidence Needed | Owner |
| --- | --- | --- |
| Current state | Analyzer outputs, meeting notes, decisions, risks, and evidence | Master Orchestrator |
| Target state | D365FO, Commerce, CRM, data, integration, security, and process design evidence | Workstream owner |
| Approval state | Sign-off, gate, audit, legal, security, finance, and business approval evidence | Accountable approver |

## AI-KI Assessment

| Area | Status | Risk | Missing Evidence | Next Action |
| --- | --- | --- | --- | --- |
| Scope | Needs control | Unapproved scope growth can increase cost and timeline | Scope baseline and change log | Validate with PMO and sponsor |
| Evidence | Needs control | Gate decisions may be unsupported | Fresh evidence and owner | Update evidence vault |
| Go-live | Needs control | Cutover or reconciliation proof may be incomplete | Rehearsal and sign-off | Route to responsible skill |

## Automation Outputs

- Decision-ready summary.
- Blocker list.
- Owner and due date proposal.
- Backlog-ready actions.
- Gate recommendation.
- Evidence checklist.

## Go/No-Go Logic

- `Ready`: required evidence is current, owners are assigned, and no critical blocker exists.
- `Needs control`: evidence is incomplete but not go-live critical.
- `Blocked`: required external approval, reconciliation, cutover, security, legal, finance, or production evidence is missing.
