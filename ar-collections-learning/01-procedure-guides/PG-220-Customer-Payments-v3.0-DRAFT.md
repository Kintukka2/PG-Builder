# D365 F&O: Customer Payments Procedure Guide

> **WORKING DRAFT. Not validated or approved.**
>
> This is a Markdown preview of the Word guide [`220-Customer Payments PG v3.0.docx`](220-Customer%20Payments%20PG%20v3.0.docx). It consolidates version 2.1 and 221 Customer Payment Corrections v0.1 (D-055). **The Word file is the editable source.**
>
> Markers such as `[G220-01]` or `[CPJ-14]` show unconfirmed items. In the Word file, each one is a review comment. Guide-level items and the index of carried items are in the [validation register](../03-validation/220-Customer-Payments-v3.0-Validation.md). The markers are not part of the guide text.

The fixed template content is not repeated here: cover, Contents, *About this guide* and *Additional Resources*.

**Version history**

| ID | Date | Author/s | BPO | Description of change |
|---|---|---|---|---|
| 1.0 | 17 February 2025 | Michael Thurlow |   | First Version (NZ) |
| 2.0 | 28 November 2025 | Daniel Moreira |   | Version Update (Global) |
| 2.1 | 29 January 2026 | Suzanne Starr |   | Content Update (Formatting) |
| 3.0 | November 2026 | Daniel Moreira | Christopher Clarke | Working draft (D-055): rebuilt in the PG master template; 221 Customer Payment Corrections merged in; Collections Officer roles; settlement methods in topic 2; direct debit links to 240. Not validated or approved. `[G220-01]` |

---

## Part 1: What do I need to know? (Customer Payments)

### High-level process

##### Part Description

**Customer Payments** are processed through an automated integration between BankFabric, ExFlow, and D365.

Bank statements are automatically transmitted via BankFabric and create bank statement transactions in D365. Remittance advice received via the Accounts Receivable mailbox is processed by ExFlow, where customer and invoice details are extracted to support automated matching.

In D365, transactions appear in **Process Customer Settlements**, where matching rules attempt to:

- Identify the Customer account from the bank narrative.
- Match the payment to one or more open invoices.
- Settle invoices automatically where criteria are met.
- Place unmatched amounts **On Account**.

This guide covers the work that follows: handling remittance exceptions in ExFlow, settling customer payments by the method that fits the payment, correcting payments and settlements, and maintaining the settlement configuration that drives automatic matching. Version 3.0 also brings in the payment corrections that were drafted as 221 Customer Payment Corrections.

At a high level, the Customer Payments process follows these stages:

- **Handle Remittance Exceptions in ExFlow**: correct the remittance advices that ExFlow cannot process, so their invoice details reach D365.
- **Settle Customer Payments**: settle each payment against the invoices or credits it pays, by the method that fits where the payment is (topic 2 shows which method to use).
- **Correct Customer Payments**: undo a settlement, reverse a payment journal, move funds between customer accounts, distribute a parent account payment, restore a written-off or overpayment amount, or write off a small residual.
- **Maintain Settlement Configuration**: keep the settlement rules, parse rules and alternate customer names up to date, so that more payments match automatically.
- **Process Intercompany Customer Payments**: Receipting Officers process payments made into the bank account of another legal entity.
- **Process Direct Debit Customer Payments**: see 240 Direct Debit and Credit Card Payments.

Writing off an uncollectible debt is in 230 Collections. General D365 tasks (switching legal entity, Favorites, personalized views and exporting grid data) are in 260 O2C Getting Started.

##### Initiation

- Bank statement transactions are imported into D365 through BankFabric. `[G220-02]`
- ExFlow cannot process a remittance advice.
- A payment is not on the bank statement, or cannot be settled automatically.
- A payment or settlement must be corrected, or funds must move between customer accounts.
- Payments repeatedly fail to match, or are applied incorrectly.
- A customer pays into the bank account of another legal entity.

##### Stream

| Stream | Process Area | Key Roles |
|---|---|---|
| Order to Cash (O2C) | Customer Payments | • Collections Officer `[G220-03]`<br>• Receipting Officer (intercompany payments) |

##### Process

The high-level Customer Payments process is as follows:

| # | Action | Who | When | Where |
|---|---|---|---|---|
| 0 | Bank statements uploaded to D365 | System (BankFabric integration) | Automatically, on the file schedule | BankFabric |
| 1 | [Handle Remittance Exceptions in ExFlow](#1-handle-remittance-exceptions-in-exflow) | Collections Officer | When ExFlow cannot process a remittance advice | ExFlow |
| 2 | [Settle Customer Payments](#2-settle-customer-payments) | Collections Officer | Daily as bank statements arrive, and when the details of what a payment pays become available | D365 |
| 3 | [Correct Customer Payments](#3-correct-customer-payments) | Collections Officer | When a payment or settlement is wrong, or funds must move between customer accounts | D365 |
| 4 | [Maintain Settlement Configuration](#4-maintain-settlement-configuration) | Collections Officer | When payments repeatedly fail to match or are applied incorrectly | D365 |
| 5 | [Process Intercompany Customer Payments](#5-process-intercompany-customer-payments) | Receipting Officer | When a customer pays into the bank account of another legal entity | D365 |
| 6 | [Process Direct Debit Customer Payments](#6-process-direct-debit-customer-payments) | Receipting Officer (see 240) | On the direct debit schedule | D365 |

### Roles and responsibilities

##### Overview

Collections Officers process customer payments and settlements and correct them. Receipting Officers process intercompany payments. Both may post a customer payment journal (CPJL), which needs no approval. Direct debit roles are in 240 Direct Debit and Credit Card Payments.

| **Tasks / Business Roles** | Collections Officer | Receipting Officer |
|---|---|---|
| 1 [Handle Remittance Exceptions in ExFlow](#1-handle-remittance-exceptions-in-exflow) | R |   |
| 2 [Settle Customer Payments](#2-settle-customer-payments) | R |   |
| 2.1 [Settle Bank Statement Payments](#21-settle-bank-statement-payments) | R |   |
| 2.2 [Record and Settle a Manual Payment Journal](#22-record-and-settle-a-manual-payment-journal) | R |   |
| 2.3 [Settle Open Customer Transactions](#23-settle-open-customer-transactions) | R |   |
| 3 [Correct Customer Payments](#3-correct-customer-payments) | R |   |
| 3.1 [Undo a Settlement](#31-undo-a-settlement) | R |   |
| 3.2 [Reverse a Customer Payment Journal](#32-reverse-a-customer-payment-journal) | R |   |
| 3.3 [Transfer Funds Between Customer Accounts](#33-transfer-funds-between-customer-accounts) | R |   |
| 3.4 [Distribute a Parent Account Payment Across Child Accounts](#34-distribute-a-parent-account-payment-across-child-accounts) | R |   |
| 3.5 [Restore a Written-Off or Overpayment Amount](#35-restore-a-written-off-or-overpayment-amount) | R |   |
| 3.6 [Write Off a Bank Fee or Small Residual](#36-write-off-a-bank-fee-or-small-residual) | R |   |
| 4 [Maintain Settlement Configuration](#4-maintain-settlement-configuration) | R |   |
| 4.1 [Maintain Customer Settlement Rules](#41-maintain-customer-settlement-rules) | R |   |
| 4.2 [Maintain Customer Parse Rules](#42-maintain-customer-parse-rules) | R |   |
| 4.3 [Review Remittance Text Analysis Rules](#43-review-remittance-text-analysis-rules) | R |   |
| 4.4 [Search for Customer using Alternate name](#44-search-for-customer-using-alternate-name) | R |   |
| 4.5 [Create or Update Customer Alternate Name](#45-create-or-update-customer-alternate-name) | R |   |
| 5 [Process Intercompany Customer Payments](#5-process-intercompany-customer-payments) |   | R |
| 6 [Process Direct Debit Customer Payments](#6-process-direct-debit-customer-payments) |   | R |

\*R = Responsible

> **Note:** Before the April go-live, Receipting Officers processed customer payments, and version 2.1 of this guide names them. Collections Officers now do this work.

### Key concepts

##### Overview

Before you start, you need to know how payments arrive and are matched, the settlement terms, and the controls that apply to every customer payment journal (CPJL) entry.

##### Automated Bank Statements

Customer payments are automatically imported in D365 from Bank Fabric integration without manual uploads. This ensures payments are available for processing as soon as the bank synch completes.

##### BankFabric

BankFabric manages the underlying bank integrations that deliver bank statements to D365. It operates in the background and does not require any interactions from end users.

##### ExFlow (Remittance Advice Automation)

ExFlow automatically process remittance advice emails and attempts to extract invoice information to support automated matching. Users only access ExFlow for exceptions where remittances could not be read automatically and require review or re-training.

##### ExFlow Training

When remittance data is corrected manually in ExFlow, the system learns the corrections to improve future matching.

##### Bank Statement Narrative

The bank statement narrative is the free-text description provided by the bank with each payment and is the primary source used to identify the customer account and invoice on a transaction. This information mainly includes invoice numbers, customer names, or references.

##### Matching Status

The Match status indicates how successfully a bank statement transaction has been matched in D365. The system first attempts to identify the customer account from the bank statement narrative. Once the customer is identified, D365 then attempts to match the payment against one or more open invoices for that customer.

The match status determines;

Whether the customer has been identified.

Whether the open invoice has been matched.

Whether the settlement is complete.

What action the Collections Officer must take.

| **Match Color** | **What it means** | **Scenario** | **User Action** | **Go to process** |
|---|---|---|---|---|
| Green | Fully Matched | The payment has been successfully matched and settled against one or more open customer invoices | No further investigation is required.<br>These transactions are fully processed by the system. | NA |
| Yellow | Proposed settlement (requires confirmation). | The customer account and open invoice(s) have been identified, and the system has generated a settlement and transaction is automatically posted. | No manual processing is required.<br>Only review if specifically required e.g. exception or discrepancy identified. | NA |
| Red | Not matched | The system could not identify the customer account or match the payment to an open invoice. | Review the bank narrative, search for the customer account or invoice or Alternate name.<br>Manually select the invoice and allocate the payment. If no invoice exists, post the payment On account. Escalate to Collections if unresolved. | [2.1.3 Process Customer Settlements – Red Status (Customer or Invoice Not Identified).](#213-process-customer-settlements--red-status-customer-or-invoice-not-identified) |
| Blue | Posted to customer account (On Account / Unallocated) | The customer account has been identified, but no matching invoice was found. | Review the narrative and open invoices. Apply the payment to the correct invoice(s) where possible or post on account if no match is identified | [2.1.2 Process Customer Settlements – Blue Status (On Account)](#212-process-customer-settlements--blue-status-customer-identified-on-account) |

##### Alternate Customer Names

Alternate customer names are additional names maintained on the customer record to improve automated matching of bank statements narratives. Customers may use different legal, trading or abbreviated names when making payments.

##### Short Payments

A short payment occurs when the amount received is less than the invoice amount. This may be caused by bank fees or underpayment by the customer.

##### Bank Fees

Bank fees are charged by the bank from a customer payment and may result in short payments. Where a bank fee is clearly identifiable, write it off (see [3.6 Write Off a Bank Fee or Small Residual](#36-write-off-a-bank-fee-or-small-residual)); otherwise, the Collections Officer investigates the difference.

##### Collections Investigation

Payments that cannot be fully resolved during settlement stay On Account, and the Collections Officer investigates them. This includes unallocated payments, short payments with unclear causes and unidentified payments. The Collections Officer may contact the customer to obtain remittance details or confirm payment intent. `[G220-04]`

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

##### Posting and permissions `[CPJ-16 to CPJ-21]`

| Topic | Status |
|---|---|
| **Who may post a CPJL** | Collections Officers and Receipting Officers. |
| **Whether approval is needed** | No approval is needed to post a CPJL. |
| **Checking the result after posting** | To be confirmed. 230 Collections topic 2.4 Investigate a Customer Account covers reviewing customer transactions. |
| **Correcting or reversing a posted journal** | To be confirmed. [3.2 Reverse a Customer Payment Journal](#32-reverse-a-customer-payment-journal) covers reversing a customer payment journal; whether it applies to these journals is to be confirmed. |
| **An unposted journal that is no longer needed** | A Collections Officer can delete it. The steps are to be confirmed. |
| **The security role needed** `[G220-05]` | To be confirmed. If a page or control is missing, a security setting is a possible cause, not a confirmed one. |

---

## Part 2: How do I do it? (Customer Payments)

### 1. Handle Remittance Exceptions in ExFlow

**Off-system**: this step is completed outside the D365 system (**ExFlow**).

##### Description

ExFlow automatically processes remittance advices received via the Accounts Receivable mailbox forwarding rule. The remittance data is successfully extracted and validated; and where no errors exist, it is exported automatically to D365 for settlement matching.

The Collections Officer accesses ExFlow only when exceptions occur.

Exceptions may include:

- Customer not identified
- Invoice number not recognized
- Invoice date missing
- Validation errors preventing exports.

When a customer or invoice is correct in ExFlow, the system retains the correction pattern and applies it to a similar remittance format in future. This reduces repeated manual intervention and improves matching accuracy over time.

Once corrected, the remittance is exported and becomes available in D365 for settlement processing.

##### Responsibility

The Collections Officer is responsible for reviewing and resolving remittance exceptions in ExFlow.

##### Summary

This step involves reviewing and resolving remittance exceptions in ExFlow:

| **If…** | **Then…** |
|---|---|
| **Access ExFlow Data Capture** | 1. Access ExFlow - ExFlow Data Capture<br>2. Open ExFlow application<br>3. Confirm the Documents workspace is displayed. |
| **In Progress – Manual Verification Required** | 4. *Click* **In progress** in the left navigation pane.<br>5. Review documents with status **Pending manual verification**.<br>6. *Select* the remittance record.<br>7. *Click* **Start** to open the document |
| **Review Extracted Data** | 8. Confirm the **Customer**, **Invoice** **number**, **Invoice** **date** and **Amount** fields are populated correctly.<br>9. Compare the extracted data to the remittance attachments for accuracy. |
| **Correct Customer Information** | 10. *Click* into the **Customer** field if blank or incorrect.<br>11. Use the lookup to search and select the customer account.<br>12. Confirm the field updates successfully. |
| **Correct Invoice Details** | 13. Enter or amend the Invoice number if not correctly extracted.<br>14. Select the correct Invoice date from the calendar.<br>15. Confirm the invoice amount matches the remittance total. |
| **Validate and Extract** | 16. *Click* **Start** to run validation.<br>17. Review validation messages.<br>18. *Click* **OK** to export.<br>19. Confirm the document is removed from **In Progress**. |

### 2. Settle Customer Payments

##### Description

A customer payment is settled against the invoices or credits it pays, so that their open amounts close. D365 offers three ways to do this. The right one depends on where the payment is: on the bank statement, in a payment journal you are preparing, or already posted to the customer account.

##### Responsibility

- Collections Officer: settles customer payments against the invoices or credits they pay.

##### Initiation

- A customer payment is received, or the details of what it pays become available.

##### Which method to use `[G220-06]`

Use the method that fits where the payment is:

| Method | Use it when |
|---|---|
| [2.1 Settle Bank Statement Payments](#21-settle-bank-statement-payments) | The payment came in on the bank statement and shows **Blue** (customer identified, On Account) or **Red** (not identified) on the **Process customer settlements** page. **Green** and **Yellow** payments need no action. |
| [2.2 Record and Settle a Manual Payment Journal](#22-record-and-settle-a-manual-payment-journal) | The payment is not on the bank statement (for example a cheque, a delayed file or a failed import), or it needs a backdated entry. Record it in a customer payment journal (**Customer payment journals** page) and settle it before you post. |
| [2.3 Settle Open Customer Transactions](#23-settle-open-customer-transactions) | The payment is already posted to the customer account, for example On Account, and you now know which invoices or credits it pays. Settle it from the customer's **Transactions** page (**Settlements** > **Settle transactions**). |

> **Note:** To move a posted payment to another customer account, or to distribute a parent account payment to child accounts, see [3 Correct Customer Payments](#3-correct-customer-payments). A small difference between a payment and its invoices is written off with [3.6 Write Off a Bank Fee or Small Residual](#36-write-off-a-bank-fee-or-small-residual).

#### 2.1 Settle Bank Statement Payments

##### Description

The Process Customer Settlements topic is used to review, record, and allocate customer payments received through bank integration.

Bank statement transactions are automatically imported into D365 via Bank Fabric. The Collections Officer reviews imported transactions, and processes those that require manual action.

When transactions are imported, D365 performs automated matching in two stages:

- **Customer identification**: D365 reads the bank narrative and attempts to identify the Customer Account number, invoice reference, Customer eBanking details, or configured matching rules.
- **Invoice Matching**: Once the Customer account is identified, D365 searches for open invoices under that customer and attempts to apply the payment.

Each transaction is assigned a Match color status – Green, Yellow, Red or Blue – indicating the outcome of this Matching logic and whether user action is required.

Green - The payment has been successfully matched and posted by the system; No user action is required.

Yellow – The system has identified the customer matched the transaction using configured matching rules. These transactions are expected to automatically post once matching rules are validated as part of the bank reconciliation process. No manual processing is required unless an exception is identified.

Red – The system could not identify the customer or match the payment to an invoice. Investigation and manual processing are required.

Blue - the customer has been identified but no invoice has been matched. The payment is posted to the customer account as an unallocated (on account) payment and requires review and allocation.

The Collections Officer focuses on transactions that require manual action, typically Red and Blue transactions, and processes or investigates them before moving to the next transaction.

This process includes;

- Reviewing imported bank statement transactions.
- Confirming or correcting customer identification.
- Settling payments against open invoices.
- Posting payments **On Account** where no invoice is available

These activities ensure customer payments are recorded accurately, invoices are cleared correctly and customer and bank balances remain aligned for reconciliation.

##### Responsibility

The Collections Officer is responsible for reviewing match status outcomes, confirming or correcting settlement and creating manual payment journals where required.

##### Initiation

This process is initiated when new bank statements transactions are automatically imported into D365 via Bank Fabric and become available for processing.

##### Topic Overview

This topic includes these steps:

| Step | Description |
|---|---|
| [Access Customer Settlements](#211-access-customer-settlements) | Open the Process customer settlements page, where imported bank transactions are reviewed and settlement starts. |
| [Process Customer Settlements – Blue Status](#212-process-customer-settlements--blue-status-customer-identified-on-account) | Review and post payments with a Blue match status: the customer is identified, but the payment is not linked to an invoice. |
| [Process Customer Settlements – Red Status](#213-process-customer-settlements--red-status-customer-or-invoice-not-identified) | Investigate payments with a Red match status: D365 could not identify the customer or match the payment to an invoice. |

#### 2.1.1 Access Customer Settlements

##### Procedure

Complete these steps to Access Customer Settlement:

| **Action** | **Description** |
|---|---|
| PROCESS START | **Pre-requisites:**<br>1. *Bank statements are visible in D365* |
| 2. *Check* the **Entity**. | Confirm that you are signed into the correct legal entity. The entity name is shown in the top-right corner of the screen. |
| 3. *Click* **Modules**. | From the left-hand navigation pane, *click* **Modules** to display the full list of available modules in Finance and Operations. |
| 4. *Navigate* to the **Process Customer Settlements** page. | From the Navigation Pane, select:<br>5. **Treasury** **Automation** **Suite** ><br>6. **Periodic** ><br>7. **Payment** **remit** **automation** ><br>8. **Process** **customer** **settlements**<br>The Process customer settlements page is displayed. |
| 9. *Apply* **Filters.** | Review or update the filter fields to refine the transactions displayed.; |
| 10. *Click* **Apply filters.** | *Click* the **Apply filters** tab whenever the filters criteria are changed e.g. when selecting a different bank statement or bank account. |
| 11. *Review I***mported transactions.** | In the **Imported** **transactions** section, review the list of transactions displayed.<br>Each row represents a bank transaction imported from the bank statement. |
| 12. *Review* **Key transaction** **details.** | For each transaction review:<br>13. Customer account<br>14. Statement account<br>15. Statement date<br>16. Note (Bank Narrative). |
| 17. *Review* the **Match** **color**. | Locate the Match color column, which displays colored indicators (Blue, Red and Yellow) |
| 18. *Identify* **Transactions requiring action***.* | Determine which transactions require manual processing:<br>19. **Red** – investigation required.<br>20. **Blue** – Review and allocation required.<br>Green and Yellow transactions do not require manual processing unless an exception is identified. |
| 21. *Begin* **Processing settlements.** | *Click* the first transaction in the **Imported** **transactions** list to begin processing.<br>Transactions should be processed from top to bottom to ensure all items are reviewed sequentially. |
| *STEP COMPLETE* | *Proceed to the relevant process based on the Match color.*<br>*Blue transactions – continue to* [2.1.2 Process Customer Settlements – Blue Status (Customer Identified, On Account)](#212-process-customer-settlements--blue-status-customer-identified-on-account)<br>*Re transactions – Continue to* [2.1.3 Process Customer Settlements – Red Status (Customer or Invoice Not Identified).](#213-process-customer-settlements--red-status-customer-or-invoice-not-identified) |

#### 2.1.2 Process Customer Settlements – Blue Status (Customer Identified, On Account)

##### Procedure

Complete these steps to Process Customer Settlement – Blue Status (On Account):

| **Action** | **Description** |
|---|---|
| *PROCESS START* | **Pre-requisites:**<br>1. *The transaction displays* **Blue** *match status*<br>2. *A customer account has been identified.*<br>3. *No invoice has been matched.* |
| 4. *Understand* **T****ransaction sequencing***.* | Transactions are processed sequentially in the **Imported transactions** list. After posting a transaction, the system automatically moves to the next transaction list. |
| 5. *Review* the **Selected** **transaction.** | From [2.1.1 Access Customer Settlements](#211-access-customer-settlements), a transaction is already selected.<br>Review the newly selected transaction before proceeding. |
| 6. *Confirm* the **Match** **status is Blue***.* | Check the **Match status** column for the selected transaction.<br>7. If **Match** **status** is **Blue**, continue with this process.<br>8. If **Match** **status** is **Red**, refer to [2.1.3 Process Customer Settlements – Red Status (Customer or Invoice Not Identified).](#213-process-customer-settlements--red-status-customer-or-invoice-not-identified)<br>9. If **Match status** is **Green** or **Yellow**, no manual processing is required. |
| 10. *Select* a **Blue** **transaction***.* | If the selected transaction is not **Blue**, *click* the transaction displaying **Blue** in the **Match** **status** column before continuing. |
| 11. *Click* **Settlement transactions**. | On the **Action** Toolbar, *click* **Settle transactions**.<br>The **Customer** **settlement** **details** screen is displayed showing the **Header** and **Proposed settlement** sections. |
| 12. *Review* **Header** **details**. | In the Header section, review:<br>13. Statement amount<br>14. Settlement amount<br>15. Difference<br>The **Difference** represents the remaining amount to allocate and must equal **0.00** before posting. |
| 16. *Review* **Bank** **narrative.** | *Scroll* to the **Note** section and review the narrative to understand payment details.<br>Use this information to confirm the customer and identify whether invoice allocation is possible. Look for:<br>17. Customer name or trading name.<br>18. Invoice numbers (may include formatting issues such as missing zeros, spaces or symbols).<br>19. Payment references or remittance details.<br>20. Indicators of multiple invoices or combined payments.<br>This step determines whether the payment can be matched to invoice(s) or should remain on account. |
| 21. *Review* the **Proposed** **settlement** line. | In the **Proposed** **settlement** section, review the system generated settlement line.<br>For Blue status:<br>22. The **Customer** **account** is populated<br>23. The payment is typically recorded on Account (no invoice selected).<br>Blue transactions typically contain a proposed customer only with no invoice allocation initially applied. |
| 24. *Identify* **Settlement scenario.** | Review how the system has applied the payment:<br>25. **On account only**: no invoice selected.<br>26. **Single invoice allocated**: one invoice matched.<br>27. **Multiple invoices allocated**: payments allocated across multiple invoice<br>28. **Partial allocation with remainder**: some invoices matched, remaining amount left On account. |
| 29. *Identify* **Combined or multi-invoice payments** | If the bank narrative indicates multiple invoices or a combine payment e.g. credit card batch payment:<br>30. Refer to the bank payment batch file stored externally, OR<br>31. Refer to the relevant payment platform for breakdown. |
| 32. *Adjust* **Settlement lines (if required).** | If a valid invoice reference is clearly identified from the bank narrative:<br>33. In the **Invoice** field, *click* the **dropdown arrow** and select the relevant invoice.<br>34. *Click* **+New** to add additional settlement lines if required.<br>35. *Update* the **Amount** field to distribute the payment across invoices. |
| 36. Review the **Header** section. | *Confirm* the **Statement amount** equals the **Settled amount**, and the **Difference** field shows **0.00**.<br>If not, adjust settlement lines until balanced. |
| 37. *Click* **Post.** | On the **Action** toolbar, *click* **Post**.<br>The system generates a **Voucher number** confirming the transaction has been posted. |
| 38. *Continue* **Processing.** | The system automatically moves to the next transaction in the **Imported transactions** list. |
| *PROCESS COMPLETE* | **Outcomes***:*<br>39. *Customer payment is validated and processed.*<br>40. *Payment is correctly allocated or recorded On account.*<br>41. *Difference = 0.00*<br>42. *Transaction is posted with a Voucher number.* |

#### 2.1.3 Process Customer Settlements – Red Status (Customer or Invoice Not Identified)

##### Procedure

Complete these steps to Process Customer Settlement – Red Status (Customer or Invoice Not Identified): `[G220-07]`

| **Action** | **Description** |
|---|---|
| *PROCESS START* | **Pre-requisites***:*<br>1. *The transaction displays as Red match status.*<br>2. *Bank statement has been imported into D365.*<br>3. *Bank statement transaction is available in Process customer settlements.* |
| 4. *Understand* **T****ransaction sequencing***.* | Transactions are processed sequentially in the **Imported transactions** list. After posting a transaction, the system automatically moves to the next transaction list. |
| 5. *Review* the **Selected** **transaction.** | From [2.1.1 Access Customer Settlements](#211-access-customer-settlements), a transaction is already selected in the **Imported transactions** list. Review the newly selected transaction before proceeding |
| 6. *Confirm* **Match status is Red.** | Check the Match status column for the selected transaction.<br>7. If the **Match** **color** is **Red**, continue with this process.<br>8. If the **Match** **color** is **Blue**, refer to [2.1.2 Process Customer Settlements – Blue Status (Customer Identified, On Account)](#212-process-customer-settlements--blue-status-customer-identified-on-account)<br>9. If Green or Yellow, no manual processing is required. |
| 10. *Select* a **Red transaction.** | If the selected transaction is not **Red**, *click* a transaction displaying **Red** in the **Match status** column before continuing. |
| 11. *Confirm* **No journal exists.** | *Scroll* to the **Voucher number** column and confirm it is blank, indicating no payment journal has been created. |
| 12. *Click* **Settlement transactions**. | On the **Action** toolbar, *click* **Settle transactions**.<br>The Customer settlement details screen is displayed showing the **Header** section and **Proposed** **settlement** section. |
| 13. *Review* **Header** details**.** | At the top of the screen, *review* the **Header** values:<br>14. Statement amount<br>15. Settlement amount<br>16. Difference.<br>Confirm the **Statement** **amount** reflects the **Bank** **transaction** **value** and the **Difference** represents the amount remaining to be allocated. This value must equal **0.00** before posting. |
| 17. *Go* to **Note** section**.** | *Scroll* to and *expand* the **Note** section to review the Bank narrative. |
| 18. *Review* the **Bank narrative.** | Review the full bank reference. Use this information to determine how the payment should be applied.<br>Look for:<br>19. Customer name or trading name.<br>20. Invoice numbers (may include formatting issues such as missing zeros, spaces or symbols).<br>21. Payment references or remittance details.<br>22. Indicators of multiple invoices or combined payments.<br>This step determines whether the payment can be matched to invoice(s) or should remain on account. |
| 23. *Determine* if the **Payment can be identified**. | Can the payment be identified: |
| 24. *Go* to **Proposed** **settlement** section*.* | *Scroll* to the **Proposed** **settlement** section. This is where the customer and invoice allocation is entered. |
| 25. *Create* a **Settlement** **line**. | *Click* +**New** on the Toolbar to create a new settlement line. |
| 26. *Confirm* **Account type.** | Ensure the account type is *set* to **Customer**. |
| 27. *Search* for the **Customer** **account**. | In the **Customer** **account** field, **use** the **dropdown** to search for the customer or *enter* values from the narrative (full or partial name, trading name or reference). |
| 28. *Go to* **Customer account** (if mismatch suspected). | If a possible customer is identified but did not auto match.<br>*Right click* the **current D365 tab** on the browser and *click* **Duplicate** in the menu to open a second D365 session while keeping the settlement screen open. |
| 29. *Navigate* to **All** **customers.** | In the duplicated session, from the Navigation pane, *select*:<br>30. **Modules** ><br>31. **Accounts** **receivable** ><br>32. **Customers** ><br>33. **All** **customers**.<br>The All customers page will display. |
| 34. *Enter* **Search** **criteria** | In the **Search** field, *enter* the **customer name, trading name**, or **partial wording** from the bank narrative. |
| 35. *Open* the **Customer** **Record.** | *Review* the list of customers displayed and *click* the relevant **Customer account number** to open the customer record. |
| 36. *Expand* the **General FastTab** | *Click* the **General FastTab** to display additional fields. |
| 37. *Locate* the **Search name** field | Go to the **Search name** (Alternate name) field within the **General FastTab**. |
| 38. *Escalate* if the **Customer** **account cannot be identified**. | If no customer can be confidently identified, stop processing and refer the transactions to the **Collections** team. |
| 39. *Compare* the **Search name** to the narrative. | Compare the **Search name** (Alternate name) value in the wording used in the bank statement narrative.<br>This field supports automated settlement matching when customers use trading names or abbreviations when making payments. |
| 40. OPTIONAL:<br>*Update* the **Search name** if required. | If the bank statement consistently uses a variation of the customer name, *click* **Edit** and update the **Search name** (Alternate name) field so the wording aligns with the bank narrative. |
| 41. *Click* **Save** | *Click* **Save** to apply the updates. This improves automated matching for future customer payments. |
| 42. *Navigate to* **Customer eBanking details** (if required). | Determine if the issue relates to Customer matching e.g. customer not found or incorrect name in the bank narrative.<br>Navigate to:<br>43. **Treasury Automation Suite** ><br>44. **Common** ><br>45. **Customer eBanking details**<br>The customer eBanking details page is displayed. |
| 46. *Search* using **bank** **narrative** **values***.* | In the **Search** field, begin *typing* a value from the bank narrative e.g. customer name, trading name or reference.<br>As you type, a dropdown list appears showing available search options:<br>47. Customer company (customer name)<br>48. Invoice account (customer account number)<br>49. Alternate customer name (stored matching reference)<br>Select the most relevant option based on the narrative. |
| 50. *Refine* the **Search** **selection***.* | If the bank narrative contains: |
| 51. *Review* **Search results.** | *Review* the records returned in the grid. Identify potential matches based on the selected search criteria.<br>If no results are returned, try an alternate search option e.g. switch from Customer company to Alternate customer name. |
| 52. *Compare* **eBanking reference to narrative.** | *Select* a **record** and *compare* the stored **Alternate customer name** to the bank narrative. Confirm that the spelling, spacing, abbreviations and numeric values align exactly with the bank statement wording. |
| 53. *Escalate* **eBanking reference updates** if required. | If the bank statement references suggest the customer eBanking reference requires updating, do not update the record.<br>**Important**: Notify the **Collections** team and provide the bank narrative details so the customer eBanking reference can be updated. |
| 54. *Return* to **Process customer settlements** page. | *Return* to **Process customer settlements** page and the transaction requiring review. |
| 55. *Select* the **Customer account** | In the **Propose** **settlement** section, *click* **Customer** **account** field and *select* the correct Customer account. |
| 56. *Click* **Tax invoice field.** | *Click* the **arrow** in the **Tax** **invoice** field to display any open invoices for the customer account. |
| 57. *Check* for a **Tax** **invoice** **reference**. | *Review* the **open invoice list** displayed in the lower grid. If the narrative includes an invoice number, *select* the relevant invoice in the list. |
| 58. *Allocate* the **Tax invoice.** | In the new line, *select* the **Tax invoice** from the dropdown list. The invoice balance will populate automatically. |
| 59. *Enter* the **Settlement amount.** | In the **Transaction amount** fields, *enter* the **payment amount** to be applied to the invoice.<br>Confirm the invoice balance updates. |
| 60. *Handle* **Payment Differences**. | Review the payment and invoice amounts to determine how the payment should be allocated or managed before settlement. |
| 61. *Validate* the **Difference**. | Scroll to the Header section at the top of the settlement form, *confirm* the **Difference** field equals 0.00 before posting<br>If it does not, review the settlement lines and adjust amounts until it balances. |
| 62. *Click* **Post**. | *Click* **Post** to create the customer payment journal and generate a Voucher number. The red status updates confirming the payment has been processed.<br>Note: The screen will automatically display the next transaction. |
| *PROCESS COMPLETE* | **Outcomes***:*<br>63. *Customer payment transaction has been investigated and reviewed.*<br>64. *Payment is allocated, posted On account, or escalated to Collections where required.*<br>65. *Settlement difference equals 0.00 before posting where settlement is completed.* |

#### 2.2 Record and Settle a Manual Payment Journal

##### Description

The **Create a Manual Payment Journal** process is used to record and allocate customer payments in D365 when the automated bank import and settlement process cannot be used.

This includes situations where:

- The payment has not been imported from the bank statement e.g. cheque, delayed file or import failure.
- A backdated entry or adjustment is required outside the automated settlement process.
- Batch payments across parent-child accounts cannot be processed through automated settlement process.
- Payments spanning multiple customer accounts and cannot be allocated automatically.
- An intercompany transfer requires manual processing.

This topic ensures customer balances, invoice settlement and ledger postings remain accurate when automation cannot fully complete the transaction.

##### Responsibility

The Collections Officer is responsible for manually creating customer payment journals when they cannot be processed automatically.

##### Initiation

This process is initiated when a customer payment cannot be processed through the automated settlement process.

> **Note:** Moving a posted payment between customer accounts and distributing a parent account payment are in [3 Correct Customer Payments](#3-correct-customer-payments) (3.3 and 3.4). Intercompany payments are in [5 Process Intercompany Customer Payments](#5-process-intercompany-customer-payments).

##### Topic Overview

This topic includes these steps:

| Step | Description |
|---|---|
| [Create a Customer Payment Journal](#221-create-a-customer-payment-journal) | Record the payment in a new customer payment journal. |
| [Settle the Customer Payment Journal](#222-settle-the-customer-payment-journal) | Settle the journal line against the invoices it pays, then validate and post the journal. |

#### 2.2.1 Create a Customer Payment Journal

##### Procedure

Complete these steps to Create a Customer Payment Journal: `[G220-08]`

| **Action** | **Description** |
|---|---|
| *PROCESS START* | **Pre-requisites:**<br>1. *The payment cannot be processed via Process customer settlements*<br>2. *Remittance has been received from a customer.* |
| 3. Check the **Entity**. | Confirm that you are signed into the correct legal entity. The entity name is shown in the top-right corner of the screen. |
| 4. *Click* **Modules**. | From the left-hand navigation pane, *click* Modules to display the full list of available modules in Finance and Operations. |
| 5. Navigate to the **Customer Payment Journals** page. | From the Navigation Pane, select:<br>6. **Accounts Receivable** ><br>7. **Payments** ><br>8. **Customer payment journals**.<br>The Customer Payment Journal page is displayed, showing all existing journal in the system. |
| 9. Click **+New**. | On the Main Toolbar, *click* **+New**. A new journal line is created, and the Journal batch number is automatically generated. |
| 10. *Enter* **Journal** **Header details**. | Complete the required fields:<br>Note: The journal name controls posting behavior and approval workflow. Always select the journal name that aligns to the transaction type. |
| 11. *Click* the **Journal Batch Number**. | *Click* the **Journal Batch Number** to open the Customer payments form. |
| 12. Enter **Customer payment details.** | In the journal lines, enter the following details. |
| 13. *Validate* the **Journal**. | On the Main Toolbar, *click* **Validate** > **Simulate** posting to verify that all lines are error-free. |
| 14. *Determine* if **Approval** is required. | Some journals can be posted directly by a user, while others require approval by an Approver before posting. |
| 15. *Check* **Approval** **status**. | To confirm the journal has been approved, open the relevant journal batch number and review the Approval options on the Main Toolbar.<br>Alternatively, verify approval through the Teams message response from the approver before proceeding to post the journal. |
| 16. *Post* the **Journal***.* | Once approval has been obtained, *click* **Post** on the Main Toolbar to process the posting.<br>A system message is displayed confirming that the posting was successful. |
| *STEP COMPLETE* | **Outcomes***:*<br>17. *Customer payment journal is created and posted.*<br>18. *Proceed onto* [2.2.2 Settle the Customer Payment Journal](#222-settle-the-customer-payment-journal) |

#### 2.2.2 Settle the Customer Payment Journal

##### Procedure

Complete these steps to Settle Customer Payment Journal: `[G220-09]`

| **Action** | **Description** |
|---|---|
| *PROCESS START* | **Pre-requisites:**<br>1. *The payment journal has been created for the customer payment.*<br>2. *Customer remittance or payment reference details are available to identify the correct invoice(s).*<br>3. *The payment cannot be processed through Process customer settlements.* |
| 4. *Select* the **Payment line.** | In the **Customer payments** screen, *click* the checkbox to the left of the required payment line to highlight it. |
| 5. *Open* **Settle transactions.** | On the **Action** pane, *click* **Settle transactions** to open the Settle transactions form, which displays all open invoices for the selected customer in the upper grid. |
| 6. *Review* the **Open invoice list**. | *Review* the available **Tax invoice** records to identify the invoice that matches the remittance or bank narrative. |
| 7. *Confirm* the **Correct invoice before marking.** | *Click* the **Invoice row** once to highlight it.<br>In the **Line details** section, confirm supporting information such as Tax invoice date, Company, Voucher, and Description match the invoice you intend to settle. |
| 8. *Mark* the **Invoice for settlement**. | In the upper grid, c*lick* the **checkbox** in the **Mark** column for the selected invoice. The system flags the invoice as selected for settlement and uses the invoice balance as the default allocation amount. |
| 9. *Click* **Fully settle** if required. | If the payment is intended to clear the invoice completely, *click* **Fully** **settle** checkbox for the same invoice line.<br>This confirms the full outstanding balance will be settled when the journal is posted. |
| 10. *Check* the **Totals** **balance**. | In the **Totals** section at the bottom, *review* the **Payment amount** and **Settlement** balance.<br>These fields confirm whether the selected invoice allocation fully matches the payment line. |
| 11. *Confirm* the **Settlement** **balance.** | Check that the **Settlement** **balance** displays **0.00**. This confirms the marked invoice(s) have been allocated correctly and payment amount is fully applied. |
| 12. *Confirm* **Payment** **currency**. | Check that the **Accounting** and **Payment** **currency** values in the **Totals** section match the invoice currency shown.<br>If currencies differ, stop and escalate before proceeding. |
| 13. *Click* **OK** to confirm settlement. | *Click* **OK** to save the settlement selection and return to the journal screen with the invoice now linked for settlement., |
| 14. *Repeat* as required | Repeat the settlement steps for any remaining payment lines until all receipts are matched to the corresponding invoices. |
| 15. *Save* the **Journal** | On the Main Toolbar, *click* **Save** to record all settlements in the journal before proceeding to validate and post. |
| 16. *Validate* the **Journal**. | On the Main Toolbar, *click* **Validate** > **Simulate posting** to verify that all lines are error free.<br>Note: If errors appear, review the message log, correct the issues, and simulate again until successful. |
| 17. *Submit* for **Approval** (if required). | Once validated, on the Main Toolbar, *select* **Approval** > **Report** **as** **ready**. The journal is marked as ready for review by the approver. |
| 18. *Notify* the **Approver** | Send a Teams message to the approver requesting them to review and approve the customer payment journal. |
| 19. *Check* **Approval** **status**. | To confirm the journal has been approved, open the relevant journal batch number and review the Approval options on the Main Toolbar.<br>Alternatively, verify approval through the Teams message response form the approver before proceeding to post the journal. |
| 20. *Click* **Post** to finalize the journal. | Once approval has been obtained, *click* **Post** on the Main Toolbar to process the posting.<br>A system message is displayed confirming that the posting was successful. |
| *PROCESS COMPLETE* | **Outcomes***:*<br>21. *Customer payment is settled against the correct customer invoice(s).*<br>22. *Settlement balance equals 0.00 before posting.*<br>23. *Customer payment journal is validated, approved and posted successfully to the General Ledger.* |

#### 2.3 Settle Open Customer Transactions

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

### 3. Correct Customer Payments

##### Description

Use these topics when a customer payment or settlement must be corrected after it is posted: undo a settlement, reverse a customer payment journal, move funds to another customer account, distribute a parent account payment, restore a written-off or overpayment amount, or write off a small residual. Topics 3.3 to 3.5 use a customer payment journal (CPJL): the controls that apply to every CPJL entry are in Part 1 Key concepts. Writing off an uncollectible debt is a different task, in 230 Collections.

Until they are confirmed, these are outside the scope of this topic: a payment already settled against invoices on the wrong account, how to identify a parent-child relationship in D365, and when a write-off should be reversed or cancelled instead of restored. `[RO-02 / CPJ-17 / CPJ-19, PC-01 / CPJ-17 / CPJ-19, CPJ-17 / CPJ-19 / TF-05 / TF-06]`

Topics 3.3 to 3.5 and the journal controls in Part 1 come from AI-generated notes of the AR Training D365 Part 2 session and have not been checked against the recording. Topics 2.3, 3.1 and 3.6 come from the legacy 230 Collections PG (v2.3, sections 6.5, 6.6 and 6.8), which is about a year old, and have not been checked against current D365. Do not use these topics on live customer accounts until their blocking items are closed. `[G220-10]`

##### Responsibility

- Collections Officer: corrects customer payments and settlements.

##### Initiation

- A settlement was made in error, or against the wrong invoices.
- A posted customer payment journal is wrong.
- A payment was posted to the wrong customer account, or funds must move between related customer accounts.
- A payment held on a parent customer account must be distributed to confirmed child accounts.
- An overpayment or a written-off amount must be put back on a customer account.
- A small residual balance remains on a customer transaction, such as a bank fee, a foreign exchange difference, or a minor over or short payment.

##### Topic Overview

This topic includes these steps:

| Step | Description |
|---|---|
| [Undo a Settlement](#31-undo-a-settlement) | Reverse a settlement made in error or against the wrong invoices. |
| [Reverse a Customer Payment Journal](#32-reverse-a-customer-payment-journal) | Reverse a posted customer payment journal and reopen the invoices it settled. |
| [Transfer Funds Between Customer Accounts](#33-transfer-funds-between-customer-accounts) | Move a payment to the correct customer account, or between related accounts, with a CPJL. |
| [Distribute a Parent Account Payment Across Child Accounts](#34-distribute-a-parent-account-payment-across-child-accounts) | Distribute a payment held on a parent account to confirmed child accounts. |
| [Restore a Written-Off or Overpayment Amount](#35-restore-a-written-off-or-overpayment-amount) | Put an overpayment or a written-off amount back on a customer account. |
| [Write Off a Bank Fee or Small Residual](#36-write-off-a-bank-fee-or-small-residual) | Clear a small residual, such as a bank fee, with a reason code. |

#### 3.1 Undo a Settlement

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
| 11. *Confirm* the transactions are open. | Set **Show** to **Open** and check that the payment and the invoices are listed. Settle them correctly with [Settle Customer Transactions](#23-settle-open-customer-transactions). |
| *PROCESS COMPLETE* (light green) | *Outcomes:*<br>• The incorrect settlement is reversed.<br>• The payment and the invoices are open and can be settled again. |

#### 3.2 Reverse a Customer Payment Journal

##### Description

Use this procedure to reverse a posted customer payment journal: to correct an error, reopen the invoices it settled, and keep the financial and audit records accurate.

##### Responsibility

- Collections Officer: reverses customer payment journals posted in error.

##### Initiation

- A posted customer payment journal is wrong and must be reversed.

##### Procedure

Complete these steps to Reverse a Customer Payment Journal:

| **Action** | **Description** |
|---|---|
| *PROCESS START* | **Pre-requisites:**<br>1. *Customer payment journal has been posted in D365.*<br>2. *The customer payment transaction has been identified and confirmed for reversal.*<br>3. *reversal approval has been obtained in line with business and financial control requirements.* |
| 4. Check the **Entity**. | Confirm that you are signed into the correct legal entity. The entity name is shown in the top-right corner of the screen. |
| 5. *Click* **Modules**. | From the left-hand navigation pane, *click* Modules to display the full list of available modules in Finance and Operations. |
| 6. *Navigate* to the **Customer Payment Journals** page. | From the Navigation Pane, select:<br>7. **Accounts** **Receivable** ><br>8. **Payments** ><br>9. **Customer** **payment** **journals**.<br>The Customer Payment Journal page is displayed, showing all existing journal in the system. |
| 10. *Locate* the **Specific** **payment** **journal**. | Use available filtering options to find the required customer payment journal:<br>*Review* the filtered results list, then *click* the required **Journal batch number** to open the journal for review. |
| 11. Open **Voucher details.** | In the journal lines, *click* to the left of the required payment line to select it, then *click* **Voucher** on the Action bar.<br>The Voucher transactions page opens, displaying all related voucher entries for the selected payment. |
| 12. *Click* **Reverse transactions**. | On the Main Toolbar, *click* **Reverse** transactions to open the Reverse transactions pane. |
| 13. Enter **Reversal details**. | Complete the following fields: |
| 14. *Reverse* the **Transaction**. | *Click* **Reverse** to process the reversal.<br>The system displays a message and once completed the Transaction reversal results page opens confirming the transaction has been successfully reversed. |
| 15. *Return* to the **Journal** | *Click* the **Back arrow twice** to return first to the **Voucher** **transactions** page, then to the **Customer payments** page. |
| 16. *Click* **Post** to finalize the reversal | Back in the Customer Payment journal page, on the Main Toolbar, *click* **Post** to finalize the reversal.<br>A system message will display confirming that the payment has been cancelled for the voucher number. |
| *PROCESS COMPLETE* | **Outcomes***:*<br>17. *The selected customer payment transaction is reversed successfully.*<br>18. *Reversing entries are created and posted against the original voucher transaction.*<br>19. *Customer account balances and related Accounts Receivable records are updated to reflect the reversal.* |

#### 3.3 Transfer Funds Between Customer Accounts

##### Description

Use this topic to move funds from one customer account to another. You create a CPJL journal, enter a debit line for the source customer and a credit line for the destination customer, check that the journal balances, run Simulate Posting and post.

##### Responsibility

- Collections Officer: prepares and posts the transfer journal.

##### Initiation

- A payment was posted to the wrong customer account, or funds must move to a confirmed related account.

##### Topic Overview

This topic includes these steps:

| Step | Description |
|---|---|
| [Create the Journal and Enter the Source Line](#331-create-the-journal-and-enter-the-source-line) | Create the CPJL and enter the debit line for the customer the funds come from. Output: the source line is complete. |
| [Enter the Destination Line](#332-enter-the-destination-line) | Enter the matching credit line for the customer receiving the funds. Output: a two-line journal. |
| [Validate and Post the Journal](#333-validate-and-post-the-journal) | Check the balance, run Simulate Posting, correct errors and post. Output: the transfer is posted. |

#### 3.3.1 Create the Journal and Enter the Source Line

##### Procedure

Complete these steps to create the journal and enter the source line:

| **Action** | **Description** |
|---|---|
| *PROCESS START* (light blue) | *Pre-requisites:*<br>• Access to D365 and to **Customer payment journal**. `[CPJ-21]`<br>• The source and destination customer accounts, the amount and the currency of the original payment.<br>• Confirmation that the destination account is correct.<br>• Whether the payment is already settled on the source account. `[TF-05]`<br>*Responsibility:*<br>• Collections Officer |
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
| *STEP COMPLETE* (light blue) | • The source line is complete.<br>• Continue to [Enter the Destination Line](#332-enter-the-destination-line) |

#### 3.3.2 Enter the Destination Line

##### Procedure

Complete these steps to enter the destination line:

| **Action** | **Description** |
|---|---|
| *PROCESS START* (light blue) | *Pre-requisites:*<br>• The source line is complete (see [Create the Journal and Enter the Source Line](#331-create-the-journal-and-enter-the-source-line)).<br>*Responsibility:*<br>• Collections Officer |
| 1. *Add* a new line. `[CPJ-01 / CPJ-05]` | Add another line to the journal. |
| 2. *Select* the destination customer account. | Select the customer account receiving the funds. The customer name fills in automatically. |
| 3. *Enter* the amount as a credit. `[CPJ-06]` | Enter the same amount as the source line as a credit, in the same currency. |
| 4. *Enter* the line description. | Use the same description as the source line, so the transfer can be identified in both customers' histories. |
| 5. *Select* **Ledger** as the **Offset account type**. `[TF-04]` | Apply the same offset treatment as the source line. |
| 6. *Select* the bank-to-bank transfer clearing account. | Select the same clearing account as the source line. |
| 7. *Complete* the line. | Tab through every field in the line. |
| *STEP COMPLETE* (light blue) | • The journal has a source debit line and a matching destination credit line.<br>• Continue to [Validate and Post the Journal](#333-validate-and-post-the-journal) |

#### 3.3.3 Validate and Post the Journal

##### Procedure

Complete these steps to validate and post the journal:

| **Action** | **Description** |
|---|---|
| *PROCESS START* (light blue) | *Pre-requisites:*<br>• Both lines are complete (see [Enter the Destination Line](#332-enter-the-destination-line)).<br>*Responsibility:*<br>• Collections Officer |
| 1. *Check* the journal balances. `[CPJ-13]` | Confirm that total debits equal total credits, and that the currency and date are correct. |
| 2. *Run* **Simulate Posting**. `[CPJ-14]` | Check the journal before posting. A blue result means the journal is ready to post. |
| 3. *Correct* any errors. `[CPJ-15]` | If Simulate Posting shows an error, read it, correct the line it names and run Simulate Posting again. If you cannot resolve the error, log a request through the D365 issue form (see **Additional Resources**) before you post. |
| 4. *Post* the journal. `[CPJ-16 / CPJ-17]` | Post only when every line is complete, the journal balances and Simulate Posting succeeds. |
| 5. *Verify* the transfer. `[CPJ-18]` | Check that the transfer appears with its description on both customer accounts. |
| *PROCESS COMPLETE* (light green) | *Outcomes:*<br>• A balanced CPJL is posted: a debit on the source customer and a matching credit on the destination customer, with the bank-to-bank transfer clearing account as the offset. `[CPJ-19]`<br>• The transfer can be identified by its description in both customers' histories. |

#### 3.4 Distribute a Parent Account Payment Across Child Accounts

##### Description

Use this topic to distribute a payment from a parent customer account to confirmed child accounts. You create a CPJL journal, enter one debit line for the parent account and one credit line for each child account, check that the child credits match the parent debit, run Simulate Posting and post. If only part of the payment is allocated, you move only that part and record why the rest stays on the parent account.

##### Responsibility

- Collections Officer: prepares and posts the distribution journal.

##### Initiation

- A payment held on a parent customer account must be distributed to one or more confirmed child accounts.

##### Topic Overview

This topic includes these steps:

| Step | Description |
|---|---|
| [Create the Journal and Enter the Parent Line](#341-create-the-journal-and-enter-the-parent-line) | Create the CPJL and enter the debit for the amount being moved off the parent account. Output: the parent line is complete. |
| [Enter the Child Lines](#342-enter-the-child-lines) | Enter one credit line for each child account. Output: the distribution is entered. |
| [Validate and Post the Journal](#343-validate-and-post-the-journal) | Check the totals, run Simulate Posting, correct errors, post, and record any residual. Output: the distribution is posted. |

#### 3.4.1 Create the Journal and Enter the Parent Line

##### Procedure

Complete these steps to create the journal and enter the parent line:

| **Action** | **Description** |
|---|---|
| *PROCESS START* (light blue) | *Pre-requisites:*<br>• Access to D365 and to **Customer payment journal**. `[CPJ-21]`<br>• A confirmed parent-child relationship.<br>• A confirmed allocation: each child account, its amount, and the total to move.<br>• The currency of the original receipt.<br>*Responsibility:*<br>• Collections Officer |
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
| *STEP COMPLETE* (light blue) | • The parent line is complete.<br>• Continue to [Enter the Child Lines](#342-enter-the-child-lines) |

#### 3.4.2 Enter the Child Lines

##### Procedure

Complete these steps for each child account:

| **Action** | **Description** |
|---|---|
| *PROCESS START* (light blue) | *Pre-requisites:*<br>• The parent line is complete (see [Create the Journal and Enter the Parent Line](#341-create-the-journal-and-enter-the-parent-line)).<br>*Responsibility:*<br>• Collections Officer |
| 1. *Add* a new line. `[CPJ-01 / CPJ-05]` | Add another line to the journal. |
| 2. *Select* the child customer account. | Select a child account in the confirmed allocation. The customer name fills in automatically. |
| 3. *Enter* the child's amount as a credit. `[CPJ-06]` | Enter the amount allocated to this child account as a credit, in the same currency as the parent line. |
| 4. *Enter* the line description. | Use a description that identifies the transfer in this child account's history. |
| 5. *Select* **Ledger** as the **Offset account type**. `[PC-03]` | Apply the same offset treatment as the parent line. |
| 6. *Select* the bank-to-bank transfer clearing account. | Select the same clearing account as the parent line. |
| 7. *Complete* the line. | Tab through every field in the line. |
| 8. *Repeat* for each child account. | Repeat steps 1 to 7 until every child account in the confirmed allocation has a credit line. |
| *STEP COMPLETE* (light blue) | • Every child account in the allocation has a credit line.<br>• Continue to [Validate and Post the Journal](#343-validate-and-post-the-journal) |

#### 3.4.3 Validate and Post the Journal

##### Procedure

Complete these steps to validate and post the journal:

| **Action** | **Description** |
|---|---|
| *PROCESS START* (light blue) | *Pre-requisites:*<br>• The parent line and every child line are complete (see [Enter the Child Lines](#342-enter-the-child-lines)).<br>*Responsibility:*<br>• Collections Officer |
| 1. *Check* the distributed total. `[CPJ-13]` | Confirm that the child credits add up to the parent debit, and that the currency and date are correct. |
| 2. *Run* **Simulate Posting**. `[CPJ-14]` | Check the journal before posting. A blue result means the journal is ready to post. |
| 3. *Correct* any errors. `[CPJ-15]` | If Simulate Posting shows an error, read it, correct the line it names and run Simulate Posting again. If you cannot resolve the error, log a request through the D365 issue form (see **Additional Resources**) before you post. |
| 4. *Post* the journal. `[CPJ-16 / CPJ-17]` | Post only when every line is complete, the totals match and Simulate Posting succeeds. |
| 5. *Record* the purpose of any residual. `[PC-04]` | Optional. In a partial allocation, add a note that explains why the remaining amount stays on the parent account. Otherwise, go to step 6. |
| 6. *Verify* the distribution. `[CPJ-18]` | Check that the distribution appears with its description on the parent and child accounts. |
| *PROCESS COMPLETE* (light green) | *Outcomes:*<br>• A balanced CPJL is posted: a debit on the parent account and matching credits on the child accounts, with the bank-to-bank transfer clearing account as the offset. `[CPJ-19]`<br>• Any residual stays on the parent account with a note that explains its purpose. |

#### 3.5 Restore a Written-Off or Overpayment Amount

##### Description

Use this topic to put a written-off or overpayment amount back on a customer account. You create a CPJL journal with one credit line for the customer, offset to the Overpayment ledger, then run Simulate Posting and post.

##### Responsibility

- Collections Officer: prepares and posts the restoration journal.

##### Initiation

- An overpayment or a written-off amount must be put back on a customer account.

##### Topic Overview

This topic includes these steps:

| Step | Description |
|---|---|
| [Create the Restoration Line](#351-create-the-restoration-line) | Create the CPJL and enter the customer credit with the Overpayment ledger offset. Output: the line is complete. |
| [Validate and Post the Journal](#352-validate-and-post-the-journal) | Run Simulate Posting, correct errors and post. Output: the amount is back on the customer account. |

#### 3.5.1 Create the Restoration Line

##### Procedure

Complete these steps to create the restoration line:

| **Action** | **Description** |
|---|---|
| *PROCESS START* (light blue) | *Pre-requisites:*<br>• Access to D365 and to **Customer payment journal**. `[CPJ-21]`<br>• The customer account, amount and original currency.<br>*Responsibility:*<br>• Collections Officer |
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
| *STEP COMPLETE* (light blue) | • The restoration line is complete.<br>• Continue to [Validate and Post the Journal](#352-validate-and-post-the-journal) |

#### 3.5.2 Validate and Post the Journal

##### Procedure

Complete these steps to validate and post the journal:

| **Action** | **Description** |
|---|---|
| *PROCESS START* (light blue) | *Pre-requisites:*<br>• The restoration line is complete (see [Create the Restoration Line](#351-create-the-restoration-line)).<br>*Responsibility:*<br>• Collections Officer |
| 1. *Run* **Simulate Posting**. `[CPJ-14]` | Check the journal before posting. A blue result means the journal is ready to post. |
| 2. *Correct* any errors. `[CPJ-15]` | If Simulate Posting shows an error, read it, correct the line it names and run Simulate Posting again. If you cannot resolve the error, log a request through the D365 issue form (see **Additional Resources**) before you post. |
| 3. *Post* the journal. `[CPJ-16 / CPJ-17]` | Post only when the line is complete and Simulate Posting succeeds. |
| 4. *Verify* the restoration. `[CPJ-18]` | Check that the amount appears with its description on the customer account. |
| *PROCESS COMPLETE* (light green) | *Outcomes:*<br>• A CPJL is posted with a credit on the customer account and the Overpayment ledger as the offset. `[CPJ-19]`<br>• The entry can be identified by its description in the customer's history. |

#### 3.6 Write Off a Bank Fee or Small Residual

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

### 4. Maintain Settlement Configuration

##### Description

The process of Maintain Settlement Configuration ensures that D365 can correctly identify customers and automatically match payments to invoices by analyzing bank narrative, searching for customers and updating configuration where required.

This includes:

- Reviewing bank narrative and identifying matching issues.
- Searching for customers using available references.
- Creating or updating Alternate customer names.
- Maintaining settlement and Parse rules where recurring issues are identified.

Maintaining these settings improves automatic matching and reduces the number of truncations requiring manual investigation.

Matching occurs automatically when:

- A bank statement is imported via BankFabric.
- Remittance data is received via ExFlow
- Configured matching logic is successfully applied.

| **Matching behavior** | **Description** |
|---|---|
| Settlement rules | Control how payments are applied and invoices are selected. |
| Parse rules | Extract values such as invoice numbers, customer reference or structured date from the bank narrative. |
| Alternate customer names | Support matching where different customer references are used. |

##### Responsibility

The Collections Officer is responsible for reviewing recurring unmatched or partially matched transactions, identifying patterns in bank narrative failures, and updating alternate names or permitted configuration settings where applicable.

##### Initiation

This process is initiated when:

- Customer or invoice details are not identified from the bank narrative.
- Payments are not matched or are incorrectly applied during Process customer settlement.
- A recurring pattern is identified across multiple transactions.

##### Topic Overview

This topic includes these steps:

| Step | Description |
|---|---|
| [Maintain Customer Settlement Rules](#41-maintain-customer-settlement-rules) | Updates how D365 applies payments when transactions are allocated incorrectly or placed On Account. Improves settlement accuracy and reduces manual intervention. |
| [Maintain Customer Parse Rules](#42-maintain-customer-parse-rules) | Updates how D365 reads the bank narrative when customer or invoice details are not identified. Improved extraction and matching accuracy. |
| [Review Remittance Text Analysis Rules](#43-review-remittance-text-analysis-rules) | Analyses how D365 interprets bank narrative to identify why matching failed and determine the correct customer reference. |
| [Search for Customer using Alternate name](#44-search-for-customer-using-alternate-name) | Identifies customers using alternate names or references when the standard name is not recognized. |
| [Create or Update Customer Alternate Name](#45-create-or-update-customer-alternate-name) | Maintains alternate customer names to improve future matching and reduce repeat investigation. |

#### 4.1 Maintain Customer Settlement Rules

##### Procedure

Complete these steps to Maintain Customer Settlement Rules:

| **Action** | **Description** |
|---|---|
| *PROCESS START* | **Pre-requisites:**<br>1. *Recurring matching issues identified during process customer settlements.*<br>2. *Pattern observed in how payments are being incorrectly matched or processed.* |
| 3. *Confirm* **Matching** **issue.** | Identify a recurring issue during settlements e.g. overpayments going on account, incorrect invoice matching or customer identified but not allocated correctly. |
| 4. *Duplicate* the **D365** **screen**. | *Right-click* on the current **D365 browser tab** and *select* **Duplicate**.<br>This opens a new session, allowing the user to review remittance rules without losing the Process customer settlements screen. |
| 5. *Click* **Modules**. | From the left-hand navigation pane, *click* **Modules** to display the full list of available modules in Finance and Operations. |
| 6. Navigate to the **Settlement** **Rules** page. | From the Navigation Pane, select:<br>7. **Treasury Automation Suite** ><br>8. **Setup** ><br>9. **Settlement Rules.**<br>The Settlement Rules page is displayed. |
| 10. *Review* **Existing** **Rules.** | Review the existing rule list to determine whether a rule already exists for the bank narrative pattern or transaction type. |
| 11. *Review* **Rule behavior**. | Review how the rule is applying transactions, including invoice selection and handling of unmatched balances. |
| 12. OPTIONAL:<br>*Update* **Rule.** | Modify the rule where a consistent issue has been identified to align with expected settlement behavior. |
| 13. *Create* a **New** **rule.** | If an existing rule does not support the required behavior”<br>14. *Click* **+New**<br>15. Define the settlement logic e.g. how invoices should be selected or how balances should be treated.<br>16. Assign the rule to the appropriate rule group. |
| 17. *Click* **Save**. | *Click* **Save** to apply the updated or new rule. |
| *PROCESS COMPLETE* | **Outcomes***:*<br>18. *Settlement behavior aligns with expected processing.*<br>19. *Recurring allocation issues are reduced.*<br>20. *Transactions require less manual intervention.* |

#### 4.2 Maintain Customer Parse Rules

##### Procedure

Complete these steps to Maintain Customer Parse Rules:

| **Action** | **Description** |
|---|---|
| *PROCESS START* | **Pre-requisites:**<br>1. *Customer or invoice is not identified from the bank narrative.*<br>2. *Narrative pattern is consistent across multiple transactions.* |
| 3. *Confirm* **Matching** **issue.** | During settlement processing, identify transaction where the customer or invoice is not recognized from the bank narrative. |
| 4. *Review* the **Bank** **narrative.** | In the **Process** **customer** **settlements** screen, *review* the **Notes** field to understand how the payment reference is structured. |
| 5. *Copy* the **Narrative** **text**. | *Copy* the relevant portion of the narrative for analysis. |
| 6. *Click* **Modules**. | From the left-hand navigation pane, *click* **Modules** to display the full list of available modules in Finance and Operations. |
| 7. *Navigate* to the **Parse** **rules** page. | From the Navigation Pane, *select*:<br>8. **Treasury** **Automation** **Suite** ><br>9. **Setup** ><br>10. **Parse** **rules**.<br>The Parse rules page is displayed. |
| 11. *Locate* **Existing** **Rule.** | *Identify* a rule that relates to the narrative structure or pattern. |
| 12. *Review* **Parsing** **logic**. | *Review* how the rule extracts values e.g. invoice number, customer name or text pattern. |
| 13. OPTIONAL:<br>*Update* **Rule**. | *Adjust* the **parsing logic** to correctly extract values based on the narrative format. |
| 14. *Create* a **New** **rule**. | If an existing rule does not support the required format:<br>15. *Click* **+New**<br>16. Define the text pattern e.g. prefixes, suffixes or structure.<br>17. Specify how the value should be extracted e.g. customer or invoice reference. |
| 18. *Click* **Save**. | *Click* **Save** to apply the updated or new parse rule. |
| *PROCESS COMPLETE* | **Outcomes***:*<br>19. *Bank narrative is correctly interpreted.*<br>20. *Customer and invoice identification improves.*<br>21. *Automatic matching success increases.* |

#### 4.3 Review Remittance Text Analysis Rules

##### Procedure

Complete these steps to Review Remittance Text Analysis Rules:

| **Action** | **Description** |
|---|---|
| *PROCESS START* | **Pre-requisites:**<br>1. *A bank transaction with narrative / notes is available.*<br>2. *The transaction requires investigation.* |
| 3. *Copy* the **Narrative** **text**. | In the **Process** **customer** **settlements** screen, *review* the **Notes** field.<br>*Select* and *copy* the **full narrative text** from the **Notes** field. |
| 4. *Duplicate* the **D365** **screen**. | *Right-click* on the current **D365 browser tab** and *select* **Duplicate**.<br>This opens a new session, allowing the user to review remittance rules without losing the Process customer settlements screen. |
| 5. *Click* **Modules**. | In the duplicated session, from the left-hand navigation pane, *click* **Modules** to display the full list of available modules in Finance and Operations. |
| 6. *Navigate* to the **Remittance text analysis rule** page. | From the Navigation Pane, *select*:<br>7. **Treasury** **Automation** **Suite** ><br>8. **Setup** ><br>9. **Remittance text analysis rules.** |
| 10. *Select* the **Analysis** **context**. | In the **Remittance** **text** **analysis** **rules** screen, *select* **Customer** as the analysis type. |
| 11. *Paste* the **Narrative** for analysis. | *Paste* the copied **Narrative** **text** into the **Test** field. |
| 12. *Run* the **Analysis**. | Click **Analyze** to process the narrative. |
| 13. *Open* the **Message** **details**. | Review **Message** **details** to view the analysis results. |
| 14. *Review* **Substring** **matching** **results**. | Go to the **Substring** **matching** section to identify any **customer** **names**, **trading** **names** or **references** that match known customers. |
| 15. Identify the customer value**.** | Determine the most relevant customer wording to use for searching or creating an Alternate customer name. |
| 16. *Determine* the **Next** **action.** | Based on the analysis results: |
| *PROCESS COMPLETE* | **Outcomes***:*<br>17. *The bank narrative has been analyzed using remittance rules.*<br>18. *Customer related value is identified (where possible).*<br>19. *The appropriate next step is determined.* |

#### 4.4 Search for Customer using Alternate name

##### Procedure

Complete these steps to Search for Customer using Alternate Name:

| **Action** | **Description** |
|---|---|
| *PROCESS START* | **Pre-requisites:**<br>1. *A payment narrative or reference is available*<br>2. *Customer cannot be identified using the standard customer search.* |
| 3. *Click* **Modules**. | From the left-hand navigation pane, *click* **Modules** to display the full list of available modules in Finance and Operations. |
| 4. Navigate to the **Customer eBanking details** page. | From the Navigation Pane, *select*:<br>5. **Treasury** **Automation** **Suite** ><br>6. **Common** ><br>7. **Customer eBanking details.** |
| 8. *Search* using the **Alternate** **name.** | In the **Search** field, *paste* the **Customer name**.<br>Ensure the search option is set to **Invoice** **account** (not Customer account or alternate account) otherwise results may not return correctly. |
| 9. *Review* the **Search** **results.** | *Review* the results to identify a matching customer record.<br>*Confirm* the alternate name aligns with the narrative and represents the correct customer. |
| 10. *Identify* the **Customer** **account.** | From the matching record, *note* the **Customer** **account** linked to the alternate name search results. |
| 11. *Return* to the **Process Customer Settlements** screen. | Navigate to the **Process** **Customer** **settlements** screen. |
| 12. *Apply* the **Correct** **customer.** | *Update* or *confirm* the correct **Customer** **account** based on the alternate name search results. |
| *PROCESS COMPLETE* | **Outcomes***:*<br>13. *The correct customer account is identified using the alternate name.*<br>14. *The transaction can now be processed or investigated further.* |

#### 4.5 Create or Update Customer Alternate Name

##### Procedure

Complete these steps to Update Customer Alternate Name:

| **Action** | **Description** |
|---|---|
| *PROCESS START* | **Pre-requisites:**<br>1. *A payment narrative or reference is available*<br>2. *Customer cannot be identified using the alternate name search.* |
| 3. *Copy* the **Narrative** **text**. | In the **Process** **customer** **settlements** screen, *review* the **Notes** field.<br>*Select* and *copy* the **full narrative text** from the **Notes** field. |
| 4. *Duplicate* the **D365** **screen**. | *Right-click* on the current **D365 browser tab** and *select* **Duplicate**.<br>This opens a new session, allowing the user to review remittance rules without losing the Process customer settlements screen. |
| 5. *Click* **Modules**. | From the left-hand navigation pane, *click* Modules to display the full list of available modules in Finance and Operations. |
| 6. Navigate to the **Customer eBanking details** page. | From the Navigation Pane, *select*:<br>7. **Treasury** **Automation** **Suite** ><br>8. **Common** ><br>9. **Customer eBanking details.** |
| 10. *Search* using the **Alternate** **name.** | In the **Search** field, *paste* the narrative value.<br>Ensure the search option is set to Alternate customer name (not Customer account or invoice account). |
| 11. *Review* the **Search** **results.** | *Review* the results to identify a matching customer record.<br>*Confirm* the alternate name aligns with the narrative and represents the correct customer. |
| 12. *Create* **New** **alternate** **name.** | On the Main Toolbar, *click* **+New** to create a new eBanking record. |
| 13. *Select* **Legal** **entity**. | In the **Company** / **Legal** entity field, *select* the relevant entity e.g. 115A. |
| 14. *Enter* the **Customer** **account** | In the **Customer** **account** field, *select* the correct customer account. |
| 15. *Enter* the **Alternate** **customer** **name**. | In the **Alternate** **customer** **name** field, *enter* the wording exactly as identified from the narrative or analysis. |
| 16. OPTIONAL:<br>*Review* **Direct** **debit** options. | Ensure Direct debit options are only selected where required. If not applicable, leave it unticked. |
| 17. *Click* **Save**. | *Click* **Save** to store the alternate name for future automatic matching. |
| 18. *Return* to the **Process Customer Settlements** screen. | Navigate to the **Process** **Customer** **settlements** screen to continue processing. |
| *PROCESS COMPLETE* | **Outcomes***:*<br>19. *Alternate customer name is created or updated.*<br>20. *Future transactions can be matched automatically.*<br>21. *Current transaction can proceed without rework.* |

### 5. Process Intercompany Customer Payments

##### Description

Use this topic when a customer pays into the bank account of one legal entity for an invoice held in another, for example a payment into the bank account of 101a for an invoice in 238a. Receipting Officers process these intercompany (ICO) payments.

##### Responsibility

- Receipting Officer: processes intercompany customer payments.

##### Initiation

- A customer payment arrives in the bank account of a legal entity other than the one that holds the invoice.

##### Procedure

> **Being worked on.** The steps come from Maria Pabalan's session with Amy on Friday 6 November 2026. This topic will be updated; until then, ask a Receipting Officer or Maria Pabalan. `[G220-11]`

### 6. Process Direct Debit Customer Payments

##### Description

Direct debit customer payments are processed in **240 Direct Debit and Credit Card Payments**, topic 2 Process a Direct Debit Run. It replaces section 5 of version 2.1 (D-053). This topic stays here as the way in from Customer Payments.

##### Responsibility

- See 240 Direct Debit and Credit Card Payments.

---

## Part 3: Reports (Customer Payments)

##### Page Overview

This page contains various reports related to the Customer Payments module.

##### Open Transactions Reports

| **Navigation** | **Description** |
|---|---|
| 1. **Accounts Receivable > Inquiries and Reports > Open Transactions Report.** |   |

##### Transaction Report

| **Navigation** | **Description** |
|---|---|
| 1. **Accounts Receivable > Inquiries and Reports > Transactions Report.** |   |

##### Customer to Ledger Reconciliation Report

| **Navigation** | **Description** |
|---|---|
| 1. **Accounts Receivable > Enquiries and Reports > Customer > Customer to Ledger Reconciliation Report.** |   |

##### Customer Posted Payment Journal Report

| **Navigation** | **Description** |
|---|---|
| 1. **Accounts Receivable > Enquiries and Reports > Payments > Customer Posted Payment Journal Report.** |   |

##### Customer Base Data Report

| **Navigation** | **Description** |
|---|---|
| 1. **Accounts Receivable > Enquiries and Reports > Customers > Customer Base Data Report** | This report can be printed to meet the requirement for tax periodic review, and includes the specific Tax Group, WHT Tax Group, Address (Location) and other relevant data fields. Alternatively, the customer master form, can be personalized to include the fields that are required to conduct periodic tax reviews. This can then be easily exported to Excel. |

---

## Additional Resources

The standard template block, unchanged.
