#!/usr/bin/env python3
"""Check a foreground/background pair against WCAG text contrast thresholds."""

from __future__ import annotations

import argparse
import re


HEX_COLOR = re.compile(r"^#?([0-9a-fA-F]{6})$")
PRIMARY = "#158FB2"
DARK_FOREGROUNDS = {"#000000", "#0F657D", "#003848"}


def normalize_hex(value: str) -> str:
    match = HEX_COLOR.fullmatch(value.strip())
    if not match:
        raise argparse.ArgumentTypeError(f"invalid color {value!r}; use a six-digit hex value such as #FFFFFF")
    return f"#{match.group(1).upper()}"


def relative_luminance(value: str) -> float:
    normalized = normalize_hex(value)[1:]
    channels = [int(normalized[index : index + 2], 16) / 255 for index in (0, 2, 4)]
    linear = [channel / 12.92 if channel <= 0.04045 else ((channel + 0.055) / 1.055) ** 2.4 for channel in channels]
    return 0.2126 * linear[0] + 0.7152 * linear[1] + 0.0722 * linear[2]


def contrast_ratio(foreground: str, background: str) -> float:
    foreground_luminance = relative_luminance(foreground)
    background_luminance = relative_luminance(background)
    lighter = max(foreground_luminance, background_luminance)
    darker = min(foreground_luminance, background_luminance)
    return (lighter + 0.05) / (darker + 0.05)


def brand_policy_error(foreground: str, background: str) -> str | None:
    if background == PRIMARY and foreground in DARK_FOREGROUNDS:
        return "dark text is not approved on a Primary fill; use a Dark fill with white text or a Light fill with Logo dark text"
    return None


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--foreground", required=True, type=normalize_hex, help="text color as six-digit hex")
    parser.add_argument("--background", required=True, type=normalize_hex, help="background color as six-digit hex")
    parser.add_argument(
        "--text-size",
        choices=("normal", "large"),
        default="normal",
        help="normal requires 4.5:1; large (18 pt regular or 14 pt bold and larger) requires 3:1",
    )
    return parser


def main() -> int:
    args = build_parser().parse_args()
    threshold = 4.5 if args.text_size == "normal" else 3.0
    ratio = contrast_ratio(args.foreground, args.background)
    policy_error = brand_policy_error(args.foreground, args.background)
    if policy_error:
        print(
            f"FAIL (brand policy): {args.foreground} on {args.background} = {ratio:.2f}:1; "
            f"{policy_error}"
        )
        return 1
    verdict = "PASS" if ratio >= threshold else "FAIL"
    print(
        f"{verdict}: {args.foreground} on {args.background} = {ratio:.2f}:1 "
        f"(requires {threshold:.2f}:1 for {args.text_size} text)"
    )
    return 0 if ratio >= threshold else 1


if __name__ == "__main__":
    raise SystemExit(main())
