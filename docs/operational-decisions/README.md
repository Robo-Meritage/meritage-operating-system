# Operational Decisions

> This folder records the business decisions that shaped how Meritage operates. It is distinct from the Architecture Decision Records in [docs/decisions/](../decisions/README.md), which document repository and technology choices. Operational decisions document *why Meritage does business the way it does*.
>
> ---
>
> ## Purpose
>
> Every firm develops practices over time. Some are deliberate. Many are inherited. The best ones are reasoned. When someone asks “Why do we do it this way?” there should be a documented answer.
>
> This folder captures the reasoning behind Meritage's most consequential business decisions. It protects institutional knowledge from advisor turnover, prevents revisiting settled questions, and provides new team members with a window into how the firm thinks.
>
> ---
>
> ## Distinction from Architecture Decision Records
>
> | Folder | Decision Type | Examples |
> |---|---|---|
> | docs/decisions/ | Repository and technology | Why Markdown, why GitHub, why this folder structure |
> | docs/operational-decisions/ | Business and advisory methodology | Why Reverse Lehman, why 5P Framework, why we require management call prep |
>
> Both use a similar format. Both are permanent records. Neither is deleted — decisions may be superseded, but the original reasoning is preserved.
>
> ---
>
> ## Format
>
> Each operational decision record (ODR) follows this structure:
>
> ```
> # ODR-[NNN]: [Short Title]
>
> **Date:** YYYY-MM-DD
> **Status:** [Active / Superseded / Deprecated]
> **Superseded by:** [ODR-NNN, if applicable]
>
> ## Decision
> [One sentence: the decision made.]
>
> ## Context
> [What situation or question prompted this decision? What was the firm experiencing?]
>
> ## Options Considered
> 1. [Option A]
> 2. [Option B]
> 3. [Option C, if applicable]
>
> ## Rationale
> [Why was this option chosen? What factors were weighted? What trade-offs were accepted?]
>
> ## Implications
> [What changed as a result? What does this decision constrain or enable?]
>
> ## Related Documents
> [Links to standards, frameworks, or modules affected.]
> ```
>
> ---
>
> ## Index
>
> | File | Title | Date | Status |
> |---|---|---|---|
> | [odr-001-reverse-lehman-fee-structure.md](odr-001-reverse-lehman-fee-structure.md) | Why Meritage Uses the Reverse Lehman Fee Structure | 2026-07-01 | Active |
> | [odr-002-advisor-centric-qualification.md](odr-002-advisor-centric-qualification.md) | Why Meritage Moved from Broker-Centric to Advisor-Centric Qualification | 2026-07-01 | Active |
> | [odr-003-5p-framework-adoption.md](odr-003-5p-framework-adoption.md) | Why Meritage Adopted the 5P Framework | 2026-07-01 | Active |
> | [odr-004-management-call-preparation.md](odr-004-management-call-preparation.md) | Why Meritage Requires Formal Management Call Preparation | 2026-07-01 | Active |
>
> ---
>
> ## Related Documents
>
> - [Architecture Decision Records](../decisions/README.md)
> - - [Capability Maturity Model](../capability-maturity.md)
>   - - [Meritage 5P Framework](../frameworks/meritage-5p-framework.md)
>     - - [What We Believe](../company/what-we-believe.md)
>       - - [Case Studies](../case-studies/README.md)
>        
>         - ---
>
> *Last updated: 2026-07-01*
> *See [CONTRIBUTING.md](../../CONTRIBUTING.md) for document standards.*
