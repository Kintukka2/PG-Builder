# D365 F&O: Customer Payment Corrections Procedure Guide

> **Withdrawn (D-055).** This guide is merged into [220 Customer Payments v3.0](220-Customer%20Payments%20PG%20v3.0.docx) ([preview](PG-220-Customer-Payments-v3.0-DRAFT.md)): topic 1 is 220 topic 2.3, topic 2 is 3.1, topics 3 to 6 are 3.3 to 3.6, and Part 1 Key concepts are in 220 Part 1. Code 221 is not used. This file is kept as the record of v0.1; edit 220.

> **WORKING DRAFT. Not validated or approved.**
>
> This is a Markdown preview of the Word guide [`221-Customer Payment Corrections PG v0.1.docx`](221-Customer%20Payment%20Corrections%20PG%20v0.1.docx). It was assembled from the topic drafts named in its version history, under D-045 and D-046. **The Word file is the editable source.**
>
> Markers such as `[G221-01]` or `[CPJ-14]` show unconfirmed items. In the Word file, each one is a review comment. Guide-level items and the index of carried items are in the [validation register](../03-validation/221-Customer-Payment-Corrections-Validation.md). The markers are not part of the guide text.

The fixed template content is not repeated here: cover, Contents, *About this guide* and *Additional Resources*.

**Version history**

| ID | Date | Author/s | BPO | Description of change |
|---|---|---|---|---|
| 0.1 | November 2026 | Daniel Moreira | To be confirmed `[G221-02]` | Working draft assembled from the Customer Account Transfers, Parent Payment Distribution and Overpayment and Write-Off Restoration topic drafts, the Customer Payment Journal Controls reference, and legacy 230 Collections sections 6.5, 6.6 and 6.8 (D-045, D-046). Not validated or approved. |

Guide code, title and scope: `[G221-01]`.

---

## Part 1: What do I need to know? (Customer Payment Corrections)

### High-level process

##### Part Description

This guide covers corrections to customer payments and settlements in D365: settling a payment against open transactions, undoing an incorrect settlement, transferring funds between customer accounts, distributing a parent account payment across child accounts, restoring a written-off or overpayment amount, and writing off a bank fee or small residual balance. Recording a customer payment is in 220 Customer Payments. Writing off an uncollectible debt is in 230 Collections.

Until they are confirmed, these are outside the scope of this guide: who approves a customer payment journal, correcting or reversing a posted journal, a payment already settled against invoices on the wrong account, how to identify a parent-child relationship in D365, and when a write-off should be reversed or cancelled instead of restored. `[CPJ-17 / CPJ-19 / TF-05 / TF-06, PC-01 / CPJ-17 / CPJ-19, RO-02 / CPJ-17 / CPJ-19]`

Topics 3 to 5 and the journal controls in Part 1 come from AI-generated notes of the AR Training D365 Part 2 session and have not been checked against the recording. Topics 1, 2 and 6 come from the legacy 230 Collections PG (v2.3, sections 6.5, 6.6 and 6.8), which is about a year old, and have not been checked against current D365. Do not use this guide on live customer accounts until its blocking items close. `[SRC-01, G221-03]`

##### Initiation

- A payment must be matched to the open invoices or credits it pays. `[G221-04]`
- A settlement was made in error, or against the wrong invoices.
- A payment was posted to the wrong customer account, or funds must move between related customer accounts. `[TF-01]`
- A payment held on a parent customer account must be distributed to confirmed child accounts. `[PC-06]`
- An overpayment or a written-off amount must be put back on a customer account. `[RO-04]`
- A small residual balance remains on a customer transaction, such as a bank fee, a foreign exchange difference, or a minor over or short payment.

##### Stream

| Stream | Process Area | Key Roles |
|---|---|---|
| Order to Cash (O2C) `[GOV-01]` | Customer Payment Corrections | • Collections Officer `[G221-05]`<br>• Group Billing and Credit Manager<br>• To be confirmed for topics 3 to 5 |

##### Process

The high-level process is as follows:

| # | Action | Who | When | Where |
|---|---|---|---|---|
| 1 | [Settle Customer Transactions](#1-settle-customer-transactions) | Collections Officer | When a payment must be matched to the open invoices or credits it pays | D365 |
| 2 | [Undo a Settlement](#2-undo-a-settlement) | Collections Officer | When a settlement was made in error, or against the wrong invoices | D365 |
| 3 | [Transfer Funds Between Customer Accounts](#3-transfer-funds-between-customer-accounts) | To be confirmed | When a payment was posted to the wrong account, or funds must move between related accounts | D365 |
| 4 | [Distribute a Parent Account Payment Across Child Accounts](#4-distribute-a-parent-account-payment-across-child-accounts) | To be confirmed | When a payment held on a parent account must be distributed to confirmed child accounts | D365 |
| 5 | [Restore a Written-Off or Overpayment Amount](#5-restore-a-written-off-or-overpayment-amount) | To be confirmed | When an overpayment or written-off amount must be put back on a customer account | D365 |
| 6 | [Write Off a Bank Fee or Small Residual](#6-write-off-a-bank-fee-or-small-residual) | Collections Officer; approver to be confirmed | When a small residual balance remains after a payment | D365 |

### Roles and responsibilities

##### Overview

The roles for topics 1, 2 and 6 come from the legacy 230 Collections PG. The roles that prepare, post and approve the customer payment journals in topics 3 to 5 are not yet confirmed. `[CPJ-16 / CPJ-17]`

| **Tasks / Business Roles** | Collections Officer | Group Billing and Credit Manager |
|---|---|---|
| [Settle Customer Transactions](#1-settle-customer-transactions) | R |   |
| [Undo a Settlement](#2-undo-a-settlement) | R |   |
| [Transfer Funds Between Customer Accounts](#3-transfer-funds-between-customer-accounts) | TBC | TBC |
| [Distribute a Parent Account Payment Across Child Accounts](#4-distribute-a-parent-account-payment-across-child-accounts) | TBC | TBC |
| [Restore a Written-Off or Overpayment Amount](#5-restore-a-written-off-or-overpayment-amount) | TBC | TBC |
| [Write Off a Bank Fee or Small Residual](#6-write-off-a-bank-fee-or-small-residual) | R | TBC |

\*R = Responsible; TBC = to be confirmed

### Key concepts

##### Overview

Before you start, you need to know how settlement works, the controls that apply to every Customer payment journal (CPJL) entry, and how parent and child accounts and restoration entries are defined.

##### Settlement

| Term | Description |
|---|---|
| **Settlement** | Matching a payment against one or more open invoices or credits on the same customer account, so that their open amounts close. Only open transactions can be settled. `[G221-06]` |
| **Partial settlement** | Settling only part of an invoice, by reducing the amount to settle on the marked line. The rest of the invoice stays open. |
| **Undo settlement** | Reverses a settlement made in error or against the wrong invoices. The payment and the invoices return to open and can be settled again. |
| **Residual write-off** | Clears a small residual balance, such as a bank fee, a foreign exchange difference, an over or short payment or a penny difference, with a reason code. The reason code's posting setup determines the ledger account. |

##### Customer payment journal

| Term | Description |
|---|---|
| **Customer payment journal (CPJL)** | The journal used to transfer funds between customer accounts, distribute a parent account payment and restore a written-off or overpayment amount. `[CPJ-02]` |
| **Bank-to-bank transfer clearing account** | The ledger account used as the offset for a transfer between customer accounts. Do not post a transfer directly to a bank account. `[TF-03 / CPJ-09]` |
| **Simulate Posting** | A check run on the journal before posting. A blue result means the journal is ready to post. A red result shows errors to correct. `[CPJ-14]` |

##### Journal set-up

| Control | What to do |
|---|---|
| **Use CPJL** | Use the Customer payment journal (CPJL) to transfer funds between customer accounts and to restore written-off or overpayment amounts. `[CPJ-01 / CPJ-02]` |
| **Describe the journal and every line** | Enter a clear description on the journal and on each line, including the relevant customer code, so the entry can be identified in each customer's history. `[CPJ-03 / CPJ-04]` |
| **Use the right date** | The current date is the default. A wrong-account correction may use the original customer payment date when appropriate. Use a prior-period date only when it is required and the period is open. `[CPJ-05]` |
| **Keep the original currency** | Enter every line in the currency of the original payment or transaction. `[CPJ-07]` |

##### Line coding

| Control | What to do |
|---|---|
| **Debit to remove, credit to return** | Funds removed from a customer account are a debit. Funds placed on a customer account are a credit. `[CPJ-06]` |
| **Offset to the correct ledger account** | Set **Offset account type** to **Ledger**. For a transfer between customer accounts, use the bank-to-bank transfer clearing account, never a bank account. For a restoration, use the Overpayment ledger. `[CPJ-08 / CPJ-09 / TF-03 / RO-01]` |
| **Leave unsupported fields blank** | For a restoration, do not enter financial tags, an invoice number or a bank account. `[CPJ-10]` |
| **Keep pre-populated dimensions** | For a restoration, do not change the financial dimensions that fill in automatically. `[CPJ-11]` |
| **Complete each line before the next** | Tab through every field in a line before you start the next one, so that fields such as the voucher fill in correctly. `[CPJ-12]` |

##### Validation and posting

| Control | What to do |
|---|---|
| **Balance the journal** | For a transfer or distribution, total debits must equal total credits. In a distribution, the child credits must add up to the parent debit. `[CPJ-13]` |
| **Simulate before posting** | Run Simulate Posting. A blue result means the journal is ready to post. A red result shows errors to read and correct. If you cannot resolve an error, log a request through the D365 issue form (see **Additional Resources**). `[CPJ-14 / CPJ-15]` |
| **Post only when complete and validated** | Post only after every line is complete, the journal balances and Simulate Posting succeeds. `[CPJ-16 / CPJ-17]` |

##### Allocations and amounts

| Term | Description |
|---|---|
| **Partial allocation** | In a parent-account distribution, move only the confirmed amount. The rest stays on the parent account, with a note that explains its purpose. `[PC-04]` |
| **Example amounts** | The training uses example amounts: $100, and a $10,000 receipt with $8,000 distributed and $2,000 left on the parent account. They are examples only, not thresholds, limits or approval levels. |

##### Parent and child accounts

| Term | Description |
|---|---|
| **Parent-child relationship** | D365 does not provide a reliable parent-child indicator. Do not rely on account names alone. `[PC-01]` |
| **Confirmed allocation** | Which child accounts the payment belongs to, and how much each receives, confirmed from remittance, customer confirmation or other validated evidence. `[PC-02]` |
| **Distribution** | One debit on the parent account can be distributed across several child credits, if the child credits add up to the parent debit. |
| **Residual** | In a partial allocation, the part of the payment that is not yet allocated. It stays on the parent account, with a note that explains its purpose. For example, $8,000 of a $10,000 receipt is distributed and $2,000 stays on the parent account. The amounts are an example only, not a threshold. `[PC-04 / PC-05]` |

##### Restoration entry

| Term | Description |
|---|---|
| **Credit to the customer** | An amount being returned to the customer account is entered as a credit. `[CPJ-06]` |
| **Overpayment ledger** | The main account used as the offset for a restoration entry. `[RO-01 / CPJ-09]` |

##### Before you post a transfer

| Rule | Description |
|---|---|
| **Confirm the destination first** | Confirm the correct destination account before you start. `[TF-02]` |
| **Use the original currency** | Use the same currency as the original customer payment. `[CPJ-07]` |
| **Describe the transfer** | Use clear descriptions on the journal and on both lines, so the transfer can be identified in each customer's history. `[CPJ-04]` |
| **Balance the lines** | The source debit and the destination credit must be the same amount. |
| **Simulate before posting** | Run Simulate Posting and resolve every error before you post. |

##### Before you post a distribution

| Rule | Description |
|---|---|
| **Confirm before processing** | Confirm the relationship and the allocation before you create the journal. |
| **Use the original currency** | Keep every line in the currency of the original receipt. `[CPJ-07]` |
| **Describe every line** | Use descriptions that let the transfer be identified in each customer's history. `[CPJ-04]` |
| **Use the clearing account** | Use **Ledger** as the offset type and the bank-to-bank transfer clearing account as the offset. `[TF-03 / CPJ-09]` |
| **Balance the distribution** | The child credits must add up to the amount debited from the parent account. |
| **Simulate before posting** | Run Simulate Posting and resolve every error before you post. |

##### Before you post a restoration `[RO-03]`

| Rule | Description |
|---|---|
| **Use the original currency** | The currency must match the original transaction. `[CPJ-07]` |
| **Describe the entry** | Use a clear description that includes the customer code, for example "Overpayment put back on customer account". `[CPJ-04]` |
| **Leave unsupported fields blank** | Do not enter financial tags, an invoice number or a bank account. `[CPJ-10]` |
| **Keep pre-populated dimensions** | Do not change the financial dimensions that fill in automatically. `[CPJ-11]` |
| **Simulate before posting** | Run Simulate Posting and resolve every error before you post. |

##### Not yet confirmed `[CPJ-16 to CPJ-21]`

| Topic | Status |
|---|---|
| **Who may post a CPJL** | To be confirmed. |
| **Whether approval is needed** | To be confirmed. |
| **Checking the result after posting** | To be confirmed. 230 Collections topic 2.4 Investigate a Customer Account covers reviewing customer transactions. |
| **Correcting or reversing a posted journal** | To be confirmed. Legacy 220 Customer Payments section 4.3 covers reversing a customer payment journal; whether it applies to these journals is to be confirmed. |
| **An unposted journal that is no longer needed** | To be confirmed. |
| **The security role needed** | To be confirmed. If a page or control is missing, a security setting is a possible cause, not a confirmed one. |

---

## Part 2: How do I do it? (Customer Payment Corrections)

### 1. Settle Customer Transactions

##### Description

Use this procedure to settle a customer payment against the open invoices or credits it pays. You open the customer's open transactions, select the payment, mark the invoices to settle and post the settlement. When complete, the payment and the invoices show as settled.

##### Responsibility

- Collections Officer: settles customer payments against open transactions.

##### Initiation

- A payment must be matched to the open invoices or credits it pays.

##### Procedure

Complete these steps to settle customer transactions:

| **Action** | **Description** |
|---|---|
| *PROCESS START* (light blue) | *Pre-requisites:*<br>• The customer account exists in D365, and the payment and the invoices or credits it pays are open on it. `[G221-07]`<br>*Responsibility:*<br>• Collections Officer |
| 1. *Check* the **Entity**. | Confirm you are signed into the correct **Legal Entity** (top-right). |
| 2. *Click* **Modules**. | From the left-hand **Navigation Pane**, click **Modules**. |
| 3. *Navigate* to the **All customers** page. `[G221-08]` | From the **Navigation Pane**, *select*:<br>• **Accounts receivable >**<br>• **Customers >**<br>• **All customers** |
| 4. *Open* the customer account. | Search for the customer and click the customer **Account** to open it. |
| 5. *Open* the customer's transactions. | On the Main Toolbar, *select*:<br>• **Customer >**<br>• **Transactions >**<br>• **Transactions**<br>The **Customer transactions** page is displayed. |
| 6. *Show* open transactions. | In the **Show** field, select **Open**. Only open transactions can be settled. |
| 7. *Select* the payment. | Click the payment voucher to highlight it. |
| 8. *Open* **Settle transactions**. `[G221-09]` | On the Main Toolbar, click **Settlements** and open **Settle transactions**. The page lists the open invoices and credits that can be settled. |
| 9. *Mark* the invoices to settle. `[G221-10]` | In the **Mark** column, select each invoice or credit the payment pays.<br>**Note:** For a partial settlement, reduce the **Amount to settle** on the line. |
| 10. *Confirm* the total settlement amount. `[G221-11]` | Check that the **Total settlement amount** at the bottom of the page is 0.00. If it is not, review the marked lines and amounts. |
| 11. *Click* **Post**. | Click **Post**. The marked transactions are settled and no longer show when **Show** is **Open**. |
| *PROCESS COMPLETE* (light green) | *Outcomes:*<br>• The payment is settled against the marked invoices or credits.<br>• The customer balance and the transaction status are updated. |

> **Note:** To exclude a transaction from collection letters and direct debit runs, see 230 Collections topic 7.3 Change Customer Account Status. Legacy 230 included it in this procedure as optional steps.

### 2. Undo a Settlement

##### Description

Use this procedure to reverse a settlement made in error or against the wrong invoices. You find the settled payment or invoice, undo the settlement and check that the transactions are open again.

##### Responsibility

- Collections Officer: reverses incorrect settlements.

##### Initiation

- A settlement was made in error, or against the wrong invoices.

##### Procedure

Complete these steps to undo a settlement:

| **Action** | **Description** |
|---|---|
| *PROCESS START* (light blue) | *Pre-requisites:*<br>• The settlement was made in error, or against the wrong invoices.<br>*Responsibility:*<br>• Collections Officer |
| 1. *Check* the **Entity**. | Confirm you are signed into the correct **Legal Entity** (top-right). |
| 2. *Click* **Modules**. | From the left-hand **Navigation Pane**, click **Modules**. |
| 3. *Navigate* to the **All customers** page. | From the **Navigation Pane**, *select*:<br>• **Accounts receivable >**<br>• **Customers >**<br>• **All customers** |
| 4. *Open* the customer account. | Search for the customer and click the customer **Account** to open it. |
| 5. *Open* the customer's transactions. | On the Main Toolbar, *select*:<br>• **Customer >**<br>• **Transactions >**<br>• **Transactions**<br>The **Customer transactions** page is displayed. |
| 6. *Show* all transactions. | In the **Show** field, select **All**. Settled transactions are not shown when **Show** is **Open**. |
| 7. *Click* the voucher. | Click the **Voucher** link of the payment, or of a settled invoice, that needs to be unsettled. The **Customer transaction** page is displayed. |
| 8. *Open* **Undo settlement**. `[G221-12]` | On the Main Toolbar, click **Settlements > Undo settlement**. The **Undo settlement** page is displayed. |
| 9. *Mark* the lines to reverse. | In the **Mark** column, select the lines to unsettle, usually the payment and the invoices it was settled against. |
| 10. *Click* **Reverse**. `[G221-13]` | Click **Reverse**. The settlement is removed, and the payment and the invoices return to open. |
| 11. *Confirm* the transactions are open. | Set **Show** to **Open** and check that the payment and the invoices are listed. Settle them correctly with [Settle Customer Transactions](#1-settle-customer-transactions). |
| *PROCESS COMPLETE* (light green) | *Outcomes:*<br>• The incorrect settlement is reversed.<br>• The payment and the invoices are open and can be settled again. |

### 3. Transfer Funds Between Customer Accounts

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
| [Create the Journal and Enter the Source Line](#31-create-the-journal-and-enter-the-source-line) | Create the CPJL and enter the debit line for the customer the funds come from. Output: the source line is complete. |
| [Enter the Destination Line](#32-enter-the-destination-line) | Enter the matching credit line for the customer receiving the funds. Output: a two-line journal. |
| [Validate and Post the Journal](#33-validate-and-post-the-journal) | Check the balance, run Simulate Posting, correct errors and post. Output: the transfer is posted. |

#### 3.1 Create the Journal and Enter the Source Line

##### Procedure

Complete these steps to create the journal and enter the source line:

| **Action** | **Description** |
|---|---|
| *PROCESS START* (light blue) | *Pre-requisites:*<br>• Access to D365 and to **Customer payment journal**. `[CPJ-21]`<br>• The source and destination customer accounts, the amount and the currency of the original payment.<br>• Confirmation that the destination account is correct.<br>• Whether the payment is already settled on the source account. `[TF-05]`<br>*Responsibility:*<br>• To be confirmed |
| 1. *Check* the **Entity**. | Confirm you are signed into the correct **Legal Entity** (top-right). |
| 2. *Click* **Modules**. | From the left-hand **Navigation Pane**, click **Modules**. |
| 3. *Navigate* to the **Customer payment journal** page. `[CPJ-01]` | From the **Navigation Pane**, *select*:<br>• **Credit and collections >**<br>• **Customer payment journal**<br>You can also open **Customer payment journal** from your **Favorites** (see 260 O2C Getting Started, topic 3 Add Pages to Favorites). |
| 4. *Create* a new journal. `[CPJ-01 / CPJ-02]` | Start a new CPJL journal. |
| 5. *Enter* the journal description. `[CPJ-03]` | Describe the transfer clearly and include the customer codes, for example "Transfer funds from customer A to customer B". |
| 6. *Open* the journal lines. `[CPJ-01]` | Open the lines of the new journal. |
| 7. *Enter* the transaction date. `[CPJ-05]` | The current date is the default. A wrong-account correction may use the original customer payment date when appropriate. |
| 8. *Select* the source customer account. | Select the customer account the funds are being removed from. The customer name fills in automatically. |
| 9. *Enter* the amount as a debit. `[CPJ-06]` | Enter the amount being removed from the source customer as a debit, in the currency of the original payment. |
| 10. *Enter* the line description. `[CPJ-03]` | Use the same clear transfer description, so the transaction can be identified in the customer's history. |
| 11. *Select* **Ledger** as the **Offset account type**. `[CPJ-08]` | Set the offset account type to **Ledger**. |
| 12. *Select* the bank-to-bank transfer clearing account. `[TF-03]` | Select the clearing account used for transfers between customer accounts as the offset account. Do not use a bank account. |
| 13. *Complete* the line. `[CPJ-12]` | Tab through every field in the line before you start the next one, so that fields such as the voucher fill in correctly. |
| *STEP COMPLETE* (light blue) | • The source line is complete.<br>• Continue to [Enter the Destination Line](#32-enter-the-destination-line) |

#### 3.2 Enter the Destination Line

##### Procedure

Complete these steps to enter the destination line:

| **Action** | **Description** |
|---|---|
| *PROCESS START* (light blue) | *Pre-requisites:*<br>• The source line is complete (see [Create the Journal and Enter the Source Line](#31-create-the-journal-and-enter-the-source-line)).<br>*Responsibility:*<br>• To be confirmed |
| 1. *Add* a new line. `[CPJ-01 / CPJ-05]` | Add another line to the journal. |
| 2. *Select* the destination customer account. | Select the customer account receiving the funds. The customer name fills in automatically. |
| 3. *Enter* the amount as a credit. `[CPJ-06]` | Enter the same amount as the source line as a credit, in the same currency. |
| 4. *Enter* the line description. | Use the same description as the source line, so the transfer can be identified in both customers' histories. |
| 5. *Select* **Ledger** as the **Offset account type**. `[TF-04]` | Apply the same offset treatment as the source line. |
| 6. *Select* the bank-to-bank transfer clearing account. | Select the same clearing account as the source line. |
| 7. *Complete* the line. | Tab through every field in the line. |
| *STEP COMPLETE* (light blue) | • The journal has a source debit line and a matching destination credit line.<br>• Continue to [Validate and Post the Journal](#33-validate-and-post-the-journal) |

#### 3.3 Validate and Post the Journal

##### Procedure

Complete these steps to validate and post the journal:

| **Action** | **Description** |
|---|---|
| *PROCESS START* (light blue) | *Pre-requisites:*<br>• Both lines are complete (see [Enter the Destination Line](#32-enter-the-destination-line)).<br>*Responsibility:*<br>• To be confirmed |
| 1. *Check* the journal balances. `[CPJ-13]` | Confirm that total debits equal total credits, and that the currency and date are correct. |
| 2. *Run* **Simulate Posting**. `[CPJ-14]` | Check the journal before posting. A blue result means the journal is ready to post. |
| 3. *Correct* any errors. `[CPJ-15]` | If Simulate Posting shows an error, read it, correct the line it names and run Simulate Posting again. If you cannot resolve the error, log a request through the D365 issue form (see **Additional Resources**) before you post. |
| 4. *Post* the journal. `[CPJ-16 / CPJ-17]` | Post only when every line is complete, the journal balances and Simulate Posting succeeds. |
| 5. *Verify* the transfer. `[CPJ-18]` | Check that the transfer appears with its description on both customer accounts. |
| *PROCESS COMPLETE* (light green) | *Outcomes:*<br>• A balanced CPJL is posted: a debit on the source customer and a matching credit on the destination customer, with the bank-to-bank transfer clearing account as the offset. `[CPJ-19]`<br>• The transfer can be identified by its description in both customers' histories. |

### 4. Distribute a Parent Account Payment Across Child Accounts

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
| [Create the Journal and Enter the Parent Line](#41-create-the-journal-and-enter-the-parent-line) | Create the CPJL and enter the debit for the amount being moved off the parent account. Output: the parent line is complete. |
| [Enter the Child Lines](#42-enter-the-child-lines) | Enter one credit line for each child account. Output: the distribution is entered. |
| [Validate and Post the Journal](#43-validate-and-post-the-journal) | Check the totals, run Simulate Posting, correct errors, post, and record any residual. Output: the distribution is posted. |

#### 4.1 Create the Journal and Enter the Parent Line

##### Procedure

Complete these steps to create the journal and enter the parent line:

| **Action** | **Description** |
|---|---|
| *PROCESS START* (light blue) | *Pre-requisites:*<br>• Access to D365 and to **Customer payment journal**. `[CPJ-21]`<br>• A confirmed parent-child relationship.<br>• A confirmed allocation: each child account, its amount, and the total to move.<br>• The currency of the original receipt.<br>*Responsibility:*<br>• To be confirmed |
| 1. *Check* the **Entity**. | Confirm you are signed into the correct **Legal Entity** (top-right). |
| 2. *Click* **Modules**. | From the left-hand **Navigation Pane**, click **Modules**. |
| 3. *Navigate* to the **Customer payment journal** page. `[CPJ-01]` | From the **Navigation Pane**, *select*:<br>• **Credit and collections >**<br>• **Customer payment journal**<br>You can also open **Customer payment journal** from your **Favorites** (see 260 O2C Getting Started, topic 3 Add Pages to Favorites). |
| 4. *Create* a new journal. `[CPJ-01 / CPJ-02]` | Start a new CPJL journal. |
| 5. *Enter* the journal description. `[CPJ-03]` | Describe the transfer clearly, so it identifies the parent and child transfer. |
| 6. *Open* the journal lines. `[CPJ-01]` | Open the lines of the new journal. |
| 7. *Enter* the transaction date. `[CPJ-05]` | Enter the date for the distribution. |
| 8. *Select* the parent customer account. | Select the parent account that holds the payment. The customer name fills in automatically. |
| 9. *Enter* the amount to move as a debit. `[CPJ-06]` | Enter the total being moved off the parent account as a debit, in the currency of the original receipt. In a partial allocation, enter only the confirmed amount. The rest stays on the parent account. |
| 10. *Enter* the line description. `[CPJ-03]` | Use a description that identifies the transfer in the parent account's history. |
| 11. *Select* **Ledger** as the **Offset account type**. `[CPJ-08]` | Set the offset account type to **Ledger**. |
| 12. *Select* the bank-to-bank transfer clearing account. `[TF-03 / PC-03]` | Select the clearing account as the offset account. |
| 13. *Complete* the line. `[CPJ-12]` | Tab through every field in the line before you start the next one, so that fields such as the voucher fill in correctly. |
| *STEP COMPLETE* (light blue) | • The parent line is complete.<br>• Continue to [Enter the Child Lines](#42-enter-the-child-lines) |

#### 4.2 Enter the Child Lines

##### Procedure

Complete these steps for each child account:

| **Action** | **Description** |
|---|---|
| *PROCESS START* (light blue) | *Pre-requisites:*<br>• The parent line is complete (see [Create the Journal and Enter the Parent Line](#41-create-the-journal-and-enter-the-parent-line)).<br>*Responsibility:*<br>• To be confirmed |
| 1. *Add* a new line. `[CPJ-01 / CPJ-05]` | Add another line to the journal. |
| 2. *Select* the child customer account. | Select a child account in the confirmed allocation. The customer name fills in automatically. |
| 3. *Enter* the child's amount as a credit. `[CPJ-06]` | Enter the amount allocated to this child account as a credit, in the same currency as the parent line. |
| 4. *Enter* the line description. | Use a description that identifies the transfer in this child account's history. |
| 5. *Select* **Ledger** as the **Offset account type**. `[PC-03]` | Apply the same offset treatment as the parent line. |
| 6. *Select* the bank-to-bank transfer clearing account. | Select the same clearing account as the parent line. |
| 7. *Complete* the line. | Tab through every field in the line. |
| 8. *Repeat* for each child account. | Repeat steps 1 to 7 until every child account in the confirmed allocation has a credit line. |
| *STEP COMPLETE* (light blue) | • Every child account in the allocation has a credit line.<br>• Continue to [Validate and Post the Journal](#43-validate-and-post-the-journal) |

#### 4.3 Validate and Post the Journal

##### Procedure

Complete these steps to validate and post the journal:

| **Action** | **Description** |
|---|---|
| *PROCESS START* (light blue) | *Pre-requisites:*<br>• The parent line and every child line are complete (see [Enter the Child Lines](#42-enter-the-child-lines)).<br>*Responsibility:*<br>• To be confirmed |
| 1. *Check* the distributed total. `[CPJ-13]` | Confirm that the child credits add up to the parent debit, and that the currency and date are correct. |
| 2. *Run* **Simulate Posting**. `[CPJ-14]` | Check the journal before posting. A blue result means the journal is ready to post. |
| 3. *Correct* any errors. `[CPJ-15]` | If Simulate Posting shows an error, read it, correct the line it names and run Simulate Posting again. If you cannot resolve the error, log a request through the D365 issue form (see **Additional Resources**) before you post. |
| 4. *Post* the journal. `[CPJ-16 / CPJ-17]` | Post only when every line is complete, the totals match and Simulate Posting succeeds. |
| 5. *Record* the purpose of any residual. `[PC-04]` | Optional. In a partial allocation, add a note that explains why the remaining amount stays on the parent account. Otherwise, go to step 6. |
| 6. *Verify* the distribution. `[CPJ-18]` | Check that the distribution appears with its description on the parent and child accounts. |
| *PROCESS COMPLETE* (light green) | *Outcomes:*<br>• A balanced CPJL is posted: a debit on the parent account and matching credits on the child accounts, with the bank-to-bank transfer clearing account as the offset. `[CPJ-19]`<br>• Any residual stays on the parent account with a note that explains its purpose. |

### 5. Restore a Written-Off or Overpayment Amount

##### Description

Use this topic to put a written-off or overpayment amount back on a customer account. You create a CPJL journal with one credit line for the customer, offset to the Overpayment ledger, then run Simulate Posting and post.

##### Responsibility

- To be confirmed: prepares and posts the restoration journal. `[GOV-01]`

##### Initiation

- An overpayment or a written-off amount must be put back on a customer account.

##### Topic Overview

This topic includes these steps:

| Step | Description |
|---|---|
| [Create the Restoration Line](#51-create-the-restoration-line) | Create the CPJL and enter the customer credit with the Overpayment ledger offset. Output: the line is complete. |
| [Validate and Post the Journal](#52-validate-and-post-the-journal) | Run Simulate Posting, correct errors and post. Output: the amount is back on the customer account. |

#### 5.1 Create the Restoration Line

##### Procedure

Complete these steps to create the restoration line:

| **Action** | **Description** |
|---|---|
| *PROCESS START* (light blue) | *Pre-requisites:*<br>• Access to D365 and to **Customer payment journal**. `[CPJ-21]`<br>• The customer account, amount and original currency.<br>*Responsibility:*<br>• To be confirmed |
| 1. *Check* the **Entity**. | Confirm you are signed into the correct **Legal Entity** (top-right). |
| 2. *Click* **Modules**. | From the left-hand **Navigation Pane**, click **Modules**. |
| 3. *Navigate* to the **Customer payment journal** page. `[CPJ-01]` | From the **Navigation Pane**, *select*:<br>• **Credit and collections >**<br>• **Customer payment journal**<br>You can also open **Customer payment journal** from your **Favorites** (see 260 O2C Getting Started, topic 3 Add Pages to Favorites). |
| 4. *Create* a new journal. `[CPJ-01 / CPJ-02]` | Start a new CPJL journal. |
| 5. *Enter* the journal description. `[CPJ-03]` | Use a clear description that includes the customer code, for example "Overpayment put back on customer account". |
| 6. *Open* the journal lines. `[CPJ-01]` | Open the lines of the new journal. |
| 7. *Enter* the transaction date. `[CPJ-05]` | Use the current date, unless a valid prior-period date is required and the period is open. |
| 8. *Select* the customer account. | Select the customer the amount is returned to. The name fills in automatically. |
| 9. *Enter* the amount as a credit. `[CPJ-06 / CPJ-07]` | Enter the amount as a credit, in the currency of the original transaction. |
| 10. *Enter* the line description. `[CPJ-03]` | Use the same description, so the entry shows in the customer's history. |
| 11. *Leave* the other fields blank. `[CPJ-10]` | Do not enter financial tags, an invoice number or a bank account. |
| 12. *Select* **Ledger** as the **Offset account type**. `[CPJ-08]` | Set the offset account type to **Ledger**. |
| 13. *Select* the Overpayment ledger. `[RO-01]` | Search for and select the Overpayment ledger in the main account field. |
| 14. *Keep* the dimensions. `[CPJ-11]` | Do not change the financial dimensions that fill in automatically. |
| 15. *Complete* the line. `[CPJ-12]` | Tab through every field, so fields such as the voucher fill in. |
| *STEP COMPLETE* (light blue) | • The restoration line is complete.<br>• Continue to [Validate and Post the Journal](#52-validate-and-post-the-journal) |

#### 5.2 Validate and Post the Journal

##### Procedure

Complete these steps to validate and post the journal:

| **Action** | **Description** |
|---|---|
| *PROCESS START* (light blue) | *Pre-requisites:*<br>• The restoration line is complete (see [Create the Restoration Line](#51-create-the-restoration-line)).<br>*Responsibility:*<br>• To be confirmed |
| 1. *Run* **Simulate Posting**. `[CPJ-14]` | Check the journal before posting. A blue result means the journal is ready to post. |
| 2. *Correct* any errors. `[CPJ-15]` | If Simulate Posting shows an error, read it, correct the line it names and run Simulate Posting again. If you cannot resolve the error, log a request through the D365 issue form (see **Additional Resources**) before you post. |
| 3. *Post* the journal. `[CPJ-16 / CPJ-17]` | Post only when the line is complete and Simulate Posting succeeds. |
| 4. *Verify* the restoration. `[CPJ-18]` | Check that the amount appears with its description on the customer account. |
| *PROCESS COMPLETE* (light green) | *Outcomes:*<br>• A CPJL is posted with a credit on the customer account and the Overpayment ledger as the offset. `[CPJ-19]`<br>• The entry can be identified by its description in the customer's history. |

### 6. Write Off a Bank Fee or Small Residual

##### Description

Use this procedure to write off a small residual balance on a customer transaction, such as a bank fee, a foreign exchange difference, an over or short payment or a penny difference. You start the write-off from **Aged balances**, select a reason code, check the general journal D365 creates and submit it for approval. Writing off an uncollectible debt is a different task, in 230 Collections.

##### Responsibility

- Collections Officer: creates the write-off and submits the journal for approval.
- Approver: to be confirmed. Approves the write-off journal. `[G221-14]`

##### Initiation

- A small residual balance remains on a customer transaction after a payment.

##### Procedure

Complete these steps to write off a bank fee or small residual:

| **Action** | **Description** |
|---|---|
| *PROCESS START* (light blue) | *Pre-requisites:*<br>• The residual amount and its cause are known: a bank fee, a foreign exchange difference, an over or short payment, or a penny difference. `[G221-15]`<br>*Responsibility:*<br>• Collections Officer |
| 1. *Check* the **Entity**. | Confirm you are signed into the correct **Legal Entity** (top-right). |
| 2. *Click* **Modules**. | From the left-hand **Navigation Pane**, click **Modules**. |
| 3. *Navigate* to the **Aged balances** page. `[G221-16]` | From the **Navigation Pane**, *select*:<br>• **Credit and collections >**<br>• **Collections >**<br>• **Aged balances**<br>You can also open **Aged balances** from your **Favorites**. |
| 4. *Select* the customer. | In the **Customer aging** list, select the customer account. |
| 5. *Select* the open transaction. | In **Open transactions**, find the invoice or other open transaction with the residual, and click the line to select it. |
| 6. *Click* **Write off**. `[G221-17]` | On the toolbar, click **Write off**. The write-off window opens. |
| 7. *Select* the **Reason code**. `[G221-18]` | Select the reason for the residual, for example:<br>• **BANK FEE**<br>• **FOREX**<br>• **OVER/SHORT**<br>• **PENNY DIFF**<br>The reason code's posting setup determines the ledger account. |
| 8. *Confirm* the **Amount**. | Confirm the amount. For a partial write-off, change it to the amount to write off. |
| 9. *Click* **OK**. `[G221-19]` | Click **OK**. D365 creates a general journal for the write-off and settles it against the selected transaction. |
| 10. *Open* the general journal. | Open the general journal D365 created, from the journal link or from **General journals**. |
| 11. *Verify* the journal. | Check:<br>• The amount and the description.<br>• The ledger account the reason code posts to.<br>• Any required financial dimensions. |
| 12. *Submit* the journal for approval. | On the Main Toolbar, click **Approval > Report as ready**. The approver receives a notification to review the journal, and you receive a notification when it is approved. |
| 13. *Confirm* the write-off in **Aged balances**. `[G221-20]` | Return to **Customer aging** and click **Refresh**.<br>**Note:** A batch job updates aging balances every 10 minutes, so the write-off may not show straight away. |
| *PROCESS COMPLETE* (light green) | *Outcomes:*<br>• The residual is written off: the balance is cleared, or reduced for a partial write-off.<br>• The transaction shows as settled.<br>• The write-off journal is submitted for approval. |

---

## Part 3: Reports (Customer Payment Corrections)

##### Overview

Reports for this process are pending SME confirmation. `[GOV-04]`

---

## Additional Resources

The standard template block, unchanged.
