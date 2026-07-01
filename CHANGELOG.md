## [v0.7.4] — 2026-07 — Staged Migration Architecture

### Upgraded
- `docs/knowledge/chat-history/README.md` — Revised ingestion pipeline: Classify → Extract → Deduplicate → Link → Commit → Log. Added two-phase migration architecture: Phase 1 (Meritage Project, highest signal), Phase 2 (full export with classification filter). Added deduplication requirement and rationale. Updated to link to new migration log.
-
- ### Added
- - `docs/knowledge/migration/README.md` — Migration folder overview: purpose, architecture summary, why a migration log matters, current phase status.
  - - `docs/knowledge/migration/migration-log.md` — Audit trail for all ingestion batches. Includes batch entry template (source, conversations processed, records created, deduplication actions, conflicts flagged, ignored conversations, open questions). Resumable across sessions.
    -
    - ### Architecture Note
    - The ingestion pipeline now has five distinct steps where v0.7.3 had three. The additions — Classify and Deduplicate — address the core risk of a year-long collaboration corpus: noise ingestion and topic fragmentation. One authoritative synthesis per topic is more valuable than multiple partial records.
    -
    - ---
    -
    - ## [v0.7.3] — 2026-07-01

### Chat History Ingestion Infrastructure

This milestone establishes the ingestion layer for the ChatGPT-to-Claude knowledge migration. The recognition that drove this: the MOS captures final outputs. The 70–80% of knowledge that exists in the conversation corpus — decisions, rejected options, reasoning, preferences, patterns — does not yet exist in the repository. This is a data engineering problem, not a documentation problem.

**New folder: docs/knowledge/chat-history/**
- `README.md` — establishes the ingestion pipeline, the extraction format (Topic / Learned / Rejected / Accepted / Why / Patterns / Open Questions / Links), the folder taxonomy, ingestion status tracker, priority order, and a clear statement of the missing ingredient (Claude cannot access ChatGPT; conversations must be provided)
- - `INGESTION-GUIDE.md` — the operational protocol: how to export ChatGPT conversations, the exact prompt to use when starting an ingestion session, what Claude does with each batch (identify → extract → categorize → flag conflicts → commit → update status), quality standards for extracted knowledge, batch size guidance, and what happens after ingestion
  -
  - **11 category subfolders initialized** (all awaiting corpus):
  - - `agreements/` — Highest priority: engagement agreements, NDAs, affiliate agreements, LOIs
    - - `applebites/` — High priority: completely absent from MOS
      - - `empire-builder/` — High priority: completely absent from MOS
        - - `deal-analysis/` — High priority: deal-level institutional knowledge
          - - `emails/` — Email rewrites, templates, communication style
            - - `gtm/` — Go-to-market strategy, referral programs
              - - `hr/` — Hiring, onboarding, org design
                - - `marketing/` — LinkedIn, webinars, content, brand
                  - - `operations/` — CRM, systems, tools, workflows
                    - - `transcripts/` — Call transcripts and meeting notes
                      - - `weekly-calls/` — Recurring strategic discussions
                        -
                        - **Strategic framing:**
                        - The next action is not building more repository structure. It is providing the corpus. The fastest path: export ChatGPT conversations via Settings → Data Controls → Export Data, then paste batches into Claude sessions using the prompt in INGESTION-GUIDE.md. Start with agreements — highest specificity, most decisions with explicit rationale. Claude processes each batch without requiring pre-filtering or pre-organization by Daniel.
                        -
                        - ---
                        -
                        - ## [v0.7.2] — 2026-07-01

### Knowledge Extraction Interview Series Initialized

This milestone establishes the interview infrastructure for the knowledge extraction workstream and corrects a framing error from v0.7.1.

**Framing correction:** The phrase "Knowledge That Lives Only in Daniel" has been replaced throughout the knowledge folder with the more accurate framing: **"Knowledge That Exists Only Across Daniel + ChatGPT."** The synthesized patterns from thousands of interactions are a form of knowledge that neither party holds alone. The interview series is designed to surface both sources.

**New folder: docs/knowledge/interviews/**
- `README.md` — establishes the interview methodology, the roles of subject/interviewer/encoder, session index, what each session produces, how to conduct a session, and six additional topics identified as recurring ChatGPT themes
- - `interview-template.md` — the reusable blank format including: pre-session preparation (scope + opening questions + connections to prior sessions + known gaps), session summary, key insights table, decisions surfaced, positions challenged, open questions, repository updates, notes for next session
  -
  - **Six interview session files initialized:**
  - - `session-01-strategy.md` — **Ready.** Pre-session preparation complete with 10 opening questions covering origin, differentiation, broker vs. advisor distinction, the client you said no to, valuation philosophy, market choice, success definition, competition, constraints, and beliefs not yet proven
    - - `session-02-products.md` — Placeholder. Will cover AppleBites, Empire Builder, product strategy
      - - `session-03-people.md` — Placeholder. Will cover Brian, team roles, decision rights, communication, hiring
        - - `session-04-deals.md` — Placeholder. Will cover deal-level institutional knowledge, negotiation philosophy, red flags
          - - `session-05-ai.md` — Placeholder. Will cover AI expectations, where AI should challenge vs. defer, common mistakes
            - - `session-06-future.md` — Placeholder. Will cover three-to-five year direction, capabilities to build, services to avoid, what success looks like beyond revenue
              -
              - **Strategic framing:**
              - The shift from inference to extraction is now structural. Claude no longer guesses at tacit knowledge — it creates the infrastructure to receive it. Daniel talks, the AI organizes and tests, Claude encodes. Each session produces a permanent record with traceability: if someone later asks why a principle exists, they can follow the link to the conversation that produced it.
              -
              - Session 01 (Meritage Strategy) is ready to run whenever Daniel is.
              -
              - ---
              -
              - —————————–——————→# Changelog

All notable changes to the Meritage Operating System are documented here.

This project follows [Keep a Changelog](https://keepachangelog.com/en/1.0.0/) format.

---

## [0.6.0] – 2026-06-29

### Added

MOS v0.6: Client Qualification & Engagement — capability-first sprint encoding the qualification decision engine.

- `docs/frameworks/meritage-5p-framework.md` — The Meritage 5P Framework: proprietary qualification mental model evaluating every opportunity through People, Performance, Position, Potential, and Preparedness. Fully realized with what each lens evaluates, what excellent looks like, disqualifying signals in each lens, and how the framework recurs across the engagement lifecycle.
- - `docs/m-and-a/02-qualification.md` — Module 02 fully realized: answers four questions (Should we take this client? Can we successfully represent them? What work is required before going to market? If we say no, why?). Includes the 5P Framework application, 100-point Qualification Score with 6 weighted categories, step-by-step qualification process, objective decline reason taxonomy, and complete Common Failure Modes section.
  - - `docs/standards/client-qualification-standard.md` — The Meritage Client Qualification Standard: defines what a complete qualification assessment must contain (5 required components), minimum acceptable quality, conditions that preclude proceeding, conditions requiring documentation only, and disqualifying findings by 5P lens.
    - - `docs/templates/qualification-discovery-questionnaire.md` — Structured discovery conversation guide organized by the 5P Framework. 60–90 minute interview structure with opening approach, section-by-section questions for all 5 lenses, closing protocol including the preliminary valuation expectations test, and post-meeting notes template.
      - - `docs/templates/client-qualification-scorecard.md` — 100-point scoring instrument with 6 weighted categories (Financial Quality 20, Seller Readiness 20, Operational Maturity 20, Market Attractiveness 15, Growth Potential 15, Transaction Readiness 10). Includes scoring guidance per criterion, score interpretation guide (80–100 proceed, 65–79 proceed with caution, 50–64 conditional, <50 decline), disqualifying findings checklist, and qualification decision documentation section.
        -
        - ### Updated
        -
        - - `docs/frameworks/README.md` — Added 5P Framework to current frameworks table; marked both frameworks as Complete.
          - - `docs/m-and-a/README.md` — Marked Module 02 as Complete.
            - - `docs/INDEX.md` — Added 5P Framework to Frameworks section; added client-qualification-standard.md to Standards section; added two new templates to Templates section; marked Module 02 as Complete.
              -
              - ---
              -
              - ## [0.5.1] – 2026-06-29

### Added

MOS v0.5.1: Positioning module, Frameworks architecture, and module renumbering (13 modules total).

- `docs/m-and-a/05-positioning.md` — Module 05 fully realized: complete Philosophy, Process (5 steps: Buyer Universe Analysis, Investment Thesis Development, Strategic Fit Analysis, Risk Identification and Mitigation Framing, Positioning Brief), Standards, Common Failure Modes (6), AI Assistance, KPIs, and Lessons Learned. Introduces the Investment Thesis Construction Test (Specificity, Buyer, Defensibility, Goldman Sachs). Distinct from GTM: positioning is strategy, GTM is execution.
- - `docs/frameworks/README.md` — New folder: reusable mental models (frameworks) for Meritage advisory work. Documents the Meritage IP Pyramid: Beliefs → Frameworks → Standards → Methods → Templates → AI Prompts. Explains the distinction between frameworks (define thinking), standards (define expectations), and methods (define execution).
  - - `docs/frameworks/positioning-framework.md` — First Meritage Framework. Covers the Positioning Equation, the Buyer Lens Framework (Financial, Strategic, Owner-Operator, ESOP), the Investment Thesis Construction Test, the Risk Framing Principle, the Positioning-Valuation Relationship, and the Three Narratives (Internal, Teaser, CIM).
    - - Modules 06–13 (renumbered from 05–12): GTM, Buyer Outreach, IOIs, Management Calls, LOI, Due Diligence, Closing, Post-Close. Each updated with correct numbering, updated cross-references, and Lessons Learned section.
      -
      - ### Updated
      -
      - - `docs/m-and-a/04-valuation.md` — Added Lessons Learned section. Updated Related Documents to link to 05-positioning.md as next stage. Updated KPI for Seller alignment rate to reference positioning instead of GTM.
        - - `docs/m-and-a/README.md` — Updated to 13 modules. Added dependency chain diagram. Added Lessons Learned to module structure table. Updated module status table. Added Relationship to Frameworks section.
          - - `docs/INDEX.md` — Added Meritage Frameworks section. Updated The Meritage Method to 13 modules with Module 05 Positioning marked Complete.
            - - `docs/m-and-a/05-gtm.md` through `docs/m-and-a/12-post-close.md` — Replaced with redirect notices pointing to new numbered files (06-13). Archived per MOS archiving conventions.
              -
              - ---
              -
              - ## [0.5.0] – 2026-06-29

### Added

MOS v0.5: Operational Excellence — first fully realized module and cross-cutting standards architecture.

- `docs/m-and-a/04-valuation.md` — Module 04 fully realized: complete Philosophy, Process (5 steps), Standards, Common Failure Modes (7), AI Assistance, and KPIs. Meritage-specific content on financial normalization, comparable transaction analysis, value drivers and detractors, valuation range development, and Seller alignment. No generic investment banking language.
- - `docs/standards/README.md` — New folder: cross-cutting quality standards that apply across multiple engagement stages. Explains the distinction between standards (quality bar) and modules (process steps), what belongs here, and what is planned.
  - - `docs/standards/valuation-standard.md` — First Meritage Operating Standard. Defines the Completeness Standard (5 components), Accuracy Standard, Communication Standard, and Prohibited Representations for all valuation work. Status: Authoritative.
    -
    - ### Updated
    -
    - - `docs/m-and-a/README.md` — Reflects the hub module concept: each module links outward to philosophy, operating standard, process, and assets. Added Status column to module table. Added Relationship to Standards section.
      - - `docs/INDEX.md` — Added Meritage Operating Standards section. Added Status column to The Meritage Method table showing Module 04 as Complete.
        -
        - ---
        -
        - ## [0.4.0] — 2026-06-29

### Added

MOS v0.4: The Meritage Method — sell-side playbook architecture. All 13 files scaffolded with standard section headings. Process content pending module-by-module development.

- `docs/m-and-a/README.md` — The Meritage Method overview: what it is, why modules, module structure table, relationship to Domain Model
- - `docs/m-and-a/01-origination.md` — Origination module scaffold
  - - `docs/m-and-a/02-qualification.md` — Qualification module scaffold
    - - `docs/m-and-a/03-engagement.md` — Engagement module scaffold
      - - `docs/m-and-a/04-valuation.md` — Valuation module scaffold
        - - `docs/m-and-a/05-gtm.md` — Go-to-Market module scaffold
          - - `docs/m-and-a/06-buyer-outreach.md` — Buyer Outreach module scaffold
            - - `docs/m-and-a/07-indications-of-interest.md` — Indications of Interest module scaffold
              - - `docs/m-and-a/08-management-calls.md` — Management Calls module scaffold
                - - `docs/m-and-a/09-letter-of-intent.md` — Letter of Intent module scaffold
                  - - `docs/m-and-a/10-due-diligence.md` — Due Diligence module scaffold
                    - - `docs/m-and-a/11-closing.md` — Closing module scaffold
                      - - `docs/m-and-a/12-post-close.md` — Post-Close module scaffold
                       
                        - Each module contains: Purpose, Philosophy, Scope, Roles and Responsibilities, Inputs, Process (pending), Standards (pending), Common Failure Modes (pending), AI Assistance (can/cannot), KPIs (pending), Related Documents.
                       
                        - ### Updated
                       
                        - - `docs/INDEX.md` — Added The Meritage Method section with all 13 files
                         
                          - ---

                          ## [0.3.0] — 2026-06-29

                          ### Added / Replaced

                          - `docs/domain/README.md` — Domain Model folder index
                          - - `docs/domain/glossary.md` — 21+ terms; Authoritative / Pending Definition status
                            - - `docs/domain/business-entities.md` — 14 canonical entity definitions
                              - - `docs/domain/lifecycle.md` — 12-stage engagement lifecycle
                                - - `docs/domain/relationships.md` — Mermaid diagrams and relationship rules
                                  - - `docs/company/what-we-believe.md` — 10 Meritage beliefs
                                   
                                    - ---

                                    ## [0.2.1] — 2026-06-29

                                    ### Added

                                    - `docs/templates/document-template.md`
                                    - - `docs/decisions/adr-001-markdown-as-source-of-truth.md`
                                      - - `docs/INDEX.md`
                                       
                                        - ---

                                        ## [0.2.0] — 2026-06-29

                                        ### Added

                                        - `docs/company/company-overview.md`
                                        - - `docs/ai/claude-context.md`
                                          - - `docs/executive/executive-manual.md`
                                            - - `docs/operations/operating-principles.md`
                                              - - `docs/marketing/brand-voice.md`
                                               
                                                - ---

                                                ## [0.1.0] — 2026-06-29

                                                ### Added

                                                - Repository bootstrap: root files, 12 `docs/` subfolders, `assets/`, `archive/`
                                               
                                                - ---

                                                *Last updated: 2026-06-29*
