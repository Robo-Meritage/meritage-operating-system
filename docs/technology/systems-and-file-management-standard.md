# Systems & File Management Standard

**Classification:** Internal
**Category:** Technology / Operations
**Status:** Active
**Last Updated:** 2026-07-02
**Source:** ChatGPT — Meritage Partners Project — "New Hire Onboarding Review"

---

## Purpose

Defines Meritage's operating stack, the system of record for each type of information, the standard deal folder structure, and the document lifecycle across the deal process. This is the authoritative reference for where information lives and how it moves. It supersedes any prior tool arrangement (Meritage has moved off Ninety).

---

## Operating Stack — System of Record Map

Meritage does not operate inside a single platform. It runs a Google-centric operating system with deal-specific overlays. Each platform has one job:

| Platform | Role | System of record for |
|----------|------|----------------------|
| **Google Drive (G-Suite)** | Internal repository and working environment | **All deal materials** — financial worksheets, teasers, CIM drafts, internal documents. The master version always lives in Drive. |
| **MadeMarket** | Deal pipeline and buyer management | The **buyer list**, pipeline stage, buyer outreach/activity, NDA tracking, and CIM distribution (post-NDA). Distribution and tracking only — not file storage. |
| **PandaDoc** | Execution layer | NDAs and agreements are sent and executed here. |
| **Orangedox** | Controlled distribution (GTM, post-NDA) | Approved teaser/CIM materials shared with investors during go-to-market. |
| **Suralink** | Diligence data room (post-LOI, invite-only) | Diligence documents once a deal reaches diligence; becomes the single source of truth for diligence. |
| **ROAM** | Internal team communication | Deal-specific chats per the [Roam Deal Communication Policy](../knowledge/chat-history/operations/roam-deal-communication-policy-2026-05.md). No deal-critical data should live *exclusively* in ROAM. |

**Core principle:** Google Drive is always the source of truth. MadeMarket is distribution and tracking only. Everything created outside Drive must map back to Drive.

---

## Standard Deal Folder Structure (Google Drive)

Every deal uses the same root folder structure. This consistency is what makes the Drive-as-source-of-truth model work.

```
[Deal Root Folder]
├── 01 Financials
├── 02 Adjustments & EBITDA
├── 03 CIM Materials
├── 04 Teaser Data Room
├── 05 Buyer Communications
├── 06 Diligence (Pre-Suralink)
└── 07 Final Docs
```

**Non-negotiable rules:**
- Never deviate from the structure or create duplicate structures.
- Never rename core folders.
- Never store files locally — all work lives in the deal folder.

---

## Document Lifecycle — File Sharing Workflow

Documents move through three environments across the deal lifecycle:

1. **Google Drive — source of truth.** All materials are created and maintained here throughout.
2. **Orangedox — controlled distribution (post-NDA, GTM).** At the distribution stage, approved materials are moved from Drive into Orangedox for controlled investor sharing.
3. **Suralink — diligence data room (post-LOI).** Once an LOI is executed and the deal enters diligence, materials are moved from Orangedox into Suralink for the remainder of the process.

**Movement rules:**
- Documents are **moved, not copied.** No duplication across systems.
- Movement between platforms is intentional and staged (Drive → Orangedox → Suralink), triggered by NDA (distribution) and LOI (diligence).
- Google Drive retains the master version at all times; external platforms are controlled mirrors, not replacements.
- The **Deal Owner** and **Deal Admin** decide what is shared and when.

---

## Document Control Standards

- Every deal has a single **file owner**, a **deal lead**, and a **financial owner**.
- No duplicate financial models.
- No `Final_v2_FINAL`-style naming. Use date-based naming or an in-file version log.
- Confirm the deal owner before making structural changes to a deal folder.

---

## Known Gap (Flagged)

As of this conversation, Meritage had no enforced SOP system — onboarding was memory-based and execution was personality-dependent. The recommendation captured was to build a "Meritage Operating Manual" (onboarding guide, deal lifecycle SOP, financial analysis SOP, folder-structure template, naming conventions). The Meritage Operating System (this repository) is the durable answer to that gap; the [New Hire Onboarding Checklist](../operations/new-hire-onboarding-checklist.md) operationalizes it.

---

## Related Documents

- [New Hire Onboarding Checklist](../operations/new-hire-onboarding-checklist.md)
- [Roam Deal Communication Policy](../knowledge/chat-history/operations/roam-deal-communication-policy-2026-05.md)
- [Deal Pipeline Management Patterns](../knowledge/chat-history/operations/deal-pipeline-management-patterns-2026-06.md)

---

*See [CONTRIBUTING.md](../../CONTRIBUTING.md) for document standards.*
