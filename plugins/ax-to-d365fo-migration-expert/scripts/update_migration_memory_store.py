#!/usr/bin/env python3
"""Persist migration memory into a local SQLite database and JSONL ledger."""

from __future__ import annotations

import argparse
import hashlib
import json
import sqlite3
from datetime import datetime, timezone
from pathlib import Path


def read_source(source: Path) -> str:
    if source.is_file():
        return source.read_text(encoding="utf-8", errors="ignore")
    parts = []
    if source.exists():
        for path in sorted(source.rglob("*")):
            if path.is_file() and path.suffix.lower() in {".md", ".json", ".csv", ".txt", ".xpp", ".xpo"}:
                parts.append(path.read_text(encoding="utf-8", errors="ignore"))
    return "\n".join(parts)


def signals(text: str) -> list[str]:
    lower = text.lower()
    result = []
    for label, words in {
        "commerce-pos": ["commerce", "retail", "pos", "store", "payment", "csu"],
        "crm-lead-to-cash": ["crm", "dataverse", "lead", "opportunity", "customer master"],
        "finance-reconciliation": ["ledger", "finance", "reconciliation", "tax", "balance"],
        "integration-risk": ["aif", "integration", "service", "odata", "middleware", "api"],
        "security-gate": ["security", "ciso", "role", "sod", "pci", "secret"],
        "cutover-risk": ["cutover", "rollback", "smoke", "rehearsal", "hypercare"],
    }.items():
        if any(word in lower for word in words):
            result.append(label)
    return result or ["general-migration"]


def ensure_schema(conn: sqlite3.Connection) -> None:
    conn.execute(
        """
        create table if not exists memory_entries (
            id integer primary key autoincrement,
            created_utc text not null,
            project text not null,
            source text not null,
            source_hash text not null,
            signal text not null,
            summary text not null
        )
        """
    )
    conn.execute("create index if not exists ix_memory_project on memory_entries(project)")
    conn.execute("create index if not exists ix_memory_signal on memory_entries(signal)")


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("source")
    parser.add_argument("--project", default="Migration Project")
    parser.add_argument("--output", default="migration-memory-store")
    args = parser.parse_args()

    source = Path(args.source)
    output = Path(args.output)
    output.mkdir(parents=True, exist_ok=True)
    text = read_source(source)
    digest = hashlib.sha256(text.encode("utf-8", errors="ignore")).hexdigest()
    now = datetime.now(timezone.utc).isoformat()
    entries = [
        {
            "created_utc": now,
            "project": args.project,
            "source": str(source),
            "source_hash": digest,
            "signal": signal,
            "summary": f"{args.project}: reusable migration memory for {signal}",
        }
        for signal in signals(text)
    ]
    db = output / "migration-memory.sqlite"
    conn = sqlite3.connect(db)
    ensure_schema(conn)
    conn.executemany(
        "insert into memory_entries(created_utc, project, source, source_hash, signal, summary) values(:created_utc, :project, :source, :source_hash, :signal, :summary)",
        entries,
    )
    conn.commit()
    conn.close()
    with (output / "migration-memory.jsonl").open("a", encoding="utf-8") as handle:
        for entry in entries:
            handle.write(json.dumps(entry, ensure_ascii=True) + "\n")
    (output / "migration-memory-store.md").write_text(
        "# Migration Memory Store\n\n"
        f"Project: `{args.project}`\n\n"
        f"SQLite: `{db.name}`\n\n"
        "## Signals\n\n"
        + "\n".join(f"- {entry['signal']}" for entry in entries)
        + "\n",
        encoding="utf-8",
    )
    print(f"Updated migration memory store into {output.resolve()}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
