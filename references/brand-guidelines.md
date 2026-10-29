# Crestwood Church Branding

## Typography
- Primary font: Raleway (use for headings and body copy).
- Bundled font: `assets/fonts/Raleway-VariableFont_wght.ttf` for portable generated outputs.
- Explicitly set generated body copy to weight 400 or 500 and headings to weight 600 or 700. The bundled variable font can otherwise open at weight 100 (Thin), which is not readable at normal document and diagram sizes.
- If Raleway is unavailable, note the limitation and ask before substituting.

## Color palette
- Primary: #158fb2
- Dark: #0f657d
- Light: #5cb1ca
- Logo dark blue: #003848 (use for staff email signature divider to match the square wordmark box)
- Signature text teal: #083C4F (matches the Matt Merrill staff signature reference; approved on white)

## Approved text and background pairings

Normal-size text requires at least `4.5:1` contrast. Large text (at least 18 pt regular or 14 pt bold) requires at least `3:1`.

| Use | Text | Background | Contrast |
|---|---|---|---:|
| Dark filled box | White `#FFFFFF` | Dark `#0F657D` | 6.61:1 |
| Extra-dark filled box | White `#FFFFFF` | Logo dark `#003848` | 12.66:1 |
| Light filled box | Logo dark `#003848` | Light `#5CB1CA` | 5.18:1 |
| Normal text on white | Dark `#0F657D` or Logo dark `#003848` | White `#FFFFFF` | 6.61:1 or 12.66:1 |
| Staff signature text | Signature teal `#083C4F` | White `#FFFFFF` | 11.87:1 |
| Large heading only | Primary `#158FB2` | White `#FFFFFF` | 3.75:1 |

- Do not use Light blue text on white; Light (`#5CB1CA`) on white is only 2.44:1.
- Do not use dark text on Dark (`#0F657D`) or Logo dark (`#003848`) backgrounds; use white text.
- Do not place normal-size text directly on Primary (`#158FB2`), and do not use black, Dark, or Logo dark text on a Primary fill even when the mathematical contrast passes. Use a Dark fill with white text or a Light fill with Logo dark text instead.
- Do not use white normal-size text on Primary; that pairing is only 3.75:1 and is suitable only for large text.
- Primary and Light remain brand colors, but brand consistency never overrides readability.

For a custom combination, run:

```bash
python3 scripts/check_contrast.py --foreground '#FFFFFF' --background '#0F657D' --text-size normal
```

The checker uses WCAG contrast math and has no third-party dependencies.

## Logos and Marks
- Primary horizontal logo files:
  - assets/Crestwood-Horizontal-Logo.svg (preferred scalable/vector use; letterforms are outlined)
  - assets/Crestwood-Horizontal-Logo.editable.svg (editable source/reference; requires Raleway)
  - assets/Crestwood-Horizontal-Logo.webp (web use)
  - assets/Crestwood-Horizontal-Logo.png (Office docs and email clients)
- Alternate C mark files:
  - assets/Crestwood-C-Mark.svg (vector use, web, print, scalable layouts)
  - assets/Crestwood-C-Mark.png (Office docs, email clients, square/avatar-style placements)
- Square wordmark files:
  - assets/Crestwood-Square-Wordmark.svg (vector use, web, print, scalable layouts)
  - assets/Crestwood-Square-Wordmark.png (Office docs, email clients, email signatures, square/avatar-style placements)
- Staff signature reference logo:
  - assets/Crestwood-Staff-Signature-Wordmark.png (logo only, extracted from the user-supplied `Matt Opt 2.jpg`; use for the 800x200 signature generator)
- Font files:
  - assets/fonts/Raleway-VariableFont_wght.ttf (bundled for generated outputs and staff systems without Raleway installed)
  - assets/fonts/OFL.txt (Raleway font license)
- Use the primary horizontal logo by default when the church name should be visible.
- Use the alternate C mark when a compact icon-style mark is a better fit, such as square social/avatar placements, small badges, watermarks, stickers, or layout accents where the full horizontal logo would be crowded.
- Use the square wordmark when a compact square mark is needed but the words "Crestwood Church" should still be visible, such as staff email signatures, profile-style image blocks, or other small layouts based on the square signature mark.
- Keep aspect ratio; scale uniformly (same percentage horizontally and vertically); do not stretch, skew, or recolor any logo or mark.
- Place with clear space around logos/marks; avoid crowding other elements.

## Usage notes
- Prefer clean, modern layouts with generous whitespace.
- Use Primary for large headings, rules, icons, and accents; use Dark or Logo dark with white text for strong filled areas; use Light only as a background with Logo dark text.
- Avoid adding new colors unless the user asks.

## Generated visual readability check

Before delivering a document, slide, graphic, email image, or web layout:

1. Choose an approved text/background pairing above or run `scripts/check_contrast.py`.
2. Explicitly set Raleway weight 400 or 500 for body text and weight 600 or 700 for headings.
3. Size body text for the final placed dimensions, not merely the source canvas dimensions.
4. Render at final size and inspect at 100% zoom for contrast, thin type, cramped wrapping, clipping, and text that becomes too small when embedded.
5. If any text is difficult to read, change the pairing, weight, size, or layout before delivery.

## Staff email signatures
- Use a white 800x200 px banner image for Gmail signatures; export PNG for the final email-client asset.
- Prefer `scripts/create_staff_email_signature.py` for generated signature images; it defaults to the bundled Raleway font and does not require system font installation.
- Runtime requirement: Python 3 with Pillow. If Pillow is missing, install the skill's `requirements.txt` in the active environment, then run `python3 scripts/create_staff_email_signature.py ...` or the platform's equivalent Python command.
- Use `assets/Crestwood-Staff-Signature-Wordmark.png` at its native 153x152 px size, placed at (34, 24). It preserves the exact reference logo, including its padding and edge antialiasing; the visible frame spans x=38..182 and y=28..171. The asset is a logo-only crop of reference bounds (34, 24, 187, 176), with no personal staff details. Do not crop, resize, redraw, or substitute the generic square wordmark in this generator. Keep the divider at x=228 and text at x=251.
- Add a thin vertical divider in Logo dark blue (#003848) between the logo and staff details, about 3 px wide and about the same height as the logo.
- Use the generator's calibrated Raleway treatment: 44 px name at weight 475 with 0.95 px letter spacing, and 27.75 px combined role/email at weight 470 with 0.8 px letter spacing, in signature text teal (#083C4F). Longer details use separate 24 px lines. These variable-font settings, baseline positions, and 4x text rendering match the apparent weight and spacing of the Matt Merrill reference; a uniform weight 500 makes both lines too heavy. Reduce individual line sizes if needed to prevent overflow.
- Use this text pattern when it fits cleanly: `Name` on line 1 and `Role | email@crestwoodrva.org` on line 2.
- For longer roles or emails, use three lines: `Name`, `Role`, `email@crestwoodrva.org`.
- Do not store individual staff signature images in skill assets unless the user explicitly asks for reusable template examples; generated personal signatures should live outside the skill repository.
- After generating a signature image, visually inspect the PNG for readable text weight, centered logo placement, and no text overflow.
