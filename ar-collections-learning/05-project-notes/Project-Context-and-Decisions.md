# Project Context and Decisions: AR Collections Learning

| Field | Value |
|---|---|
| Topic | D365 Accounts Receivable (AR) Collections |
| Last updated | 2026-10-25 |
| Current focus | Validation of the 13 SME review drafts (clean-session test and SME question pack). Part 2 adds three SME review drafts for Customer payment journal (CPJL) transfers and restorations, and a CPJL controls reference, built from AI-generated notes that still need the recording check. |

This file records the project context drawn from the source documents, inconsistencies found between them, and decisions made during development. Update it whenever a decision is made or a source is added.

---

## 1. Source documents

Sources 0–3.2 are the source of truth for **process content**. Source 4 (the Part 2 update pack) adds working evidence for the Part 2 session: its notes are Teams AI-generated, so they are evidence to check against the recording, not authority (D-035). All sources are held outside this repository and must not be overwritten. T1 and T2 are the source of truth for **PG format and authoring rules**. They are stored unchanged in `/templates`. Always Save As a copy; never edit the master.

| Ref | File | Content | Primary use |
|---|---|---|---|
| 0 | `0. Recommended Learning Structure.txt` | Three-layer learning structure. Inventory of 27 topics with documentation readiness. Proposed PG IDs `PG-AR-001` to `PG-AR-022`. Biggest information gaps. | Topic inventory and initial readiness |
| 1 | `1. Prioritised learning architectur.txt` | P1–P4 priority definitions. Modules 1–12 with learning outcomes, sequences, deliverable types and readiness. Recommended development sequence. Gap-validation checklist (A–L). Publication gate. | Learning architecture, publication gate |
| 2 | `2. D365 AR learning development roadmap.txt` | Release 1–4 roadmap. 32-item prioritised master backlog. Cross-release workstreams (screenshots, business rules, references, assurance). Development gates. Definitions of ready. | Delivery roadmap and gates |
| 3.1 | `3.1 Recommended first drafting batch.txt` | First drafting batch (6 PGs), second batch hold list, "do not draft as final" list. | Drafting order |
| 3.2 | `3.2 Configure AR Collections Favour.txt` | Baseline draft v0.1 of the Favourites PG. Screenshot plan with timestamps, captions and callouts. | Baseline for the first PG |
| 4.0 | `00_Source_Notes_Part1_and_Part2.docx` (in `AR_Training_D365_Part2_Update_Pack.zip`) | Source status, and the Part 1 and Part 2 topic inventories from Teams AI-generated meeting notes. Customer Pools finding. | Part 2 evidence (to check against the recording) |
| 4.1 | `01_Updated_Learning_Architecture.docx` | Architecture change from Part 2: a Customer Payment Journals module (Priority 2) and customer account transfers (Priority 3). | Learning architecture update |
| 4.2 | `02_Updated_Development_Roadmap.docx` | Releases 1, 2, 3A, 3B and 4, numbered 1 to 23. Release 3A: CPJL and transfers. | Roadmap update |
| 4.3 | `03_Updated_Readiness_and_Gap_Matrix.docx` | Readiness of each Part 2 topic. The CPJL validation checklist (14 checks) and the Customer Pools checklist (7 checks). | Readiness and validation |
| 4.4 | `04_PG_Draft_Transfer_Funds_Between_Customer_Accounts.docx` | Working PG draft: 15 steps. | Baseline for the Transfer Funds guide |
| 4.5 | `05_PG_Draft_Parent_to_Child_Account_Transfer.docx` | Working PG draft: 11 steps, with partial allocation. | Baseline for the Parent Payment guide |
| 4.6 | `06_PG_Draft_Restore_Written_Off_Overpayment.docx` | Working PG draft: 13 steps. | Baseline for the Restore guide |
| 4.7 | `07_Claude_Code_Handover_Prompt.txt` | Tasks and source discipline for the Part 2 batch. | Instructions, not process evidence |
| T1 | `PG_Word_Template-MASTER TEMPLATE.docx` (in [`/templates`](../../templates/)) | The master Word template currently in use: cover, contents, version history, About this guide, Parts 1–3, Additional Resources, boundary rows and styles. | **Governs PG format and output** |
| T2 | `PG_Template_Authoring_Guide_v1.docx` (in [`/templates`](../../templates/)) | Companion authoring handbook: section-by-section content rules, the action-row pattern, the standard navigation pattern, the question log, Word maintenance and the final checklist. | **Governs PG authoring rules** |

The underlying evidence for all sources is the *AR Training D365* session recording and transcript. Source 4 covers Part 2 of the same session.

---

## 2. Project objective

Build a role-based AR Collections learning pathway in D365. It is made of granular Procedure Guides (PGs) and supporting learning content. It enables learners to:

1. Navigate the correct D365 environment.
2. Identify and prioritise collection work.
3. Investigate customer accounts.
4. Contact customers and record collection activity.
5. Process allocations and settlements.
6. Perform controlled financial adjustments.
7. Maintain customer information and manage exceptions.

(Source 2, roadmap objective.)

Each PG covers **a single granular D365 task and its associated controls**. Learning modules stay learner-focused (source 1).

## 3. Intended audience

- **Primary:** New AR Collections users (Collections officers) learning to perform routine AR Collections work in D365.
- **Entry point:** Release 1 gives a new AR Collections user enough capability to enter the correct legal entity, configure their workspace, review overdue accounts, investigate a customer and record collection activity (source 2).
- **Out of scope for this audience until confirmed:** Direct debit and credit card administration. These were explicitly excluded from the training session (source 1, checklist L).

## 4. Learning architecture

### 4.1 Content types (source 0)

- Learning modules
- Procedure Guides (PGs)
- Knowledge articles
- Reference guides
- Business rules

Source 1 also uses: system overview, guided practice, microlearning, knowledge note or lesson, decision aid, template and critical control.

### 4.2 Three-layer structure (source 0)

| Layer | Focus |
|---|---|
| Learning Module 1: D365 AR Collections Fundamentals | Legal entities, workspaces, Credit and Collections workspace, Favourites and personalisation, views, customer navigation |
| Learning Module 2: AR Collections Operations | Overdues, activities, accounts, transactions, statements, ageing, settlement, allocation, unallocated payments, write-offs, notes, exclusions, maintenance, reporting |
| Learning Module 3: Advanced AR Administration | Customer master, contacts, addresses, letter and statement controls, payment terms, D365 ↔ CargoWise synchronisation, journal approval workflow |

### 4.3 Prioritised modules (source 1)

| Priority | Definition | Modules |
|---|---|---|
| P1 | Day-one capability. Needed before a user can safely begin routine AR work. | 1 Navigate the AR Collections environment; 2 Configure D365 for efficient AR work |
| P2 | Core operational capability. Needed to manage collections and allocations independently. | 3 Review the AR collections workload; 4 Investigate a customer account; 5 Record and manage collection activity; 6 Generate customer documents; 7 Investigate unallocated payments; 8 Settle customer transactions |
| P3 | Controlled financial processing. Higher-risk tasks involving settlement, write-offs or approvals. | 9 Process customer write-offs |
| P4 | Administration and exceptions. Less frequent work needing more business knowledge or validation. | 10 Maintain customer contact and address details; 11 Manage customer collection controls; 12 Reference, reporting and data extraction |

The Favourites PG sits in **Module 1, sequence 1.5** ("Add required AR pages to Favourites"). It is supported by **1.6**, a guided practice that opens each of the four pages.

### 4.4 Part 2 update (source 4.1)

Part 2 closes the evidence gap for customer account transfers and Customer payment journals. It does **not** close the gap for Customer Pools (D-035).

| Area | Before Part 2 | After Part 2 |
|---|---|---|
| Customer payment journal (CPJL) | Named only as a Favorites page; its use was open (Favorites `VG-18`) | Priority 2 module: purpose, descriptions, line coding, currency, offsets and validation. Reference drafted. |
| Transfer funds between customer accounts | Not ready (source 2 rank 27, Release 4) | Strong PG candidate: two balanced lines, bank-to-bank transfer clearing offset. Working draft. |
| Parent payment across child accounts | Not ready; "do not draft" (section 6) | Strong PG candidate: one parent debit, several child credits. Working draft. |
| Partial parent-account allocation | Not covered | Covered: move only the confirmed amount; the residual stays on the parent with a note. Part of the Parent Payment guide (D-039). |
| Restore a written-off or overpayment amount | Not covered | Strong PG candidate: customer credit, Overpayment ledger offset. Working draft. |
| Simulate Posting | Not covered | Shared control: in the reference and each guide's validate-and-post steps (D-039). |
| Identify parent-child relationships | Not ready (rank 26) | Still partial. Part 1 notes: D365 has no reliable indicator (`PC-01`). |
| Customer Pools | Not in the backlog | Not ready. Validation backlog only ([register](../03-validation/Customer-Pools-Validation.md)). |

## 5. Development priorities

### 5.1 Releases (source 2)

| Release | Goal | Backlog ranks |
|---|---|---|
| 1 | Minimum viable AR Collections pathway | 1–10 (orientation, legal entities, workspace, favourites, views, overdues, aged balances, account investigation, notes and activities, record activity) |
| 2 | Payment, settlement and customer documents | 11–17 |
| 3 | Financial controls and customer administration | 18–25 |
| 4 | Exceptions and specialist processes | 26–32 |

### 5.2 Drafting order (source 3.1)

**First batch:**

1. Configure AR Collections favourites
2. Create and save a personalised D365 view
3. Review customer aged balances
4. View and download a customer invoice
5. Export all rows from a D365 grid
6. Review customer notes and activities

All six are drafted as SME review drafts (October 2026).

**Second batch (limited validation needed), drafted:** switch legal entities, navigate the workspace, review overdue customers, investigate a customer account, record a collection activity, preview and download a statement, generate and send a statement.

**Do not draft as final:** settle or undo transactions, write-offs, write-off journal submission, customer contact or address maintenance, customer exclusions, payment terms, parent-child fund transfers, direct debit and credit cards.

**Part 2 drafts (October 2026):** transfer funds between customer accounts, transfer a parent account payment across child accounts, and restore a written-off or overpayment amount, plus the CPJL controls reference. All four are v0.1 SME review drafts in the master template (D-041). The "do not draft as final" rule still applies to them.

### 5.3 Part 2 roadmap (source 4.2)

Source 4.2 renumbers the roadmap 1 to 23 and splits Release 3. The source 2 backlog ranks stay the project's IDs (I-10). New items take ranks from 33.

| Part 2 item | Deliverable | Release | Source 2 rank | Project position |
|---|---|---|---|---|
| 14 | Understand Customer Payment Journals (CPJL) | 3A | New (35) | Reference: SME review draft (D-041, D-042) |
| 15 | Transfer funds between customer accounts | 3A | 27 | PG SME review draft (D-041); moved from Release 4 to 3 (D-036) |
| 16 | Transfer a parent-account payment across child accounts | 3A | New (33) | PG SME review draft (D-041) |
| 17 | Handle a partial parent-account allocation | 3A | — | Covered in item 16 (D-039) |
| 18 | Restore a written-off or overpayment amount | 3A | New (34) | PG SME review draft (D-041) |
| 19 | Validate a CPJL using Simulate Posting | 3A | — | Covered in the reference and items 15, 16 and 18 (D-039) |
| 20 to 23 | Write-offs, write-off journal, contacts and addresses, exclusions | 3B | 18 to 25 | Unchanged: not drafted |
| Release 4 | Customer Pools; parent-child identification; payment terms; direct debit and credit cards; custom transaction report; daily bank statements | 4 | New (36); 26; 30; 31 and 32; 28; 29 | Customer Pools added as a validation item only (D-035). Others unchanged. |

## 6. Draft-ready vs validation-blocked content

| Category | Meaning | Rule |
|---|---|---|
| **Ready to draft** | Meets the definition of ready for drafting (source 2): clear task boundary, known starting path, actions demonstrated, exact labels available, gaps recorded, module assigned. | May be drafted. Gaps go into the validation register. |
| **Draft ready, publication blocked** | Can be drafted from the recording, but has unresolved business rules, approvals or cross-system effects. Examples: unallocated payments, write-offs, contact maintenance. | Draft only as a working draft. Do **not** finalise until the listed gaps are validated. |
| **System steps ready, governance blocked** | The system steps are demonstrated, but reasons, approvals, documentation or review controls are missing. Example: exclude from credit management. | Same as above. |
| **Partial / Not ready** | The process was discussed but not demonstrated in enough detail. Examples: bank statements, payment terms, Customer Pools, parent-child identification. (Parent-child *transfers* moved to "draft ready, publication blocked" with the Part 2 evidence, D-035.) | Do not draft a PG. Collect evidence first (SME playback or a new recording). |
| **Ready for publication** | Meets the definition of ready for publication and passes the 20-point publication gate (sources 1 and 2). | May be published after process-owner approval. |

Development gates (source 2): Identified → Source reviewed → Gap validated → Drafted → System tested → SME validated → Process-owner approved → Published.

---

## 7. Source inconsistencies identified

| # | Inconsistency | Sources | Working position |
|---|---|---|---|
| I-01 | Readiness ratings differ. Source 0 marks write-offs, customer master maintenance, synchronisation and exclusions as "✅ Yes". Sources 1, 2 and 3.1 mark them as publication-blocked or partial. | 0 vs 1, 2, 3.1 | The stricter, later assessment governs (D-004). |
| I-02 | Release placement differs. Source 1's "Release 1" includes statements, unallocated payments and settlement. Source 2 puts these in Release 2. | 1 vs 2 | Source 2 governs release packaging (D-004). |
| I-03 | Drafting order differs from backlog rank. Source 3.1 drafts some Release 2 items (invoice, export) before Release 1 items (legal entities, workspace). | 2 vs 3.1 | Source 3.1 governs drafting order. Source 2 governs release packaging (D-005). |
| I-04 | PG IDs. Source 0 numbers PGs `PG-AR-001` to `022` in topic order (Favourites = `PG-AR-010`). This does not match the source 2 backlog ranks (Favourites = rank 4). | 0 vs 2 | ID scheme not yet decided (D-006). |
| I-05 | "Age Balances" (source 0) vs "Aged balances" (sources 1, 2, 3.1, 3.2). | 0 vs others | "Aged balances" is provisional. Validate (`VG-01`). |
| I-06 | "Credit & Collections" (source 0) vs "Credit and collections" (module) vs "Customer Credit and Collections" (workspace). | 0, 1, 2, 3.2 | Module and workspace are kept distinct. Validate (`VG-21`). |
| I-07 | The Favourites PG title varies across all five sources. | 0, 1, 2, 3.1, 3.2 | Title from the task brief is used (D-002). |
| I-08 | Source 0 lists "Persist Views Across Legal Entities" as covered. Source 1 marks view scope "Ready with validation". Source 3.1 says to phrase it exactly as demonstrated and validate it. | 0 vs 1, 3.1 | Treat as a validation item in the Views PG. Do not carry it into the Favourites PG. |
| I-09 | Release placement of transfers. Source 2 ranks *Transfer funds between accounts* 27, in Release 4 (not ready). Source 4.2 puts transfers and restoration in Release 3A. | 2 vs 4.2 | Part 2 supplies the evidence that blocked them, so they move to Release 3 (D-036, proposed; `SRC-04`). |
| I-10 | Numbering. Source 4.2 numbers its roadmap 1 to 23, which does not match the source 2 backlog ranks 1 to 32. | 2 vs 4.2 | Source 2 ranks stay the IDs. New Part 2 items take ranks 33 to 36 (D-036). |
| I-11 | Source 4.2's Release 1 lists seven items. It leaves out orientation, legal entities and workspace (source 2 ranks 1 to 3), which are in source 2's Release 1. | 2 vs 4.2 | Not a removal. Source 2 governs Releases 1 and 2. The Legal Entities and Workspace drafts keep their place. |
| I-12 | Date rule wording. The transfer draft says a wrong-account correction may use the original payment date "when appropriate". The restore draft says to use a prior-period date only when required and the period is open. | 4.4 vs 4.6 | Both kept as stated in the notes. One rule to confirm (`CPJ-05`). |
| I-13 | Blank fields and dimensions. "Leave financial tags, invoice number and bank account blank" and "do not change pre-populated dimensions" are stated for restoration entries only. | 4.6 vs 4.4, 4.5 | Steps in the Restore guide only. Questions for the transfer guides (`CPJ-10`, `CPJ-11`). |
| I-14 | Source 4.1 has two "Priority 3" sections (customer account transfers; controlled financial processing), and lists restoration under the second. Source 4.2 puts restoration in Release 3A with the transfers. | 4.1 vs 4.2 | Source 4.2 governs packaging, as source 2 does for earlier releases (D-005). |
| I-15 | Source 4.3 rates transfers and restoration as strong candidates, while source 4.0 says all Part 2 content must be validated against the recording. | 4.0 vs 4.3 | Strong *draft* candidates only. Nothing is publishable until the recording check (`SRC-01`). |

---

## 8. Decisions log

| ID | Date | Decision | Rationale | Status |
|---|---|---|---|---|
| D-001 | 2026-10-08 | The attached source documents are the source of truth. No D365 steps, labels, business rules, approvals or behaviour are added without evidence. Anything uncertain becomes a `VG-xx` validation gap. | Task brief evidence rules | Adopted |
| D-002 | 2026-10-08 | Working title for the first PG: **Configure AR Collections Favourites in D365**. | Task brief; reconciles I-07 | Adopted (final title under `VG-22`) |
| D-003 | 2026-10-08 | Folder structure: `01-procedure-guides`, `02-screenshot-registers`, `03-validation`, `04-quality-assurance`, `05-project-notes`, under a topic folder (`ar-collections-learning`). | Task brief | Adopted |
| D-004 | 2026-10-08 | Where readiness or release placement conflicts, the later and stricter assessment governs (sources 1 and 2 over source 0). | Conservative publication control | Adopted |
| D-005 | 2026-10-08 | Source 3.1 governs drafting order. Source 2 governs release packaging. | I-03 | Adopted |
| D-006 | 2026-10-08 | PG ID scheme to be decided. Option A: keep source 0 IDs (`PG-AR-010`). Option B: renumber to the source 2 backlog rank. Until decided, files use descriptive names (`PG-AR-<Task-Name>`). | I-04 | **Open** |
| D-007 | 2026-10-08 | Validation gaps use IDs scoped to each PG (`VG-01`…). Each PG has its own validation register. | Traceability | Adopted |
| D-008 | 2026-10-08 | Figures are numbered per PG and mapped to steps in a separate screenshot register. The PG holds placeholders until frames are approved. | Task brief | **Amended by D-017**: no placeholders in the Word PG |
| D-009 | 2026-10-08 | Working format is editable Markdown. Prose uses UK/AU English. UI labels match the D365 screen exactly. | Task brief; source spelling | **Superseded by D-013**. PG text is US English. Working notes may keep UK/AU spelling. |
| D-010 | 2026-10-08 | Legal entity confirmation is a **prerequisite**, not a procedure step, in non-transactional PGs. It stays a procedure step in transactional PGs (source 2 control). | Source 2 control applies "before performing a transaction" | **Superseded by D-015** |
| D-011 | 2026-10-08 | Do not create separate "Locate X" steps. Location information goes in the Description of the action step. | One-action-per-step rule; finding D1 | Proposed for template |
| D-012 | 2026-10-08 | Recording frames confirm locations. Publication screenshots are recaptured in a clean session unless a frame fully supports the step. | Pre-existing favourites in recording | Adopted |
| D-013 | 2026-10-08 | PGs are produced in the **PG master template** (T1) following the **authoring guide** (T2). This retires the provisional 16-section Markdown structure. The Word `.docx` is the editable source. The Markdown file in `01-procedure-guides` is a read-only preview, updated after the Word file. PG text uses English (United States). | User direction; T2 "Prepare the working file" | Adopted |
| D-014 | 2026-10-08 | First PG: process name **AR Collections Favorites**, giving cover title *D365 F&O: AR Collections Favorites Procedure Guide*. Single standalone topic **1. Configure AR Collections Favorites**. File name `TBC-AR Collections Favorites PG v0.2.docx`. `TBC` stands in for the unassigned guide code. | T2 naming and topic rules; `VG-22` | Provisional |
| D-015 | 2026-10-08 | Use the template's standard navigation pattern in every procedure: *Check* the **Entity**, then *Click* **Modules**. For Favorites, the effect of legal entity is unconfirmed, so Step 1 carries `VG-23`. | T2 "Use the standard navigation pattern" | Adopted |
| D-016 | 2026-10-08 | The validation register is the guide's question log. `VG-xx` IDs stay stable and are used in place of `Qxx`. Open items affecting the text are added as Word comments (author "Validation register") anchored to that text. | T2 "Separate writing decisions from missing facts" | Adopted |
| D-017 | 2026-10-08 | No screenshots or placeholders in the Word PG until menu locations are confirmed. Then insert only the figures that add context, using the screenshot register. | T2 "Screenshots are optional" | Adopted |
| D-018 | 2026-10-08 | The template has no Troubleshooting section. Troubleshooting content is dropped, and the supported escalation route (D365 issue form, from Additional Resources) moves into the relevant procedure row. | T2 "Retain the standard support content" | Adopted |
| D-019 | 2026-10-14 | Second PG: process name **AR Collections Personalized Views**. Topic 1 *Create a Personalized View* is a parent topic with four subtopics (Arrange the Columns; Filter the List, optional; Add a Footer Total, optional; Save and Pin the View). Topic 2 *Update a Saved View* is standalone. File name `TBC-AR Collections Personalized Views PG v0.1.docx`. | T2 topic-structure rules; sources 1, 2, 3.1 | Provisional (`VG-24`, `VG-28` in its register) |
| D-020 | 2026-10-14 | Where a control label or location was not captured, the step names the user action without inventing a label. Each such step carries a Word comment and a VG item. | T2 "Separate writing decisions from missing facts" | Adopted |
| D-021 | 2026-10-14 | Third PG: process name **AR Collections Aged Balances**. Two standalone topics: *Review Customer Aged Balances* (Currency column, zero-balance filter, descending sort) and *Filter Aged Balances by Customer or Currency*. Aging indicators are excluded until validated. Opening a customer belongs to the *Investigate a customer account* guide. | Sources 1, 2, 3.1; T2 topic rules | Provisional (`VG-10`, `VG-17`, `VG-23` in its register) |
| D-022 | 2026-10-14 | Start each new topic and Part on a new page with the heading's *page break before* setting, not a page-break paragraph. This avoids stray blank pages when a table ends at the foot of a page. | Render review of the Aged Balances guide | Adopted |
| D-023 | 2026-10-14 | Fourth PG: process name **AR Collections Customer Invoices**. One parent topic, *View and Download a Customer Invoice*, with subprocedures *Open the Invoice Preview* and *Download the Invoice as PDF* (optional). The path to the customer's transactions is not invented; step 1.1.2 names the action only. Finding invoices with Show closed or Hide FX revaluations belongs to the *Review customer transactions* guide. Sending the invoice to the customer is out of scope. | Sources 0, 1, 2, 3.1; T2 parent-topic pattern | Provisional (`VG-01`, `VG-16`, `VG-21`, `VG-22` in its register) |
| D-024 | 2026-10-14 | Fifth PG: process name **AR Collections Export to Excel**. One standalone topic, *Export All Rows from a Grid*. As a utility task performed on many pages, it opens "the page that holds the data" after the Entity check instead of one Modules/Navigate path. No export volume limit is stated until confirmed. The custom all-customer transaction report and bank statements are separate guides. | Sources 0, 1, 2, 3.1; T2 topic rules | Provisional (`VG-06`, `VG-10`, `VG-15`, `VG-20` in its register) |
| D-025 | 2026-10-14 | Sixth PG: process name **AR Collections Notes and Activities**. Two standalone topics: *Review Customer Notes* (Notes in the Customer credit and collections workspace, filtered by customer, then optionally by creator, date or note type) and *Review All Customer Activities* (All customers, then View all activities). System-generated entries are described in general terms only. Recording a new activity belongs to the *Record a collection activity* guide. | Sources 0, 1, 2, 3.1; T2 topic rules | Provisional (`VG-05`, `VG-17`, `VG-22` in its register) |
| D-026 | 2026-10-14 | First second-batch PG: process name **AR Collections Legal Entities**. Two standalone topics: *Switch Legal Entity with the Selector* and *Switch Legal Entity Using the Ledger Code*. Neither starts with the standard Entity/Modules rows, because the switch is the task; each ends by confirming the active legal entity. No URL parameter or example code is given until confirmed. Persistence of Favorites and views across legal entities is not stated. | Sources 0, 1, 2, 3.1; T2 topic rules | Provisional (`VG-05`, `VG-07`, `VG-12`, `VG-17` in its register) |
| D-027 | 2026-10-14 | Second second-batch PG: process name **AR Collections Workspace**. Two standalone topics: *Open the Customer Credit and Collections Workspace* (Entity, then **Workspaces** in place of **Modules**) and *Locate Collection Work in the Workspace* (the four sections source 2 names as relevant, each referred to its own guide). Other sections are named without saying whether they are used; indicators are out of scope. | Sources 0, 1, 2, 3.2; T2 navigation pattern | Provisional (`VG-08`, `VG-13`, `VG-17` in its register) |
| D-028 | 2026-10-14 | Third second-batch PG: process name **AR Collections Overdue Customers**. Two standalone topics: *Review Customers Overdue* (Workspaces, then Customers overdue, aging period, sort, optional email column, compare balance due with overdue amount) and *Check an Overdue Balance Before Contact* (open the account, review the balance, check low-value balances for fees or overpayments, contact only when valid). No order for working accounts is given until the prioritization rules are confirmed. Aging indicators are deferred. | Sources 0, 1, 2, 3.1; T2 topic rules | Provisional (`VG-08` to `VG-11`, `VG-17` in its register) |
| D-029 | 2026-10-14 | Fourth second-batch PG: process name **AR Collections Customer Account**. One parent topic, *Investigate a Customer Account*, with subprocedures *Open the Customer Account*, *Review Customer Transactions* and *Review Settlement History* (optional). Source 0's three suggested guides (PG-AR-005, -015, -017) become its subprocedures. Settlement history is review-only: **Undo settlement** is excluded as a higher-risk action. Notes, activities and invoices are referred to their own guides. | Sources 0, 1, 2; T2 parent-topic pattern; settlement gating rule | Provisional (`VG-13`, `VG-15`, `VG-19` in its register) |
| D-030 | 2026-10-14 | Fifth second-batch PG: process name **AR Collections Collection Activities**. One standalone topic, *Record a Customer Collection Activity*: All customers, open the account, New activity, type, summary, notes, save, check it is listed. Activity types are given as examples only, and no mandatory or prohibited note content is stated until the collection-note standard exists. | Sources 0, 1, 2; T2 topic rules | Provisional (`VG-05`, `VG-06`, `VG-09`, `VG-10`, `VG-19` in its register) |
| D-031 | 2026-10-14 | Sixth second-batch PG: process name **AR Collections Statement Preview**. One parent topic, *Preview and Download a Customer Statement*, with *Generate the Statement Preview* (Only open, company logo, clear Print management destination, Screen destination, generate, review) and *Download the Statement as PDF* (optional). Preview and send are separate guides; checking that Print management destination is cleared is a Key concept rule. | Sources 0, 1, 2; Customer Invoices pattern | Provisional (`VG-05`, `VG-19`, `VG-24` in its register) |
| D-032 | 2026-10-14 | Last second-batch PG: process name **AR Collections Statement Distribution**. One parent topic, *Generate and Send a Customer Statement*, with *Send the Statement* (Only open, company logo, Print management destination, generate) and *Verify Statement Delivery* (delivery message, Collections sent mailbox where required, failed-delivery process). Checks before sending are Key concept rules. As a customer-facing guide, it is not tested on real customers until the parameter, recipient, multi-currency and failed-delivery items close. | Sources 0, 1, 2, 3.1 | Provisional (`VG-05`, `VG-06`, `VG-10`, `VG-12`, `VG-17`, `VG-21` in its register) |
| D-033 | 2026-10-15 | Validate all 13 guides in **one clean-session D365 test**, run as a single route that visits each page once (menus once in S2; the Aged balances grid reused for the export). Every open Test-method item is assigned to exactly one step. Safety rules: test customer only, no financial changes (S9 read-only), nothing sent to a customer (S12 uses Screen; S13 gated), mock note text, missing controls recorded as possible security causes. | Validation registers; D-016; brief rules on security diagnosis | Proposed (plan awaiting SME review) |
| D-034 | 2026-10-15 | Collect all non-test answers through one **SME question pack**: each shared rule is asked once and applied to every guide that uses it. Every open item whose method includes SME, Rec or Dec maps to exactly one answer row (191 items, 119 blocking); Test-only items stay with the test plan (D-033). Scope boundaries are put to the BPO as the drafts' current choice, not as settled. Answers close register items only when recorded with name and date. | Validation registers; D-016; D-033 | Proposed (pack awaiting SME answers) |
| D-035 | 2026-10-23 | Part 2 (source 4) closes the evidence gap for **Customer payment journals and customer account transfers**: transfer between customers, parent to multiple children, partial allocation, restoration through the Overpayment ledger, and Simulate Posting. These move from "partial / not ready" to "draft ready, publication blocked". It does **not** close the **Customer Pools** gap: Customer Pools stays a validation backlog item with no PG ([register](../03-validation/Customer-Pools-Validation.md)). The Part 2 notes are Teams AI-generated, so every Part 2 statement is labelled as stated in the notes and stays unconfirmed until checked against the recording. The example amounts in the notes ($100; $10,000, $8,000 and $2,000) are examples, not thresholds. | Source 4 and its handover (4.7); D-001; D-004 | Adopted |
| D-036 | 2026-10-23 | Release placement: *Transfer funds between accounts* (rank 27) moves from Release 4 to Release 3, with the new Part 2 items. Source 2 ranks stay the project's IDs. New items: rank 33 *Transfer a parent account payment across child accounts*, 34 *Restore a written-off or overpayment amount*, 35 *Customer Payment Journal controls reference*, 36 *Customer Pools* (validation only). Nothing previously drafted is moved or removed. | I-09, I-10, I-11 | Proposed (confirm with the BPO, `SRC-04`) |
| D-037 | 2026-10-23 | The three Part 2 guides and the reference start as **working Markdown drafts**. They follow the master template's section order and boundary rows, so the Word build is mechanical, but they are not built in Word until the Part 2 recording is checked. This is an exception to D-013 (Word is the editable source) for unchecked AI-note evidence. Once built, the Word file becomes the editable source and the Markdown file becomes its preview. | Handover task 5; avoids Word review comments on unchecked notes | **Amended by D-041**: the Word build was brought forward |
| D-038 | 2026-10-23 | One validation register covers the three Part 2 guides and the reference, because most items are shared. IDs are prefixed by scope (`SRC`, `GOV`, `CPJ`, `TF`, `PC`, `RO`) instead of a per-guide `VG-xx` sequence. Customer Pools uses `CP-xx` in its own register. This amends D-007 for this batch only. | Handover suggested files; traceability | Adopted |
| D-039 | 2026-10-23 | Part 2 roadmap item 17 (partial allocation) is part of the Parent Payment guide. Item 19 (Simulate Posting) is a shared control in the reference and in each guide's validate-and-post subprocedure. Neither is a separate guide unless the recording shows steps beyond these. | No steps beyond those already in the guides | Adopted |
| D-040 | 2026-10-23 | New folder `06-reference-guides` for reference content (a source 0 content type). The first entry is the CPJL controls reference, limited to controls the Part 2 notes support. | Handover suggested files | Adopted |
| D-041 | 2026-10-25 | At the user's request, the three Part 2 guides are built in the PG master template as **v0.1 SME review drafts** before the recording check. Process names: **AR Collections Customer Account Transfers**, **AR Collections Parent Payment Distribution** and **AR Collections Overpayment and Write-Off Restoration**. Each has one parent topic with subprocedures (three, three and two). Every procedure starts with the full standard navigation pattern (Entity, Modules, then Navigate to **Customer payment journal** under **Credit and collections**), which adds a step to each first subprocedure. Open items become Word comments that start with their register ID. The Word file is now the editable source and the Markdown file its preview, which also keeps a step-evidence table. The recording check (`SRC-01`) still blocks testing on real accounts and publication. | User request; D-013; D-015; D-020 | Adopted |
| D-042 | 2026-10-25 | The CPJL controls reference is built from the master template as a **Reference Guide** (title changed from "Procedure Guide"). Its controls sit in Part 1 *Key concepts* tables (Journal set-up, Line coding, Validation and posting, Allocations and amounts, Not covered by this reference). Part 2 lists the three guides instead of procedures. Files sit in `06-reference-guides`. | D-040; the template has no reference layout | Adopted |
| D-043 | 2026-10-25 | Collect the Part 2 and Customer Pools answers through a **Part 2 supplement** to the SME question pack, with `P2-` question IDs so it never clashes with the main pack. Every open item whose method includes SME, Rec or Dec maps to exactly one question (50 items, 42 blocking). The three Test-only items (`CPJ-06`, `CPJ-08`, `CPJ-13`) wait for a controlled Customer payment journal test, which the clean-session test plan does not include yet. | D-034; D-035 | Proposed (supplement awaiting SME answers) |

---

## 9. Proposed reusable PG template elements (superseded)

> **Superseded by D-013.** The PG master template (T1) and authoring guide (T2) are now the standard. The list below is kept for traceability. Elements 1–2 and 15–16 continue as project-level working files: the status tracker, validation register and screenshot register. The rest are replaced by the template's own components.

These elements came from the Favourites PG. They are candidates for the standard PG template, to confirm after the second PG (*Create and save a personalised D365 view*) tests them against a more complex task.

1. **Draft banner.** A "DRAFT — NOT FOR PUBLICATION" notice that points to the validation notes.
2. **Document status block.** PG ID, version, status, development gate, learning module and sequence, release and backlog rank, risk rating, evidence source with timestamp range, last updated.
3. **The 16-section structure** from the task brief.
4. **Scope table** with in-scope bullets and an out-of-scope table that points to where each topic is covered.
5. **Prerequisites** in the standard order: sign-in, legal entity (with its D-010 placement), module or page access, interface state. Includes a standard security-access note phrased as a possibility.
6. **Navigation path table** (Page | Path), with a standard note when intermediate menu groups are not captured.
7. **Procedure in parts.** Each part has a short heading and a Step / Action / Description table. Steps are numbered continuously across parts. Each part ends with a one-line **Part result**.
8. **Step-writing rules.** One action per step, starting with a verb. **Bold** UI labels. Location in the Description. Expected system response only where supported. VG IDs inline.
9. **Figure placeholder block.** `> **[Figure n placeholder]** <caption text>. See screenshot register.`, placed directly after its step.
10. **Warning placeholder block.** For warnings that depend on an unresolved VG item, placed immediately before the consequential step.
11. **Expected results** with a "Not yet confirmed" line for excluded behaviour.
12. **Verification checklist** using Markdown checkboxes.
13. **Troubleshooting table.** Issue | Possible causes | What to do, with standard rows: missing module, missing page, action did not take effect. Includes the standard "do not substitute a similarly named page" guidance.
14. **Related learning content table.** Item | Type | Backlog status.
15. **Draft validation notes** grouped by theme (labels, locations, behaviour, persistence, purpose, access and governance, screenshots), linked to a full validation register.
16. **Companion files** for each PG: screenshot register (summary table, per-figure detail, recapture specification) and validation register (baseline review, VG register, terminology register, publication gate status).
17. **Document control.** Roles, test context (D365 version, security role, legal entity) and version history.

## 10. Next steps

1. **One clean-session D365 test** using the [test plan](../03-validation/Clean-Session-Test-Plan.md): 16 stations and 87 steps that test the 148 open items whose method includes Test (112 blocking) across all 13 registers. Station S13 (sending a statement) is gated on the SME statement controls in step 9. Record results in the [test log](../03-validation/Clean-Session-Test-Log.xlsx).
2. **Recording evidence:** transcript excerpts and timestamps for the views, Aged balances, invoice, export, notes, legal entity, workspace, overdue, customer account, activity and statement demonstrations (Views `VG-27`, Aged Balances `VG-21`, Customer Invoices `VG-20`, Export to Excel `VG-19`, Notes and Activities `VG-21`, Legal Entities `VG-21`, Workspace `VG-21`, Overdue Customers `VG-21`, Customer Account `VG-23`, Collection Activities `VG-23`, Statement Preview `VG-23`, Statement Distribution `VG-25`).
3. **SME answers** through the [SME question pack](../03-validation/SME-Question-Pack.md) and its [response sheet](../03-validation/SME-Question-Pack-Responses.xlsx): 31 questions that cover 191 open items (119 blocking). Answer A1 to A6 first (initiation, stream and role, BPO, reports, security role, review and approval; 78 blocking items). The export volume limit and the handling rule for exported customer data (Export to Excel `VG-06`, `VG-08`) are question B2.
4. Decide the guide codes (D-006) and approve or edit the [PG Delivery Flow](https://claude.ai/artifact/Qb7C1s8Vmnt8av3ams3jrJ).
5. Both drafting batches are complete, and Part 2 adds three working drafts (step 10). Before any further drafting, the priority is validation: the clean-session test (step 1) and the SME answers (steps 3 and 6 to 9). The remaining backlog items are higher-risk (settlement, write-offs, customer maintenance, exclusions, payment terms, account transfers) and stay behind the validation gate (source 3.1).
6. Ask the SME for the **legal entity name and code reference** (source 1). It closes Legal Entities `VG-06` and supports every guide's *Check* the **Entity** row. Pack question **B7**.
7. Ask the SME for the **collections prioritization rules** and the **aging indicator legend** (source 1, checklist A). They close Overdue Customers `VG-11` and `VG-12` and Aged Balances `VG-10`. The prioritization rules are pack question **B4.3**. The aging legend items are deferred, so they are outside the pack until they are reopened.
8. Ask the SME for the **AR collection-note standard** (source 1, open questions B): approved activity types, mandatory and prohibited content, naming convention, and example notes. It closes Collection Activities `VG-05`, `VG-06` and `VG-09` to `VG-11`. Pack questions **B3.1** to **B3.3**.
9. Ask the SME for the **statement controls** (source 2, required validation): approved parameters, recipient source, multi-currency exclusion rules and the failed-delivery process. They close Statement Distribution `VG-05`, `VG-06`, `VG-10`, `VG-12` and `VG-17`, and Statement Preview `VG-03` to `VG-05`. Pack questions **B5.1** to **B5.4**, which also gate test station S13.
10. **Check the Part 2 recording** against the three working drafts and the CPJL reference (`SRC-01`), and record timestamps (`SRC-02`). The guides are already built in the master template (D-041), so update the Word files and their previews from the results. Register: [Part2-CPJL-and-Transfers-Validation.md](../03-validation/Part2-CPJL-and-Transfers-Validation.md) (46 items, 38 blocking).
11. **Part 2 SME answers** through the [Part 2 supplement](../03-validation/SME-Question-Pack-Part2-Supplement.md) and its [response sheet](../03-validation/SME-Question-Pack-Part2-Responses.xlsx): 27 questions for 50 items (42 blocking). Answer **P2-C1** (recording check) first, then **P2-A1** and **P2-A3** (who may post, and approval). Three Test-only items (`CPJ-06`, `CPJ-08`, `CPJ-13`) need a controlled CPJL test in a test environment, not yet in the test plan.
12. **Customer Pools evidence:** supplement question **P2-E1**. A "no" closes most of Part E ([register](../03-validation/Customer-Pools-Validation.md)).
13. Part 2 gives evidence for Favorites `VG-18` (what Customer payment journal is used for). Close it once the recording check confirms it.
