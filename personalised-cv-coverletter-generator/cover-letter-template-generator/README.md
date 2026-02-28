# cover-letter-template-generator

Builds and maintains a personal cover letter system — your writing style, a phrase library,
reusable templates, and a selector that picks the right structure for each application.

---

## Components

### Onboarding (do this once)

**`onboarding/coverletter-pdf-parser-prompt.md`**
Drop old cover letters into `archive/pre-gen/` and Claude reads them to bootstrap:
- Your writing style profile (`writing-style.md`)
- A starter phrase library (`phrase-library.md`)
- A suggested first template

**`onboarding/writing-style-wizard.md`**
A guided conversation to capture your voice — tone, rhythm, vocabulary preferences,
what you want to avoid. Output saved as `writing-style.md` alongside your assets.
Run this even if you don't have old cover letters.

### Phrase library

**`phrase-library/phrase-library.template.md`**
A growing collection of phrases you like, organised by section and tone.
The cover-letter-generator draws from this to keep language fresh and on-voice.
Add phrases over time as you write applications you're happy with.

### Template generation and selection

**`template-generator-prompt.md`**
Answers nine context questions → generates a `cover-letter-template.md` with a metadata
header for the library.

**`template-selector-prompt.md`**
Given a job-brief, checks your template library and recommends the best match
or tells you to generate new (with pre-filled answers).

---

## Recommended workflow

```
Once (onboarding):
1. coverletter-pdf-parser-prompt.md   → writing-style.md + phrase-library.md starter
2. writing-style-wizard.md            → refine writing-style.md

Per application:
3. job-listing-analyzer               → job-brief.md
   brand-inspector                    → brand-brief.md   (parallel)
   company-analyzer                   → company-brief.md (parallel)

4. template-selector-prompt.md
   → existing template OR generate new via template-generator-prompt.md

5. cover-letter-generator
   ← assets/ + job-brief + brand-brief + company-brief
   ← cover-letter-template + writing-style + phrase-library
   → your cover letter
```

---

## File locations (personal, outside this repo)

```
your-cv-setup/
├── assets/
├── templates/
│   ├── cover-letter/
│   │   ├── TMPL-CL-BOLD-MOTIVATION.md
│   │   └── TMPL-CL-NARRATIVE-FIT.md
│   └── cv/
├── writing-style.md              ← your voice profile
├── phrase-library.md             ← reusable phrases by section
├── archive/
│   └── pre-gen/
│       ├── coverletter-2022.pdf
│       └── coverletter-2024-pm.pdf
└── applications/
    └── company-role-2025/
        ├── job-brief.md
        ├── brand-brief.md
        ├── company-brief.md
        └── cover-letter-template.md
```

---

## Length styles

| Style | Words | When to use |
|---|---|---|
| Short & bold | 100–150 | Direct referral, exec roles, creative fields that value confidence |
| Structured | ~200 | ATS-heavy pipelines, roles where scanability matters, technical roles |
| Engaging narrative | 300–400 | Writing-heavy roles, culture-first companies, when story is the point |
