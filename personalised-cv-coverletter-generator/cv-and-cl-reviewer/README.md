# cv-and-cl-reviewer

Reviews your generated CV and cover letter from six distinct perspectives,
each with a different evaluation lens and set of priorities.

Output: a crisp feedback summary per persona, followed by a prioritised change list.
You choose which recommendations to apply — none, some, or all.

---

## The six personas

| Persona | Primary focus | Reviews |
|---|---|---|
| **ATS** | Keyword matching, parseable structure, format compliance | CV (primary) |
| **HR Recruiter** | First impression, scannability, role fit clarity, red flags | CV + CL |
| **Hiring Manager** | Evidence quality, seniority calibration, domain credibility | CV + CL |
| **Role Expert** | Technical accuracy, peer credibility, depth vs surface exposure | CV (primary), CL briefly |
| **CEO / CFO / Legal** | Leadership signals, commercial claims, liability, comp positioning | CV + CL |
| **Narrative Copywriter** | Voice, clichés, readability, CL opening, career narrative arc | CL (primary), CV briefly |

Personas are calibrated to the specific role and company from your job-brief.
"Role Expert" for a product management role looks different from one for an engineering role.

---

## Output structure

For each persona:
- **Signal**: STRONG / GOOD / MIXED / WEAK
- **Observations**: 2–3 crisp lines (what's working and what isn't)
- **Change suggestions**: numbered, specific, actionable

Then:
- **Cross-persona priority table**: issues flagged by multiple reviewers rank highest
- **Your choices**: select which recommendations to apply
- **Edit guidance**: exact instructions for each chosen change

---

## What gets reviewed

The `.md` files — the canonical reviewed content. Not the HTML (that's derived).
Both CV and CL are reviewed together where relevant — consistency between them matters.

---

## When to run this

After Phase 3 of the cv-generator and cover-letter-generator (HTML is saved),
before making any final manual edits. The reviewer informs what to edit;
Phase 4 of the generators handles the edit sync back to assets.
