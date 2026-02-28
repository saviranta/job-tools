# cv-generator

Generates a tailored CV for a specific job application in four human-reviewed phases.

Each phase pauses for your review and approval before proceeding.
The markdown file is the canonical reviewed draft — the HTML is derived from it.
Manual HTML edits are synced back to the markdown and optionally to your asset files.

---

## Four phases

```
Phase 1: Pre-flight check
  → verifies all files are present
  → shows selection summary (template, clusters, roles, profile)
  → waits for user approval

Phase 2: Markdown draft
  → generates cv.md — full CV in human-readable markdown
  → waits for user review and approval (edit requests handled here)

Phase 3: HTML generation
  → fills cv-output.html slots from approved cv.md
  → saves to outputs/YYYYMMDD_surname_company.html
  → user opens in browser or PDF viewer to review

Phase 4: Edit sync
  → guides user on where to make manual HTML edits
  → after edits: user describes changes, Claude updates cv.md
  → checks if edits reveal improvements worth saving back to assets
```

---

## File naming

All files — working and final — use the same prefix: `YYYYMMDD_surname_company`

```
20260228_smith_acme_cv.md        ← reviewed markdown draft
20260228_smith_acme_cv.html      ← final print-ready CV
```

Saved to the application folder and `outputs/` respectively.
No generic filenames — every file unambiguously identifies the specific application.

---

## File hierarchy

```
assets/ ──────────────────────────────────────────→ YYYYMMDD_[surname]_[company]_cv.md
job-brief.md ─────────────────────────────────────→              ↓
cv-template.md ───────────────────────────────────→ YYYYMMDD_[surname]_[company]_cv.html
cv-output.html (skeleton) ────────────────────────→              ↓
                                  outputs/YYYYMMDD_[surname]_[company]_cv.html
```

Manual edits to the HTML are reflected back up to the .md and optionally to assets.

---

## Required inputs

| File | Source | Required |
|---|---|---|
| `assets/*.md` | asset-setup | Yes — all five files |
| `cv-template.md` | cv-template-generator | Yes |
| `cv-output.html` | output-html-style-generator | Yes |
| `job-brief.md` | job-listing-analyzer | Yes |
| `brand-brief.md` | brand-inspector | Recommended |

---

## Output files

| File | Location | Description |
|---|---|---|
| `YYYYMMDD_surname_company_cv.md` | application folder | Reviewed markdown draft |
| `YYYYMMDD_surname_company_cv.html` | `outputs/` | Final print-ready CV |
