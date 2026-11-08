# O2C PG Suite Plan: Where Each AR Collections Task Goes

| Field | Value |
|---|---|
| Rule | One task per topic, inside a process-level guide (D-045). The 17 AR Collections drafts are **topic drafts**: each one merges into a destination guide. |
| Guide codes | From the O2C PG Numbering Standard v1.3 (T3). This plan proposes two new codes: **221** and **260** (D-046). |
| Status | Proposed. **260 and 221 are built as v0.1 working drafts** (D-048). Both are shared with the SME for review only (D-048). Before either circulates further, the register owner records both codes in `O2C_PG_Numbering_Register.json` and its companion, and the BPO confirms the scope of 221 and the split from 230. 230 Collections has a v2.4 draft (the 221 split, D-051) and a v3.0 working draft with the nine topic drafts (D-052). 240 Direct Debit and Credit Card Payments is a v0.1 skeleton (D-053). |
| Last updated | 2026-11-01 |

---

## 1. The rule

- **One D365 task is one topic.** It is a major Part 2 topic, or a subtopic of a parent topic, as the authoring guide (T2) defines them: "A major topic represents a distinct business task or outcome."
- **A guide covers one process family outcome.** Guides are classified by their primary business outcome, as the numbering standard requires.
- **A task lives in one guide only.** Other guides link to it instead of repeating it.
- **General D365 skills go in a Getting Started guide.** Switching legal entity, favorites, views and exports are not process steps. The role-specific part (which pages to favorite, which columns to show) stays in the role's guide, which links to the general steps.
- **Topic drafts keep their working files until they merge.** That covers the TBC Word file, the Markdown preview, the screenshot register and the validation register. Item IDs stay stable after a merge; the destination guide's question log keeps the draft name with each ID, for example *Aged Balances VG-03*.

## 2. Numbering

The numbering standard (T3) allocates codes 200 to 299 to O2C in ten-number families, classified by primary business outcome.

| Range | Family | Current guides |
|---|---|---|
| 200–209 | Customer Master Data | 200 Customer Onboarding and Maintenance |
| 210–219 | Billing and Invoicing | 210 Customer Invoices; 211 Subscription Billing |
| 220–229 | Customer Payments: receipt processing, allocation, settlement and payment corrections | 220 Customer Payments; **221 proposed** |
| 230–239 | Collections: overdue receivables follow-up, collection activity and escalation | 230 Collections |
| 240–249 | Direct Debit and Automated Collections | 240 Direct Debit and Credit Card Payments: v0.1 skeleton (D-053) |
| 250–299 | Reserved for future O2C families, in ten-number blocks | **260 proposed** (new family 260–269) |
| 398, 399 | Shared guides (RCTI Hub grouping), outside the 200-series | 398 RCTI and RCI; 399 Customer and Supplier Netting |

Retired codes are never reused: 201, 202, 203, 205, 250, 298 and 299.

### 2.1 Proposed allocations

| Code | Guide | Family | Why this code |
|---|---|---|---|
| **221** | Customer Payment Corrections | 220–229 Customer Payments | Settlement, transfers between customer accounts, parent payment distribution and restoration are "settlement and payment corrections", which the standard puts in 220–229, not in Collections. 221 is the next free code in the family. |
| **260** | O2C Getting Started | New family 260–269, O2C Getting Started | A getting-started guide has no process family of its own. The standard reserves 250–299 for new O2C families in ten-number blocks. 250 is retired, so 260 is the first block that starts on a usable number ("the first number in a block is a valid guide ID"). |

If other streams later want the same Getting Started guide, it becomes one shared guide with one code, like 398 and 399 ("A shared guide needs one code").

File names follow the standard: `221-Customer Payment Corrections PG v0.1.docx` and `260-O2C Getting Started PG v0.1.docx` for the working Word files, and `NNN-Guide Title PG.pdf` once published.

### 2.2 Predecessor mapping

The standard requires a predecessor mapping for a split ("A split into distinct procedures needs separate codes and a predecessor mapping").

| From | To | Reason |
|---|---|---|
| 230 §6.5 Settling Customer Accounts | 221 topic 1 | Settlement: 220–229 |
| 230 §6.6 Unsettling Customer Accounts | 221 topic 2 | Settlement correction: 220–229 |
| 230 §6.7 Transferring Open / Closed Payments | 221 topic 3, replaced by the Transfers topic draft | Payment correction: 220–229 |
| 230 §6.8 Bank Fees Write-off Process | 221 topic 6 | Clears payment residuals (fees, FX, minor variances): a payment correction |
| 230 §2.4 Maintain Customer Direct Debit & eBanking Details | 240 topic 1 | Mandate management: 240–249. 230 keeps the topic as a link to 240 topic 1 (D-053); published 230 keeps the steps until 240 is published. |
| 220 §5 Process Direct Debit Customer Payments | 240 topic 2 | Direct debit processing: 240–249. 220 links to 240 once it is published (D-053). |

230 §6.4 Debt Write-off stays in 230. Writing off an uncollectible debt is a collections escalation outcome.

---

## 3. The suite at a glance

| Guide | Change | Receives |
|---|---|---|
| **260 O2C Getting Started** | New (proposed). v0.1 working draft built (D-048) | Legal Entities, Export to Excel, and the general steps from Favorites and Personalized Views |
| 200 Customer Onboarding and Maintenance | None from the drafts | Keeps contact, address and payment-terms maintenance (backlog ranks 21 to 23 and 30) |
| 210 Customer Invoices; 211 Subscription Billing | None | — |
| 220 Customer Payments | Links only | §4 Create a Manual Payment Journal links to the journal controls in 221 Part 1. §4.3 Reverse a Customer Payment Journal stays here; 221 links to it. |
| **221 Customer Payment Corrections** | New (proposed); split from 230. v0.1 working draft built (D-048) | Legacy 230 §6.5, §6.6 and §6.8; the Transfers topic draft (replacing §6.7), Parent Payment Distribution and Restoration topic drafts; the CPJL controls reference as Part 1 Key concepts |
| **230 Collections** | v2.4 draft applies the split to 221 (D-051); v3.0 working draft expanded and restructured (D-052) | Workspace, Overdue Customers, Aged Balances, Customer Account, Notes and Activities, Collection Activities, Customer Invoices, Statement Preview and Statement Distribution; the Collections-specific parts of Favorites and Personalized Views |
| **240 Direct Debit and Credit Card Payments** | v0.1 skeleton (D-053); ready for review from 16 November | Legacy 230 §2.4 and 220 §5; the 11 November recording; credit cards. See section 4.4 |

---

## 4. Topic outlines

Proposed outlines. The BPO can reorder or rename topics; titles follow T2 ("a clear verb and object"). 260 and 221 are built to these outlines as v0.1 working drafts (D-048).

### 4.1 260 O2C Getting Started (new; v0.1 built)

**Part 1 Key concepts:** Navigation Pane options (Modules, Workspaces, Favorites); legal entities (business names, D365 and CargoWise ledger codes, confirm before processing); views (view, default view, view scope, filter operators); grid exports (Export all rows, configured columns, volume limits, internal use only, data handling).

| Topic | Source | Type |
|---|---|---|
| 1. Switch Legal Entity with the Selector | Legal Entities topic draft, topic 1 | New |
| 2. Switch Legal Entity Using the Ledger Code | Legal Entities topic draft, topic 2 | New |
| 3. Add Pages to Favorites | Favorites topic draft (the general steps: the favorite star, then checking **Favorites**) | New |
| 4. Create a Personalized View: 4.1 Arrange the Columns; 4.2 Filter the List (optional); 4.3 Add a Footer Total (optional); 4.4 Save and Pin the View | Personalized Views topic draft, topic 1 | New |
| 5. Update a Saved View | Personalized Views topic draft, topic 2 | New |
| 6. Export All Rows from a Grid | Export to Excel topic draft | New |

The two legal entity methods are separate topics because each is complete on its own (Legal Entities decision L1; D-048).

Candidates found in the legacy PGs, not yet evidenced for AR Collections: add an attachment to a record (210 §1.2); share a link to a page (230 §6.7); check a batch job (230 §1); submit a journal for approval (230 §6.4, §6.7; 220 §4.1). Each needs the recording or an SME before it is drafted.

### 4.2 230 Collections (expanded; v3.0 working draft built)

Two drafts exist. **v2.4** (D-051) applies only the split from the published v2.3: 6.5 to 6.8 move to 221, the transaction exclusion steps move to 6.3, and 2.4 is flagged for 240. It is for sign-off together with 221. **v3.0** (D-052) is the next major version, rebuilt in the master template with the nine topic drafts, as below.

**Part 1 additions:** a Key concept **Set up D365 for collections work**, with the four AR Collections favorite pages (from the Favorites topic draft) and the recommended view columns (from the Personalized Views topic draft), linking to 260 topics 3 and 4. Also the workspace terms and the Key concepts of every topic draft, after the legacy Key concepts.

| Topic in v3.0 | Source | Type |
|---|---|---|
| 1. Start the Collections Day: 1.1 Open the Customer Credit and Collections Workspace; 1.2 Locate Collection Work in the Workspace | Workspace topic draft | New |
| 2. Monitor Customers (parent) | Legacy 2 | Existing |
| 2.1 Review Customers Overdue | Overdue Customers topic draft, topic 1 | New |
| 2.2 Review Customer Aged Balances | Aged Balances topic draft, topic 1; legacy 2.1 as a note | Merge |
| 2.3 Filter Aged Balances by Customer or Currency | Aged Balances topic draft, topic 2 | New |
| 2.4 Investigate a Customer Account: 2.4.1 Open the Customer Account; 2.4.2 Review Customer Transactions; 2.4.3 Review Settlement History | Customer Account topic draft | New |
| 2.5 Review Customer Notes | Notes and Activities topic draft, topic 1 | New |
| 2.6 Review All Customer Activities | Notes and Activities topic draft, topic 2; legacy 2.2 as a note | Merge |
| 2.7 Update Customer Details | Legacy 2.3 (duplicates 200 §3.4: link instead, BPO to decide) | Existing |
| 2.8 Maintain Customer Direct Debit & eBanking Details | A link to 240 topic 1 (D-053) | Link |
| 3. Manage Customer Pools and Collection Agents: 3.1 Create Customer Pools for Collections; 3.2 Add a New Collections Agent | Legacy 3 | Existing |
| 4. Contact the Customer (off-system): 4.1 Check an Overdue Balance Before Contact | Legacy 4; Overdue Customers topic draft, topic 2 | Existing and new |
| 5. Record a Customer Collection Activity | Collection Activities topic draft; legacy 5 as a note | Merge |
| 6. Manage Customer Statements: 6.1 Preview and Download a Customer Statement (6.1.1, 6.1.2); 6.2 Generate and Send a Customer Statement (6.2.1, 6.2.2) | Statement Preview topic draft; Statement Distribution topic draft, legacy 1 as a note | New and merge |
| 7. Resolve the Account (parent) | Legacy 6 | Existing |
| 7.1 View and Download a Customer Invoice (7.1.1, 7.1.2) | Customer Invoices topic draft; legacy 6.1 as a note | Merge |
| 7.2 Create and Send a Collection Letter | Legacy 6.2 | Existing |
| 7.3 Change Customer Status (including exclusion from credit management) | Legacy 6.3, with the transaction exclusion steps from legacy 6.5 | Existing |
| 7.4 Write Off an Uncollectible Debt | Legacy 6.4 | Existing |
| 8. Update and Close a Customer Activity | Legacy 7 | Existing |

**Merge rule (D-052):** where a topic draft and a legacy section cover the same task, the draft's procedure is the topic and the legacy-only content is a note with a `G230` item to confirm. No legacy steps are mixed into draft procedures.

**Legacy-to-new topic numbers in 230:** 1 → 6.2; 2 → 2; 2.1 → 2.2; 2.2 → 2.6; 2.3 → 2.7; 2.4 → 2.8, then 240; 3 → 3; 4 → 4; 5 → 5; 6 → 7; 6.1 → 7.1; 6.2 → 7.2; 6.3 → 7.3; 6.4 → 7.4; 6.5 to 6.8 → 221; 7 → 8.

### 4.3 221 Customer Payment Corrections (new; v0.1 built)

**Part 1 Key concepts:** Customer payment journal controls (from the CPJL controls reference: journal set-up, line coding, validation and posting, allocations and amounts); settlement; parent and child accounts (backlog rank 26, once it has evidence).

| Topic | Source | Type |
|---|---|---|
| 1. Settle Customer Transactions | Legacy 230 §6.5 | Moved |
| 2. Undo a Settlement | Legacy 230 §6.6 | Moved |
| 3. Transfer Funds Between Customer Accounts | Transfers topic draft (replaces legacy 230 §6.7 once the conflicts in the cross-comparison are resolved) | Replace |
| 4. Distribute a Parent Account Payment Across Child Accounts (including partial allocation) | Parent Payment Distribution topic draft | New |
| 5. Restore a Written-Off or Overpayment Amount | Restoration topic draft | New |
| 6. Write Off a Bank Fee or Small Residual | Legacy 230 §6.8 | Moved |

Candidate: investigate an unallocated payment (backlog rank 14), once its content is ready.

### 4.4 240 Direct Debit and Credit Card Payments (v0.1 skeleton)

Scope and structure come from the 9 November scoping meeting (D-053). Context first, then short how-to topics, then exceptions; credit cards follow with their own topics and exceptions. Placeholders mark topics that are being worked on, so the structure stays stable while content arrives. Scoping answers are in the doc *240 Direct Debit Scoping Questions* (https://claude.ai/artifact/SegmHCWvsPWuHYeJiLEQdo).

| Topic in v0.1 | Who | Content now | Source |
|---|---|---|---|
| 1. Maintain a Customer's Direct Debit Details | Collections Officer | Legacy steps, flagged | Legacy 230 §2.4; the 11 November recording |
| 2. Process a Direct Debit Run: 2.1 Run the Mid-Month Direct Debit Batch; 2.2 Run an Ad Hoc Direct Debit | Receipting Officer | 2.1 legacy steps, flagged; 2.2 placeholder | Legacy 220 §5; the recording |
| 3. Approve a Direct Debit Run | Chris Clarke, Arash Najafi | Placeholder | The recording |
| 4. Handle Direct Debit Exceptions: 4.1 Follow Up a Failed Direct Debit; 4.2 Fix Direct Debit Errors; 4.3 Process a Direct Debit Reversal | Collections Officer; Receipting Officer | Placeholders | The recording; a later session on reversals |
| 5. Credit Card Payments: 5.1 Maintain Card Details; 5.2 Send a Payment Link; 5.3 Process an Ad Hoc Card Payment; 5.4 Handle Card Exceptions | Collections Officer; Receipting Officer | Placeholders | When credit card payments go live |

Alternate names and payment matching stay in 220. Excluding a customer from direct debit runs uses the normal dispute process (230 topic 7.3). 230 topic 2.8 links to 240 topic 1, and 220 §5 will link to 240 topic 2.

---|---|---|
| Maintain a customer's direct debit set-up (method of payment, payment specification, eBanking details, direct debit settings, customer bank account) | Legacy 230 §2.4 | Move from 230 |
| Change or remove direct debit when a customer changes payment method | Legacy 230 §2.4 (final step) | Move from 230, subject to scope clarification with Maria Pabalan |
| Process direct debit customer payments (payment proposal, direct debit journal, validate, create and send the direct debit file) | Legacy 220 §5 | Move from 220 |
| Maintain credit card payments | Backlog rank 32; no content | Scope decision open |

Excluding a transaction from direct debit runs stays in 230 topic 7.3, which links to 240. eBanking details used for payment matching (220 §3.4 and §3.5) stay in 220. Nothing is drafted for 240 until the BPO confirms the scope and the legacy steps are checked against a recording or a D365 test (D-044). Scoping questions for the meeting with Maria Pabalan (ADO Task 16894) are in the doc *240 Direct Debit Scoping Questions* (https://claude.ai/artifact/SegmHCWvsPWuHYeJiLEQdo): scope and boundaries, roles, set-up, collection runs, and controls.

---

## 5. Topic drafts and their destinations

| Topic draft | Destination | Merge type | Open items (blocking) |
|---|---|---|---|
| Favorites | 260 topic 3 (merged in 260 v0.1); the AR page list is in 230 v3.0 Part 1 | Split | 30 (16) |
| Personalized Views | 260 topics 4 and 5 (merged in 260 v0.1); the recommended columns are in 230 v3.0 Part 1 | Split | 29 (23) |
| Legal Entities | 260 topics 1 and 2 (merged in 260 v0.1) | New | 22 (13) |
| Export to Excel | 260 topic 6 (merged in 260 v0.1) | New | 20 (12) |
| Workspace | 230 topics 1.1 and 1.2 (merged in 230 v3.0) | New | 22 (14) |
| Overdue Customers | 230 topics 2.1 and 4.1 (merged in 230 v3.0) | New | 22 (16) |
| Aged Balances | 230 topics 2.2 and 2.3 (merged in 230 v3.0) | Merge with legacy 2.1 | 22 (15) |
| Customer Account | 230 topic 2.4 (merged in 230 v3.0) | New | 24 (17) |
| Notes and Activities | 230 topics 2.5 and 2.6 (merged in 230 v3.0) | Merge with legacy 2.2 | 22 (15) |
| Collection Activities | 230 topic 5 (merged in 230 v3.0) | Merge with legacy 5 | 24 (17) |
| Statement Preview | 230 topic 6.1 (merged in 230 v3.0) | New | 24 (16) |
| Statement Distribution | 230 topic 6.2 (merged in 230 v3.0) | Merge with legacy 1 | 25 (19) |
| Customer Invoices | 230 topic 7.1 (merged in 230 v3.0) | Merge with legacy 6.1 | 22 (14) |
| Customer Account Transfers | 221 topic 3 (merged in 221 v0.1) | Replace legacy 230 §6.7 | Shared Part 2 register: 46 (38) |
| Parent Payment Distribution | 221 topic 4 (merged in 221 v0.1) | New | Shared Part 2 register |
| Overpayment and Write-Off Restoration | 221 topic 5 (merged in 221 v0.1) | New | Shared Part 2 register |
| CPJL controls reference | 221 Part 1 Key concepts (merged in 221 v0.1) | New | Shared Part 2 register |
| Customer Pools (no draft) | 230 topic 3, already in the legacy guide | Existing | 7 (7) |

## 6. Backlog and destinations

| Rank | Backlog item | Destination |
|---|---|---|
| 1 | AR Collections orientation (learning module) | Learning content linking to 260 and 230 topic 1 |
| 2 | Switch between legal entities | 260 topics 1 and 2 |
| 3 | Navigate the Customer Credit and Collections workspace | 230 topics 1.1 and 1.2 |
| 4 | Configure AR Collections Favorites | 260 topic 3; 230 Part 1 |
| 5 | Create and save a personalized view | 260 topics 4 and 5; 230 Part 1 |
| 6 | Review overdue customers | 230 topics 2.1 and 4.1 |
| 7 | Review customer aged balances | 230 topics 2.2 and 2.3 |
| 8 | Investigate a customer account | 230 topic 2.4 |
| 9 | Review customer notes and activities | 230 topics 2.5 and 2.6 |
| 10 | Record a collection activity | 230 topic 5 |
| 11 | View and download a customer invoice | 230 topic 7.1 |
| 12 | Generate and send a customer statement | 230 topic 6.2 |
| 13 | Preview and download a customer statement | 230 topic 6.1 |
| 14 | Investigate unallocated payments | 221 (candidate topic) |
| 15 | Settle customer transactions | 221 topic 1 |
| 16 | Review and undo settlements | Review: 230 topic 2.4.3. Undo: 221 topic 2 |
| 17 | Export all rows from a D365 grid | 260 topic 6 |
| 18 | Write off a customer transaction | Uncollectible debt: 230 topic 7.4. Bank fee or residual: 221 topic 6 |
| 19 | Validate and submit a write-off journal | 230 topic 7.4 |
| 20 | Cancel an unposted write-off | 230 topic 7.4 (new subtopic, no content yet) |
| 21 | Maintain customer contacts | 200 §3.4 |
| 22 | Maintain customer addresses | 200 §3.3 |
| 23 | Add an invoice-only address | 200 §3.3 |
| 24 | Exclude a customer from credit management | 230 topic 7.3 |
| 25 | Exclude a customer from statements | 230 topic 6 (new subtopic, no content yet) |
| 26 | Identify parent-child accounts (knowledge article) | 221 Part 1 Key concepts |
| 27 | Transfer funds between accounts | 221 topic 3 |
| 28 | Search the custom transaction report | 230 Part 3 Reports |
| 29 | Review daily bank statements | 220 |
| 30 | Change customer payment terms | 200 §3.7 |
| 31 | Maintain direct debit | 240 topic 1 |
| 32 | Maintain credit cards | 240 topic 5 (D-053) |
| 33 | Transfer a parent account payment across child accounts | 221 topic 4 |
| 34 | Restore a written-off or overpayment amount | 221 topic 5 |
| 35 | Customer Payment Journal controls reference | 221 Part 1 Key concepts |
| 36 | Customer Pools | 230 topic 3 |

---

## 7. Merge gate

A topic draft merges into its destination guide when all of these hold. 260 and 221 (D-048) and 230 v3.0 (D-052) were built ahead of this gate at the user's request: they stay v0.1 working drafts, inside the project team, until gate 1 holds, and gates 2 to 4 still apply before either is published.

1. **Codes recorded.** For 221 and 260: the register owner has recorded the code, and the BPO has confirmed the scope ("Confirm scope before adding a new standalone guide").
2. **Conflicts resolved.** Every conflict between the topic and legacy content (cross-comparison section 5) is settled by the D365 test, the recording or the SME. Where legacy content and the recording disagree, the recording governs (D-044).
3. **New draft version.** Merging creates the destination guide's next draft version. The published version stays live until that draft passes its gates.
4. **Higher-risk topics keep their gates.** All of 221, and 230 topics 6.2, 7.3 and 7.4, are not published until their blocking items close.

## 8. What changes elsewhere

- **SME question packs:** D1 and P2-D1 now ask the SME to confirm each draft's destination, not to assign a guide code.
- **Validation registers:** each guide-code item now reads as a destination item. IDs are unchanged.
- **Clean-session test plan:** unchanged. It tests labels and behavior, wherever the topic lands.
- **CPJL controls reference:** merged into 221 Part 1 (v0.1). The file stays in `06-reference-guides`, frozen (D-048).

## Change log

| Date | Change |
|---|---|
| 2026-11-01 | Plan created: one task per topic (D-045), codes 221 and 260 proposed under the O2C numbering standard (D-046). |
| 2026-11-01 | 260 and 221 built as v0.1 working drafts (D-048); 260 topics renumbered 1 to 6; 240 Direct Debit recorded as required with no document yet, with a proposed scope (D-049). |
| 2026-11-03 | Plan shared with the O2C stakeholders (D-050). ADO tickets: 221 Task 16993, 260 Task 16994, 240 Task 16894, 230 Task 16886. Each guide needs BPO sign-off. |
| 2026-11-03 | 230 v2.4 draft built from v2.3: the split to 221 applied (D-051, ADO Task 16886). |
| 2026-11-03 | 230 v3.0 working draft built with the nine topic drafts (D-052); section 4.2 shows it as built, and the destinations in sections 5 and 6 use its topic numbers. |
| 2026-11-08 | Section 4.4 links the 240 scoping questions. |
| 2026-11-09 | 240 scope and structure from the 9 November meeting (D-053): section 4.4 shows the v0.1 skeleton; 230 topic 2.8 links to 240 topic 1. |
