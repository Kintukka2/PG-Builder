# Validation Register: Vendor Invoices v1.0 (working draft)

| Field | Value |
|---|---|
| Guide (editable source) | [`CLAUDE-TBC-Vendor Invoices PG v1.0.docx`](../01-procedure-guides/CLAUDE-TBC-Vendor%20Invoices%20PG%20v1.0.docx) |
| Review PDF | [`CLAUDE-TBC-Vendor Invoices PG v1.0.pdf`](../01-procedure-guides/CLAUDE-TBC-Vendor%20Invoices%20PG%20v1.0.pdf) |
| Markdown preview | [`PG-Vendor-Invoices-v1.0-DRAFT.md`](../01-procedure-guides/PG-Vendor-Invoices-v1.0-DRAFT.md) |
| Status | Working draft v1.0 (D-057): legacy version 0.2 converted to the PG master template. Not shared yet; needs SME review and BPO sign-off. Version 0.2 stays the published guide until 1.0 passes its gates. |
| Last updated | 2026-11-12 |
| Items | 22 guide-level items (`VI`), all open: 17 blocking, 5 non-blocking. 37 Word review comments. |

This file is the guide's **question log**. Its items use the prefix `VI` (Vendor Invoices), which does not depend on the guide code, so the IDs stay stable when the code is allocated (`VI-01`). Each open item that affects the text is a Word review comment by "Validation register" (VR). `VI-19` is about removed content, so it has no comment.

---

## 1. Source

| Source | What this guide takes from it |
|---|---|
| *D365 F&O: Vendor Invoices (NZ) Procedure Guide*, version 0.2, released 30 January 2025 (author Michael Thurlow, BPO Ghada Boulos). Legacy file `04-D365_FO_Vendor_Invoices_PG.docx`, supplied by the user on 2026-11-12 and held outside this repository. | Every procedure, the roles, the high-level process, the reports and six screenshots. The legacy content is **reference evidence**: no item closes on it alone, and a test, a recording or an SME answer governs where it disagrees (same rule as D-044). |

---

## 2. Conversion decisions

| # | Decision | Reason |
|---|---|---|
| C1 | Rebuilt in the PG master template with every fixed component kept: cover, contents, version history, *About this guide*, color key, Parts 1 to 3 and *Additional Resources*. | User request: convert the old guide to the new look standard (T1, T2). |
| C2 | The seven legacy procedures become four major topics: **1 Create a Vendor Invoice** (1.1 Search for an Existing Purchase Order, 1.2 Create a Vendor Invoice from a Purchase Order, 1.3 Create a Manual Vendor Invoice, 1.4 Add an Attachment to a Vendor Invoice), **2 Submit a Vendor Invoice to the Workflow**, **3 Post a Vendor Invoice**, **4 Confirm a Purchase Order**. The Process table has one row per topic, plus row 0 for the vendor's email. | T2: related stages that deliver one outcome are subtopics of one major topic; the four topics match legacy high-level process rows 2 to 5. |
| C3 | Steps are rewritten as **Action / Description** rows, one action per row, with an italic verb and bold UI labels. Legacy rows with several actions, the *Field / Action* tables and the *If / Then* tables are split into rows or written as conditions in the Description. No D365 label, path or value is added. | T2 *Write clear procedure rows*. |
| C4 | Where the legacy step said "select the required entity" and "From the Navigation Pane, select ...", the template's standard navigation pattern is used: *Check* the **Entity**, *Click* **Modules**, *Navigate* to the page. Topics 3 and 1.3 also start with the entity check. | T2 *Use the standard navigation pattern*; README conventions. |
| C5 | Each procedure opens with **PROCESS START** and closes with **STEP COMPLETE** (with *Continue to* links) or, for topics 3 and 4, **PROCESS COMPLETE**. Topic 2 ends with STEP COMPLETE because posting follows. | T2 *Use process boundaries*. |
| C6 | **Accounts Payable Specialist** is used throughout. The legacy roles table, Process table and first two topics name it; the other five legacy topics name the Accounts Payable Officer (`VI-05`). | One role name across the Stream table, Process table, role matrix and topics (T2). |
| C7 | Key concepts are drawn only from legacy statements: purchase orders and requisitions, the two invoice types, match status, the workflow rules, and the Pending vendor invoices page. | T2 *Key concepts*: no invented terms or rules. |
| C8 | Each of the 12 legacy reports gets its own Heading 5 and Navigation / Description table, with the legacy labels and paths unchanged (`VI-18`). | T2 *Retain Part 3 Reports*. |
| C9 | The legacy *Reference-based training instructions* units are removed (`VI-19`). | The master template has no such unit. |
| C10 | The six legacy screenshots are kept beside their steps. The user name in the workflow screenshot is masked. The two workflow screenshots show the purchase order workflow and are flagged for replacement (`VI-20`). | Screenshots are optional and must not carry unneeded personal data (T2; README). |
| C11 | Prose is in English (United States); legacy UI labels such as *Enquiries and reports* and *Vendor ageing report* are kept as they appear (`VI-18`). | T2 language rule; README *UI labels match the D365 screen exactly*. |
| C12 | File name `CLAUDE-TBC-Vendor Invoices PG v1.0.docx`: `TBC` until the P2P code is allocated (`VI-01`), and `CLAUDE-` until publication (D-056). | Numbering standard; D-056. |

---

## 3. Legacy-to-new mapping

| Legacy topic (v0.2) | v1.0 location |
|---|---|
| Part 1 Overview and Context | Part 1 Part Description and Stream |
| Part 1 High-level process (rows 1 to 5) | Part 1 Process (rows 0 to 4) |
| Part 1 Roles and responsibilities | Part 1 Roles and responsibilities |
| Search for an existing purchase order | 1.1 |
| Create a vendor invoice from a purchase order | 1.2 |
| Create a manual vendor invoice | 1.3 |
| Add an attachment to a vendor invoice | 1.4 |
| Submit a vendor invoice to the workflow | 2 |
| Post a vendor invoice | 3 |
| Confirm a purchase order | 4 |
| Part 3 Standard (out-of-the-box) reports | Part 3 Reports (12 reports) |
| Reference-based training instructions (every topic) | Removed (`VI-19`) |
| Document control | Version history row 0.2 |

---

## 4. Guide-level items (`VI`)

**Priority:** **B** = blocks publication. **N** = non-blocking. **Method:** **Test** = D365 test in a clean session. **SME** = subject-matter expert or process owner. **Dec** = project decision.

| ID | Item to confirm | Location | Priority | Method | Status |
|---|---|---|---|---|---|
| VI-01 | Guide code to be allocated. Vendor Invoices is in the Purchase-to-Pay (P2P) stream, outside the O2C numbering standard (codes 200 to 299). The register owner allocates its code from the P2P numbering standard; until then the working file name uses TBC. The legacy file name was 04-D365_FO_Vendor_Invoices_PG. | Cover and version history | B | Dec | Open |
| VI-02 | Version 1.0 is a working draft converted from legacy version 0.2 (released 30 January 2025). Its procedures are legacy reference evidence and are not re-validated: check each topic against current D365 F&O or with the SME before use. Confirm that Ghada Boulos is still the BPO. Version 1.0 needs BPO sign-off. | Version history | B | SME, Dec | Open |
| VI-03 | Confirm the scope. The legacy title is Vendor Invoices (NZ) and vendors send invoices to the apanz mailbox, but Part 3 includes the Payment Times Reporting Scheme (PTRS), which is an Australian report. Confirm whether this guide covers New Zealand only, and which legal entity users select. | Part 1 Part Description; Part 3 PTRS | B | SME | Open |
| VI-04 | Confirm the stream. The legacy Context text says Vendor Invoices is part of the Purchase-to-Pay (P2P) stream, but the legacy stream table shows O2C. This draft uses Purchase-to-Pay (P2P). | Part 1 Stream | B | SME | Open |
| VI-05 | Confirm the role. The legacy Process table, the legacy roles table and the legacy topics Search for an Existing Purchase Order and Create a Vendor Invoice from a Purchase Order name the Accounts Payable Specialist. The other five legacy topics name the Accounts Payable Officer. This draft uses Accounts Payable Specialist throughout. Confirm the role, or whether an Accounts Payable Officer does topics 1.3, 1.4, 2, 3 and 4. | Part 1 Stream, Roles and responsibilities; every topic | B | SME | Open |
| VI-06 | Confirm the trigger. The legacy Process table says 'When a customer invoice is received'; this draft reads it as a vendor invoice. Confirm that vendors send every invoice to apanz@wisetechglobal.com, and whether invoices arrive any other way. | Part 1 Initiation and Process | B | SME | Open |
| VI-07 | Confirm how to find the purchase requisition for a vendor invoice on the All purchase requisitions page (for example, a filter by vendor or by purchase order number). The legacy step says only 'Click the relevant purchase requisition'. Confirm also why the search starts from purchase requisitions and not from All purchase orders. | Part 1 Key concepts; 1.1 step 4 | B | SME, Test | Open |
| VI-08 | Confirm that the purchase requisition status must be Closed, and what the Accounts Payable Specialist does if it is not. | Part 1 Key concepts; 1.1 step 4 | B | SME | Open |
| VI-09 | Test the steps that add the Purchase order column (right-click the line header, Insert columns, Update) in current D365 F&O, and confirm the labels. The legacy guide gave them as one Important note; this draft gives one action per row. | 1.1 steps 5 to 10 | N | Test | Open |
| VI-10 | Confirm that Default from is always set to Ordered quantity. The legacy screenshot shows Receive now quantity selected, with Ordered quantity, Registered quantity, Product receipt quantity and Registered quantity and services as the other options. | 1.2 step 3 | B | SME | Open |
| VI-11 | Confirm how to correct an invoice when the Match status is Failed: the common reasons for a failure, what the Accounts Payable Specialist may change on the invoice, and who to contact when it cannot be corrected. The legacy step says only 'correct the invoice as required before continuing'. | Part 1 Key concepts; 1.2 step 10 | B | SME | Open |
| VI-12 | Test steps 11 and 12. After step 9 the user is on the Invoice matching details page, so Back returns to the Vendor invoice page. When the Match status is Passed, the user is already on the Vendor invoice page. Confirm when Back is needed. | 1.2 step 12 | N | Test | Open |
| VI-13 | Confirm the rule for each line value: how to choose the procurement category, and whether the quantity and unit price come from the vendor's invoice. The legacy values (PRIN > Printing and Stationery, 10, Each, 10) are examples. Confirm whether Unit is always Each, and whether other header or line fields are needed (for example tax or financial dimensions). | 1.3 steps 10 to 14 | B | SME | Open |
| VI-14 | Confirm the workflow rules: the currency of the $100,000 threshold, what Treasury does with the notification (information only, or an approval), how long the workflow takes to reach Completed, and what to do if the status is not Completed (for example, rejected). | Part 1 Key concepts; topic 2 | B | SME | Open |
| VI-15 | Confirm what it means when a posted invoice is still displayed on the Pending vendor invoices page, and how the user returns to that page after posting. For an invoice that is no longer displayed, the legacy step says 'The invoice has been confirmed'; this draft reads it as posted. | Part 1 Key concepts; topic 3 step 6 | B | SME, Test | Open |
| VI-16 | Confirm the path to view a posted invoice. The legacy note gives All purchase orders, then Invoice > Generate > Invoice, which is the path that creates an invoice in 1.2 step 2. The legacy path also starts from Accounts payable, while topic 4 opens All purchase orders from Procurement and sourcing. | Topic 3 PROCESS COMPLETE | B | Test | Open |
| VI-17 | Confirm what happens after the purchase order is confirmed: whether the user returns to topic 3 to post the invoice again. The legacy step says the All purchase orders page opens when a purchase order is clicked; this draft says the purchase order opens. | Topic 4 | B | SME, Test | Open |
| VI-18 | Check each report label and navigation path in current D365 F&O (the legacy guide uses labels such as Enquiries and reports and Vendor ageing report). Confirm which reports belong in this guide: the Vendor posted payment journal report may belong with Vendor Payments, and the PTRS is Australian (VI-03). Supply a link to the D365 F&O Reports: Run a Standard Report Quick Reference Card. | Part 3 Reports | B | Test, SME | Open |
| VI-19 | The legacy topics ended with Reference-based training instructions, which the master template does not include, so they are removed. They told trainees to use an assigned purchase order, vendor or invoice and to contact the 'Customer Invoices champion'. Confirm where training instructions now live, and whether a Vendor Invoices champion should be named. | Removed from every topic | N | Dec | Open |
| VI-20 | Replace these screenshots. They show the Purchase order workflow (Document type: Purchase orders), not the vendor invoice workflow that this topic submits. Confirm which workflow the vendor invoice is submitted to. The user name in the first screenshot is masked. | Topic 2 steps 5 and 6 | B | Test, SME | Open |
| VI-21 | Confirm the related P2P guides (Vendor Onboarding and Maintenance, Purchase Requisitions, Vendor Payments), with their titles and codes, so that this guide can link to them. | Part 1 Part Description | N | Dec | Open |
| VI-22 | The screenshots in topic 1 are the legacy screenshots (January 2025). Check that each one matches current D365 F&O, and recapture any that do not in a clean session, with data masked. | 1.1 step 11; 1.2 steps 3, 7 and 9 | N | Test | Open |

---

## 5. Review comments by section

Every review comment in the Word guide, in document order.

| Section | Items |
|---|---|
| Version history | `VI-02`, `VI-01` |
| Part 1 High-level process | `VI-03`, `VI-21`, `VI-06`, `VI-04`, `VI-05`, `VI-06` |
| Part 1 Roles and responsibilities | `VI-05` |
| Part 1 Key concepts | `VI-07`, `VI-08`, `VI-11`, `VI-14`, `VI-15` |
| Topic 1 Create a Vendor Invoice | `VI-05` |
| 1.1 Search for an Existing Purchase Order | `VI-07`, `VI-08`, `VI-09`, `VI-22` |
| 1.2 Create a Vendor Invoice from a Purchase Order | `VI-10`, `VI-11`, `VI-12` |
| 1.3 Create a Manual Vendor Invoice | `VI-05`, `VI-13` |
| 1.4 Add an Attachment to a Vendor Invoice | `VI-05` |
| Topic 2 Submit a Vendor Invoice to the Workflow | `VI-14`, `VI-05`, `VI-20`, `VI-14` |
| Topic 3 Post a Vendor Invoice | `VI-05`, `VI-15`, `VI-16` |
| Topic 4 Confirm a Purchase Order | `VI-05`, `VI-17`, `VI-17` |
| Part 3 Reports | `VI-18`, `VI-03` |

---

## 6. Publication gate status

| Gate | Status |
|---|---|
| Identified | Done: legacy v0.2 supplied for conversion (2026-11-12) |
| Source reviewed | Done: legacy content mapped (section 3) and conflicts raised as items |
| Gap validated | Open: 22 items (17 blocking) |
| Drafted | Done: v1.0 working draft in the master template |
| System tested | Not started (`VI-09`, `VI-12`, `VI-15` to `VI-18`, `VI-20`, `VI-22`) |
| SME validated | Not started |
| Process-owner approved | Not started: BPO to confirm (`VI-02`) |
| Published | No. Remove the `CLAUDE-` prefix and allocate the code (`VI-01`) at publication |
