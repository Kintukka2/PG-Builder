# D365 F&O: AR Collections Notes and Activities Procedure Guide

> **SME REVIEW DRAFT. Not validated or approved.**
>
> This is a Markdown preview of the Word guide [`TBC-AR Collections Notes and Activities PG v0.1.docx`](TBC-AR%20Collections%20Notes%20and%20Activities%20PG%20v0.1.docx). That guide was built from the PG master template in [`/templates`](../../templates/). **The Word file is the editable source.**
>
> `[VG-xx]` markers show unconfirmed items. In the Word file, each one is a review comment. Full details are in the [validation register](../03-validation/PG-AR-Notes-and-Activities-Validation.md). The markers are not part of the guide text.

The fixed template content is not repeated here: cover, Contents, *About this guide* and *Additional Resources*.

**Version history**

| ID | Date | Author/s | BPO | Description of change |
|---|---|---|---|---|
| 0.1 | October 2026 | Daniel Moreira | To be confirmed `[VG-16]` | SME review draft created from the PG master template. Not validated or approved. |

Guide code and final title: `[VG-17]`.

---

## Part 1: What do I need to know? (AR Collections Notes and Activities)

### High-level process

##### Part Description

This guide explains how a Collections Officer reviews a customer's collection history in D365 before contacting the customer. It covers filtering the **Notes** page to one customer and, if needed, by creator, date or note type, and opening **View all activities** from the customer account. Recording a new collection activity is outside the scope of this guide.

##### Initiation

- A Collections Officer needs to review previous collection notes and contact with a customer before contacting them. `[VG-14]`

##### Stream

| Stream | Process Area | Key Roles |
|---|---|---|
| Accounts Receivable `[VG-15]` | AR Collections | • Collections Officer |

##### Process

| # | Action | Who | When | Where |
|---|---|---|---|---|
| 1 | [Review Customer Notes](#1-review-customer-notes) | Collections Officer | Before contacting a customer, to see previous collection notes | D365 |
| 2 | [Review All Customer Activities](#2-review-all-customer-activities) | Collections Officer | Before contacting a customer, to see previous contact with them | D365 |

### Roles and responsibilities

##### Overview

The Collections Officer reviews notes and activities in their own D365 session.

| Tasks / Business Roles | Collections Officer |
|---|---|
| [Review Customer Notes](#1-review-customer-notes) | R |
| [Review All Customer Activities](#2-review-all-customer-activities) | R |

### Key concepts

##### Overview

Before you start, you need to know what the Notes page and customer activities show, and where collection notes are recorded.

##### Notes and activities

| Term | Description |
|---|---|
| **Notes** | A page in the **Customer credit and collections** workspace that lists notes recorded against customer accounts. You filter it to see one customer's collection history. `[VG-01, VG-02]` |
| **System-generated entries** | The Notes page lists entries created by D365, such as statements and collection letters, alongside notes entered by users. `[VG-05, VG-06]` |
| **Customer activities** | Records of collection contact with a customer, such as an email or phone activity. **View all activities** on the customer account lists them. `[VG-12]` |

##### Recording collection history

| Rule | Description |
|---|---|
| **Record notes at customer level** | Collection notes are recorded against the customer account rather than against individual invoices, so the full history is in one place. `[VG-11]` |

---

## Part 2: How do I do it? (AR Collections Notes and Activities)

### 1. Review Customer Notes

##### Description

Use this procedure to filter the **Notes** page to one customer, narrow it if needed, and review the customer's collection notes.

##### Responsibility

- Collections Officer: reviews a customer's collection notes before contacting them.

##### Initiation

- A Collections Officer needs to review previous collection notes before contacting a customer.

##### Procedure

Complete these steps to review a customer's notes:

| Action | Description |
|---|---|
| *PROCESS START* (light blue) | *Pre-requisites:*<br>• Access to D365 and to the **Customer credit and collections** workspace.<br>• The customer account number.<br>*Responsibility:*<br>• Collections Officer |
| 1. *Check* the **Entity**. | Confirm you are signed into the correct **Legal Entity** (top-right). |
| 2. *Open* the **Notes** page. `[VG-01, VG-02]` | Open **Notes** from the **Customer credit and collections** workspace. |
| 3. *Open* the filter for the customer column. `[VG-03]` | Open the filter for the customer column. |
| 4. *Enter* the customer account. | Enter or select the customer account number. |
| 5. *Apply* the filter. | Apply the filter. Only notes for that customer are listed. |
| 6. *Filter* by creator, date or note type. `[VG-04]` | Optional. Filter the creator, date or note type column in the same way. Otherwise, go to step 7. |
| 7. *Review* the notes. `[VG-06]` | Read the notes. Check which entries were entered by users and which were created by D365. |
| 8. *Confirm* you have the customer's collection history. `[VG-13]` | Check that the list shows only the customer you selected and covers the period you need. |
| *PROCESS COMPLETE* (light green) | *Outcomes:*<br>• You have reviewed the customer's collection notes. |

### 2. Review All Customer Activities

##### Description

Use this procedure to review all recorded activities for a customer. You open the customer account from **All customers** and then open **View all activities** to see the customer's contact history.

##### Responsibility

- Collections Officer: reviews a customer's contact history before contacting them.

##### Initiation

- A Collections Officer needs to review previous contact with a customer before contacting them. `[VG-14]`

##### Procedure

Complete these steps to review a customer's activities:

| Action | Description |
|---|---|
| *PROCESS START* (light blue) | *Pre-requisites:*<br>• Access to D365 and to the **Credit and collections** module.<br>• The customer account number.<br>*Responsibility:*<br>• Collections Officer |
| 1. *Check* the **Entity**. | Confirm you are signed into the correct **Legal Entity** (top-right). |
| 2. *Click* **Modules**. | From the left-hand **Navigation Pane**, click **Modules**. |
| 3. *Navigate* to the **All customers** page. `[VG-07]` | From the **Navigation Pane**, *select*:<br>• **Credit and collections >**<br>• **All customers**<br>If **All customers** is in your **Favorites** (see the AR Collections Favorites guide), you can open it from **Favorites** instead. |
| 4. *Open* the customer account. `[VG-08]` | Find the customer and open the account. |
| 5. *Click* **View all activities**. `[VG-09]` | Open the list of activities recorded for the customer. |
| 6. *Filter* the activities. `[VG-10]` | Optional. Filter the list to the activities you need. If you don't need to filter, go to step 7. |
| 7. *Review* the customer's contact history. | Read the activities to see when and how the customer was contacted. |
| *PROCESS COMPLETE* (light green) | *Outcomes:*<br>• You have reviewed the customer's recorded activities. |

---

## Part 3: Reports (AR Collections Notes and Activities)

##### Overview

Reports for this process are pending SME confirmation. `[VG-18]`

---

## Additional Resources

The standard template block, unchanged.
