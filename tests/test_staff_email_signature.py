from __future__ import annotations

import sys
import tempfile
import unittest
from pathlib import Path

from PIL import Image, ImageChops, ImageFont

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "scripts"))
import create_staff_email_signature as signature


class StaffSignatureTests(unittest.TestCase):
    def render(self, role: str, email: str) -> Image.Image:
        with tempfile.TemporaryDirectory() as directory:
            output = Path(directory) / "signature.png"
            signature.create_signature(
                "Dr. Chris Wilms", role, email, output, signature.DEFAULT_FONT
            )
            with Image.open(output) as image:
                self.assertEqual(image.format, "PNG")
                self.assertEqual(image.mode, "RGB")
                self.assertEqual(image.size, (800, 200))
                return image.copy()

    def text_bands(self, image: Image.Image) -> int:
        ink = ImageChops.difference(image, Image.new("RGB", image.size, "white"))
        occupied = [ink.crop((251, y, 800, y + 1)).getbbox() is not None for y in range(200)]
        return sum(value and (y == 0 or not occupied[y - 1]) for y, value in enumerate(occupied))

    def test_short_details_use_two_lines_and_reference_geometry(self) -> None:
        image = self.render("Elder", "chriswilms@crestwoodrva.org")
        self.assertEqual(self.text_bands(image), 2)
        ink = ImageChops.difference(image, Image.new("RGB", image.size, "white"))
        mask = image.crop((0, 0, 200, 200)).getchannel("R").point(lambda value: 255 if value < 132 else 0)
        left, top, right, bottom = mask.getbbox()
        self.assertEqual(left, 38)
        self.assertEqual(top, 28)
        self.assertEqual(right - left, 145)
        self.assertEqual(bottom - top, 144)
        self.assertEqual(image.getpixel((228, 100)), (0, 56, 72))
        self.assertIsNone(ink.crop((784, 0, 800, 200)).getbbox())

    def test_reference_logo_is_preserved_without_resampling(self) -> None:
        image = self.render("Elder", "chriswilms@crestwoodrva.org")
        with Image.open(signature.LOGO) as logo:
            self.assertEqual(logo.size, (153, 152))
            self.assertEqual(image.crop((34, 24, 187, 176)).tobytes(), logo.convert("RGB").tobytes())

    def test_long_details_use_three_lines_without_overflow(self) -> None:
        image = self.render("Director of Congregational Care and Community Life", "staff@crestwoodrva.org")
        self.assertEqual(self.text_bands(image), 3)
        ink = ImageChops.difference(image, Image.new("RGB", image.size, "white"))
        self.assertIsNone(ink.crop((784, 0, 800, 200)).getbbox())

    def test_name_weight_renders_heavier_than_regular(self) -> None:
        medium = signature.load_raleway(45, signature.DEFAULT_FONT)
        regular = ImageFont.truetype(str(signature.DEFAULT_FONT), medium.size)
        regular.set_variation_by_axes([400])
        def coverage(font: ImageFont.FreeTypeFont) -> int:
            return sum(bytes(font.getmask("Dr. Chris Wilms")))
        self.assertGreater(coverage(medium), coverage(regular))

    def test_reference_text_dimensions_and_optical_weight(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            output = Path(directory) / "matt.png"
            signature.create_signature("Dr. Matt Merrill", "Senior Pastor", "matt@crestwoodrva.org", output, signature.DEFAULT_FONT)
            with Image.open(output) as image:
                # Measured from the supplied 800x200 Matt reference; allow antialiasing differences.
                for box, width, height, coverage in [((240, 55, 795, 105), 313, 32, 2600), ((240, 105, 795, 145), 529, 27, 2608)]:
                    red = image.crop(box).getchannel("R")
                    mask = red.point(lambda value: 255 if value < 132 else 0)
                    left, top, right, bottom = mask.getbbox()
                    self.assertAlmostEqual(right - left, width, delta=1)
                    self.assertAlmostEqual(bottom - top, height, delta=1)
                    ink = sum((255 - value) / 247 for value in red.tobytes())
                    self.assertAlmostEqual(ink, coverage, delta=coverage * 0.04)

    def test_unfittable_text_is_rejected(self) -> None:
        with self.assertRaises(ValueError):
            signature.fit_font("W" * 1000, 24, 529, signature.DEFAULT_FONT)


if __name__ == "__main__":
    unittest.main()
