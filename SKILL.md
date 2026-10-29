---
name: crestwood-church-branding
description: 'Use for any Crestwood Church material: docx, xlsx, pptx, PDFs, graphics, posters, flyers, newsletters, websites, or staff and congregation communications.'
---

# Crestwood Church Branding

## Quick start
- Confirm the request is for Crestwood Church or a church-specific audience; if unclear, ask.
- Apply the brand guidelines in `references/brand-guidelines.md`.
- Use the horizontal logo when the church name should be visible, the C mark for icon-like placements, and the square wordmark for signatures or avatars. Prefer SVG for vector output and PNG for Office or email.
- Pass the Accessibility and contrast gate below before delivering any design that uses colored text or a colored background.
- Generate staff email signatures with `scripts/create_staff_email_signature.py`; install `requirements.txt` if Pillow is unavailable.

## Workflow
1. Identify the output format and audience.
2. Apply the reference typography, colors, and correct logo asset without recoloring or distortion.
3. Select an approved text/background pairing and explicitly set Raleway weight.
4. Render at final size and inspect readability at 100% zoom. Ask before substituting unavailable brand elements.

## Accessibility and contrast gate

- Normal-size text must have at least `4.5:1` contrast. Large text (at least 18 pt regular or 14 pt bold) must have at least `3:1`.
- Use white text on Dark (`#0F657D`) or Logo dark (`#003848`) fills.
- Use Logo dark (`#003848`) text on Light (`#5CB1CA`) fills.
- On white, use Dark or Logo dark for normal text. Primary (`#158FB2`) is limited to large headings, rules, icons, and accents.
- Do not use Light (`#5CB1CA`) as text on white, dark text on Dark/Logo dark fills, or dark text on a Primary fill.
- For generated graphics, explicitly set Raleway to weight 400 or 500 for body text and weight 600 or 700 for headings. The bundled variable font may otherwise render at weight 100 (Thin).
- For any other color combination, run `python3 scripts/check_contrast.py --foreground '#FFFFFF' --background '#0F657D' --text-size normal` and use only a passing pairing.
- Contrast math is necessary but not sufficient: render at final size and inspect the actual output for readable weight, size, wrapping, and background pairing.

## Format-specific guidance
- Documents and emails: use Raleway, Primary for large headings or rules, and the horizontal logo where the church name should appear.
- Staff signatures: use the generator's calibrated Raleway text and dedicated `assets/Crestwood-Staff-Signature-Wordmark.png` to match the Matt Merrill reference, with a white 800x200 PNG and Logo dark divider. Prefer two lines, with role and email together; the generator uses three lines when needed. Keep personal outputs outside the skill.
- Spreadsheets: use Raleway headers and readable approved header-row pairings.
- Presentations, posters, and web: use Dark/Logo dark blocks with white text or Light blocks with Logo dark text. Reserve Primary for large headings and accents.

Do not introduce new colors or fonts unless requested.
