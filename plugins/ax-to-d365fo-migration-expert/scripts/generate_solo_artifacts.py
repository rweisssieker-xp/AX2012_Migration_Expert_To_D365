#!/usr/bin/env python3
from __future__ import annotations

import argparse
from pathlib import Path

from solo_pack_common import MODE_OUTPUTS, generate_mode


def main() -> int:
    parser = argparse.ArgumentParser(description="Generate solo/master-orchestrator artifacts.")
    parser.add_argument("source")
    parser.add_argument("--mode", choices=sorted(MODE_OUTPUTS), required=True)
    parser.add_argument("--output")
    parser.add_argument("--role", default="")
    parser.add_argument("--audience", default="")
    args = parser.parse_args()
    source = Path(args.source)
    output = Path(args.output) if args.output else source / args.mode
    extra = " ".join(part for part in [f"Role: {args.role}" if args.role else "", f"Audience: {args.audience}" if args.audience else ""] if part)
    generate_mode(source, output, args.mode, extra)
    print(f"Generated {args.mode} artifacts into {output.resolve()}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
