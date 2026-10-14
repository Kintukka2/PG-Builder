# D365 F&O: AR Collections Statement Preview Procedure Guide

> **SME REVIEW DRAFT. Not validated or approved.**
>
> This is a Markdown preview of the Word guide [`TBC-AR Collections Statement Preview PG v0.1.docx`](TBC-AR%20Collections%20Statement%20Preview%20PG%20v0.1.docx). That guide was built from the PG master template in [`/templates`](../../templates/). **The Word file is the editable source.**
>
> `[VG-xx]` markers show unconfirmed items. In the Word file, each one is a review comment. Full details are in the [validation register](../03-validation/PG-AR-Statement-Preview-Validation.md). The markers are not part of the guide text.

The fixed template content is not repeated here: cover, Contents, *About this guide* and *Additional Resources*.

**Version history**

| ID | Date | Author/s | BPO | Description of change |
|---|---|---|---|---|
| 0.1 | October 2026 | Daniel Moreira | To be confirmed `[VG-18]` | SME review draft created from the PG master template. Not validated or approved. |

Guide code and final title: `[VG-19]`.

---

## Part 1: What do I need to know? (AR Collections Statement Preview)

### High-level process

##### Part Description

This guide explains how a Collections Officer generates a customer statement on screen to review it, without sending it to the customer, and downloads it as a PDF. The preview uses **Screen** as the destination instead of **Print management**. Sending a statement to the customer is covered by a separate guide.

##### Initiation

- A Collections Officer needs to review a customer statement, or needs a copy of it, without sending it to the customer. `[VG-16]`

##### Stream

| Stream | Process Area | Key Roles |
|---|---|---|
| Accounts Receivable `[VG-17]` | AR Collections | • Collections Officer |

##### Process

| # | Action | Who | When | Where |
|---|---|---|---|---|
| 1 | [Preview and Download a Customer Statement](#1-preview-and-download-a-customer-statement) | Collections Officer | When a statement must be reviewed or copied without sending it to the customer | D365 |

### Roles and responsibilities

##### Overview

The Collections Officer previews and downloads statements in their own D365 session.

| Tasks / Business Roles | Collections Officer |
|---|---|
| [Preview and Download a Customer Statement](#1-preview-and-download-a-customer-statement) | R |

### Key concepts

##### Overview

Before you start, you need to know how statement destinations work, so that a preview is not sent to the customer, and the rule for customer-facing documents.

##### Statements and destinations

| Term | Description |
|---|---|
| **Customer statement** | A document that lists a customer's transactions. With **Only open** selected, it lists only open transactions. `[VG-03]` |
| **Print management destination** | The destination used to deliver a statement to the customer. Clear it when you only want to preview the statement. `[VG-05]` |
| **Screen destination** | Displays the statement on screen so you can review it and download it, without sending it. `[VG-06]` |

##### Previewing safely

| Rule | Description |
|---|---|
| **Check the destination first** | Before you generate a preview, check that **Print management destination** is cleared and **Screen** is selected. `[VG-05]` |
| **Use PDF, not Excel** | Provide customer-facing account information as a PDF. Do not send a customer an Excel export. `[VG-15]` |

---

## Part 2: How do I do it? (AR Collections Statement Preview)

### 1. Preview and Download a Customer Statement

##### Description

Use this topic to generate a customer statement on screen and, when you need a copy, download it as a PDF. You set the statement options, clear **Print management destination**, select **Screen**, review the statement and then download it.

##### Responsibility

- Collections Officer: previews customer statements without sending them.

##### Initiation

- A Collections Officer needs to review a customer statement, or needs a copy of it, without sending it to the customer.

##### Topic Overview

This topic includes these steps:

| Step | Description |
|---|---|
| [Generate the Statement Preview](#11-generate-the-statement-preview) | Set the statement options and generate it with Screen as the destination. Output: the statement is shown on screen. |
| [Download the Statement as PDF](#12-download-the-statement-as-pdf) | Optional. Download the statement as a PDF with a meaningful file name. Output: a PDF copy of the statement. |

#### 1.1 Generate the Statement Preview

##### Procedure

Complete these steps to generate the statement preview:

| Action | Description |
|---|---|
| *PROCESS START* (light blue) | *Pre-requisites:*<br>• Access to D365 and to customer statements.<br>• The customer account number.<br>*Responsibility:*<br>• Collections Officer |
| 1. *Check* the **Entity**. | Confirm you are signed into the correct **Legal Entity** (top-right). |
| 2. *Open* the **Statements** page. `[VG-01]` | Open the customer statement page. |
| 3. *Select* the customer. `[VG-02]` | Select the customer account the statement is for. |
| 4. *Select* **Only open**. `[VG-03]` | Include only open transactions. |
| 5. *Include* the company logo. `[VG-04]` | Select the option that includes the company logo. |
| 6. *Clear* **Print management destination**. `[VG-05]` | Clear this option so the statement is not delivered to the customer. |
| 7. *Select* **Screen** as the destination. `[VG-06]` | Set the destination to **Screen**. |
| 8. *Generate* the statement. `[VG-07]` | Generate the statement. It opens on screen. |
| 9. *Review* the statement. `[VG-08]` | Check that it shows the correct customer and their open transactions. |
| *STEP COMPLETE* (light blue) | • *The statement is open on screen.*<br>• *Continue to [Download the Statement as PDF](#12-download-the-statement-as-pdf)* |

#### 1.2 Download the Statement as PDF

##### Procedure

This subprocedure is optional. Complete it when you need a copy of the statement. If you only needed to review it, the task is complete.

Complete these steps to download the statement as a PDF:

| Action | Description |
|---|---|
| *PROCESS START* (light blue) | *Pre-requisites:*<br>• The statement is open on screen (see [Generate the Statement Preview](#11-generate-the-statement-preview)).<br>*Responsibility:*<br>• Collections Officer |
| 1. *Download* the statement as a PDF. `[VG-09]` | From the on-screen statement, download it as a PDF file. |
| 2. *Enter* a meaningful file name. `[VG-10, VG-12]` | Name the file so the customer and the statement date can be identified. |
| 3. *Save* the PDF. `[VG-11]` | Save the PDF file. |
| 4. *Confirm* the PDF shows the correct statement. | Open the PDF and check that it shows the statement you reviewed. |
| *PROCESS COMPLETE* (light green) | *Outcomes:*<br>• The statement is saved as a PDF and has not been sent to the customer. `[VG-24]` |

---

## Part 3: Reports (AR Collections Statement Preview)

##### Overview

Reports for this process are pending SME confirmation. `[VG-20]`

---

## Additional Resources

The standard template block, unchanged.
