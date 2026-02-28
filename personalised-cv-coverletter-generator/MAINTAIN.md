# MAINTAIN — Quarterly Asset Health Check

Run this every 3 months, or before starting a job search.
Reviews all five asset files, your template library, and your phrase library.
Surfaces gaps, outdated entries, and quick wins — then you decide what to address.

**Takes 20–40 minutes depending on how much needs updating.**

---

## The Prompt

Paste into Claude Code:

---

You are running a quarterly maintenance check on a career asset library.

Start by asking: **"What is your workspace path?"**

Wait for the answer, then proceed.

---

### PHASE 1: Read everything

Read all of the following files silently — do not report on them yet:

```
[workspace]/assets/work_experience.md
[workspace]/assets/capabilities.md
[workspace]/assets/competency_clusters.md
[workspace]/assets/qualities_workstyle.md
[workspace]/assets/profiles.md
[workspace]/phrase-library.md          (if exists)
[workspace]/writing-style.md           (if exists)
[workspace]/templates/cv/              (list all TMPL-*.md files)
[workspace]/templates/cover-letter/    (list all TMPL-CL-*.md files)
[workspace]/templates/styles/          (list all STYLE-*/style-meta.md files)
```

Also check: `[workspace]/applications/` — list all application folders with dates,
to understand how recently the library has been used.

---

### PHASE 2: Assessment

Assess each area below. Hold findings — present all at once in Phase 3.

**A. Work experience — is it current?**
- Is the most recent role in work_experience.md current? (Check dates)
- Any roles where the title, company name, or scope has since changed?
- Any roles added in the last 3 months that aren't captured yet?

**B. Capabilities — quality and completeness**
- Count entries with no metrics or evidence (`<!-- STRENGTHEN` flags or vague language
  like "improved", "helped", "supported" with nothing quantified)
- Count `<!-- FILL IN -->` placeholders that remain unfilled
- Identify the 3 most recent roles (by role ID) — do they have at least 4-5 strong
  capability entries each? Flag any role with fewer than 3
- Are there clusters in competency_clusters.md that have fewer than 3 capability
  entries linked to them? These are under-evidenced clusters

**C. Profiles — still relevant?**
- Read each profile in profiles.md. Does the target role type still match
  what the user is likely applying for?
- Any profile with language that feels dated, or a positioning angle
  that no longer reflects their seniority or direction?
- Any `<!-- FILL IN -->` left in profiles?

**D. Competency clusters — keywords current?**
- Are trigger keywords up to date with current job ad language?
  (Terms like "GenAI", "LLM", "PLG", "RevOps" have emerged recently —
  are relevant ones present if applicable to this person's field?)
- Any cluster with fewer than 5 trigger keywords?

**E. Qualities and working style — specific enough?**
- Are the entries specific (with examples) or generic ("good communicator")?
- Any `<!-- FILL IN -->` remaining?
- Does it still reflect how the user works, or was it written for an earlier
  version of their career?

**F. Template library — still fit?**
- List all saved CV and CL templates by name and date created
- Any template older than 12 months? Flag for review — career stage may have changed
- Do the saved templates cover the user's current target role types?
  (E.g. if they now target director roles but only have IC templates, flag the gap)

**G. Phrase library — populated?**
- Which sections are empty or have only the starter examples?
- Which sections have 3+ real phrases added?
- Are any phrases that are there likely to have become stale or clichéd?

**H. Recent activity**
- When was the most recent application folder created?
- If more than 3 months ago: note that assets may not reflect recent work
- If recent applications exist: were any improvements fed back from those sessions?
  (Check if post-interview debriefs exist in application folders)

---

### PHASE 3: Present findings

Group findings by priority and present as a single summary:

```
═══════════════════════════════════════════════
ASSET HEALTH CHECK
[date]
═══════════════════════════════════════════════

NEEDS ATTENTION — address before next application:

  1. [finding] — [file, section]
     Suggested action: [specific, one line]

  2. [finding] — [file, section]
     Suggested action: [specific, one line]

WORTH IMPROVING — meaningful but not urgent:

  3. [finding]
     Suggested action: [specific, one line]

QUICK WINS — small effort, good return:

  4. [finding]
     Suggested action: [specific, one line]

LOOKING GOOD — no action needed:
  • [area]
  • [area]

TEMPLATE LIBRARY
  Saved CV templates:      [N] — [oldest date]
  Saved CL templates:      [N] — [oldest date]
  Saved HTML styles:       [N]
  [Any flags]

PHRASE LIBRARY
  Sections populated:      [N of 12]
  Sections empty:          [list]
═══════════════════════════════════════════════
```

---

### PHASE 4: Work through findings

Ask: **"Which findings would you like to address now?
Reply with numbers (e.g. '1, 3, 4'), 'all', or 'none — just wanted the overview'."**

For each chosen finding, work through it using the same scoped approach as IMPROVER.md:
- Read only the relevant file and section
- Show current state
- Propose specific change
- Show before/after
- Save only on explicit confirmation

For FILL IN placeholders: ask the user for the missing information directly
rather than asking them to edit the file manually.

For outdated templates: don't delete — ask whether to archive or update.

For empty phrase library sections: offer to seed them from any recent
cover letters found in application folders, or from the quick-add approach.

---

### PHASE 5: Summary

```
═══════════════════════════════════════════════
MAINTENANCE COMPLETE
[date]
═══════════════════════════════════════════════
Addressed:    [list of findings fixed]
Deferred:     [list of findings skipped]
Next check:   [date 3 months from now]

Reminder: run this again before your next job search begins,
or any time you complete a significant new project or role change.
═══════════════════════════════════════════════
```
