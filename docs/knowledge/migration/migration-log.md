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


### Batch 6 — 2026-07-01

**Source:** Phase 1: Meritage Project (Feb–Jun 2026)
**Conversations Processed:** 4 full reads (Response to Compensation Proposal/Jeanne Cummings; Subcontractor Agreements and IP; E&O Coverage Analysis/Scott Stepanik; GTM Call Follow-up/PlanNet)
**Ingested By:** Claude Sonnet 4.6

#### Records Created

| File | Category | Topic |
|---|---|---|
| `hr/deal-principal-compensation-structure-2026-02.md` | hr/ | **Highest Priority** — Deal principal comp model confirmed: 15% of 60% net per deal; 40% house overhead; flat universal %; no base salary; Empire Builder $3,500/month |
| `agreements/subcontractor-ip-protection-2026-03.md` | agreements/ | IP protection strategy: 3 protected assets (Meritage, Empire Builder, AppleBites); $5M pre-set IP value; attorney Helen follow-up |
| `hr/eo-coverage-scott-stepanik-litigation-2026-02.md` | hr/ | **Sensitive** — Scott Stepanik lawsuit; biBERK E&O does not cover; 4 coverage barriers; Schmidt deal only $750K; litigation strategy |
| `deal-analysis/plannet-engagement-fee-negotiation-2026-06.md` | deal-analysis/ | PlanNet (Andrew Harrod) engagement; non-standard 8/7/6/5/4% fee schedule; 3 firm positions (no carve-out, no discount, paid when paid) |

#### Key Knowledge Milestones This Batch

- **Internal Compensation Model Fully Documented:** Deal principals earn 15% of 60% net (after 40% house overhead). No base salary. Flat universal % for support staff. This is the first full record of Meritage's compensation architecture.
- **Active Litigation Documented:** Scott Stepanik lawsuit (former contractor, Austrian citizen) against Meritage and Brian Franco personally. E&O does not cover. Defense will be out-of-pocket or via EPLI if it exists.
- **IP Asset List Confirmed:** Meritage Partners, Empire Builder, AppleBites — all three identified as protected IP assets with $5M pre-set damages approach.

#### Conflicts Flagged

- **HIGH PRIORITY — Fee Structure Conflict:** PlanNet engagement uses 8/7/6/5/4% descending sell-side structure, conflicting with standard ascending 1/2/3/4/5% documented in Batch 5. Daniel must clarify which is standard and when each applies. (Pending)
- **Scott Stepanik Litigation Status:** Unknown as of mid-2026. EPLI policy existence unconfirmed. (Pending)
- **Empire Builder Pricing:** Confirmed at $3,500/month by Daniel, who considers it under-priced. (Pending pricing decision)

    - ---

### Batch 7 — Priority Queue

**Highest Priority (Score 5):**
| Conversation | Topic | Action |
|---|---|---|
| "Transcript Analysis and Prep" (Jun 24, 2026) | Call prep / transcript patterns | Review — may be transcripts/ |
| "Due Diligence Preparation" (Jun 25, 2026) | DD process documentation | Review |
| "CIM Comparison and Grading" (Jun 5, 2026) | CIM standards and grading | Create |
| "Response to Carter" (date TBD) | Deal negotiation patterns | Review |
| "Schmidt Deal Pay Breakdown" (date TBD) | Deal-specific (Schmidt $750K) | Review — connects to litigation |
| "Follow-up Call Prep" (Jun 17, 2026) | Deal/call prep | Review |
| "Quarterly Review Summary" (date TBD) | Company performance review | Review |

**Medium Priority (Score 4):**
| Conversation | Topic | Action |
|---|---|---|
| "Deal Management Coaching" (Jun 12, 2026) | Deal management patterns | Review |
| "Redline JV Agreement" (date TBD) | JV redline patterns | Update agreements/ |
| "Employee vs Contractor Classification" (date TBD) | Contractor classification rules | Review |
| "CIM Questionnaire for Clarity" (date TBD) | CIM process | Review |
| "New Hire Onboarding Review" (date TBD) | Onboarding patterns | Review — update hr/ |
| "Calculate adjusted EBITDA" (date TBD) | EBITDA methodology | Review |


*Part of the [Meritage Operating System](../../../README.md). See [CONTRIBUTING.md](../../../CONTRIBUTING.md) for standards.*

---

### Batch 7 — 2026-07-01

**Source:** Phase 1: Meritage Project (May–Jul 2026)
**Conversations Processed:** 8 full reads (Transcript Analysis and Prep; Due Diligence Preparation/Gavnat; CIM Comparison and Grading; Follow-up Call Prep/Ganesh; GTM Call Follow-up/PlanNet; Engagement Agreement Comparison/SPR; Deal Management Coaching/Skinner; Agreement Cancellation Review/Stahl; Strategic Referral Partner Agreement/Fresh; Agreement Termination Clause/Skinner)
**Ingested By:** Claude Sonnet 4.6
**Note:** Session interrupted by computer crash after 3 records committed. Migration log completed in resumed session.

#### Records Created

| File | Category | Topic |
|------|----------|-------|
| `deal-readiness-assessment-framework-2026-06.md` | deal-analysis/ | Three-Tier Deal Readiness Model (pre-Brian intro gate); Gree HVAC transcript analysis |
| `gavnat-acquisition-dd-management-2026-05.md` | deal-analysis/ | Gavnat acquisition due diligence management; DD room structure |
| `cim-creation-standard-2026-06.md` | operations/ | CIM grading criteria; CIM creation standards; what makes a CIM investable |
| `deal-pipeline-management-patterns-2026-06.md` | operations/ | Deal pipeline management model; buyer objection reframing; offer approval gates; buyer list accountability; Empire Builder feeder strategy |

#### Records Reviewed — No New File Required (deduplicated to existing records)

| Conversation | Disposition |
|-------------|-------------|
| Follow-up Call Prep (Ganesh — Jun 17) | Score 3 — Operational/vendor pattern. Ganesh EBITDA review vendor structure captured as decision context only. No net new institutional knowledge above existing operations docs. |
| GTM Call Follow-up (PlanNet — Jun 15) | Score 2 — Confirms PlanNet email handling patterns already in `plannet-engagement-fee-negotiation-2026-06.md`. No new content. |
| Engagement Agreement Comparison (SPR — Jun 12) | Score 3 — SPR Double Lehman vs. Reverse Lehman for $18-21M deal. Confirms fee framework. Small additions could go to spr-engagement-fee-negotiation but core knowledge already captured. Deduplication applied. |
| Agreement Cancellation Review (Stahl — Jun 8) | Score 3 — Confirms termination protocol already in `advisor-onboarding-jessica-stahl-prior-agreement-2026-06.md`. Adds "within 12 months" clarification; existing record is comprehensive. Deduplication applied. |
| Strategic Referral Partner Agreement (Fresh — Jun 26) | Score 3 — Full agreement text now in `referral-partner-agreement-fresh-2026-06.md`. COI waterfall already captured from prior Batch 5 record. Deduplication applied. |
| Agreement Termination Clause (Skinner — Jul 1) | Score 4 — Skinner agreement full text and Section 12 gap analysis. Advisor compensation structure (50% company overhead / 50% distributable pool / 4% advisor / 18% principal advisor) confirms Batch 6 comp model. Termination clause improvements documented in `advisor-termination-clause-2026-07.md` (existing record already captured this). |

#### Key Knowledge Milestones This Batch

- **Deal Readiness Model:** Three-tier gate system before Brian/family office introduction is now documented for the first time in MOS.
- **CIM Standards:** CIM grading criteria and quality standards documented.
- **Deal Pipeline Patterns:** Formal operational patterns for pipeline management, buyer list accountability, Empire Builder feeder, and offer approval gates are now captured.
- **Advisor Comp Confirmation:** 50% company / 50% distributable pool / 4% advisor / 18% principal advisor confirmed across two separate conversations.

#### Conflicts Flagged

| Conflict | Status |
|---------|--------|
| Ganesh EBITDA vendor relationship — build vs. buy decision pending | Pending Daniel's review |
| Buyer list SLA — no documented standard for completion timing | Pending |
| Empire Builder routing criteria — EBITDA threshold for redirect vs. M&A not defined | Pending |
| Advisor termination Section 12 gap — "For Cause" definition missing from standard agreement | Pending — flag for Helen (attorney) |
| SPR fee negotiation outcome — did they proceed on Reverse Lehman or Double Lehman? | Pending — deal status unknown |

#### Conversations Classified as Score 1-2 (No Repository Action)

- GTM Call Follow-up (PlanNet email thread) — Score 2
- Follow-up Call Prep (Ganesh vendor discussion) — Score 3 (no new file)

---

## Summary Statistics

| Metric | Value |
|--------|-------|
| Total batches completed | 7 |
| Total conversations processed (full read) | ~25 |
| Total conversations surveyed (corpus sizing) | ~175 |
| Total records created | 12 |
| Total records updated (deduplication) | 4 |
| Total conflicts flagged | 15+ |
| Total conversations classified as Ignore | 0 |
| Phase 1 status | In progress — ~25 of ~175 processed |
| Phase 2 status | Not started |

---

## Batch 8 — Priority Queue

### Highest Priority (Score 5):

| Conversation | Topic | Action |
|-------------|-------|--------|
| "Exporting Project Data" (Jul 1, 2026) | Migration setup | Review — may be meta |
| "Offer Letter for Nick" (Jun 24, 2026) | Nick Pond contractor agreement | Review — update hr/ |
| "Response to Carter" (date TBD) | Deal negotiation patterns | Review |
| "Schmidt Deal Pay Breakdown" (date TBD) | Deal-specific (Schmidt $750K) | Review — connects to litigation |
| "Quarterly Review Summary" (date TBD) | Company performance review | Review |

### Medium Priority (Score 4):

| Conversation | Topic | Action |
|-------------|-------|--------|
| "Redline JV Agreement" (date TBD) | JV redline patterns | Update agreements/ |
| "Employee vs Contractor Classification" (date TBD) | Contractor classification rules | Review |
| "New Hire Onboarding Review" (date TBD) | Onboarding patterns | Update hr/ |
| "Calculate adjusted EBITDA" (date TBD) | EBITDA methodology | Review |
| "Post for Jack Hanks Classes" (Jun 4) | GTM/marketing patterns | Review |
| "Meritage M&A Advisor Perspective" (Jun 4) | Positioning language | Update marketing/ |
| "Filling out payroll details" (May 29) | Payroll/HR policy | Review |
| "Email Notification Draft" (May 27) | Email templates | Update marketing/ |
| "Management Call Prep Outline" (Jun 1) | Deal management | Update operations/ |

---

*Part of the Meritage Operating System. See CONTRIBUTING.md for standards.*
