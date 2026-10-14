# D365 F&O: AR Collections Export to Excel Procedure Guide

> **SME REVIEW DRAFT. Not validated or approved.**
>
> This is a Markdown preview of the Word guide [`TBC-AR Collections Export to Excel PG v0.1.docx`](TBC-AR%20Collections%20Export%20to%20Excel%20PG%20v0.1.docx). That guide was built from the PG master template in [`/templates`](../../templates/). **The Word file is the editable source.**
>
> `[VG-xx]` markers show unconfirmed items. In the Word file, each one is a review comment. Full details are in the [validation register](../03-validation/PG-AR-Export-to-Excel-Validation.md). The markers are not part of the guide text.

The fixed template content is not repeated here: cover, Contents, *About this guide* and *Additional Resources*.

**Version history**

| ID | Date | Author/s | BPO | Description of change |
|---|---|---|---|---|
| 0.1 | October 2026 | Daniel Moreira | To be confirmed `[VG-14]` | SME review draft created from the PG master template. Not validated or approved. |

Guide code and final title: `[VG-15]`.

---

## Part 1: What do I need to know? (AR Collections Export to Excel)

### High-level process

##### Part Description

This guide explains how a Collections Officer exports the rows of a D365 grid to Excel for internal analysis. It covers preparing the grid columns, using **Export all rows** from the grid header and checking that the exported file includes the fields you need. The export is not a customer-facing document. Searching the custom all-customer transaction report and locating bank statements are outside the scope of this guide.

##### Initiation

- A Collections Officer needs D365 grid data in Excel for internal analysis. `[VG-12]`

##### Stream

| Stream | Process Area | Key Roles |
|---|---|---|
| Accounts Receivable `[VG-13]` | AR Collections | • Collections Officer |

##### Process

| # | Action | Who | When | Where |
|---|---|---|---|---|
| 1 | [Export All Rows from a Grid](#1-export-all-rows-from-a-grid) | Collections Officer | When grid data is needed in Excel for internal analysis | D365 |

### Roles and responsibilities

##### Overview

The Collections Officer exports grid data in their own D365 session.

| Tasks / Business Roles | Collections Officer |
|---|---|
| [Export All Rows from a Grid](#1-export-all-rows-from-a-grid) | R |

### Key concepts

##### Overview

Before you start, you need to know what an export contains and the rule for using exported data.

##### Grid exports

| Term | Description |
|---|---|
| **Export all rows** | An option on the grid header that exports the grid's rows to an Excel file. `[VG-01, VG-05]` |
| **Configured columns** | The export contains the columns configured on the grid. Add any column you need before you export. `[VG-04]` |
| **Export volume** | Limits apply to how much data can be exported. The limits for your environment are pending confirmation. `[VG-06]` |

##### Using exported data

| Rule | Description |
|---|---|
| **Internal analysis only** | Use exported data for internal analysis. Customer-facing invoices and account documents use the approved PDF output. Do not send a customer an Excel export. `[VG-09]` |
| **Exported customer data** | Exported files can contain customer information. Store and share them according to the approved data handling rules. `[VG-08]` |

---

## Part 2: How do I do it? (AR Collections Export to Excel)

### 1. Export All Rows from a Grid

##### Description

Use this procedure to export the rows of a D365 grid to Excel for internal analysis. You prepare the grid columns, export all rows from the grid header and check the exported file.

##### Responsibility

- Collections Officer: exports grid data for internal analysis.

##### Initiation

- A Collections Officer needs D365 grid data in Excel for internal analysis.

##### Procedure

Complete these steps to export all rows from a grid:

| Action | Description |
|---|---|
| *PROCESS START* (light blue) | *Pre-requisites:*<br>• Access to D365 and to the page that holds the data.<br>*Responsibility:*<br>• Collections Officer |
| 1. *Check* the **Entity**. | Confirm you are signed into the correct **Legal Entity** (top-right). |
| 2. *Open* the page that holds the data. `[VG-10, VG-11]` | Open the D365 page whose grid holds the data you need, for example **Aged balances** from your **Favorites**. |
| 3. *Confirm* the grid shows the columns you need. | The export contains the columns configured on the grid. If a column is missing, add it with **Insert columns** (see the AR Collections Personalized Views guide). |
| 4. *Right-click* the grid header. `[VG-02]` | Right-click the header of any column in the grid. |
| 5. *Select* **Export all rows**. `[VG-01]` | Select **Export all rows** from the menu. |
| 6. *Download* the export. `[VG-03]` | Download the exported file when D365 has prepared it. |
| 7. *Open* the exported file. `[VG-07]` | Open the downloaded file in Excel. |
| 8. *Confirm* the required fields were exported. | Check that the file includes every field you need for your analysis. |
| *PROCESS COMPLETE* (light green) | *Outcomes:*<br>• The grid rows are exported to an Excel file with the configured columns.<br>• The file is used for internal analysis only. |

---

## Part 3: Reports (AR Collections Export to Excel)

##### Overview

Reports for this process are pending SME confirmation. `[VG-16]`

---

## Additional Resources

The standard template block, unchanged.
