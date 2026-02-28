# LinkedIn Profile Parser

Convert your LinkedIn profile into a first draft of your asset files.
Pick the option that matches your setup.

---

## Option A: Claude Code + Playwright Scraper (automated)

**Best for:** Claude Code users who have the [`playwright-web-scraper`](https://github.com/saviranta/claude-code-tools/tree/main/playwright-web-scraper) tool set up.

**What it does:** Playwright opens your browser profile (with your LinkedIn session),
scrapes your profile page, and feeds the content into the parsing prompt below.

**Setup:**

1. Make sure you have the `playwright-web-scraper` tool from `claude-code-tools`
2. In your `scraping-scope.md`, define:

```markdown
## What to scrape
My own LinkedIn profile page at linkedin.com/in/[your-username]

## What content matters
Everything: headline, about section, all work experience entries (title, company, dates,
description, bullets), skills, certifications, education, recommendations received.

## What to skip
Ads, suggested connections, job recommendations, notification banners.

## How much depth
All experience entries — no limits. Scroll to load all content.
```

3. Run the site structure analyzer first:
   ```bash
   python site-structure-analyzer.py
   ```
   Note: LinkedIn requires authentication. Set `use_persistent_profile=True` in the scraper
   and log in once via the browser; subsequent runs will reuse your session.

4. Run the scraper and save the output to a text file
5. Paste that text into the parsing prompt at the bottom of this file

---

## Option B: Claude Code + Chrome MCP (browser-assisted)

**Best for:** Claude Code users with the Chrome MCP extension configured.

**What it does:** Claude navigates your live browser session, reads your LinkedIn profile,
and populates the asset files — no export or copy-paste needed.

**How to use:**

Ask Claude Code:

```
I want to parse my LinkedIn profile into my career asset library.
My LinkedIn URL is: linkedin.com/in/[your-username]

Please:
1. Navigate to my profile (I'm already logged in)
2. Read all sections: headline, about, all experience entries, skills, education, recommendations
3. Scroll to make sure all experience entries are loaded
4. Use the parsing rules below to generate the five asset files

[PASTE THE PARSING PROMPT BELOW]
```

Claude will navigate your browser, extract the content, and return formatted asset files.

---

## Option C: Manual LinkedIn Export

**Best for:** Anyone. No tools required.

**How to export your LinkedIn data:**
1. Go to LinkedIn → Me → Settings & Privacy → Data Privacy → Get a copy of your data
2. Select "Want something in particular?" → check Profile, Positions, Skills, Recommendations
3. Download and open `Profile.csv` and `Positions.csv`
4. Copy the relevant content (or copy your LinkedIn profile page text directly from your browser)
5. Paste into the parsing prompt below

---

## The Parsing Prompt

Use this with any of the three options above. Paste it into Claude followed by your LinkedIn content.

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
- Fill gaps with questions: note `<!-- FILL IN: ask user about X -->` where LinkedIn doesn't provide enough

**profiles.md**
- Write 2-3 positioning statements based on the career trajectory and apparent target direction
- Note what type of role and company each profile is best suited for

Where information is missing or thin, add a placeholder comment: `<!-- FILL IN: [what's needed] -->`

Use the template format from the `assets/` folder exactly.
