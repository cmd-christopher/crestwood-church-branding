from __future__ import annotations

import subprocess
import sys
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
CHECKER = ROOT / "scripts" / "check_contrast.py"
SKILL = ROOT / "SKILL.md"
GUIDELINES = ROOT / "references" / "brand-guidelines.md"


class ContrastCheckerTests(unittest.TestCase):
    def run_checker(self, foreground: str, background: str, text_size: str = "normal") -> subprocess.CompletedProcess[str]:
        self.assertTrue(CHECKER.exists(), "scripts/check_contrast.py must exist")
        return subprocess.run(
            [
                sys.executable,
                str(CHECKER),
                "--foreground",
                foreground,
                "--background",
                background,
                "--text-size",
                text_size,
            ],
            check=False,
            capture_output=True,
            text=True,
        )

    def test_approved_brand_pairs_pass_for_normal_text(self) -> None:
        for foreground, background in (
            ("#FFFFFF", "#0F657D"),
            ("#FFFFFF", "#003848"),
            ("#003848", "#5CB1CA"),
            ("#0F657D", "#FFFFFF"),
        ):
            with self.subTest(foreground=foreground, background=background):
                result = self.run_checker(foreground, background)
                self.assertEqual(result.returncode, 0, result.stdout + result.stderr)
                self.assertIn("PASS", result.stdout)

    def test_light_blue_text_on_white_fails(self) -> None:
        result = self.run_checker("#5CB1CA", "#FFFFFF")
        self.assertNotEqual(result.returncode, 0)
        self.assertIn("FAIL", result.stdout)

    def test_white_on_primary_is_not_approved_for_normal_text(self) -> None:
        result = self.run_checker("#FFFFFF", "#158FB2")
        self.assertNotEqual(result.returncode, 0)
        self.assertIn("FAIL", result.stdout)

    def test_white_on_primary_passes_only_for_large_text(self) -> None:
        result = self.run_checker("#FFFFFF", "#158FB2", text_size="large")
        self.assertEqual(result.returncode, 0, result.stdout + result.stderr)
        self.assertIn("PASS", result.stdout)

    def test_dark_text_on_dark_fills_fails(self) -> None:
        for foreground, background in (("#000000", "#0F657D"), ("#0F657D", "#003848")):
            with self.subTest(foreground=foreground, background=background):
                result = self.run_checker(foreground, background)
                self.assertNotEqual(result.returncode, 0)
                self.assertIn("FAIL", result.stdout)

    def test_dark_text_on_primary_fill_is_rejected_by_brand_policy(self) -> None:
        result = self.run_checker("#000000", "#158FB2")
        self.assertNotEqual(result.returncode, 0)
        self.assertIn("brand policy", result.stdout.lower())


class SkillGuidanceTests(unittest.TestCase):
    def test_skill_contains_an_accessibility_gate(self) -> None:
        text = SKILL.read_text(encoding="utf-8").lower()
        self.assertIn("accessibility and contrast gate", text)
        self.assertIn("4.5:1", text)
        self.assertIn("render at final size", text)

    def test_guidelines_define_safe_color_pairings(self) -> None:
        text = GUIDELINES.read_text(encoding="utf-8").lower()
        self.assertIn("approved text and background pairings", text)
        self.assertIn("#5cb1ca", text)
        self.assertIn("#003848", text)
        self.assertIn("do not use light blue text on white", text)
        self.assertIn("do not place normal-size text directly on primary", text)

    def test_guidance_requires_explicit_variable_font_weights(self) -> None:
        combined = (SKILL.read_text(encoding="utf-8") + GUIDELINES.read_text(encoding="utf-8")).lower()
        self.assertIn("weight 400", combined)
        self.assertIn("weight 600", combined)
        self.assertIn("variable font", combined)


if __name__ == "__main__":
    unittest.main()
