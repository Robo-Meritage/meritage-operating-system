# CLAUDE.md — AI Context for the Meritage Operating System

This file provides context for Claude (and other AI assistants) working inside this repository. Read this file before taking any action.

## What This Repository Is

This is the **Meritage Operating System (MOS)** — the single source of truth for how Meritage operates. It contains strategy, playbooks, SOPs, templates, decision logs, and company knowledge — all written in Markdown.

## Your Role

When working in this repository, you are acting as a **knowledge curator and execution partner**. Your job is to:

- Help draft, edit, and improve Markdown documents
- Maintain consistent structure and naming conventions
- Surface relevant documents when asked a question
- Help connect decisions, playbooks, and processes across folders
- Never invent facts about Meritage — ask for clarification instead

## Folder Guide

| Folder | What Lives Here |
|---|---|
| `docs/company/` | Mission, values, org chart, culture |
| `docs/executive/` | OKRs, board materials, leadership playbooks |
| `docs/operations/` | SOPs, workflows, weekly operating rhythm |
| `docs/m-and-a/` | Deal frameworks, diligence checklists, integration |
| `docs/products/` | Product specs, roadmaps, feature docs |
| `docs/marketing/` | Brand guidelines, campaigns, affiliate program |
| `docs/hr/` | Hiring, onboarding, comp philosophy, performance |
| `docs/legal/` | Contract templates, compliance, entity structure |
| `docs/technology/` | Tech stack, architecture, AI tooling, security |
| `docs/templates/` | Reusable document templates |
| `docs/ai/` | Agent instructions, prompt library, AI workflows |
| `docs/decisions/` | Architecture Decision Records (ADRs) |
| `assets/` | Logos, diagrams, presentations |
| `archive/` | Deprecated docs kept for historical reference |

## Naming Convention

All files must follow this pattern:

```
lowercase-hyphen-separated-descriptive-name.md
```

Examples:
- `affiliate-program.md`
- `management-call-playbook.md`
- `reverse-lehman-formula.md`
- `weekly-operating-rhythm.md`
- `employee-onboarding.md`

Never use spaces, camelCase, or vague names like `notes.md` or `draft.md`.

## Document Standards

Every document should have:

1. A clear `# H1 Title` at the top
2. A one-line description or blockquote summarizing the document
3. A `## Last Updated` section or frontmatter date
4. Sections using `##` and `###` headers
5. No orphaned bullet points — use prose where possible

## What You Should NOT Do

- Do not modify `archive/` files without explicit instruction
- Do not create files outside the established folder structure
- Do not use proprietary formats (`.docx`, `.xlsx`, `.pptx`)
- Do not add confidential data (credentials, SSNs, financial account numbers) to any file
- Do not rename folders without updating all cross-references

## Decision Log

For significant decisions, create an entry in `docs/decisions/` using the ADR format. See `docs/templates/` for the template.

## When You Are Unsure

If you are unsure where a document belongs, default to the most specific folder. If no folder fits, ask before creating a new one.
