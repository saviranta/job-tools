# Personalised CV and Cover Letter Generator

A prompt-based system for generating tailored, print-ready CVs and cover letters
from a personal career asset library. Runs in Claude Code. Human-reviewed at every
decision point — no content is written or saved without your approval.

---

## How it works

You maintain a library of career assets — your experience, capabilities, competency
clusters, and positioning profiles. When you apply for a role, the system analyses
the job listing and company, selects the right content from your library, generates
a CV and cover letter in structured markdown, fills them into a branded HTML template,
and runs a six-persona review. You approve or adjust at each stage.

Every output file is named `YYYYMMDD_[surname]_[company]_cv.html` (or `_cl.html`) —
no generic filenames, ever.

---

## Getting started

**Prerequisites:**
- Claude Code with file system access
- Chrome browser with the Claude in Chrome MCP extension (for reading job listings and company sites live)
- ~30–60 minutes for initial asset setup (one-time)

**Step 1 — Run SETUP.md**
Creates your personal workspace folder and copies the asset template files.
Your workspace lives on your machine, outside this repo, and is never committed anywhere.

**Step 2 — Fill in your asset files**
Open `asset-setup/QUICKSTART.md` for the three paths to get started:
existing CV, LinkedIn profile, or from scratch.

**Step 3 — Apply for a role**
Run `GENERATE-CV-CL.md` (or trigger `/generate-application` if you've set it up as a Claude Code skill).

---

## System overview

```
asset-setup/                    Career asset library templates and onboarding
job-listing-analyzer/           Analyse job listings and company websites
brand-inspector/                Decode company visual and tone identity
cv-template-generator/          Design CV structure for different contexts
cover-letter-template-generator/ Design cover letter structure and voice profile
output-html-style-generator/    Generate branded HTML/CSS output skeletons
cv-generator/                   Generate tailored CV (4 phases, human-reviewed)
cover-letter-generator/         Generate tailored cover letter (4 phases, human-reviewed)
cv-and-cl-reviewer/             Six-persona review with prioritised feedback
```

**Workflow files at root:**
- `SETUP.md` — first-time workspace setup
- `GENERATE-CV-CL.md` — full application generation workflow

---

## Language support

**This system is English-only.**

All brief files, templates, CV drafts, and cover letter drafts are generated in English.
If a job listing, company website, or any input source is in another language, the system
will translate extracted content to English before processing. The user is informed when
translation has been performed.

**If you need output in another language** (e.g. a Finnish CV for a Finnish company),
the system is not currently configured for this. To add language support, you would need to:

1. Update the language rule in `GENERATE-CV-CL.md` and each analysis prompt
2. Update the cv-generator and cover-letter-generator content rules to target the desired output language
3. Review and localise the asset file templates in `asset-setup/assets/`
4. Consider that ATS keyword matching, phrase library, and writing-style guidance
   will all need language-specific versions

Until then, treat this as an English-language generation tool that can read source
material in any language.

---

## Design principles

- **Assets as source of truth** — all CV and CL content is drawn from your asset library.
  Nothing is invented. Metrics are used verbatim.
- **Human approval at every gate** — no file is saved without explicit confirmation.
  Asset files require the phrase "update assets" to write.
- **Reusable templates and styles** — CV templates, CL templates, and HTML styles accumulate
  in a library. The selector checks the library before generating new.
- **Six-persona review** — ATS, HR Recruiter, Hiring Manager, Role Expert, CEO/CFO/Legal,
  Narrative Copywriter. Contradictory recommendations are surfaced before applying.
- **Workspace separation** — this repo contains tools only. Your personal data
  (assets, templates, applications, outputs) lives in your workspace, never here.

---

## Repo structure

```
personalised-cv-coverletter-generator/
├── SETUP.md
├── GENERATE-CV-CL.md
├── README.md                       ← you are here
├── asset-setup/
│   ├── QUICKSTART.md
│   ├── assets/                     ← five .template.md files
│   ├── onboarding/                 ← linkedin, pdf, and quickstart prompts
│   └── maintenance/                ← quick-add and update-guide prompts
├── job-listing-analyzer/
├── brand-inspector/
├── cv-template-generator/
├── cover-letter-template-generator/
├── output-html-style-generator/
├── cv-generator/
├── cover-letter-generator/
└── cv-and-cl-reviewer/
```
