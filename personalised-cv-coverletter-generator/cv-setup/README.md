# cv-setup

The starting point for personalised CV and cover letter generation.

This tool helps you build and maintain a **career asset library** — five structured files
that capture everything you've done, how you work, and how you want to be positioned.
The downstream tools (job analyzer, cv-generator, cover-letter-generator) pull from these files.

---

## What's in here

```
cv-setup/
├── assets/               ← template files for your career asset library
│   ├── work_experience.template.md
│   ├── capabilities.template.md
│   ├── competency_clusters.template.md
│   ├── qualities_workstyle.template.md
│   └── profiles.template.md
│
├── onboarding/           ← how to get started fast
│   ├── quickstart-prompt.md       ← guided conversation to build your files from scratch
│   ├── linkedin-parser-prompt.md  ← convert a LinkedIn export to asset files
│   ├── cv-pdf-parser-prompt.md    ← convert an existing CV/PDF to asset files
│   └── assets-explained.md       ← what each file does and why
│
└── maintenance/          ← how to keep your assets current over time
    ├── quick-add-prompt.md   ← capture a raw thought before it's gone
    ├── update-guide.md       ← when and what to update
    └── review-prompt.md      ← periodic audit of your full asset library
```

---

## Getting started

### Option 1: Build from scratch (quickstart)
Use `onboarding/quickstart-prompt.md` — paste it into Claude and answer questions.
Takes 30–60 minutes for a first pass. Output will be rough; that's intentional.

### Option 2: Start from LinkedIn
Export your LinkedIn data and use `onboarding/linkedin-parser-prompt.md`.
Faster if you already have a detailed profile.

### Option 3: Start from an existing CV
Copy your CV text and use `onboarding/cv-pdf-parser-prompt.md`.
Works best with a detailed CV.

### After onboarding
Save the generated files to an `assets/` folder (not in this repo — your personal data stays local).
Then use the maintenance prompts to fill gaps and keep things current.

---

## The asset files

Read `onboarding/assets-explained.md` for a full description of how the files connect.

In short:
- `work_experience.md` — role IDs that anchor everything else
- `capabilities.md` — the core database: tagged evidence linked to roles and clusters
- `competency_clusters.md` — the matching layer: keywords map job ads to your strengths
- `qualities_workstyle.md` — your voice: used in cover letters
- `profiles.md` — positioning statements for different target contexts

---

## Keeping assets current

**Sporadic updates** (you just thought of something):
→ Use `maintenance/quick-add-prompt.md`

**Periodic review** (quarterly or before a job search):
→ Use `maintenance/review-prompt.md`

**General guidance** (what to update and when):
→ Read `maintenance/update-guide.md`

---

## What comes next

Once your asset files are populated, the other tools in `personalised-cv-coverletter-generator/` use them to generate tailored applications:

- `job-listing-analyzer/` — reads a job ad and identifies which of your assets are most relevant
- `cv-template-generator/` — generates a CV structure by asking about context (ATS vs human, seniority, etc.)
- `cv-generator/` — combines your assets + job analysis + template into a tailored CV
- `cover-letter-generator/` — combines your assets + working style + job analysis into a cover letter
