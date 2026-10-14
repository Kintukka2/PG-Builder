# D365 F&O: AR Collections Personalized Views Procedure Guide

> **SME REVIEW DRAFT. Not validated or approved.**
>
> This is a Markdown preview of the Word guide [`TBC-AR Collections Personalized Views PG v0.1.docx`](TBC-AR%20Collections%20Personalized%20Views%20PG%20v0.1.docx). That guide was built from the PG master template in [`/templates`](../../templates/). **The Word file is the editable source.** Make content changes there first, then update this preview.
>
> `[VG-xx]` markers show unconfirmed items. In the Word file, each one is a review comment for the SME. Full details are in the [validation register](../03-validation/PG-AR-Personalized-Views-Validation.md). The markers are not part of the guide text.

The fixed template content is not repeated here: cover, Contents, *About this guide* and the *Additional Resources* links. The sections below are the content this guide adds.

**Version history**

| ID | Date | Author/s | BPO | Description of change |
|---|---|---|---|---|
| 0.1 | October 2026 | Daniel Moreira | To be confirmed `[VG-23]` | SME review draft created from the PG master template. Not validated or approved. |

Guide code and final title: `[VG-24]`.

---

## Part 1: What do I need to know? (AR Collections Personalized Views)

### High-level process

##### Part Description

This guide explains how a Collections Officer creates, saves and updates a personalized view of a D365 page, so the page shows the columns, filters and totals needed for collection work. It covers arranging columns, filtering the list, adding a footer total, saving the layout as a named view, pinning the view as the default and updating a saved view. Views are set up separately for each page. Exporting data and the use of specific AR pages are outside the scope of this guide.

##### Initiation

- A page does not show the information needed for collection work, such as due dates, currencies or overdue balances. `[VG-21]`

##### Stream

| Stream | Process Area | Key Roles |
|---|---|---|
| Accounts Receivable `[VG-22]` | AR Collections | • Collections Officer |

##### Process

The high-level process is as follows:

| # | Action | Who | When | Where |
|---|---|---|---|---|
| 1 | [Create a Personalized View](#1-create-a-personalized-view) | Collections Officer | When a page does not show the information needed for collection work | D365 |
| 2 | [Update a Saved View](#2-update-a-saved-view) | Collections Officer | When a saved view needs a further change | D365 |

### Roles and responsibilities

##### Overview

The Collections Officer creates and maintains views in their own D365 session.

| Tasks / Business Roles | Collections Officer |
|---|---|
| [Create a Personalized View](#1-create-a-personalized-view) | R |
| [Update a Saved View](#2-update-a-saved-view) | R |

\*R = Responsible

### Key concepts

##### Overview

Before you start, you need to know what a view contains, the filter operators used in this guide and the columns recommended for AR Collections work.

##### What a view contains

| Term | Description |
|---|---|
| **View** | A saved layout for a page: the columns shown and their order, any filters and any footer totals. `[VG-18]` |
| **Default view** | The view you pin as the default for a page. `[VG-14]` |
| **View scope** | Views are set up separately for each page. Set up a view on each page you use. `[VG-02]` |

##### Filter operators

| Operator | Use |
|---|---|
| **not equal to** | Excludes rows that have the value you enter. For example, a balance not equal to **0** excludes zero-balance accounts. `[VG-08]` |
| **is one of** | Includes only rows that match one of several values you select. |

##### Columns recommended for AR Collections views

| Column | Notes |
|---|---|
| **Recommended columns** | Customer account, Customer name, Transaction date, Due date, Description, Amount, Currency, Overdue balance and Email address. `[VG-01]` |

---

## Part 2: How do I do it? (AR Collections Personalized Views)

### 1. Create a Personalized View

##### Description

Use this topic to set up a page so that it shows the information you need for collection work, then save that layout as a named view and pin it as your default. You arrange the columns, optionally filter the rows and add a footer total, and then save the view. Views are set up separately for each page, so repeat this topic for each page you use.

##### Responsibility

- Collections Officer: creates views for the pages they use.

##### Initiation

- A page does not show the information needed for collection work, such as due dates, currencies or overdue balances.

##### Topic Overview

This topic includes these steps:

| Step | Description |
|---|---|
| [Arrange the Columns](#11-arrange-the-columns) | Add, remove and reorder columns. Output: the grid shows the columns you need. |
| [Filter the List](#12-filter-the-list) | Optional. Limit the rows shown, for example to exclude zero balances. Output: the grid shows only the rows you need. |
| [Add a Footer Total](#13-add-a-footer-total) | Optional. Show a total for a column in the grid footer. Output: the footer shows the total. |
| [Save and Pin the View](#14-save-and-pin-the-view) | Save the layout as a named view and pin it as your default. Output: a saved default view for the page. |

#### 1.1 Arrange the Columns

Complete these steps to show the columns you need, in the order you need:

| Action | Description |
|---|---|
| *PROCESS START* (light blue) | *Pre-requisites:*<br>• Access to D365 and to the page you want to personalize.<br>*Responsibility:*<br>• Collections Officer |
| 1. *Check* the **Entity**. `[VG-02]` | Confirm you are signed into the correct **Legal Entity** (top-right). |
| 2. *Open* the page you want to personalize. `[VG-01]` | Open the page whose layout you want to save, for example a page in your **Favorites**. |
| 3. *Click* **Insert columns**. `[VG-03]` | Use **Insert columns** to add columns that the grid does not currently show. |
| 4. *Select* the columns to add. | Select each column you need for collection work. See **Columns recommended for AR Collections views** in Key concepts. |
| 5. *Confirm* the selected columns are added to the grid. `[VG-04]` | Check that each selected column now appears in the grid. |
| 6. *Remove* each column you do not need. `[VG-05]` | Remove columns that are not needed for collection work, so the grid stays readable. |
| 7. *Move* the columns into the order you need. `[VG-06]` | Reposition the columns so the information you check first appears first. |
| *STEP COMPLETE* (light blue) | • The grid shows the columns you need, in your chosen order.<br>• Continue to [Filter the List](#12-filter-the-list) |

#### 1.2 Filter the List

This subprocedure is optional. Complete it when the view should show only some rows. Otherwise, continue to [Add a Footer Total](#13-add-a-footer-total).

Complete these steps to show only the rows you need:

| Action | Description |
|---|---|
| *PROCESS START* (light blue) | *Pre-requisites:*<br>• The grid shows the columns you need (see [Arrange the Columns](#11-arrange-the-columns)).<br>*Responsibility:*<br>• Collections Officer |
| 1. *Open* the filter for the column. `[VG-07]` | Open the filter for the column whose values you want to limit. |
| 2. *Select* the filter operator. `[VG-08]` | Select the operator that matches the rows you want, for example **not equal to** to exclude a value or **is one of** to include several values. See **Filter operators** in Key concepts. |
| 3. *Enter* the filter value. `[VG-29]` | Enter the value or values for the operator. For example, to exclude zero balances, use **not equal to** with the value **0**. |
| 4. *Confirm* only the required rows are displayed. | Check that the grid shows only the rows that match the filter. |
| *STEP COMPLETE* (light blue) | • The grid shows only the rows you need.<br>• Continue to [Add a Footer Total](#13-add-a-footer-total) |

#### 1.3 Add a Footer Total

This subprocedure is optional. Complete it when the view should show a total for a column. Otherwise, continue to [Save and Pin the View](#14-save-and-pin-the-view).

Complete these steps to show a column total in the grid footer:

| Action | Description |
|---|---|
| *PROCESS START* (light blue) | *Pre-requisites:*<br>• The grid shows the columns you need (see [Arrange the Columns](#11-arrange-the-columns)).<br>*Responsibility:*<br>• Collections Officer |
| 1. *Show* the grid footer. `[VG-09]` | Turn on the footer for the grid. |
| 2. *Add* a **Sum** to the column. `[VG-10]` | Add a sum for the column you want totaled, such as an amount or balance column. |
| 3. *Confirm* the total is displayed. | Check that the footer shows the total for the column. |
| *STEP COMPLETE* (light blue) | • The footer shows the total for the column.<br>• Continue to [Save and Pin the View](#14-save-and-pin-the-view) |

#### 1.4 Save and Pin the View

Complete these steps to save the layout as a named view and pin it as your default:

| Action | Description |
|---|---|
| *PROCESS START* (light blue) | *Pre-requisites:*<br>• The grid shows the columns, and any filters and totals, you need (see [Arrange the Columns](#11-arrange-the-columns)).<br>*Responsibility:*<br>• Collections Officer |
| 1. *Click* **Save as**. `[VG-11]` | Save the current layout as a new view. |
| 2. *Enter* the view name. `[VG-12]` | Enter a name that identifies the page and the purpose of the view. |
| 3. *Save* the new view. `[VG-13]` | Save the view with the name you entered. |
| 4. *Select* **Pin as default**. `[VG-14]` | Pin the view as your default for this page. |
| 5. *Confirm* the view is saved and pinned. `[VG-15]` | Check that your view is listed for this page and is set as the default. |
| *PROCESS COMPLETE* (light green) | *Outcomes:*<br>• The page has a saved view with the columns, filters and totals you set. `[VG-18, VG-19]`<br>• The view is pinned as your default for this page. |

### 2. Update a Saved View

##### Description

Use this procedure when a saved view needs a further change, such as an added column, a changed filter or a new total. You select the saved view, make the change and save it, so the view keeps the change the next time you use it.

##### Responsibility

- Collections Officer: maintains the views they have saved.

##### Initiation

- A saved view needs a further change. `[VG-28]`

##### Procedure

Complete these steps to update a saved view:

| Action | Description |
|---|---|
| *PROCESS START* (light blue) | *Pre-requisites:*<br>• A saved view for the page (see [Create a Personalized View](#1-create-a-personalized-view)).<br>*Responsibility:*<br>• Collections Officer |
| 1. *Check* the **Entity**. `[VG-02]` | Confirm you are signed into the correct **Legal Entity** (top-right). |
| 2. *Open* the page that has the saved view. | Open the page whose view you want to change. |
| 3. *Select* the saved view. `[VG-16]` | Select the view you want to change. |
| 4. *Make* the change to the layout. | Change the columns, filters or totals as described in [Create a Personalized View](#1-create-a-personalized-view). |
| 5. *Click* **Save**. `[VG-17]` | Save the change to the selected view. |
| 6. *Confirm* the view shows the change. | Check that the selected view now includes the change. |
| *PROCESS COMPLETE* (light green) | *Outcomes:*<br>• The saved view includes the change. |

---

## Part 3: Reports (AR Collections Personalized Views)

##### Overview

Reports for this process are pending SME confirmation. `[VG-20]`

---

## Additional Resources

The standard template block, unchanged: User Support (D365 issue form, Atlas D365 User Support Hub) and Self-Service Resources (AVA, Procedure Guides, Atlas Training Hub).
