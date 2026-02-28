# Job Listing Analyzer

Match a job ad against your career asset library to get a targeted brief
for your CV and cover letter.

---

## Option A: Paste the job listing

**Best for:** Any job ad, no tools required.

1. Copy the full job listing text (title, responsibilities, requirements, nice-to-haves)
2. Copy your five asset files
3. Paste the prompt below into Claude, followed by the job listing and your assets

---

## Option B: Claude Code + Chrome MCP (read the listing directly)

**Best for:** Claude Code users with the Chrome MCP extension. Avoids copy-paste,
and Claude can re-read specific sections if needed.

Ask Claude Code:

```
Analyze this job listing against my career asset library.

Job listing URL: [paste URL here]

Please:
1. Navigate to the job listing and read the full description
2. If there's a "see more" or truncated section, expand it before reading
3. Use the analysis prompt below to produce the job brief

My asset files are at: [path to your assets/ folder]

[PASTE THE ANALYSIS PROMPT FROM BELOW]
```

---

## The Analysis Prompt

Paste this into Claude (with your assets and the job listing text, or via MCP as above).

---

You are analyzing a job listing against my career asset library to produce a targeted job brief.

Here is the job listing:

[PASTE JOB LISTING HERE — or omit if using Chrome MCP]

Here are my asset files:

[PASTE work_experience.md]

[PASTE capabilities.md]

[PASTE competency_clusters.md]

[PASTE qualities_workstyle.md]

[PASTE profiles.md]

---

Analyze the job listing and produce a structured job brief with the following sections:

**1. Role snapshot**
- Job title, company name, seniority level (IC / lead / manager / director+)
- What problem this role is hired to solve
- The one thing they're optimising for (speed, quality, scale, transformation, etc.)

**2. Cluster ranking**
List my competency clusters in order of relevance to this job ad.
For each, note the specific job ad phrases that activate it.
Format:
```
1. [CLUSTER-ID] [Cluster Name] — activated by: "phrase", "phrase"
2. ...
```
Flag clusters the job strongly emphasises that I have thin evidence for.

**3. Capability shortlist**
Select the 6-10 capabilities and accomplishments from my assets that best match this role.
For each, note:
- The entry title
- Why it's relevant (one line)
- Whether the evidence is strong, moderate, or thin

**4. Role and experience selection**
- Which of my roles should feature on the CV for this application?
- Which should be de-emphasised or omitted?
- How should the most relevant role be framed for this context?

**5. Profile recommendation**
- Which of my profiles (from profiles.md) is the closest fit?
- What one or two adjustments would make it land better for this specific role?

**6. Keywords to mirror**
List exact phrases from the job ad that I should use in my CV and cover letter
(not paraphrased — the actual words). Group by theme:
- Role-specific terms
- Methodology / process terms
- Outcome / impact terms
- Soft skill / culture terms

**7. Positioning angle**
In 2-3 sentences: what is the strongest claim I can make for this role,
given my evidence? This is the core argument the cover letter should build around.

**8. Gaps and reframes**
- What does the job ask for that is weak or absent in my assets?
- For each gap: is it a real gap, or can it be reframed from existing evidence?
- Suggest a reframe where possible.

Output this as a structured markdown document I can save as `job-brief.md`.
