# IMPROVER — Targeted Improvement Workflow

Helps you improve specific parts of your assets, templates, or outputs
without touching anything you didn't ask about.

**Principle: only what you name gets changed.** Unless you explicitly say
"review everything" or "while you're there, also fix X", the improver
works in a tight scope and stops.

---

## When to use this

- The reviewer flagged something specific and you want to act on it
- You've noticed your assets are thin in one area
- A cover letter felt off and you want to understand why
- You want to update one asset entry after a new project or role
- A template isn't working for a certain company type
- Your phrase library is empty in one section

---

## The Prompt

Paste into Claude Code:

---

You are running a targeted improvement session.

Your first and most important job is to understand the exact scope before touching anything.

Ask me: **"What specifically would you like to improve? Be as precise as you can —
for example: 'my capabilities.md has thin evidence for my last role',
'the HR recruiter persona flagged scannability in my CV template',
'the opening lines in my phrase library feel generic', or 'my profiles.md
doesn't reflect that I'm now targeting director-level roles'."**

Wait for my answer. Then do the following before making any changes:

---

### PHASE 1: Scope definition

**Map the request to specific files.**

Based on what I described, identify:
- Which file(s) need to change
- Which section(s) within those files
- What type of change (add / edit / remove / restructure)
- What files are NOT in scope (explicitly name them)

Show me the scope as a table:

```
IN SCOPE:
  File                         Section              Change type
  ─────────────────────────────────────────────────────────────
  [file]                       [section]            [add/edit/remove]

OUT OF SCOPE (not touching):
  [file] — [reason]
  [file] — [reason]
```

Then ask: **"Does this scope look right? Reply yes to proceed,
or tell me what to add or remove from scope."**

Do not read or open any file until scope is confirmed.

---

### PHASE 2: Read and assess

Read only the in-scope files and sections.

For each, show me:
- The current content (relevant section only, not the whole file)
- A brief assessment: what's working, what's weak, what's missing
- 2-3 specific improvement suggestions before touching anything

Ask: **"Would you like me to apply these suggestions, or do you want to
adjust the approach first?"**

---

### PHASE 3: Make changes

Apply only the agreed changes, to only the agreed files.

For each change:
- Show the before (current text)
- Show the after (proposed text)
- Explain the reasoning in one line

Ask: **"Does this look right? Reply yes to save, or tell me what to adjust."**

Iterate until approved. Save only when explicitly confirmed.

---

### PHASE 4: Downstream check

After saving, check: does this change affect anything downstream?

Common downstream effects:
- Editing a capabilities.md entry → check if it's referenced in a saved cv-template
  (cv-generator instructions block may name this entry)
- Editing profiles.md → check if any saved CL templates reference the old framing
- Editing competency_clusters.md trigger keywords → check if cv-templates need updating
- Editing writing-style.md → note that next CL generation will behave differently

For any downstream effect found: name it and ask whether to address it now or later.
Do not make downstream changes without asking.

---

### PHASE 5: Summary

Confirm what was changed:

```
═══════════════════════════════════════════════
IMPROVEMENTS SAVED
═══════════════════════════════════════════════
Changed:
  [file] → [what changed, one line]

Not changed (out of scope):
  [files]

Downstream to consider later:
  [any flagged downstream effects]
═══════════════════════════════════════════════
```

---

## Common improvement scenarios

Reference for what scope looks like in practice:

| You say... | In scope | Out of scope |
|---|---|---|
| "My last role has thin evidence" | capabilities.md (entries for that role ID) | All other roles, all other files |
| "My positioning feels off for director roles" | profiles.md (relevant profile), competency_clusters.md (cluster descriptions) | CV templates, CL templates |
| "The copywriter flagged clichés in my CL" | YYYYMMDD_*_cl.md (that specific letter) | Assets, templates |
| "I want to add a new skill I just realised I have" | capabilities.md (new entry), maybe competency_clusters.md (if new cluster) | Everything else |
| "My phrase library openings feel generic" | phrase-library.md (opening lines section only) | Other phrase library sections, assets |
| "I want to try a bolder tone in my CL template" | cover-letter-template.md (the specific template) | Assets, other templates |
| "The ATS persona flagged missing keywords" | capabilities.md (add keywords to tags), competency_clusters.md (add to trigger keywords) | CV structure, HTML files |
