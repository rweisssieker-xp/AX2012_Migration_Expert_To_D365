import csv
import importlib.util
import sys
import tempfile
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SCRIPT = ROOT / "scripts" / "analyze_ax_inventory.py"


spec = importlib.util.spec_from_file_location("analyze_ax_inventory", SCRIPT)
analyzer = importlib.util.module_from_spec(spec)
assert spec.loader is not None
sys.modules[spec.name] = analyzer
spec.loader.exec_module(analyzer)


class AnalyzerTests(unittest.TestCase):
    def test_csv_inventory_generates_expected_reports(self):
        with tempfile.TemporaryDirectory() as tmp:
            output = Path(tmp)
            items = []
            for row in analyzer.load_rows(ROOT / "examples" / "sample-ax-inventory.csv"):
                items.append(analyzer.to_item(ROOT / "examples" / "sample-ax-inventory.csv", row))

            analyzer.write_reports(items, output)

            self.assertTrue((output / "ai-command-center-dashboard.md").exists())
            self.assertTrue((output / "dashboard.html").exists())
            self.assertTrue((output / "ai-cost-model.md").exists())
            self.assertTrue((output / "ai-azure-devops-work-items.csv").exists())
            self.assertTrue((output / "persona-ceo-summary.md").exists())
            self.assertTrue((output / "persona-ciso-security-view.md").exists())
            self.assertTrue((output / "steering-committee-pack.md").exists())
            self.assertTrue((output / "team-execution-pack.md").exists())
            self.assertEqual(len(list(output.iterdir())), 46)

    def test_xpp_pattern_detection_flags_direct_sql_and_posting(self):
        rows = analyzer.load_rows(ROOT / "examples" / "sample-xpp-class.xpp")
        item = analyzer.to_item(ROOT / "examples" / "sample-xpp-class.xpp", rows[0])

        self.assertIn("direct-sql", item.risk_flags)
        self.assertIn("posting", item.risk_flags)
        self.assertEqual(item.complexity, "High")

    def test_azure_devops_csv_is_valid_csv(self):
        rows = analyzer.load_rows(ROOT / "examples" / "sample-ax-inventory.csv")
        items = [analyzer.to_item(ROOT / "examples" / "sample-ax-inventory.csv", row) for row in rows]
        text = analyzer.azure_devops_work_items(items)
        parsed = list(csv.reader(text.splitlines()))

        self.assertEqual(parsed[0], ["Work Item Type", "Title", "Description", "Tags", "Effort", "Risk"])
        self.assertEqual(len(parsed), len(items) + 1)
