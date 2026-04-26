#!/usr/bin/env python3
"""Analyze AX inventory exports and generate D365FO migration assessment reports.

Accepted inputs are CSV or JSON files with object, integration, report, ISV, role,
or data-domain rows. The script is intentionally schema-tolerant so it can work
with early discovery exports before a normalized inventory model exists.
"""

from __future__ import annotations

import argparse
import csv
import html
import json
import re
from dataclasses import dataclass, field
from pathlib import Path
from typing import Any

PLUGIN_ROOT = Path(__file__).resolve().parents[1]
CONFIG_DIR = PLUGIN_ROOT / "config"

RISK_KEYWORDS = {
    "direct-sql": ["select *", "insert_recordset", "connection", "statement", "odbc", "sql", "recordinsertlist"],
    "aif": ["aif", "documentservice", "axd", "service reference"],
    "client-dependency": ["com", "activex", "winapi", "filesystem", "fileio", "excel", "clipboard"],
    "overlayering": ["overlayer", "usr", "cus", "var", "syp", "gls"],
    "posting": ["ledger", "post", "settle", "inventtrans", "custtrans", "vendtrans"],
    "batch": ["runbasebatch", "batch", "sysoperation"],
}

DEFAULT_COST_MODEL = {
    "hours_per_effort_point": 6,
    "hours_per_day": 8,
    "risk_multiplier": {
        "Low": 1.0,
        "Medium": 1.15,
        "High": 1.3,
        "Critical": 1.5,
    },
    "blended_day_rate": 950,
}

DEFAULT_STANDARD_FEATURE_MAP = {
    "customer": "Customer master, customer groups, credit and collections, customer data entities",
    "cust": "Customer master, customer groups, credit and collections, customer data entities",
    "vendor": "Vendor master, procurement categories, vendor data entities",
    "vend": "Vendor master, procurement categories, vendor data entities",
    "sales": "Sales order management, pricing, trade agreements, sales order data entities",
    "purchase": "Procurement and sourcing, purchase orders, vendor collaboration",
    "purch": "Procurement and sourcing, purchase orders, vendor collaboration",
    "invent": "Inventory management, warehouse management, inventory data entities",
    "warehouse": "Warehouse management, mobile device flows, work templates",
    "ledger": "General ledger, financial dimensions, journals, Financial Reporter",
    "tax": "Tax configuration, localization, electronic reporting where applicable",
    "project": "Project management and accounting",
    "retail": "Dynamics 365 Commerce and channel architecture",
}

OBJECT_EFFORT = {
    "table": 3,
    "class": 3,
    "form": 4,
    "report": 3,
    "query": 1,
    "menuitem": 1,
    "security": 2,
    "batch": 4,
    "service": 4,
}


@dataclass
class InventoryItem:
    source_file: str
    raw: dict[str, Any]
    category: str = "object"
    object_type: str = "unknown"
    name: str = ""
    layer: str = ""
    module: str = ""
    usage: str = ""
    complexity: str = ""
    technology: str = ""
    business_purpose: str = ""
    risk_flags: list[str] = field(default_factory=list)
    disposition: str = "Review"
    target_pattern: str = ""
    effort_points: int = 1
    confidence: str = "Medium"
    confidence_reason: str = ""
    rationale: str = ""


def norm_key(value: str) -> str:
    return "".join(ch.lower() for ch in value if ch.isalnum())


def get(row: dict[str, Any], *names: str, default: str = "") -> str:
    normalized = {norm_key(str(key)): value for key, value in row.items()}
    for name in names:
        value = normalized.get(norm_key(name))
        if value is not None:
            return str(value).strip()
    return default


def load_rows(path: Path) -> list[dict[str, Any]]:
    if path.suffix.lower() == ".json":
        data = json.loads(path.read_text(encoding="utf-8-sig"))
        if isinstance(data, list):
            return [dict(item) for item in data if isinstance(item, dict)]
        if isinstance(data, dict):
            for key in ("items", "objects", "inventory", "rows"):
                if isinstance(data.get(key), list):
                    return [dict(item) for item in data[key] if isinstance(item, dict)]
            return [data]

    with path.open("r", encoding="utf-8-sig", newline="") as handle:
        if path.suffix.lower() in (".csv", ".tsv"):
            dialect = "excel-tab" if path.suffix.lower() == ".tsv" else "excel"
            return list(csv.DictReader(handle, dialect=dialect))

        return load_text_inventory(path, handle.read())


def load_text_inventory(path: Path, text: str) -> list[dict[str, Any]]:
    rows: list[dict[str, Any]] = []
    current_type = infer_text_object_type(path, text)
    current_name = path.stem

    for line in text.splitlines():
        stripped = line.strip()
        if not stripped:
            continue
        xpo_match = re.search(r"^(?:CLASS|TABLE|FORM|REPORT|QUERY|JOB|MAP|VIEW)\s+#?([A-Za-z0-9_]+)", stripped, re.I)
        method_match = re.search(r"\b(?:class|table|form|report)\s+([A-Za-z0-9_]+)", stripped, re.I)
        if xpo_match:
            current_type = xpo_match.group(0).split()[0].title()
            current_name = xpo_match.group(1)
        elif method_match:
            current_name = method_match.group(1)

    category = "object"
    if re.search(r"\b(AIF|Axd|service|OData)\b", text, re.I):
        category = "integration"
    elif re.search(r"\b(SSRS|report|SRSReport)\b", text, re.I):
        category = "report"
    elif re.search(r"\b(role|duty|privilege|security)\b", text, re.I):
        category = "security"

    rows.append(
        {
            "Category": category,
            "ObjectType": current_type,
            "Name": current_name,
            "Layer": infer_layer(text),
            "Module": infer_module(text),
            "Usage": "",
            "Complexity": infer_code_complexity(text),
            "Technology": "X++ / XPO / AOT text",
            "BusinessPurpose": code_pattern_summary(text),
            "CodePatterns": ", ".join(detect_code_patterns(text)),
        }
    )
    return rows


def infer_text_object_type(path: Path, text: str) -> str:
    suffix = path.suffix.lower()
    if suffix == ".xpo":
        for token in ("CLASS", "TABLE", "FORM", "REPORT", "QUERY", "JOB"):
            if re.search(rf"\b{token}\b", text, re.I):
                return token.title()
    return "Class" if re.search(r"\bclass\b", text, re.I) else "unknown"


def infer_layer(text: str) -> str:
    match = re.search(r"\b(USR|CUS|VAR|ISV|GLS|SYP|SYS)\b", text, re.I)
    return match.group(1).upper() if match else ""


def infer_module(text: str) -> str:
    lowered = text.lower()
    for key, module in {
        "cust": "Accounts receivable",
        "vend": "Accounts payable",
        "sales": "Sales",
        "purch": "Procurement",
        "invent": "Inventory",
        "ledger": "Finance",
        "whs": "Warehouse management",
        "retail": "Retail / Commerce",
    }.items():
        if key in lowered:
            return module
    return ""


def infer_code_complexity(text: str) -> str:
    patterns = detect_code_patterns(text)
    if len(patterns) >= 5 or any(pattern in patterns for pattern in ("custom-posting", "direct-sql", "client-dependency")):
        return "High"
    if len(patterns) >= 2:
        return "Medium"
    return "Low"


def detect_code_patterns(text: str) -> list[str]:
    pattern_map = {
        "tts-transaction": r"\btts(Begin|Commit|Abort)\b",
        "direct-sql": r"\b(Connection|Statement|ODBC|RecordInsertList|insert_recordset|update_recordset|delete_from)\b",
        "runbase-batch": r"\bRunBaseBatch\b",
        "sysoperation": r"\bSysOperation\b",
        "aif-service": r"\b(AIF|Axd|DocumentService)\b",
        "client-dependency": r"\b(COM|ActiveX|WinAPI|FileIO|AsciiIo|CommaIo|Excel)\b",
        "number-sequence": r"\bNumberSeq\b",
        "custom-posting": r"\b(SalesFormLetter|PurchFormLetter|InventTrans|LedgerJournal|CustTrans|VendTrans)\b",
        "form-logic": r"\b(FormRun|FormDataSource|modifiedField|validateWrite)\b",
    }
    return [name for name, pattern in pattern_map.items() if re.search(pattern, text, re.I)]


def code_pattern_summary(text: str) -> str:
    patterns = detect_code_patterns(text)
    return "Detected code patterns: " + ", ".join(patterns) if patterns else "No high-risk X++ patterns detected."


def infer_category(path: Path, row: dict[str, Any]) -> str:
    text = " ".join([path.stem, *[str(value) for value in row.values()]]).lower()
    if any(word in text for word in ("integration", "aif", "odata", "service", "edi", "middleware")):
        return "integration"
    if any(word in text for word in ("report", "ssrs", "power bi", "management reporter")):
        return "report"
    if any(word in text for word in ("isv", "addon", "add-on", "vertical")):
        return "isv"
    if any(word in text for word in ("role", "duty", "privilege", "security")):
        return "security"
    if any(word in text for word in ("data", "table", "entity", "history", "transaction")):
        return "data" if "data" in path.stem.lower() else "object"
    return "object"


def detect_risks(item: InventoryItem) -> list[str]:
    text = " ".join(str(value).lower() for value in item.raw.values())
    flags: list[str] = []
    for risk, keywords in RISK_KEYWORDS.items():
        if any(keyword in text for keyword in keywords):
            flags.append(risk)
    if item.category == "integration" and not flags:
        flags.append("integration-modernization")
    if item.category == "report":
        flags.append("report-rationalization")
    if "custom-posting" in text:
        flags.append("posting")
    if "tts-transaction" in text:
        flags.append("transaction-scope")
    return sorted(set(flags))


def score_effort(item: InventoryItem) -> int:
    base = OBJECT_EFFORT.get(item.object_type.lower(), 2)
    if item.category == "integration":
        base = 5
    elif item.category == "report":
        base = 3
    elif item.category == "isv":
        base = 6
    elif item.category == "security":
        base = 2
    elif item.category == "data":
        base = 4

    complexity = item.complexity.lower()
    if "high" in complexity:
        base += 4
    elif "medium" in complexity:
        base += 2
    elif "low" in complexity:
        base += 0

    base += min(len(item.risk_flags), 4)
    return base


def classify(item: InventoryItem) -> None:
    text = " ".join(str(value).lower() for value in item.raw.values())
    usage = item.usage.lower()
    object_type = item.object_type.lower()

    if any(word in text for word in ("obsolete", "unused", "not used", "retire", "decommission")):
        item.disposition = "Retire"
        item.target_pattern = "Remove after business validation"
        item.confidence = "High"
        item.rationale = "Inventory indicates obsolete or unused functionality."
    elif "low" in usage or "rare" in usage:
        item.disposition = "Retire Candidate"
        item.target_pattern = "Business validation before migration"
        item.rationale = "Low usage suggests scope reduction opportunity."
    elif item.category == "integration":
        item.disposition = "Rebuild"
        item.target_pattern = integration_pattern(item)
        item.rationale = "Legacy integrations usually need redesign for D365FO operations and monitoring."
    elif item.category == "report":
        item.disposition = "Standard / Power BI Review"
        item.target_pattern = "D365FO workspace, SSRS, Power BI, Financial Reporter, or archive"
        item.rationale = "Reports should be rationalized before rebuild."
    elif item.category == "isv":
        item.disposition = "ISV Review"
        item.target_pattern = "D365FO ISV successor, standard replacement, custom extension, or retire"
        item.rationale = "ISV capability needs product roadmap and licensing validation."
    elif item.category == "security":
        item.disposition = "Map"
        item.target_pattern = "D365FO roles, duties, privileges, and SoD review"
        item.rationale = "Security must be mapped rather than technically migrated as-is."
    elif "direct-sql" in item.risk_flags or "client-dependency" in item.risk_flags:
        item.disposition = "Rebuild"
        item.target_pattern = "Extension/service/data entity redesign"
        item.rationale = "Unsupported legacy dependency detected."
    elif object_type in ("table", "class", "form", "service", "batch"):
        item.disposition = "Extend"
        item.target_pattern = extension_pattern(item)
        item.rationale = "Customization likely needs extension-based migration."
    else:
        item.disposition = "Review"
        item.target_pattern = "Fit-gap validation required"
        item.rationale = "Insufficient evidence for an automatic recommendation."
    item.confidence, item.confidence_reason = evidence_confidence(item)


def evidence_confidence(item: InventoryItem) -> tuple[str, str]:
    evidence_fields = [
        item.name,
        item.category,
        item.object_type,
        item.module,
        item.usage,
        item.complexity,
        item.technology,
        item.business_purpose,
    ]
    filled = sum(1 for value in evidence_fields if value)
    if item.disposition == "Retire" or filled >= 7:
        return "High", "Inventory row contains strong classification evidence."
    if filled >= 5:
        return "Medium", "Inventory row supports a recommendation but needs workshop validation."
    return "Low", "Recommendation is based on limited inventory evidence."


def extension_pattern(item: InventoryItem) -> str:
    object_type = item.object_type.lower()
    if object_type == "class":
        return "Chain of Command or event handler"
    if object_type == "form":
        return "Form extension plus event handlers"
    if object_type == "table":
        return "Table extension, data entity, and validation events"
    if object_type == "batch":
        return "SysOperation/batch framework alignment"
    if object_type == "service":
        return "Custom service, OData, or data entity"
    return "D365FO extension pattern"


def integration_pattern(item: InventoryItem) -> str:
    text = " ".join(str(value).lower() for value in item.raw.values())
    if "aif" in text or "axd" in text:
        return "OData, custom service, Business Events, or middleware"
    if "file" in text or "csv" in text or "ftp" in text:
        return "Managed file integration through middleware or recurring data jobs"
    if "sql" in text:
        return "Data entity, export, reporting replica, or data lake pattern"
    if "crm" in text or "dataverse" in text:
        return "Dataverse integration or Dual-write review"
    return "Middleware-backed D365FO integration pattern"


def to_item(path: Path, row: dict[str, Any]) -> InventoryItem:
    item = InventoryItem(
        source_file=path.name,
        raw=row,
        category=get(row, "category", "area", default=infer_category(path, row)).lower(),
        object_type=get(row, "object_type", "type", "object type", "aot type", default="unknown"),
        name=get(row, "name", "object", "object name", "aot name", "integration", "report", default="unnamed"),
        layer=get(row, "layer", "model", "package"),
        module=get(row, "module", "area", "process"),
        usage=get(row, "usage", "usage evidence", "used", "frequency"),
        complexity=get(row, "complexity", "difficulty"),
        technology=get(row, "technology", "tech", "interface type"),
        business_purpose=get(row, "business purpose", "purpose", "description"),
    )
    item.risk_flags = detect_risks(item)
    item.effort_points = score_effort(item)
    classify(item)
    return item


def complexity_rating(items: list[InventoryItem]) -> tuple[str, int]:
    score = sum(item.effort_points for item in items)
    score += sum(3 for item in items if "direct-sql" in item.risk_flags)
    score += sum(3 for item in items if "aif" in item.risk_flags)
    score += sum(2 for item in items if item.disposition in ("Rebuild", "ISV Review"))

    if score >= 180:
        return "Critical", score
    if score >= 90:
        return "High", score
    if score >= 35:
        return "Medium", score
    return "Low", score


def md_table(headers: list[str], rows: list[list[Any]]) -> str:
    lines = [
        "| " + " | ".join(headers) + " |",
        "| " + " | ".join("---" for _ in headers) + " |",
    ]
    for row in rows:
        values = [str(value).replace("\n", " ").replace("|", "/") for value in row]
        lines.append("| " + " | ".join(values) + " |")
    return "\n".join(lines)


def write_reports(items: list[InventoryItem], output: Path) -> None:
    output.mkdir(parents=True, exist_ok=True)
    rating, score = complexity_rating(items)
    cost_model = load_json_config("migration-cost-model.json", DEFAULT_COST_MODEL)
    feature_map = load_json_config("standard-feature-map.json", DEFAULT_STANDARD_FEATURE_MAP)
    d365fo_kb = load_json_config("d365fo-knowledge-base.json", {})

    summary_rows = [
        ["Total items", len(items)],
        ["Complexity rating", rating],
        ["Complexity score", score],
        ["Retire candidates", sum(1 for item in items if "Retire" in item.disposition)],
        ["Rebuild / ISV review", sum(1 for item in items if item.disposition in ("Rebuild", "ISV Review"))],
        ["Risk flags", sum(len(item.risk_flags) for item in items)],
    ]
    (output / "ai-analysis-summary.md").write_text(
        "# AI AX Inventory Analysis Summary\n\n"
        + md_table(["Metric", "Value"], summary_rows)
        + "\n\n## Top Risks\n\n"
        + top_risks(items)
        + "\n",
        encoding="utf-8",
    )

    disposition_rows = [
        [
            item.name,
            item.object_type,
            item.category,
            item.disposition,
            item.target_pattern,
            ", ".join(item.risk_flags),
            item.effort_points,
            item.rationale,
        ]
        for item in sorted(items, key=lambda value: value.effort_points, reverse=True)
    ]
    (output / "ai-customization-disposition.md").write_text(
        "# AI Customization Disposition\n\n"
        + md_table(
            ["Name", "Type", "Category", "Disposition", "Target pattern", "Risks", "Effort", "Rationale"],
            disposition_rows,
        )
        + "\n",
        encoding="utf-8",
    )

    risk_rows = [
        [item.name, item.category, ", ".join(item.risk_flags), item.disposition, item.rationale]
        for item in items
        if item.risk_flags
    ]
    (output / "ai-risk-radar.md").write_text(
        "# AI Migration Risk Radar\n\n"
        + md_table(["Item", "Category", "Risk flags", "Recommendation", "Reason"], risk_rows)
        + "\n",
        encoding="utf-8",
    )

    effort_by_category: dict[str, int] = {}
    count_by_category: dict[str, int] = {}
    for item in items:
        effort_by_category[item.category] = effort_by_category.get(item.category, 0) + item.effort_points
        count_by_category[item.category] = count_by_category.get(item.category, 0) + 1
    effort_rows = [
        [category, count_by_category[category], points, effort_band(points)]
        for category, points in sorted(effort_by_category.items())
    ]
    (output / "ai-effort-estimate.md").write_text(
        "# AI Migration Effort Estimate\n\n"
        + md_table(["Workstream", "Items", "Effort points", "Effort band"], effort_rows)
        + "\n\nEffort points are heuristic planning indicators, not person-day commitments.\n",
        encoding="utf-8",
    )

    (output / "ai-executive-briefing.md").write_text(
        executive_briefing(items, rating, score),
        encoding="utf-8",
    )

    (output / "ai-migration-backlog.md").write_text(
        migration_backlog(items),
        encoding="utf-8",
    )

    (output / "ai-workshop-questions.md").write_text(
        workshop_questions(items),
        encoding="utf-8",
    )

    (output / "ai-decision-log.md").write_text(
        decision_log(items),
        encoding="utf-8",
    )

    (output / "ai-data-quality-checks.md").write_text(
        data_quality_checks(items),
        encoding="utf-8",
    )

    (output / "ai-wave-roadmap.md").write_text(
        wave_roadmap(items),
        encoding="utf-8",
    )

    (output / "ai-command-center-dashboard.md").write_text(
        command_center_dashboard(items, rating, score),
        encoding="utf-8",
    )

    (output / "ai-evidence-confidence.md").write_text(
        evidence_confidence_report(items),
        encoding="utf-8",
    )

    (output / "ai-risk-mitigation-playbooks.md").write_text(
        risk_mitigation_playbooks(items),
        encoding="utf-8",
    )

    (output / "ai-data-entity-mapping.md").write_text(
        data_entity_mapping(items),
        encoding="utf-8",
    )

    (output / "ai-quality-gates.md").write_text(
        quality_gates(items, rating),
        encoding="utf-8",
    )

    (output / "ai-upgrade-path-decision.md").write_text(
        upgrade_path_decision(items, rating),
        encoding="utf-8",
    )

    (output / "ai-anti-waste-score.md").write_text(
        anti_waste_score(items),
        encoding="utf-8",
    )

    (output / "ai-before-after-architecture.md").write_text(
        before_after_architecture(items),
        encoding="utf-8",
    )

    (output / "ai-cost-model.md").write_text(
        cost_model_report(items, rating, cost_model),
        encoding="utf-8",
    )

    (output / "ai-standard-feature-matches.md").write_text(
        standard_feature_matches(items, feature_map, d365fo_kb),
        encoding="utf-8",
    )

    (output / "ai-dependency-graph.md").write_text(
        dependency_graph(items),
        encoding="utf-8",
    )

    (output / "dashboard.html").write_text(
        html_dashboard(items, rating, score, cost_model),
        encoding="utf-8",
    )

    (output / "ai-azure-devops-work-items.csv").write_text(
        azure_devops_work_items(items),
        encoding="utf-8",
    )
    (output / "ai-what-if-scenarios.md").write_text(what_if_scenarios(items, rating, cost_model), encoding="utf-8")
    (output / "ai-do-not-migrate-report.md").write_text(do_not_migrate_report(items), encoding="utf-8")
    (output / "ai-risk-heatmap.md").write_text(risk_heatmap(items), encoding="utf-8")
    (output / "ai-value-tracker.md").write_text(value_tracker(items, cost_model), encoding="utf-8")
    (output / "ai-executive-stories.md").write_text(executive_stories(items, rating), encoding="utf-8")
    (output / "ai-adrs.md").write_text(architecture_decision_records(items), encoding="utf-8")
    (output / "migration-knowledge-graph.json").write_text(json.dumps(knowledge_graph(items), indent=2), encoding="utf-8")
    (output / "persona-ceo-summary.md").write_text(persona_ceo_summary(items, rating, score, cost_model), encoding="utf-8")
    (output / "persona-cio-architecture-view.md").write_text(persona_cio_architecture_view(items, rating), encoding="utf-8")
    (output / "persona-ciso-security-view.md").write_text(persona_ciso_security_view(items), encoding="utf-8")
    (output / "persona-project-manager-control-view.md").write_text(persona_pm_control_view(items, rating), encoding="utf-8")
    (output / "persona-team-member-task-view.md").write_text(persona_team_member_task_view(items), encoding="utf-8")
    (output / "steering-committee-pack.md").write_text(steering_committee_pack(items, rating, score, cost_model), encoding="utf-8")
    (output / "raid-log.md").write_text(raid_log(items), encoding="utf-8")
    (output / "raci-matrix.md").write_text(raci_matrix(items), encoding="utf-8")
    (output / "weekly-status-report.md").write_text(weekly_status_report(items, rating), encoding="utf-8")
    (output / "ciso-security-gate-pack.md").write_text(ciso_security_gate_pack(items), encoding="utf-8")
    (output / "project-operating-model.md").write_text(project_operating_model(items), encoding="utf-8")
    (output / "board-ceo-narrative.md").write_text(board_ceo_narrative(items, rating, cost_model), encoding="utf-8")
    (output / "team-execution-pack.md").write_text(team_execution_pack(items), encoding="utf-8")
    (output / "role-based-prompt-library.md").write_text(role_based_prompt_library(), encoding="utf-8")
    (output / "project-onboarding-guide.md").write_text(project_onboarding_guide(items), encoding="utf-8")

    (output / "inventory-normalized.json").write_text(
        json.dumps([item_to_dict(item) for item in items], indent=2),
        encoding="utf-8",
    )


def top_risks(items: list[InventoryItem]) -> str:
    counts: dict[str, int] = {}
    for item in items:
        for flag in item.risk_flags:
            counts[flag] = counts.get(flag, 0) + 1
    if not counts:
        return "No risk flags detected from the provided inventory.\n"
    rows = [[flag, count] for flag, count in sorted(counts.items(), key=lambda pair: pair[1], reverse=True)]
    return md_table(["Risk", "Count"], rows)


def effort_band(points: int) -> str:
    if points >= 60:
        return "High"
    if points >= 25:
        return "Medium"
    return "Low"


def load_json_config(name: str, default: dict[str, Any]) -> dict[str, Any]:
    path = CONFIG_DIR / name
    if not path.exists():
        return default
    loaded = json.loads(path.read_text(encoding="utf-8"))
    merged = dict(default)
    merged.update(loaded)
    return merged


def executive_briefing(items: list[InventoryItem], rating: str, score: int) -> str:
    retire_count = sum(1 for item in items if "Retire" in item.disposition)
    rebuild_count = sum(1 for item in items if item.disposition in ("Rebuild", "ISV Review"))
    integration_count = sum(1 for item in items if item.category == "integration")
    report_count = sum(1 for item in items if item.category == "report")
    rows = [
        ["Complexity", rating],
        ["Complexity score", score],
        ["Inventory items analyzed", len(items)],
        ["Scope reduction candidates", retire_count],
        ["Rebuild / ISV review items", rebuild_count],
        ["Integrations requiring modernization", integration_count],
        ["Reports requiring rationalization", report_count],
    ]
    decisions = [
        ["Migration approach", "Confirm reimplementation, hybrid, or upgrade-led path."],
        ["Scope reduction", "Validate retire candidates with business owners."],
        ["Integration architecture", "Select middleware and D365FO target patterns."],
        ["Data history", "Decide full migration vs archive/reporting history."],
        ["ISV strategy", "Confirm D365FO availability, licensing, and replacement options."],
    ]
    return (
        "# AI Executive Migration Briefing\n\n"
        "## Current Assessment\n\n"
        + md_table(["Topic", "Value"], rows)
        + "\n\n## Steering Decisions Needed\n\n"
        + md_table(["Decision", "Required action"], decisions)
        + "\n\n## Next 30 / 60 / 90 Days\n\n"
        + md_table(
            ["Window", "Focus"],
            [
                ["30 days", "Complete inventory, validate scope reduction, confirm migration approach."],
                ["60 days", "Finalize fit-gap, integration target architecture, data strategy, and ISV decisions."],
                ["90 days", "Start build waves, migration trial planning, test strategy, and cutover rehearsals."],
            ],
        )
        + "\n"
    )


def migration_backlog(items: list[InventoryItem]) -> str:
    rows = []
    for index, item in enumerate(sorted(items, key=lambda value: value.effort_points, reverse=True), start=1):
        rows.append(
            [
                f"BL-{index:03d}",
                backlog_epic(item),
                f"{item.disposition}: {item.name}",
                f"Target pattern agreed: {item.target_pattern}; risks reviewed: {', '.join(item.risk_flags) or 'none'}",
                item.category,
                item.effort_points,
                "High" if item.effort_points >= 9 else "Medium" if item.effort_points >= 5 else "Low",
            ]
        )
    return "# AI Migration Backlog\n\n" + md_table(
        ["ID", "Epic", "Story", "Acceptance criteria", "Workstream", "Effort", "Risk"],
        rows,
    ) + "\n"


def backlog_epic(item: InventoryItem) -> str:
    if item.category == "integration":
        return "Integration modernization"
    if item.category == "report":
        return "Report rationalization"
    if item.category == "security":
        return "Security mapping"
    if item.category == "isv":
        return "ISV strategy"
    if item.category == "data":
        return "Data migration"
    return "Customization migration"


def workshop_questions(items: list[InventoryItem]) -> str:
    rows = []
    for index, item in enumerate(items, start=1):
        rows.append(
            [
                f"Q-{index:03d}",
                item.category,
                question_for(item),
                item.disposition,
                item.name,
            ]
        )
    return "# AI Workshop Questions\n\n" + md_table(
        ["ID", "Workstream", "Question", "Related decision", "Evidence item"],
        rows,
    ) + "\n"


def question_for(item: InventoryItem) -> str:
    if "Retire" in item.disposition:
        return f"Can the business confirm that {item.name} is no longer required in the D365FO target scope?"
    if item.category == "integration":
        return f"What SLA, monitoring, replay, and error-handling requirements apply to {item.name}?"
    if item.category == "report":
        return f"Who consumes {item.name}, how often, and can D365FO standard reporting or Power BI replace it?"
    if item.category == "isv":
        return f"Is there a supported D365FO version or standard replacement for {item.name}?"
    if item.category == "security":
        return f"Which D365FO duties and privileges should replace {item.name}, and are there SoD concerns?"
    if item.category == "data":
        return f"Does {item.name} require full history migration, archive access, or only opening balances/open transactions?"
    return f"What business outcome does {item.name} support, and is that outcome covered by D365FO standard?"


def decision_log(items: list[InventoryItem]) -> str:
    rows = []
    high_value = [item for item in items if item.effort_points >= 8 or "Retire" in item.disposition]
    for index, item in enumerate(high_value, start=1):
        rows.append(
            [
                f"DEC-{index:03d}",
                f"Target disposition for {item.name}",
                item.rationale,
                "Migrate as-is; redesign; replace with standard/ISV; retire",
                item.disposition,
                "Proposed",
            ]
        )
    return "# AI Migration Decision Log\n\n" + md_table(
        ["ID", "Decision", "Context", "Options considered", "Recommendation", "Status"],
        rows,
    ) + "\n"


def data_quality_checks(items: list[InventoryItem]) -> str:
    data_items = [item for item in items if item.category == "data" or item.object_type.lower() == "table"]
    if not data_items:
        data_items = items[:5]
    rows = []
    for item in data_items:
        rows.append(
            [
                item.name,
                "Mandatory fields, duplicates, inactive values, dimensions, orphan references, balances",
                "Before trial migration 1",
                "Data migration lead",
            ]
        )
    return "# AI Data Quality Checks\n\n" + md_table(
        ["Data area", "Checks", "When", "Owner"],
        rows,
    ) + "\n"


def wave_roadmap(items: list[InventoryItem]) -> str:
    wave1 = [item.name for item in items if item.disposition in ("Retire Candidate", "Review", "Map")]
    wave2 = [item.name for item in items if item.disposition in ("Extend", "Standard / Power BI Review")]
    wave3 = [item.name for item in items if item.disposition in ("Rebuild", "ISV Review")]
    rows = [
        ["Wave 0", "Discovery and scope reduction", ", ".join(wave1[:8]) or "Inventory, fit-gap, decisions"],
        ["Wave 1", "Standard/configuration and low-risk extensions", ", ".join(wave2[:8]) or "Configuration and standard replacements"],
        ["Wave 2", "Complex rebuilds, integrations, ISVs", ", ".join(wave3[:8]) or "High-risk technical work"],
        ["Wave 3", "Data migration, testing, cutover", "Trial migrations, UAT, cutover rehearsal, go-live"],
    ]
    return "# AI Migration Wave Roadmap\n\n" + md_table(["Wave", "Purpose", "Candidate scope"], rows) + "\n"


def command_center_dashboard(items: list[InventoryItem], rating: str, score: int) -> str:
    retire = sum(1 for item in items if "Retire" in item.disposition)
    rebuild = sum(1 for item in items if item.disposition in ("Rebuild", "ISV Review"))
    low_confidence = sum(1 for item in items if item.confidence == "Low")
    high_risk = sum(1 for item in items if item.effort_points >= 9)
    return (
        "# AI Migration Command Center Dashboard\n\n"
        + md_table(
            ["KPI", "Value"],
            [
                ["Complexity rating", rating],
                ["Complexity score", score],
                ["Inventory items", len(items)],
                ["Scope reduction candidates", retire],
                ["High-risk items", high_risk],
                ["Rebuild / ISV review items", rebuild],
                ["Low-confidence recommendations", low_confidence],
            ],
        )
        + "\n\n## Go / No-Go View\n\n"
        + md_table(
            ["Gate", "Required evidence", "Exit criteria", "Current status"],
            gate_status_rows(items, rating),
        )
        + "\n"
    )


def evidence_confidence_report(items: list[InventoryItem]) -> str:
    rows = [
        [item.name, item.disposition, item.confidence, item.confidence_reason, missing_evidence(item)]
        for item in items
    ]
    return "# AI Evidence Confidence Score\n\n" + md_table(
        ["Item", "Recommendation", "Confidence", "Reason", "Missing evidence"],
        rows,
    ) + "\n"


def missing_evidence(item: InventoryItem) -> str:
    missing = []
    if not item.usage:
        missing.append("usage")
    if not item.business_purpose:
        missing.append("business purpose")
    if not item.module:
        missing.append("module")
    if not item.complexity:
        missing.append("complexity")
    return ", ".join(missing) or "none"


def risk_mitigation_playbooks(items: list[InventoryItem]) -> str:
    risks = sorted({flag for item in items for flag in item.risk_flags})
    rows = [[risk, mitigation_for(risk), owner_for_risk(risk), "Discovery / Solution design"] for risk in risks]
    return "# AI Risk-to-Mitigation Playbooks\n\n" + md_table(
        ["Risk", "Mitigation playbook", "Owner", "When"],
        rows,
    ) + "\n"


def mitigation_for(risk: str) -> str:
    return {
        "direct-sql": "Replace direct SQL with data entities, custom services, export patterns, or reporting replicas.",
        "aif": "Redesign AIF services using OData, custom services, Business Events, or middleware.",
        "client-dependency": "Remove COM, ActiveX, WinAPI, local file, and client-side dependencies.",
        "overlayering": "Replace overlayered behavior with extensions, Chain of Command, and event handlers.",
        "posting": "Run senior architecture review for financial/inventory posting changes and reconciliation impact.",
        "batch": "Align to SysOperation and D365FO batch operations with monitoring and retry behavior.",
        "report-rationalization": "Validate usage and replace with standard reports, workspaces, Power BI, or archive access.",
        "integration-modernization": "Define SLA, monitoring, replay, authentication, and support ownership.",
    }.get(risk, "Define mitigation during solution design.")


def owner_for_risk(risk: str) -> str:
    if risk in ("direct-sql", "aif", "client-dependency", "overlayering", "batch"):
        return "Technical architect"
    if risk == "posting":
        return "Solution architect / finance lead"
    if risk == "report-rationalization":
        return "Reporting lead"
    return "Workstream lead"


def data_entity_mapping(items: list[InventoryItem]) -> str:
    rows = []
    for item in items:
        if item.category in ("data", "integration") or item.object_type.lower() == "table":
            rows.append(
                [
                    item.name,
                    item.object_type,
                    suggested_data_entity(item),
                    "Validate mandatory fields, dimensions, references, and legal entity handling.",
                    "Record count, balance/quantity check, exception report",
                ]
            )
    return "# AI Data Entity Mapping\n\n" + md_table(
        ["AX source", "Source type", "D365FO target candidate", "Transformation notes", "Reconciliation"],
        rows,
    ) + "\n"


def standard_feature_matches(items: list[InventoryItem], feature_map: dict[str, Any], d365fo_kb: dict[str, Any] | None = None) -> str:
    rows = []
    for item in items:
        text = " ".join([item.name, item.module, item.business_purpose]).lower()
        matches = [str(value) for key, value in feature_map.items() if key.lower() in text]
        kb_matches = []
        for section in (d365fo_kb or {}).values():
            if isinstance(section, dict):
                for key, values in section.items():
                    if key.lower() in text:
                        kb_matches.extend(values if isinstance(values, list) else [values])
        matches.extend(str(value) for value in kb_matches)
        rows.append(
            [
                item.name,
                item.category,
                "; ".join(matches[:3]) or "No confident standard match from local map",
                "Medium" if matches else "Low",
                "Validate in fit-gap workshop",
            ]
        )
    return "# AI D365FO Standard Feature Matches\n\n" + md_table(
        ["AX item", "Category", "D365FO standard candidate", "Fit confidence", "Next validation"],
        rows,
    ) + "\n"


def suggested_data_entity(item: InventoryItem) -> str:
    text = " ".join([item.name, item.module, item.business_purpose]).lower()
    if "cust" in text or "customer" in text:
        return "Customer-related data entity review"
    if "vend" in text or "vendor" in text:
        return "Vendor-related data entity review"
    if "invent" in text or "warehouse" in text:
        return "Inventory / warehouse data entity review"
    if "ledger" in text or "finance" in text:
        return "Financial data entity review"
    if "sales" in text:
        return "Sales order / customer transaction entity review"
    return "Data management entity mapping required"


def quality_gates(items: list[InventoryItem], rating: str) -> str:
    return "# AI Migration Quality Gates\n\n" + md_table(
        ["Gate", "Required evidence", "Exit criteria", "Current status"],
        gate_status_rows(items, rating),
    ) + "\n"


def gate_status_rows(items: list[InventoryItem], rating: str) -> list[list[str]]:
    low_conf = sum(1 for item in items if item.confidence == "Low")
    high_risk = sum(1 for item in items if item.effort_points >= 9)
    return [
        ["Readiness Gate", "Inventory, scope, risks", "No critical unknowns", "At risk" if low_conf else "On track"],
        ["Design Gate", "Fit-gap, target architecture, decisions", "High-risk designs approved", "At risk" if high_risk else "On track"],
        ["Build Gate", "Backlog, estimates, dependencies", "Build scope baselined", "Proposed"],
        ["Data Gate", "Mappings, quality checks, reconciliation", "Trial migration criteria approved", "Proposed"],
        ["UAT Gate", "Test cases, roles, data, defects", "Business acceptance criteria approved", "Proposed"],
        ["Cutover Gate", "Runbook, rollback, smoke tests", "Go/no-go criteria met", "At risk" if rating in ("High", "Critical") else "Proposed"],
    ]


def upgrade_path_decision(items: list[InventoryItem], rating: str) -> str:
    rebuild = sum(1 for item in items if item.disposition in ("Rebuild", "ISV Review"))
    retire = sum(1 for item in items if "Retire" in item.disposition)
    recommendation = "Hybrid or reimplementation-led approach"
    if rating in ("Low", "Medium") and rebuild <= 2:
        recommendation = "Evaluate upgrade-led or hybrid approach"
    if rating in ("High", "Critical") or rebuild >= 5:
        recommendation = "Reimplementation-led approach with aggressive scope reduction"
    rows = [
        ["Complexity rating", rating],
        ["Rebuild / ISV review count", rebuild],
        ["Scope reduction candidates", retire],
        ["Recommended approach", recommendation],
        ["Required validation", "Confirm source AX version, Microsoft-supported tooling, data volume, and customization inventory."],
    ]
    return "# AI Upgrade Path Decision\n\n" + md_table(["Factor", "Assessment"], rows) + "\n"


def anti_waste_score(items: list[InventoryItem]) -> str:
    waste_points = 0
    rows = []
    for item in items:
        reason = ""
        points = 0
        if "Retire" in item.disposition:
            points += 5
            reason = "Retire candidate"
        if item.category == "report":
            points += 2
            reason = append_reason(reason, "report rationalization")
        if item.category == "data" and "history" in " ".join(str(value) for value in item.raw.values()).lower():
            points += 3
            reason = append_reason(reason, "history migration review")
        if item.category == "isv":
            points += 3
            reason = append_reason(reason, "ISV replacement review")
        if points:
            waste_points += points
            rows.append([item.name, points, reason, item.disposition])
    band = "High" if waste_points >= 25 else "Medium" if waste_points >= 10 else "Low"
    return (
        "# AI Migration Anti-Waste Score\n\n"
        + md_table([ "Metric", "Value" ], [["Anti-waste score", waste_points], ["Opportunity band", band]])
        + "\n\n## Opportunity Items\n\n"
        + md_table(["Item", "Points", "Reason", "Recommendation"], rows)
        + "\n"
    )


def append_reason(existing: str, value: str) -> str:
    return f"{existing}, {value}" if existing else value


def before_after_architecture(items: list[InventoryItem]) -> str:
    integrations = [item.name for item in items if item.category == "integration"]
    reports = [item.name for item in items if item.category == "report"]
    data = [item.name for item in items if item.category == "data"]
    rows = [
        ["Application", "Dynamics AX legacy environment", "Dynamics 365 Finance & Operations cloud environment"],
        ["Integrations", ", ".join(integrations) or "Legacy integrations not inventoried", "OData, custom services, Business Events, middleware, managed files"],
        ["Reporting", ", ".join(reports) or "Legacy reports not inventoried", "D365FO workspaces, SSRS, Power BI, Financial Reporter, archive"],
        ["Data", ", ".join(data) or "Legacy data domains not inventoried", "Data entities, recurring data jobs, archive/reporting store"],
        ["Security", "AX groups/roles", "D365FO roles, duties, privileges, SoD controls"],
        ["ALM", "Layer/model deployment", "Packages, build validation, release pipeline, environment governance"],
    ]
    return "# AI Before / After Architecture\n\n" + md_table(["Domain", "Before AX", "After D365FO"], rows) + "\n"


def azure_devops_work_items(items: list[InventoryItem]) -> str:
    lines = ["Work Item Type,Title,Description,Tags,Effort,Risk"]
    for item in sorted(items, key=lambda value: value.effort_points, reverse=True):
        title = f"{item.disposition}: {item.name}".replace('"', "'")
        desc = f"{item.rationale} Target: {item.target_pattern}".replace('"', "'")
        tags = f"AXMigration;{item.category};{';'.join(item.risk_flags)}".replace('"', "'")
        risk = "High" if item.effort_points >= 9 else "Medium" if item.effort_points >= 5 else "Low"
        lines.append(f'User Story,"{title}","{desc}","{tags}",{item.effort_points},{risk}')
    return "\n".join(lines) + "\n"


def what_if_scenarios(items: list[InventoryItem], rating: str, model: dict[str, Any]) -> str:
    points = sum(item.effort_points for item in items)
    retire_points = sum(item.effort_points for item in items if "Retire" in item.disposition)
    scenarios = [
        ["Baseline", points, rating, "Current analyzed scope"],
        ["Scope reducer", max(points - retire_points, 0), "Lower", "Retire candidates removed after validation"],
        ["Report rationalization", max(points - sum(i.effort_points for i in items if i.category == "report") // 2, 0), "Lower", "Half of reports replaced/retired"],
        ["Archive history", max(points - sum(i.effort_points for i in items if i.category == "data") // 2, 0), "Lower", "History archived instead of fully migrated"],
        ["Rebuild everything", points + sum(i.effort_points for i in items if i.disposition != "Retire"), "Higher", "No scope reduction accepted"],
    ]
    return "# AI What-if Simulator\n\n" + md_table(["Scenario", "Effort points", "Risk direction", "Assumption"], scenarios) + "\n"


def do_not_migrate_report(items: list[InventoryItem]) -> str:
    rows = []
    for item in items:
        if "Retire" in item.disposition or item.category == "report" or (item.category == "data" and "history" in " ".join(str(v) for v in item.raw.values()).lower()):
            rows.append([item.name, item.disposition, item.rationale, f"Can {item.name} be retired, replaced, or archived?", "Higher cost and test scope if migrated"])
    return "# AI Do Not Migrate Report\n\n" + md_table(["Item", "Recommendation", "Reason", "Validation question", "Risk if migrated"], rows) + "\n"


def risk_heatmap(items: list[InventoryItem]) -> str:
    rows = []
    for item in sorted(items, key=lambda value: value.effort_points, reverse=True):
        impact = "High" if item.effort_points >= 9 else "Medium" if item.effort_points >= 5 else "Low"
        probability = "High" if len(item.risk_flags) >= 2 else "Medium" if item.risk_flags else "Low"
        rows.append([item.name, item.category, impact, probability, ", ".join(item.risk_flags) or "none"])
    return "# AI Migration Risk Heatmap\n\n" + md_table(["Item", "Workstream", "Impact", "Probability", "Risk drivers"], rows) + "\n"


def value_tracker(items: list[InventoryItem], model: dict[str, Any]) -> str:
    hours_per_point = float(model.get("hours_per_effort_point", 6))
    hours_per_day = float(model.get("hours_per_day", 8))
    rate = float(model.get("blended_day_rate", 950))
    rows = []
    for item in items:
        if "Retire" in item.disposition or item.category in ("report", "isv"):
            days = item.effort_points * hours_per_point / hours_per_day
            rows.append([item.name, item.disposition, item.effort_points, round(days, 1), round(days * rate)])
    return "# AI Migration Value Tracker\n\n" + md_table(["Item", "Value lever", "Avoidable points", "Avoidable days", "Indicative value"], rows) + "\n"


def executive_stories(items: list[InventoryItem], rating: str) -> str:
    retire = sum(1 for item in items if "Retire" in item.disposition)
    risks = sum(len(item.risk_flags) for item in items)
    return f"""# AI Executive Story Generator

## CFO Story

Migration complexity is **{rating}**. The current evidence shows **{retire}** scope-reduction candidates and **{risks}** risk flags. The financial story is cost avoidance through retiring low-value customizations, rationalizing reports, and avoiding unnecessary history migration.

## CIO Story

The technical story is legacy debt reduction: remove direct SQL, AIF, overlayering, client dependencies, and unsupported posting customizations before they become cloud operating risks.

## COO Story

The operating story is process standardization: use D365FO standard capabilities where possible and reserve custom build for true business differentiation.

## Program Manager Story

The delivery story is staged control: baseline scope, validate retire candidates, sequence high-risk rebuilds, and use quality gates before UAT and cutover.
"""


def architecture_decision_records(items: list[InventoryItem]) -> str:
    rows = []
    for index, item in enumerate([i for i in items if i.effort_points >= 8 or "Retire" in i.disposition], start=1):
        rows.append([f"ADR-{index:03d}", f"Disposition for {item.name}", item.rationale, item.disposition, "Proposed"])
    return "# Architecture Decision Records\n\n" + md_table(["ID", "Decision", "Context", "Decision", "Status"], rows) + "\n"


def knowledge_graph(items: list[InventoryItem]) -> dict[str, Any]:
    nodes = []
    edges = []
    for item in items:
        item_id = graph_id(item.name)
        nodes.append({"id": item_id, "label": item.name, "type": item.category})
        if item.module:
            module_id = graph_id("module-" + item.module)
            nodes.append({"id": module_id, "label": item.module, "type": "process"})
            edges.append({"from": module_id, "to": item_id, "type": "contains"})
        for risk in item.risk_flags:
            risk_id = graph_id("risk-" + risk)
            nodes.append({"id": risk_id, "label": risk, "type": "risk"})
            edges.append({"from": item_id, "to": risk_id, "type": "has_risk"})
    unique_nodes = {node["id"]: node for node in nodes}
    return {"nodes": list(unique_nodes.values()), "edges": edges}


def migration_metrics(items: list[InventoryItem], rating: str, model: dict[str, Any]) -> dict[str, Any]:
    points = sum(item.effort_points for item in items)
    retire = sum(1 for item in items if "Retire" in item.disposition)
    high_risk = sum(1 for item in items if item.effort_points >= 9)
    risks = sum(len(item.risk_flags) for item in items)
    days = points * float(model.get("hours_per_effort_point", 6)) / float(model.get("hours_per_day", 8))
    return {"points": points, "retire": retire, "high_risk": high_risk, "risks": risks, "days": round(days, 1), "rating": rating}


def persona_ceo_summary(items: list[InventoryItem], rating: str, score: int, model: dict[str, Any]) -> str:
    metrics = migration_metrics(items, rating, model)
    return f"""# CEO Migration Summary

## Executive Position

The migration currently rates **{rating}** with a complexity score of **{score}**. The AI analysis identified **{metrics['retire']}** scope-reduction candidates, **{metrics['high_risk']}** high-risk items, and **{metrics['risks']}** risk flags.

## CEO Decisions Needed

{md_table(["Decision", "Why it matters"], [
    ["Approve scope-reduction mandate", "Avoid migrating low-value customizations, reports, and historical data."],
    ["Confirm business standardization appetite", "D365FO value depends on process simplification, not legacy recreation."],
    ["Assign executive owners for unresolved high-risk items", "Risk decisions need accountable business leadership."],
    ["Confirm investment envelope", "Current heuristic effort is " + str(metrics["days"]) + " person-days before detailed planning."]
])}

## Board-Level Message

The migration should be governed as a business simplification and risk-reduction program, not only as an ERP technical move.
"""


def persona_cio_architecture_view(items: list[InventoryItem], rating: str) -> str:
    rows = []
    for item in sorted(items, key=lambda value: value.effort_points, reverse=True):
        if item.category in ("integration", "data", "report", "object", "isv"):
            rows.append([item.name, item.category, item.target_pattern, ", ".join(item.risk_flags) or "none", item.effort_points])
    return "# CIO Architecture View\n\n" + md_table(
        ["Item", "Domain", "Target pattern", "Architecture risk", "Effort"],
        rows,
    ) + "\n\n## CIO Focus\n\n- Remove unsupported legacy integration patterns.\n- Reduce technical debt before cloud migration.\n- Sequence high-risk rebuilds through architecture gates.\n"


def persona_ciso_security_view(items: list[InventoryItem]) -> str:
    security_items = [item for item in items if item.category == "security" or any(flag in item.risk_flags for flag in ("direct-sql", "client-dependency", "aif"))]
    rows = [[item.name, item.category, ", ".join(item.risk_flags) or "security mapping", security_control_for(item), "CISO / security lead"] for item in security_items]
    return "# CISO Security View\n\n" + md_table(["Item", "Area", "Risk", "Control / review", "Owner"], rows) + "\n"


def security_control_for(item: InventoryItem) -> str:
    if "direct-sql" in item.risk_flags:
        return "Replace direct data access with governed service/entity pattern."
    if "client-dependency" in item.risk_flags:
        return "Remove local/client dependency and review endpoint/security model."
    if "aif" in item.risk_flags:
        return "Review authentication, replay, monitoring, and least privilege for new integration."
    return "Map roles, duties, privileges, and SoD controls."


def persona_pm_control_view(items: list[InventoryItem], rating: str) -> str:
    rows = [
        ["Complexity", rating, "Program Manager", "Track weekly"],
        ["High-risk items", sum(1 for item in items if item.effort_points >= 9), "Workstream leads", "Escalate blockers"],
        ["Open decisions", sum(1 for item in items if item.effort_points >= 8 or "Retire" in item.disposition), "Steering committee", "Decision log"],
        ["Scope reduction candidates", sum(1 for item in items if "Retire" in item.disposition), "Business owners", "Validate in workshops"],
    ]
    return "# Project Manager Control View\n\n" + md_table(["Control", "Value", "Owner", "Action"], rows) + "\n"


def persona_team_member_task_view(items: list[InventoryItem]) -> str:
    rows = []
    for index, item in enumerate(sorted(items, key=lambda value: value.effort_points, reverse=True), start=1):
        rows.append([f"T-{index:03d}", task_for_item(item), item.category, suggested_owner(item), "New"])
    return "# Team Member Task View\n\n" + md_table(["ID", "Task", "Workstream", "Suggested owner", "Status"], rows) + "\n"


def task_for_item(item: InventoryItem) -> str:
    if "Retire" in item.disposition:
        return f"Validate retirement decision for {item.name}."
    if item.category == "integration":
        return f"Document target integration design for {item.name}."
    if item.category == "report":
        return f"Validate usage and target reporting pattern for {item.name}."
    if item.category == "security":
        return f"Map security role/duties for {item.name}."
    return f"Review migration disposition and target pattern for {item.name}."


def suggested_owner(item: InventoryItem) -> str:
    return {
        "integration": "Integration lead",
        "report": "Reporting lead",
        "security": "Security lead",
        "data": "Data migration lead",
        "isv": "Solution architect",
    }.get(item.category, "Functional / technical lead")


def steering_committee_pack(items: list[InventoryItem], rating: str, score: int, model: dict[str, Any]) -> str:
    metrics = migration_metrics(items, rating, model)
    decisions = [[f"DEC-{idx:03d}", f"Approve {item.disposition} for {item.name}", suggested_owner(item), "Next steering"] for idx, item in enumerate(items, start=1) if item.effort_points >= 8 or "Retire" in item.disposition]
    return "# Steering Committee Pack\n\n" + md_table(
        ["Metric", "Value"],
        [["Complexity", rating], ["Score", score], ["High-risk items", metrics["high_risk"]], ["Scope reduction candidates", metrics["retire"]], ["Effort points", metrics["points"]]],
    ) + "\n\n## Decisions Needed\n\n" + md_table(["ID", "Decision", "Owner", "Due"], decisions) + "\n"


def raid_log(items: list[InventoryItem]) -> str:
    rows = []
    for index, item in enumerate(items, start=1):
        if item.risk_flags:
            rows.append([f"R-{index:03d}", "Risk", item.name, ", ".join(item.risk_flags), suggested_owner(item), "Open"])
        if item.effort_points >= 8:
            rows.append([f"D-{index:03d}", "Dependency", item.name, "Requires architecture/business decision", suggested_owner(item), "Open"])
    return "# RAID Log\n\n" + md_table(["ID", "Type", "Item", "Description", "Owner", "Status"], rows) + "\n"


def raci_matrix(items: list[InventoryItem]) -> str:
    workstreams = sorted({item.category for item in items})
    rows = [[ws.title(), suggested_owner(InventoryItem(source_file="", raw={}, category=ws)), "Solution architect", "Business owner", "Program manager"] for ws in workstreams]
    return "# RACI Matrix\n\n" + md_table(["Workstream", "Responsible", "Accountable", "Consulted", "Informed"], rows) + "\n"


def weekly_status_report(items: list[InventoryItem], rating: str) -> str:
    return "# Weekly Status Report\n\n" + md_table(
        ["Area", "Status", "Comment"],
        [
            ["Overall", "Amber" if rating in ("Medium", "High") else "Red" if rating == "Critical" else "Green", f"Complexity is {rating}."],
            ["Scope", "Amber", f"{sum(1 for item in items if 'Retire' in item.disposition)} scope-reduction candidates need validation."],
            ["Risks", "Amber", f"{sum(len(item.risk_flags) for item in items)} risk flags detected."],
            ["Decisions", "Amber", "High-effort and retire decisions require owner confirmation."],
        ],
    ) + "\n"


def ciso_security_gate_pack(items: list[InventoryItem]) -> str:
    rows = [
        ["Identity and access", "Roles/duties mapped", "Required before UAT", "Open"],
        ["SoD", "Segregation of duties reviewed", "Required before UAT", "Open"],
        ["Integrations", "Auth, secrets, monitoring, replay reviewed", "Required before SIT", "Open"],
        ["Sensitive data", "GDPR/DSGVO and retention reviewed", "Required before data migration trial", "Open"],
        ["Go-live", "Privileged access and emergency access reviewed", "Required before cutover", "Open"],
    ]
    return "# CISO Security Gate Pack\n\n" + md_table(["Gate", "Evidence", "Timing", "Status"], rows) + "\n\n## Security Items\n\n" + persona_ciso_security_view(items)


def project_operating_model(items: list[InventoryItem]) -> str:
    return "# Project Operating Model\n\n" + md_table(
        ["Area", "Recommendation"],
        [
            ["Governance", "Weekly delivery review and bi-weekly steering committee."],
            ["Decision rights", "Business owns scope decisions; architecture owns technical patterns; CISO owns security gates."],
            ["Escalation", "Escalate high-risk blockers within 48 hours."],
            ["Cadence", "Daily workstream standups during build/test/cutover windows."],
            ["Artifacts", "Maintain RAID, RACI, decision log, backlog, cutover runbook, and test dashboard."],
        ],
    ) + "\n"


def board_ceo_narrative(items: list[InventoryItem], rating: str, model: dict[str, Any]) -> str:
    metrics = migration_metrics(items, rating, model)
    return f"""# Board / CEO Narrative

## Why Migrate

The AX estate carries technical and operational risk that increases cost, slows change, and limits supportability.

## Why Now

D365FO migration is an opportunity to retire low-value scope, standardize processes, modernize integrations, and improve security governance.

## Risk of Doing Nothing

Legacy customizations, direct integrations, aging reports, and unclear data history requirements will continue to increase operational risk.

## Investment Logic

The current AI scan estimates **{metrics['points']} effort points** and highlights **{metrics['retire']} scope-reduction opportunities**. The recommended path is controlled scope reduction before build commitment.
"""


def team_execution_pack(items: list[InventoryItem]) -> str:
    return "# Team Execution Pack\n\n## Daily Task List\n\n" + persona_team_member_task_view(items) + "\n## Defect Triage Template\n\n" + md_table(
        ["Defect", "Severity", "Owner", "Root cause", "Next action"],
        [["", "Sev 1 / Sev 2 / Sev 3", "", "", ""]],
    ) + "\n"


def role_based_prompt_library() -> str:
    return """# Role-Based Prompt Library

## CEO

Act as a CEO reviewing this AX to D365FO migration. Summarize business value, risk of delay, investment logic, and top decisions needed.

## CIO

Act as a CIO reviewing this migration architecture. Identify technical debt, supportability risks, integration modernization needs, and architecture decisions.

## CISO

Act as a CISO reviewing this migration. Identify identity, access, SoD, integration security, sensitive data, retention, and go-live security gate risks.

## Project Manager

Act as the program manager. Generate RAID, weekly status, dependencies, milestones, blockers, and steering committee decisions.

## Project Team Member

Act as a workstream team member. Convert the analysis into daily tasks, workshop questions, test scripts, and defect triage actions.
"""


def project_onboarding_guide(items: list[InventoryItem]) -> str:
    return "# Project Onboarding Guide\n\n" + md_table(
        ["Topic", "What new team members need to know"],
        [
            ["Mission", "Reduce AX migration scope while preserving business-critical capability."],
            ["Evidence", "Use inventory, reports, telemetry, and workshop validation."],
            ["Workflow", "Analyze, validate, decide, design, build, test, cutover, stabilize."],
            ["Key files", "Dashboard, RAID, decision log, backlog, security gate, cutover plan."],
            ["First task", "Review persona-team-member-task-view.md and assigned workstream reports."],
        ],
    ) + "\n"


def cost_model_report(items: list[InventoryItem], rating: str, model: dict[str, Any]) -> str:
    total_points = sum(item.effort_points for item in items)
    hours_per_point = float(model.get("hours_per_effort_point", 6))
    hours_per_day = float(model.get("hours_per_day", 8))
    day_rate = float(model.get("blended_day_rate", 950))
    risk_multiplier = float(model.get("risk_multiplier", {}).get(rating, 1.15))
    base_days = total_points * hours_per_point / hours_per_day
    adjusted_days = base_days * risk_multiplier
    low_budget = adjusted_days * day_rate * 0.85
    high_budget = adjusted_days * day_rate * 1.25
    rows = [
        ["Effort points", round(total_points, 2)],
        ["Base person-days", round(base_days, 1)],
        ["Risk multiplier", risk_multiplier],
        ["Adjusted person-days", round(adjusted_days, 1)],
        ["Budget range", f"{round(low_budget):,} - {round(high_budget):,}"],
    ]
    return "# AI Migration Cost Model\n\n" + md_table(["Metric", "Value"], rows) + "\n"


def dependency_graph(items: list[InventoryItem]) -> str:
    lines = ["# AI Migration Dependency Graph\n", "```mermaid", "graph TD"]
    for item in items:
        node = graph_id(item.name)
        lines.append(f'  {node}["{escape_mermaid(item.name)}"]')
        if item.module:
            module = graph_id("module-" + item.module)
            lines.append(f'  {module}["{escape_mermaid(item.module)}"] --> {node}')
        for risk in item.risk_flags:
            risk_node = graph_id("risk-" + risk)
            lines.append(f'  {node} --> {risk_node}["Risk: {escape_mermaid(risk)}"]')
        if item.category in ("integration", "report", "data"):
            gate = graph_id("gate-" + item.category)
            lines.append(f'  {node} --> {gate}["{item.category.title()} workstream"]')
    lines.append("```")
    return "\n".join(lines) + "\n"


def graph_id(value: str) -> str:
    cleaned = re.sub(r"[^A-Za-z0-9_]", "_", value)
    return "N_" + cleaned[:60]


def escape_mermaid(value: str) -> str:
    return value.replace('"', "'")


def html_dashboard(items: list[InventoryItem], rating: str, score: int, model: dict[str, Any]) -> str:
    retire = sum(1 for item in items if "Retire" in item.disposition)
    high_risk = sum(1 for item in items if item.effort_points >= 9)
    total_points = sum(item.effort_points for item in items)
    cards = [
        ("Complexity", rating),
        ("Score", str(score)),
        ("Items", str(len(items))),
        ("Retire Candidates", str(retire)),
        ("High Risk", str(high_risk)),
        ("Effort Points", str(total_points)),
    ]
    rows = "\n".join(
        f"<tr><td>{html.escape(item.name)}</td><td>{html.escape(item.category)}</td><td>{html.escape(item.disposition)}</td><td>{item.effort_points}</td><td>{html.escape(', '.join(item.risk_flags))}</td></tr>"
        for item in sorted(items, key=lambda value: value.effort_points, reverse=True)
    )
    card_html = "\n".join(f'<section class="card"><span>{label}</span><strong>{value}</strong></section>' for label, value in cards)
    options = "\n".join(
        f'<option value="{html.escape(value)}">{html.escape(value.title())}</option>'
        for value in sorted({item.category for item in items})
    )
    return f"""<!doctype html>
<html lang="en">
<head>
  <meta charset="utf-8">
  <title>AX to D365FO Migration Command Center</title>
  <style>
    body {{ font-family: Segoe UI, Arial, sans-serif; margin: 0; background: #f6f8fb; color: #172033; }}
    header {{ background: #0078d4; color: white; padding: 28px 36px; }}
    main {{ padding: 28px 36px; }}
    .grid {{ display: grid; grid-template-columns: repeat(auto-fit, minmax(160px, 1fr)); gap: 14px; margin-bottom: 28px; }}
    .card {{ background: white; border: 1px solid #d9e2ec; border-radius: 8px; padding: 16px; }}
    .card span {{ display: block; color: #526173; font-size: 13px; }}
    .card strong {{ display: block; font-size: 28px; margin-top: 8px; }}
    table {{ width: 100%; border-collapse: collapse; background: white; border: 1px solid #d9e2ec; }}
    th, td {{ text-align: left; padding: 10px 12px; border-bottom: 1px solid #edf1f5; }}
    th {{ background: #eef5fb; }}
    .toolbar {{ display: flex; gap: 12px; margin: 0 0 18px; }}
    input, select {{ padding: 9px 10px; border: 1px solid #b8c5d1; border-radius: 6px; }}
  </style>
</head>
<body>
  <header><h1>AX to D365FO Migration Command Center</h1><p>Generated from AX inventory evidence.</p></header>
  <main>
    <div class="grid">{card_html}</div>
    <h2>Disposition and Risk</h2>
    <div class="toolbar">
      <input id="search" placeholder="Search items, risks, disposition" oninput="filterRows()">
      <select id="category" onchange="filterRows()"><option value="">All categories</option>{options}</select>
    </div>
    <table id="items"><thead><tr><th>Item</th><th>Category</th><th>Disposition</th><th>Effort</th><th>Risks</th></tr></thead><tbody>{rows}</tbody></table>
  </main>
  <script>
    function filterRows() {{
      const q = document.getElementById('search').value.toLowerCase();
      const c = document.getElementById('category').value.toLowerCase();
      document.querySelectorAll('#items tbody tr').forEach(row => {{
        const text = row.innerText.toLowerCase();
        const category = row.children[1].innerText.toLowerCase();
        row.style.display = text.includes(q) && (!c || category === c) ? '' : 'none';
      }});
    }}
    document.querySelectorAll('th').forEach((th, index) => th.onclick = () => {{
      const tbody = document.querySelector('#items tbody');
      [...tbody.rows].sort((a, b) => a.children[index].innerText.localeCompare(b.children[index].innerText, undefined, {{numeric: true}})).forEach(row => tbody.appendChild(row));
    }});
  </script>
</body>
</html>
"""


def item_to_dict(item: InventoryItem) -> dict[str, Any]:
    return {
        "source_file": item.source_file,
        "category": item.category,
        "object_type": item.object_type,
        "name": item.name,
        "layer": item.layer,
        "module": item.module,
        "usage": item.usage,
        "complexity": item.complexity,
        "technology": item.technology,
        "business_purpose": item.business_purpose,
        "risk_flags": item.risk_flags,
        "disposition": item.disposition,
        "target_pattern": item.target_pattern,
        "effort_points": item.effort_points,
        "confidence": item.confidence,
        "confidence_reason": item.confidence_reason,
        "rationale": item.rationale,
    }


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("inputs", nargs="+", help="CSV or JSON AX inventory files.")
    parser.add_argument(
        "--output",
        default="migration-analysis",
        help="Output directory for generated reports. Default: migration-analysis",
    )
    args = parser.parse_args()

    items: list[InventoryItem] = []
    for input_name in args.inputs:
        path = Path(input_name)
        for row in load_rows(path):
            items.append(to_item(path, row))

    write_reports(items, Path(args.output))
    print(f"Analyzed {len(items)} inventory items into {Path(args.output).resolve()}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
