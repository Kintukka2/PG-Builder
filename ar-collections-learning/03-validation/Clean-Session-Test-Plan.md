# Clean-Session D365 Test Plan: AR Collections Guides

| Field | Value |
|---|---|
| Scope | The 13 AR Collections procedure guides in SME review draft |
| Items tested | 148 open validation items whose method includes **Test** (112 blocking, 36 non-blocking), across all 13 validation registers |
| Route | 16 stations, 87 steps, in one session; station S13 is gated |
| Results log | [`Clean-Session-Test-Log.xlsx`](Clean-Session-Test-Log.xlsx): one row per step and one row per item |
| Status | Draft plan for SME review. Not yet run. |
| Last updated | 2026-10-15 |

This plan tests the drafts against D365. It does not change them. Every step names the validation items it tests (`FAV 02` means Favorites VG-02). Record what D365 actually shows; where it differs from the draft, the draft changes.

Guide keys:

| Key | Guide | Validation register |
|---|---|---|
| FAV | AR Collections Favorites | [`PG-AR-Configure-Collections-Favourites-Validation.md`](PG-AR-Configure-Collections-Favourites-Validation.md) |
| VIEW | AR Collections Personalized Views | [`PG-AR-Personalized-Views-Validation.md`](PG-AR-Personalized-Views-Validation.md) |
| AGED | AR Collections Aged Balances | [`PG-AR-Aged-Balances-Validation.md`](PG-AR-Aged-Balances-Validation.md) |
| INV | AR Collections Customer Invoices | [`PG-AR-Customer-Invoices-Validation.md`](PG-AR-Customer-Invoices-Validation.md) |
| EXP | AR Collections Export to Excel | [`PG-AR-Export-to-Excel-Validation.md`](PG-AR-Export-to-Excel-Validation.md) |
| NOTE | AR Collections Notes and Activities | [`PG-AR-Notes-and-Activities-Validation.md`](PG-AR-Notes-and-Activities-Validation.md) |
| LE | AR Collections Legal Entities | [`PG-AR-Legal-Entities-Validation.md`](PG-AR-Legal-Entities-Validation.md) |
| WS | AR Collections Workspace | [`PG-AR-Workspace-Validation.md`](PG-AR-Workspace-Validation.md) |
| OD | AR Collections Overdue Customers | [`PG-AR-Overdue-Customers-Validation.md`](PG-AR-Overdue-Customers-Validation.md) |
| ACCT | AR Collections Customer Account | [`PG-AR-Customer-Account-Validation.md`](PG-AR-Customer-Account-Validation.md) |
| ACT | AR Collections Collection Activities | [`PG-AR-Collection-Activities-Validation.md`](PG-AR-Collection-Activities-Validation.md) |
| SP | AR Collections Statement Preview | [`PG-AR-Statement-Preview-Validation.md`](PG-AR-Statement-Preview-Validation.md) |
| SD | AR Collections Statement Distribution | [`PG-AR-Statement-Distribution-Validation.md`](PG-AR-Statement-Distribution-Validation.md) |

---

## 1. Safety rules

These apply for the whole session. Stop and record the step ID if any of them cannot be kept.

1. **Use the test customer only.** No step touches a real customer account.
2. **Change nothing financial.** Do not tick **Mark**, settle, post, or use **Undo settlement** (S9 is read-only).
3. **Send nothing to a customer.** In S12, clear **Print management destination** and select **Screen** before generating. Run S13 only when its gate is met.
4. **Mock text only.** The S11 activity uses "TEST - mock activity". Real collection notes are never typed or captured.
5. **Handle files as customer data.** Store exported and downloaded files only where approved, and delete them at S15 (Export to Excel VG-08 is still open).
6. **Do not diagnose access.** If a page or control is missing, record it as a possible security cause in S15. Do not conclude it is a security issue.
7. **Mask screenshots.** Follow the [clean-session specification](../02-screenshot-registers/PG-AR-Configure-Collections-Favourites-Screenshots.md#4-clean-session-recapture-specification). The masking policy is still open (Favorites VG-27).

---

## 2. Before the session

| # | Prerequisite | Needed for | Ready |
|---|---|---|---|
| P1 | A training or demonstration environment, as source 2's capture standards require. The SME confirms which one. | All | ☐ |
| P2 | A test user with the standard AR Collections security role, who has never added the four Favorites pages or saved views. | All; S2; S6; S15 | ☐ |
| P3 | The test user can access two legal entities. | S1, S3, S4, S8, S14 | ☐ |
| P4 | A **test customer** with: at least one open, overdue invoice; one closed transaction; one payment settled against an invoice; one user-entered note and one entry created by D365. | S4, S5, S8, S9, S10, S12 | ☐ |
| P5 | Optional on the test customer: a credit note and a foreign-currency transaction. | S8 (revaluations), S10 step 5 | ☐ |
| P6 | For S13 only: the test customer's statement recipient is an internal mailbox, confirmed by the SME. | S13 | ☐ |
| P7 | Screen recording running, and the results log open. | All | ☐ |
| P8 | A second browser and, optionally, a second test user. | S14 | ☐ |

**S13 gate.** Run S13 only after the SME has answered Statement Distribution VG-05 (Print management destination), VG-06 (recipient source), VG-10 (failed delivery), VG-12 (multi-currency exclusions) and VG-17 (approved parameters), and P6 is confirmed. Otherwise skip it; its 3 items stay open.

---

## 3. Session route

The order reuses each page once: menus are walked once (S2) and serve every later guide, and the Aged balances grid (S6) is reused for the export (S7).

| Station | Title | Guides | Items tested | Blocking |
|---|---|---|---|---|
| [S0](#s0-session-setup-and-navigation-pane) | Session setup and Navigation Pane | FAV, WS | 5 | 2 |
| [S1](#s1-legal-entity-switching) | Legal entity switching | LE, FAV | 7 | 4 |
| [S2](#s2-modules-menus-and-favorites) | Modules, menus and Favorites | FAV, AGED, ACCT, NOTE, ACT | 14 | 12 |
| [S3](#s3-customer-credit-and-collections-workspace) | Customer credit and collections workspace | WS, NOTE, OD | 12 | 8 |
| [S4](#s4-notes) | Notes | NOTE | 4 | 3 |
| [S5](#s5-customers-overdue) | Customers overdue | OD, ACT | 8 | 5 |
| [S6](#s6-aged-balances-and-personalized-views) | Aged balances and personalized views | AGED, VIEW | 23 | 20 |
| [S7](#s7-export-all-rows) | Export all rows | EXP | 7 | 4 |
| [S8](#s8-customer-account-and-transactions) | Customer account and transactions | ACCT, NOTE, ACT, INV | 11 | 9 |
| [S9](#s9-settlement-history-review-only) | Settlement history (review only) ⚠️ | ACCT, INV | 4 | 4 |
| [S10](#s10-customer-invoice) | Customer invoice | INV | 6 | 5 |
| [S11](#s11-activities) | Activities | NOTE, ACT | 10 | 7 |
| [S12](#s12-statement-preview) | Statement preview ⚠️ | SP, SD | 14 | 13 |
| [S13](#s13-statement-send-gated) | Statement send (gated) ⚠️ | SD | 3 | 3 |
| [S14](#s14-persistence) | Persistence | FAV, VIEW, LE | 5 | 0 |
| [S15](#s15-security-role-and-wrap-up) | Security role and wrap-up | ALL | 15 | 13 |
| | **Total** | | **148** | **112** |

---

## 4. Stations

### S0 Session setup and Navigation Pane

Start a clean session and record the baseline before anything is changed.

| Step | Action | Record | Items |
|---|---|---|---|
| S0.1 | Sign in with the test user in a fresh browser profile (no saved favorites, views or history). Note the date, environment, browser, zoom and D365 language setting. | Environment name, browser and version, zoom, language setting, user ID (masked in screenshots). | — |
| S0.2 | Check how the D365 interface spells Favorites in the Navigation Pane. | Exact spelling shown: "Favorites" or "Favourites". | FAV 28 |
| S0.3 | Hover over each Navigation Pane icon in turn: Home, Favorites, Recents, Workspaces, Modules. | Each icon's tooltip or label. Describe the Modules and Workspaces icons. | FAV 08, 09; WS 01 |
| S0.4 | Collapse the Navigation Pane, then show it again. | The control that hides and shows the Navigation Pane, and its label. | FAV 12 |

### S1 Legal entity switching

Confirm the selector, the URL method and what changes when the legal entity changes. Uses two legal entities the test user can access.

| Step | Action | Record | Items |
|---|---|---|---|
| S1.1 | Find the legal entity selector in the D365 header and click it. | Exact label and location; what the list shows (business names, ledger codes or both); whether it can be searched. | LE 01, 02 |
| S1.2 | Open any page (for example a workspace), then select the second legal entity. | What D365 displays after the switch (same page or dashboard); whether the open page or unsaved input is affected. | LE 03, 11 |
| S1.3 | Check how the active legal entity is shown after the switch. | Where and how the active legal entity is displayed. | LE 04 |
| S1.4 | Look at the browser address bar and find the part of the URL that holds the ledger code. Change it to the first legal entity's D365 ledger code and press Enter. | The URL part that holds the code (do not record the environment address); whether the switch works; what is displayed. | LE 05 |
| S1.5 | Return to the legal entity used for the rest of the session. Note whether the entity affects what the Favorites guide asks users to check first. | Whether Step 1 (Check the Entity) is needed in the Favorites guide. | FAV 23 |

### S2 Modules, menus and Favorites

Walk the module menus once and run the Favorites guide. This tests the shared menu-group items for every later guide.

| Step | Action | Record | Items |
|---|---|---|---|
| S2.1 | Click Modules and open Credit and collections. | Exact module label as listed. Whether pages sit inside a menu group or submenu, and whether it must be expanded first. | FAV 06, 21 |
| S2.2 | Find All customers in Credit and collections. | Menu group or submenu that contains All customers. | FAV 02; ACCT 01; NOTE 07; ACT 01 |
| S2.3 | Find Aged balances in Credit and collections. | Exact page label (Aged balances or Age balances) and its menu group. | FAV 01, 03; AGED 01, 02 |
| S2.4 | Find Customer payment journal in Credit and collections. | Whether it is in Credit and collections, and its menu location. | FAV 04 |
| S2.5 | Open Accounts receivable and find Open customer invoices. | Menu group or submenu that contains Open customer invoices. | FAV 05 |
| S2.6 | Add All customers to Favorites with its star. Capture the star before and after. Click the selected star once more, then re-add it if it was removed. | Star appearance before and after; whether it shows only on hover; whether clicking a selected star removes the favorite. | FAV 07 |
| S2.7 | Add Aged balances, Customer payment journal and Open customer invoices to Favorites. Open Favorites. | The order in which the four favorites are listed. | FAV 13 |

### S3 Customer credit and collections workspace

Open the workspace and locate the four sections the guides use.

| Step | Action | Record | Items |
|---|---|---|---|
| S3.1 | Click Workspaces and select the Customer credit and collections workspace. | Exact workspace label in the list; how the workspace opens. | WS 02; NOTE 02 |
| S3.2 | Describe what the workspace shows when it opens. Compare its name with the Credit and collections module. | The workspace layout and section names; the labels that distinguish workspace from module. | WS 03, 11 |
| S3.3 | Locate Customers overdue. | Exact label and location. | WS 04; OD 01 |
| S3.4 | Locate Payment journals not posted. | Exact label and location. | WS 05 |
| S3.5 | Locate Notes. | Exact label and location. | WS 06; NOTE 01 |
| S3.6 | Locate Open payment journals. | Exact label and location. | WS 07 |
| S3.7 | Switch to the second legal entity and back, and watch the section counts or lists. Check whether the workspace can be starred or opened from the dashboard. | Whether sections change with the legal entity; whether the workspace can be added to Favorites or the dashboard. | WS 10, 12 |

### S4 Notes

Filter Notes to the test customer and identify entry types.

| Step | Action | Record | Items |
|---|---|---|---|
| S4.1 | Open Notes and open the filter for the customer column. Filter to the test customer. | Exact customer column label and how its filter opens. | NOTE 03 |
| S4.2 | Check the creator, date and note type columns. Filter by one of them. | Exact labels of the creator, date and note type columns, and whether a note type column exists. | NOTE 04 |
| S4.3 | Compare a user-entered note with an entry created by D365 (for example a statement or collection letter). | How users tell the two apart (column, value or icon). | NOTE 06 |
| S4.4 | Check whether notes from the second legal entity appear. | Yes or no, and how they are identified. | NOTE 13 |

### S5 Customers overdue

Review Customers overdue and open an account from it.

| Step | Action | Record | Items |
|---|---|---|---|
| S5.1 | Open Customers overdue from the workspace. Note the aging period shown when it opens. | The default aging period. | OD 03 |
| S5.2 | Find the aging period control. Select 90+, then 61-90. | Label and location of the control; the periods available. | OD 02 |
| S5.3 | Identify the balance due and overdue amount columns. | Exact column labels. Record any tooltip or help text that explains them (meanings still need SME confirmation). | OD 04 |
| S5.4 | Sort the overdue amount column from largest to smallest. | How the column is sorted and the sort option label. | OD 05 |
| S5.5 | Use Insert columns to add the customer email column. | Exact email column label; whether it can be added on this page. | OD 06 |
| S5.6 | Check whether the zero-balance, currency and customer filters used on Aged balances work here. | Which filters work. | OD 22 |
| S5.7 | Check whether a new activity can be created from this page. Do not create one here. | Yes or no, and the control label. | ACT 03 |
| S5.8 | Open the test customer's account from the list. | How the account opens (for example the account number link). | OD 07 |

### S6 Aged balances and personalized views

Run the Aged Balances guide and the Personalized Views guide on the same grid. Save one test view.

| Step | Action | Record | Items |
|---|---|---|---|
| S6.1 | Open Aged balances from Favorites. Check whether the Currency column is shown, and whether the page has an aging period or band selector. | Currency column shown by default (yes or no); any aging period or band selector and its label. | AGED 11, 12 |
| S6.2 | Click Insert columns, add Currency and apply the selection. | Location of Insert columns on this page; what D365 displays; the control that applies the selection. | AGED 04; VIEW 03, 04 |
| S6.3 | Remove one column, then move another column to a new position. | How a column is removed and its label; how columns are repositioned. | VIEW 05, 06 |
| S6.4 | Identify the balance column to filter. Open its filter, select not equal to, enter 0 and apply. | Exact balance column label; how the filter opens; operator labels; the apply control. | AGED 03, 05; VIEW 07, 08, 29 |
| S6.5 | Sort the balance column from largest to smallest. | How the column is sorted and the sort option label. | AGED 06 |
| S6.6 | Open the customer column filter, select is one of and choose two customers. | Exact customer column label; whether is one of allows several. | AGED 07 |
| S6.7 | Show the grid footer and add a sum to the balance column. | How the footer is shown; how a sum is added; which columns support a sum. | VIEW 09, 10 |
| S6.8 | Save the layout as a new view named "TEST - delete after session". Complete Save as. | Label and location of Save as; the control that completes it. | VIEW 11, 13 |
| S6.9 | Pin the test view as the default. Note how D365 shows the saved view and the pinned default. | Label and location of Pin as default and what it does; how a saved and a pinned view are shown. | VIEW 14, 15 |
| S6.10 | Change the view (add a column), save the change to the existing view, then reselect the view from the view selector. | The control that saves changes to an existing view; how a saved view is selected. | VIEW 16, 17 |
| S6.11 | Leave the page and come back. Check whether the filter and footer total are kept. | Whether filters and totals are saved with the view. | VIEW 18 |

### S7 Export all rows

Export the test view from Aged balances. Use test or mock data only, and delete the file after the session.

| Step | Action | Record | Items |
|---|---|---|---|
| S7.1 | Right-click a column heading of the Aged balances grid. | Where the right-click works (any heading or a specific part). | EXP 02 |
| S7.2 | Select Export all rows. | Exact label; what D365 displays; any volume limit message. | EXP 01, 06 |
| S7.3 | Download the file. | Label of the download control; file format; where the file is saved. | EXP 03, 07 |
| S7.4 | Open the file and compare it with the grid. | Whether hidden columns are left out, and whether rows hidden by the filter are included. | EXP 04, 05 |

### S8 Customer account and transactions

Open the test customer from All customers and review transactions without changing anything.

| Step | Action | Record | Items |
|---|---|---|---|
| S8.1 | Open All customers from Favorites and open the test customer's account. Note whether Aged balances and Customers overdue also opened it (S5, S6). | How the account opens; whether the other routes are suitable for the guides. | ACCT 02, 03; NOTE 08; ACT 02 |
| S8.2 | Find the balance and overdue amount on the account. | Exact labels and location. | ACCT 04 |
| S8.3 | Open the customer's transactions. | Label and location of the control; the page name and path. | ACCT 05; INV 01 |
| S8.4 | Select Show open, then Show closed, then return to Show open. | Exact labels and location; what each shows. | ACCT 06 |
| S8.5 | Hide currency revaluations. | Exact label and location of the control. | ACCT 07 |
| S8.6 | Check the due date, amount, currency and description columns. Switch legal entity and back to see if other entities' transactions appear. | Exact column labels; whether other legal entities appear. | ACCT 09, 14 |

### S9 Settlement history (review only)

Read a settled transaction's history. Do not mark rows, settle, or use Undo settlement.

> ⚠️ **Read-only: no settlement changes.**

| Step | Action | Record | Items |
|---|---|---|---|
| S9.1 | Click a settled payment so it is highlighted. Do not tick its Mark checkbox. | How a row is highlighted; that marking is not needed. | ACCT 10; INV 02 |
| S9.2 | Click View settlements. | Exact label and location. | ACCT 11 |
| S9.3 | Read the settlement history, then close it without changes. | What it shows (settled-against transactions, amounts, dates) and how to read it. | ACCT 12 |

### S10 Customer invoice

Open an invoice from its transaction and download the PDF.

| Step | Action | Record | Items |
|---|---|---|---|
| S10.1 | Highlight an invoice transaction and click Original document. | Exact label and location; what D365 displays. | INV 03 |
| S10.2 | Select the invoice in the original document list. | What the list shows and how the invoice is selected. | INV 04 |
| S10.3 | Click Print preview. | Exact label and location; how the preview is displayed. | INV 05 |
| S10.4 | Download the invoice as PDF. | Label and location of the download control; whether the file is named before or after the download. | INV 07, 10 |
| S10.5 | Repeat steps 1 to 3 for a credit note, if the test customer has one. | Whether the same steps apply to other document types. | INV 11 |

### S11 Activities

Review activities and record one mock activity on the test customer.

| Step | Action | Record | Items |
|---|---|---|---|
| S11.1 | On the test customer's account, click View all activities. Filter the list. | Exact label and location; which columns can be filtered. | NOTE 09, 10 |
| S11.2 | Compare the activities list with the Notes entries for the same customer. | How activities relate to Notes entries. | NOTE 12 |
| S11.3 | Click New activity. | Exact label and location. | ACT 04 |
| S11.4 | Select an activity type. Enter a summary and notes using mock text only ("TEST - mock activity"). | Exact labels of the type, summary and notes fields; the type values offered. | ACT 05, 07, 08 |
| S11.5 | Save the activity and check that it is listed. | The save control; where the activity appears. | ACT 12, 13 |
| S11.6 | Check whether system-generated activities appear and how they differ. | How they are identified. | ACT 15 |

### S12 Statement preview

Preview a statement for the test customer with Screen as the destination. Nothing is sent.

> ⚠️ **Confirm Print management destination is cleared before generating.**

| Step | Action | Record | Items |
|---|---|---|---|
| S12.1 | Open the Statements page. | Exact label and navigation path. | SP 01; SD 01 |
| S12.2 | Select the test customer. | How the customer is selected (for example the records to include filter). | SP 02; SD 02 |
| S12.3 | Find Only open and the company logo option. | Exact labels. | SP 03, 04; SD 03, 04 |
| S12.4 | Find Print management destination. Clear it and select Screen. | Exact labels and location; how it is cleared. | SP 05, 06 |
| S12.5 | Generate the statement. | The control that generates it; that it opens on screen. | SP 07 |
| S12.6 | Download the statement as PDF. | Download control; whether the file is named before or after. | SP 09, 12 |
| S12.7 | Check whether the test customer is excluded from statements, and how this is shown. | Where the exclusion setting is visible. | SD 13 |

### S13 Statement send (gated)

Send one statement to the test customer, whose statement recipient is an internal mailbox.

> ⚠️ **GATED: run only after the SME closes Statement Distribution VG-05, VG-06, VG-10, VG-12 and VG-17, and the test customer's recipient is confirmed as an internal mailbox. Skip otherwise.**

| Step | Action | Record | Items |
|---|---|---|---|
| S13.1 | With the approved parameters, select Print management destination. | Exact label; what the option does. | SD 05 |
| S13.2 | Generate the statement. | The control that generates and sends it. | SD 07 |
| S13.3 | Read the delivery message. | Exact wording and location. | SD 08 |

### S14 Persistence

Check what carries over between legal entities, sessions and browsers.

| Step | Action | Record | Items |
|---|---|---|---|
| S14.1 | Switch to the second legal entity. Check Favorites and the test view on Aged balances. | Whether favorites and the view are available there. | FAV 10; VIEW 02; LE 12 |
| S14.2 | Sign out and in again; then sign in from a second browser. | Whether favorites persist between sessions and browsers. | FAV 11 |
| S14.3 | Optional, with a second test user: check whether the test view is visible to them. | Whether a saved view is personal. | VIEW 19 |

### S15 Security role and wrap-up

Record the role used and anything that was not available, then clean up.

| Step | Action | Record | Items |
|---|---|---|---|
| S15.1 | Record the test user's security role name. List every control or page in S0 to S13 that was missing or disabled. Record each as a possible security cause, not a confirmed one. | Role name; missing items with the step ID. | FAV 17; VIEW 25; AGED 19; INV 18; EXP 17; LE 19; NOTE 19; WS 19; OD 19; ACCT 21; ACT 21; SP 21; SD 23 |
| S15.2 | Note any AR Collections page that showed data from more than one legal entity. | Page names. | LE 22 |
| S15.3 | Check the screenshots taken against the clean-session specification. | Screenshot set reference. | FAV 24 |
| S15.4 | Clean up: unpin and delete the test view, remove test favorites if required, delete the exported and downloaded files, and leave the mock activity (record its ID). | Cleanup done (yes or no); mock activity ID. | — |

---

## 5. Coverage by guide

Items that need an SME answer, a recording or a project decision are not tested here. They stay open after the session.

| Guide | Open items | Tested here (B / N) | Stations | Left for SME, recording or decision |
|---|---|---|---|---|
| AR Collections Favorites | 30 | 18 (9 / 9) | S0, S1, S2, S14, S15 | 12 |
| AR Collections Personalized Views | 29 | 19 (16 / 3) | S6, S14, S15 | 10 |
| AR Collections Aged Balances | 22 | 10 (8 / 2) | S2, S6, S15 | 12 |
| AR Collections Customer Invoices | 22 | 9 (8 / 1) | S8, S9, S10, S15 | 13 |
| AR Collections Export to Excel | 20 | 8 (5 / 3) | S7, S15 | 12 |
| AR Collections Notes and Activities | 22 | 12 (9 / 3) | S2, S3, S4, S8, S11, S15 | 10 |
| AR Collections Legal Entities | 22 | 9 (5 / 4) | S1, S14, S15 | 13 |
| AR Collections Workspace | 22 | 11 (7 / 4) | S0, S3, S15 | 11 |
| AR Collections Overdue Customers | 22 | 9 (7 / 2) | S3, S5, S15 | 13 |
| AR Collections Customer Account | 24 | 13 (11 / 2) | S2, S8, S9, S15 | 11 |
| AR Collections Collection Activities | 24 | 11 (9 / 2) | S2, S5, S8, S11, S15 | 13 |
| AR Collections Statement Preview | 24 | 10 (10 / 0) | S12, S15 | 14 |
| AR Collections Statement Distribution | 25 | 9 (8 / 1) | S12, S13, S15 | 16 |
| **Total** | **308** | **148 (112 / 36)** | | **160** |

---

## 6. After the session

1. **Results log.** Complete the *Items* sheet: for each item, the result (*Confirmed*, *Differs from draft* or *Could not test*) and the evidence (step ID, screenshot or recording time).
2. **Validation registers.** For each tested item, change *Status* to *Closed* with the evidence, for example "Closed: test S6.4, 2026-10-xx". Items that differ from the draft stay open until the guide text is changed. Add a change-log entry to each register.
3. **Word guides.** Update the text to match D365, remove the review comment for each closed item, and move each changed guide to v0.2. Regenerate its PDF and Markdown preview.
4. **Command Centre.** Set each closed gap to *Closed* and move guides whose blocking test items are all closed to *System tested*.
5. **Findings.** Anything that contradicts the drafts or the sources goes to the SME with the step ID. Missing controls are listed as possible security causes (S15.1), not diagnoses.

## 7. Exit criteria

- Every step in S0 to S12, S14 and S15 has a result. S13 is either run under its gate or marked *Not run: gate not met*.
- Every tested item has a result and evidence in the *Items* sheet.
- Screenshots meet the clean-session specification, or none were taken.
- Cleanup in S15.4 is done.

## 8. Change log

| Date | Change |
|---|---|
| 2026-10-15 | Plan created from the 13 validation registers. |
