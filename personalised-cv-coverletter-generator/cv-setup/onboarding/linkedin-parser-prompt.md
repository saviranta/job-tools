# LinkedIn Profile Parser Prompt

Use this to convert your LinkedIn profile export into a first draft of your asset files.
Faster than the quickstart if you already have a detailed LinkedIn profile.

**How to export your LinkedIn data:**
1. Go to LinkedIn → Me → Settings & Privacy → Data Privacy → Get a copy of your data
2. Select "Want something in particular?" → check Profile, Positions, Skills, Recommendations
3. Download and open `Profile.csv` and `Positions.csv`
4. Copy the relevant text (or paste your LinkedIn profile page text directly)

**How to use this prompt:**
1. Copy everything below the line
2. Paste into Claude, followed by your LinkedIn content
3. Claude will generate your asset files
4. Save to `assets/` and refine using the maintenance prompts

---

You are converting a LinkedIn profile into a structured career asset library for job applications.

The library consists of five files:
1. **work_experience.md** — career history with unique role IDs
2. **capabilities.md** — searchable capability and accomplishment database
3. **competency_clusters.md** — skill groupings with job-ad trigger keywords
4. **qualities_workstyle.md** — working style and personal attributes
5. **profiles.md** — positioning statements

Here is my LinkedIn profile content:

[PASTE YOUR LINKEDIN PROFILE TEXT HERE]

---

From this content, generate all five asset files following these rules:

**work_experience.md**
- Create one role ID per distinct role (uppercase short label: COMPANY-ROLE)
- Group multiple roles at the same company under an umbrella ID where relevant
- Extract scope signals: team size, revenue, geographic reach, company stage
- Add a Quick Reference table at the bottom mapping contexts to role IDs

**capabilities.md**
- Extract every meaningful capability and accomplishment from the profile
- For each: write a title, description, evidence/metrics (use numbers from the profile), tags, role reference, and cluster reference
- Tags should match the language recruiters use in job ads — not internal jargon
- Mark entries as `Capability` or `Accomplishment`

**competency_clusters.md**
- Infer 6-10 clusters from the skills and experience described
- Write trigger keywords that would appear in job ads targeting these strengths
- Write 3 content structure bullet patterns per cluster

**qualities_workstyle.md**
- Extract personal attributes, leadership style, and working approach from the About section and recommendation language
- If recommendations are included, mine them for specific behavioural evidence
- Fill gaps with questions: note [FILL IN: ask user about X] where LinkedIn doesn't provide enough

**profiles.md**
- Write 2-3 positioning statements based on the career trajectory and apparent target direction
- Note what type of role and company each profile is best suited for

Where information is missing or thin, add a placeholder comment: `<!-- FILL IN: [what's needed] -->`

Use the template format from the `assets/` folder exactly.
