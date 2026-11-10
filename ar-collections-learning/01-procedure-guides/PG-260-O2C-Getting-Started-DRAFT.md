# D365 F&O: O2C Getting Started Procedure Guide

> **WORKING DRAFT. Not validated or approved.**
>
> This is a Markdown preview of the Word guide [`260-O2C Getting Started PG v0.2.docx`](260-O2C%20Getting%20Started%20PG%20v0.2.docx). It was assembled from the topic drafts named in its version history, under D-045 and D-046. **The Word file is the editable source.**
>
> Markers such as `[G260-01]` or `[Legal Entities VG-01]` show unconfirmed items. In the Word file, each one is a review comment. Guide-level items and the index of carried items are in the [validation register](../03-validation/260-O2C-Getting-Started-Validation.md). The markers are not part of the guide text.

The fixed template content is not repeated here: cover, Contents, *About this guide* and *Additional Resources*.

**Version history**

| ID | Date | Author/s | BPO | Description of change |
|---|---|---|---|---|
| 0.1 | November 2026 | Daniel Moreira | To be confirmed | Working draft assembled from the Legal Entities, Favorites, Personalized Views and Export to Excel topic drafts (D-045, D-046). Not validated or approved. |
| 0.2 | November 2026 | Daniel Moreira | To be confirmed `[G260-02]` | SME review by Maria Pabalan (10 November 2026) applied (D-054): ledger code URL example; view selector, Save as, footer total and all-legal-entities default steps; full filter operator list; topic 7 Remove a Page from Favorites; role O2C End-user. Not validated or approved. |

Guide code, title and scope: `[G260-01]`.

---

## Part 1: What do I need to know? (O2C Getting Started)

### High-level process

##### Part Description

This guide covers the general D365 tasks that every Order to Cash (O2C) user needs before starting process work: switching to the correct legal entity, adding pages to **Favorites**, creating and updating personalized views, and exporting grid data to Excel. These tasks are not steps in a business process. Each O2C process guide links to them and lists its own pages, columns and views: for AR Collections, see 230 Collections Part 1.

The steps come from the AR Training D365 sessions, where they were demonstrated on AR Collections pages. They apply to any D365 page that has the same controls. `[G260-03]`

##### Initiation

- A new O2C user is setting up D365 before starting routine process work. `[G260-04]`

##### Stream

| Stream | Process Area | Key Roles |
|---|---|---|
| Order to Cash (O2C) `[G260-05]` | O2C Getting Started | • All O2C roles |

##### Process

The high-level process is as follows:

| # | Action | Who | When | Where |
|---|---|---|---|---|
| 1 | [Switch Legal Entity with the Selector](#1-switch-legal-entity-with-the-selector) | O2C End-user | When work is needed in a legal entity other than the active one | D365 |
| 2 | [Switch Legal Entity Using the Ledger Code](#2-switch-legal-entity-using-the-ledger-code) | O2C End-user | When the D365 ledger code is known and switching through the URL is appropriate | D365 |
| 3 | [Add Pages to Favorites](#3-add-pages-to-favorites) | O2C End-user | When setting up D365, or when a page is used often | D365 |
| 4 | [Create a Personalized View](#4-create-a-personalized-view) | O2C End-user | When a page does not show the information needed | D365 |
| 5 | [Update a Saved View](#5-update-a-saved-view) | O2C End-user | When a saved view needs a further change | D365 |
| 6 | [Export All Rows from a Grid](#6-export-all-rows-from-a-grid) | O2C End-user | When grid data is needed in Excel for internal analysis | D365; Excel |
| 7 | [Remove a Page from Favorites](#7-remove-a-page-from-favorites) | O2C End-user | When a page in your Favorites is no longer needed | D365 |

### Roles and responsibilities

##### Overview

Every O2C user completes these tasks in their own D365 session.

| **Tasks / Business Roles** | O2C End-user |
|---|---|
| [Switch Legal Entity with the Selector](#1-switch-legal-entity-with-the-selector) | R |
| [Switch Legal Entity Using the Ledger Code](#2-switch-legal-entity-using-the-ledger-code) | R |
| [Add Pages to Favorites](#3-add-pages-to-favorites) | R |
| [Create a Personalized View](#4-create-a-personalized-view) | R |
| [Update a Saved View](#5-update-a-saved-view) | R |
| [Export All Rows from a Grid](#6-export-all-rows-from-a-grid) | R |
| [Remove a Page from Favorites](#7-remove-a-page-from-favorites) | R |

\*R = Responsible

### Key concepts

##### Overview

Before you start, you need to know the **Navigation Pane** options, how legal entities are identified, what a view contains and what a grid export contains.

##### Navigation Pane options

| Option | Description |
|---|---|
| **Modules** | Opens the list of D365 modules, such as **Credit and collections** and **Accounts receivable**. Clicking a module opens its module menu. |
| **Favorites** | Lists the pages you have added as favorites. Click a page in the list to open it. |

##### Legal entities

| Term | Description |
|---|---|
| **Legal entity** | A company set up in D365. The pages you open show data for the active legal entity, so you must work in the legal entity that holds the customer accounts you need. `[Legal Entities VG-22]` |
| **Business name** | The name of the business a legal entity represents. Use the business name to identify the legal entity you need. |
| **Ledger code** | The code D365 uses for a legal entity. D365 ledger codes differ from CargoWise ledger codes. `[Legal Entities VG-08]` |

##### Working in the correct legal entity

| Rule | Description |
|---|---|
| **Work with business names** | Identify legal entities by their business names rather than their ledger codes. `[Legal Entities VG-09]` |
| **Confirm before processing** | Confirm the active legal entity before you perform any transaction. `[Legal Entities VG-10]` |

##### What a view contains

| Term | Description |
|---|---|
| **View** | A saved layout for a page: the columns shown and their order, any filters and any footer totals. `[Personalized Views VG-18]` |
| **Default view** | The view you pin as the default for a page. `[Personalized Views VG-14]` |
| **View scope** | Views are set up separately for each page. Set up a view on each page you use. `[Personalized Views VG-02]` |

##### Filter operators

The operators you can select depend on the type of column you filter.

**Text columns**

| Operator | Use |
|---|---|
| **is exactly** `[Personalized Views VG-08]` | Matches the value exactly, for example customer account 112A. |
| **is not** | Excludes the exact value. |
| **contains** | Matches any value that includes the text you type. |
| **does not contain** | Excludes values that include the text. |
| **begins with** | Matches values that start with the text. |
| **ends with** | Matches values that end with the text. |
| **is one of** | Matches any of several values. Separate the values with commas. |
| **matches** | Matches a pattern with wildcards: an asterisk (*) for any characters and a question mark (?) for a single character. |

**Number and amount columns**

| Operator | Use |
|---|---|
| **equals / does not equal** | An exact amount, or every amount except one. For example, a balance that does not equal **0** excludes zero-balance accounts. |
| **greater than / less than** | Values above or below a threshold, such as overdue balances. |
| **between** | A range from one value to another. |
| **is one of** | A list of specific values. |

**Date columns**

| Operator | Use |
|---|---|
| **is / is not** | A specific date, or every date except one. |
| **before / after** | Dates earlier or later than a given date, such as due dates. |
| **between** | A date range. |

##### Grid exports

| Term | Description |
|---|---|
| **Export all rows** | An option on the grid header that exports the grid's rows to an Excel file. `[Export to Excel VG-01 / VG-05]` |
| **Configured columns** | The export contains the columns configured on the grid. Add any column you need before you export. `[Export to Excel VG-04]` |
| **Export volume** | Limits apply to how much data can be exported. The limits for your environment are pending confirmation. `[Export to Excel VG-06]` |

##### Using exported data

| Rule | Description |
|---|---|
| **Internal analysis only** | Use exported data for internal analysis. Customer-facing invoices and account documents use the approved PDF output. Do not send a customer an Excel export. `[Export to Excel VG-09]` |
| **Exported customer data** | Exported files can contain customer information. Store and share them according to the approved data handling rules. `[Export to Excel VG-08]` |

---

## Part 2: How do I do it? (O2C Getting Started)

### 1. Switch Legal Entity with the Selector

##### Description

Use this procedure to switch to another legal entity with the legal entity selector in the D365 header. You find the legal entity by its business name, select it and confirm that it is active.

##### Responsibility

- O2C End-user: works in the legal entity required for the task.

##### Initiation

- An O2C user needs to work in a legal entity other than the one that is active.

##### Procedure

Complete these steps to switch legal entity with the selector:

| **Action** | **Description** |
|---|---|
| *PROCESS START* (light blue) | *Pre-requisites:*<br>• Access to D365 and to the required legal entity.<br>• The business name of the required legal entity.<br>*Responsibility:*<br>• O2C End-user |
| 1. *Click* the legal entity selector. `[Legal Entities VG-01]` | In the D365 header (top-right), click the legal entity selector. It shows the active legal entity. |
| 2. *Find* the required legal entity. `[Legal Entities VG-02]` | Find the legal entity by its business name. |
| 3. *Select* the legal entity. `[Legal Entities VG-03]` | Select the legal entity. D365 switches to it. |
| 4. *Confirm* the active legal entity. `[Legal Entities VG-04]` | Check that the selector now shows the required legal entity before you continue.<br>The ledger code after **cmp=** in the browser address bar also changes to the code of the selected legal entity (see [Switch Legal Entity Using the Ledger Code](#2-switch-legal-entity-using-the-ledger-code)). |
| *PROCESS COMPLETE* (light green) | *Outcomes:*<br>• D365 is working in the required legal entity. |

### 2. Switch Legal Entity Using the Ledger Code

##### Description

Use this procedure to switch legal entity by changing the ledger code in the D365 URL. You replace the ledger code in the browser address bar and confirm that the required legal entity is active.

##### Responsibility

- O2C End-user: works in the legal entity required for the task.

##### Initiation

- The D365 ledger code of the required legal entity is known, and switching through the URL is appropriate. `[Legal Entities VG-07]`

##### Procedure

Complete these steps to switch legal entity using the ledger code:

| **Action** | **Description** |
|---|---|
| *PROCESS START* (light blue) | *Pre-requisites:*<br>• Access to D365 and to the required legal entity.<br>• The D365 ledger code of the required legal entity.<br>*Responsibility:*<br>• O2C End-user |
| 1. *Click* the browser address bar. | Click the address bar to edit the D365 URL. |
| 2. *Find* the ledger code in the URL. `[Legal Entities VG-05]` | In the address bar, find **cmp=** in the URL. The code after it is the ledger code of the active legal entity. For example:<br>https://wtg.operations.dynamics.com/?cmp=**112a**&mi=LedgerJournalTable_CustPaym<br>Here the ledger code is **112a**. |
| 3. *Enter* the required ledger code. `[Legal Entities VG-06]` | Replace the code after **cmp=** with the D365 ledger code of the required legal entity. Do not use the CargoWise code. |
| 4. *Press* **Enter**. | Press **Enter** to open D365 in the required legal entity. |
| 5. *Confirm* the active legal entity. | Check that the legal entity selector (top-right) shows the required legal entity before you continue. |
| *PROCESS COMPLETE* (light green) | *Outcomes:*<br>• D365 is working in the required legal entity. |

### 3. Add Pages to Favorites

##### Description

Use this procedure to add a D365 page to your **Favorites**, so that it opens directly from **Favorites** in the **Navigation Pane** instead of through the module menus. You find the page in its module menu, click its favorite star and check that it appears under **Favorites**. Each process guide lists the pages its users add: for AR Collections, see 230 Collections Part 1. `[G260-06]`

##### Responsibility

- O2C End-user: adds the pages they use to their own Favorites.

##### Initiation

- A new O2C user is setting up D365, or a page is used often.

##### Procedure

Complete these steps to add a page to your Favorites:

| **Action** | **Description** |
|---|---|
| *PROCESS START* (light blue) | *Pre-requisites:*<br>• Access to D365 and to the module that contains the page. `[Favorites VG-17]`<br>• The **Navigation Pane** is visible. `[Favorites VG-12]`<br>*Responsibility:*<br>• O2C End-user |
| 1. *Check* the **Entity**. `[Favorites VG-23 / VG-10]` | Confirm you are signed into the correct **Legal Entity** (top-right). To change it, see [Switch Legal Entity with the Selector](#1-switch-legal-entity-with-the-selector). |
| 2. *Click* **Modules**. `[Favorites VG-08]` | From the left-hand **Navigation Pane**, click **Modules**. |
| 3. *Click* the module that contains the page. | From the list of modules, click the module, for example **Credit and collections** or **Accounts receivable**. The module menu opens. |
| 4. *Click* the favorite star for the page. `[Favorites VG-02 / VG-06, Favorites VG-07]` | In the module menu, find the page and click its favorite star. The page is added to your **Favorites**.<br>To add another page, repeat steps 2 to 4. |
| 5. *Click* **Favorites**. `[Favorites VG-09 / VG-28]` | From the left-hand **Navigation Pane**, click **Favorites**. Your favorites list is displayed. |
| 6. *Confirm* the page is listed. `[Favorites VG-13 / VG-16]` | Confirm that the page appears in your favorites list. If a module or page is not available to you, log a request through the D365 issue form (see **Additional Resources**). |
| 7. *Click* the page in your favorites list. | The page opens. |
| *PROCESS COMPLETE* (light green) | *Outcomes:*<br>• The page appears under **Favorites** in the **Navigation Pane**. `[Favorites VG-10 / VG-11]`<br>• The page opens from **Favorites**. |

> **Note:** To remove a page from your **Favorites**, see [Remove a Page from Favorites](#7-remove-a-page-from-favorites).

### 4. Create a Personalized View

##### Description

Use this topic to set up a page so that it shows the information you need for your work, then save that layout as a named view and pin it as your default. You arrange the columns, optionally filter the rows and add a footer total, and then save the view. Views are set up separately for each page, so repeat this topic for each page you use.

##### Responsibility

- O2C End-user: creates views for the pages they use.

##### Initiation

- A page does not show the information needed for your work, such as due dates, currencies or overdue balances.

##### Topic Overview

This topic includes these steps:

| Step | Description |
|---|---|
| [Arrange the Columns](#41-arrange-the-columns) | Add the columns you need, remove the ones you do not and reorder them so the most important information appears first. Output: the grid shows the columns you need, in your chosen order. |
| [Filter the List](#42-filter-the-list) | Optional. Limit the rows shown by filtering on a column value, for example to exclude zero balances or to include only certain customers. Output: the grid shows only the rows you need. |
| [Add a Footer Total](#43-add-a-footer-total) | Optional. Turn on the grid footer and add a sum to a column, such as an amount or balance column, so you can see the total at a glance. Output: the footer shows the total for the column. |
| [Save and Pin the View](#44-save-and-pin-the-view) | Save the layout as a named view and pin it as your default, so the page opens with your columns, filters and totals each time you use it. Output: a saved default view for the page. |

#### 4.1 Arrange the Columns

##### Procedure

Complete these steps to show the columns you need, in the order you need:

| **Action** | **Description** |
|---|---|
| *PROCESS START* (light blue) | *Pre-requisites:*<br>• Access to D365 and to the page you want to personalize.<br>*Responsibility:*<br>• O2C End-user |
| 1. *Check* the **Entity**. `[Personalized Views VG-02]` | Confirm you are signed into the correct **Legal Entity** (top-right). |
| 2. *Open* the page you want to personalize. `[Personalized Views VG-01]` | Open the page whose layout you want to save, for example a page in your **Favorites**. |
| 3. *Click* **Insert columns**. `[Personalized Views VG-03]` | Use **Insert columns** to add columns that the grid does not currently show. |
| 4. *Select* the columns to add. | Select each column you need for your work. Each process guide lists the columns recommended for its pages: for AR Collections, see 230 Collections Part 1. |
| 5. *Confirm* the selected columns are added to the grid. `[Personalized Views VG-04]` | Check that each selected column now appears in the grid. |
| 6. *Remove* each column you do not need. `[Personalized Views VG-05]` | Remove columns that are not needed for your work, so the grid stays readable. |
| 7. *Move* the columns into the order you need. `[Personalized Views VG-06]` | Reposition the columns so the information you check first appears first. |
| *STEP COMPLETE* (light blue) | • The grid shows the columns you need, in your chosen order.<br>• Continue to [Filter the List](#42-filter-the-list) |

#### 4.2 Filter the List

##### Procedure

This subprocedure is optional. Complete it when the view should show only some rows. Otherwise, continue to [Add a Footer Total](#43-add-a-footer-total).

Complete these steps to show only the rows you need:

| **Action** | **Description** |
|---|---|
| *PROCESS START* (light blue) | *Pre-requisites:*<br>• The grid shows the columns you need (see [Arrange the Columns](#41-arrange-the-columns)).<br>*Responsibility:*<br>• O2C End-user |
| 1. *Open* the filter for the column. `[Personalized Views VG-07]` | Open the filter for the column whose values you want to limit. |
| 2. *Select* the filter operator. `[Personalized Views VG-08]` | Select the operator that matches the rows you want, for example **does not equal** to exclude a value or **is one of** to include several values. The operators depend on the column type: see **Filter operators** in Key concepts for the full list. |
| 3. *Enter* the filter value. `[Personalized Views VG-29]` | Enter the value or values for the operator. For example, to exclude zero balances, use **does not equal** with the value **0**. |
| 4. *Confirm* only the required rows are displayed. | Check that the grid shows only the rows that match the filter. |
| *STEP COMPLETE* (light blue) | • The grid shows only the rows you need.<br>• Continue to [Add a Footer Total](#43-add-a-footer-total) |

#### 4.3 Add a Footer Total

##### Procedure

This subprocedure is optional. Complete it when the view should show a total for a column. Otherwise, continue to [Save and Pin the View](#44-save-and-pin-the-view).

Complete these steps to show a column total in the grid footer:

| **Action** | **Description** |
|---|---|
| *PROCESS START* (light blue) | *Pre-requisites:*<br>• The grid shows the columns you need (see [Arrange the Columns](#41-arrange-the-columns)).<br>*Responsibility:*<br>• O2C End-user |
| 1. *Show* the grid footer. `[Personalized Views VG-09]` | Turn on the footer for the grid. |
| 2. *Add* a **Sum** to the column. `[Personalized Views VG-10]` | Hover over the footer under the column you want totaled, such as an amount or balance column, until a **+** symbol appears. Click **+** to calculate the total for the column. |
| 3. *Confirm* the total is displayed. | Check that the footer shows the total for the column. |
| *STEP COMPLETE* (light blue) | • The footer shows the total for the column.<br>• Continue to [Save and Pin the View](#44-save-and-pin-the-view) |

#### 4.4 Save and Pin the View

##### Procedure

Complete these steps to save the layout as a named view and pin it as your default:

| **Action** | **Description** |
|---|---|
| *PROCESS START* (light blue) | *Pre-requisites:*<br>• The grid shows the columns, and any filters and totals, you need (see [Arrange the Columns](#41-arrange-the-columns)).<br>*Responsibility:*<br>• O2C End-user |
| 1. *Click* the view name. | At the top of the page, click the view name beside the page title to open the view selector. If you have never saved a view, the view name is **My view**.<br>An asterisk (*) after the view name shows that the page has changes you can save. |
| 2. *Click* **Save as**. `[Personalized Views VG-11]` | In the view selector, click **Save as** to save the current layout as a new view. |
| 3. *Enter* the view name. `[Personalized Views VG-12]` | Enter a name that identifies the page and the purpose of the view. |
| 4. *Save* the new view. `[Personalized Views VG-13]` | Save the view with the name you entered. |
| 5. *Select* **Pin as default**. `[Personalized Views VG-14]` | Pin the view as your default for this page. |
| 6. *Set* the default for all legal entities. `[G260-07]` | Optional. To make the view your default in every legal entity, not only the active one, select the option to set it as the default view across all legal entities. |
| 7. *Confirm* the view is saved and pinned. `[Personalized Views VG-15]` | Check that your view is listed in the view selector and is set as the default for this page. If you set it for all legal entities, it is also your default after you switch legal entity. |
| *PROCESS COMPLETE* (light green) | *Outcomes:*<br>• The page has a saved view with the columns, filters and totals you set. `[Personalized Views VG-18 / VG-19]`<br>• The view is pinned as your default for this page. |

### 5. Update a Saved View

##### Description

Use this procedure when a saved view needs a further change, such as an added column, a changed filter or a new total. You select the saved view, make the change and save it, so the view keeps the change the next time you use it.

##### Responsibility

- O2C End-user: maintains the views they have saved.

##### Initiation

- A saved view needs a further change. `[Personalized Views VG-28]`

##### Procedure

Complete these steps to update a saved view:

| **Action** | **Description** |
|---|---|
| *PROCESS START* (light blue) | *Pre-requisites:*<br>• A saved view for the page (see [Create a Personalized View](#4-create-a-personalized-view)).<br>*Responsibility:*<br>• O2C End-user |
| 1. *Check* the **Entity**. `[Personalized Views VG-02]` | Confirm you are signed into the correct **Legal Entity** (top-right). |
| 2. *Open* the page that has the saved view. | Open the page whose view you want to change. |
| 3. *Select* the saved view. `[Personalized Views VG-16]` | Click the view name beside the page title to open the view selector, then select the view you want to change. |
| 4. *Make* the change to the layout. | Change the columns, filters or totals as described in [Create a Personalized View](#4-create-a-personalized-view). |
| 5. *Click* **Save**. `[Personalized Views VG-17]` | In the view selector, click **Save** to save the change to the selected view. An asterisk (*) after the view name shows that the change is not saved yet. |
| 6. *Confirm* the view shows the change. | Check that the selected view now includes the change. |
| *PROCESS COMPLETE* (light green) | *Outcomes:*<br>• The saved view includes the change. |

### 6. Export All Rows from a Grid

##### Description

Use this procedure to export the rows of a D365 grid to Excel for internal analysis. You prepare the grid columns, export all rows from the grid header and check the exported file.

##### Responsibility

- O2C End-user: exports grid data for internal analysis.

##### Initiation

- An O2C user needs D365 grid data in Excel for internal analysis.

##### Procedure

Complete these steps to export all rows from a grid:

| **Action** | **Description** |
|---|---|
| *PROCESS START* (light blue) | *Pre-requisites:*<br>• Access to D365 and to the page that holds the data.<br>*Responsibility:*<br>• O2C End-user |
| 1. *Check* the **Entity**. | Confirm you are signed into the correct **Legal Entity** (top-right). |
| 2. *Open* the page that holds the data. `[Export to Excel VG-10 / VG-11]` | Open the D365 page whose grid holds the data you need, for example **Aged balances** from your **Favorites**. |
| 3. *Confirm* the grid shows the columns you need. | The export contains the columns configured on the grid. If a column is missing, add it with **Insert columns** (see [Arrange the Columns](#41-arrange-the-columns)). |
| 4. *Right-click* the grid header. `[Export to Excel VG-02]` | Right-click the header of any column in the grid. |
| 5. *Select* **Export all rows**. `[Export to Excel VG-01]` | Select **Export all rows** from the menu. |
| 6. *Download* the export. `[Export to Excel VG-03]` | Download the exported file when D365 has prepared it. |
| 7. *Open* the exported file. `[Export to Excel VG-07]` | Open the downloaded file in Excel. |
| 8. *Confirm* the required fields were exported. | Check that the file includes every field you need for your analysis. |
| *PROCESS COMPLETE* (light green) | *Outcomes:*<br>• The grid rows are exported to an Excel file with the configured columns.<br>• The file is used for internal analysis only. |

### 7. Remove a Page from Favorites

##### Description

Use this procedure to remove a page you no longer need from your **Favorites**. You open your favorites list, click the page's filled favorite star and check that the page is no longer listed. Removing a favorite does not change your access to the page: it still opens from its module menu. `[G260-08]`

##### Responsibility

- O2C End-user: removes pages they no longer need from their own Favorites.

##### Initiation

- A page in your Favorites is no longer needed.

##### Procedure

Complete these steps to remove a page from your Favorites:

| **Action** | **Description** |
|---|---|
| *PROCESS START* (light blue) | *Pre-requisites:*<br>• Access to D365.<br>• The page is in your **Favorites**.<br>*Responsibility:*<br>• O2C End-user |
| 1. *Check* the **Entity**. `[Favorites VG-23 / VG-10]` | Confirm you are signed into the correct **Legal Entity** (top-right). |
| 2. *Click* **Favorites**. | From the left-hand **Navigation Pane**, click **Favorites**. Your favorites list is displayed. |
| 3. *Click* the favorite star for the page. | In your favorites list, find the page and click its filled favorite star. The page is removed from your **Favorites**.<br>You can also click the filled star next to the page in its module menu. |
| 4. *Confirm* the page is no longer listed. | Check that the page no longer appears in your favorites list. |
| *PROCESS COMPLETE* (light green) | *Outcomes:*<br>• The page no longer appears under **Favorites** in the **Navigation Pane**.<br>• The page still opens from its module menu. |

---

## Part 3: Reports (O2C Getting Started)

##### Overview

No reports apply to this guide. Each O2C process guide lists the reports for its process.

---

## Additional Resources

The standard template block, unchanged.
