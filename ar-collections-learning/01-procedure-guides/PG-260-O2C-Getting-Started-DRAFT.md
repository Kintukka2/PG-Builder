# D365 F&O: O2C Getting Started Procedure Guide

> **WORKING DRAFT. Not validated or approved.**
>
> This is a Markdown preview of the Word guide [`CLAUDE-260-O2C Getting Started PG v0.2.docx`](CLAUDE-260-O2C%20Getting%20Started%20PG%20v0.2.docx). This is Daniel Moreira’s v0.2 of 12 November 2026, built from Maria Pabalan’s review of v0.1, which is the master copy (D-078); it went to Maria for final approval. The repository copy adds the formatting rules, one review comment per open blocking item and the notes to the author (D-078). **The Word file is the editable source.**
>
> Markers such as `[G260-01]` or `[Legal Entities VG-01]` show the open blocking items. In the Word file, each has one review comment, at the place it matters most (D-067); non-blocking items are in their registers only. Guide-level items and the index of carried items are in the [validation register](../03-validation/260-O2C-Getting-Started-Validation.md). Notes marked **ACTION: REVIEW REQUIREMENT**, and <mark>highlighted</mark> phrases, are internal notes to the author (yellow in the Word file); they are removed before publication (D-060). The markers are not part of the guide text.

The fixed template content is not repeated here: cover, Contents, *About this guide* and *Additional Resources*.

**Version history**

| ID | Date | Author/s | BPO | Description of change |
|---|---|---|---|---|
| 0.2 | November 2026 | Maria Pabalan;<br>Daniel Moreira | Christopher Clarke | Updated following Maria Pabalan’s review comments. Pending final approval. |

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
| 3 | [Add/Remove Pages to Favorites](#3-addremove-pages-to-favorites) | O2C End-user | When setting up D365, or when a page is used often | D365 |
| 4 | [Create a Personalized View](#4-create-a-personalized-view) | O2C End-user | When a page does not show the information needed | D365 |
| 5 | [Update a Saved View](#5-update-a-saved-view) | O2C End-user | When a saved view needs a further change | D365 |
| 6 | [Export All Rows from a Grid](#6-export-all-rows-from-a-grid) | O2C End-user | When grid data is needed in Excel for internal analysis | D365; Excel |

### Roles and responsibilities

##### Overview

Every O2C user completes these tasks in their own D365 session.

| **Tasks / Business Roles** | O2C End-user |
|---|---|
| [1. Switch Legal Entity with the Selector](#1-switch-legal-entity-with-the-selector) | R |
| [2. Switch Legal Entity Using the Ledger Code](#2-switch-legal-entity-using-the-ledger-code) | R |
| [3. Add/Remove Pages to Favorites](#3-addremove-pages-to-favorites) | R |
| [4. Create a Personalized View](#4-create-a-personalized-view) | R |
| [5. Update a Saved View](#5-update-a-saved-view) | R |
| [6. Export All Rows from a Grid](#6-export-all-rows-from-a-grid) | R |

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
| **Legal entity** | A company set up in D365. The pages you open show data for the active legal entity, so you must work in the legal entity that holds the customer accounts you need. |
| **Business name** | The name of the business a legal entity represents. Use the business name to identify the legal entity you need. |
| **Ledger code** | The code D365 uses for a legal entity. D365 ledger codes differ from CargoWise ledger codes. |

##### Working in the correct legal entity

| Rule | Description |
|---|---|
| **Work with business names** | Identify legal entities by their business names rather than their ledger codes. |
| **Confirm before processing** | Confirm the active legal entity before you perform any transaction. |

##### What a view contains

| Term | Description |
|---|---|
| **View** | A saved layout for a page: the columns shown and their order, any filters and any footer totals. |
| **Default view** | The view you pin as the default for a page. |
| **View scope** | Views are set up separately for each page. When setting a default, choose whether it applies to the current legal entity or across all legal entities. |

##### Filter operators

| Filter Type | Filter Operator | What it does? |
|---|---|---|
| Text | **"is exactly"** | Matches the exact value, for example customer account 112A. |
| Text | **"is not"** | Excludes the exact value. |
| Text | **"contains"** | Matches any value containing the text entered. |
| Text | **"does not contain"** | Excludes values containing the text entered. |
| Text | **"begins with"** | Matches values starting with the text entered. |
| Text | **"ends with"** | Matches values ending with the text entered. |
| Text | **"is one of"** | Matches any of several values. Separate the values with commas. |
| Text | **"matches"** | Matches a pattern: \* represents any characters; ? represents one character. |
| Number | **"equals"** | Includes an exact amount; for example, equals 0 includes zero balances. |
| Number | **"does not equal"** | Excludes an exact amount; for example, does not equal 0 excludes zero balances. |
| Number | **"greater than"** | Matches values above the entered threshold. |
| Number | **"less than"** | Matches values below the entered threshold. |
| Number | **"between"** | Matches values within the entered range. |
| Number | **"is one of"** | Matches any value in a comma-separated list of specific numbers. |
| Date | **"is"** | Includes a specific date. |
| Date | **"is not"** | Excludes a specific date. |
| Date | **"before"** | Matches dates earlier than the date entered. |
| Date | **"after"** | Matches dates later than the date entered. |
| Date | **"between"** | Matches dates within the entered date range. |

##### Grid exports

| Term | Description |
|---|---|
| **Export all rows** | An option on the grid header that exports the grid's rows to an Excel file. |
| **Configured columns** | The export contains the columns configured on the grid. Add any column you need before you export. |
| **Export volume** | Limits apply to how much data can be exported. <mark>The limits for your environment are pending confirmation.</mark> `[Export to Excel VG-06]` |

##### Using exported data

| Rule | Description |
|---|---|
| **Internal analysis only** | Use exported data for internal analysis. Customer-facing invoices and account documents use the approved PDF output. Do not send a customer an Excel export. |
| **Exported customer data** | Exported files can contain customer information. Store and share them according to the approved data handling rules. `[Export to Excel VG-08]` |

---

## Part 2: How do I do it? (O2C Getting Started)

### 1. Switch Legal Entity with the Selector

##### Description

Use this procedure to switch to another legal entity (LE) with the legal entity selector in the D365 header. You find the legal entity by its business name, select it and confirm that it is active.

##### Responsibility

- O2C End-user: works in the legal entity required for the task.

##### Initiation

- An O2C user needs to work in a legal entity other than the one that is active.

##### Procedure

Complete these steps to switch legal entity with the selector:

| **Action** | **Description** |
|---|---|
| *PROCESS START* (light blue) | Pre-requisites:<br>• Access to D365 and to the required legal entity.<br>• The business name of the required legal entity.<br>Responsibility:<br>• O2C End-user |
| 1. *Click* the legal entity selector. `[Legal Entities VG-01]` | In the D365 header (top-right), click the legal entity selector. It shows the active legal entity. |
| 2. *Find* the required legal entity. `[Legal Entities VG-02]` | Find the legal entity by its business name. |
| 3. *Select* the legal entity. | Select the legal entity. D365 switches to it. |
| 4. *Confirm* the active legal entity. `[Legal Entities VG-04]` | Check that the selector now shows the required legal entity before you continue.<br>Note: you can also check the URL to determine which LE you are in; "https://wtg.operations.dynamics.com/?cmp=112a&mi=LedgerJournalTable_CustPaym" |
| *PROCESS COMPLETE* (light green) | Outcomes:<br>• D365 is working in the required legal entity. |

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
| *PROCESS START* (light blue) | Pre-requisites:<br>• Access to D365 and to the required legal entity.<br>• The D365 ledger code of the required legal entity.<br>Responsibility:<br>• O2C End-user |
| 1. *Click* the browser address bar. | Click the address bar to edit the D365 URL. |
| 2. *Find* the ledger code in the URL. `[Legal Entities VG-05]` | Find the cmp= parameter in the URL. The value immediately after cmp= is the D365 ledger code; in the example below it is 112a.<br>https://wtg.operations.dynamics.com/?cmp=112a&mi=LedgerJournalTable_CustPaym |
| 3. *Enter* the required ledger code. `[Legal Entities VG-06]` | Replace only the ledger code after cmp= with the required D365 ledger code. Leave the rest of the URL unchanged. Do not use the CargoWise code. |
| 4. *Press* **Enter**. | Press **Enter** to open D365 in the required legal entity. |
| 5. *Confirm* the active legal entity. | Check that the legal entity selector (top-right) shows the required legal entity before you continue. |
| *PROCESS COMPLETE* (light green) | Outcomes:<br>• D365 is working in the required legal entity. |

### 3. Add/Remove Pages to Favorites

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
| *PROCESS START* (light blue) | Pre-requisites:<br>• Access to D365 and to the module that contains the page. `[Favorites VG-17]`<br>• The **Navigation Pane** is visible.<br>Responsibility:<br>• O2C End-user |
| 1. *Check* the **Entity**. | Confirm you are signed into the correct **Legal Entity** (top-right). To change it, see [1. Switch Legal Entity with the Selector](#1-switch-legal-entity-with-the-selector). |
| 2. *Click* **Modules**. | From the left-hand **Navigation Pane**, click **Modules**. |
| 3. *Click* the module that contains the page. | From the list of modules, click the module, for example **Credit and collections** or **Accounts receivable**. The module menu opens. |
| 4. *Click* the favorite star for the page. `[Favorites VG-07]` `[Favorites VG-02 / VG-06]` | In the module menu, find the page and click its favorite star. The page is added to your **Favorites**.<br>Note: To add another page, repeat steps 2 to 4. |
| 5. *Click* **Favorites**. `[Favorites VG-09 / VG-28]` | From the left-hand **Navigation Pane**, click **Favorites**. Your favorites list is displayed. |
| 6. *Confirm* the page is listed. `[Favorites VG-13 / VG-16]` | Confirm that the page appears in your favorites list. If a module or page is not available to you, log a request through the D365 issue form (see **Additional Resources**). |
| 7. *Click* the page in your favorites list. | The page opens. |
| *PROCESS COMPLETE* (light green) | Outcomes:<br>• The page appears under **Favorites** in the **Navigation Pane**.<br>• The page opens from **Favorites**. |

##### Remove a Page from Favorites `[G260-08]`

| **Action** | **Description** |
|---|---|
| *PROCESS START* (light blue) | Pre-requisites:<br>• The page is already in your Favorites.<br>Responsibility:<br>• O2C End-user |
| 1. *Click* **Favorites**. | From the left-hand **Navigation Pane**, click **Favorites**. Your favorites list is displayed. |
| 2. *Confirm* the page is listed. | Find the page and click its selected star to remove it from Favorites. This does not remove the page or your access to it. |
| *PROCESS COMPLETE* (light green) | The page is removed from Favorites. You can still open it through its module menu. |

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
| [4.1 Arrange the Columns](#41-arrange-the-columns) | Add the columns you need, remove the ones you do not and reorder them so the most important information appears first. Output: the grid shows the columns you need, in your chosen order. |
| [4.2 Filter the List](#42-filter-the-list) | Optional. Limit the rows shown by filtering on a column value, for example to exclude zero balances or to include only certain customers. Output: the grid shows only the rows you need. |
| [4.3 Add a Footer Total](#43-add-a-footer-total) | Optional. Turn on the grid footer and add a sum to a column, such as an amount or balance column, so you can see the total at a glance. Output: the footer shows the total for the column. |
| [4.4 Save and Pin the View](#44-save-and-pin-the-view) | Save the layout as a named view and pin it as your default, so the page opens with your columns, filters and totals each time you use it. Output: a saved default view for the page. |

#### 4.1 Arrange the Columns

##### Procedure

Complete these steps to show the columns you need, in the order you need:

| **Action** | **Description** |
|---|---|
| *PROCESS START* (light blue) | Pre-requisites:<br>• Access to D365 and to the page you want to personalize.<br>Responsibility:<br>• O2C End-user |
| 1. *Check* the **Entity**. | Confirm you are signed into the correct **Legal Entity** (top-right). |
| 2. *Open* the page you want to personalize. `[Personalized Views VG-01]` | Open the page whose layout you want to save, for example a page in your **Favorites**. |
| 3. *Click* **Insert columns**. `[Personalized Views VG-03]` | Use **Insert columns** to add columns that the grid does not currently show. |
| 4. *Select* the columns to add. | Select each column you need for your work. Each process guide lists the columns recommended for its pages: for AR Collections, see 230 Collections Part 1. |
| 5. *Confirm* the selected columns are added to the grid. `[Personalized Views VG-04]` | Check that each selected column now appears in the grid. |
| 6. *Remove* each column you do not need. `[Personalized Views VG-05]` | Remove columns that are not needed for your work, so the grid stays readable. |
| 7. *Move* the columns into the order you need. `[Personalized Views VG-06]` | Reposition the columns so the information you check first appears first. |
| *STEP COMPLETE* (light blue) | • The grid shows the columns you need, in your rearranged order.<br>• Continue to [4.2 Filter the List](#42-filter-the-list) |

#### 4.2 Filter the List

##### Procedure

This subprocedure is optional. Complete it when the view should show only some rows. Otherwise, continue to [4.3 Add a Footer Total](#43-add-a-footer-total). Complete these steps to show only the rows you need:

| **Action** | **Description** |
|---|---|
| *PROCESS START* (light blue) | Pre-requisites:<br>• The grid shows the columns you need (see [4.1 Arrange the Columns](#41-arrange-the-columns)).<br>Responsibility:<br>• O2C End-user |
| 1. *Open* the filter for the column. `[Personalized Views VG-07]` | Open the filter for the column whose values you want to limit. |
| 2. *Select* the filter operator. `[Personalized Views VG-08]` | Select the operator that matches the rows you want. The available operators depend on whether the column contains text, numbers or dates.<br>Note: [See Filter operators in Key concepts for the full list](#filter-operators) |
| 3. *Enter* the filter value. | Enter the value or values for the selected operator. For example, to exclude zero balances, select does not equal (or not equal to, where shown) and enter 0. |
| 4. *Confirm* only the required rows are displayed. | Check that the grid shows only the rows that match the filter. |
| *STEP COMPLETE* (light blue) | • The grid shows only the rows you need.<br>• Continue to [4.3 Add a Footer Total](#43-add-a-footer-total) |

#### 4.3 Add a Footer Total

##### Procedure

This subprocedure is optional. Complete it when the view should show a total for a column. Otherwise, continue to [4.4 Save and Pin the View](#44-save-and-pin-the-view).

Complete these steps to show a column total in the grid footer:

| **Action** | **Description** |
|---|---|
| *PROCESS START* (light blue) | Pre-requisites:<br>• The grid shows the columns you need (see [4.1 Arrange the Columns](#41-arrange-the-columns)).<br>Responsibility:<br>• O2C End-user |
| 1. *Show* the grid footer. `[Personalized Views VG-09]` | Turn on the footer for the grid. |
| 2. *Hover* over the column footer. `[Personalized Views VG-10]` | Hover over the footer beneath the numeric column you want to total until the '+' symbol appears. |
| 3. *Click* the **+** symbol. | Open the **Calculate column** options for that column. |
| 4. *Select* **Sum**. | Select **Sum** in the **Calculate column** options to total the selected amount or balance column. |
| 5. *Confirm* the total is displayed. | Check that the footer shows the total for the column. |
| *STEP COMPLETE* (light blue) | • The footer shows the total for the column.<br>• Continue to [4.4 Save and Pin the View](#44-save-and-pin-the-view) |

#### 4.4 Save and Pin the View

##### Procedure

Complete these steps to save the layout as a named view and pin it as your default:

| **Action** | **Description** |
|---|---|
| *PROCESS START* (light blue) | Pre-requisites:<br>• The grid shows the columns, and any filters and totals, you need (see [4.1 Arrange the Columns](#41-arrange-the-columns)).<br>Responsibility:<br>• O2C End-user |
| 1. *Open* the view selector. | Above the grid, open the current view name (My View for a new personal view).<br>Note: An asterisk '\*' beside the view name indicates unsaved changes that can be saved. |
| 2. *Click* **Save as**. `[Personalized Views VG-11]` | In the view menu, select Save as to save the current layout as a new named view. |
| 3. *Enter* the view name. | Enter a name that identifies the page and the purpose of the view. |
| 4. *Save* the new view. `[Personalized Views VG-13]` | Save the view with the name you entered. |
| 5. *Select* **Pin as default**. `[Personalized Views VG-14]` | Pin the view as your default for this page. Select the option to use the default across all legal entities if that is the scope you need; otherwise keep the current-entity scope. `[G260-07]` |
| 6. *Confirm* the view is saved and pinned. `[Personalized Views VG-15]` | Check that your view is listed for this page and is set as the default. Ensure to also select the toggle to make this view the default view for all legal entities. |
| *PROCESS COMPLETE* (light green) | Outcomes:<br>• The page has a saved view with the columns, filters and totals you set. `[Personalized Views VG-18 / VG-19]`<br>• The view is pinned as your default for this page. |

### 5. Update a Saved View

##### Description

Use this procedure when a saved view needs a further change, such as an added column, a changed filter or a new total. You select the saved view, make the change and save it, so the view keeps the change the next time you use it.

##### Responsibility

- O2C End-user: maintains the views they have saved.

##### Initiation

- A saved view needs a further change.

##### Procedure

Complete these steps to update a saved view:

| **Action** | **Description** |
|---|---|
| *PROCESS START* (light blue) | Pre-requisites:<br>• A saved view for the page (see [4. Create a Personalized View](#4-create-a-personalized-view)).<br>Responsibility:<br>• O2C End-user |
| 1. *Check* the **Entity**. | Confirm you are signed into the correct **Legal Entity** (top-right). |
| 2. *Open* the page that has the saved view. | Open the page whose view you want to change. |
| 3. *Select* the saved view. `[Personalized Views VG-16]` | Open the view selector above the grid and select the saved view you want to change. |
| 4. *Make* the change to the layout. | Change the columns, filters or totals as described in [4. Create a Personalized View](#4-create-a-personalized-view). |
| 5. *Click* **Save**. `[Personalized Views VG-17]` | Open the view menu and select Save. An asterisk beside the view name indicates that the current layout has unsaved changes. |
| 6. *Confirm* the view shows the change. | Check that the selected view now includes the change. |
| *PROCESS COMPLETE* (light green) | Outcomes:<br>• The saved view includes the change. |

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
| *PROCESS START* (light blue) | Pre-requisites:<br>• Access to D365 and to the page that holds the data.<br>Responsibility:<br>• O2C End-user |
| 1. *Check* the **Entity**. | Confirm you are signed into the correct **Legal Entity** (top-right). |
| 2. *Open* the page that holds the data. | Open the D365 page whose grid holds the data you need, for example **Aged balances** from your **Favorites**. |
| 3. *Confirm* the grid shows the columns you need. | The export contains the columns configured on the grid. If a column is missing, add it with **Insert columns** (see [4.1 Arrange the Columns](#41-arrange-the-columns)). |
| 4. *Right-click* the grid header. `[Export to Excel VG-02]` | Right-click the header of any column in the grid. |
| 5. *Select* **Export all rows**. `[Export to Excel VG-01]` | Select **Export all rows** from the menu. |
| 6. *Download* the export. `[Export to Excel VG-03]` | Download the exported file when D365 has prepared it. |
| 7. *Open* the exported file. | Open the downloaded file in Excel. |
| 8. *Confirm* the required fields were exported. | Check that the file includes every field you need for your analysis. |
| *PROCESS COMPLETE* (light green) | Outcomes:<br>• The grid rows are exported to an Excel file with the configured columns.<br>• The file is used for internal analysis only. |

---

## Part 3: Reports (O2C Getting Started)

##### Overview

No reports apply to this guide. Each O2C process guide lists the reports for its process.

---

## Additional Resources

The standard template block, unchanged.
