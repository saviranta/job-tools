# Qualitative Eval Prompt

Evaluates a generated CV and cover letter on four structural quality rubrics.
Faster and more targeted than the 6-persona reviewer — designed to catch
systemic generation problems, not to polish finished copy.

**When to use:**
- After any generation run, before or after the 6-persona review
- When iterating on prompts (run this across several applications to spot patterns)
- As a quick sanity check when you've made changes to asset files or templates

**How to use in Claude Code:**
1. Fill in the file paths below
2. Paste the full prompt into Claude Code

---

## Your file paths

```
CV_DRAFT:       [path to YYYYMMDD_surname_company_cv.md]
CL_DRAFT:       [path to YYYYMMDD_surname_company_cl.md]
JOB_BRIEF:      [path to job-brief.md]
COMPANY_BRIEF:  [path to company-brief.md]
```

---

## The Prompt

<!-- BEGIN PROMPT -->

---

You are running a targeted quality eval on a generated CV and cover letter.
Read all four files, then evaluate against the four rubrics below.

This is not a line-by-line review — it is a structural diagnosis.
Each rubric scores 1–3. Total score is 4–12.

---

### Rubric 1: Positioning angle fit (CV + CL)

*Does the cover letter's opening actually land the positioning angle from the job-brief?
Or does it drift into generic language that could apply to any application?*

Check:
- Find the "Positioning angle" in job-brief.md (section 7)
- Read the first 2–3 sentences of the cover letter
- Read the profile / summary section of the CV

Score:
- **3** — The positioning angle is clearly present in both the CL opening and the CV profile.
  The application makes a specific claim that matches the job-brief's stated angle.
- **2** — The positioning angle is present but diluted. One document lands it;
  the other is generic or only implies it.
- **1** — The positioning angle is missing or buried. The CL opens generically.
  A recruiter reading it would not know the specific argument being made.

Output:
```
Rubric 1 — Positioning angle fit:  [score]/3
  [1–2 sentences: what's landing, what's missing]
  Flag: [specific sentence or section that most needs attention — or "none"]
```

---

### Rubric 2: Evidence prominence

*Is the strongest capability evidence in the most visible positions?
The most impressive metric or outcome should be near the top, not buried.*

Check:
- Identify the 1–2 strongest evidence items (clearest metric or outcome) across the
  CV and CL. Look at both the content and the Evidence level in the trace log if available.
- Check where these appear: profile? First bullet of first role? Mid-CV? CL body?

Score:
- **3** — Strongest evidence appears within the first visible section of the CV
  (profile or first role block) AND within the CL body (not just at the end).
- **2** — Strongest evidence is present but not prominently positioned. It's findable
  but takes effort to see on a scan.
- **1** — The strongest evidence is buried — mid-CV or not in the CL at all.
  A 15-second scan would miss it.

Output:
```
Rubric 2 — Evidence prominence:  [score]/3
  Strongest evidence: "[the metric or outcome]"
  Where it appears: [CV section + CL section — or "CL only" / "buried in role 2"]
  Flag: [specific move to improve prominence — or "none"]
```

---

### Rubric 3: Company paragraph specificity

*Does the cover letter's company reference paragraph name something specific,
or does it read as generic praise that could apply to any company?*

Check:
- Find the company connection paragraph in the CL (usually the paragraph referencing
  the company directly — their mission, a product, an initiative)
- Cross-check: is every specific claim in that paragraph traceable to a named
  item in company-brief.md? (connection points, recent initiatives, values language)

Score:
- **3** — The paragraph names a specific product decision, initiative, stated value,
  or observable signal from company-brief. It could not be sent to any other company.
- **2** — The paragraph references the company's general domain or mission but
  doesn't name anything specific. It's tailored but not anchored.
- **1** — The paragraph is generic ("I admire your innovative approach" / "your
  impressive growth trajectory"). It could appear in any cover letter.

Output:
```
Rubric 3 — Company paragraph specificity:  [score]/3
  Specific reference found: [the named thing — or "none"]
  In company-brief: [yes / no / partially]
  Flag: [what specific reference from company-brief could replace the generic — or "none"]
```

---

### Rubric 4: Metric-to-claim balance

*Are strong claims backed by proportionate evidence?
A claim is only as credible as the evidence behind it.*

Check:
- Identify the 2–3 strongest claims in the CV and CL (statements of impact, leadership,
  or exceptional results)
- For each: is there a specific metric or concrete outcome directly attached?
- Flag any claim where the strength of the assertion outpaces the evidence

Score:
- **3** — All strong claims have proportionate evidence attached. The documents
  make no claim they can't support within the same sentence or bullet.
- **2** — Most claims are backed; 1–2 have evidence that is slightly underpowered
  (claim is bold, metric is vague or absent).
- **1** — One or more significant claims are unsupported. The document asserts
  something impressive without evidence to match.

Output:
```
Rubric 4 — Metric-to-claim balance:  [score]/3
  Strongest unsupported claim: "[the claim]" — [why it's underpowered]
  [or "All strong claims are backed"]
  Flag: [suggested addition or softening — or "none"]
```

---

### Summary

After all four rubrics:

```
═══════════════════════════════════════
EVAL SUMMARY
═══════════════════════════════════════
Rubric 1 — Positioning fit:       [N]/3
Rubric 2 — Evidence prominence:   [N]/3
Rubric 3 — Company specificity:   [N]/3
Rubric 4 — Claim-to-evidence:     [N]/3
                                 ─────
Total:                            [N]/12

Interpretation:
  10–12  Strong — ready to send
  7–9    Good — one focused improvement recommended
  4–6    Needs work — address flagged items before sending

Priority fix: [the single highest-impact flag from the rubrics above]
═══════════════════════════════════════
```

Ask: "Would you like me to address any of the flagged items?
Tell me which rubric(s) to work on, or say **skip** to move on."
