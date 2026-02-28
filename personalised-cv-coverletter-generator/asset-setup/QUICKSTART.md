# asset-setup — Start Here

This tool builds your **career asset library**: five structured files that capture
your experience, skills, and positioning. The downstream tools use them to generate
tailored CVs and cover letters.

---

## Step 1: Choose how to get started

Pick the path that matches what you already have.

### I have a LinkedIn profile
→ [`onboarding/linkedin-parser-prompt.md`](onboarding/linkedin-parser-prompt.md)

Three options: automated scraping with Claude Code, browser-assisted extraction,
or a manual LinkedIn data export. Output: a populated first draft of all five asset files.

### I have an existing CV (PDF or Word)
→ [`onboarding/cv-pdf-parser-prompt.md`](onboarding/cv-pdf-parser-prompt.md)

Two options: paste text into Claude, or drop PDFs into an archive folder
and let Claude Code parse them automatically. Good if you have multiple old CVs.

### I'm starting from scratch
→ [`onboarding/quickstart-prompt.md`](onboarding/quickstart-prompt.md)

A guided conversation — Claude asks the right questions, you answer.
Takes 30–60 minutes. Output will be rough; you'll refine it over time.

---

## Step 2: Understand what you're building

→ [`onboarding/assets-explained.md`](onboarding/assets-explained.md)

Read this to understand the five files, how they connect, and why the structure matters.

---

## Step 3: Save your asset files

After onboarding, save your generated files to an `assets/` folder.
Keep that folder **local and outside this repo** — it contains your personal data.

```
your-assets/
├── work_experience.md
├── capabilities.md
├── competency_clusters.md
├── qualities_workstyle.md
└── profiles.md
```

The `assets/*.template.md` files in this repo show the expected format for each file.

---

## Step 4: Keep your assets current

**When something happens worth capturing:**
→ [`maintenance/quick-add-prompt.md`](maintenance/quick-add-prompt.md) — drop a raw thought, get a formatted entry

**When to update and what:**
→ [`maintenance/update-guide.md`](maintenance/update-guide.md)

**Every quarter or before a job search:**
→ [`maintenance/review-prompt.md`](maintenance/review-prompt.md) — full audit with prioritised gaps

---

## What comes next

Once your asset files are in good shape, use the rest of `personalised-cv-coverletter-generator/`
to generate applications:
- `job-listing-analyzer/` → match your assets to a job ad
- `cv-template-generator/` → design a CV structure for the context
- `cv-generator/` → produce the tailored CV
- `cover-letter-generator/` → produce the cover letter
