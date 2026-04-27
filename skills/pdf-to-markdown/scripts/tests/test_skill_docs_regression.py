from __future__ import annotations

import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
SKILL_ROOT = ROOT if (ROOT / "SKILL.md").exists() else ROOT / "skills/pdf-to-markdown"
SKILL_MD = SKILL_ROOT / "SKILL.md"


class SkillDocsRegressionTests(unittest.TestCase):
    def test_skill_md_points_to_visual_search_protocol(self) -> None:
        text = SKILL_MD.read_text(encoding="utf-8")

        self.assertIn("## Visual reading and search", text)
        self.assertIn("pdftotext -layout -f START -l END", text)
        self.assertIn("references/visual.md", text)

    def test_skill_md_points_to_proposal_stage_overlay_workflow(self) -> None:
        text = SKILL_MD.read_text(encoding="utf-8")

        self.assertIn("## Project-specific overlays", text)
        self.assertIn("../../proposals/pdf-to-markdown-modular-overlays.md", text)
        self.assertIn("scripts/tests/", text)
        self.assertNotIn("SKILL2.md", text)
        self.assertNotIn("projects/module-system", text)


if __name__ == "__main__":
    unittest.main()
