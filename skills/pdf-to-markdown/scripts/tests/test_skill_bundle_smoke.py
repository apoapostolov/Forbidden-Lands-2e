from __future__ import annotations

import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
SKILL_ROOT = ROOT if (ROOT / "SKILL.md").exists() else ROOT / "skills/pdf-to-markdown"
SKILL_SCRIPTS = SKILL_ROOT / "scripts"

ALLOWED_FILES = {
    "README.md",
    "markdown_reflow.py",
    "ocr_markdown_audit.py",
    "pdf_debug_passes.py",
    "pdf_to_markdown.py",
    "repair_flattened_tables.py",
    "split_markdown_sections.py",
    "unwrap_paragraphs.py",
}

LEGACY_FORBIDDEN_FILES = {
    "TRADEROADS_VIABILITY_REPORT.md",
    "analyze_book03_bestiary_sizes.py",
    "analyze_corebook.py",
    "assemble_merged_bestiary.py",
    "band_economy_sim.py",
    "build_mercenaries.py",
    "fix_ch09_hollows.py",
    "fix_weatherstone_vale.py",
    "lifepath_balance_report.txt",
    "lifepath_simulation.py",
    "merge_bestiary.py",
    "split_mercenaries.py",
    "traderoads_analysis.py",
    "traderoads_sensitivity.py",
    "traderoads_simulation.py",
    "update_book02_resources.py",
    "module_overlay.py",
    "module_registry.py",
    "module_validation.py",
    "module_archive.py",
}


class SkillBundleSmokeTests(unittest.TestCase):
    def test_skill_scripts_tree_is_curated(self) -> None:
        names = {
            path.name
            for path in SKILL_SCRIPTS.iterdir()
            if path.is_file()
        }

        self.assertTrue(ALLOWED_FILES.issubset(names))
        self.assertFalse(names & LEGACY_FORBIDDEN_FILES)
        self.assertEqual(names, ALLOWED_FILES)


if __name__ == "__main__":
    unittest.main()
