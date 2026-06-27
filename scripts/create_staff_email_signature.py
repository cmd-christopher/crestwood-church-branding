#!/usr/bin/env python3
"""Create a Crestwood staff email signature PNG."""

from __future__ import annotations

import argparse
from pathlib import Path

try:
    from PIL import Image, ImageDraw, ImageFont
except ImportError as exc:
    raise SystemExit(
        "This script requires Pillow. Install it with `python3 -m pip install Pillow` "
        "or run it in an agent harness that already provides Pillow."
    ) from exc


SKILL_DIR = Path(__file__).resolve().parents[1]
LOGO = SKILL_DIR / "assets" / "Crestwood+Square+Wordmark.png"
DEFAULT_FONT = SKILL_DIR / "assets" / "fonts" / "Raleway-VariableFont_wght.ttf"

WIDTH, HEIGHT = 800, 200
WHITE = (255, 255, 255, 255)
LOGO_DARK_BLUE = (0, 56, 72, 255)


def load_raleway(size: int, font_path: Path) -> ImageFont.FreeTypeFont:
    font = ImageFont.truetype(str(font_path), size=size)
    if hasattr(font, "set_variation_by_axes"):
        try:
            # Variable fonts can default to Thin; force regular when supported.
            font.set_variation_by_axes([400])
        except OSError:
            pass
    return font


def text_width(draw: ImageDraw.ImageDraw, text: str, font: ImageFont.FreeTypeFont) -> int:
    left, _top, right, _bottom = draw.textbbox((0, 0), text, font=font)
    return right - left


def fit_font(
    draw: ImageDraw.ImageDraw,
    text: str,
    starting_size: int,
    max_width: int,
    font_path: Path,
) -> ImageFont.FreeTypeFont:
    for size in range(starting_size, 11, -1):
        font = load_raleway(size, font_path)
        if text_width(draw, text, font) <= max_width:
            return font
    return load_raleway(12, font_path)


def create_signature(name: str, role: str, email: str, output: Path, font_path: Path) -> None:
    if not LOGO.exists():
        raise FileNotFoundError(f"Missing logo asset: {LOGO}")
    if not font_path.exists():
        raise FileNotFoundError(f"Missing Raleway font: {font_path}")

    canvas = Image.new("RGBA", (WIDTH, HEIGHT), WHITE)
    draw = ImageDraw.Draw(canvas)

    logo_size = 145
    logo = Image.open(LOGO).convert("RGBA")
    logo.thumbnail((logo_size, logo_size), Image.Resampling.LANCZOS)
    logo_x = 34
    logo_y = (HEIGHT - logo.height) // 2
    canvas.alpha_composite(logo, (logo_x, logo_y))

    divider_x = 214
    divider_y = (HEIGHT - logo_size) // 2
    draw.rounded_rectangle(
        (divider_x, divider_y, divider_x + 3, divider_y + logo_size),
        radius=1,
        fill=LOGO_DARK_BLUE,
    )

    text_x = 244
    max_text_width = WIDTH - text_x - 40
    name_font = fit_font(draw, name, 43, max_text_width, font_path)
    detail_font = fit_font(draw, role, 24, max_text_width, font_path)
    email_font = fit_font(draw, email, 24, max_text_width, font_path)

    draw.text((text_x, 48), name, font=name_font, fill=LOGO_DARK_BLUE)
    draw.text((text_x, 103), role, font=detail_font, fill=LOGO_DARK_BLUE)
    draw.text((text_x, 134), email, font=email_font, fill=LOGO_DARK_BLUE)

    output.parent.mkdir(parents=True, exist_ok=True)
    canvas.convert("RGB").save(output, "PNG", optimize=True)


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--name", required=True)
    parser.add_argument("--role", required=True)
    parser.add_argument("--email", required=True)
    parser.add_argument("--output", required=True, type=Path)
    parser.add_argument("--font", default=DEFAULT_FONT, type=Path, help="Defaults to bundled Raleway.")
    return parser.parse_args()


def main() -> None:
    args = parse_args()
    create_signature(args.name, args.role, args.email, args.output, args.font)
    print(args.output)


if __name__ == "__main__":
    main()
