# Validation Register: AR Collections Statement Preview

| Field | Value |
|---|---|
| Related PG (editable source) | [`../01-procedure-guides/TBC-AR Collections Statement Preview PG v0.1.docx`](../01-procedure-guides/TBC-AR%20Collections%20Statement%20Preview%20PG%20v0.1.docx) |
| Markdown preview | [`../01-procedure-guides/PG-AR-Statement-Preview-DRAFT.md`](../01-procedure-guides/PG-AR-Statement-Preview-DRAFT.md) |
| Screenshot register | [`../02-screenshot-registers/PG-AR-Statement-Preview-Screenshots.md`](../02-screenshot-registers/PG-AR-Statement-Preview-Screenshots.md) |
| Last updated | 2026-10-14 |
| Items | 24 total, all open: 16 blocking, 8 non-blocking |

This file is the guide's **question log** (decision D-016). The `VG-xx` IDs are scoped to this guide and never renumbered. Each open item that affects the text is also a Word review comment by "Validation register" (VR).

---

## 1. Evidence base

| Source | What it supports |
|---|---|
| 0, Topic 22 *Generate and Send Customer Statements* | Statement generation; Print Management; Open Only; Company Logo; customer delivery method; screen preview. Rated ready. Suggested PG `PG-AR-018 Generate and Send Customer Statements` (one guide for preview and send). |
| 0, Topic 17 *Excluding Customers from Statements* | Multi-currency examples and known statement limitations. Belongs to the exclusion guide. |
| 1, Module 6 | Sequences 6.3 (generate a statement), 6.4 (include company logo), 6.5 (include open transactions only), 6.6 (Print management destination) and 6.7 (preview rather than send), all ready; 6.9 (multiple related accounts) partial. The recording demonstrates statement parameters, "Only open", company logo, Print management destination and screen preview. Proposed PGs include *Preview and download a customer statement*. Critical control: customer-facing information as PDF rather than Excel. |
| 1, questions I *Customer statements* | Validate statement parameters; whether Only open must always be selected; when the company logo is required; the meaning and effect of Print management destination; the preview-only process; multi-currency limitations; the required file format. |
| 2, Release 2 item 13 | Scope: clear Print management destination, select Screen as the destination, generate the statement, review the output, download as PDF. Status: ready to develop. |
| 2, Release 2 item 12 | The send guide distinguishes customer delivery through Print management from displaying the statement on screen. |
| Customer Invoices guide | PDF download, naming and save-location questions (its VG-07 to VG-10). |

**Not available:** a transcript excerpt, timestamps, the navigation path to Statements, or exact labels for the parameters, destinations and download control.

---

## 2. Drafting decisions for this guide

| # | Decision | Reason |
|---|---|---|
| P1 | One parent topic, **1. Preview and Download a Customer Statement**, with **1.1 Generate the Statement Preview** and **1.2 Download the Statement as PDF** (optional). | Mirrors the Customer Invoices guide: review on screen, then optionally download. |
| P2 | This guide covers preview only. Sending is the *Generate and send a customer statement* guide. | Sources 1 and 2 propose two guides; source 0 proposes one (`VG-19`, `VG-24`). |
| P3 | Clearing **Print management destination** and selecting **Screen** are separate steps, and checking them is a Key concept rule. | This is the safeguard that keeps a preview from reaching the customer (source 2; `VG-05`). |
| P4 | Step 1.1.2 opens **Statements** without a navigation path. | The path was not captured (`VG-01`). |
| P5 | Multi-currency limitations and multiple related accounts are not covered. | They belong to the send and exclusion guides, or are partial in source 1 (`VG-13`, `VG-14`). |

---

## 3. Validation gap register

**Priority:** **B** = blocks publication. **N** = non-blocking.

**Method:** **Test** = D365 test in a clean session. **Rec** = recording or transcript review. **SME** = subject-matter expert or process owner. **Dec** = project decision.

| ID | Item to confirm | Location in Word guide | Word comment | Priority | Method | Status |
|---|---|---|---|---|---|---|
| VG-01 | Exact label of the **Statements** page and its navigation path. | 1.1 Step 2 | 9 | B | Test, Rec | Open |
| VG-02 | How the customer is selected, for example through the records to include filter. | 1.1 Step 3 | 10 | B | Test, Rec | Open |
| VG-03 | Exact label of **Only open** and whether it must always be selected. | Key concepts; 1.1 Step 4 | 4, 11 | B | Test, SME | Open |
| VG-04 | Exact label of the company logo option and when it must be included. | 1.1 Step 5 | 12 | B | Test, SME | Open |
| VG-05 | Meaning and effect of **Print management destination**, how it is cleared, and what happens if it is left set. | Key concepts (term and rule); 1.1 Step 6 | 5, 7, 13 | B | Test, SME | Open |
| VG-06 | Exact label and location of the **Screen** destination. | Key concepts; 1.1 Step 7 | 6, 14 | B | Test | Open |
| VG-07 | The control that generates the statement, for example **OK**. | 1.1 Step 8 | 15 | B | Test | Open |
| VG-08 | Which statement details users must check. | 1.1 Step 9 | 16 | N | SME | Open |
| VG-09 | Exact label and location of the control that downloads the PDF. | 1.2 Step 1 | 17 | B | Test | Open |
| VG-10 | Whether a file naming convention applies to statement PDFs. See Customer Invoices VG-08. | 1.2 Step 2 | 18 | N | SME | Open |
| VG-11 | Where statement PDFs should be saved. See Customer Invoices VG-09. | 1.2 Step 3 | 19 | N | SME | Open |
| VG-12 | Whether the file is named before or after the download. See Customer Invoices VG-10. | 1.2 Steps 1–3 | 18 | B | Test | Open |
| VG-13 | Multi-currency statement limitations that affect a preview (source 1, questions I). | Not in guide | — | N | SME | Open |
| VG-14 | Statements for multiple related accounts (source 1, sequence 6.9: partial). | Not in guide | — | N | Dec | Open |
| VG-15 | Wording and owner of the PDF-not-Excel rule. Shared with Aged Balances VG-13, Customer Invoices VG-12 and Export to Excel VG-09. | Key concepts | 8 | N | SME | Open |
| VG-16 | Initiation events for this task. | Part 1 Initiation; topic Initiation; Process table *When* | 2 | B | SME | Open |
| VG-17 | Stream, process area and business role name. Shared with the other AR Collections guides. | Stream table; Process table; Roles matrix | 3 | B | SME | Open |
| VG-18 | Business process owner (BPO). | Version history | 1 | B | SME | Open |
| VG-19 | Guide code and final title, and whether preview and send are separate guides (source 0 proposes one: `PG-AR-018`). | Cover; file name | 0 | B | Dec | Open |
| VG-20 | Whether any reports or inquiries apply. If none, "No applicable reports". | Part 3 | 21 | B | SME | Open |
| VG-21 | The security role needed to generate statements, and a test with it. | PROCESS START (1.1) | — | B | Test, SME | Open |
| VG-22 | SME factual review, a test by someone other than the author, and approval. | Whole guide | — | B | SME | Open |
| VG-23 | Recording timestamps for the statement demonstration. | Screenshot register | — | N | Rec | Open |
| VG-24 | Confirm that sending a statement is covered by the *Generate and send a customer statement* guide. | 1.2 PROCESS COMPLETE | 20 | N | Dec | Open |

**Fastest route to closure:** one clean-session D365 test that previews a statement for a test customer closes `VG-01` to `VG-07` (labels), `VG-09` and `VG-12`. Run it with **Screen** as the destination and a test customer, so no statement can reach a real customer. `VG-03` to `VG-05` also need an SME answer on the required parameters.

---

## 4. Publication readiness

| Check | Status |
|---|---|
| Template structure is complete; unused examples are removed | Met |
| Process table rows match the Part 2 topics (1 row) | Met; values pending `VG-16` and `VG-17` |
| Parent topic Overview lists both subprocedures | Met |
| Standard navigation pattern | Partial: Entity check, then open Statements (`VG-01`) |
| Each procedure table restarts numbering at 1 | Met |
| Exact system labels | Open (`VG-01` to `VG-07`, `VG-09`) |
| Business rules separate from procedure | Met (destination check and PDF rule in Key concepts) |
| Customer-facing risk controlled | Met in the text: Print management cleared, Screen selected; pending `VG-05` |
| Reports | Open (`VG-20`) |
| Roles, BPO, guide code | Open (`VG-17`, `VG-18`, `VG-19`) |
| Peer test, SME review, approval | Open (`VG-21`, `VG-22`) |
| Review comments resolved before release | Open (22 Word comments) |

---

## 5. Change log

| Date | Change |
|---|---|
| 2026-10-14 | Register created with the v0.1 SME review draft. |
