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

**Q8: How much human character should be in the writing?**

Check all that apply. These are deliberate techniques that make writing feel authored
rather than generated. Select only what you're comfortable with — some are low-risk,
some are context-dependent.

*Low risk — almost always fine:*
- [ ] Varying sentence lengths — mix of short punchy lines and longer flowing ones,
      rather than uniformly medium-length sentences
- [ ] Sentence starting with "And", "But", or "Because" — used once, intentionally,
      for rhythm or emphasis
- [ ] Em dash for a beat — "I've done this work — and I'd do it again." Used once or twice.
- [ ] A parenthetical aside — (something said slightly off the main thread, in brackets)
      signals a thinking, present person rather than a polished machine

*Medium risk — depends on company and role:*
- [ ] One sentence that runs slightly long — the kind you write when you're genuinely
      into what you're saying; reads as enthusiasm, not sloppiness
- [ ] Informal contraction in an unexpected place — "That's" instead of "That is" mid-paragraph,
      or "I've" where a very formal letter might say "I have"
- [ ] Conversational word in an otherwise professional sentence — one "actually", "honestly",
      or "quite" that loosens the register without breaking it

*Higher risk — use with judgement:*
- [ ] 1–2 minor typographic imperfections — a transposition ("teh" → "the") or a
      doubled word caught-but-left ("I have have"), the kind that slips through
      a personal proofread. **Avoid for roles where precision is the product
      (legal, finance, editorial, QA).**
- [ ] One comma splice — two independent clauses joined by a comma rather than a
      semicolon or conjunction. Very common in confident human writing, occasionally
      jarring to copy editors.
- [ ] Oxford comma inconsistency — used in most lists, dropped in one.
      Subtle, but a real human fingerprint.

---

**Q9: Save to template library or use once?**

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

Generate a template ID from the name given in Q9 (uppercase with hyphens):
e.g. `narrative-motivation-fit` → `TMPL-CL-NARRATIVE-MOTIVATION-FIT`.
If one-off, use `TMPL-CL-ONEOFF`.

**Library collision check (for library templates only):**
Before saving, check whether a file with this ID already exists in
`[workspace]/templates/cover-letter/`. If it does, do not overwrite it silently.
Ask: "A template named [TMPL-CL-ID] already exists. Replace it, save as [TMPL-CL-ID]-2, or cancel?"
Wait for the user's choice before saving.

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
human_character: [comma-separated list of selected Q8 options, or "none"]
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

**4. Human character instructions**

Based on Q8 selections, produce a specific instruction list for the cover-letter-generator.
Be precise — not "vary sentence length" but "include at least two sentences under 8 words
and at least one sentence over 25 words in the body paragraphs."

For each selected technique, write one concrete instruction:

- *Varying sentence lengths* → "Body paragraphs must contain at least one sentence under
  8 words and one over 25 words. Do not make all sentences 15–20 words."
- *Sentence starting with And/But/Because* → "One sentence, in [section], may start with
  'And' or 'But'. Use once only."
- *Em dash* → "Use one em dash for rhythm or emphasis, in [section]. Not in the opening line."
- *Parenthetical aside* → "Include one parenthetical (in brackets) in [section].
  Should feel like a thinking-out-loud moment, not a disclaimer."
- *One long sentence* → "One sentence in [section] may run 35–45 words — the kind that
  builds as it goes. Should read as enthusiasm, not padding."
- *Informal contraction* → "Use one informal contraction in [section] where a very formal
  letter would avoid it. E.g. 'That's' instead of 'That is'."
- *Conversational word* → "One instance of 'actually', 'honestly', or 'quite' in [section].
  Single use only."
- *Minor typographic imperfection* → "Introduce one transposition-type error (e.g. 'teh',
  'adn') in a non-critical word in [section]. Not in the opening sentence, a proper noun,
  or a number."
- *Comma splice* → "One comma splice is permitted in [section] — two short independent
  clauses joined by a comma, where a semicolon would be technically correct."
- *Oxford comma inconsistency* → "Use the Oxford comma throughout, but drop it in one list."

If no Q8 options were selected: "Write with consistent, clean, polished prose throughout.
No deliberate imperfections."

**5. What not to include**

Based on Q2 (what was NOT selected) and Q7 (exclusions) and Q8 (higher-risk options NOT selected):
- Sections or themes to omit entirely
- Phrases or framings to avoid for this specific application

**6. cover-letter-generator instructions**

A block to pass directly to the cover-letter-generator:
- Which asset clusters to prioritise (from job-brief if provided)
- Which capabilities/accomplishments to draw on (top 2-3 from job-brief shortlist)
- Where to use the phrase library (by section)
- Specific personalisation to include (from company-brief or brand-brief)
- Word count target per section

Output the full `cover-letter-template.md` as a single markdown document, ready to save.
