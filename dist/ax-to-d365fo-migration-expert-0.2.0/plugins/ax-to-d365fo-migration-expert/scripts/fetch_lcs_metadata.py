#!/usr/bin/env python3
"""Fetch LCS metadata from a configured HTTP endpoint."""

from __future__ import annotations

import argparse
import json
import os
import urllib.request
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--path", default="/")
    parser.add_argument("--output", required=True)
    parser.add_argument("--dry-run", action="store_true")
    args = parser.parse_args()
    cfg = json.loads((ROOT / "config" / "integrations.json").read_text(encoding="utf-8"))["lcs"]
    base = os.environ.get(cfg["base_url_env"], "").rstrip("/")
    token = os.environ.get(cfg["token_env"], "")
    if args.dry_run:
        print(f"Would call {cfg['base_url_env']}{args.path} with bearer token from {cfg['token_env']}")
        return 0
    if not base or not token:
        raise SystemExit(f"Missing {cfg['base_url_env']} or {cfg['token_env']}")
    request = urllib.request.Request(base + args.path)
    request.add_header("Authorization", f"Bearer {token}")
    with urllib.request.urlopen(request) as response:
        data = response.read()
    Path(args.output).write_bytes(data)
    print(f"Wrote LCS response to {Path(args.output).resolve()}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
