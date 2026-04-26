#!/usr/bin/env python3
from __future__ import annotations

import argparse
from pathlib import Path

from solo_pack_common import run_solo


def main() -> int:
    parser = argparse.ArgumentParser(description="Run the full solo migration orchestration.")
    parser.add_argument("--project", required=True)
    parser.add_argument("--input", action="append", required=True, dest="inputs")
    parser.add_argument("--output", default="solo-migration")
    args = parser.parse_args()
    path = run_solo(args.project, args.inputs, Path(args.output))
    print(f"Generated solo migration operating system: {path.resolve()}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
