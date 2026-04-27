from __future__ import annotations

import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
SCRIPTS = ROOT / "scripts"
sys.path.insert(0, str(SCRIPTS))

import pdf_to_markdown as ptm  # noqa: E402


class PdfToMarkdownTests(unittest.TestCase):
    def test_parse_mapping_flag_parses_pairs(self) -> None:
        result = ptm.parse_mapping_flag(["old=new", "foo = bar"])
        self.assertEqual(result, {"old": "new", "foo": "bar"})

    def test_parse_mapping_flag_rejects_invalid_input(self) -> None:
        with self.assertRaises(ValueError):
            ptm.parse_mapping_flag(["missing-equals"])

    def test_repair_flattened_tables_text_rebuilds_row_line(self) -> None:
        sample = "D66 WEALTH GEAR 11-16 Too much debt. -2 21-26 In debt. -1\n"

        fixed, changed = ptm.repair_flattened_tables_text(sample)

        self.assertEqual(changed, 1)
        self.assertEqual(
            fixed,
            "| D66 | WEALTH GEAR |\n| --- | --- |\n| 11-16 | Too much debt. -2 |\n| 21-26 | In debt. -1 |\n",
        )

    def test_build_pipeline_passes_stays_generic(self) -> None:
        names = [name for name, _ in ptm.build_pipeline_passes(ptm.DOCUMENT_PROFILES["default"])]

        self.assertIn("flattened-tables", names)
        self.assertIn("dropcap-repair", names)
        self.assertNotIn("forbidden-lands", names)

    def test_run_passes_can_select_a_single_pass(self) -> None:
        calls: list[str] = []

        def first(lines: list[str]) -> list[str]:
            calls.append("first")
            return [*lines, "first\n"]

        def second(lines: list[str]) -> list[str]:
            calls.append("second")
            return [*lines, "second\n"]

        result = ptm.run_passes(
            ["start\n"],
            [("first", first), ("second", second)],
            selected_passes=["second"],
        )

        self.assertEqual(calls, ["second"])
        self.assertEqual(result, ["start\n", "second\n"])

    def test_run_passes_can_skip_a_pass(self) -> None:
        calls: list[str] = []

        def first(lines: list[str]) -> list[str]:
            calls.append("first")
            return [*lines, "first\n"]

        def second(lines: list[str]) -> list[str]:
            calls.append("second")
            return [*lines, "second\n"]

        result = ptm.run_passes(
            ["start\n"],
            [("first", first), ("second", second)],
            skip_passes=["first"],
        )

        self.assertEqual(calls, ["second"])
        self.assertEqual(result, ["start\n", "second\n"])

    def test_cli_version_reports_script_version(self) -> None:
        completed = subprocess.run(
            [sys.executable, str(SCRIPTS / "pdf_to_markdown.py"), "--version"],
            check=True,
            capture_output=True,
            text=True,
        )

        self.assertEqual(completed.stdout.strip(), ptm.__version__)

    def test_cli_list_passes_prints_expected_pass(self) -> None:
        with tempfile.TemporaryDirectory() as tmpdir:
            pdf_path = Path(tmpdir) / "sample.pdf"
            out_dir = Path(tmpdir) / "out"
            pdf_path.write_text("", encoding="utf-8")

            completed = subprocess.run(
                [
                    sys.executable,
                    str(SCRIPTS / "pdf_to_markdown.py"),
                    "--list-passes",
                    str(pdf_path),
                    str(out_dir),
                ],
                check=True,
                capture_output=True,
                text=True,
            )

        passes = completed.stdout.splitlines()
        self.assertIn("flattened-tables", passes)
        self.assertIn("dropcap-repair", passes)


if __name__ == "__main__":
    unittest.main()
