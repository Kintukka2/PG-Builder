# D365 F&O: AR Collections Parent Payment Distribution Procedure Guide

> **SME REVIEW DRAFT. Not validated or approved.**
>
> This is a Markdown preview of the Word guide [`TBC-AR Collections Parent Payment Distribution PG v0.1.docx`](TBC-AR%20Collections%20Parent%20Payment%20Distribution%20PG%20v0.1.docx). That guide was built from the PG master template in [`/templates`](../../templates/). **The Word file is the editable source.**
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

## Part 1: What do I need to know? (AR Collections Parent Payment Distribution)

### High-level process

##### Part Description

This guide explains how to distribute a payment held on a parent customer account to one or more child customer accounts with a **Customer payment journal** (CPJL). One debit line moves the amount off the parent account, and one credit line for each child account receives its share. It also covers a partial allocation, where only the confirmed part of the payment is moved and the rest stays on the parent account. A transfer between two customer accounts is covered by the AR Collections Customer Account Transfers guide.

How to identify a parent-child relationship in D365, approval, and correcting or reversing a posted journal are outside the scope of this guide until confirmed. `[PC-01, CPJ-17, CPJ-19]`

##### Initiation

- A payment held on a parent customer account must be distributed to one or more confirmed child accounts. `[PC-06]`

##### Stream

| Stream | Process Area | Key Roles |
|---|---|---|
| Accounts Receivable `[GOV-01]` | AR Collections | • To be confirmed |

##### Process

| # | Action | Who | When | Where |
|---|---|---|---|---|
| 1 | [Transfer a Parent Account Payment Across Child Accounts](#1-transfer-a-parent-account-payment-across-child-accounts) | To be confirmed | When a payment on a parent account must be distributed to confirmed child accounts | D365 |

### Roles and responsibilities

##### Overview

The business role that prepares and posts this journal is not yet confirmed. `[CPJ-16, CPJ-17]`

| Tasks / Business Roles | To be confirmed |
|---|---|
| [Transfer a Parent Account Payment Across Child Accounts](#1-transfer-a-parent-account-payment-across-child-accounts) | R |

### Key concepts

##### Overview

Before you start, you need to know how the relationship and the allocation are confirmed, how the journal distributes the payment, and what happens to any amount that is not allocated.

##### Parent and child accounts

| Term | Description |
|---|---|
| **Parent-child relationship** | D365 does not provide a reliable parent-child indicator. Do not rely on account names alone. `[PC-01]` |
| **Confirmed allocation** | Which child accounts the payment belongs to, and how much each receives, confirmed from remittance, customer confirmation or other validated evidence. `[PC-02]` |
| **Distribution** | One debit on the parent account can be distributed across several child credits, if the child credits add up to the parent debit. |
| **Residual** | In a partial allocation, the part of the payment that is not yet allocated. It stays on the parent account, with a note that explains its purpose. For example, $8,000 of a $10,000 receipt is distributed and $2,000 stays on the parent account. The amounts are an example only, not a threshold. `[PC-04, PC-05]` |

##### Before you post `[CPJ-10, CPJ-11]`

| Rule | Description |
|---|---|
| **Confirm before processing** | Confirm the relationship and the allocation before you create the journal. |
| **Use the original currency** | Keep every line in the currency of the original receipt. `[CPJ-07]` |
| **Describe every line** | Use descriptions that let the transfer be identified in each customer's history. `[CPJ-04]` |
| **Use the clearing account** | Use **Ledger** as the offset type and the bank-to-bank transfer clearing account as the offset. `[TF-03, CPJ-09]` |
| **Balance the distribution** | The child credits must add up to the amount debited from the parent account. |
| **Simulate before posting** | Run Simulate Posting and resolve every error before you post. |

---

## Part 2: How do I do it? (AR Collections Parent Payment Distribution)

### 1. Transfer a Parent Account Payment Across Child Accounts

##### Description

Use this topic to distribute a payment from a parent customer account to confirmed child accounts. You create a CPJL journal, enter one debit line for the parent account and one credit line for each child account, check that the child credits match the parent debit, run Simulate Posting and post. If only part of the payment is allocated, you move only that part and record why the rest stays on the parent account.

##### Responsibility

- To be confirmed: prepares and posts the distribution journal. `[GOV-01]`

##### Initiation

- A payment held on a parent customer account must be distributed to one or more confirmed child accounts.

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
| *PROCESS START* (light blue) | *Pre-requisites:*<br>• Access to D365 and to **Customer payment journal**. `[CPJ-21]`<br>• A confirmed parent-child relationship.<br>• A confirmed allocation: each child account, its amount, and the total to move.<br>• The currency of the original receipt.<br>*Responsibility:*<br>• To be confirmed |
| 1. *Check* the **Entity**. | Confirm you are signed into the correct **Legal Entity** (top-right). |
| 2. *Click* **Modules**. | From the left-hand **Navigation Pane**, click **Modules**. |
| 3. *Navigate* to the **Customer payment journal** page. `[CPJ-01]` | From the **Navigation Pane**, *select*:<br>• **Credit and collections >**<br>• **Customer payment journal**<br>You can also open **Customer payment journal** from your **Favorites** (see the AR Collections Favorites guide). |
| 4. *Create* a new journal. `[CPJ-01, CPJ-02]` | Start a new CPJL journal. |
| 5. *Enter* the journal description. `[CPJ-03]` | Describe the transfer clearly, so it identifies the parent and child transfer. |
| 6. *Open* the journal lines. `[CPJ-01]` | Open the lines of the new journal. |
| 7. *Enter* the transaction date. `[CPJ-05]` | Enter the date for the distribution. |
| 8. *Select* the parent customer account. | Select the parent account that holds the payment. The customer name fills in automatically. |
| 9. *Enter* the amount to move as a debit. `[CPJ-06]` | Enter the total being moved off the parent account as a debit, in the currency of the original receipt. In a partial allocation, enter only the confirmed amount. The rest stays on the parent account. |
| 10. *Enter* the line description. `[CPJ-03]` | Use a description that identifies the transfer in the parent account's history. |
| 11. *Select* **Ledger** as the **Offset account type**. `[CPJ-08]` | Set the offset account type to **Ledger**. |
| 12. *Select* the bank-to-bank transfer clearing account. `[TF-03, PC-03]` | Select the clearing account as the offset account. |
| 13. *Complete* the line. `[CPJ-12]` | Tab through every field in the line before you start the next one, so that fields such as the voucher fill in correctly. |
| *STEP COMPLETE* (light blue) | • *The parent line is complete.*<br>• *Continue to [Enter the Child Lines](#12-enter-the-child-lines)* |

#### 1.2 Enter the Child Lines

##### Procedure

Complete these steps for each child account:

| Action | Description |
|---|---|
| *PROCESS START* (light blue) | *Pre-requisites:*<br>• The parent line is complete (see [Create the Journal and Enter the Parent Line](#11-create-the-journal-and-enter-the-parent-line)).<br>*Responsibility:*<br>• To be confirmed |
| 1. *Add* a new line. `[CPJ-01, CPJ-05]` | Add another line to the journal. |
| 2. *Select* the child customer account. | Select a child account in the confirmed allocation. The customer name fills in automatically. |
| 3. *Enter* the child's amount as a credit. `[CPJ-06]` | Enter the amount allocated to this child account as a credit, in the same currency as the parent line. |
| 4. *Enter* the line description. | Use a description that identifies the transfer in this child account's history. |
| 5. *Select* **Ledger** as the **Offset account type**. `[PC-03]` | Apply the same offset treatment as the parent line. |
| 6. *Select* the bank-to-bank transfer clearing account. | Select the same clearing account as the parent line. |
| 7. *Complete* the line. | Tab through every field in the line. |
| 8. *Repeat* for each child account. | Repeat steps 1 to 7 until every child account in the confirmed allocation has a credit line. |
| *STEP COMPLETE* (light blue) | • *Every child account in the allocation has a credit line.*<br>• *Continue to [Validate and Post the Journal](#13-validate-and-post-the-journal)* |

#### 1.3 Validate and Post the Journal

##### Procedure

Complete these steps to validate and post the journal:

| Action | Description |
|---|---|
| *PROCESS START* (light blue) | *Pre-requisites:*<br>• The parent line and every child line are complete (see [Enter the Child Lines](#12-enter-the-child-lines)).<br>*Responsibility:*<br>• To be confirmed |
| 1. *Check* the distributed total. `[CPJ-13]` | Confirm that the child credits add up to the parent debit, and that the currency and date are correct. |
| 2. *Run* **Simulate Posting**. `[CPJ-14]` | Check the journal before posting. A blue result means the journal is ready to post. |
| 3. *Correct* any errors. `[CPJ-15]` | If Simulate Posting shows an error, read it, correct the line it names and run Simulate Posting again. If you cannot resolve the error, log a request through the D365 issue form (see **Additional Resources**) before you post. |
| 4. *Post* the journal. `[CPJ-16, CPJ-17]` | Post only when every line is complete, the totals match and Simulate Posting succeeds. |
| 5. *Record* the purpose of any residual. `[PC-04]` | Optional. In a partial allocation, add a note that explains why the remaining amount stays on the parent account. Otherwise, go to step 6. |
| 6. *Verify* the distribution. `[CPJ-18]` | Check that the distribution appears with its description on the parent and child accounts. |
| *PROCESS COMPLETE* (light green) | *Outcomes:*<br>• A balanced CPJL is posted: a debit on the parent account and matching credits on the child accounts, with the bank-to-bank transfer clearing account as the offset. `[CPJ-19]`<br>• Any residual stays on the parent account with a note that explains its purpose. |

---

## Part 3: Reports (AR Collections Parent Payment Distribution)

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
| 1.1.7 | Shared CPJL control; not in the pack's parent draft | Action named; date rule open (`CPJ-05`) |
| 1.1.5, 1.1.8 to 1.1.13 | Part 2 notes; pack draft steps 2, 3, 5 to 7 and 9 | Stated in notes; recording check pending |
| 1.2.2 to 1.2.8 | Part 2 notes; pack draft steps 4 to 7 | Stated in notes; offset on child lines open (`PC-03`) |
| 1.3.1 to 1.3.4 | Part 2 notes; pack draft steps 8, 10 and 11; template support route (D-018) | Stated in notes; controls and posting rules open |
| 1.3.5 | Part 2 notes; pack draft step 9 | Stated in notes; where the note goes is open (`PC-04`) |
| 1.3.6 | Listed as a gap in the pack draft | Action named; method open (`CPJ-18`) |

The pack draft's step 1, *Confirm the approved allocation*, is a business check rather than a D365 step. It is a prerequisite and a Key concepts rule here.

