# CV Template Generator Prompt

Answer the questions below, then paste everything into Claude.
Claude will generate a `cv-template.md` — the structural brief for your CV.
The cv-generator uses this template to place content from your asset files.

**How to use:**
1. Answer the questions in the block below (replace the bracketed options with your choice)
2. Optionally paste in your `brand-brief.md` and/or `job-brief.md`
3. Paste everything into Claude
4. Save the output as `cv-template.md` in your application folder

---

## Context Questions

Answer each question before pasting.

---

**Q1: Will this CV be processed by an ATS (Applicant Tracking System)?**

Pick one:
- [ ] Yes — large company, job board application, or I know they use ATS
- [ ] Probably — I'm not sure but want to be safe
- [ ] No — direct referral, small company, creative/agency role, or portfolio-first field
- [ ] Unknown

---

**Q2: What is the seniority level of the role?**

Pick one:
- [ ] Individual contributor / specialist (no people management)
- [ ] Senior IC or team lead (technical authority, may mentor)
- [ ] Manager (people manager, owns a team)
- [ ] Director or above (organisational scope, strategy)

---

**Q3: What type of company is this?**

Pick one:
- [ ] Early-stage startup (under ~100 people)
- [ ] Growth stage / scale-up
- [ ] Enterprise or large public company
- [ ] Agency or consultancy
- [ ] Public sector or non-profit

---

**Q4: What industry or domain is this role in?**

Pick one (or write your own):
- [ ] Technology / software / SaaS
- [ ] Fintech / financial services / banking
- [ ] Healthcare / medtech / biotech
- [ ] Retail / e-commerce / consumer
- [ ] Media / publishing / content
- [ ] Manufacturing / industrials / logistics
- [ ] Public sector / government / NGO
- [ ] Education / research / academia
- [ ] Professional services / consulting / legal
- [ ] Other: [specify]

---

**Q5: What is the primary area of expertise this role sits in?**

Check all that apply (most roles have a primary + 1-2 secondary):
- [ ] Engineering / software development / technical
- [ ] Product management / product design
- [ ] Data / analytics / data science / ML
- [ ] Sales / business development / revenue
- [ ] Marketing / growth / brand / content
- [ ] Customer success / support / account management
- [ ] Operations / project management / programme delivery
- [ ] Strategy / consulting / business analysis
- [ ] Finance / accounting / commercial
- [ ] People / HR / talent / organisational design
- [ ] Research / UX research / user insight
- [ ] Design / creative / UX/UI
- [ ] Legal / compliance / risk
- [ ] Leadership / general management (cross-functional)
- [ ] Other: [specify]

---

**Q6: What CV structure fits this role?**

Pick one:
- [ ] Chronological — employment history first, accomplishments nested under each role
- [ ] Skills / capabilities first — lead with what I can do, then support with roles
- [ ] Hybrid — brief positioning statement, then chronological roles

---

**Q7: Target CV length?**

Pick one:
- [ ] 1 page — highly compressed, maximum impact per line
- [ ] 2 pages — standard for experienced candidates
- [ ] No strict limit — role expects depth (academic, technical lead, executive)

---

**Q8: What sections should be included?**

Check all that apply:
- [ ] Profile / positioning statement (2-4 lines at the top)
- [ ] Core skills / competencies summary
- [ ] Work experience (standard)
- [ ] Key accomplishments / highlights (standalone section, separate from roles)
- [ ] Education
- [ ] Certifications or training
- [ ] Languages
- [ ] Publications or speaking
- [ ] Portfolio or work samples (link)
- [ ] Volunteer or advisory roles
- [ ] Other: [specify]

---

**Q9: Anything to emphasise or de-emphasise?**

Free text — e.g.:
- "Emphasise the last 5 years, compress everything before 2018"
- "Lead with technical depth, management experience is secondary for this role"
- "Exclude exact dates — I'm returning from a career break"
- "This is a board-adjacent role — titles and company names matter most"

[YOUR NOTES HERE]

---

**Q10: Save this template to your library, or use it once?**

Pick one:
- [ ] Save to library — I'll reuse this structure for similar applications
- [ ] One-off — this context is unusual, don't add to library

If saving to library, give the template a short descriptive name:
e.g. `startup-pm-ats-2page`, `enterprise-director-designed`, `agency-ic-1page`

Template name: [YOUR NAME HERE]

---

## Optional: Paste supporting files

If you have these, paste them below. Claude will use them to inform the styling
and section emphasis.

**brand-brief.md** (from brand-inspector):
[PASTE HERE — or delete this section]

**job-brief.md** (from job-listing-analyzer):
[PASTE HERE — or delete this section]

---

## The Generation Prompt

Paste everything above into Claude, followed by this:

---

You are generating a CV template based on the context answers, and optionally
a brand brief and job brief provided above.

The template is not the CV itself. It is a structural brief that the cv-generator
will use to populate content from a career asset library.

If the user chose to save to library (Q10), generate a template ID from their name
(uppercase, hyphens): e.g. `startup-pm-ats-2page` → `TMPL-STARTUP-PM-ATS-2PAGE`.
If one-off, use `TMPL-ONEOFF`.

Produce a `cv-template.md` starting with a metadata header, then the sections below.

**Metadata header** (must be first — used by the template selector for matching):

```
---
id: TMPL-[GENERATED-ID]
name: [Human-readable name from Q10, or "One-off"]
library: true / false
ats: yes / probably / no / unknown
seniority: ic / senior-ic / manager / director
company_type: [from Q3: startup / scale-up / enterprise / agency / public-sector]
domain: [from Q4]
expertise: [from Q5, comma-separated]
length: 1-page / 2-page / unlimited
created: [today's date]
---
```

**1. Template summary**
One paragraph: what this template is optimised for and why.
Include: ATS status, seniority, company type, industry domain, and primary expertise area.
(e.g. "ATS-safe two-page chronological CV for a senior product manager role in fintech,
targeting a scale-up. Skills-forward section order, dense evidence under each role,
metrics-led bullets, no graphics or tables.")

**2. Page setup**
- Column layout: single / two-column / hybrid (specify)
- Margin guidance: standard (2.5cm) / narrow (1.5cm) / wide (3cm)
- Line spacing: compact / standard / generous
- ATS notes: any structural constraints to flag (no tables, no text boxes, etc.)

**3. Header specification**
What to include in the CV header, in order:
- Full name (size/weight guidance)
- Professional title or headline (include? wording guidance?)
- Contact line (email / phone / LinkedIn / location — what to show and how)
- Photo: include / exclude (note regional norms if relevant)
- Any other header elements

**4. Section list**
The ordered list of sections for this CV, with the exact section heading to use:

```
1. [Section name] — [one line: what goes here]
2. [Section name] — [one line: what goes here]
...
```

**5. Per-section brief**
For each section listed above:

**[Section name]**
- Format: bullets / prose / table / hybrid
- Length: [e.g. "3-5 bullets per role", "2-4 lines of prose", "no more than 6 items"]
- Emphasis: [what to prioritise — e.g. "lead with outcome, not task"]
- Source in assets: [which asset file and field to draw from]
- Notes: [any specific guidance for this section]

**6. Visual parameters**

*If brand-brief.md was provided:*
- Header background color: [from brand palette]
- Accent color (section titles, role titles, links): [specific suggestion]
- Heading font: [name + weight]
- Body font: [name + weight]
- Overall density: [matches their brand profile]

*If no brand-brief:*
- Recommend a clean, neutral palette appropriate for the company type and role
- Suggest Google Fonts pairing

**7. Domain and expertise calibration**
Based on the industry domain (Q4) and expertise area(s) (Q5), note:
- What evidence types are most valued in this domain (metrics / case studies / technical depth / client outcomes / publications / portfolio)
- Which sections or bullet patterns are conventional for this expertise area
  (e.g. sales roles lead with quota attainment and pipeline numbers; engineering roles
  lead with technical scope and system impact; research roles may foreground methodology)
- Any domain-specific conventions to follow or avoid
  (e.g. academic CVs use different structures; creative roles may expect a portfolio link above the fold)

**8. cv-generator instructions**
A short block of instructions to pass to the cv-generator, summarising:
- Which asset clusters to prioritise (draw from job-brief if provided)
- How many roles to include
- How to handle gaps or older experience
- What evidence type to lead with, given the domain and expertise area
- Tone guidance for any prose sections

Output the full `cv-template.md` as a single markdown document, ready to save.
