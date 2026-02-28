# POST-INTERVIEW — After-Interview Capture

Run this within 24 hours of an interview, while the detail is still fresh.
Captures what happened, extracts what to strengthen, and feeds improvements
back into your assets and phrase library.

**Takes 15–30 minutes. The longer you wait, the less you'll remember.**

---

## The Prompt

Paste into Claude Code:

---

You are running a post-interview debrief and asset update session.

Start by asking two questions:

1. **"Which application was this interview for?"**
   (Give me the company name and role, or the application folder name)

2. **"What stage was this?"**
   - First screen / recruiter call
   - Hiring manager interview
   - Panel or cross-functional interview
   - Technical / skills assessment
   - Final round
   - Other: [describe]

Wait for both answers. Then read the relevant files:
- `[workspace]/applications/[folder]/job-brief.md`
- `[workspace]/applications/[folder]/[surname]_[company]_cv.md`
- `[workspace]/applications/[folder]/[surname]_[company]_cl.md`

This gives context for the debrief. Do not report on these files — just hold them.

---

### PHASE 1: Debrief conversation

Work through the following questions one group at a time.
Ask them conversationally — not as a form. Follow up when answers are thin.

**Group 1: What happened**

- How did it go overall? First instinct — positive, mixed, or uncertain?
- How long did it run, and who was in the room (or on the call)?
- What was the overall format — conversational, structured questions,
  case study, technical test, presentation, something else?

**Group 2: What they asked**

- What were the main questions or topics they covered?
  (Take time here — go through the interview in sequence if it helps)
- Were there any questions that caught you off guard?
- Were there any questions you felt you answered particularly well?
- Were there any questions you felt under-prepared for, or where
  you wish you'd had a better example ready?

**Group 3: What landed**

- Which parts of your background or story seemed to resonate most?
- Did they refer back to anything from your CV or cover letter?
  What specifically?
- Was there a moment where you felt the energy in the conversation shift
  positively? What were you talking about?

**Group 4: What was probed or challenged**

- Did they push back on anything — a claim, a timeframe, a scope?
- Did they ask follow-up questions that suggested scepticism or curiosity?
- Anything where you left feeling your answer wasn't quite convincing?

**Group 5: What you learned about them**

- Did anything come up about the company, team, or role that wasn't in
  the job ad or your research?
- Did they share anything about what they're trying to solve or build?
- What seemed to matter most to them in a candidate?

**Group 6: Outcome and next steps**

- What are the next steps and timeline they gave you?
- How do you feel about your chances? What's your read?
- Is there anything you'd do differently if you had a second round?

---

### PHASE 2: Structured summary

After the debrief conversation, synthesise into a structured debrief document.
Save it as: `[workspace]/applications/[folder]/YYYYMMDD_interview-debrief.md`

Format:

```markdown
# Interview Debrief
[Company] — [Role] — [Stage]
[Date]

## Overall read
[2-3 sentences: how it went, gut feeling, energy in the room]

## Questions asked
[Bulleted list of topics and specific questions remembered]

## What landed well
[Specific moments, topics, or examples that resonated]

## What to strengthen
[Specific topics, examples, or types of question that felt under-prepared]

## New company/role information
[Anything learned that wasn't in the job ad or briefs]

## Next steps
[Timeline and what happens next]

## For next round (if applicable)
[Specific things to prepare, anticipate, or adjust]
```

Show me the debrief document and ask: **"Does this capture it accurately?
Reply yes to save, or tell me what to adjust."**

Save on confirmation.

---

### PHASE 3: Asset update plan

Based on the debrief, identify specific updates across files.
Present the full plan before making any changes.

**Capabilities to strengthen:**
For each topic or question where the answer felt thin or unconvincing,
identify the relevant capabilities.md entry (by title or role ID).
Suggest what to add: a better example, a metric, a more specific outcome.

**Phrasings that landed — add to phrase library:**
For each moment that resonated, extract the essence of what was said.
Suggest the phrase or sentence pattern to save to phrase-library.md,
with the right section and tone tag.

**Profiles to adjust:**
If the interview revealed that their priorities differ from the job-brief framing,
suggest a positioning adjustment in the relevant profile in profiles.md.

**Template notes:**
If the CV structure, emphasis, or cover letter approach clearly worked or didn't,
note this on the relevant template file (add a comment to the metadata block).

**Company brief update:**
If new information about the company emerged, suggest additions to company-brief.md.

Present the plan:

```
═══════════════════════════════════════════════
RECOMMENDED ASSET UPDATES
Based on: [Company] [Role] [Stage] — [Date]
═══════════════════════════════════════════════

CAPABILITIES TO STRENGTHEN:
  1. [entry title] in capabilities.md
     Current: "[current text]"
     Strengthen: [specific suggestion — what example or metric to add]

  2. [entry title]
     Strengthen: [suggestion]

PHRASE LIBRARY ADDITIONS:
  3. Section: [section name]
     Add: "[phrase or pattern]" — [tone tag]
     Why: [what it captured that worked]

PROFILE ADJUSTMENT:
  4. [PROF-N] — [what to adjust and why]

TEMPLATE NOTE:
  5. [TMPL-ID] — add comment: "[what worked or didn't]"

COMPANY BRIEF UPDATE:
  6. Add to company-brief.md: [new information]

NOTHING TO CHANGE:
  • [areas that are solid — no action needed]
═══════════════════════════════════════════════
```

Ask: **"Which updates would you like to make?
Reply with numbers, 'all', or 'none — just save the debrief'."**

---

### PHASE 4: Make updates

For each chosen update, apply the scoped approach from IMPROVER.md:
- Show before/after for every change
- Save only on explicit confirmation

For capabilities: if the user can't remember the specific metric or example
right now, add a targeted `<!-- STRENGTHEN: [what's needed] -->` flag
so it surfaces in the next MAINTAIN run.

---

### PHASE 5: Summary

```
═══════════════════════════════════════════════
POST-INTERVIEW COMPLETE
[Company] — [Role] — [Stage] — [Date]
═══════════════════════════════════════════════

Saved:
  Debrief:       applications/[folder]/YYYYMMDD_interview-debrief.md

Updated:
  [list of files changed]

Flagged for later:
  [any STRENGTHEN flags added]

[If next round exists:]
  Next round prep: review applications/[folder]/YYYYMMDD_interview-debrief.md
  → "For next round" section has your specific prep notes
═══════════════════════════════════════════════
```
