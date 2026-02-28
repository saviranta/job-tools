# Capabilities & Accomplishments

<!--
PURPOSE: Your searchable career database. This is the core asset file.
Every capability you have and every meaningful thing you've achieved lives here,
tagged and cross-referenced so the cv-generator can find exactly the right
evidence for any job ad.

HOW DOWNSTREAM TOOLS USE THIS FILE:
- cv-generator searches by Tags to find relevant capabilities for a job ad
- Cluster refs link capabilities to competency_clusters.md for skills sections
- Role refs link to work_experience.md to provide context
- Evidence/Metrics are pulled verbatim into CV bullet points

DESIGN PRINCIPLE:
Keep entries atomic — one capability or one accomplishment per row.
A capability is something you can do. An accomplishment is proof that you did it.
Both belong here. The cv-generator mixes them based on what the job ad signals.
-->

## Column Reference

| Column | Purpose | Values |
|--------|---------|--------|
| Category | Grouping for navigation | e.g. Leadership, Strategy, Execution, Technical, Domain |
| Type | Capability or evidence | `Capability` or `Accomplishment` |
| Title | Short label | Max 8 words |
| Description | Full description | 1-3 sentences or bullet points |
| Evidence / Metrics | Proof points | Numbers, outcomes, deliverables — be specific |
| Tags | Keyword matching | Lowercase, comma-separated |
| Context Relevance | Where this fits best | e.g. startup, enterprise, b2b, healthcare |
| Role | Which job this comes from | ID from work_experience.md |
| Clusters | Competency cluster match | IDs from competency_clusters.md |

---

## Data

<!--
Add one entry per capability or accomplishment.
Copy the block below and fill it in. Delete columns you don't have data for yet.
-->

### [Category Name]

**Title**: [Short label]
**Type**: Capability / Accomplishment
**Description**:
[What you do or did. Be concrete.]

**Evidence / Metrics**:
[Numbers, outcomes, or specific deliverables. "Grew X by Y%", "Led team of N", "Delivered in Z weeks".]

**Tags**: `tag1`, `tag2`, `tag3`
**Context Relevance**: startup, b2b
**Role**: ROLE-1
**Clusters**: EXEC, METR

---

**Title**: [Short label]
**Type**: Capability / Accomplishment
**Description**:
[What you do or did.]

**Evidence / Metrics**:
[Proof.]

**Tags**: `tag1`, `tag2`
**Context Relevance**: enterprise, b2b
**Role**: ROLE-2
**Clusters**: LEAD, STAK

---

<!--
TIPS FOR GOOD ENTRIES:
- Accomplishments > capabilities. "Grew revenue 3x" beats "Revenue growth experience"
- Be specific with numbers even if approximate: "~50%" is better than "significantly"
- One metric per entry. If you have three metrics, make three entries.
- Tags should match words a recruiter would use in a job ad, not your internal jargon
- If you're unsure of the cluster, leave it blank and fill in later
-->
