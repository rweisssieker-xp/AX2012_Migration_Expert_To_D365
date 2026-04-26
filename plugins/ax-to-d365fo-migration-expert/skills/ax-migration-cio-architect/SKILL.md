---
name: ax-migration-cio-architect
description: Use when a CIO, CTO, enterprise architect, solution architect, IT director, or technical leadership team needs AX to D365FO target architecture, modernization path, integration strategy, technical debt, ALM, environment, or platform decisions.
---

# AX Migration CIO Architect

## Purpose

Turn AX technical evidence into D365FO architecture decisions. Focus on modernization, supportability, technical debt reduction, integration redesign, data architecture, reporting architecture, ALM, environments, and platform governance.

## Default Outputs

- CIO architecture control tower.
- Current-state to target-state architecture view.
- Upgrade vs hybrid vs reimplementation decision.
- Integration modernization plan.
- Technical debt and dependency map.
- Environment and ALM plan.
- Architecture decision records.

## Workflow

1. Identify source version, customization patterns, integrations, reports, data domains, ISVs, and operations constraints.
2. Classify each major technical area as `standardize`, `configure`, `extend`, `rebuild`, `replace`, `retire`, or `archive`.
3. Map legacy patterns to D365FO patterns: extensions, Chain of Command, event handlers, data entities, OData, Business Events, Dataverse, Dual-write, Power BI, and managed middleware.
4. Surface architecture risks and dependencies before proposing a delivery sequence.
5. Produce decisions with options, recommendation, tradeoffs, evidence, and downstream work items.

## Use Generated Artifacts

Prefer these analyzer outputs when available:

- `persona-cio-architecture-view.md`
- `ai-before-after-architecture.md`
- `ai-upgrade-path-decision.md`
- `ai-dependency-graph.md`
- `migration-knowledge-graph.json`
- `ai-standard-feature-matches.md`
- `ai-data-entity-mapping.md`
- `ai-adrs.md`

## Quality Bar

- Avoid lift-and-shift recommendations unless evidence supports them.
- Prefer D365FO standard capability before custom build.
- Call out unsupported or fragile patterns such as direct SQL, overlayering, COM/client dependencies, AIF-only designs, and custom posting logic.
- Include operating model implications: monitoring, ownership, release process, security, and support.
