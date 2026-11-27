# D365 F&O: Getting Started Procedure Guide

> **WORKING DRAFT v0.1. Not validated or approved.**
>
> Markdown preview of the Word guide [`CLAUDE-TBC-D365 F&O Getting Started PG v0.1.docx`](CLAUDE-TBC-D365%20F%26O%20Getting%20Started%20PG%20v0.1.docx), generated from it. Written from the [discovery](../05-project-notes/Discovery-Map.md) of 26 November 2026 (Microsoft Learn and the D365 documentation), not yet checked in our D365 environment. Markers such as `[GS-04]` show the open blocking items: in the Word file each has one review comment (D-067). The items are in the [validation register](../03-validation/D365-FO-Getting-Started-Validation.md). Notes to the author are <mark>highlighted</mark> (ACTION: REVIEW REQUIREMENT, D-060).
>
> The fixed template content (cover, Contents, *About this guide*, *Additional Resources*) is not repeated here.

**Version history**

| ID | Date | Author/s | BPO | Description of change |
|---|---|---|---|---|
| 0.1 | November 2026 | Daniel Moreira | Ken Lee | First draft from the discovery (draft) |

---

## Part 1: What do I need to know? (Getting Started)

### High-level process

##### Part Description

This guide covers the D365 skills that every D365 user needs before starting process work, whatever their stream: finding their way around the screen, opening pages, switching legal entity, working with records, filtering lists, saving personalized views, exporting to Excel, running reports, attaching documents, taking part in workflow approvals, setting up alerts and getting help. These tasks are not steps in a business process. Each process guide links to them and lists its own pages, workspaces, columns and views.

The steps come from Microsoft’s documentation and training for finance and operations apps (Microsoft Learn), checked against WiseTech Global’s D365 environment. Screen labels can differ slightly from one D365 release to the next. `[GS-02]`

The finance concepts that finance users need next (financial dimensions, journals, vouchers, posting periods and finding posted transactions) are in the D365 Finance Basics guide. <mark>Link to D365 Finance Basics when it is published.</mark> `[GS-03]`

This guide does not cover Copilot or the other AI features in D365.

##### Initiation
- A new user is setting up D365 before starting routine process work.
- A user needs a general D365 skill that their process guide refers to.

##### Stream

| Stream | Process Area | Key Roles |
|---|---|---|
| All streams | D365 F&O Getting Started, for Order to Cash (O2C), Procure to Pay (P2P), Record to Report (R2R) and Tax | • D365 End-user |

##### Process

The high-level process is as follows:

| # | Action | Who | When | Where |
|---|---|---|---|---|
| 1 | Set Up Your D365 Session | D365 End-user | When a user starts using D365, and when their settings need to change | D365 |
| 2 | Open a Page | D365 End-user | Whenever a page or workspace is needed for a task | D365 |
| 3 | Switch Legal Entity | D365 End-user | When work is needed in a legal entity other than the active one | D365 |
| 4 | Work with Records | D365 End-user | When a record needs to be viewed, created, changed or deleted | D365 |
| 5 | Find Records with Filters | D365 End-user | When a list shows more records than the task needs | D365 |
| 6 | Create a Personalized View | D365 End-user | When a page does not show the information needed in the way it is needed | D365 |
| 7 | Manage Saved Views and Personalizations | D365 End-user | When a saved view or a page layout needs to change, or be reset | D365 |
| 8 | Export Data and Work in Excel | D365 End-user | When page data is needed in Excel | D365; Excel |
| 9 | Run a Report | D365 End-user | When a report is needed on screen, as a file or in the background | D365 |
| 10 | Attach a Document | D365 End-user | When a file, note or link must be kept with a record | D365 |
| 11 | Submit and Approve Workflow Items | D365 End-user | When a document needs approval, or a work item is assigned to the user | D365 |
| 12 | Set Up an Alert | D365 End-user | When the user needs to know that a record has changed or a date is due | D365 |
| 13 | Get Help and Report a Problem | D365 End-user | When a message appears, help is needed, or something does not work | D365 |

> **Note:** The topics can be read in any order. A new user should read topics 1 to 5 first: they are used in every other topic and in every process guide.

### Roles and responsibilities

##### Overview

Every D365 user completes these tasks in their own D365 session. In workflow, the same user can be the person who submits a document or the person a work item is assigned to; topic 11 covers both.

| **Tasks / Business Roles** | D365 End-user |
|---|---|
| 1. Set Up Your D365 Session | R |
| 2. Open a Page | R |
| 3. Switch Legal Entity | R |
| 4. Work with Records | R |
| 5. Find Records with Filters | R |
| 6. Create a Personalized View | R |
| 7. Manage Saved Views and Personalizations | R |
| 8. Export Data and Work in Excel | R |
| 9. Run a Report | R |
| 10. Attach a Document | R |
| 11. Submit and Approve Workflow Items | R |
| 12. Set Up an Alert | R |
| 13. Get Help and Report a Problem | R |

*R = Responsible

### Key concepts

##### Overview

Before you start, you need to know the parts of the D365 screen, how legal entities work, what the system messages mean, how filters and views behave, and the difference between the ways of getting data out of D365. Each concept below supports one or more topics in Part 2.

##### The parts of the screen

Every procedure in this guide and in the process guides uses these names. Learn them first.

| Element | Where it is | What it is for |
|---|---|---|
| **Navigation bar** | The bar across the top of the screen | Holds the legal entity selector (it shows the active ledger code, for example **100A**), **Search for a page** (magnifying glass), the **Action center** (bell), **Settings** (gear), **Help & Support** (?) and your initials. |
| **Navigation Pane** | The pane on the left | Opens any page: **Home**, **Favorites**, **Recent**, **Workspaces** and **Modules**. |
| **Dashboard** | The first page after you sign in | Shows a calendar, your **Work items assigned to me**, and tiles for apps and workspaces. Return to it from the **Home** button in the **Navigation Pane**. |
| **Workspace** | Opened from a tile or from **Workspaces** | An activity page for one area of work: summary tiles with counts, tabbed lists and links to related pages. |
| **Action Pane** | The bar below the navigation bar, on every page | Holds the buttons and tabs for the page, such as **Edit**, **New**, **Delete** and **Options**, and **Action search**. |
| **Message bar** | Below the Action Pane | Shows information, warnings and errors about the page you are on. |
| **Grid** | The centre of a list page | Rows of records and columns of data. You filter, sort and select rows here. |
| **FastTab** | On a record’s details page | A section of fields that expands and collapses. |
| **FactBox** | The pane on the right of some pages | Related information about the selected record, such as balances or contacts. |

<mark>Microsoft Learn example (demo data): A customer page with the parts of the screen labelled. Replace with a WTG screenshot.</mark> `[GS-28]`

<mark>Microsoft Learn example (demo data): The navigation bar, Action Pane and Navigation Pane, labelled. Replace with a WTG screenshot.</mark>

##### Pages and views

| Page type or view | What it shows | Use it to |
|---|---|---|
| **List page (Grid view)** | Many records in a grid | Find, filter and select records, and change several records without opening each one. |
| **Details page (Details view)** | One record, in FastTabs | Review or change one record. A narrow list on the left moves between records. |
| **Header view and Lines view** | A document such as a journal or an order | **Header** holds the document’s main fields; **Lines** holds its lines. |
| **Dialog** | A pane that opens over the page | Enter the details of an action, then select **OK** or **Cancel**. |

##### Legal entities

| Term | Description |
|---|---|
| **Legal entity** | A company set up in D365. The pages you open show the data of the active legal entity only, and the records you create belong to it. |
| **Business name** | The name of the business a legal entity represents. Use it to identify the legal entity you need. |
| **Ledger code** | The code D365 uses for a legal entity. It appears in the legal entity selector and in the D365 URL after **cmp=**. D365 ledger codes differ from CargoWise ledger codes. |
| **Default company** | The legal entity D365 opens in when you sign in. You set it in your user options (topic 1.2). |

##### Working in the correct legal entity
- Check the active legal entity before you create, change or post anything. A record created in the wrong legal entity belongs to that entity.
- Identify legal entities by their business names rather than their ledger codes.
- A page opened in a new window keeps the legal entity it was opened in, so two windows can show different legal entities.

##### What you can see in D365

The pages, workspaces, legal entities and buttons you see depend on your D365 profile, which your manager requests for you. It gives you the access your role needs. If a page, module, legal entity or button that your process guide mentions is missing, or a message says you do not have access, contact the BAU Support team (topic 13.3).

##### System messages

D365 tells you about problems and results in four places. Where a message appears tells you what caused it.

| Where it appears | What it tells you | What to do |
|---|---|---|
| **Message bar (below the Action Pane)** | Information, a warning or an error about the page you are on, usually about the data you entered. | Read it before you continue. Fix the field it names, then save again. Select **Message details** where shown to see every message. |
| **Message box (over the page)** | An error that stops the action. | Read it, select the button it offers, then fix the cause. |
| **Action center (bell on the navigation bar)** | The result of work that ran in the background, such as a report or a batch job, and your alerts. | Open the bell to read new messages. It keeps up to 500 messages. |
| **Feature callout** | A short pop-up next to a control that introduces a new feature. | Select **Got it** to close it. |

<mark>Microsoft Learn example (demo data): Information, warning and error messages in the message bar. Replace with a WTG screenshot.</mark>

| Message type | Meaning |
|---|---|
| **Information** | Tells you something. Usually no action is needed. |
| **Warning** | The data may cause a problem later. Check it before you continue. |
| **Error** | The action failed. Fix the cause before you try again. |

##### Filter operators

The column filter and the Filter pane offer operators. The operators shown depend on whether the column holds text, numbers or dates.

| Operator | What it finds | Typed as (with matches) |
|---|---|---|
| **is exactly / is equal to** | The exact value. | circle |
| **is not / is not equal to** | Every value except this one. | !circle |
| **is one of** | Any of several values, separated by commas. | circle,square |
| **contains** | Values that contain the text. | *circle* |
| **does not contain** | Values that do not contain the text. | !*circle* |
| **begins with** | Values that start with the text. | circle* |
| **after / greater than** | Values above the one entered. | >100 |
| **greater than or equal** | Values from the one entered upwards. | 100.. |
| **before / less than** | Values below the one entered. | <100 |
| **less than or equal** | Values up to the one entered. | ..100 |
| **between** | Values from the first to the second. | 100..200 |
| **matches** | The pattern you type, using the symbols in the next table. | See below |

##### Query symbols

The symbols below work only with the **matches** operator. With any other operator, D365 searches for the symbol as plain text: **matches A*** finds names that start with A, while **is exactly A*** finds only the text “A*”.

| Type | Finds | Example |
|---|---|---|
| **value*** | Values that start with the text. | **S*** finds Sydney and San Francisco. |
| ***value** | Values that end with the text. | ***east** finds Northeast. |
| ***value*** | Values that contain the text. | ***th*** finds Northeast and Southeast. |
| **?** | An unknown character at that position. | **Sm?th** finds Smith and Smyth. |
| **!value** | Every value except this one. | **!Smith** |
| **value,value** | Any of the values listed. | **A,D,F** |
| **from..to** | Values from the first to the second. | **1..10**; for text, **A..C** finds values starting with A or B, and exactly C. |
| **""** | Blank values. | Two double quotes find rows with no value in the column. |
| **T** | Today’s date. | **T** in a date column. |

##### Relative dates

A filter with a fixed date keeps that date in a saved view for ever. A relative date, typed with **matches** and in brackets, is worked out again each time the view opens, so the view stays current.

| Type | Finds |
|---|---|
| **(Day(0))** | Today. (Day(-1)) is yesterday and (Day(1)) tomorrow. |
| **(DayRange(-30,0))** | The last 30 days, up to today. |
| **(LessThanDate(0))** | Dates before today, for example overdue due dates. |
| **(GreaterThanDate(30))** | Dates more than 30 days from today. |
| **(MonthRange(-2,0))** | The previous two months and this month. |
| **(YearRange(-1,0))** | The previous year and this year. |

##### Views and personalization

| Term | Description |
|---|---|
| **View** | A named, saved layout of a page. On a list page it also holds filters, sorting and grouping. The view name shows above the grid. |
| **Standard view** | The view D365 provides. It cannot be changed: save your changes as a new view. |
| **Asterisk (*) after the view name** | The page has changes that are not saved in the view yet. Switching to another view discards them. |
| **Locked view (padlock)** | A view that cannot be edited, such as **Standard** or a view published to you. **Save as** makes your own copy. |
| **Default view** | The view a page opens in. You set it with **Pin as default**, for the current legal entity or for all legal entities. |
| **Saved for you automatically** | Column widths, footer totals and expanded or collapsed FastTabs are remembered for each view without saving. |
| **Saved only when you save the view** | Columns added, hidden or moved, filters, sorting and grouping. |

> **Note:** A page opened from a workspace tile, or from a menu item that has its own filter (for example a list of customers on hold), opens with that filter instead of your default view.

##### Getting data into Excel

| Tool | What you get | Use it when |
|---|---|---|
| **Export to Excel (Export all rows)** | A one-off copy of the grid as it is shown: the same columns, filter and values. It cannot be refreshed or sent back to D365. | You need the data for analysis or a report outside D365. |
| **Open in Excel** | A live workbook linked to D365 through the Microsoft Dynamics Office Add-in. You can refresh it, and change rows and publish them back. | Your process guide tells you to update records from Excel. |

> **Important:** Exported files can hold confidential company and customer data. Keep them in an approved WiseTech Global location and delete them when you no longer need them. `[[Q01] GS-19: Confirm]`

##### Report destinations

| Destination | What happens | In the background? |
|---|---|---|
| **Screen** | The report opens in the PDF viewer, where you can download or print it. This is the default. | No |
| **File** | The report is saved in the format you choose, such as PDF or Excel, and downloaded. | No |
| **Print archive** | A copy is stored in the **Print archive**, where you open it later. | Yes |
| **Email** | The report is sent as an attachment. | Yes |
| **Printer** | The report prints on a network printer set up for D365. | Yes |

##### Workflow

A workflow routes a document, such as a journal or a vendor invoice, to the people who must review or approve it. The steps, approvers and buttons you see depend on how each workflow is set up, so your process guide says which workflow applies.

| Term | Description |
|---|---|
| **Originator** | The person who submits the document to workflow. |
| **Work item** | A task, review or approval that the workflow assigns to you. It appears in **Work items assigned to me**. |
| **Approver** | A person who approves, rejects, requests a change or delegates the work item. |
| **Workflow history** | The record of the document in workflow: who submitted and acted on it, when, and their comments. |
| **Delegate** | Give a work item to another user, who acts on your behalf. |

> **Note:** Workflow email notifications do not appear in the **Action center**. Check **Work items assigned to me** on the dashboard.

##### Keyboard shortcuts

To see the shortcuts for a page, right-click anywhere on the page and select **View shortcuts**. The list groups them under **Navigate**, **Act on data**, **Close** and **Other**. Pressing **Alt+Shift+K** shows a similar list that starts with **Shortcuts for selected element**: it changes with the part of the page you are on. **View all product shortcuts** opens Microsoft’s full list.

| Shortcut | What it does (as D365 labels it) |
|---|---|
| **Alt+G** | Search for a page |
| **Alt+Q** | Search for an action |
| **Ctrl+Shift+O** | Change company (legal entity) |
| **Alt+Shift+Home** | Go to the dashboard |
| **Alt+F1** | Open navigation pane |
| **F2** | Switch to edit mode |
| **Alt+N** | Create a new record |
| **Alt+S** | Save record |
| **Alt+Delete** | Delete record |
| **Ctrl+Shift+F5** | Revert any changes |
| **Shift+F5** | Refresh data |
| **Ctrl+Shift+M** | Select or clear all rows |
| **Ctrl+Shift+G / Ctrl+Shift+D** | Switch to grid view / details view |
| **Alt+M, F** | Go to the filter pane |
| **Ctrl+Shift+F3** | Open advanced filtering and sorting options |
| **Ctrl+Shift+P** | Personalize this page |
| **Ctrl+Shift+E** | Export to Excel |
| **Ctrl+Shift+F7** | Open message center |
| **Esc** | Close the page |
| **Shift+Esc** | Save changes and close the page |
| **Alt+Shift+Q** | Close the page and discard any unsaved changes |

These shortcuts work inside a field or a grid: `[GS-07]`

| Shortcut | What it does |
|---|---|
| **Ctrl+G** | Filter the current grid column |
| **Alt+Down arrow** | Open a lookup or date picker |
| **T / D** | In a date field: today / the session date |
| **Ctrl+Shift+A** | Attach a document to the record |

---

## Part 2: How do I do it? (Getting Started)

### 1. Set Up Your D365 Session

##### Description

Use this topic to sign in to D365, set the user options that control how D365 opens and shows dates and numbers, and change the session date when a task needs a different date.

##### Responsibility
- D365 End-user: sets up and manages their own D365 session.

##### Initiation
- A new user starts using D365, or a user needs to change their settings or the session date.

##### Topic Overview

This topic includes these steps:

| Step | Description |
|---|---|
| 1.1 Sign In and Sign Out | Open D365 in the browser, sign in with your work account, and sign out when you finish. |
| 1.2 Set Your User Options | Set your default legal entity, start page, language, date and number format, and time zone. |
| 1.3 Change the Session Date | Optional. Change the date D365 uses by default for the current session, then reset it. |

#### 1.1 Sign In and Sign Out

##### Description

Use this procedure to open D365 in your browser and sign in with your WiseTech Global work account, and to sign out at the end of your work. D365 runs in a web browser; Microsoft recommends the latest Microsoft Edge.

##### Responsibility
- D365 End-user: completes this task in their own D365 session.

##### Initiation
- A user starts or finishes their D365 work.

##### Procedure

Complete these steps to sign in to D365:

| **Action** | **Description** |
|---|---|
| *PROCESS START* | Pre-requisites:<br>• Your manager has requested your D365 profile.<br>• A supported browser, such as Microsoft Edge.<br>Responsibility:<br>• D365 End-user |
| 1. *Open* your browser. | Open Microsoft Edge (recommended) or another supported browser. |
| 2. *Enter* the **D365 URL**. `[GS-04]` | Enter the D365 address in the address bar: https://wtg.operations.dynamics.com/. Add it to your browser favorites so you can open it quickly. |
| 3. *Sign in* with your work account. | Sign in with your WiseTech Global email address and password, and approve the sign-in request if one is shown. |
| 4. *Confirm* the **Dashboard** is displayed. | D365 opens on the dashboard, or on the initial page set in your user options, in your default legal entity.<br><mark>Microsoft Learn example (demo data): The default dashboard after sign-in. Replace with a WTG screenshot.</mark> |
| 5. *Select* your initials to sign out. | When you finish, select your initials at the right of the navigation bar, then select **Sign out**. Save your work first. |
| *STEP COMPLETE* | You are signed in to D365.<br>Continue to 1.2 Set Your User Options |

> **Note:** D365 signs you out after a period without activity. A countdown message appears first: select it to stay signed in. Unsaved changes are lost when the session closes.

#### 1.2 Set Your User Options

##### Description

Use this procedure to set the options that apply to you on every page: the legal entity D365 opens in, the page it opens on, and your language, date, time, number format and time zone. Changes take effect when you save.

##### Responsibility
- D365 End-user: sets their own user options.

##### Initiation
- A new user sets up D365, or a user’s legal entity, location or preferences change.

##### Procedure

Complete these steps to set your user options:

| **Action** | **Description** |
|---|---|
| *PROCESS START* | Pre-requisites:<br>• You are signed in to D365 (see 1.1 Sign In and Sign Out).<br>Responsibility:<br>• D365 End-user |
| 1. *Click* **Settings**. | On the navigation bar, click **Settings** (the gear icon). |
| 2. *Select* **User options**. | Select **User options**. The **Options** page opens on the **Visual** tab, where you can choose a colour theme and the size of page elements. |
| 3. *Click* the **Preferences** tab. | Click **Preferences**.<br><mark>Microsoft Learn example (demo data): User options, Preferences tab: Startup and language settings. Replace with a WTG screenshot.</mark> |
| 4. *Select* the **Company**. | On the **Startup** FastTab, select in **Company** the legal entity D365 opens in when you sign in. |
| 5. *Select* the **Initial page**. | Select the page D365 opens on, for example **Default dashboard**. |
| 6. *Check* the **Default view/edit mode**. `[GS-05]` | Leave the default unless your process guide says otherwise. It controls whether pages open locked for viewing or ready for editing. |
| 7. *Select* the **Language**. | On the **Language and country/region preferences** FastTab, select your **Language**. |
| 8. *Select* the **Date, time, and number format**. | Select the format for your country, for example **en-AU**. |
| 9. *Select* the **Time zone**. | Select the time zone you work in, so dates and times show in your local time. |
| 10. *Click* **Save**. | Click **Save**. The options apply from now on. |
| *PROCESS COMPLETE* | Outcomes:<br>• D365 opens in your default legal entity and on your initial page, and shows dates, times and numbers in your format and time zone. |

#### 1.3 Change the Session Date

##### Description

Use this procedure to change the date D365 uses by default for the current session, for example when a process guide tells you to enter transactions with an earlier date. The session date is the default date for new journals and documents. It applies to your current session only and returns to today when you sign out or the session closes.

##### Responsibility
- D365 End-user: changes the session date only when their task requires it.

##### Initiation
- A process guide tells you to work with a date other than today.

##### Procedure

Complete these steps to change the session date:

| **Action** | **Description** |
|---|---|
| *PROCESS START* | Pre-requisites:<br>• You are signed in to D365.<br>• Your process guide tells you to use a different date.<br>Responsibility:<br>• D365 End-user |
| 1. *Click* **Modules**. | From the left-hand **Navigation Pane**, click **Modules**. |
| 2. *Navigate* to the **Session date and time** page. | From the **Navigation Pane**, *select*:<br>• **Common >**<br>• **Common >**<br>• **Session date and time** |
| 3. *Enter* the **Date**. | Enter the date your process guide gives. |
| 4. *Click* **OK**. | Click **OK**. New records in this session now default to that date. |
| 5. *Reset* the session date when you finish. | Repeat steps 1 to 4 with today’s date, or sign out, so later work is not dated by mistake. |
| *PROCESS COMPLETE* | Outcomes:<br>• D365 uses the date you entered as the default date for the rest of the session. |

> **Important:** A wrong session date gives new journals and documents the wrong date. Change it only when your process guide tells you to, and reset it as soon as you finish. `[[Q02] GS-06: Confirm]`

### 2. Open a Page

##### Description

Use this topic to open the pages and workspaces you need: from the Navigation Pane, with the page search, from your Favorites, or from a workspace. Each process guide gives the path to its own pages.

##### Responsibility
- D365 End-user: opens the pages their work needs.

##### Initiation
- A user needs a page or workspace for a task.

##### Topic Overview

This topic includes these steps:

| Step | Description |
|---|---|
| 2.1 Open a Page from the Navigation Pane | Open a page from its module menu, or from Recent. |
| 2.2 Search for a Page | Find a page by typing part of its name. |
| 2.3 Add/Remove Pages to Favorites | Mark the pages you use often, and remove them when you no longer need them. |
| 2.4 Work from a Workspace | Open a workspace and use its tiles, lists and links. |

#### 2.1 Open a Page from the Navigation Pane

##### Description

Use this procedure to open a page from its module menu in the Navigation Pane. Every process guide gives the path as a list of menu levels, for example **Accounts receivable > Customers > All customers**.

##### Responsibility
- D365 End-user: opens the pages their work needs.

##### Initiation
- A user needs a page and knows its navigation path.

##### Procedure

Complete these steps to open a page from the Navigation Pane:

| **Action** | **Description** |
|---|---|
| *PROCESS START* | Pre-requisites:<br>• Access to D365.<br>• The navigation path of the page, from your process guide.<br>Responsibility:<br>• D365 End-user |
| 1. *Check* the **Entity**. | Confirm you are signed into the correct **Legal Entity** (top-right). To change it, see 3.1 Switch Legal Entity with the Selector. |
| 2. *Click* **Modules**. | From the left-hand **Navigation Pane**, click **Modules**. If the pane is closed, click the menu icon at its top. |
| 3. *Click* the module. | Click the first level of the path, for example **Accounts receivable**. The module menu opens.<br><mark>Microsoft Learn example (demo data): A module menu open in the Navigation Pane. Replace with a WTG screenshot.</mark> |
| 4. *Click* the page. | Find the page under its menu heading, for example **Customers > All customers**, and click it. |
| 5. *Confirm* the page is open. | Check the page title. If the module or page is not shown, contact the BAU Support team (topic 13.3). |
| *PROCESS COMPLETE* | Outcomes:<br>• The page is open in the active legal entity. |

> **Note:** **Recent** in the **Navigation Pane** lists the pages you opened most recently. Use it to return to a page quickly.

#### 2.2 Search for a Page

##### Description

Use this procedure to find a page or workspace by typing words from its name. The search finds pages, not data: to find a customer, vendor or invoice, open its list page and filter it (topic 5).

##### Responsibility
- D365 End-user: finds pages by name.

##### Initiation
- A user needs a page but does not know, or does not want to follow, its navigation path.

##### Procedure

Complete these steps to search for a page:

| **Action** | **Description** |
|---|---|
| *PROCESS START* | Pre-requisites:<br>• Access to D365.<br>Responsibility:<br>• D365 End-user |
| 1. *Click* **Search for a page**. | On the navigation bar, click **Search for a page** (the magnifying glass), or press **Alt+G**. |
| 2. *Type* words from the page name. | Type one or more words, for example **payment journal**. Each result shows the page name and its navigation path.<br><mark>Microsoft Learn example (demo data): Search for a page: results with their navigation paths. Replace with a WTG screenshot.</mark> |
| 3. *Select* the page. | Select the page in the results. If it is not listed, add or change words: the search shows up to 10 results. |
| 4. *Confirm* the page is open. | Check the page title before you continue. |
| *PROCESS COMPLETE* | Outcomes:<br>• The page is open. |

#### 2.3 Add/Remove Pages to Favorites

##### Description

Use this procedure to add a D365 page to your Favorites, so that it opens directly from **Favorites** in the **Navigation Pane**, and to remove it when you no longer need it. Each process guide lists the pages worth adding for its work.

##### Responsibility
- D365 End-user: adds the pages they use to their own Favorites.

##### Initiation
- A new user sets up D365, or a page is used often.

##### Procedure

Complete these steps to add a page to your Favorites:

| **Action** | **Description** |
|---|---|
| *PROCESS START* | Pre-requisites:<br>• Access to D365 and to the module that contains the page.<br>Responsibility:<br>• D365 End-user |
| 1. *Check* the **Entity**. | Confirm you are signed into the correct **Legal Entity** (top-right). To change it, see 3.1 Switch Legal Entity with the Selector. |
| 2. *Click* **Modules**. | From the left-hand **Navigation Pane**, click **Modules**. |
| 3. *Click* the module that contains the page. | Click the module, for example **Accounts payable**. The module menu opens. |
| 4. *Click* the favorite star for the page. | In the module menu, find the page and click the star next to it. The page is added to your **Favorites**.<br>Note: To add another page, repeat steps 2 to 4.<br><mark>Microsoft Learn example (demo data): The favorite star next to a page in a module menu. Replace with a WTG screenshot.</mark> |
| 5. *Click* **Favorites**. | From the left-hand **Navigation Pane**, click **Favorites**. Your favorites list is displayed. |
| 6. *Confirm* the page is listed. | Confirm that the page appears in your favorites list. |
| *PROCESS COMPLETE* | Outcomes:<br>• The page appears under **Favorites** in the **Navigation Pane** and opens from there. |

##### Remove a Page from Favorites

Complete these steps to remove a page from your Favorites:

| **Action** | **Description** |
|---|---|
| *PROCESS START* | Pre-requisites:<br>• The page is in your Favorites.<br>Responsibility:<br>• D365 End-user |
| 1. *Click* **Favorites**. | From the left-hand **Navigation Pane**, click **Favorites**. |
| 2. *Click* the star for the page. | Click the filled star next to the page. The page is removed from Favorites; your access to it does not change. |
| *PROCESS COMPLETE* | Outcomes:<br>• The page is no longer in your Favorites. It still opens from its module menu. |

#### 2.4 Work from a Workspace

##### Description

Use this procedure to open a workspace and use its parts. A workspace brings together the work of one area, for example customer payments or vendor invoices: summary tiles with counts, tabbed lists of records that need action, and links to related pages. Selecting a tile or a list row opens the records behind it.

##### Responsibility
- D365 End-user: starts their work from the workspace for their area.

##### Initiation
- A user starts work in an area that has a workspace, as their process guide describes.

##### Procedure

Complete these steps to work from a workspace:

| **Action** | **Description** |
|---|---|
| *PROCESS START* | Pre-requisites:<br>• Access to D365 and to the workspace.<br>Responsibility:<br>• D365 End-user |
| 1. *Check* the **Entity**. | Confirm you are signed into the correct **Legal Entity** (top-right). To change it, see 3.1 Switch Legal Entity with the Selector. |
| 2. *Click* **Workspaces**. | From the left-hand **Navigation Pane**, click **Workspaces**, or select the workspace tile on the dashboard. |
| 3. *Select* the workspace. | Select the workspace your process guide names. |
| 4. *Review* the summary tiles. | Each tile shows a count of records, for example unposted journals. Click a tile to open the list of those records.<br><mark>Microsoft Learn example (demo data): A workspace: summary tiles, Filter box, tabbed lists and links. Replace with a WTG screenshot.</mark> |
| 5. *Select* a tab in the lists. | In the workspace lists, select a tab to see the records it holds. Use the **Filter** box above the list to narrow it. |
| 6. *Click* a link. | Optional. Under **Links**, click a page to open it. |
| 7. *Return* to the dashboard. | When you finish, click **Home** in the **Navigation Pane**, or press **Alt+Shift+Home**. |
| *PROCESS COMPLETE* | Outcomes:<br>• You have opened the records or pages you need from the workspace. |

> **Note:** Some workspaces have a filter at the top that applies to the whole workspace, and a button on the Action Pane that sets them up for you. Your process guide explains the settings for its workspace.

### 3. Switch Legal Entity

##### Description

Use this topic to change the legal entity you are working in. Every page shows the data of the active legal entity, so check it before every task and switch when the task needs another one.

##### Responsibility
- D365 End-user: works in the legal entity required for the task.

##### Initiation
- A user needs to work in a legal entity other than the active one.

##### Topic Overview

This topic includes these steps:

| Step | Description |
|---|---|
| 3.1 Switch Legal Entity with the Selector | Select the legal entity by its business name in the legal entity selector. |
| 3.2 Switch Legal Entity Using the Ledger Code | Change the ledger code in the D365 URL when the code is known. |

#### 3.1 Switch Legal Entity with the Selector

##### Description

Use this procedure to switch to another legal entity with the legal entity selector on the navigation bar. It is the usual way to switch, and it lets you find the legal entity by its business name.

##### Responsibility
- D365 End-user: works in the legal entity required for the task.

##### Initiation
- A user needs to work in a legal entity other than the active one.

##### Procedure

Complete these steps to switch legal entity with the selector:

| **Action** | **Description** |
|---|---|
| *PROCESS START* | Pre-requisites:<br>• Access to D365 and to the required legal entity.<br>• The business name of the required legal entity.<br>Responsibility:<br>• D365 End-user |
| 1. *Click* the legal entity selector. | On the navigation bar (top-right), click the legal entity selector. It shows the active legal entity. You can also press **Ctrl+Shift+O**. |
| 2. *Find* the required legal entity. | Find the legal entity by its business name, or type part of the name or ledger code to narrow the list.<br><mark>Microsoft Learn example (demo data): The legal entity selector open, listing legal entities. Replace with a WTG screenshot.</mark> |
| 3. *Select* the legal entity. | Select the legal entity. D365 switches to it. |
| 4. *Confirm* the active legal entity. | Check that the selector now shows the required legal entity before you continue.<br>Note: The ledger code also shows in the URL after **cmp=**, for example https://wtg.operations.dynamics.com/?cmp=112a. |
| *PROCESS COMPLETE* | Outcomes:<br>• D365 is working in the required legal entity. |

> **Note:** If a legal entity you need is not in the list, contact the BAU Support team (topic 13.3).

#### 3.2 Switch Legal Entity Using the Ledger Code

##### Description

Use this procedure to switch legal entity by changing the ledger code in the D365 URL, when you know the D365 ledger code. It is quicker when you move between legal entities often.

##### Responsibility
- D365 End-user: works in the legal entity required for the task.

##### Initiation
- The D365 ledger code of the required legal entity is known, and switching through the URL is quicker.

##### Procedure

Complete these steps to switch legal entity using the ledger code:

| **Action** | **Description** |
|---|---|
| *PROCESS START* | Pre-requisites:<br>• Access to D365 and to the required legal entity.<br>• The D365 ledger code of the required legal entity.<br>Responsibility:<br>• D365 End-user |
| 1. *Click* the browser address bar. | Click the address bar to edit the D365 URL. |
| 2. *Find* the ledger code in the URL. | Find **cmp=** in the URL. The value immediately after **cmp=** is the D365 ledger code; in this example it is 112a:<br>https://wtg.operations.dynamics.com/?cmp=112a&mi=LedgerJournalTable_CustPaym |
| 3. *Enter* the required ledger code. | Replace only the ledger code after **cmp=** with the required D365 ledger code. Leave the rest of the URL unchanged. Do not use the CargoWise code. |
| 4. *Press* **Enter**. | Press **Enter** to open D365 in the required legal entity. |
| 5. *Confirm* the active legal entity. | Check that the legal entity selector (top-right) shows the required legal entity before you continue. |
| *PROCESS COMPLETE* | Outcomes:<br>• D365 is working in the required legal entity. |

### 4. Work with Records

##### Description

Use this topic to change, create and delete records, to enter values with lookups and date pickers, and to run any button on a page with action search. Most pages open locked for viewing, so that data is not changed by accident: you switch to Edit mode to make changes.

##### Responsibility
- D365 End-user: views and maintains the records their role allows.

##### Initiation
- A user needs to change, create or delete a record, or to run an action on a page.

##### Topic Overview

This topic includes these steps:

| Step | Description |
|---|---|
| 4.1 Edit, Save and Revert a Record | Switch to Edit mode, change a record and save it, or undo unsaved changes. |
| 4.2 Create and Delete a Record | Add a new record, or delete one. |
| 4.3 Enter Values with Lookups and Date Pickers | Choose valid values from a lookup and dates from a date picker. |
| 4.4 Run an Action with Action Search | Find and run a button on the page by typing its name. |

#### 4.1 Edit, Save and Revert a Record

##### Description

Use this procedure to change a record and save the change, or to undo changes you have not saved. In View mode the Action Pane shows **Edit**; in Edit mode it shows **Save**.

##### Responsibility
- D365 End-user: changes records their role allows them to change.

##### Initiation
- A record needs to change, as a process guide describes.

##### Procedure

Complete these steps to edit and save a record:

| **Action** | **Description** |
|---|---|
| *PROCESS START* | Pre-requisites:<br>• The record is open (see 2.1 Open a Page from the Navigation Pane).<br>Responsibility:<br>• D365 End-user |
| 1. *Check* the **Entity**. | Confirm you are signed into the correct **Legal Entity** (top-right). To change it, see 3.1 Switch Legal Entity with the Selector. |
| 2. *Click* **Edit**. | On the Action Pane, click **Edit**, or press **F2**. The fields you can change become editable. If **Edit** is not shown, the page is always editable or always read-only.<br><mark>Microsoft Learn example (demo data): The Action Pane with Edit, New and Delete. Replace with a WTG screenshot.</mark> |
| 3. *Enter* the change. | Change the fields your process guide gives. Read any message that appears in the message bar. |
| 4. *Click* **Save**. `[GS-09]` | On the Action Pane, click **Save**, or press **Alt+S**. |
| 5. *Confirm* the record is saved. | Check that no error shows in the message bar and the changed values remain. To undo changes you have not saved, select **Revert** on the **Options** tab of the Action Pane, or press **Ctrl+Shift+F5**. |
| *PROCESS COMPLETE* | Outcomes:<br>• The record shows the change, saved. |

#### 4.2 Create and Delete a Record

##### Description

Use this procedure to add a new record, or to delete one, on a page where your process guide tells you to. A deleted record cannot be restored, so check it before you delete.

##### Responsibility
- D365 End-user: creates and deletes records their role allows.

##### Initiation
- A process guide tells the user to create or delete a record.

##### Procedure

Complete these steps to create a record:

| **Action** | **Description** |
|---|---|
| *PROCESS START* | Pre-requisites:<br>• The page is open in the required legal entity.<br>Responsibility:<br>• D365 End-user |
| 1. *Check* the **Entity**. | Confirm you are signed into the correct **Legal Entity** (top-right). To change it, see 3.1 Switch Legal Entity with the Selector. |
| 2. *Click* **New**. | On the Action Pane, click **New**, or press **Alt+N**. A new record or row opens; on some pages a dialog opens instead. |
| 3. *Enter* the required fields. | Enter the values your process guide gives. Required fields are marked; D365 shows a message for any that are missing. |
| 4. *Click* **Save**. | Click **Save**, or **OK** in a dialog. |
| 5. *Confirm* the record is created. | Check that the new record appears in the list with the values you entered. |
| *PROCESS COMPLETE* | Outcomes:<br>• The new record is saved in the active legal entity. |

##### Delete a Record

Complete these steps to delete a record:

| **Action** | **Description** |
|---|---|
| *PROCESS START* | Pre-requisites:<br>• Your process guide tells you to delete the record.<br>Responsibility:<br>• D365 End-user |
| 1. *Select* the record. | Select the record in the list, or open it. |
| 2. *Click* **Delete**. | On the Action Pane, click **Delete**, or press **Alt+Delete**. |
| 3. *Confirm* the deletion. `[GS-10]` | Read the message and click **Yes** to delete the record. |
| *PROCESS COMPLETE* | Outcomes:<br>• The record is deleted and no longer in the list. |

#### 4.3 Enter Values with Lookups and Date Pickers

##### Description

Use this procedure to fill a field from its list of valid values (a lookup), and a date field from the date picker. Many lookups accept the name as well as the code: in a customer account field you can type the customer’s name instead of the account number.

##### Responsibility
- D365 End-user: enters values in the records they work on.

##### Initiation
- A field with a drop-down arrow needs a value.

##### Procedure

Complete these steps to enter a value with a lookup:

| **Action** | **Description** |
|---|---|
| *PROCESS START* | Pre-requisites:<br>• The record is in Edit mode (see 4.1 Edit, Save and Revert a Record).<br>Responsibility:<br>• D365 End-user |
| 1. *Type* the start of the value. | Type the first characters of the code or name. After a short pause the lookup opens, showing values that begin with what you typed. Keep typing to narrow the list. |
| 2. *Select* the value. | Use the **Up** and **Down** arrow keys, then press **Enter**, or click the value. To see the whole list, click the arrow or press **Alt+Down arrow**. |
| 3. *Filter* the lookup if the value is not found. | Optional. To find a value by other text, clear the field, open the lookup, then filter a lookup column as in 5.2 Filter and Sort a Column. |
| 4. *Enter* a date. | In a date field, type the date, or click the calendar icon (**Alt+Down arrow**) and pick it. Type **T** for today, or **D** for the session date. |
| 5. *Confirm* the values are accepted. | Check that no error shows beside the field or in the message bar. |
| *PROCESS COMPLETE* | Outcomes:<br>• The fields hold valid values. |

> **Note:** In a numeric field you can type a calculation starting with an equals sign, for example **=15*4**, and D365 enters the result.

#### 4.4 Run an Action with Action Search

##### Description

Use this procedure to find and run a button on the current page by typing its name, instead of looking through the Action Pane tabs. It finds buttons on the Action Pane and toolbars that the page shows.

##### Responsibility
- D365 End-user: runs page actions by name.

##### Initiation
- A user needs a button but does not know which tab holds it.

##### Procedure

Complete these steps to run an action with action search:

| **Action** | **Description** |
|---|---|
| *PROCESS START* | Pre-requisites:<br>• The page is open.<br>Responsibility:<br>• D365 End-user |
| 1. *Click* **Action search**. | At the right of the Action Pane, click the magnifying glass, or press **Alt+Q**. |
| 2. *Type* the button name. | Type all or part of the button name. Each result shows where the button sits, for example its tab. |
| 3. *Select* the button. | Select the button in the results. It runs as if you had clicked it on the Action Pane. |
| 4. *Confirm* the action ran. | Check the result on the page or in the message bar. |
| *PROCESS COMPLETE* | Outcomes:<br>• The action has run on the current page. |

### 5. Find Records with Filters

##### Description

Use this topic to find the records you need on a list page. D365 has four filter tools: the **Filter** box above a grid (QuickFilter), the filter on a column header, the **Filter pane**, and **Advanced filter or sort**. The operators and symbols they accept are in Part 1, Filter operators.

##### Responsibility
- D365 End-user: filters the lists they work with.

##### Initiation
- A list shows more records than the task needs.

##### Topic Overview

This topic includes these steps:

| Step | Description |
|---|---|
| 5.1 Filter with the QuickFilter | Filter one column by typing in the Filter box. |
| 5.2 Filter and Sort a Column | Filter or sort from a column header. |
| 5.3 Filter with the Filter Pane | Filter several fields at once, including fields not shown in the grid. |
| 5.4 Use Advanced Filter or Sort | Optional. Build a filter on several fields, or sort by more than one column. |

#### 5.1 Filter with the QuickFilter

##### Description

Use this procedure to filter a list quickly on one column, by typing in the **Filter** box above the grid.

##### Responsibility
- D365 End-user: filters the lists they work with.

##### Initiation
- A user needs to find a record or a few records quickly.

##### Procedure

Complete these steps to filter with the QuickFilter:

| **Action** | **Description** |
|---|---|
| *PROCESS START* | Pre-requisites:<br>• The list page is open.<br>Responsibility:<br>• D365 End-user |
| 1. *Check* the **Entity**. | Confirm you are signed into the correct **Legal Entity** (top-right). To change it, see 3.1 Switch Legal Entity with the Selector. |
| 2. *Type* the value in the **Filter** box. | Type the value in the **Filter** box above the grid. A list of columns appears below the box.<br><mark>Microsoft Learn example (demo data): The Filter box with its column list. Replace with a WTG screenshot.</mark> |
| 3. *Select* the column. | Select the column the value belongs to, for example **Name** or **Account**. D365 remembers the column you choose. |
| 4. *Press* **Enter**. | Press **Enter**. The grid shows only the matching rows. |
| 5. *Clear* the filter when you finish. | Delete the text in the **Filter** box and press **Enter** to see all rows again. |
| *PROCESS COMPLETE* | Outcomes:<br>• The grid shows the rows that match the value. |

#### 5.2 Filter and Sort a Column

##### Description

Use this procedure to filter a column with an operator, such as **contains** or **greater than**, or to sort the grid by a column. A column whose header cannot be clicked cannot be filtered or sorted.

##### Responsibility
- D365 End-user: filters and sorts the lists they work with.

##### Initiation
- A user needs to limit or order the rows by one column.

##### Procedure

Complete these steps to filter and sort a column:

| **Action** | **Description** |
|---|---|
| *PROCESS START* | Pre-requisites:<br>• The list page is open.<br>Responsibility:<br>• D365 End-user |
| 1. *Check* the **Entity**. | Confirm you are signed into the correct **Legal Entity** (top-right). To change it, see 3.1 Switch Legal Entity with the Selector. |
| 2. *Click* the column header. | Click the header of the column, or select a cell in it and press **Ctrl+G**. The column filter opens.<br><mark>Microsoft Learn example (demo data): A column header filter with sort, operator, Apply and Clear. Replace with a WTG screenshot.</mark> |
| 3. *Select* the filter operator. | Select the operator next to the field name, for example **contains**. See Filter operators in Part 1. |
| 4. *Enter* the filter value. | Enter the value. For example, to exclude zero balances, select **is not equal to** and enter **0**. |
| 5. *Click* **Apply**. | Click **Apply**, or press **Enter**. The grid shows only the matching rows. **Clear** removes this column’s filter. |
| 6. *Sort* the column. | Optional. In the same drop-down, select **Sort A to Z** or **Sort Z to A** (for numbers and dates, smallest or largest first). |
| 7. *Confirm* the rows shown. | Check that the grid shows only the rows you need, in the order you need. |
| *PROCESS COMPLETE* | Outcomes:<br>• The grid is filtered and sorted by the column. |

#### 5.3 Filter with the Filter Pane

##### Description

Use this procedure to filter several fields at once, including fields that the grid does not show. The Filter pane applies to the main list of the page, not to lines grids.

##### Responsibility
- D365 End-user: filters the lists they work with.

##### Initiation
- A user needs to filter on more than one field, or on a field that is not in the grid.

##### Procedure

Complete these steps to filter with the Filter pane:

| **Action** | **Description** |
|---|---|
| *PROCESS START* | Pre-requisites:<br>• The list page is open.<br>Responsibility:<br>• D365 End-user |
| 1. *Check* the **Entity**. | Confirm you are signed into the correct **Legal Entity** (top-right). To change it, see 3.1 Switch Legal Entity with the Selector. |
| 2. *Click* **Show filters**. `[GS-11]` | Click **Show filters** (the funnel icon at the side of the page), or press **Alt+M, F**. The Filter pane opens.<br><mark>Microsoft Learn example (demo data): The Filter pane with Add, Apply and Reset. Replace with a WTG screenshot.</mark> |
| 3. *Enter* a value for each field. | For each field, select the operator and enter the value. |
| 4. *Click* **Add a filter field**. | Optional. To filter on a field that is not listed, click **Add a filter field** and select it. |
| 5. *Click* **Apply**. | Click **Apply**. The grid shows only the rows that match every filter. |
| 6. *Confirm* the rows shown. | Check the rows, then close the pane with **Hide filters** or **Esc**. |
| *PROCESS COMPLETE* | Outcomes:<br>• The grid shows the rows that match all the filters. |

#### 5.4 Use Advanced Filter or Sort

##### Description

Use this procedure to build a filter from several criteria, on fields the page does not show, or to sort by more than one column. The dialog uses the names of the underlying tables and fields, which can differ from the page labels. Most users need it rarely.

##### Responsibility
- D365 End-user: builds advanced filters when a simple filter is not enough.

##### Initiation
- A filter needs more criteria than the Filter pane offers, or the list must be sorted by more than one column.

##### Procedure

Complete these steps to use advanced filter or sort:

| **Action** | **Description** |
|---|---|
| *PROCESS START* | Pre-requisites:<br>• The list page is open.<br>Responsibility:<br>• D365 End-user |
| 1. *Press* **Ctrl+Shift+F3**. `[GS-12]` | Press **Ctrl+Shift+F3** (**Open advanced filtering and sorting options**). The advanced filter dialog opens on the **Range** tab. |
| 2. *Click* **Add**. | On the **Range** tab, click **Add** to add a line.<br><mark>Microsoft Learn example (demo data): The advanced filter dialog, Range tab. Replace with a WTG screenshot.</mark> |
| 3. *Select* the **Field**. | Select the table and field to filter on. |
| 4. *Enter* the **Criteria**. | Enter the value, using the symbols in Filter operators in Part 1. |
| 5. *Click* **OK**. | Click **OK**. The page shows the rows that match the criteria. |
| *PROCESS COMPLETE* | Outcomes:<br>• The grid shows the rows that match the advanced criteria. |

### 6. Create a Personalized View

##### Description

Use this topic to set up a page so it shows the columns, filters and totals you need, and save that layout as a view that opens by default. Each process guide lists the columns recommended for its pages.

##### Responsibility
- D365 End-user: creates personal views for the pages they use.

##### Initiation
- A page does not show the information needed in the way it is needed.

##### Topic Overview

This topic includes these steps:

| Step | Description |
|---|---|
| 6.1 Arrange the Columns | Add, hide, move, freeze and size columns. Output: the grid shows the columns you need. |
| 6.2 Add a Footer Total | Optional. Show a total, minimum, maximum or average under a numeric column. |
| 6.3 Group Rows | Optional. Group the rows by a column, with subtotals. |
| 6.4 Save and Pin the View | Save the layout as a named view and pin it as your default. |

#### 6.1 Arrange the Columns

##### Description

Use this procedure to show the columns you need in the order you need them. Changes to columns are kept only when you save the view (6.4); column widths are remembered automatically.

##### Responsibility
- D365 End-user: arranges the grids they use.

##### Initiation
- A grid lacks a column the task needs, or shows columns it does not.

##### Procedure

Complete these steps to arrange the columns:

| **Action** | **Description** |
|---|---|
| *PROCESS START* | Pre-requisites:<br>• Access to D365 and to the page.<br>Responsibility:<br>• D365 End-user |
| 1. *Check* the **Entity**. | Confirm you are signed into the correct **Legal Entity** (top-right). To change it, see 3.1 Switch Legal Entity with the Selector. |
| 2. *Open* the page you want to personalize. | Open the list page whose layout you want to save. |
| 3. *Right-click* a column header. | Right-click the header of any column. The menu shows the column options.<br><mark>Microsoft Learn example (demo data): The column header menu: Insert columns, Hide this column, Export all rows. Replace with a WTG screenshot.</mark> |
| 4. *Click* **Insert columns**. | Click **Insert columns**, select each column you need, then click **Update**. The columns are added to the grid. |
| 5. *Hide* each column you do not need. | Right-click the header of the column and click **Hide this column**. |
| 6. *Move* the columns into the order you need. | Drag a column header to its new position. |
| 7. *Freeze* the key column. | Optional. Right-click the header of the column you always need to see, such as the account, and click **Freeze column**. It stays in view as you scroll. |
| 8. *Size* the columns. | Drag the edge of a column header to resize it, or double-click the edge to fit the column to its content. |
| *STEP COMPLETE* | The grid shows the columns you need, in your order.<br>Continue to 6.2 Add a Footer Total |

#### 6.2 Add a Footer Total

##### Description

Use this procedure to show a calculated value at the foot of a numeric column, such as the total of an amount column. With more than one row selected, the footer shows the value for the selected rows. Footer totals are remembered automatically for the view; they do not need to be saved.

##### Responsibility
- D365 End-user: adds totals to the grids they use.

##### Initiation
- A user needs the total of a numeric column at a glance.

##### Procedure

Complete these steps to add a footer total:

| **Action** | **Description** |
|---|---|
| *PROCESS START* | Pre-requisites:<br>• The grid shows the column to total (see 6.1 Arrange the Columns).<br>Responsibility:<br>• D365 End-user |
| 1. *Right-click* in the numeric column. | Right-click a value in the amount or balance column. |
| 2. *Click* **View column totals**. `[GS-13]` | Click **View column totals**, then the value you need: **Total**, **Minimum**, **Maximum** or **Average**. The footer opens below the grid.<br><mark>Microsoft Learn example (demo data): Footer totals under numeric columns. Replace with a WTG screenshot.</mark> |
| 3. *Click* **Calculate**. | If the footer shows a dash, the list is too large to total automatically: click **Calculate** in the footer. |
| 4. *Confirm* the total is displayed. | Check that the footer shows the value under the column. |
| *STEP COMPLETE* | The footer shows the value for the column.<br>Continue to 6.3 Group Rows |

> **Note:** To show or hide the footer, select **Grid options** (the three dots at the right of the grid header) and **Show footer** or **Hide footer**.

#### 6.3 Group Rows

##### Description

Use this procedure to group the rows by the values of a column, for example by customer or currency. Each group has a header row with its row count and any footer totals as subtotals. Skip it if you do not need groups: continue to 6.4 Save and Pin the View.

##### Responsibility
- D365 End-user: groups the grids they use.

##### Initiation
- A user needs subtotals or rows organized by a value.

##### Procedure

Complete these steps to group rows:

| **Action** | **Description** |
|---|---|
| *PROCESS START* | Pre-requisites:<br>• The grid shows the column to group by.<br>Responsibility:<br>• D365 End-user |
| 1. *Right-click* the column header. | Right-click the header of the column to group by. |
| 2. *Click* **Group by this column**. | Click **Group by this column**. A header row starts each group. Group by another column to add a level, up to five.<br><mark>Microsoft Learn example (demo data): Rows grouped by a column, with subtotals. Replace with a WTG screenshot.</mark> |
| 3. *Expand* or collapse a group. | Click the arrow in a group header to show or hide its rows. |
| 4. *Confirm* the grouping. | Check the groups and their subtotals. To remove grouping, select **Grid options** > **Ungroup all**. |
| *STEP COMPLETE* | The rows are grouped, with subtotals.<br>Continue to 6.4 Save and Pin the View |

#### 6.4 Save and Pin the View

##### Description

Use this procedure to save the layout as a named view and pin it as your default, so the page opens with your columns, filters and grouping each time.

##### Responsibility
- D365 End-user: saves and pins their own views.

##### Initiation
- The page layout is ready to keep.

##### Procedure

Complete these steps to save and pin the view:

| **Action** | **Description** |
|---|---|
| *PROCESS START* | Pre-requisites:<br>• The grid shows the columns, and any filters, totals and grouping, you need.<br>Responsibility:<br>• D365 End-user |
| 1. *Open* the view selector. | Above the grid, click the current view name, for example **Standard**.<br>Note: An asterisk (*) beside the view name means the layout has unsaved changes. |
| 2. *Click* **Save as**. | Click **Save as**. The **Save view as** pane opens. |
| 3. *Enter* the view name. | Enter a name that identifies the page and the purpose of the view. Add a description if it helps. |
| 4. *Select* **Pin as default**. | Select **Pin as default** so the page opens in this view. |
| 5. *Select* the legal entities. `[GS-14]` | Keep the view for all legal entities, or limit it to the legal entities you select. |
| 6. *Click* **Save**. | Click **Save**. |
| 7. *Confirm* the view is saved and pinned. | Check that the view name shows above the grid without an asterisk, and that the view is marked as the default in the view selector. |
| *PROCESS COMPLETE* | Outcomes:<br>• The page has a saved view with your layout, pinned as your default. |

### 7. Manage Saved Views and Personalizations

##### Description

Use this topic to change a saved view, organize your views, personalize the fields of a page, and reset a page you have personalized.

##### Responsibility
- D365 End-user: manages their own views and personalizations.

##### Initiation
- A saved view needs to change, a page layout needs tidying, or a page needs to return to its default layout.

##### Topic Overview

This topic includes these steps:

| Step | Description |
|---|---|
| 7.1 Update a Saved View | Change a saved view and save it. |
| 7.2 Manage My Views | Rename, reorder, pin or delete your views. |
| 7.3 Personalize a Page | Hide, move or add fields on a page with the personalization toolbar. |
| 7.4 Clear a Personalization | Return a view or page to its default layout. |

#### 7.1 Update a Saved View

##### Description

Use this procedure to change a view you saved, for example to add a column or change a filter. A view you cannot edit shows a padlock: use **Save as** to make your own copy.

##### Responsibility
- D365 End-user: updates their own saved views.

##### Initiation
- A saved view needs a further change.

##### Procedure

Complete these steps to update a saved view:

| **Action** | **Description** |
|---|---|
| *PROCESS START* | Pre-requisites:<br>• A saved view for the page (see 6. Create a Personalized View).<br>Responsibility:<br>• D365 End-user |
| 1. *Check* the **Entity**. | Confirm you are signed into the correct **Legal Entity** (top-right). To change it, see 3.1 Switch Legal Entity with the Selector. |
| 2. *Open* the page that has the saved view. | Open the page whose view you want to change. |
| 3. *Select* the saved view. | Open the view selector above the grid and select the view. |
| 4. *Make* the change to the layout. | Change the columns, filters or grouping as in 6. Create a Personalized View. An asterisk shows beside the view name. |
| 5. *Click* **Save**. | Open the view selector and click **Save**. |
| 6. *Confirm* the view shows the change. | Check that the view name shows without an asterisk and the change is kept when you reopen the page. |
| *PROCESS COMPLETE* | Outcomes:<br>• The saved view includes the change. |

#### 7.2 Manage My Views

##### Description

Use this procedure to rename your views, change their order in the view selector, pin one as default, or delete those you no longer use. A deleted view cannot be restored. Views published to you can be pinned but not renamed or deleted.

##### Responsibility
- D365 End-user: organizes their own views.

##### Initiation
- A user’s views for a page need organizing.

##### Procedure

Complete these steps to manage your views:

| **Action** | **Description** |
|---|---|
| *PROCESS START* | Pre-requisites:<br>• The page has views you saved.<br>Responsibility:<br>• D365 End-user |
| 1. *Open* the view selector. | Above the grid, click the view name. |
| 2. *Click* **More**. | Click **More**, then **Manage my views**. |
| 3. *Select* a view. | Under **My views**, select the view to change. |
| 4. *Click* the action you need. | Click **Pin as default**, **Move up**, **Move down**, **Rename** or **Delete**. |
| 5. *Click* **Update**. | Click **Update** to apply the changes. |
| *PROCESS COMPLETE* | Outcomes:<br>• Your views are named, ordered and pinned as you need. |

#### 7.3 Personalize a Page

##### Description

Use this procedure to change the fields shown on a page, such as a details page or a FastTab, with the personalization toolbar. Changes made with the toolbar are kept only when you save them to a view.

##### Responsibility
- D365 End-user: personalizes the pages they use.

##### Initiation
- A page shows fields the user does not need, or lacks one they do.

##### Procedure

Complete these steps to personalize a page:

| **Action** | **Description** |
|---|---|
| *PROCESS START* | Pre-requisites:<br>• The page is open.<br>Responsibility:<br>• D365 End-user |
| 1. *Open* the personalization toolbar. `[GS-15]` | On the Action Pane, select **Options** > **Personalize this page**, or press **Ctrl+Shift+P**. The toolbar opens and the page becomes read-only. |
| 2. *Click* the tool you need. | Click **Hide** to hide a field, **Move** to drag it to another place, or **Add a field** to add one.<br><mark>Microsoft Learn example (demo data): The personalization toolbar. Replace with a WTG screenshot.</mark> |
| 3. *Select* the field. | Select the field or section on the page. Hidden fields show shaded while the toolbar is open: select one again to show it. |
| 4. *Click* **Close**. | Close the toolbar. An asterisk shows beside the view name. |
| 5. *Save* the view. | Save the change to your view as in 7.1 Update a Saved View, or with **Save as**. |
| *PROCESS COMPLETE* | Outcomes:<br>• The page shows the fields you need, saved in your view. |

#### 7.4 Clear a Personalization

##### Description

Use this procedure to return the current view, or a page without views, to its default layout. Clearing cannot be undone. To discard only unsaved changes, switch back to the saved view instead.

##### Responsibility
- D365 End-user: resets their own personalizations.

##### Initiation
- A personalized page is not working as expected, or needs to return to its default.

##### Procedure

Complete these steps to clear a personalization:

| **Action** | **Description** |
|---|---|
| *PROCESS START* | Pre-requisites:<br>• The page is open in the view to reset.<br>Responsibility:<br>• D365 End-user |
| 1. *Open* the personalization toolbar. | Select **Options** > **Personalize this page**, or press **Ctrl+Shift+P**. |
| 2. *Click* the more options button. | On the toolbar, click **…** (more options). |
| 3. *Click* **Clear**. | Click **Clear** and confirm. The personalizations of the current view are removed. |
| 4. *Confirm* the default layout. | Check that the page shows its default fields and columns. |
| *PROCESS COMPLETE* | Outcomes:<br>• The view or page is back to its default layout. |

### 8. Export Data and Work in Excel

##### Description

Use this topic to get data from a page into Excel: as a one-off export of the grid, or as a workbook linked to D365. See Getting data into Excel in Part 1 to choose between them.

##### Responsibility
- D365 End-user: exports or opens the data their role allows.

##### Initiation
- Page data is needed in Excel.

##### Topic Overview

This topic includes these steps:

| Step | Description |
|---|---|
| 8.1 Export All Rows from a Grid | Export the grid, as shown, to an Excel file. |
| 8.2 Open a Page in Excel and Publish Changes | Open a linked workbook, refresh it and, where your process guide allows, publish changes to D365. |

#### 8.1 Export All Rows from a Grid

##### Description

Use this procedure to export the rows of a grid to an Excel file. The export contains the columns and rows the grid shows, with its filters, so arrange and filter the grid first. The export is a copy: it does not change when the data in D365 changes.

##### Responsibility
- D365 End-user: exports grid data for internal analysis.

##### Initiation
- Grid data is needed in Excel for internal analysis.

##### Procedure

Complete these steps to export all rows from a grid:

| **Action** | **Description** |
|---|---|
| *PROCESS START* | Pre-requisites:<br>• Access to D365 and to the page that holds the data.<br>Responsibility:<br>• D365 End-user |
| 1. *Check* the **Entity**. | Confirm you are signed into the correct **Legal Entity** (top-right). To change it, see 3.1 Switch Legal Entity with the Selector. |
| 2. *Open* the page that holds the data. | Open the list page whose grid holds the data you need. |
| 3. *Confirm* the grid shows the columns and rows you need. | The export contains the columns and filters of the grid. Add any column you need first (see 6.1 Arrange the Columns). |
| 4. *Right-click* the grid header. | Right-click the header of any column in the grid. |
| 5. *Select* **Export all rows**. `[[Q03] GS-16: Confirm]` | Select **Export all rows**. To export only some rows, select them first and choose **Export marked rows**.<br>Note: You can also select **Open in Microsoft Office** > **Export to Excel** on the Action Pane, or press **Ctrl+Shift+E**.<br><mark>Microsoft Learn example (demo data): The column header menu: Insert columns, Hide this column, Export all rows. Replace with a WTG screenshot.</mark> |
| 6. *Download* the export. | Download the file when D365 has prepared it. The download link works for 15 minutes. |
| 7. *Open* the exported file. | Open the file in Excel. |
| 8. *Confirm* the required fields were exported. | Check that the file holds every field and row you need. |
| *PROCESS COMPLETE* | Outcomes:<br>• The grid rows are in an Excel file with the grid’s columns, for internal use. |

#### 8.2 Open a Page in Excel and Publish Changes

##### Description

Use this procedure to open the data of a page in an Excel workbook that stays linked to D365 through the Microsoft Dynamics Office Add-in. You can refresh the workbook with current data and, where your process guide says so, change rows and publish them back to D365. The add-in does not run on Excel for Mac.

##### Responsibility
- D365 End-user: opens linked workbooks, and publishes changes only where their process guide allows.

##### Initiation
- A process guide tells the user to view or update records in Excel.

##### Procedure

Complete these steps to open a page in Excel:

| **Action** | **Description** |
|---|---|
| *PROCESS START* | Pre-requisites:<br>• Access to D365 and to the page.<br>• Excel 2016 or later, or Excel for the web.<br>Responsibility:<br>• D365 End-user |
| 1. *Check* the **Entity**. | Confirm you are signed into the correct **Legal Entity** (top-right). To change it, see 3.1 Switch Legal Entity with the Selector. |
| 2. *Click* **Open in Microsoft Office**. | On the Action Pane of the page, click **Open in Microsoft Office** (the Office icon). |
| 3. *Select* the **Open in Excel** option. | Under **Open in Excel**, select the option your process guide names, then open the workbook.<br><mark>Microsoft Learn example (demo data): The Open in Microsoft Office menu: Open in Excel and Export to Excel. Replace with a WTG screenshot.</mark> |
| 4. *Click* **Enable editing**. | In Excel, click **Enable editing** so the add-in can run. The first time, click **Trust this Add-in**, and sign in with your work account if asked. |
| 5. *Confirm* the data is loaded. | The add-in opens on the right and reads the data. Check the rows and the user name shown in the add-in.<br><mark>Microsoft Learn example (demo data): The Microsoft Dynamics Office Add-in in Excel, with Refresh and Publish. Replace with a WTG screenshot.</mark> |
| 6. *Change* the rows. `[[Q04] GS-17: Confirm]` | Optional. Change the values your process guide gives. Remove any Excel column filters first. |
| 7. *Click* **Publish**. | Click **Publish** in the add-in. The **Messages** count shows how many records were added, changed or deleted, and any errors. |
| 8. *Confirm* the changes in D365. | Refresh the page in D365 and check the changed records. Dates and times in the add-in are shown in UTC. |
| *PROCESS COMPLETE* | Outcomes:<br>• The workbook shows current D365 data, and any published changes are saved in D365. |

> **Important:** Publishing from Excel changes the records in D365. Publish only where your process guide tells you to, and check the result in D365.

### 9. Run a Report

##### Description

Use this topic to run a D365 report: set its parameters and destination, view, download or print it, run it in the background when it is large, and find the output afterwards. Reports open from the **Inquiries and reports** menu of their module; each process guide names its reports in its Part 3.

##### Responsibility
- D365 End-user: runs the reports their role needs.

##### Initiation
- A report is needed on screen, as a file, or in the background.

##### Topic Overview

This topic includes these steps:

| Step | Description |
|---|---|
| 9.1 Set the Report Parameters and Destination | Fill in the report dialog: parameters, records to include and destination. |
| 9.2 View, Download and Print a Report | Use the PDF viewer for a report sent to the screen. |
| 9.3 Run a Report in the Background | Optional. Send a large report to run in the background. |
| 9.4 Find Background Output | Find a background report in the Action center, My batch jobs and the Print archive. |

#### 9.1 Set the Report Parameters and Destination

##### Description

Use this procedure to fill in a report dialog. Most dialogs have the same sections: **Parameters** for the report’s options, **Records to include** to limit the records, **Destination** for where the report goes, and **Run in the background**.

##### Responsibility
- D365 End-user: runs the reports their role needs.

##### Initiation
- A user opens a report from a module’s Inquiries and reports menu.

##### Procedure

Complete these steps to set the report parameters and destination:

| **Action** | **Description** |
|---|---|
| *PROCESS START* | Pre-requisites:<br>• Access to D365 and to the report.<br>Responsibility:<br>• D365 End-user |
| 1. *Check* the **Entity**. | Confirm you are signed into the correct **Legal Entity** (top-right). To change it, see 3.1 Switch Legal Entity with the Selector. |
| 2. *Navigate* to the report. `[GS-18]` | From the **Navigation Pane**, click **Modules**, select the module, then select the report under **Inquiries and reports**, using the path your process guide gives. The report dialog opens. |
| 3. *Enter* the **Parameters**. | Enter the report options your process guide gives, such as dates or a customer range.<br><mark>Microsoft Learn example (demo data): A report dialog: Parameters, Destination and Records to include. Replace with a WTG screenshot.</mark> |
| 4. *Click* **Filter**. | Optional. On the **Records to include** FastTab, click **Filter** to limit the records, for example to one account, then click **OK**. |
| 5. *Check* the **Destination**. | The **Destination** FastTab shows where the report goes. **Screen** is the default. |
| 6. *Click* **Change**. | Optional. To send the report elsewhere, click **Change**, select **File**, **Email**, **Printer** or **Print archive**, and click **OK**. See Report destinations in Part 1.<br><mark>Microsoft Learn example (demo data): Print destination settings: Print archive, Screen, Printer, File, Email. Replace with a WTG screenshot.</mark> |
| 7. *Click* **OK**. | Click **OK** to run the report. |
| *STEP COMPLETE* | The report runs to the destination you chose.<br>Continue to 9.2 View, Download and Print a Report |

#### 9.2 View, Download and Print a Report

##### Description

Use this procedure to work with a report sent to the screen. It opens in the PDF viewer, which shows the report as it will print. Links in a report work only while you preview it, not in a downloaded file.

##### Responsibility
- D365 End-user: views, downloads and prints the reports they run.

##### Initiation
- A report was run with the destination Screen.

##### Procedure

Complete these steps to view, download and print a report:

| **Action** | **Description** |
|---|---|
| *PROCESS START* | Pre-requisites:<br>• The report was run to **Screen** (see 9.1 Set the Report Parameters and Destination).<br>Responsibility:<br>• D365 End-user |
| 1. *Review* the report. | Scroll through the report in the viewer, and use the page controls on its toolbar to move between pages.<br><mark>Microsoft Learn example (demo data): A report in the PDF viewer. Replace with a WTG screenshot.</mark> |
| 2. *Click* the download button. | Optional. On the viewer toolbar, click download to save the report as a PDF. |
| 3. *Click* **Print**. | Optional. Click **Print** on the viewer toolbar to print to your local printer. |
| 4. *Close* the viewer. | Close the viewer to return to D365. |
| *PROCESS COMPLETE* | Outcomes:<br>• The report has been reviewed, and downloaded or printed if needed. |

> **Note:** A report that runs too long while you wait can time out. Run large reports in the background (9.3) and split very large runs into smaller ranges.

#### 9.3 Run a Report in the Background

##### Description

Use this procedure to run a large report as a batch job, so you can keep working while it runs. A background report cannot go to **Screen** or **File**: send it to the **Print archive**, **Email** or a **Printer**. Skip this subtopic for reports that run quickly: continue to 9.2 View, Download and Print a Report.

##### Responsibility
- D365 End-user: runs large reports in the background.

##### Initiation
- A report is large, or a process guide tells the user to run it in the background.

##### Procedure

Complete these steps to run a report in the background:

| **Action** | **Description** |
|---|---|
| *PROCESS START* | Pre-requisites:<br>• The report dialog is open with its parameters set (see 9.1 Set the Report Parameters and Destination).<br>Responsibility:<br>• D365 End-user |
| 1. *Expand* **Run in the background**. | In the report dialog, expand the **Run in the background** FastTab. |
| 2. *Set* **Batch processing** to **Yes**. | Turn on **Batch processing**.<br><mark>Microsoft Learn example (demo data): Run in the background with Batch processing on. Replace with a WTG screenshot.</mark> |
| 3. *Enter* the **Task description**. | Enter a description you will recognize, for example the report name and date. You find the output by it later. |
| 4. *Select* the **Destination**. | On the **Destination** FastTab, click **Change** and select **Print archive**, then click **OK**. |
| 5. *Click* **Alerts**. | Optional. Click **Alerts** and select when to be told, for example when the job has **Ended** or has an **Error**. |
| 6. *Click* **OK**. | Click **OK**. The report is queued; it usually starts within a minute. |
| *STEP COMPLETE* | The report is queued as a batch job.<br>Continue to 9.4 Find Background Output |

> **Note:** Leave **Batch group** and the other background settings as they are unless your process guide gives a value.

#### 9.4 Find Background Output

##### Description

Use this procedure to check a background report and open its output. The **Action center** tells you when it has finished, **My batch jobs** shows its status, and the **Print archive** holds the report.

##### Responsibility
- D365 End-user: finds the output of their background reports.

##### Initiation
- A report was run in the background.

##### Procedure

Complete these steps to find background output:

| **Action** | **Description** |
|---|---|
| *PROCESS START* | Pre-requisites:<br>• A report was run in the background to the Print archive (see 9.3 Run a Report in the Background).<br>Responsibility:<br>• D365 End-user |
| 1. *Click* the **Action center**. | On the navigation bar, click the bell. A message shows when the job has finished. |
| 2. *Navigate* to the **My batch jobs** page. `[GS-20]` | If the job has not finished, from the **Navigation Pane**, *select*:<br>• **Modules >**<br>• **Common >**<br>• **Inquiries >**<br>• **Batch jobs >**<br>• **My batch jobs** |
| 3. *Check* the job **Status**. | Find the job by its task description. **Waiting** or **Executing** means it is still running; **Ended** means it finished; **Error** means it failed: contact the BAU Support team.<br><mark>Microsoft Learn example (demo data): A batch job and its status. Replace with a WTG screenshot.</mark> |
| 4. *Navigate* to the **Print archive** page. | From the **Navigation Pane**, *select*:<br>• **Modules >**<br>• **Common >**<br>• **Inquiries >**<br>• **Print archive** |
| 5. *Select* the report. | Select the report by its description.<br><mark>Microsoft Learn example (demo data): The Print archive list. Replace with a WTG screenshot.</mark> |
| 6. *Click* **Print preview**. | Click **Print preview** to open the report, then download or print it as in 9.2 View, Download and Print a Report. |
| *PROCESS COMPLETE* | Outcomes:<br>• The background report is open from the Print archive. |

### 10. Attach a Document

##### Description

Use this topic to attach a file, a note or a link to a record, such as a remittance to a payment journal or a supporting document to an invoice, and to open the attachments already there. The **Attach** button (paperclip) at the top right of a page shows how many attachments the record has.

##### Responsibility
- D365 End-user: attaches the supporting documents their process requires.

##### Initiation
- A file, note or link must be kept with a record, as a process guide describes.

##### Procedure

Complete these steps to attach a document:

| **Action** | **Description** |
|---|---|
| *PROCESS START* | Pre-requisites:<br>• The record is selected or open.<br>• The file to attach, if attaching a file.<br>Responsibility:<br>• D365 End-user |
| 1. *Check* the **Entity**. | Confirm you are signed into the correct **Legal Entity** (top-right). To change it, see 3.1 Switch Legal Entity with the Selector. |
| 2. *Select* the record. | Select the record to attach to. On a page with a header and lines, click in the part (header or line) that the attachment belongs to. |
| 3. *Click* **Attach**. | Click **Attach** (the paperclip, top right), or press **Ctrl+Shift+A**. The **Attachments** page opens. |
| 4. *Click* **New**. `[[Q05] GS-21: Confirm]` | Click **New** and select the type: **File**, **Note** or **URL**.<br><mark>Microsoft Learn example (demo data): The Attachments page: New > File, Image, Note or URL. Replace with a WTG screenshot.</mark> |
| 5. *Select* the file. | For a file, click **Browse**, select the file and open it. For a note or URL, enter it in **Notes**. |
| 6. *Enter* the **Description**. | Enter a description that says what the document is. |
| 7. *Confirm* the attachment is listed. | Check that the attachment is listed and its preview shows. Close the page: the **Attach** button now counts it. |
| *PROCESS COMPLETE* | Outcomes:<br>• The document is attached to the record and counted on the **Attach** button. |

> **Note:** To open an attachment, click **Attach** on the record, select the attachment and review it in the **Preview** FastTab, or click **Open**. If the **Attach** button is missing, check **Enable document handling** in your user options (topic 1.2).

### 11. Submit and Approve Workflow Items

##### Description

Use this topic to send a document to workflow for approval, follow it, and act on the work items assigned to you. The **Workflow** button on the Action Pane shows the actions available to you at the current step; your process guide says which documents go through workflow and who approves them. See Workflow in Part 1 for the terms.

##### Responsibility
- D365 End-user: submits their own documents and acts on the work items assigned to them.

##### Initiation
- A document needs approval, or a work item is assigned to the user.

##### Topic Overview

This topic includes these steps:

| Step | Description |
|---|---|
| 11.1 Submit a Document to Workflow | Submit, follow and, if needed, recall your document. |
| 11.2 Act on a Work Item | Approve, reject, request a change or delegate a work item assigned to you. |
| 11.3 Delegate Your Work Items While Away | Optional. Send new work items to another user while you are away. |

#### 11.1 Submit a Document to Workflow

##### Description

Use this procedure to submit a document, such as a journal, to its workflow. The comment you enter goes to the approver with the document. After submitting, follow the document in its workflow history; you can recall it to stop the workflow if you need to correct it.

##### Responsibility
- D365 End-user: submits their own documents to workflow.

##### Initiation
- A document is ready for approval, as the process guide describes.

##### Procedure

Complete these steps to submit a document to workflow:

| **Action** | **Description** |
|---|---|
| *PROCESS START* | Pre-requisites:<br>• The document is complete and saved.<br>Responsibility:<br>• D365 End-user |
| 1. *Check* the **Entity**. | Confirm you are signed into the correct **Legal Entity** (top-right). To change it, see 3.1 Switch Legal Entity with the Selector. |
| 2. *Open* the document. | Open the document to submit. |
| 3. *Click* **Workflow**. `[GS-22]` | On the Action Pane, click **Workflow**. The workflow message bar above the page shows the workflow’s instructions. |
| 4. *Click* **Submit**. | Click **Submit**. |
| 5. *Enter* the comment. | Enter a comment for the approver, then click **Submit**. The document’s approval status changes. |
| 6. *Click* **View history**. | Optional. Click **Workflow** > **View history** to see who the document is with and what has happened. To stop the workflow, click **Recall**, enter a comment and click **OK**. |
| *PROCESS COMPLETE* | Outcomes:<br>• The document is in workflow, waiting for approval. |

#### 11.2 Act on a Work Item

##### Description

Use this procedure to act on a work item assigned to you: approve, reject, request a change, or delegate it to another user. Work items show on the dashboard under **Work items assigned to me**. The actions offered depend on the workflow step.

##### Responsibility
- D365 End-user: acts on the work items assigned to them.

##### Initiation
- A work item is assigned to the user.

##### Procedure

Complete these steps to act on a work item:

| **Action** | **Description** |
|---|---|
| *PROCESS START* | Pre-requisites:<br>• A work item is assigned to you.<br>Responsibility:<br>• D365 End-user |
| 1. *Open* **Work items assigned to me**. | On the dashboard, find **Work items assigned to me**, or from the **Navigation Pane**, *select*:<br>• **Modules >**<br>• **Common >**<br>• **Work items >**<br>• **Work items assigned to me**<br><mark>Microsoft Learn example (demo data): Work items assigned to me on the dashboard. Replace with a WTG screenshot.</mark> |
| 2. *Click* the document link. | Click the document ID to open the document. |
| 3. *Review* the document. | Review the document, its attachments and the submitter’s comment. **Workflow** > **View history** shows its history. |
| 4. *Click* **Workflow**. | On the Action Pane, click **Workflow**. |
| 5. *Select* the action. | **Approve** to approve; **Reject** to end the workflow; **Request change** to return it to the submitter; **Delegate** to give it to another user. |
| 6. *Enter* the comment. | Enter a comment, and for **Delegate** the user, then confirm. Your comment is kept in the workflow history. |
| 7. *Confirm* the work item is done. | Check that the item is no longer in **Work items assigned to me**. |
| *PROCESS COMPLETE* | Outcomes:<br>• The work item is completed and the document has moved on in its workflow. |

#### 11.3 Delegate Your Work Items While Away

##### Description

Use this procedure to send the work items assigned to you during an absence to another user automatically. The delegation applies to new work items in the period you set. Agree it with the person first.

##### Responsibility
- D365 End-user: sets up delegation before planned absence.

##### Initiation
- A user who receives work items will be away.

##### Procedure

Complete these steps to delegate your work items while away:

| **Action** | **Description** |
|---|---|
| *PROCESS START* | Pre-requisites:<br>• The person you delegate to has agreed and has access to the documents.<br>Responsibility:<br>• D365 End-user |
| 1. *Click* **Settings**. | On the navigation bar, click **Settings** (gear), then **User options**. |
| 2. *Click* the **Workflow** tab. | Click **Workflow** and expand **Delegation**.<br><mark>Microsoft Learn example (demo data): User options, Workflow tab: Delegation. Replace with a WTG screenshot.</mark> |
| 3. *Click* **Add**. | Click **Add**. |
| 4. *Select* the **Scope**. | Select **All** for every work item, or **Module** or **Workflow** for one kind, then select it in **Name**. |
| 5. *Select* the **Delegate**. | Select the user who acts for you. |
| 6. *Enter* the dates. | Enter the **Start date/time** and **End date/time** of your absence, and a **Comment**. |
| 7. *Select* **Enabled**. | Turn on **Enabled**, then click **Save**. |
| *PROCESS COMPLETE* | Outcomes:<br>• New work items assigned to you in the period go to your delegate. |

<mark>Company rules for delegation to be confirmed. `[[Q06] GS-27: Confirm]`</mark>

### 12. Set Up an Alert

##### Description

Use this topic to be told when a record changes or a date falls due, for example when a vendor’s bank account changes or an invoice is due. Alerts appear in the **Action center** and can also be emailed. They are created by a background job, so an alert can arrive some minutes after the change.

##### Responsibility
- D365 End-user: sets up alerts for the records they monitor.

##### Initiation
- A user needs to know when a record changes or a date is due.

##### Procedure

Complete these steps to set up an alert:

| **Action** | **Description** |
|---|---|
| *PROCESS START* | Pre-requisites:<br>• The page with the record is open.<br>Responsibility:<br>• D365 End-user |
| 1. *Check* the **Entity**. | Confirm you are signed into the correct **Legal Entity** (top-right). To change it, see 3.1 Switch Legal Entity with the Selector. |
| 2. *Select* the record and field. | Select the record, and click in the field the alert is about, for example **Due date**. |
| 3. *Click* the **Options** tab. | On the Action Pane, click **Options**. |
| 4. *Click* **Create alert rule**. `[[Q07] GS-23: Confirm]` | In the **Share** group, click **Create alert rule**. The **Create alert rule** dialog opens. |
| 5. *Select* the event. | Under **Alert me when**, select the **Field** and the **Event**, for example **has changed** or **is due in**.<br><mark>Microsoft Learn example (demo data): The Create alert rule dialog. Replace with a WTG screenshot.</mark> |
| 6. *Select* the records. | Under **Alert me for**, select **Current selected record** or **All records** in the current view. Filter the page first to narrow **All records**. |
| 7. *Enter* the end date. | Under **Alert me until**, choose an end date or no end. |
| 8. *Enter* the **Subject**. | Under **Alert me with**, enter a **Subject** and **Message**. Turn on **Send email** to receive it by email too. |
| 9. *Click* **OK**. | Click **OK** to create the rule. |
| *PROCESS COMPLETE* | Outcomes:<br>• The alert rule is active; its alerts arrive in the **Action center**. |

> **Note:** To change or delete your alerts, select **Options** > **Alert me** to open **Manage alert rules**.

### 13. Get Help and Report a Problem

##### Description

Use this topic to understand the messages D365 shows, find help for the page you are on, raise a problem with the BAU Support team, and reset your own settings when a page behaves oddly.

##### Responsibility
- D365 End-user: reads system messages, uses the help available and reports problems.

##### Initiation
- A message appears, a user needs help with a page, or something does not work.

##### Topic Overview

This topic includes these steps:

| Step | Description |
|---|---|
| 13.1 Read System Messages | Read the message bar, message details and the Action center. |
| 13.2 Use the Help Pane | Open help for the current page. |
| 13.3 Raise a Problem with the BAU Support Team | Report a problem or an access issue, with the details support needs. |
| 13.4 Reset Your Usage Data | Optional. Clear your saved usage data and personalizations. |

#### 13.1 Read System Messages

##### Description

Use this procedure to read the messages D365 shows: messages about the current page in the message bar, and messages from background work in the Action center. See System messages in Part 1.

##### Responsibility
- D365 End-user: reads and acts on the messages D365 shows.

##### Initiation
- A message appears in the message bar, or the Action center bell shows new messages.

##### Procedure

Complete these steps to read system messages:

| **Action** | **Description** |
|---|---|
| *PROCESS START* | Pre-requisites:<br>• Access to D365.<br>Responsibility:<br>• D365 End-user |
| 1. *Read* the message bar. | Read the message below the Action Pane. It names the field or record to fix. |
| 2. *Click* **Message details**. | Optional. If the message summarizes several messages, click **Message details** to see each one.<br><mark>Microsoft Learn example (demo data): An error in the message bar with Message details. Replace with a WTG screenshot.</mark> |
| 3. *Fix* the cause. | Correct the value or the step the message names, then repeat the action. |
| 4. *Click* the **Action center**. | On the navigation bar, click the bell, or press **Ctrl+Shift+F7** (**Open message center**), to read messages from reports, batch jobs and alerts.<br><mark>Microsoft Learn example (demo data): Messages in the Action center. Replace with a WTG screenshot.</mark> |
| 5. *Copy* the message text. | If you cannot fix the cause, copy the full message text for the BAU Support team (13.3). |
| *PROCESS COMPLETE* | Outcomes:<br>• The message is understood and acted on, or ready to report. |

#### 13.2 Use the Help Pane

##### Description

Use this procedure to open help for the page you are on. The Help pane lists Microsoft articles for the current page; an article opens in a new browser tab. Hover over a field to see its description. Microsoft’s help describes standard D365: your process guide is the reference for how WiseTech Global uses it.

##### Responsibility
- D365 End-user: uses the Help pane for the page they are on.

##### Initiation
- A user needs to understand a page or field.

##### Procedure

Complete these steps to use the Help pane:

| **Action** | **Description** |
|---|---|
| *PROCESS START* | Pre-requisites:<br>• Access to D365.<br>Responsibility:<br>• D365 End-user |
| 1. *Click* **Help & Support**. `[GS-24]` | On the navigation bar, click **Help & Support** (?). |
| 2. *Click* **Help**. | Click **Help**. The Help pane opens with articles for the current page.<br><mark>Microsoft Learn example (demo data): The Help pane for the current page. Replace with a WTG screenshot.</mark> |
| 3. *Search* the help. | Optional. If no article fits, type keywords in the search box. |
| 4. *Select* an article. | Select an article. It opens in a new browser tab. |
| *PROCESS COMPLETE* | Outcomes:<br>• The help article for the page is open. |

> **Important:** If a task guide is offered in the Help pane, the data you enter while it plays is real. Do not play task guides in the live environment.

#### 13.3 Raise a Problem with the BAU Support Team

##### Description

Use this procedure to report a D365 problem, or a missing page, module, legal entity or button, to the BAU Support team. Do not use the **Support** option on the D365 Help menu: it goes to Microsoft’s support, not WiseTech Global’s. Give the details below so the team can find the problem quickly.

##### Responsibility
- D365 End-user: reports problems and access issues to the BAU Support team.

##### Initiation
- Something in D365 does not work, a message cannot be resolved, or access is missing.

##### Procedure

Complete these steps to raise a problem with the BAU Support team:

| **Action** | **Description** |
|---|---|
| *PROCESS START* | Pre-requisites:<br>• Access to D365.<br>Responsibility:<br>• D365 End-user |
| 1. *Note* the legal entity and page. | Note the legal entity (top-right), the page name and its URL from the address bar. |
| 2. *Note* the steps. | Note what you did, step by step, and what you expected to happen. |
| 3. *Copy* the message. | Copy the full text of any message, with its **Message details** (see 13.1 Read System Messages). |
| 4. *Take* a screenshot. | Take a screenshot that shows the page and the message. |
| 5. *Raise* the issue. `[[Q08] GS-25: Confirm]` | Raise the issue with the BAU Support team through the D365 issue form in **Additional Resources**, with the details from steps 1 to 4. <mark>Confirm the route: the D365 issue form, the Atlas D365 User Support Hub or AVA.</mark> |
| *PROCESS COMPLETE* | Outcomes:<br>• The problem is reported to the BAU Support team with the details they need. |

#### 13.4 Reset Your Usage Data

##### Description

Use this procedure to see and delete the data D365 keeps about how you use it, such as saved personalizations, and to show again the feature pop-ups you dismissed. Use it when the BAU Support team advises it. Deleted personalizations cannot be restored.

##### Responsibility
- D365 End-user: resets their own usage data when advised.

##### Initiation
- The BAU Support team advises resetting usage data, or a user wants to remove old personalizations.

##### Procedure

Complete these steps to reset your usage data:

| **Action** | **Description** |
|---|---|
| *PROCESS START* | Pre-requisites:<br>• Access to D365.<br>Responsibility:<br>• D365 End-user |
| 1. *Click* **Settings**. | On the navigation bar, click **Settings** (gear), then **User options**. |
| 2. *Click* **Usage data**. `[GS-26]` | On the Action Pane, click **Usage data**. |
| 3. *Click* the **Personalization** tab. | Click **Personalization** to see your saved personalizations. |
| 4. *Select* the data to delete. | Select the rows to remove, or use the option to reset feature callouts. |
| 5. *Click* **Delete**. | Click **Delete** and confirm. |
| *PROCESS COMPLETE* | Outcomes:<br>• The selected usage data is deleted. |

---

## Part 3: Reports (Getting Started)

##### Overview

These inquiry pages support the tasks in this guide: they show the output of your background reports and the progress of the documents you submit to workflow. The reports for each process are in that process guide’s Part 3.

##### My batch jobs

| **Navigation** | **Description** |
|---|---|
| **Common*** > *<br>**Inquiries*** > *<br>**Batch jobs*** > *<br>**My batch jobs** | Shows the batch jobs you created, such as reports run in the background, with their status: Waiting, Executing, Ended or Error. Use it after 9.3 Run a Report in the Background to check that your job finished, and contact the BAU Support team if it shows **Error**. |

##### Print archive

| **Navigation** | **Description** |
|---|---|
| **Common*** > *<br>**Inquiries*** > *<br>**Print archive** | Holds the reports sent to the **Print archive**, including those run in the background. Find a report by its description and select **Print preview** to open, download or print it (9.4 Find Background Output). |

##### Workflow history

| **Navigation** | **Description** |
|---|---|
| **Common*** > *<br>**Inquiries*** > *<br>**Workflow*** > *<br>**Workflow history** | Shows each document submitted to workflow: its status, who it is with, and every action and comment. Use it to follow a document you submitted (11.1 Submit a Document to Workflow), or open it from the document with **Workflow** > **View history**. |

##### Work items assigned to me

| **Navigation** | **Description** |
|---|---|
| **Common*** > *<br>**Work items*** > *<br>**Work items assigned to me** | Lists the workflow tasks and approvals waiting for you, with links to each document. The same list is on the dashboard. Check it daily if you approve documents (11.2 Act on a Work Item). |

---

## Additional Resources
