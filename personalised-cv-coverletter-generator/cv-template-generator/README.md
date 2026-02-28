# cv-template-generator

Generates a tailored CV structure before content is added.

The template captures decisions about layout, section order, emphasis, and styling
so that the cv-generator has a clear brief to work from — not a blank canvas.

---

## Why a template generator, not a fixed template

The right CV structure depends on context:

| Factor | Impact on structure |
|---|---|
| ATS screening expected | Single column, standard section names, no tables or graphics |
| Human-eye first | Can use two columns, styled header, more visual hierarchy |
| IC role | Technical depth, project evidence, skills prominent |
| People manager | Leadership scope, team size, strategic decisions front and centre |
| Startup | Concise, high-impact, personality welcome |
| Enterprise | Formal, structured, titles and tenure legible at a glance |
| 1 page | Ruthlessly prioritised, no education block unless recent |
| 2 pages | Narrative arc across career, evidence can breathe |

A generated template locks in these choices so you're not making structural decisions
mid-draft.

---

## Inputs

**Required:**
- Answers to the context questions (in the prompt)

**Optional but recommended:**
- `brand-brief.md` from the brand-inspector → informs visual styling
- `job-brief.md` from the job-listing-analyzer → informs section emphasis and ordering

---

## Output

A `cv-template.md` file containing:
- Page setup (margins, columns, density)
- Header specification (what to include, layout)
- Section list in order, with section names to use
- Per-section brief (format, length, emphasis, what to draw from assets)
- Visual parameters (fonts, colors, accent usage — if brand-brief provided)

---

## How it connects

```
job-brief.md  ──┐
brand-brief.md ─┤→ cv-template-generator → cv-template.md
context Q&A  ───┘                                ↓
                                          cv-generator
                                    (populates the template
                                     from your asset files)
```
