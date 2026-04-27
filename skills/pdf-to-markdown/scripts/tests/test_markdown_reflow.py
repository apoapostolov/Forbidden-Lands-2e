from __future__ import annotations

import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
SCRIPTS = ROOT / "scripts"
sys.path.insert(0, str(SCRIPTS))

import markdown_reflow as mr  # noqa: E402


class MarkdownReflowTests(unittest.TestCase):
    def test_unwrap_preserves_tables_and_lists(self) -> None:
        sample = (
            "This is a hard wrapped paragraph\n"
            "that should join cleanly.\n\n"
            "- First item\n"
            "  continues on the next line\n\n"
            "| Head 1 | Head 2 |\n"
            "| --- | --- |\n"
            "| One | Two |\n"
        )

        result = mr.process_text(sample, mode="unwrap")

        self.assertIn("This is a hard wrapped paragraph that should join cleanly.", result)
        self.assertIn("- First item continues on the next line", result)
        self.assertIn("| Head 1 | Head 2 |", result)
        self.assertIn("| One | Two |", result)

    def test_wrap_preserves_tables_while_reflowing_prose(self) -> None:
        sample = (
            "This is a longer paragraph that should wrap when the target width is small.\n\n"
            "| Head 1 | Head 2 |\n"
            "| --- | --- |\n"
            "| One | Two |\n"
        )

        result = mr.process_text(sample, mode="wrap", width=32)

        self.assertIn("This is a longer paragraph", result)
        self.assertIn("should wrap when the target", result)
        self.assertIn("| Head 1 | Head 2 |", result)
        self.assertIn("| One | Two |", result)

    def test_cli_version_reports_helpful_version(self) -> None:
        with tempfile.TemporaryDirectory() as tmpdir:
            md_path = Path(tmpdir) / "sample.md"
            md_path.write_text("Paragraph\n", encoding="utf-8")

            completed = subprocess.run(
                [sys.executable, str(SCRIPTS / "markdown_reflow.py"), "--version", str(md_path)],
                check=True,
                capture_output=True,
                text=True,
            )

        self.assertEqual(completed.stdout.strip(), mr.__version__)


if __name__ == "__main__":
    unittest.main()
