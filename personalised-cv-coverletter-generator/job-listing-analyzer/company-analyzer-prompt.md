# Company Analyzer

Surface what you need to know about the company to personalise your application.
Covers culture signals, recent priorities, tone, and specific connection points.

Run this alongside (or after) the job listing analyzer. Save the output as `company-brief.md`.

---

## Option A: Claude Code + Chrome MCP (recommended)

**Best for:** Claude Code users with the Chrome MCP extension.
Claude navigates the company site live and synthesises across multiple pages.

Ask Claude Code:

```
Analyze [Company Name] to help me personalise my job application.
Their website is: [company URL]

Please visit and read the following pages (navigate to each in sequence):
1. Homepage — understand positioning and what they lead with
2. About / Our story — culture, mission, founding context
3. Team or Leadership page — how they describe their people
4. Blog or News — what they're writing about recently (read 2-3 recent posts)
5. Careers or Jobs page — how they describe their culture to candidates

Stop-early rule: if you have sufficient content for all 7 brief sections after
fewer pages, stop browsing — do not visit additional pages unnecessarily.

Then use the analysis prompt below to produce a company brief.

[PASTE THE ANALYSIS PROMPT FROM BELOW]
```

---

## Option B: Claude Code + Playwright Scraper (automated)

**Best for:** Claude Code users with the [`playwright-web-scraper`](https://github.com/saviranta/claude-code-tools/tree/main/playwright-web-scraper) tool set up.
Good for scraping companies with content-rich sites or for running multiple analyses.

**Scraping scope setup:**

Create a `scraping-scope.md` for the company with content like:

```markdown
## What to scrape
[Company Name]'s public website at [company URL]

## What content matters
- Homepage: main headline, positioning statement, product/service description
- About or Our Story page: mission, founding story, values, culture language
- Team or Leadership page: how they describe their people, leadership bios
- Blog or News: the 3 most recent posts — titles and full body text
- Careers or Jobs page: how they describe working there, culture claims

## What to skip
Pricing pages, technical docs, login-gated content, cookie banners.

## How much depth
Surface-level on most pages. Full text on About, Blog posts, and Careers.
```

Run the site structure analyzer, then the scraper. Feed the output into the analysis prompt below.

---

## The Analysis Prompt

Paste this after the scraped or browsed content.

<!-- BEGIN PROMPT -->

---

You are analyzing a company to help me personalise a job application.

Here is the company content you've gathered (website copy, about page, blog posts, careers page):

[CONTENT HERE — or omit if Claude already has it from Chrome MCP browsing]

---

Produce a structured company brief with the following sections:

**1. Company snapshot**
- What the company does (one clear sentence)
- Stage: early-stage / growth / scale-up / enterprise / public
- Approximate size (if findable)
- Market: who they sell to, competitive context
- Product model: SaaS / marketplace / services / hardware / etc.

**2. Mission and values language**
- What phrases do they repeat when describing their mission?
- What values language appears in About, Careers, or leadership bios?
- Quote specific phrases — I'll mirror these in the cover letter.

**3. Culture signals**
- How do they describe their team or way of working?
- Do they signal: fast-paced / deliberate / collaborative / autonomous / customer-obsessed?
- Any tension between stated values and implied culture (e.g., "work-life balance" alongside "high performance expectations")?
- Likely management style based on available signals

**4. Recent priorities and initiatives**
- What are they writing about, announcing, or building right now?
- Any recent launches, expansions, pivots, or strategic shifts?
- What problems are they visibly trying to solve?

**5. Tone calibration**
- Formal or informal?
- Technical depth or accessible language?
- Earnest / mission-driven, or pragmatic / commercial?
- What's the right register for a cover letter to this company?
- One sentence: "Write as if you are..."

**6. Connection points**
Specific, concrete things I can reference in my application that show genuine research:
- A specific product decision or initiative worth mentioning
- A value or mission claim I can connect to my own experience
- A recent challenge or ambition I can position myself against
- Something from leadership bios or team descriptions worth acknowledging

List 3-5 connection points, each with a suggested one-liner for how to use it.

**7. Red flags or context to be aware of**
- Anything in the public record that suggests instability, culture mismatch, or risk?
- Glassdoor signals, recent layoffs, leadership changes, funding pressure (if visible)?
- Note these for my awareness — not necessarily to address in the application.

**Source integrity rule:**
If any page was unavailable, gated, or only partially loaded during browsing,
mark the affected section with `[INFERRED — verify]` rather than filling it from
assumptions. Do not present inferred content as if it were read directly from the site.

**Personal data rule:**
Do not record any personal contact details, employee names beyond leadership bios,
or identification data in this file. company-brief.md is a company and culture analysis only.

**Language rule:**
All output must be in English. If the company content is in another language, translate
all extracted content to English before producing this document.

Output this as a structured markdown document I can save as `company-brief.md`.
