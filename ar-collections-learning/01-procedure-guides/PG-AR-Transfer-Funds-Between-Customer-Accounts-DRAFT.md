# D365 F&O: AR Collections Customer Account Transfers Procedure Guide

> **SME REVIEW DRAFT. Not validated or approved.**
>
> This is a Markdown preview of the Word guide [`TBC-AR Collections Customer Account Transfers PG v0.1.docx`](TBC-AR%20Collections%20Customer%20Account%20Transfers%20PG%20v0.1.docx). That guide was built from the PG master template in [`/templates`](../../templates/). **The Word file is the editable source.**
>
> **Built from AI-generated notes.** The content comes from Teams AI-generated notes of the *AR Training D365* Part 2 session and has not yet been checked against the recording (`SRC-01`). This is a higher-risk guide: do not use it on real customer accounts, and do not finalise it, until its blocking items close.
>
> `[XX-nn]` markers show unconfirmed items. In the Word file, each one is a review comment. Full details are in the [validation register](../03-validation/Part2-CPJL-and-Transfers-Validation.md). The markers are not part of the guide text.

The fixed template content is not repeated here: cover, Contents, *About this guide* and *Additional Resources*.

**Version history**

| ID | Date | Author/s | BPO | Description of change |
|---|---|---|---|---|
| 0.1 | October 2026 | Daniel Moreira | To be confirmed `[GOV-02]` | SME review draft created from the PG master template. Built from the Part 2 notes; not yet checked against the recording, validated or approved. `[SRC-01]` |

Guide code and final title: `[GOV-03]`.

---

## Part 1: What do I need to know? (AR Collections Customer Account Transfers)

### High-level process

##### Part Description

This guide explains how to move funds from one customer account to another with a **Customer payment journal** (CPJL). The transfer has two lines: a debit on the source customer and a matching credit on the destination customer, each with the bank-to-bank transfer clearing account as the offset. Distributing a parent-account payment across child accounts is covered by the AR Collections Parent Payment Distribution guide. Putting an amount back on a customer account is covered by the AR Collections Overpayment and Write-Off Restoration guide.

Approval, correcting or reversing a posted journal, payments already settled on the wrong account, and transfers between legal entities are outside the scope of this guide until confirmed. `[CPJ-17, CPJ-19, TF-05, TF-06]`

##### Initiation

- A payment was posted to the wrong customer account. `[TF-01]`
- Funds need to move between related customer accounts, and the correct destination has been confirmed.

##### Stream

| Stream | Process Area | Key Roles |
|---|---|---|
| Accounts Receivable `[GOV-01]` | AR Collections | • To be confirmed |

##### Process

| # | Action | Who | When | Where |
|---|---|---|---|---|
| 1 | [Transfer Funds Between Customer Accounts](#1-transfer-funds-between-customer-accounts) | To be confirmed | When a payment is on the wrong customer account, or funds must move to a confirmed related account | D365 |

### Roles and responsibilities

##### Overview

The business role that prepares and posts this journal is not yet confirmed. `[CPJ-16, CPJ-17]`

| Tasks / Business Roles | To be confirmed |
|---|---|
| [Transfer Funds Between Customer Accounts](#1-transfer-funds-between-customer-accounts) | R |

### Key concepts

##### Overview

Before you start, you need to know which journal and offset account a transfer uses, and the checks to make before you post.

##### Customer payment journal

| Term | Description |
|---|---|
| **Customer payment journal (CPJL)** | The journal used to transfer funds between customer accounts. `[CPJ-02]` |
| **Bank-to-bank transfer clearing account** | The ledger account used as the offset for a transfer between customer accounts. Do not post a transfer directly to a bank account. `[TF-03, CPJ-09]` |
| **Simulate Posting** | A check run on the journal before posting. A blue result means the journal is ready to post. A red result shows errors to correct. `[CPJ-14]` |

##### Before you post `[CPJ-10, CPJ-11]`

| Rule | Description |
|---|---|
| **Confirm the destination first** | Confirm the correct destination account before you start. `[TF-02]` |
| **Use the original currency** | Use the same currency as the original customer payment. `[CPJ-07]` |
| **Describe the transfer** | Use clear descriptions on the journal and on both lines, so the transfer can be identified in each customer's history. `[CPJ-04]` |
| **Balance the lines** | The source debit and the destination credit must be the same amount. |
| **Simulate before posting** | Run Simulate Posting and resolve every error before you post. |

---

## Part 2: How do I do it? (AR Collections Customer Account Transfers)

### 1. Transfer Funds Between Customer Accounts

##### Description

Use this topic to move funds from one customer account to another. You create a CPJL journal, enter a debit line for the source customer and a credit line for the destination customer, check that the journal balances, run Simulate Posting and post.

##### Responsibility

- To be confirmed: prepares and posts the transfer journal. `[GOV-01]`

##### Initiation

- A payment was posted to the wrong customer account, or funds must move to a confirmed related account.

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
| *PROCESS START* (light blue) | *Pre-requisites:*<br>• Access to D365 and to **Customer payment journal**. `[CPJ-21]`<br>• The source and destination customer accounts, the amount and the currency of the original payment.<br>• Confirmation that the destination account is correct.<br>• Whether the payment is already settled on the source account. `[TF-05]`<br>*Responsibility:*<br>• To be confirmed |
| 1. *Check* the **Entity**. | Confirm you are signed into the correct **Legal Entity** (top-right). |
| 2. *Click* **Modules**. | From the left-hand **Navigation Pane**, click **Modules**. |
| 3. *Navigate* to the **Customer payment journal** page. `[CPJ-01]` | From the **Navigation Pane**, *select*:<br>• **Credit and collections >**<br>• **Customer payment journal**<br>You can also open **Customer payment journal** from your **Favorites** (see the AR Collections Favorites guide). |
| 4. *Create* a new journal. `[CPJ-01, CPJ-02]` | Start a new CPJL journal. |
| 5. *Enter* the journal description. `[CPJ-03]` | Describe the transfer clearly and include the customer codes, for example "Transfer funds from customer A to customer B". |
| 6. *Open* the journal lines. `[CPJ-01]` | Open the lines of the new journal. |
| 7. *Enter* the transaction date. `[CPJ-05]` | The current date is the default. A wrong-account correction may use the original customer payment date when appropriate. |
| 8. *Select* the source customer account. | Select the customer account the funds are being removed from. The customer name fills in automatically. |
| 9. *Enter* the amount as a debit. `[CPJ-06]` | Enter the amount being removed from the source customer as a debit, in the currency of the original payment. |
| 10. *Enter* the line description. `[CPJ-03]` | Use the same clear transfer description, so the transaction can be identified in the customer's history. |
| 11. *Select* **Ledger** as the **Offset account type**. `[CPJ-08]` | Set the offset account type to **Ledger**. |
| 12. *Select* the bank-to-bank transfer clearing account. `[TF-03]` | Select the clearing account used for transfers between customer accounts as the offset account. Do not use a bank account. |
| 13. *Complete* the line. `[CPJ-12]` | Tab through every field in the line before you start the next one, so that fields such as the voucher fill in correctly. |
| *STEP COMPLETE* (light blue) | • *The source line is complete.*<br>• *Continue to [Enter the Destination Line](#12-enter-the-destination-line)* |

#### 1.2 Enter the Destination Line

##### Procedure

Complete these steps to enter the destination line:

| Action | Description |
|---|---|
| *PROCESS START* (light blue) | *Pre-requisites:*<br>• The source line is complete (see [Create the Journal and Enter the Source Line](#11-create-the-journal-and-enter-the-source-line)).<br>*Responsibility:*<br>• To be confirmed |
| 1. *Add* a new line. `[CPJ-01, CPJ-05]` | Add another line to the journal. |
| 2. *Select* the destination customer account. | Select the customer account receiving the funds. The customer name fills in automatically. |
| 3. *Enter* the amount as a credit. `[CPJ-06]` | Enter the same amount as the source line as a credit, in the same currency. |
| 4. *Enter* the line description. | Use the same description as the source line, so the transfer can be identified in both customers' histories. |
| 5. *Select* **Ledger** as the **Offset account type**. `[TF-04]` | Apply the same offset treatment as the source line. |
| 6. *Select* the bank-to-bank transfer clearing account. | Select the same clearing account as the source line. |
| 7. *Complete* the line. | Tab through every field in the line. |
| *STEP COMPLETE* (light blue) | • *The journal has a source debit line and a matching destination credit line.*<br>• *Continue to [Validate and Post the Journal](#13-validate-and-post-the-journal)* |

#### 1.3 Validate and Post the Journal

##### Procedure

Complete these steps to validate and post the journal:

| Action | Description |
|---|---|
| *PROCESS START* (light blue) | *Pre-requisites:*<br>• Both lines are complete (see [Enter the Destination Line](#12-enter-the-destination-line)).<br>*Responsibility:*<br>• To be confirmed |
| 1. *Check* the journal balances. `[CPJ-13]` | Confirm that total debits equal total credits, and that the currency and date are correct. |
| 2. *Run* **Simulate Posting**. `[CPJ-14]` | Check the journal before posting. A blue result means the journal is ready to post. |
| 3. *Correct* any errors. `[CPJ-15]` | If Simulate Posting shows an error, read it, correct the line it names and run Simulate Posting again. If you cannot resolve the error, log a request through the D365 issue form (see **Additional Resources**) before you post. |
| 4. *Post* the journal. `[CPJ-16, CPJ-17]` | Post only when every line is complete, the journal balances and Simulate Posting succeeds. |
| 5. *Verify* the transfer. `[CPJ-18]` | Check that the transfer appears with its description on both customer accounts. |
| *PROCESS COMPLETE* (light green) | *Outcomes:*<br>• A balanced CPJL is posted: a debit on the source customer and a matching credit on the destination customer, with the bank-to-bank transfer clearing account as the offset. `[CPJ-19]`<br>• The transfer can be identified by its description in both customers' histories. |

---

## Part 3: Reports (AR Collections Customer Account Transfers)

##### Overview

Reports for this process are pending SME confirmation. `[GOV-04]`

---

## Additional Resources

The standard template block, unchanged.

---

## Step evidence

*Working note for reviewers; not part of the Word guide.* It shows where each step comes from, so you can see what the notes state and what is still open.

| Step | Source | Status |
|---|---|---|
| 1.1.1, 1.1.2 | Template standard navigation pattern (D-015) | Pattern |
| 1.1.3 | Favorites guide (recording frame 00:33:51) | Module from Part 1; menu group open (`CPJ-01`) |
| 1.1.4, 1.1.6, 1.2.1 | Implied by the Part 2 notes (journal header and lines) | Action named without a label (D-020) |
| 1.1.5, 1.1.7 to 1.1.13 | Part 2 notes; pack draft steps 2 to 9 | Stated in notes; recording check pending |
| 1.2.2 to 1.2.7 | Part 2 notes; pack draft steps 10 to 12 | Stated in notes; offset on this line open (`TF-04`) |
| 1.3.1 to 1.3.4 | Part 2 notes; pack draft steps 13 to 15; template support route (D-018) | Stated in notes; controls and posting rules open |
| 1.3.5 | Listed as a gap in the pack draft | Action named; method open (`CPJ-18`) |

