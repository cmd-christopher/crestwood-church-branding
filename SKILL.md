---
name: crestwood-church-branding
description: Apply Crestwood Church branding (Raleway font, #158fb2 palette, logo) when creating or editing any church-related materials, including Word/docx letters, Excel/xlsx spreadsheets, PowerPoint/pptx presentations, posters, flyers, newsletters, emails to the Crestwood congregation, or any document explicitly for Crestwood Church or its congregation.
---

# Crestwood Church Branding

## Quick start
- Confirm the request is for Crestwood Church or a church-specific audience; if unclear, ask.
- Apply the brand guidelines in `references/brand-guidelines.md`.
- Use the primary horizontal logo from `assets/Crestwood+Horizontal+Logo.svg` for scalable/vector output; use `assets/Crestwood+Horizontal+Logo.webp` or `assets/Crestwood+Horizontal+Logo.png` when raster formats are required.
- Use the alternate C mark from `assets/Crestwood+C+Mark.svg` or `assets/Crestwood+C+Mark.png` only when a compact icon-style mark is a better fit than the full horizontal logo.
- Use the square wordmark from `assets/Crestwood+Square+Wordmark.svg` or `assets/Crestwood+Square+Wordmark.png` when a compact square mark should still spell out "Crestwood Church," such as email signatures or avatar-like placements.
- For staff email signature images, use `scripts/create_staff_email_signature.py` unless there is a specific reason to hand-build the layout.

## Workflow
1. Identify the output format (docx, xlsx, pptx, pdf, image, web) and the audience.
2. Apply typography, colors, and logo usage from `references/brand-guidelines.md`.
3. Keep layouts clean and readable; do not introduce new colors or fonts unless requested.
4. If a required brand element is unavailable (e.g., font missing), call it out and ask before substituting.

## Format-specific guidance
- Text documents (letters, memos, newsletters): use Raleway for headings and body, apply the Primary color for headings or section rules, and place the primary horizontal logo in the header or cover.
- Emails to the congregation: use Raleway if supported, use the Primary color for headings or accents, and include the primary horizontal logo in the header or signature block when possible.
- Staff email signatures: use `scripts/create_staff_email_signature.py` to create the standard white 800x200 Gmail PNG with the square wordmark, regular-weight Raleway, and text/divider in the logo box color (#003848). Keep individual personal signature files out of this reusable skill unless explicitly requested.
- Spreadsheets (budgets, finance): use Raleway for headers, apply the Primary color to header rows, and keep data readability as the priority.
- Presentations/posters: use bold color blocks with the Primary or Dark palette, include the primary horizontal logo on the title slide or footer, and use Light for subtle backgrounds. Use the C mark sparingly for compact icon placements, watermarks, or stickers. Use the square wordmark for square/avatar-style needs where the church name should remain visible.

## Notes
- If the user asks for a web page or UI, apply these brand guidelines to the design.
- Do not recolor or distort any logo/mark; only scale uniformly (same percentage horizontally and vertically).
