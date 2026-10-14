# D365 F&O: AR Collections Customer Invoices Procedure Guide

> **SME REVIEW DRAFT. Not validated or approved.**
>
> This is a Markdown preview of the Word guide [`TBC-AR Collections Customer Invoices PG v0.1.docx`](TBC-AR%20Collections%20Customer%20Invoices%20PG%20v0.1.docx). That guide was built from the PG master template in [`/templates`](../../templates/). **The Word file is the editable source.**
>
> `[VG-xx]` markers show unconfirmed items. In the Word file, each one is a review comment. Full details are in the [validation register](../03-validation/PG-AR-Customer-Invoices-Validation.md). The markers are not part of the guide text.

The fixed template content is not repeated here: cover, Contents, *About this guide* and *Additional Resources*.

**Version history**

| ID | Date | Author/s | BPO | Description of change |
|---|---|---|---|---|
| 0.1 | October 2026 | Daniel Moreira | To be confirmed `[VG-15]` | SME review draft created from the PG master template. Not validated or approved. |

Guide code and final title: `[VG-16]`.

---

## Part 1: What do I need to know? (AR Collections Customer Invoices)

### High-level process

##### Part Description

This guide explains how a Collections Officer opens a customer invoice from the customer's transactions, reviews it in print preview and downloads it as a PDF. The invoice is reached through **Original document** and **Print preview** on the highlighted transaction. Finding transactions on the customer account, and sending the invoice to the customer, are outside the scope of this guide.

##### Initiation

- A customer or colleague needs a copy of an invoice, or the invoice must be reviewed before contacting the customer. `[VG-13]`

##### Stream

| Stream | Process Area | Key Roles |
|---|---|---|
| Accounts Receivable `[VG-14]` | AR Collections | • Collections Officer |

##### Process

| # | Action | Who | When | Where |
|---|---|---|---|---|
| 1 | [View and Download a Customer Invoice](#1-view-and-download-a-customer-invoice) | Collections Officer | When a copy of an invoice is needed, or an invoice must be reviewed before contacting the customer | D365 |

### Roles and responsibilities

##### Overview

The Collections Officer opens and downloads invoices in their own D365 session.

| Tasks / Business Roles | Collections Officer |
|---|---|
| [View and Download a Customer Invoice](#1-view-and-download-a-customer-invoice) | R |

### Key concepts

##### Overview

Before you start, you need to know how D365 links an invoice to its transaction, how to select a transaction row, and the rule for sending documents to customers.

##### Invoices and transactions

| Term | Description |
|---|---|
| **Original document** | The document D365 produced for a posted transaction, such as the customer invoice. You open it from the transaction it belongs to. `[VG-03, VG-04]` |
| **Print preview** | Shows the original document on screen so you can review it and download it as a PDF. |
| **Highlighted row** | Click a transaction row to highlight it before you open its original document. Highlighting a row is not the same as marking it with its checkbox. `[VG-02]` |

##### Sending documents to customers

| Rule | Description |
|---|---|
| **Use PDF, not Excel** | Provide customer-facing account information as a PDF. Do not send a customer an Excel export. `[VG-12]` |

---

## Part 2: How do I do it? (AR Collections Customer Invoices)

### 1. View and Download a Customer Invoice

##### Description

Use this topic to open a customer invoice and, when you need a copy, download it as a PDF. You highlight the invoice transaction, open its **Original document**, review the invoice in **Print preview** and then download it with a file name that identifies the customer and invoice.

##### Responsibility

- Collections Officer: retrieves and reviews customer invoices.

##### Initiation

- A customer or colleague needs a copy of an invoice, or the invoice must be reviewed before contacting the customer.

##### Topic Overview

This topic includes these steps:

| Step | Description |
|---|---|
| [Open the Invoice Preview](#11-open-the-invoice-preview) | Highlight the invoice transaction and open the invoice in Print preview. Output: the invoice is shown on screen. |
| [Download the Invoice as PDF](#12-download-the-invoice-as-pdf) | Optional. Download the invoice as a PDF with a meaningful file name. Output: a PDF copy of the invoice. |

#### 1.1 Open the Invoice Preview

##### Procedure

Complete these steps to open the invoice in print preview:

| Action | Description |
|---|---|
| *PROCESS START* (light blue) | *Pre-requisites:*<br>• Access to D365 and to the customer account.<br>• The customer account and the invoice you need.<br>*Responsibility:*<br>• Collections Officer |
| 1. *Check* the **Entity**. | Confirm you are signed into the correct **Legal Entity** (top-right). |
| 2. *Open* the customer's transactions. `[VG-01]` | Open the transactions for the customer account, for example from **All customers** in your **Favorites**. |
| 3. *Click* the invoice transaction. `[VG-02]` | Click the row for the invoice so it is highlighted. |
| 4. *Click* **Original document**. `[VG-03]` | Open the original document for the highlighted transaction. |
| 5. *Select* the invoice. `[VG-04]` | Select the invoice in the list of original documents. |
| 6. *Click* **Print preview**. `[VG-05]` | The invoice opens in print preview. |
| 7. *Confirm* it is the invoice you need. `[VG-06]` | Review the invoice information in the preview and check that it is the invoice you selected. |
| *STEP COMPLETE* (light blue) | • *The invoice is open in print preview.*<br>• *Continue to [Download the Invoice as PDF](#12-download-the-invoice-as-pdf)* |

#### 1.2 Download the Invoice as PDF

##### Procedure

This subprocedure is optional. Complete it when you need a copy of the invoice, for example to send to a customer. If you only needed to review the invoice, the task is complete.

Complete these steps to download the invoice as a PDF:

| Action | Description |
|---|---|
| *PROCESS START* (light blue) | *Pre-requisites:*<br>• The invoice is open in print preview (see [Open the Invoice Preview](#11-open-the-invoice-preview)).<br>*Responsibility:*<br>• Collections Officer |
| 1. *Download* the invoice as a PDF. `[VG-07]` | From the print preview, download the invoice as a PDF file. |
| 2. *Enter* a meaningful file name. `[VG-08, VG-10]` | Name the file so the customer and the invoice can be identified. |
| 3. *Save* the PDF. `[VG-09]` | Save the PDF file. |
| 4. *Confirm* the PDF shows the correct invoice. | Open the PDF and check that it shows the invoice you selected. |
| *PROCESS COMPLETE* (light green) | *Outcomes:*<br>• The invoice is saved as a PDF with a file name that identifies the customer and invoice. `[VG-21]` |

---

## Part 3: Reports (AR Collections Customer Invoices)

##### Overview

Reports for this process are pending SME confirmation. `[VG-17]`

---

## Additional Resources

The standard template block, unchanged.
