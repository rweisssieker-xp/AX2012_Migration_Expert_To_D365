#!/usr/bin/env python3
"""Create a project-specific AX to D365FO migration workspace from templates."""

from __future__ import annotations

import argparse
import shutil
from pathlib import Path


TEMPLATE_DIR = Path(__file__).resolve().parents[1] / "templates"


def normalize_project_name(value: str) -> str:
    cleaned = "".join(ch.lower() if ch.isalnum() else "-" for ch in value.strip())
    parts = [part for part in cleaned.split("-") if part]
    return "-".join(parts) or "migration-project"


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("project", help="Customer or migration project name.")
    parser.add_argument(
        "--output",
        default="migration-workspaces",
        help="Parent output directory. Default: migration-workspaces",
    )
    args = parser.parse_args()

    project_dir = Path(args.output) / normalize_project_name(args.project)
    project_dir.mkdir(parents=True, exist_ok=True)

    for template in TEMPLATE_DIR.glob("*.md"):
        shutil.copy2(template, project_dir / template.name)

    print(f"Created migration workspace: {project_dir.resolve()}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
