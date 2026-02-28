# Asset Update Guide

A reference for keeping your asset files current over time.
Covers what to update, when, and how to spot gaps.

---

## When to update

**After a significant work event:**
- You shipped something notable (feature, project, campaign, process change)
- You ran something well (a workshop, a negotiation, a difficult conversation)
- You solved a hard problem or unblocked a team
- You received feedback — positive or critical — that surprised you

**After a job application:**
- Which capabilities came up in the interview? Add missing evidence.
- Which parts of your CV drew questions? Strengthen the weak spots.
- Which clusters did the job ad emphasise that you underweighted? Adjust tags.

**On a schedule (quarterly minimum):**
- Is your most recent role still up to date in `work_experience.md`?
- Are there accomplishments from the last 3 months that aren't in `capabilities.md`?
- Have you changed how you describe yourself? Update `profiles.md`.
- Are there any `<!-- FILL IN -->` placeholders you can now complete?

---

## What to update and where

### New role or title change → `work_experience.md`
- Add a new role block with a new role ID
- If same company with added scope, update the existing entry and note the title change
- Update the Quick Reference table at the bottom

### New accomplishment → `capabilities.md`
- Use the quick-add-prompt.md for sporadic updates
- For larger updates, add directly using the entry format:
  ```
  | Category | Type | Title | Description | Evidence/Metrics | Tags | Context Relevance | Role | Clusters |
  ```
- Accomplishments are higher value than capabilities — prioritise those

### New skill area emerging → `competency_clusters.md`
- If you're seeing a pattern of new capabilities in an area, consider:
  - Adding trigger keywords to an existing cluster
  - Creating a new cluster if it's genuinely distinct

### New project or feedback → `qualities_workstyle.md`
- Add concrete examples to existing bullets (specific > general)
- If feedback surfaces a new working style trait, add it to the right section

### Targeting a new type of role → `profiles.md`
- Add a new profile (PROF-N) rather than rewriting an existing one
- Note the target role type and company stage clearly

---

## Signs your assets need attention

- You're rewriting the same sentences every time you apply
- A recruiter or interviewer asks about something you don't have a strong example for
- Your CV feels generic even after using the cv-generator
- You're finding yourself in the wrong interviews (wrong role level, wrong company type)
- More than 3 months have passed since you last touched the files

---

## What not to do

**Don't delete old entries.** Archive them with a comment if they're no longer relevant.
Old evidence can still be useful for cover letters or niche roles.

**Don't wait until you're job hunting.** The hardest part of keeping assets useful
is remembering what you did six months ago. Capture things while they're fresh.

**Don't edit assets during an application.** Update assets after. During an application,
use what you have — don't rebuild mid-cycle.

---

## Quick reference: which file for which update?

| You want to capture... | File |
|---|---|
| A new role, title, or employer | `work_experience.md` |
| Something you shipped or achieved | `capabilities.md` |
| A skill you've become stronger in | `capabilities.md` + maybe `competency_clusters.md` |
| How you prefer to work or lead | `qualities_workstyle.md` |
| A new type of job you're targeting | `profiles.md` |
| New keywords you're seeing in job ads | `competency_clusters.md` (trigger keywords) |
