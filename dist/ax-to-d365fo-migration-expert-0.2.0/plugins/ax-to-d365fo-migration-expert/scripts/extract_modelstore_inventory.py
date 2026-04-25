#!/usr/bin/env python3
"""Normalize AX modelstore-style CSV exports into analyzer inventory CSV."""

from __future__ import annotations

import argparse
import csv
from pathlib import Path


def pick(row: dict[str, str], *names: str) -> str:
    lowered = {key.lower().replace(" ", ""): value for key, value in row.items()}
    for name in names:
        value = lowered.get(name.lower().replace(" ", ""))
        if value:
            return value.strip()
    return ""


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("input")
    parser.add_argument("--output", required=True)
    args = parser.parse_args()

    with Path(args.input).open("r", encoding="utf-8-sig", newline="") as handle:
        rows = list(csv.DictReader(handle))

    output = Path(args.output)
    output.parent.mkdir(parents=True, exist_ok=True)
    with output.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=["Category", "ObjectType", "Name", "Layer", "Module", "Usage", "Complexity", "Technology", "BusinessPurpose"])
        writer.writeheader()
        for row in rows:
            object_type = pick(row, "ElementType", "ObjectType", "Type", "AOTType") or "unknown"
            writer.writerow(
                {
                    "Category": "Object",
                    "ObjectType": object_type,
                    "Name": pick(row, "Name", "ElementName", "ObjectName", "AOTName") or "unnamed",
                    "Layer": pick(row, "Layer", "Model", "ModelName"),
                    "Module": pick(row, "Module", "Path", "ParentName"),
                    "Usage": pick(row, "Usage", "Frequency"),
                    "Complexity": pick(row, "Complexity") or "Medium",
                    "Technology": "AX modelstore export",
                    "BusinessPurpose": pick(row, "Description", "BusinessPurpose", "Purpose"),
                }
            )
    print(f"Normalized {len(rows)} modelstore rows to {output.resolve()}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
