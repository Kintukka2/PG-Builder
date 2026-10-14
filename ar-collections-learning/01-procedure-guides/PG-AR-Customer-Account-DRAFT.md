# D365 F&O: AR Collections Customer Account Procedure Guide

> **SME REVIEW DRAFT. Not validated or approved.**
>
> This is a Markdown preview of the Word guide [`TBC-AR Collections Customer Account PG v0.1.docx`](TBC-AR%20Collections%20Customer%20Account%20PG%20v0.1.docx). That guide was built from the PG master template in [`/templates`](../../templates/). **The Word file is the editable source.**
>
> `[VG-xx]` markers show unconfirmed items. In the Word file, each one is a review comment. Full details are in the [validation register](../03-validation/PG-AR-Customer-Account-Validation.md). The markers are not part of the guide text.

The fixed template content is not repeated here: cover, Contents, *About this guide* and *Additional Resources*.

**Version history**

| ID | Date | Author/s | BPO | Description of change |
|---|---|---|---|---|
| 0.1 | October 2026 | Daniel Moreira | To be confirmed `[VG-18]` | SME review draft created from the PG master template. Not validated or approved. |

Guide code and final title: `[VG-19]`.

---

## Part 1: What do I need to know? (AR Collections Customer Account)

### High-level process

##### Part Description

This guide explains how a Collections Officer investigates a customer account before contacting the customer. It covers opening the account and its balances, reviewing the customer's open and closed transactions, and reviewing the settlement history of a transaction. Changing or undoing a settlement is outside the scope of this guide.

##### Initiation

- A Collections Officer needs to understand a customer's account before contacting them. `[VG-16]`

##### Stream

| Stream | Process Area | Key Roles |
|---|---|---|
| Accounts Receivable `[VG-17]` | AR Collections | • Collections Officer |

##### Process

| # | Action | Who | When | Where |
|---|---|---|---|---|
| 1 | [Investigate a Customer Account](#1-investigate-a-customer-account) | Collections Officer | Before contacting a customer about their account | D365 |

### Roles and responsibilities

##### Overview

The Collections Officer investigates customer accounts in their own D365 session.

| Tasks / Business Roles | Collections Officer |
|---|---|
| [Investigate a Customer Account](#1-investigate-a-customer-account) | R |

### Key concepts

##### Overview

Before you start, you need to know how transactions and settlements appear on a customer account, and what this guide does not change.

##### Transactions and settlements

| Term | Description |
|---|---|
| **Open and closed transactions** | Open transactions still have an amount outstanding. Closed transactions have been fully settled. You can show either set on the customer's transactions. `[VG-06]` |
| **Currency revaluations** | Entries D365 creates when it revalues foreign currency balances. Hide them so the list shows only the customer's own transactions. `[VG-07, VG-08]` |
| **Settlement** | The matching of a payment or credit to the invoices it pays. A transaction's settlement history shows what it was settled against. `[VG-12]` |

##### Reviewing without changing

| Rule | Description |
|---|---|
| **Do not undo settlements here** | This guide only reviews settlement history. Undoing a settlement changes financial records and is covered by a separate guide once validated. `[VG-13]` |

---

## Part 2: How do I do it? (AR Collections Customer Account)

### 1. Investigate a Customer Account

##### Description

Use this topic to investigate a customer account before you contact the customer. You open the account and check its balances, review the customer's transactions and, where needed, review how a transaction was settled.

##### Responsibility

- Collections Officer: investigates the customer account before contact.

##### Initiation

- A Collections Officer needs to understand a customer's account before contacting them.

##### Topic Overview

This topic includes these steps:

| Step | Description |
|---|---|
| [Open the Customer Account](#11-open-the-customer-account) | Open the customer account and check the balance and overdue amount. Output: the account is open. |
| [Review Customer Transactions](#12-review-customer-transactions) | Review open and closed transactions without currency revaluations. Output: you know what makes up the balance. |
| [Review Settlement History](#13-review-settlement-history) | Optional. Review what a transaction was settled against. Output: you know how a payment or credit was applied. |

#### 1.1 Open the Customer Account

##### Procedure

Complete these steps to open the customer account:

| Action | Description |
|---|---|
| *PROCESS START* (light blue) | *Pre-requisites:*<br>• Access to D365 and to the **Credit and collections** module.<br>• The customer account number or name.<br>*Responsibility:*<br>• Collections Officer |
| 1. *Check* the **Entity**. | Confirm you are signed into the correct **Legal Entity** (top-right). |
| 2. *Click* **Modules**. | From the left-hand **Navigation Pane**, click **Modules**. |
| 3. *Navigate* to the **All customers** page. `[VG-01, VG-03]` | From the **Navigation Pane**, *select*:<br>• **Credit and collections >**<br>• **All customers**<br>You can also open **All customers** from your **Favorites** (see the AR Collections Favorites guide). |
| 4. *Open* the customer account. `[VG-02]` | Find the customer and open the account. |
| 5. *Review* the account balance. `[VG-04]` | Check the customer's balance and overdue amount. |
| *STEP COMPLETE* (light blue) | • *The customer account is open.*<br>• *Continue to [Review Customer Transactions](#12-review-customer-transactions)* |

#### 1.2 Review Customer Transactions

##### Procedure

Complete these steps to review the customer's transactions:

| Action | Description |
|---|---|
| *PROCESS START* (light blue) | *Pre-requisites:*<br>• The customer account is open (see [Open the Customer Account](#11-open-the-customer-account)).<br>*Responsibility:*<br>• Collections Officer |
| 1. *Click* **Transactions**. `[VG-05]` | Open the customer's transactions from the customer account. |
| 2. *Select* **Show open**. `[VG-06]` | Show only open transactions. |
| 3. *Hide* currency revaluations. `[VG-07]` | Hide currency revaluation entries so only the customer's own transactions are listed. |
| 4. *Review* the open transactions. `[VG-09]` | For each transaction, check the due date, amount, currency and description. |
| 5. *Select* **Show closed**. | Optional. To see settled transactions, show closed transactions. Otherwise, go to step 6. |
| 6. *Confirm* you know what makes up the balance. `[VG-15]` | Check that the transactions you reviewed explain the balance and overdue amount. |
| *STEP COMPLETE* (light blue) | • *You have reviewed the customer's transactions.*<br>• *Continue to [Review Settlement History](#13-review-settlement-history)* |

#### 1.3 Review Settlement History

##### Procedure

This subprocedure is optional. Complete it when you need to know what a payment, credit or invoice was settled against.

Complete these steps to review a transaction's settlement history:

| Action | Description |
|---|---|
| *PROCESS START* (light blue) | *Pre-requisites:*<br>• The customer's transactions are open (see [Review Customer Transactions](#12-review-customer-transactions)).<br>*Responsibility:*<br>• Collections Officer |
| 1. *Click* the transaction. `[VG-10]` | Click the transaction so it is highlighted. Do not mark it. |
| 2. *Click* **View settlements**. `[VG-11]` | Open the settlement history for the highlighted transaction. |
| 3. *Review* the settlement. `[VG-12]` | Check which transactions it was settled against, and the amounts and dates. |
| 4. *Close* the settlement history. | Close the page without changing the settlement. |
| 5. *Continue* the investigation. | If needed, review the customer's notes and activities (see the AR Collections Notes and Activities guide) or open an invoice (see the AR Collections Customer Invoices guide). |
| *PROCESS COMPLETE* (light green) | *Outcomes:*<br>• You have investigated the customer account and can contact the customer. |

---

## Part 3: Reports (AR Collections Customer Account)

##### Overview

Reports for this process are pending SME confirmation. `[VG-20]`

---

## Additional Resources

The standard template block, unchanged.
