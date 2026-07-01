# ChatGPT Collaboration Learnings

> This document captures the patterns, successful approaches, failed experiments, and institutional knowledge that accumulated during the Meritage-ChatGPT collaboration. It is the raw material of the knowledge transfer — the things that can't be inferred from polished documentation alone.
>
> **Classification:** Proprietary
> **Audience:** Claude and authorized AI systems
> **Status:** Partially complete. Entries marked *[Pending]* require Daniel's direct input.
>
> ---
>
> ## How to Read This Document
>
> This is not a polished document. It is a working record. Some entries are detailed. Some are placeholders. The value is not in the prose — it is in the patterns.
>
> When Claude reads this document, the goal is to build an internal model of the history and context behind the MOS. A new session that begins with this document should feel less like starting over and more like continuing.
>
> ---
>
> ## What Worked
>
> ### Framing shifts
>
> The most productive moments in the collaboration were framing shifts — when the question changed, not just the answer.
>
> - "We're encoding intellectual property, not writing documentation." (v0.5) — This reframe raised the quality standard for everything that followed.
> - - "What capability are we building?" rather than "What document do we write next?" (v0.6) — This reframe changed how milestones were scoped.
>   - - "Stop versioning by document count. Start tracking capability maturity." (v0.7) — This reframe changed what progress means.
>    
>     - Pattern: Daniel generates the reframe. The AI's job is to hear it, accept it fully, and apply it rigorously to everything that follows.
>    
>     - ### Structural proposals before content
>    
>     - Daniel consistently responded better to proposed structures (outlines, frameworks, dependency chains) before content was written. This saved significant rework.
>
> Pattern: When beginning a new document type or module, propose the structure first. Wait for alignment. Then write.
>
> ### The Goldman Sachs Test as a quality gate
>
> Once introduced, this test became the reliable standard for catching generic language. Any sentence that could apply to Goldman Sachs, a regional broker, and Meritage equally is not specific enough.
>
> Pattern: Apply this test to every paragraph of every MOS document. If a paragraph fails, rewrite it.
>
> ### Dependency chain thinking
>
> Once the dependency chain (Qualification → Engagement → Valuation → Positioning → GTM → ...) was made explicit, the sequencing of work became clearer and the rationale for priorities became defensible.
>
> Pattern: Always check the dependency chain before proposing next steps. A module that has unresolved dependencies upstream is a risk.
>
> ### Lessons Learned sections
>
> Adding Lessons Learned to every module (even as placeholders) was a structural decision that created space for institutional memory. The placeholder format — Company → Takeaway → Framework impact — is correct and should be maintained.
>
> Pattern: Lessons Learned sections should never be deleted, even when empty. They signal that the module expects to accumulate experience over time.
>
> ---
>
> ## What Didn't Work
>
> ### Building before establishing the dependency
>
> Early in the collaboration, some modules were built before their upstream dependencies were solid. This created inconsistencies that required retroactive reconciliation.
>
> Learning: The dependency chain should be verified before beginning any new module. If a dependency is at Level 1 (scaffold), document it as a risk before proceeding.
>
> ### Generic module content
>
> Scaffolded modules that were populated with generic M&A language had to be substantially rewritten when fully realized. Generic content creates a false sense of completeness.
>
> Learning: Empty scaffolds (placeholder sections with a brief description of what belongs there) are better than generic content. Generic content is harder to update than an empty placeholder.
>
> ### Version numbering by document count
>
> Early version numbering tracked file additions. This produced misleading progress indicators — adding a scaffold file looked the same as fully realizing a module.
>
> Learning: The Capability Maturity Model (v0.7) is the correct replacement. Version milestones should be tied to capability advancement, not file creation.
>
> ### Overly long documents in a single typing session
>
> Very large files typed in a single session sometimes triggered CDP timeout errors. The content was always fully entered, but the error created uncertainty.
>
> Learning: For files over approximately 150 lines, consider building in sections or verifying content is present before committing.
>
> ---
>
> ## Recurring Patterns
>
> ### The reframe-then-execute pattern
>
> Daniel consistently offers a strategic reframe before asking for execution. The reframe is the actual instruction. The execution request that follows is secondary. AI systems should listen for the reframe and make sure it is fully absorbed before proceeding.
>
> ### Principles before tactics
>
> When Daniel describes how something should work, he starts with principles. The tactics follow from the principles. AI systems should capture the principles and derive the tactics from them, not reverse-engineer the principles from tactical requests.
>
> ### Simultaneous tracks
>
> Daniel thinks in parallel workstreams. The MOS has always had a content track (writing modules) and a structural track (architecture, frameworks, standards). Both are active simultaneously. AI systems should be capable of switching between tracks in a single session without losing context.
>
> ### Explicit rejection of the obvious
>
> Daniel will often say "not X" before saying "Y." The rejection is as informative as the choice. Capturing what was explicitly rejected is as important as capturing what was chosen.
>
> ---
>
> ## Topics Explored Repeatedly
>
> *[Pending: Daniel to identify. What questions or topics came up more than twice in the ChatGPT collaboration? These represent areas of ongoing uncertainty, recurring challenges, or unresolved strategic questions.]*
>
> Provisional observations (to be confirmed):
> - Fee structure: how to present the Reverse Lehman to resistant sellers
> - - Qualification: where to draw the line between conditional engagement and decline
>   - - Valuation: how to handle significant valuation expectation gaps at engagement
>     - - AI boundaries: what AI can and cannot do in an advisory context
>      
>       - ---
>
> ## Decisions Made That Aren't Formally Recorded
>
> *[Pending: Daniel to identify. The operational decisions folder captures four formal ODRs. What other decisions were made in the ChatGPT conversation history that should be documented? This is one of the highest-value sections to complete.]*
>
> Areas to consider:
> - Engagement agreement structure decisions
> - - Specific qualification criteria that were debated and resolved
>   - - Positioning approach decisions (what to include in a CIM vs. what to withhold)
>     - - Buyer outreach strategy decisions
>       - - Technology choices (what tools Meritage uses or doesn't use)
>        
>         - ---
>
> ## The Knowledge That Lives Only in Daniel
>
> This section is a structured list of areas where the knowledge transfer is incomplete because the knowledge has never been written down. These are the highest-priority items for Daniel to address.
>
> | Topic | Why It Matters | Priority |
> |---|---|---|
> | AppleBites context | AI cannot assist with AppleBites work without knowing what it is | High |
> | Empire Builder context | AI cannot assist with Empire Builder work without knowing what it is | High |
> | Brian's profile | AI needs to know Brian's role and preferences to assist in joint decisions | High |
> | Agreement structures rejected | Prevents AI from proposing structures already tried and abandoned | Medium |
> | Reverse Lehman in the room | The formal rationale exists; the live presentation script does not | Medium |
> | Buyer community relationships | Which buyers Meritage has relationships with, and the nature of those relationships | Medium |
> | Writing style evolution | How early document preferences differed from current ones | Low |
> | Recurring friction points | What types of requests or situations produce frustration | Low |
>
> ---
>
> ## How This Document Should Be Used
>
> **Daniel's role:** Add to this document whenever a pattern, preference, decision, or piece of institutional knowledge comes up in conversation that isn't captured elsewhere. The question to ask is: *If I didn't remember this, what would we have to relearn?*
>
> **Claude's role:** Read this document at the beginning of any working session involving Meritage advisory or strategic work. Update it when a new pattern is observed. Flag when an entry appears to be outdated or superseded.
>
> **The test:** An AI system that has read this document should be able to say, with reasonable confidence, what Daniel would do in situations not explicitly covered by the MOS.
>
> ---
>
> *Last updated: 2026-07-01*
> *See [CONTRIBUTING.md](../../CONTRIBUTING.md) for document standards.*
