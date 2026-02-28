# Quickstart Discovery Prompt

Paste this into Claude to generate a first draft of all your asset files in one conversation.
The output will be rough — that's intentional. Getting something down quickly is more valuable
than getting it perfect. You'll refine it over time using the maintenance prompts.

**How to use:**
1. Copy everything below the line
2. Paste into Claude (Claude.ai, API, or Claude Code)
3. Answer Claude's questions — as much or as little as you have time for
4. Ask Claude to generate the asset files when you're done
5. Save the output to your `assets/` folder

---

You are helping me build a personal career asset library for job applications.
The library consists of five structured files:

1. **work_experience.md** — my career history with unique role IDs
2. **capabilities.md** — a searchable database of what I can do and what I've achieved (tagged, cross-referenced)
3. **competency_clusters.md** — grouped skill areas with trigger keywords for job ad matching
4. **qualities_workstyle.md** — my working style, leadership approach, and personal attributes
5. **profiles.md** — positioning statements for different target contexts

Your task is to gather the information needed to populate these files by asking me questions.
Work through the areas below one at a time. Ask follow-up questions when you need more
specificity — especially on evidence, metrics, and outcomes.

When we're done, generate all five files in the correct format using the templates I'll share.

---

## AREA 1: Career History

Start here. For each role I describe:
- Ask for the company, title, dates, and team/budget/revenue scope
- Ask what changed because I was there — what was different when I left vs. when I joined
- Ask for the 2-3 things I'm most proud of from that role
- Assign a role ID (short uppercase label, e.g. ACME-PM, STARTUP-LEAD)

Begin by asking me to walk you through my career, starting from the most recent role.

---

## AREA 2: Capabilities and Accomplishments

For each role we discuss, ask:
- What specific skills did I use or develop?
- What are my 2-3 strongest proof points (with numbers if possible)?
- What problems was I uniquely good at solving?
- What would colleagues say I'm known for?

For each capability or accomplishment:
- Assign relevant tags (lowercase keywords a recruiter might search for)
- Link to the role ID from Area 1
- Note which competency cluster it belongs to (or leave blank if unclear)

---

## AREA 3: Competency Clusters

Based on what we've covered in Areas 1 and 2, propose 6-10 competency clusters that
reflect my actual strengths. For each cluster:
- Give it a short ID and name
- Write 3-5 trigger keywords (what a job ad would say to activate this cluster)
- Write a brief content structure (3 bullet point patterns)

Ask me to confirm, adjust, or add clusters before finalising.

---

## AREA 4: Working Style and Personal Attributes

Ask me about:
- How I communicate (with executives, with teams, in writing)
- How I approach problems I haven't seen before
- What colleagues would say makes me different
- How I lead or influence — with or without formal authority
- What kind of environment brings out my best work
- What I find genuinely energising and what drains me

---

## AREA 5: Positioning and Target Context

Ask me about:
- What types of roles am I targeting right now?
- What company stages or sizes appeal to me?
- What's my strongest claim for each target context?
- What makes me a non-obvious but compelling candidate?

Use this to draft 2-3 profile statements, one per distinct target context.

---

## Generating the Files

When we've covered enough ground (or I say "generate"), produce all five asset files
using the templates from `assets/`. Follow the structure exactly — role IDs, cluster IDs,
tags, and cross-references must be consistent across files.

**Note on capabilities.md:** This file has two sections that both need populating:
- `## INDEX` — one table row per entry (ID, title, clusters, evidence level, preview)
- `## ENTRIES` — full content for each entry (description, evidence/metrics, tags)

Generate both sections. Every CAP-ID in INDEX must have a matching entry in ENTRIES.
Tools read INDEX first for selection, then load specific ENTRIES by CAP-ID — both
sections must be present for the cv-generator and cover-letter-generator to work.

Tell me: "Here are your asset files. Save each one to your assets/ folder and review them.
Use the maintenance prompts to fill gaps and keep them updated."
