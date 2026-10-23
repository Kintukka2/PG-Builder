# D365 F&O: AR Collections Transfer a Parent Account Payment Across Child Accounts Procedure Guide

> **WORKING DRAFT. Not validated, not approved, not for publication.**
>
> This is a working Markdown draft built from the *AR Training D365* Part 2 update pack. It follows the section order of the PG master template, but it has not been built in Word yet (decision D-037). The Word build follows once the Part 2 recording has been checked.
>
> **Higher-risk guide.** It moves funds between customer accounts and relies on a parent-child relationship that D365 does not reliably show. Do not use it on real customer accounts, and do not finalise it, until its blocking items close (source 3.1; README development gates).
>
> **Evidence.** The steps come from Teams AI-generated notes of the Part 2 session and the pack's working draft (sources 4.0 and 4.5). Neither has been checked against the recording (`SRC-01`). `[XX-nn]` markers point to items in the [validation register](../03-validation/Part2-CPJL-and-Transfers-Validation.md). Where the notes do not give a detail precisely enough, the step carries a **validation placeholder** instead of a guess. The [step evidence](#step-evidence) table shows the source of each step.

## Document control

| Field | Value |
|---|---|
| Guide code and final title | To be confirmed `[GOV-03]` |
| Version | 0.1 working draft, October 2026. Author: Daniel Moreira. |
| Business process owner | To be confirmed `[GOV-02]` |
| Status and gate | Working draft. Gate: Drafted (working Markdown). Next: check against the Part 2 recording, then build in the master template. |
| Roadmap | Part 2 roadmap items 16 and 17 (partial allocation), Release 3A (proposed D-036). New to the backlog. |
| Shared controls | [Customer Payment Journal controls reference](../06-reference-guides/REF-AR-Customer-Payment-Journal-Controls-DRAFT.md) |
| Screenshot register | [PG-AR-Transfer-Parent-Payment-Across-Child-Accounts-Screenshots.md](../02-screenshot-registers/PG-AR-Transfer-Parent-Payment-Across-Child-Accounts-Screenshots.md) |

**Version history**

| ID | Date | Author/s | BPO | Description of change |
|---|---|---|---|---|
| 0.1 | October 2026 | Daniel Moreira | To be confirmed `[GOV-02]` | Working draft created from the AR Training D365 Part 2 update pack. Not validated or approved. |

---

## Part 1: What do I need to know? (AR Collections Transfer a Parent Account Payment Across Child Accounts)

### High-level process

##### Part Description

This guide explains how to distribute a payment held on a parent customer account to one or more child customer accounts with a **Customer payment journal** (CPJL). One debit line moves the amount off the parent account, and one credit line for each child account receives its share. It also covers a partial allocation, where only the confirmed part of the payment is moved and the rest stays on the parent account.

A transfer between two unrelated customer accounts is covered in the *Transfer Funds Between Customer Accounts* guide.

Out of scope until confirmed: how to identify a parent-child relationship in D365 (`PC-01`; backlog rank 26), approval workflow (`CPJ-17`) and correcting or reversing a posted journal (`CPJ-19`).

##### Initiation

- A payment held on a parent customer account must be distributed to one or more confirmed child accounts. `[PC-06]`

##### Stream

| Stream | Process Area | Key Roles |
|---|---|---|
| Accounts Receivable `[GOV-01]` | AR Collections `[GOV-01]` | • To be confirmed `[GOV-01]` |

##### Process

| # | Action | Who | When | Where |
|---|---|---|---|---|
| 1 | [Transfer a Parent Account Payment Across Child Accounts](#1-transfer-a-parent-account-payment-across-child-accounts) | To be confirmed `[GOV-01]` | When a payment on a parent account must be distributed to confirmed child accounts | D365 |

### Roles and responsibilities

##### Overview

The sources do not say which business role prepares this journal, which role may post it (`CPJ-16`) or whether it needs approval (`CPJ-17`).

| Tasks / Business Roles | To be confirmed `[GOV-01]` |
|---|---|
| [Transfer a Parent Account Payment Across Child Accounts](#1-transfer-a-parent-account-payment-across-child-accounts) | R |

### Key concepts

##### Overview

Before you start, you need to know how the relationship and the allocation are confirmed, how the journal distributes the payment, and what happens to any amount that is not allocated.

##### Parent and child accounts

| Term | Description |
|---|---|
| **Parent-child relationship** | The Part 1 notes say D365 does not provide a reliable parent-child indicator. Do not rely on account names alone. `[PC-01]` |
| **Confirmed allocation** | Which child accounts the payment belongs to, and how much each receives, confirmed from remittance, customer confirmation or other validated evidence. `[PC-02]` |
| **Distribution** | One debit on the parent account can be distributed across several child credits, if the child credits add up to the parent debit. |
| **Residual** | In a partial allocation, the part of the payment that is not yet allocated. It stays on the parent account, with a note that explains its purpose. `[PC-04, PC-05]` |

The notes use the example of a $10,000 receipt where $8,000 is distributed to child accounts and $2,000 stays on the parent account. The amounts are an example only, not a threshold.

##### Before you post

| Rule | Description |
|---|---|
| **Confirm before processing** | Confirm the relationship and the allocation before you create the journal. `[PC-01, PC-02]` |
| **Use the original currency** | Keep every line in the currency of the original receipt. `[CPJ-07]` |
| **Describe every line** | Use descriptions that let the transfer be identified in each customer's history. `[CPJ-03, CPJ-04]` |
| **Use the clearing account** | Use **Ledger** as the offset type and the bank-to-bank transfer clearing account as the offset. `[TF-03, PC-03]` |
| **Balance the distribution** | The child credits must add up to the amount debited from the parent account. `[CPJ-13]` |
| **Simulate before posting** | Run Simulate Posting and resolve every error before you post. `[CPJ-14]` |
| **Blank fields and dimensions** | For restoration entries, the notes say to leave financial tags, invoice number and bank account blank, and not to change pre-populated dimensions. Whether this also applies to transfers is not confirmed. `[CPJ-10, CPJ-11]` |

---

## Part 2: How do I do it? (AR Collections Transfer a Parent Account Payment Across Child Accounts)

### 1. Transfer a Parent Account Payment Across Child Accounts

##### Description

Use this topic to distribute a payment from a parent customer account to confirmed child accounts. You create a CPJL journal, enter one debit line for the parent account and one credit line for each child account, check that the child credits match the parent debit, run Simulate Posting and post. If only part of the payment is allocated, you move only that part and record why the rest stays on the parent account.

##### Responsibility

- To be confirmed: prepares and posts the distribution journal. `[GOV-01, CPJ-16]`

##### Initiation

- A payment held on a parent customer account must be distributed to one or more confirmed child accounts. `[PC-06]`

##### Topic Overview

This topic includes these steps:

| Step | Description |
|---|---|
| [Create the Journal and Enter the Parent Line](#11-create-the-journal-and-enter-the-parent-line) | Create the CPJL and enter the debit for the amount being moved off the parent account. Output: the parent line is complete. |
| [Enter the Child Lines](#12-enter-the-child-lines) | Enter one credit line for each child account. Output: the distribution is entered. |
| [Validate and Post the Journal](#13-validate-and-post-the-journal) | Check the totals, run Simulate Posting, correct errors, post, and record any residual. Output: the distribution is posted. |

#### 1.1 Create the Journal and Enter the Parent Line

##### Procedure

Complete these steps to create the journal and enter the parent line:

| Action | Description |
|---|---|
| *PROCESS START* (light blue) | *Pre-requisites:*<br>• Access to D365 and to **Customer payment journal**. `[CPJ-21]`<br>• A confirmed parent-child relationship. `[PC-01]`<br>• A confirmed allocation: each child account and its amount, and the total to move. `[PC-02]`<br>• The currency of the original receipt.<br>*Responsibility:*<br>• To be confirmed `[GOV-01]` |
| 1. *Check* the **Entity**. | Confirm you are signed into the correct **Legal Entity** (top-right). |
| 2. *Open* **Customer payment journal**. `[CPJ-01]` | The Favorites guide places **Customer payment journal** in the **Credit and collections** module. If you have added it to your favorites, open it from there.<br>**Validation placeholder (`CPJ-01`):** exact navigation path. |
| 3. *Create* a new journal. `[CPJ-01, CPJ-02]` | Start a new CPJL journal.<br>**Validation placeholder (`CPJ-01`, `CPJ-02`):** the control that creates the journal, and how the CPJL journal name is selected. |
| 4. *Enter* the journal description. `[CPJ-03, CPJ-04]` | Describe the transfer clearly, so it identifies the parent and child transfer. |
| 5. *Open* the journal lines. `[CPJ-01]` | **Validation placeholder (`CPJ-01`):** how the journal lines are opened from the journal. |
| 6. *Enter* the transaction date. `[CPJ-05]` | **Validation placeholder (`CPJ-05`):** the date field label, the date to use and whether it is set on the journal or on each line. |
| 7. *Select* the parent customer account. | Select the parent account that holds the payment. The customer name fills in automatically. |
| 8. *Enter* the amount to move as a debit. `[CPJ-06, CPJ-07]` | Enter the total being moved off the parent account as a debit, in the currency of the original receipt. In a partial allocation, enter only the confirmed amount. The rest stays on the parent account.<br>**Validation placeholder (`CPJ-06`):** how debits are entered. |
| 9. *Enter* the line description. `[CPJ-03, CPJ-04]` | Use a description that identifies the transfer in the parent account's history. |
| 10. *Select* **Ledger** as the **Offset account type**. `[CPJ-08, PC-03]` | Set the offset account type to **Ledger**. |
| 11. *Select* the bank-to-bank transfer clearing account. `[TF-03, PC-03]` | Select the clearing account as the offset account.<br>**Validation placeholder (`TF-03`, `PC-03`):** the account label and value, and whether the parent line takes the offset. |
| 12. *Complete* the line. `[CPJ-12]` | Tab through every field in the line before you start the next one, so that fields such as the voucher fill in correctly. |
| *STEP COMPLETE* (light blue) | • *The parent line is complete.*<br>• *Continue to [Enter the Child Lines](#12-enter-the-child-lines)* |

#### 1.2 Enter the Child Lines

##### Procedure

Complete these steps for each child account:

| Action | Description |
|---|---|
| *PROCESS START* (light blue) | *Pre-requisites:*<br>• The parent line is complete (see [Create the Journal and Enter the Parent Line](#11-create-the-journal-and-enter-the-parent-line)).<br>*Responsibility:*<br>• To be confirmed `[GOV-01]` |
| 1. *Add* a new line. `[CPJ-01]` | **Validation placeholder (`CPJ-01`, `CPJ-05`):** how a new line is added, and whether the date must be entered again on this line. |
| 2. *Select* the child customer account. | Select a child account in the confirmed allocation. The customer name fills in automatically. |
| 3. *Enter* the child's amount as a credit. `[CPJ-06, CPJ-07]` | Enter the amount allocated to this child account as a credit, in the same currency as the parent line. |
| 4. *Enter* the line description. `[CPJ-03, CPJ-04]` | Use a description that identifies the transfer in this child account's history. |
| 5. *Select* **Ledger** as the **Offset account type**. `[CPJ-08, PC-03]` | Apply the same offset treatment as the parent line.<br>**Validation placeholder (`PC-03`):** whether each child line takes the offset in the demonstrated UI. |
| 6. *Select* the bank-to-bank transfer clearing account. `[TF-03, PC-03]` | Select the same clearing account as the parent line. |
| 7. *Complete* the line. `[CPJ-12]` | Tab through every field in the line. |
| 8. *Repeat* for each child account. | Repeat steps 1 to 7 until every child account in the confirmed allocation has a credit line. |
| *STEP COMPLETE* (light blue) | • *Every child account in the allocation has a credit line.*<br>• *Continue to [Validate and Post the Journal](#13-validate-and-post-the-journal)* |

#### 1.3 Validate and Post the Journal

##### Procedure

Complete these steps to validate and post the journal:

| Action | Description |
|---|---|
| *PROCESS START* (light blue) | *Pre-requisites:*<br>• The parent line and every child line are complete (see [Enter the Child Lines](#12-enter-the-child-lines)).<br>*Responsibility:*<br>• To be confirmed `[GOV-01]` |
| 1. *Check* the distributed total. `[CPJ-13]` | Confirm that the child credits add up to the parent debit, and that the currency and date are correct.<br>**Validation placeholder (`CPJ-13`):** where the totals are shown. |
| 2. *Run* **Simulate Posting**. `[CPJ-14]` | Check the journal before posting. The notes describe a blue result as ready to post.<br>**Validation placeholder (`CPJ-14`):** the control's label and location. |
| 3. *Correct* any errors. `[CPJ-15]` | If Simulate Posting shows an error, read it, correct the line it names, and run Simulate Posting again. If you cannot resolve the error, ask for help before you post.<br>**Validation placeholder (`CPJ-15`):** the support route. |
| 4. *Post* the journal. `[CPJ-16, CPJ-17]` | Post only when every line is complete, the totals match and Simulate Posting succeeds.<br>**Validation placeholder (`CPJ-16`, `CPJ-17`):** the Post control, who may post, and whether approval is needed. |
| 5. *Record* the purpose of any residual. `[PC-04]` | Optional. In a partial allocation, add a note that explains why the remaining amount stays on the parent account. Otherwise, go to step 6.<br>**Validation placeholder (`PC-04`):** where, how and at what point the note is added. |
| 6. *Verify* the distribution. `[CPJ-18]` | **Validation placeholder (`CPJ-18`):** how to confirm the result on the parent and child accounts after posting. |
| *PROCESS COMPLETE* (light green) | *Outcomes:*<br>• A balanced CPJL is posted: a debit on the parent account and matching credits on the child accounts, with the bank-to-bank transfer clearing account as the offset.<br>• Any residual stays on the parent account with a note that explains its purpose.<br>• If the posted journal is wrong, the correction process is not yet confirmed. `[CPJ-19]` |

---

## Part 3: Reports (AR Collections Transfer a Parent Account Payment Across Child Accounts)

##### Overview

Reports for this process are pending SME confirmation. `[GOV-04]`

---

## Related content

| Item | Relationship |
|---|---|
| [Customer Payment Journal controls reference](../06-reference-guides/REF-AR-Customer-Payment-Journal-Controls-DRAFT.md) | The shared CPJL controls this guide applies. |
| [Transfer Funds Between Customer Accounts](PG-AR-Transfer-Funds-Between-Customer-Accounts-DRAFT.md) | The same journal pattern with one source line and one destination line. |
| Identify parent-child accounts (backlog rank 26) | Knowledge article, not ready. Needed for `PC-01`. |
| [AR Collections Customer Account](PG-AR-Customer-Account-DRAFT.md) | Reviewing customer transactions. A possible way to check the result after posting; not confirmed (`CPJ-18`). |
| [AR Collections Collection Activities](PG-AR-Collection-Activities-DRAFT.md) and [Notes and Activities](PG-AR-Notes-and-Activities-DRAFT.md) | Customer notes. Whether the residual note is a customer note is not confirmed (`PC-04`). |

## Step evidence

| Step | Source | Status |
|---|---|---|
| 1.1.1 | Template standard navigation pattern (D-015) | Pattern |
| 1.1.2 | Favorites guide (recording frame 00:33:51); Part 2 notes | Location from Part 1; path is a placeholder |
| 1.1.3, 1.1.5, 1.2.1 | Implied by the Part 2 notes (header and lines) | Placeholders |
| 1.1.6 | Shared CPJL control; not in the pack's parent draft | Placeholder |
| 1.1.4, 1.1.7 to 1.1.12 | Part 2 notes; pack draft steps 2, 3, 5 to 7 and 9 | Stated in notes; recording check pending |
| 1.2.2 to 1.2.8 | Part 2 notes; pack draft steps 4 to 7 | Stated in notes; offset on child lines open (`PC-03`) |
| 1.3.1 to 1.3.4 | Part 2 notes; pack draft steps 8, 10 and 11 | Stated in notes; controls and posting rules open |
| 1.3.5 | Part 2 notes; pack draft step 9 | Stated in notes; where the note goes is open (`PC-04`) |
| 1.3.6 | Listed as a gap in the pack draft | Placeholder |

The pack draft's step 1, *Confirm the approved allocation*, is a business check rather than a D365 step. It is a prerequisite and a Key concepts rule here.

## Draft validation notes

All items are in the [validation register](../03-validation/Part2-CPJL-and-Transfers-Validation.md).

- **Source:** recording check `SRC-01`; timestamps `SRC-02`.
- **Business checks:** relationship method `PC-01`; allocation evidence `PC-02`.
- **Labels and navigation:** `CPJ-01` to `CPJ-03`, `CPJ-08`, `CPJ-14`, `CPJ-16`.
- **Accounts:** clearing account `TF-03`; offset on each line `PC-03`; account numbers in guides `CPJ-09`.
- **Partial allocation:** where the residual note goes `PC-04`; who follows it up `PC-05`.
- **Business rules:** dates `CPJ-05`, debit and credit entry `CPJ-06`, currency `CPJ-07`, blank fields and dimensions `CPJ-10` and `CPJ-11`, description standard `CPJ-04`.
- **Controls:** totals `CPJ-13`, errors and support `CPJ-15`, posting permission `CPJ-16`, approval `CPJ-17`, verification `CPJ-18`, reversal `CPJ-19`, security role `CPJ-21`.
- **Governance:** initiation `PC-06`, role `GOV-01`, BPO `GOV-02`, code and title `GOV-03`, reports `GOV-04`, review and approval `GOV-05`.
