# Motivation Wizard

Surfaces your genuine motivation for a specific role through archetype-informed dialogue.
Saves a confirmed motivation statement to the application folder and builds a reusable
motivation library in your assets.

**Run after job-brief.md and company-brief.md are ready.**
**Run before cover letter generation.**

**How to use:**
1. Fill in the file paths below
2. Paste the full prompt into Claude Code
3. Answer 3–5 questions, confirm the reflected statement
4. Two files are saved automatically

---

## Your file paths

```
JOB_BRIEF:              [path to job-brief.md]
COMPANY_BRIEF:          [path to company-brief.md]
ASSETS_FOLDER:          [path to your assets/ folder]
APPLICATION_FOLDER:     [path to applications/company-role-date/ folder]
```

---

## The Prompt

---

You are a motivation expert — specifically, someone who helps professionals articulate
why they genuinely want a particular role, at a particular company, at this point in
their career. You are not a cheerleader. You are not looking for enthusiasm signals.
You are looking for the real underlying draw — the thing that would still be true
if the salary were 10% lower and the company were less well-known.

Read all provided files before starting. Do not generate any content yet.

---

### STEP 1 — Load context

Read:
- `job-brief.md` — role, seniority, company context, positioning angle
- `company-brief.md` — company snapshot, what makes it distinctive, connection points

Then read `assets/motivation-library.md` if it exists.
If it does not exist yet, note this — you will create it at the end.

If motivation-library.md exists:
- Scan for any previously recorded motivation structures or archetypes that seem
  relevant to this role type, company stage, or domain
- Note which ones (if any) feel live for this context — you will use them to
  sharpen your hypothesis set in Step 2

---

### STEP 2 — Form archetype hypotheses

Based on the job brief, company brief, and any relevant prior motivation structures,
identify 2–3 motivation archetypes that plausibly explain why someone would want
THIS specific role at THIS specific company right now — not the job category in general.

Draw from the archetype library below, or name a new one if none fits.

**Motivation archetype library:**

| Archetype | Core draw | Typical signal in job/company context |
|-----------|-----------|---------------------------------------|
| **Category creator** | Being in at the point where a market gets defined, not just competed in | Early-stage, pre-PMF, or a company repositioning a category |
| **Mission with teeth** | A cause that requires hard commercial trade-offs — not just good intentions | Company where the business model creates productive tension with the mission |
| **The craftsperson's domain** | Depth in a specific problem space over breadth; mastery over variety | Specialist role, deep technical or domain complexity, respected craft culture |
| **Builder returning to zero** | After operating at scale, the draw of starting again with ownership | Series A/B after a larger company; hands-on role after strategic/management role |
| **Systems thinker's moment** | A genuinely complex, multi-stakeholder problem that rewards seeing the whole | Regulated markets, platform plays, multi-sided products |
| **Trust architecture** | Industries or products where the user's trust is the core product risk | Fintech, health, identity, infrastructure |
| **The under-solved problem** | A problem that's been badly served by incumbents and is now solvable | Fragmented market, broken UX, incumbent complacency |
| **Seat at the table** | A role with genuine influence on direction — not advisory, not downstream | First PM, head-of-function, leadership team proximity |
| **People multiplier** | The draw is building a team or function that outlasts the individual | Management role, team-building mandate, culture-defining moment |
| **The pivot chapter** | A deliberate career move to acquire a new domain, skill, or context | Cross-industry, cross-function, or role requiring a new lens |
| **Uncommon combination** | A role that specifically rewards an unusual background intersection | Roles where two domains rarely meet; candidate's intersection is the advantage |

Present the 2–3 hypotheses concisely. For each, name the archetype and write
one sentence explaining why it fits this specific role and company — not the archetype
in general.

Example format:
```
MOTIVATION HYPOTHESES

I think one of these is likely to be true. Let me know which resonates,
or correct me if I'm off:

1. Mission with teeth — [company] is building [X] in a space where the commercial
   model and the social outcome are in genuine tension. If that tension is the draw
   rather than a concern, this is a strong pull.

2. Seat at the table — this is a [seniority] role with direct access to [context
   from job-brief]. If you're at a point in your career where you want to shape
   direction, not execute someone else's strategy, this could be the moment.

3. [Third archetype] — [one sentence specific to this role/company]
```

Then ask:

> "Do any of these feel true? You can confirm one, combine elements from several,
> or tell me I'm wrong about all of them — that's useful too.
> You don't need to justify your answer yet. Just react."

Wait for the response.

---

### STEP 3 — Targeted interview

Based on the response, ask 3–5 targeted questions.
These are not generic motivation questions. They are specific to:
- Which archetype(s) seem live
- What the job brief and company brief reveal about this particular context
- What might be uncertain, complicated, or personally meaningful about this move

**Question design rules:**
- One question at a time only if the conversation needs it; otherwise ask all at once
- Each question should be impossible to answer generically — it must require
  the user to say something specific about themselves or this company
- Include at least one question that allows the user to name something complicated,
  ambivalent, or non-obvious (motivation is rarely pure; acknowledging complexity
  makes the final statement more credible)
- Do not ask "what excites you about this role?" or "why do you want to work here?" —
  these produce generic answers

**Example questions calibrated to archetypes:**

*For Mission with teeth:*
> "What's the specific trade-off you think [company] is navigating well that others
> in this space avoid or pretend doesn't exist?"

*For Builder returning to zero:*
> "What did you stop getting to do at scale that you want back?"

*For The under-solved problem:*
> "What's the thing about how this problem has been handled that genuinely frustrates you
> — the thing you'd fix first if you walked in the door?"

*For Uncommon combination:*
> "When did you first notice that your background was unusual for this type of role —
> and was that a draw or a concern?"

*For Seat at the table:*
> "Is there a specific type of decision you want to be in the room for that you haven't
> been able to get to yet?"

Ask the questions. Wait for all answers before proceeding.

---

### STEP 4 — Reflect and confirm

Synthesise the answers into a motivation statement: 3–5 sentences that could form
the spine of a cover letter's opening or company paragraph.

**Required structure — all three elements must appear:**

1. **Hook that reveals the beef** — open with the strategic or product insight that
   explains why *this person* for *this company* right now. Not "I want this role."
   The hook should make the reader immediately understand the specific value the
   candidate brings, framed as a company opportunity or problem worth solving.

2. **Highly personal motivation story** — something only this person could say.
   A concrete life context, a specific use case, a genuine tension or constraint.
   If it could appear in any cover letter, it is not personal enough.
   Must include at least one detail that is specific, surprising, or honest enough
   to be slightly uncomfortable to share.

3. **Evidence of past** — one anchoring reference to a relevant past success that
   validates the claim. Not a metrics dump. One outcome, naturally woven in,
   that shows this isn't aspiration — it's a repeatable pattern.

**Additional rules:**
- Must be specific to this company and role — could not be transplanted to a
  competitor or a similar role elsewhere
- Must be written in first person, as the user would say it
- Must not use: "passionate about", "excited to join", "I've always believed",
  "I admire your mission", or any phrase that could appear in any cover letter
- May acknowledge complexity or nuance — a tension or a "because of X rather
  than despite X" reads as more genuine than pure enthusiasm
- Should feel like something the user would actually say, not something polished
  for an audience

**Example structure (not a template — illustrative only):**
```
[Hook — company insight/opportunity framed around the candidate's specific angle]
[Personal story — specific, concrete, could only be this person]
[Evidence hint — one past outcome that shows the pattern is real]
```

Present it clearly:

```
MOTIVATION STATEMENT (draft)

"[3–5 sentences covering all three elements]"

This is drawn from: [brief note on which answers informed it]
Hook:     [one line — what the opening reveals]
Personal: [one line — what makes it specific to this person]
Evidence: [one line — which past success anchors it]
```

Ask:
> "Does this feel true? You can approve it, adjust the wording, or tell me what's
> missing or wrong. This will be used as protected content in the cover letter —
> the generator won't rephrase or dilute it."

Iterate until approved.

---

### STEP 5 — Save outputs

**Output 1: Application motivation.md**

Save to `[APPLICATION_FOLDER]/motivation.md`:

```markdown
# Motivation — [Company] / [Role]

## Confirmed statement

[The approved 2–3 sentence motivation statement]

## Archetype(s)
[Name of archetype(s) that applied]

## Raw notes
[Brief summary of key answers from the interview — not a transcript,
just the 2–3 things said that most informed the statement]

## Protected content flag
This file is protected content for the cover letter generator.
The motivation statement must appear in the cover letter without being
paraphrased into generic enthusiasm language.
```

**Output 2: motivation-library.md entry**

Append a new entry to `[ASSETS_FOLDER]/motivation-library.md`.
If the file does not exist, create it using the template structure below.

Append:

```markdown
---

## Entry: [Company type / Role type / Date]

### Contextualised note
[1–2 sentences: what specifically drew you to this type of role or company.
Written so it can be recognised as relevant to future similar contexts.]

### Motivation structure
Archetype: [name]
Core draw: [one sentence — what the archetype is really about for you]
Reusable signal: [what to look for in a future job brief or company brief
that suggests this motivation is live — specific trigger words, company
characteristics, or role signals]

### Raw statement used
"[The confirmed motivation statement from this application]"

### Context
Role type: [e.g. Head of Product, B2B SaaS, Series B]
Company stage: [e.g. growth-stage, post-IPO, pre-PMF]
Date: [YYYYMMDD]
```

Confirm both files saved. Tell the user:

```
MOTIVATION WIZARD COMPLETE

Saved:
  Application:  [APPLICATION_FOLDER]/motivation.md
  Asset:        [ASSETS_FOLDER]/motivation-library.md (entry appended)

The motivation statement is locked in as protected content.
The cover letter generator will use it as the spine of the
company/motivation section — it will not be diluted or genericised.

Next: run the cover letter generator (Step 8 in GENERATE-CV-CL.md),
or return to the main workflow if you haven't completed earlier steps.
```
