# CV / PDF Parser Prompt

Use this to convert an existing CV into a first draft of your asset files.
Works best with a detailed CV — the more content you have, the richer the output.

**How to extract text from a PDF CV:**
- Mac: open in Preview → Edit → Select All → Copy
- Any browser: open PDF → Ctrl/Cmd+A → Ctrl/Cmd+C
- Or use a tool like pdftotext, Adobe Acrobat, or an online PDF-to-text converter

**How to use this prompt:**
1. Copy everything below the line
2. Paste into Claude, followed by your CV text
3. Claude will generate your asset files
4. Save to `assets/` and refine using the maintenance prompts

---

You are converting an existing CV into a structured career asset library for job applications.

The library consists of five files:
1. **work_experience.md** — career history with unique role IDs
2. **capabilities.md** — searchable capability and accomplishment database
3. **competency_clusters.md** — skill groupings with job-ad trigger keywords
4. **qualities_workstyle.md** — working style and personal attributes
5. **profiles.md** — positioning statements

Here is my CV:

[PASTE YOUR CV TEXT HERE]

---

From this content, generate all five asset files following these rules:

**work_experience.md**
- Create one role ID per distinct role (uppercase short label: COMPANY-ROLE)
- Group multiple roles at the same company under an umbrella ID where relevant
- Infer scope signals from CV language: team size, revenue, scale, geography
- Add a Quick Reference table mapping contexts (leadership, technical, etc.) to role IDs

**capabilities.md**
- Extract every bullet point, achievement, and skill from the CV as a separate entry
- Rewrite CV bullets into the asset format: Title / Description / Evidence+Metrics / Tags
- Where the CV uses vague language ("improved", "led", "drove"), flag it: `<!-- STRENGTHEN: add specific metric -->`
- Assign tags that match job ad language, not the CV's own phrasing
- Link each entry to its role ID and suggest a competency cluster

**competency_clusters.md**
- Infer 6-10 clusters from the skills section and role descriptions
- Write trigger keywords matching what job ads say when they want these skills
- Write 3 content structure bullet patterns per cluster

**qualities_workstyle.md**
- Extract tone and style signals from the CV's language and profile/summary section
- Where the CV is thin on personality, add: `<!-- FILL IN: ask user about X -->`

**profiles.md**
- If the CV has a profile or summary section, use it as the basis for PROF-1
- Write 1-2 additional profile variants for adjacent target contexts you can infer from the career trajectory
- Note the target role type and company type for each

Where content is missing, add `<!-- FILL IN: [what's needed] -->` rather than inventing.

Use the template format from the `assets/` folder exactly.
