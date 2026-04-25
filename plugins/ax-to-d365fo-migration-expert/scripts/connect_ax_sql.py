#!/usr/bin/env python3
"""Extract AX modelstore inventory directly from SQL Server via ODBC."""

from __future__ import annotations

import argparse
import csv
import json
import os
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]


def load_config() -> dict:
    return json.loads((ROOT / "config" / "integrations.json").read_text(encoding="utf-8"))["ax_sql"]


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--query", help="SQL query to execute. Defaults to integrations.json query.")
    parser.add_argument("--output", required=True)
    parser.add_argument("--dry-run", action="store_true", help="Print required settings without connecting.")
    args = parser.parse_args()
    cfg = load_config()
    env_name = cfg["connection_string_env"]
    query = args.query or cfg["default_query"]
    if args.dry_run:
        print(f"Set {env_name} to an ODBC connection string.")
        print(f"Query: {query}")
        return 0
    conn_str = os.environ.get(env_name)
    if not conn_str:
        raise SystemExit(f"Missing environment variable {env_name}")
    try:
        import pyodbc
    except ImportError as exc:
        raise SystemExit("pyodbc is required for direct AX SQL extraction.") from exc
    with pyodbc.connect(conn_str) as conn:
        cursor = conn.cursor()
        cursor.execute(query)
        columns = [col[0] for col in cursor.description]
        rows = cursor.fetchall()
    output = Path(args.output)
    output.parent.mkdir(parents=True, exist_ok=True)
    with output.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.writer(handle)
        writer.writerow(columns)
        writer.writerows(rows)
    print(f"Wrote {len(rows)} AX SQL rows to {output.resolve()}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
