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
LOGO = SKILL_DIR / "assets" / "Crestwood-Staff-Signature-Wordmark.png"
DEFAULT_FONT = SKILL_DIR / "assets" / "fonts" / "Raleway-VariableFont_wght.ttf"

WIDTH, HEIGHT = 800, 200
WHITE = (255, 255, 255, 255)
LOGO_DARK_BLUE = (0, 56, 72, 255)
TEXT_TEAL = (8, 60, 79, 255)
TEXT_SCALE = 4


def load_raleway(size: float, font_path: Path, weight: int = 475) -> ImageFont.FreeTypeFont:
    font = ImageFont.truetype(str(font_path), size=round(size * TEXT_SCALE), layout_engine=ImageFont.Layout.BASIC)
    if hasattr(font, "set_variation_by_axes"):
        try:
            font.set_variation_by_axes([weight])
        except OSError:
            pass
    return font


def text_width(text: str, font: ImageFont.FreeTypeFont, tracking: float = 0) -> float:
    bounds = font.getmask(text).getbbox()
    if bounds is None:
        return 0
    left, _top, right, _bottom = bounds
    return (right - left) / TEXT_SCALE + tracking * max(0, len(text) - 1)


def fit_font(
    text: str,
    starting_size: int,
    max_width: int,
    font_path: Path,
    weight: int = 475,
    tracking: float = 0.95,
) -> ImageFont.FreeTypeFont:
    for size in range(starting_size, 11, -1):
        font = load_raleway(size, font_path, weight)
        if text_width(text, font, tracking) <= max_width:
            return font
    raise ValueError(f"Signature text is too long to fit: {text!r}")


def draw_text(draw: ImageDraw.ImageDraw, x: float, baseline: float, text: str, font: ImageFont.FreeTypeFont, tracking: float) -> None:
    # Supersampling preserves fractional spacing and avoids heavy pixel-rounded strokes.
    for character in text:
        draw.text((x * TEXT_SCALE, baseline * TEXT_SCALE), character, font=font, fill=TEXT_TEAL, anchor="ls")
        x += font.getlength(character) / TEXT_SCALE + tracking


def create_signature(name: str, role: str, email: str, output: Path, font_path: Path) -> None:
    if not LOGO.exists():
        raise FileNotFoundError(f"Missing logo asset: {LOGO}")
    if not font_path.exists():
        raise FileNotFoundError(f"Missing Raleway font: {font_path}")

    canvas = Image.new("RGBA", (WIDTH, HEIGHT), WHITE)
    draw = ImageDraw.Draw(canvas)

    logo = Image.open(LOGO).convert("RGBA")
    # Keep the reference logo's original lettering, proportions, and edge pixels.
    canvas.alpha_composite(logo, (34, 24))

    divider_x = 228
    divider_height = 145
    divider_y = (HEIGHT - divider_height) // 2
    draw.rectangle(
        (divider_x, divider_y, divider_x + 2, divider_y + divider_height),
        fill=LOGO_DARK_BLUE,
    )

    text_x = 251
    max_text_width = WIDTH - text_x - 18
    text_layer = Image.new("RGBA", (WIDTH * TEXT_SCALE, HEIGHT * TEXT_SCALE))
    text_draw = ImageDraw.Draw(text_layer)
    name_font = fit_font(name, 44, max_text_width, font_path)
    details = f"{role} | {email}"
    detail_font = load_raleway(27.75, font_path, weight=470)
    if text_width(details, detail_font, tracking=0.8) <= max_text_width:
        draw_text(text_draw, text_x, 99, name, name_font, tracking=0.95)
        draw_text(text_draw, text_x, 132.25, details, detail_font, tracking=0.8)
    else:
        detail_font = fit_font(role, 24, max_text_width, font_path, weight=470, tracking=0.8)
        email_font = fit_font(email, 24, max_text_width, font_path, weight=470, tracking=0.8)
        draw_text(text_draw, text_x, 80, name, name_font, tracking=0.95)
        draw_text(text_draw, text_x, 116, role, detail_font, tracking=0.8)
        draw_text(text_draw, text_x, 147, email, email_font, tracking=0.8)

    canvas.alpha_composite(text_layer.resize((WIDTH, HEIGHT), Image.Resampling.LANCZOS))

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
