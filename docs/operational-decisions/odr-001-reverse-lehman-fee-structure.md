# ODR-001: Why Meritage Uses the Reverse Lehman Fee Structure

**Date:** 2026-07-01
**Status:** Active
**Last reviewed:** 2026-07-02
**Superseded by:** N/A

---

> **Terminology & mechanics clarification (confirmed by Daniel, 2026-07-02).**
> "Reverse Lehman" is Meritage's intentional, client-facing name for its fee structure and is retained deliberately across all documentation.
> Mechanically, the **confirmed sell-side scale is ascending**: 1% on the first $1M of enterprise value, rising through the tranches to a **5% cap** (1% / 2% / 3% / 4% / 5%), and is typically protected by a minimum fee floor on smaller deals. The buy-side scale is descending (5% / 4% / 3% / 2% / 1%).
> This supersedes the earlier phrasing that the sell-side applied "a higher percentage to lower tranches," which described a descending structure and is inaccurate for sell-side engagements. See [`reverse-lehman-fee-framework-2026-05.md`](../knowledge/chat-history/agreements/reverse-lehman-fee-framework-2026-05.md) for the authoritative tier schedule.
>
> **Open item for Daniel:** the *Rationale* section below was written against the earlier (descending) interpretation. The economic justification for the confirmed *ascending* scale — and specifically how the minimum fee floor ensures adequate compensation on smaller engagements — should be reviewed and rewritten by Daniel. Flagged, not changed.

---

## Decision

Meritage uses a Reverse Lehman fee structure for sell-side engagements. The confirmed mechanics are an ascending tranche scale (1% → 5% cap) with a minimum fee floor on smaller deals; see the clarification note above for detail.

---

## Context

Traditional Lehman Formula structures (5% on the first $1M, 4% on the second, 3% on the third, etc.) were designed for larger transactions common in institutional investment banking. Applied to lower middle market transactions — where deal values typically range from $5M to $75M — the Lehman Formula produces fees that do not adequately compensate for the work required on smaller engagements and may misalign incentives on larger ones.

Meritage operates exclusively in the lower middle market. The work required to execute a $10M transaction is not proportionally less than the work required on a $30M transaction. Fixed costs of engagement preparation, positioning, buyer outreach, and process management do not scale linearly with enterprise value.

---

## Options Considered

1. **Standard Lehman Formula** — Percentage decreasing as value increases. Common at traditional investment banks. Poorly suited to lower middle market engagements where base work is constant.
2. **Flat Percentage Fee** — A single percentage applied to all transaction values. Simple to explain. Does not reflect the disproportionate effort on smaller engagements.
3. **Reverse Lehman Formula** — Meritage's chosen structure, branded "Reverse Lehman." (See the confirmed mechanics in the clarification note above.)
4. **Fixed Retainer + Success Fee** — Reduces pure success-fee risk. May conflict with seller preference for pay-at-close structures.

---

## Rationale

*Note (2026-07-02): the rationale below predates confirmation of the ascending tier mechanics and is retained pending Daniel's review — see the open item flagged at the top of this document.*

The Reverse Lehman structure aligns Meritage's economics with the realities of lower middle market advisory work:

- A $10M transaction requires nearly as much advisor effort as a $25M transaction. The Reverse Lehman compensates accordingly.
- The structure incentivizes Meritage to maximize the transaction value — every incremental dollar of enterprise value above a threshold has a fee implication.
- It is transparent and explainable to clients. The formula is disclosed at engagement and tied directly to outcome.
- It is standard practice among quality lower middle market advisors and distinguishes Meritage from brokers who use percentage-of-revenue or flat-fee structures.

The retainer component (where applicable) covers the cost of engagement preparation work that occurs before any transaction certainty exists.

---

## Implications

- All engagement agreements must disclose the Reverse Lehman structure clearly and in plain language.
- Advisors must be prepared to explain and defend the fee structure during initial engagement conversations.
- Module 03 (Engagement) documents how and when the fee structure is introduced to prospective clients.
- The fee structure is a factor in qualification: Meritage declines engagements where a seller's expectation of advisor fees is fundamentally incompatible with the Reverse Lehman structure.

---

## Related Documents

- [Module 03: Engagement](../m-and-a/03-engagement.md)
- [Module 02: Qualification](../m-and-a/02-qualification.md)
- [Module 04: Valuation](../m-and-a/04-valuation.md)
- [Operational Decisions Index](README.md)

---

*Last updated: 2026-07-02*
*See [CONTRIBUTING.md](../../CONTRIBUTING.md) for document standards.*
