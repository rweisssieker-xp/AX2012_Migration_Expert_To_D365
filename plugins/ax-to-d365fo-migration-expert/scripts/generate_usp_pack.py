#!/usr/bin/env python3
"""Generate a productized AI/KI USP pack for migration positioning and delivery."""

from __future__ import annotations

import argparse
import csv
import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
CONFIG = ROOT / "config" / "usp-catalog.json"


def load_catalog() -> list[dict[str, object]]:
    data = json.loads(CONFIG.read_text(encoding="utf-8"))
    return list(data["usps"])


def render_markdown(usps: list[dict[str, object]], project: str) -> str:
    rows = []
    for item in usps:
        rows.append(
            "| {id} | {name} | {audience} | {claim} | {automation} | {proof} |".format(
                id=item["id"],
                name=item["name"],
                audience=", ".join(item["audience"]),
                claim=item["claim"],
                automation=", ".join(item["automation"]),
                proof=", ".join(item["proof"]),
            )
        )
    top = "\n".join(f"- **{item['name']}**: {item['claim']}" for item in usps[:10])
    return (
        "# AI/KI USP Pack\n\n"
        f"Project: `{project}`\n\n"
        "## Executive USP Narrative\n\n"
        "The plugin differentiates itself by turning AX to D365FO migration work into an evidence-backed, "
        "role-aware, local-first migration operating system. It does not only create reports; it routes skills, "
        "generates packs, challenges status, detects missing evidence, creates go-live gates, and produces board-ready outputs.\n\n"
        "## Top 10 Board-Level USPs\n\n"
        f"{top}\n\n"
        "## Full USP Catalog\n\n"
        "| ID | USP | Audience | Claim | Automation | Proof |\n"
        "| --- | --- | --- | --- | --- | --- |\n"
        + "\n".join(rows)
        + "\n\n## Positioning\n\n"
        "- For CEOs: board-ready migration truth, value, risk, and go-live confidence.\n"
        "- For CIOs: architecture, standardization, workstream orchestration, and reusable migration intelligence.\n"
        "- For CISOs: evidence gates, security scans, PCI/POS controls, and audit-ready proof.\n"
        "- For PMOs: autonomous control, action inboxes, status honesty, and cutover confidence.\n"
        "- For partners and solo consultants: a local command center that makes one operator behave like a full migration team.\n"
    )


def render_html(markdown: str) -> str:
    body = []
    in_table = False
    for line in markdown.splitlines():
        if line.startswith("# "):
            body.append(f"<h1>{line[2:]}</h1>")
        elif line.startswith("## "):
            if in_table:
                body.append("</tbody></table>")
                in_table = False
            body.append(f"<h2>{line[3:]}</h2>")
        elif line.startswith("| ID |"):
            body.append("<table><thead><tr><th>ID</th><th>USP</th><th>Audience</th><th>Claim</th><th>Automation</th><th>Proof</th></tr></thead><tbody>")
            in_table = True
        elif line.startswith("| ---"):
            continue
        elif in_table and line.startswith("| "):
            cells = [cell.strip() for cell in line.strip("|").split("|")]
            body.append("<tr>" + "".join(f"<td>{cell}</td>" for cell in cells) + "</tr>")
        elif line.startswith("- "):
            body.append(f"<p>{line}</p>")
        elif line.strip():
            body.append(f"<p>{line}</p>")
    if in_table:
        body.append("</tbody></table>")
    return (
        "<!doctype html><html lang=\"en\"><head><meta charset=\"utf-8\"><title>AI/KI USP Pack</title>"
        "<style>body{font-family:Segoe UI,Arial,sans-serif;margin:0;background:#f6f8fb;color:#172033}"
        "main{max-width:1180px;margin:auto;padding:28px}h1{color:#17446b}h2{margin-top:28px}"
        "table{width:100%;border-collapse:collapse;background:#fff;border:1px solid #d9e2ec}"
        "th,td{padding:9px;border-bottom:1px solid #e7edf3;text-align:left;vertical-align:top;font-size:13px}"
        "th{background:#eef3f8}p{line-height:1.45}</style></head><body><main>"
        + "\n".join(body)
        + "</main></body></html>"
    )


def write_csv(usps: list[dict[str, object]], output: Path) -> None:
    with (output / "ai-ki-usp-catalog.csv").open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=["id", "name", "audience", "claim", "automation", "proof"])
        writer.writeheader()
        for item in usps:
            writer.writerow(
                {
                    "id": item["id"],
                    "name": item["name"],
                    "audience": ", ".join(item["audience"]),
                    "claim": item["claim"],
                    "automation": ", ".join(item["automation"]),
                    "proof": ", ".join(item["proof"]),
                }
            )


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("source", nargs="?", default=".", help="Optional analysis or project folder used for context.")
    parser.add_argument("--project", default="Migration Project")
    parser.add_argument("--output", default="usp-packs")
    args = parser.parse_args()

    output = Path(args.output)
    output.mkdir(parents=True, exist_ok=True)
    usps = load_catalog()
    markdown = render_markdown(usps, args.project)
    (output / "ai-ki-usp-pack.md").write_text(markdown, encoding="utf-8")
    (output / "ai-ki-usp-pack.html").write_text(render_html(markdown), encoding="utf-8")
    (output / "ai-ki-usp-catalog.json").write_text(json.dumps({"source": args.source, "project": args.project, "usps": usps}, indent=2), encoding="utf-8")
    write_csv(usps, output)
    print(f"Generated AI/KI USP pack into {output.resolve()}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
