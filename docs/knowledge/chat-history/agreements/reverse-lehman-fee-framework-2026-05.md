# Meritage Reverse Lehman Fee Framework

**Source:** ChatGPT — Meritage Partners Project — Multiple conversations (Apr–Jun 2026): "Fee Structure Options" (May 1), "Engagement Agreement Comparison" (Jun 12), "Branch · Reverse Lehman Formula" (May 12), "Exhibit A Rewrite" (~Apr 2026)
**Category:** agreements/
**Classification:** Proprietary
**Score:** 5 — New institutional knowledge (missing from MOS)
**Entities:** Merlin Law Group (buy-side client), K2D Consulting Engineers (sell-side client), SPR/Kent (sell-side client)

---

## Critical Gap (Resolved)

The Meritage fee structure (Reverse Lehman) is repeatedly referenced throughout the repository but had never been fully documented. This record now captures the authoritative fee schedule for both buy-side and sell-side, and all fee structure variations as they appear in actual client-facing documents.

---

## Meritage Standard Reverse Lehman — Sell-Side (CONFIRMED)

The sell-side Reverse Lehman was confirmed from a client-facing Exhibit A reviewed in the "Exhibit A Rewrite" conversation. The structure is **ascending** (increases with deal size):

| Tier | Rate |
|---|---|
| 1st $1,000,000 of Purchase Price | 1.0% |
| 2nd $1,000,000 | 2.0% |
| 3rd $1,000,000 | 3.0% |
| 4th $1,000,000 | 4.0% |
| All amounts above $4,000,000 | 5.0% |

**Why ascending sell-side:** The seller benefits from higher valuations at higher deal sizes. An ascending structure aligns Meritage incentives with maximizing transaction value — Meritage earns proportionally more as deal size increases.

**Effective rates (sell-side):**
- $18M deal: ~4.44% effective
- $20M deal: ~4.50% effective
- $21M deal: ~4.52% effective

**Status:** Confirmed from explicit client-facing Exhibit A language ("Exhibit A – Compensation and Payment, Section 2").

---

## Meritage Standard Reverse Lehman — Buy-Side (CONFIRMED)

The buy-side structure is **descending** (decreases with deal size), confirmed from the Merlin Law Group buy-side engagement (May 2026):

| Tier | Rate |
|---|---|
| First $1,000,000 of transaction value | 5.0% |
| Next $4,000,000 ($1M – $5M) | 4.0% |
| Next $5,000,000 ($5M – $10M) | 3.0% |
| Next $10,000,000 ($10M – $20M) | 2.0% |
| All amounts above $20,000,000 | 1.0% |

**Why descending buy-side:** Meritage charges more for smaller deals (more advisory intensity per dollar) and less for larger deals (scale benefit to buyer). Incentivizes closing over maximizing price.

Effective fee on a $10M buy-side transaction: ~$300K (= 5% x $1M + 4% x $4M + 3% x $5M)

---

## Alternative Sell-Side Fee Structures

### Flat Threshold Structure (Client-Specific)

For certain engagements, Meritage has used a non-tiered flat threshold model:

| Condition | Rate |
|---|---|
| Purchase Price <= $3,000,000 | 5.0% flat (applies to entire amount) |
| Purchase Price > $3,000,000 | 6.0% flat (applies to entire amount) |

**Key distinction:** The percentage applies to the **entire** Purchase Price, not incrementally.

**Trade-offs noted:**
- Simpler to communicate, sacrifices upside on larger deals
- Hard step at $3,000,001 creates potential negotiation friction
- No minimum fee = increased "tourist client" risk
- Typically paired with a $5,000 non-refundable engagement fee for alignment

### Engagement Fee + Success Fee Structure

For some sell-side engagements:
- $5,000 one-time, non-refundable engagement fee due at execution
- Success fee on the Reverse Lehman schedule (or flat threshold)

**Why:** Creates initial commitment from seller. Zero-upfront engagements increase probability of non-closing clients.

---

## Alternative Buy-Side Engagement Models

For the Merlin Law Group engagement, Meritage presented three buy-side engagement options:

**Option 1: Full Buy-Side Mandate**
- Monthly retainer: $6,500–$8,500/month
- Success fee: 3%–5% of purchase price
- Use case: Actively building acquisition pipeline in market

**Option 2: Phased Mandate (Recommended)**
- Phase 1 (Strategy & Initial Sourcing): $2,000/month, month-to-month
- Phase 2 (Full Mandate, triggered by specific opportunity): $5,000/month + Reverse Lehman success fee
- Why recommended: Removes "we don't want monthly" objection; creates clear path to Phase 2 economics.

**Option 3: Success-Fee Dominant**
- No ongoing monthly during sourcing
- $7,500 activation fee per deal pursued
- 3.5%–4.5% success fee
- Use case: Transactional; client only wants to engage when a deal is directly in front of them

---

## Non-Standard Structures Encountered

### Double Lehman (SPR Client Request)

SPR's counsel changed Meritage's standard structure to Double Lehman. At a $20M deal this produced ~3.0% effective fee vs. ~4.5% under Reverse Lehman — a 30–35% reduction. Meritage rejected this.

### Ascending Lehman (K2D Client Request)

K2D requested an ascending structure (1%/1%/2%/3%/4%/5%/6%), which favors larger deal sizes. Negotiated final: 4% top tier with $1M cap.

---

## Fee Compression Risk

**"They didn't change your rate. They changed your base."**

Clients who cannot reduce the headline fee percentage often try to reduce realized fees by changing what the fee applies to:
- Excluding earnouts until received
- Excluding rollover equity until liquidated
- Excluding assumed debt from purchase price
- Adding fee caps
- Tightening "introduction" definitions

Meritage must track both: fee percentage AND fee base.

### Purchase Price / Aggregate Consideration — Standard Definition

From the confirmed Exhibit A language, the standard Meritage definition includes:

**(a) Cash Consideration** — All cash paid to Seller at closing

**(b) Non-Cash Consideration** — Fair market value of any non-cash consideration (securities, assets), as mutually agreed in writing prior to or at closing

**(c) Rollover Equity** — Any equity interest retained or rolled over by Seller, included at agreed fair market value at closing

**(d) Deferred or Contingent Consideration** — Earnouts, seller notes, deferred payments EXCLUDED from Purchase Price at closing; included only when actually received by Seller in cash

**(e) Indebtedness Assumed by Buyer** — Third-party indebtedness expressly assumed by Buyer at closing, INCLUDED in Purchase Price

**Excluded from indebtedness:** Ordinary-course accounts payable; debt repaid from Company cash at closing; intercompany obligations

---

## The "NDA-Triggered Introduction" Standard

A buyer is "introduced" once a confidentiality agreement (NDA) is executed with that party in connection with the process.

**Why:** Removes subjectivity, creates objective trigger, audit trail tied to NDAs, prevents client from recharacterizing relationships after the fact.

Developed in response to K2D's buyer list requirement. Should be used in all future engagements with any Approved Buyer List.

---

## Patterns

- Meritage always anchors to its standard Reverse Lehman structure in first drafts.
- Meritage does not volunteer alternative structures; it presents them as accommodations when clients push back.
- When a client insists on a non-standard structure, Meritage negotiates economics (cap, top tier rate) rather than the structure itself.
- Sell-side Reverse Lehman is ascending (1/2/3/4/5%); buy-side Reverse Lehman is descending (5/4/3/2/1%). Both are called "Reverse Lehman."
- Option 2 (phased mandate) is consistently recommended in buy-side proposals.

## Open Questions

- Is there a standard minimum fee on Meritage engagements?
- What is the standard tail period? (SPR referenced 12 months from Effective Date; Meritage prefers termination/expiration date language)
- Tier breakpoint discrepancy: sell-side tiers are $1M increments up to $4M; buy-side tiers have wider bands ($5M, $10M, $20M). This may reflect different typical deal size ranges.

## Conflicts to Flag

- docs/m-and-a/03-engagement.md references fees but does not document the fee schedule. This record should be used to update Module 03.
- **RESOLVED (Jul 2026):** Sell-side exact tier breakpoints confirmed from Exhibit A Rewrite conversation.

## Links

- docs/knowledge/chat-history/deal-analysis/spr-engagement-fee-negotiation-2026-06.md
- docs/knowledge/chat-history/deal-analysis/k2d-engagement-fee-negotiation-2026-05.md
- docs/m-and-a/03-engagement.md — Engagement module (update needed)

---

*Part of the Meritage Operating System. See CONTRIBUTING.md for standards.*
