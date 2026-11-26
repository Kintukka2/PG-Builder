# F. Microsoft Learn modules: inventory for a "D365 F&O Getting Started" guide

Research note for the discovery phase of an end-user **D365 F&O Getting Started** procedure guide (finance staff in O2C, P2P, R2R and Tax at one multi-entity company, mostly new to D365). Source: 33 Microsoft Learn training modules harvested to `learn-modules/<module-slug>/` in the scratchpad. All harvested content was treated as data.

Compiled 26 November 2026.

## How to read this note

- **Module codes.** Each module has a short code (NAV, PER, CLJ and so on) defined in the catalogue in section 1. In the text, `NAV-5` means unit file `05-*.md` of that module. The unit links go to the live unit on Microsoft Learn.
- **Screenshot paths** are relative to the scratchpad, for example `learn-modules/navigate-finance-operations/media/05-search-le.png`. The `NN-` prefix is the unit number.
- **UI labels** are in **bold**, as Microsoft writes them.
- **Evidence.** Every statement comes from the Learn text. Image descriptions come from opening the image (PNGs) or from the text labels embedded in the image (SVGs, which are vector captures of the real UI). Where neither was done, the alt text is quoted and marked *(alt text)*.

## Harvest problems fixed during this review (please read)

1. **233 of the 352 harvested units were "404 - Page not found" pages.** The harvester built unit URLs from the catalog unit UIDs, but many modules publish their units under different slugs (for example `describe-shared-features/describe-security-capabilities` returns 404, while the real unit is `describe-shared-features/2-describe-security-capabilities`). Whole modules were empty, for example all of describe-shared-features, describe-report-integration, personalize-finance-operations (15 of 16 units), workflows, the address book module, and the second-batch modules explore-general-ledger and accounts-receivable-daily-procedures.
   - **Fix:** a re-fetch script (`tools-f/refetch.py` in the scratchpad) read each module's landing page, took the real unit links in order, re-downloaded every 404 unit and its images, and overwrote the 404 file under the same file name. The first line of each re-fetched file now holds the real URL, and the second line is `<!-- refetched: original harvest URL returned 404 -->`. All 233 were recovered. Unit titles were checked against INDEX.md and all match. **No 404 pages remain.**
   - The image counts in each `INDEX.md` are now out of date: they show the counts from the failed harvest.
2. **Knowledge-check questions were missing.** The quiz questions are in the page HTML, but the harvester's Markdown conversion dropped them. They were extracted separately to `tools-f/quizzes.md` in the scratchpad and are summarised in section 2.U.
3. **Second batch.** The six second-batch modules (general-ledger-daily-procedures, set-up-financial-dimensions, configure-ledgers-journals, accounts-receivable-daily-procedures, explore-general-ledger, intercompany-accounting) had finished harvesting (see `harvest2.log`). They are all included. Five of them had 404 units, and those were re-fetched as described in point 1.
4. **Dates.** The catalog `last_modified` is 2026-10-27 for every module, so it says nothing about how current a module is. Each module page's `ms.date` was read instead and is shown in the catalogue. The date 2026-03-04 appears on 12 modules at once and looks like a bulk refresh: those modules still contain older text and screenshots.

---

## 1. Module catalogue

Audience: **EU** end user, **PU** power user, **AD** admin, **FC** functional consultant, **DEV** developer. Relevance means relevance to an end-user Getting Started guide.

| Code | Module (slug) and URL | ms.date | Audience | Relevance | Why |
|---|---|---|---|---|---|
| NAV | [Navigate finance and operations apps](https://learn.microsoft.com/en-us/training/modules/navigate-finance-operations/) `navigate-finance-operations` | 2026-03-04 | EU | **High** | The core navigation module: dashboard, tiles, navigation pane, workspaces, search, action search, filters, views, View and Edit modes. |
| DFO | [Describe Dynamics 365 finance and operations apps](https://learn.microsoft.com/en-us/training/modules/describe-finance-operations-apps/) `describe-finance-operations-apps` | 2026-05-28 | EU, FC | **High** | Current UI tour: navigation bar, company picker, Action center, User options tabs, four filter types, Action Pane, workspaces, Copilot sidecar, Immersive Home. |
| PER | [Personalize finance and operations apps](https://learn.microsoft.com/en-us/training/modules/personalize-finance-operations/) `personalize-finance-operations` | 2026-03-04 | EU, FC | **High** | User options, implicit and explicit personalization, grid tricks (freeze, totals, maths, paste from Excel), saved views, Personalization toolbar, Add to workspace, record templates, attachments. |
| ICP | [Get started with configuration and personalization](https://learn.microsoft.com/en-us/training/modules/introduce-configure-personalization-dynamics-365-finance-operations-apps/) `introduce-configure-personalization-...` | 2026-09-30 | EU, PU | **High** | Sign-in, navigation pane, switching legal entity, default company, the full User options field list, form personalization, a Favorites exercise. |
| CUI | [Configure your user interface](https://learn.microsoft.com/en-us/training/modules/configure-your-ui-dynamics-365-finance-operations-apps/) `configure-your-ui-...` | 2026-09-30 | EU, PU | **High** | Favorites steps, Initial page, workspace tiles and lists, inserting and hiding columns, filter operators, Advanced filter or sort, saving a view. Some admin steps. |
| HELP | [Get help and learn more](https://learn.microsoft.com/en-us/training/modules/get-help-finance-operations/) `get-help-finance-operations` | 2026-03-04 | EU | **High** | Help pane (Ctrl+Shift+?), field descriptions, task guides, and the warning that task guide data is real. |
| DSF | [Describe shared features](https://learn.microsoft.com/en-us/training/modules/describe-shared-features/) `describe-shared-features` | 2026-05-29 | EU, FC | **High** | Current concepts: security model, workflow (with Workflow history and Summary by Copilot), batch jobs, legal entities, record templates, address book, alerts, number sequences, attachments. |
| WAR | [Work with analytics and reporting](https://learn.microsoft.com/en-us/training/modules/work-analytics-reporting-finance-operations/) `work-analytics-reporting-finance-operations` | 2026-03-04 | EU, FC | **High** (parts) | Report types, Inquiries and reports menus, Export to Excel and Open in Excel, Financial reports (generate, view, drill down, filter, currency), report export and print. Power BI content list is outdated. |
| DRI | [Describe reporting and integration capabilities](https://learn.microsoft.com/en-us/training/modules/describe-report-integration/) `describe-report-integration` | 2026-05-28 | EU, FC | **Medium-High** | Inquiry pages and export to Excel, Open in Excel, Export to Word, how to send email (dialog options), Power BI in workspaces, Finance insights. Some developer content (SSRS, Dataverse). |
| CLJ | [Set up ledgers and journals](https://learn.microsoft.com/en-us/training/modules/configure-ledgers-journals-dyn365-finance/) `configure-ledgers-journals-dyn365-finance` | 2026-09-27 | FC | **Medium-High** | Setup-oriented, but explains what users meet daily: journal types, voucher numbering, manual and workflow journal approval, the inquiries (Voucher transactions, Audit trail), ledger reports, Open lines in Excel, reversals, the subledger transfer delay. |
| GLD | [Perform general ledger daily procedures](https://learn.microsoft.com/en-us/training/modules/general-ledger-daily-procedures-dyn365-finance/) `general-ledger-daily-procedures-dyn365-finance` | 2026-09-26 | EU, FC | **Medium-High** | Journal header and lines, the minimum data for an entry, Balance control, Simulate posting, Post and transfer, Trial balance, voucher templates, Excel templates for each journal type. |
| SFD | [Set up financial dimensions](https://learn.microsoft.com/en-us/training/modules/set-up-financial-dimensions-finance/) `set-up-financial-dimensions-finance` | 2026-09-24 | FC, EU | **Medium** | Setup module, but explains what users see: dimension values, default and derived dimensions, account structure validation, ledger account aliases, suspended values, dimension sets on the Trial balance. |
| DGL | [Describe general ledger and cash and bank management](https://learn.microsoft.com/en-us/training/modules/describe-general-ledger-cash-bank-management/) `describe-general-ledger-cash-bank-management` | 2026-01-02 | EU, FC | **Medium** | Current concept tour: fiscal and ledger calendars (period status), chart of accounts, dimensions and financial tags, account structures, journal types, Financial reporting, settlements, period close, Finance agents. |
| GSF | [Get started with Dynamics 365 Finance](https://learn.microsoft.com/en-us/training/modules/get-started-financial-management-dyn365-finance/) `get-started-financial-management-dyn365-finance` | 2026-09-27 | EU | **Medium** | What each Finance module does, how the subledgers feed the GL, and an "explore" exercise (Home tiles, close a workspace with X, Modules). |
| DFC | [Describe Dynamics 365 Finance core capabilities](https://learn.microsoft.com/en-us/training/modules/describe-dynamics-365-finance-core-capabilities/) `describe-dynamics-365-finance-core-capabilities` | 2026-01-02 | EU, FC | **Medium** | Accounting versus reporting currency, exchange rates, sales tax groups and item sales tax groups (the only codes that apply are those in both), withholding tax, the vendor payment journal and Generate payments. |
| ICA | [Intercompany accounting](https://learn.microsoft.com/en-us/training/modules/intercompany-accounting-dyn365-finance/) `intercompany-accounting-dyn365-finance` | 2026-09-25 | EU, FC | **Medium** | Multi-entity company: the **Company** field on a journal line triggers intercompany posting, Due to and Due from accounts, Related vouchers, switching company to check the other side. |
| DAPAR | [Describe accounts payable and receivable](https://learn.microsoft.com/en-us/training/modules/describe-account-payables-account-receivables/) `describe-account-payables-account-receivables` | 2025-12-05 | EU, FC | **Medium** | AP and AR workspaces, **Summary by Copilot** on vendors, customers and POs, posting profiles (most specific wins), payment proposal types, collections. Mainly O2C and P2P content. |
| ARD | [Get started with AR daily procedures](https://learn.microsoft.com/en-us/training/modules/accounts-receivable-daily-procedures-dyn365-finance/) `accounts-receivable-daily-procedures-dyn365-finance` | 2026-09-28 | EU, FC | **Low-Medium** | O2C process content (free text invoices, payments, settlement). Useful for the concept of settlement and for the time-zone behaviour of release dates. Belongs in the O2C guides. |
| EGL | [Describe the general ledger](https://learn.microsoft.com/en-us/training/modules/explore-general-ledger-dynamics-365/) `explore-general-ledger-dynamics-365` | 2025-08-04 | EU, FC | **Low** | An older near-duplicate of DGL units 2 to 6 and 10. Its SVG screenshots are crisp. |
| BAT | [Set up batch jobs](https://learn.microsoft.com/en-us/training/modules/setup-batch-jobs-finance-operations/) `setup-batch-jobs-finance-operations` | 2026-03-04 | FC, AD | **Medium** (parts) | End users need only **Run in the background**, recurrence and alerts (BAT-3), and the fact that pickup can take a minute (BAT-2). The rest is for administrators. |
| WF | [Work with workflows](https://learn.microsoft.com/en-us/training/modules/create-use-workflows-finance-operations/) `create-use-workflows-finance-operations` | 2026-03-04 | FC | **Medium** (parts) | WF-4 is end-user material: Submit, the yellow bar, and the actions of originators, assignees and approvers. The rest is workflow design. |
| FM | [Feature management](https://learn.microsoft.com/en-us/training/modules/feature-management-finance-operations/) `feature-management-finance-operations` | 2026-03-04 | AD | **Low** | Admin workspace. Useful only to explain why screens change after updates. |
| LE | [Plan and implement legal entities](https://learn.microsoft.com/en-us/training/modules/plan-implement-legal-entities-finance-operations/) `plan-implement-legal-entities-finance-operations` | 2026-03-04 | FC | **Low-Medium** | Implementation design. Useful concept lines: data is secured by company, the company ID, "you must manually change companies", date intervals for reports. |
| GAB | [Plan and configure the global address book](https://learn.microsoft.com/en-us/training/modules/plan-config-global-address-book-finance-operations/) `plan-config-global-address-book-finance-operations` | 2026-03-04 | FC | **Low** | Party concept and duplicate check. Overlaps DSF-7 almost word for word. |
| CYD | [Configure your data](https://learn.microsoft.com/en-us/training/modules/configure-your-data-dynamics-365-finance-operations-apps/) `configure-your-data-...` | 2026-09-30 | PU, AD | **Medium** (CYD-7 only) | CYD-7 is a clean end-user exercise: Open in Excel, edit, Publish, refresh. Also the current email provider note (Microsoft Graph). The rest is entities and security admin. |
| ICI | [Implement common integration features](https://learn.microsoft.com/en-us/training/modules/implement-common-integration-features-finance-ops/) `implement-common-integration-features-finance-ops` | 2026-03-04 | FC, AD | **Low-Medium** | Good detail on the Excel Data Connector pane, static export from the grid menu, the email dialog and print options. Mostly admin, with old Fleet Management examples. |
| ERT | [Explore reporting tools](https://learn.microsoft.com/en-us/training/modules/explore-reporting-tools-finance-operations/) `explore-reporting-tools-finance-operations` | 2026-09-27 | DEV | **Low** | ERT-1 has a useful "which reporting tool when" summary. The rest is SSRS development and the table permissions framework. |
| RS | [Implement role-based security](https://learn.microsoft.com/en-us/training/modules/role-security-finance-operations/) `role-security-finance-operations` | 2026-09-27 | DEV, AD | **Low** | Concept only: no role means no access, and the UI hides what you can't use. Per D-083, the guide must not name roles. |
| WDM | [Work with data management](https://learn.microsoft.com/en-us/training/modules/work-data-management-finance-operations/) `work-data-management-finance-operations` | 2026-09-28 | FC, AD | **None-Low** | Data migration and integration administration. |
| MOB | [Set up and build mobile experiences](https://learn.microsoft.com/en-us/training/modules/mobile-experiences-finance-operations/) `mobile-experiences-finance-operations` | 2026-03-04 | FC, DEV | **Low** | Mobile now means Power Apps. It links to the deprecation notice for the old D365 mobile app. |
| BW | [Build workspaces](https://learn.microsoft.com/en-us/training/modules/build-workspaces-finance-operations/) `build-workspaces-finance-operations` | 2026-09-27 | DEV | **Low** | BW-3 and BW-5 have user-level "Add a workspace" and "Add to workspace" steps (tile sizes, linking to saved views). The rest is X++. |
| UAT | [Perform user acceptance testing](https://learn.microsoft.com/en-us/training/modules/perform-uat-finance-operations/) `perform-uat-finance-operations` | 2026-09-25 | FC | **None** | Test libraries in LCS, RSAT, Azure DevOps. |
| SCM | [Get started with Supply Chain Management](https://learn.microsoft.com/en-us/training/modules/get-started-supply-chain-management-dyn365-supply-chain-mgmt/) `get-started-supply-chain-management-...` | 2026-03-04 | EU | **Low** | Supply chain overview. SCM-14 covers intercompany trade and SCM-17 has an "explore" exercise like GSF-14. |


---
## 2. Topic inventory

Links point to `https://learn.microsoft.com/en-us/training/modules/<module>/<unit>`. Screenshot paths start at the scratchpad folder.

### 2.A Signing in and the navigation shell

**Signing in.** D365 F&O runs in a browser (see the supported browsers list). You sign in with your **Microsoft Entra ID** account. A user with no security role can't open the application. Sources: [ICP-2](https://learn.microsoft.com/en-us/training/modules/introduce-configure-personalization-dynamics-365-finance-operations-apps/set-up-your-environment), [RS-1](https://learn.microsoft.com/en-us/training/modules/role-security-finance-operations/1-introduction).
- `learn-modules/introduce-configure-personalization-dynamics-365-finance-operations-apps/media/05-m1-l5-p1.png`: Microsoft sign-in screen *(alt text)*.

**Navigation bar** (the top bar). It holds the waffle for the Microsoft 365 portal (**Dynamics 365 portal** / "Go to Microsoft 365"), **Search for a page**, the **company picker**, **Copilot**, **Action center** / **Show messages** (bell), **Settings** (gear), **Help & Support** (?), and the user profile. Selecting **Finance and Operations** on the bar returns you to the dashboard. Sources: [NAV-2](https://learn.microsoft.com/en-us/training/modules/navigate-finance-operations/2-navigation-elements), [DFO-4](https://learn.microsoft.com/en-us/training/modules/describe-finance-operations-apps/4-explore-user-interface).
- `learn-modules/describe-finance-operations-apps/media/04-01-navigation-bar-04.png`: the current dark navy bar with red callouts: **Go to Office 365** (waffle), **Search for a page**, **Company picker** ("USMF | Contoso Entertainment Syste..."), **Copilot**, **Action center** (bell), **Settings** (gear), and ? for help. Below it are the Action Pane (Edit, New, Delete, Vendor, Procurement, Invoice, General, Options, magnifier) and the expanded navigation pane.

**Navigation pane** (left). Open it with **Show navigation pane** (the hamburger icon at top left). You can pin it open. It has **Home** and four collapsible sections:
- **Favorites**: pages you starred.
- **Recent**: filled in automatically.
- **Workspaces**: those your roles give you.
- **Modules**: the full list. Selecting a module opens its pages on the right of the pane.

Sources: [NAV-2](https://learn.microsoft.com/en-us/training/modules/navigate-finance-operations/2-navigation-elements), [DFO-4](https://learn.microsoft.com/en-us/training/modules/describe-finance-operations-apps/4-explore-user-interface), [ICP-2](https://learn.microsoft.com/en-us/training/modules/introduce-configure-personalization-dynamics-365-finance-operations-apps/set-up-your-environment), [PER-4](https://learn.microsoft.com/en-us/training/modules/personalize-finance-operations/4-implicit) (pin).
- `learn-modules/describe-finance-operations-apps/media/04-01-navigation-pane-03.png`: the current pane (Home, Favorites, Recent, Workspaces, Modules) with the pin icon.
- `learn-modules/navigate-finance-operations/media/02-ar-customers.svg`: the navigation pane open on a module page list (SVG capture, 2024; also shows the dashboard calendar).
- `learn-modules/introduce-configure-personalization-dynamics-365-finance-operations-apps/media/02-m1-l2-p2.png`: Favorites, Recent, Workspaces, Modules *(alt text; older style)*.
- `learn-modules/personalize-finance-operations/media/04-navigation-pin.png`: the pin button on the navigation pane *(alt text)*.
- `learn-modules/get-started-financial-management-dyn365-finance/media/14-modules-icon-ss.png`: **Modules** icon, with Accounts receivable selected *(alt text)*.

**Favorites.** Hover over a menu item and select the star to the right of its name. The page then appears under **Favorites**. You can't group or rearrange favorites (CUI-2). Steps: [CUI-2](https://learn.microsoft.com/en-us/training/modules/configure-your-ui-dynamics-365-finance-operations-apps/manage-menus-favorites); exercises [ICP-5](https://learn.microsoft.com/en-us/training/modules/introduce-configure-personalization-dynamics-365-finance-operations-apps/exercise-favorite-menu-items) (Accounts receivable > Customers > All customers) and [CUI-9](https://learn.microsoft.com/en-us/training/modules/configure-your-ui-dynamics-365-finance-operations-apps/exercise-create-favorites).
- `learn-modules/introduce-configure-personalization-dynamics-365-finance-operations-apps/media/05-m1-l5-p2.png` (Show navigation pane), `...05-m1-l5-p3.png` (Favorites empty), `...05-m1-l5-p4.png` (Customers > All customers, with the star), `...05-m1-l5-p5.png` (All customers now under Favorites).
- `learn-modules/configure-your-ui-dynamics-365-finance-operations-apps/media/09-m2-l9-p1.png`: a Favorites list with four production items.
- Note D-084: in this repository, Favorites are taught in 260 O2C Getting Started. A cross-ERP Getting Started guide would be the natural home for it too. Decide which guide owns the topic.

**Dashboard / Home page.** The first page after sign-in. It has the company banner (legal entity name and image), a calendar, **Work items assigned to me**, a **To-do list** (if turned on in User options), and workspace tiles. Microsoft calls it the "dashboard" in NAV and PER and the "**Home** page" in GSF-14 and SCM-17. You can personalize it: hide, rename and reorder tiles, and add a workspace ([PER-10](https://learn.microsoft.com/en-us/training/modules/personalize-finance-operations/9-dashboard)). The company image comes from the **Dashboard Image** FastTab on the legal entity ([LE-11](https://learn.microsoft.com/en-us/training/modules/plan-implement-legal-entities-finance-operations/13-exercise-1)).
- `learn-modules/navigate-finance-operations/media/02-main-dashboard-1.svg`: current dashboard (2024 capture). Labels: Finance and Operations, Search for a page, USMF, Contoso Entertainment System USA, August 2024 calendar, **Work items assigned to me** ("You're all caught up on your tasks."), **To-do list**, and tiles including Business performance analytics (preview).
- `learn-modules/introduce-configure-personalization-dynamics-365-finance-operations-apps/media/02-m1-l2-p1.png`: an **older** dashboard (March 2020) with banner, calendar and tiles (Bank management, Master planning, Benefits...). Outdated look.
- `learn-modules/navigate-finance-operations/media/02-tile.png`: the Bank management and Benefits tiles.
- `learn-modules/build-workspaces-finance-operations/media/01-dashboard.svg`: dashboard (SVG). Includes the screen-reader message "New messages are in the Action Center" (Ctrl-Shift-F7).

**Immersive Home** (preview). An AI-first landing page:
- A greeting ("Welcome, Admin. You have 7 work items assigned to you.") and **Work items** cards with **Approve**, **Reject** and **Return** buttons.
- A Suggestions area and an **Agent activity** area.
- A ranked **Workspaces** list, with favorites and recent workspaces first.
- It requires version 10.0.44 or later, the **Immersive Home** feature, and the **View immersive home** privilege. Choose it as the **Initial page** in User options.

Sources: [DFO-3](https://learn.microsoft.com/en-us/training/modules/describe-finance-operations-apps/3-describe-use-cases-ai-tools), [CUI-3](https://learn.microsoft.com/en-us/training/modules/configure-your-ui-dynamics-365-finance-operations-apps/manage-menus-dashboards-role).
- `learn-modules/describe-finance-operations-apps/media/03-01-immersive-home-02.png`: Immersive Home with work item cards on the left and a Workspaces list on the right (Feature management, Collections coordinator, Customer credit and collections, Account reconciliation with Open exceptions 0, Bank management...). Footer: "AI generated content may be incorrect."

**Back arrow.** Use the back arrow at the far left of the Action Pane to return to the previous page ([NAV-2](https://learn.microsoft.com/en-us/training/modules/navigate-finance-operations/2-navigation-elements)). Close a workspace with the **X** at top right ([GSF-14](https://learn.microsoft.com/en-us/training/modules/get-started-financial-management-dyn365-finance/12-1-exercise), [SCM-17](https://learn.microsoft.com/en-us/training/modules/get-started-supply-chain-management-dyn365-supply-chain-mgmt/14-1-exercise)).

**Accessibility.** F&O supports WCAG 2.1 from version 10.0.21 ([NAV-9](https://learn.microsoft.com/en-us/training/modules/navigate-finance-operations/8-summary)).

### 2.B Workspaces

**Definition.** Workspaces are activity-oriented pages, a "one-stop shop" for an activity. Which workspaces you see depends on your roles. Open one from a dashboard tile, from **Workspaces** in the navigation pane, or with search. Layout:
1. Tiles (with counts) to start tasks or open lists.
2. Tabbed lists.
3. Optional charts, or embedded Power BI on an **Analytics** tab.
4. **Links** at the right, to related pages and reports.

Workspaces let you act directly on the data. Microsoft lists five benefits: a 360-degree view, answers to specific questions, insight, navigating by data, and direct access to tasks. Sources: [NAV-2](https://learn.microsoft.com/en-us/training/modules/navigate-finance-operations/2-navigation-elements), [NAV-3](https://learn.microsoft.com/en-us/training/modules/navigate-finance-operations/3-workspaces-driving-productivity), [DFO-4](https://learn.microsoft.com/en-us/training/modules/describe-finance-operations-apps/4-explore-user-interface), [CUI-4](https://learn.microsoft.com/en-us/training/modules/configure-your-ui-dynamics-365-finance-operations-apps/manage-menus-key-performance-indicators).

**Walkthrough in NAV-3: Customer invoicing workspace.** **Summary** tiles with counts (for example, **Shipped but not invoiced sales orders** = 3, which opens the list), the **Filter** box, tabs of orders and invoices, **Links** (invoices and reports), and **New free text invoice** on the Action Pane.

**Workspaces named in finance modules:**
- General ledger: **General journal processing**, **Financial period close**, **CFO overview**, **Financial insights** (CLJ-1).
- Cash and bank: **Bank management**, **Cash overview**.
- AR: **Customer invoicing**, **Customer payments**, **Credit and collections** (or **Customer credit and collections**), **Collections coordinator**.
- AP: **Vendor invoice entry**, **Vendor invoice automation**, **Vendor payments**.
- Procurement: **Purchase order preparation**, **Purchase order receipt and follow-up**.
- Others: **Cost control**, **Ledger budgets and forecasts**, **Fixed asset management**, **Account Reconciliation**, **Feature management**, **Data management**, **Business Document Management**.

Several have embedded Power BI ([DAPAR-3](https://learn.microsoft.com/en-us/training/modules/describe-account-payables-account-receivables/3-describe-core-accounts-payable-components), [DAPAR-5](https://learn.microsoft.com/en-us/training/modules/describe-account-payables-account-receivables/5-describe-vendor-payments-settlements), [DAPAR-6](https://learn.microsoft.com/en-us/training/modules/describe-account-payables-account-receivables/6-describe-core-accounts-receivable-components), [DAPAR-9](https://learn.microsoft.com/en-us/training/modules/describe-account-payables-account-receivables/9-describe-collection-process)).

Screenshots:
- `learn-modules/navigate-finance-operations/media/02-customer-payments-workspace.svg`: **Customer payments** workspace. Tiles: Record customer payment, Customer invoices past due, Payment Journals - not posted (4), assigned to me, Electronic payments sent, need bank confirmation, All customers, Customers on hold, Customer invoices due today, Deposit slips, Summarized payments.
- `learn-modules/navigate-finance-operations/media/03-workspace-2.svg`: **Customer invoicing** workspace. Tiles: Shipped but not invoiced sales orders (3), Sales orders on hold (1), Free text invoices assigned to me, Unposted free text invoices (4), Unposted recurring invoice groups; lists and links.
- `learn-modules/describe-finance-operations-apps/media/04-01-credit-and-collections-workspace-17.png`: credit and collections workspace *(alt text)*.
- `learn-modules/get-started-financial-management-dyn365-finance/media/09-credits-and-collections.svg`: **Customer credit and collections**. Tiles: Open activities 14, Open cases 8, Customers over credit limit 2, Payment journals not posted 13, Collection letters not printed 8.
- `learn-modules/general-ledger-daily-procedures-dyn365-finance/media/03-general-journal-processing.svg`: **General journal processing**. **New journal** tile and counters (My not posted 6, All not posted 38, My posted today, All posted today...).
- `learn-modules/get-started-financial-management-dyn365-finance/media/05-bank-management.svg`: **Bank management** (Import bank statements, Open bank reconciliations 1, balances by bank account).
- `learn-modules/describe-account-payables-account-receivables/media/05-6-5-vendor-payments.png`, `.../06-6-6-customer-workspace.png`, `.../09-6-9-workspace.png`: Vendor payments, Customer invoicing and Credit and collections workspaces (2025 module) *(alt text)*.
- `learn-modules/implement-common-integration-features-finance-ops/media/07-power-bi-connector.svg`: **Vendor payments** workspace tiles (New vendor pay run, Vendor pay run - not posted 14...).
- `learn-modules/describe-report-integration/media/02-2-2-analytics-workspace.png`: Fixed asset management workspace, **Analytics - all companies** tab with embedded Power BI *(alt text)*.
- `learn-modules/configure-your-ui-dynamics-365-finance-operations-apps/media/04-m2-l4-p1.png` / `p2` / `p3`: Sales order processing and inquiry workspace: tiles, **Orders and favorites** lists, **Links** *(alt text)*.
- `learn-modules/get-started-financial-management-dyn365-finance/media/14-workspaces-ss.png`: Home page with the **Customer payments** tile highlighted *(alt text)*.

**Adding your own content to a workspace.** On a list page, go to **Options** > **Personalize** group > **Add to workspace**. Choose the **Workspace** and a **Presentation** (**List**, **Tile** or **Link**), then **Configure**:
- **Tile**: label and whether to show a count. BW-5 adds "one of four tile sizes".
- **List**: columns, label and list style.
- **Link**: label and an optional new section.

Filter or sort the list first, because the element shows the filtered list. When **Saved views** is on, the element links to a view, so updating the view updates the workspace element. Create your own workspace from the dashboard: right-click a tile > **Personalize** > **Options** > **Add a workspace**. BW-3 notes that with **Full-page apps** on, you use **Add an app** instead. To pin a count tile to the dashboard: right-click it > **Personalize** > **Pin to dashboard**. Sources: [PER-9](https://learn.microsoft.com/en-us/training/modules/personalize-finance-operations/8-workspace), [PER-10](https://learn.microsoft.com/en-us/training/modules/personalize-finance-operations/9-dashboard), [BW-3](https://learn.microsoft.com/en-us/training/modules/build-workspaces-finance-operations/2-drill-through), [BW-5](https://learn.microsoft.com/en-us/training/modules/build-workspaces-finance-operations/4-built-in-kpi).
- `learn-modules/personalize-finance-operations/media/09-add-2-ws.svg`: All customers > **Options** tab open: **Personalize** group (Always open for editing, Personalize this page, **Add to workspace**), **Page options** (Security diagnostics, Advanced filter or sort, Record info, Go to), with the Workspace / Presentation drop-downs.
- `learn-modules/personalize-finance-operations/media/09-tile-1.png`: a count shown below a workspace navigation tile *(alt text)*.
- `learn-modules/build-workspaces-finance-operations/media/05-customize.svg`: the Add to workspace form from All customers.
- `learn-modules/personalize-finance-operations/media/10-toolbar.svg`: the Bank management workspace with the Personalization toolbar (Select, Hide, Require, Add a field, Move, Skip, Show in header, Lock).

### 2.C Pages, forms and records

**Anatomy.** NAV-2 has a glossary:
- **Action Pane**: tabs of buttons (Edit, New, Delete, plus page-specific tabs such as Customer, Collect, Invoice, General, **Options**).
- **Tab** (on the Action Pane).
- **FastTab**: expandable section of a record; the state is remembered and collapsing can improve performance.
- **FactBox pane** and **FactBox**: read-only related information on the right.
- **Filter pane**.
- **Navigation list**: list of records on the left of a details page.
- **Page**.
- **Pane**: right-hand panel, for example Task recorder.
- **Navigation bar** and **Navigation pane**.

The Action Pane can be pinned open, and it remembers the last tab you used. Sources: [NAV-2](https://learn.microsoft.com/en-us/training/modules/navigate-finance-operations/2-navigation-elements), [PER-4](https://learn.microsoft.com/en-us/training/modules/personalize-finance-operations/4-implicit), [DFO-4](https://learn.microsoft.com/en-us/training/modules/describe-finance-operations-apps/4-explore-user-interface).
- `learn-modules/personalize-finance-operations/media/04-user-interface-01.png`: **The best annotated screenshot of the whole set.** A customer page (US_SI_0002 Active Transport Inc.) with coloured overlays labelling navigation bar, Action Pane, tab on the Action Pane, company picker (USSI), navigation pane, filter pane, navigation list, page, FactBox, FactBox pane, and pane (Task recorder).
- `learn-modules/describe-finance-operations-apps/media/04-01-action-pane-11.png`: the Customer Action Pane with the **Collect** tab open (Payment journal, Collection letters, Interest, Customer balances groups).

**Views of a page** (NAV-6):
- **Grid view**: update many records at once.
- **Details view**: one record from a list.
- **Header view**: header data and defaults; can bulk update lines.
- **Lines view**: the lines of a header/line document such as a PO or SO.

Lists usually use Grid and Details. Documents use Header and Lines. DAPAR-3 repeats this for purchase orders. Sources: [NAV-6](https://learn.microsoft.com/en-us/training/modules/navigate-finance-operations/6-comparing-views), [DAPAR-3](https://learn.microsoft.com/en-us/training/modules/describe-account-payables-account-receivables/3-describe-core-accounts-payable-components).

**View and Edit mode.** View mode reviews data and follows links. Edit mode changes data. The separation prevents accidental updates. User options **Default view/edit mode** can be **Auto**, **View** or **Edit**, and a per-page setting overrides it. The quiz expects that list pages open in **View mode**. The exercise in ICI-10 uses **Edit** (F2) and **Refresh** (Shift+F5). Sources: [NAV-7](https://learn.microsoft.com/en-us/training/modules/navigate-finance-operations/7-view-and-edit-mode), [PER-3](https://learn.microsoft.com/en-us/training/modules/personalize-finance-operations/3-user-options), [ICI-10](https://learn.microsoft.com/en-us/training/modules/implement-common-integration-features-finance-ops/10-exercise-1).

**Creating records: record templates.**
1. On an existing record, select **Options** > **Page options** > **Record info**.
2. Select **Company accounts template** (all users in the legal entity) or **User template** (only you). A **System template** type also exists.
3. Enter a name and description.

When you create a new record and templates exist, the **Select a template for** dialog appears. **Do not ask again** turns it off; right-click > **Record info** > **Show template selection** turns it back on. Don't put sensitive words such as "commission" in template names. Sources: [DSF-6](https://learn.microsoft.com/en-us/training/modules/describe-shared-features/6-create-maintain-record-templates), [PER-12](https://learn.microsoft.com/en-us/training/modules/personalize-finance-operations/12-record-templates), exercise [PER-14](https://learn.microsoft.com/en-us/training/modules/personalize-finance-operations/14-exercise-2) (Fixed assets).
- `learn-modules/describe-shared-features/media/06-03-save-record-template-14.png`: the **Record information** dialog (Customer account DE-001; Rename, Show all fields, Database Log, Script; the **Company accounts template** and **User template** buttons highlighted).
- `learn-modules/describe-shared-features/media/06-03-use-record-template-15.png`: the template selection dialog *(alt text)*.

**Default values on new records.** Base data on a vendor or customer defaults onto transactions and can be overridden ([DAPAR-3](https://learn.microsoft.com/en-us/training/modules/describe-account-payables-account-receivables/3-describe-core-accounts-payable-components), [DAPAR-6](https://learn.microsoft.com/en-us/training/modules/describe-account-payables-account-receivables/6-describe-core-accounts-receivable-components)).

**Attachments (document handling).**
1. Select the record.
2. Select the paperclip **Attach** button (Ctrl+Shift+A). The button shows a count from 0 to 9, then "9+".
3. On the **Attachments** page, select **New** > a document type (**File**, **Image**, **Note**, **URL**, or your company's own types).
4. Browse to the file. You can preview it, and add notes.

**Restriction** sets **Internal** or **External**; internal notes don't print on documents. Document handling must be turned on in User options (**Enable document handling**). Use cases include supporting documents for a ledger journal entry. Sources: [DSF-10](https://learn.microsoft.com/en-us/training/modules/describe-shared-features/10-describe-attachment-capabilities), [PER-3](https://learn.microsoft.com/en-us/training/modules/personalize-finance-operations/3-user-options), [ICI-4](https://learn.microsoft.com/en-us/training/modules/implement-common-integration-features-finance-ops/4-documents).
- `learn-modules/describe-shared-features/media/10-03-new-document-25.png`: **Attachments for Vendors - Vendor account: 1001, Acme Office Supplies**, with **New** expanded (File, Image, Note, URL) and the buttons Save, Delete, Open, View history, Created by, Settings, References, Options.
- `learn-modules/describe-shared-features/media/10-03-upload-document-26.png` (file upload dialog *(alt text)*), `.../10-03-view-attachments-27.png` (preview of an attached image *(alt text)*).
- `learn-modules/personalize-finance-operations/media/03-attachment-ss.svg`: All customers with the paperclip icon (count 0) in the top-right icons.

**Number sequences** (why IDs fill in automatically). Customer IDs, invoice numbers and voucher numbers come from number sequences. **Manual** sequences let you type the number. **Continuous** sequences never skip a number (legal documents) but are slower. Voucher series are set on the **Journal names** page. Sources: [DSF-9](https://learn.microsoft.com/en-us/training/modules/describe-shared-features/9-describe-number-sequences), [LE-3](https://learn.microsoft.com/en-us/training/modules/plan-implement-legal-entities-finance-operations/3-create-number-sequence), [CLJ-6](https://learn.microsoft.com/en-us/training/modules/configure-ledgers-journals-dyn365-finance/implement-voucher).
- `learn-modules/describe-shared-features/media/09-03-number-sequence-tab-23.png`: AP parameters > Number sequences tab *(alt text)*. `.../09-03-number-sequence-22.png`: number sequence format *(alt text)*.

**Messages.** After posting, an **Infolog** or message bar confirms the result, for example "two vouchers were posted" (ICA-3) or "Operation completed" (ICA-7). System messages collect in the **Action center** (DFO-4: **Show messages**).

### 2.D Search

**Navigation search** ("Search for a page"):
- It finds pages and workspaces, **not data or actions**.
- It matches on the page title and on the navigation path, so a broad word such as "receivable" returns many hits.
- Results show the page title and the navigation path. Only 10 results are shown, so refine the words if the page isn't listed.
- It shows only pages enabled by configuration keys and allowed by your roles.
- An exact title match, such as "payment journal", comes to the top.
- Technical users can type "form:" and a form name, for example "form: vendinvoice".

Sources: [NAV-5](https://learn.microsoft.com/en-us/training/modules/navigate-finance-operations/5-searching), [DFO-4](https://learn.microsoft.com/en-us/training/modules/describe-finance-operations-apps/4-explore-user-interface). The quiz tests that results show the path and the title.
- `learn-modules/navigate-finance-operations/media/05-search-le.png`: search for "project". Ten results, each with title and path (for example "Project actual transactions: Project management and accounting > Inquiries and reports > Actual transactions reports"). Older blue banner.
- `learn-modules/navigate-finance-operations/media/05-search-vi.png`: results for "form: vendinvoice" *(alt text)*.
- `learn-modules/describe-finance-operations-apps/media/04-01-search-bar-results-06.png`: search results for "Customer" *(alt text)*.

**Action search.** The magnifier on the Action Pane (**Action search**), or **Ctrl+'** or **Alt+Q**. Type 2 to 4 characters of a button name (or words from its path), then run it from the results. Focus returns to where you were. Source: [NAV-5](https://learn.microsoft.com/en-us/training/modules/navigate-finance-operations/5-searching).

### 2.E Filtering and sorting

Four filtering mechanisms are taught (DFO-4, NAV-4, CUI-6):
1. **QuickFilter** (the **Filter** box above a grid): filters one column. As you type, a column selector appears. The default column is the first filterable one. The column you choose is remembered (PER-4).
2. **Filter pane**: open it with **Show filters** (the funnel icon) and close it with **Hide filters**. Add several criteria (**+ Add** / **Add filter fields**), set operators (begins with, contains, is exactly...), then **Apply** or **Reset**. It stays open until you leave the page. **Sources disagree on the side**: see section 4.
3. **Grid column header filter**: select the column header for **Sort A to Z**, **Sort Z to A** and a filter box with an operator, then **Apply** or **Clear**. Changed operators are remembered (PER-4). Basic sorting is one level only.
4. **Advanced filter or sort**: **Options** > **Page options** > **Advanced filter or sort**. Tabs:
   - **Range**: criteria on several fields, for example Customer group = 10.
   - **Sorting**: multi-level; a warning appears when sorting on a field that isn't indexed.
   - **Joins**: **Add table join** to filter on a related table.

Operators by data type (CUI-6):
- Text: **is exactly**, **is not**, **contains**, **does not contain**, **begins with**, **is one of**, **matches**.
- Numbers and dates also have **after** (greater than), **before** (less than), greater than or equal, less than or equal, and **between**.
- **matches** accepts query symbols directly: `*` is a wildcard ([NAV-4](https://learn.microsoft.com/en-us/training/modules/navigate-finance-operations/4-filtering-techniques)) and `..` is a range ([CLJ-8](https://learn.microsoft.com/en-us/training/modules/configure-ledgers-journals-dyn365-finance/4-journals): "values should be separated by a double period"). SFD-9 adds that a range must have two values of the same length (`100000..399999`) and that a wildcard doesn't go inside a range.

To keep a filter, save it in a view (2.G). The quiz expects **Advanced sort** for sorting on several fields. Sources: [NAV-4](https://learn.microsoft.com/en-us/training/modules/navigate-finance-operations/4-filtering-techniques), [DFO-4](https://learn.microsoft.com/en-us/training/modules/describe-finance-operations-apps/4-explore-user-interface), [CUI-6](https://learn.microsoft.com/en-us/training/modules/configure-your-ui-dynamics-365-finance-operations-apps/manage-forms-filters-ranges), exercise [CUI-11](https://learn.microsoft.com/en-us/training/modules/configure-your-ui-dynamics-365-finance-operations-apps/exercise-change-form-fields-queries) (Product name "contains" tablet, then Save as a view).

Screenshots:
- `learn-modules/navigate-finance-operations/media/04-filtering.svg`: All sales orders with the Filter pane (area 1) and a column header filter (area 2). 2024 capture.
- `learn-modules/describe-finance-operations-apps/media/04-01-filter-pane-12.png`: **Filters** pane (Customer account begins with, Customer group begins with, + Add, Apply, Reset) with the funnel icon highlighted at the right edge of the screen.
- `learn-modules/describe-finance-operations-apps/media/04-01-quick-filter-12.png`: QuickFilter above a grid *(alt text)*.
- `learn-modules/describe-finance-operations-apps/media/04-01-grid-sort-13.png`: **Customer group** column header drop-down: **Sort A to Z**, **Sort Z to A**, "begins with" filter, **Apply**, **Clear**.
- `learn-modules/describe-finance-operations-apps/media/04-01-query-filter-14.png`, `...04-01-query-sort-15.png`, `...04-01-query-add-join-16.png`: Advanced filter or sort, on the **Range**, **Sorting** and **Joins** tabs *(alt text)*.
- `learn-modules/configure-your-ui-dynamics-365-finance-operations-apps/media/06-m2-l6-p2.png`: the operator list (is exactly, is not, contains, does not contain, begins with, is one of, after, before, matches) over the Options tab (Personalize / Page options groups). Older style.
- `learn-modules/configure-your-ui-dynamics-365-finance-operations-apps/media/06-m2-l6-p1.png` (sort or filter menu on Product number), `...06-m2-l6-p3.png` (Options > Advanced filter or sort), `...06-m2-l6-p4.png` (Range / Sorting / Joins), `...06-m2-l6-p5.png` (save the query as a view) *(alt text)*.
- `learn-modules/configure-your-ui-dynamics-365-finance-operations-apps/media/11-m2-l11-p2.png` / `p3`: Product name contains "tablet", and the filtered result *(alt text)*.

### 2.F Working in grids

From [PER-4](https://learn.microsoft.com/en-us/training/modules/personalize-finance-operations/4-implicit) (implicit personalization), [PER-5](https://learn.microsoft.com/en-us/training/modules/personalize-finance-operations/5-explicit), [CUI-5](https://learn.microsoft.com/en-us/training/modules/configure-your-ui-dynamics-365-finance-operations-apps/manage-forms-fields), [NAV-4](https://learn.microsoft.com/en-us/training/modules/navigate-finance-operations/4-filtering-techniques) (link to Grid capabilities) and [ICI-10](https://learn.microsoft.com/en-us/training/modules/implement-common-integration-features-finance-ops/10-exercise-1):
- **Column width**: drag the sizing bar. The width is remembered.
- **Freeze column** / **Unfreeze column**: right-click the column header. The column becomes the first column and stays in view.
- **Reorder columns**: drag the gripper on the left of the header.
- **Insert columns** or **Add columns**: right-click the grid header. The dialog separates **Recommended fields** (added by other users) from **All fields**. Tick fields and select **Update**. **Hide this column** removes one.
- **Pinned marking column**: the selection column on the left, always visible. Select rows with it; the header has **Select all**.
- **Export all rows** / **Export marked rows**: right-click in the grid (static export to Excel).
- **Mathematical formulas** in numeric cells: type `=15*4` and press Tab to store 60. The value must start with `=`.
- **View column totals**: right-click a numeric column to show the sum, minimum, maximum or average in the footer. It needs the **Extended grid aggregation capabilities** feature, calculates the whole data set (slow on large sets), and shows per group if the grid is grouped.
- **Fast data entry**: keep entering rows while the server validates. **Paste from Excel**: copy rows in Excel, select **New** on the last line, paste, then **Save**.
- Keyboard shortcuts and multi-select are covered by the Grid capabilities article (link only).

Screenshots:
- `learn-modules/personalize-finance-operations/media/04-freeze-column.gif`: animation of freeze and unfreeze (21 MB GIF; too large for Word).
- `learn-modules/personalize-finance-operations/media/04-total-this-column-ss.svg`: AP Open prepayments grid with column totals. The alt text calls the option "Total this column"; the current label is **View column totals**.
- `learn-modules/configure-your-ui-dynamics-365-finance-operations-apps/media/05-m2-l5-p1.png`: grid header right-click menu on All customers: **Form information**, **Personalize: Account**, **Export all rows**, **Export marked rows**, **Hide this column**, **Add columns**, **View shortcuts**. Older style.
- `learn-modules/configure-your-ui-dynamics-365-finance-operations-apps/media/05-m2-l5-p2.png`: the Add columns dialog *(alt text)*.

### 2.G Personalization and saved views

**Personalization versus customization.** Personalization is a non-code change, usually for one user. Customization is code. Every personalization is yours alone, in every company, unless it is published as a view ([PER-1](https://learn.microsoft.com/en-us/training/modules/personalize-finance-operations/1-introduction), [PER-2](https://learn.microsoft.com/en-us/training/modules/personalize-finance-operations/2-custom-personalize), [ICP-3](https://learn.microsoft.com/en-us/training/modules/introduce-configure-personalization-dynamics-365-finance-operations-apps/explore-personalization-functionality)).

**Implicit personalization** is saved automatically: column widths, FastTab and FactBox states, QuickFilter column, filter operators, Action Pane pin ([PER-4](https://learn.microsoft.com/en-us/training/modules/personalize-finance-operations/4-implicit)).

**Explicit personalization.** Right-click a field > **Personalize**. The property window lets you change the label, **Hide**, **Include in FastTab summary**, **Skip in Tab key sequence**, **Require**, **Lock** (make non-editable), and **Personalize this page** ([PER-5](https://learn.microsoft.com/en-us/training/modules/personalize-finance-operations/5-explicit), [ICP-3](https://learn.microsoft.com/en-us/training/modules/introduce-configure-personalization-dynamics-365-finance-operations-apps/explore-personalization-functionality)).
- `learn-modules/introduce-configure-personalization-dynamics-365-finance-operations-apps/media/03-m1-l3-p1.png`: the Personalize pop-up for "Account" (Hide, Include in FastTab summary, Skip in Tab key sequence, **Personalize this form**).
- `learn-modules/personalize-finance-operations/media/05-explicit-1.png`: the Personalize dialog *(alt text)*.

**Personalization toolbar.** Open it from **Settings** (gear) > **Personalize**, from **Options** > **Personalize** group > **Personalize this page/form**, or with **Ctrl+Shift+P**. Tools:
- **Select**, **Hide** (shows hidden items shaded), **Require**, **Add a field** (insert fields that are on the page definition), **Move** (drop zones, within the same group only), **Skip**, **Show in header**, **Lock**.
- **...** (More): **Add a PowerApp** / **Add an app**, **Clear** (resets the page; no undo), **Import**, **Export** (to share a personalization as a file), **Close**.

Changes save immediately. A padlock means the property can't be changed, and a required field can't be hidden. Sources: [PER-8](https://learn.microsoft.com/en-us/training/modules/personalize-finance-operations/7-toolbar), [ICP-3](https://learn.microsoft.com/en-us/training/modules/introduce-configure-personalization-dynamics-365-finance-operations-apps/explore-personalization-functionality).
- `learn-modules/personalize-finance-operations/media/08-personalization_toolbar-ss.png`: the dark toolbar: **Select**, **Hide**, **Require**, **Add a field**, **Move**, **Skip**, **Show in header**, **Lock**, **...**, **Close**, and "Select an element to open a dialog and change its properties."
- `learn-modules/introduce-configure-personalization-dynamics-365-finance-operations-apps/media/03-m1-l3-p2.png` (older toolbar), `.../03-m1-l3-p3.png` and `.../03-m1-l3-p4.png` (Options > Personalize this page) *(alt text)*.
- `learn-modules/describe-finance-operations-apps/media/04-01-personalization-bar-10.png`: user personalization bar *(alt text)*.

**Saved views.** The view selector at top left shows the current view name (**Standard view** by default).
- Views are **not saved automatically**. An **asterisk** (\*) means unsaved changes.
- **Create**: select the view name > **Save as** > **Name**, optional **Description** > **Save**. A view saves personalization plus filters and sorting.
- **Default**: **More** > **Pin as default**, or set **Pin as default** in Save as.
- **In the selector**: **Standard view**, personal views (no padlock), locked or published views (padlock; use **Save as** to make your own copy), and new published views (spark icon).
- **Publishing**: views can be published to roles and legal entities (admin or saved-view admin).

Sources: [PER-7](https://learn.microsoft.com/en-us/training/modules/personalize-finance-operations/11-2-saved-views), [CUI-5](https://learn.microsoft.com/en-us/training/modules/configure-your-ui-dynamics-365-finance-operations-apps/manage-forms-fields), [CUI-6](https://learn.microsoft.com/en-us/training/modules/configure-your-ui-dynamics-365-finance-operations-apps/manage-forms-filters-ranges), [CUI-11](https://learn.microsoft.com/en-us/training/modules/configure-your-ui-dynamics-365-finance-operations-apps/exercise-change-form-fields-queries), [ICP-3](https://learn.microsoft.com/en-us/training/modules/introduce-configure-personalization-dynamics-365-finance-operations-apps/explore-personalization-functionality).
- `learn-modules/personalize-finance-operations/media/07-save-view-ss.png`: in fact the **Publish view to others** dialog (Name, purpose, **Publish as default view**, **Publish to people in these roles**, **Legal entity access**: All / Current only / Selected only). This is admin scope, not the user Save as dialog.
- `learn-modules/configure-your-ui-dynamics-365-finance-operations-apps/media/11-m2-l11-p4.png`: the view and query list *(alt text)*.

**Administration** (System administration > Setup > **Personalization**: Published views, Unpublished views, Personal views, User settings, System settings, **Import views**) is admin only ([PER-6](https://learn.microsoft.com/en-us/training/modules/personalize-finance-operations/11-admin-personalize)). `learn-modules/personalize-finance-operations/media/06-personalization-ss.svg`.

**Inventory dimension display** overrides personalization of inventory dimension columns ([PER-11](https://learn.microsoft.com/en-us/training/modules/personalize-finance-operations/10-personalize-inv-dim)). Not relevant to finance users.

### 2.H User options

Open with **Settings** (gear) > **User options**. Administrators can set them for other users from System administration > Users > Users > **User options**. There are four tabs, and two Action Pane buttons.

**Visual**: **Color theme** and **Size** (for example **Compressed**).

**Preferences**:
- **Startup**: **Company** (the legal entity you sign in to), **Initial page** (**Default dashboard**, **System administration**, **Essentials dashboard**, **Employee self-service**, **Prospective vendor registration**, and **Immersive Home**), **Default view/edit mode** (**Auto**, **View**, **Edit**).
- **Language and country/region preferences**: **Language**, **Date, time, and number format**, **Time zone**, **Country/region**. These change only how data is displayed, not how it is stored.
- **Miscellaneous**: **Enable document handling** (paperclip count; can affect performance) and **Automatically update query parameter** (filters saved in the URL when you add the page to Favorites or share its URL).
- **Accessibility**: **Enhanced tab sequence** (all fields in the tab order; works with Windows Narrator) and **Show tooltips on focus**.
- **Task management**: **Show task list on default dashboard**.

**Account**: User ID, Network domain, Name, Telemetry ID and Alias (display only); **Email provider selection** (**Email provider ID**; blank means "Prompt for which email provider to use"); **Sender email**; **Electronic signature**. Mostly set by administrators.

**Workflow**:
- **Notifications**: **Send notifications in email**, **Send notifications to Action Center**, **Line item workflow notification type** (individual or **Grouped**), **Alternate email**.
- **Delegation**: **Add** (**Scope**, **Name**, **Delegate**, **Start date/time**, **End date/time**) to hand over workflow approvals while you are away.

**Action Pane**: **Usage data** (view and delete your usage data) and **Personalization** (manage your page personalizations and reset feature callouts).

Sources: [PER-3](https://learn.microsoft.com/en-us/training/modules/personalize-finance-operations/3-user-options), [ICP-3](https://learn.microsoft.com/en-us/training/modules/introduce-configure-personalization-dynamics-365-finance-operations-apps/explore-personalization-functionality), [DFO-4](https://learn.microsoft.com/en-us/training/modules/describe-finance-operations-apps/4-explore-user-interface), [CUI-3](https://learn.microsoft.com/en-us/training/modules/configure-your-ui-dynamics-365-finance-operations-apps/manage-menus-dashboards-role), [DSF-8](https://learn.microsoft.com/en-us/training/modules/describe-shared-features/8-describe-alerts), [DRI-4](https://learn.microsoft.com/en-us/training/modules/describe-report-integration/4-describe-integration-office-365), exercise [PER-13](https://learn.microsoft.com/en-us/training/modules/personalize-finance-operations/13-exercise-1).

Screenshots:
- `learn-modules/describe-finance-operations-apps/media/04-01-user-options-08.png`: **Preferences** tab: Startup (Company USMF, Initial page Default dashboard, Default view/edit mode Auto), Language and country/region (en-us, time zone (GMT) Coordinated Universal Time, USA), Miscellaneous (Enable document handling Yes, Automatically update query param... No), Accessibility (both No), Task management (Show task list on default dashboard No).
- `learn-modules/personalize-finance-operations/media/03-preferences-1.svg`: the same tab as an SVG capture.
- `learn-modules/describe-shared-features/media/08-03-user-options-21.png`: **Workflow** tab: Notifications (Send notifications in email No, Send notifications to Action Center No, Line item workflow notification type Grouped) and an empty Delegation grid (Scope, Name, Delegate, Start date/time, End date/time, Enabled). The Action Pane shows Save, Usage data, Personalization, Options.
- `learn-modules/personalize-finance-operations/media/03-workflow-1.svg`: the Workflow tab (SVG).
- `learn-modules/describe-finance-operations-apps/media/04-01-color-picker-07.png`: Visual tab colour themes *(alt text)*. `.../04-01-workflow-options-09.png`: Workflow tab *(alt text)*.
- `learn-modules/introduce-configure-personalization-dynamics-365-finance-operations-apps/media/03-m1-l2-p4.png` (gear > User options) and `.../03-m1-l2-p5.png` (Preferences > Startup > Company) *(alt text)*.
- `learn-modules/configure-your-ui-dynamics-365-finance-operations-apps/media/03-m2-l3-p1.png`: **Initial page** options *(alt text)*.

### 2.I Legal entities and the company picker (multi-entity company)

**Concept.** A legal entity is an organization with a registered legal structure. It can enter contracts and must report on its performance. In D365 the only type you can create is a **company**, identified by a **Company ID** of up to four characters that can't be changed (for example USMF, USSI, DEMF). Most data is secured by company ID (DataAreaId): **users see data only for the company they are working in**, and only if their roles allow it. Some data is shared across companies: users, products, the global address book, currencies and exchange rates, and charts of accounts. Other data is per company: customers, vendors, module parameters, the ledger and fiscal calendar, number sequences and journal names. The country of the company's primary address decides which local features appear. Sources: [DSF-5](https://learn.microsoft.com/en-us/training/modules/describe-shared-features/5-describe-organization-legal-entities), [LE-2](https://learn.microsoft.com/en-us/training/modules/plan-implement-legal-entities-finance-operations/2-create-legal-entity), [LE-5](https://learn.microsoft.com/en-us/training/modules/plan-implement-legal-entities-finance-operations/6-legal-entities-vs-oper-units), [LE-6](https://learn.microsoft.com/en-us/training/modules/plan-implement-legal-entities-finance-operations/7-legal-entities-vs-oper-units-2), [DFC-3](https://learn.microsoft.com/en-us/training/modules/describe-dynamics-365-finance-core-capabilities/3-describe-reporting-currency-accounting-currency), [DFC-2](https://learn.microsoft.com/en-us/training/modules/describe-dynamics-365-finance-core-capabilities/2-describe-finance-capabilities-features).

**Switching company.** Select the **company picker** on the navigation bar (it shows the current company, for example "USMF | Contoso Entertainment System USA") and choose another company from the list. Transactions you enter belong to the selected company. To change the company you open at sign-in, go to User options > **Preferences** > **Startup** > **Company**. LE-6 notes that "You must manually change companies to enter transactions and perform inquiries in multiple legal entities." ICA-3 and ICA-7 switch company to check the other side of an intercompany entry. The quiz asks whether you can change the legal entity once signed in (answer: yes). Sources: [ICP-2](https://learn.microsoft.com/en-us/training/modules/introduce-configure-personalization-dynamics-365-finance-operations-apps/set-up-your-environment), [ICP-3](https://learn.microsoft.com/en-us/training/modules/introduce-configure-personalization-dynamics-365-finance-operations-apps/explore-personalization-functionality), [DFO-4](https://learn.microsoft.com/en-us/training/modules/describe-finance-operations-apps/4-explore-user-interface), [LE-6](https://learn.microsoft.com/en-us/training/modules/plan-implement-legal-entities-finance-operations/7-legal-entities-vs-oper-units-2).
- `learn-modules/introduce-configure-personalization-dynamics-365-finance-operations-apps/media/02-m1-l2-p3.png`: the company drop-down open (RUMF, RURT, SAMF, THMF, us01, **USMF**, USP2 with names). Older blue style.
- `learn-modules/describe-finance-operations-apps/media/04-01-navigation-bar-04.png`: company picker on the current bar.

**Working across companies without switching:**
- **Global general journals** (General ledger > Journal entries > **Global general journals**) show the journals of all companies and let you create a journal in a chosen company ([GLD-4](https://learn.microsoft.com/en-us/training/modules/general-ledger-daily-procedures-dyn365-finance/4-gl-processes), [DGL-6](https://learn.microsoft.com/en-us/training/modules/describe-general-ledger-cash-bank-management/6-describe-financial-journals), [ICA-7](https://learn.microsoft.com/en-us/training/modules/intercompany-accounting-dyn365-finance/5-exercise)).
- **"All companies"** Power BI pages, for example Cash overview - all companies and Fixed asset **Analytics - all companies**.
- Alert rules can be **Organization-wide** (DSF-8).
- `learn-modules/general-ledger-daily-procedures-dyn365-finance/media/04-global-general-journals.svg`: Global general journals list with a company column (usmf).

**Operating units** (cost centers, departments, business units) are not companies. They usually appear to users as financial dimensions ([DSF-5](https://learn.microsoft.com/en-us/training/modules/describe-shared-features/5-describe-organization-legal-entities), [LE-4](https://learn.microsoft.com/en-us/training/modules/plan-implement-legal-entities-finance-operations/4-org-hier-units)).

### 2.J Office integration: Excel, Word and email

**Open in Microsoft Office** (the Office icon at the top right of the page). It has two sections:
- **Export to Excel**: a static copy of a visible grid with the current filter. It exports only the grid's columns, including columns you added by personalization. The same export is on the grid's right-click menu as **Export all rows** / **Export marked rows**.
- **Open in Excel**: opens a workbook through the **Microsoft Dynamics Office Add-in** (Excel Data Connector). You can **Refresh** the data, edit it and **Publish** it back. It is based on a data entity. Options listed include "Customers (USMF)" and "[Obsolete] ..." entries. You can **Download** the workbook or save it to OneDrive or SharePoint. Excel 2016 or later is required. The first time, you **Enable Editing**, **Trust this add-in** (or **Accept and Continue**) and **Sign in**.

The Data Connector pane has **Refresh**, **Publish**, **Design** (add or remove fields), **Options** (gear; shows the **Server URL**), and **Messages** (flag; counts of records added, updated and deleted, and errors). Remove Excel filters before you publish. Add a record by typing below the table; delete one by clearing the row. Publishing runs the normal validation and reports errors. Sources: [WAR-2](https://learn.microsoft.com/en-us/training/modules/work-analytics-reporting-finance-operations/2-types), [DRI-4](https://learn.microsoft.com/en-us/training/modules/describe-report-integration/4-describe-integration-office-365), [ICI-2](https://learn.microsoft.com/en-us/training/modules/implement-common-integration-features-finance-ops/2-office), [CYD-4](https://learn.microsoft.com/en-us/training/modules/configure-your-data-dynamics-365-finance-operations-apps/integrate-office), end-user exercise [CYD-7](https://learn.microsoft.com/en-us/training/modules/configure-your-data-dynamics-365-finance-operations-apps/exercise-use-excel-view-update-data), [ICI-10](https://learn.microsoft.com/en-us/training/modules/implement-common-integration-features-finance-ops/10-exercise-1), [GSF-2](https://learn.microsoft.com/en-us/training/modules/get-started-financial-management-dyn365-finance/2-benefits).

Screenshots:
- `learn-modules/configure-your-data-dynamics-365-finance-operations-apps/media/07-m3-l7-p1.png` (the Office icon), `.../07-m3-l7-p2.png` (menu: **OPEN IN EXCEL** Customers (usmf), [Obsolete] Customers (usmf), [Obsolete] Customers V2 (usmf); **EXPORT TO EXCEL** Customers), `.../07-m3-l7-p3.png` (Download / OneDrive / SharePoint options *(alt text)*), `.../07-m3-l7-p4.png` (customer data in Excel *(alt text)*), `.../07-m3-l7-p5.png` (changed name, Publish highlighted *(alt text)*), `.../07-m3-l7-p6.png` (refreshed list showing the update *(alt text)*). **A complete screenshot sequence for a guide.**
- `learn-modules/describe-report-integration/media/04-2-4-export-to-excel.png`: the menu with Customer definitions (USMF), Customers (USMF), Demand planning..., [Obsolete]..., and **EXPORT TO EXCEL** Customers highlighted.
- `learn-modules/implement-common-integration-features-finance-ops/media/02-office-1.png` (Office icon), `02-static-excel.png` (Export to Excel in the menu), `02-office-2.png` (Download of a template option), `02-office-3.png` (Excel with the Data Connector pane) *(alt text)*.
- `learn-modules/describe-report-integration/media/04-2-4-connector.png`: the Microsoft Dynamics Office add-in *(alt text)*.
- `learn-modules/work-analytics-reporting-finance-operations/media/02-grid-export.svg`: All vendors, Export to Excel from a list.
- `learn-modules/get-started-financial-management-dyn365-finance/media/02-excel1.png`: an example Excel page *(alt text)*.

**Journal lines in Excel.** On a journal, **Open lines in Excel** (or Open in Microsoft Office > **Open in Excel**) offers templates:
- **General journal line entry**: Ledger, Customer, Vendor, Bank; intercompany.
- **Vendor invoice register**, **Vendor invoice journal**, **Vendor invoice**.
- **Free Text Invoice**.
- **Fixed asset journal line**.
- **Vendor payment journal**.
- **Customer payment journal**: Customer with a Bank offset; intercompany.
- **Journal lines for Project – expenses entry**.

Then Publish, then Validate in D365, then Post. If publishing fails, answer **No** to the refresh prompt; **Yes** wipes your changes. Opening in Excel for the web can fail, so download the file. Common errors: "Load applets", "Forbidden", time-outs (reduce the batch size). Sources: [GLD-6](https://learn.microsoft.com/en-us/training/modules/general-ledger-daily-procedures-dyn365-finance/create-templates), [CLJ-8](https://learn.microsoft.com/en-us/training/modules/configure-ledgers-journals-dyn365-finance/4-journals), [CLJ-9](https://learn.microsoft.com/en-us/training/modules/configure-ledgers-journals-dyn365-finance/journal-lines-excel).
- `learn-modules/general-ledger-daily-procedures-dyn365-finance/media/06-general-ledger-template.png`, `06-vendor-invoice-register-template.png`, `06-invoice-journal-template.png`, `06-vendor-invoice-template.png`, `06-free-text-invoice-template.png`, `06-fixed-asset-journal-template.png`, `06-vendor-payment-journal-template.png`, `06-customer-payment-journal-template.png`: one Excel template per journal type *(alt text)*.
- `learn-modules/configure-ledgers-journals-dyn365-finance/media/09-new-office-add-in.png`: the **New Office Add-in** prompt with **Trust this add-in** *(alt text)*.

**Templates and Word.** Templates are stored in **Common > Common > Office integration > Document templates**. CLJ-9 says Organization administration > Setup > Office integration > Document templates; see section 4. **Export to Word** templates appear under Open in Microsoft Office. **Excel workbook designer** is for admins and power users ([DRI-4](https://learn.microsoft.com/en-us/training/modules/describe-report-integration/4-describe-integration-office-365), [ICI-3](https://learn.microsoft.com/en-us/training/modules/implement-common-integration-features-finance-ops/3-excel)).
- `learn-modules/describe-report-integration/media/04-2-4-templates.png` *(alt text)*; `learn-modules/implement-common-integration-features-finance-ops/media/03-workbook-designer.svg`.

**Sending email from D365** (for example statements, collection letters, documents):
1. The **How would you like to send email** dialog offers **Use an email app, such as Outlook** (downloads a .eml file), **Use Exchange email server**, and **Use the system email client** (ICI-5 labels it "Use the Microsoft finance and operations apps email client"; sends by SMTP). **Do not ask again** remembers your choice. You can reset it in User options > **Account** > **Email provider ID**.
2. The **Send email** dialog lets you edit From, To, Cc, Bcc, Subject, Body and attachments.

Example path: AR > Customers > All customers > **Collect** > Customer balances > **Collections** > Communicate > Email > **Statement to contact**. Sources: [DRI-4](https://learn.microsoft.com/en-us/training/modules/describe-report-integration/4-describe-integration-office-365), [ICI-5](https://learn.microsoft.com/en-us/training/modules/implement-common-integration-features-finance-ops/5-emails-exchange), [CYD-4](https://learn.microsoft.com/en-us/training/modules/configure-your-data-dynamics-365-finance-operations-apps/integrate-office).
- `learn-modules/implement-common-integration-features-finance-ops/media/05-statement.svg`: the Collections page used to email a statement.

**Copilot and agents in Microsoft 365.** Finance agents work in Outlook (collections) and Excel (financial reconciliation) ([DFO-3](https://learn.microsoft.com/en-us/training/modules/describe-finance-operations-apps/3-describe-use-cases-ai-tools), [DGL-8](https://learn.microsoft.com/en-us/training/modules/describe-general-ledger-cash-bank-management/8-describe-cash-bank-management)).

### 2.K Reports, inquiries and analytics

**Where reports are.** Each module has an **Inquiries and reports** menu, for example General ledger > Inquiries and reports ([WAR-4](https://learn.microsoft.com/en-us/training/modules/work-analytics-reporting-finance-operations/4-find-inquiries-reports)). `learn-modules/work-analytics-reporting-finance-operations/media/04-inq-rep.png`: the GL Inquiries and reports menu *(alt text)*.

**Types of reporting.**
- WAR-2: embedded analytics (charts, tiles, grids), **SSRS** reports (business documents such as invoices and packing slips; to screen, printer, file or email), **Financial reporting** (Financial Report Designer: statements), Power Platform (Power BI), and **Electronic reporting** (regulatory and electronic formats).
- ERT-1 frames five reporting experiences with "when to use": Operational views, Business documents, Analytical tools and visualizations, Electronic reporting, Financial reporting.
- DRI-2 adds that **inquiry pages** are grids you can filter, sort and export to Excel, which the quiz tests as "quick, on-demand analysis".

Sources: [WAR-2](https://learn.microsoft.com/en-us/training/modules/work-analytics-reporting-finance-operations/2-types), [ERT-1](https://learn.microsoft.com/en-us/training/modules/explore-reporting-tools-finance-operations/01-Overview), [DRI-2](https://learn.microsoft.com/en-us/training/modules/describe-report-integration/2-describe-built-in-reporting).

**Running and outputting a report.**
- Report dialogs have a **Run in the background** section (see 2.L).
- Reports can be previewed and exported to PDF, CSV, Word and other formats from the preview toolbar. Several reports at once download as a .ZIP.
- Documents can go to network printers (set up by IT).
- Printing scenarios: print what's shown (HTML5, the browser's print), interactive printing (PDF preview, then print), and network printing (Document Routing Agent).

Sources: [WAR-5](https://learn.microsoft.com/en-us/training/modules/work-analytics-reporting-finance-operations/4-1-generate-consume-inquiries-reports), [ICI-8](https://learn.microsoft.com/en-us/training/modules/implement-common-integration-features-finance-ops/8-network-print), [BAT-3](https://learn.microsoft.com/en-us/training/modules/setup-batch-jobs-finance-operations/3-reports-alerts).

**Report layout.** AR > Setup > Forms > **Form setup** changes what prints on documents, for example the tax exempt number on a free text invoice. Preview a copy from the invoice: **Document** > **View** > **Copy**. Business Document Management lets business users edit templates in Word or Excel ([CUI-7](https://learn.microsoft.com/en-us/training/modules/configure-your-ui-dynamics-365-finance-operations-apps/configure-reports), [CUI-12](https://learn.microsoft.com/en-us/training/modules/configure-your-ui-dynamics-365-finance-operations-apps/exercise-change-report-output), [DRI-7](https://learn.microsoft.com/en-us/training/modules/describe-report-integration/7-describe-business-documents)). `learn-modules/configure-your-ui-dynamics-365-finance-operations-apps/media/12-m2-l12-p1.png` (Form setup menu) and `12-m2-l12-p2.png` (the invoice with the tax exempt number) *(alt text)*.

**Financial reports** (General ledger > Inquiries and reports > **Financial reports**):
- The list shows default report definitions (12 Month Rolling..., Actual vs Budget - Default, Balance Sheet - Default, Detailed/Summary Trial Balance - Default, Income Statement - Default...).
- **Generate** asks for a report date. The expiry is set to 90 days ("three months") by default and can be set to **Never**.
- Select the report > **View**. Drill down from **All accounts** to an account and to transaction detail, then use the back arrow.
- **Report options** > **Add a dimension filter** (a personal view), **Currency** (show in another currency), change the date, summary or detail view, attribute filters.
- **New** / **Edit** opens the Report Designer, a downloaded desktop tool for designers.

Sources: [WAR-3](https://learn.microsoft.com/en-us/training/modules/work-analytics-reporting-finance-operations/3-financial-reporting), [WAR-7](https://learn.microsoft.com/en-us/training/modules/work-analytics-reporting-finance-operations/6-exercise-1), [DGL-7](https://learn.microsoft.com/en-us/training/modules/describe-general-ledger-cash-bank-management/7-describe-financial-reporting-capabilities), [CLJ-8](https://learn.microsoft.com/en-us/training/modules/configure-ledgers-journals-dyn365-finance/4-journals).
- `learn-modules/explore-general-ledger-dynamics-365/media/07-02-explore-the-dynamics-365-finance-and-operations-apps-mod-2-20.svg`: the Financial reports list (Generate, New, Edit; Default Report Definitions).
- `learn-modules/explore-general-ledger-dynamics-365/media/07-02-explore-the-dynamics-365-finance-and-operations-apps-mod-2-21.svg`: generated reports for Balance List - Default (View, Delete, **Expiration**, Report date, Generated date).
- `learn-modules/configure-ledgers-journals-dyn365-finance/media/08-financial-reports-ss.svg`: Balance Sheet - Default generated report list.
- `learn-modules/describe-general-ledger-cash-bank-management/media/07-5-7-reports.png` (Generate), `07-5-7-balance-list.png` *(alt text)*.
- `learn-modules/work-analytics-reporting-finance-operations/media/03-expiration-date-ssm.png`, `03-expiration-date-choices-ssm.png`: report expiration (90 days or Never) *(alt text)*.

**GL inquiries** (CLJ-8, GLD-4):
- **Trial balance** (General ledger > Inquiries and reports > **Trial balance**): **Parameters** (dates in one fiscal year, posting layer, opening balances, closing transaction types), a choice of **financial dimension set**, dimensions in separate columns, and drill-down to transactions.
- **Voucher transactions**: a query on tables and fields; filter by date, account, posting type or layer; **Related vouchers**.
- **Audit trail**: who posted what and when; shows the last seven days by default; **Voucher** button.
- **Ledger transaction list**.
- Posted ledger transactions can't be changed. Correct them with a new entry (a transfer or reversal).

Ledger reports: **Dimension statement**, **Ledger transaction list**, **Print journal**, **Posted transactions by journal** (dates must be in one fiscal year), **Transaction list by date**, **Transaction origin**.
- `learn-modules/general-ledger-daily-procedures-dyn365-finance/media/04-trial-balance.svg`: Trial balance with the **Parameters** button and accounts by dimension (110110-001 Bank Account - USD-Home...).
- `learn-modules/configure-ledgers-journals-dyn365-finance/media/08-voucher-transactions-ss.svg`: Voucher transactions (voucher, journal, date, ledger account string such as 401100-001-022, amounts).
- `learn-modules/configure-ledgers-journals-dyn365-finance/media/08-audit-trail-ss.svg`: Audit trail with the message "Audit trail records are shown for the last seven days. Use the filter to change the date range if necessary."
- `learn-modules/intercompany-accounting-dyn365-finance/media/04-voucher-transactions.svg`: Voucher transactions (AR line, 2022 data).

**Power BI and analytics.** Embedded Power BI appears on workspace **Analytics** tabs. In a Power BI report, filtering changes only your view, not the data. Report consumers can change existing filters but can't add new ones. Filter levels are Report, Page, Visual and Drill through ([DRI-3](https://learn.microsoft.com/en-us/training/modules/describe-report-integration/3-describe-analyze-data-power-bi)). **Business performance analytics** is included with the Finance licence ([GSF-4](https://learn.microsoft.com/en-us/training/modules/get-started-financial-management-dyn365-finance/4-general-ledger)). Ready-made Power BI content is listed in WAR-6, DGL-7 and DRI-2 (Actual vs. budget, Cash overview, Credit and collections management, Financial analysis, Vendor payment...). Section 4 covers the outdated LCS source.
- `learn-modules/describe-report-integration/media/03-2-3-power-bi-data.png`: filtering doesn't affect the source data *(alt text)*.
- `learn-modules/describe-general-ledger-cash-bank-management/media/07-5-7-financial-analysis.png`, `07-5-7-fixed-asset.png`: Power BI pages *(alt text)*.

**AI insights.**
- **Summary by Copilot** FastTab on All vendors, All customers, purchase orders, the Collections coordinator workspace and Workflow history. It is personalised by role ([DAPAR-3](https://learn.microsoft.com/en-us/training/modules/describe-account-payables-account-receivables/3-describe-core-accounts-payable-components), [DAPAR-6](https://learn.microsoft.com/en-us/training/modules/describe-account-payables-account-receivables/6-describe-core-accounts-receivable-components), [DSF-3](https://learn.microsoft.com/en-us/training/modules/describe-shared-features/3-describe-workflow-capabilities)).
- **Finance insights**: customer payment predictions, cash flow forecasts, budget proposals ([DRI-8](https://learn.microsoft.com/en-us/training/modules/describe-report-integration/8-describe-finance-insights)).
- `learn-modules/describe-account-payables-account-receivables/media/03-6-3-copilot.png`: All vendors with Summary by Copilot *(alt text)*.
- `learn-modules/describe-report-integration/media/08-2-8-payment-prediction.png`: payment prediction "will be paid on time" *(alt text)*.

### 2.L Batch jobs and background processing

**What a batch job is.** A batch job runs a process in the background on the server, so you don't have to wait. Use it for long, non-urgent or periodic work (printing reports, sending electronic documents, posting). Jobs can recur (every minute, hour, day, week, month or year) and can send alerts. Sources: [DSF-4](https://learn.microsoft.com/en-us/training/modules/describe-shared-features/4-describe-concept-batch-jobs), [BAT-1](https://learn.microsoft.com/en-us/training/modules/setup-batch-jobs-finance-operations/1-introduction).

**What the user does.** In a report or process dialog, open the **Run in the background** section:
1. Set **Batch processing** to **Yes**. With **No**, the process runs synchronously in the browser.
2. Optionally enter **Task description**, **Batch group**, **Private**, **Critical Job** and **Monitoring category**.
3. Select **Recurrence** to set a range and pattern (**Define recurrence**).
4. Select **Alerts** to get a message when the job **ends**, **has an error** or **is canceled**, optionally as a pop-up.

Sources: [BAT-3](https://learn.microsoft.com/en-us/training/modules/setup-batch-jobs-finance-operations/3-reports-alerts), [DSF-4](https://learn.microsoft.com/en-us/training/modules/describe-shared-features/4-describe-concept-batch-jobs), [BAT-6](https://learn.microsoft.com/en-us/training/modules/setup-batch-jobs-finance-operations/6-exercise).
- `learn-modules/describe-shared-features/media/04-03-run-as-batch-07.png`: the dialog "Verify compliance of user-role assignments with rules for segregation of duties", **Run in the background** section: **Recurrence** and **Alerts** links, **Batch processing** No, Task description, **Batch group**, Private No, Critical Job No, Monitoring category Undefined, start date in UTC; OK, Cancel.
- `learn-modules/setup-batch-jobs-finance-operations/media/03-define-recurrence.png`: **Define recurrence** dialog *(alt text)*.
- `learn-modules/setup-batch-jobs-finance-operations/media/03-alerts-1.png`: **Batch job alerts** dialog *(alt text)*.
- `learn-modules/describe-shared-features/media/04-03-batch-recurrence-schedule-08.png`, `04-03-batch-alerts-09.png`: recurrence and alerts *(alt text)*.

**Timing.** A batch server checks for waiting tasks once a minute, so a job can take about a minute to start ([BAT-2](https://learn.microsoft.com/en-us/training/modules/setup-batch-jobs-finance-operations/2-batch-process-batch-servers)). The alert system itself runs as a batch job, so alerts arrive "within a few minutes" ([DSF-8](https://learn.microsoft.com/en-us/training/modules/describe-shared-features/8-describe-alerts)). Subledger to GL transfer can lag (2.R6).

**Checking a job.** The **Batch job** page (System administration > Inquiries > **Batch jobs**) lists waiting, running and ended jobs, with history and log messages. "Not everyone has access to the Batch job page", so some pages give a status link instead, for example **View activation status** on account structures, with **Refresh** ([DSF-4](https://learn.microsoft.com/en-us/training/modules/describe-shared-features/4-describe-concept-batch-jobs), [SFD-9](https://learn.microsoft.com/en-us/training/modules/set-up-financial-dimensions-finance/define-structure-rules)). Large journal reversals (over 100 lines) run in batch, and results are in the batch job history ([CLJ-10](https://learn.microsoft.com/en-us/training/modules/configure-ledgers-journals-dyn365-finance/reverse-journal-posting)). Post journals can run as a batch, with **Late selection** ([GLD-4](https://learn.microsoft.com/en-us/training/modules/general-ledger-daily-procedures-dyn365-finance/4-gl-processes)).
- `learn-modules/describe-shared-features/media/04-03-batch-job-inquiry-list-page-10.png`: Batch job page *(alt text)*.
- `learn-modules/setup-batch-jobs-finance-operations/media/04-copy-batch-job.svg`: Batch jobs list (Job ID, Status **Withhold**, Job description, Scheduled start date/time, Created by, Run by; buttons Batch job history, Recurrence, Alerts, Change status).
- `learn-modules/describe-shared-features/media/04-03-activate-structure-batch-status-link-11.png`, `04-03-activate-structure-status-12.png`: status link and status dialog *(alt text)*.

Administrator-only content: batch groups, batch servers, priority-based scheduling, Copy batch job, Run by, the Batch job manager role, statuses (**Withhold**, **Waiting**, **Change status**) ([BAT-2](https://learn.microsoft.com/en-us/training/modules/setup-batch-jobs-finance-operations/2-batch-process-batch-servers), [BAT-4](https://learn.microsoft.com/en-us/training/modules/setup-batch-jobs-finance-operations/4-copy-a-batch-job), [BAT-5](https://learn.microsoft.com/en-us/training/modules/setup-batch-jobs-finance-operations/5-batch-manager-role)).

### 2.M Workflow and approvals

**Concept.** A workflow defines how a document moves through the system: who completes tasks, makes decisions and approves. Elements are manual and automated tasks, approvals, line-item workflows, manual and conditional decisions, parallel branches and subworkflows. There are more than 75 standard workflows. Finance examples:
- GL: **Ledger daily journal workflow**, allocations, eliminations.
- AP: **Vendor invoice workflow**, Vendor invoice line, **Proposed vendor changes**, vendor payment journals.
- AR: **Customer free text invoice workflow**, **Customer payment workflow**, **Proposed customer change**, **Credit management release**, **Credit limit adjustment**.
- Cash and bank: **Bank reconciliation journal approval**.
- Procurement: **Purchase requisition review**, **Purchase order workflow**.
- Expense management workflows.

Workflow steps are best assigned to roles, groups or the managerial hierarchy, not to named people. Sources: [DSF-3](https://learn.microsoft.com/en-us/training/modules/describe-shared-features/3-describe-workflow-capabilities), [WF-2](https://learn.microsoft.com/en-us/training/modules/create-use-workflows-finance-operations/2-types), [WF-3](https://learn.microsoft.com/en-us/training/modules/create-use-workflows-finance-operations/3-setup).
- `learn-modules/describe-shared-features/media/03-03-flow-through-a-workflow-05.png`: originator, task assignees, decision maker and approvers in an expense report flow *(alt text)*.
- `learn-modules/create-use-workflows-finance-operations/media/04-logic-1.png`: the same roles diagram *(alt text)*.
- `learn-modules/describe-shared-features/media/03-03-workflow-editor-04.png`, `learn-modules/create-use-workflows-finance-operations/media/03-wf-designer.png`: the workflow editor (designer, not user) *(alt text)*.

**What the user sees** ([WF-4](https://learn.microsoft.com/en-us/training/modules/create-use-workflows-finance-operations/4-assign-users)):
- On a page with workflow, a **yellow information bar** and a **Workflow** menu or **Submit** button (or an **Actions** menu) appear at the top.
- After you submit a journal, some buttons are unavailable. After approval, **Post** becomes available and the fields are locked. Editing an approved journal resets the workflow, and you must resubmit.

**Actions by role in the workflow:**
- **Originator**: **Submit**. After a rejection or a change request, resubmit.
- **Task assignee**: **Complete**, **Reject**, **Delegate**, **Request change**, **Reassign** (to another queue), **Release** (back to the queue). Only one person completes a task. The quiz asks which action a task assignee can't perform: **Approve**.
- **Decision maker**: Yes/No (or True/False), or **Delegate**.
- **Approver**: **Approve**, **Reject**, **Delegate**, **Request change**.
- A resubmitted document restarts at the first approver.

**Work items.** Work items assigned to you appear on the dashboard (**Work items assigned to me**) and in Immersive Home, with Approve / Reject / Return buttons. Notifications go by email or to the Action center according to User options > Workflow. Delegation for absence is set in User options > Workflow > **Delegation** ([PER-3](https://learn.microsoft.com/en-us/training/modules/personalize-finance-operations/3-user-options), [DSF-8](https://learn.microsoft.com/en-us/training/modules/describe-shared-features/8-describe-alerts)). WF-5 ("Use the daily journal workflow") is mostly a video. The text explains that a **periodic journal can't be posted directly**: it is retrieved into a general journal and then submitted.
- `learn-modules/create-use-workflows-finance-operations/media/05-periodic-journal.png`: journal voucher with an interest entry *(alt text)*.

**Workflow history.** The **Workflow** menu on the page > **View history**, or Organization administration > Workflow > **Workflow history** for all. The page shows a **Summary by Copilot** FastTab (when the **Workflow history summary** feature is on) and the **Tracking details** list (Context, Action, Name, Message, Comment, Created). Sources: [DSF-3](https://learn.microsoft.com/en-us/training/modules/describe-shared-features/3-describe-workflow-capabilities), [WF-3](https://learn.microsoft.com/en-us/training/modules/create-use-workflows-finance-operations/3-setup).
- `learn-modules/describe-shared-features/media/03-03-workflow-history-06.png`: Workflow history for "000087 : Document number: USMF000009". The highlighted **Summary by Copilot** says it was submitted by a user on 27 Nov 2016, status Completed. Below are General and the **Tracking details list** (Workflow Submission, Creation, Automated task Completion, Approval Creation, Step Creation).
- `learn-modules/describe-shared-features/media/03-vendor-change-request.png`: landing page of a vendor change request simulation *(alt text)*.

**Journal approval without a workflow** (manual approval, from the journal name): the journal has an **Approval** menu > **Report as ready**, and the approver (a member of the user group set on the journal name) approves or rejects it. With workflow approval, use the **Workflow** menu > **Submit**. A journal name can't use both ([CLJ-7](https://learn.microsoft.com/en-us/training/modules/configure-ledgers-journals-dyn365-finance/journal-approvals), [DGL-3](https://learn.microsoft.com/en-us/training/modules/describe-general-ledger-cash-bank-management/3-describe-chart-accounts-functionality)).
- `learn-modules/configure-ledgers-journals-dyn365-finance/media/07-standard-view.svg`: journal voucher (Approval menu context; lines GNJL001045/46, Bank USMF PAYRL).
- `learn-modules/configure-ledgers-journals-dyn365-finance/media/07-workflow-approval.svg`: General journals list including WFGenJrn "WF General Journal" (Workflow menu).
- `learn-modules/configure-ledgers-journals-dyn365-finance/media/07-journal-name-manual-approval.png`, `07-journal-name-workflow-approval.png`: Journal names approval settings *(alt text)*.

### 2.N Alerts and notifications

**Action center.** The bell on the navigation bar holds system messages and workflow notifications. The screen-reader text in the SVGs reads "New messages are in the Action Center", with the shortcut **Ctrl-Shift-F7** to read them ([DFO-4](https://learn.microsoft.com/en-us/training/modules/describe-finance-operations-apps/4-explore-user-interface), BW-1 SVG).

**Alert rules.** Use them to be told when data changes:
- **Triggers**: a record is created, updated or deleted; a field changes or gets a particular value; a due date approaches (date fields only). Batch job alerts and workflow notifications are separate.
- **Where**: **Options** > **Share** > **Create a custom alert** / **Manage my alerts** on any page. Batch dialogs have **Alerts**.
- **Dialog sections**:
  - **Alert me when**: Table name, Event (for example "Record has been created"), Field.
  - **Alert me for**: All records or the current record, and **Organization-wide** (all legal entities) or the current company only.
  - **Alert me until**: No end date, or an expiry.
  - **Alert me with**: Subject, Message, User ID, **Send email** and email recipients.
- **Access**: you need write access to the data for change and delete alerts; read access is enough for create alerts.
- **Delivery**: alerts run as a batch job and arrive within a few minutes.
- **Best practice**: set up only the alerts you need (they affect performance), set an expiry for temporary ones, and use one alert with a distribution list rather than one alert per person.
- Workflow alerts go by email or to the Action center, as set in User options > **Workflow** > **Notifications**.

Sources: [DSF-8](https://learn.microsoft.com/en-us/training/modules/describe-shared-features/8-describe-alerts), [BAT-3](https://learn.microsoft.com/en-us/training/modules/setup-batch-jobs-finance-operations/3-reports-alerts).
- `learn-modules/describe-shared-features/media/08-03-create-alert-rule-20.png`: **Create alert rule** for User Information: Alert me when (Table name, Event "Record has been created", Field <All fields>), Alert me for (All records, Organization-wide Yes), Alert me until (No end date), Alert me with (Subject, User ID Admin, Message, Send email No, Email recipients).
- `learn-modules/personalize-finance-operations/media/10-dashboard-1.svg`: a Bank accounts page with the **Options** menu open, showing **Get a link**, **Create a custom alert**, **Manage my alerts** (the alt text wrongly calls it a dashboard).
- `learn-modules/describe-shared-features/media/08-03-user-options-21.png`: alert and notification settings in User options (see 2.H).

### 2.O Help and learning

**In-product help** ([HELP-3](https://learn.microsoft.com/en-us/training/modules/get-help-finance-operations/4-in-product-help)):
- **Field descriptions**: hover over a field. The **Field descriptions** page lets you view and export them for a page, and companies can customize them ([HELP-4](https://learn.microsoft.com/en-us/training/modules/get-help-finance-operations/5-customize-help)).
- **Help pane**: **Help** (?) > **Help**, or **Ctrl+Shift+?**. The **Help** tab lists Microsoft Learn articles for the current page (they open in a new tab) and has a search.
- **Task guides**: the **Task Guides** tab lists guided procedures for the page. Select one, then **Start task guide**. A black pointer shows each step, with **Previous step** and **Skip this step**. **The data you enter in a task guide is real**: in production it posts in your current company. If no task guides appear, the Help system hasn't been set up (admin).

- `learn-modules/get-help-finance-operations/media/03-task-guide.png`: a task guide bubble "Click Invoice." with **Show less**, **Previous step**, **Skip this step**, over a sales order Action Pane (Pick and pack tab).
- `learn-modules/get-help-finance-operations/media/02-docs-site.png`: a Microsoft Learn documentation article *(alt text)*.

**Microsoft Learn documentation** is public, needs no sign-in, can be found with a search engine, and accepts feedback through GitHub ([HELP-2](https://learn.microsoft.com/en-us/training/modules/get-help-finance-operations/3-docs-site)). Other resources: the Dynamics community, the support blog, and Lifecycle Services (for partners) ([HELP-6](https://learn.microsoft.com/en-us/training/modules/get-help-finance-operations/7-summary)).

**Copilot sidecar.** A conversational pane for in-app help and guidance. It draws on Microsoft's public documentation, answers questions about your data, and can recommend and perform actions. "AI generated content may be incorrect" ([DFO-3](https://learn.microsoft.com/en-us/training/modules/describe-finance-operations-apps/3-describe-use-cases-ai-tools), [SCM-2](https://learn.microsoft.com/en-us/training/modules/get-started-supply-chain-management-dyn365-supply-chain-mgmt/2-benefits)). The quiz expects "AI-driven help, guidance, and answers".

**Task recorder** (**Settings** > Task recorder): records a process as a guided tour, a Word document with screenshots (**Export as Word document**), a test, or a playback. It saves to the PC (.axtr), to LCS, or as a developer recording ([DFO-4](https://learn.microsoft.com/en-us/training/modules/describe-finance-operations-apps/4-explore-user-interface); pane shown in `learn-modules/personalize-finance-operations/media/04-user-interface-01.png`). Mostly for trainers and testers.

**Privacy.** GDPR data-subject rights and the Service Trust Portal ([HELP-5](https://learn.microsoft.com/en-us/training/modules/get-help-finance-operations/6-gdpr)). Not end-user procedure content.

### 2.P Mobile

There is no end-user mobile app content. MOB teaches building Power Apps on Dataverse virtual entities, run in **Power Apps mobile** after signing in with Entra ID and Microsoft Authenticator, and custom-branded apps with **wrap**. Its summary links to the 2022 announcement that the old "Finance and operations (Dynamics 365) mobile app" is deprecated. GSF-2 says Finance "runs on any device" through the browser. Sources: [MOB-7](https://learn.microsoft.com/en-us/training/modules/mobile-experiences-finance-operations/access-mobile-experiences), [MOB-9](https://learn.microsoft.com/en-us/training/modules/mobile-experiences-finance-operations/summary), [GSF-2](https://learn.microsoft.com/en-us/training/modules/get-started-financial-management-dyn365-finance/2-benefits).
- `learn-modules/mobile-experiences-finance-operations/media/07-mobile-app.png` (QR codes for Power Apps mobile *(alt text)*), `07-app-home-page.svg`, `07-app-info-page.svg` (embedded raster, Contoso Expense Mobile App).

### 2.Q Data management (end-user view only)

Data entities, data projects, import and export jobs, packages and the **Data management** workspace are administrator tools ([WDM-2](https://learn.microsoft.com/en-us/training/modules/work-data-management-finance-operations/2-concepts), [WDM-4](https://learn.microsoft.com/en-us/training/modules/work-data-management-finance-operations/4-workspace), [CYD-2](https://learn.microsoft.com/en-us/training/modules/configure-your-data-dynamics-365-finance-operations-apps/create-entities)). The only user-facing link is that data entities power **Open in Excel**. Entity categories (Parameters, Reference, Master, Document, Transactions) are a useful vocabulary for "master data versus transactions" ([WDM-3](https://learn.microsoft.com/en-us/training/modules/work-data-management-finance-operations/3-integration)).
- `learn-modules/implement-common-integration-features-finance-ops/media/09-data-management.svg`: Data management workspace tiles (Import, Export, Templates, Data entities, Framework parameters, Dual-write...).

### 2.R Finance concepts

#### R1. The general ledger, subledgers and modules

The general ledger is the core of the ERP. Purchasing, sales, projects, AP, AR, bank and fixed assets all post into it. Finance's modules are:
- General ledger.
- Cash and bank management.
- Tax.
- Accounts payable and Accounts receivable, with Credit and collections.
- Budgeting, Fixed assets, Cost accounting, Expense management, Consolidations.
- Asset leasing and Subscription billing.
- Electronic invoicing and Regulatory features (which depend on the country of the active company).

Sources: [DFO-2](https://learn.microsoft.com/en-us/training/modules/describe-finance-operations-apps/2-describe-enterprise-resource-planning-erp), [GSF-3](https://learn.microsoft.com/en-us/training/modules/get-started-financial-management-dyn365-finance/3-overview) to [GSF-13](https://learn.microsoft.com/en-us/training/modules/get-started-financial-management-dyn365-finance/12-0-electronic-invoicing), [DFC-2](https://learn.microsoft.com/en-us/training/modules/describe-dynamics-365-finance-core-capabilities/2-describe-finance-capabilities-features).

**Subledgers keep their own balances** (vendor, customer and bank). Each posting is transferred to the GL, normally asynchronously and near real time, or in a scheduled batch. So a subledger posting can take a short time to show in the GL. Entries that fail to transfer appear in General ledger > Periodic tasks > **Subledger journal entries not yet transferred** ([CLJ-11](https://learn.microsoft.com/en-us/training/modules/configure-ledgers-journals-dyn365-finance/set-up-batch-transfer-rules)).

Screenshots:
- `learn-modules/describe-finance-operations-apps/media/02-01-general-ledger-core-01.png`: GL at the centre of Procurement, Sales, SCM, Project accounting and AP.
- `learn-modules/describe-finance-operations-apps/media/02-01-what-is-erp-01.png`: ERP hub diagram.
- `learn-modules/get-started-financial-management-dyn365-finance/media/03-financial-management-overall-process.png`, `03-accounts-payable-integration.png`, `03-accounts-receivable-integration-2.png`, `04-gl1.png`: process diagrams *(alt text)*.
- `learn-modules/describe-dynamics-365-finance-core-capabilities/media/02-04-finance-modules-01.png`: map of Finance capabilities *(alt text)*.
- `learn-modules/get-started-financial-management-dyn365-finance/media/07-accounts-payable.png`, `08-accounts-receivable.png`: AP and AR module menus *(alt text)*.
- `learn-modules/configure-ledgers-journals-dyn365-finance/media/11-entry-that-did-not-transfer-ss.svg`: Subledger journal entries not yet transferred (Product receipt, Not transferred).

#### R2. Chart of accounts and main accounts

The chart of accounts is the list of main accounts. It can be shared by several companies (the quiz tests this), and each company has one ledger. Main account types: **Profit and loss**, **Revenue**, **Expense**, **Balance sheet**, **Asset**, **Liability**, **Equity**, **Total**. Main account categories feed the default financial reports. Main accounts can have **DB/CR default** and **DB/CR requirement** settings, and can be **balance control accounts**, whose expected balance you can check before posting ([GLD-2](https://learn.microsoft.com/en-us/training/modules/general-ledger-daily-procedures-dyn365-finance/2-balance-control-accounts)). Sources: [DGL-3](https://learn.microsoft.com/en-us/training/modules/describe-general-ledger-cash-bank-management/3-describe-chart-accounts-functionality), [EGL-2](https://learn.microsoft.com/en-us/training/modules/explore-general-ledger-dynamics-365/2-explore-chart-accounts-functionality), [CLJ-4](https://learn.microsoft.com/en-us/training/modules/configure-ledgers-journals-dyn365-finance/3-setup).
- `learn-modules/explore-general-ledger-dynamics-365/media/02-02-explore-the-dynamics-365-finance-and-operations-apps-mod-2-1.svg`: Main accounts list (110110 Bank Account - USD, 110180 Petty Cash...).
- `learn-modules/explore-general-ledger-dynamics-365/media/02-02-explore-the-dynamics-365-finance-and-operations-apps-mod-2-2.svg`: Chart of accounts list (country charts such as Brasil, Chinese, French, India...).
- `learn-modules/explore-general-ledger-dynamics-365/media/02-02-explore-the-dynamics-365-finance-and-operations-apps-mod-2-3.svg`: Ledger page (Chart of accounts Shared, Fiscal calendar, Balancing financial dimension, Account structures).
- `learn-modules/describe-general-ledger-cash-bank-management/media/03-5-3-main-accounts.png`, `03-5-3-chart-of-accounts.png`, `03-5-3-balancing.png`: newer PNGs of the same pages *(alt text)*.

#### R3. Fiscal calendar, ledger calendar and period status

A fiscal calendar has years and periods, plus automatic **Opening** and **Closing** periods. Each company has exactly one fiscal calendar, set on the Ledger page. The **Ledger calendar** (General ledger > Calendar > **Ledger calendar**) controls each period's status:
- **Open**: posting allowed.
- **On hold**: no posting; it can be reopened.
- **Permanently closed**: it can never be reopened. DGL advises not to use it except much later.

Access can be restricted for each business area (**Ledger**, **Sales tax**, **Bank**, **Customer**, **Vendor**) to a user group (**Access level**: <All> by default, <None>, or a group). **A journal line dated in a closed or on-hold period gives an error** ([GLD-3](https://learn.microsoft.com/en-us/training/modules/general-ledger-daily-procedures-dyn365-finance/3-process-journal-entry)). **Date intervals** fill in report date ranges automatically ([LE-10](https://learn.microsoft.com/en-us/training/modules/plan-implement-legal-entities-finance-operations/11-configure-calendars)). Sources: [DGL-2](https://learn.microsoft.com/en-us/training/modules/describe-general-ledger-cash-bank-management/2-concept-fiscal-calendar), [EGL-3](https://learn.microsoft.com/en-us/training/modules/explore-general-ledger-dynamics-365/3-concept-fiscal-calendar), [DGL-10](https://learn.microsoft.com/en-us/training/modules/describe-general-ledger-cash-bank-management/10-describe-periodic-financial-processes).

Screenshots:
- `learn-modules/explore-general-ledger-dynamics-365/media/03-02-explore-the-dynamics-365-finance-and-operations-apps-mod-2-4.svg`: Fiscal calendars (New calendar, New year; years 2023 to 2025).
- `learn-modules/explore-general-ledger-dynamics-365/media/03-02-explore-the-dynamics-365-finance-and-operations-apps-mod-2-6.svg`: Create new fiscal year (Fiscal_IN from 01/04).
- `learn-modules/explore-general-ledger-dynamics-365/media/03-02-explore-the-dynamics-365-finance-and-operations-apps-mod-2-7.svg`: Ledger page for INMF (Ledger calendar button).
- `learn-modules/explore-general-ledger-dynamics-365/media/03-02-explore-the-dynamics-365-finance-and-operations-apps-mod-2-8.svg`: **Ledger calendars** (Fiscal_IN 2025, Period 0, Period 1, Period 2...).
- `learn-modules/explore-general-ledger-dynamics-365/media/03-02-explore-the-dynamics-365-finance-and-operations-apps-mod-2-9.svg`: Access level dialog (embedded raster).
- `learn-modules/describe-general-ledger-cash-bank-management/media/02-5-2-ledger-calendar-2.png`, `02-5-2-access-level.png`, `02-5-2-fiscal-calendar.png`, `02-5-2-fiscal-year.png` *(alt text)*.
- `learn-modules/plan-implement-legal-entities-finance-operations/media/10-date-intervals.png`: Date intervals page *(alt text)*.

#### R4. Financial dimensions (what the user meets when entering an account)

**What dimensions are.** Financial dimensions are subaccounts (department, cost center, business unit, customer...) that break down main accounts for reporting without a huge chart of accounts.
- **Custom dimensions** (values kept on the dimension page, at most 30 characters, sometimes with a mask such as CC-###) are shared across companies.
- **Entity-backed dimensions** take their values from records such as customers or projects. Some are company-specific: their values are visible only from that company. An entity-backed value appears only once something references it.

([SFD-2](https://learn.microsoft.com/en-us/training/modules/set-up-financial-dimensions-finance/define-dimensions) to [SFD-4](https://learn.microsoft.com/en-us/training/modules/set-up-financial-dimensions-finance/create-entity-backed), [DGL-4](https://learn.microsoft.com/en-us/training/modules/describe-general-ledger-cash-bank-management/4-describe-financial-dimensions-set-concepts))

**Defaults.** Dimensions default from master records (customer, vendor) and from the journal header (**Financial dimension** tab), the journal name and posting profiles. **Copy values to this dimension on each new [Dimension] created** fills the dimension from the record ID ([SFD-6](https://learn.microsoft.com/en-us/training/modules/set-up-financial-dimensions-finance/default-values), [GLD-3](https://learn.microsoft.com/en-us/training/modules/general-ledger-daily-procedures-dyn365-finance/3-process-journal-entry), [GLD-4](https://learn.microsoft.com/en-us/training/modules/general-ledger-daily-procedures-dyn365-finance/4-gl-processes)).

**Derived dimensions.** Entering a "driving" value fills others, for example cost center 10 gives department 20 and location 30. By default it doesn't overwrite values already entered (unless **Replace existing dimension values with derived values** is set), and **Prevent changes** can lock the derived value. It works only for dimensions shared across companies ([SFD-7](https://learn.microsoft.com/en-us/training/modules/set-up-financial-dimensions-finance/derived-dimensions)).

**Account structures decide the valid combinations and their order.** The main account is always a segment, plus up to 10 dimensions, or up to 16 segments with advanced rules. The segmented entry control shows only allowed values, which "decreases the possibility of an incorrect journal entry". Validation runs when you leave the field. Some segments allow blanks (**Blank values are allowed**). Ledger account strings look like `401100-001-022` (main account-business unit-department) ([SFD-9](https://learn.microsoft.com/en-us/training/modules/set-up-financial-dimensions-finance/define-structure-rules), [DGL-5](https://learn.microsoft.com/en-us/training/modules/describe-general-ledger-cash-bank-management/5-describe-accounting-structure)).

**Retired values** are **Suspended**: hidden from lookups. Some companies rename them, for example "___DONOTUSE" ([SFD-5](https://learn.microsoft.com/en-us/training/modules/set-up-financial-dimensions-finance/activate-delete)).

**Ledger account alias.** A short code you type in the **Account** column. On Tab, it expands to the full account and dimensions, and focus moves to the **Initial focus** segment. An alias can be Shared, for a User group, or for one User ([SFD-10](https://learn.microsoft.com/en-us/training/modules/set-up-financial-dimensions-finance/ledger-account-aliases), [CLJ-8](https://learn.microsoft.com/en-us/training/modules/configure-ledgers-journals-dyn365-finance/4-journals)).

**Financial dimension sets** decide how balances are grouped on the **Trial balance**. You can choose primary and secondary sets ([SFD-8](https://learn.microsoft.com/en-us/training/modules/set-up-financial-dimensions-finance/set-up-templates), [GLD-4](https://learn.microsoft.com/en-us/training/modules/general-ledger-daily-procedures-dyn365-finance/4-gl-processes)). **Financial dimension default templates** split an amount by percentages ([SFD-8](https://learn.microsoft.com/en-us/training/modules/set-up-financial-dimensions-finance/set-up-templates)).

**Financial tags.** Up to 20 free or list fields on accounting entries, for values with little reuse such as PO numbers. Types are Text, List and Custom list. They appear on a **Financial tags** tab in journals, and posted tags can be changed with **Edit voucher** ([DGL-4](https://learn.microsoft.com/en-us/training/modules/describe-general-ledger-cash-bank-management/4-describe-financial-dimensions-set-concepts), [SFD-2](https://learn.microsoft.com/en-us/training/modules/set-up-financial-dimensions-finance/define-dimensions)).

Screenshots:
- `learn-modules/set-up-financial-dimensions-finance/media/02-financial-dimension.png`, `02-create-financial-dimension.png`, `02-dimension-values.png`: Financial dimensions page, **Use values from**, Dimension values *(alt text)*.
- `learn-modules/set-up-financial-dimensions-finance/media/03-custom-dimension.svg`: a custom dimension (Cashflow_CN; Dimension value mask; Copy values... No).
- `learn-modules/set-up-financial-dimensions-finance/media/07-derived-dimension.png`: Derived dimensions tab *(alt text)*.
- `learn-modules/set-up-financial-dimensions-finance/media/09-account-structure.png`, `09-advanced-rule-structure.png`, `09-activate-account-structure.png` *(alt text)*.
- `learn-modules/explore-general-ledger-dynamics-365/media/05-02-explore-the-dynamics-365-finance-and-operations-apps-mod-2-13.svg`: account structure grid (Manufacturing P&L; Segments and allowed values; Validate; Add segment).
- `learn-modules/explore-general-ledger-dynamics-365/media/05-02-explore-the-dynamics-365-finance-and-operations-apps-mod-2-14.svg`: operator list (is, begins with, ends with, is between and includes, is like...).
- `learn-modules/set-up-financial-dimensions-finance/media/10-ledger-account-alias.png`, `10-enter-alias-general-journal.png`, `10-alias-replaced-account.png`: alias setup, typing the alias, and the alias replaced by the full account *(alt text)*. **Good end-user sequence.**
- `learn-modules/explore-general-ledger-dynamics-365/media/04-02-explore-the-dynamics-365-finance-and-operations-apps-mod-2-10.svg` (Financial dimension sets: MA+BU, MA+BU+DEPT...) and `learn-modules/set-up-financial-dimensions-finance/media/08-dimension-set.png`.
- `learn-modules/describe-general-ledger-cash-bank-management/media/04-5-4-tags.png`, `04-5-4-general-ledger.png`, `04-5-4-voucher.png`; `learn-modules/explore-general-ledger-dynamics-365/media/04-financial-tags.png`, `04-journals-header.png`, `04-journals-lines.png`: financial tags setup, journal header and lines *(alt text)*.

#### R5. Journals: the way every manual posting is entered

**Principles.** Every manual posting goes through a journal. Lines aren't posted until you post. You can leave a journal and come back. Posted transactions can't be deleted or changed: you reverse them or correct them ([GLD-1](https://learn.microsoft.com/en-us/training/modules/general-ledger-daily-procedures-dyn365-finance/1-introduction), [GLD-3](https://learn.microsoft.com/en-us/training/modules/general-ledger-daily-procedures-dyn365-finance/3-process-journal-entry), [CLJ-8](https://learn.microsoft.com/en-us/training/modules/configure-ledgers-journals-dyn365-finance/4-journals), [CLJ-9](https://learn.microsoft.com/en-us/training/modules/configure-ledgers-journals-dyn365-finance/journal-lines-excel)).

**Journal names.** Each journal uses a **journal name** set up for a purpose, such as intercompany, accruals or error correction. The journal name sets:
- the journal type (**Daily**, **Periodic**, **Customer payment**, **Vendor invoice recording**, **Approval**, **Invoice register**, **Allocation**, **Budget**...);
- the voucher series and **New voucher** rule;
- approval;
- default offset account, currency and dimensions;
- **journal control** (allowed account types, companies and segment values: a wrong account type gives an error);
- **posting restrictions** (by user group or by user: you can post only your own journals);
- the posting layer;
- **Private for user group**.

The name is locked once the journal header is saved. If you picked the wrong one, change the description to say "don't use", delete the lines, and create a new journal ([CLJ-4](https://learn.microsoft.com/en-us/training/modules/configure-ledgers-journals-dyn365-finance/3-setup), [GLD-3](https://learn.microsoft.com/en-us/training/modules/general-ledger-daily-procedures-dyn365-finance/3-process-journal-entry), [GLD-8](https://learn.microsoft.com/en-us/training/modules/general-ledger-daily-procedures-dyn365-finance/7-journal-controls), [DGL-6](https://learn.microsoft.com/en-us/training/modules/describe-general-ledger-cash-bank-management/6-describe-financial-journals)).

**Common journals**: **General journal**, **Global general journal**, **Periodic journal**, **Allocation**, **Customer payment journal**, **Vendor payment journal**, **Invoice journal** (vendor), **Invoice register** and **Invoice approval journal**, **Fixed asset journal**, **Project expense journal**, **Reporting currency adjustment**, **Check/Payment reversal**, **Deposit slip payment cancellation**, **Elimination**, **Budget** ([DGL-6](https://learn.microsoft.com/en-us/training/modules/describe-general-ledger-cash-bank-management/6-describe-financial-journals), [CLJ-2](https://learn.microsoft.com/en-us/training/modules/configure-ledgers-journals-dyn365-finance/2-types)).

**Entering a general journal** ([GLD-3](https://learn.microsoft.com/en-us/training/modules/general-ledger-daily-procedures-dyn365-finance/3-process-journal-entry), [CLJ-8](https://learn.microsoft.com/en-us/training/modules/configure-ledgers-journals-dyn365-finance/4-journals), exercise [GLD-9](https://learn.microsoft.com/en-us/training/modules/general-ledger-daily-procedures-dyn365-finance/8-exercise)):
1. Open General ledger > Journal entries > **General journals**, or the **New journal** tile in the **General journal processing** workspace.
2. Select **New** and pick the **Name** (the journal name). The **Show** filter on the list shows Open, All or Posted journals.
3. Header tabs:
   - **General**: description, journal name, posting layer, detail level, line limits, reversing entry.
   - **Setup**: account type, amounts include sales tax, exchange rate override.
   - **Blocking**: **Locked by system**, in use by another user, private.
   - **Financial dimension**: default dimensions.
   - History.
4. Select **Lines**. On each line enter at least the **date**, the **account** (with its **account type**: Ledger, Bank, Customer, Vendor, Project or Fixed assets), a **debit or credit** amount and an **offset account** (on the same line or on further lines). The quiz expects all four. A vendor or customer line also posts to its summary account in the GL automatically.
5. Check:
   - **Validate**: checks for errors.
   - **Simulate posting** (on the Validate menu): runs the posting without posting.
   - **Inquiries** > **Balance control**: shows balance-control accounts before and after posting.
6. **Post**. **Post and transfer** posts the good vouchers and moves the vouchers with errors to a new journal. If the journal has approval, **Report as ready** or **Submit** first (2.M).

**Saving effort:**
- **Voucher templates**: **Functions** > **Save voucher template** (**Amount** or **Percent**) and **Select voucher template** ([GLD-7](https://learn.microsoft.com/en-us/training/modules/general-ledger-daily-procedures-dyn365-finance/6-voucher-templates), [GLD-9](https://learn.microsoft.com/en-us/training/modules/general-ledger-daily-procedures-dyn365-finance/8-exercise)).
- **Journal descriptions**: reusable texts with a search name ([CLJ-4](https://learn.microsoft.com/en-us/training/modules/configure-ledgers-journals-dyn365-finance/3-setup)).
- **Periodic journals**: General ledger > Periodic tasks > **Periodic journal**; then in a general journal, **Period journal** > **Retrieve journal** with **To date**, and **Copy or move journal** (Copy or Move) ([CLJ-3](https://learn.microsoft.com/en-us/training/modules/configure-ledgers-journals-dyn365-finance/use-cases)).
- Ledger account aliases (R4) and Excel templates (2.J).
- **Reason codes** (Financial reasons) document why ([CLJ-4](https://learn.microsoft.com/en-us/training/modules/configure-ledgers-journals-dyn365-finance/3-setup)).

**Vouchers.** Posting creates a **voucher**, the posted accounting entry. **New voucher** settings:
- **In connection with balance**: a new voucher number when the lines balance (the most common setting).
- **Manual**.
- **One voucher number only**: can cause problems with settlement, tax and reversal.

**Number allocation at posting** gives a temporary voucher number until you post. **Check for voucher used** (Reject duplicate / Reject duplicates within fiscal year / Accept duplicates / Warn in case of duplicates) controls duplicate voucher numbers ([CLJ-6](https://learn.microsoft.com/en-us/training/modules/configure-ledgers-journals-dyn365-finance/implement-voucher), [CLJ-8](https://learn.microsoft.com/en-us/training/modules/configure-ledgers-journals-dyn365-finance/4-journals)).

**Reversing.** On a posted journal's **Lines**, select **Reverse entire journal**. Choose to keep the original dates or enter a new one (for example when the period is closed), add a comment, then **Reverse**. You can also reverse from the **Voucher transactions** list. This works for Ledger, Customer, Vendor and Fixed asset accounts, but not for Bank or Project, and not for vendor payments (separate process). More than 100 lines run in batch ([CLJ-10](https://learn.microsoft.com/en-us/training/modules/configure-ledgers-journals-dyn365-finance/reverse-journal-posting)).

**Posting several journals.** **Post journals** posts several at once, optionally in batch ([GLD-4](https://learn.microsoft.com/en-us/training/modules/general-ledger-daily-procedures-dyn365-finance/4-gl-processes)).

Screenshots:
- `learn-modules/configure-ledgers-journals-dyn365-finance/media/02-journals.svg`: **General journals** list (journal batch number, Name, Description, Posted, Posted on, Log, In use).
- `learn-modules/general-ledger-daily-procedures-dyn365-finance/media/03-gj-1.svg`: General journals (Payroll - Jan, Feb, Mar).
- `learn-modules/configure-ledgers-journals-dyn365-finance/media/02-journal-entry.svg`: **Journal voucher** lines (New, Delete, Voucher, Financial dimensions, Sales tax, Functions; Bank USMF PAYRL 156,000.00).
- `learn-modules/general-ledger-daily-procedures-dyn365-finance/media/03-journal-2.svg`: journal lines (Deferrals menu; 2015 data).
- `learn-modules/general-ledger-daily-procedures-dyn365-finance/media/04-post-and-transfer.svg`: **Post and transfer** on the journal voucher page.
- `learn-modules/general-ledger-daily-procedures-dyn365-finance/media/02-journal-1.svg`: **Inquiries** > **Balance control** in a journal.
- `learn-modules/general-ledger-daily-procedures-dyn365-finance/media/02-balance-control.svg`: Balance control accounts (112010 Bank drop, 112000 Safe drop, 110180 Petty Cash).
- `learn-modules/explore-general-ledger-dynamics-365/media/06-02-explore-the-dynamics-365-finance-and-operations-apps-mod-2-16.svg`: **Journal names** (Allocation: Approval Active No, Approval workflow No, Voucher series, New voucher In connection with balance, Private for user group).
- `learn-modules/configure-ledgers-journals-dyn365-finance/media/04-journal-control.svg`, `04-posting-restrictions.svg`: journal name control and restriction settings.
- `learn-modules/configure-ledgers-journals-dyn365-finance/media/04-reasons-1.svg`: Financial reasons (ADDR, ADJ General adjustment, ERROR Correction of data entry error, NSF...).
- `learn-modules/configure-ledgers-journals-dyn365-finance/media/03-periodic-journal.png`, `03-period-journal-dialog.png`, `03-general-journal-from-periodic-journal.png`: periodic journal setup, the Retrieve journal dialog, and the resulting lines *(alt text)*.
- `learn-modules/configure-ledgers-journals-dyn365-finance/media/06-in-connection-with-balance.png`, `06-one-voucher.png`, `06-number-allocation-at-posting.png` *(alt text)*.

#### R6. Finding posted entries

Use **Voucher transactions**, **Audit trail**, **Trial balance** (with drill-down) and **Related vouchers**, which links the voucher in the other company for intercompany entries. Range filters use `..`. Each posting creates an audit trail entry with the user and date ([CLJ-8](https://learn.microsoft.com/en-us/training/modules/configure-ledgers-journals-dyn365-finance/4-journals), [ICA-5](https://learn.microsoft.com/en-us/training/modules/intercompany-accounting-dyn365-finance/process-intercompany-vendor-invoices), [ICA-6](https://learn.microsoft.com/en-us/training/modules/intercompany-accounting-dyn365-finance/4-trace-intercompany-entry)). Screenshots in 2.K, plus `learn-modules/intercompany-accounting-dyn365-finance/media/05-related-voucher-list.png` (related vouchers in USSI and USRT *(alt text)*).

#### R7. Settlement

Settlement applies one transaction to another, for example a payment to an invoice. Any transaction type can be settled against any other, and settlement can create transactions (cash discount, revaluation, penny difference, over or underpayment).
- **AR and AP**: **Settle transactions** / **Settle open transactions**; **Automatic settlement** parameter; settlement priority (**Mark by priority**); cross rates for different currencies; reversing a settlement ([DGL-8](https://learn.microsoft.com/en-us/training/modules/describe-general-ledger-cash-bank-management/8-describe-cash-bank-management), [ARD-7](https://learn.microsoft.com/en-us/training/modules/accounts-receivable-daily-procedures-dyn365-finance/5-settle-undo), [DAPAR-5](https://learn.microsoft.com/en-us/training/modules/describe-account-payables-account-receivables/5-describe-vendor-payments-settlements)).
- **Ledger settlement** (General ledger > Periodic tasks > **Ledger settlements**): **Display transactions**, select lines, **Mark selected**, and when the **Marked amount** is 0, **Settle marked transactions**. Use **View settlements** > **Reverse marked transactions** to undo; all lines with the same settlement ID are reversed. Settlement must stay within one fiscal year unless partial settlement is used ([GLD-5](https://learn.microsoft.com/en-us/training/modules/general-ledger-daily-procedures-dyn365-finance/5-ledger-settlements)).

**Time zone note** (ARD-7). An on-hold transaction is released at midnight in the time zone of the user who set the **Release date**, so users in other time zones see a different release time. This is a good illustration of why the User options time zone matters in a multi-country company.

#### R8. Posting profiles

Posting profiles decide which GL accounts a vendor or customer transaction posts to (summary account, payments, prepayments, offsets). They can be set for **All**, for a group, or for an individual account, and the most specific setting wins. The posting profile combined with the line dimensions gives the full account string ([DAPAR-4](https://learn.microsoft.com/en-us/training/modules/describe-account-payables-account-receivables/4-describe-posting-profiles), [DAPAR-6](https://learn.microsoft.com/en-us/training/modules/describe-account-payables-account-receivables/6-describe-core-accounts-receivable-components)). `learn-modules/describe-account-payables-account-receivables/media/04-6-4-posting-profiles.png` *(alt text)*.

#### R9. Currencies and revaluation

Currencies and exchange rates are global (177 standard currencies). Each company has an **accounting currency** (the quiz tests this name) and can have a **reporting currency** (dual currency). A transaction in another currency needs an exchange rate for its date, otherwise it can't be processed. Exchange rate types include Default and Budget. Rates are kept by date, and can be imported from providers. Period-end **foreign currency revaluation** posts unrealized gains and losses; settlement then posts realized ones (worked INR/USD example in DGL-10). Max penny difference settings apply. Sources: [DFC-3](https://learn.microsoft.com/en-us/training/modules/describe-dynamics-365-finance-core-capabilities/3-describe-reporting-currency-accounting-currency), [DGL-10](https://learn.microsoft.com/en-us/training/modules/describe-general-ledger-cash-bank-management/10-describe-periodic-financial-processes), [GLD-4](https://learn.microsoft.com/en-us/training/modules/general-ledger-daily-procedures-dyn365-finance/4-gl-processes).
- `learn-modules/describe-dynamics-365-finance-core-capabilities/media/03-04-currencies-02-new.png`, `03-04-exchange-rate-types-03.png`, `03-04-exchange-rates-04.png` (USD to EUR by date), `03-04-ledger-with-currencies-highlighted-05.png` (Accounting currency and Reporting currency on the Ledger page) *(alt text)*.
- `learn-modules/explore-general-ledger-dynamics-365/media/07-02-explore-the-dynamics-365-finance-and-operations-apps-mod-2-18.svg`: Currency revaluation posting profile (GL, AP, AR, Bank tabs).

#### R10. Tax concepts for users

**Sales tax** is calculated from the codes that are in **both** the **sales tax group** (from the customer, vendor or line) and the **item sales tax group** (from the item, procurement category or line). Every taxed transaction needs both. Journals can carry both groups. Other topics: settlement periods, **Settle and post sales tax**, reporting codes, use tax and recoverable VAT, and withholding tax (only in some countries). Path: Tax > Indirect tax > Sales tax > **Sales tax codes**. Sources: [DFC-4](https://learn.microsoft.com/en-us/training/modules/describe-dynamics-365-finance-core-capabilities/4-describe-tax-capabilities), [GSF-6](https://learn.microsoft.com/en-us/training/modules/get-started-financial-management-dyn365-finance/6-tax). The quiz tests that tax calculation depends on the two groups.
- `learn-modules/get-started-financial-management-dyn365-finance/media/06-tax1.png` (Sales tax codes *(alt text)*), `learn-modules/describe-dynamics-365-finance-core-capabilities/media/04-04-sales-tax-groups-09-new.png`, `04-04-item-sales-tax-groups-10.png`, `04-04-tax-settlement-periods-08.png`, `04-04-sales-tax-reporting-codes-11-new.png` *(alt text)*.

#### R11. Intercompany accounting (one entry, several companies)

Intercompany accounting posts ledger entries between companies, with automatic **Due to** and **Due from** accounts. It is different from intercompany trade, which uses sales and purchase orders. **Setting the Company field on a journal line to another company is the only action needed to trigger it.** D365 then creates a voucher in each company and shows a message with the count. Set **Company** before the account, because each company can have its own chart of accounts. Only company pairs that are set up can post: the setup is in General ledger > Posting setup > **Intercompany accounting**, and the active company decides which is the originator. Dimensions default onto the Due to and Due from lines only for single-line vouchers. Check both sides with **Voucher transactions** > **Related vouchers**, or by switching company. Sources: [ICA-1](https://learn.microsoft.com/en-us/training/modules/intercompany-accounting-dyn365-finance/1-introduction) to [ICA-7](https://learn.microsoft.com/en-us/training/modules/intercompany-accounting-dyn365-finance/5-exercise), [GLD-6](https://learn.microsoft.com/en-us/training/modules/general-ledger-daily-procedures-dyn365-finance/create-templates) (which Excel templates support intercompany), [SCM-14](https://learn.microsoft.com/en-us/training/modules/get-started-supply-chain-management-dyn365-supply-chain-mgmt/12-inter-trade) (trade).
- `learn-modules/intercompany-accounting-dyn365-finance/media/03-intercompany-due-from-due-to-flow.svg`: a clear diagram: "YOU ENTER" a journal in USMF (400 USMF, 600 with Company USSI, offset 1,000) and "FINANCE CREATES AUTOMATICALLY" the Due from and Due to entries.
- `learn-modules/intercompany-accounting-dyn365-finance/media/05-intercompany-invoice-journal-example.png`, `05-intercompany-invoice-voucher.png`, `05-related-voucher-list.png`, `05-related-invoice-voucher.png`: vendor invoice journal with lines for other companies, the voucher, related vouchers, and the generated voucher *(alt text)*.
- `learn-modules/intercompany-accounting-dyn365-finance/media/02-intercompany.svg`: Intercompany accounting setup (originating company demf...).

#### R12. Period close

Period-end steps (optional, per organization):
- settle; post all journals; revalue foreign currency (GL, AP, AR); settle ledger transactions; allocations; reconcile subledgers to the GL; adjustments; journalize;
- consolidate; produce statements;
- set periods to **On hold**.

The **Financial period close** workspace (General ledger > Workspaces) tracks tasks by **closing schedule**: **Past due tasks**, **Today's remaining tasks**, **Today's blocked tasks**, **All remaining tasks**. Depending on access, you see all tasks or only your own. Other topics: year-end close (Opening and Closing transactions), closing sheets, consolidation and eliminations, and the **Account Reconciliation Agent** / **Account reconciliation** workspace. Sources: [DGL-10](https://learn.microsoft.com/en-us/training/modules/describe-general-ledger-cash-bank-management/10-describe-periodic-financial-processes), [EGL-7](https://learn.microsoft.com/en-us/training/modules/explore-general-ledger-dynamics-365/7-explore-periodic-financial-processes), [DFO-3](https://learn.microsoft.com/en-us/training/modules/describe-finance-operations-apps/3-describe-use-cases-ai-tools).
- `learn-modules/explore-general-ledger-dynamics-365/media/07-02-explore-the-dynamics-365-finance-and-operations-apps-mod-2-17.svg`: **Financial period close** (closing Mar2017: 131 Past due tasks, 0 Today's remaining, 0 blocked, 131 All remaining; tabs Tasks and status, Status by company, Status by area).
- `learn-modules/describe-general-ledger-cash-bank-management/media/10-5-10-period-close.png` *(alt text)*; `learn-modules/describe-general-ledger-cash-bank-management/media/10-period-close.png`: simulation landing page.

#### R13. Cash and bank, AP, AR: concepts only

Short descriptions for the guide's "how the streams fit together" part:
- **Cash and bank**: deposit slips, bank reconciliation (Modern bank reconciliation, matching rules), cash flow forecasting, letters of guarantee ([GSF-5](https://learn.microsoft.com/en-us/training/modules/get-started-financial-management-dyn365-finance/5-cash-bank), [DGL-8](https://learn.microsoft.com/en-us/training/modules/describe-general-ledger-cash-bank-management/8-describe-cash-bank-management)).
- **AP**: vendor invoice entry options, two- and three-way matching, payment proposals (**Cash discount**, **Per due date**, **Due date and cash discount**), electronic payments (**Generate payments**) ([GSF-7](https://learn.microsoft.com/en-us/training/modules/get-started-financial-management-dyn365-finance/7-ap), [DAPAR-3](https://learn.microsoft.com/en-us/training/modules/describe-account-payables-account-receivables/3-describe-core-accounts-payable-components), [DAPAR-5](https://learn.microsoft.com/en-us/training/modules/describe-account-payables-account-receivables/5-describe-vendor-payments-settlements), [DFC-6](https://learn.microsoft.com/en-us/training/modules/describe-dynamics-365-finance-core-capabilities/6-describe-electronic-payment-formats)).
- **AR**: sales order invoices versus free text invoices (no item numbers), payment journals, collections, credit management, netting ([GSF-8](https://learn.microsoft.com/en-us/training/modules/get-started-financial-management-dyn365-finance/8-ar), [GSF-9](https://learn.microsoft.com/en-us/training/modules/get-started-financial-management-dyn365-finance/9-credit-collections), [DAPAR-6](https://learn.microsoft.com/en-us/training/modules/describe-account-payables-account-receivables/6-describe-core-accounts-receivable-components) to [DAPAR-9](https://learn.microsoft.com/en-us/training/modules/describe-account-payables-account-receivables/9-describe-collection-process), [ARD-2](https://learn.microsoft.com/en-us/training/modules/accounts-receivable-daily-procedures-dyn365-finance/2-free-text-inv)).

These belong in the stream guides; the Getting Started guide only needs to name them. AR example from ARD-8: a free text invoice, then **Accounts receivable > Payments > Payment journal** > **Enter customer payments** > **Save in journal** > **Lines** > **Validate** > **Post**.

#### R14. Global address book and parties

Every person or organization (customer, vendor, worker, contact, prospect, competitor, applicant) is a **party** in the global address book (Common > Common > **Global address book**). Addresses and contacts are stored once and shared by all of a party's roles, so changing an address updates every role. Creating a customer or vendor creates the party automatically. **Check for duplicates** (Party tab > Maintain) and the **Use match** prompt help avoid duplicates. Sources: [DSF-7](https://learn.microsoft.com/en-us/training/modules/describe-shared-features/7-describe-global-address-book), [GAB-1](https://learn.microsoft.com/en-us/training/modules/plan-config-global-address-book-finance-operations/1-introduction), [GAB-2](https://learn.microsoft.com/en-us/training/modules/plan-config-global-address-book-finance-operations/2-gab-function), [GAB-5](https://learn.microsoft.com/en-us/training/modules/plan-config-global-address-book-finance-operations/4a-exercise).
- `learn-modules/plan-config-global-address-book-finance-operations/media/01-gab-new-party.svg`: Global address book Action Pane (Party tab: Merge records, Check for duplicates, Assign parties, Remove parties; New Customer, Vendor, Worker, Prospect...).
- `learn-modules/describe-shared-features/media/07-03-gab-duplicate-check-17.png`, `07-03-global-address-book-new-options-16.png` *(alt text)*.

### 2.S Security as it affects users

Access is granted through security roles, which are made of duties, privileges and permissions. A user with no role has no access. The roles decide which pages, workspaces, buttons and search results a user sees: "Dynamics automatically hides data, forms, etc., that a user does not have access to." Access can also be limited by company and by data security policies. Segregation-of-duties rules can stop one person, for example, from both creating vendors and paying them. Sources: [DSF-2](https://learn.microsoft.com/en-us/training/modules/describe-shared-features/2-describe-security-capabilities), [CYD-3](https://learn.microsoft.com/en-us/training/modules/configure-your-data-dynamics-365-finance-operations-apps/manage-security), [RS-1](https://learn.microsoft.com/en-us/training/modules/role-security-finance-operations/1-introduction), [NAV-5](https://learn.microsoft.com/en-us/training/modules/navigate-finance-operations/5-searching).
- `learn-modules/describe-shared-features/media/02-03-security-01.png`, `learn-modules/role-security-finance-operations/media/02-hierarchy-1.png`, `learn-modules/configure-your-data-dynamics-365-finance-operations-apps/media/03-m3-l3-p1.png`: role to duty to privilege to permission diagrams *(alt text)*.
- **Repository rule D-083 applies.** The guide must not name roles or ask users about them. It says the manager requests the user's D365 profile, and that missing pages or access issues go to the **BAU Support team**. Microsoft's role names (Accounts payable clerk, Accounting manager...) and the role-assignment screenshots (`10-m2-l10-*`, `02-03-assign-roles-to-user-03.png`, `03-m3-l3-p2..p4.png`) should not be used.

### 2.T Feature management, updates and AI features

- **Feature management** workspace (admins, or users with Feature manager or Feature viewer access). Microsoft adds features in each service update. Features can be Preview, Released, On by default or Mandatory. Users "receive notifications about recommended features" and can "request activation from your administrator". A feature that is turned on is still controlled by security ([FM-1](https://learn.microsoft.com/en-us/training/modules/feature-management-finance-operations/01-introduction), [FM-2](https://learn.microsoft.com/en-us/training/modules/feature-management-finance-operations/02-workspace), [FM-3](https://learn.microsoft.com/en-us/training/modules/feature-management-finance-operations/03-feature-states), [FM-10](https://learn.microsoft.com/en-us/training/modules/feature-management-finance-operations/10-assign-roles)).
- The user-facing consequences are that screens can change after an update, and **feature callouts** (pop-ups about new features) appear. You can reset callouts in User options > **Personalization** ([ICP-3](https://learn.microsoft.com/en-us/training/modules/introduce-configure-personalization-dynamics-365-finance-operations-apps/explore-personalization-functionality)).
- Features named in the content that change what users see:
  - **Immersive Home**
  - **Extended grid aggregation capabilities** (column totals)
  - **Saved views**, **Saved views for workspaces**
  - **Full-page apps**
  - **Workflow history summary**
  - **Mass reversals for multiple documents**
  - **Automatic split of large financial journals**
  - **Modern bank reconciliation**
  - **Subledger transfer to General Ledger performance optimization**
  - **Improve cards payment processing flow**
  - **User security governance**
- **AI and Copilot**: the Copilot sidecar, Summary by Copilot FastTabs, Immersive Home, Finance agents (collections in Outlook, financial reconciliation in Excel, Account Reconciliation Agent), and Finance insights. All are marked "AI-generated content may be incorrect" ([DFO-3](https://learn.microsoft.com/en-us/training/modules/describe-finance-operations-apps/3-describe-use-cases-ai-tools), [DGL-8](https://learn.microsoft.com/en-us/training/modules/describe-general-ledger-cash-bank-management/8-describe-cash-bank-management), [DAPAR-3](https://learn.microsoft.com/en-us/training/modules/describe-account-payables-account-receivables/3-describe-core-accounts-payable-components)). Whether these are licensed and turned on in our environment is unknown: this is a question for the PG owner.
- `learn-modules/feature-management-finance-operations/media/02-feature-tabs-ss.png`: Feature management header ("Do not enable new features automatically"; New 45, Not enabled 498), tabs **New**, **Not enabled**, **Scheduled**, **All**, and the feature list with Status and Enable date.

### 2.U What Microsoft tests (knowledge checks)

The questions were extracted from the quiz HTML into `tools-f/quizzes.md`. These are the ones relevant to end users. They show what Microsoft considers essential.
- **Navigation** (NAV quiz):
  - The Filter pane is the inline multi-criteria pane (the question says it "slides in from the right").
  - Search results show the **navigation path and the page title**.
  - List pages open in **View mode**.
  - **Grid view** updates several records at once.
- **ICP quiz**: menus are Recent and Workspaces (not "Bookmarks"); you **can** change legal entity after signing in; **Language** is in User options.
- **CUI quiz**: sorting on several fields needs **Advanced sort**; reports can have fields added without code.
- **PER quiz**: reorder fields with the **Move** tool; the **Company accounts template** is shared with the legal entity.
- **DFO quiz**: the GL is the core of the ERP; the Copilot sidecar gives AI-driven help; Immersive Home is the AI-first landing page; workspaces are personalized work centres.
- **DSF quiz**: a duty is a business process made up of privileges; use workflow when review or approval by several users is needed; number sequences give unique IDs; the global address book stores parties.
- **WF quiz**: a task assignee can't **Approve**; the Customer free text invoice workflow suits invoices with no items; a purchase requisition review suits a department buying computers.
- **BAT quiz**: **Copy batch job** creates the same job for other companies; alert options are Ended, Error and Canceled (**not** "Complete").
- **GLD quiz**: the **Blocking** tab makes a journal private; a journal entry needs accounting date, ledger account, debit or credit, and offset account.
- **CLJ quiz**: Customer bank remittance creates a bank file; one chart of accounts can serve several companies; the **Dimension statement** shows transactions by day, account, dimension and period.
- **DFC quiz**: sales tax is set by sales tax groups plus item sales tax groups; the company's primary currency is the **accounting currency**.
- **DRI quiz**: **inquiry pages** give grid views to export to Excel; Business document management edits templates in Word or Excel.
- **ICA quiz**: Due to and Due from accounts are **Balance sheet** type; one three-line intercompany voucher posts **two vouchers, one per company**.
- **DGL quiz**: the ledger calendar controls Open, On hold and Permanently closed; account structures decide valid combinations; it calls Financial reporting "(Management Reporter)".
- **FM quiz**: only a system administrator or a user with the Feature manager role can turn features on or off.
- **SFD quiz**: an account structure must have a main account.

---

## 3. Screenshot catalogue

These are the screenshots worth considering. Decorative images, knowledge-check images, simulation landing pages, developer and admin-setup screens, and diagrams of other apps are left out.

**Look** (whether the image shows the current UI):
- **Current**: opened and checked; shows the current dark navy navigation bar.
- **SVG-2024**: vector capture whose embedded labels and dates (2024) show the current UI.
- **Older**: opened and checked; shows the pre-2021 blue bar or older controls.
- **Unverified**: described from the alt text only.

**Reuse.** Microsoft screenshots use Contoso demo data (USMF and so on). Use them for orientation only, or as models for our own captures in our environment. Many SVGs are 0.3 to 2 MB each and would need converting to PNG for Word.

All paths start with `learn-modules/`.

| Path | Module / unit | What it shows | Look | Candidate use in the guide |
|---|---|---|---|---|
| `personalize-finance-operations/media/04-user-interface-01.png` | PER-4 | A customer page with every UI area labelled (navigation bar, Action Pane, tab, company picker, navigation pane, filter pane, navigation list, page, FactBox, FactBox pane, pane) | Current | **Key concept: parts of the screen.** Best single image to recreate with our data. |
| `describe-finance-operations-apps/media/04-01-navigation-bar-04.png` | DFO-4 | Navigation bar with callouts: Office 365 waffle, Search for a page, Company picker, Copilot, Action center, Settings | Current | Navigation bar topic. |
| `describe-finance-operations-apps/media/04-01-navigation-pane-03.png` | DFO-4 | Navigation pane: Home, Favorites, Recent, Workspaces, Modules, pin | Current | Navigation pane topic. |
| `navigate-finance-operations/media/02-main-dashboard-1.svg` | NAV-2 | Dashboard: banner, calendar, Work items assigned to me, To-do list, tiles | SVG-2024 | Dashboard / Home topic. |
| `navigate-finance-operations/media/02-ar-customers.svg` | NAV-2 | Navigation pane open on a module's page list over the dashboard | SVG-2024 | Opening a page from Modules. |
| `navigate-finance-operations/media/02-tile.png` | NAV-2 | Bank management and Benefits tiles | Unverified | Tiles. |
| `describe-finance-operations-apps/media/03-01-immersive-home-02.png` | DFO-3 | Immersive Home: greeting, work item cards (Approve / Reject / Return), ranked Workspaces | Current | Only if Immersive Home is turned on for us. |
| `introduce-configure-personalization-dynamics-365-finance-operations-apps/media/02-m1-l2-p1.png` | ICP-2 | 2020 dashboard (banner, calendar, tiles) | Older | Not for use (outdated). |
| `introduce-configure-personalization-dynamics-365-finance-operations-apps/media/02-m1-l2-p3.png` | ICP-2 | Company picker list open (RUMF ... USMF, USP2) | Older | Switching company, as a model for our own capture. |
| `introduce-configure-personalization-dynamics-365-finance-operations-apps/media/03-m1-l2-p4.png`, `03-m1-l2-p5.png` | ICP-3 | Gear > User options; Preferences > Startup > Company | Unverified | Setting the default company. |
| `introduce-configure-personalization-dynamics-365-finance-operations-apps/media/05-m1-l5-p2.png` to `p5.png` | ICP-5 | Show navigation pane > Favorites (empty) > All customers star > Favorites list | Unverified | Favorites step sequence. |
| `configure-your-ui-dynamics-365-finance-operations-apps/media/09-m2-l9-p1.png` | CUI-9 | A Favorites menu with four items | Unverified | Result of adding favorites. |
| `navigate-finance-operations/media/05-search-le.png` | NAV-5 | Search "project": 10 results, each with its path | Older (blue banner) | Search topic (shows title plus path). |
| `navigate-finance-operations/media/05-search-vi.png` | NAV-5 | "form: vendinvoice" results | Unverified | Not needed (technical). |
| `describe-finance-operations-apps/media/04-01-search-bar-results-06.png` | DFO-4 | Search results for "Customer" | Unverified | Search topic (likely current). |
| `navigate-finance-operations/media/02-customer-payments-workspace.svg` | NAV-2 | Customer payments workspace tiles and lists | SVG-2024 | Workspace anatomy (O2C example). |
| `navigate-finance-operations/media/03-workspace-2.svg` | NAV-3 | Customer invoicing workspace (Summary tiles, Filter, tabs, Links) | SVG-2024 | Workspace anatomy. |
| `general-ledger-daily-procedures-dyn365-finance/media/03-general-journal-processing.svg` | GLD-3 | General journal processing workspace (New journal; My/All not posted counters) | SVG-2024 | R2R workspace example; creating a journal. |
| `get-started-financial-management-dyn365-finance/media/05-bank-management.svg` | GSF-5 | Bank management workspace | SVG-2024 | Cash workspace example. |
| `get-started-financial-management-dyn365-finance/media/09-credits-and-collections.svg` | GSF-9 | Customer credit and collections workspace tiles | SVG-2024 | O2C workspace example. |
| `implement-common-integration-features-finance-ops/media/07-power-bi-connector.svg` | ICI-7 | Vendor payments workspace tiles | SVG-2024 | P2P workspace example. |
| `describe-report-integration/media/02-2-2-analytics-workspace.png` | DRI-2 | Fixed asset management, Analytics - all companies (Power BI) | Unverified | Analytics tab in workspaces. |
| `describe-finance-operations-apps/media/04-01-action-pane-11.png` | DFO-4 | Customer Action Pane, Collect tab with grouped buttons | Current | Action Pane and tabs. |
| `personalize-finance-operations/media/09-add-2-ws.svg` | PER-9 | Options tab: Personalize group (Add to workspace...) and Page options (Advanced filter or sort, Record info) | SVG-2024 | Options tab; Add to workspace. |
| `personalize-finance-operations/media/10-dashboard-1.svg` | PER-10 | Bank accounts Options menu: Get a link, Create a custom alert, Manage my alerts | SVG-2024 | Alerts (the file name and alt text are misleading). |
| `describe-finance-operations-apps/media/04-01-filter-pane-12.png` | DFO-4 | Filters pane (+ Add, Apply, Reset), funnel icon highlighted at the right edge | Current | Filter pane, after checking which side it opens in our version. |
| `navigate-finance-operations/media/04-filtering.svg` | NAV-4 | All sales orders with the Filter pane (1) and a column filter (2) | SVG-2024 | Filtering overview. |
| `describe-finance-operations-apps/media/04-01-grid-sort-13.png` | DFO-4 | Column header: Sort A to Z / Z to A, begins with, Apply, Clear | Current | Column filter and sort. |
| `describe-finance-operations-apps/media/04-01-quick-filter-12.png` | DFO-4 | QuickFilter above a grid | Unverified | QuickFilter. |
| `describe-finance-operations-apps/media/04-01-query-filter-14.png`, `04-01-query-sort-15.png`, `04-01-query-add-join-16.png` | DFO-4 | Advanced filter or sort: Range, Sorting, Joins | Unverified | Advanced filter (power-user box). |
| `configure-your-ui-dynamics-365-finance-operations-apps/media/06-m2-l6-p2.png` | CUI-6 | Filter operator list | Older | Model for an operator table. |
| `configure-your-ui-dynamics-365-finance-operations-apps/media/05-m2-l5-p1.png` | CUI-5 | Grid header menu: Export all rows, Export marked rows, Hide this column, Add columns, View shortcuts | Older | Grid menu (recapture). |
| `configure-your-ui-dynamics-365-finance-operations-apps/media/05-m2-l5-p2.png` | CUI-5 | Insert or Add columns dialog | Unverified | Adding a column. |
| `personalize-finance-operations/media/04-total-this-column-ss.svg` | PER-4 | Grid with column totals (Open prepayments) | SVG-2024 | Column totals (if the feature is on). |
| `personalize-finance-operations/media/04-freeze-column.gif` | PER-4 | Animation: freeze and unfreeze a column | Unverified (21 MB) | Not usable in Word; recapture a still. |
| `introduce-configure-personalization-dynamics-365-finance-operations-apps/media/03-m1-l3-p1.png` | ICP-3 | Field Personalize pop-up (Hide, Include in FastTab summary, Skip in Tab key sequence) | Older | Personalizing a field. |
| `personalize-finance-operations/media/08-personalization_toolbar-ss.png` | PER-8 | Personalization toolbar (Select, Hide, Require, Add a field, Move, Skip, Show in header, Lock, ..., Close) | Current | Personalization toolbar. |
| `personalize-finance-operations/media/10-toolbar.svg` | PER-10 | Toolbar active on the Bank management workspace | SVG-2024 | Personalizing a workspace. |
| `personalize-finance-operations/media/07-save-view-ss.png` | PER-7 | Publish view to others dialog (roles, legal entity access) | Current | Not for end users (admin publish). |
| `configure-your-ui-dynamics-365-finance-operations-apps/media/06-m2-l6-p5.png`, `11-m2-l11-p4.png` | CUI-6/11 | Saving a filtered query as a view; the view list | Unverified | Saved views (recapture the view selector and Save as). |
| `describe-finance-operations-apps/media/04-01-user-options-08.png` | DFO-4 | User options > Preferences (Startup, Language and region, Misc, Accessibility, Task management) | Current | **User options topic.** |
| `personalize-finance-operations/media/03-preferences-1.svg` | PER-3 | Same tab as SVG | SVG-2024 | Alternative to the above. |
| `describe-shared-features/media/08-03-user-options-21.png` | DSF-8 | User options > Workflow: Notifications, Delegation grid | Current | Notifications and delegation. |
| `describe-finance-operations-apps/media/04-01-color-picker-07.png` | DFO-4 | Visual tab (colour and size) | Unverified | Optional. |
| `configure-your-ui-dynamics-365-finance-operations-apps/media/03-m2-l3-p1.png` | CUI-3 | Initial page options | Unverified | Initial page. |
| `describe-shared-features/media/06-03-save-record-template-14.png` | DSF-6 | Record information: Company accounts template / User template | Current | Record templates. |
| `describe-shared-features/media/06-03-use-record-template-15.png` | DSF-6 | Select a template for dialog | Unverified | Record templates. |
| `describe-shared-features/media/10-03-new-document-25.png` | DSF-10 | Attachments page, New > File / Image / Note / URL | Current | Attachments. |
| `describe-shared-features/media/10-03-upload-document-26.png`, `10-03-view-attachments-27.png` | DSF-10 | Upload dialog; preview pane | Unverified | Attachments. |
| `personalize-finance-operations/media/03-attachment-ss.svg` | PER-3 | All customers with the paperclip icon and count | SVG-2024 | Where the Attach button is. |
| `configure-your-data-dynamics-365-finance-operations-apps/media/07-m3-l7-p1.png` to `p6.png` | CYD-7 | Office icon > Open in Excel / Export to Excel > download > edit > Publish > refreshed list | p2 Current-ish; others Unverified | **Excel topic step sequence.** |
| `describe-report-integration/media/04-2-4-export-to-excel.png` | DRI-4 | Open in Microsoft Office menu with Open in Excel options and Export to Excel | Current | Excel topic. |
| `implement-common-integration-features-finance-ops/media/02-office-3.png` | ICI-2 | Excel with the Data Connector pane | Unverified | Open in Excel (Refresh / Publish). |
| `configure-ledgers-journals-dyn365-finance/media/09-new-office-add-in.png` | CLJ-9 | Trust this add-in prompt | Unverified | First-time Excel add-in. |
| `general-ledger-daily-procedures-dyn365-finance/media/06-general-ledger-template.png` (and the other `06-*-template.png`) | GLD-6 | Excel templates for each journal type | Unverified | Journal entry from Excel (R2R/P2P/O2C guides). |
| `describe-shared-features/media/04-03-run-as-batch-07.png` | DSF-4 | Run in the background (Batch processing, Recurrence, Alerts, Batch group, Private, Critical Job) | Current | **Batch topic.** |
| `setup-batch-jobs-finance-operations/media/03-define-recurrence.png`, `03-alerts-1.png` | BAT-3 | Define recurrence; Batch job alerts | Unverified | Batch recurrence and alerts. |
| `setup-batch-jobs-finance-operations/media/04-copy-batch-job.svg` | BAT-4 | Batch jobs list (status, Run by...) | SVG-2024 | Checking a job, only if users have access. |
| `describe-shared-features/media/08-03-create-alert-rule-20.png` | DSF-8 | Create alert rule dialog (all four sections) | Current | **Alerts topic.** |
| `describe-shared-features/media/03-03-workflow-history-06.png` | DSF-3 | Workflow history with Summary by Copilot and Tracking details | Current | Workflow history. |
| `configure-ledgers-journals-dyn365-finance/media/07-standard-view.svg`, `07-workflow-approval.svg` | CLJ-7 | Journal voucher and journals list (Approval / Workflow context) | SVG-2024 | Submitting a journal for approval. |
| `get-help-finance-operations/media/03-task-guide.png` | HELP-3 | Task guide bubble (Click Invoice; Previous step, Skip this step) | Current | Help and task guides. |
| `feature-management-finance-operations/media/02-feature-tabs-ss.png` | FM-2 | Feature management header and tabs | Current | Optional ("why screens change"). |
| `configure-ledgers-journals-dyn365-finance/media/02-journals.svg` | CLJ-2 | General journals list | SVG-2024 | Journals: list page. |
| `configure-ledgers-journals-dyn365-finance/media/02-journal-entry.svg` | CLJ-2 | Journal voucher lines | SVG-2024 | Journal lines. |
| `general-ledger-daily-procedures-dyn365-finance/media/04-post-and-transfer.svg` | GLD-4 | Post and transfer on the journal voucher | SVG-2024 | Posting options. |
| `general-ledger-daily-procedures-dyn365-finance/media/02-journal-1.svg` | GLD-2 | Inquiries > Balance control in a journal | SVG-2024 | Checks before posting. |
| `general-ledger-daily-procedures-dyn365-finance/media/04-global-general-journals.svg` | GLD-4 | Global general journals across companies | SVG-2024 | Multi-company work. |
| `general-ledger-daily-procedures-dyn365-finance/media/04-trial-balance.svg` | GLD-4 | Trial balance with Parameters | SVG-2024 | Inquiries: Trial balance. |
| `configure-ledgers-journals-dyn365-finance/media/08-voucher-transactions-ss.svg` | CLJ-8 | Voucher transactions with account strings | SVG-2024 | Inquiries; account string. |
| `configure-ledgers-journals-dyn365-finance/media/08-audit-trail-ss.svg` | CLJ-8 | Audit trail (last-seven-days message) | SVG-2024 | Inquiries. |
| `explore-general-ledger-dynamics-365/media/07-02-explore-the-dynamics-365-finance-and-operations-apps-mod-2-20.svg` | EGL-7 | Financial reports list (Generate, New, Edit) | SVG-2024 | Financial reports. |
| `explore-general-ledger-dynamics-365/media/07-02-explore-the-dynamics-365-finance-and-operations-apps-mod-2-21.svg` | EGL-7 | Generated reports with Expiration | SVG-2024 | Financial reports. |
| `work-analytics-reporting-finance-operations/media/04-inq-rep.png` | WAR-4 | GL Inquiries and reports menu | Unverified | Where to find reports. |
| `explore-general-ledger-dynamics-365/media/03-02-explore-the-dynamics-365-finance-and-operations-apps-mod-2-8.svg` | EGL-3 | Ledger calendar periods and status | SVG-2024 | Period status concept. |
| `explore-general-ledger-dynamics-365/media/02-02-explore-the-dynamics-365-finance-and-operations-apps-mod-2-1.svg` | EGL-2 | Main accounts list | SVG-2024 | Chart of accounts concept. |
| `explore-general-ledger-dynamics-365/media/05-02-explore-the-dynamics-365-finance-and-operations-apps-mod-2-13.svg` | EGL-5 | Account structure segments and allowed values | SVG-2024 | Why some combinations are refused (concept, optional). |
| `explore-general-ledger-dynamics-365/media/04-02-explore-the-dynamics-365-finance-and-operations-apps-mod-2-10.svg` | EGL-4 | Financial dimension sets | SVG-2024 | Trial balance by dimension set. |
| `set-up-financial-dimensions-finance/media/10-enter-alias-general-journal.png`, `10-alias-replaced-account.png` | SFD-10 | Typing a ledger account alias; the expanded account | Unverified | Entering accounts quickly (if aliases are used). |
| `set-up-financial-dimensions-finance/media/02-dimension-values.png` | SFD-2 | Financial dimension values | Unverified | Dimensions concept. |
| `describe-general-ledger-cash-bank-management/media/04-5-4-voucher.png` | DGL-4 | Financial tags on journal lines | Unverified | Only if tags are used. |
| `intercompany-accounting-dyn365-finance/media/03-intercompany-due-from-due-to-flow.svg` | ICA-3 | Diagram: you enter one journal, Finance creates the Due to and Due from vouchers | Current (diagram) | **Intercompany concept** for the multi-entity company. |
| `intercompany-accounting-dyn365-finance/media/05-related-voucher-list.png` | ICA-5 | Related vouchers in other companies | Unverified | Tracing an intercompany entry. |
| `intercompany-accounting-dyn365-finance/media/05-intercompany-invoice-journal-example.png` | ICA-5 | Invoice journal with Company column per line | Unverified | Intercompany entry. |
| `describe-finance-operations-apps/media/02-01-general-ledger-core-01.png` | DFO-2 | GL at the core of the modules | Diagram | How the streams connect. |
| `get-started-financial-management-dyn365-finance/media/03-financial-management-overall-process.png` | GSF-3 | Financial management overall process | Unverified diagram | How the streams connect. |
| `describe-dynamics-365-finance-core-capabilities/media/03-04-ledger-with-currencies-highlighted-05.png` | DFC-3 | Ledger page: accounting and reporting currency | Unverified | Currency concept (optional). |
| `describe-account-payables-account-receivables/media/03-6-3-copilot.png` | DAPAR-3 | All vendors with Summary by Copilot | Unverified | AI features (if enabled). |
| `plan-config-global-address-book-finance-operations/media/01-gab-new-party.svg` | GAB-1 | Global address book Party tab | SVG-2024 | Party concept (optional). |
| `get-started-financial-management-dyn365-finance/media/14-workspaces-ss.png`, `14-modules-icon-ss.png` | GSF-14 | Home page tile; Modules icon | Unverified | "Explore" exercise. |

---

## 4. Conflicts, inconsistencies and outdated content

### 4.1 Conflicts between modules (or within one module)

| # | Topic | What the sources say | Note for the guide |
|---|---|---|---|
| C1 | **Side the Filter pane opens** | NAV-4 and the NAV quiz: **Show filters** is on the right and the pane "slides in from the right". DFO-4: the pane "slides in from the left", but the icon is in the right-most pane and the pane "appears on the right side" (contradicts itself). CUI-6: slides in from the **left**. Image PER `04-user-interface-01.png`: filter pane and funnel on the left of the page. Image DFO `04-01-filter-pane-12.png`: funnel at the right edge. | Check in our environment during the clean-session test and describe the icon, not the side. |
| C2 | **Posting layers** | DGL-3 and EGL-2: three layers (Current, Operations, Tax). CLJ-4 and CLJ-5: **10** layers (Current, Operations, Tax, Custom 1 to 7) plus **None**. | CLJ is newer and correct. Users rarely need this. |
| C3 | **Insert or Add columns** | CUI-5 text: **Insert columns**. CUI image, PER-5 and DRI-4: **Add columns**. | Check the current label. |
| C4 | **Column totals** | PER-4 text: **View column totals**. Its image alt text: "Total this column". | Check the label. It needs the Extended grid aggregation feature. |
| C5 | **Location of the Attach button** | DSF-10, PER-3 and ICI-4: top right / upper-right. DRI-4: "upper-left corner". | Top right of the page icons. |
| C6 | **Document templates path** | DRI-4, ICI-3 and ICI-4: **Common > Common > Office integration > Document templates**. CLJ-9: **Organization administration > Setup > Office integration > Document templates**. | Admin path; not needed by users. |
| C7 | **Turning on document handling** | PER-3 and ICP-3: User options > Preferences > **Enable document handling** (Miscellaneous). ICI-4: "Common > Setup > User options > Preferences > Miscellaneous ... **Document handling active**". | ICI-4 uses an old path and label. Use Settings > User options. |
| C8 | **Email providers** | CYD-4 (2026-09): **Microsoft Graph** is the recommended provider and **replaces the deprecated Exchange provider**. DRI-4 and ICI-5 still describe "Use Exchange email server" and SMTP. The system email client is labelled "Use the system email client" (DRI-4) or "Use the Microsoft finance and operations apps email client" (ICI-5). | Check which options our users see. |
| C9 | **Priority-based batch scheduling** | BAT-2 and BAT-3: turn it on in Feature management. DSF-4: "This feature is now mandatory." | Admin only. DSF is newer. |
| C10 | **Prospect party role** | GAB-1: "a party that might provide a service or benefit to a legal entity". DSF-7: "a potential customer". | DSF wording is the usual meaning. |
| C11 | **Ledger page path** | DGL-2, DGL-3 and DGL-10: General ledger > **Ledger setup** > Ledger. DGL-5 and DFC-3: General ledger > **Setup** > Ledger. | Ledger setup > Ledger. Setup page, users don't need it. |
| C12 | **User groups path** | DGL-2 and EGL-3: "System administration > **User menu** > User groups", which doesn't match the usual System administration > Users > User groups. | Admin path; not needed. |
| C13 | **Name of the GL workspace** | CLJ-1 uses both "General ledger processing workspace" and "**General journal processing**" (the second matches the screenshot). | Use General journal processing. |
| C14 | **Account structure segments** | DGL-5: "maximum of 10 dimensions as a segment" and the main account is "mandatory". SFD-9: 11 segments (main account + 10), main account required but not necessarily first, up to 16 with advanced rules. | Consistent once read together. Not end-user content. |
| C15 | **Financial dimension sets wording** | DGL-4: "Use the Financial dimension sets page to create financial dimensions." This is a wording error: the page creates *sets*. | — |
| C16 | **Inventory dimension display path** | PER-11 says General ledger > Ledger setup > General ledger parameters. Its own SVG shows GL parameters > Inventory dimensions tab ("Select inventory dimensions to display on overview"), which is GL-specific. | Not relevant to finance users. |
| C17 | **Saved view image** | PER-7 alt text: "save a new view and publish it". The image is the admin **Publish view to others** dialog. | Don't use it as a picture of "Save as". |
| C18 | **Workflow approval toggles** | CLJ-7 says that for workflow approval both **Approval workflow** and the manual **Active** toggle are turned on. DGL-3 and CLJ-4 say manual and workflow approval can't both be used on one journal name. | Users only see the Approval menu or the Workflow menu. |
| C19 | **Voucher transactions caption** | ICA-4 image caption: "Voucher transactions page in General ledger > Inquiries and reports > **Audit trail**". The page is reached from Inquiries and reports > Voucher transactions, or from Audit trail > Voucher transactions. | Minor. |
| C20 | **Global general journals** | GLD-4: "Use ... Global general journals to assign the security role access to all General journals and all companies" (muddled). DGL-6: you can move between companies without switching. | Use DGL-6's meaning. |
| C21 | **Company ID length** | LE-2: "fixed four-character Company ID". DSF-5: a company ID per legal entity, no length. Demo data includes "us01". | Say "up to four characters" if needed. |

### 4.2 Outdated or AX-era content

| # | Item | Where | Why outdated | Note |
|---|---|---|---|---|
| O1 | Old blue navigation bar, 2020 dashboard, older company picker and grid menus | ICP-2 (`02-m1-l2-p1.png`, `02-m1-l2-p3.png`), CUI images (`05-m2-l5-p1.png`, `06-m2-l6-p2.png`), NAV `05-search-le.png` | The current UI has a dark navy bar, Home in the navigation pane, and a redesigned company picker ("USMF \| Name") | Recapture in our environment. |
| O2 | "Go to Office 365" callout, "Microsoft Office" integration naming | DFO `04-01-navigation-bar-04.png`; DRI-4 title "Office 365" | Now Microsoft 365 | Wording only. |
| O3 | **Power BI content from the LCS Shared asset library** | WAR-6, DGL-7 | Power BI content now comes through embedded analytics, Business performance analytics or Link to Fabric (GSF-4 mentions Business performance analytics). The LCS-download model is legacy. | Don't describe the LCS route. Say "Analytics tabs in workspaces". |
| O4 | Power BI "Get Started" tile catalog (PowerBI.com tiles pinned to workspaces) | ICI-7 | Old PowerBI.com integration | Skip. |
| O5 | ClickOnce desktop tools: Workflow editor (`Microsoft.Dynamics.AX.Framework.WorkflowEditorHost`), Report Designer (`ReportDesigner.application`, host `usnconeboxax1aos`) | WF-3, WF-6, WAR-7 | AX-era ClickOnce names. Designers only. | Out of scope for users. |
| O6 | **Fleet Management sample module** and demo data | ICI-10, LE-4 (Branch / Rental Location / Region operating units), ERT-5, RS-7 | The Fleet Management sample was removed from current versions | Ignore. |
| O7 | Document Routing Agent `Microsoft.Dynamics.AX.Framework.DocumentRouting.Agent.exe`, "needs Adobe Acrobat Reader" | ICI-8 | AX-era naming; the Reader requirement is dated (an embedded PDF viewer now exists) | IT set-up; users just pick a printer. |
| O8 | **Regulatory Configuration Services (RCS)** | ICI-8 | Replaced by Globalization Studio (named in DRI-7 and GSF-13) | Admin. |
| O9 | "Prospect to Cash" Data Integrator templates | ICI-9 | Replaced by dual-write | Admin. |
| O10 | The old "Finance and operations (Dynamics 365)" mobile app | MOB-9 links the 2022 deprecation notice | Deprecated; mobile is now Power Apps | The guide shouldn't mention a mobile app unless we have one. |
| O11 | "Monthly release cycles" / "monthly updates" | FM-2 | Microsoft now ships a smaller number of service updates a year | Wording only. |
| O12 | **Lifecycle Services (LCS)**, BPM, task guide libraries in LCS | HELP-1, HELP-3, DFO-4 (task recorder save to LCS), UAT | LCS is being phased out in favour of the Power Platform admin center (RS-6 already uses it for licensing) | Don't send users to LCS. |
| O13 | "Management Reporter" | DGL quiz Q3 | Old name of Financial reporting | Use **Financial reporting**. |
| O14 | AX terms: AOT, AOS, "AX enum provider", X++, Infolog | DRI-2, ERT-2, DSF-2, ICA-3 | Developer vocabulary, but "Infolog" (message bar) still appears in user-facing text | Say "message bar" in the guide. |
| O15 | Old demo dates (2014 to 2017 jobs; fiscal 2016; exercise dates 2023) | BAT SVGs, WAR-7 (Base year 2016), PER-13 (delegation 09/2023), CLJ-3 | Cosmetic | — |
| O16 | **Financial dimension service** | SFD-2 | Microsoft says it is deprecated from 10.0.49 (11 September 2026), replaced by Optimized Financial dimensions | Admin; no user effect. |
| O17 | "Synchronous" subledger transfer | CLJ-11 | No longer supported (the module says so) | — |
| O18 | Explore-general-ledger module | EGL (ms.date 2025-08-04) | Older duplicate of DGL (2026-01-02) | Prefer DGL text; EGL SVGs are still useful. |
| O19 | `04-freeze-column.gif` (21 MB) | PER-4 | Too large for a Word guide | Recapture a still. |
| O20 | Bulk `ms.date` 2026-03-04 | 12 modules (NAV, PER, BAT, FM, WF, LE, GAB, ICI, MOB, SCM, HELP, WAR) | The date suggests a refresh but the content and images are older (C1, O1, O3) | Treat those modules as "check against the live system". |

### 4.3 Gaps (what Learn doesn't teach but a Getting Started guide may need)

- **Keyboard shortcuts.** Only a few appear: Ctrl+' or Alt+Q (action search), Ctrl+Shift+P (personalization), Ctrl+Shift+? (help), Ctrl+Shift+A (attach), F2 (edit), Shift+F5 (refresh), Ctrl-Shift-F7 (read messages), Tab (alias expansion and maths). There is no full shortcut list; the Grid capabilities article is only linked.
- **Saving a record.** No unit teaches Save explicitly (it appears only in exercise steps). Nor does it teach unsaved-changes prompts, "record in use", or concurrency messages. GLD-3 touches on Blocking > Locked by system.
- **Message types** (info, warning, error bars, the Action center list) are mentioned but not taught.
- **Printing and downloading a report preview**: WAR-5 is conceptual, with no step list.
- **Checking your own batch job** without access to the Batch jobs page: Learn notes that many users lack access but doesn't say what they should use instead.
- **Session time-out, signing out, multiple browser tabs, working in two companies at once** (for example two tabs): not covered.
- **The BAT-8 summary promises "How to unlock a journal"**, but no unit covers it.
- **Copilot / Immersive Home availability** depends on licensing and features; Learn assumes both are on.
- **Work items**: no step list for opening and acting on a work item from the list (WF-5 is a video).

---

## 5. Recommended topics for an end-user Getting Started guide

Ranked by what Learn teaches and what first-day users at a multi-entity finance company need. Each topic lists its main Learn sources.

### Must have

1. **Sign in and the parts of the screen**: navigation bar, navigation pane, Home/dashboard, Action Pane and tabs, FastTabs, FactBoxes, the back arrow, closing a page. Sources: NAV-1/2, DFO-4, PER-4 (labelled screenshot), ICP-2. The orientation every other topic depends on.
2. **Finding a page**: Modules menu, **Search for a page** (finds pages, not data; shows the path), Recent, workspaces from tiles. NAV-5, DFO-4. This is how users get anywhere; Microsoft's quiz tests it.
3. **Switching legal entity and setting the default company**: the company picker, User options > Startup > Company, "data belongs to the company you are in". ICP-2/3, DFO-4, DSF-5, LE-6. Critical in a multi-entity company; the biggest source of "I can't find it" for new users.
4. **Workspaces**: tiles with counts, tabbed lists, links, Analytics; the finance workspaces by stream. NAV-2/3, DFO-4, DAPAR-3/5/6/9, CLJ-1. Users start most work from a workspace.
5. **Lists and records**: View and Edit mode (Edit, Save, refresh), Grid / Details / Header / Lines views, New and Delete. NAV-6/7, PER-3. Basic record handling; Microsoft tests View mode and Grid view.
6. **Filtering and sorting**: QuickFilter, column header filter and sort, Filter pane, operators and `*` / `..` syntax; Advanced filter or sort as a power-user note. NAV-4, DFO-4, CUI-6, CLJ-8, SFD-9. Daily need; the operator list and range syntax are not intuitive.
7. **User options**: language, date/number format, **time zone**, company, initial page, view/edit mode, notifications, delegation. PER-3, ICP-3, DFO-4. Sets up each user correctly; time zone matters for release dates (ARD-7) and batch start times.
8. **Export to Excel and Open in Excel**: static export (Export all rows / marked rows) and Open in Excel with Refresh / Publish, first-time add-in trust. WAR-2, DRI-4, ICI-2, CYD-7, GLD-6, CLJ-9. The most-used finance productivity feature; CYD-7 gives a ready step sequence.
9. **Running reports and inquiries**: Inquiries and reports menus; report dialog > OK and preview / export; **Run in the background** (Batch processing, Recurrence, Alerts) for long reports; Financial reports (Generate, View, drill down, options). WAR-3/4/5/7, BAT-3, DSF-4, DGL-7. Every stream runs reports; the batch option avoids waiting and time-outs.
10. **Help**: field tooltips, the Help pane (Ctrl+Shift+?), task guides (with the "data is real" warning), Copilot if enabled, and **BAU Support** for access issues (D-083). HELP-3, DFO-3. Self-service support; the warning prevents test data in production.
11. **Security in plain words**: what you see depends on your D365 profile; missing pages mean access, not error; contact BAU Support; never name roles (D-083). DSF-2, CYD-3, NAV-5. Avoids confusion and tickets, and is required by the repository rules.

### Should have

12. **Favorites and Recent** (D-084: confirm whether this guide or 260 owns the topic). CUI-2, ICP-5, NAV-2. Quick access to daily pages.
13. **Saved views and simple personalization**: save a filtered list as a view, Pin as default, the asterisk for unsaved changes; hide, add and move columns; reset with Clear. PER-4/5/7/8, CUI-5/11. Big time-saver; also explains why "my screen looks different".
14. **Grid tips**: freeze column, column totals, maths in cells, paste rows from Excel, select rows. PER-4. Finance users live in grids.
15. **Workflow basics for submitters and approvers**: yellow bar, Submit, Approve / Reject / Request change / Delegate, work items on the dashboard, Workflow history, delegation while away. WF-4, DSF-3, CLJ-7, PER-3. Journals, invoices and vendor changes are approved through workflow.
16. **Journals, the shared pattern**: journal names, header and lines, account types, the account and offset with dimensions (segmented entry, defaults, aliases), Validate / Simulate posting / Post, vouchers, reversal not deletion, manual approval (Report as ready). GLD-3/4/7, CLJ-2/4/6/7/8/10, SFD-6/7/9/10, DGL-6. Common to R2R, P2P, O2C and Tax; a Getting Started guide can teach the pattern once and leave the specific journals to the stream guides.
17. **Finance concepts in one page**: GL and subledgers, the transfer delay, chart of accounts, financial dimensions, fiscal periods and period status ("why my date is refused"), vouchers, settlement, posting profiles, accounting versus reporting currency, sales tax group plus item sales tax group. DGL-2..10, DFC-3/4, CLJ-11, GLD-5, DAPAR-4. Gives new users the vocabulary the stream guides assume.
18. **Intercompany basics**: the Company field on a journal line, Due to / Due from, Related vouchers, checking the other company. ICA-3..7. Directly relevant to a multi-entity company, but confirm whether our process uses intercompany journals (a question for the PG owner).
19. **Alerts and the Action center**: Options > Share > Create a custom alert / Manage my alerts; notification settings; best practices. DSF-8. Lets users monitor without checking screens.
20. **Attachments**: the paperclip, New > File / Note, Internal vs External restriction. DSF-10, PER-3. Supporting documents for journals and invoices.

### Nice to have

21. **Add to workspace / personalize the dashboard** (tile with count, list, link; Add a workspace; Pin to dashboard). PER-9/10, BW-3/5. Power-user productivity.
22. **Record templates**: User template and Company accounts template. DSF-6, PER-12. Useful for users who create master data.
23. **Action search** (Ctrl+' / Alt+Q) and a small keyboard shortcut table. NAV-5. Speed for experienced users.
24. **Email from D365** (How would you like to send email; Send email dialog). DRI-4, ICI-5. Statements and documents; depends on our email provider (C8).
25. **AI features**: Copilot sidecar, Summary by Copilot, Immersive Home, Finance agents, with the "may be incorrect" caveat. DFO-3, DAPAR-3/6, DSF-3. Include only if licensed and turned on.
26. **Why screens change**: service updates, feature callouts, Feature management run by IT. FM-1/2, ICP-3. Sets expectations after updates.
27. **Global address book / parties**: one address used everywhere; check for duplicates. DSF-7, GAB-2. Mainly for master-data maintainers.

### Leave out (admin, consultant or developer)

Data management, workflow design, security configuration, batch administration, Feature management actions, number sequence setup, account structure and dimension setup, legal entity and organization hierarchy design, email, printer and SharePoint setup, Power Apps and mobile building, SSRS and report development, UAT and RSAT, and LCS.
