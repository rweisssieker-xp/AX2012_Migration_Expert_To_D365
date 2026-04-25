#!/usr/bin/env python3
"""Compare two normalized inventory JSON files and report migration scope changes."""

from __future__ import annotations

import argparse
import json
from pathlib import Path


def load(path: str) -> dict[str, dict]:
    data = json.loads(Path(path).read_text(encoding="utf-8"))
    return {item["name"]: item for item in data}


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("baseline")
    parser.add_argument("current")
    parser.add_argument("--output", default="inventory-change-monitor.md")
    args = parser.parse_args()
    old = load(args.baseline)
    new = load(args.current)
    added = sorted(set(new) - set(old))
    removed = sorted(set(old) - set(new))
    changed = sorted(name for name in set(old) & set(new) if old[name] != new[name])
    text = "# Continuous Migration Monitor\n\n" + "\n".join([
        f"- Added scope items: {len(added)}",
        f"- Removed scope items: {len(removed)}",
        f"- Changed scope items: {len(changed)}",
        "",
        "## Added\n",
        "\n".join(f"- {name}" for name in added) or "None",
        "\n## Removed\n",
        "\n".join(f"- {name}" for name in removed) or "None",
        "\n## Changed\n",
        "\n".join(f"- {name}" for name in changed) or "None",
    ])
    Path(args.output).write_text(text + "\n", encoding="utf-8")
    print(f"Wrote {Path(args.output).resolve()}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
