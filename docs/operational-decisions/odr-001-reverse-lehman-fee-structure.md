# ODR-001: Why Meritage Uses the Reverse Lehman Fee Structure

**Date:** 2026-07-01
**Status:** Active
**Last reviewed:** 2026-07-02
**Superseded by:** N/A

---

> **Terminology & mechanics (confirmed by Daniel, 2026-07-02).**
> "Reverse Lehman" is Meritage's intentional, client-facing name for its fee structure and is retained deliberately across all documentation.
> Mechanically, the **sell-side scale is ascending**: 1% on the first $1M of enterprise value, rising through the tranches to a **5% cap** (1% / 2% / 3% / 4% / 5%), protected by a **$250,000 minimum success fee (floor)**. The buy-side scale is descending (5% / 4% / 3% / 2% / 1%).
> See [`reverse-lehman-fee-framework-2026-05.md`](../knowledge/chat-history/agreements/reverse-lehman-fee-framework-2026-05.md) for the authoritative tier schedule and floor detail.

---

## Decision

Meritage uses a **Reverse Lehman** fee structure for sell-side engagements: an **ascending tranche scale** (1% → 5% cap) protected by a **$250,000 minimum success fee**. The ascending marginal rate ties Meritage's economics to the upside it creates for the Seller; the minimum floor ensures every engagement — regardless of deal size — covers the fixed work required to run a quality process.

---

## Context

Traditional Lehman Formula structures (5% on the first $1M, 4% on the second, 3% on the third, etc.) were designed for larger transactions common in institutional investment banking. Applied to lower middle market transactions — where deal values typically range from $5M to $75M — a front-weighted formula caps the advisor's participation in exactly the upside the advisor is hired to create, and does not, on its own, guarantee adequate compensation on smaller engagements.

Meritage operates exclusively in the lower middle market. The work required to execute a $10M transaction is not proportionally less than the work required on a $30M transaction. Fixed costs of engagement preparation, positioning, buyer outreach, and process management do not scale linearly with enterprise value. Meritage's structure addresses both realities: the ascending scale rewards value creation on larger deals, and the minimum fee floor protects the economics of smaller ones.

---

## Options Considered

1. **Standard (front-weighted) Lehman Formula** — Percentage decreasing as value increases. Common at traditional investment banks. Caps advisor participation in the upside and is poorly suited to aligning incentives in lower middle market sell-side work.
2. **Flat Percentage Fee** — A single percentage applied to all transaction values. Simple to explain. Does not reward value creation and carries no minimum-fee protection ("tourist client" risk).
3. **Reverse Lehman + Minimum Fee** — Meritage's chosen structure, branded "Reverse Lehman": an ascending tranche scale (1/2/3/4/5%, 5% cap) with a $250,000 floor. Aligns advisor economics with maximizing transaction value while protecting small-deal compensation.
4. **Fixed Retainer + Success Fee** — Reduces pure success-fee risk. May conflict with seller preference for pay-at-close structures. Used in combination where appropriate (see Implications).

---

## Rationale

The Reverse Lehman structure aligns Meritage's economics with the realities of lower middle market advisory work:

- **The ascending scale aligns incentives with the Seller.** Because the marginal rate *rises* with deal size to a 5% cap, Meritage earns proportionally more on every incremental dollar of enterprise value it helps create. The advisor is paid the most precisely where it does its highest-value work — pushing valuation and terms upward — so Meritage's and the Seller's interests point in the same direction.
- **The minimum fee floor compensates for non-scaling work.** A $10M transaction requires nearly as much advisor effort as a $25M one; the fixed costs of preparation, positioning, and process management do not scale with size. The lightly charged early tranches (only ~$100K across the first $4M) would not cover that work on a small deal — so the **$250,000 minimum success fee** guarantees adequate compensation. The floor, not a front-weighted percentage, is how Meritage protects smaller-engagement economics.
- **It is transparent and explainable to clients.** The formula and the floor are disclosed at engagement and tied directly to outcome.
- **It differentiates Meritage** from brokers who use percentage-of-revenue or flat-fee structures, and it is consistent with quality lower middle market advisory practice.

The retainer component (where applicable) covers the cost of engagement preparation work that occurs before any transaction certainty exists.

---

## Implications

- All engagement agreements must disclose the Reverse Lehman structure — including the ascending tiers and the $250,000 minimum success fee — clearly and in plain language.
- Advisors must be prepared to explain and defend both the scale and the floor during initial engagement conversations.
- Module 03 (Engagement) documents how and when the fee structure is introduced to prospective clients.
- The fee structure is a factor in qualification: Meritage declines engagements where a seller's expectation of advisor fees is fundamentally incompatible with the Reverse Lehman structure.

---

## Related Documents

- [Reverse Lehman Fee Framework](../knowledge/chat-history/agreements/reverse-lehman-fee-framework-2026-05.md)
- [Module 03: Engagement](../m-and-a/03-engagement.md)
- [Module 02: Qualification](../m-and-a/02-qualification.md)
- [Module 04: Valuation](../m-and-a/04-valuation.md)
- [Operational Decisions Index](README.md)

---

*Last updated: 2026-07-02*
*See [CONTRIBUTING.md](../../CONTRIBUTING.md) for document standards.*
