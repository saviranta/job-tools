# Cover Letter Template Generator Prompt

Answer the questions below, then paste everything into Claude.
Claude generates a `cover-letter-template.md` — the structural brief for your letter.
The cover-letter-generator uses this template alongside your writing-style.md and phrase-library.md.

**How to use:**
1. Answer the questions below
2. Optionally paste `brand-brief.md`, `job-brief.md`, `writing-style.md`
3. Paste everything into Claude
4. Save the output as `cover-letter-template.md` in your application folder
   (and optionally to `templates/cover-letter/` for future reuse)

---

## Context Questions

---

**Q1: Length and structural style**

Pick one — this is the most consequential decision:

- [ ] **Short & bold** (100–150 words)
  Everything stripped to essentials. One strong opening, one proof point, one closing line.
  Best for: direct referrals, exec roles, creative fields that value confidence over completeness.

- [ ] **Structured** (~200 words)
  Opening paragraph → 3 tight bullets → closing paragraph.
  Best for: ATS-heavy pipelines, technical roles, recruiters who skim before they read.

- [ ] **Engaging narrative** (300–400 words, fits one page)
  Flowing prose, no visual structure. Story-driven, voice-forward.
  Best for: writing-heavy roles, culture-first companies, when you want personality to land.

---

**Q2: What to emphasise**

Check all that apply — these will shape which sections get weight and which are minimal:

- [ ] Genuine motivation for this specific role
- [ ] Cultural or values fit
- [ ] Skills and area of expertise
- [ ] Specific past experience (e.g. a directly relevant role or project)
- [ ] Personal story or career journey
- [ ] Praise or admiration for the company (specific, not generic)
- [ ] Constructive insight about a challenge the company faces
- [ ] Career trajectory and growth direction
- [ ] A specific quantified achievement
- [ ] Domain or industry knowledge
- [ ] Referral or personal connection to someone at the company

---

**Q3: Opening approach**

Pick one:

- [ ] Bold claim — lead with your strongest asset or most relevant credential
- [ ] Storytelling hook — open with a moment, observation, or specific detail that draws them in
- [ ] Direct statement of interest — clear, grounded, no preamble
- [ ] Company-first — start with something specific about them before turning to yourself

---

**Q4: Closing approach**

Pick one:

- [ ] Forward-looking call to action ("I'd welcome a conversation to explore...")
- [ ] Availability and practicalities ("Available from [date], happy to discuss...")
- [ ] Warm sign-off (brief, genuine, no ask)
- [ ] Include salary expectation
- [ ] Include both availability and salary

---

**Q5: Tone**

Pick one:

- [ ] Formal and polished
- [ ] Professional with warmth
- [ ] Direct and confident (minimal warmth signalling)
- [ ] Conversational (reads like a smart person talking, not a letter)

---

**Q6: Domain and expertise area**

What is the industry and job function of this role?
(Used to calibrate what kind of evidence to lead with and what language fits.)

Domain: [e.g. technology, fintech, healthcare, retail, consulting]
Expertise area: [e.g. product management, engineering, sales, research, operations]

---

**Q7: Anything specific to include or exclude?**

Free text — e.g.:
- "I'm changing industries — need to address the pivot without over-explaining it"
- "This is an internal application — tone should acknowledge existing relationship"
- "Don't include salary — it wasn't asked for"
- "I have a career gap — I want to briefly acknowledge it rather than avoid it"
- "Strong referral — mention [Name] early"

[YOUR NOTES HERE]

---

**Q8: Save to template library or use once?**

- [ ] Save to library — I'll reuse this structure for similar applications
- [ ] One-off — this context is unusual

If saving, give it a short descriptive name:
e.g. `narrative-motivation-fit`, `structured-skills-ats`, `bold-exec-referral`

Template name: [YOUR NAME HERE]

---

## Optional: Paste supporting files

**writing-style.md:**
[PASTE HERE — or delete. If provided, Claude will align the template's tone guidance
to your voice profile and flag any contradictions.]

**brand-brief.md** (from brand-inspector):
[PASTE HERE — or delete. Cover letter tone guidance from brand-brief overrides Q5
where the two conflict — brand-brief reflects what the company responds to.]

**job-brief.md** (from job-listing-analyzer):
[PASTE HERE — or delete. Cluster ranking and positioning angle will inform
which emphasis areas get most weight.]

**phrase-library.md:**
[PASTE HERE — or delete. Claude will note which sections can draw from your
library and flag any sections with no suitable phrases yet.]

---

## The Generation Prompt

Paste everything above into Claude, followed by this:

---

You are generating a cover letter template based on the context answers and any
supporting files provided.

The template is not the letter itself. It is a structural and tonal brief that the
cover-letter-generator uses alongside the career asset library and writing-style.md.

Generate a template ID from the name given in Q8 (uppercase with hyphens):
e.g. `narrative-motivation-fit` → `TMPL-CL-NARRATIVE-MOTIVATION-FIT`.
If one-off, use `TMPL-CL-ONEOFF`.

Produce a `cover-letter-template.md` starting with a metadata header.

**Metadata header:**

```
---
id: TMPL-CL-[GENERATED-ID]
name: [Human-readable name, or "One-off"]
library: true / false
length_style: short-bold / structured / narrative
emphasis: [comma-separated list from Q2]
opening: bold-claim / storytelling / direct / company-first
closing: call-to-action / availability / warm-signoff / salary / availability-and-salary
tone: formal / professional-warm / direct / conversational
domain: [from Q6]
expertise: [from Q6]
created: [today's date]
---
```

Then produce the following sections:

**1. Template summary**
One paragraph: what this template is optimised for, who it's best suited to,
and what it will feel like to receive.

**2. Structural blueprint**

Specify the exact sections of the letter in order. For each section:
- Section name (internal label, not a heading in the letter unless structured style)
- Purpose: what this section must accomplish
- Length: word count or sentence count target
- Tone note: any specific register for this section
- Emphasis: which of the Q2 items this section carries
- Phrase library note: which phrase-library section to draw from (if library was provided,
  flag specific phrases that fit; if not, note what type of phrase to use)

Adapt the blueprint to the chosen length style:

*Short & bold:*
```
1. Opening statement (1-2 sentences)
2. Core claim or proof point (2-3 sentences)
3. Closing line (1 sentence)
```

*Structured:*
```
1. Opening paragraph (3-4 sentences)
2. Bullet 1 — [emphasis area]
3. Bullet 2 — [emphasis area]
4. Bullet 3 — [emphasis area]
5. Closing paragraph (2-3 sentences)
```

*Engaging narrative:*
```
1. Opening (2-3 sentences — hook)
2. Body paragraph 1 — [emphasis areas]
3. Body paragraph 2 — [emphasis areas]
4. Company/fit paragraph (2-3 sentences)
5. Closing (2-3 sentences)
```

**3. Voice and tone guidance**

Based on writing-style.md (if provided) and Q5 tone selection:
- How to open sentences in this letter
- What to avoid in this specific context
- Register calibration: formal vs warm vs direct
- Any tension between the brand-brief tone and the user's natural voice — and how to resolve it
- 2-3 example sentence openers that fit this template's tone

**4. What not to include**

Based on Q2 (what was NOT selected) and Q7 (exclusions):
- Sections or themes to omit entirely
- Phrases or framings to avoid for this specific application

**5. cover-letter-generator instructions**

A block to pass directly to the cover-letter-generator:
- Which asset clusters to prioritise (from job-brief if provided)
- Which capabilities/accomplishments to draw on (top 2-3 from job-brief shortlist)
- Where to use the phrase library (by section)
- Specific personalisation to include (from company-brief or brand-brief)
- Word count target per section

Output the full `cover-letter-template.md` as a single markdown document, ready to save.
