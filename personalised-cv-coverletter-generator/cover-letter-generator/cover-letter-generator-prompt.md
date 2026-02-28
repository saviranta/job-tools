# Cover Letter Generator Prompt

Generates a tailored cover letter in four human-reviewed phases.
Run in Claude Code — it reads your files, writes outputs, and pauses at each gate.

**How to use:**
1. Fill in the file paths below
2. Paste the full prompt into Claude Code
3. Review and approve at each phase before Claude proceeds

---

## Your file paths

```
ASSETS_FOLDER:              [path to your assets/ folder]
CL_TEMPLATE:                [path to cover-letter-template.md]
HTML_SKELETON:              [path to cl-output.html from output-html-style-generator]
JOB_BRIEF:                  [path to job-brief.md]
COMPANY_BRIEF:              [path to company-brief.md]
BRAND_BRIEF:                [path to brand-brief.md — or leave blank]
WRITING_STYLE:              [path to writing-style.md — or leave blank]
PHRASE_LIBRARY:             [path to phrase-library.md — or leave blank]
APPLICATION_FOLDER:         [path to applications/company-role-date/ folder]
OUTPUTS_FOLDER:             [path to outputs/ folder]
YOUR_SURNAME:               [your surname, lowercase, no spaces]
COMPANY_NAME:               [company name, lowercase, no spaces]
```

---

## The Prompt

---

You are generating a tailored cover letter for a specific job application.
Work through four phases. Pause at the end of each phase and wait for explicit
user approval before proceeding.

All files use the naming format `YYYYMMDD_[surname]_[company]_cl.*` where the date
is today. No generic filenames.

---

## PHASE 1: Pre-flight check

Read all input files. Do not generate any content yet.

**Step 1a — Verify files**

| File | Status | Notes |
|---|---|---|
| assets/capabilities.md | ✓ Found / ✗ Missing | [entry count] |
| assets/qualities_workstyle.md | ✓ Found / ✗ Missing | |
| assets/profiles.md | ✓ Found / ✗ Missing | [profile count] |
| cover-letter-template.md | ✓ Found / ✗ Missing | [template ID] |
| cl-output.html | ✓ Found / ✗ Missing | [structure: short-bold/structured/narrative] |
| job-brief.md | ✓ Found / ✗ Missing | |
| company-brief.md | ✓ Found / ✗ Missing | |
| brand-brief.md | ✓ Found / — Not provided | |
| writing-style.md | ✓ Found / — Not provided | [warn if missing — voice constraints won't apply] |
| phrase-library.md | ✓ Found / — Not provided | |

If any required file is missing: stop and tell the user what's needed.

**Step 1b — Selection summary**

```
═══════════════════════════════════════════════
COVER LETTER GENERATION PLAN
YYYYMMDD_[surname]_[company]_cl
═══════════════════════════════════════════════

TEMPLATE
  ID:         [cover-letter-template id]
  Structure:  [short-bold / structured / narrative]
  Target:     [word count range from template]
  Tone:       [tone from template]

OPENING
  Approach:   [bold-claim / storytelling / direct / company-first]
  Phrase lib: [N opening phrases available — or "none, will generate fresh"]

EMPHASIS AREAS (priority order from template)
  1. [emphasis item]
  2. [emphasis item]
  [...]

POSITIONING ANGLE
  [1-2 sentence angle from job-brief]

EVIDENCE TO DRAW ON
  [top 2-3 capability/accomplishment titles from job-brief shortlist,
   most relevant to the CL emphasis areas]

COMPANY CONNECTION POINTS (from company-brief)
  1. [specific connection point + suggested one-liner]
  2. [specific connection point + suggested one-liner]

KEYWORDS TO WEAVE IN
  [subset of job-brief keywords relevant to a cover letter — not the full list]

HUMAN CHARACTER
  [list of selected techniques from cl-template, or "None — clean prose"]

PHRASE LIBRARY MATCHES
  [For each section with available phrases, list count:
   Opening: N | Skills bridge: N | Closing: N | etc.]

WRITING STYLE
  [Brief: tone summary from writing-style.md, or "Not provided"]
  Red flags to avoid: [list from writing-style.md, or "None provided"]

OUTPUT FILES
  Draft:  [APPLICATION_FOLDER]/YYYYMMDD_[surname]_[company]_cl.md
  Final:  [OUTPUTS_FOLDER]/YYYYMMDD_[surname]_[company]_cl.html
═══════════════════════════════════════════════
```

Ask: "Does this look right? Reply **go** to generate the cover letter draft,
or tell me what to adjust."

---

## PHASE 2: Markdown draft

Wait for Phase 1 approval before starting.

Generate `YYYYMMDD_[surname]_[company]_cl.md` and save it to the application folder.

**Before writing — rules to load:**

Read and hold in context:
- The cl-template structural blueprint (section order, length per section, emphasis per section)
- The human character instructions block from the cl-template
- The voice constraints from writing-style.md (vocabulary, sentence rhythm, red flags)
- Available phrases from phrase-library.md for each section

**Content rules:**

*Opening*
- Follow the opening approach from cl-template
- Must not start with "I"
- Must not use phrases flagged in writing-style.md red flags
  (e.g. "I am writing to express my interest", "I am passionate about", "team player")
- Embed the positioning angle from job-brief within the first 2-3 sentences
- If phrase-library has a suitable opening, use or adapt it — note which one
- If generating fresh: lead with a specific observation, claim, or moment —
  not a restatement of the job title

*Body sections — adapt to cl-template length_style:*

**short-bold:**
- One proof point only — the strongest from the job-brief capability shortlist
- 2-3 sentences maximum; every word earns its place
- Mirror 1-2 keywords from the job-brief list

**structured (opening + 3 bullets + closing):**
- Each bullet maps to one emphasis area (in priority order from cl-template)
- Bullet format: outcome or claim first, evidence second, 1-2 lines each
- Draw evidence from capabilities.md entries — lead with the metric or result
- Metrics rule: use metrics exactly as they appear in the source entry. Do not round,
  extrapolate, or improve them. If no metric exists, describe the outcome without one.
- Mirror keywords naturally across the three bullets — not all in one

**narrative (body paragraphs):**
- Paragraph 1: strongest emphasis areas + evidence woven into prose
- Paragraph 2: secondary emphasis areas, career story or trajectory if selected
- Do not use sub-headings — this is flowing prose
- Paragraph length: match writing-style.md rhythm guidance
- Each paragraph has a clear purpose — no filler sentences

*Company connection paragraph (all styles except short-bold):*
- Draw from company-brief connection points — use 1-2 specific references
- Every specific claim in this paragraph must be traceable to a named item in
  company-brief.md. Do not speculate about challenges, initiatives, or priorities
  not documented there.
- One of: reference a product decision, initiative, published piece, or stated value
- Connect it to your own experience or perspective — not just praise
- If "constructive company insight" was selected in emphasis: this is where it lives —
  name only a challenge explicitly documented in company-brief, and connect it to
  what you bring. Do not infer or fabricate company problems.
- Use vocabulary from company-brief values language section
- Do not: use generic superlatives ("incredible mission", "innovative company")

*Closing:*
- Match the closing approach from cl-template
- If phrase-library has a suitable closing, use or adapt it — note which one
- Include salary / availability if specified in cl-template closing approach
- End with intention — not an apology ("I hope to hear from you") or
  an overclaim ("I know I am the perfect candidate")

**Voice application:**

If writing-style.md was provided:
- Apply sentence rhythm guidance throughout
- Use vocabulary from the "words to use" list where natural
- Eliminate any phrase on the red flags list — check the full draft before saving
- Match the formality level from the tone profile

**Human character application:**

Apply each technique specified in the cl-template human_character instructions.
After the draft, append a hidden comment block noting where each technique was used:

```
<!-- HUMAN CHARACTER APPLIED
  varying-sentence-lengths: paragraphs 1 and 2
  em-dash: "work — and I'd do it again" in paragraph 1
  parenthetical: "(something I'd noticed before seeing this role)" in company paragraph
  [etc.]
-->
```

This comment does not appear in the HTML output — it's for your reference only.

**Word count:**

After generating, display:
```
Word count: [N words]
Target:     [range from cl-template]
Status:     [On target / [N] words over — suggest cuts / [N] words under — suggest additions]
```

If over target by more than 15%: identify the weakest sentence(s) and suggest cuts
before asking for approval.

**Save the file, display its full contents in the chat.**

Ask: "Review `YYYYMMDD_[surname]_[company]_cl.md`. Reply **approved** to generate the HTML,
or tell me what to change. Word count is [N] (target: [range]).

You can request changes to specific sections or ask me to adjust the tone, emphasis,
or a specific phrase. I'll regenerate, save, and show you the updated version."

Iterate — regenerate, save, display word count, ask again — until user replies **approved**.

---

## PHASE 3: HTML generation

Wait for Phase 2 approval before starting.

Read the approved `YYYYMMDD_[surname]_[company]_cl.md` and the `cl-output.html` skeleton.

**Slot filling:**

Map each section of the markdown to its `{{SLOT_NAME}}` in the skeleton:

| Markdown section | Slot |
|---|---|
| Opening paragraph | `{{OPENING_PARAGRAPH}}` |
| Bullet 1/2/3 (structured) | `{{BODY_BULLETS}}` — as `<li>` items |
| Body paragraph 1 | `{{BODY_PARAGRAPH_1}}` |
| Body paragraph 2 | `{{BODY_PARAGRAPH_2}}` |
| Company paragraph | `{{COMPANY_PARAGRAPH}}` |
| Closing paragraph | `{{CLOSING_PARAGRAPH}}` |
| Sign-off | `{{SIGNATURE}}` |
| Candidate name | `{{CANDIDATE_NAME}}` |
| Contact line | `{{CONTACT_LINE}}` |
| Date | `{{DATE}}` |
| Recipient | `{{RECIPIENT}}` |
| Company name | `{{COMPANY_NAME}}` |
| Role title | `{{ROLE_TITLE}}` |

Strip the `<!-- HUMAN CHARACTER APPLIED -->` comment block before filling slots —
it must not appear in the HTML output.

Do not modify any CSS or structural HTML — slot content only.

**Save to:** `[OUTPUTS_FOLDER]/YYYYMMDD_[surname]_[company]_cl.html`

Confirm save, then tell the user:

```
Cover letter saved to:
outputs/YYYYMMDD_[surname]_[company]_cl.html

Open in your browser to review. Print to PDF: Cmd+P → Save as PDF.

When you've reviewed it, reply:
  - approved — if it looks right
  - [describe edits needed] — I'll guide you to the right place in the HTML
```

---

## PHASE 4: Manual edit guidance and sync

**If the user approves without edits:** confirm completion and list all output files.

**If the user describes edits:**

For each edit, specify:
- Exact slot or HTML element to find (`{{SLOT_NAME}}` or CSS class)
- What to change
- Whether it's a content edit (sync to .md) or visual edit (HTML only)

After the user confirms edits are done:

**1. Update the .md file** with any content changes. Save it.

**2. Check for phrase library additions:**
Did any sentence in the final letter work particularly well?
For each strong line, suggest adding it to phrase-library.md:

```
Suggest adding to phrase-library.md:

Section: [Opening / Skills bridge / Company connection / Closing / etc.]
Phrase: "[the line]"
Tone tag: [formal / warm / direct / narrative / bold]
Note: [optional — when to use]
```

Ask: "Would you like me to add these to your phrase library?"
If yes: read the current phrase-library.md, add the entries, save.

**3. Check for writing-style.md refinements:**
Did the iteration surface anything about your voice — a phrasing you preferred,
a structure that felt more natural, a red flag to add?
If yes, suggest the specific update and ask permission before saving.

**4. Final summary:**

```
═══════════════════════════════════════════════
COVER LETTER COMPLETE
═══════════════════════════════════════════════
Draft:   applications/[folder]/YYYYMMDD_[surname]_[company]_cl.md
Final:   outputs/YYYYMMDD_[surname]_[company]_cl.html

Print to PDF: open in Chrome → Cmd+P → Save as PDF
             Settings: A4, margins None, background graphics ON
═══════════════════════════════════════════════
```
