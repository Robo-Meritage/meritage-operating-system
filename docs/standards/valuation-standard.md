# Valuation & Financial Normalization Standard

**Classification:** Internal
**Category:** Standards
**Status:** Active
**Last Updated:** 2026-07-02
**Source:** ChatGPT — Meritage Partners Project — "Owner Replacement Salary Methods," "Fee multiplier calculation," EBITDA-cluster conversations

---

## Purpose

Defines the practitioner methodology Meritage uses to normalize earnings and develop an Enterprise Value range for a lower middle market company. This standard is the "how"; [M&A Module 04: Valuation](../m-and-a/04-valuation.md) is the "why and when" (philosophy, Seller communication, expectation management). Read them together.

**Core principle:** Lower middle market buyers pay for normalized, defensible, recurring earnings — not reported earnings. Valuation begins with financial normalization and is not stated until that work is complete.

---

## Step 1 — EBITDA Normalization (Add-Back Analysis)

Start from reported earnings and build to **Adjusted EBITDA** by identifying and supporting each adjustment:

- **Owner compensation normalization** — adjust owner pay to a market-rate replacement cost (see the methodology below). This is usually the largest and most scrutinized add-back.
- **One-time / non-recurring items** — legal settlements, one-off projects, non-recurring professional fees, etc.
- **Personal / discretionary expenses run through the business** — personal vehicles, travel, memberships not required to operate.
- **Above- or below-market expenses** — rent to a related party, family members on payroll, etc., adjusted to market.

Every adjustment must be documented and defensible in diligence. Un-supportable add-backs damage credibility and get repriced at the quality-of-earnings stage.

---

## Step 2 — Owner Replacement Compensation Methodology

Do **not** answer "what is the industry-standard owner salary for this NAICS code?" Instead answer: **"What would it cost to replace the owner's functions?"** This replacement-cost approach mirrors how accredited valuation analysts normalize owner compensation and is far more defensible in an M&A setting.

**Primary sources (market compensation, Tier 1):**
- BLS Occupational Employment and Wage Statistics (OEWS)
- Economic Research Institute (ERI)
- Salary.com
- PayScale

Do **not** use valuation/transaction databases (BizEquity, ValuSource, Pratt's Stats/DealStats, PeerComps) as the *primary* source for owner compensation — those are for valuation multiples and comparable transactions.

**Inputs:** NAICS code · Revenue · EBITDA · Employee count · Geography (state or metro) · Owner role(s).

**Owner role options:** CEO/President · General Manager · Sales Leader · Technical Expert · Operator/Working Owner · Multiple Roles.

**Method:**
1. Estimate a market salary for each role the owner actually performs.
2. Sum them to a **Combined Replacement Cost**.
3. Apply a weighting factor for how much the owner personally carries those functions:
   - **100%** — owner actively performs the role(s)
   - **50%** — a management team already exists
   - **25%** — largely absentee owner
4. **Normalized Owner Compensation = weighted Replacement Cost.**

**Secondary validation:** cross-check the calculated replacement salary against owner-compensation ranges in transaction databases (DealStats, ValuSource, PeerComps, BizComps) and flag large variances.

**Worked example (from source):** NAICS 238160 Roofing Contractors, ~$5M revenue, ~20 employees, owner acting as CEO **and** Sales Manager → CEO $140,000 + Sales Manager $90,000 = **$230,000** combined replacement cost (at 100% weighting).

> **Apple Bites roadmap note:** the durable goal is a proprietary lookup — NAICS → Revenue Band → Employee Band → Geographic Multiplier → Replacement Salary Range — powering the "Normalized Owner Compensation" field in the Apple Bites valuation tool.

---

## Step 3 — Multiple Selection & Enterprise Value Range

- Multiple selection is a judgment call informed by data, not a formula. Comparable-transaction databases provide ranges; experience determines where within the range a company sits (management depth, customer concentration, margin defensibility, growth, operational readiness). See Module 04.
- For SaaS / CRM targets, use the [SaaS/CRM Valuation Multiples Reference](../deal-analysis/saas-crm-valuation-multiples-2025-10.md) (ARR vs. EBITDA multiple guidance).
- Develop a **low / mid / target** EV range (Adjusted EBITDA × selected multiple) and use it as the internal anchor for positioning and negotiation — not as a listing price.

---

## Guardrails

- This is an advisory estimate — not a certified appraisal, tax opinion, or legal opinion of value.
- Do not inflate valuations to win engagements. Present what the market will bear and align Seller expectations before signing (see Module 04).

---

## Related Documents

- [M&A Module 04: Valuation](../m-and-a/04-valuation.md)
- [SaaS/CRM Valuation Multiples Reference](../deal-analysis/saas-crm-valuation-multiples-2025-10.md)
- [Reverse Lehman Fee Framework](../knowledge/chat-history/agreements/reverse-lehman-fee-framework-2026-05.md)

---

*See [CONTRIBUTING.md](../../CONTRIBUTING.md) for document standards.*
