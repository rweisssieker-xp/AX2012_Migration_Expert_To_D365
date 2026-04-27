#!/usr/bin/env python3
"""Scan migration files for secrets, connection strings, and common personal data patterns."""

from __future__ import annotations

import argparse
import csv
import json
import re
from pathlib import Path


RULES = [
    ("possible-secret", re.compile(r"(?i)(password|pwd|secret|token|pat|bearer)\s*[:=]\s*[^\s,;]+")),
    ("sql-connection-string", re.compile(r"(?i)(server|data source)\s*=\s*[^;]+;.*(user id|uid|password|pwd)\s*=")),
    ("email-address", re.compile(r"\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}\b")),
    ("iban", re.compile(r"\b[A-Z]{2}\d{2}[A-Z0-9]{10,30}\b")),
    ("credit-card-like", re.compile(r"\b(?:\d[ -]*?){13,16}\b")),
]


def candidate_files(source: Path) -> list[Path]:
    if source.is_file():
        return [source]
    suffixes = {".md", ".json", ".csv", ".txt", ".ps1", ".py", ".xpp", ".xpo", ".xml", ".config"}
    return sorted(path for path in source.rglob("*") if path.is_file() and path.suffix.lower() in suffixes)


def scan_file(path: Path) -> list[dict[str, object]]:
    text = path.read_text(encoding="utf-8", errors="ignore")
    findings = []
    for idx, line in enumerate(text.splitlines(), start=1):
        for rule, pattern in RULES:
            if pattern.search(line):
                findings.append({"file": str(path), "line": idx, "rule": rule, "sample": pattern.sub("[REDACTED]", line.strip())[:180]})
    return findings


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("source")
    parser.add_argument("--output", default="security-scan")
    parser.add_argument("--fail-on-findings", action="store_true")
    args = parser.parse_args()
    source = Path(args.source)
    output = Path(args.output)
    output.mkdir(parents=True, exist_ok=True)
    findings = []
    for path in candidate_files(source):
        findings.extend(scan_file(path))
    status = "Blocked" if findings else "Ready"
    (output / "security-scan-report.json").write_text(json.dumps({"status": status, "findings": findings}, indent=2), encoding="utf-8")
    with (output / "security-scan-findings.csv").open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=["file", "line", "rule", "sample"])
        writer.writeheader()
        writer.writerows(findings)
    rows = "\n".join(f"| {Path(item['file']).name} | {item['line']} | {item['rule']} | `{item['sample']}` |" for item in findings) or "| None | - | - | - |"
    (output / "security-scan-report.md").write_text(
        "# Security And PII Scan\n\n"
        f"Status: `{status}`\n\n"
        "| File | Line | Rule | Redacted sample |\n| --- | ---: | --- | --- |\n"
        + rows
        + "\n",
        encoding="utf-8",
    )
    print(f"Security scan status {status} into {output.resolve()}")
    return 2 if findings and args.fail_on_findings else 0


if __name__ == "__main__":
    raise SystemExit(main())
