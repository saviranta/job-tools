# HTML Style Generator Prompt

Generates two HTML/CSS skeleton files — one for the CV, one for the cover letter —
from your brand brief, CV template, and cover letter template.

**How to use:**
1. Paste your `brand-brief.md`, `cv-template.md`, and `cover-letter-template.md` below
2. Answer the two quick questions
3. Paste the full prompt into Claude Code
4. Save the two output files to your application folder
5. Optionally save the style to your library

---

## Quick questions

**Q1: Save this style to your library for reuse?**
- [ ] Yes — this layout pattern will work for similar applications
- [ ] No — one-off for this application

If yes, give it a short name:
e.g. `startup-minimal-2col`, `enterprise-formal-1col`, `agency-bold-dark`

Style name: [YOUR NAME HERE]

---

**Q2: Output format for the CV?**
- [ ] HTML file (styled, print-ready) — recommended for designed CVs
- [ ] Markdown with HTML header block — recommended for ATS-first CVs where
      a plain text fallback matters

Cover letters are always HTML.

---

## Paste your input files

**brand-brief.md:**
[PASTE HERE]

**cv-template.md:**
[PASTE HERE]

**cover-letter-template.md:**
[PASTE HERE]

**job-brief.md** (optional — for role/company context):
[PASTE HERE — or delete]

---

## The Generation Prompt

Paste everything above into Claude Code, followed by this:

---

You are generating two HTML/CSS skeleton files for a job application:
- `cv-output.html` — the visual container for the CV
- `cl-output.html` — the visual container for the cover letter

Both files must share the same CSS custom properties so they look designed together.
Use the brand-brief for colors and fonts, the cv-template for CV structure and layout,
and the cover-letter-template for CL structure.

Generate a style ID from the name in Q1:
e.g. `startup-minimal-2col` → `STYLE-STARTUP-MINIMAL-2COL`.
If one-off, use `STYLE-ONEOFF`.

---

### Shared requirements for both files

**CSS custom properties** — define these at `:root` level in both files,
with identical values so the documents look like a pair:

```css
:root {
  --color-primary: /* from brand-brief primary color */;
  --color-secondary: /* from brand-brief secondary color */;
  --color-accent: /* from brand-brief accent color */;
  --color-header-bg: /* header background — brand primary or light secondary */;
  --color-header-text: /* text on header background — white or dark */;
  --color-body-text: #333333;
  --color-subtle: /* muted tone for dates, labels, secondary info */;
  --font-heading: /* from brand-brief or cv-template visual parameters */;
  --font-body: /* from brand-brief or cv-template visual parameters */;
  --page-padding: /* from cv-template margin guidance */;
  --line-height: /* from cv-template density — compact/standard/generous */;
}
```

**Google Fonts** — import both heading and body fonts at the top of `<head>`.
Use the exact font names from brand-brief or cv-template visual parameters.
If no specific fonts are named, select an appropriate pairing for the design register:
- Startup / minimal → Inter, Plus Jakarta Sans, or DM Sans
- Corporate / formal → Source Serif 4 + Source Sans 3, or Playfair Display + Lato
- Creative / bold → Fraunces + Instrument Sans, or Syne + Manrope

**Print CSS** — both files must include:

```css
@media print {
  @page {
    margin: 0;
    size: A4;
  }
  body {
    print-color-adjust: exact;
    -webkit-print-color-adjust: exact;
  }
  .header {
    /* Header must span full page width edge-to-edge when printed.
       Use negative margins matching the body padding: */
    margin-left: calc(-1 * var(--page-padding));
    margin-right: calc(-1 * var(--page-padding));
    padding-left: var(--page-padding);
    padding-right: var(--page-padding);
    margin-top: calc(-1 * var(--page-padding));
    padding-top: var(--page-padding);
  }
}
```

**No decorative lines** — use whitespace, background color blocks, and font weight
for visual separation. No `border-bottom`, `hr`, or decorative rules.

**Placeholder slots** — use `{{SLOT_NAME}}` syntax for all content.
Every slot must have a visible placeholder so the file renders meaningfully
even before content is filled.

---

### cv-output.html requirements

**Structure** — adapt to the cv-template layout:
- Single column: full-width sections, no sidebar
- Two-column: sidebar (left, ~30% width) for contact/skills/education;
  main column (right, ~70%) for experience and profile
- Hybrid: as specified in cv-template

**Header section:**
```html
<header class="cv-header" style="background-color: var(--color-header-bg);">
  <div class="header-photo-block">
    <!-- Include photo slot only if cv-template says include photo -->
    <!-- <img src="{{PHOTO}}" class="candidate-photo" alt=""> -->
  </div>
  <div class="header-text-block">
    <h1 class="candidate-name">{{CANDIDATE_NAME}}</h1>
    <p class="candidate-title">{{CANDIDATE_TITLE}}</p>
    <p class="contact-line">{{CONTACT_LINE}}</p>
  </div>
</header>
```

**Section structure** — generate one `<section>` block per section in the cv-template
section list, in exact order. Each section:
```html
<section class="cv-section cv-section--[section-id]">
  <h2 class="section-title">SECTION NAME</h2>
  <div class="section-content">
    {{SECTION_SLOT}}
  </div>
</section>
```

**Experience section** — show two role blocks as example, with numbered slots:
```html
<div class="role-block">
  <div class="role-header">
    <span class="role-title">{{ROLE_TITLE_1}}</span>
    <span class="role-company">{{COMPANY_1}}</span>
    <span class="role-dates">{{DATES_1}}</span>
  </div>
  <ul class="role-bullets">{{BULLETS_1}}</ul>
</div>
```

**Typography:**
- Section titles: `var(--font-heading)`, uppercase, letter-spaced, the accent or primary color
- Role titles: `var(--font-heading)`, bold, body text color
- Company / dates: `var(--font-body)`, `var(--color-subtle)`
- Body text and bullets: `var(--font-body)`, `var(--color-body-text)`

**Metadata comment block** at top of file:
```html
<!--
  STYLE ID: [STYLE-ID]
  Generated for: [role title from job-brief, or "General application"]
  Layout: [single/two-column/hybrid]
  CV sections: [comma-separated list from cv-template]
  Fonts: [heading font] / [body font]
  Colors: primary=[hex] secondary=[hex] accent=[hex]
  Library: [true/false]
  Created: [date]
-->
```

---

### cl-output.html requirements

**Structure** — adapt to the cover-letter-template length_style:
- `short-bold`: minimal wrapper, generous whitespace, large opening statement
- `structured`: clear visual separation between opening / bullets / closing
- `narrative`: flowing paragraphs, no visual dividers between sections

**Header** — matches cv-output.html exactly (same background, same fonts, same contact line).
This is what makes the pair look like a set:
```html
<header class="cl-header" style="background-color: var(--color-header-bg);">
  <h1 class="candidate-name">{{CANDIDATE_NAME}}</h1>
  <p class="contact-line">{{CONTACT_LINE}}</p>
</header>
```

**Letter metadata block:**
```html
<div class="letter-meta">
  <p class="letter-date">{{DATE}}</p>
  <p class="letter-recipient">{{RECIPIENT}}</p>
  <p class="letter-company">{{COMPANY_NAME}}</p>
  <p class="letter-role">Re: {{ROLE_TITLE}}</p>
</div>
```

**Body slots** — generate based on cl-template `length_style`:

*short-bold:*
```html
<div class="cl-body">
  <p class="cl-opening">{{OPENING_PARAGRAPH}}</p>
  <p class="cl-body-1">{{BODY_PARAGRAPH_1}}</p>
  <p class="cl-closing">{{CLOSING_PARAGRAPH}}</p>
</div>
```

*structured:*
```html
<div class="cl-body">
  <p class="cl-opening">{{OPENING_PARAGRAPH}}</p>
  <ul class="cl-bullets">{{BODY_BULLETS}}</ul>
  <p class="cl-closing">{{CLOSING_PARAGRAPH}}</p>
</div>
```

*narrative:*
```html
<div class="cl-body">
  <p class="cl-opening">{{OPENING_PARAGRAPH}}</p>
  <p class="cl-body-1">{{BODY_PARAGRAPH_1}}</p>
  <p class="cl-body-2">{{BODY_PARAGRAPH_2}}</p>
  <p class="cl-company">{{COMPANY_PARAGRAPH}}</p>
  <p class="cl-closing">{{CLOSING_PARAGRAPH}}</p>
</div>
```

**Sign-off:**
```html
<div class="cl-signoff">
  <p>{{SIGNATURE}}</p>
  <p class="candidate-name-signoff">{{CANDIDATE_NAME}}</p>
</div>
```

**Metadata comment block** at top of file:
```html
<!--
  STYLE ID: [STYLE-ID]
  Generated for: [role title from job-brief, or "General application"]
  CL structure: [short-bold / structured / narrative]
  Fonts: [heading font] / [body font]
  Colors: primary=[hex] secondary=[hex] accent=[hex]
  Library: [true/false]
  Created: [date]
-->
```

---

### Style library metadata

If Q1 is "save to library", also output a `style-meta.md` file to save alongside
the HTML files in `templates/styles/[STYLE-ID]/`:

```markdown
---
id: [STYLE-ID]
name: [Human-readable name]
library: true
layout: single-column / two-column / hybrid
header_style: colored-band / minimal / dark
density: compact / standard / generous
design_register: startup / corporate / creative / agency / academic
cv_sections: [comma-separated section list]
cl_structure: short-bold / structured / narrative
font_heading: [font name]
font_body: [font name]
color_primary: [hex]
color_secondary: [hex]
color_accent: [hex]
created: [date]
---

## Notes
[Any specific adaptation notes — e.g. "swap --color-header-bg per application brand"]
```

---

### Output checklist

Before returning the files, verify:
- [ ] Both files import the same Google Fonts
- [ ] Both files define identical CSS custom properties at `:root`
- [ ] Print CSS is present in both with full-bleed header handling
- [ ] All slots from the README slot reference are present
- [ ] Section order in cv-output.html matches cv-template section list exactly
- [ ] CL body slots match the cl-template length_style
- [ ] No decorative lines (`border-bottom`, `hr`) anywhere
- [ ] Metadata comment block at top of each file
