# Chat History Ingestion

**Classification:** Internal  
**Status:** Infrastructure Complete — Corpus Pending  
**Last Updated:** 2026-07

---

## Purpose

This folder is the landing zone for structured knowledge extracted from the ChatGPT collaboration history between Daniel and ChatGPT. It is not a document archive. It is a knowledge extraction target.

The goal is to capture two things:

1. **What Daniel knows** — decisions, preferences, frameworks, and positions that were articulated across conversations.
2. 2. **What the collaboration synthesized** — patterns, connections, and conclusions that emerged across multiple conversations and are not obvious from any single exchange.
  
   3. ---
  
   4. ## Staged Migration Architecture
  
   5. Knowledge transfer follows a two-phase approach. Do not ingest everything at once.
  
   6. ### Phase 1: Meritage Project Conversations (Highest Priority)
  
   7. Start with conversations that already live in the ChatGPT Meritage Partners Project. These are highly curated and almost entirely relevant. They include agreements, GTM, deal strategy, HR, referral programs, operations, M&A methodology, templates, and policies.
  
   8. **Why Phase 1 first:** Highest signal-to-noise ratio. Near-zero classification overhead. Fastest path to high-value knowledge.
  
   9. ### Phase 2: Full Export — Classify and Filter
  
   10. Use the full ChatGPT export (`conversations.json`) to identify additional Meritage-related conversations that happened outside the project. During Phase 2, each conversation is classified before extraction:
  
   11. | Classification | Action |
   12. |---|---|
   13. | Meritage — direct | Extract and commit |
   14. | Meritage — related | Review before extracting |
   15. | Unrelated | Ignore |
  
   16. **Why classify first:** A full ChatGPT export contains casual chats, experiments, dead ends, personal topics, duplicate iterations, and material unrelated to Meritage. Ingesting noise wastes extraction effort and degrades repository quality.
  
   17. ---
  
   18. ## Ingestion Pipeline
  
   19. Every conversation batch passes through this pipeline before committing.
  
   20. ```
       Conversation
       ↓
       Classify
           • Meritage (direct)
           • Meritage (related — review first)
           • Ignore
       ↓
       Extract
           Facts / Decisions / Preferences / Patterns / Lessons
       ↓
       Deduplicate
           Check for existing records on the same topic.
           Merge or synthesize rather than creating a duplicate entry.
       ↓
       Link to Existing Knowledge
           Reference existing MOS documents where relevant.
           Flag conflicts for resolution.
       ↓
       Commit
           File: [topic-slug]-[YYYY-MM].md in the correct subfolder.
       ↓
       Update Migration Log
           docs/knowledge/migration/migration-log.md
       ```

       **The deduplication step is critical.** Over a year of collaboration, the same topics were revisited repeatedly. One authoritative synthesis per topic is more valuable than ten slightly different entries.

       ---

       ## Extraction Format

       Each extracted knowledge record uses this structure:

       ```markdown
       ## [Topic Name]
       **Source:** [Conversation identifier or date]
       **Category:** [folder name]
       **Entities:** [list]

       ### Learned
       [What was established as true or accepted.]

       ### Rejected
       | Option | Reason rejected |
       |---|---|

       ### Accepted
       [What was adopted or decided.]

       ### Why
       [The reasoning — never omit this field.]

       ### Patterns
       [What this reveals about Daniel's preferences or operating model.]

       ### Open Questions
       [What was left unresolved.]

       ### Links
       [MOS documents this knowledge should be read alongside.]
       ```

       **Never omit the Why field.** The value of the knowledge is in the reasoning, not just the conclusion.

       ---

       ## Category Routing

       | Topic | Folder |
       |---|---|
       | Agreements, NDAs, affiliate agreements, LOIs | `agreements/` |
       | AppleBites product | `applebites/` |
       | Empire Builder product | `empire-builder/` |
       | Deals, client analysis, negotiation | `deal-analysis/` |
       | Email rewrites and templates | `emails/` |
       | GTM, lead generation | `gtm/` |
       | Hiring, onboarding, org design | `hr/` |
       | LinkedIn, webinars, content marketing | `marketing/` |
       | CRM, systems, tools, operations | `operations/` |
       | Call transcripts | `transcripts/` |
       | Recurring strategic discussions | `weekly-calls/` |

       ---

       ## Ingestion Priority Order

       | Priority | Category | Reason |
       |---|---|---|
       | 1 | agreements/ | Highest specificity. Most decisions have explicit rationale. |
       | 2 | applebites/, empire-builder/ | Completely absent from MOS. High gap value. |
       | 3 | deal-analysis/ | Institutional knowledge. Not capturable from any other source. |
       | 4 | operations/ | CRM, systems, and workflow decisions. |
       | 5 | gtm/, marketing/ | Strategic but some overlap with existing MOS modules. |
       | 6 | hr/ | Important but lower urgency. |
       | 7 | emails/, transcripts/ | High volume, lower density. |
       | 8 | weekly-calls/ | Useful but most insights surface in other categories too. |

       ---

       ## Ingestion Status

       | Category | Records | Last Updated | Status |
       |---|---|---|---|
       | agreements/ | 0 | — | Awaiting corpus |
       | applebites/ | 0 | — | Awaiting corpus |
       | empire-builder/ | 0 | — | Awaiting corpus |
       | deal-analysis/ | 0 | — | Awaiting corpus |
       | emails/ | 0 | — | Awaiting corpus |
       | gtm/ | 0 | — | Awaiting corpus |
       | hr/ | 0 | — | Awaiting corpus |
       | marketing/ | 0 | — | Awaiting corpus |
       | operations/ | 0 | — | Awaiting corpus |
       | transcripts/ | 0 | — | Awaiting corpus |
       | weekly-calls/ | 0 | — | Awaiting corpus |

       ---

       ## File Naming

       `[topic-slug]-[YYYY-MM].md`

       Examples:
       - `reverse-lehman-rationale-2025-03.md`
       - - `affiliate-program-structure-2025-06.md`
         - - `ward-engineering-deal-2025-11.md`
          
           - ---

           ## Quality Standards

           - Do not invent content that is not in the conversation.
           - - Do not summarize for brevity at the expense of specific decisions.
             - - Do not omit decisions because they seem minor. The value is in the specifics.
               - - One authoritative synthesis per topic is better than multiple partial records.
                 - - Every record must link to relevant MOS documents where they exist.
                   - - Conflicts with existing MOS documents must be flagged — not silently resolved.
                    
                     - ---

                     ## Related Documents

                     - [INGESTION-GUIDE.md](./INGESTION-GUIDE.md) — Step-by-step operational protocol
                     - - [Migration Log](../migration/migration-log.md) — Audit trail for all ingestion batches
                       - - [ChatGPT Learnings](../chatgpt-learnings.md) — Meta-patterns from AI collaboration
                         - - [Daniel's Operating Model](../daniels-operating-model.md) — How Daniel thinks and works
                           - - [ChatGPT Handoff](../../ai/chatgpt-handoff.md) — Knowledge transfer overview
                            
                             - ---

                             *Part of the [Meritage Operating System](../../../README.md). See [CONTRIBUTING.md](../../../CONTRIBUTING.md) for standards.*
