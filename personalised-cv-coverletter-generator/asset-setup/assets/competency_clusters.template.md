# Competency Clusters

<!--
PURPOSE: Modular skill sections for CV templates. Instead of listing every skill,
clusters group related capabilities into named sections that can be mixed and matched
based on what a job ad emphasises.

HOW DOWNSTREAM TOOLS USE THIS FILE:
- cv-template-generator selects 4-6 clusters based on job ad keywords
- cv-generator pulls evidence from capabilities.md using cluster IDs
- Trigger keywords are matched against job ad text to score relevance

HOW TO BUILD YOUR CLUSTERS:
Start with the suggested clusters below. Add, rename, or remove based on
what your career actually contains. Each cluster should map to a real
strength you can back with evidence from capabilities.md
-->

## Cluster Selection Logic

1. Analyze job ad → extract keywords
2. Match keywords against trigger words in each cluster
3. Score clusters → select top 4-6 by relevance
4. Pull evidence from capabilities.md using cluster IDs
5. Rank by score — highest-relevance clusters appear first on CV

---

## Cluster Index

<!--
Suggested starter clusters. Rename or replace to fit your career.
Primary Templates column: which CV contexts this cluster suits best
(A=IC/Senior, B=Director/Lead, C=Public/Healthcare, D=Enterprise, E=VP/C-level)
-->

| ID | Name | Best for | Trigger Keywords |
|----|------|----------|-----------------|
| `EXEC` | Execution & Delivery | All | ship, build, launch, deliver, implement, release |
| `DISC` | Discovery & Research | IC, Senior | user research, discovery, interview, insight, customer |
| `TECH` | Technical Fluency | IC, Senior | SQL, API, data, technical, integration, engineering |
| `METR` | Metrics & Impact | All | KPI, OKR, metric, analytics, impact, growth, revenue |
| `LEAD` | Team Leadership | Director+ | team, lead, hire, manage, people, coach, develop |
| `STRA` | Strategy | Director+ | strategy, vision, roadmap, portfolio, planning |
| `STAK` | Stakeholder Management | Director+ | stakeholder, executive, alignment, influence, partner |
| `DOMA` | Domain Expertise | All | [add your industry-specific terms] |

<!--
Add your own clusters below. Copy the format from the definitions section.
-->

---

## Cluster Definitions

### EXEC — Execution & Delivery

**Trigger keywords**:
```
ship, shipped, build, built, launch, launched, deliver, delivered,
implement, implemented, release, deploy, feature, MVP, production,
go-live, iteration, sprint, agile, backlog, velocity
```

**Content structure**:
```
• [0→1 capability: Built X from concept to production]
• [Delivery pace: Shipped X in Y timeframe]
• [End-to-end ownership: Discovery → Spec → Launch → Iteration]
```

**Evidence tags** (from capabilities.md): `execution`, `delivery`, `shipping`, `launch`

---

### METR — Metrics & Impact

**Trigger keywords**:
```
KPI, OKR, metric, metrics, analytics, data-driven, impact, growth,
revenue, ARR, MRR, retention, churn, conversion, ROI, outcome
```

**Content structure**:
```
• [Revenue or growth metric: Grew X by Y%]
• [Efficiency metric: Reduced X by Y]
• [Scale metric: Reached X users / markets / partners]
```

**Evidence tags** (from capabilities.md): `metrics`, `growth`, `revenue`, `impact`

---

### LEAD — Team Leadership

**Trigger keywords**:
```
team, lead, manage, hire, recruit, coach, develop, people, direct reports,
org, headcount, performance, culture, mentor, onboard
```

**Content structure**:
```
• [Team size and scope: Led team of N across X functions]
• [Development: Hired / grew / coached team members]
• [Culture or process: Established X practice or ritual]
```

**Evidence tags** (from capabilities.md): `leadership`, `team`, `hiring`, `coaching`

---

<!--
Add your remaining cluster definitions here, following the same format.
Each definition should have:
- Trigger keywords (what job ad language activates this cluster)
- Content structure (3 bullet point patterns for this cluster)
- Evidence tags (what to search for in capabilities.md)
-->
