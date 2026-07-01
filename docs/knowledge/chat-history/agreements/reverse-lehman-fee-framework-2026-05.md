# Meritage Reverse Lehman Fee Framework

**Source:** ChatGPT — Meritage Partners Project — Multiple conversations (Apr–Jun 2026): "Fee Structure Options" (May 1), "Engagement Agreement Comparison" (Jun 12), "Branch · Reverse Lehman Formula" (May 12)  
**Category:** agreements/  
**Classification:** Proprietary  
**Score:** 5 — New institutional knowledge (missing from MOS)  
**Entities:** Merlin Law Group (buy-side client), K2D Consulting Engineers (sell-side client), SPR/Kent (sell-side client)

---

## Critical Gap

The Meritage fee structure (Reverse Lehman) is repeatedly referenced throughout the repository but has never been fully documented. This record captures the authoritative fee schedule and all variations as they appear in actual client-facing documents.

---

## Meritage Standard Reverse Lehman — Sell-Side

Based on multiple conversations, Meritage's sell-side Reverse Lehman produces:
- ~4.44% effective fee on $18M deals
- - ~4.50% effective fee on $20M deals
  - - ~4.52% effective fee on $21M deals
   
    - The exact tier schedule has not been explicitly shown in conversations reviewed to date. The effective fee rates suggest a structure that starts at 5%+ on smaller amounts and decreases at higher tiers.
   
    - **Status:** Approximate effective rates confirmed. Exact tier breakpoints to be confirmed from additional conversation review.
   
    - ---

    ## Meritage Standard Reverse Lehman — Buy-Side (Confirmed)

    This schedule was explicitly shown in client-facing correspondence for the Merlin Law Group engagement (May 2026):

    | Tier | Rate |
    |---|---|
    | First $1,000,000 of transaction value | 5.0% |
    | Next $4,000,000 ($1M – $5M) | 4.0% |
    | Next $5,000,000 ($5M – $10M) | 3.0% |
    | Next $10,000,000 ($10M – $20M) | 2.0% |
    | All amounts above $20,000,000 | 1.0% |

    **Effective fee on a $10M buy-side transaction:** ~$300K (= 5% of $1M + 4% of $4M + 3% of $5M)

    ---

    ## Alternative Fee Structures Offered (Buy-Side Context)

    For the Merlin Law Group engagement, Meritage presented three options:

    ### Option 1: Full Buy-Side Mandate
    - Monthly: $6,500–$8,500/month
    - - Success fee: 3%–5% of purchase price
      - - Use case: Actively building pipeline in market
       
        - ### Option 2: Phased Mandate (Recommended)
        - - Phase 1 (Strategy & Initial Sourcing): $2,000/month, month-to-month
          - - Phase 2 (Full Mandate, triggered by specific opportunity): $5,000/month + Reverse Lehman success fee
            - - Use case: Group that wants to move into acquisition mode but isn't fully ready
             
              - ### Option 3: Success-Fee Dominant
              - - No ongoing monthly during sourcing
                - - $7,500 activation fee per deal pursued
                  - - 3.5%–4.5% success fee
                    - - Use case: Transactional; client only wants to engage when a deal is directly in front of them
                     
                      - **Why Option 2 is recommended:** "Its real purpose: removes their 'we don't want monthly' objection, nudges them toward Option 2."
                     
                      - ---

                      ## Non-Standard Structures Encountered

                      ### Double Lehman (SPR Client Request)
                      SPR's counsel changed Meritage's standard structure to Double Lehman. At a $20M deal this produced ~3.0% effective fee vs. ~4.5% under Reverse Lehman — a 30–35% reduction. Meritage rejected this.

                      ### Ascending Lehman (K2D Client Request)
                      K2D requested an ascending structure (1%→1%→2%→3%→4%→5%→6%), which favors larger deal sizes. Negotiated final: 4% top tier with $1M cap.

                      ---

                      ## Fee Compression Risk

                      A critical distinction emerged from K2D and SPR negotiations:

                      > "They didn't change your rate. They changed your base."
                      >
                      > Clients who cannot reduce the headline fee percentage often try to reduce realized fees by changing **what the fee applies to**:
                      > - Excluding earnouts until received
                      > - - Excluding rollover equity until liquidated
                      >   - - Excluding assumed debt from purchase price
                      >     - - Adding fee caps
                      >       - - Tightening "introduction" definitions
                      >        
                      >         - Meritage must track both: fee percentage AND fee base.
                      >        
                      >         - ---
                      >
                      > ## The "NDA-Triggered Introduction" Standard
                      >
                      > For any engagement with an Approved Buyer List or buyer attribution provisions, Meritage's position is:
                      >
                      > **A buyer is "introduced" once a confidentiality agreement (NDA) is executed with that party in connection with the process.**
                      >
                      > **Why:**
                      > - Removes subjectivity about what counts as an introduction
                      > - - Creates a clear, objective trigger
                      >   - - Creates an audit trail tied to executed NDAs
                      >     - - Prevents client from recharacterizing a relationship after the fact
                      >      
                      >       - This standard was developed in response to K2D's buyer list requirement and should be used in all future engagements that include any form of Approved Buyer List.
                      >      
                      >       - ---
                      >
                      > ## Patterns
                      >
                      > - Meritage always anchors to its standard Reverse Lehman structure in first drafts.
                      > - - Meritage does not volunteer alternative structures; it presents them as accommodations when client pushes back.
                      >   - - When a client insists on a non-standard structure, Meritage negotiates the economics (cap, top tier rate) rather than the structure itself.
                      >     - - The buy-side and sell-side fee schedules appear to be structurally similar but may have different tier breakpoints.
                      >       - - Option 2 (phased mandate) is consistently recommended as the "recommended" option in buy-side proposals because it is the most likely client choice and creates a clear path to Phase 2 economics.
                      >        
                      >         - ---
                      >
                      > ## Open Questions
                      >
                      > - What is the exact tier structure for the sell-side Reverse Lehman? (Confirm from additional conversation review.)
                      > - - Is the buy-side schedule (5/4/3/2/1%) the same as the sell-side, or are there different tier breakpoints?
                      >   - - Is there a standard minimum fee on Meritage engagements?
                      >     - - What is the standard tail period (the SPR conversation referenced 12 months from Effective Date; Meritage prefers termination/expiration)?
                      >      
                      >       - ---
                      >
                      > ## Conflicts to Flag
                      >
                      > - This is the most important missing document in the current MOS. The `docs/m-and-a/03-engagement.md` references fees but does not document the fee schedule. This record should be used to update Module 03.
                      > - - The `docs/m-and-a/04-valuation.md` should reference the fee structure as it affects how enterprise value and deal economics are presented to clients.
                      >  
                      >   - ---
                      >
                      > ## Links
                      >
                      > - [docs/knowledge/chat-history/deal-analysis/spr-engagement-fee-negotiation-2026-06.md](../deal-analysis/spr-engagement-fee-negotiation-2026-06.md) — SPR fee negotiation
                      > - - [docs/knowledge/chat-history/deal-analysis/k2d-engagement-fee-negotiation-2026-05.md](../deal-analysis/k2d-engagement-fee-negotiation-2026-05.md) — K2D fee negotiation
                      >   - - [docs/m-and-a/03-engagement.md](../../../m-and-a/03-engagement.md) — Engagement module (update needed)
                      >    
                      >     - ---
                      >
                      > *Part of the [Meritage Operating System](../../../../README.md). See [CONTRIBUTING.md](../../../../CONTRIBUTING.md) for standards.*
