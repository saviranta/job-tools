# CV Generator Prompt

Generates a tailored CV in four human-reviewed phases.
Run this in Claude Code — it reads your files, writes outputs, and pauses at each
phase gate for your review and approval.

**How to use:**
1. Fill in the file paths below
2. Paste the full prompt into Claude Code
3. Review and approve at each phase before Claude proceeds

---

## Your file paths

Fill these in before pasting:

```
ASSETS_FOLDER:          [path to your assets/ folder]
CV_TEMPLATE:            [path to cv-template.md for this application]
HTML_SKELETON:          [path to cv-output.html from output-html-style-generator]
JOB_BRIEF:              [path to job-brief.md]
BRAND_BRIEF:            [path to brand-brief.md — or leave blank]
APPLICATION_FOLDER:     [path to applications/company-role-date/ folder]
OUTPUTS_FOLDER:         [path to outputs/ folder]
YOUR_SURNAME:           [your surname, lowercase, no spaces]
COMPANY_NAME:           [company name, lowercase, no spaces — e.g. acmecorp]
```

---

## The Prompt

Paste this into Claude Code with the paths filled in above.

---

You are generating a tailored CV for a specific job application.
Work through four phases. Pause at the end of each phase and wait for explicit
user approval before proceeding to the next.

All output files — working and final — use the naming format:
`YYYYMMDD_[surname]_[company]_cv.md` and `YYYYMMDD_[surname]_[company]_cv.html`
where the date is today. No generic filenames.

---

## PHASE 1: Pre-flight check

Read all input files from the paths provided. Do not generate any CV content yet.

**Step 1a — Verify files**

Check each required file exists and is populated. Report status as a table:

| File | Status | Notes |
|---|---|---|
| assets/work_experience.md | ✓ Found / ✗ Missing | [role count if found] |
| assets/capabilities.md | ✓ Found / ✗ Missing | [entry count if found] |
| assets/competency_clusters.md | ✓ Found / ✗ Missing | [cluster count if found] |
| assets/qualities_workstyle.md | ✓ Found / ✗ Missing | |
| assets/profiles.md | ✓ Found / ✗ Missing | [profile count if found] |
| cv-template.md | ✓ Found / ✗ Missing | [template ID if found] |
| cv-output.html | ✓ Found / ✗ Missing | [style ID if found] |
| job-brief.md | ✓ Found / ✗ Missing | |
| brand-brief.md | ✓ Found (optional) / — Not provided | |

If any required file is missing: stop, tell the user what's missing and where to get it.
Do not proceed until all required files are present.

**Step 1b — Selection summary**

Read the cv-template and job-brief and show the user what has been selected
for this application:

```
═══════════════════════════════════════════════
CV GENERATION PLAN
YYYYMMDD_[surname]_[company]_cv
═══════════════════════════════════════════════

TEMPLATE
  ID:       [cv-template id]
  Layout:   [single/two-column/hybrid]
  Length:   [1-page/2-page/unlimited]
  ATS:      [yes/probably/no]

PROFILE
  Using:    [PROF-N name from profiles.md]
  Angle:    [positioning angle from job-brief, 1 sentence]

ROLES TO INCLUDE
  1. [ROLE-ID] — [title, company] (full detail)
  2. [ROLE-ID] — [title, company] (full detail)
  3. [ROLE-ID] — [title, company] (compressed — dates + 1-2 bullets only)
  [as specified in job-brief role selection]

CLUSTERS TO PRIORITISE
  1. [CLUSTER-ID] — [name]
  2. [CLUSTER-ID] — [name]
  3. [CLUSTER-ID] — [name]
  [from job-brief cluster ranking, top 4-6]

CAPABILITIES SHORTLIST
  [N] entries selected from capabilities.md

  Will draw from:
  [ROLE-ID] [Role title]:
    • [capability entry title] — [CAP-ID if present]
    • [capability entry title] — [CAP-ID if present]
    [repeat for each role being included]

  Thin evidence (will omit or frame directionally):
    • [entry title] — [reason: no metric / vague outcome / thin scope]

  Not drawing from (out of scope for this application):
    • [entry title]

KEYWORDS TO MIRROR
  [list from job-brief keywords section]

SECTIONS (in order)
  [numbered list matching cv-template section list]

OUTPUT FILES
  Draft:  [APPLICATION_FOLDER]/YYYYMMDD_[surname]_[company]_cv.md
  Final:  [OUTPUTS_FOLDER]/YYYYMMDD_[surname]_[company]_cv.html
═══════════════════════════════════════════════
```

**Step 1c — Guardrail checks**

Run all four checks silently, then present findings before the approval gate.

*Asset quality gate:*
Count `<!-- FILL IN -->` placeholders and vague capability entries (no metric and no concrete outcome — entries containing only words like "improved", "supported", "helped" with nothing quantified) across the capabilities selected for this application.
If more than 30% of selected entries are unfilled or vague: flag this as a warning — the CV may be thin. List which entries are affected and suggest either strengthening them first or excluding them.

*Cross-reference integrity:*
Verify that every role ID referenced in the selected capabilities entries exists in work_experience.md.
Verify that every cluster in the top-ranked shortlist has at least one matching capability entry.
If any reference is broken: list it and stop — do not proceed until resolved.

*ATS vs layout conflict:*
If the cv-template has `ats: yes` or `ats: probably` AND the layout is two-column: flag this as a conflict. Two-column layouts are frequently misread by ATS parsers. Ask the user to choose: prioritise ATS safety (switch to single-column) or keep the design (accept ATS risk).

*Template length vs content estimate:*
Estimate: given the number of roles included, bullets per role from the cv-template guidance, and sections selected, will the content fit the template's page target?
If the estimate is materially over (e.g. 3-page content in a 1-page template): flag it and suggest either compressing roles or relaxing the page constraint before generation.

Present the results:

```
GUARDRAIL CHECKS
  Asset quality:        [OK / WARNING — N entries thin or unfilled: list]
  Cross-references:     [OK / BROKEN — list broken references]
  ATS vs layout:        [OK / CONFLICT — describe]
  Content vs length:    [OK / OVER — estimate and suggestion]
```

If any check produces a BROKEN or CONFLICT result: do not proceed. Resolve first.
If WARNING results only: the user may still reply **go** to proceed with awareness.

Then ask:
"Does this selection look right and are you happy with the guardrail results?
Reply **go** to generate the CV draft, or tell me what to adjust."

---

## PHASE 2: Markdown draft

Wait for user approval from Phase 1 before starting.

Generate `YYYYMMDD_[surname]_[company]_cv.md` — the full CV in structured markdown.
Save it to the application folder.

**Content rules:**

*Profile / positioning statement*
- Draw from the recommended profile in profiles.md
- Rewrite the opening to embed the job-brief positioning angle
- The rewrite must stay within the language and claims present in the source profile.
  Do not add roles, outcomes, or capabilities not stated in profiles.md.
- Mirror 2-3 keywords from the job-brief keywords list
- Match the cv-template per-section length guidance

*Skills / competencies section (if in template)*
- Draw from the top-ranked clusters in job-brief
- Use the cluster names and trigger keywords as vocabulary
- Format as specified in cv-template (tag cloud / grouped list / inline)

*Work experience — for each included role*
- Open with the role title, company, and dates exactly as in work_experience.md
- Bullets drawn exclusively from capabilities.md entries matching that role's ID,
  filtered by the job-brief capability shortlist
- Each bullet: lead with outcome or impact, not the task
- After each bullet, append a hidden source comment: `<!-- source: [entry title] -->`
  These are stripped in Phase 3 and must not appear in the HTML output.
- Metrics rule: use metrics exactly as they appear in the source entry. Do not round,
  extrapolate, combine, or improve them. If no metric exists in the source, describe
  the outcome without one — do not invent a number.
- Thin evidence rule: if job-brief flags an entry as thin evidence, either omit the
  bullet or frame it directionally ("experience with X", not "led X achieving Y").
  Do not write a confident claim on weak evidence.
- Mirror job-brief keywords naturally — do not force them
- No repeated opening verb across bullets in the same role
- Length: match the cv-template per-section bullet guidance
- Compressed roles: dates + company only, or 1-2 high-level bullets — no detail

*Education, extras*
- Draw from work_experience.md or qualities_workstyle.md as appropriate
- Format as cv-template specifies

**Markdown format:**

Use clear section headers matching cv-template section names exactly.
Within each section, use the format the cv-template specifies (bullets / prose / table).
Do not add HTML — this is the review draft, not the final output.

**After saving the file, display its full contents in the chat.**

Then ask:
"Review `YYYYMMDD_[surname]_[company]_cv.md`. Reply **approved** to generate the HTML,
or tell me what to change. You can request changes section by section or all at once —
I'll regenerate and save the updated file before asking again."

Handle change requests iteratively — regenerate, save, display, ask again —
until the user replies **approved**.

---

## PHASE 3: HTML generation

Wait for Phase 2 approval before starting.

Read the approved `YYYYMMDD_[surname]_[company]_cv.md` and the `cv-output.html` skeleton.

**Slot filling rules:**

- Map each section of the markdown to its corresponding `{{SLOT_NAME}}` in the skeleton
- Convert markdown formatting to HTML fragments:
  - Bullet points → `<li>` items (do not add `<ul>` — the skeleton wraps them)
  - Bold → `<strong>`
  - Role titles, companies, dates → their respective slot elements
- Do not modify any CSS, layout, or structural HTML — only fill slots
- If the markdown has more content than a slot expects, trim to fit;
  if less, do not pad

**Save the completed file** to:
`[OUTPUTS_FOLDER]/YYYYMMDD_[surname]_[company]_cv.html`

**Slot validation — run before confirming save:**
Scan the saved HTML file for any remaining `{{` strings.
If any unfilled slots are found: list them and stop — do not tell the user to open the file.
Resolve each missing slot before proceeding.

Confirm the save, then tell the user:

```
HTML CV saved to:
outputs/YYYYMMDD_[surname]_[company]_cv.html

Open it in your browser to review the visual output.
Print to PDF from your browser (Cmd+P / Ctrl+P → Save as PDF) for the final file.

When you've reviewed it, reply:
  - approved — if it looks right
  - [describe any edits needed] — I'll guide you to the right place in the HTML
```

---

## PHASE 4: Manual edit guidance and sync

Wait for the user to review the HTML output.

**If the user approves without edits:** confirm completion and summarise the output files.

**If the user describes edits needed:**

For each edit requested, tell the user:
- Exactly which `{{SLOT_NAME}}` or HTML element to find in the file
- What to change (the specific text, element, or property)
- Whether this is a content edit (will be synced back to .md) or a visual/layout edit (HTML only)

Format edit guidance as a numbered list:
```
1. Open outputs/YYYYMMDD_[surname]_[company]_cv.html in a text editor
2. Find: <h1 class="candidate-name">{{CANDIDATE_NAME}}</h1>
   Change to: [corrected content]
3. Find: the first <li> in the .role-block for [Role Title]
   Change to: [corrected bullet]
   → This is a content change — update the .md file too (see below)
```

**After the user confirms edits are done:**

1. Update `YYYYMMDD_[surname]_[company]_cv.md` to reflect any content changes
   (visual/layout edits to the HTML are not mirrored to the .md)
   Save the updated .md file.

2. Review the edits and check: does any change reveal something worth saving
   back to the asset files? For example:
   - A better way to phrase a capability bullet → suggest updating capabilities.md
   - A stronger positioning statement → suggest updating profiles.md
   - A new keyword that landed well → suggest adding to competency_clusters.md trigger keywords

   For each suggestion, show the exact formatted entry to add and which file it belongs in.
   Ask: "Would you like me to update [asset file] with this?
   Reply **update assets** to confirm, or **skip** to leave them unchanged."
   Only proceed with asset file writes on receipt of the exact phrase "update assets".

3. Confirm final output:

```
═══════════════════════════════════════════════
CV COMPLETE
═══════════════════════════════════════════════
Draft:   applications/[folder]/YYYYMMDD_[surname]_[company]_cv.md
Final:   outputs/YYYYMMDD_[surname]_[company]_cv.html

Print to PDF: open the HTML in Chrome → Cmd+P → Save as PDF
             Recommended settings: Paper A4, Margins None, Background graphics ON
═══════════════════════════════════════════════
```
