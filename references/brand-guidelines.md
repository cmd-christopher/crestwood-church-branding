# Crestwood Church Branding

## Typography
- Primary font: Raleway (use for headings and body copy).
- Bundled font: `assets/fonts/Raleway-VariableFont_wght.ttf` for portable generated outputs.
- If Raleway is unavailable, note the limitation and ask before substituting.

## Color palette
- Primary: #158fb2
- Dark: #0f657d
- Light: #5cb1ca
- Logo dark blue: #003848 (use for staff email signature text and divider to match the square wordmark box)

## Logos and Marks
- Primary horizontal logo files:
  - assets/Crestwood+Horizontal+Logo.svg (preferred scalable/vector use; letterforms are outlined)
  - assets/Crestwood+Horizontal+Logo.editable.svg (editable source/reference; requires Raleway)
  - assets/Crestwood+Horizontal+Logo.webp (web use)
  - assets/Crestwood+Horizontal+Logo.png (Office docs and email clients)
- Alternate C mark files:
  - assets/Crestwood+C+Mark.svg (vector use, web, print, scalable layouts)
  - assets/Crestwood+C+Mark.png (Office docs, email clients, square/avatar-style placements)
- Square wordmark files:
  - assets/Crestwood+Square+Wordmark.svg (vector use, web, print, scalable layouts)
  - assets/Crestwood+Square+Wordmark.png (Office docs, email clients, email signatures, square/avatar-style placements)
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
- Use the Primary color for accents and headings; use Dark for emphasis or footers; use Light for subtle backgrounds.
- Avoid adding new colors unless the user asks.

## Staff email signatures
- Use a white 800x200 px banner image for Gmail signatures; export PNG for the final email-client asset.
- Prefer `scripts/create_staff_email_signature.py` for generated signature images; it defaults to the bundled Raleway font and does not require system font installation.
- Place `assets/Crestwood+Square+Wordmark.svg` or `.png` on the left at about 140-145 px square, vertically centered with generous white space.
- Add a thin vertical divider in Logo dark blue (#003848) between the logo and staff details, about 3 px wide and about the same height as the logo.
- Set all text in Raleway, Logo dark blue (#003848). Use a large regular-weight name line, then smaller regular-weight title/email lines. When using a variable Raleway font, explicitly set weight 400; do not rely on the font default, which can render too thin.
- Use this text pattern when it fits cleanly: `Name` on line 1 and `Role | email@crestwoodrva.org` on line 2.
- For longer roles or emails, use three lines: `Name`, `Role`, `email@crestwoodrva.org`.
- Do not store individual staff signature images in skill assets unless the user explicitly asks for reusable template examples; generated personal signatures should live outside the skill repository.
- After generating a signature image, visually inspect the PNG for readable text weight, centered logo placement, and no text overflow.
