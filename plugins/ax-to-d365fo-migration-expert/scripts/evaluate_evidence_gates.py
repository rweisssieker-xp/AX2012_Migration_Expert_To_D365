#!/usr/bin/env python3
"""Generate interactive evidence gate questions and go-live status."""

from __future__ import annotations

import argparse
import json
from pathlib import Path


GATES = [
    ("ciso_approval", "Ist CISO-Freigabe vorhanden?", True),
    ("cutover_rehearsal", "Ist Cutover-Rehearsal bestanden?", True),
    ("finance_reconciliation", "Sind Finance-Reconciliations signiert?", True),
    ("uat_signoff", "Ist UAT fachlich abgenommen?", True),
    ("commerce_payments", "Sind Payment/PCI Evidence und Store Smoke Tests vorhanden?", False),
    ("rollback_plan", "Ist Rollback/Recovery Plan getestet?", True),
]


def status(answers: dict[str, bool]) -> str:
    missing_required = [key for key, _, required in GATES if required and not answers.get(key)]
    missing_optional = [key for key, _, required in GATES if not required and not answers.get(key)]
    if missing_required:
        return "Blocked"
    if missing_optional:
        return "Needs control"
    return "Ready"


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("source", nargs="?", default=".", help="Analysis folder or project folder used as evidence context.")
    parser.add_argument("--output", default="evidence-gates")
    for key, _, _ in GATES:
        parser.add_argument(f"--{key.replace('_', '-')}", choices=["yes", "no"], default="no")
    args = parser.parse_args()
    answers = {key: getattr(args, key) == "yes" for key, _, _ in GATES}
    result = {"status": status(answers), "answers": answers, "source": str(Path(args.source))}
    output = Path(args.output)
    output.mkdir(parents=True, exist_ok=True)
    questions = "\n".join(f"- [{ 'x' if answers[key] else ' ' }] {question} `--{key.replace('_', '-')}`" for key, question, _ in GATES)
    actions = "\n".join(f"- Close evidence for `{key}`." for key, value in answers.items() if not value) or "- No missing gate evidence."
    (output / "evidence-gate-questionnaire.md").write_text(
        "# Evidence Gate Questionnaire\n\n"
        f"Source: `{args.source}`\n\n"
        + questions
        + "\n",
        encoding="utf-8",
    )
    (output / "go-live-gate-result.json").write_text(json.dumps(result, indent=2), encoding="utf-8")
    (output / "next-evidence-actions.md").write_text(f"# Next Evidence Actions\n\n## Status\n\n`{result['status']}`\n\n## Actions\n\n{actions}\n", encoding="utf-8")
    print(f"Generated evidence gate result {result['status']} into {output.resolve()}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
