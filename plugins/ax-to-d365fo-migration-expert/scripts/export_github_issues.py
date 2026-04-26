#!/usr/bin/env python3
"""Export migration analysis tasks as GitHub issue import Markdown."""

from __future__ import annotations

import argparse
import csv
from pathlib import Path


def read_work_items(path: Path) -> list[dict[str, str]]:
    if not path.exists():
        return []
    with path.open("r", encoding="utf-8-sig", newline="") as handle:
        return list(csv.DictReader(handle))


def issue_body(row: dict[str, str]) -> str:
    title = row.get("Title", "Migration work item")
    description = row.get("Description", "")
    tags = row.get("Tags", "migration")
    effort = row.get("Effort", "")
    risk = row.get("Risk", "")
    return f"""# {title}

## Description
{description}

## Migration Metadata
- Tags: {tags}
- Effort: {effort}
- Risk: {risk}

## Acceptance Criteria
- Source evidence reviewed.
- Target D365FO approach documented.
- Owner and reviewer assigned.
- Test/evidence attached before closure.
"""


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("analysis_dir")
    parser.add_argument("--output", default="github-issues")
    args = parser.parse_args()
    analysis_dir = Path(args.analysis_dir)
    output = Path(args.output)
    output.mkdir(parents=True, exist_ok=True)
    rows = read_work_items(analysis_dir / "ai-azure-devops-work-items.csv")
    if not rows:
        raise SystemExit("No ai-azure-devops-work-items.csv found. Run analyze first.")
    for index, row in enumerate(rows, start=1):
        safe = "".join(ch if ch.isalnum() else "-" for ch in row.get("Title", "issue").lower()).strip("-")[:70]
        (output / f"{index:03d}-{safe or 'migration-issue'}.md").write_text(issue_body(row), encoding="utf-8")
    print(f"Exported {len(rows)} GitHub issue files into {output.resolve()}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
