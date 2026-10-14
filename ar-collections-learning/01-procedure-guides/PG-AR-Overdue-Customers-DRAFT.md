# D365 F&O: AR Collections Overdue Customers Procedure Guide

> **SME REVIEW DRAFT. Not validated or approved.**
>
> This is a Markdown preview of the Word guide [`TBC-AR Collections Overdue Customers PG v0.1.docx`](TBC-AR%20Collections%20Overdue%20Customers%20PG%20v0.1.docx). That guide was built from the PG master template in [`/templates`](../../templates/). **The Word file is the editable source.**
>
> `[VG-xx]` markers show unconfirmed items. In the Word file, each one is a review comment. Full details are in the [validation register](../03-validation/PG-AR-Overdue-Customers-Validation.md). The markers are not part of the guide text.

The fixed template content is not repeated here: cover, Contents, *About this guide* and *Additional Resources*.

**Version history**

| ID | Date | Author/s | BPO | Description of change |
|---|---|---|---|---|
| 0.1 | October 2026 | Daniel Moreira | To be confirmed `[VG-16]` | SME review draft created from the PG master template. Not validated or approved. |

Guide code and final title: `[VG-17]`.

---

## Part 1: What do I need to know? (AR Collections Overdue Customers)

### High-level process

##### Part Description

This guide explains how a Collections Officer reviews **Customers overdue** to find customers with overdue balances for an aging period, and then checks that a customer's overdue balance is valid before contacting them. Recording the contact, investigating the full customer account and the aging indicators are outside the scope of this guide.

##### Initiation

- A Collections Officer needs to identify which customers to contact about overdue balances. `[VG-14]`

##### Stream

| Stream | Process Area | Key Roles |
|---|---|---|
| Accounts Receivable `[VG-15]` | AR Collections | • Collections Officer |

##### Process

| # | Action | Who | When | Where |
|---|---|---|---|---|
| 1 | [Review Customers Overdue](#1-review-customers-overdue) | Collections Officer | When identifying customers to contact about overdue balances | D365 |
| 2 | [Check an Overdue Balance Before Contact](#2-check-an-overdue-balance-before-contact) | Collections Officer | Before contacting a customer about an overdue balance | D365 |

### Roles and responsibilities

##### Overview

The Collections Officer reviews overdue customers in their own D365 session.

| Tasks / Business Roles | Collections Officer |
|---|---|
| [Review Customers Overdue](#1-review-customers-overdue) | R |
| [Check an Overdue Balance Before Contact](#2-check-an-overdue-balance-before-contact) | R |

### Key concepts

##### Overview

Before you start, you need to know what Customers overdue shows, how aging periods and amounts work on the page, and the rule for checking a balance before contact.

##### Customers overdue

| Term | Description |
|---|---|
| **Customers overdue** | A page in the **Customer credit and collections** workspace that lists customers with overdue balances. `[VG-01]` |
| **Aging period** | The page shows overdue balances for the aging period you select, for example **90+** or **61-90** days. `[VG-02, VG-03]` |
| **Balance due and overdue amount** | The balance due is the customer's total outstanding balance. The overdue amount is the part that is past its due date. The two can differ. `[VG-04]` |

##### Before contacting a customer

| Rule | Description |
|---|---|
| **Check the balance first** | Investigate an overdue balance before you contact the customer. A low-value balance may represent fees or an overpayment rather than an unpaid invoice. `[VG-09]` |

---

## Part 2: How do I do it? (AR Collections Overdue Customers)

### 1. Review Customers Overdue

##### Description

Use this procedure to open **Customers overdue**, select an aging period and sort the list so the largest overdue amounts appear first.

##### Responsibility

- Collections Officer: identifies customers with overdue balances.

##### Initiation

- A Collections Officer needs to identify which customers to contact about overdue balances.

##### Procedure

Complete these steps to review customers overdue:

| Action | Description |
|---|---|
| *PROCESS START* (light blue) | *Pre-requisites:*<br>• Access to D365 and to the **Customer credit and collections** workspace.<br>*Responsibility:*<br>• Collections Officer |
| 1. *Check* the **Entity**. | Confirm you are signed into the correct **Legal Entity** (top-right). |
| 2. *Click* **Workspaces**. | From the **Navigation Pane**, click **Workspaces**, then select **Customer credit and collections**. |
| 3. *Click* **Customers overdue**. `[VG-01]` | In the workspace, click **Customers overdue**. |
| 4. *Select* the aging period. `[VG-02]` | Select the aging period you are working on, for example **90+**. |
| 5. *Sort* the overdue amount from largest to smallest. `[VG-05]` | Sort the overdue amount column in descending order so the largest overdue amounts appear first. |
| 6. *Add* the email address column. `[VG-06]` | Optional. Add the email column with **Insert columns** (see the AR Collections Personalized Views guide). Otherwise, go to step 7. |
| 7. *Review* the balance due and overdue amount. `[VG-04]` | Check the aging period, then compare each customer's balance due with the overdue amount, largest first. |
| *PROCESS COMPLETE* (light green) | *Outcomes:*<br>• **Customers overdue** shows the selected aging period, sorted from the largest overdue amount. |

### 2. Check an Overdue Balance Before Contact

##### Description

Use this procedure to check that a customer's overdue balance is valid before you contact the customer. You open the customer account from **Customers overdue**, review what makes up the overdue amount and check low-value balances for fees or overpayments.

##### Responsibility

- Collections Officer: confirms an overdue balance is valid before contact.

##### Initiation

- A Collections Officer is about to contact a customer about an overdue balance. `[VG-14]`

##### Procedure

Complete these steps to check an overdue balance:

| Action | Description |
|---|---|
| *PROCESS START* (light blue) | *Pre-requisites:*<br>• **Customers overdue** is open (see [Review Customers Overdue](#1-review-customers-overdue)).<br>*Responsibility:*<br>• Collections Officer |
| 1. *Select* the customer. | In **Customers overdue**, select the customer whose balance you are checking. |
| 2. *Open* the customer account. `[VG-07]` | Open the customer account from the list. |
| 3. *Review* the overdue balance. `[VG-08]` | Check which transactions make up the overdue amount. |
| 4. *Check* a low-value balance. | If the overdue amount is low, check whether it represents fees or an overpayment rather than an unpaid invoice. |
| 5. *Confirm* the balance is valid. `[VG-10]` | Contact the customer only when the overdue balance is valid. If it is not, do not contact the customer and investigate the balance first. |
| *PROCESS COMPLETE* (light green) | *Outcomes:*<br>• You have confirmed whether the overdue balance is valid before contacting the customer. |

---

## Part 3: Reports (AR Collections Overdue Customers)

##### Overview

Reports for this process are pending SME confirmation. `[VG-18]`

---

## Additional Resources

The standard template block, unchanged.
