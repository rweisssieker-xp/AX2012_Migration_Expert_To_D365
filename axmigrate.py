#!/usr/bin/env python3
"""Root-level shortcut for the AX to D365FO Migration Expert CLI."""

from __future__ import annotations

import subprocess
import sys
from pathlib import Path


CLI = Path(__file__).resolve().parent / "plugins" / "ax-to-d365fo-migration-expert" / "scripts" / "migration_cli.py"


if __name__ == "__main__":
    raise SystemExit(subprocess.call([sys.executable, str(CLI), *sys.argv[1:]]))
