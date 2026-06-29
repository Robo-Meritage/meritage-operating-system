# Entity Relationships

> How the entities in the Meritage domain model connect to each other.
>
> ---
>
> ## Overview
>
> This document maps the relationships between the entities defined in [`business-entities.md`](business-entities.md). It answers the question: given any entity, what other entities does it connect to, and how?
>
> Relationship notation used in this document:
> - `A → B` means A has a relationship to B (A is the subject)
> - - `one` / `many` describes cardinality
>   - - `[required]` means the relationship must exist; `[optional]` means it may not
>    
>     - ---
>
> ## Core Relationship Map
>
> ```
>                     AFFILIATE
>                         |
>               Qualified Introduction
>                         |
>                     OPPORTUNITY
>                         |
>               Engagement Agreement
>                         |
>                    ENGAGEMENT
>                    /         \
>           SELLER             BUYER(S)
>               |                  |
>            COMPANY             NDA(s)
>               |                  |
>              CIM ---------- Distributed to
>               |                  |
>         VALUATION          MANAGEMENT CALL
>                                  |
>                               IOI(s)
>                                  |
>                                LOI
>                                  |
>                           DUE DILIGENCE
>                                  |
>                               CLOSE
>                              /      \
>                      SUCCESS FEE   REVENUE SHARE
>                                         |
>                                     AFFILIATE
> ```
>
> ---
>
> ## Relationship Tables
>
> ### People and Organizations
>
> | Entity | Relates To | Cardinality | Required? | Notes |
> |---|---|---|---|---|
> | **Seller** | Company | one-to-one | Required | A Seller owns one Company per engagement |
> | **Seller** | Engagement Agreement | one-to-one | Required | Governs the advisory relationship |
> | **Seller** | Principal Advisor | many-to-one | Required | One PA owns the Seller relationship |
> | **Buyer** | NDA | one-to-one | Required | Must sign NDA before receiving CIM |
> | **Buyer** | CIM | many-to-one | Required | One CIM distributed to many Buyers |
> | **Buyer** | Management Call | one-to-one | Optional | Not all Buyers advance to Management Call |
> | **Buyer** | IOI | one-to-one | Optional | Not all Buyers submit an IOI |
> | **Buyer** | LOI | one-to-one | Optional | At most one Buyer executes the LOI |
> | **Affiliate** | Qualified Introduction | one-to-many | Optional | An Affiliate may make multiple introductions |
> | **Affiliate** | Affiliate Agreement | one-to-one | Required | Must have a signed agreement to be an Affiliate |
> | **Affiliate** | Revenue Share | one-to-many | Optional | Earned only if introduction results in a Close |
> | **Principal Advisor** | Engagement | one-to-many | Required | One PA may own multiple Engagements |
> | **Strategic Growth Advisor** | Engagement | many-to-many | Optional | An SGA may support multiple Engagements |
>
> ---
>
> ### Deals and Documents
>
> | Entity | Relates To | Cardinality | Required? | Notes |
> |---|---|---|---|---|
> | **Engagement** | Company | one-to-one | Required | One Engagement per Company per process |
> | **Engagement** | Seller | one-to-one | Required | One Seller per sell-side Engagement |
> | **Engagement** | Principal Advisor | many-to-one | Required | One PA per Engagement |
> | **Engagement** | Engagement Agreement | one-to-one | Required | Agreement must be signed to open Engagement |
> | **Company** | CIM | one-to-one | Required | One CIM per Company per process |
> | **Company** | Valuation | one-to-many | Optional | May have multiple Valuations over time |
> | **Company** | Buyers | one-to-many | Optional | Multiple Buyers may pursue one Company |
> | **Deal** | Lifecycle Stage | one-to-one | Required | Every Deal has exactly one current stage |
> | **Deal** | Affiliate | many-to-one | Optional | A Deal may or may not have an Affiliate source |
> | **LOI** | Due Diligence | one-to-one | Required | LOI execution triggers Due Diligence |
> | **Close** | Success Fee | one-to-one | Required | Every Close generates a Success Fee |
> | **Close** | Revenue Share | one-to-one | Optional | Only if a Qualified Introduction exists |
>
> ---
>
> ## Key Constraints
>
> These constraints are invariants: they must always be true in a valid Deal.
>
> 1. **One Principal Advisor per Engagement.** An Engagement cannot have two Principal Advisors. Ownership is singular.
>
> 2. 2. **NDA before CIM.** A Buyer cannot receive a CIM without first signing an NDA. No exceptions.
>   
>    3. 3. **Engagement Agreement before work begins.** No advisory work is performed without a signed Engagement Agreement. Verbal agreements do not constitute engagements.
>      
>       4. 4. **Affiliate Agreement before Qualified Introduction.** An introduction cannot be a Qualified Introduction unless the Affiliate had a signed agreement at the time of the introduction.
>         
>          5. 5. **One active LOI at a time.** A Seller may negotiate with multiple Buyers through IOI stage, but once an LOI is signed, it grants exclusivity. No parallel LOI negotiations.
>            
>             6. 6. **Close triggers Success Fee.** The Success Fee is calculated at Close and cannot be waived without a written amendment to the Engagement Agreement.
>               
>                7. 7. **Revenue Share requires a confirmed Qualified Introduction.** Meritage does not pay Revenue Share without a written introduction notice and confirmation that the introduction meets the criteria in the Affiliate Agreement.
>                  
>                   8. ---
>                  
>                   9. ## Relationship Lifecycle Intersections
>                  
>                   10. Some relationships only exist at specific lifecycle stages:
>
> | Relationship | First appears at stage | Ends at stage |
> |---|---|---|
> | Seller ↔ Principal Advisor | Engagement (4) | Post-Close |
> | Company ↔ Buyer | Market (6) | Close (11) or Buyer Withdrawn |
> | NDA | Market (6) | Expires per terms |
> | CIM distribution | Market (6) | Close (11) or Withdrawn |
> | Management Call | Management Calls (7) | Completed (one-time event) |
> | IOI | IOI Review (8) | Accepted, declined, or superseded |
> | LOI | LOI Negotiation (9) | Executed, expired, or terminated |
> | Due Diligence | Due Diligence (10) | Complete or terminated |
> | Success Fee | Close (11) | Paid |
> | Revenue Share | Close (11) | Paid |
>
> ---
>
> ## Related Documents
>
> - [`business-entities.md`](business-entities.md) — Full entity definitions
> - - [`glossary.md`](glossary.md) — Term definitions
>   - - [`lifecycle.md`](lifecycle.md) — Lifecycle stage definitions
>     - - `docs/m-and-a/` — Process documentation
>       - - `docs/legal/` — Contract templates
>        
>         - ---
>
> *Last updated: 2026-06-29*
