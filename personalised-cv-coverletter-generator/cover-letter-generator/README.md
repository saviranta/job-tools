# cover-letter-generator

Generates a tailored cover letter in four human-reviewed phases.
Same pattern as the cv-generator — pauses at each gate for your review and approval.

---

## Four phases

```
Phase 1: Pre-flight check
  → verifies all files are present
  → shows selection summary (template, emphasis areas, tone, human character,
    company connection points, phrase library matches)
  → waits for user approval

Phase 2: Markdown draft
  → generates YYYYMMDD_[surname]_[company]_cl.md
  → applies writing-style.md voice constraints and red flags
  → draws from phrase-library.md where available
  → applies human character techniques from cl-template
  → shows word count against target
  → iterates until user replies 'approved'

Phase 3: HTML generation
  → fills cl-output.html slots from approved markdown
  → saves to outputs/YYYYMMDD_[surname]_[company]_cl.html

Phase 4: Edit sync
  → guides manual HTML edits with exact element locations
  → syncs content edits back to .md
  → checks for phrase library additions (good lines get saved)
  → checks for writing-style.md refinements
```

---

## File naming

All files use `YYYYMMDD_[surname]_[company]_cl.*` — no generic filenames.

---

## Required inputs

| File | Source | Required |
|---|---|---|
| `assets/capabilities.md` | asset-setup | Yes |
| `assets/qualities_workstyle.md` | asset-setup | Yes |
| `assets/profiles.md` | asset-setup | Yes |
| `cover-letter-template.md` | cover-letter-template-generator | Yes |
| `cl-output.html` | output-html-style-generator | Yes |
| `job-brief.md` | job-listing-analyzer | Yes |
| `company-brief.md` | company-analyzer | Yes |
| `brand-brief.md` | brand-inspector | Recommended |
| `writing-style.md` | cover-letter-template-generator/onboarding | Recommended |
| `phrase-library.md` | cover-letter-template-generator/phrase-library | Optional |

---

## Output files

| File | Location | Description |
|---|---|---|
| `YYYYMMDD_[surname]_[company]_cl.md` | application folder | Reviewed markdown draft |
| `YYYYMMDD_[surname]_[company]_cl.html` | `outputs/` | Final print-ready cover letter |
