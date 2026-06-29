# Contributing to the Meritage Operating System

> This guide explains how to add, edit, and maintain documents in the MOS.

## Core Principle

The Meritage Operating System is a living document. It should be updated continuously as the company evolves. Every team member is a contributor.

## File Format

All documents must be written in **Markdown** (`.md`). No exceptions.

Reasons:
- AI tools ingest Markdown natively
- GitHub renders it automatically
- Plain text is easy to search and version
- Portable across any platform or tool

## Naming Convention

Files must use lowercase, hyphen-separated names that clearly describe their content.

**Pattern:** `lowercase-hyphen-separated-descriptive-name.md`

| Instead of | Use |
|---|---|
| `proposal.docx` | `affiliate-program.md` |
| `Call Notes Final v2.docx` | `management-call-playbook.md` |
| `Fee Structure.xlsx` | `reverse-lehman-formula.md` |
| `Weekly Sync.docx` | `weekly-operating-rhythm.md` |
| `New Hire.docx` | `employee-onboarding.md` |

Never use:
- Spaces in filenames
- CamelCase or PascalCase
- Version numbers in filenames (use Git for versioning)
- Vague names like `notes.md`, `draft.md`, or `misc.md`

## Folder Structure

Place files in the most specific applicable folder:

| Folder | What goes here |
|---|---|
| `docs/company/` | Mission, values, org chart, culture |
| `docs/executive/` | OKRs, board materials, leadership playbooks |
| `docs/operations/` | SOPs, workflows, weekly operating rhythm |
| `docs/m-and-a/` | Deal frameworks, diligence checklists, integration |
| `docs/products/` | Product specs, roadmaps, feature docs |
| `docs/marketing/` | Brand guidelines, campaigns, affiliate program |
| `docs/hr/` | Hiring, onboarding, comp, performance |
| `docs/legal/` | Contract templates, compliance, entity structure |
| `docs/technology/` | Tech stack, architecture, AI tooling, security |
| `docs/templates/` | Reusable document templates |
| `docs/ai/` | Agent instructions, prompt library, AI workflows |
| `docs/decisions/` | Architecture Decision Records (ADRs) |

## Document Structure

Every document should follow this structure:

```markdown
# Document Title

> One-line description of what this document is and why it exists.

## Section One

Content here...

## Section Two

Content here...

---

*Last updated: YYYY-MM-DD*
```

### Required Elements

1. **H1 title** at the top
2. **Blockquote description** immediately below the title
3. **Sections** using `##` and `###` headings
4. **Last updated date** at the bottom

## How to Add a New Document

1. Identify the correct folder for your document
2. Create a new file with a descriptive, hyphen-separated name ending in `.md`
3. Follow the document structure above
4. Commit directly to `main` for routine additions
5. Open a pull request for significant changes or anything that affects multiple documents
6. Update `CHANGELOG.md` with your addition

## How to Edit an Existing Document

1. Open the file in GitHub
2. Click the pencil icon to edit
3. Make your changes
4. Write a clear commit message (e.g., `docs: update employee-onboarding with new Day 1 checklist`)
5. Commit directly to `main` for minor edits
6. Update the `Last updated` date at the bottom of the document

## Commit Message Format

Use the following prefixes:

| Prefix | When to use |
|---|---|
| `docs:` | Adding or updating a document |
| `structure:` | Adding folders or reorganizing |
| `fix:` | Correcting errors in existing docs |
| `archive:` | Moving a document to archive/ |

Example: `docs: add reverse-lehman-formula.md to m-and-a`

## Archiving Documents

When a document is no longer current but should be preserved:

1. Move it to `archive/`
2. Add a note at the top: `> **Archived:** YYYY-MM-DD. Reason: [brief explanation]`
3. Update `CHANGELOG.md`

Do not delete documents. Archive them.

## Questions

If you are unsure where a document belongs or how to structure it, open a GitHub issue or ask in the team channel.
