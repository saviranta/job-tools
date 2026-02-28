# Template Selector Prompt

Run this after the job-listing-analyzer to check whether a suitable template
already exists in your library before generating a new one.

**How to use:**
1. Paste your `job-brief.md`
2. Paste the metadata headers from all templates in your `templates/` folder
3. Paste the prompt below into Claude
4. Claude recommends which template to use — or tells you to generate a new one

---

## How to extract metadata from your templates

You only need to paste the metadata headers, not the full template content.
Each template starts with a `---` block. Copy from `---` to the closing `---` for each file.

Example of what to paste:

```
TMPL-STARTUP-PM-ATS-2PAGE:
---
id: TMPL-STARTUP-PM-ATS-2PAGE
name: Startup PM — ATS-safe, 2-page
library: true
ats: probably
seniority: manager
company_type: startup, scale-up
domain: technology, fintech
expertise: product-management, strategy
length: 2-page
created: 2025-01-15
---

TMPL-ENTERPRISE-DIR-DESIGNED:
---
id: TMPL-ENTERPRISE-DIR-DESIGNED
name: Enterprise Director — designed, 2-page
library: true
ats: no
seniority: director
company_type: enterprise
domain: technology, professional-services
expertise: leadership, strategy, operations
length: 2-page
created: 2025-02-01
---
```

---

## The Selector Prompt

Paste this into Claude along with your job-brief and template metadata.

---

I have a library of CV templates, each described by a metadata header.
I also have a job brief from the job-listing-analyzer for a specific application.

Here is my job brief:

[PASTE job-brief.md HERE]

Here are the metadata headers for all templates in my library:

[PASTE TEMPLATE METADATA HEADERS HERE]

---

Based on the job brief and the template metadata, do the following:

**1. Match analysis**

For each template in the library, score the match on these dimensions:
- ATS requirement (does the template's ATS setting suit this application?)
- Seniority (does the template target the right level?)
- Company type (startup vs enterprise vs agency, etc.)
- Domain (industry match)
- Expertise area (job function match)
- Length (appropriate for this role and level?)

**2. Recommendation**

Pick one outcome:

**Option A — Strong match exists:**
"Use `[TEMPLATE-ID]`. It matches on [list of matching dimensions].
Minor adaptation needed: [e.g. 'update accent color from brand-brief', 'adjust
expertise framing from product to growth']."

Copy the template to your application folder as `cv-template.md` and apply the
suggested adaptations before running the cv-generator.

**Option B — Partial match:**
"The closest template is `[TEMPLATE-ID]`, but it diverges on [dimensions].
Options: (1) use it as-is and accept the mismatch, (2) use it as a starting
point and adjust [specific sections], or (3) generate a new template.
Recommended: [your recommendation]."

**Option C — No suitable match:**
"No existing template fits this application well. Generate a new one using
`template-generator-prompt.md` with these suggested answers:
- Q1 (ATS): [suggestion based on job brief]
- Q2 (Seniority): [suggestion]
- Q3 (Company type): [suggestion]
- Q4 (Domain): [suggestion]
- Q5 (Expertise): [suggestion]
- Q6 (Structure): [suggestion]
- Q7 (Length): [suggestion]
- Q8 (Sections): [suggestion]
- Q10 (Library): Save to library — suggested name: [name]"

**3. If Option C: pre-filled answer block**

Output a ready-to-use answer block for `template-generator-prompt.md`
with all nine context questions pre-filled based on the job brief.
The user only needs to review and adjust before pasting.
