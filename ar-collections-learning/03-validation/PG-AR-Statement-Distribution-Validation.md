# Validation Register: AR Collections Statement Distribution

| Field | Value |
|---|---|
| Related PG (editable source) | [`../01-procedure-guides/TBC-AR Collections Statement Distribution PG v0.1.docx`](../01-procedure-guides/TBC-AR%20Collections%20Statement%20Distribution%20PG%20v0.1.docx) |
| Markdown preview | [`../01-procedure-guides/PG-AR-Statement-Distribution-DRAFT.md`](../01-procedure-guides/PG-AR-Statement-Distribution-DRAFT.md) |
| Screenshot register | [`../02-screenshot-registers/PG-AR-Statement-Distribution-Screenshots.md`](../02-screenshot-registers/PG-AR-Statement-Distribution-Screenshots.md) |
| Last updated | 2026-10-14 |
| Items | 25 total, all open: 19 blocking, 6 non-blocking |

This file is the guide's **question log** (decision D-016). The `VG-xx` IDs are scoped to this guide and never renumbered. Each open item that affects the text is also a Word review comment by "Validation register" (VR).

> **Customer-facing guide.** This guide sends documents to customers. Its blocking items on parameters, recipients, multi-currency exclusions and failed delivery (`VG-05`, `VG-06`, `VG-10`, `VG-12`, `VG-17`) must be closed before it is tested on any real customer.

---

## 1. Evidence base

| Source | What it supports |
|---|---|
| 0, Topic 22 *Generate and Send Customer Statements* | Statement generation; Use Print Management; Open Only; Company Logo; customer delivery method; screen preview. Rated ready ("very detailed"). Suggested PG `PG-AR-018 Generate and Send Customer Statements`. |
| 0, Topic 17 *Excluding Customers from Statements* | Exclude Collection Fees toggle; multi-currency examples; known statement limitations. Suggested PG `PG-AR-014`. |
| 1, Module 6 | Sequences 6.3 (generate a statement), 6.4 (company logo), 6.5 (open transactions only), 6.6 (Print management destination), 6.8 (verify statement delivery), all ready; 6.9 (multiple related accounts) partial. The recording demonstrates statement parameters, "Only open", company logo, Print management destination and checking that the statement was sent. |
| 1, questions I *Customer statements* | Validate statement parameters; whether Only open is always selected; when the logo is required; the recipient source; the meaning and effect of Print management destination; the customer-send process; how users verify delivery; where sent statements are retained; how failed delivery is identified; multiple related accounts; multi-currency limitations and the customers to exclude; whether statements may be manually emailed; the required file format. |
| 2, Release 2 item 12 | Scope: open Statements, select Only open, include the company logo, use Print management destination, send to the customer, verify the delivery message, check the Collections sent mailbox if required. Status: ready with control validation. Required validation: approved statement parameters, multi-currency exclusion rules, failed delivery process, recipient source. |
| Statement Preview guide | Shared Statements page and customer selection items (its VG-01, VG-02). |

**Not available:** a transcript excerpt, timestamps, exact labels, the delivery message wording, the mailbox location, or any of the required validation answers in source 2.

---

## 2. Drafting decisions for this guide

| # | Decision | Reason |
|---|---|---|
| G1 | One parent topic, **1. Generate and Send a Customer Statement**, with **1.1 Send the Statement** and **1.2 Verify Statement Delivery**. | Sending and verifying are one task; verification is a source 1 sequence (6.8). |
| G2 | Previewing is referred to the Statement Preview guide, not repeated. | The two guides share the same parameters but differ in destination. |
| G3 | The checks before sending are Key concept rules and a prerequisite, not invented steps. | How users check exclusions and multi-currency limitations is not captured (`VG-12`, `VG-13`). |
| G4 | The failed-delivery step names the process without describing it. | The process is a required validation in source 2 (`VG-10`). |
| G5 | Multiple related accounts, manual emailing and file format are not covered. | Open questions in source 1 (`VG-14` to `VG-16`). |
| G6 | Treated as customer-facing: it is not tested on real customers until the parameter, recipient, exclusion and failed-delivery items close. | Incorrect instructions could affect customer communications (source 3.1). |

---

## 3. Validation gap register

**Priority:** **B** = blocks publication. **N** = non-blocking.

**Method:** **Test** = D365 test in a clean session. **Rec** = recording or transcript review. **SME** = subject-matter expert or process owner. **Dec** = project decision.

| ID | Item to confirm | Location in Word guide | Word comment | Priority | Method | Status |
|---|---|---|---|---|---|---|
| VG-01 | Exact label of the **Statements** page and its navigation path. Shared with Statement Preview VG-01. | 1.1 Step 2 | 9 | B | Test, Rec | Open |
| VG-02 | How the customer is selected. Shared with Statement Preview VG-02. | 1.1 Step 3 | 10 | B | Test, Rec | Open |
| VG-03 | Exact label of **Only open** and whether it must always be selected. | 1.1 Step 4 | 11 | B | Test, SME | Open |
| VG-04 | Exact label of the company logo option and when it must be included. | 1.1 Step 5 | 12 | B | Test, SME | Open |
| VG-05 | Exact label and the meaning and effect of **Print management destination**. | Key concepts; 1.1 Step 6 | 4, 13 | B | Test, SME | Open |
| VG-06 | Where the recipient address comes from (the recipient source). | Key concepts; 1.1 Step 6 | 4, 13 | B | SME | Open |
| VG-07 | The control that generates and sends the statement, for example **OK**. | 1.1 Step 7 | 14 | B | Test | Open |
| VG-08 | Wording and location of the delivery message. | Key concepts; 1.2 Step 1 | 5, 15 | B | Test, Rec | Open |
| VG-09 | When the Collections sent mailbox must be checked, where it is, and who can access it. | Key concepts; 1.2 Step 2 | 6, 16 | B | SME | Open |
| VG-10 | How failed delivery is identified, and the process to follow. | 1.2 Step 3 | 17 | B | SME | Open |
| VG-11 | Where sent statements are retained. | 1.2 PROCESS COMPLETE | 18 | N | SME | Open |
| VG-12 | The multi-currency statement limitations and which customers must be excluded because of them. | Key concepts (rule) | 7 | B | SME | Open |
| VG-13 | How users check whether a customer is excluded from statements (source 0, Topic 17). | Key concepts (rule) | 7 | N | Test, SME | Open |
| VG-14 | Statements for multiple related accounts (source 1, sequence 6.9: partial). | Not in guide | — | N | Dec | Open |
| VG-15 | Whether statements may ever be emailed manually. | Not in guide | — | N | SME | Open |
| VG-16 | The required statement file format. | Not in guide | — | N | SME | Open |
| VG-17 | The approved statement parameters. | Key concepts (rule) | 8 | B | SME | Open |
| VG-18 | Initiation events, for example a statement cycle or a customer request. | Part 1 Initiation; topic Initiation; Process table *When* | 2 | B | SME | Open |
| VG-19 | Stream, process area and business role name. Shared with the other AR Collections guides. | Stream table; Process table; Roles matrix | 3 | B | SME | Open |
| VG-20 | Business process owner (BPO). | Version history | 1 | B | SME | Open |
| VG-21 | Guide code and final title. Source 0 proposes `PG-AR-018 Generate and Send Customer Statements`. | Cover; file name | 0 | B | Dec | Open |
| VG-22 | Whether any reports or inquiries apply. If none, "No applicable reports". | Part 3 | 19 | B | SME | Open |
| VG-23 | The security role needed to send statements, and a test with it. | PROCESS START (1.1) | — | B | Test, SME | Open |
| VG-24 | SME factual review, a test by someone other than the author, and approval. | Whole guide | — | B | SME | Open |
| VG-25 | Recording timestamps for the statement demonstration. | Screenshot register | — | N | Rec | Open |

**Fastest route to closure:** the SME answers for source 2's required validation (`VG-05`, `VG-06`, `VG-10`, `VG-12`, `VG-17`) come first. After that, one controlled test on a test customer whose statements go to an internal mailbox closes `VG-01` to `VG-04`, `VG-07` and `VG-08`. The Statement Preview test closes the shared items `VG-01` and `VG-02` without sending anything.

---

## 4. Publication readiness

| Check | Status |
|---|---|
| Template structure is complete; unused examples are removed | Met |
| Process table rows match the Part 2 topics (1 row) | Met; values pending `VG-18` and `VG-19` |
| Parent topic Overview lists both subprocedures | Met |
| Standard navigation pattern | Partial: Entity check, then open Statements (`VG-01`) |
| Each procedure table restarts numbering at 1 | Met |
| Exact system labels | Open (`VG-01` to `VG-05`, `VG-07`, `VG-08`) |
| Business rules separate from procedure | Met (checks before sending in Key concepts) |
| Customer-facing controls validated | **Open** (`VG-05`, `VG-06`, `VG-10`, `VG-12`, `VG-17`) |
| Reports | Open (`VG-22`) |
| Roles, BPO, guide code | Open (`VG-19`, `VG-20`, `VG-21`) |
| Peer test, SME review, approval | Open (`VG-23`, `VG-24`) |
| Review comments resolved before release | Open (20 Word comments) |

---

## 5. Change log

| Date | Change |
|---|---|
| 2026-10-14 | Register created with the v0.1 SME review draft. |
