# Capabilities & Accomplishments

<!--
PURPOSE: Your searchable career database, split into two sections for efficient loading.

INDEX — lightweight lookup table used in Phase 1 selection.
        One row per entry. Read this to score and shortlist CAP-IDs.

ENTRIES — full capability/accomplishment content. Loaded by CAP-ID in Phase 2.
          Only the selected entries are read — not the whole section.

HOW DOWNSTREAM TOOLS USE THIS FILE:
- cv-generator Phase 1: reads INDEX only → selects CAP-IDs
- cv-generator Phase 2: loads ENTRIES for selected CAP-IDs only
- cover-letter-generator: reads INDEX, then loads 1–6 ENTRIES scaled to length_style
- Cross-references: Role IDs → work_experience.md | Cluster IDs → competency_clusters.md
- Evidence / Metrics in ENTRIES are used verbatim in bullets — never paraphrased

DESIGN PRINCIPLE:
Keep entries atomic — one capability or one accomplishment per entry.
A capability is something you can do. An accomplishment is proof that you did it.
Both belong here. The generator mixes them based on what the job ad signals.
-->

---

## INDEX

One table per role. List every capability/accomplishment from that role.
Phase 1 reads only this section — keep Preview tight and specific (the key metric or outcome).

Evidence levels:
- `strong` — metric + clear outcome present
- `moderate` — outcome described, no specific metric
- `thin` — stated but vague; will be omitted or framed directionally by cv-generator

### ROLE-001 — [Title], [Company] ([start year]–[end year])

| ID | Entry title | Clusters | Evidence | Preview |
|----|-------------|----------|----------|---------|
| CAP-001 | [Short entry title — max 8 words] | [CLUS-ID], [CLUS-ID] | strong | [key metric or outcome in ≤8 words] |
| CAP-002 | [Short entry title] | [CLUS-ID] | moderate | [outcome in ≤8 words] |

### ROLE-002 — [Title], [Company] ([start year]–[end year])

| ID | Entry title | Clusters | Evidence | Preview |
|----|-------------|----------|----------|---------|
| CAP-003 | [Short entry title] | [CLUS-ID], [CLUS-ID] | strong | [key metric in ≤8 words] |
| CAP-004 | [Short entry title] | [CLUS-ID] | thin | [what it covers in ≤8 words] |

---

## ENTRIES

Full content for each entry. Loaded by CAP-ID — only selected entries are read.
Keep exact metrics here; they are quoted verbatim into CV bullets.

### CAP-001 — [Entry title] [ROLE-001]

**Type**: Capability / Accomplishment
**Description**:
[What you did or can do. Be concrete. 1–3 sentences.]

**Evidence / Metrics**:
[Numbers, outcomes, deliverables. Be exact — these are used verbatim.
"Grew X by Y% in Z months" is better than "significantly improved X".]

**Tags**: `tag1`, `tag2`, `tag3`
**Context Relevance**: startup, b2b

---

### CAP-002 — [Entry title] [ROLE-001]

**Type**: Capability / Accomplishment
**Description**:
[What you did or can do.]

**Evidence / Metrics**:
[Proof point. If no hard metric, describe the outcome specifically.]

**Tags**: `tag1`, `tag2`
**Context Relevance**: enterprise

---

### CAP-003 — [Entry title] [ROLE-002]

**Type**: Capability / Accomplishment
**Description**:
[What you did or can do.]

**Evidence / Metrics**:
[Proof point.]

**Tags**: `tag1`, `tag2`
**Context Relevance**: b2b, saas

---

### CAP-004 — [Entry title] [ROLE-002]

**Type**: Capability
**Description**:
[What you can do — even without a strong proof point. Mark honestly.]

**Evidence / Metrics**:
[Whatever you have. If thin: note "no specific metric available".]

**Tags**: `tag1`
**Context Relevance**: any

---

<!--
TIPS FOR GOOD ENTRIES:

INDEX tips:
- Preview should be the strongest single datapoint from Evidence — what would make a
  recruiter stop and read more. Think: "most impressive thing in ≤8 words"
- Set Evidence level honestly — thin evidence prompts the cv-generator to omit or
  frame directionally rather than write a confident claim

ENTRIES tips:
- Accomplishments > capabilities. "Grew revenue 3x in 18 months" beats "Revenue growth"
- Be specific with numbers even if approximate: "~50%" is better than "significantly"
- One metric per entry. If you have three metrics, make three entries with three CAP-IDs
- Tags should match words a recruiter would use in a job ad, not your internal jargon
- If a cluster is unclear, leave it blank and fill it in later

MAINTENANCE:
- When you add a new entry: add a row to INDEX first, then add the full entry to ENTRIES
- Keep CAP-IDs sequential across all roles (CAP-001, CAP-002... not per-role)
- Role IDs must match work_experience.md exactly
-->
