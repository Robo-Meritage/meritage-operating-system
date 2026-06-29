# Changelog

All notable changes to the Meritage Operating System are documented here.

This project follows [Keep a Changelog](https://keepachangelog.com/en/1.0.0/) format.

---

## [0.3.0] — 2026-06-29

### Added / Replaced

MOS v0.3: Domain Model — the canonical business language for Meritage Partners. All five domain files were written to spec, replacing earlier drafts.

- `docs/domain/README.md` — Purpose of the Domain Model; why operational documents should reference definitions here rather than redefine terms inline
- - `docs/domain/glossary.md` — Alphabetical glossary of 21+ terms; each marked Authoritative or Pending Definition; includes AppleBites, Empire Builder, and GTM as Pending Definition terms
  - - `docs/domain/business-entities.md` — 14 canonical entity definitions (Company, Client, Seller, Buyer, Opportunity, Deal, Advisor, Principal Advisor, Referral Partner, Affiliate, Engagement, CIM, Management Call, Due Diligence); each with Purpose, Owner, Relationships, Lifecycle Status, and Related Documents
    - - `docs/domain/lifecycle.md` — 12-stage sell-side engagement lifecycle (Lead → Qualification → Engagement → GTM → Buyer Outreach → IOIs → LOIs → Management Calls → Due Diligence → Closing → Post-Close → Earnout Monitoring); each stage described in 1–2 paragraphs; Earnout Monitoring marked Pending Definition
      - - `docs/domain/relationships.md` — Four Mermaid diagrams (Origination Flow, Deal Flow, Referral/Affiliate, Advisor Relationships); key relationship rules table; narrative explanations for each diagram
       
        - ### Updated
       
        - - `docs/INDEX.md` — Domain Model section updated to reflect spec-compliant file descriptions
         
          - ---

          ## [0.2.1] — 2026-06-29

          ### Added

          - `docs/templates/document-template.md` — Reusable blank template for all new MOS documents
          - - `docs/decisions/adr-001-markdown-as-source-of-truth.md` — ADR documenting the decision to use Markdown as the source of truth for all MOS content
            - - `docs/INDEX.md` — Master navigation page listing every substantive document in the repository
             
              - ---

              ## [0.2.0] — 2026-06-29

              ### Added

              - `docs/company/company-overview.md` — Full company overview
              - - `docs/ai/claude-context.md` — Comprehensive AI context document
                - - `docs/executive/executive-manual.md` — COO operating playbook
                  - - `docs/operations/operating-principles.md` — Ten core operating principles
                    - - `docs/marketing/brand-voice.md` — Brand voice guide
                     
                      - ---

                      ## [0.1.0] — 2026-06-29

                      ### Added

                      - `README.md` — Repository overview, structure map, naming conventions, and getting started guide
                      - - `CLAUDE.md` — Short-form AI context file
                        - - `AGENTS.md` — Agent roster for Claude and GitHub Copilot
                          - - `CHANGELOG.md` — This file
                            - - `CONTRIBUTING.md` — Contribution guide
                              - - `.gitignore` — Excludes OS files, editor artifacts, proprietary formats, secrets
                                - - All 12 `docs/` subfolder `README.md` index files
                                  - - All 3 `assets/` subfolder `README.md` index files
                                    - - `archive/README.md`
                                     
                                      - ---

                                      *Last updated: 2026-06-29*
