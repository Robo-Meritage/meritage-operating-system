# AGENTS.md — AI Agent Roster for the Meritage Operating System

> This file defines the AI agents authorized to work in this repository, their roles, capabilities, and operating constraints.

## Overview

The Meritage Operating System is designed to be **AI-native**. Agents are used to draft documents, maintain structure, surface knowledge, and assist decision-making. This file is the authoritative reference for how agents should operate.

## Active Agents

### Claude (Anthropic)

**Primary use:** Document drafting, editing, research synthesis, Q&A against the knowledge base.

**Authorized actions:**
- Read and navigate all files in this repository
- Draft new Markdown documents following MOS conventions
- Edit and improve existing documents
- Summarize and synthesize content across folders
- Suggest structure, naming, and organization improvements

**Constraints:**
- Must follow naming conventions defined in `CONTRIBUTING.md`
- Must not add confidential data to any file
- Must not modify `archive/` without explicit human instruction
- Must ask for clarification before creating new top-level folders
- Context file: `CLAUDE.md`

---

### GitHub Copilot

**Primary use:** In-editor assistance for writing and editing Markdown files.

**Authorized actions:**
- Autocomplete and suggest content within files
- Help format tables, lists, and code blocks

**Constraints:**
- Suggestions must be reviewed by a human before committing
- Should not generate content that contradicts existing MOS documents

---

## Agent Operating Principles

All agents working in this repository must follow these principles:

1. **Source of truth first** — If a fact exists in this repo, use it. Do not hallucinate Meritage-specific details.
2. **Markdown only** — All outputs must be valid Markdown. No HTML, no DOCX, no PDFs.
3. **Naming conventions** — Follow the `lowercase-hyphen-separated.md` pattern at all times.
4. **Human in the loop** — Significant structural changes require human review before committing.
5. **Audit trail** — All agent-made changes should be clearly attributed in commit messages (e.g., `docs: [claude] drafted employee-onboarding.md`).
6. **Least privilege** — Agents should only access what they need for the current task.

## Adding a New Agent

To authorize a new agent:

1. Add it to the **Active Agents** section above with its role, authorized actions, and constraints.
2. Create a context file in `docs/ai/` (e.g., `docs/ai/gpt-context.md`).
3. Open a PR and get approval from a team lead.
4. Document the decision in `docs/decisions/`.

## Revoking Agent Access

To revoke or restrict an agent:

1. Move its entry from **Active Agents** to an **Inactive Agents** section below.
2. Note the date and reason for revocation.
3. Archive its context file.

## Inactive Agents

_None at this time._
