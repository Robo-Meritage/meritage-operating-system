# Entity Relationships

> How the major Meritage business entities relate to one another. This document provides conceptual understanding, not operational instruction.
>
> ---
>
> ## Overview
>
> This document maps the relationships between the entities defined in [`business-entities.md`](business-entities.md). It answers the question: given any entity, what does it connect to and how?
>
> Two primary relationship flows govern most of what Meritage does:
>
> 1. **The origination flow** — how a Referral Partner or Affiliate introduction becomes a Client and then an Engagement
> 2. 2. **The deal flow** — how a Seller and an Opportunity progress through the transaction lifecycle to Close
>   
>    3. ---
>   
>    4. ## Origination Flow
>   
>    5. This diagram shows how a new client relationship originates through a Referral Partner or Affiliate.
>
>    6. ```mermaid
>       graph TD
>           A[Referral Partner / Affiliate] -->|Qualified Introduction| B[Opportunity]
>           B -->|Engagement Agreement Signed| C[Client]
>           C -->|Sell-Side| D[Engagement]
>           D -->|Deal Opened| E[Deal]
>       ```
>
> **Narrative**
>
> A Referral Partner or Affiliate makes a Qualified Introduction — a formal written notice that introduces a potential client to Meritage under the terms of a signed agreement. That introduction creates an Opportunity in the Meritage pipeline.
>
> If Meritage qualifies the Opportunity and both parties agree to proceed, an Engagement Agreement is signed and the referred party becomes a Client. The Engagement is then opened, and the Client's transaction becomes an active Deal.
>
> ---
>
> ## Deal Flow
>
> This diagram shows how a Seller and their Company move through the transaction process toward Close.
>
> ```mermaid
> graph TD
>     A[Seller] -->|Owns| B[Company / Opportunity]
>     B -->|Engagement Signed| C[Engagement]
>     C -->|GTM + Buyer Outreach| D[Buyer]
>     D -->|Signs NDA, Receives CIM| E[Management Call]
>     E -->|Buyer Submits| F[IOI]
>     F -->|Seller Selects Buyer| G[LOI]
>     G -->|Triggers| H[Due Diligence]
>     H -->|Completed| I[Closing]
> ```
>
> **Narrative**
>
> The Seller owns a Company and enters the Meritage process as an Opportunity. Once an Engagement Agreement is signed, Meritage prepares deal materials and takes the Company to market (GTM). Qualified Buyers sign NDAs, receive the CIM, and participate in Management Calls.
>
> Interested Buyers submit IOIs. Meritage and the Seller evaluate the IOIs and select a preferred Buyer to negotiate a LOI with. LOI execution triggers the Due Diligence period. Successful due diligence leads to Closing.
>
> ---
>
> ## Key Relationship Rules
>
> These rules are invariants — they must be true in any valid Meritage Deal.
>
> | Rule | Description |
> |---|---|
> | One Principal Advisor per Engagement | An Engagement cannot have two Principal Advisors. Ownership is singular. |
> | NDA before CIM | A Buyer cannot receive a CIM without first signing an NDA. |
> | Engagement Agreement before work begins | No advisory work is performed without a signed Engagement Agreement. |
> | Affiliate Agreement before Qualified Introduction | An introduction is not a Qualified Introduction unless a signed agreement was in place at the time. |
> | One active LOI at a time | Once a LOI is signed, the Seller grants exclusivity. No parallel LOI negotiations. |
> | Close triggers Success Fee | The Success Fee is calculated at Close per the Engagement Agreement. |
> | Revenue Share requires a Qualified Introduction | Meritage does not pay Revenue Share without a written introduction notice that meets the agreement criteria. |
>
> ---
>
> ## Referral and Affiliate Relationship
>
> The Referral Partner and Affiliate entities overlap significantly. Both refer clients to Meritage and both earn Revenue Share. The distinction, where it exists, is in the specific agreement type in use. The executed agreement governs in all cases.
>
> ```mermaid
> graph LR
>     A[Referral Partner] -->|Signed Agreement| B[Meritage]
>     C[Affiliate] -->|Signed Agreement| B
>     B -->|Qualified Introduction Confirmed + Close| D[Revenue Share]
>     D --> A
>     D --> C
> ```
>
> ---
>
> ## Advisor Relationships
>
> The Advisor entity encompasses both Principal Advisors and Strategic Growth Advisors. A Principal Advisor owns the Engagement; a Strategic Growth Advisor supports it.
>
> ```mermaid
> graph TD
>     A[COO] -->|Assigns| B[Principal Advisor]
>     B -->|Owns| C[Engagement]
>     D[Strategic Growth Advisor] -->|Supports| C
>     C -->|Serves| E[Client]
> ```
>
> ---
>
> ## Related Documents
>
> - [`business-entities.md`](business-entities.md) — Full entity definitions
> - - [`glossary.md`](glossary.md) — Term definitions
>   - - [`lifecycle.md`](lifecycle.md) — Engagement lifecycle stages
>     - - `docs/m-and-a/` — Operational process documentation (pending)
>      
>       - ---
>
> *Last updated: 2026-06-29*
