# Style Selector Prompt

Check your style library before generating a new HTML style.
A saved style can often be reused with only brand color swaps — much faster than
generating from scratch.

**How to use:**
1. Paste your `brand-brief.md` and the metadata from your style library
2. Paste the prompt into Claude
3. Claude recommends an existing style or tells you to generate new

---

## How to extract style metadata

Each saved style has a `style-meta.md` in its folder. Paste the `---` block only:

```
STYLE-STARTUP-MINIMAL-2COL:
---
id: STYLE-STARTUP-MINIMAL-2COL
name: Startup Minimal — two column
library: true
layout: two-column
header_style: colored-band
density: generous
design_register: startup
cv_sections: profile, skills, experience, education
cl_structure: narrative
font_heading: Plus Jakarta Sans
font_body: Inter
color_primary: #1A1A2E
color_secondary: #4A90D9
color_accent: #F5A623
created: 2025-01-15
---

STYLE-ENTERPRISE-FORMAL-1COL:
---
id: STYLE-ENTERPRISE-FORMAL-1COL
...
---
```

---

## The Selector Prompt

---

I have a style library for CV and cover letter HTML templates.
I want to check if an existing style fits my current application before generating new.

Here is my brand brief:

[PASTE brand-brief.md HERE]

Here is my cv-template (visual parameters section is most important):

[PASTE cv-template.md HERE — or just the Visual Parameters section]

Here is my cover-letter-template (length_style and tone):

[PASTE cover-letter-template.md — or just the metadata header]

Here are my saved style metadata blocks:

[PASTE STYLE METADATA BLOCKS HERE]

---

Based on the brand brief and templates, evaluate each saved style:

**1. Match scoring**

For each style, assess:
- Layout match (does the saved layout — single/two-column — match cv-template?)
- Design register (startup / corporate / creative — does it suit this company?)
- Density match (does the saved density match the cv-template margin/spacing guidance?)
- CL structure match (does the saved cl_structure match the cover-letter-template?)
- Font suitability (do the saved fonts suit this brand context, even if not identical?)

**2. Color adaptability**

A style is a strong match even if colors differ — CSS custom properties make color
swaps trivial. Note:
- Which colors need updating to match the brand-brief palette
- Estimated effort: "swap 2 hex values in :root" vs "significant restyle needed"

**3. Recommendation**

**Option A — Strong match:**
"Use `[STYLE-ID]`. Layout and structure match. Color adaptations needed:
- `--color-primary`: change from [old] to [new from brand-brief]
- `--color-header-bg`: change from [old] to [new]
- `--font-heading`: change from [old] to [new] (update Google Fonts import too)

Make these changes in both `cv-output.html` and `cl-output.html` before using."

**Option B — Partial match:**
"Closest style is `[STYLE-ID]`. Matches on [dimensions] but diverges on [dimensions].
Options:
1. Use as-is with color swap — acceptable if [condition]
2. Adapt the layout — change [specific elements]
3. Generate new

Recommended: [recommendation with reason]."

**Option C — No suitable match:**
"No existing style fits well. Generate a new one using `style-generator-prompt.md`.
Key parameters to specify:
- Layout: [recommendation from cv-template]
- Design register: [from brand-brief design personality]
- Fonts: [specific suggestions from brand-brief]
- Colors: [hex values from brand-brief]
- CL structure: [from cover-letter-template]"
