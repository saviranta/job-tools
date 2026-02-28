# cv-template-generator

Generates tailored CV structures and saves them to a personal template library.
Templates are reusable — once created, they can be selected automatically for
future applications with a matching context.

---

## Why a template library, not one-off templates

A template encodes a set of structural decisions (ATS vs designed, seniority level,
company type, domain, expertise area, length). Those decisions don't change every application —
a senior PM at a fintech scale-up applies roughly the same structure each time.

Maintaining a library means:
- Most applications just pick a template, not generate one
- You build up tested, refined structures over time
- The job analyzer can recommend the right template automatically

---

## Template library structure

Keep your templates in a `templates/` folder alongside your `assets/`:

```
your-cv-setup/
├── assets/
├── templates/
│   ├── TMPL-STARTUP-PM-ATS.md
│   ├── TMPL-ENTERPRISE-DIR-DESIGNED.md
│   └── TMPL-AGENCY-IC-1PAGE.md
└── applications/
    └── company-role-2025/
        ├── job-brief.md
        ├── brand-brief.md
        ├── company-brief.md
        └── cv-template.md   ← copy of chosen template (may be lightly adapted)
```

Each template file has a **metadata header** at the top that describes what context it's
built for. This is what the selector reads when matching to a job.

---

## Recommended workflow

```
1. job-listing-analyzer   → job-brief.md
   brand-inspector        → brand-brief.md   (run in parallel)

2. template-selector-prompt.md
   → checks templates/ against job-brief
   → recommends an existing template OR says "generate new"

3a. If match found:
    copy matching template to applications/company-role-2025/cv-template.md
    (lightly adapt if brand-brief suggests different colors/fonts)

3b. If no match:
    template-generator-prompt.md → new template → save to templates/ library
    copy to applications/company-role-2025/cv-template.md

4. cv-generator
   ← assets/ + job-brief.md + brand-brief.md + cv-template.md
   → your tailored CV
```

---

## Inputs

**Required:**
- Answers to the nine context questions (in `template-generator-prompt.md`)

**Optional but recommended:**
- `brand-brief.md` from brand-inspector → informs visual styling
- `job-brief.md` from job-listing-analyzer → informs section emphasis

---

## Output: cv-template.md

A template file with:
- A **metadata header** (used by the selector for matching)
- Template summary
- Page setup and ATS constraints
- Header specification
- Ordered section list
- Per-section brief (format, length, emphasis, asset source)
- Visual parameters (from brand-brief or sensible defaults)
- Domain and expertise calibration notes
- cv-generator instructions block
