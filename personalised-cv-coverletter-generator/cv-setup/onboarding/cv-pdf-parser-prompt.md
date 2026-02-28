# CV / PDF Parser

Convert an existing CV into a first draft of your asset files.
Pick the option that matches your setup.

---

## Option A: Paste text into Claude

**Best for:** A single CV you have open right now.

**How to extract text from a PDF:**
- Mac: open in Preview → Edit → Select All → Copy
- Any browser: open PDF → Cmd+A → Cmd+C
- Or use a tool like pdftotext, Adobe Acrobat, or an online PDF-to-text converter

**How to use:**
1. Extract the text from your CV
2. Copy the parsing prompt at the bottom of this file
3. Paste it into Claude followed by your CV text
4. Claude will generate your asset files

---

## Option B: Archive folder + Claude Code (batch, auto-updating)

**Best for:** You have multiple old CVs, or you want Claude Code to read and populate your assets automatically — including as you add new CV versions over time.

**How it works:**
- Save your CVs (any version, any role) as PDFs into a local `archive/pre-gen/` folder
- Claude Code reads them using its built-in PDF reading capability
- Claude parses all of them and populates or updates your five asset files
- Run it again any time you add a new CV version — it merges rather than overwrites

**Setup:**

1. Create the folder structure next to your `assets/` folder:

   ```
   your-cv-setup/
   ├── assets/
   │   ├── work_experience.md
   │   ├── capabilities.md
   │   └── ...
   └── archive/
       └── pre-gen/
           ├── cv-2019.pdf
           ├── cv-2022-pm.pdf
           └── cv-2025-latest.pdf
   ```

2. In Claude Code, run this prompt:

```
I'm building a career asset library from my existing CVs.

My archive folder is at: [path to archive/pre-gen/]
My assets folder is at: [path to assets/]

Please:
1. Read all PDF files in the archive/pre-gen/ folder
2. Extract all experience, skills, accomplishments, and profile content
3. If the asset files already exist, merge new content in — don't overwrite entries that are already there
4. If the asset files don't exist yet, generate them from scratch using the template format

[PASTE THE PARSING RULES FROM THE BOTTOM OF THIS FILE]
```

3. Claude Code will read each PDF (it handles PDFs natively), reconcile content across versions, and output updated asset files.

**Tip:** The oldest CV often has roles that didn't make it into your latest one. Including all versions means nothing gets lost.

---

## The Parsing Rules

Use these with either option. They tell Claude how to structure the output.

---

You are converting an existing CV into a structured career asset library for job applications.

The library consists of five files:
1. **work_experience.md** — career history with unique role IDs
2. **capabilities.md** — searchable capability and accomplishment database
3. **competency_clusters.md** — skill groupings with job-ad trigger keywords
4. **qualities_workstyle.md** — working style and personal attributes
5. **profiles.md** — positioning statements

Here is my CV:

[PASTE YOUR CV TEXT HERE — or omit this line if using Option B with Claude Code]

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
