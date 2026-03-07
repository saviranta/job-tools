# Personalised CV and Cover Letter Generator

A prompt-based system for generating tailored, print-ready CVs and cover letters
from a personal career asset library. Runs in Claude Code. Human-reviewed at every
decision point — no content is written or saved without your approval.

---

## How it works

You maintain a library of career assets — your experience, capabilities, competency
clusters, positioning profiles, motivations, and differentiators. When you apply for
a role, the system analyses the job listing and company, selects the right content from
your library, surfaces role-specific differentiators and genuine motivations, generates
a CV and cover letter in structured markdown, fills them into a branded HTML template,
and runs a seven-persona review. You approve or adjust at each stage.

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
Also prompts you to add your **profile photo** (`assets/profile-photo.jpg`) — it appears in all CV and cover letter headers automatically.

**Step 2 — Fill in your asset files**
Open `asset-setup/QUICKSTART.md` for the three paths to get started:
existing CV, LinkedIn profile, or from scratch.

**Step 3 — Apply for a role**
Run `GENERATE-CV-CL.md` (or trigger `/generate-application` if you've set it up as a Claude Code skill).

---

## System overview

```
asset-setup/                     Career asset library templates and onboarding
motivation-wizard/               Build your motivation library; extract role-specific motivation per application
differentiator-explorer/         Build your differentiator library; surface 2–3 role-specific anchors per application
job-listing-analyzer/            Analyse job listings and company websites
brand-inspector/                 Decode company visual and tone identity
cv-template-generator/           Design CV structure for different contexts
cover-letter-template-generator/ Design cover letter structure and voice profile
output-html-style-generator/     Generate branded HTML/CSS output skeletons
cv-generator/                    Generate tailored CV (4 phases, human-reviewed)
cover-letter-generator/          Generate tailored cover letter (4 phases, human-reviewed)
cv-and-cl-reviewer/              Seven-persona review with prioritised feedback
eval/                            Mechanical checks and qualitative eval prompt
```

**Workflow files at root:**
- `SETUP.md` — first-time workspace setup
- `GENERATE-CV-CL.md` — full application generation workflow

**Session break points** are built into the workflow. The full run can be split across
sessions: the application folder with all brief and template files is saved at each
break point so you can resume without losing context.

---

## Asset library

Your career data lives in your workspace `assets/` folder:

| File | Contents |
|------|----------|
| `profile-photo.jpg` | Your profile photo — referenced automatically in all CV and CL headers |
| `work_experience.md` | Role history with unique role IDs (ROLE-001, etc.) |
| `capabilities.md` | Capability and accomplishment entries, tagged and cross-referenced. Split into an INDEX (for fast Phase 1 selection) and ENTRIES (full content, loaded by CAP-ID in Phase 2) |
| `competency_clusters.md` | Grouped skill areas with trigger keywords for job ad matching |
| `qualities_workstyle.md` | Working style, leadership approach, personal attributes |
| `profiles.md` | Positioning statements for different target contexts |
| `motivation-library.md` | Curated motivation entries built by the Motivation Wizard (one-time setup, updated over time) |
| `differentiators.md` | What makes you genuinely distinct — built by the Differentiator Explorer (one-time setup, updated over time) |

Assets are the single source of truth. The generators draw content only from these
files — nothing is invented. Metrics are used verbatim.

**`motivation-library.md` and `differentiators.md` are optional but strongly recommended.**
When present, the cover letter generator treats role-specific motivation and differentiator
framings as protected content — they must appear in the letter substantively intact and cannot
be diluted into generic enthusiasm language.

---

## Eval and tracing

Every completed application saves a `trace.md` to its folder: templates used, capabilities
selected, keyword hit rate, iteration counts, and guardrail results.

Two optional eval tools run post-generation:

**`eval/eval.py`** — mechanical checks (run any time, no prompting needed):
- Keyword coverage: how many job-brief keywords appear in the CV and CL
- Citation integrity: source comments in the CV traced back to real asset entries
- Metric integrity: numbers in CV bullets verified against asset entries verbatim

**`eval/eval-prompt.md`** — qualitative eval (paste into Claude Code):
- Positioning fit, evidence prominence, company paragraph specificity, claim-to-evidence balance
- Scores 1–3 per rubric; 10–12 total = ready to send

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
  Nothing is invented. Metrics are used verbatim. Source citations are embedded in every
  CV bullet so the trail back to the asset is always traceable.
- **Human approval at every gate** — no file is saved without explicit confirmation.
  Asset files require the phrase "update assets" to write.
- **Lazy asset loading** — capabilities are indexed separately from their full content.
  Phase 1 reads only the index to score and shortlist entries; Phase 2 loads only the
  selected entries. This keeps context lean without sacrificing quality.
- **Profile photo by default** — all CV and CL HTML outputs include a circular profile
  photo in the header. Place `profile-photo.jpg` in your assets folder once; it's used
  in every application automatically.
- **Brand inspector is optional** — you can choose to match your output to the company's
  visual brand (recommended) or skip to a generic professional style. If you run the
  inspector, you can also drop screenshots into `brand-brief-assets/` and describe what
  to notice in each — giving the tool visual confirmation rather than inference.
- **A4-paginated HTML output** — the CV uses explicit page divs (`.cv-page-brochure`
  for page 1, `.cv-page-extended` for pages 2+) rather than CSS page-break hints.
  This produces reliable pagination when printing to PDF from Chrome.
- **Reusable templates and styles** — CV templates, CL templates, and HTML styles
  accumulate in a library. The selector checks the library before generating new.
- **Seven-persona review** — ATS, HR Recruiter, Hiring Manager, Role Expert, CEO/CFO/Legal,
  Narrative Copywriter, Authenticity & Distinction Reviewer. Contradictory recommendations
  are surfaced before applying. The seventh persona specifically checks for AI-pattern flags,
  generic application risk, motivation authenticity, and differentiator presence.
- **Workspace separation** — this repo contains tools only. Your personal data
  (assets, templates, applications, outputs) lives in your workspace, never here.
- **Eval by default** — every run produces a trace log. Mechanical checks and a
  qualitative eval prompt are available for post-generation integrity checking.

---

## Repo structure

```
personalised-cv-coverletter-generator/
├── SETUP.md
├── GENERATE-CV-CL.md
├── README.md                        ← you are here
├── asset-setup/
│   ├── QUICKSTART.md
│   ├── assets/                      ← seven .template.md files
│   ├── onboarding/                  ← linkedin, pdf, and quickstart prompts
│   └── maintenance/                 ← quick-add and update-guide prompts
├── motivation-wizard/               ← motivation-wizard-prompt.md
├── differentiator-explorer/         ← differentiator-explorer-prompt.md
├── job-listing-analyzer/
├── brand-inspector/
├── cv-template-generator/
├── cover-letter-template-generator/
│   └── onboarding/                  ← writing-style wizard
├── output-html-style-generator/
├── cv-generator/
├── cover-letter-generator/
├── cv-and-cl-reviewer/              ← seven-persona review
└── eval/
    ├── eval.py                      ← mechanical checks script (Python, stdlib only)
    ├── eval-prompt.md               ← qualitative eval prompt
    └── README.md
```
