# Business Entities

> Every object Meritage works with, defined once. Each entity has a canonical definition, owner, lifecycle, and relationships to other entities.
>
> ---
>
> ## How to Read This Document
>
> Each entity is documented with five fields:
>
> - **Definition** — What this entity is
> - - **Owner** — Who at Meritage is responsible for this entity
>   - - **Lifecycle** — The states this entity moves through
>     - - **Relationships** — How this entity connects to others
>       - - **Linked documents** — Where this entity is referenced or governed
>        
>         - For plain-language definitions, see [`glossary.md`](glossary.md). For lifecycle stage detail, see [`lifecycle.md`](lifecycle.md). For relationship maps, see [`relationships.md`](relationships.md).
>        
>         - ---
>
> ## People and Organizations
>
> ---
>
> ### Company
>
> **Definition**
> The business being evaluated, represented, or acquired. In a sell-side engagement, the Company is Meritage's client's business. In a buy-side engagement, the Company is the target.
>
> **Owner**
> Principal Advisor assigned to the Engagement.
>
> **Lifecycle**
> `Identified` → `Under Evaluation` → `Engaged` → `Marketed` → `Under LOI` → `In Due Diligence` → `Closed` or `Withdrawn`
>
> **Relationships**
> - Has one or more **Sellers** (owners)
> - - Is the subject of one **Engagement**
>   - - Receives interest from one or more **Buyers**
>     - - Is described in one **CIM**
>       - - May have one or more **Valuations**
>        
>         - **Linked documents**
>         - - `docs/domain/lifecycle.md`
>           - - `docs/m-and-a/` (deal process)
>            
>             - ---
>
> ### Seller
>
> **Definition**
> The individual or group of individuals who own the Company and have engaged Meritage to manage its sale. A Seller is a Client from the moment an Engagement Agreement is signed.
>
> **Owner**
> Principal Advisor.
>
> **Lifecycle**
> `Contact` → `Prospect` → `Client (Seller)` → `Post-Close`
>
> **Relationships**
> - Owns one **Company**
> - - Is party to one **Engagement Agreement**
>   - - Is represented by one **Principal Advisor**
>     - - Interacts with **Buyers** via **Management Call**
>       - - Receives **Valuation** from Meritage
>        
>         - **Linked documents**
>         - - `docs/m-and-a/` (sell-side process)
>           - - `docs/legal/` (Engagement Agreement template)
>            
>             - ---
>
> ### Buyer
>
> **Definition**
> Any party that has signed an NDA and received a CIM for a Company Meritage represents. A Prospective Buyer becomes a Buyer at NDA execution.
>
> **Owner**
> Principal Advisor (who manages the buyer process).
>
> **Lifecycle**
> `Prospective Buyer` → `NDA Signed` → `CIM Received` → `Management Call` → `IOI Submitted` → `LOI Executed` → `Due Diligence` → `Closed` or `Withdrawn`
>
> **Relationships**
> - Pursues one **Company**
> - - Signs one **NDA**
>   - - May submit one **IOI**
>     - - May execute one **LOI**
>       - - May complete **Due Diligence**
>         - - May participate in a **Management Call**
>          
>           - **Linked documents**
>           - - `docs/m-and-a/` (buyer management process)
>             - - `docs/legal/` (NDA template)
>              
>               - ---
>
> ### Client
>
> **Definition**
> Any party — Seller or Buyer — that has a signed Engagement Agreement with Meritage. The term "Client" is used when the distinction between Seller and Buyer is not relevant.
>
> **Owner**
> Principal Advisor.
>
> **Lifecycle**
> `Prospect` → `Client` → `Post-Engagement`
>
> **Relationships**
> - Is either a **Seller** or a **Buyer**
> - - Is party to one **Engagement Agreement**
>   - - May have been introduced by an **Affiliate**
>    
>     - **Linked documents**
>     - - `docs/legal/` (Engagement Agreement)
>      
>       - ---
>
> ### Principal Advisor
>
> **Definition**
> The senior Meritage professional who owns the client relationship for a given Engagement. Responsible for deal execution, client communication, and outcomes. Every Engagement has exactly one Principal Advisor.
>
> **Owner**
> Self-owned (COO assigns at Engagement creation).
>
> **Lifecycle**
> Assigned at Engagement creation. Remains assigned through Close or termination.
>
> **Relationships**
> - Owns one or more **Engagements**
> - - Manages the **Seller** relationship
>   - - Manages the **Buyer** process
>     - - May be supported by one or more **Strategic Growth Advisors**
>      
>       - **Linked documents**
>       - - `docs/executive/executive-manual.md`
>         - - `docs/hr/` (role definition)
>          
>           - ---
>
> ### Strategic Growth Advisor (SGA)
>
> **Definition**
> A senior advisor or operating partner affiliated with Meritage who contributes domain expertise, buyer introductions, or operational support on specific engagements. Not an employee. Compensation is per-engagement.
>
> **Owner**
> COO.
>
> **Lifecycle**
> `Identified` → `Agreement Signed` → `Engaged on Deal` → `Post-Close`
>
> **Relationships**
> - Supports one or more **Engagements**
> - - Reports to **Principal Advisor** on deal matters
>   - - May introduce **Buyers** or **Sellers**
>    
>     - **Linked documents**
>     - - `docs/legal/` (SGA agreement template)
>      
>       - ---
>
> ### Affiliate
>
> **Definition**
> An individual or firm that refers potential Clients to Meritage under a signed Affiliate Agreement. Earns a Revenue Share on transactions resulting from Qualified Introductions.
>
> **Owner**
> COO (manages affiliate relationships).
>
> **Lifecycle**
> `Identified` → `Agreement Signed` → `Active` → `Inactive` or `Terminated`
>
> **Relationships**
> - Makes one or more **Qualified Introductions**
> - - Earns **Revenue Share** on resulting transactions
>   - - Is governed by an **Affiliate Agreement**
>    
>     - **Linked documents**
>     - - `docs/legal/` (Affiliate Agreement template)
>       - - `docs/domain/glossary.md` (Qualified Introduction definition)
>        
>         - ---
>
> ## Transaction Documents
>
> ---
>
> ### Engagement Agreement
>
> **Definition**
> The contract between Meritage and a Client. Defines scope, fees, exclusivity, term, and termination. Required before any advisory work begins.
>
> **Owner**
> Principal Advisor (executes); COO (approves non-standard terms).
>
> **Lifecycle**
> `Draft` → `Sent` → `Negotiating` → `Signed` → `Active` → `Completed` or `Terminated`
>
> **Relationships**
> - Governs one **Engagement**
> - - Binds one **Client** (Seller or Buyer) and Meritage
>   - - Defines the **Success Fee** and any **Retainer**
>    
>     - **Linked documents**
>     - - `docs/legal/` (template)
>      
>       - ---
>
> ### NDA (Non-Disclosure Agreement)
>
> **Definition**
> A confidentiality agreement signed by a Prospective Buyer before receiving the CIM. Required before any material information about the Company is shared.
>
> **Owner**
> Principal Advisor.
>
> **Lifecycle**
> `Sent` → `Signed` → `Active` → `Expired`
>
> **Relationships**
> - Signed by one **Buyer**
> - - Governs access to one **CIM**
>   - - Precedes **Management Call**
>    
>     - **Linked documents**
>     - - `docs/legal/` (NDA template)
>      
>       - ---
>
> ### CIM (Confidential Information Memorandum)
>
> **Definition**
> The primary marketing document for a Company. Prepared by Meritage and distributed to qualified Buyers after NDA signing. Contains financials, business description, market context, and deal structure preferences.
>
> **Owner**
> Principal Advisor.
>
> **Lifecycle**
> `Draft` → `Seller Review` → `Approved` → `Distributed` → `Superseded` or `Withdrawn`
>
> **Relationships**
> - Describes one **Company**
> - - Is distributed to one or more **Buyers**
>   - - Requires a signed **NDA** before distribution
>     - - Precedes **Management Call** and **IOI**
>      
>       - **Linked documents**
>       - - `docs/m-and-a/` (CIM preparation process)
>         - - `docs/templates/` (CIM template)
>          
>           - ---
>
> ### IOI (Indication of Interest)
>
> **Definition**
> A non-binding document from a Buyer expressing preliminary acquisition interest with an indicated price range and structure. Evaluated by Meritage and the Seller to determine which Buyers advance to LOI.
>
> **Owner**
> Principal Advisor.
>
> **Lifecycle**
> `Received` → `Under Review` → `Accepted` or `Declined`
>
> **Relationships**
> - Submitted by one **Buyer**
> - - References one **Company**
>   - - May advance to **LOI**
>     - - Follows **Management Call**
>      
>       - **Linked documents**
>       - - `docs/m-and-a/`
>        
>         - ---
>
> ### LOI (Letter of Intent)
>
> **Definition**
> A semi-binding document executed by Buyer and Seller establishing agreed deal terms, price, structure, exclusivity period, and conditions. Triggers the due diligence period.
>
> **Owner**
> Principal Advisor (negotiates); external counsel (drafts).
>
> **Lifecycle**
> `Draft` → `Negotiating` → `Executed` → `Expired`, `Terminated`, or `Advanced to Close`
>
> **Relationships**
> - Executed by one **Buyer** and one **Seller**
> - - References one **Company**
>   - - Triggers **Due Diligence**
>     - - Precedes **Close**
>      
>       - **Linked documents**
>       - - `docs/m-and-a/`
>         - - `docs/legal/` (LOI template)
>          
>           - ---
>
> ## Deal Stages and Events
>
> ---
>
> ### Opportunity
>
> **Definition**
> A potential Deal that Meritage has identified or been approached about, for which no Engagement Agreement has yet been signed.
>
> **Owner**
> Principal Advisor (or COO until assigned).
>
> **Lifecycle**
> `Identified` → `Qualifying` → `Proposal Sent` → `Engaged` or `Lost`
>
> **Relationships**
> - May involve a **Company** and a **Seller**
> - - May be introduced by an **Affiliate**
>   - - Converts to an **Engagement** upon agreement signing
>    
>     - **Linked documents**
>     - - `docs/m-and-a/` (pipeline management)
>      
>       - ---
>
> ### Deal
>
> **Definition**
> A specific M&A transaction that Meritage is actively advising on under a signed Engagement Agreement.
>
> **Owner**
> Principal Advisor.
>
> **Lifecycle**
> See [`lifecycle.md`](lifecycle.md).
>
> **Relationships**
> - Has one **Company**
> - - Has one **Seller** (or **Buyer** in buy-side)
>   - - Has one **Principal Advisor**
>     - - Produces one **CIM**, one or more **NDAs**, one or more **IOIs**, one **LOI**, and one **Close**
>       - - May involve one or more **SGAs**
>         - - May be sourced by an **Affiliate**
>          
>           - **Linked documents**
>           - - `docs/m-and-a/`
>             - - `docs/domain/lifecycle.md`
>              
>               - ---
>
> ### Management Call
>
> **Definition**
> The first substantive meeting between a qualified Buyer and the Company's management team. Facilitated by Meritage. Typically held after NDA signing and CIM review. A successful Management Call leads to an IOI.
>
> **Owner**
> Principal Advisor (sets agenda and facilitates).
>
> **Lifecycle**
> `Scheduled` → `Completed` → `IOI Received` or `Buyer Withdrawn`
>
> **Relationships**
> - Involves one **Buyer** and one **Company** (Seller team)
> - - Follows **NDA** signing and **CIM** review
>   - - Precedes **IOI**
>    
>     - **Linked documents**
>     - - `docs/m-and-a/management-call-playbook.md` (when created)
>      
>       - ---
>
> ### Due Diligence
>
> **Definition**
> The investigation period following LOI execution. The Buyer (and advisors) verify financial, legal, operational, and commercial claims about the Company. Meritage coordinates the Seller's responses.
>
> **Owner**
> Principal Advisor.
>
> **Lifecycle**
> `Initiated` → `In Progress` → `Completed` → `Advanced to Close` or `Deal Terminated`
>
> **Relationships**
> - Follows executed **LOI**
> - - Involves **Buyer** (and their advisors)
>   - - Meritage coordinates on behalf of **Seller**
>     - - May produce a **QoE** report
>      
>       - **Linked documents**
>       - - `docs/m-and-a/` (due diligence checklist)
>        
>         - ---
>
> ### Valuation
>
> **Definition**
> Meritage's estimate of a Company's Enterprise Value, prepared as part of the engagement process or at Seller request. Expressed as a range. Not a certified appraisal.
>
> **Owner**
> Principal Advisor.
>
> **Lifecycle**
> `Requested` → `In Progress` → `Delivered` → `Revised` or `Superseded`
>
> **Relationships**
> - References one **Company**
> - - Informs the **Engagement Agreement** (floor price expectations)
>   - - Informs **CIM** preparation
>    
>     - **Linked documents**
>     - - `docs/m-and-a/` (valuation methodology)
>      
>       - ---
>
> ## Financial Constructs
>
> ---
>
> ### Success Fee
>
> **Definition**
> The primary fee earned by Meritage at Close, calculated as a percentage of Enterprise Value using the Reverse Lehman Formula.
>
> **Owner**
> COO (fee schedule); Principal Advisor (per-deal terms).
>
> **Lifecycle**
> Accrues at Close. Paid per Engagement Agreement terms (typically at Close or within a short window).
>
> **Relationships**
> - Earned on one **Deal**
> - - Calculated from **Enterprise Value**
>   - - May trigger a **Revenue Share** to an **Affiliate**
>     - - Governed by the **Engagement Agreement**
>      
>       - **Linked documents**
>       - - `docs/m-and-a/reverse-lehman-formula.md` (when created)
>        
>         - ---
>
> ### Revenue Share
>
> **Definition**
> A percentage of the Success Fee paid by Meritage to an Affiliate whose Qualified Introduction resulted in a closed transaction. Amount and terms are defined in the Affiliate Agreement.
>
> **Owner**
> COO.
>
> **Lifecycle**
> Triggered at Close when a Qualified Introduction is confirmed. Paid per the Affiliate Agreement.
>
> **Relationships**
> - Paid to one **Affiliate**
> - - Calculated from the **Success Fee**
>   - - Governed by the **Affiliate Agreement**
>     - - Requires a confirmed **Qualified Introduction**
>      
>       - **Linked documents**
>       - - `docs/legal/` (Affiliate Agreement template)
>         - - `docs/m-and-a/reverse-lehman-formula.md` (when created)
>          
>           - ---
>
> ### Qualified Introduction
>
> **Definition**
> An introduction made by an Affiliate that meets the conditions defined in the Affiliate Agreement, entitling the Affiliate to a Revenue Share if the introduction results in a closed transaction.
>
> **Owner**
> COO (determines qualification).
>
> **Lifecycle**
> `Introduction Made` → `Notice Filed` → `Engagement Signed` → `Qualified` or `Disqualified`
>
> **Relationships**
> - Made by one **Affiliate**
> - - Introduces one **Client** (Seller or Buyer) to Meritage
>   - - If qualified and closed, triggers **Revenue Share**
>    
>     - **Linked documents**
>     - - `docs/legal/` (Affiliate Agreement template)
>       - - `docs/domain/glossary.md`
>        
>         - ---
>
> ## Related Documents
>
> - [`glossary.md`](glossary.md) — Plain-language definitions for all terms
> - - [`lifecycle.md`](lifecycle.md) — Lifecycle stage detail
>   - - [`relationships.md`](relationships.md) — Entity relationship map
>     - - `docs/m-and-a/` — Process documentation for each deal stage
>       - - `docs/legal/` — Contract templates
>        
>         - ---
>
> *Last updated: 2026-06-29*
