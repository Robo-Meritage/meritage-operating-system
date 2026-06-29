# Domain Model

> The canonical business language for Meritage Partners. Define once. Reference everywhere.
>
> ---
>
> ## Purpose
>
> The Domain Model is the foundation of the Meritage Operating System. It establishes the shared vocabulary, entity definitions, lifecycle stages, and relationships that every other document in MOS depends on.
>
> Before this folder existed, terms like "Client," "Engagement," and "Qualified Introduction" were defined inconsistently across documents — sometimes differently in the same document. The Domain Model eliminates that ambiguity by establishing a single authoritative definition for each term and entity.
>
> ---
>
> ## Why Operational Documents Should Reference These Definitions
>
> When a playbook, template, or process document needs to reference a business term, it should link to the relevant definition here rather than define it inline. There are three reasons for this:
>
> **Consistency.** A term defined in one place means the same thing everywhere. A term defined in ten places means ten slightly different things.
>
> **Maintainability.** When a definition changes — because the business evolves or a term is refined — updating one canonical source is correct. Updating ten scattered definitions is error-prone and typically incomplete.
>
> **AI readability.** When Claude or any other AI tool reads MOS documents, a consistent vocabulary allows it to reason accurately about the business. Inconsistent definitions force the AI to guess at meaning, which degrades the quality of its output.
>
> ---
>
> ## What Belongs in This Folder
>
> | File | Contents |
> |---|---|
> | `glossary.md` | Alphabetical definitions of all key terms |
> | `business-entities.md` | Structured definitions of every object Meritage works with |
> | `lifecycle.md` | High-level stages of a Meritage engagement |
> | `relationships.md` | How major entities relate to one another |
>
> ---
>
> ## How to Use This Folder
>
> - **Before defining any term in a new document**, check `glossary.md` first. If the term exists, link to it.
> - - **If a term is missing**, add it to `glossary.md` before using it elsewhere. Mark it as `Pending Definition` if the authoritative definition has not yet been established.
>   - - **Do not redefine canonical terms** in downstream documents. If a definition is wrong, update it here and record the change in `CHANGELOG.md`.
>     - - **Mermaid diagrams** in `relationships.md` are the canonical visual representation of how entities relate. Reference them in other documents by linking to this folder.
>      
>       - ---
>
> *Last updated: 2026-06-29*
