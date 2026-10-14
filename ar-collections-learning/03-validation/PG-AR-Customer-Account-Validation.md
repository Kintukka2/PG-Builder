# Validation Register: AR Collections Customer Account

| Field | Value |
|---|---|
| Related PG (editable source) | [`../01-procedure-guides/TBC-AR Collections Customer Account PG v0.1.docx`](../01-procedure-guides/TBC-AR%20Collections%20Customer%20Account%20PG%20v0.1.docx) |
| Markdown preview | [`../01-procedure-guides/PG-AR-Customer-Account-DRAFT.md`](../01-procedure-guides/PG-AR-Customer-Account-DRAFT.md) |
| Screenshot register | [`../02-screenshot-registers/PG-AR-Customer-Account-Screenshots.md`](../02-screenshot-registers/PG-AR-Customer-Account-Screenshots.md) |
| Last updated | 2026-10-14 |
| Items | 24 total, all open: 17 blocking, 7 non-blocking |

This file is the guide's **question log** (decision D-016). The `VG-xx` IDs are scoped to this guide and never renumbered. Each open item that affects the text is also a Word review comment by "Validation register" (VR).

---

## 1. Evidence base

| Source | What it supports |
|---|---|
| 0, Topic 6 *Customer Account Investigation* | Enter customer account; review transactions, balances, notes and collection history. Rated ready. Suggested PG `PG-AR-005 Review a Customer Account`. |
| 0, Topic 19 *Customer Transactions Screen* | Show Open; Show Closed; Hide FX Revaluations; review transactions. Rated ready. Suggested PG `PG-AR-015 Review Customer Transactions`. |
| 0, Topic 21 *View Settlements* | View Settlement; allocation history; Undo settlement. Rated ready. Suggested PG `PG-AR-017 Review Transaction Settlement History`. |
| 1, Module 4 | Sequences 4.1 (open a customer from All customers), 4.2 (open a customer from Aged balances), 4.3 (review open and closed transactions), 4.4 (hide currency revaluations), 4.5 (review due dates, amounts and currencies) and 4.6 (review transaction settlement history), all ready. The recording demonstrates Customer transactions, hiding currency revaluations, switching between open and closed records and viewing settlement history. |
| 2, Release 1 item 8 | Scope: open the customer account; review account balance and overdue amounts; review open and closed transactions; hide currency revaluations; review due dates and transaction descriptions; review previous settlement activity; review notes and activities; open supporting documents. |
| 2, Release 2 (settlement correction) | Undo settlement is the correction method; status partial, with approval and documentation requirements still to validate. |
| Earlier guides | All customers path (Favorites); highlighting versus marking (Customer Invoices VG-02); notes and activities (Notes and Activities guide); invoices (Customer Invoices guide). |

**Not available:** a transcript excerpt, timestamps, or exact labels for the account page, the Transactions control, the show and hide controls or View settlements.

---

## 2. Drafting decisions for this guide

| # | Decision | Reason |
|---|---|---|
| C1 | One parent topic, **1. Investigate a Customer Account**, with three subprocedures: **1.1 Open the Customer Account**, **1.2 Review Customer Transactions** and **1.3 Review Settlement History** (optional). | Source 2 describes one investigation in sequence. Source 0's three suggested guides become its subprocedures (`VG-19`). |
| C2 | Notes, activities and invoices are referred to their own guides in the last step. | They are already drafted (Notes and Activities, Customer Invoices). |
| C3 | Settlement history is review-only. **Undo settlement** is excluded and stated as a rule. | Settlement changes are higher-risk and are not finalised until their gaps are validated (project rule; `VG-13`). |
| C4 | The guide opens customers from **All customers**. Other routes are a question. | Source 1 also lists Aged balances; Customers overdue is in the Overdue Customers guide (`VG-03`). |
| C5 | Step 1.2.6 asks users to check that the transactions explain the balance. | This is the check that Overdue Customers step 2.3 refers to (`VG-15`). |

---

## 3. Validation gap register

**Priority:** **B** = blocks publication. **N** = non-blocking.

**Method:** **Test** = D365 test in a clean session. **Rec** = recording or transcript review. **SME** = subject-matter expert or process owner. **Dec** = project decision.

| ID | Item to confirm | Location in Word guide | Word comment | Priority | Method | Status |
|---|---|---|---|---|---|---|
| VG-01 | Menu group for **All customers** in Credit and collections. Shared with Favorites VG-02. | 1.1 Step 3 | 8 | B | Test | Open |
| VG-02 | How the customer account opens from All customers. Shared with Notes and Activities VG-08. | 1.1 Step 4 | 9 | B | Test | Open |
| VG-03 | Whether users should also open customers from Aged balances or Customers overdue (source 1, sequence 4.2). | 1.1 Step 3 | 8 | N | SME, Test | Open |
| VG-04 | Exact labels and location of the balance and overdue amount on the customer account. | 1.1 Step 5 | 10 | B | Test | Open |
| VG-05 | Exact label and location of the control that opens Customer transactions. | 1.2 Step 1 | 11 | B | Test, Rec | Open |
| VG-06 | Exact labels and location of **Show open** and **Show closed**, and the open/closed meanings. | Key concepts; 1.2 Step 2 | 4, 12 | B | Test, Rec | Open |
| VG-07 | Exact label and location of the control that hides currency revaluations (source 0: "Hide FX Revaluations"). | Key concepts; 1.2 Step 3 | 5, 13 | B | Test, Rec | Open |
| VG-08 | Wording of the currency revaluation definition. | Key concepts | 5 | N | SME | Open |
| VG-09 | Exact labels of the due date, amount, currency and description columns. | 1.2 Step 4 | 14 | B | Test | Open |
| VG-10 | How a transaction row is selected, and that it does not need to be marked. Shared with Customer Invoices VG-02. | 1.3 Step 1 | 16 | B | Test | Open |
| VG-11 | Exact label and location of **View settlements**. | 1.3 Step 2 | 17 | B | Test, Rec | Open |
| VG-12 | What the settlement history shows and how users read it (source 0: allocation history). | Key concepts; 1.3 Step 3 | 6, 18 | B | Test, SME | Open |
| VG-13 | Confirm that Undo settlement stays out of this guide. | Key concepts (rule) | 7 | N | Dec | Open |
| VG-14 | Whether Customer transactions shows transactions from other legal entities. | Not in guide | — | N | Test | Open |
| VG-15 | What users must check before contacting a customer. Also answers Overdue Customers VG-08. | 1.2 Step 6 | 15 | N | SME | Open |
| VG-16 | Initiation events for this task. | Part 1 Initiation; topic Initiation; Process table *When* | 2 | B | SME | Open |
| VG-17 | Stream, process area and business role name. Shared with the other AR Collections guides. | Stream table; Process table; Roles matrix | 3 | B | SME | Open |
| VG-18 | Business process owner (BPO). | Version history | 1 | B | SME | Open |
| VG-19 | Guide code and final title, and whether source 0's three suggested guides (PG-AR-005, -015, -017) stay combined here. | Cover; file name | 0 | B | Dec | Open |
| VG-20 | Whether any reports or inquiries apply. If none, "No applicable reports". | Part 3 | 19 | B | SME | Open |
| VG-21 | The security role needed for customer accounts, transactions and settlement history, and a test with it. | PROCESS START (1.1) | — | B | Test, SME | Open |
| VG-22 | SME factual review, a test by someone other than the author, and approval. | Whole guide | — | B | SME | Open |
| VG-23 | Recording timestamps for the customer account demonstration. | Screenshot register | — | N | Rec | Open |
| VG-24 | Confirm that the custom all-customer transaction report (source 1, sequence 4.11: gap) is a separate guide. | Part 3 | 19 | N | Dec | Open |

**Fastest route to closure:** one clean-session D365 walkthrough of a customer account, through to View settlements, closes `VG-01`, `VG-02`, `VG-04` to `VG-07` and `VG-09` to `VG-11`. It also closes Favorites VG-02, Notes and Activities VG-08 and Customer Invoices VG-01 and VG-02.

---

## 4. Publication readiness

| Check | Status |
|---|---|
| Template structure is complete; unused examples are removed | Met |
| Process table rows match the Part 2 topics (1 row) | Met; values pending `VG-16` and `VG-17` |
| Parent topic Overview lists all subprocedures | Met (3) |
| Standard navigation pattern | Met in 1.1; menu group pending `VG-01` |
| Each procedure table restarts numbering at 1 | Met |
| Exact system labels | Open (`VG-01`, `VG-02`, `VG-04` to `VG-07`, `VG-09` to `VG-11`) |
| Business rules separate from procedure | Met (no-undo rule in Key concepts) |
| Higher-risk actions excluded | Met (Undo settlement out of scope) |
| Reports | Open (`VG-20`) |
| Roles, BPO, guide code | Open (`VG-17`, `VG-18`, `VG-19`) |
| Peer test, SME review, approval | Open (`VG-21`, `VG-22`) |
| Review comments resolved before release | Open (20 Word comments) |

---

## 5. Change log

| Date | Change |
|---|---|
| 2026-10-14 | Register created with the v0.1 SME review draft. |
