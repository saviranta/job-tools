# output-html-style-generator

Generates the HTML/CSS visual layer for a specific job application —
two skeleton files (CV and cover letter) with named content placeholder slots.

The content generators fill the slots. This tool only handles the visual container.

---

## Why this step exists

Keeping visual design separate from content generation means:
- Both documents share a consistent visual identity (same fonts, colors, spacing)
- The cv-generator and cover-letter-generator fill structured slots — they don't write HTML
- Styles are reusable: once you have a clean "startup minimal" or "enterprise formal"
  skeleton, you adapt it per-application rather than regenerating from scratch

---

## Inputs

| File | Source | Required |
|---|---|---|
| `brand-brief.md` | brand-inspector | Yes — drives colors, fonts, layout personality |
| `cv-template.md` | cv-template-generator | Yes — drives CV section list, column layout, density |
| `cover-letter-template.md` | cover-letter-template-generator | Yes — drives CL structure and section slots |
| `job-brief.md` | job-listing-analyzer | Optional — role/company context for any fine-tuning |

---

## Outputs

Two HTML files, saved to the application folder:

**`cv-output.html`**
Complete HTML/CSS skeleton for the CV. Sections match the cv-template section list exactly.
Content slots use `{{SLOT_NAME}}` syntax.

**`cl-output.html`**
Complete HTML/CSS skeleton for the cover letter. Structure matches the cl-template blueprint.
Content slots use `{{SLOT_NAME}}` syntax.

Both files share the same CSS custom properties (colors, fonts, spacing) so they look like
they were designed together.

---

## Slot reference

Slots the content generators are expected to fill:

### CV slots
| Slot | Description |
|---|---|
| `{{CANDIDATE_NAME}}` | Full name |
| `{{CANDIDATE_TITLE}}` | Professional headline |
| `{{CONTACT_LINE}}` | Email · Phone · LinkedIn · Location (formatted inline) |
| `{{PROFILE_SECTION}}` | 2-4 line positioning statement (omit wrapper if not in template) |
| `{{SKILLS_SECTION}}` | Skills block (format depends on template) |
| `{{EXPERIENCE_SECTION}}` | Full experience block (roles + bullets) |
| `{{ROLE_TITLE_N}}` | Role title for role N |
| `{{COMPANY_N}}` | Company name for role N |
| `{{DATES_N}}` | Date range for role N |
| `{{BULLETS_N}}` | Bullet list for role N |
| `{{EDUCATION_SECTION}}` | Education block |
| `{{EXTRAS_SECTION}}` | Certifications, languages, publications, etc. |

### Cover letter slots
| Slot | Description |
|---|---|
| `{{CANDIDATE_NAME}}` | Full name |
| `{{CONTACT_LINE}}` | Email · Phone · LinkedIn |
| `{{DATE}}` | Letter date |
| `{{RECIPIENT}}` | Hiring manager name or "Hiring Team" |
| `{{COMPANY_NAME}}` | Company name |
| `{{ROLE_TITLE}}` | Role being applied for |
| `{{OPENING_PARAGRAPH}}` | First paragraph |
| `{{BODY_BULLETS}}` | 3 bullet points (structured style only — omit otherwise) |
| `{{BODY_PARAGRAPH_1}}` | Body paragraph 1 (narrative/short-bold) |
| `{{BODY_PARAGRAPH_2}}` | Body paragraph 2 (narrative only) |
| `{{COMPANY_PARAGRAPH}}` | Company/fit paragraph (narrative only) |
| `{{CLOSING_PARAGRAPH}}` | Closing paragraph |
| `{{SIGNATURE}}` | Sign-off line + name |

---

## Style library

Save generated styles for reuse. Styles encode the *structure and visual pattern*
(two-column, colored header, density, font pairing) — brand colors are applied as
CSS custom properties and can be swapped per-application.

```
templates/
└── styles/
    ├── STYLE-STARTUP-MINIMAL-2COL/
    │   ├── cv-output.html
    │   └── cl-output.html
    └── STYLE-ENTERPRISE-FORMAL-1COL/
        ├── cv-output.html
        └── cl-output.html
```

---

## Workflow position

```
brand-brief.md ──────────────────────────────────────┐
cv-template.md ──────────────────────────────────────┤→ output-html-style-generator
cover-letter-template.md ────────────────────────────┘        ↓
                                              cv-output.html + cl-output.html
                                                              ↓
                          cv-generator → fills cv-output.html → final CV
                 cover-letter-generator → fills cl-output.html → final CL
```
