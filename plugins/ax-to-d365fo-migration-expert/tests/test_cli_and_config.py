import json
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
REPO = ROOT.parents[1]
CLI = REPO / "axmigrate.py"


class CliAndConfigTests(unittest.TestCase):
    def test_doctor_runs(self):
        result = subprocess.run([sys.executable, str(CLI), "doctor"], cwd=REPO, text=True, capture_output=True)
        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertIn("Python:", result.stdout)
        self.assertIn("Plugin root:", result.stdout)

    def test_examples_runs(self):
        result = subprocess.run([sys.executable, str(CLI), "examples"], cwd=REPO, text=True, capture_output=True)
        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertIn("Analyze sample inventory", result.stdout)

    def test_config_files_are_json(self):
        for path in (ROOT / "config").glob("*.json"):
            with self.subTest(path=path.name):
                json.loads(path.read_text(encoding="utf-8"))

    def test_root_cli_analyze_generates_dashboard(self):
        with tempfile.TemporaryDirectory() as tmp:
            result = subprocess.run(
                [
                    sys.executable,
                    str(CLI),
                    "analyze",
                    str(ROOT / "examples" / "sample-ax-inventory.csv"),
                    "--output",
                    tmp,
                ],
                cwd=REPO,
                text=True,
                capture_output=True,
            )
            self.assertEqual(result.returncode, 0, result.stderr)
            self.assertTrue((Path(tmp) / "dashboard.html").exists())

    def test_wizard_generates_plan(self):
        with tempfile.TemporaryDirectory() as tmp:
            result = subprocess.run(
                [
                    sys.executable,
                    str(CLI),
                    "wizard",
                    "--profile",
                    "commerce",
                    "--project",
                    "Validation Commerce",
                    "--output",
                    tmp,
                ],
                cwd=REPO,
                text=True,
                capture_output=True,
            )
            self.assertEqual(result.returncode, 0, result.stderr)
            self.assertTrue((Path(tmp) / "wizard-plan.md").exists())
            self.assertIn("commerce-pack", (Path(tmp) / "wizard-plan.md").read_text(encoding="utf-8"))
