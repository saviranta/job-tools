# job-tools

Agentic tools for job searching, application writing, and career positioning. Each tool is a self-contained prompt workflow or agent pattern — bring your own personal data, use the tools to generate output.

## Tools

| Tool | Description |
|------|-------------|
| `job-listing-analyzer/` | Interprets a job ad and company website: extracts role type, seniority signals, culture cues, and what the employer actually values |
| `brand-inspector/` | Analyzes a company's website to extract its design system (colors, typography, layout) for use in styled documents |
| `cv-template-selector/` | Algorithm for choosing the right CV structure given a job context |
| `cv-generator/` | Two-phase CV generation: outline → full content, with review gates between phases |
| `cover-letter-generator/` | Structured cover letter in four sections, tone-matched to role and company |
| `competency-cluster-library/` | Modular competency cluster pattern — a way to organize and reuse capability descriptions across applications |
| `linkedin-profile-writer/` | Role-by-role narrative structure for LinkedIn, with scroll-hook opening format |

## Design principles

**Separation of tool and data.** These tools contain prompts, workflows, and structural patterns — not personal information. You provide your own career assets (work history, skills, voice) as input; the tools produce the output.

**Composable.** Tools are designed to chain: `job-listing-analyzer` → `cv-template-selector` → `cv-generator` → `cover-letter-generator` is a natural end-to-end flow.

**Brand-aware.** The `brand-inspector` feeds into document styling so generated CVs and cover letters visually match the company's identity.

## Structure

```
job-tools/
├── job-listing-analyzer/
├── brand-inspector/
├── cv-template-selector/
├── cv-generator/
├── cover-letter-generator/
├── competency-cluster-library/
└── linkedin-profile-writer/
```

Each tool folder contains:
- `README.md` — what it does, inputs, outputs, usage
- `prompt.md` — the core prompt(s)
- `example/` — a worked example with anonymized data

## Related

- [pm-tools](https://github.com/saviranta/PM-tools) — LLM workflows for product management
- [claude-code-tools](https://github.com/saviranta/claude-code-tools) — Claude Code–specific workflows and configurations
