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
/YOUR/FULL/PATH/TO/job-tools/personalised-cv-coverletter-generator/GENERATE-CV-CL.md

Ask the user for the job listing URL or text and the company website URL,
then proceed through the full workflow.
```

**Note:** Replace `/YOUR/FULL/PATH/TO/job-tools` with the actual path to where you cloned this repo.

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

### STEPS 1–3 — Analysis (run in sequence, no pauses between)

Steps 1, 2, and 3 each need only the inputs you've already provided.
Run all three, then show the combined summary and wait for one approval.

---

**Step 1 — Analyse the job listing**

Read: `job-listing-analyzer/job-listing-prompt.md`

Follow its instructions using the job URL or pasted text provided.
If a URL was given, use Chrome MCP to read it directly (Option B in the prompt).
If text was pasted, use that (Option A).

Save output as: `[workspace]/applications/[company]-[role]-[date]/job-brief.md`

---

**Step 2 — Analyse the company**

Read: `job-listing-analyzer/company-analyzer-prompt.md`

Follow its instructions using the company URL provided. Use Chrome MCP (Option A).

Save output as: `[workspace]/applications/[company]-[role]-[date]/company-brief.md`

---

**Step 3 — Inspect the brand**

Read: `brand-inspector/brand-inspector-prompt.md`

Follow its instructions using the company URL. Use Chrome MCP (Option A).
Focus on: homepage, about page, careers page, and any press kit or design system link.

Save output as: `[workspace]/applications/[company]-[role]-[date]/brand-brief.md`

---

**After all three are saved, show the combined summary:**

```
JOB BRIEF
  Role and seniority:        [value]
  Top 3 clusters activated:  [value]
  Positioning angle:         [value]
  Top 3 capabilities:        [value]
  Gap flags:                 [value or none]

COMPANY BRIEF
  Snapshot:                  [one line]
  Top 2 connection points:   [value]
  Tone calibration:          [value]

BRAND BRIEF
  Color palette:             [primary + accent hex]
  Font pairing:              [value]
  Design personality:        [one sentence]
  CL tone guidance:          [one sentence]
```

Ask: "Do these briefs look right? Reply **go** to continue, or tell me what to adjust."

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
Show the template and ask: "Does this CV template look right? Reply **yes** to use it, or tell me what to change."

Copy the chosen template to: `[workspace]/applications/[company]-[role]-[date]/[company]-cv-template.md`
Apply any brand color/font adaptations from the brand-brief now.

---

### STEP 5 — Select or generate cover letter template

Read: `cover-letter-template-generator/template-selector-prompt.md`

Check `[workspace]/templates/cover-letter/` for existing templates.
Same process as Step 4.

Ask: "Use existing CL template or generate new?"

If generating new: run the generator. Show the template and ask: "Does this CL template look right? Reply **yes** to use it, or tell me what to change."

Save chosen template to: `[workspace]/applications/[company]-[role]-[date]/[company]-cover-letter-template.md`

---

### STEP 6 — Select or generate HTML style

Read: `output-html-style-generator/style-selector-prompt.md`

Check `[workspace]/templates/styles/` for existing styles.
Note: color mismatches are not disqualifying — CSS custom properties make swaps trivial.

Ask: "Use existing style or generate new?"

If generating new: read `output-html-style-generator/style-generator-prompt.md` and run it.
Save the generated style to `[workspace]/templates/styles/[STYLE-ID]/`.
Ask: "Does this HTML style look right? Reply **yes** to proceed, or tell me what to change."

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
- WRITING_STYLE: `[workspace]/writing-style.md` (if it exists — run cover-letter-template-generator/onboarding/writing-style-wizard.md first to create it)
- PHRASE_LIBRARY: `[workspace]/phrase-library.md` (if it exists)

Run all four phases, pausing at each gate for approval.

---

### STEP 9 — Review

Read: `cv-and-cl-reviewer/reviewer-prompt.md`

Use the approved `.md` files from Steps 7 and 8.
Run all six personas and present the cross-persona priority summary.

Ask: "Which recommendations would you like to apply?
Reply with persona names, item numbers, or 'none'."

Apply chosen changes to the `.md` files. Sync all content changes back to the corresponding HTML output files. Confirm which files were updated.

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

