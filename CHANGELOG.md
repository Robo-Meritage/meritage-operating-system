# Changelog

All notable changes to the Meritage Operating System are documented here.

This project follows [Keep a Changelog](https://keepachangelog.com/en/1.0.0/) format.

---

## [0.5.1] – 2026-06-29

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
