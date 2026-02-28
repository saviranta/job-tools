# CV and Cover Letter Reviewer Prompt

Reviews your CV and cover letter from six perspectives and returns
a prioritised, actionable feedback summary.

**How to use:**
1. Fill in the file paths (Claude Code) or paste content directly
2. Paste the prompt into Claude Code or Claude
3. Review the feedback and choose which suggestions to apply
4. Claude guides you through each chosen edit

---

## Your file paths (Claude Code)

```
CV_DRAFT:           [path to YYYYMMDD_[surname]_[company]_cv.md]
CL_DRAFT:           [path to YYYYMMDD_[surname]_[company]_cl.md]
JOB_BRIEF:          [path to job-brief.md]
COMPANY_BRIEF:      [path to company-brief.md — or leave blank]
CV_TEMPLATE:        [path to cv-template.md — for ATS and format context]
CL_TEMPLATE:        [path to cover-letter-template.md — for intent context]
```

**Or paste directly:**
Skip the paths and paste the content of each file after the prompt.

---

## The Prompt

---

You are reviewing a CV and cover letter from six distinct perspectives.
Each perspective has a different evaluation lens — what one persona prioritises,
another ignores entirely.

Read all provided files before starting. Then work through each persona in sequence.

The role being applied for and the company context come from the job-brief.
Calibrate every persona to that specific context — a "Role Expert" reviewing
a CFO application has entirely different criteria from one reviewing a UX designer application.

---

### Persona 1: ATS — Applicant Tracking System

*Lens: a machine parsing the CV for keyword matches and structural compliance.
No interpretation, no context, no charity. Only what's literally present.*

**What to evaluate (CV only):**

1. **Keyword match** — Cross-reference the job-brief keywords list against the CV text.
   Report: which keywords are present (and where), which are absent, which are
   paraphrased but not verbatim (ATS may not match these).

2. **Section header compliance** — Are section headers using standard parseable names
   ("Work Experience" not "Where I've Been", "Education" not "Learning")?
   Flag non-standard headers.

3. **Format risks** — Any of the following will cause ATS parsing failures:
   - Two-column layouts (content in columns is often read out of order)
   - Tables used for content (not just formatting)
   - Text inside graphics or image files
   - Headers/footers containing important information
   - Non-standard fonts that may not embed correctly
   Note: flag these only if the cv-template indicates a designed/two-column format.

4. **Keyword density** — Are the top 3 priority keywords from the job-brief
   appearing at least twice each in the CV body?

**Output format:**

```
── ATS ─────────────────────────────────────
Signal: STRONG / GOOD / MIXED / WEAK

Keywords present:    [list — term: location]
Keywords absent:     [list — these are gaps]
Keywords paraphrased only: [list — at risk]

Observations:
• [observation 1]
• [observation 2]

Change suggestions:
1. [specific, actionable change]
2. [specific, actionable change]
────────────────────────────────────────────
```

---

### Persona 2: HR Recruiter / Application Reviewer

*Lens: a recruiter with 200 applications to screen. Spending 15–30 seconds on the CV,
60 seconds on the cover letter if the CV clears. Looking for reasons to progress or reject.*

**What to evaluate:**

*CV (15-second scan):*
1. **Role fit legibility** — Can they see in one scan what this person does and why
   they fit? Is the headline/title right? Is the most relevant role prominent?
2. **Scannability** — Does visual hierarchy guide the eye? Are bullets digestible?
   Are dates and company names easy to locate?
3. **Red flags** — Employment gaps (unexplained), very short tenures, title inflation,
   vague claims without evidence, a recent role that seems like a step down.
4. **Seniority signal** — Does the CV read at the right level for the role?
   (Too junior = undersells; too senior = misaligned)

*Cover letter (60-second read):*
1. **Does the opening earn the next sentence?** Is the first line interesting enough
   to continue reading, or does it feel like every other letter?
2. **Is the fit obvious by the end of paragraph 1?** Or does the recruiter have to
   work to understand why this person applied?
3. **Length appropriateness** — Does it respect the reader's time?

**Output format:**

```
── HR RECRUITER ─────────────────────────────
Signal: STRONG / GOOD / MIXED / WEAK

Observations:
• [observation 1 — CV]
• [observation 2 — CL]
• [observation 3]

Red flags identified:
• [flag or "None identified"]

Change suggestions:
1. [specific change]
2. [specific change]
─────────────────────────────────────────────
```

---

### Persona 3: Hiring Manager

*Lens: the person who will actually work with this candidate. They know the role deeply,
have read the job description recently, and are asking: "Can this person do the job?
Would I want them on my team? Would I trust them with this?"*

**What to evaluate (CV + CL):**

1. **Evidence quality** — Are accomplishments specific and credible?
   "Led a team" is weak. "Led a 6-person team that reduced onboarding time by 40%" is strong.
   Flag every claim that would prompt "prove it" in an interview.

2. **Seniority calibration** — Does the scope of evidence match the level of the role?
   Under-scoped (too junior): lacks evidence of the scale or independence the role requires.
   Over-scoped (too senior): may make the hiring manager worry the candidate would be bored
   or frustrated.

3. **Domain credibility** — Does this person sound like they've actually done this work?
   Are they using the vocabulary correctly? Is there evidence of genuine depth,
   or does it read like someone who has skimmed the job description?

4. **Interview risk** — Identify 1–2 claims in the CV or CL that would be challenged
   or probed in interview. Are they well-supported enough to withstand that?

5. **CL positioning** — Does the cover letter's positioning angle (from job-brief)
   land convincingly? Does it address the right problem?

**Output format:**

```
── HIRING MANAGER ───────────────────────────
Signal: STRONG / GOOD / MIXED / WEAK

Observations:
• [observation 1]
• [observation 2]
• [observation 3]

Interview risk flags:
• "[claim]" — likely to be probed; [assessment of how well it's supported]

Change suggestions:
1. [specific change]
2. [specific change]
─────────────────────────────────────────────
```

---

### Persona 4: Role Expert

*Lens: a senior practitioner in the exact field being applied for — a peer or near-peer.
They are reading for technical accuracy, realistic claims, and genuine depth.
They will notice misused terminology, inflated scope, and missing signals
that someone who's really done this work would naturally include.*

**Calibrate this persona to the role from the job-brief.**
Examples of calibration:
- Product management: looking for evidence of discovery work, prioritisation decisions,
  stakeholder trade-offs, not just shipping features
- Software engineering: looking for architectural decisions, scale signals, testing discipline
- Sales: looking for pipeline numbers, methodology signals, named deal complexity
- Research: looking for methodology rigour, sample sizes, insight-to-action chain
- Design: looking for process signals, constraints navigated, not just portfolio outputs

**What to evaluate (CV primarily, CL briefly):**

1. **Terminology accuracy** — Is domain vocabulary used correctly and precisely?
   Flag any terms that are misused, over-generalised, or would make a peer wince.

2. **Depth vs surface exposure** — Does the evidence suggest the candidate has gone
   deep in this work, or skimmed across it? What's missing that deep experience
   would naturally produce?

3. **Peer credibility** — Would a senior practitioner in this field take this CV
   seriously as a peer-level application? What would they question?

4. **Missing domain signals** — What evidence, if present, would significantly
   strengthen credibility in this role? (Specific tools, methodologies, scale markers,
   types of problem solved.)

**Output format:**

```
── ROLE EXPERT ──────────────────────────────
Signal: STRONG / GOOD / MIXED / WEAK
[Role calibration: e.g. "Reviewing as: Senior Product Manager, B2B SaaS"]

Observations:
• [observation 1]
• [observation 2]
• [observation 3]

Missing domain signals:
• [what's absent that would strengthen credibility]

Change suggestions:
1. [specific change]
2. [specific change]
─────────────────────────────────────────────
```

---

### Persona 5: CEO / CFO / Legal — Joint Review

*Three lenses, one review. They read together when a candidate is being considered
at a level that touches leadership, budget, or risk. Their concerns don't always align.*

**CEO lens:**
- Does this person read as a leader, not just an executor?
- Is their ambition calibrated appropriately — neither timid nor grandiose?
- Do they show commercial or strategic thinking, not just functional excellence?
- Culture signal: would this person fit the leadership team?

**CFO lens:**
- Are numerical claims precise and defensible? ("~$2M impact" vs "significant revenue impact")
- Is commercial scope correctly represented? (P&L ownership, budget authority, revenue responsibility)
- Any claims that would be hard to evidence if reference-checked?

**Legal lens:**
- Any statements that could create liability? (Claiming ownership of IP, naming confidential
  clients, stating competitive intelligence, claiming sole credit for team achievements)
- NDA risk: does any claim reveal information a previous employer might consider protected?
- Any statements that are factually risky if challenged? (e.g. overstated titles, dates)

**What to evaluate (CV + CL):**

**Output format:**

```
── CEO / CFO / LEGAL ────────────────────────
Signal: STRONG / GOOD / MIXED / WEAK

CEO observations:
• [observation]
• [observation]

CFO observations:
• [observation or "No concerns"]

Legal flags:
• [flag or "No flags identified"]

Change suggestions:
1. [specific change — note which lens it addresses]
2. [specific change]
─────────────────────────────────────────────
```

---

### Persona 6: Narrative Copywriter

*Lens: a professional writer who crafts persuasive, human-sounding documents.
They are reading for voice, clichés, rhythm, and whether this feels like
a person wrote it or a template produced it.*

**What to evaluate (CL primarily, CV briefly):**

1. **Cliché audit** — Flag every cliché in both documents:
   "results-driven", "passionate about", "team player", "proven track record",
   "dynamic", "leverage", "synergy", "detail-oriented", "strategic thinker",
   "thought leader", "move the needle", "circle back", or any phrase that
   has been used so many times it carries no meaning.
   For each: suggest a concrete replacement.

2. **Opening line** — Does the cover letter's first sentence earn the second?
   Rate it: Earns it / Borderline / Loses the reader.
   If borderline or losing: suggest a stronger alternative.

3. **Voice consistency** — Does the document sound like one person throughout,
   or does the register shift awkwardly? Are there sentences that clearly sound
   AI-generated next to sentences that sound human?

4. **Career narrative** — Does the CV tell a coherent story when read as a whole?
   Is there a clear throughline — a direction the career is heading — or does it
   read as a list of disconnected jobs?

5. **The one line working hardest** — Identify the single most effective sentence
   in the cover letter. This is the line to protect and build around.

**Output format:**

```
── NARRATIVE COPYWRITER ─────────────────────
Signal: STRONG / GOOD / MIXED / WEAK

Clichés found:
• "[phrase]" → suggest: [replacement]
• "[phrase]" → suggest: [replacement]
• [or "None found — well done"]

Opening line: [Earns it / Borderline / Loses the reader]
[Assessment + suggested alternative if needed]

Best line in the CL:
"[the line]"

Observations:
• [voice/narrative observation]
• [voice/narrative observation]

Change suggestions:
1. [specific change]
2. [specific change]
─────────────────────────────────────────────
```

---

### Cross-persona priority summary

After all six personas, produce a priority table:

```
═══════════════════════════════════════════════
PRIORITY CHANGE SUMMARY
═══════════════════════════════════════════════

HIGH PRIORITY — flagged by 2+ personas:
  1. [issue] — flagged by: [Persona A, Persona B]
     Action: [consolidated change suggestion]

  2. [issue] — flagged by: [Persona A, Persona C]
     Action: [consolidated change suggestion]

MEDIUM PRIORITY — single persona, high signal:
  3. [issue] — flagged by: [Persona]
     Action: [change suggestion]

LOW PRIORITY — minor or stylistic:
  4. [issue]
     Action: [change suggestion]

THINGS WORKING WELL — do not change:
  • [what's landing across multiple personas]
  • [what's landing across multiple personas]
═══════════════════════════════════════════════
```

---

### User choice and edit guidance

After the summary, ask:

"Which recommendations would you like to apply?

You can say:
- **All high priority** — apply everything in the HIGH PRIORITY section
- **[Persona name] only** — e.g. 'HR Recruiter and Copywriter only'
- **[Item numbers]** — e.g. 'Apply 1, 3, and 5'
- **None** — useful to know, no changes needed right now

Or describe specific changes you want to make and I'll guide you to the right place."

**Before applying: check for contradictions between selected items.**
If two selected recommendations conflict with each other (e.g. ATS says add a keyword that the Copywriter flagged as a cliché; HR Recruiter wants shorter bullets that the Hiring Manager wants expanded with more evidence), surface the conflict explicitly:

```
CONFLICT DETECTED
  Item [N] and Item [M] contradict each other:
  [N]: [what it recommends]
  [M]: [what it recommends]
  Which takes priority for this application?
```

Wait for the user to resolve any conflicts before proceeding.

For each chosen recommendation, provide:
- The exact text to find in the `.md` file
- The replacement text
- Whether the change also affects the HTML (and if so, which slot)

After edits are confirmed: remind the user to re-run Phase 4 of the relevant
generator (cv-generator or cover-letter-generator) to sync changes to the HTML
output file and check for any asset improvements worth saving.
