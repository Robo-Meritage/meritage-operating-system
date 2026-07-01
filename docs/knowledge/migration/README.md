# Knowledge Migration

**Classification:** Internal  
**Status:** Active  
**Last Updated:** 2026-07

---

## Purpose

This folder contains the audit trail for the knowledge migration from ChatGPT to the Meritage Operating System.

The migration is a data engineering project, not a documentation project. Its purpose is to harvest knowledge that currently exists only across the Daniel + ChatGPT collaboration history and transform it into structured, retrievable records in this repository.

---

## What This Folder Contains

| File | Purpose |
|---|---|
| [migration-log.md](./migration-log.md) | Running log of all ingestion batches — source, date, conversations processed, records created, duplicates merged, conflicts flagged |

---

## Migration Architecture

The migration follows a two-phase approach documented in the [Chat History README](../chat-history/README.md).

**Phase 1:** Meritage Project conversations (highest signal-to-noise ratio)  
**Phase 2:** Full ChatGPT export filtered by classification

**Pipeline per batch:**

```
Conversation → Classify → Extract → Deduplicate → Link → Commit → Log
```

---

## Why a Migration Log

The migration will span multiple sessions. Without a log:

- There is no way to know which conversations have been processed.
- - Duplicate ingestion is likely — the same conversation could be processed twice.
  - - There is no audit trail if a record needs to be traced back to its source.
    - - Progress cannot be reported or resumed cleanly.
     
      - The migration log makes the process resumable, auditable, and transparent.
     
      - ---

      ## Migration Status

      | Phase | Status |
      |---|---|
      | Phase 1: Meritage Project | Not started — corpus pending |
      | Phase 2: Full export | Not started — corpus pending |

      ---

      ## Related Documents

      - [Chat History README](../chat-history/README.md) — Full ingestion pipeline and category routing
      - - [INGESTION-GUIDE.md](../chat-history/INGESTION-GUIDE.md) — Step-by-step operational protocol
        - - [Migration Log](./migration-log.md) — Batch-by-batch audit trail
         
          - ---

          *Part of the [Meritage Operating System](../../../README.md). See [CONTRIBUTING.md](../../../CONTRIBUTING.md) for standards.*
