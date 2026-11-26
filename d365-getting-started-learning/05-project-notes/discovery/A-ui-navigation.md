# A. Core user interface and navigation: Microsoft documentation inventory

Discovery research for the **D365 F&O Getting Started** procedure guide. Area: core user interface and navigation.
Researched 26 November 2026 against Microsoft Learn (en-us). All pages were fetched live; the "ms.date" shown for each source is the date Microsoft last revised the page.

Out of scope here (covered by other research areas, mentioned only as cross-references): grids, filtering, personalization and saved views; Excel, export, reports, document handling, batch and alerts; workflow, Help and Copilot features.

Screenshots are saved in `media/ui-navigation/`. Filenames ending in `-training` come from Microsoft Learn training modules, not product docs. They are often newer and labelled.

> **Notes for the guide author (house rules that affect this area)**
> - D-083: several Microsoft pages name security roles and privileges (for example "System User", "View immersive home" privilege, "System Administrator"). The guide must not repeat them. Where access is needed, say the manager requests the D365 profile. For a missing page or control, say contact the **BAU Support team**.
> - D-084: Favorites belongs in 260 O2C Getting Started. Since this is a Getting Started guide, Favorites can be taught here (see section 9).
> - Many Microsoft steps are written for a **system administrator** (for example setting another user's initial page or time zone). The end-user version of the same step is noted where Microsoft gives one.

---

## 1. Names of the user interface elements (the "map" of the screen)

**What it is.** Microsoft's reference list of the names of the parts of the screen. It is the vocabulary a new user needs before following any procedure guide. The same list appears in the Learn training module *Navigate finance and operations apps*.

**Elements as Microsoft names them** (exact wording from the docs):

| Element | Microsoft's description |
|---|---|
| **Navigation bar** | The bar at the top of the interface. It contains the **Dynamics 365 portal**, **Search**, **company picker**, **Action center**, **Settings**, **Help & Support**, and the user profile. |
| **Navigation pane** | The left-most pane. From here, you can find any page in the product. |
| **Action Pane** | The bar beneath the navigation bar. Here, you can select tabs to change records shown in the page. You can edit and save the records here. |
| **Tab** (Action Pane) | A menu of options that appears when you select a given option in the Action Pane. |
| **Page** | The central focus of the interface. Selections made on the other UI components affect what records are shown here. |
| **Navigation list** | On some pages, you scroll through this pane to find a specific record. When selected, the details of the record appear in the page. |
| **Filter pane** | On some pages, select **Show filters** to open this pane and narrow the results. |
| **FactBox** | Shows information and activity for certain records. |
| **FactBox pane** | Where you scroll through the FactBoxes for a record. (In personalization docs this pane is called **Related information**.) |
| **Pane** | The right-most pane. Opens when aspects of a record need to be changed and saved. |

**Other terms on the same page:**
- **Tab**: a selection that opens a different aspect of a record on the same page, usually containing **fields** (UI elements that allow typed input).
- **FastTab**: a tab that lets several tabs be visible at the same time. Expand it with the downward-pointing arrow on its right end.
- **Section**: any area of a page that organizes one category of information (for example "Summary", "Orders and favorites", "Links" on a workspace).
- **Dialog**: a pane that opens to change or create a record. A **drop-down menu** is a field with a downward arrow that lists options. A **drop-down dialog** opens next to the button you selected.
- **Toolbar**: tools such as adding or removing records, often above a **grid** (rows of records with columns of data). A **list** is a collection of records you scroll through.
- **Notifications** appear four ways: **Feature callout**, **Action center**, **Message bar** (beneath the Action Pane), **Message box** (over the interface; must be answered before you continue). See section 18.

**Navigation bar icons, from the labelled training screenshot** (left to right): Microsoft 365 app launcher ("waffle", labelled *Go to Office 365*), app name (*Finance and Operations*), **Search for a page**, **Company picker** (shows e.g. `USMF | Contoso Entertainment Syste...`), **Copilot**, **Action center** (bell), **Settings** (gear), **Help** (?), user initials. The Action Pane below it shows back arrow, **Edit**, **New**, **Delete**, page tabs, **Options**, and the action search magnifier. Right-hand page icons include the Office/attach/refresh/pop-out buttons and, on the far right edge, the Filter and FactBox toggles.

**Key concepts for new users:** navigation bar vs. navigation pane vs. Action Pane (three different bars that new users confuse); FastTab; FactBox; dialog vs. message box.

**Gotchas and tips:**
- Microsoft's docs call the top-right Action center button **Show messages** in some places (messaging API article; training module) and **Action center** in others.
- The user avatar was removed in 10.0.17: users see their **initials in a circle** on the navigation bar instead.
- The Microsoft 365 waffle icon takes the user out of D365 to the Microsoft 365 portal.

**Admin setup / feature flag:** none.

**Version notes:** article last revised 3 Jan 2025. The training unit adds the Copilot icon to the bar.

**Sources:**
- https://learn.microsoft.com/en-us/dynamics365/fin-ops-core/fin-ops/get-started/user-interface-elements
- https://learn.microsoft.com/en-us/training/modules/navigate-finance-operations/2-navigation-elements
- https://learn.microsoft.com/en-us/training/modules/describe-finance-operations-apps/4-explore-user-interface

**Screenshots:** `navigation-bar-labelled-training.png` (best single image: labelled navigation bar, Action Pane and navigation pane), `navigation-pane-training.png`, `action-pane-customer-page-training.png`.

---

## 2. Navigation concepts: dashboard, navigation pane, workspaces, tiles, search

**What it is.** Microsoft's model of how users move around. The five primary navigation concepts are **Dashboard**, **Navigation pane**, **Workspaces**, **Tiles** and **Navigation search**. They work together: the same menu structure builds the dashboard tiles and the navigation pane.

**End-user steps as documented:**
- Return to the dashboard: select the **Home** icon in the left-side navigation pane (developer doc), or select the app name (*Finance and Operations*) on the navigation bar (training). Keyboard: **Alt+Shift+Home**.
- Open the navigation pane: select the **Expand the navigation pane** / **Show navigation pane** button (the "hamburger" or **Menu** button) in the upper left. You can pin it open; the app keeps it open until you collapse it. Keyboard: **Alt+F1** toggles open / pinned open / closed.
- Open a workspace: select its tile on the dashboard, select it in the **Workspaces** section of the navigation pane, or find it with navigation search.
- Go back: use the back arrow at the left end of the Action Pane (training), or **Esc** to close the page (see section 16).

**Navigation pane sections** (four collapsible sections, plus **Home** at the top):
- **Favorites**: pages you marked with the star (see section 9).
- **Recent**: pages you visited most recently (see section 9).
- **Workspaces**: the workspaces you have access to.
- **Modules**: the full list of modules. Selecting a module opens the right side of the pane with that module's menu (for example **Accounts receivable** > **Customers** > **All customers**).

**Tiles.** A tile is a rectangular button that opens a page. Types: **Standard** (no data), **Count** (shows a count of items in the linked list, e.g. "3 shipped but not invoiced sales orders"), **KPI** (summary of a KPI), **Link** (opens a URL). Keyboard: **Alt+Up arrow** shows refresh information for a count tile.

**Key concepts:** module, menu path (the "navigation path" a guide gives, e.g. **Modules** > **Accounts receivable** > **Customers** > **All customers**), workspace, tile, count tile.

**Gotchas and tips:**
- What a user sees in the navigation pane, dashboard and search depends on their access (Microsoft: "role"). For the guide: a missing page means contact BAU Support (D-083).
- Navigation pane state (pinned/collapsed) is remembered per user automatically.

**Admin setup:** none.

**Sources:**
- https://learn.microsoft.com/en-us/dynamics365/fin-ops-core/dev-itpro/user-interface/page-navigation (revised 25 Apr 2025)
- https://learn.microsoft.com/en-us/training/modules/navigate-finance-operations/2-navigation-elements
- https://learn.microsoft.com/en-us/dynamics365/fin-ops-core/dev-itpro/get-started/personalize-user-experience (navigation pane pinning)

**Screenshots:** `navigation-pane-training.png`, `navigation-pane-modules-ar-training.svg` (Accounts receivable module menu open), `tile-standard.png`, `tile-count.png`, `tile-kpi.png`, `tile-link.png`, `workspace-tiles-training.png`.

---

## 3. Default dashboard

**What it is.** The page that opens by default when a user signs in (their default **initial page**). It is preconfigured with components that help users reach workspaces and other pages. Users only see components they have permission to use.

**Out-of-the-box components:**
- A page header with the name of the current legal entity (company) and a banner image.
- An **Apps** area: tiles for finance and operations apps available to you (and possibly set-up documentation links).
- A **Workspaces** area: one tile per workspace you can access. Tiles can show information you pinned from a workspace.
- A **Search people** field (finds personnel in the Human Resources **People** workspace; not relevant to finance users).
- A calendar (session date picker) where you can set the current session date (see section 14).
- **Work items assigned to me**: workflow work items assigned to you, with links to act on them (cross-reference: workflow research area).

**End-user steps:**
- Pin workspace information to the dashboard: open the workspace, right-click a tile, select **Personalize: <tile name>**, then select **Pin to dashboard** (clear it to remove).
- The dashboard can be personalized (cross-reference: personalization research area).

**Key concepts:** initial page, workspace tile, session date.

**Gotchas:**
- The header shows the **current legal entity**: a quick visual check of which company you are in.
- The banner or logo per legal entity is admin-configured (see "Change the banners or logo images for legal entities").

**Admin setup:** banner/logo is admin; otherwise none.

**Sources:**
- https://learn.microsoft.com/en-us/dynamics365/fin-ops-core/fin-ops/get-started/default-dashboard (revised 25 Apr 2025)
- https://learn.microsoft.com/en-us/dynamics365/fin-ops-core/fin-ops/get-started/tasks/change-banner-or-logo

**Screenshots:** `default-dashboard.png` (1920x1080, as an administrator sees it), `dashboard-training.svg`.

---

## 4. Immersive Home (the new AI-first landing page)

**What it is.** A modern, AI-first landing page and an alternative **initial page** to the default dashboard. It greets the user by name, summarizes their most important work, and lets them act on work items (for example approvals) without leaving the page. It is also the entry point to AI agents.

**Components:**
- **Greeting and summary**: welcomes you by name and summarizes relevant work items.
- **Suggestions** area: callouts, for example to enroll an agent skill for a task.
- **Work items** area: priority-ranked activity cards (title, summary, action buttons, link to the related task or workspace). Similar items can collapse into one card. Examples include expense approvals and other workflow work items, and agent-prepared items for review. Completed activities disappear. You can add long-running activities to **Pinned items**.
- **Agent activity** area (only when AI agents are enabled): per-agent metrics, with **View activity** and **View agents** buttons.
- **Workspaces** area: ranked tiles; ranking uses how recently you used each workspace, and **favorite workspaces rank at the top**. Pin workspace information as for the dashboard (right-click tile > **Personalize: <tile name>** > **Pin to dashboard**).
- Activity cards include a feedback mechanism (if the admin enabled Copilot user feedback).

**End-user steps:** to make it your start page, set **Initial page** in **User options** (section 5). Microsoft does not document separate end-user steps beyond that.

**Admin setup / feature flag:**
- Version **10.0.44 or later**.
- Feature management: **Immersive Home** must be turned on.
- Users need a specific privilege (Microsoft names it); per D-083 the guide does not name it.

**Version notes:**
- Release plan 2025 wave 1/wave 2: *Stay focused and simplify tasks with Immersive Home and adaptive experiences*: public preview 6 Jun 2025, **general availability 13 Mar 2026**, "Users by admins, makers, or analysts" (must be enabled by an admin).
- The Copilot overview page (revised 4 Aug 2026) still lists it as **"Immersive Home (production ready preview)"**, and the training module says "currently in preview". The docs disagree on status: confirm with the company whether it is enabled before the guide teaches it.

**Sources:**
- https://learn.microsoft.com/en-us/dynamics365/fin-ops-core/fin-ops/copilot/immersive-home (revised 7 May 2026)
- https://learn.microsoft.com/en-us/dynamics365/release-plan/2025wave2/enterprise-resource-planning/finance-operations-crossapp-capabilities/stay-focused-simplify-tasks-immersive-home-adaptive-experiences
- https://learn.microsoft.com/en-us/dynamics365/fin-ops-core/fin-ops/copilot/copilot-for-finance-operations
- https://learn.microsoft.com/en-us/training/modules/describe-finance-operations-apps/3-describe-use-cases-ai-tools

**Screenshots:** `immersive-home.png` (1920x1080), `immersive-home-copilot-sidecar-training.png` (Immersive Home with the Copilot sidecar open).

---

## 5. User options (Settings > User options)

**What it is.** The page of personal, system-wide settings for the current user: theme, size, default company, initial page, default view/edit mode, language, time zone, date/time/number format, accessibility and more. Available to all users, even those without personalization rights.

**End-user steps:** select **Settings** (gear icon) on the navigation bar > **User options**. Change a value and select **Save**. Four tabs:

**Visual tab** ("Choose color theme and the size of elements")
- **Color theme**: a row of colour swatches plus a black-and-white **high contrast** swatch (from the screenshot).
- **Size**: two layouts (larger and denser elements) shown as thumbnails. Microsoft describes this only as "the default size of elements on pages".

**Preferences tab** ("Set up default preference"), FastTabs as shown in the training screenshot:
- **Startup**: **Company** (default legal entity at sign-in), **Initial page** (e.g. **Default dashboard**), **Default view/edit mode** (e.g. **Auto**; see section 11).
- **Language and country/region preferences**: **Language**, **Date, time, and number format**, **Time zone**, **Country/region**. Changes take effect immediately.
- **Miscellaneous**: **Enable document handling** (attachments; cross-reference: documents research area); **URL manipulations** > **Automatically update query parameters** (screenshot only; not explained in the docs).
- **Accessibility**: **Enhanced tab sequence** (all fields in the Tab order); **Show tooltips on focus** (tooltip shows automatically when a control gets focus).
- **Task management**: **Show task list on default dashboard**.

**Account tab**: user name, email provider and email address used to send mail from D365, electronic signature option.

**Workflow tab**: workflow email options and delegation (cross-reference: workflow research area).

**Action Pane: Usage data**: view and delete your usage data and personalizations. On its **Personalization** tab you can also **reset feature callouts** so they show again.

**Set your own initial page (Microsoft's exact steps):**
1. Open the **Settings** menu (gear icon) in the top navigation bar.
2. Select **User options**.
3. Open the **Preferences** tab.
4. On the **Startup** FastTab, set the **Initial page** field to your preferred initial page.
5. Select **Save**.

**Time zone.** Microsoft documents only the administrator path: **System administration** > **Users** > **Users** > select user > **User options** > **Preferences** > **Time zone** > **Save**. The end-user equivalent is the **Time zone** field on their own **Preferences** tab.

**Key concepts:** default company vs. current company; initial page; time zone affects displayed date/times.

**Gotchas:**
- **Dark mode: not documented.** No Microsoft page found describes a dark mode or dark theme for F&O. The only documented options are the colour themes and the high-contrast swatch. Don't promise dark mode.
- Microsoft says the Preferences tab "includes several miscellaneous preferences that vary from release to release". Take screenshots from the company's own environment.
- Language changes the labels: screenshots in a procedure guide assume en-us (or the company's language).
- Notification preferences: no "notifications" setting is documented under User options for F&O. Alert notifications are set up per rule (cross-reference: alerts research area).

**Admin setup:** none for the user's own options; admins can set them for other users from **System administration** > **Users** > **Users** > **User options**.

**Sources:**
- https://learn.microsoft.com/en-us/dynamics365/fin-ops-core/dev-itpro/get-started/personalize-user-experience ("System-wide options for the current user"; revised 26 Mar 2026)
- https://learn.microsoft.com/en-us/dynamics365/fin-ops-core/fin-ops/get-started/set-users-initial-page (revised 5 Mar 2026)
- https://learn.microsoft.com/en-us/dynamics365/fin-ops-core/fin-ops/organization-administration/tasks/set-users-preferred-time-zone
- https://learn.microsoft.com/en-us/training/modules/describe-finance-operations-apps/4-explore-user-interface
- https://learn.microsoft.com/en-us/dynamics365/fin-ops-core/dev-itpro/user-interface/feature-callouts (resetting callouts)

**Screenshots:** `user-options-visual-tab-training.png`, `user-options-preferences-tab-training.png`, `user-options-workflow-tab-training.png`.

---

## 6. Legal entity (company) picker

**What it is.** The control on the navigation bar that shows and changes the current legal entity (company). Transactions you enter belong to the selected legal entity. Microsoft: "A legal entity is an organization that is identified through registration with a legal authority."

**End-user steps:**
- Select the **company picker** on the navigation bar and choose the company. Keyboard: **Ctrl+Shift+O** moves focus to the company picker.
- Set the company you start in: **Settings** > **User options** > **Preferences** > **Startup** > **Company** > **Save**.

**Key concepts:** legal entity = company = the four-character company code (e.g. `USMF`); default company; the dashboard header shows the current legal entity.

**Gotchas:**
- Microsoft's user docs are thin here: there is no dedicated article on switching company. Behaviour has to be confirmed in the company's environment, for example whether open pages change company and how pop-out windows behave.
- **Open in new window** pop-ups show the company the page was opened in, read-only (section 10). A user can therefore have windows open in different companies.
- Since 10.0.49 the Dynamics 365 ERP MCP tools "honor the session's company context", which confirms company is per session (agent-facing).

**Admin setup:** which companies a user can see depends on their access (D-083: contact BAU Support if a company is missing).

**Sources:**
- https://learn.microsoft.com/en-us/dynamics365/fin-ops-core/fin-ops/get-started/user-interface-elements
- https://learn.microsoft.com/en-us/training/modules/describe-finance-operations-apps/4-explore-user-interface ("Company picker")
- https://learn.microsoft.com/en-us/dynamics365/fin-ops-core/fin-ops/get-started/shortcut-keys
- https://learn.microsoft.com/en-us/dynamics365/fin-ops-core/fin-ops/get-started/default-dashboard

**Screenshots:** `navigation-bar-labelled-training.png` (company picker labelled).

---

## 7. Navigation search ("Search for a page")

**What it is.** The **Search** box on the navigation bar finds and opens **pages and workspaces** (not data, not actions). It matches your words against page titles **and** their navigation paths.

**End-user steps (Microsoft):**
1. Select the **Search** icon (the box shows **Search for a page**) to display the **Search** box. Keyboard: **Ctrl+/** or **Alt+G**.
2. Type one or more words, e.g. "vendor invoice" or "payment journal".
3. Select the page in the results. Each result shows the page title and its navigation path.

**Tips documented by Microsoft:**
- An exact page title ("payment journal") puts that page at the top.
- Words match the path too: "receivable" returns pages in **Accounts receivable**; "ven bal report" matches *vendor balance* in the title and *report* in the path; "l e" matches pages whose words start with "l" then "e".
- Power users: **form:** followed by the technical form name (e.g. `form: vendinvoice`).
- Results are **limited to 10**: refine the words if the page isn't listed.
- Only pages enabled in the configuration and that the user can access appear.
- You can only open top-level pages this way; secondary pages need context from their parent page.

**Key concepts:** page vs. data vs. action search (three different searches).

**Gotchas:** new users try to search for a customer or invoice number here. It won't find data (use list page filters, a cross-reference to the filtering research area).

**Admin setup:** none.

**Copilot / natural-language search:** no natural-language *navigation* search is documented. The Copilot sidecar (generative help and guidance) and *Chat with finance and operations data* / *Ask about your ERP data in natural language* (GA 26 Jan 2026) answer questions in natural language. Cross-reference: Copilot research area.

**Sources:**
- https://learn.microsoft.com/en-us/dynamics365/fin-ops-core/fin-ops/get-started/navigation-search (revised 10 Mar 2026)
- https://learn.microsoft.com/en-us/dynamics365/fin-ops-core/dev-itpro/user-interface/page-navigation#navigation-search
- https://learn.microsoft.com/en-us/training/modules/navigate-finance-operations/5-searching
- https://learn.microsoft.com/en-us/dynamics365/fin-ops-core/fin-ops/get-started/accessibility-features

**Screenshots:** `navigation-search-results-customer-training.png`, `navigation-search-results-training.png`, `navigation-search-form-name-training.png`.

---

## 8. Action search

**What it is.** A search box on the Action Pane that finds and **runs a button** (action) from any visible Action Pane or toolbar on the current page. It replaced the old **Key Tips** (Alt + letters), which are no longer available.

**End-user steps (Microsoft, exact):**
1. On the Action Pane, click in the **Action search** field. (The field contains a magnifying glass icon.)
2. Type all or part of the name of the button that you want to run. You can also search by words from the button's "path". Typically a button appears near the top of the results after two to four characters.
3. Find and run the button in the results list (mouse or keyboard).

After the button runs, focus returns to your last position on the page. Keyboard: **Ctrl+'** (apostrophe) or **Alt+Q**; press it again to return focus. (The action-search article says **Ctrl+/** or **Alt+Q**; the shortcut-key article and accessibility article say **Ctrl+'** or **Alt+Q**. Ctrl+/ is navigation search in the shortcut list. Treat **Alt+Q** as the safe shortcut and test the other in the company's environment.)

**Understanding results:** each result shows the button's path: Action Pane tab > button group > menu button > separator, or FastTab. For example, **Totals** shows path **Sales order** > **View**, and **On-hand inventory** shows **Sales order lines** > **Inventory** > **View**.

**Gotchas:** drop dialog buttons and buttons inside subforms do not show in Action search.

**Admin setup:** none.

**Sources:**
- https://learn.microsoft.com/en-us/dynamics365/fin-ops-core/fin-ops/get-started/action-search (revised 10 Mar 2026)
- https://learn.microsoft.com/en-us/dynamics365/fin-ops-core/fin-ops/get-started/accessibility-features (worked example: **Email notification log**)
- https://learn.microsoft.com/en-us/training/modules/navigate-finance-operations/5-searching

**Screenshots:** `navigation-bar-labelled-training.png` (shows the magnifier at the end of the Action Pane). No dedicated action-search screenshot exists in the docs. Capture one from the company's environment.

---

## 9. Favorites and Recent

**What it is.** Two sections of the navigation pane. **Favorites** lists pages you marked with a star. **Recent** is filled automatically with the pages you visited most recently.

**End-user steps (Microsoft):**
- Add a favorite: in the navigation pane, select the **star icon** next to the page (in a module's menu). Select it again to remove.
- Keyboard: with focus on a page in the navigation pane, **Shift+F** adds or removes it as a favorite.
- Open: **Navigation pane** > **Favorites** (or **Recent**) > select the page.

**Tips (training):** Favorites help both for pages used often and for pages used rarely but hard to find. Recent helps switch back and forth between areas.

**Related:** favourite *workspaces* rank first on Immersive Home.

**Gotchas:** no documented limit, ordering or sharing for favorites. The docs say nothing about renaming or arranging favorites.

**Admin setup:** none.

**Sources:**
- https://learn.microsoft.com/en-us/dynamics365/fin-ops-core/dev-itpro/user-interface/page-navigation#navigation-pane
- https://learn.microsoft.com/en-us/training/modules/navigate-finance-operations/2-navigation-elements
- https://learn.microsoft.com/en-us/dynamics365/fin-ops-core/fin-ops/get-started/shortcut-keys (Shift+F)

**Screenshots:** `navigation-pane-training.png`, `navigation-pane-modules-ar-training.svg`.

---

## 10. Open in new window (pages side by side) and Popout

**What it is.** The **Open in new window** icon (system **Popout** button, right side of the Action Pane) moves the current page into a pop-up browser window so you can work on two pages side by side, e.g. a journal list and a journal's lines.

**How it behaves (Microsoft):**
- Selecting **Open in new window** opens the page (e.g. journal lines) in a pop-up and takes the original window back to the previous page (the journal list).
- If the pages' data is related, changing the selected record in the main window automatically refreshes the pop-up (e.g. select another journal; the pop-up shows its lines).
- The whole page opens in the pop-up, so you can't keep two views (e.g. Grid and Details) of the same page side by side. Use the navigation list instead.
- Only available when more than one page is open in the window.
- The pop-up closes when its last page closes, or when you navigate to a different area in the main window.
- The pop-up's top bar shows the company the page was opened in, read-only.
- If the main window is closed or refreshed, all pop-ups become **read-only**.

**Prerequisite:** allow pop-ups in the browser for the site (e.g. `*.dynamics.com`). Likely an IT/browser-policy item.

**Gotchas:** refreshing the main browser tab freezes the pop-ups. Users can lose unsaved work in a pop-up that way.

**Related:** opening a second **browser tab** with the same environment URL is a separate, undocumented approach. The deep-links article covers shareable URLs to forms (developer-generated). Microsoft does not document copying the browser URL to share a record as an end-user task.

**Sources:**
- https://learn.microsoft.com/en-us/dynamics365/fin-ops-core/fin-ops/get-started/display-pages-side-by-side (revised 3 Jan 2025)
- https://learn.microsoft.com/en-us/dynamics365/fin-ops-core/dev-itpro/user-interface/system-defined-buttons ("Refresh, Popout, and Close system buttons")
- https://learn.microsoft.com/en-us/dynamics365/fin-ops-core/dev-itpro/user-interface/create-deep-links

**Screenshots:** none in the docs. Capture from the environment.

---

## 11. View mode and Edit mode (Edit, Save, Read mode, Revert)

**What it is.** Most pages open locked for viewing (**View mode**) to prevent accidental changes. You switch to **Edit mode** to change data. Microsoft: "This distinction is important, because it helps prevent accidental updates to data."

**Uses (training):**
- **View mode**: review data on a list page or record, open related records through links.
- **Edit mode**: change data directly on the page. Links still work.

**Buttons and behaviour (system-defined buttons doc), for a normal page (**ViewEditMode = Auto**):**
- In View mode, the **Edit** button is shown on the Action Pane.
- In Edit mode, the **Save** button is shown on the Action Pane, and **Read mode** and **Revert** are on the Action Pane's **Options** tab.
- Some pages are always editable (only **Save** and **Revert**) or always read-only (none of these buttons).
- Keyboard: **F2** toggles edit mode.

**User setting:** **User options** > **Preferences** > **Startup** > **Default view/edit mode** (screenshot shows **Auto**). Microsoft: it "determines whether a page is locked for viewing or opened for editing every time that you open it". The values are not listed in the user docs. The screenshot shows **Auto**; the developer property values are View / Edit / Auto. Confirm the dropdown values in the environment.

**Gotchas:**
- New users type into a field and nothing happens because they're in View mode. Teach: select **Edit** (or press F2).
- Grid view of list pages allows bulk editing in the list (Details Master pattern) when in Edit mode.

**Sources:**
- https://learn.microsoft.com/en-us/training/modules/navigate-finance-operations/7-view-and-edit-mode
- https://learn.microsoft.com/en-us/dynamics365/fin-ops-core/dev-itpro/user-interface/system-defined-buttons ("Edit, Done, Save, and Restore system buttons")
- https://learn.microsoft.com/en-us/dynamics365/fin-ops-core/dev-itpro/get-started/personalize-user-experience

**Screenshots:** `action-pane-customer-page-training.png` (Edit / New / Delete on the Action Pane), `user-options-preferences-tab-training.png` (Default view/edit mode).

---

## 12. Create, save, revert, refresh and delete records (save behaviour)

**What it is.** The standard record actions on every page. **New**, **Delete**, **Edit**/**Save**, **Refresh**, **Attach** and **Export** are provided by the platform on every standard page. **Refresh**, **Popout** (Open in new window) and **Close** sit on the right side of the Action Pane.

**End-user actions and shortcuts (Microsoft):**

| Action | Button | Shortcut |
|---|---|---|
| Create a new record | **New** | **Alt+N** |
| Delete a record | **Delete** | **Alt+Del** or **Alt+F9** |
| Save record | **Save** | **Alt+S** or **Ctrl+S** |
| Revert (restore) unsaved changes | **Revert** (Options tab) | **Ctrl+Shift+F5** |
| Refresh data | **Refresh** | **Shift+F5** |
| Toggle edit mode | **Edit** / **Read mode** | **F2** |
| Close the page (Back) | **Close** / back arrow | **Esc** |
| Close the page with explicit save | | **Shift+Esc** |
| Close the page discarding unsaved changes | | **Alt+Shift+Q** |
| New row at bottom of a grid | | **Down arrow** from the last row |
| Revert a new unsaved grid row | | **Ctrl+Shift+F5** (10.0.32+) |

**Save behaviour ("dirty" records):** Microsoft's end-user docs do **not** have an article on when a record is saved automatically. What the docs do say:
- Validation messages appear in the message bar while you work; the invalid value stays, flagged as invalid, and you can correct it any time **before the data is saved**. Table-level validation messages clear "the next time that the user crosses a **save boundary**" (messaging article).
- If you try to save a page that still has invalid data, an interrupting error dialog appears.
- **Close the page with explicit save** (Shift+Esc) vs **Close the page discarding any unsaved changes** (Alt+Shift+Q) implies that unsaved changes exist and that Esc/Back alone is not the same as discarding.
- Session timeout: users get a countdown notice before an inactive session closes, "to help prevent users from losing any unsaved changes" (section 20).
- Common behaviour to confirm by testing (not documented on Learn): moving to another record or closing the page typically saves pending changes; Revert restores the last saved values.

**Gotchas:** tell users to **Save** explicitly and check the message bar. Behaviour when navigating away should be tested in the company's environment before the guide states it.

**Sources:**
- https://learn.microsoft.com/en-us/dynamics365/fin-ops-core/fin-ops/get-started/shortcut-keys (Page shortcuts)
- https://learn.microsoft.com/en-us/dynamics365/fin-ops-core/dev-itpro/user-interface/system-defined-buttons
- https://learn.microsoft.com/en-us/dynamics365/fin-ops-core/dev-itpro/user-interface/messaging-user ("When are validation messages cleaned up?")
- https://learn.microsoft.com/en-us/dynamics365/fin-ops-core/dev-itpro/user-interface/details-master-form-pattern

**Screenshots:** `action-pane-customer-page-training.png`.

---

## 13. Page types and views: workspaces, list pages, details pages, Grid / Details / Header / Lines views

**What it is.** About 90 percent of pages follow a small set of **form patterns**, so once a user recognises the patterns they can work on any page. For a new user the useful distinctions are:
- **Workspace**: an activity-oriented page (e.g. **Customer payments**, **Customer invoicing**, **Credit and collections**). Typical sections: **Summary** tiles (often count tiles), tabbed **lists** (e.g. "Shipped but not invoiced sales orders"), optional charts or Power BI, and **Links** to related pages. Workspaces scroll vertically (the old horizontal "panorama" was removed in 10.0.25 and deprecated in 10.0.29). Some workspaces have Action Pane buttons that start tasks (e.g. **New free text invoice** on **Customer invoicing**).
- **List page / Grid view**: a grid for browsing, filtering and selecting records; FactBoxes on the right show related data for the selected row.
- **Details page (Details view)**: one record, laid out in FastTabs; a narrow list on the left (navigation list) lets you move between records.
- **Header view / Lines view** (Details Transaction pattern, e.g. sales or purchase orders, journals): **Header** holds the header fields; **Lines** holds the lines grid, line details and key header fields.
- **Dialogs and sliders**: a **slider** dialog slides in from the right to collect information (e.g. creating a new record); select **OK** or **Cancel**, or click the shaded area on the left to cancel. A **MessageBox** is a full-width modal "lightbox" message.

**Views (training, "Compare views"):**
- **Grid view**: update many records at once without opening each one.
- **Details view**: review one selected record.
- **Line view** and **Header view**: for header/line data such as purchase and sales orders. Header view is also where you can enter defaults or bulk-update lines on some pages.
- Switch views: **Options** tab > **Change view** (system button), or keyboard **Ctrl+Shift+G** (grid), **Ctrl+Shift+D** (details), **Ctrl+Shift+H** (header), **Ctrl+Shift+L** (lines). Navigation list: **Alt+M,S** or **Ctrl+F8**.
- Move between records outside a grid: **Ctrl+Up/Down arrow** (previous/next), **Ctrl+Home/End** (first/last).

**Workspace filters and configuration:** many workspaces have a workspace-wide filter (upper-left) and section filters; some have a configure button on the Action Pane that opens a settings dialog. (Overlaps with the filtering research area.)

**FastTabs and FactBoxes:** expanded/collapsed state is remembered automatically. Collapsing them can improve performance, because data isn't fetched until expanded. FactBox shortcuts: **Alt+M,B** or **Ctrl+F2** open/focus the FactBox pane; **Alt+<n>** jumps to the nth FastTab or FactBox; **Alt+0** collapses.

**Hyperlinked values ("View details"):** a field value shown as a hyperlink opens the related record (for example a customer account). **View details** is also on the right-click menu. Keyboard: **Ctrl+Enter**.

**Sources:**
- https://learn.microsoft.com/en-us/training/modules/navigate-finance-operations/6-comparing-views
- https://learn.microsoft.com/en-us/training/modules/navigate-finance-operations/3-workspaces-driving-productivity
- https://learn.microsoft.com/en-us/dynamics365/fin-ops-core/fin-ops/get-started/configure-filter-workspaces
- https://learn.microsoft.com/en-us/dynamics365/fin-ops-core/dev-itpro/user-interface/list-page-form-pattern
- https://learn.microsoft.com/en-us/dynamics365/fin-ops-core/dev-itpro/user-interface/details-master-form-pattern
- https://learn.microsoft.com/en-us/dynamics365/fin-ops-core/dev-itpro/user-interface/details-transaction-form-pattern
- https://learn.microsoft.com/en-us/dynamics365/fin-ops-core/dev-itpro/user-interface/workspace-form-pattern
- https://learn.microsoft.com/en-us/dynamics365/fin-ops-core/dev-itpro/user-interface/slider-messagebox
- https://learn.microsoft.com/en-us/dynamics365/fin-ops-core/fin-ops/get-started/client-faq ("Where is the View details functionality?")
- https://learn.microsoft.com/en-us/dynamics365/fin-ops-core/dev-itpro/get-started/personalize-user-experience (FastTab/FactBox state)
- https://learn.microsoft.com/en-us/dynamics365/fin-ops-core/fin-ops/get-started/accessibility-features ("Form patterns")
- https://learn.microsoft.com/en-us/dynamics365/fin-ops-core/fin-ops/get-started/removed-deprecated-features-platform-updates (Panorama tab style)

**Screenshots:** `workspace-customer-payments-training.svg`, `workspace-customer-invoicing-areas-training.svg` (labelled workspace areas), `workspace-credit-collections-training.png`, `workspace-filter-expanded.png`, `workspace-section-filters.png`.

---

## 14. Change the session date

**What it is.** By default the current date is used when you enter and post journals and source documents. You can change the date **for your current session**, for example to back-date entries. Relevant for period-end work in R2R and AP/AR.

**End-user steps (Microsoft, exact):**
1. In the navigation pane, go to **Modules** > **Common** > **Common** > **Session date and time**.
2. In the **Date** field, enter a date.
3. Select **OK**.

Alternative: the calendar (session date picker) on the **default dashboard**. In a date field, press **D** to enter the session date (and **T** for today's date).

**Gotchas:**
- Applies to the current session only (lost when you sign out or the session times out).
- It changes the default posting/document date: a high-risk setting if forgotten. The guide should tell users to reset it, and the company may restrict it (confirm policy).

**Admin setup:** none documented.

**Sources:**
- https://learn.microsoft.com/en-us/dynamics365/fin-ops-core/fin-ops/organization-administration/tasks/change-date-session (revised 10 Mar 2026)
- https://learn.microsoft.com/en-us/dynamics365/fin-ops-core/fin-ops/get-started/default-dashboard
- https://learn.microsoft.com/en-us/dynamics365/fin-ops-core/fin-ops/get-started/shortcut-keys (input control shortcuts)

**Screenshots:** none in the docs.

---

## 15. Lookups and date pickers (entering values)

**What it is.** Many fields have a **lookup**: a drop-down list of valid values (customers, vendors, accounts). Lookups now open automatically as you type and filter as you go.

**Behaviour and steps (Microsoft):**
- Start typing (e.g. "col" in **City**). After a short pause the lookup opens, filtered to values that begin with what you typed. The cursor stays in the field, so keep typing to narrow the list.
- **Up/Down arrow** highlights a row; **Enter** selects it.
- **Type the name, not only the ID:** many lookups (not all) accept the ID *or* the name. For example, in **Customer account** you can type "Forest Wholesales" instead of "US-003". The **Name** column moves first and the list sorts by name.
- **Find by other text (e.g. "cable")**: clear the field, open the lookup, then use the lookup's **column header** filter (contains, etc.). Keyboard: **Alt+Down arrow** a second time to move into the lookup, Tab to the column, **Ctrl+G** to open its filter.
- Open a lookup, combo box, date picker or drop dialog: **Alt+Down arrow** (or **Enter** when the **Standardize keyboard interaction for combo box and lookup controls** feature is on). **Esc** closes it.
- **Alt+Up arrow** opens the control's enhanced preview.
- Segmented entry (e.g. main account + financial dimensions): **Alt+Down arrow** opens the segment list, **Alt+W** switches between **Show valid** and **Show all**, **Enter** selects a value and moves to the next segment. (Cross-reference with R2R ledger account entry.)

**Date picker shortcuts:** **Alt+Down arrow** open; **Ctrl+Arrow** move between dates; **Page up/down** previous/next month; **Ctrl+Shift+Page up/down** previous/next year; **Ctrl+Home** today; **T** pick today; **C** clear; **N** pick *Never* (max date). In the date field itself: **D** session date, **T** today.

**Deprecated:** typing an asterisk (*) to force a lookup to open is **deprecated**.

**Feature management:** *Standardize keyboard interaction for combo box and lookup controls* changes keyboard behaviour (Enter opens).

**Sources:**
- https://learn.microsoft.com/en-us/dynamics365/fin-ops-core/fin-ops/get-started/use-lookups-to-find-information (revised 23 Jan 2025)
- https://learn.microsoft.com/en-us/dynamics365/fin-ops-core/fin-ops/get-started/shortcut-keys
- https://learn.microsoft.com/en-us/dynamics365/fin-ops-core/dev-itpro/user-interface/contextual-data-entry-lookups (developer background)
- https://learn.microsoft.com/en-us/dynamics365/fin-ops-core/dev-itpro/user-interface/lookups-controls

**Screenshots:** none suitable for end users in the docs. Capture from the environment.

---

## 16. Keyboard shortcuts

**What it is.** Microsoft's full list of keyboard shortcuts (US keyboard layout). Some are **key chords**: e.g. **Alt+M, A** means press Alt+M, release, then press A.

**Find shortcuts in the app:** right-click a control and select **View shortcuts**, or press **Alt+Shift+K** (press again to see all shortcuts for the page).

**The essentials for a Getting Started guide** (all from Microsoft's list):

| Task | Shortcut |
|---|---|
| Search for a page | **Ctrl+/** or **Alt+G** |
| Action search | **Ctrl+'** or **Alt+Q** |
| Go to the dashboard | **Alt+Shift+Home** |
| Toggle navigation pane (open / pinned / closed) | **Alt+F1** |
| Move to the company picker | **Ctrl+Shift+O** |
| New record | **Alt+N** |
| Save | **Alt+S** or **Ctrl+S** |
| Delete | **Alt+Del** or **Alt+F9** |
| Toggle edit mode | **F2** |
| Refresh | **Shift+F5** |
| Revert | **Ctrl+Shift+F5** |
| Close page (Back) | **Esc** |
| Open lookup / date picker | **Alt+Down arrow** |
| Open hyperlink | **Ctrl+Enter** |
| Session date / today in a date field | **D** / **T** |
| Open Filter pane | **Alt+M, F** or **Ctrl+F3** |
| Grid column filter | **Ctrl+G** |
| Open FactBox pane | **Alt+M, B** or **Ctrl+F2** |
| Message bar / Message center | **Ctrl+F7** / **Ctrl+Shift+F7** |
| Open Help pane | **Ctrl+?** |
| Export to Excel | **Ctrl+Shift+E** |
| Attach a document | **Ctrl+Shift+A** |
| Simulate right-click | **Shift+F10** |
| View available shortcuts | **Alt+Shift+K** |

Full sections in the article: Action, Date picker, FactBox, Filtering, Page, Page navigation, Grid (many grid shortcuts are 10.0.32+), Input control, Messaging, Navigation, Personalization, Segmented entry, Task recorder.

**Focus management** (worth one line in the guide): when a page opens, focus is on the first editable field. After an Action Pane or toolbar button runs, focus returns to the last field you were in.

**Feature management:** *Streamline tabbing behavior in full-page forms* (10.0.26) lets Tab move through all regions of the page.

**Gotchas:** shortcuts depend on keyboard layout. Some browser shortcuts conflict (e.g. Ctrl+F is the browser's find, not D365's). The action-search article and the shortcut list disagree on Ctrl+/ vs Ctrl+' (section 8).

**Sources:**
- https://learn.microsoft.com/en-us/dynamics365/fin-ops-core/fin-ops/get-started/shortcut-keys (revised 10 Mar 2026)

**Screenshots:** none in the docs. Capture the **View shortcuts** dialog from the environment.

---

## 17. Right-click (shortcut) menus

**What it is.** Two different right-click menus. Right-click in an editable field (or on selected text) gives the **browser's** menu (**Cut**, **Copy**, **Paste**). Right-click a field label or a read-only value gives the **app's** shortcut menu (e.g. **View details**, **View shortcuts**, **Personalize**, **Insert columns**, **Hide this column**).

**Keyboard:** **Shift+F10** simulates a right-click; **Ctrl+F10** opens the context menu.

**Sources:**
- https://learn.microsoft.com/en-us/dynamics365/fin-ops-core/fin-ops/get-started/client-faq
- https://learn.microsoft.com/en-us/dynamics365/fin-ops-core/dev-itpro/get-started/personalize-user-experience ("Shortcut menu options")

**Screenshots:** `personalize-element-property-window.png` (right-click > Personalize; cross-reference only).

---

## 18. Messages: message bar, message box, Action center, Message details, feature callouts

**What it is.** How the system tells you things. Where a message appears depends on what caused it:
- **Message bar** (beneath the Action Pane): messages about **the current page**, mostly data validation ("This customer is marked as inactive.", "The transaction on voucher do not balance."). Types: **info**, **warning**, **error**. They belong to the page: leave the page and they disappear; come back and they reappear. A message can carry a link button that runs a related action (10.0.10+). Keyboard: **Ctrl+F7**.
- **Message box**: interrupts you; you must read and dismiss it before continuing. Errors overlay the page in a modal "light box", with a bold main instruction and details below.
- **Action center** (bell icon / **Show messages** on the navigation bar): messages from **background (asynchronous) tasks**, such as a batch job or report finishing. Shows a count of new messages since you last opened it. Holds up to **500** messages, first in, first out. Alert notifications also arrive here (cross-reference: alerts research area).
- **Message details** pane: when a task produces a collection of messages (e.g. posting results), the message bar or Action center shows a summary. Its severity is the worst message in the collection. Select **Message details** to see all of them. Keyboard: **Ctrl+Shift+F7** goes to the Message Center.
- **Feature callout**: a pop-up next to a control introducing a new feature, optionally with **Learn more**. Select **Got it** to dismiss it for good. Reset them in **User options** > **Usage data** > **Personalization** tab. **Alt+M, C** moves to the next callout. Admins can turn callouts off (**Client performance options** > **Feature callouts enabled**).

**Message types (Microsoft definitions):**
- **Notification** (info): informs; usually no action needed.
- **Warning**: data is in an incorrect state that may cause an issue later.
- **Error**: an action has failed. Non-interrupting errors let you carry on; interrupting errors stop you until fixed.

**Behaviour:** validation messages clear themselves when you correct the field (field-level) or at the next save (table-level). If you close a slider dialog right after starting an action, its messages go to the parent page.

**Admin / feature flags:** *Enable system notification management*; *Auto-blocking of high-volume notification rules* (10.0.39). If a notification rule is blocked, users are notified. Both are admin features.

**Gotchas:** a batch job (e.g. posting run in batch) reports to the Action center, not the page. New users miss these. Teach them to check the bell.

**Sources:**
- https://learn.microsoft.com/en-us/dynamics365/fin-ops-core/dev-itpro/user-interface/messaging-user (revised 12 Mar 2026)
- https://learn.microsoft.com/en-us/dynamics365/fin-ops-core/dev-itpro/user-interface/messaging-api-center-bar-details
- https://learn.microsoft.com/en-us/dynamics365/fin-ops-core/dev-itpro/user-interface/feature-callouts
- https://learn.microsoft.com/en-us/dynamics365/fin-ops-core/fin-ops/get-started/user-interface-elements ("Notifications")
- https://learn.microsoft.com/en-us/dynamics365/fin-ops-core/fin-ops/get-started/shortcut-keys (Messaging shortcuts)

**Screenshots:** `message-bars-info-warning-error.png`, `message-bar-types.jpg`, `message-box-error.jpg`, `action-center-messages.png`, `message-bar-setprefix-notification.png`, `message-details-pane.png`, `message-bar-info-message-details.jpg`, `message-bar-warning-message-details.jpg`, `message-bar-error-message-details.jpg`, `message-bar-with-action-link.png`, `feature-callout.png`.

---

## 19. Accessibility features

**What it is.** Features for keyboard-only and assistive-technology users. These help every user.

**Documented features:**
- Every field and control has a label and shortcut description that screen readers (e.g. Windows **Narrator**) read.
- Keyboard shortcuts and **Action search** for heads-down data entry. Worked example: press **Ctrl+'**, type "email" / "notific" / "log" to run **Email notification log**; press **Ctrl+'** again to return to your field.
- Navigation search with **Alt+G**.
- **Tab sequence** is "optimized": by default Tab stops only on the fields needed for typical tasks. Turn on **Enhanced tab sequence** (User options > Preferences > Accessibility) to include all fields, then use personalization to skip the ones you don't need.
- **Show tooltips on focus** (User options > Preferences > Accessibility).
- **Responsive layout**: zoom to **200 percent** or more. On small screens the layout collapses (single column, Action Pane collapsed).
- **High contrast** colour theme swatch on User options > Visual (screenshot).

**Admin setup:** none.

**Sources:**
- https://learn.microsoft.com/en-us/dynamics365/fin-ops-core/fin-ops/get-started/accessibility-features (revised 23 Jan 2025)
- https://learn.microsoft.com/en-us/training/modules/describe-finance-operations-apps/4-explore-user-interface

**Screenshots:** `user-options-visual-tab-training.png`, `user-options-preferences-tab-training.png`.

---

## 20. Session timeout and connection behaviour

**What it is.** An inactive browser session closes after a set time (default **30 minutes**, range 5 to 60, set by the administrator in **System parameters** > **General** > **Session management**). Before it closes, the user sees a **countdown notification** with a chance to reconnect: 5 minutes before (timeout over 30 minutes), 2 minutes before (10 to 30 minutes), 30 seconds before (under 10 minutes).

**Why a new user needs it:** unsaved changes can be lost. The session date also resets.

**Related (on-premises only):** without internet access the Office app launcher, Help pane and Open in Excel are unavailable and users see initials instead of a photo. Not relevant to a cloud deployment, but explains a missing Help pane if internet access is restricted.

**Sources:**
- https://learn.microsoft.com/en-us/dynamics365/fin-ops-core/dev-itpro/sysadmin/session-idle-timeout (revised 13 Mar 2026)
- https://learn.microsoft.com/en-us/dynamics365/fin-ops-core/dev-itpro/user-interface/client-disconnected

**Screenshots:** none.

---

## 21. Client FAQ (browser questions)

**What it is.** A short FAQ for the web client.
- **Symbols not loading**: browser security settings may block the symbol font. Add the app site to trusted sites. (The Internet Explorer instructions in it are obsolete: IE11 support ended August 2021; Microsoft recommends **Microsoft Edge**.)
- **Keeping Action Pane tabs open (like the AX 2012 ribbon)**: Microsoft says "planning to implement". The personalization article describes pinning the Action Pane open, which the app remembers per page.
- **Different right-click menus**: see section 17.
- **Where is View details**: hyperlinked values, or **View details** on the right-click menu.

**Sources:**
- https://learn.microsoft.com/en-us/dynamics365/fin-ops-core/fin-ops/get-started/client-faq (revised 31 Dec 2024)
- https://learn.microsoft.com/en-us/dynamics365/fin-ops-core/fin-ops/get-started/removed-deprecated-features-platform-updates (Internet Explorer 11)
- https://learn.microsoft.com/en-us/dynamics365/fin-ops-core/dev-itpro/get-started/personalize-user-experience (pin Action Pane)

---

## 22. Copilot in the navigation bar (cross-reference only)

The navigation bar now has a **Copilot** icon that opens the Copilot **sidecar** (the primary Copilot interface: generative help and guidance, chat with F&O data). Covered by the Copilot research area. Points relevant to this area:
- The Copilot overview (revised 4 Aug 2026) lists across all apps: Generative help and guidance, Workflow history summary, enhanced feedback, Chat with finance and operations data, Immersive Home (production ready preview), and the ERP MCP server.
- **Removed September 2026:** *Follow-up questions in the Copilot sidecar (preview)*: never made generally available, now removed.
- Release plan items with a user-facing angle: *Ask about your ERP data in natural language* (GA 26 Jan 2026); *Use Copilot Cowork to orchestrate insights and actions across Dynamics 365 ERP* (GA 16 Jun 2026, enabled by admins); *Open records in Dynamics 365 ERP applications with deep links from copilot responses* (GA 18 Aug 2026).

**Sources:**
- https://learn.microsoft.com/en-us/dynamics365/fin-ops-core/fin-ops/copilot/copilot-for-finance-operations
- https://learn.microsoft.com/en-us/dynamics365/release-plan/2025wave2/enterprise-resource-planning/finance-operations-crossapp-capabilities/planned-features
- https://learn.microsoft.com/en-us/dynamics365/release-plan/2026wave1/enterprise-resource-planning/finance-operations-crossapp-capabilities/planned-features

---

## 23. What's new or changed in the UI, 2025 to 2026 (10.0.41 to 10.0.50; release waves)

**Finding: Microsoft has announced no new navigation model or "modern UI" redesign for the core F&O web client in this period.** The core UI pages (UI elements, navigation, shortcuts, lookups) have only had editorial revisions. The visible user-facing change is **Immersive Home**; the rest is Copilot and agents.

| Version / wave | User-interface items (platform) | Source |
|---|---|---|
| 10.0.41 | Deep link to F&O records from Dataverse virtual entities. | whats-new-platform-updates-10-0-41 |
| 10.0.42 | Adaptive Card controls on forms (developer; used by Immersive Home style experiences). | -10-0-42 |
| 10.0.43 | HTML editor control upgraded to CKEditor 5 (on by default from 10.0.44, then mandatory); User security governance (admin). | -10-0-43 |
| 10.0.44 | Minimum version for **Immersive Home** (per its article). No UI items in the platform notes. | -10-0-44; immersive-home |
| 10.0.45 | Copilot: add file and screenshot attachments to a Copilot chat (Feature management). | -10-0-45 |
| 10.0.46 | Interactive query timeout reduced from 30 to 5 minutes (long-running interactive queries now time out sooner). | -10-0-46 |
| 10.0.47 (Mar 2026) | ERP MCP data tools; batch history logging. No end-user UI items. | -10-0-47 |
| 10.0.48 (Jun 2026) | ERP MCP deep links and attachments. No end-user UI items. | -10-0-48 |
| 10.0.49 (Sep 2026) | ERP MCP enhancements (agents only). No end-user UI items. | -10-0-49 |
| 10.0.50 (preview Oct 2026, GA Dec 2026) | Developer (X++) items only. | -10-0-50 |
| 2025 wave 1/2 | Immersive Home and adaptive experiences: preview 6 Jun 2025, **GA 13 Mar 2026** (admin-enabled). | release plan |
| 2026 wave 1 | Copilot client actions, Copilot Cowork, MCP, deep links from Copilot responses. No core UI items. | release plan |
| 2026 wave 2 | **No 2026 wave 2 release plan exists on Learn** (the URL returns 404). All release plans were **archived in October 2026**; Microsoft now points to the roadmap at https://aka.ms/AIatWorkRoadmap. | release-plan index |

**Deprecated or removed items a new-user guide should not mention as current:**
- **Key Tips** (Alt + letters on the Action Pane): replaced by Action search.
- Typing **\*** to open a lookup: deprecated.
- **Panorama** (horizontally scrolling) workspaces: removed from the Operational workspace pattern in 10.0.25, deprecated in 10.0.29.
- **User avatar** photo: removed in 10.0.17; initials are shown.
- **Internet Explorer 11**: unsupported since August 2021; use Microsoft Edge.
- **Finance and operations (Dynamics 365) mobile app**: deprecated June 2022, end of support October 2024 (Power Apps replaces it).
- **Follow-up questions in the Copilot sidecar (preview)**: removed September 2026.
- **Online users** page (admin): legacy, to be removed.

**Sources:**
- https://learn.microsoft.com/en-us/dynamics365/fin-ops-core/fin-ops/get-started/whats-new-platform-updates-10-0-41 through -10-0-50
- https://learn.microsoft.com/en-us/dynamics365/finance/get-started/whats-new-changed-10-0-47 through -10-0-50 (Finance app notes; no core UI items)
- https://learn.microsoft.com/en-us/dynamics365/fin-ops-core/fin-ops/get-started/removed-deprecated-features-platform-updates (revised 25 Aug 2026)
- https://learn.microsoft.com/en-us/dynamics365/release-plan/

---

## 24. Feature management (awareness only)

**What it is.** The admin workspace where new features are turned on. A new user doesn't use it. It matters for the guide because some behaviours depend on features being on. Features in this area: **Immersive Home**; **Standardize keyboard interaction for combo box and lookup controls**; **Streamline tabbing behavior in full-page forms**; **Enable system notification management**; **Auto-blocking of high-volume notification rules**; the new grid control (grid research area). Before writing steps, confirm with the system owner which of these are on.

**Source:** https://learn.microsoft.com/en-us/dynamics365/fin-ops-core/fin-ops/get-started/feature-management/feature-management-overview

---

## Suggested Getting Started topics from this area (ranked)

**Must-have**
1. **Find your way around the screen** (navigation bar, navigation pane, Action Pane, page, FactBoxes, FastTabs): the vocabulary every other guide uses; without it, steps like "On the Action Pane, select…" mean nothing.
2. **Open pages: navigation pane, modules and navigation search**: every procedure guide starts with a navigation path. Search (Ctrl+/ or Alt+G) is the fastest route for new users. Include the 10-result limit and that it finds pages, not data.
3. **Check and change the company (legal entity)**: posting in the wrong company is a high-impact error. Users must know the picker and their default company.
4. **View mode and Edit mode; create, save, revert and delete records**: the first thing new users get stuck on, and the basis of every data-entry step.
5. **Read system messages (message bar, message boxes, Action center)**: users must recognise errors and warnings and know that batch results arrive in the Action center.
6. **Workspaces, tiles and the dashboard (or Immersive Home, if enabled)**: most O2C/P2P/R2R guides start from a workspace. Users need to read summary tiles, lists and links.
7. **Enter values with lookups and date pickers**: type-ahead, name-or-ID entry and the column filter in a lookup speed up every transaction guide.

**Should-have**
8. **Set your User options**: initial page, default company, language, date/number format and time zone (for consistent dates across regions), plus theme and size.
9. **Favorites and Recent**: quick access to frequently used pages (taught here per D-084).
10. **List pages and views (Grid, Details, Header, Lines; navigation list; hyperlinks/View details)**: needed to follow guides for orders, journals and customer/vendor records.
11. **Action search**: runs any Action Pane button by name; very useful when an action is buried in a tab. Note the Ctrl+' vs Ctrl+/ discrepancy.
12. **Keyboard shortcuts quick reference** (one-page table plus Alt+Shift+K): high value for heads-down AP/AR data entry.
13. **Change the session date**: R2R and period-end users need it, but also a risk to flag (reset it; company policy).

**Nice-to-have**
14. **Open in new window (side by side)**: helpful for journals and lines; needs pop-ups allowed in the browser.
15. **Accessibility options** (enhanced tab sequence, tooltips on focus, high contrast, zoom).
16. **Session timeout and unsaved changes**: short note: save before leaving the desk; watch for the countdown.
17. **Right-click menus and the client FAQ**: browser vs app menu; trusted-site fix for missing symbols.
18. **What's new / feature callouts**: how to dismiss and reset callouts; a short "what changed recently" note (Immersive Home, Copilot icon).

Open points to confirm in the company's environment before drafting: whether Immersive Home is on; the **Default view/edit mode** values; whether the lookup keyboard feature is on; save behaviour when navigating away; which colour theme and size to show in screenshots; the browser pop-up policy for `*.dynamics.com`.

---

## All URLs consulted

Product documentation (fin-ops-core/fin-ops):
- https://learn.microsoft.com/en-us/dynamics365/fin-ops-core/fin-ops/get-started/user-interface-elements
- https://learn.microsoft.com/en-us/dynamics365/fin-ops-core/fin-ops/get-started/default-dashboard
- https://learn.microsoft.com/en-us/dynamics365/fin-ops-core/fin-ops/copilot/immersive-home
- https://learn.microsoft.com/en-us/dynamics365/fin-ops-core/fin-ops/get-started/set-users-initial-page
- https://learn.microsoft.com/en-us/dynamics365/fin-ops-core/fin-ops/get-started/accessibility-features
- https://learn.microsoft.com/en-us/dynamics365/fin-ops-core/fin-ops/get-started/client-faq
- https://learn.microsoft.com/en-us/dynamics365/fin-ops-core/fin-ops/get-started/action-search
- https://learn.microsoft.com/en-us/dynamics365/fin-ops-core/fin-ops/get-started/configure-filter-workspaces
- https://learn.microsoft.com/en-us/dynamics365/fin-ops-core/fin-ops/get-started/display-pages-side-by-side
- https://learn.microsoft.com/en-us/dynamics365/fin-ops-core/fin-ops/get-started/shortcut-keys
- https://learn.microsoft.com/en-us/dynamics365/fin-ops-core/fin-ops/get-started/navigation-search
- https://learn.microsoft.com/en-us/dynamics365/fin-ops-core/fin-ops/get-started/use-lookups-to-find-information
- https://learn.microsoft.com/en-us/dynamics365/fin-ops-core/fin-ops/get-started/tasks/change-banner-or-logo
- https://learn.microsoft.com/en-us/dynamics365/fin-ops-core/fin-ops/get-started/help-overview (checked for cross-reference only)
- https://learn.microsoft.com/en-us/dynamics365/fin-ops-core/fin-ops/get-started/feature-management/feature-management-overview
- https://learn.microsoft.com/en-us/dynamics365/fin-ops-core/fin-ops/organization-administration/tasks/change-date-session
- https://learn.microsoft.com/en-us/dynamics365/fin-ops-core/fin-ops/organization-administration/tasks/set-users-preferred-time-zone
- https://learn.microsoft.com/en-us/dynamics365/fin-ops-core/fin-ops/copilot/copilot-for-finance-operations
- https://learn.microsoft.com/en-us/dynamics365/fin-ops-core/fin-ops/copilot/copilot-chat (404, not found)
- https://learn.microsoft.com/en-us/dynamics365/fin-ops-core/fin-ops/get-started/whats-new-changed
- https://learn.microsoft.com/en-us/dynamics365/fin-ops-core/fin-ops/get-started/whats-new-platform-updates-10-0-41
- https://learn.microsoft.com/en-us/dynamics365/fin-ops-core/fin-ops/get-started/whats-new-platform-updates-10-0-42
- https://learn.microsoft.com/en-us/dynamics365/fin-ops-core/fin-ops/get-started/whats-new-platform-updates-10-0-43
- https://learn.microsoft.com/en-us/dynamics365/fin-ops-core/fin-ops/get-started/whats-new-platform-updates-10-0-44
- https://learn.microsoft.com/en-us/dynamics365/fin-ops-core/fin-ops/get-started/whats-new-platform-updates-10-0-45
- https://learn.microsoft.com/en-us/dynamics365/fin-ops-core/fin-ops/get-started/whats-new-platform-updates-10-0-46
- https://learn.microsoft.com/en-us/dynamics365/fin-ops-core/fin-ops/get-started/whats-new-platform-updates-10-0-47
- https://learn.microsoft.com/en-us/dynamics365/fin-ops-core/fin-ops/get-started/whats-new-platform-updates-10-0-48
- https://learn.microsoft.com/en-us/dynamics365/fin-ops-core/fin-ops/get-started/whats-new-platform-updates-10-0-49
- https://learn.microsoft.com/en-us/dynamics365/fin-ops-core/fin-ops/get-started/whats-new-platform-updates-10-0-50
- https://learn.microsoft.com/en-us/dynamics365/fin-ops-core/fin-ops/get-started/removed-deprecated-features-platform-updates

Developer / IT pro documentation (fin-ops-core/dev-itpro):
- https://learn.microsoft.com/en-us/dynamics365/fin-ops-core/dev-itpro/get-started/personalize-user-experience
- https://learn.microsoft.com/en-us/dynamics365/fin-ops-core/dev-itpro/user-interface/page-navigation
- https://learn.microsoft.com/en-us/dynamics365/fin-ops-core/dev-itpro/user-interface/page-layout
- https://learn.microsoft.com/en-us/dynamics365/fin-ops-core/dev-itpro/user-interface/messaging-user
- https://learn.microsoft.com/en-us/dynamics365/fin-ops-core/dev-itpro/user-interface/messaging-api-center-bar-details
- https://learn.microsoft.com/en-us/dynamics365/fin-ops-core/dev-itpro/user-interface/feature-callouts
- https://learn.microsoft.com/en-us/dynamics365/fin-ops-core/dev-itpro/user-interface/slider-messagebox
- https://learn.microsoft.com/en-us/dynamics365/fin-ops-core/dev-itpro/user-interface/system-defined-buttons
- https://learn.microsoft.com/en-us/dynamics365/fin-ops-core/dev-itpro/user-interface/form-styles-patterns
- https://learn.microsoft.com/en-us/dynamics365/fin-ops-core/dev-itpro/user-interface/list-page-form-pattern
- https://learn.microsoft.com/en-us/dynamics365/fin-ops-core/dev-itpro/user-interface/details-master-form-pattern
- https://learn.microsoft.com/en-us/dynamics365/fin-ops-core/dev-itpro/user-interface/details-transaction-form-pattern
- https://learn.microsoft.com/en-us/dynamics365/fin-ops-core/dev-itpro/user-interface/workspace-form-pattern
- https://learn.microsoft.com/en-us/dynamics365/fin-ops-core/dev-itpro/user-interface/general-form-guidelines
- https://learn.microsoft.com/en-us/dynamics365/fin-ops-core/dev-itpro/user-interface/lookups-controls
- https://learn.microsoft.com/en-us/dynamics365/fin-ops-core/dev-itpro/user-interface/contextual-data-entry-lookups
- https://learn.microsoft.com/en-us/dynamics365/fin-ops-core/dev-itpro/user-interface/create-deep-links
- https://learn.microsoft.com/en-us/dynamics365/fin-ops-core/dev-itpro/user-interface/client-disconnected
- https://learn.microsoft.com/en-us/dynamics365/fin-ops-core/dev-itpro/sysadmin/session-idle-timeout

Finance app what's new:
- https://learn.microsoft.com/en-us/dynamics365/finance/get-started/whats-new-changed-10-0-47
- https://learn.microsoft.com/en-us/dynamics365/finance/get-started/whats-new-changed-10-0-48
- https://learn.microsoft.com/en-us/dynamics365/finance/get-started/whats-new-changed-10-0-49
- https://learn.microsoft.com/en-us/dynamics365/finance/get-started/whats-new-changed-10-0-50

Release plans:
- https://learn.microsoft.com/en-us/dynamics365/release-plan/
- https://learn.microsoft.com/en-us/dynamics365/release-plan/2025wave1/finance-supply-chain/finance-operations-crossapp-capabilities/planned-features
- https://learn.microsoft.com/en-us/dynamics365/release-plan/2025wave2/enterprise-resource-planning/finance-operations-crossapp-capabilities/planned-features
- https://learn.microsoft.com/en-us/dynamics365/release-plan/2025wave2/enterprise-resource-planning/finance-operations-crossapp-capabilities/stay-focused-simplify-tasks-immersive-home-adaptive-experiences
- https://learn.microsoft.com/en-us/dynamics365/release-plan/2026wave1/enterprise-resource-planning/finance-operations-crossapp-capabilities/planned-features
- https://learn.microsoft.com/en-us/dynamics365/release-plan/2026wave2/ (404, not published)
- https://learn.microsoft.com/en-us/dynamics365/release-plan/2026wave2/enterprise-resource-planning/finance-operations-crossapp-capabilities/planned-features (404)

Microsoft Learn training:
- https://learn.microsoft.com/en-us/training/paths/get-started-finance-operations/
- https://learn.microsoft.com/en-us/training/modules/navigate-finance-operations/ (units 1-introduction, 2-navigation-elements, 3-workspaces-driving-productivity, 5-searching, 6-comparing-views, 7-view-and-edit-mode)
- https://learn.microsoft.com/en-us/training/modules/describe-finance-operations-apps/ (units 3-describe-use-cases-ai-tools, 4-explore-user-interface)

Search API used for discovery: https://learn.microsoft.com/api/search (queries on view/edit mode, company picker, dark mode, save behaviour, natural-language search, Action center; few relevant hits).

Raw page captures (Markdown) are in `raw-ui/`.
