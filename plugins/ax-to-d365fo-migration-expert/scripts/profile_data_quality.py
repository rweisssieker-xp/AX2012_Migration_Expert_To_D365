#!/usr/bin/env python3
"""Profile CSV data quality for migration readiness."""

from __future__ import annotations

import argparse
import csv
from collections import Counter
from pathlib import Path


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("input")
    parser.add_argument("--output", default="data-quality-profile.md")
    args = parser.parse_args()
    path = Path(args.input)
    with path.open("r", encoding="utf-8-sig", newline="") as handle:
        rows = list(csv.DictReader(handle))
    fields = rows[0].keys() if rows else []
    out = ["# Data Quality AI Profiler\n"]
    out.append(f"\nRows: {len(rows)}\n")
    out.append("| Column | Nulls | Distinct | Duplicate-heavy |")
    out.append("| --- | --- | --- | --- |")
    for field in fields:
        values = [row.get(field, "") for row in rows]
        nulls = sum(1 for value in values if not str(value).strip())
        counts = Counter(values)
        duplicate_heavy = "Yes" if rows and counts.most_common(1)[0][1] > max(2, len(rows) * 0.5) else "No"
        out.append(f"| {field} | {nulls} | {len(set(values))} | {duplicate_heavy} |")
    Path(args.output).write_text("\n".join(out) + "\n", encoding="utf-8")
    print(f"Wrote {Path(args.output).resolve()}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
