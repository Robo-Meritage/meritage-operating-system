# Chat History Ingestion

> This folder is the primary knowledge migration workstream. Its purpose is to transform the existing ChatGPT conversation history into structured, retrievable knowledge in the MOS repository.
> >
> >> The MOS currently captures final outputs. This folder captures the decisions, preferences, patterns, and reasoning that produced those outputs.
> >>
> >> **Classification:** Proprietary
> >> **Audience:** Claude and Meritage principals
> >>
> >> ---
> >>
> >> ## The Problem This Solves
> >>
> >> Over the last year of ChatGPT collaboration, thousands of decisions were made. Agreements were drafted and revised. Frameworks were accepted and rejected. Preferences were revealed. Patterns emerged across dozens of conversations that weren't obvious in any single one.
> >>
> >> None of that lives in the MOS. It lives in chat history that Claude cannot access.
> >>
> >> The MOS repository is well-structured but incomplete. It contains approximately 20–30% of the knowledge that exists in the collaboration. The remaining 70–80% is in the conversation corpus.
> >>
> >> This folder is the extraction engine.
> >>
> >> ---
> >>
> >> ## This Is a Data Engineering Problem
> >>
> >> This is not a documentation problem. It is not an interview problem. It is an ingestion problem.
> >>
> >> The workflow is:
> >>
> >> ```
> >> Conversation provided by Daniel
> >>         ↓
> >> Claude identifies topic and entities
> >>         ↓
> >> Claude extracts facts, decisions, preferences, patterns, lessons
> >>         ↓
> >> Claude links extracted knowledge to existing MOS documents
> >>         ↓
> >> Claude commits structured knowledge to this folder
> >>         ↓
> >> Daniel reviews for quality and flags gaps
> >> ```
> >>
> >> Daniel provides the raw material. Claude processes it. Nothing is invented. Everything is extracted.
> >>
> >> ---
> >>
> >> ## The Extraction Format
> >>
> >> Every conversation or conversation batch produces one or more knowledge records. Each record follows this structure:
> >>
> >> ```
> >> ## [Topic Name]
> >>
> >> **Source:** [Conversation date or identifier, if known]
> >> **Category:** [agreements / gtm / hr / operations / applebites / empire-builder / etc.]
> >> **Entities:** [People, companies, products, or deals mentioned]
> >>
> >> ### Learned
> >> [What was established as true, accurate, or accepted in this conversation.]
> >>
> >> ### Rejected
> >> [What was explicitly considered and ruled out. Include what it was and why.]
> >>
> >> | Option | Reason rejected |
> >> |---|---|
> >> | [Option A] | [Why] |
> >>
> >> ### Accepted
> >> [What was adopted, approved, or decided.]
> >>
> >> ### Why
> >> [The reasoning behind what was accepted. This is the most important field.]
> >>
> >> ### Patterns
> >> [Recurring behaviors, preferences, or tendencies that this conversation illustrates. These are about Daniel or the collaboration, not just about the topic.]
> >>
> >> ### Open Questions
> >> [Anything left unresolved that should be carried forward.]
> >>
> >> ### Links
> >> [Connections to existing MOS documents that this knowledge affects or should be read alongside.]
> >> ```
> >>
> >> ---
> >>
> >> ## Folder Structure
> >>
> >> Knowledge records are organized by topic category, matching the domains that appeared repeatedly in the ChatGPT collaboration.
> >>
> >> ```
> >> chat-history/
> >> ├── README.md              ← this file
> >> ├── INGESTION-GUIDE.md     ← how to submit conversations for processing
> >> ├── agreements/            ← engagement agreements, NDAs, affiliate agreements, LOIs
> >> ├── applebites/            ← AppleBites product and strategy
> >> ├── deal-analysis/         ← specific deal work, negotiation, client analysis
> >> ├── emails/                ← email rewrites, templates, communication style
> >> ├── empire-builder/        ← Empire Builder product and strategy
> >> ├── gtm/                   ← go-to-market strategy, marketing, lead generation
> >> ├── hr/                    ← hiring, onboarding, org design, compensation
> >> ├── marketing/             ← LinkedIn, webinars, content, brand
> >> ├── operations/            ← systems, CRM, processes, tools
> >> ├── transcripts/           ← call transcripts and meeting notes
> >> └└── weekly-calls/          ← recurring strategic discussions
> >> ```
> >>
> >> ---
> >>
> >> ## Ingestion Status
> >>
> >> | Category | Records | Last ingested | Notes |
> >> |---|---|---|---|
> >> | agreements/ | 0 | — | Awaiting corpus |
> >> | applebites/ | 0 | — | Awaiting corpus |
> >> | deal-analysis/ | 0 | — | Awaiting corpus |
> >> | emails/ | 0 | — | Awaiting corpus |
> >> | empire-builder/ | 0 | — | Awaiting corpus |
> >> | gtm/ | 0 | — | Awaiting corpus |
> >> | hr/ | 0 | — | Awaiting corpus |
> >> | marketing/ | 0 | — | Awaiting corpus |
> >> | operations/ | 0 | — | Awaiting corpus |
> >> | transcripts/ | 0 | — | Awaiting corpus |
> >> | weekly-calls/ | 0 | — | Awaiting corpus |
> >>
> >> ---
> >>
> >> ## What "Awaiting Corpus" Means
> >>
> >> Claude cannot access ChatGPT's conversation history. The conversations must be provided directly — pasted into a session, uploaded as text files, or exported and shared in any readable format.
> >>
> >> Once provided, Claude processes each batch immediately. No pre-processing by Daniel is required. Daniel's only job at ingestion time is to provide the raw conversations. Claude handles the extraction, categorization, and committing.
> >>
> >> See [INGESTION-GUIDE.md](INGESTION-GUIDE.md) for the exact process.
> >>
> >> ---
> >>
> >> ## Priority Order for Ingestion
> >>
> >> When corpus is available, process in this order:
> >>
> >> 1. **Agreements** — highest specificity, most decisions with explicit rationale
> >> 2. 2. **AppleBites and Empire Builder** — completely absent from MOS; any conversation fills a gap
> >>    3. 3. **Deal analysis** — institutional knowledge about specific engagements
> >>       4. 4. **Operations** — CRM, systems, tools decisions
> >>          5. 5. **GTM and marketing** — strategy and execution patterns
> >>             6. 6. **HR** — hiring and org design
> >>                7. 7. **Emails and transcripts** — communication style and preferences
> >>                   8. 8. **Weekly calls** — strategic evolution over time
> >>                     
> >>                      9. ---
> >>                     
> >>                      10. ## Related Documents
> >>                     
> >>                      11. - [INGESTION-GUIDE.md](INGESTION-GUIDE.md)
> >> - [Knowledge Transfer Index](../README.md)
> >> - - [ChatGPT Handoff](../../ai/chatgpt-handoff.md)
> >>   - - [Daniel's Operating Model](../daniels-operating-model.md)
> >>    
> >>     - ---
> >>
> >> *Last updated: 2026-07-01*
> >> *See [CONTRIBUTING.md](../../../CONTRIBUTING.md) for document standards.*
