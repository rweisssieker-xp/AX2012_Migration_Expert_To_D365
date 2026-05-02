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

    def test_usp_pack_generates_catalog(self):
        with tempfile.TemporaryDirectory() as tmp:
            result = subprocess.run(
                [
                    sys.executable,
                    str(CLI),
                    "usp-pack",
                    str(ROOT / "examples" / "sample-ax-inventory.csv"),
                    "--project",
                    "USP Test",
                    "--output",
                    tmp,
                ],
                cwd=REPO,
                text=True,
                capture_output=True,
            )
            self.assertEqual(result.returncode, 0, result.stderr)
            self.assertTrue((Path(tmp) / "ai-ki-usp-pack.md").exists())
            self.assertTrue((Path(tmp) / "ai-ki-usp-catalog.json").exists())
            self.assertIn("Autonomous Migration PMO", (Path(tmp) / "ai-ki-usp-pack.md").read_text(encoding="utf-8"))

    def test_router_gates_memory_security_and_ui_commands(self):
        with tempfile.TemporaryDirectory() as tmp:
            tmp_path = Path(tmp)
            analysis = tmp_path / "analysis"
            analyze = subprocess.run(
                [sys.executable, str(CLI), "analyze", str(ROOT / "examples" / "sample-ax-inventory.csv"), "--output", str(analysis)],
                cwd=REPO,
                text=True,
                capture_output=True,
            )
            self.assertEqual(analyze.returncode, 0, analyze.stderr)
            commands = [
                ([sys.executable, str(CLI), "orchestrate", str(analysis), "--output", str(tmp_path / "orchestration")], tmp_path / "orchestration" / "skill-routing.json"),
                ([sys.executable, str(CLI), "evidence-gates", str(analysis), "--ciso-approval", "yes", "--cutover-rehearsal", "yes", "--finance-reconciliation", "yes", "--uat-signoff", "yes", "--rollback-plan", "yes", "--output", str(tmp_path / "gates")], tmp_path / "gates" / "go-live-gate-result.json"),
                ([sys.executable, str(CLI), "memory-store", str(analysis), "--project", "Unit Test", "--output", str(tmp_path / "memory")], tmp_path / "memory" / "migration-memory.sqlite"),
                ([sys.executable, str(CLI), "security-scan", str(analysis), "--output", str(tmp_path / "security")], tmp_path / "security" / "security-scan-report.json"),
                ([sys.executable, str(CLI), "project-ui", "--output", str(tmp_path / "ui")], tmp_path / "ui" / "project-wizard.html"),
            ]
            for command, expected in commands:
                with self.subTest(command=command[2]):
                    result = subprocess.run(command, cwd=REPO, text=True, capture_output=True)
                    self.assertEqual(result.returncode, 0, result.stderr)
                    self.assertTrue(expected.exists(), expected)

    def test_guided_run_and_health_snapshot_commands(self):
        with tempfile.TemporaryDirectory() as tmp:
            tmp_path = Path(tmp)
            guided = tmp_path / "guided"
            result = subprocess.run(
                [
                    sys.executable,
                    str(CLI),
                    "guided-run",
                    str(ROOT / "examples" / "sample-ax-inventory.csv"),
                    "--project",
                    "Unit Guided",
                    "--ciso-approval",
                    "yes",
                    "--cutover-rehearsal",
                    "yes",
                    "--finance-reconciliation",
                    "yes",
                    "--uat-signoff",
                    "yes",
                    "--rollback-plan",
                    "yes",
                    "--output",
                    str(guided),
                ],
                cwd=REPO,
                text=True,
                capture_output=True,
            )
            self.assertEqual(result.returncode, 0, result.stderr)
            self.assertTrue((guided / "guided-run-plan.md").exists())
            self.assertTrue((guided / "role-action-inbox.md").exists())
            self.assertTrue((guided / "project-health-snapshot.html").exists())
            self.assertTrue((guided / "index.html").exists())

            snapshot = tmp_path / "snapshot"
            result = subprocess.run(
                [sys.executable, str(CLI), "health-snapshot", str(guided), "--output", str(snapshot)],
                cwd=REPO,
                text=True,
                capture_output=True,
            )
            self.assertEqual(result.returncode, 0, result.stderr)
            self.assertTrue((snapshot / "project-health-snapshot.md").exists())

    def test_advanced_control_commands(self):
        expected = {
            "usp-actions": "usp-to-action-map.md",
            "truth-detector": "project-truth-detector.md",
            "cutover-confidence": "cutover-confidence-score.md",
            "meeting-actions": "meeting-to-migration-actions.md",
            "proposal-pack": "proposal-sales-pack.md",
            "role-prompt-pack": "role-prompt-pack-2.md",
            "evidence-freshness": "evidence-freshness-monitor.md",
            "dependency-risk-graph": "dependency-risk-graph.md",
            "partner-deliverable-check": "partner-deliverable-check.md",
            "release-pack": "release-pack-manifest.md",
            "demo-portal": "demo-portal-2.html",
            "wizard-ui": "interactive-wizard-ui-2.html",
        }
        with tempfile.TemporaryDirectory() as tmp:
            tmp_path = Path(tmp)
            source = ROOT / "examples" / "sample-ax-inventory.csv"
            for command, output_file in expected.items():
                output = tmp_path / command
                with self.subTest(command=command):
                    result = subprocess.run(
                        [sys.executable, str(CLI), command, str(source), "--project", "Control Test", "--output", str(output)],
                        cwd=REPO,
                        text=True,
                        capture_output=True,
                    )
                    self.assertEqual(result.returncode, 0, result.stderr)
                    self.assertTrue((output / output_file).exists(), output / output_file)
