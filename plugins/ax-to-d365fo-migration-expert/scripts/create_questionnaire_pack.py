#!/usr/bin/env python3
"""Create role-based questionnaire and migration factory planning packs."""

from __future__ import annotations

import argparse
import json
from pathlib import Path


QUESTIONS = {
    "ceo": [
        "Which business outcomes must the migration deliver beyond technical replacement?",
        "Which processes or legal entities create the highest revenue, compliance, or operational risk?",
        "What is the acceptable go-live risk and downtime window?",
        "Which scope reduction decisions need executive approval?",
    ],
    "cio": [
        "Which integrations are business critical and which can be retired or redesigned?",
        "Where does AX contain unsupported or fragile customization patterns?",
        "Which target architecture decisions are already fixed?",
        "Which ALM, environment, monitoring, and support constraints must be respected?",
    ],
    "ciso": [
        "Which sensitive data domains, retention rules, and audit controls apply?",
        "Which roles or duties create SoD risk?",
        "Which integrations use secrets, direct SQL, files, or privileged access?",
        "What evidence is required for security gate approval?",
    ],
    "pm": [
        "What is the scope baseline and change control process?",
        "Which workstreams have named owners and delivery capacity?",
        "Which decisions block timeline, budget, or quality gates?",
        "What steering cadence and escalation path is approved?",
    ],
    "team": [
        "Which objects, reports, integrations, and data domains are assigned to your workstream?",
        "What acceptance evidence is required for completion?",
        "Which dependencies or missing decisions block execution?",
        "Which test cases prove the migrated behavior works?",
    ],
    "change": [
        "Which roles and business processes change materially?",
        "Who owns UAT sign-off per process?",
        "Which training and communication waves are required?",
        "What hypercare exit criteria will prove adoption?",
    ],
}


def render_questionnaire(persona: str) -> str:
    title = persona.upper() if persona != "pm" else "PMO"
    lines = [f"# {title} Migration Questionnaire", "", "| Question | Answer | Decision / Action | Owner |", "| --- | --- | --- | --- |"]
    for question in QUESTIONS[persona]:
        lines.append(f"| {question} |  |  |  |")
    lines.extend(["", "## AI-KI Follow-up", "", "- Convert answers into risks, decisions, backlog items, and evidence gaps.", "- Update persona pack after every workshop."])
    return "\n".join(lines) + "\n"


def factory_model() -> str:
    return """# Migration Factory Mode

## Portfolio Control
| Customer / Legal Entity / Wave | Scope | Readiness | Top Risk | Next Gate | Owner |
| --- | --- | --- | --- | --- | --- |
|  |  |  |  |  |  |

## Factory Cadence
- Weekly scope reduction review.
- Weekly architecture and security gate review.
- Daily delivery blocker review during build and cutover.
- Steering committee every two weeks or at gate changes.

## Automation Flow
1. Analyze inventory.
2. Generate persona packs.
3. Run questionnaire workshops.
4. Export ADO/GitHub work items.
5. Track readiness score by persona and wave.
6. Refresh reports after scope changes.
"""


def cutover_pack() -> str:
    return """# Cutover War Room Live Pack

| Time | Activity | Owner | Dependency | Go/No-Go Signal | Rollback Point | Status |
| --- | --- | --- | --- | --- | --- | --- |
|  |  |  |  |  |  |  |

## Blocker Log
| ID | Blocker | Impact | Decision Needed | Owner | Deadline |
| --- | --- | --- | --- | --- | --- |

## Communication Templates
- Go decision:
- Delay decision:
- Rollback decision:
- Business validation complete:
"""


def hypercare_pack() -> str:
    return """# Hypercare Command Center

| Defect / Issue | Severity | Business Impact | Owner | ETA | Status |
| --- | --- | --- | --- | --- | --- |
|  |  |  |  |  |  |

## Daily Hypercare Report
- New critical issues:
- Resolved issues:
- Business process adoption:
- Data/integration exceptions:
- Exit criteria progress:
"""


def partner_pack() -> str:
    return """# Partner Sales Accelerator

## Discovery Offer
- AX migration scope reduction assessment.
- Executive value cockpit.
- CIO/CISO risk review.
- Delivery backlog and roadmap.

## Proposal Building Blocks
| Section | Auto-generated Source |
| --- | --- |
| Scope | Analysis summary and disposition |
| Assumptions | Evidence confidence and questionnaire |
| Risks | Risk radar and RAID |
| Workplan | Wave roadmap and backlog |
| Governance | Operating model and steering pack |
"""


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", default="migration-questionnaires")
    parser.add_argument("--persona", choices=[*QUESTIONS.keys(), "all"], default="all")
    args = parser.parse_args()
    output = Path(args.output)
    output.mkdir(parents=True, exist_ok=True)
    personas = list(QUESTIONS) if args.persona == "all" else [args.persona]
    for persona in personas:
        (output / f"{persona}-questionnaire.md").write_text(render_questionnaire(persona), encoding="utf-8")
    (output / "migration-factory-mode.md").write_text(factory_model(), encoding="utf-8")
    (output / "cutover-war-room-live-pack.md").write_text(cutover_pack(), encoding="utf-8")
    (output / "hypercare-command-center.md").write_text(hypercare_pack(), encoding="utf-8")
    (output / "partner-sales-accelerator.md").write_text(partner_pack(), encoding="utf-8")
    (output / "questionnaire-schema.json").write_text(json.dumps(QUESTIONS, indent=2), encoding="utf-8")
    print(f"Generated questionnaire pack into {output.resolve()}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
