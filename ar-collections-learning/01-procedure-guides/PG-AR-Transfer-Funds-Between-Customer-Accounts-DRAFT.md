# D365 F&O: AR Collections Transfer Funds Between Customer Accounts Procedure Guide

> **WORKING DRAFT. Not validated, not approved, not for publication.**
>
> This is a working Markdown draft built from the *AR Training D365* Part 2 update pack. It follows the section order of the PG master template, but it has not been built in Word yet (decision D-037). The Word build follows once the Part 2 recording has been checked.
>
> **Higher-risk guide.** It moves funds between customer accounts. Do not use it on real customer accounts, and do not finalise it, until its blocking items close (source 3.1; README development gates).
>
> **Evidence.** The steps come from Teams AI-generated notes of the Part 2 session and the pack's working draft (sources 4.0 and 4.4). Neither has been checked against the recording (`SRC-01`). `[XX-nn]` markers point to items in the [validation register](../03-validation/Part2-CPJL-and-Transfers-Validation.md). Where the notes do not give a detail precisely enough, the step carries a **validation placeholder** instead of a guess. The [step evidence](#step-evidence) table shows the source of each step.

## Document control

| Field | Value |
|---|---|
| Guide code and final title | To be confirmed `[GOV-03]` |
| Version | 0.1 working draft, October 2026. Author: Daniel Moreira. |
| Business process owner | To be confirmed `[GOV-02]` |
| Status and gate | Working draft. Gate: Drafted (working Markdown). Next: check against the Part 2 recording, then build in the master template. |
| Roadmap | Part 2 roadmap item 15, Release 3A (proposed D-036). Source 2 backlog rank 27. |
| Shared controls | [Customer Payment Journal controls reference](../06-reference-guides/REF-AR-Customer-Payment-Journal-Controls-DRAFT.md) |
| Screenshot register | [PG-AR-Transfer-Funds-Between-Customer-Accounts-Screenshots.md](../02-screenshot-registers/PG-AR-Transfer-Funds-Between-Customer-Accounts-Screenshots.md) |

**Version history**

| ID | Date | Author/s | BPO | Description of change |
|---|---|---|---|---|
| 0.1 | October 2026 | Daniel Moreira | To be confirmed `[GOV-02]` | Working draft created from the AR Training D365 Part 2 update pack. Not validated or approved. |

---

## Part 1: What do I need to know? (AR Collections Transfer Funds Between Customer Accounts)

### High-level process

##### Part Description

This guide explains how to move funds from one customer account to another with a **Customer payment journal** (CPJL). The transfer has two lines: a debit on the source customer and a matching credit on the destination customer, each using the bank-to-bank transfer clearing account as the offset.

Moving a payment from a parent account across several child accounts is covered in the *Transfer a Parent Account Payment Across Child Accounts* guide. Putting an amount back on a customer account is covered in the *Restore a Written-Off or Overpayment Amount* guide.

Out of scope until confirmed: approval workflow (`CPJ-17`), correcting or reversing a posted journal (`CPJ-19`), payments already settled on the wrong account (`TF-05`) and transfers between legal entities (`TF-06`).

##### Initiation

- A payment was posted to the wrong customer account. `[TF-01]`
- Funds need to move between related customer accounts, and the correct destination has been confirmed. `[TF-01]`

##### Stream

| Stream | Process Area | Key Roles |
|---|---|---|
| Accounts Receivable `[GOV-01]` | AR Collections `[GOV-01]` | • To be confirmed `[GOV-01]` |

##### Process

| # | Action | Who | When | Where |
|---|---|---|---|---|
| 1 | [Transfer Funds Between Customer Accounts](#1-transfer-funds-between-customer-accounts) | To be confirmed `[GOV-01]` | When a payment is on the wrong customer account, or funds must move to a confirmed related account | D365 |

### Roles and responsibilities

##### Overview

The sources do not say which business role prepares this journal, which role may post it (`CPJ-16`) or whether it needs approval (`CPJ-17`).

| Tasks / Business Roles | To be confirmed `[GOV-01]` |
|---|---|
| [Transfer Funds Between Customer Accounts](#1-transfer-funds-between-customer-accounts) | R |

### Key concepts

##### Overview

Before you start, you need to know which journal and offset account a transfer uses, and the checks to make before you post.

##### Customer payment journal

| Term | Description |
|---|---|
| **Customer payment journal (CPJL)** | The journal used to transfer funds between customer accounts. `[CPJ-02]` |
| **Bank-to-bank transfer clearing account** | The ledger account used as the offset for a transfer between customer accounts. Do not post a transfer directly to a bank account. `[TF-03]` |
| **Simulate Posting** | Checks the journal before it is posted. The notes describe a blue result as ready to post and a red result as errors to correct. `[CPJ-14]` |

##### Before you post

| Rule | Description |
|---|---|
| **Confirm the destination first** | Confirm the correct destination account before you start. `[TF-02]` |
| **Use the original currency** | Use the same currency as the original customer payment. `[CPJ-07]` |
| **Describe the transfer** | Use clear descriptions on the journal and on both lines, so the transfer can be identified in each customer's history. `[CPJ-03, CPJ-04]` |
| **Balance the lines** | The source debit and the destination credit must be the same amount. `[CPJ-13]` |
| **Simulate before posting** | Run Simulate Posting and resolve every error before you post. `[CPJ-14]` |
| **Blank fields and dimensions** | For restoration entries, the notes say to leave financial tags, invoice number and bank account blank, and not to change pre-populated dimensions. Whether this also applies to transfers is not confirmed. `[CPJ-10, CPJ-11]` |

---

## Part 2: How do I do it? (AR Collections Transfer Funds Between Customer Accounts)

### 1. Transfer Funds Between Customer Accounts

##### Description

Use this topic to move funds from one customer account to another. You create a CPJL journal, enter a debit line for the source customer and a credit line for the destination customer, check that the journal balances, run Simulate Posting and post.

##### Responsibility

- To be confirmed: prepares and posts the transfer journal. `[GOV-01, CPJ-16]`

##### Initiation

- A payment was posted to the wrong customer account, or funds must move to a confirmed related account. `[TF-01]`

##### Topic Overview

This topic includes these steps:

| Step | Description |
|---|---|
| [Create the Journal and Enter the Source Line](#11-create-the-journal-and-enter-the-source-line) | Create the CPJL and enter the debit line for the customer the funds come from. Output: the source line is complete. |
| [Enter the Destination Line](#12-enter-the-destination-line) | Enter the matching credit line for the customer receiving the funds. Output: a two-line journal. |
| [Validate and Post the Journal](#13-validate-and-post-the-journal) | Check the balance, run Simulate Posting, correct errors and post. Output: the transfer is posted. |

#### 1.1 Create the Journal and Enter the Source Line

##### Procedure

Complete these steps to create the journal and enter the source line:

| Action | Description |
|---|---|
| *PROCESS START* (light blue) | *Pre-requisites:*<br>• Access to D365 and to **Customer payment journal**. `[CPJ-21]`<br>• The source and destination customer accounts, the amount and the currency of the original payment.<br>• Confirmation that the destination account is correct. `[TF-02]`<br>• Whether the payment is already settled on the source account. `[TF-05]`<br>*Responsibility:*<br>• To be confirmed `[GOV-01]` |
| 1. *Check* the **Entity**. | Confirm you are signed into the correct **Legal Entity** (top-right). |
| 2. *Open* **Customer payment journal**. `[CPJ-01]` | The Favorites guide places **Customer payment journal** in the **Credit and collections** module. If you have added it to your favorites, open it from there.<br>**Validation placeholder (`CPJ-01`):** exact navigation path. |
| 3. *Create* a new journal. `[CPJ-01, CPJ-02]` | Start a new CPJL journal.<br>**Validation placeholder (`CPJ-01`, `CPJ-02`):** the control that creates the journal, and how the CPJL journal name is selected. |
| 4. *Enter* the journal description. `[CPJ-03, CPJ-04]` | Describe the transfer clearly and include the customer codes, for example "Transfer funds from customer A to customer B". |
| 5. *Open* the journal lines. `[CPJ-01]` | **Validation placeholder (`CPJ-01`):** how the journal lines are opened from the journal. |
| 6. *Enter* the transaction date. `[CPJ-05]` | The notes say the current date is the default. A wrong-account correction may use the original customer payment date when appropriate.<br>**Validation placeholder (`CPJ-05`):** the date field label, whether the date is set on the journal or on each line, and the backdating rule. |
| 7. *Select* the source customer account. | Select the customer account the funds are being removed from. The customer name fills in automatically. |
| 8. *Enter* the amount as a debit. `[CPJ-06, CPJ-07]` | Enter the amount being removed from the source customer as a debit, in the currency of the original payment.<br>**Validation placeholder (`CPJ-06`):** how debits are entered. |
| 9. *Enter* the line description. `[CPJ-03, CPJ-04]` | Use the same clear transfer description, so the transaction can be identified in the customer's history. |
| 10. *Select* **Ledger** as the **Offset account type**. `[CPJ-08]` | Set the offset account type to **Ledger**. |
| 11. *Select* the bank-to-bank transfer clearing account. `[TF-03, CPJ-08]` | Select the clearing account used for transfers between customer accounts as the offset account. Do not use a bank account.<br>**Validation placeholder (`TF-03`):** the account label and value. |
| 12. *Complete* the line. `[CPJ-12]` | Tab through every field in the line before you start the next one, so that fields such as the voucher fill in correctly. |
| *STEP COMPLETE* (light blue) | • *The source line is complete.*<br>• *Continue to [Enter the Destination Line](#12-enter-the-destination-line)* |

#### 1.2 Enter the Destination Line

##### Procedure

Complete these steps to enter the destination line:

| Action | Description |
|---|---|
| *PROCESS START* (light blue) | *Pre-requisites:*<br>• The source line is complete (see [Create the Journal and Enter the Source Line](#11-create-the-journal-and-enter-the-source-line)).<br>*Responsibility:*<br>• To be confirmed `[GOV-01]` |
| 1. *Add* a new line. `[CPJ-01]` | **Validation placeholder (`CPJ-01`, `CPJ-05`):** how a new line is added, and whether the date must be entered again on this line. |
| 2. *Select* the destination customer account. | Select the customer account receiving the funds. The customer name fills in automatically. |
| 3. *Enter* the amount as a credit. `[CPJ-06, CPJ-07]` | Enter the same amount as the source line as a credit, in the same currency. |
| 4. *Enter* the line description. `[CPJ-03, CPJ-04]` | Use the same description as the source line, so the transfer can be identified in both customers' histories. |
| 5. *Select* **Ledger** as the **Offset account type**. `[CPJ-08, TF-04]` | Apply the same offset treatment as the source line.<br>**Validation placeholder (`TF-04`):** whether the destination line also takes the offset in the demonstrated UI. |
| 6. *Select* the bank-to-bank transfer clearing account. `[TF-03, TF-04]` | Select the same clearing account as the source line. |
| 7. *Complete* the line. `[CPJ-12]` | Tab through every field in the line. |
| *STEP COMPLETE* (light blue) | • *The journal has a source debit line and a matching destination credit line.*<br>• *Continue to [Validate and Post the Journal](#13-validate-and-post-the-journal)* |

#### 1.3 Validate and Post the Journal

##### Procedure

Complete these steps to validate and post the journal:

| Action | Description |
|---|---|
| *PROCESS START* (light blue) | *Pre-requisites:*<br>• Both lines are complete (see [Enter the Destination Line](#12-enter-the-destination-line)).<br>*Responsibility:*<br>• To be confirmed `[GOV-01]` |
| 1. *Check* the journal balances. `[CPJ-13]` | Confirm that total debits equal total credits, and that the currency and date are correct.<br>**Validation placeholder (`CPJ-13`):** where the totals are shown. |
| 2. *Run* **Simulate Posting**. `[CPJ-14]` | Check the journal before posting. The notes describe a blue result as ready to post.<br>**Validation placeholder (`CPJ-14`):** the control's label and location. |
| 3. *Correct* any errors. `[CPJ-15]` | If Simulate Posting shows an error, read it, correct the line it names, and run Simulate Posting again. If you cannot resolve the error, ask for help before you post.<br>**Validation placeholder (`CPJ-15`):** the support route. |
| 4. *Post* the journal. `[CPJ-16, CPJ-17]` | Post only when every line is complete, the journal balances and Simulate Posting succeeds.<br>**Validation placeholder (`CPJ-16`, `CPJ-17`):** the Post control, who may post, and whether approval is needed. |
| 5. *Verify* the transfer. `[CPJ-18]` | **Validation placeholder (`CPJ-18`):** how to confirm the transfer on both customer accounts after posting. |
| *PROCESS COMPLETE* (light green) | *Outcomes:*<br>• A balanced CPJL is posted: a debit on the source customer and a matching credit on the destination customer, with the bank-to-bank transfer clearing account as the offset.<br>• The transfer can be identified by its description in both customers' histories.<br>• If the posted journal is wrong, the correction process is not yet confirmed. `[CPJ-19]` |

---

## Part 3: Reports (AR Collections Transfer Funds Between Customer Accounts)

##### Overview

Reports for this process are pending SME confirmation. `[GOV-04]`

---

## Related content

| Item | Relationship |
|---|---|
| [Customer Payment Journal controls reference](../06-reference-guides/REF-AR-Customer-Payment-Journal-Controls-DRAFT.md) | The shared CPJL controls this guide applies. |
| [Transfer a Parent Account Payment Across Child Accounts](PG-AR-Transfer-Parent-Payment-Across-Child-Accounts-DRAFT.md) | The same journal pattern with one parent line and several child lines. |
| [Restore a Written-Off or Overpayment Amount](PG-AR-Restore-Written-Off-Overpayment-DRAFT.md) | The other CPJL guide from Part 2. |
| [AR Collections Customer Account](PG-AR-Customer-Account-DRAFT.md) | Reviewing customer transactions. A possible way to check the result after posting; not confirmed (`CPJ-18`). |
| [AR Collections Favorites](PG-AR-Configure-Collections-Favourites-DRAFT.md) | Adds **Customer payment journal** to your favorites. |
| [AR Collections Workspace](PG-AR-Workspace-DRAFT.md) | **Payment journals not posted** lists journals that have not been posted. |
| Investigate unallocated payments (backlog rank 14) | Not drafted. Source 4.1 places "investigate receipts, obtain remittance, identify related accounts" in the same learning pathway. |

## Step evidence

| Step | Source | Status |
|---|---|---|
| 1.1.1 | Template standard navigation pattern (D-015) | Pattern |
| 1.1.2 | Favorites guide (recording frame 00:33:51); Part 2 notes | Location from Part 1; path is a placeholder |
| 1.1.3, 1.1.5, 1.2.1 | Implied by the Part 2 notes (header and lines) | Placeholders |
| 1.1.4, 1.1.6 to 1.1.12 | Part 2 notes; pack draft steps 2 to 9 | Stated in notes; recording check pending |
| 1.2.2 to 1.2.7 | Part 2 notes; pack draft steps 10 to 12 | Stated in notes; offset on this line open (`TF-04`) |
| 1.3.1 to 1.3.4 | Part 2 notes; pack draft steps 13 to 15 | Stated in notes; controls and posting rules open |
| 1.3.5 | Listed as a gap in the pack draft | Placeholder |

## Draft validation notes

All items are in the [validation register](../03-validation/Part2-CPJL-and-Transfers-Validation.md).

- **Source:** recording check `SRC-01`; timestamps `SRC-02`.
- **Labels and navigation:** `CPJ-01` to `CPJ-03`, `CPJ-08`, `CPJ-14`, `CPJ-16`.
- **Accounts:** clearing account `TF-03`; offset on the destination line `TF-04`; account numbers in guides `CPJ-09`.
- **Business rules:** dates `CPJ-05`, debit and credit entry `CPJ-06`, currency `CPJ-07`, blank fields and dimensions `CPJ-10` and `CPJ-11`, description standard `CPJ-04`.
- **Business checks:** confirming the destination `TF-02`; settled payments `TF-05`; legal entity scope `TF-06`.
- **Controls:** balance check `CPJ-13`, errors and support `CPJ-15`, posting permission `CPJ-16`, approval `CPJ-17`, verification `CPJ-18`, reversal `CPJ-19`, security role `CPJ-21`.
- **Governance:** initiation `TF-01`, role `GOV-01`, BPO `GOV-02`, code and title `GOV-03`, reports `GOV-04`, review and approval `GOV-05`.
