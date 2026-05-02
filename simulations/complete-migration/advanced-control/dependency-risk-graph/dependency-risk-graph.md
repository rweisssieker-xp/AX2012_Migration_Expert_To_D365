# Dependency Risk Graph

Project: `Contoso Complete AX to D365FO Migration`

Source: `simulations\complete-migration\guided-run`

Status: `Ready`

Score: `95`

## Purpose

Visualizes dependencies between workstreams, gates, tests, integrations, and cutover steps.

## AI Signals

- evidence: `857`
- cutover: `157`
- security: `299`
- finance: `317`
- commerce: `539`
- data: `1050`
- integration: `550`
- testing: `95`

## Graph

```mermaid
graph TD
  Analysis[Analysis] --> Skill Routing[Skill Routing]
  Skill Routing[Skill Routing] --> Evidence Gates[Evidence Gates]
  Evidence Gates[Evidence Gates] --> Security[Security]
  Security[Security] --> Finance[Finance]
  Finance[Finance] --> CommercePOS[Commerce/POS]
  CommercePOS[Commerce/POS] --> Testing[Testing]
  Testing[Testing] --> Cutover[Cutover]
  Cutover[Cutover] --> Go-live[Go-live]
```
