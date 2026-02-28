# GENERATE-CV-CL — Generate a CV and Cover Letter

The main workflow. Takes a job listing and company, works through all tools
in sequence with your review and approval at each decision point, and produces
a print-ready HTML CV and cover letter.

**Prerequisites:** your asset files must be populated. If not, run `SETUP.md` first.

---

## Add this as a Claude Code skill

Add the following to your `CLAUDE.md` (or create `~/.claude/commands/generate-application.md`)
so you can trigger this workflow with `/generate-application` in any Claude Code session:

```markdown
# /generate-application

Start a CV and cover letter generation session for a job application.

Read and follow the workflow in:
[path to this repo]/personalised-cv-coverletter-generator/GENERATE-CV-CL.md

Ask the user for the job listing URL or text and the company website URL,
then proceed through the full workflow.
```

---

## The Prompt

Paste into Claude Code (or trigger via `/generate-application` if set up as a skill):

---

You are running the full CV and cover letter generation workflow for a job application.

Work through the steps below in sequence. At each decision point, pause and wait for
my explicit approval before proceeding to the next step. Do not skip ahead.

**Start by asking me two questions:**

1. "What is the job listing URL? (Or paste the job description text if you don't have a URL)"
2. "What is the company website URL?"

Then ask: "What is your workspace path?" (e.g. `~/cv-workspace`)

Wait for all three answers, then proceed.

---

### STEP 1 — Analyse the job listing

Read: `job-listing-analyzer/job-listing-prompt.md`

Follow its instructions using the job URL or pasted text provided.
If a URL was given, use Chrome MCP to read it directly (Option B in the prompt).
If text was pasted, use that (Option A).

Save output as: `[workspace]/applications/[company]-[role]-[date]/job-brief.md`

After saving, show me a 5-line summary of the job brief:
- Role and seniority
- Top 3 clusters activated
- Positioning angle
- Top 3 capabilities to highlight
- Any gap flags

Ask: "Does this job brief look right? Reply **go** to continue, or tell me what's off."

---

### STEP 2 — Analyse the company (run in parallel with Step 1 if possible)

Read: `job-listing-analyzer/company-analyzer-prompt.md`

Follow its instructions using the company URL provided. Use Chrome MCP (Option A).

Save output as: `[workspace]/applications/[company]-[role]-[date]/company-brief.md`

After saving, show me:
- Company snapshot (one line)
- Top 2 connection points to use
- Tone calibration summary

Then proceed to Step 3 without waiting — both briefs feed into it.

---

### STEP 3 — Inspect the brand

Read: `brand-inspector/brand-inspector-prompt.md`

Follow its instructions using the company URL. Use Chrome MCP (Option A).
Focus on: homepage, about page, careers page, and any press kit or design system link.

Save output as: `[workspace]/applications/[company]-[role]-[date]/brand-brief.md`

After saving, show me:
- Color palette (primary + accent)
- Font pairing
- Design personality (one sentence)
- Cover letter tone guidance (one sentence)

Ask: "Does the brand brief look right? Reply **go** to continue."

---

### STEP 4 — Select or generate CV template

Read: `cv-template-generator/template-selector-prompt.md`

Check `[workspace]/templates/cv/` for existing templates.
Paste metadata headers from all templates found there into the selector.
Use the job-brief to score matches.

Show me the recommendation:
- If strong match: which template, what adaptations needed
- If no match: pre-filled answer block for the generator

Ask: "Use existing template or generate new? Reply **use [TMPL-ID]** or **generate new**."

If generating new: read `cv-template-generator/template-generator-prompt.md` and run it.
Save the generated template to `[workspace]/templates/cv/[TMPL-ID].md`.

Copy the chosen template to: `[workspace]/applications/[company]-[role]-[date]/cv-template.md`
Apply any brand color/font adaptations from the brand-brief now.

---

### STEP 5 — Select or generate cover letter template

Read: `cover-letter-template-generator/template-selector-prompt.md`

Check `[workspace]/templates/cover-letter/` for existing templates.
Same process as Step 4.

Ask: "Use existing CL template or generate new?"

Save chosen template to: `[workspace]/applications/[company]-[role]-[date]/cover-letter-template.md`

---

### STEP 6 — Select or generate HTML style

Read: `output-html-style-generator/style-selector-prompt.md`

Check `[workspace]/templates/styles/` for existing styles.
Note: color mismatches are not disqualifying — CSS custom properties make swaps trivial.

Ask: "Use existing style or generate new?"

If generating new: read `output-html-style-generator/style-generator-prompt.md` and run it.
Save the generated style to `[workspace]/templates/styles/[STYLE-ID]/`.

Copy both files to the application folder:
- `[workspace]/applications/[company]-[role]-[date]/cv-output.html`
- `[workspace]/applications/[company]-[role]-[date]/cl-output.html`

Apply brand color/font adaptations to both files now (update `:root` CSS variables).

---

### STEP 7 — Generate the CV

Read: `cv-generator/cv-generator-prompt.md`

Fill in the file paths section using:
- ASSETS_FOLDER: `[workspace]/assets/`
- CV_TEMPLATE: `[workspace]/applications/[company]-[role]-[date]/cv-template.md`
- HTML_SKELETON: `[workspace]/applications/[company]-[role]-[date]/cv-output.html`
- JOB_BRIEF: `[workspace]/applications/[company]-[role]-[date]/job-brief.md`
- BRAND_BRIEF: `[workspace]/applications/[company]-[role]-[date]/brand-brief.md`
- APPLICATION_FOLDER: `[workspace]/applications/[company]-[role]-[date]/`
- OUTPUTS_FOLDER: `[workspace]/outputs/`

Run all four phases, pausing at each gate for approval.

---

### STEP 8 — Generate the cover letter

Read: `cover-letter-generator/cover-letter-generator-prompt.md`

Fill in the file paths using the same application folder.
Add:
- COMPANY_BRIEF: `[workspace]/applications/[company]-[role]-[date]/company-brief.md`
- WRITING_STYLE: `[workspace]/writing-style.md` (if it exists)
- PHRASE_LIBRARY: `[workspace]/phrase-library.md` (if it exists)

Run all four phases, pausing at each gate for approval.

---

### STEP 9 — Review

Read: `cv-and-cl-reviewer/reviewer-prompt.md`

Use the approved `.md` files from Steps 7 and 8.
Run all six personas and present the cross-persona priority summary.

Ask: "Which recommendations would you like to apply?
Reply with persona names, item numbers, or 'none'."

Apply chosen changes. Sync back to `.md` files and HTML outputs.

---

### STEP 10 — Final outputs

Confirm both files are saved in `[workspace]/outputs/`:
- `YYYYMMDD_[surname]_[company]_cv.html`
- `YYYYMMDD_[surname]_[company]_cl.html`

Tell me:

```
═══════════════════════════════════════════════
APPLICATION COMPLETE
═══════════════════════════════════════════════

CV:            outputs/YYYYMMDD_[surname]_[company]_cv.html
Cover letter:  outputs/YYYYMMDD_[surname]_[company]_cl.html

TO EXPORT AS PDF:
  1. Open each file in Chrome
  2. Cmd+P (Mac) or Ctrl+P (Windows)
  3. Destination → Save as PDF
  4. Paper size: A4
  5. Margins: None
  6. ✓ Background graphics

Application folder: applications/[company]-[role]-[date]/
  All working files, briefs, and templates are saved here.
═══════════════════════════════════════════════
```

---

## Other useful workflows

Two additional workflows worth building later:

**MAINTAIN.md** — Quarterly asset health check.
Runs `asset-setup/maintenance/review-prompt.md` across all five asset files,
surfaces outdated entries and unfilled placeholders, checks whether your
template library still reflects your current career stage, and prompts targeted updates.
Run every 3 months or before starting a job search.

**POST-INTERVIEW.md** — After-interview capture.
Records what was asked, what landed well, what was challenged.
Updates capabilities.md with any new evidence surfaced, adds effective phrasings
to the phrase library, notes which template and approach worked (or didn't),
and flags anything to strengthen before the next round or application.
Run within 24 hours of an interview while it's fresh.
