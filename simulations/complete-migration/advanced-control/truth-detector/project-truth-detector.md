# Project Truth Detector

Project: `Contoso Complete AX to D365FO Migration`

Source: `simulations\complete-migration\guided-run`

Status: `Ready`

Score: `100`

## Purpose

Compares reported status with evidence, gates, tests, and generated artifacts.

## AI Signals

- evidence: `857`
- cutover: `157`
- security: `299`
- finance: `317`
- commerce: `539`
- data: `1050`
- integration: `550`
- testing: `95`

## Recommended Actions

- Challenge all green status items without evidence file, owner, or gate result.
- Escalate missing CISO, UAT, finance, rollback, and cutover evidence.
- Compare steering reports against `go-live-gate-result.json` and evidence manifest.
