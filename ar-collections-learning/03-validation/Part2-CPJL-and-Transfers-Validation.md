# Validation Register: Part 2 Customer Payment Journal and Transfer Guides

| Field | Value |
|---|---|
| Covers | [Transfer Funds Between Customer Accounts](../01-procedure-guides/PG-AR-Transfer-Funds-Between-Customer-Accounts-DRAFT.md) (`TF`) · [Transfer a Parent Account Payment Across Child Accounts](../01-procedure-guides/PG-AR-Transfer-Parent-Payment-Across-Child-Accounts-DRAFT.md) (`PC`) · [Restore a Written-Off or Overpayment Amount](../01-procedure-guides/PG-AR-Restore-Written-Off-Overpayment-DRAFT.md) (`RO`) · [Customer Payment Journal controls reference](../06-reference-guides/REF-AR-Customer-Payment-Journal-Controls-DRAFT.md) (`CPJ`) |
| Screenshot registers | [Transfer Funds](../02-screenshot-registers/PG-AR-Transfer-Funds-Between-Customer-Accounts-Screenshots.md) · [Parent Payment](../02-screenshot-registers/PG-AR-Transfer-Parent-Payment-Across-Child-Accounts-Screenshots.md) · [Restore](../02-screenshot-registers/PG-AR-Restore-Written-Off-Overpayment-Screenshots.md) |
| Source | AR Training D365 Part 2 update pack (sources 4.0 to 4.7 in the [project notes](../05-project-notes/Project-Context-and-Decisions.md#1-source-documents)) |
| Last updated | 2026-10-23 |
| Items | 46 total, all open: 38 blocking, 8 non-blocking |

This file is the **question log** for the three Part 2 working drafts and the shared controls reference (decision D-016). One register covers all four documents because they share most of their controls. IDs are prefixed by scope and never renumbered (decision D-038):

| Prefix | Scope |
|---|---|
| `SRC` | The Part 2 source itself |
| `GOV` | Governance shared by all three guides |
| `CPJ` | Customer payment journal controls shared by all three guides and the reference |
| `TF` | Transfer Funds Between Customer Accounts only |
| `PC` | Transfer a Parent Account Payment Across Child Accounts only |
| `RO` | Restore a Written-Off or Overpayment Amount only |

Customer Pools has its own register: [Customer-Pools-Validation.md](Customer-Pools-Validation.md).

> **Higher-risk guides.** All three guides move or reinstate customer funds. They stay working drafts, and are not tested on real customer accounts or finalised, until their blocking items close and the Part 2 recording has been checked (`SRC-01`; source 3.1 "do not draft as final"; README development gates).

---

## 1. Evidence base

| Source | What it supports | Limits |
|---|---|---|
| 4.0 *Source Notes Part 1 and Part 2* | Part 2 topic inventory: CPJL for restoring written-off or overpayment amounts and for transfers between customer accounts; header and line descriptions; dates; customer and currency coding; the Overpayment ledger offset; a two-line transfer using the bank-to-bank transfer clearing account; multi-account distribution; partial allocation; Simulate Posting; line-completion discipline; balance, date and currency controls; error escalation to "SYD" during training; "PG/Ava" follow-up support. Part 1: D365 lacks a reliable parent-child indicator. | Teams AI-generated meeting notes. Not checked against the recording. |
| 4.1 *Updated Learning Architecture* | Priority 2 adds a Customer Payment Journals module. Priority 3 adds customer account transfers: two strong PG candidates, partial allocation covered, parent-child identification still partial. | Summary only. |
| 4.2 *Updated Development Roadmap* | Release 3A, items 14 to 19: CPJL reference, transfer between customers, parent to multiple children, partial allocation, restoration, Simulate Posting. | Renumbers the backlog (see the project notes, I-10). |
| 4.3 *Updated Readiness and Gap Matrix* | Readiness of each Part 2 topic. The CPJL validation checklist (14 checks) and the Customer Pools checklist (7 checks). | Summary only. |
| 4.4 *PG Draft Transfer Funds Between Customer Accounts* | A 15-step draft: CPJL, description, date, source debit, line description, Ledger offset, clearing account, line completion, destination credit, balance, Simulate Posting, post. | The draft names its own gaps (menu path, clearing account, offset on both lines, posting and approval, verification, reversal). |
| 4.5 *PG Draft Parent to Child Account Transfer* | An 11-step draft: confirm the allocation, parent debit, one credit per child, currency, descriptions, clearing account, totals, residual left on the parent with a note, Simulate Posting, post. Example: $8,000 of a $10,000 receipt distributed, $2,000 left. | The example amounts are examples only, not thresholds. |
| 4.6 *PG Draft Restore Written-Off Overpayment* | A 13-step draft: CPJL, description, date, customer, credit, currency, leave financial tags, invoice number and bank account blank, Ledger offset, Overpayment ledger, leave pre-populated dimensions unchanged, line completion, Simulate Posting, post. | Names its own gaps (path, Overpayment ledger, dimension exceptions, backdating, posting and approval, verification, reversal). |
| 4.7 *Claude Code Handover Prompt* | The tasks and source discipline for this batch. | Instructions, not process evidence. |
| Favorites guide (sources 3.2 and 1) | **Customer payment journal** is a key AR Collections page in the **Credit and collections** module (recording frame 00:33:51). | Its menu location is still open as Favorites `VG-04`. |
| Workspace guide (sources 0, 1 and 2) | The workspace shows **Payment journals not posted** and **Open payment journals**. | Labels still open as Workspace `VG-05` and `VG-07`. |

**Not available in any source:** the exact navigation path and controls, field labels, the journal name display, the account labels or values for the Overpayment ledger and the clearing account, who may post, whether approval is needed, how to verify the result after posting, and how to correct or reverse a posted journal.

---

## 2. Drafting decisions

| # | Decision | Reason |
|---|---|---|
| G1 | The three guides and the reference are **working Markdown drafts**. They follow the master template's section order so that the Word build is mechanical, but they are not built in Word until the recording is checked (D-037). | Handover task 5. Avoids building Word review comments on unchecked AI notes. |
| G2 | Each guide uses one parent topic with three subprocedures (Restore: two): create the journal and the first line, add the remaining lines, then validate and post. | Matches the source drafts' sequence. The validate-and-post subprocedure is shared. |
| G3 | **Partial allocation** is part of the Parent Payment guide (steps 1.1.8 and 1.3.5), not a separate guide. **Simulate Posting** is covered in the reference and in each guide's validate-and-post subprocedure (D-039). | Roadmap items 17 and 19 have no steps beyond the ones already in those guides. |
| G4 | Steps the notes imply but do not show precisely enough (opening the journal lines, adding a line, the Post control, checking the result after posting) are **validation placeholders**, not invented steps. | Handover task 10; D-020. |
| G5 | The notes give "leave financial tags, invoice number and bank account blank" and "do not change pre-populated dimensions" for **restoration entries only**. They are steps in the Restore guide and questions for the two transfer guides (`CPJ-10`, `CPJ-11`). | The notes do not say whether these rules apply to transfers. |
| G6 | No role is named as able to post a CPJL, and no approval rule is stated. | Handover source discipline; `CPJ-16`, `CPJ-17`. |
| G7 | Troubleshooting is limited to what the notes support: read a Simulate Posting error, correct it, and ask for help if it cannot be resolved. It sits in the procedure row (D-018). | The support route is not confirmed (`CPJ-15`). |
| G8 | Every guide starts with the standard navigation pattern (*Check* the **Entity**). The location of **Customer payment journal** comes from the Favorites guide, not from Part 2. | D-015; Favorites `VG-04`. |

---

## 3. Validation gap register

**Priority:** **B** = blocks publication. **N** = non-blocking.

**Method:** **Test** = D365 test in a clean session. **Rec** = recording or transcript review. **SME** = subject-matter expert or process owner. **Dec** = project decision.

**Location** names the guide (`TF`, `PC`, `RO`) or the reference (`REF`) and the step or section.

### 3.1 Source (`SRC`)

| ID | Item to confirm | Location | Priority | Method | Status |
|---|---|---|---|---|---|
| SRC-01 | Check every step in the three guides and every control in the reference against the Part 2 recording or transcript. The notes are Teams AI-generated. | All four documents | B | Rec | Open |
| SRC-02 | Recording timestamps for the restoration, two-line transfer, parent-to-multiple-child, partial allocation and Simulate Posting demonstrations. | Screenshot registers | N | Rec | Open |
| SRC-03 | What "PG/Ava follow-up support" in the notes refers to, and whether the guides should point to it. | REF Related content | N | SME | Open |
| SRC-04 | Whether to adopt the Part 2 roadmap's Release 3A placement for transfers and restoration. Source 2 ranks *Transfer funds between accounts* 27, in Release 4. Proposed in D-036. | Document control (all) | N | Dec | Open |

### 3.2 Governance (`GOV`)

| ID | Item to confirm | Location | Priority | Method | Status |
|---|---|---|---|---|---|
| GOV-01 | Stream, process area and the business role that prepares these journals. Confirm whether Collections Officers do this work or another team does. | Part 1 Stream, Process and Roles (all) | B | SME | Open |
| GOV-02 | Business process owner (BPO) for each guide. | Document control (all) | B | SME | Open |
| GOV-03 | Guide codes and final titles (D-006). | Document control (all) | B | Dec | Open |
| GOV-04 | Whether any reports or inquiries apply. If none, "No applicable reports". | Part 3 (all) | B | SME | Open |
| GOV-05 | SME factual review, a test by someone other than the author, and approval. | Whole guide (all) | B | SME | Open |

### 3.3 Customer payment journal controls (`CPJ`)

| ID | Item to confirm | Location | Priority | Method | Status |
|---|---|---|---|---|---|
| CPJ-01 | Navigation and controls: the path to **Customer payment journal** (Favorites `VG-04` places it in **Credit and collections**), the control that creates a new journal, how the journal lines are opened, and how a new line is added. | TF/PC/RO steps 1.1.2, 1.1.3, 1.1.5, 1.2.1; REF control 1 | B | Test, Rec | Open |
| CPJ-02 | How the CPJL journal name or code appears and is selected when a journal is created. | TF/PC/RO step 1.1.3; REF control 1 | B | Test, Rec | Open |
| CPJ-03 | Exact labels of the header **Description** field and the line **Description** field. | TF/PC/RO steps 1.1.4 and line descriptions; REF control 2 | B | Test, Rec | Open |
| CPJ-04 | The description standard: required wording and customer codes for header and line descriptions. The notes give examples only. | TF/PC/RO description steps; REF control 2 | N | SME | Open |
| CPJ-05 | The date field label and default, and the backdating rule. The notes give two wordings: the original payment date may be used for a wrong-account correction "when appropriate" (TF), and a prior-period date only when required and the period is open (RO). Confirm the rule and who decides. | TF/PC/RO date step; REF control 3 | B | Test, SME | Open |
| CPJ-06 | How debits and credits are shown and entered: separate **Debit** and **Credit** fields, or signed amounts. | TF/PC/RO amount steps; REF control 5 | B | Test | Open |
| CPJ-07 | The currency field label and behavior, and what to do if the original currency cannot be used. | TF/PC/RO currency rule; REF control 4 | B | Test, SME | Open |
| CPJ-08 | Exact labels of **Offset account type**, its **Ledger** value and the offset (main) account field, and how the account lookup works. Also whether the offset is entered on each line. | TF/PC/RO offset steps; REF control 6 | B | Test | Open |
| CPJ-09 | Whether the guides should show account numbers for the Overpayment ledger and the bank-to-bank transfer clearing account, or only names to search for. | REF control 6 | B | Dec, SME | Open |
| CPJ-10 | Fields to leave blank (financial tags, invoice number, bank account): their exact labels, and whether the rule also applies to transfers. | RO step 1.1.11; TF/PC Key concepts; REF control 7 | B | Test, SME | Open |
| CPJ-11 | Pre-populated financial dimensions: confirm they are never changed, whether there are exceptions, and whether the rule also applies to transfers. | RO step 1.1.14; TF/PC Key concepts; REF control 8 | B | SME | Open |
| CPJ-12 | Which fields complete when the user tabs through a line (the notes mention voucher information). | TF/PC/RO "Complete the line" steps; REF control 9 | N | Test, Rec | Open |
| CPJ-13 | Where the journal totals are shown, to check that debits equal credits. | TF/PC step 1.3.1; REF control 10 | B | Test | Open |
| CPJ-14 | The **Simulate Posting** label and location, and how results are shown. The notes describe a blue result as ready and red results as errors. | TF/PC step 1.3.2, RO step 1.2.1; REF control 11 | B | Test, Rec | Open |
| CPJ-15 | Common Simulate Posting errors and their fixes, and the support route when an error cannot be resolved. The notes mention escalation to "SYD" during training. | TF/PC step 1.3.3, RO step 1.2.2; REF control 11 | B | SME | Open |
| CPJ-16 | The **Post** control label and location, and which role may post a CPJL. | TF/PC step 1.3.4, RO step 1.2.3; REF control 12 | B | Test, SME | Open |
| CPJ-17 | Whether CPJL transfers and restorations need approval (for example a workflow), and whether any value threshold applies. The amounts in the notes are examples, not thresholds. | TF/PC step 1.3.4, RO step 1.2.3; REF control 12 | B | SME | Open |
| CPJ-18 | How to confirm the result after posting, for example in the customer's transactions (see the Customer Account guide). | TF step 1.3.5, PC step 1.3.6, RO step 1.2.4 | B | Test, SME | Open |
| CPJ-19 | How a posted journal is corrected or reversed. | PROCESS COMPLETE (all); REF "Not covered" | B | SME | Open |
| CPJ-20 | What to do with an unposted journal that is no longer needed. It would appear under **Payment journals not posted** in the workspace (Workspace `VG-05`). | REF "Not covered" | N | SME, Test | Open |
| CPJ-21 | The security role needed to open and create a CPJL, and a test with it. A missing page or control may have a security cause; that is a possible cause, not a diagnosis. | PROCESS START (all) | B | Test, SME | Open |

### 3.4 Transfer Funds Between Customer Accounts (`TF`)

| ID | Item to confirm | Location | Priority | Method | Status |
|---|---|---|---|---|---|
| TF-01 | Initiation events. The notes give two: a payment posted to the wrong customer account, and funds to move between related accounts once the destination is confirmed. Confirm them and add any others. | Part 1 Initiation; topic Initiation | B | SME | Open |
| TF-02 | How the correct destination account is confirmed, and what evidence is kept. | PROCESS START (1.1); Key concepts | B | SME | Open |
| TF-03 | The exact label and value of the bank-to-bank transfer clearing account. | Key concepts; steps 1.1.11 and 1.2.6 | B | Test, SME | Open |
| TF-04 | Whether the destination line also takes the Ledger offset and the clearing account in the demonstrated UI, as the source draft implies (step 12). | Steps 1.2.5 and 1.2.6 | B | Rec, Test | Open |
| TF-05 | What to do when the payment is already settled against invoices on the wrong account. Not covered by the notes. | PROCESS START (1.1) | B | SME | Open |
| TF-06 | Whether transfers between customers in different legal entities are in scope. Not covered by the notes. | Part Description (out of scope) | N | SME | Open |

### 3.5 Transfer a Parent Account Payment Across Child Accounts (`PC`)

| ID | Item to confirm | Location | Priority | Method | Status |
|---|---|---|---|---|---|
| PC-01 | The formal method or reference for confirming a parent-child relationship. The Part 1 notes say D365 has no reliable parent-child indicator. Linked to backlog rank 26, *Identify parent-child accounts* (knowledge article, not ready). | Key concepts; PROCESS START (1.1) | B | SME | Open |
| PC-02 | The evidence needed to confirm the allocation to each child account (the notes name remittance and customer confirmation), and where it is kept. | Key concepts; PROCESS START (1.1) | B | SME | Open |
| PC-03 | The clearing-account treatment on a distribution with several lines: whether the parent line and each child line take the Ledger offset and the clearing account. | Steps 1.1.10, 1.1.11, 1.2.5 and 1.2.6 | B | Rec, Test | Open |
| PC-04 | Where, how and at what point the note that explains a residual left on the parent account is added (for example a customer note or the journal line), and its wording. | Key concepts; step 1.3.5 | B | Rec, SME | Open |
| PC-05 | Who follows up a residual left on the parent account, and when. | Key concepts | N | SME | Open |
| PC-06 | Initiation events. The notes give one: a payment held on a parent account must be distributed to one or more confirmed child accounts. | Part 1 Initiation; topic Initiation | B | SME | Open |

### 3.6 Restore a Written-Off or Overpayment Amount (`RO`)

| ID | Item to confirm | Location | Priority | Method | Status |
|---|---|---|---|---|---|
| RO-01 | The exact label, value and lookup term of the Overpayment ledger (main account). | Key concepts; step 1.1.13 | B | Test, SME | Open |
| RO-02 | Scope: whether restoring a written-off amount and putting an overpayment back are the same procedure, and when a write-off should be reversed or cancelled instead. Linked to the write-off backlog items (ranks 18 to 20). | Part Description; Key concepts | B | SME | Open |
| RO-03 | Who authorizes putting an amount back on a customer account, and what evidence is kept. | PROCESS START (1.1) | B | SME | Open |
| RO-04 | Initiation events: when a restoration is needed. | Part 1 Initiation; topic Initiation | B | SME | Open |

---

## 4. Coverage of the pack's CPJL checklist

Every check in the CPJL validation checklist in source 4.3 maps to an item above.

| Source 4.3 check | Item |
|---|---|
| Navigation path to Customer payment journal and New journal | CPJ-01 |
| Journal name or code display for CPJL | CPJ-02 |
| Header Description and line Description labels | CPJ-03 |
| Date field label and backdating rule | CPJ-05 |
| Debit and credit sign convention as displayed | CPJ-06 |
| Customer currency field and behavior | CPJ-07 |
| Overpayment main account lookup term, and whether account numbers are documented | RO-01, CPJ-09 |
| Bank-to-bank transfer clearing account label and value | TF-03 |
| Whether offset account type and account are entered per line, and whether both transfer lines take the same clearing account | CPJ-08, TF-04, PC-03 |
| What must be left blank: financial tags, invoice number, bank account | CPJ-10 |
| Pre-populated financial dimensions must not change; exceptions | CPJ-11 |
| Simulate Posting navigation and success or error presentation | CPJ-14 |
| Posting permissions and approval for CPJL transfers | CPJ-16, CPJ-17 |
| Correction or reversal after posting | CPJ-19 |

The gaps the three source drafts list are also covered: verification after posting (`CPJ-18`), the parent-child relationship method (`PC-01`), the residual note (`PC-04`), dimension exceptions (`CPJ-11`) and backdating governance (`CPJ-05`).

---

## 5. Publication readiness

| Check | Transfer Funds | Parent Payment | Restore |
|---|---|---|---|
| Steps checked against the Part 2 recording | Open (`SRC-01`) | Open (`SRC-01`) | Open (`SRC-01`) |
| Built in the PG master template | Not started (D-037) | Not started | Not started |
| Exact system labels and navigation | Open (`CPJ-01` to `CPJ-03`, `CPJ-08`, `CPJ-14`, `CPJ-16`) | Open (same) | Open (same) |
| Account labels and values | Open (`TF-03`, `CPJ-09`) | Open (`TF-03`, `CPJ-09`) | Open (`RO-01`, `CPJ-09`) |
| Business rules (dates, currency, blank fields, dimensions) | Open (`CPJ-05`, `CPJ-07`, `CPJ-10`, `CPJ-11`) | Open (same) | Open (same) |
| Business checks before processing | Open (`TF-02`, `TF-05`) | Open (`PC-01`, `PC-02`) | Open (`RO-02`, `RO-03`) |
| Posting permission, approval, verification, reversal | Open (`CPJ-16` to `CPJ-19`) | Open (same) | Open (same) |
| Roles, BPO, guide code, reports | Open (`GOV-01` to `GOV-04`) | Open (same) | Open (same) |
| SME review, peer test, approval | Open (`GOV-05`) | Open (`GOV-05`) | Open (`GOV-05`) |

---

## 6. Change log

| Date | Change |
|---|---|
| 2026-10-23 | Register created from the AR Training D365 Part 2 update pack, with the three working drafts and the controls reference. |
