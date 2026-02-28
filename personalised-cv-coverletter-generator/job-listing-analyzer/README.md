# job-listing-analyzer

Analyze a job listing and the hiring company before generating your CV or cover letter.

Running both tools gives you a **job brief** and a **company brief** — structured outputs
that the cv-generator and cover-letter-generator use to make your application as targeted
as possible.

---

## The two tools

### 1. Job Listing Analyzer (`job-listing-prompt.md`)

Reads a job ad and matches it against your career asset library. Output:
- Which of your competency clusters the job activates (ranked)
- Which capabilities and accomplishments to feature
- Which roles to include and how to frame them
- Which profile to use as the base
- Exact keywords to mirror from the job ad
- Your strongest positioning angle for this specific role
- Gaps to acknowledge or reframe

Two options: paste the listing, or let Claude read it directly from the URL.

### 2. Company Analyzer (`company-analyzer-prompt.md`)

Reads the company's website and surfaces what you need to personalise your application.
Output:
- Company snapshot (stage, product, market)
- Culture and values language to mirror
- Recent priorities and initiatives to reference
- Tone calibration for the cover letter
- Specific connection points that show genuine research

Two options: Claude navigates the company site via Chrome MCP, or automated scraping
via the `playwright-web-scraper` tool.

---

## Recommended workflow

```
1. job-listing-prompt.md     → job-brief.md     (save this)
2. company-analyzer-prompt.md → company-brief.md (save this)
3. cv-generator              ← feeds on assets + job-brief + company-brief
4. cover-letter-generator    ← feeds on assets + job-brief + company-brief
```

Run the job listing analyzer first. Run the company analyzer in parallel or after.
Both outputs are inputs to the generation step.

---

## Where to save the outputs

Save your briefs alongside your assets, outside this repo:

```
your-asset-setup/
├── assets/
├── archive/
└── applications/
    └── company-role-2025/
        ├── job-brief.md
        └── company-brief.md
```

One folder per application keeps everything in context for generation.
