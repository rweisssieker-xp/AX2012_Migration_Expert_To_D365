#!/usr/bin/env python3
"""Analyze AX usage telemetry CSV and summarize usage frequency."""

from __future__ import annotations

import argparse
import csv
from collections import Counter
from pathlib import Path


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("input")
    parser.add_argument("--object-column", default="Object")
    parser.add_argument("--output", default="usage-telemetry-summary.csv")
    args = parser.parse_args()
    with Path(args.input).open("r", encoding="utf-8-sig", newline="") as handle:
        rows = list(csv.DictReader(handle))
    counts = Counter(row.get(args.object_column, "") for row in rows if row.get(args.object_column, ""))
    output = Path(args.output)
    with output.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.writer(handle)
        writer.writerow(["Name", "UsageCount", "Usage"])
        for name, count in counts.most_common():
            usage = "High" if count >= 100 else "Medium" if count >= 10 else "Low"
            writer.writerow([name, count, usage])
    print(f"Wrote usage summary to {output.resolve()}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
