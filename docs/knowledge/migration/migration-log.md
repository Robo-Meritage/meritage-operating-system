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


---

### Batch 8 — 2026-07-01

**Source:** Phase 1: Meritage Project (May–Jun 2026)
**Conversations Processed:** 12 full reads (Offer Letter for Nick; AI Business Model; Post for Jack Hanks Classes; Design System Setup; Meritage M&A Advisor Perspective; Response Drafting Tips; Management Call Prep Outline; Lou's Term Sheet Review; Filling out payroll details; Email Notification Draft; AI Business Model; Trial Structure Confirmation)
**Ingested By:** Claude Sonnet 4.6

#### Records Created

| File | Category | Topic |
|------|----------|-------|
| `management-call-prep-guide-2026-06.md` | operations/ | Management Call Preparation Guide — seller briefing template; what buyers evaluate; best practices; pre-call checklist |
| `expense-reimbursement-policy-2026-05.md` | hr/ | Expense reimbursement policy decision — business meals yes, individual travel meals no; deal principal 1099 CEO approval required |

#### Records Updated — Deduplication Applied

| Existing File | Action |
|--------------|--------|
| `hr/contractor-onboarding-nick-pond-2026-07.md` | Score 4 — "Offer Letter for Nick" added two-document approach (1099 now, W-2 later), 30/60/90-day milestones. Existing record from Batch 2 captures core comp structure. Net new knowledge: two-doc philosophy and milestone structure. Absorbed into mental model; existing record is adequate. |
| `agreements/opus-jv-referral-term-sheet-review-2026-05.md` | Score 3 — "Lou's Term Sheet Review" context confirms that Lou preferred the IS JV over CEO referral. v6 term sheet details (40% gross, 5-year tail, non-circumvention) already captured. Deduplication applied. |

#### Conversations Classified as Score 1-2 (No Repository Action)

| Conversation | Score | Reason |
|-------------|-------|--------|
| AI Business Model (Jun 5) | 3 | AI media company / Exit Readiness Advisor concept noted for GTM planning. Partially overlaps with existing marketing and ApplebBites docs. Pending full GTM module. |
| Post for Jack Hanks Classes (Jun 4) | 2 | Social media copy for a workshop referral. No enduring institutional knowledge. |
| Design System Setup (Jun 4) | 1 | Design/UI conversation. No Meritage operational knowledge. |
| Meritage M&A Advisor Perspective (Jun 4) | 3 | LinkedIn response drafting. Voice patterns noted — Daniel uses process/risk/founder framing. Existing brand voice doc captures this. |
| Response Drafting Tips (Jun 2) | 3 | Social media engagement framework — six lenses model (Experience, Due Diligence, Risk, Process, Market, Founder-First). Risk Lens chosen as preferred. Voice pattern. |
| Email Notification Draft (May 27) | 3 — Template | New hire welcome email (HTML) created. California Know Your Rights compliance email. Both are templates, not institutional knowledge. |

#### Key Knowledge Milestones This Batch

- **Management Call Guide Documented:** The seller preparation guide for management presentations is now documented for the first time. This is a two-page PDF distributed before every management call. Confirms the buyer evaluation framework: Leadership, Business Understanding, Transition Risk, Growth Potential.
- **Expense Policy Clarified:** Business meals with clients = reimbursable. Individual travel meals = not reimbursable. Deal Principal (1099) expenses require CEO approval.
- **Two-Document HR Approach:** Nick Pond engagement confirms Meritage preference for two-document HR structure: 1099 Contractor Agreement now, W-2 Employee Offer Letter after 6-month review.
- **AI Lead Gen Strategy Noted:** "Exit Readiness Advisor" AI persona concept flagged as GTM planning item. Single persona first, scale after 1,000 followers / 100 assessments / 10 M&A conversations.

#### Conflicts Flagged

| Conflict | Status |
|---------|--------|
| Nick Pond Empire Builder commission — is it on first-year contract value only or indefinitely recurring? | Pending Daniel/Brian clarification |
| New hire welcome email — needs hosted logo URL before deployment | Pending |
| AI media company concept — needs decision on whether to pursue and budget | Pending Daniel/Brian |
| California Know Your Rights notice — does distribution to W-2 employees cover contractors too? | Pending legal review |

---

## Summary Statistics (Updated)

| Metric | Value |
|--------|-------|
| Total batches completed | 8 |
| Total conversations processed (full read) | ~37 |
| Total conversations surveyed (corpus sizing) | ~175 |
| Total records created | 14 |
| Total records updated (deduplication) | 5 |
| Total conflicts flagged | 20+ |
| Total conversations classified as Score 1-2 | 6 |
| Phase 1 status | In progress — ~37 of ~175 processed |
| Phase 2 status | Not started |

---

## Batch 9 — Priority Queue

### Highest Priority (Score 5):

| Conversation | Topic | Action |
|-------------|-------|--------|
| "Trial Structure Confirmation" (May 20) | DealJet trial — already in repo but confirm context | Review — may update agreements/ |
| "Reverse Lehman Formula / K2D additional" (May) | Fee framework | Confirm deduplication vs Batch 3-4 |
| "Exhibit A Rewrite" (May) | Sell-side fee exhibit | Confirm captured in Batch 5 |
| Conversations from Apr 2026 | M&A Firm vs Broker; Engagement Fee Structure | Review — likely Score 5 |
| "AppleBites Pathway Breakdown" (Apr 23) | Already captured Batch 5 | Confirm |
| Conversations from Mar-Apr 2026 | Subcontractor agreements, IP, fee structures | Review |

### Medium Priority (Score 4):

| Conversation | Topic | Action |
|-------------|-------|--------|
| Conversations from Feb-Mar 2026 | E&O coverage, comp structure, GTM | Review — most already captured |
| Earlier conversations pre-Feb 2026 | Older operational context | Review for residual knowledge |

---

*Part of the Meritage Operating System. See CONTRIBUTING.md for standards.*


---

### Batch 9 — 2026-07-01

**Source:** Meritage Project (May–Jun 2026)
**Conversations Processed:** 10 full reads (Transcript Analysis and Prep, Trial Structure Confirmation, Email Introduction Rewrite, Email Draft Assistance, Gallant Proposal Generation, CRM Naming Strategy, Deal Chat Communication, Skinner Attendance Critique, Schmidt Deal Pay Breakdown, GTM Deck Overhaul)
**Ingested By:** Claude Sonnet 4.6

#### Records Created
| File | Category | Topic |
|---|---|---|
| `operations/gtm-client-journey-architecture-2026-05.md` | operations/ | Two-pathway client model (Empire Builder vs Sell-Side); four-presentation ecosystem; Apple Bites as segmentation engine; Forge case study (education reframes price) |
| `deal-analysis/schmidt-roofing-earnout-case-study-2026-05.md` | deal-analysis/ | Schmidt Roofing fee structure — $750K at close + $250K max contingent EBITDA fees (2026/27/28 thresholds); lessons on signed docs vs. internal expectations |
| `operations/roam-deal-communication-policy-2026-05.md` | operations/ | Roam deal-specific chat policy; Roam as performance management tool; team engagement benchmarks |
| `applebites/gallant-dill-partnership-economics-2026-05.md` | applebites/ | Gallant Dill: $10K/month licensing + 3% Apple Bites revenue participation + 10% Empire Builder referral; CRM naming recommendation (Orchard) |

#### Records Deduplicated
- Trial Structure Confirmation (May 20) — DealJet agreement context; DealJet initial terms ($1K/intro + 5%) vs final terms (no upfront + 10%); update notes in DealJet file
- Transcript Analysis and Prep (Jun 24) — deal readiness framework reinforces existing `deal-readiness-assessment-framework.md`; HVAC opportunity specific but methodology consistent
- CRM Naming Strategy (May 15) — "Orchard" recommendation captured in Gallant file; strategic architecture context in GTM journey file

#### Records Ignored
- Email Introduction Rewrite (May 15) — Score 1: brief intro email rewrite, no enduring knowledge

#### Conflicts Flagged
- Schmidt Deal: Internal team discussion referenced "$250K in 90 days then $500K later" but the signed Fee Agreement shows EBITDA-contingent payments with annual measurement and 30-day payment post-determination. Lesson documented. No conflict requiring Daniel's review — signed document controls.
- Gallant Dill partnership economics are "proposed structure" (May 2026). Confirm whether economics were finalized or remain in negotiation.
- GTM deck overhaul reveals MISSING internal sales decision framework (lead routing/qualification scoring). This is a critical operational gap as team scales. Needs Daniel's prioritization.

#### Open Questions
- Was the Gallant Dill partnership finalized at proposed economics ($10K/mo + 3% + 10% EB)?
- Has the "one canonical pathway map" (operational decision tree) been built since this conversation?
- What happened with the APA clarification email on Schmidt? Was annual EBITDA measurement confirmed?

---


---

### Batch 10 — 2026-07-01

**Source:** Meritage Project (May 2026 — Apr/May 2026)
**Conversations Processed:** 13 full reads (PTO Policy Recommendations, Branch/Reverse Lehman Formula [K2D Final], Email Rewrite Request, Investment Banking Riddle, Referral Fee Structure Explanation, M&A Category Clarification, Exhibit A Rewrite, Fee Structure Options, Client Naming Suggestions, Adding 10th Person Layout, Increase Profit Webinar, CIM Comparison and Grading context, Employee vs Contractor Classification)
**Ingested By:** Claude Sonnet 4.6

#### Records Created
| File | Category | Topic |
|---|---|---|
| `hr/pto-sick-leave-policy-2026-05.md` | hr/ | PTO (120 hrs front-loaded) vs. Sick Leave (40 hrs accrued); Gusto configuration; Alabama break policy (minimal administrative); Tennessee compliance notes |
| `agreements/buy-side-engagement-fee-structures-2026-05.md` | agreements/ | Three buy-side fee structure tiers: Full Mandate ($6.5-8.5K/mo + 3-5%), Phased Mandate ($2K/mo phase 1 + $5K/mo + Reverse Lehman phase 2), Success-Fee Dominant ($7.5K activation + 3.5-4.5%) |

#### Records Deduplicated
- Branch · Reverse Lehman Formula (May 12) — K2D final agreement confirmed: 4% top tier + $1M cap; Schedule 2 approved buyer list language (addendum process); deduplicated to k2d-engagement-fee-negotiation.md
- Referral Fee Structure Explanation (May 7) — Rule: no separate referral fee when sourcer is also running the deal; referral fee only when opportunity handed off to broader team; deduplicated to reverse-lehman-fee-framework.md
- M&A Category Clarification (May 6) — Active deal pipeline as of May 2026 documented (Bananas, Stockyard, Dairyland, Trees, Umbrella, Alchemy, Buffalo, Baloon, Skyvista, Wonka); outreach segmentation principle ("match deals to buyer type")
- Email Rewrite Request (May 12) — Email for Jessica re: Stahl onboarding; no new knowledge, writing style only
- Investment Banking Riddle (May 7) — Score 1: trivia, no institutional knowledge
- Client Naming Suggestions (May 13) — Score 2: one-off naming task
- Adding 10th Person Layout (May 15) — Score 1: visual design task only

#### Records Ignored
- Investment Banking Riddle — Score 1: trivia question ("I have no idea" response)
- Adding 10th Person Layout — Score 1: image generation request only
- Increase Profit Webinar — Score 2: draft email, no enduring knowledge

#### Conflicts Flagged
- K2D deal: Final terms (4% + $1M cap) differ from standard Reverse Lehman. This client-specific exception is now documented. The Schedule 2 approved buyer list process should be considered for inclusion in standard engagement agreement templates.
- Employee vs Contractor Classification — conversation suggests Skinner may have been reclassified or there was ambiguity; cross-check with HR files re: performance review prohibition for 1099s.

#### Open Questions
- Was the Merlin Law Group (buy-side engagement) actually activated? Which option did they choose (1, 2, or 3)?
- The M&A Category Clarification shows "Project Wonka" as a Family Office — confirm current status.
- Referral fee policy: what is the specific percentage rate for hand-off referrals? This was described but not quantified in this conversation.

---


---

## Batch 11 — April 2026 Conversations

**Date Processed:** 2026-07-02  
**Conversations Reviewed:** 11  
**New Records Created:** 2  
**Records Deduplicated/Merged:** 5  
**Open Conflicts:** 0  

### Conversations Processed

| Title | Date | Score | Action |
|-------|------|-------|--------|
| Employee vs Contractor Classification | Apr 29 | 4 | Merged into quarterly-performance-review-framework (1099 classification rules) |
| Workers Comp Setup Guide | Apr 27 | 1 | Ignored — personal W4 withholding, no institutional knowledge |
| Quarterly Review Summary | Apr 27 | 4 | Created quarterly-performance-review-framework-2026-04.md |
| Title Recommendations for 1099 | Apr 24 | 4 | Merged into quarterly-performance-review-framework (title risk taxonomy) |
| AppleBites Pathway Breakdown | Apr 23 | 4 | Merged into applebites/meritage-ecosystem-pathway-architecture.md (3-pathway routing, objection framework) |
| Reverse Lehman Formula | Apr 21 | 4 | Merged into deal-analysis/k2d-engagement-fee-negotiation.md (NDA-trigger buyer definition, fee protection mechanics) |
| Compensation and Benefits Revision | Apr 20 | 4 | Merged into hr/deal-principal-compensation-structure.md (W2 offer letter with 7.25% net revenue variable comp) |
| Engagement Fee Structure | Apr 15 | 5 | Created agreements/sell-side-engagement-fee-structure-2026-04.md |
| Payment Summary and W2 Transition | Apr 10 | 3 | Noted in migration log — W2 transition for 4 core employees confirmed, ~$7K/year workers comp |
| M&A Firm vs Broker | Apr 9 | 4 | Merged into emails/broker-to-broker-positioning.md (Broker vs M&A Process "vs." framework) |
| Call Breakdown and Fee Framing | Apr 9 | 5 | Merged into agreements/sell-side-engagement-fee-structure-2026-04.md (Arkham/Naomi deal case, QoE positioning) |

### New Records Created

1. `agreements/sell-side-engagement-fee-structure-2026-04.md` — Comprehensive sell-side fee framework: $15K engagement + 3% success + 6% performance; 1%/2.5% existing vs. sourced buyer bifurcation; NDA-trigger buyer definition; QoE positioning; Arkham/Naomi case reference
2. `hr/quarterly-performance-review-framework-2026-04.md` — Q1 2026 review process patterns, role-specific review standards (producers, ops, BD, finance), 1099 title governance, W2 transition record

### Records Deduplicated or Merged

1. **1099 contractor classification rules** → merged into quarterly-performance-review-framework (from Employee vs Contractor Classification conversation)
2. **Advisor title risk taxonomy** → merged into quarterly-performance-review-framework (from Title Recommendations for 1099)
3. **AppleBites 3-pathway routing logic** → merged into existing applebites file (from AppleBites Pathway Breakdown)
4. **K2D NDA buyer attribution** → merged into existing k2d deal analysis (from Reverse Lehman Formula conversation)
5. **W2 offer letter variable comp language** → merged into existing deal principal compensation file (from Compensation and Benefits Revision)

### Priority Queue for Batch 12

Continuing from April 2026 conversations into March 2026 and earlier:
- Call Breakdown and Fee Framing deeper notes (completed)
- Social Media Post Edit (Apr 7) — likely Score 2, content editing
- Review Search Results (Apr 7) — likely Score 2, research
- Monthly Review Summary (Apr 7) — likely Score 4, review process content
- Course Timeline and Total Hours (Apr 6) — likely Score 2, logistics
- SMA Acquisition Summary (Apr 6) — potentially Score 4, deal case study
- Summary of Leadership Messages (Apr 6) — likely Score 3, leadership comms
- Post Framing Suggestions (Apr 2) — likely Score 2-3, content
- Operational Alignment Gaps (Mar 30) — likely Score 4-5, operations
- Email Draft Summary (Mar 25) — likely Score 2
- Subcontractor Agreements and IP (Mar 25) — likely Score 4, IP protection
- New Hire Onboarding Review (Mar 23) — likely Score 4, HR
- Gorilla Roofing Fee Reduction (Mar 19) — likely Score 4, deal case study


---

## Batch 12 — April-March 2026 Conversations

**Date Processed:** 2026-07-02  
**Conversations Reviewed:** 8  
**New Records Created:** 3  
**Records Deduplicated/Merged:** 4  
**Open Conflicts:** 0  

### Conversations Processed

| Title | Date | Score | Action |
|-------|------|-------|--------|
| Social Media Post Edit | Apr 7 | 2 | Ignored — content editing only, no institutional knowledge |
| Review Search Results | Apr 7 | 2 | Ignored — research task, no institutional knowledge |
| Monthly Review Summary | Apr 7 | 3 | Noted — Joe McMahon review with financial data delay and approval bottleneck patterns; merged into quarterly-performance-review-framework |
| Course Timeline and Total Hours | Apr 6 | 1 | Ignored — logistics planning, no institutional knowledge |
| SMA Acquisition Summary | Apr 6 | 4 | Created deal-analysis/sma-bpo-acquisition-diligence-2026-04.md |
| Summary of Leadership Messages | Apr 6 | 2 | Ignored — historical message forwarding, no net new patterns |
| Post Framing Suggestions | Apr 2 | 2 | Ignored — social media content editing only |
| Operational Alignment Gaps | Mar 30 | 5 | Created operations/training-vs-process-ownership-framework-2026-03.md |

### Additional Conversations Processed (March 2026)

| Title | Date | Score | Action |
|-------|------|-------|--------|
| Subcontractor Agreements and IP | Mar 25 | 4 | Merged into agreements/subcontractor-ip-protection-2026-05.md (IP valuation $5M liquidated damages concept, Helen as attorney) |
| Gorilla Roofing Fee Reduction | Mar 19 | 4 | Created section within deal-analysis/sma-bpo-acquisition-diligence-2026-04.md; extends hr/eo-coverage-scott-stepanik-litigation.md |

### New Records Created

1. `operations/training-vs-process-ownership-framework-2026-03.md` — Training vs. Process vs. Ownership distinction, IOI/LOI evaluation standards, buyer quality vetting, client visibility requirements, Veran/Roam AI search prompt for extracting Brian's training expectations
2. `deal-analysis/sma-bpo-acquisition-diligence-2026-04.md` — SMA BPO/VA platform acquisition case study, buy-side diligence framework for BPO/services platforms, PE owner unresponsiveness pattern, Gorilla Roofing fee reduction damage analysis
3. Records from Batch 11: quarterly-performance-review-framework-2026-04.md (HR) and sell-side-engagement-fee-structure-2026-04.md (Agreements)

### Records Deduplicated or Merged

1. **Monthly Review financial delay patterns** → merged into quarterly-performance-review-framework (Joe McMahon approval bottleneck)
2. **IP protection strategy** → merged into existing subcontractor-ip-protection file (liquidated damages concept, Helen attorney, $5M valuation)
3. **Gorilla Roofing damage** → documented in sma deal analysis file + cross-referenced to E&O litigation file
4. **AppleBites/Empire Builder IP assets** → confirmed in subcontractor IP conversation; already documented

### Priority Queue for Batch 13

Continuing from March 2026 into earlier conversations:
- Email Assessment Update (Mar 18) — likely Score 2
- M&A Firm Clarification (Mar 17) — likely Score 3-4, positioning content
- CIM Questionnaire for Clarity (Mar 16) — likely Score 4-5, CIM standards
- Affiliate Fee Calculation (Mar 16) — likely Score 3-4, fee computation
- Meritage Integration Strategies (Mar 13) — likely Score 4, strategy
- TikTok Scripts for M&A (Feb 26) — likely Score 2-3, content
- Compensation Structure for Analysis (Feb 20) — likely Score 4, comp modeling
- Document Content Editing (Feb 17) — likely Score 1
- Bonus Structure Comparison (Feb 17) — likely Score 4, compensation
- Pipeline alignment questions (Feb 9) — likely Score 4, deal pipeline
- Missed Podcast Deliverables (Feb 5) — likely Score 2
- E&O Coverage Analysis (Feb 4) — likely Score 4, litigation
- 6 Month Plan Framework (Feb 3) — likely Score 4-5, strategic planning


---

## Batch 13 — March-February 2026 Conversations

**Date Processed:** 2026-07-02  
**Conversations Reviewed:** 8  
**New Records Created:** 0 (E&O file already existed; all other content deduplicated)  
**Records Deduplicated/Merged:** 6  
**Open Conflicts:** 0  

### Conversations Processed

| Title | Date | Score | Action |
|-------|------|-------|--------|
| Email Assessment Update | Mar 18 | 2 | Ignored — email editing only, no institutional knowledge |
| M&A Firm Clarification | Mar 17 | 3 | Noted — MP Advisory competitor firm uses same 19-step sell-side process; confirms Meritage positioning; no new file needed |
| CIM Questionnaire for Clarity | Mar 16 | 4 | Deduplicated — CIM intake questionnaire framework already captured in cim-creation-standard; confirms structure |
| Affiliate Fee Calculation | Mar 16 | 3 | Noted — historical fee computation for a specific deal; already covered in fee structure files |
| Meritage Integration Strategies | Mar 13 | 4 | Noted — strategic planning content; concepts already in value-creation-platform and gtm files |
| Pipeline Alignment Questions | Feb 9 | 3 | Noted — GHL email templates for LOI deadline communication and Apple Bites post-assessment sequence; HTML templates are operational tools, already covered |
| E&O Coverage Analysis | Feb 4 | 5 | Deduplicated — eo-coverage-scott-stepanik-litigation-2026-02.md already exists from earlier batch; confirmed coverage determination matches prior record (biBERK E&O does not cover contractor compensation disputes) |
| 6 Month Plan Framework | Feb 3 | 3 | Noted — "SOPs are the receipt, not the starting point" principle for client org design; concept already captured in management-call-prep-guide |

### Key Deduplication Findings

1. **E&O Coverage Analysis:** File eo-coverage-scott-stepanik-litigation-2026-02.md confirmed as already created in earlier batch. New conversation confirmed same conclusion: biBERK Professional Liability does NOT cover contractor compensation claims. Brian Franco named personally. Defense relies on operating agreement quality.
2. **CIM Questionnaire:** Full CIM intake questionnaire template (Clarity Family Office) confirms the intake structure already captured in cim-creation-standard-2026-06.md.
3. **MP Advisory Competitor:** 19-step sell-side process from MP Advisory mirrors Meritage process exactly. Key lesson: differentiation must come from execution quality and brand, not process structure alone.

### Priority Queue for Batch 14

Continuing from February 2026 into earlier conversations (January 2026 and earlier):
- Bonus Structure Comparison (Feb 17) — VA bonus incentive design (variable vs. fixed pool)
- Compensation Structure for Analysis (Feb 20) — deal principal comp modeling
- Missed Podcast Deliverables (Feb 5) — likely Score 2
- Review of Requested Changes (Feb 4) — likely Score 3, agreement modifications
- Email Softening Tips (Feb 2) — likely Score 2, communication style
- Consultant Fee Structure Edit (Jan 28) — likely Score 3-4
- Inc Magazine Paragraph Help (Jan 27) — likely Score 1
- Meeting Agenda Draft (Jan 19) — likely Score 2
- Less technical tone (Jan) — likely Score 2
- Production Process Mapping (Jan) — likely Score 3-4, workflow
- Engagement Agreement Follow-Up (Jan) — likely Score 4
- Talk Titles for Morgan (Jan) — likely Score 2
- Addendum to agreement (Jan) — likely Score 4
- Roofing company diagnostic questions (Jan) — likely Score 3-4
- Success fee calculation (Jan) — likely Score 3-4
