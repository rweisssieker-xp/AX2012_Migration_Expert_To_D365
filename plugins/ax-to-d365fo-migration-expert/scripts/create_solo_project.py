#!/usr/bin/env python3
from __future__ import annotations

import argparse
from pathlib import Path

from solo_pack_common import create_solo_project


def main() -> int:
    parser = argparse.ArgumentParser(description="Create a solo AX to D365FO migration project.")
    parser.add_argument("project")
    parser.add_argument("--output", default="solo-migration")
    args = parser.parse_args()
    path = create_solo_project(args.project, Path(args.output))
    print(f"Created solo migration project: {path.resolve()}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
