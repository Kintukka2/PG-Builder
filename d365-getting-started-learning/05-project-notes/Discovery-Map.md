# D365 F&O Getting Started: discovery map

> **Discovery output, 26 November 2026.** Not a guide draft. It maps what Microsoft documents and teaches about getting started in Dynamics 365 finance and operations apps, and proposes the topics for a **D365 F&O Getting Started PG** for finance end users in every stream (O2C, P2P, R2R, Tax). **Decided 26 November 2026** (section 6): two guides, *D365 F&O Getting Started* for all D365 users and *D365 Finance Basics* for finance users, codes from the 100 series later, 260 unchanged, Copilot and AI out. How the outline below splits between the two guides is in the [project notes](Project-Context-and-Decisions.md#1-the-two-guides).

## 1. What was researched

| Area | Write-up | Screenshots | Coverage |
|---|---|---|---|
| A. UI shell and navigation | [A-ui-navigation.md](discovery/A-ui-navigation.md) | [36](discovery/media/ui-navigation/) | Screen elements, navigation pane, dashboard, Immersive Home, User options (all tabs), company picker, navigation and action search, Favorites and Recent, Open in new window, View/Edit mode, save/revert/refresh/delete, page types, session date, lookups and date pickers, keyboard shortcuts, messages, accessibility, session timeout, Client FAQ, what's new 10.0.41 to 10.0.50 |
| B. Grids, filters, personalization, saved views | [B-grids-filters-views.md](discovery/B-grids-filters-views.md) | [15](discovery/media/grids-views/) | Grid control, totals, grouping, freezing, selection, paste from Excel, math in fields, all filter tools, full operator and query-syntax tables, workspaces, personalization toolbar, saved views, custom fields, shortcut tables, comparison with 260 |
| C. Office, reports, documents, batch, alerts | [C-office-reports-batch-alerts.md](discovery/C-office-reports-batch-alerts.md) | [44](discovery/media/office-reports-batch/) | Export to Excel, Open in Excel and the add-in, attachments, email, report dialog and destinations, print archive, financial reports, Power BI, ER outputs, Run in the background, My batch jobs, alerts, Action center |
| D. Workflow, help, Copilot, troubleshooting | [D-workflow-help-copilot.md](discovery/D-workflow-help-copilot.md) | [28](discovery/media/workflow-help-copilot/) | Every workflow action, work items, history, delegation, help pane and task guides, Copilot sidecar and summaries, finance agents, Teams and mobile, session basics, resetting settings |
| E. Finance concepts and how others onboard | [E-finance-concepts-and-onboarding-patterns.md](discovery/E-finance-concepts-and-onboarding-patterns.md) | [38](discovery/media/finance-concepts/) | 19 shared finance concepts (legal entities, dimensions and segmented entry, journals, vouchers, periods, dates, inquiries, reversals, currency, GST, parties, number sequences, intercompany) and 16 external onboarding sources compared |
| F. Microsoft Learn modules | [F-learn-modules-inventory.md](discovery/F-learn-modules-inventory.md) | [learn-modules/](discovery/learn-modules/) | 33 modules (352 units) read in full: catalogue, topic inventory, screenshot catalogue, 21 conflicts, 20 outdated items, ranked topics. Knowledge checks: [KNOWLEDGE-CHECKS.md](discovery/learn-modules/KNOWLEDGE-CHECKS.md) |

The full text of every Learn unit is in [`discovery/learn-modules/`](discovery/learn-modules/), one folder per module, each with an `INDEX.md` of unit URLs. Only the screenshots that the inventory (F) cites are stored, except six over 1.5 MB; the rest are on the unit pages. The image counts in each `INDEX.md` predate a re-fetch and are not current.

**About the screenshots.** All are Microsoft images with demo data (Contoso, USMF), kept as layout references for the discovery. The guide's screenshots come from the clean-session test in our D365 environment. Many Microsoft images are old: most of the workflow and help images show the 2017 client.

## 2. What the research found

1. **The interface is stable.** No core UI redesign in 10.0.41 to 10.0.50 or in the 2025 wave 2 and 2026 wave 1 release plans. Grids, filters and saved views are unchanged for end users since 10.0.38. The only visible change is **Immersive Home** (10.0.44 or later, behind a feature switch). Release plans were archived in October 2026, and there is no 2026 wave 2 plan; Microsoft now points to its AI roadmap.
2. **Microsoft teaches the interface, not the finance basics.** The Learn path *Get started with finance and operations apps* covers the screen and navigation only. Nothing in it teaches entering dimensions, period status, dates, why posting fails or how to find a posted voucher, which is where new finance users make most mistakes (E, part 2, lists 14 common mistakes).
3. **Microsoft's own guidance supports one shared guide.** Success by Design advises keeping system training separate from process training, and training a shared system area once rather than in every process. That is the role of this guide: process guides link to it.
4. **The biggest gaps are reports, sessions and support.** There is no current Microsoft end-user article for the report dialog, print destinations, the print archive, **My batch jobs** or the message details pane; for signing in and out, several tabs, "Something went wrong", sharing a link to a record; or for what to capture for a support ticket. These topics must be written from the clean-session test, and they are among the most useful.
5. **Facts that change what the guide says:**
   - **Export to Excel** exports 50,000 rows by default (configurable up to 1,000,000; Microsoft recommends no more than 100,000), and the download link lasts 15 minutes.
   - The **interactive query time-out dropped from 30 to 5 minutes** in January 2026 (10.0.46), so large reports and runs belong in **Run in the background**.
   - The **Excel add-in** publishes up to 100 rows per batch, holds about 1 million cells, shows dates in UTC and does not run on Mac.
   - **Financial reports** expire after 90 days, and since 10.0.45 older reports recalculate their drill-down from current data: export the final version to keep an exact copy.
   - The Exchange email provider stopped working in September 2024.
   - The **F&O mobile app is retired**; approvals in Teams or Outlook exist only if IT built Power Automate flows.
   - **Copilot** answers from Microsoft's public documentation, not our setup, and several Copilot summaries are on by default (workflow history, Customer, Collections coordinator, Vendor, Purchase order).
   - Filter wildcards (`*`, `?`, `..`, `!`) work only with the **matches** operator; relative dates such as `(DayRange(-30,0))` keep a saved view current.
   - Footer totals and column widths save themselves; filters and personalization need **Save** or **Save as**. A page opened from a tile or a filtered menu item skips the default view.
6. **Microsoft contradicts itself** in places the guide must test rather than copy: the action search shortcut (Ctrl+/ or Ctrl+'; Alt+Q is in both), the help pane shortcut (Ctrl+Shift+? or Ctrl+?), the alert button label ("Create a custom alert" or "Create alert rule"), which side the Filter pane opens, and the personalization toolbar tool names. 21 conflicts are listed in F, section 4.

## 3. Proposed outline

Titles follow the template's verb-and-object rule. **Source** points to the research sections; **260** marks content that 260 O2C Getting Started already has. **Priority** is the research's must / should / nice-to-have for a new finance user.

### Part 1: What do I need to know?

Key concepts, each in the form its content needs (D-059):

| Key concept | What it covers | Source | Priority |
|---|---|---|---|
| How this guide fits | Shared skills here; each process guide adds its own pages, views and columns and links back | E part 2 (SbD) | Must |
| The parts of the screen | Navigation bar, navigation pane and modules, dashboard or Immersive Home, workspaces and tiles, Action Pane and tabs, FastTabs, FactBoxes, list and details pages, Grid / Details / Header / Lines views | A, F 2 | Must |
| Legal entities | Data belongs to the company you are in; lists show one company; the default company; posting in the wrong company is the most common silent error | A, E 1, 260 | Must |
| What you can see | Access comes from the D365 profile your manager requests; a missing page or button is access, not an error: contact the BAU Support team (D-083) | E, F | Must |
| System messages | Message bar, message box, Action center, message details pane; info, warning and error; what to copy for BAU Support | A, C, D | Must |
| Filter operators and query syntax | Full table: operators, `*`, `?`, `..`, `!`, `,`, `""`, `T`, relative dates; the matches rule | B | Must |
| Views and personalization | Saved view vs personalization; what saves itself; locked and published views; when the default view is skipped | B, 260 | Must |
| Financial dimensions and the account field | Main account plus dimension segments; where default dimensions come from (journal name, header, account, offset) | E 1 | Must |
| Journals and vouchers | Header and lines, journal name, Validate, Post, one voucher per transaction, debits equal credits | E 1 | Must |
| Periods and dates | Period status (Open, On hold, Permanently closed, per module); posting, document and session date; why a date is refused | E 1 | Must |
| Corrections | Posted entries are reversed, not edited | E 1 | Must |
| Why won't it post? | Closing reference table of the common posting failures and their fixes | E 1.19 | Should |
| Currencies, GST, parties, number sequences, intercompany | One short concept each, at the depth a new user needs | E 1 | Should |
| Workflow statuses and notifications | What the message bar means, which emails arrive, that workflow items are not in the Action center | D | Should |
| Using Copilot | What it answers, check every output, data privacy, when it is missing | D | Should, if enabled |
| Keyboard shortcuts | One-page card; Alt+Shift+K shows the rest | A, B | Should |

### Part 2: How do I do it?

| # | Topic | Subtopics | Source | 260 | Priority |
|---|---|---|---|---|---|
| 1 | Set Up Your D365 Session | 1.1 Sign In and Sign Out (session timeout, browser); 1.2 Set Your User Options (default company, initial page, language, date and number format, time zone); 1.3 Change the Session Date | A, D, F | — | Must |
| 2 | Open a Page | 2.1 Open a Page from the Navigation Pane; 2.2 Search for a Page; 2.3 Add/Remove Pages to Favorites; 2.4 Work from a Workspace | A, B, F | Topic 3 (Favorites) | Must |
| 3 | Switch Legal Entity | 3.1 Switch Legal Entity with the Selector; 3.2 Switch Legal Entity Using the Ledger Code | A, E | Topics 1, 2 | Must |
| 4 | Work with Records | 4.1 Edit, Save and Revert a Record; 4.2 Create and Delete a Record; 4.3 Enter Values with Lookups and Date Pickers; 4.4 Run an Action with Action Search | A, B | — | Must |
| 5 | Find Records with Filters | 5.1 Filter with the QuickFilter; 5.2 Filter and Sort a Column; 5.3 Filter with the Filter Pane; 5.4 Use Advanced Filter or Sort | B | Extends 4.2 | Must |
| 6 | Create a Personalized View | 6.1 Arrange the Columns (insert, hide, move, freeze, autofit, sort); 6.2 Add a Footer Total; 6.3 Group Rows; 6.4 Save and Pin the View | B | Topic 4 | Must |
| 7 | Manage Saved Views and Personalizations | 7.1 Update a Saved View; 7.2 Manage My Views; 7.3 Personalize a Page; 7.4 Clear a Personalization | B | Topic 5 | Should |
| 8 | Enter an Account and Financial Dimensions | One procedure on a journal line: segments, lookup, Show all / Show valid, type-ahead, validation | E | — | Must |
| 9 | Find a Posted Transaction | 9.1 Open Voucher Transactions; 9.2 View the Transaction Origin; 9.3 View Customer or Vendor Transactions | E | — | Must |
| 10 | Export Data and Work in Excel | 10.1 Export All Rows from a Grid; 10.2 Open a Page in Excel and Publish Changes | C | Topic 6 | Must (10.1), Should (10.2) |
| 11 | Run a Report | 11.1 Set the Report Parameters and Destination; 11.2 View, Download and Print a Report; 11.3 Run a Report in the Background; 11.4 Find Background Output (My batch jobs, Print archive, Action center) | C | — | Must |
| 12 | Attach a Document | Attach a file, note or link; find and preview attachments | C | — | Must |
| 13 | Submit and Approve Workflow Items | 13.1 Submit, Track and Recall a Document; 13.2 Approve, Reject or Delegate a Work Item; 13.3 Delegate Your Work Items While Away | D | — | Must |
| 14 | Set Up an Alert | Create and manage alert rules; batch job alerts for your own runs | C | — | Should |
| 15 | Get Help and Report a Problem | 15.1 Use the Help Pane; 15.2 Ask Copilot (if enabled); 15.3 Raise a Problem with the BAU Support Team (what to capture); 15.4 Reset Your Usage Data | D | — | Must |

Left out as admin or consultant content: data management, workflow design, security configuration, batch administration, Feature management, number sequence setup, dimension and account structure setup, legal entity setup, publishing views, task recorder authoring, LCS. Nice-to-have items not in the outline (side-by-side windows, accessibility, record templates, Power BI, ER outputs, Word export, agents overview, Task guides) can join if the PG owner wants them.

### Part 3: Reports

The inquiries and reports a new user meets in every stream, with how to open each: **Voucher transactions**, **Trial balance**, **Customer transactions** and **Vendor transactions**, **Financial reports** (open, generate, drill down, export; the 90-day expiry), and Power BI analytical workspaces if the tenant has them (C, E).

### Size

15 topics and about 45 subtopics, against 6 topics in 260. Two ways to keep it usable, for the PG owner to choose (decision D3):

- **One guide in two halves:** topics 1 to 7 and 10 to 15 (system skills), then 8 and 9 with the finance concepts.
- **Two guides:** *D365 F&O Getting Started* (system skills) and *D365 Finance Basics* (dimensions, journals, vouchers, periods, finding transactions).

## 4. Overlap with 260 O2C Getting Started

260 has six topics (legal entity twice, Favorites, personalized view with four subtopics, update a saved view, export all rows). All six map to topics 2.3, 3, 6, 7.1 and 10.1 above. The research also found points in 260 to check in the clean-session test (B, section on 260):

| 260 place | What Microsoft documents |
|---|---|
| 4.3 Add a Footer Total | The labels are **Show total** / **Select calculated value** and **View column totals** (Total, Minimum, Maximum, Average), not "+" and "Calculate column" |
| 4.3 and 4.4 | Footer totals save themselves; they are not part of the saved view |
| 4.4 Save and Pin the View | The default view is probably **Standard**, not "My View"; steps 5 and 6 contradict each other on the legal-entity default (G260-07, already open) |
| 4.2 Filter the List | Some operator labels differ, and the meaning of `?` needs checking |
| 4.4 (note) | A page opened from a tile or a filtered menu item does not apply the default view |

These are not applied to 260: 260 is with the SME for final approval. They can go into the 260 register as non-blocking items if you want.

## 5. To confirm in our environment

**Clean-session test (screen labels and navigation; not SME questions):**

- Our D365 version, and whether **Immersive Home** is on (it changes the landing page).
- The **Default view/edit mode** values in User options; save behaviour when navigating away.
- Shortcuts: action search (Ctrl+/ or Ctrl+'), help pane (Ctrl+Shift+? or Ctrl+?), page search.
- The alert button label; the footer total labels; the default view name; which side the Filter pane opens.
- The **?** menu items, the work items pages, where **Post and transfer** sits, and the workspace names ("General journal processing", "Ledger budgets and forecasts").
- The report dialog, print destinations, print archive, **My batch jobs** and message details pane, end to end (no current Microsoft article).

**For IT or the PG owner (configuration facts):**

- Is Copilot on, and which summaries? Are finance agents licensed?
- The Export to Excel row limit; whether bulk edit, extended totals (Min/Max/Average) and paste from Excel are enabled.
- Does the organization publish standard views to users?
- The email provider, and whether statements and documents are sent from D365.
- Power BI analytical workspaces; financial tags; intercompany journals in use.
- What BAU Support needs in a ticket (Activity ID, page, company, steps).

## 6. Decisions for the PG owner

Made on 26 November 2026 and recorded in the [project notes](Project-Context-and-Decisions.md#2-decisions-log):

| # | Decision | Outcome |
|---|---|---|
| D1 | Code | The 100 series, for high-level and general guides, once 460 to 462 are approved and the legacy 100 documents retired. No code until then (D-102). |
| D2 | 260 O2C Getting Started | Stays as it is; revisited after the new guides are approved (D-103). |
| D3 | Size | Two guides: *D365 F&O Getting Started* and *D365 Finance Basics* (D-101). |
| D4 | AI features | Out of both guides; research parked; possibly a third guide (D-104). |
| D5 | Audience | Getting Started for all D365 users; Finance Basics for finance users (D-101). |
| D6 | Board cards | Three cards created; the user creates the ADO tickets (D-105). |

## 7. Next steps

1. The user creates the ADO tickets, and Claude adds them to the cards.
2. Claude drafts v0.1 of each guide in the master template from this map, with an ACTION: REVIEW REQUIREMENT note and register item for every point in section 5 that the clean-session test or IT must confirm.
3. The clean-session test confirms the labels and gives the guide's own screenshots.
