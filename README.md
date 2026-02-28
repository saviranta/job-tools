# job-tools

Agentic tools for job searching, application writing, and career positioning.
Each tool is a self-contained prompt workflow — bring your own personal data,
use the tools to generate output.

All tools run in Claude Code. No code to run, no servers to set up.

---

## Tools

### [personalised-cv-coverletter-generator](./personalised-cv-coverletter-generator/)

Generates tailored, print-ready CVs and cover letters from a personal career asset library.

- Analyses the job listing and company website (Chrome MCP)
- Matches your capabilities to the role using a tagged, indexed asset library
- Generates CV and cover letter in structured markdown, then fills branded HTML templates
- Runs a six-persona review (ATS, HR Recruiter, Hiring Manager, Role Expert, CEO/CFO/Legal, Copywriter)
- Human-reviewed at every decision point — nothing is saved without your approval
- Includes mechanical eval checks and a qualitative eval prompt for post-generation integrity

Full workflow, asset templates, and onboarding prompts included.

---

## Design principles

**Separation of tool and data.** These tools contain prompts, workflows, and structural
patterns — not personal information. You provide your own career assets (work history,
skills, voice) as input; the tools produce the output. Your data lives in your workspace,
never in this repo.

**Prompt-based, not code-based.** Workflows are markdown files pasted into Claude Code.
No dependencies, no installs beyond Claude Code itself.

**Human in the loop.** Every significant decision has an approval gate. Nothing is
written to file without confirmation.

---

## Related

- [pm-tools](https://github.com/saviranta/PM-tools) — LLM workflows for product management
- [claude-code-tools](https://github.com/saviranta/claude-code-tools) — Claude Code–specific workflows and configurations
