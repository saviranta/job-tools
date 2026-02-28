# Cover Letter PDF Parser

Parse your existing cover letters to bootstrap your writing style profile,
phrase library, and first template — without starting from a blank page.

---

## Setup

1. Create an `archive/pre-gen/` folder alongside your `assets/` folder
2. Drop your old cover letters there as PDFs (any version, any role — more is better)
3. Run the prompt below in Claude Code

The more letters you include, the richer the style extraction.
Letters from different contexts (startup, enterprise, different roles) help Claude
identify what's consistent (your voice) vs what varies (your framing).

---

## The Prompt

Run this in Claude Code, pointing to your archive folder.

---

I want to bootstrap my cover letter system from my existing cover letters.

My archive folder is at: [path to archive/pre-gen/]
My assets folder is at: [path to assets/]

Please:
1. Read all PDF files in the archive/pre-gen/ folder
2. Perform the analysis below across all letters
3. Generate the three output files

---

### Analysis to perform

**Writing style extraction**

Across all letters, identify:

- **Voice and tone**: How do I naturally write? (formal / warm / direct / narrative)
  What adjectives describe the overall feel?
- **Sentence rhythm**: Do I write in short punchy sentences, longer flowing ones, or mixed?
  Approximate average sentence length.
- **Opening patterns**: How do I typically open? (with a claim / with context / with a question /
  with a reference to the company)
- **First-person style**: How do I use "I"? Confident and direct, or hedged?
  Do I avoid "I am passionate about" type phrases — or use them?
- **Vocabulary fingerprint**: Words and phrases I use repeatedly. Words I never use.
  Sophistication level (plain / professional / elevated).
- **Closing patterns**: How do I typically close? (assertive / warm / neutral)
- **What works**: Which letters read best? What makes them stronger?
- **What to avoid**: Any patterns that feel weak, generic, or off-voice?

**Phrase extraction**

Pull out phrases worth keeping — strong lines, good transitions, effective closings.
Organise by section: opening, motivation, skills bridge, company connection, closing.

**Template inference**

Based on the letters, what structure do I default to?
- What length do I tend to write?
- Do I use visual structure (headers/bullets) or flowing prose?
- What sections always appear?

---

### Output files

**1. `writing-style.md`**

A voice profile I can hand to the cover-letter-generator. Include:
- Tone summary (2-3 sentences)
- Sentence rhythm guidance
- Vocabulary: words to use / words to avoid
- Opening: what works for me
- Closing: what works for me
- 3-5 example sentences extracted from my letters that exemplify my best voice
- Red flags: patterns to avoid (extracted from weaker sections)

**2. `phrase-library.md`**

Organised by section, pull the strongest phrases from my existing letters.
Use the template format from `phrase-library/phrase-library.template.md`.
Mark each phrase with a tone tag: [formal] [warm] [direct] [narrative].

**3. `first-template-suggestion.md`**

Based on the patterns observed, suggest a first cover letter template using the
format from `template-generator-prompt.md`. Pre-fill the metadata header and
all sections. Note: "Inferred from existing letters — review before saving to library."

---

### If letters are thin or only one exists

If there isn't enough to infer a reliable style, flag which sections need input:
`<!-- FILL IN: not enough examples to infer — run writing-style-wizard.md -->`

Still extract whatever phrases are worth keeping.
