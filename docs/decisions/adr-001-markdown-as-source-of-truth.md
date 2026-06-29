# ADR-001: Markdown as the Source of Truth for MOS

> All Meritage Operating System documents are authored and stored as Markdown files.
>
> ---
>
> ## Status
>
> Accepted
>
> ---
>
> ## Date
>
> 2026-06-29
>
> ---
>
> ## Context
>
> Meritage needed a documentation format for the MOS that would be durable, readable, version-controllable, and accessible to both human operators and AI tools.
>
> The primary options evaluated were:
>
> 1. **Microsoft Word / Google Docs** — familiar, widely used, supports rich formatting
> 2. 2. **Notion / Confluence** — structured wikis with built-in navigation and databases
>    3. 3. **Markdown in a Git repository** — plain text, version-controlled, platform-agnostic
>       4. 4. **PDF** — portable and final, but not editable or diffable
>         
>          5. The decision needed to account for how Meritage works: a small, senior-led team that uses AI tools extensively, operates across multiple platforms, and needs documentation that is searchable, reviewable, and maintainable without a dedicated ops staff.
>         
>          6. ---
>         
>          7. ## Decision
>
> **All MOS documents are authored in Markdown and stored in a GitHub repository.**
>
> Proprietary formats (.docx, .xlsx, .pptx) are excluded from the repository. PDFs are permitted only as final external deliverables in `assets/presentations/`. The Markdown source always takes precedence.
>
> ---
>
> ## Rationale
>
> ### AI compatibility
> Markdown is the native input format for large language models. Every document in MOS can be pasted directly into Claude, GPT, or any other AI assistant without conversion, stripping, or reformatting. This is not incidental — AI-assisted work is a core part of how Meritage operates.
>
> ### Version control
> Git provides a complete, auditable history of every change to every document. You can see who changed what, when, and why. This is not possible with Google Docs version history or Word track changes at the same level of precision and permanence.
>
> ### GitHub renders Markdown natively
> Documents are readable directly in the browser at any URL in the repository. No special software is required. Any stakeholder with the URL can read any document.
>
> ### Portability
> Markdown files are plain text. They can be opened in any text editor, converted to HTML or PDF with standard tools, and migrated to any future platform without data loss or format degradation. There is no vendor lock-in.
>
> ### Searchability
> Plain text is the most searchable format that exists. GitHub's code search, local grep, and AI-assisted search all work on Markdown without indexing or conversion.
>
> ### Simplicity
> Markdown has a minimal syntax that anyone can learn in under an hour. It enforces consistency across documents and eliminates the formatting debt that accumulates in Word documents over time.
>
> ---
>
> ## Consequences
>
> ### Positive
> - Every document is AI-ready without preprocessing
> - - Full version history for all operational knowledge
>   - - No software licenses required to read or write documents
>     - - Consistent structure enforced by format constraints
>       - - Easy to search, diff, and review via pull request
>        
>         - ### Negative / Trade-offs
>         - - Rich formatting (embedded charts, complex tables, pixel-level layout) is not possible in Markdown
>           - - External stakeholders who expect Word documents or PDFs require a conversion step for final deliverables
>             - - Contributors unfamiliar with Markdown require a brief onboarding to the syntax
>              
>               - ### Mitigations
>               - - Complex tables and charts that cannot be expressed in Markdown are created as images and stored in `assets/diagrams/`
>                 - - External deliverables (proposals, CIMs, pitch decks) are converted to PDF or Word from the Markdown source and stored in `assets/presentations/`; the Markdown source is always retained
>                   - - `CONTRIBUTING.md` provides a syntax reference and document template to reduce onboarding friction
>                    
>                     - ---
>
> ## Alternatives Considered
>
> **Microsoft Word / Google Docs**
> Rejected. These formats are not natively version-controlled, are not AI-readable without conversion, and accumulate formatting debt over time. Collaboration requires a shared platform account and creates dependency on a third-party service.
>
> **Notion / Confluence**
> Rejected. These are excellent tools for team wikis but introduce platform dependency, are not AI-readable in their native format, and export to formats (HTML, PDF) that are not diffable. If the platform changes its pricing or availability, the knowledge base is at risk.
>
> **PDF**
> Rejected as a source format. PDFs are appropriate as final external deliverables but cannot be edited, searched efficiently, or version-controlled. They are outputs, not sources.
>
> ---
>
> ## Related Documents
>
> - `README.md` — Repository overview and naming conventions
> - - `CONTRIBUTING.md` — Document standards and Markdown syntax reference
>   - - `docs/ai/claude-context.md` — AI context including document format requirements
>     - - `docs/decisions/` — Index of all Architecture Decision Records
>      
>       - ---
>
> *Last updated: 2026-06-29*
