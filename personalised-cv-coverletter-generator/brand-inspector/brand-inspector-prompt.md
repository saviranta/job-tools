# Brand Inspector Prompt

Analyze a company's brand to inform the visual design and tone of your CV and cover letter.

---

## Option A: Claude Code + Chrome MCP (recommended)

**Best for:** Claude Code users with the Chrome MCP extension.
Claude navigates the company site, captures visual and tonal signals across multiple pages,
and synthesises them into styling recommendations.

Ask Claude Code:

```
Analyze the brand of [Company Name] to help me style my job application.
Their website is: [company URL]

Please navigate and read the following pages in sequence:
1. Homepage — visual hierarchy, hero copy, color use, imagery style
2. About or Our Story — typography, layout density, brand voice
3. Careers page — how they present themselves to candidates visually and in copy
4. Blog or Content — writing style, paragraph length, tone
5. Press kit or Brand page (check footer for links) — if available, read it;
   this may have official color codes, font names, and brand guidelines
6. Their LinkedIn company page — profile banner, post tone and style

Then use the analysis prompt below to produce the brand brief.
```

**Tip:** If the company has a design system page (e.g. design.company.com, brand.company.com)
or a Figma community file, link it in the prompt — it's the most reliable source of
official colors and typefaces.

---

## Option B: Claude Code + Playwright Scraper (automated)

**Best for:** Claude Code users with the [`playwright-web-scraper`](https://github.com/saviranta/claude-code-tools/tree/main/playwright-web-scraper) tool set up.

**Scraping scope setup:**

Create a `scraping-scope.md` for the company's brand:

```markdown
## What to scrape
[Company Name]'s public website at [company URL]

## What content matters
- Homepage: headline text, visual layout description (if you can infer it from structure),
  hero section copy, navigation labels
- About or Our Story page: full text, mission statements, values copy
- Careers or Jobs page: how they describe working there, team language, any visual
  treatment clues from CSS class names or image alt text
- Blog: 2-3 recent post titles and opening paragraphs — for tone analysis
- Footer: look for links to press kit, brand guidelines, or design system

## What to skip
Product pricing, login-gated content, support docs.

## How much depth
Full text on About and Careers. Headlines and first paragraphs for blog posts.
```

**Note:** For visual analysis, Chrome MCP is more reliable — it sees the rendered page.
The playwright scraper captures text and structure but not actual colors or rendered fonts.
Consider pairing: scraper for text/tone analysis, Chrome MCP screenshot for visual analysis.

---

## The Analysis Prompt

Paste this after browsing or scraping. For Chrome MCP, also ask Claude to take a screenshot
of the homepage before running this — visual inspection is part of the analysis.

---

You are analyzing a company's brand to help me style a job application (CV and cover letter).

Here is the company's website content and any visual observations:

[CONTENT / OBSERVATIONS HERE — or omit if Claude already has it from Chrome MCP browsing]

---

Produce a structured brand brief with the following sections:

**1. Visual brand**

*Color palette*
- Primary color: [name + hex if available, otherwise descriptive: "deep navy blue"]
- Secondary color: [name + hex or description]
- Accent / highlight color: [name + hex or description]
- Background treatment: white / off-white / dark / gradient?
- Overall palette mood: conservative / bold / fresh / minimal / warm / technical

*Typography*
- Heading style: serif / sans-serif / geometric / humanist / slab
- Body text: weight and density (light and airy / regular / dense and compact)
- Font names if identifiable (from press kit, CSS, or Google Fonts references)
- Typography mood: authoritative / approachable / modern / classic / technical

*Layout and density*
- Whitespace use: generous / moderate / dense
- Visual structure: grid-based / fluid / editorial / minimal
- Information density: sparse (big statements, lots of space) / rich (lots of detail visible)
- Overall layout personality: one of: Corporate formal / Tech minimal / Startup bold /
  Creative expressive / Academic structured / Consumer friendly

**2. Design personality**
In one sentence: what design archetype is this company?
(e.g. "Clean, confident SaaS — white space heavy, geometric sans-serif, one strong accent color")

**3. Communication style**
- Written tone: [select from: formal / professional / conversational / casual]
- Sentence structure: long and detailed / short and punchy / mixed
- Vocabulary register: technical / business / accessible / creative
- How they write about people: "our team", "our people", "Xers", name-first, etc.
- Signature phrases: 2-3 phrases they repeat that reveal their brand voice

**4. CV styling recommendations**

Based on the above, recommend:

*Layout*
- Suggested layout style: [e.g. "Single column with generous margins", "Two-column with left sidebar"]
- Header treatment: [e.g. "Clean name + title, no decorative elements"]
- Section dividers: lines / color blocks / whitespace only / bold section labels

*Colors*
- Header background: [suggested color from their palette, or neutral]
- Accent color (links, role titles, section headings): [specific suggestion]
- Body text: #333 (default) or adjusted?
- What to avoid: any colors that would clash or feel off-brand

*Typography*
- Heading font suggestion: [specific Google Font or category]
- Body font suggestion: [specific Google Font or category]
- Weight and size approach: [e.g. "Bold headings, light body, generous line spacing"]

*Overall impression to aim for*
One sentence describing the feeling your CV should give off in this company's context.

**5. Cover letter tone guidance**

- Register: [formal / warm-professional / direct / narrative]
- Paragraph style: [long-form flowing / short punchy paragraphs / mixed]
- Opening line approach: [bold claim / context-setting / direct statement of interest]
- Language to use: [examples of vocabulary that fits their voice]
- Language to avoid: [jargon or styles that would feel off]
- One sentence: "Write the cover letter as if you are..."

**6. Brand references to surface**
If you found any of the following, note them for use in the cv-template-generator:
- Official font names
- Official hex color codes (from press kit, CSS variables, or brand guidelines)
- Design system URL
- Brand guidelines PDF link

**Source integrity rule:**
If any page was unavailable, gated, or only partially loaded during browsing,
mark the affected section with `[INFERRED — verify]` rather than filling it from
assumptions. For colors and fonts specifically: only report hex values or font names
you can directly observe (from CSS, press kit, or brand guidelines). If you cannot
confirm them, give a descriptive approximation and mark it `[ESTIMATED]`.

Output this as a structured markdown document I can save as `brand-brief.md`.
