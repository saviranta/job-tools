# Eval Tools

Optional quality checks for generated CV and cover letter applications.
Two tools — one script, one prompt — covering different failure modes.

---

## eval.py — Mechanical checks

Runs three deterministic checks against the output markdown files:

| Check | What it catches |
|-------|----------------|
| Keyword coverage | Job-brief keywords missing from CV and CL text |
| Citation integrity | `<!-- source: X -->` comments that don't trace to a real capability entry |
| Metric integrity | Numbers/percentages in CV bullets that don't appear verbatim in the assets |

**Run it:**
```bash
python eval/eval.py [application_folder] [assets_folder]

# Example:
python eval/eval.py ~/cv-workspace/applications/acme-pm-20260228 ~/cv-workspace/assets
```

Assets folder defaults to `../../assets` relative to the application folder
(i.e. `workspace/assets/`) if not provided.

**Requires:** Python 3.10+ (uses `Path | None` union syntax). No dependencies beyond stdlib.

---

## eval-prompt.md — Qualitative checks

Four rubrics covering things the script can't detect:

| Rubric | What it checks |
|--------|---------------|
| Positioning fit | Does the CL opening land the job-brief angle, or drift generic? |
| Evidence prominence | Is the strongest metric near the top, or buried? |
| Company specificity | Does the company paragraph name something real, or just praise? |
| Claim-to-evidence balance | Are strong claims backed by proportionate evidence? |

Scores each rubric 1–3. Total 4–12 with interpretation bands (10–12 = ready to send).

**Run it:** Paste `eval/eval-prompt.md` from `<!-- BEGIN PROMPT -->` into Claude Code
with the CV, CL, job-brief, and company-brief file paths filled in.

---

## Trace log

The main workflow (GENERATE-CV-CL.md Step 10) saves a `trace.md` to each application
folder automatically. It records: templates used, CAP-IDs selected, keyword hit rate,
iteration counts, guardrail results, and the eval commands to run.

Use the trace log to spot patterns across applications:
- Consistently missing certain keyword types → adjust Phase 1 keyword selection
- High iteration counts on CL Phase 2 → adjust CL template or writing-style.md
- Recurring guardrail warnings → strengthen those asset entries
