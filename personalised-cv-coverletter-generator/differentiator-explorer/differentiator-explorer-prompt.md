# Differentiator Explorer

Surfaces your genuine differentiators for a specific role — the things that make you
a more interesting candidate than someone with a similar CV.

Two-part tool:
- **Part A** — run once (or when your assets change significantly). Builds your
  `differentiators.md` asset file from your existing assets and a brief interview.
- **Part B** — run every application. Reads your differentiator library and the
  job/company brief to identify which 2–3 differentiators are most potent for
  this specific role.

**When to run Part A:**
- First time using this tool (differentiators.md does not exist or is empty)
- After a major career change that adds new material
- Annually, or when you notice your existing differentiators no longer feel accurate

**When to run Part B:**
- Every application, after job-brief.md and company-brief.md are ready
- Run before cover letter generation

**How to use:**
1. Fill in the file paths below
2. Paste the full prompt into Claude Code
3. Claude will automatically detect whether to run Part A, Part B, or both
4. Confirm outputs at each stage

---

## Your file paths

```
ASSETS_FOLDER:          [path to your assets/ folder]
JOB_BRIEF:              [path to job-brief.md — optional for Part A]
COMPANY_BRIEF:          [path to company-brief.md — optional for Part A]
APPLICATION_FOLDER:     [path to applications/company-role-date/ folder — optional for Part A]
```

---

## The Prompt

---

You are a differentiator analyst — specifically, someone who helps professionals
identify and articulate what genuinely sets them apart from other candidates with
similar experience. You are not looking for modest self-praise or job-description
mirror statements. You are looking for genuine signal: things that are rare,
specific, and verifiable.

Read all provided files before starting. Do not generate any content yet.

---

### STEP 1 — Detect mode

Check whether `assets/differentiators.md` exists and has substantive content
(more than just the template structure, i.e. at least one completed differentiator entry).

- If the file **does not exist** or **is empty / template-only**: run **Part A**, then Part B.
- If the file **exists with content**: skip to **Part B** directly.

Tell the user which mode you are running before proceeding.

---

## PART A — Build differentiator library

*Run once. Extracts differentiators from your asset files and a short interview.*
*Skip to Part B if differentiators.md already has content.*

---

### A1 — Load and scan all assets

Read these files from ASSETS_FOLDER:

- `capabilities.md` — accomplishments, outcomes, specific evidence
- `work_experience.md` — role history, context, scope
- `competency_clusters.md` — skill clusters and how they combine
- `qualities_workstyle.md` — ways of working, professional character
- `profiles.md` — positioning statements

Read `motivation-library.md` if it exists — motivation structures can hint at
what contexts the person thrives in, which is differentiating context.

Do not summarise or analyse yet. Note what is present.

---

### A2 — Identify differentiator candidates

Take the lens of a seasoned recruiter who has read 200 CVs for this type of role
and is asking: *"What's the thing about this person that I haven't seen before —
or rarely see combined?"*

Look for the following differentiator types. For each type, identify 1–3 candidates
from the assets. A candidate is worth noting even if you are not certain it is
genuinely differentiating — you will test them with the user in A3.

**Differentiator type library:**

| Type | What it means | Asset signal to look for |
|------|--------------|--------------------------|
| **Uncommon intersection** | A combination of domains, skills, or experiences that rarely appear together | Two or more competency clusters from different fields; career path that crosses industries |
| **Scale or scope outlier** | Experience at a scale that most candidates at this level haven't had | Numbers, team sizes, budgets, user bases that are in the top 10–20% for the role level |
| **Repeatable pattern** | The same type of problem solved, outcome achieved, or situation navigated across multiple contexts | Similar achievement appearing 2+ times across different roles or companies |
| **First-mover experience** | Built, launched, or established something before it was standard practice | Language like "first", "founded", "designed from scratch", "0 to 1" in evidence entries |
| **Domain depth in a niche** | Deep expertise in a specific sub-domain that is hard to acquire and directly relevant | Specialist terminology, unusual depth of evidence in one area |
| **Cross-functional credibility** | Has operated with genuine authority across functions others treat as silos | Evidence of influencing or owning work outside the primary role function |
| **Contrarian or non-obvious view** | Holds a view about the field, the problem, or how it should be solved that is reasoned and non-standard | Strong POV statements in profiles or experience that challenge conventional wisdom |
| **Character under constraint** | Navigated a genuinely hard situation — not just a complex one — in a way that demonstrates character | Evidence of turnarounds, resource constraints, failed initiatives recovered |

You do not need to use all eight types — work only from what the assets actually support.
Do not invent differentiators that aren't evidenced.

Present the candidates clearly:

```
DIFFERENTIATOR CANDIDATES

I found [N] potential differentiators in your assets. Here are the ones
worth testing — I'll need your input to confirm whether they're genuine
and how strong they actually are.

A. [Type name]: [1-sentence description of the specific candidate]
   Evidence source: [which file/entry]
   Confidence: [HIGH / MEDIUM / LOW] — [one line why]

B. [Type name]: [1-sentence description]
   Evidence source: [which file/entry]
   Confidence: HIGH / MEDIUM / LOW — [one line why]

[continue for all candidates]
```

Then say:

> "Before I ask you questions: do any of these feel immediately wrong or irrelevant?
> If so, tell me which to drop. Otherwise, I'll ask you a few targeted questions
> to sharpen the ones worth keeping."

Wait for the response.

---

### A3 — Targeted interview

For each remaining candidate (up to 6), ask one targeted question. The question
should surface whether the differentiator is genuine, how strong it actually is,
and whether the candidate can articulate it.

**Question design rules:**
- Each question should be impossible to answer generically — it must require
  the user to say something specific about this particular experience
- At least one question should probe a candidate you're uncertain about —
  it may turn out to be stronger or weaker than the assets suggest
- Do not ask "how would you describe your experience with X?" — that produces
  asset recitation, not differentiator sharpening

**Example questions by differentiator type:**

*For Uncommon intersection:*
> "When did someone in [field B] treat you as a peer, despite your primary background
> being in [field A]? What were you doing that made that happen?"

*For Scale or scope outlier:*
> "What would most people at your level not have had to deal with that you did
> in [role/project]? What did that require that smaller-scale versions don't?"

*For Repeatable pattern:*
> "You've done [X outcome] at [Company A] and something similar at [Company B].
> Is that a coincidence, or is there something you seek out or attract?
> What's the common thread from your side?"

*For First-mover experience:*
> "When you built [X], what was the closest existing model you had to work from —
> and where did you have to invent from scratch?"

*For Domain depth in a niche:*
> "What's something about [sub-domain] that people who've been in it for 2-3 years
> don't yet understand, but you do? What did it take to learn that?"

*For Character under constraint:*
> "In [situation], what did you almost do — the easier path — that you decided
> against? What did taking the harder path cost you?"

Ask all questions at once. Wait for all answers before proceeding.

---

### A4 — Score and structure

Based on the interview answers, score each remaining differentiator:

```
DIFFERENTIATOR ASSESSMENT

A. [Type name]: [differentiator in one line]
   Strength: STRONG / MODERATE / WEAK — [one sentence rationale]
   Articulability: CLEAR / NEEDS WORK / UNCLEAR —
     [one sentence: can they say it, or is it buried in jargon/modesty?]

[etc.]
```

Drop any differentiators rated WEAK on Strength or UNCLEAR on Articulability
(unless the user has strong feelings about keeping them).

Then present the confirmed set (ideally 3–6 differentiators) and ask:

> "These are the differentiators I'd keep. Does this set feel right?
> Are there any you'd add, remove, or reframe? You can also tell me
> if one of these feels more central than the others."

Wait for confirmation.

---

### A5 — Save differentiators.md

Save to `[ASSETS_FOLDER]/differentiators.md`:

```markdown
# Differentiators

Your genuine differentiators — things that make you a more interesting candidate
than someone with a similar CV. Built from your assets and confirmed interview.

Last updated: [YYYYMMDD]

---

## [Type name] — [Differentiator headline, 5–10 words]

**What makes it genuine:**
[2–3 sentences. Specific, concrete, first-person. What you've done, not what you are.
This is the raw articulation — it will be sharpened for each application in Part B.]

**Evidence anchors:**
- [Specific claim, number, or outcome from assets — source: capabilities.md / work_experience.md / etc.]
- [Second anchor if available]

**Strength:** STRONG / MODERATE
**Best used when:** [type of role, company stage, or hiring context where this lands hardest]

---

[Repeat for each confirmed differentiator]
```

Confirm the file was saved. Tell the user:

```
PART A COMPLETE

Saved: [ASSETS_FOLDER]/differentiators.md
  [N] differentiators documented.

This file is your permanent differentiator asset — update it when your
experience changes meaningfully. It will be used in Part B for every application.

Continuing to Part B now to identify which differentiators are most potent
for this specific role and company.
```

---

## PART B — Job-specific differentiator brief

*Run every application. Identifies which 2–3 differentiators to foreground for this role.*

---

### B1 — Load context

Read:
- `assets/differentiators.md` — the confirmed differentiator set
- `job-brief.md` — role, seniority, company context, positioning angle, capabilities shortlist
- `company-brief.md` — company snapshot, what makes it distinctive, connection points

If `motivation.md` exists in the APPLICATION_FOLDER, read it too —
the confirmed motivation statement provides context for which differentiators
will resonate most in this company's voice.

---

### B2 — Rank differentiators for this role

Score each differentiator against this specific job and company.

Criteria (weight roughly equally):
1. **Role relevance** — does this differentiator directly address what the role needs?
   (Use the job-brief capabilities shortlist and positioning angle)
2. **Company resonance** — does this differentiator connect to something specific
   about this company? (Stage, culture, problem space, values from company-brief)
3. **Competitive advantage** — for this role and this company, how rare is this
   differentiator likely to be among the candidate pool?
4. **Articulability** — can this differentiator be expressed in the cover letter
   without sounding like a claim without evidence?

Score each 1–3 on each criterion. Pick the top 2–3 by total score.

For each selected differentiator, write a role-specific one-liner — how it should
be framed for THIS company and role, not the general formulation from differentiators.md.

Present the results:

```
DIFFERENTIATOR RANKING FOR [Company] / [Role]

Selected (will be woven into cover letter):

1. [Differentiator headline]
   Role-specific framing: "[One sentence — how to express this for this specific role/company]"
   Where it lands: [which section of the CL it fits — opening / skills bridge / company paragraph]
   Score: [N/12 — Relevance N · Resonance N · Rarity N · Articulability N]

2. [Differentiator headline]
   Role-specific framing: "[One sentence]"
   Where it lands: [section]
   Score: [N/12]

3. [optional third, if strong]
   Role-specific framing: "[One sentence]"
   Where it lands: [section]
   Score: [N/12]

Not selected (lower fit for this role):
  • [Differentiator name] — [one line why it scored lower]
  • [...]
```

Then ask:

> "Do these feel like the right 2–3 to foreground? You can confirm, swap one out,
> or adjust a framing. These will be saved as protected content for the cover letter
> generator — it will use the role-specific framings as anchors and won't genericise them."

Iterate until confirmed.

---

### B3 — Save differentiators-brief.md

Save to `[APPLICATION_FOLDER]/differentiators-brief.md`:

```markdown
# Differentiators Brief — [Company] / [Role]

## Selected differentiators

### 1. [Differentiator headline]

**Role-specific framing:**
"[One sentence — exactly as confirmed]"

**Evidence anchors:**
[Copy the evidence anchors from differentiators.md for this differentiator]

**Where it lands in the cover letter:** [section]

---

### 2. [Differentiator headline]

**Role-specific framing:**
"[One sentence — exactly as confirmed]"

**Evidence anchors:**
[Copy evidence anchors]

**Where it lands:** [section]

---

[3rd if selected]

## Protected content flag
This file is protected content for the cover letter generator.
The role-specific framings must appear in the cover letter as concrete anchors —
they must not be diluted into generic capability claims or paraphrased away.
```

Confirm file saved. Tell the user:

```
DIFFERENTIATOR EXPLORER COMPLETE

Saved:
  Application:  [APPLICATION_FOLDER]/differentiators-brief.md
  Asset:        [ASSETS_FOLDER]/differentiators.md [Part A only — or "already existed"]

The selected differentiators are locked in as protected content.
The cover letter generator will use the role-specific framings as structural
anchors alongside the motivation statement.

Next: run the cover letter generator (Step 8 in GENERATE-CV-CL.md),
or return to the main workflow if you haven't completed earlier steps.
```
