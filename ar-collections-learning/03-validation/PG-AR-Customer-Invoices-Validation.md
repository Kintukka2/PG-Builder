# Validation Register: AR Collections Customer Invoices

| Field | Value |
|---|---|
| Related PG (editable source) | [`../01-procedure-guides/TBC-AR Collections Customer Invoices PG v0.1.docx`](../01-procedure-guides/TBC-AR%20Collections%20Customer%20Invoices%20PG%20v0.1.docx) |
| Markdown preview | [`../01-procedure-guides/PG-AR-Customer-Invoices-DRAFT.md`](../01-procedure-guides/PG-AR-Customer-Invoices-DRAFT.md) |
| Screenshot register | [`../02-screenshot-registers/PG-AR-Customer-Invoices-Screenshots.md`](../02-screenshot-registers/PG-AR-Customer-Invoices-Screenshots.md) |
| Last updated | 2026-10-14 |
| Items | 22 total, all open: 14 blocking, 8 non-blocking |

This file is the guide's **question log** (decision D-016). The `VG-xx` IDs are scoped to this guide and never renumbered. Each open item that affects the text is also a Word review comment by "Validation register" (VR).

---

## 1. Evidence base

| Source | What it supports |
|---|---|
| 0, Topic 20 *Print and Download Customer Invoice* | Full walkthrough: Original Document, Print Preview, Download PDF, review invoice details. Rated ready. Suggested PG `PG-AR-016 View and Download Customer Invoices`. |
| 0, Topic 19 *Customer Transactions Screen* | Show Open, Show Closed, Hide FX Revaluations. Belongs to the *Review customer transactions* guide (`PG-AR-015`). |
| 1, Module 4 | Sequence 4.10: view and download an invoice (ready). The recording opens an invoice through Original document and Print preview from Customer transactions. |
| 1, Module 6 | Sequences 6.1 (view an invoice) and 6.2 (download an invoice as PDF), both ready. Critical control: customer-facing account information should be provided as PDF rather than Excel. |
| 1, sequence 8.3 | Row highlighting is different from **Mark**. |
| 2, Release 2 item 11 | Scope: select the relevant transaction, open Original document, select the invoice, open Print preview, review invoice information, download as PDF, apply a meaningful filename. |
| 2, controls | Excel exports are for internal analysis and should not replace approved PDF customer documents. |
| 3.1, first drafting batch #4 | Scope: open the customer transaction, **highlight** the required invoice, select Original document, select the invoice, open Print preview, review, download as PDF, apply a meaningful filename. Risk: low. Ready to draft. |

**Not available:** a transcript excerpt, timestamps, the navigation path to the customer's transactions, or exact control labels for the download step.

---

## 2. Drafting decisions for this guide

| # | Decision | Reason |
|---|---|---|
| I1 | One parent topic, **1. View and Download a Customer Invoice**, with two subprocedures: **1.1 Open the Invoice Preview** and **1.2 Download the Invoice as PDF**. | Viewing is complete on its own; downloading always follows viewing. This matches sources 1 (6.1 and 6.2) and the template's parent-topic pattern. |
| I2 | 1.2 is marked optional, and 1.1 ends with STEP COMPLETE and a *Continue to* link. | A user who only needs to review the invoice stops after 1.1. |
| I3 | 1.1 starts with *Check* the **Entity** but does not repeat the *Click* **Modules** and *Navigate* rows. Step 2 opens the customer's transactions instead. | The path to the transactions page was not captured (`VG-01`). The guide does not invent it. |
| I4 | Finding the invoice with Show closed or Hide FX revaluations is not included. | It belongs to the *Review customer transactions* guide (`VG-22`). |
| I5 | Sending the invoice to the customer is out of scope. | No source describes the sending step (`VG-21`). |
| I6 | The PDF-not-Excel rule is a Key concept, not a step. It uses the same wording as the Aged Balances guide. | T2 "Separate rules from procedure". One rule wording across guides. |

---

## 3. Validation gap register

**Priority:** **B** = blocks publication. **N** = non-blocking.

**Method:** **Test** = D365 test in a clean session. **Rec** = recording or transcript review. **SME** = subject-matter expert or process owner. **Dec** = project decision.

| ID | Item to confirm | Location in Word guide | Word comment | Priority | Method | Status |
|---|---|---|---|---|---|---|
| VG-01 | The page and navigation path used to open a customer's transactions, for example **Customer transactions** from **All customers**. | 1.1 Step 2 | 7 | B | Test, Rec | Open |
| VG-02 | How a transaction row is highlighted, and that it does not need to be marked. Source 1 (8.3) treats highlighting and **Mark** as different controls. | Key concepts; 1.1 Step 3 | 5, 8 | B | Test | Open |
| VG-03 | Exact label and location of **Original document**, and what D365 displays after it is clicked. | Key concepts; 1.1 Step 4 | 4, 9 | B | Test, Rec | Open |
| VG-04 | What the original document list shows for an invoice transaction, and how the invoice is selected. | Key concepts; 1.1 Step 5 | 4, 10 | B | Test, Rec | Open |
| VG-05 | Exact label and location of **Print preview**, and how the preview is displayed. | 1.1 Step 6 | 11 | B | Test | Open |
| VG-06 | Which invoice details users must check before sharing an invoice. | 1.1 Step 7 | 12 | N | SME | Open |
| VG-07 | Exact label and location of the control that downloads the PDF. | 1.2 Step 1 | 13 | B | Test, Rec | Open |
| VG-08 | Whether a file naming convention applies to customer invoice PDFs. | 1.2 Step 2 | 14 | N | SME | Open |
| VG-09 | Where customer invoice PDFs should be saved. | 1.2 Step 3 | 15 | N | SME | Open |
| VG-10 | Whether the file is named in D365 before the download, or renamed after it completes. This decides the order of steps 1 to 3. | 1.2 Steps 1–3 | 14 | B | Test | Open |
| VG-11 | Whether the same steps apply to credit notes and other document types. | Not in guide | — | N | Test, SME | Open |
| VG-12 | Wording and owner of the PDF-not-Excel rule. Shared with Aged Balances VG-13. | Key concepts | 6 | N | SME | Open |
| VG-13 | Initiation events for this task. | Part 1 Initiation; topic Initiation; Process table *When* | 2 | B | SME | Open |
| VG-14 | Stream, process area and business role name. Shared with the other AR Collections guides. | Stream table; Process table; Roles matrix | 3 | B | SME | Open |
| VG-15 | Business process owner (BPO). | Version history | 1 | B | SME | Open |
| VG-16 | Guide code and final title. Source 0 proposes `PG-AR-016`. | Cover; file name | 0 | B | Dec | Open |
| VG-17 | Whether any reports or inquiries apply. If none, "No applicable reports". | Part 3 | 17 | B | SME | Open |
| VG-18 | The security role needed to open original documents and print preview, and a test with it. | PROCESS START (1.1) | — | B | Test, SME | Open |
| VG-19 | SME factual review, a test by someone other than the author, and approval. | Whole guide | — | B | SME | Open |
| VG-20 | Recording timestamps for the invoice demonstration. | Screenshot register | — | N | Rec | Open |
| VG-21 | Which process or guide covers sending the invoice to the customer. | 1.2 PROCESS COMPLETE | 16 | N | SME, Dec | Open |
| VG-22 | Confirm that finding an invoice with **Show closed** or **Hide FX revaluations** belongs in the *Review customer transactions* guide, not here. | Part Description (scope) | — | N | Dec | Open |

**Fastest route to closure:** one clean-session D365 test that opens a posted invoice from its transaction closes `VG-01` to `VG-05`, `VG-07` and `VG-10`. That session can be the same one used for the Favorites, Personalized Views and Aged Balances tests.

---

## 4. Publication readiness

| Check | Status |
|---|---|
| Template structure is complete; unused examples are removed | Met |
| Process table rows match the Part 2 topics (1 row) | Met; values pending `VG-13` and `VG-14` |
| Parent topic Overview lists both subprocedures | Met |
| Standard navigation pattern | Partial: Entity check only; path pending `VG-01` |
| Each procedure table restarts numbering at 1 | Met |
| Exact system labels | Open (`VG-01` to `VG-05`, `VG-07`) |
| Business rules separate from procedure | Met (PDF rule in Key concepts) |
| Reports | Open (`VG-17`) |
| Roles, BPO, guide code | Open (`VG-14`, `VG-15`, `VG-16`) |
| Peer test, SME review, approval | Open (`VG-18`, `VG-19`) |
| Review comments resolved before release | Open (18 Word comments) |

---

## 5. Change log

| Date | Change |
|---|---|
| 2026-10-14 | Register created with the v0.1 SME review draft. |
