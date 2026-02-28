# Cover Letter Template Selector

Run this after the job-listing-analyzer to check your template library
before generating a new cover letter template.

**How to use:**
1. Paste your `job-brief.md`
2. Paste the metadata headers from all cover letter templates in `templates/cover-letter/`
3. Optionally paste your `writing-style.md` (helps Claude flag tone mismatches)
4. Paste the prompt below into Claude

---

## How to extract metadata from your templates

Only paste the `---` header blocks, not the full template content.

Example of what to paste:

```
TMPL-CL-NARRATIVE-MOTIVATION-FIT:
---
id: TMPL-CL-NARRATIVE-MOTIVATION-FIT
name: Narrative — motivation and cultural fit
library: true
length_style: narrative
emphasis: motivation, fit, story, praise-for-company
opening: storytelling
closing: call-to-action
tone: professional-warm
domain: technology
expertise: product-management
created: 2025-01-15
---

TMPL-CL-STRUCTURED-SKILLS-ATS:
---
id: TMPL-CL-STRUCTURED-SKILLS-ATS
name: Structured — skills-led, ATS-safe
library: true
length_style: structured
emphasis: skills, experience, achievement
opening: direct
closing: availability
tone: formal
domain: technology, fintech
expertise: engineering, data
created: 2025-02-01
---
```

---

## The Selector Prompt

---

I have a library of cover letter templates, each described by a metadata header.
I also have a job brief from the job-listing-analyzer for a specific application.

Here is my job brief:

[PASTE job-brief.md HERE]

Here are the metadata headers for all cover letter templates in my library:

[PASTE TEMPLATE METADATA HEADERS HERE]

Here is my writing style profile (optional):

[PASTE writing-style.md HERE — or delete this section]

---

Based on the job brief and the template metadata, do the following:

**1. Match analysis**

For each template, score the match on these dimensions:
- Length style (is short-bold / structured / narrative right for this company and role?)
- Emphasis alignment (does the template's emphasis match what the job-brief says to lead with?)
- Opening approach (does it suit the company type and application context?)
- Tone (does it fit the brand-brief and company culture signals in the job-brief?)
- Domain and expertise (how close is the match?)

**2. Recommendation**

Pick one outcome:

**Option A — Strong match:**
"Use `[TEMPLATE-ID]`. It matches on [dimensions].
Suggested adaptations for this specific application:
- [e.g. 'swap company-praise emphasis for achievement — this role values proof points']
- [e.g. 'adjust opening from storytelling to direct — engineering hiring manager context']"

**Option B — Partial match:**
"Closest match is `[TEMPLATE-ID]`, but it diverges on [dimensions].
Options: (1) use as-is, (2) adapt [specific section], (3) generate new.
Recommended: [recommendation with reason]."

**Option C — No suitable match:**
"No existing template fits well. Generate a new one using `template-generator-prompt.md`.
Suggested pre-filled answers based on the job brief:

- Q1 (Length style): [suggestion + reason]
- Q2 (Emphasis): [list of checked items + reason for each]
- Q3 (Opening): [suggestion + reason]
- Q4 (Closing): [suggestion]
- Q5 (Tone): [suggestion based on brand-brief signals in job-brief]
- Q6 (Domain/expertise): [from job-brief]
- Q8 (Library): Save — suggested name: [name]"

**3. If Option C: pre-filled answer block**

Output a ready-to-paste answer block for `template-generator-prompt.md` with all
questions pre-filled. The user reviews and adjusts, then pastes to generate.
