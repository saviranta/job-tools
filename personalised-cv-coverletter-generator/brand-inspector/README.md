# brand-inspector

Analyze a company's visual brand and communication style before generating your CV and cover letter.

The output — a `brand-brief.md` — feeds into:
- `cv-template-generator/` → informs color palette, typography, layout density
- `cover-letter-generator/` → informs tone register, language style, structural choices

The goal is not to copy their brand. It's to complement it — so your application
doesn't visually or tonally jar against what they're used to seeing.

---

## What the brand inspector covers

**Visual brand**
- Color palette (primary, secondary, accent)
- Typography style (serif / sans-serif, weight, density)
- Layout personality (spacious / dense, minimal / expressive)
- Overall design register (corporate / startup / creative / technical)

**Communication style**
- Written tone (formal ↔ casual, earnest ↔ direct, technical ↔ accessible)
- Language patterns (what words and phrases they repeat)
- How they write about their team, product, and customers

**Styling recommendations**
- What CV layout style fits this company context
- Color and font suggestions for your CV header and accents
- Cover letter tone guidance, distinct from the job-brief

---

## How it connects to other tools

```
brand-inspector → brand-brief.md
                        ↓
         cv-template-generator   ←  uses brand-brief for visual choices
         cover-letter-generator  ←  uses brand-brief for tone calibration

Note: company-analyzer also produces tone signals (company-brief.md).
brand-brief.md goes deeper on visual design and is the authoritative
source for styling decisions.
```

---

## Recommended workflow

Run the brand inspector at the same time as the company analyzer.
Both can run in parallel — they look at the same site but focus on different things.

Save the output to your application folder:

```
applications/
└── company-role-2025/
    ├── job-brief.md
    ├── company-brief.md
    └── brand-brief.md      ← this tool's output
```
