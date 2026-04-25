#!/usr/bin/env python3
"""Create Azure DevOps work items from analyzer CSV output."""

from __future__ import annotations

import argparse
import base64
import csv
import json
import os
import urllib.request
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]


def load_config() -> dict:
    return json.loads((ROOT / "config" / "integrations.json").read_text(encoding="utf-8"))["azure_devops"]


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("work_items_csv")
    parser.add_argument("--dry-run", action="store_true")
    args = parser.parse_args()
    cfg = load_config()
    org = os.environ.get(cfg["organization_url_env"], "").rstrip("/")
    project = os.environ.get(cfg["project_env"], "")
    pat = os.environ.get(cfg["pat_env"], "")
    with Path(args.work_items_csv).open("r", encoding="utf-8-sig", newline="") as handle:
        rows = list(csv.DictReader(handle))
    if args.dry_run:
        print(f"Would create {len(rows)} Azure DevOps work items in {org}/{project}")
        return 0
    if not org or not project or not pat:
        raise SystemExit("Missing AZDO_ORG_URL, AZDO_PROJECT, or AZDO_PAT.")
    auth = base64.b64encode(f":{pat}".encode()).decode()
    for row in rows:
        work_type = row.get("Work Item Type", "User Story").replace(" ", "%20")
        url = f"{org}/{project}/_apis/wit/workitems/${work_type}?api-version={cfg['api_version']}"
        patch = [
            {"op": "add", "path": "/fields/System.Title", "value": row.get("Title", "AX migration item")},
            {"op": "add", "path": "/fields/System.Description", "value": row.get("Description", "")},
            {"op": "add", "path": "/fields/System.Tags", "value": row.get("Tags", "AXMigration")},
        ]
        request = urllib.request.Request(url, data=json.dumps(patch).encode(), method="POST")
        request.add_header("Content-Type", "application/json-patch+json")
        request.add_header("Authorization", f"Basic {auth}")
        with urllib.request.urlopen(request) as response:
            print(response.read().decode())
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
