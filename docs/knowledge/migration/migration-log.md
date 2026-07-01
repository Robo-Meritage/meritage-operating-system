# Migration Log

**Classification:** Internal  
**Status:** Active  
**Last Updated:** 2026-07-01

---

## Purpose

This log records every ingestion batch in the knowledge migration from ChatGPT to the Meritage Operating System.

Update this log after every ingestion session.

---

## Log Entries

### Batch 1 — 2026-07-01

**Source:** Phase 1: Meritage Project (Jul → Jun 2026)  
**Conversations Processed:** 3 full reads; ~175 surveyed for corpus sizing  
**Ingested By:** Claude Sonnet 4.6

#### Records Created
| File | Category | Topic |
|---|---|---|
| `advisor-termination-clause-2026-07.md` | agreements/ | Skinner advisor agreement — Section 12 gap, termination clause, "For Cause" definition |
| `referral-partner-agreement-fresh-2026-06.md` | agreements/ | Fresh Strategic Alliance & Referral Agreement — 2% referral fee, COI waterfall |
| `value-creation-platform-2026-06.md` | operations/ | Three-document Value Creation sales process; Goodwin engagement; "diagnose first" principle |

#### Conflicts Flagged
- No referral partner program in MOS (Pending)
- - No Value Creation service line in MOS (Pending)
  - - Advisor agreement template may need Section 12 update (Pending)
   
    - ---

    ### Batch 2 — 2026-07-01

    **Source:** Phase 1: Meritage Project (Jun 2026)
    **Conversations Processed:** 3 full reads (Offer Letter for Nick; Engagement Agreement Comparison SPR; Agreement Cancellation Review Jessica Stahl)
    **Ingested By:** Claude Sonnet 4.6

    #### Records Created
    | File | Category | Topic |
    |---|---|---|
    | `contractor-onboarding-nick-pond-2026-07.md` | hr/ | Nick Pond contractor structure — $6k/month + 10% Empire Builder + 2.5% success fees; two-doc HR approach |
    | `spr-engagement-fee-negotiation-2026-06.md` | deal-analysis/ | SPR deal — Reverse Lehman vs Double Lehman comparison; three negotiation points; market fee ranges |
    | `advisor-onboarding-jessica-stahl-prior-agreement-2026-06.md` | hr/ | Jessica Stahl onboarding — prior RLB agreement termination protocol; four verification questions |

    #### Conflicts Flagged
    - No HR onboarding protocol for advisors with prior agreements (Pending)
    - - No documented fee schedule in MOS (Pending)
     
      - ---

      ### Batch 3 — 2026-07-01

      **Source:** Phase 1: Meritage Project (May 2026)
      **Conversations Processed:** 1 full read (Branch · Reverse Lehman Formula / K2D Consulting Engineers)
      **Ingested By:** Claude Sonnet 4.6

      #### Records Created
      | File | Category | Topic |
      |---|---|---|
      | `k2d-engagement-fee-negotiation-2026-05.md` | deal-analysis/ | K2D Consulting Engineers — Ascending Lehman vs Reverse Lehman; 4% cap at $1M; Approved Buyer List Schedule 2 language; when to stop negotiating |

      #### Conflicts Flagged
      - K2D Approved Buyer List Schedule 2 language should be added to standard engagement agreement template as a clause option (Pending)
     
      - ---

      ### Batch 4 — 2026-07-01

      **Source:** Phase 1: Meritage Project (Apr–May 2026)
      **Conversations Processed:** 2 full reads (Reverse Lehman Formula / K2D additional context; Fee Structure Options / Merlin Law Group buy-side)
      **Ingested By:** Claude Sonnet 4.6

      #### Records Created
      | File | Category | Topic |
      |---|---|---|
      | `reverse-lehman-fee-framework-2026-05.md` | agreements/ | Definitive Reverse Lehman buy-side fee schedule (5/4/3/2/1% by tier); buy-side engagement pricing; fee compression risk; NDA-triggered introduction standard |

      #### Records Updated (Deduplication)
      | Existing File | Action Taken |
      |---|---|
      | `k2d-engagement-fee-negotiation-2026-05.md` | Context from Reverse Lehman Formula conversation absorbed into fee framework record instead of duplicating K2D record |

      #### Conflicts Flagged
      | Conflict | Existing Document | Status |
      |---|---|---|
      | docs/m-and-a/03-engagement.md references fees but does not document the fee schedule | docs/m-and-a/03-engagement.md | HIGH PRIORITY — reverse-lehman-fee-framework-2026-05.md should be used to update Module 03 |
      | Sell-side Reverse Lehman exact tier breakpoints still not confirmed from source documents | None | Pending — need to find explicit sell-side schedule in additional conversations |

      #### Open Questions
      - What are the exact sell-side Reverse Lehman tier breakpoints? (Buy-side confirmed: 5/4/3/2/1% at $1M/$5M/$10M/$20M)
      - - Is there a standard minimum fee? What is the standard tail period?
        - - Merlin Law Group engagement: did they proceed with Option 2?
         
          - #### Notes
         
          - **Deduplication applied:** The K2D "Reverse Lehman Formula" conversation is a continuation of the same K2D deal as Batch 3. Content was synthesized into the fee framework record rather than creating a third K2D record.
         
          - **Highest-value discovery this session:** The Meritage buy-side Reverse Lehman fee schedule is now documented for the first time in the MOS. This was present only in client-facing emails and never captured in the repository. The NDA-triggered introduction standard is also a significant operational policy that belongs in the engagement module.
         
          - **Session status:** 9 conversations fully read. Repository now contains 8 structured knowledge records covering: agreements (3), deal-analysis (3), hr (2), operations (1). Migration is actively progressing.
         
          - ---

          ## Summary Statistics

          | Metric | Value |
          |---|---|
          | Total batches completed | 4 |
          | Total conversations processed (full read) | 9 |
          | Total conversations surveyed (corpus sizing) | ~175 |
          | Total records created | 8 |
          | Total records updated (deduplication) | 1 |
          | Total conflicts flagged | 9 |
          | Total conversations classified as Ignore | 0 |
          | Phase 1 status | In progress — 9 of ~175 processed |
          | Phase 2 status | Not started |

          ### Records by Category
          | Category | Count | Records |
          |---|---|---|
          | agreements/ | 3 | advisor-termination, fresh-referral, reverse-lehman-fee-framework |
          | deal-analysis/ | 3 | spr-fee-negotiation, k2d-fee-negotiation, [k2d-context absorbed] |
          | hr/ | 2 | nick-pond-contractor, jessica-stahl-onboarding |
          | operations/ | 1 | value-creation-platform |
          | applebites/ | 0 | Awaiting |
          | empire-builder/ | 0 | Awaiting |
          | gtm/ | 0 | Awaiting |
          | marketing/ | 0 | Awaiting |
          | transcripts/ | 0 | Awaiting |
          | weekly-calls/ | 0 | Awaiting |

          ### Top Priority Next Conversations
          1. M&A Firm vs Broker (Apr 9 2026) — Score 5 — Meritage positioning
          2. 2. Engagement Fee Structure (Apr 15 2026) — Score 5 — May contain sell-side Reverse Lehman tiers
             3. 3. Reverse Lehman Formula (Apr 21 2026) — Score 5 — Core formula rationale
                4. 4. AppleBites Pathway Breakdown (Apr 23 2026) — Score 5 — Product documentation
                   5. 5. Compensation Structure for Analysis (Feb 20 2026) — Score 5 — Internal comp framework
                      6. 6. M&A Firm Clarification (Mar 17 2026) — Score 5 — Meritage's full process documentation
                         7. 7. Subcontractor Agreements and IP (Mar 25 2026) — Score 5 — IP and contractor structure
                            8. 8. E&O Coverage Analysis (Feb 4 2026) — Score 5 — Insurance/liability
                              
                               9. ---
                              
                               10. ## Related Documents
                              
                               11. - [Migration README](./README.md)
                                   - - [Chat History README](../chat-history/README.md)
                                     - - [INGESTION-GUIDE.md](../chat-history/INGESTION-GUIDE.md)
                                      
                                       - ---

                                       ### Batch 5 — 2026-07-01

**Source:** Phase 1: Meritage Project (May–Jun 2026)
**Conversations Processed:** 5 full reads (Exhibit A Rewrite; AppleBites Pathway Breakdown; M&A Firm Clarification; Trial Structure Confirmation/DealJet; Lou's Term Sheet Review/Opus JV)
**Ingested By:** Claude Sonnet 4.6

#### Records Created/Updated

| File | Category | Topic |
|---|---|---|
| `reverse-lehman-fee-framework-2026-05.md` | agreements/ | **UPDATED** — Sell-side Reverse Lehman tiers confirmed (ascending 1/2/3/4/5%), flat threshold structure added, open questions resolved |
| `applebites/meritage-ecosystem-pathway-architecture-2026-04.md` | applebites/ | First AppleBites record — Three-pathway ecosystem (AppleBites/Empire Builder/Advisory), routing decision tree, exit readiness criteria |
| `emails/broker-to-broker-positioning-2026-03.md` | emails/ | Broker-to-broker positioning patterns; "force clarity first" email templates; M&A Firm Clarification session |
| `agreements/referral-partner-agreement-dealjet-2026-05.md` | agreements/ | DealJet trial structure (5 intros, 10% of fee, $3M EBITDA min, no upfront); 9-issue referral agreement review checklist |
| `agreements/opus-jv-referral-term-sheet-review-2026-05.md` | agreements/ | Opus/Lou JV framework (50/50 net, 18-month tail); 6 issues in Lou's referral term sheet rejected; "separate JV from referral" pattern |

#### Key Knowledge Milestones This Batch

- **Critical Gap Resolved:** Sell-side Reverse Lehman tier structure confirmed as ascending (1%/2%/3%/4%/5%) from explicit client-facing Exhibit A. This resolves the highest-priority open question from Batches 1–4.
- **First ApplebBites Record:** Three-pathway ecosystem fully documented for the first time in MOS.
- **Referral Rate Patterns:** 10% of Meritage fee (DealJet, affiliates standard), 2% of Gross Advisory Fees (Fresh), 40% of gross rejected (Opus). Flag for Daniel: is there a standard referral rate policy?
- **JV vs. Referral Distinction:** Established as separate structure types with different economics, accountability, and legal terms.

#### Conflicts Flagged

- Referral rate inconsistency: DealJet (10% of fee) vs. Fresh (2% of gross) vs. Opus rejected terms (40% gross). Needs reconciliation into standard policy. (Pending Daniel's review)
- 19-step exit roadmap quoted from competitor (MP Advisory website) — does Meritage have a published version? (Pending)
- Empire Builder membership details not documented — what does it cost, what does it include? (Pending)

    - ---

### Batch 6 — Priority Queue

**Highest Priority (Score 5):**
| Conversation | Topic | Action |
|---|---|---|
| "Compensation Structure for Analysis" (Feb 20, 2026) | Internal comp | Create |
| "Subcontractor Agreements and IP" (Mar 25, 2026) | IP and contractor structure | Create |
| "E&O Coverage Analysis" (Feb 4, 2026) | Insurance/liability | Create |
| "Response to Carter" (date TBD) | Deal negotiation | Review — may be deal-specific |
| "Schmidt Deal Pay Breakdown" (date TBD) | Deal-specific pay structure | Review |
| "GTM Call Follow-up" (Jun 15, 2026) | GTM patterns | Review |
| "Follow-up Call Prep" (Jun 17, 2026) | Deal prep patterns | Review |
| "Transcript Analysis and Prep" (Jun 24, 2026) | Call prep patterns | Review |
| "Due Diligence Preparation" (Jun 25, 2026) | DD process | Review |

**Medium Priority (Score 4):**
| Conversation | Topic | Action |
|---|---|---|
| "Deal Management Coaching" (Jun 12, 2026) | Deal management patterns | Review |
| "Redline JV Agreement" (date TBD) | JV redline patterns | Update agreements/ |
| "Email Rewrite Request" (May 12, 2026) | Email patterns | Update emails/ |
| "Lehman scale updates" (date TBD) | Lehman/AppleBites | Review |
| "CIM Comparison and Grading" (Jun 5, 2026) | CIM standards | Create |
| "AI Business Model" (Jun 5, 2026) | AI tools | Review |


*Part of the [Meritage Operating System](../../../README.md). See [CONTRIBUTING.md](../../../CONTRIBUTING.md) for standards.*
