# Understanding Your Asset Files

A quick guide to what each file does, why it's structured the way it is,
and how the downstream tools use them.

---

## The five files and how they connect

```
work_experience.md          ← the spine: role IDs anchor everything else
       ↓
capabilities.md             ← the database: tagged evidence linked to roles and clusters
       ↓
competency_clusters.md      ← the matching layer: keywords map job ads to your strengths
       ↓
qualities_workstyle.md      ← the voice: your authentic style, used in cover letters
       ↓
profiles.md                 ← the positioning: pre-written summaries per target context
```

---

## work_experience.md

**What it is:** Your career history, structured with unique role IDs.

**Why role IDs matter:** Every entry in `capabilities.md` references a role ID. This lets the cv-generator filter your experience to the most relevant roles for a given job — you don't have to decide upfront. The ID system also handles companies where you had multiple titles (you can group them under one umbrella ID or keep them separate).

**What makes a good entry:** Focus on scope and impact, not job description. What was the scale? What changed? What did you own end-to-end?

---

## capabilities.md

**What it is:** A searchable database of everything you can do and have achieved.

**Why it's a database, not a list:** When the cv-generator analyzes a job ad, it searches your capabilities by tags and cluster IDs to find the most relevant evidence. A structured format makes this matching reliable. A prose list doesn't.

**Capability vs. Accomplishment:**
- **Capability** = something you can do: "I design API contracts with engineering teams"
- **Accomplishment** = proof you did it: "Reduced integration time from 6 weeks to 2 weeks for enterprise customers"

Both belong here. Accomplishments are more powerful — aim for 2-3x more accomplishments than capabilities.

**Tags:** Write tags as a recruiter would write a job ad, not as you'd describe your own work. If you say "drove product strategy" internally, the job ad says "product vision", "roadmap ownership", "strategic direction". Use their words.

---

## competency_clusters.md

**What it is:** Named groupings of related skills, each with trigger keywords.

**Why clusters instead of a skills list:** A flat skills list can't be prioritised. Clusters can. When a job ad emphasises stakeholder management, the `STAK` cluster rises to the top. When it emphasises technical depth, `TECH` does. The cv-generator selects 4-6 clusters per application based on keyword matching.

**Trigger keywords:** These are the exact words that activate a cluster. If the job ad says "OKR", "impact", "revenue growth" — those match `METR`. The more specific your trigger keywords, the better the matching.

---

## qualities_workstyle.md

**What it is:** Your authentic voice — working style, leadership philosophy, personal attributes.

**Why it's separate:** Capabilities are what you've done. Workstyle is how you do it. Cover letters and profile sections need both. Keeping workstyle separate means it's easy to draw on without rewriting from scratch each time.

**What makes a good entry:** Specificity. "I communicate directly and adjust depth by audience" is useful. "Good communicator" is not. Concrete examples embedded in the text make it more credible and easier to use.

---

## profiles.md

**What it is:** Pre-written positioning statements for distinct target contexts.

**Why maintain multiple profiles:** Your strongest claim changes depending on whether you're applying to a scale-up, an enterprise, or a niche domain role. Maintaining 2-4 profiles means you're never writing from scratch — you're selecting and adapting.

**When to add a new profile:** When you're targeting a meaningfully different type of role or company. Not when you're applying to a similar role at a different company — that's what the cv-generator handles.

---

## The overall flow

```
cv-setup (you are here)
    → populate assets/

job-listing-analyzer
    → reads the job ad and company
    → identifies which clusters, roles, and profile match best

cv-template-generator
    → asks questions about ATS vs human, seniority, company type
    → generates a tailored CV structure

cv-generator
    → combines assets + job analysis + template
    → produces your CV

cover-letter-generator
    → combines assets + qualities_workstyle + job analysis
    → produces your cover letter
```
