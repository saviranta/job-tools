# SETUP — First-time Setup

Run this once to create your personal workspace and get your asset library started.

Paste this into Claude Code. It will create your folder structure, copy the template
files you need, and walk you through the first steps.

---

## Before you start

This system has two parts:
- **This repo** — the tools (prompts, templates, workflows). Read-only for you; update by pulling.
- **Your personal workspace** — your data (assets, templates, outputs, applications). Lives
  on your machine, outside this repo, never committed anywhere.

**What you'll need:**
- Claude Code with file system access
- ~30–60 minutes for the initial asset setup (quickstart interview)
- Your most recent CV or LinkedIn profile (optional but speeds things up)

---

## The Prompt

Paste into Claude Code:

---

You are setting up a personal CV and cover letter workspace.

Ask me one question first: **"Where would you like your personal workspace folder?
Give me the full path, or I'll create it at `~/cv-workspace` by default."**

Wait for my answer, then proceed.

---

### Step 1: Create folder structure

Create the following folder structure at the path I specified:

```
[workspace]/
├── assets/                    ← your five career asset files live here
├── archive/
│   └── pre-gen/               ← drop old CVs and cover letters here for parsing
├── templates/
│   ├── cv/                    ← saved CV templates (TMPL-*.md)
│   ├── cover-letter/          ← saved cover letter templates (TMPL-CL-*.md)
│   └── styles/                ← saved HTML style pairs (STYLE-*/cv-output.html + cl-output.html)
├── applications/              ← one subfolder per job application
└── outputs/                   ← final HTML files (YYYYMMDD_[surname]_[company]_cv.html etc.)
```

After creating, confirm each folder was created and show the full tree.

---

### Step 2: Copy asset templates

Copy the five template files from this repo's `asset-setup/assets/` folder
into the workspace `assets/` folder, removing the `.template` suffix:

```
asset-setup/assets/work_experience.template.md      → [workspace]/assets/work_experience.md
asset-setup/assets/capabilities.template.md         → [workspace]/assets/capabilities.md
asset-setup/assets/competency_clusters.template.md  → [workspace]/assets/competency_clusters.md
asset-setup/assets/qualities_workstyle.template.md  → [workspace]/assets/qualities_workstyle.md
asset-setup/assets/profiles.template.md             → [workspace]/assets/profiles.md
```

Confirm each file was copied.

---

### Step 3: Copy phrase library template

```
cover-letter-template-generator/phrase-library/phrase-library.template.md
  → [workspace]/phrase-library.md
```

---

### Step 4: Explain the workspace

Display this summary:

```
═══════════════════════════════════════════════
YOUR WORKSPACE IS READY
[workspace path]
═══════════════════════════════════════════════

assets/                 ← fill these in — they're the foundation of everything
  work_experience.md    ← your career history with role IDs
  capabilities.md       ← what you've done and achieved (tagged, searchable)
  competency_clusters.md← skill groupings for job-ad matching
  qualities_workstyle.md← how you work and lead
  profiles.md           ← positioning statements per target context

archive/pre-gen/        ← drop old CVs and cover letters here (PDF or Word)
                           the parsers in asset-setup/onboarding/ will read them

templates/              ← CV and cover letter templates build up here over time
                           the first one gets generated during your first application

outputs/                ← final HTML files land here, ready to print to PDF

applications/           ← one folder per job (company-role-date)
                           briefs, working files, and templates per application

phrase-library.md       ← phrases that work for you, organised by CL section
                           starts empty — builds as you write cover letters
═══════════════════════════════════════════════
```

---

### Step 5: Guide to asset setup

Tell me:

```
Next step: fill in your asset files.

Open asset-setup/QUICKSTART.md — it explains all the ways to get started
(existing CV, LinkedIn profile, or from scratch) and links to the right
prompt for each path. That file is your starting point.
```

---

### What comes after assets

Once your asset files are populated:

```
WHEN YOU HAVE A JOB TO APPLY FOR:
→ Run GENERATE-CV-CL.md (the main workflow)
  Takes a job URL + company URL → produces HTML CV and cover letter

WHEN YOU WANT TO IMPROVE YOUR ASSETS:
→ Run IMPROVER.md
  Targeted improvements — only touches what you ask about

EVERY FEW MONTHS:
→ Run asset-setup/maintenance/review-prompt.md
  Full audit of your assets with prioritised gaps
```
