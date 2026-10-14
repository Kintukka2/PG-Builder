# D365 F&O: AR Collections Aged Balances Procedure Guide

> **SME REVIEW DRAFT. Not validated or approved.**
>
> This is a Markdown preview of the Word guide [`TBC-AR Collections Aged Balances PG v0.1.docx`](TBC-AR%20Collections%20Aged%20Balances%20PG%20v0.1.docx). That guide was built from the PG master template in [`/templates`](../../templates/). **The Word file is the editable source.**
>
> `[VG-xx]` markers show unconfirmed items. In the Word file, each one is a review comment. Full details are in the [validation register](../03-validation/PG-AR-Aged-Balances-Validation.md). The markers are not part of the guide text.

The fixed template content is not repeated here: cover, Contents, *About this guide* and *Additional Resources*.

**Version history**

| ID | Date | Author/s | BPO | Description of change |
|---|---|---|---|---|
| 0.1 | October 2026 | Daniel Moreira | To be confirmed `[VG-16]` | SME review draft created from the PG master template. Not validated or approved. |

Guide code and final title: `[VG-17]`.

---

## Part 1: What do I need to know? (AR Collections Aged Balances)

### High-level process

##### Part Description

This guide explains how a Collections Officer uses the **Aged balances** page to see which customers have outstanding balances. It covers preparing the list so it shows only non-zero balances, largest first, with each account's currency, and then filtering the list to selected customers or currencies. Opening and investigating a customer account, and the aging indicators on the page, are outside the scope of this guide.

##### Initiation

- A Collections Officer needs to identify customers with outstanding balances before starting collection work. `[VG-14]`

##### Stream

| Stream | Process Area | Key Roles |
|---|---|---|
| Accounts Receivable `[VG-15]` | AR Collections | • Collections Officer |

##### Process

| # | Action | Who | When | Where |
|---|---|---|---|---|
| 1 | [Review Customer Aged Balances](#1-review-customer-aged-balances) | Collections Officer | Before starting collection work, to see which customers have outstanding balances | D365 |
| 2 | [Filter Aged Balances by Customer or Currency](#2-filter-aged-balances-by-customer-or-currency) | Collections Officer | When only selected customers or currencies need review | D365 |

### Roles and responsibilities

##### Overview

The Collections Officer reviews aged balances in their own D365 session.

| Tasks / Business Roles | Collections Officer |
|---|---|
| [Review Customer Aged Balances](#1-review-customer-aged-balances) | R |
| [Filter Aged Balances by Customer or Currency](#2-filter-aged-balances-by-customer-or-currency) | R |

### Key concepts

##### Overview

Before you start, you need to know what the Aged balances page shows, how its amounts relate to currency, and the rule for sharing balance information with customers.

##### The Aged balances page

| Term | Description |
|---|---|
| **Aged balances** | A page in the **Credit and collections** module that shows customer balances by aging period. `[VG-01]` |
| **Reporting currency** | The page can show amounts in the ledger's reporting currency, which can differ from the currency of the customer's transactions. Add the **Currency** column so each account's currency is visible. `[VG-09]` |
| **Zero balances** | Accounts with a zero balance are listed unless you filter them out. Filtering the balance column to **not equal to** **0** removes them. |

##### Sharing balances with customers

| Rule | Description |
|---|---|
| **Use PDF, not Excel** | Provide customer-facing account information as a PDF. Do not send a customer an Excel export of this page. `[VG-13]` |

---

## Part 2: How do I do it? (AR Collections Aged Balances)

### 1. Review Customer Aged Balances

##### Description

Use this procedure to open the **Aged balances** page and prepare the list for collection work. You add the **Currency** column, remove accounts with a zero balance and sort the balances from largest to smallest, so the customers with the highest outstanding balances appear first. You can save the prepared layout as a view by following the AR Collections Personalized Views guide.

##### Responsibility

- Collections Officer: reviews customer balances before collection work.

##### Initiation

- A Collections Officer needs to identify customers with outstanding balances before starting collection work.

##### Procedure

Complete these steps to prepare the aged balances list:

| Action | Description |
|---|---|
| *PROCESS START* (light blue) | *Pre-requisites:*<br>• Access to D365 and to the **Credit and collections** module.<br>*Responsibility:*<br>• Collections Officer |
| 1. *Check* the **Entity**. | Confirm you are signed into the correct **Legal Entity** (top-right). |
| 2. *Click* **Modules**. | From the left-hand **Navigation Pane**, click **Modules**. |
| 3. *Navigate* to the **Aged balances** page. `[VG-02]` | From the **Navigation Pane**, *select*:<br>• **Credit and collections >**<br>• **Aged balances**<br>If **Aged balances** is in your **Favorites** (see the AR Collections Favorites guide), you can open it from **Favorites** instead. |
| 4. *Click* **Insert columns**. `[VG-04, VG-12]` | Use **Insert columns** to add the **Currency** column if the grid does not already show it. |
| 5. *Select* the **Currency** column. | Select **Currency** in the list of columns. |
| 6. *Confirm* the **Currency** column is displayed. | Check that each account now shows its currency. |
| 7. *Open* the filter for the balance column. `[VG-03, VG-05]` | Open the filter for the balance column you are reviewing. |
| 8. *Select* **not equal to**. | Select the **not equal to** operator. |
| 9. *Enter* **0**. | Enter **0** as the filter value. |
| 10. *Apply* the filter. `[VG-05]` | Apply the filter. Accounts with a zero balance are no longer listed. |
| 11. *Sort* the balance column from largest to smallest. `[VG-06]` | Sort the balance column in descending order so the largest balances appear first. |
| 12. *Confirm* the list is ready to review. | Check that the list shows only non-zero balances, largest first, with each account's currency. |
| *PROCESS COMPLETE* (light green) | *Outcomes:*<br>• The **Aged balances** list shows only customers with a non-zero balance, sorted from largest to smallest.<br>• Each account shows its currency. |

### 2. Filter Aged Balances by Customer or Currency

##### Description

Use this procedure when you need the aged balances for selected customers or for one or more currencies. You filter the customer column to the accounts you need, or filter the **Currency** column, or both. Start from the list prepared in Review Customer Aged Balances.

##### Responsibility

- Collections Officer: narrows the aged balances list to the customers or currencies under review.

##### Initiation

- Only selected customers or currencies need review. `[VG-14]`

##### Procedure

Complete these steps to filter the aged balances list:

| Action | Description |
|---|---|
| *PROCESS START* (light blue) | *Pre-requisites:*<br>• The prepared aged balances list (see [Review Customer Aged Balances](#1-review-customer-aged-balances)).<br>*Responsibility:*<br>• Collections Officer |
| 1. *Open* the filter for the customer column. `[VG-07]` | To review selected customers, open the filter for the customer account column. If you only need a currency filter, go to step 5. |
| 2. *Select* **is one of**. `[VG-08]` | Select the **is one of** operator so you can choose several customers. |
| 3. *Select* each customer account. | Select each customer account you want to review. |
| 4. *Apply* the customer filter. | Apply the filter. Only the selected customers are listed. |
| 5. *Open* the filter for the **Currency** column. | To review one or more currencies, open the filter for the **Currency** column. If you don't need a currency filter, go to step 9. |
| 6. *Select* **is one of**. | Select the **is one of** operator so you can choose one or more currencies. |
| 7. *Select* each currency. | Select each currency you want to review. |
| 8. *Apply* the currency filter. | Apply the filter. Only accounts in the selected currencies are listed. |
| 9. *Confirm* the filtered list. | Check that the list shows only the customers or currencies you selected, largest balance first. |
| *PROCESS COMPLETE* (light green) | *Outcomes:*<br>• The **Aged balances** list shows only the selected customers or currencies, largest balance first. |

---

## Part 3: Reports (AR Collections Aged Balances)

##### Overview

Reports for this process are pending SME confirmation. `[VG-18]`

---

## Additional Resources

The standard template block, unchanged.
