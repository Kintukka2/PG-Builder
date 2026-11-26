# C. Data in and out, documents, reports, background work and alerts (Microsoft documentation inventory)

Research area C for the **D365 F&O Getting Started** guide discovery. Written 26 November 2026 from the current Microsoft Learn sources: the public docs repository `MicrosoftDocs/dynamics-365-unified-operations-public` (main branch, read on this date), live learn.microsoft.com pages, and Microsoft Learn training modules. The point of view is the end user (finance staff in O2C, P2P, R2R and Tax). Admin setup is noted only where a user depends on it.

Screenshots are in `media/office-reports-batch/` (44 files, listed per feature). Other teams cover navigation and the UI shell; grids, filters, personalization and views; and workflow, help and Copilot. Those topics appear here only as cross-references.

**What the ms.date values mean.** Each article carries an `ms.date` (its last review). Most articles in this area were reviewed in 2025 or 2026, so they are current. The exceptions are noted.

**The documentation gaps that matter most for a Getting Started guide.** Microsoft has no current end-user article for these. Each is pieced together from secondary sources, marked below:

1. The standard **report dialog**: **Parameters**, **Destination** > **Change**, **Records to include** and **Run in the background**.
2. **Print destination settings**: **Print archive**, **Screen**, **Printer**, **File** and **Email**.
3. The **Print archive**.
4. **My batch jobs**.
5. The **Infolog / Message details** pane.
6. **Print management** setup for documents.

The only current-platform walkthrough of the report dialog and Print archive is an archived Microsoft BI team blog post from 2018, which includes screenshots. The rest is mentioned in passing in module articles. Plan to capture these with screenshots from our own environment (the clean-session test).

---

## 1. The Open in Microsoft Office menu (overview)

**What it is.** A button on the Action Pane of most list and details pages (the Office icon). It groups three kinds of option:
- **Export to Excel**: a static export of a visible grid.
- **Open in Excel**: a live workbook connected through the Excel add-in. It is either *generated* (from a data entity) or a *template* (from Document templates).
- **Export to Word**: a document generated from a Word template.

**Key concepts (as documented):**
- **Export to Excel** "options are static exports of grid data. Each one corresponds to a visible grid. All the grid data for the current filter is placed into a workbook."
- **Open in Excel** experiences "utilize the Excel Add-in to facilitate refresh and publish."
- A *generated* Open in Excel option appears when a data entity has the same root data source (table) as the page. These options show "(unfiltered)" after the entity name because the page's filter is not carried into the workbook.
- An option appears only if the user has security access to the underlying entity. Per D-083, the guide says only that a missing option is a BAU Support matter.
- A *template* option appears when a template in **Common > Common > Office integration > Document templates** has *ShowInOpenInOfficeMenu* = Yes and the same root data source. **Apply current record filter** and **Apply company filter** on the template control the filtering.
- Some pages have an explicit button instead, for example **Open lines in Excel** on the General journal (see section 4).
- Since 10.0.49, the Office menu button is no longer expanded when a form opens; it expands only when clicked. Microsoft describes this as an agent (MCP) performance change. No visible change for users is documented.

**Screenshots:**
- `open-in-office-menu-export-vs-open-in-excel.png`: the menu showing a template Open in Excel option, a generated one and a static Export to Excel.
- `office-open-in-office-menu-training.png`
- `office-document-templates-page.png`

**Sources:**
- https://learn.microsoft.com/en-us/dynamics365/fin-ops-core/dev-itpro/office-integration/office-integration-edit-excel (ms.date 01/23/2025)
- https://learn.microsoft.com/en-us/dynamics365/fin-ops-core/dev-itpro/office-integration/office-integration-tutorial (03/17/2026)
- https://learn.microsoft.com/en-us/training/modules/implement-common-integration-features-finance-ops/2-office

---

## 2. Export to Excel (static export)

**What it is.** A one-way copy of the rows in a grid, exactly as shown (the current columns and current filter), into a new .xlsx file. It cannot be refreshed or published back.

**End-user steps (tutorial):**
1. Open the list page, for example **Accounts receivable > Customers > All customers**.
2. Select **Open in Microsoft Office** > **Export to Excel** > *grid name* (for example **Customers**).
3. Download and open the workbook. The workbook columns match the grid columns.

**Alternatives (shortcut menu on the grid):**
- Mark rows using the check column, right-click the grid header and select **Export marked rows**.
- Select **Export all rows** from the same menu.
- Keyboard shortcut: **Ctrl+Shift+E** (Export to Excel, from the shortcut keys article).

**Limits and gotchas:**
- **Row limit.** The default maximum is **50,000 rows**. An administrator can raise it up to **1,000,000** at **System administration > Setup > Client performance options** > **Maximum number of rows to export to Excel**. The default value of 0 means 50,000.
  - Microsoft "**strongly recommend[s]** that you **not** raise this limit above 100,000 records", because of memory risk on the servers.
  - History: the limit was 2,000 before Platform update 7, then 10,000, then configurable up to 1 million from Platform update 22.
- **Download time limit.** The download link must be used within **15 minutes**. Microsoft recommends Edge or Chrome with automatic download turned on.
  - The developer messaging API shows an "Export to Excel finished" notification in the **Action center** with a **Click to download** link that expires after 48 hours. This is a developer example, not a guaranteed user behaviour.
- **Speed.** Export to Excel is slower than OData-based options and memory-intensive. It is "not intended for auditing purposes". For very large data sets Microsoft recommends Data management (section 21).
- **When it is the right tool.** It returns data "exactly as it's shown in the grid", including calculated (display) columns, formatted values and temporary-table data, which Open in Excel cannot give.
- **Microsoft's general guidance:** "The best way for end users to get data out of the system is to use the Excel add-in" (Open in Excel), because it uses entity security and refreshes.
- **Dates.** Exported data is a point-in-time copy. Date and time in the *add-in* are UTC (see section 3); a static export shows what the grid shows.
- **Pasting back.** Copying a table from Excel and pasting it into a grid is supported on the new grid control. That belongs to the grids team; cross-reference only.

**Admin settings and features:** the Client performance options limit only. No feature flag is needed.

**Screenshots:**
- `office-static-export-to-excel-grid-shortcut-menu.png`
- `action-center-export-to-excel-finished-notification.png`

**Sources:**
- https://learn.microsoft.com/en-us/dynamics365/fin-ops-core/dev-itpro/office-integration/office-integration-troubleshooting (09/23/2025), section "Is Export to Excel the best way to get data out of the system?"
- https://learn.microsoft.com/en-us/dynamics365/fin-ops-core/fin-ops/sysadmin/security-gov-security-object-licenses-preview (note on raising the limit)
- https://learn.microsoft.com/en-us/dynamics365/fin-ops-core/dev-itpro/get-started/whats-new-platform-update-22
- https://learn.microsoft.com/en-us/dynamics365/fin-ops-core/dev-itpro/get-started/whats-new-platform-update-7
- https://learn.microsoft.com/en-us/dynamics365/fin-ops-core/fin-ops/get-started/shortcut-keys
- https://learn.microsoft.com/en-us/dynamics365/fin-ops-core/dev-itpro/user-interface/messaging-api-center-bar-details
- https://learn.microsoft.com/en-us/dynamics365/fin-ops-core/dev-itpro/get-started/grid-capabilities (pasting from Excel; grids team)

---

## 3. Open in Excel with the Microsoft Dynamics Office Add-in (Excel Data Connector)

**What it is.** A workbook bound to a data entity through OData. The **Microsoft Dynamics Office Add-in** runs in a task pane on the right of Excel. In it the user can **Refresh** data, edit cells, add and delete rows, and **Publish** the changes back to D365. Lookups, enum lists and date pickers appear in the pane.

**Requirements:**
- Excel 2016 or later (ExcelAPI 1.2). Excel for the web also works.
- **Not supported on Office for Mac.**
- The internet is needed, because the add-in loads from Microsoft content delivery networks.

### 3.1 Open from D365 (the normal user path)
1. On a page, select **Open in Microsoft Office**.
2. Select an **Open in Excel** option and open the generated workbook. The workbook holds the entity binding, a pointer to the environment and a pointer to the add-in.
3. In Excel, select **Enable editing** so the add-in can run.
4. The first time, select **Trust this Add-in**.
5. If prompted, select **Sign in** with the same credentials as D365. The add-in reuses the browser sign-in where it can. Check the user name in the upper-right corner of the add-in.
6. The add-in reads the data. "The workbook contains no data until the Excel add-in reads it in."

You can also save the workbook to SharePoint (**SharePoint** > browse > **Save**) and work in Excel for the web, where refresh, publish and design work the same way.

### 3.2 Start from Excel (power users)
1. In Excel, select **Insert** > **Add-ins** > **Store**.
2. Search for **Dynamics** and select **Add** next to **Microsoft Dynamics Office Add-in**.
3. Select **Trust this Add-in**, then **Add server information**.
4. Paste the environment URL into **Server URL**, keeping only the host name, for example `https://xxx.dynamics.com`.
5. Select **OK**, then **Yes**.
6. Select **Design** > **Add table**, choose the entity ("Name - Label" format), and move fields from **Available fields** to **Selected fields** (**Add**, or double-click).
7. Select **Done**, then **Done** again, then **Refresh**.

### 3.3 Task pane elements (documented names)
- **Source name** and **Field name**: hover over them to see the technical names.
- **Refresh**, **Publish**, **Design**, **New**, **Filter**.
- **Options** (gear).
- **Messages**: a dialog that shows info, warnings and errors, with a count badge. The tutorial also calls it the **Message Center** (flag button).
- The status bar.
- The Office Web Add-ins menu, which has a "reload" link that reloads all data.

### 3.4 Edit and publish
- **Edit:** change a cell value, then select **Publish**. The **Messages** dialog reports how many records were added, edited and deleted.
- **Add a row:** select **New**, or Tab out of the last cell of the last row, or type in the row directly under the table. For header fields, select a header field and then **New**.
- **Create a record:** the workbook must bind all **key** fields (key symbol) and **mandatory** fields (asterisk), or have them defaulted by a filter.
- **Delete:** right-click the row number > **Delete**, or right-click in the row > **Delete** > **Table Rows**.
- **Filters:** remove Excel column filters before publishing ("The filters must be removed before data changes are published").
- **Publish unavailable:** hover over **Publish** to see the reason. It is usually missing key or mandatory fields.
- **Publish order:** a header publishes before its lines. To change the order, select **Options** > **Data Connector** > **Configure publish order**.
- **Leading zeros:** set string header cells to Text format, or "00045" becomes 45 and a key-field error follows.

### 3.5 Add or remove columns
1. Select **Design**. If it is missing, select **Options** > **Enable design**.
2. Select the pencil (**Edit**) next to the data source.
3. Use **Add** or **Remove** (or double-click) and **Up** or **Down**. **Column label** renames a column.
4. Select **Update**, then **Done**, then **Refresh**.

Data sources cannot be removed from a workbook, only added.

### 3.6 Settings and limits
- **Publish batch size.** The default and maximum is 100 rows per batch.
  - Feature: **Allow configuration of the publish batch size in the Excel add-in**.
  - Admin: **Office app parameters** > **App parameters** > **Publish batch limit**.
  - User: **Options** > **Publish batch size**, then **save the workbook**, or the setting is lost.
  - Lowering it is the fix for publish time-outs.
- **Cell limit.** A data governor of about **1 million cells** by default, which can be extended to about 2.5 million on a fast machine. Use filters to work in smaller pieces.
- **Refresh on open:** **Options** > **Data Connector** > **Refresh Options** > **Refresh on open**. Old templates need this turned on.
- **Copy Environment Data:** **Options** > **Data Connector** > **Copy Environment Data**, which publishes the rows to another environment as new data. Mainly for admins and testers.
- **Date and time values in the add-in are UTC** (no client time-zone adjustment).
- **Clear binding data:** **Options** > **Data Connector** > **Clear binding data**, used before saving a workbook as a template.

### 3.7 Sign-in and troubleshooting (user-facing)
- **"Load applets" shown instead of data.** Usually the wrong account. Sign out from the user menu in the upper right and sign back in. If that fails, an admin re-initializes the **Office app parameters** tabs (**Initialize**); otherwise contact Support with the **Application correlation ID** from **Options**.
- **"Forbidden".** The wrong user is signed in, or the user has no access. Sign out and back in. Per D-083, the guide sends the user to BAU Support.
- **Blank sign-in page.** Update Excel. An AD FS tenant needs a recent Office build; VPN or proxy settings can also block the required URLs.
- **AADSTS50058 "silent sign in failed".** The token expired. Sign out and sign in again.
- **AADSTS50020 for external users.** They must be invited to the tenant as Entra B2B guests.
- **"Record for Id {guid} not found" on a template.** Templates were not copied after a database move. An admin deletes and reloads the template in **Document templates**.
- **Publishing is slow.** Microsoft suggests Fiddler, which is a developer tool. For users: reduce the batch size or filter the data.
- **Centralized deployment** of the add-in is supported. Admins set the App ID, Store and Store Type on **Office app parameters**.

**Screenshots:**
- `excel-addin-journal-entry-task-pane.png`
- `excel-addin-design-button.png`
- `excel-addin-edit-datasource-pencil.png`
- `excel-addin-add-fields.png`
- `excel-addin-refresh.png`
- `office-excel-data-connector-addin.png`

**Sources:**
- https://learn.microsoft.com/en-us/dynamics365/fin-ops-core/dev-itpro/office-integration/use-excel-add-in (the repository file is `fin-ops/mobile-apps/use-excel-add-in.md`, title "View and update entity data with Excel", 12/31/2024)
- https://learn.microsoft.com/en-us/dynamics365/fin-ops-core/dev-itpro/office-integration/office-integration (01/03/2025)
- https://learn.microsoft.com/en-us/dynamics365/fin-ops-core/dev-itpro/office-integration/office-integration-edit-excel
- https://learn.microsoft.com/en-us/dynamics365/fin-ops-core/dev-itpro/office-integration/office-integration-troubleshooting
- https://learn.microsoft.com/en-us/dynamics365/fin-ops-core/dev-itpro/office-integration/office-integration-tutorial
- Video: https://youtu.be/RTicLb-6dbI ("Create an Excel template for header and line patterns")

---

## 4. Open lines in Excel for journals and documents (finance-specific Excel templates)

**What it is.** Template-based Open in Excel buttons on journals, so that users can enter many lines in Excel and publish them. This matters a lot for R2R, AP and AR users.

**Steps (tutorial, General journal):**
1. Go to **General ledger > Journal entries > General journals** and create the journal header (**New**, choose the **Name**).
2. Select **Open lines in Excel**, then open the workbook and enable editing. The header fields are filled in.
3. Enter lines. Lookups appear for company, currency and so on.
4. Select **Publish**.
5. Back in D365, select **Lines** to see the lines.

The lines are validated against the journal rules on publish. Users then edit or post the vouchers in D365.

**Templates and where to find them:**

| Template | Account types | Where |
|---|---|---|
| Ledger journal lines | Ledger, Customer, Vendor, Bank (account and offset); intercompany supported | General journal |
| Invoice register | Vendor / Ledger; no intercompany | AP invoice register |
| Invoice journal | Vendor / Ledger; intercompany supported | AP invoice journal |
| Vendor invoice | | Vendor invoice |
| Customer invoice journal | Customer / Ledger | General journal |
| Free text invoice | | **Free text invoice** page > **Open in Excel** (Office icon) |
| Fixed assets journal | Asset to ledger, bank, customer or vendor; no intercompany | Fixed asset journal |
| Vendor payment journal | Vendor / Ledger, Bank | Vendor payment journal |
| Customer payment journal | Customer / Ledger, Bank | Customer payment journal |
| Project expense journal | Project, Ledger, Customer, Vendor | General journal Expense |

**Gotchas:**
- Financial dimensions in templates need entity changes. That is a developer task (Add dimensions to the Excel template).
- Lookups for ledger dimensions need relationships on the dimension entities.

**Sources:**
- https://learn.microsoft.com/en-us/dynamics365/finance/general-ledger/open-lines-excel-journals-documents (07/30/2026)
- https://learn.microsoft.com/en-us/dynamics365/fin-ops-core/dev-itpro/financial/add-dimensions-excel-templates
- https://learn.microsoft.com/en-us/dynamics365/fin-ops-core/dev-itpro/user-interface/add-templates-open-lines-excel-menu (developer)

---

## 5. Excel templates: Document templates and Excel workbook designer (admin and power user; brief)

- **Excel workbook designer:** **Common > Common > Office integration > Excel workbook designer**.
  - Pick an entity and fields, then select **Create workbook**. **Create blank workbook** gives just the add-in and the server pointer.
  - Other buttons: **View related form**, **Get entity record count**.
  - Key fields show a key symbol and mandatory fields an asterisk.
- **Document templates:** **Common > Common > Office integration > Document templates**.
  - Upload templates with **New** > browse. Set **Template display name**, **Apply current record filter** and **Apply company filter**.
  - **Reload system templates** restores the Microsoft templates.
  - To change a template: download it, edit it in the add-in, use **Clear binding data**, save it, and upload it under the same name (remove the `_<number>` suffix).
- **When to create a template:** when you need extra content or formatting, or several entities in one workbook. Not when a field list alone is enough.
- **Users can keep a personal template** by saving a designed workbook to their own computer and reusing it. Microsoft notes this explicitly.

**Screenshot:** `office-document-templates-page.png`

**Sources:**
- https://learn.microsoft.com/en-us/training/modules/implement-common-integration-features-finance-ops/3-excel
- https://learn.microsoft.com/en-us/dynamics365/fin-ops-core/dev-itpro/office-integration/office-integration-edit-excel
- https://learn.microsoft.com/en-us/dynamics365/fin-ops-core/dev-itpro/office-integration/customize-open-office-menu (developer)

---

## 6. Export to Word

**What it is.** Lightweight reporting: a Word document generated from an uploaded Word template, filled with the selected record.

**Steps:**
1. On the page, select **Open in Microsoft Office** > **Export to Word** > *template*.
2. Download and open the document. It contains data from the currently selected record.

**Templates (power user or admin):**
- Create a blank document from **Excel workbook designer** > **Create blank document**.
- In Word, the Dynamics add-in offers **Design** > **Add fields** or **Add table**, with **Add label** and **Add value**.
- Upload the template in **Document templates**.

Few standard Export to Word templates exist, so for most finance users this is a "nice to know".

**Source:** https://learn.microsoft.com/en-us/dynamics365/fin-ops-core/dev-itpro/office-integration/office-integration-tutorial ("Export to Word experiences")

---

## 7. Attachments (document management, also called "document handling")

**What it is.** Notes, files, images and URLs attached to any record. Users open them with the **Attach** button (paperclip) in the upper right of most pages that hold data. The two names refer to the same function.

**End-user steps:**
1. Select the record, then select **Attach** (paperclip) or press **Ctrl+Shift+A**. The **Attachments** page opens for the data source of the control that has focus. On header and lines pages, put the focus on the right part of the page first.
2. Select **New** (**+**) and choose a document type: **File**, **Image**, **Note**, **URL**, or a custom type. For File and Image you are prompted for the file (**Browse**).
3. The **Preview** FastTab shows a preview. The **Attachment** FastTab shows the details and file location.
4. **Open** opens a URL attachment on a new tab.

**Key concepts:**
- **Badge count.** The **Attach** button shows the number of attachments for the current record: an exact count from 0 to 9, then **9+**.
- **Document types and classes.** Each type has a class:
  - **Attach file**: prompts for a file.
  - **Attach URL**: the URL goes in **Notes**.
  - **Simple note**: text in **Notes**.
  - The defaults are File, Image, Note and URL. File and Image use **Azure storage**.
  - Custom types can store files in **SharePoint** folders, for example per-team folders.
- **Storage.** Azure Blob storage is the default. SharePoint Online is supported. Database storage is obsolete.
- **File types allowed** are controlled by the admin on **Document management parameters** > **File types**.
- **Maximum file size** is set by the admin (**Maximum file size in megabytes**). For the SharePoint document type the cap is **262 MB**.
- **Previews.** Supported: images, text, PDF, and Office files through the cloud WOPI (Office Online) server. Previews do not work where an IP allow list is enabled. SharePoint previews use the current user's permissions.
- **Open attachments in new window** (admin, **Document management parameters** > **General**). Recommended with SharePoint, because otherwise opening an attachment can reset the D365 session.
- **Deleted attachments (recycle bin).** When **Deferred deletion enabled** is on (admin; default 30 days):
  - A deletion raises an **Attachment deleted** notification with **undo**.
  - The **Attachments** page has **Deleted attachments** to restore or permanently delete.
  - Admins also have **System administration > Inquiries > Deleted attachments**.
- **Document history.** **Document history** on the Attachments Action Pane shows who created, deleted, restored or moved an attachment. Admins turn it on (**Enable document history**; 180-day retention).
- **Turning attachments off.** A user can disable document handling at **Settings > User options > Preferences** > **Enable document handling**. Older docs call this **Document handling active**; if a user says the Attach button "disappeared", check this first.
- **Virus scanning.** Not provided out of the box. Extension points exist (developer).
- **Export attachments** (10.0.40 and later; admin, batch):
  - Path: **Organization administration > Document management parameters > Export attachments**.
  - Per table, with **From date** / **To date**, **Include metadata** and **Run in the background**.
  - It produces zip archives attached to the setup rows.
- **Document management vs print management.** Document management attaches notes and files to records. Print management controls print settings (copies, printer destination, multilanguage text) for selected reports.
- **Printed invoices as attachments.** The feature **Archive printed customer invoices with hash numbers** plus the customer's **eInvoice attachment** = Yes saves printed invoices as attachments, with a document hash number. This is a legal or country requirement; mention only if it applies.
- **Deprecated:** the "Show related document attachments" feature, because it returned unexpected results.
- **SharePoint authentication** (admin): the **SharePoint user authentication** feature (10.0.40) was mandatory from 10.0.42, and the old connection stopped on 28 February 2025. Interactive access now uses the signed-in user, so **users need SharePoint permission on the folder** for SharePoint-stored attachments.

**Copilot cross-reference** (Copilot team): file and screenshot attachments in the Copilot chat (10.0.45 feature) and ERP MCP attachment support (10.0.48) are separate from record attachments.

**Screenshots:**
- `attachments-export-attachments-page.png`
- `attachments-export-attachments-dialog.png`
- `office-document-templates-page.png` (training)

**Sources:**
- https://learn.microsoft.com/en-us/dynamics365/fin-ops-core/fin-ops/organization-administration/configure-document-management (repository `dev-itpro/organization-administration/configure-document-management.md`, 11/13/2026)
- https://learn.microsoft.com/en-us/dynamics365/fin-ops-core/dev-itpro/organization-administration/maintain-document-management-storage
- https://learn.microsoft.com/en-us/training/modules/implement-common-integration-features-finance-ops/4-documents
- https://learn.microsoft.com/en-us/dynamics365/finance/accounts-receivable/archive-printed-invoices
- https://learn.microsoft.com/en-us/dynamics365/fin-ops-core/fin-ops/get-started/removed-deprecated-features-platform-updates
- https://learn.microsoft.com/en-us/dynamics365/fin-ops-core/dev-itpro/copilot/copilot-attachments
- Video: https://www.youtube.com/watch?v=p4rl1CkiLN4

---

## 8. Email from the app (send a document or statement by email)

**What it is.** Many processes (statements, collection letters, alerts, workflow, report destinations) send email through the SysEmail framework. Which mail route is used depends on admin settings and on the user's choice.

**End-user parts:**
- **The "How would you like to send email" dialog** appears the first time unless a provider is set. The options are:
  - **Use an email app, such as Outlook**: produces an `.eml` file with the attachment, to open and send from Outlook.
  - **Use Exchange email server**: deprecated; it stopped working on 15 September 2024.
  - **Use the system email client**: opens the **Send email** dialog and sends through the server provider (SMTP or Microsoft Graph).
  - **Do not ask again**.
- **Send email dialog:** **From** (from the user options email), **To**, **Cc**, **Bcc**, **Subject**, **Body**, an attachments list, then **Send**.
- **User options:** **Settings > User options** > **Account** tab > **Email provider selection** > **Email provider ID**. Blank means "Prompt for which email provider to use". The **Sender email** override is admin-set.
- **Example path (AR):** **Accounts receivable > Customers > All customers** > select the customer > **Collect** > **Customer balances** > **Collections** > **Communicate** > **Email** > **Statements to contact** > **OK**.
- **Batch and non-interactive email** (report destination Email, alerts, workflow) is sent by the **Email distributor batch** (admin: **System administration > Periodic tasks > Email processing > Batch**). If it is not running, nothing is sent.
- **Microsoft Graph** is the recommended provider (10.0.38 and later). It replaces Exchange.
- SMTP has no MFA or modern auth support.
- Admins review failures in **System administration > Setup > Email > Email history**, with 30-day retention.
- Exchange Online sending limits apply.

**Sources:**
- https://learn.microsoft.com/en-us/dynamics365/fin-ops-core/dev-itpro/organization-administration/configure-email
- https://learn.microsoft.com/en-us/training/modules/implement-common-integration-features-finance-ops/5-emails-exchange
- https://learn.microsoft.com/en-us/dynamics365/fin-ops-core/dev-itpro/office-integration/office-integration-tutorial ("Email experiences")
- https://learn.microsoft.com/en-us/dynamics365/fin-ops-core/fin-ops/get-started/removed-deprecated-features-platform-updates (Exchange provider)

---

## 9. Running an SSRS report: the report dialog

**What it is.** Most reports and documents (trial balance, aged balances, customer statements, invoices) are SQL Server Reporting Services (SSRS) paginated reports. The menu item (usually under *Module* > **Inquiries and reports**) opens a dialog, and the report renders according to the destination chosen.

**Official coverage:** none on current Learn for end users. The steps below come from the archived Microsoft BI team blog (2018, current-platform UI, screenshots), the batch training module, and module articles that refer to the FastTabs.

**The dialog's sections, as shown in the blog screenshot of the Customer base data report:**
- **Parameters**: report-specific options, for example **Include merged customers**.
- **Destination**: shows the current destination (default **Screen**). Select **Change** to open **Print destination settings** (section 10).
- **Records to include**: select **Filter** to restrict the records with the standard query/filter dialog, for example **Customer account** = US-045. The collection letters article uses this exact wording: "On the **Records to include** FastTab, select **Filter**…". Some newer reports show query ranges directly.
- **Run in the background**: **Batch processing** (Yes/No), **Task description**, **Batch group**, **Private**, **Critical Job**, **Monitoring category**, and the **Recurrence** and **Alerts** buttons (section 13).
- **OK** runs the report; **Cancel** closes the dialog.

**Steps to run a report on screen:**
1. Open the report from the menu, for example **Accounts receivable > Inquiries and reports > Customers > Customer base data report**.
2. Fill in **Parameters**.
3. Optionally add filters under **Records to include** > **Filter**.
4. Keep **Destination** = **Screen**.
5. Select **OK**. The report opens in the PDF viewer (section 11).

**Key concepts and gotchas:**
- **Time-outs.** Interactive report generation is limited by service time-outs: 10 minutes for the SSRS data set, per "Help prevent long-running reports from timing out". Separately, from January 2026 the **interactive SQL query time-out was cut from 30 minutes to 5 minutes** (10.0.46 platform change, rolled out globally).
  - **Practical rule for the guide:** run large reports with **Run in the background**, and split large runs into smaller ranges.
- **Drill-through links in printed documents are no longer supported** (security), and drill-through works only in preview. Do not promise users clickable links in the PDFs they save.
- The **SQL Server Reporting Services Reports** technical reference report lists every SSRS report with its data sets and filters. It helps the PG team, not users.
- SSRS reports give "email support, scheduled executions via batches, and print archive functionality".

**Screenshots** (from the archived blog, current UI of 2018):
- `report-dialog-default-destination-screen.png`
- `report-dialog-run-in-background-batch.png`: shows the Parameters, Destination/Change, Records to include and Run in the background labels.

**Sources:**
- https://learn.microsoft.com/en-us/archive/blogs/dynamicsaxbi/viewing-reports-using-non-interactive-options (2018-04-25)
- https://learn.microsoft.com/en-us/dynamics365/finance/accounts-receivable/process-collection-letters-example (Records to include > Filter)
- https://learn.microsoft.com/en-us/dynamics365/finance/general-ledger/general-ledger-statement-by-main-account (Records to include, Run in the background)
- https://learn.microsoft.com/en-us/dynamics365/finance/budgeting/budget-control-account-detail-history-report ("additional report filters on the Records to include tab")
- https://learn.microsoft.com/en-us/dynamics365/finance/accounts-payable/vendor-aging-report ("Current print destination")
- https://learn.microsoft.com/en-us/dynamics365/fin-ops-core/dev-itpro/analytics/prevent-long-running-reports-timing-out (10/27/2025)
- https://learn.microsoft.com/en-us/dynamics365/fin-ops-core/fin-ops/get-started/whats-new-platform-updates-10-0-46 (query time-out change)
- https://learn.microsoft.com/en-us/dynamics365/fin-ops-core/dev-itpro/analytics/SSRS-report
- https://learn.microsoft.com/en-us/dynamics365/fin-ops-core/dev-itpro/analytics/create-nextgen-reporting-solutions
- https://learn.microsoft.com/en-us/training/modules/build-reports-finance-operations/01-ssrs-reports ("print reports to different locations, such as your screen, a printer, a file, or an email")

---

## 10. Print destination settings (Destination) and Print management

**Print destination settings dialog** (opened from **Destination** > **Change**). The left list shows **Print archive**, **Screen**, **Printer**, **File** and **Email**; a **Save in print archive?** toggle sits on the right (blog screenshot).

| Destination | What it does |
|---|---|
| **Screen** | The default. Opens in the in-browser PDF viewer. |
| **Printer** | A network printer registered through the Document Routing Agent and set **Active** by an admin. Only those printers appear. Local printers are used through the PDF viewer's **Print** button instead. |
| **File** | Choose a format (PDF, Word, Excel, and others) and download it. |
| **Email** | Sends the report as an attachment (the batch email distributor must run). |
| **Print archive** | Stores the output in the print archive (section 12). |

**Background runs** cannot go to **Screen** or **File**: "the service prevents users from rendering report to Screen or File when running in the background". Choose **Archive**, **Printer** or **Email**.

**Print management** (for business documents: invoices, statements, purchase orders). This is *document* setup, at module level with overrides at account or transaction level, for copies, destination and footer text. It is documented on current Learn only in passing:
- "Print management lets you control print settings for selected reports. Print settings include the number of copies, the printer destination, and the multilanguage text that can be included on the report" (Configure document management FAQ).
- Posting dialogs have **Use print management destination**, which uses "the print settings that you specify for the transaction, document, or module on the **Print management setup** page" (Configure customer invoices).
- Configurable business documents: "for a preview, the scenario Preview/Print > Original can be used, and for email and printing, Preview/Print > Use print management can be used".

The detailed Print management setup guide exists only for **AX 2012**, which is legacy and not current; use it for concepts only.

**Network printing (admin):**
- Install the **Document Routing Agent** (DRA) from **Organization administration > Setup > Network printers** > **Options** > **Download document routing agent installer**, then register printers in the DRA.
- The admin sets **Active** = Yes on **Network printers**.
- Network printer settings are company-specific, so a printer can be available in one legal entity and not another.
- Known issue: barcodes can print as plain text through the DRA. The workaround is to print to screen, then print the preview.

**Sources:**
- https://learn.microsoft.com/en-us/archive/blogs/dynamicsaxbi/viewing-reports-using-non-interactive-options
- https://learn.microsoft.com/en-us/dynamics365/fin-ops-core/dev-itpro/analytics/print-documents (10/27/2025)
- https://learn.microsoft.com/en-us/training/modules/implement-common-integration-features-finance-ops/8-network-print
- https://learn.microsoft.com/en-us/dynamics365/fin-ops-core/dev-itpro/analytics/install-document-routing-agent
- https://learn.microsoft.com/en-us/dynamics365/fin-ops-core/dev-itpro/sysadmin/sys-admin-tools-network-printer
- https://learn.microsoft.com/en-us/dynamics365/finance/accounts-receivable/configure-customer-invoices
- https://learn.microsoft.com/en-us/dynamics365/fin-ops-core/fin-ops/organization-administration/configure-document-management (FAQ)
- AX 2012, legacy concepts only: https://learn.microsoft.com/en-us/dynamicsax-2012/appuser-itpro/about-print-management-document-types-and-modules
- Release plans: https://learn.microsoft.com/en-us/dynamics365-release-plan/2021wave2/finance-operations/dynamics365-finance/configurable-business-documents--specific-destinations-via-printer-management-settings ; https://learn.microsoft.com/en-us/dynamics365-release-plan/2021wave1/finance-operations/dynamics365-finance/configurable-business-documents--preview-support-print-management

**Screenshot:** `report-dialog-destination-archive-printer-email.png` (Print destination settings)

---

## 11. The report viewer (embedded PDF viewer): preview, download, export, print

**What it is.** Reports sent to **Screen** open in a modern embedded **PDF viewer**. It replaced the old HTML "Report viewer". It is on by default from Platform update 39; in PU 36–38 it was the **Report PDF viewer** feature. The viewer:
- Keeps the screen and the printed output the same.
- Has a toolbar to navigate, **download**, and **Print** to locally connected printers (network printers are not listed there).

**Extra toolbar options** (Feature management):
- **Enable Export on Report PDF viewer**: export to Word, Excel, HTML, CSV and more.
- **Enable Network Printing on Report PDF viewer**: choose a network printer and settings from the viewer.

**Accessibility:** the **Enable accessibility feature on report PDF Files** feature produces tagged PDFs (larger files). It is off by default.

**Limits:**
- Expandable and collapsible sections do not work in the PDF.
- Drill-through links work only while previewing.
- Use **Print destination** (File) to produce formats other than PDF when the Export option is not enabled.

**Screenshots:**
- `report-pdf-preview-business-document.png`
- `report-pdf-viewer-export-toolbar.png`
- `report-pdf-viewer-network-print.png`

**Sources:**
- https://learn.microsoft.com/en-us/dynamics365/fin-ops-core/dev-itpro/analytics/preview-pdf-documents (10/27/2025)
- https://learn.microsoft.com/en-us/dynamics365/fin-ops-core/dev-itpro/analytics/reporting-printing-preview-page-options (10/27/2025)

---

## 12. Print archive

**What it is.** A stored copy of report output, used for background runs and for "Save in print archive".

**Steps (blog):**
1. Go to **Common > Inquiries > Print archive**.
2. Find the document by its description (the task description of the background run).
3. Select **Print preview** to open or save the PDF.

Other buttons visible in the screenshot: **Print**, **Printer setup**, **Update**, **Delete**.

**Gaps:**
- No current Learn article covers Print archive retention or clean-up for users.
- The Print archive is separate from the **Electronic reporting jobs** archive (section 17) and from record attachments.

**Screenshots:**
- `report-print-archive-list.png`
- `report-print-archive-preview.png`
- `report-batch-job-status.png`

**Source:** https://learn.microsoft.com/en-us/archive/blogs/dynamicsaxbi/viewing-reports-using-non-interactive-options

---

## 13. Run in the background (batch processing for users)

**What it is.** Any report or periodic process dialog that has a **Run in the background** FastTab can be sent to the batch framework instead of running while you wait. You can keep working; the result arrives in the Action center, or as the destination you chose.

**End-user steps (training module and blog):**
1. In the dialog, expand **Run in the background**.
2. Set **Batch processing** = **Yes**.
3. Check the **Task description**. It is how you find the job later.
4. Optional fields:
   - **Batch group**: leave it as set unless told otherwise.
   - **Private**: hides the job from others; label from the screenshot, not documented further.
   - **Critical Job**: admin-governed.
   - **Monitoring category**.
5. Optional: select **Recurrence** to schedule (start date and time, pattern, end), and **Alerts** to be told when the job **Ended**, hits an **Error** or is **Canceled**.
6. For reports, set **Destination** to **Print archive**, **Printer** or **Email** (not Screen or File).
7. Select **OK**.
8. Check progress in **Common > Inquiries > Batch jobs > My batch jobs**. The batch job form (**System administration > Inquiries > Batch jobs**) is usually for admins.

**Key concepts:**
- **Batch job and tasks.** A batch job is one or more **batch tasks**. Tasks run sequentially or in parallel, with dependencies. The job runs with the security credentials of the user who created it.
- **Batch group.** Directs tasks to servers. With **priority-based batch scheduling**, groups carry a scheduling priority: **Low**, **Normal**, **High**, **Critical** or **Reserved capacity**. This is configured by admins.
- **Pick-up delay.** "A batch server checks for available threads one time per minute", so expect up to a minute before a waiting task starts.
- **Recurring jobs return to Waiting** after each run, whether it failed or succeeded, as long as the recurrence is still valid.
- **Status values** a user will see: Waiting, Executing, Ended, Error, Withhold, Canceling, Canceled (and "Didn't run" for tasks). **Change status** > **Withhold** means stop; **Waiting** means go. Users normally ask an admin or batch manager to change a status.
- **Cancel a running job:** **Change status** > **Canceling**. **Abort** is for admins or batch managers only and is unsafe; Enhanced batch abort has been mandatory since 10.0.39. System jobs cannot be canceled.
- **Batch job history** keeps the messages (Infolog) from each run. **Save jobs to history**: **Always**, **Errors Only** or **Never**.
  - From 10.0.39, jobs with more than 5,000 tasks keep only 2,500 tasks in history.
  - With the **Batch history logging options** flight ("Recommended", 10.0.45 onward), the **INFO** (Infolog) and **PARAMETERS** columns are no longer stored in *history*; only the current job keeps them. Older run logs may therefore show no messages.
- **The batch job page Action Pane** (screenshot) shows **Batch job history**, **Recurrence**, **Alerts**, **Generated files**, **Change status** and **Remove rec…**. **Generated files** is not documented.
- **Batch manager role.** Lets a user copy jobs and change **Run by** (the user a job runs as). Per D-083, do not name roles in the guide; just say "ask the BAU Support team".
- Use batch for large statements and reports, and split them into smaller ranges ("submit multiple smaller batches").

**Gaps:** no current Learn article for **My batch jobs**, the **Private** toggle or **Monitoring category** from the user's side. Capture in the clean-session test.

**Screenshots:**
- `report-dialog-run-in-background-batch.png`
- `batch-run-in-the-background-recurrence-dialog.png`
- `batch-alerts-training.png`
- `batch-jobs-switch-to-enhanced-form.png`
- `batch-jobs-enhanced-form.png`
- `batch-job-change-status-canceling.png`
- `batch-job-cancelled-tasks.png`
- `er-run-in-the-background-fasttab.png`

**Sources:**
- https://learn.microsoft.com/en-us/dynamics365/fin-ops-core/dev-itpro/sysadmin/batch-processing-overview (03/13/2026)
- https://learn.microsoft.com/en-us/dynamics365/fin-ops-core/fin-ops/sysadmin/create-batch-job (03/10/2026)
- https://learn.microsoft.com/en-us/dynamics365/fin-ops-core/dev-itpro/sysadmin/enhanced-forms
- https://learn.microsoft.com/en-us/dynamics365/fin-ops-core/dev-itpro/sysadmin/batch-abort (01/21/2026)
- https://learn.microsoft.com/en-us/dynamics365/fin-ops-core/dev-itpro/sysadmin/batch-history-logging-options
- https://learn.microsoft.com/en-us/dynamics365/fin-ops-core/dev-itpro/sysadmin/batch-history-cleanup
- https://learn.microsoft.com/en-us/dynamics365/fin-ops-core/dev-itpro/sysadmin/priority-based-batch-scheduling
- https://learn.microsoft.com/en-us/dynamics365/fin-ops-core/dev-itpro/sysadmin/runby
- https://learn.microsoft.com/en-us/dynamics365/fin-ops-core/dev-itpro/sysadmin/retryable-batch (mentions **Common > Inquiries > Batch jobs > My batch jobs**)
- https://learn.microsoft.com/en-us/dynamics365/fin-ops-core/dev-itpro/analytics/electronic-reporting-destinations (also mentions My batch jobs)
- https://learn.microsoft.com/en-us/training/modules/setup-batch-jobs-finance-operations/3-reports-alerts
- https://learn.microsoft.com/en-us/training/modules/setup-batch-jobs-finance-operations/2-batch-process-batch-servers
- https://learn.microsoft.com/en-us/dynamics365/fin-ops-core/fin-ops/get-started/whats-new-platform-updates-10-0-39 (batch history limit)

---

## 14. Batch job alerts

**Steps:**
1. Go to **System administration > Inquiries > Batch jobs**.
2. Select the job, then **Alerts** on the Action Pane (on the legacy form: **Batch job** tab > **Alerts**).
3. In the **Batch job alerts** dialog, set **Ended**, **Error** and **Canceled**. Under **Other alerts**, set **Show pop-ups** and **Email**; the email address is shown.
4. Select **OK**.
5. Watch the Action center.

You can also set alerts when you submit a job, using **Alerts** on the **Run in the background** FastTab.

**Gotchas:**
- **Change-based alert rules do not work on batch job status changes** (switched off for performance). Use Batch job alerts instead.
- Email alerts need the email setup and the email distributor batch.

**Screenshots:**
- `batch-job-alerts-dialog.png`
- `batch-alert-action-center-notification.png`
- `batch-jobs-legacy-form-alerts-button.png`

**Sources:**
- https://learn.microsoft.com/en-us/dynamics365/fin-ops-core/dev-itpro/sysadmin/alerts (03/13/2026)
- https://learn.microsoft.com/en-us/dynamics365/fin-ops-core/fin-ops/get-started/create-alerts

---

## 15. Messages: message bar, Action center, message boxes, Message details (Infolog)

**What it is.** The way the system tells the user something. Microsoft documents three places:
- **Message bars**, below the Action Pane: info (blue), warning (yellow) and error (red) about the *current page*, mostly validation. A message disappears when you leave the page and comes back when you return. A validation message clears when the value is fixed (field-level) or at the next save (table-level).
- **The Action center**, the bell or flag in the navigation bar: messages from **asynchronous** work such as batch jobs, report completion and alerts.
  - It shows a count of new messages since it was last opened.
  - It holds up to **500 messages** (first in, first out).
  - A notification pops up when a new message arrives.
- **Message boxes**: modal dialogs for errors that need immediate action (a "light box").

**Message details.** When a process produces a group of messages (the old "Infolog"), the message bar or Action center shows a summary with a link to the full list in the **Message details** pane. The severity shown is the worst message in the group.

**Keyboard:** **Ctrl+F7** goes to the Message bar; **Ctrl+Shift+F7** goes to the Message Center (Action center).

**System notification management (admin):**
- **Enable system notification management** monitors rules that generate more than 100 notifications per hour.
- **Auto-blocking of high-volume notification rules** (10.0.39, on by default) blocks such rules, and the affected users are notified. Users with very chatty alert rules may find them blocked.

**Gap:** the user-facing "Message details" pane, and the "Show messages" link, are shown only in screenshots. No end-user article covers reading and copying error details for support. Capture in the clean-session test.

**Screenshots:**
- `message-bar-types-info-warning-error.jpg`
- `message-box-error-example.jpg`
- `message-bar-info-message-details-link.jpg`
- `message-bar-error-message-details.jpg`
- `batch-alert-action-center-notification.png`

**Sources:**
- https://learn.microsoft.com/en-us/dynamics365/fin-ops-core/dev-itpro/user-interface/messaging-user (03/12/2026)
- https://learn.microsoft.com/en-us/dynamics365/fin-ops-core/fin-ops/get-started/user-interface-elements ("Notifications"; navigation team)
- https://learn.microsoft.com/en-us/dynamics365/fin-ops-core/fin-ops/get-started/shortcut-keys
- https://learn.microsoft.com/en-us/dynamics365/fin-ops-core/dev-itpro/user-interface/messaging-api-center-bar-details (developer)

---

## 16. Alerts (alert rules)

**What it is.** Personal rules that notify you when a record is created or deleted, a field changes, or a date falls due. Examples: a purchase order delivery date is postponed, a new sales order arrives, a vendor's bank account changes (useful for P2P fraud control).

**Create an alert rule (documented steps):**
1. Make sure the alert batch jobs run (admin): **System administration > Periodic tasks > Alerts** > **Change based alerts** and **Due date alerts**. Microsoft suggests **Recurrence** with **No end date**, pattern **Minutes**, **Count** 1, for change-based alerts.
2. Open the page with the data, for example **All purchase orders**, and select the record or the field.
3. On the Action Pane, select **Options** tab > **Share** group > **Create alert rule**. The overview article calls the button **Create a custom alert**; confirm the label in the clean-session test.
4. In the **Create alert rule** dialog:
   - **Alert me when**: **Field** and **Event**, for example **Delivery date** / **has been postponed**, **Record has been created**, **has changed**, **is due in**, **was due this amount of time ago**.
   - **Alert me for**: **Current selected record** or **All records** in the current page view. Filter the page first to narrow it. **Organization-wide** applies the rule across legal entities.
   - **Alert me until**: an end date, or no end.
   - **Alert me with**: **Subject** and **Message**; **Send email** (Yes/No); **Send externally** (business event; needs **Organization-wide** = No).
   - **Alert who**: your user ID by default. Only organization administrators can change it.
5. Select **OK**.

**Event types:**
- Create and delete events.
- Update events (a field changes).
- Due-date events (the events offered depend on the field type: dates get "is due in").

**Manage alert rules:** **Options** tab > **Alert me** (the Action Pane button) opens **Manage alert rules**, where you change events, notifications and expiry dates, or delete rules. The URL given in the brief (`alerts-managing-rules`) returns 404; the content is in the overview and create-alerts articles.

**Delivery:**
- Always to the **Action center** (pop-up notification).
- Optionally by **email** (**Send email** = Yes). Email uses predefined templates, is sent "on behalf of" the alert owner, and needs the email setup.

**Limits and gotchas:**
- **Batch timing.** Alerts are generated by batch jobs, not instantly.
  - With a low frequency, **alerts can be lost**: if the data no longer matches the rule's condition when the job runs, no alert is raised (Microsoft's customer BB example).
  - Due-date jobs should run at least daily, and alerts are not duplicated.
  - The **batch processing window** stops due-date alerts expiring when jobs have not run for days.
- **Secondary data sources.** Alerts cannot be set on some secondary data sources (for example dimension accounts on posting profiles). The workaround is SysTableBrowser, which is not for end users.
- **Batch status changes** do not trigger change-based alerts (see section 14).
- **High-volume rules may be auto-blocked** (section 15).

**Screenshots:**
- `alert-create-alert-rule-dialog-send-email.png`
- `alert-email-notification-templates.png`

**Sources:**
- https://learn.microsoft.com/en-us/dynamics365/fin-ops-core/fin-ops/get-started/alerts-overview (11/20/2025)
- https://learn.microsoft.com/en-us/dynamics365/fin-ops-core/fin-ops/get-started/create-alerts (11/20/2025)
- https://learn.microsoft.com/en-us/dynamics365/fin-ops-core/fin-ops/get-started/alerts-managing (title "Batch processing of alerts", 11/20/2025)
- https://learn.microsoft.com/en-us/dynamics365/fin-ops-core/fin-ops/get-started/alert-email-notifications (11/20/2025)
- https://learn.microsoft.com/en-us/dynamics365/fin-ops-core/dev-itpro/business-events/alerts-business-events
- Videos: https://youtu.be/ZYKMcv6kl9s (alerts on filtered data), https://youtu.be/cpzimwOjicM (alert rule options)

---

## 17. Electronic reporting (ER): what end users touch

**What it is.** ER produces configured outbound files: tax returns, payment files, Intrastat, some business documents, audit files. Users meet it as a normal dialog that runs an ER format.

**What users see:**
- **Run in the background**: **Batch processing** = **No** runs interactively and offers a download; **Yes** creates a batch job.
- **Finding background output:**
  - **Common > Inquiries > Batch jobs > My batch jobs** for status.
  - **Organization administration > Electronic reporting > Electronic reporting jobs**: select **Show files** to get the generated document, which is stored as an attachment on the job record, and to see errors and warnings.
- **Destinations** are configured by admins (**Organization administration > Electronic reporting > Electronic reporting destination**): Email, Archive, File, Screen, Power BI, Print, and PDF conversion.
  - Destinations are company-specific.
  - **Screen** opens a preview on a new browser tab (Office files through Office Online).
- **Business document management (BDM)** workspace: business users edit Excel and Word *templates* for business documents built on ER, using Office desktop or Microsoft 365 with SharePoint. Cloud only. It changes templates, not documents already generated. For a Getting Started guide this is a mention only (template owners).

**Screenshots:**
- `er-run-in-the-background-fasttab.png`
- `er-electronic-reporting-jobs-show-files.png`
- `er-destination-settings-screen.png`

**Sources:**
- https://learn.microsoft.com/en-us/dynamics365/fin-ops-core/dev-itpro/analytics/electronic-reporting-destinations
- https://learn.microsoft.com/en-us/dynamics365/fin-ops-core/dev-itpro/analytics/er-destination-type-screen (04/07/2026)
- https://learn.microsoft.com/en-us/dynamics365/fin-ops-core/dev-itpro/analytics/er-business-document-management (08/13/2026)
- https://learn.microsoft.com/en-us/dynamics365/fin-ops-core/dev-itpro/analytics/general-electronic-reporting
- https://docs.microsoft.com/learn/modules/build-reports-finance-operations/implement-business-document-management

---

## 18. Financial reporting (financial statements: Balance sheet, Income statement, Trial balance)

**What it is.** The Management Reporter-based tool for formatted financial statements, with drill-down to accounts and transactions. Report Designer (authoring) is for report owners; generating and viewing reports is for finance users.

**Version note (important):**
- Financial reporting is **now delivered as an add-in**, "Microsoft Dynamics 365 Financial Reporting". It is installed from the Power Platform admin center (recommended) or Lifecycle Services (legacy).
- Existing customers are unaffected.
- Updates are slipstreamed on their own cadence.

**Where:**
- **General ledger > Inquiries and reports > Financial reports** (the docs also say "Financial reporting").
- Also under Budgeting > Inquiries and reports (Basic budgeting, Budget planning, Budget control) and Consolidations.

**Open and generate (end user):**
1. On the list, select the report name to open it. The first time, it generates automatically for the previous month-end.
2. To run for a date, select the report, select **Generate**, enter **Report date**, then **OK**.
3. Generated versions appear in the **Reports** section, where you can **View** or **Delete** them.
4. **Report queue status** shows the progress: **Queueing**, **Queued**, **Processing**, **PostProcessing**, then **Completed**, **Failed** or **Canceled**.
   - Cancel with **Remove** before the report completes.
   - Up to 3 reports run concurrently per service instance and 5 per environment, first in, first out.

**View and explore:**
- **Drill down** from the financial level to the account level, then to transactions:
  - **Drill to report transaction level**: a formatted view.
  - **Open account transactions**: the voucher transaction inquiry.
  - Budget data can open budget account entries.
  - **Esc** or **X** closes a level.
- **Report options**: **Add an attribute filter**, **Add a dimension filter**, change the scenario on Actual vs Budget, then **OK** or **Cancel**.
- **Generate** on the Action Pane refreshes the report with the latest postings for the same period.
- **Currency** translates to any configured reporting currency.
- **Show** > **Summary lines only** toggles the detail lines.
- **Print** creates a PDF. Options: the detail-level sliders, all or current reporting units, page size, layout, fit to width and margins. You are then prompted to download or save to OneDrive or SharePoint.
- **Export** to Excel applies the export settings in the report design.

**Report groups** and **report schedules** are set up in Report Designer (designer or administrator role). A schedule uses its creator's credentials and needs credentials for each company.

**Retention and audit (key gotchas):**
- Generated reports **expire after 90 days** by default (**Financial report retention policies**). Users with the right permission can set a report to never expire.
- **From release 10.0.45, fact versioning was removed**: re-running or drilling into an older generated report recalculates the detail with current data, so drill-down lines can differ from the original. Top-level balances do not change. Microsoft's tip: **export the final report to Excel or PDF for an immutable copy**. Important for R2R month-end.

**Default reports:** 22, including Income Statement, Balance Sheet, Summary and Detailed Trial Balance, Cash Flow, Actual vs Budget, Ledger Transaction List and Audit Details.

**Security (FYI only, per D-083 not for the guide):** duties Generate, View and Maintain financial reports.

**Related analysis tools:**
- **Financial analysis** is a Power BI-embedded workspace with KPIs and statements. It is not a replacement for Financial reporting: it cannot print, it exports raw data only, and it uses accounting currency only.
- **Missing account analysis** in Report Designer is for report owners.

**Sources:**
- https://learn.microsoft.com/en-us/dynamics365/finance/general-ledger/financial-reporting-getting-started (09/28/2026)
- https://learn.microsoft.com/en-us/dynamics365/finance/general-ledger/view-financial-reports (06/01/2026)
- https://learn.microsoft.com/en-us/dynamics365/fin-ops-core/fin-ops/analytics/generate-financial-report (06/01/2026)
- https://learn.microsoft.com/en-us/dynamics365/fin-ops-core/fin-ops/analytics/financial-reporting-intro
- https://learn.microsoft.com/en-us/dynamics365/finance/general-ledger/financial-reporting-faq
- https://learn.microsoft.com/en-us/dynamics365/finance/general-ledger/fin-reports-best
- https://learn.microsoft.com/en-us/dynamics365/finance/general-ledger/balance-sheet-financial-reports
- https://learn.microsoft.com/en-us/dynamics365/finance/general-ledger/income-statement-financial-report
- https://learn.microsoft.com/en-us/dynamics365/finance/general-ledger/trial-balance-financial-reports
- https://learn.microsoft.com/en-us/dynamics365/finance/general-ledger/financial-reporting-keyboard-shortcuts
- https://learn.microsoft.com/en-us/dynamics365/fin-ops-core/dev-itpro/analytics/financial-insights ("Financial analysis", 04/08/2026)

---

## 19. Power BI in workspaces (analytical workspaces and pinned content)

**What it is:**
- **Analytical workspaces**: many workspaces have an **Analytics** tab with embedded Power BI reports. You interact by clicking visuals, and other visuals react.
- **Pinned content**: users can pin their own PowerBI.com tiles and reports into workspaces.

**End-user steps (pin a report):**
1. Open a workspace that has a **Links** section, for example **Ledger budgets and forecasts**.
2. Select **Options** tab > **Open report catalog** (or **Open tile catalog**), choose the reports, then **OK**.
3. The reports appear under a Power BI section at the bottom of **Links**. Select a report to open it full page, and use the filter pane.

Users can also create their own workspace (right-click a dashboard tile > **Add a workspace**, which creates **My Workspace 1** and so on) and pin Power BI content there. That is personalization; cross-reference the grids/personalization team.

**Admin and power user:**
- PowerBI.com integration is a one-time admin setup.
- **Select Analytics** and **Restore Analytics** (**Options** > **Power BI** group) replace an embedded analytical report for *all users in the legal entity*. Only members of the System Report Editors group can do this. It is not a personalization.

**Gotchas:**
- Power BI and entity-store data is near real-time, not real-time. Analytical workspaces need the Entity store refreshed (admin).
- Dates are UTC in Power BI and the Excel add-in.

**Screenshots:**
- `powerbi-open-report-catalog-dialog.jpg`
- `powerbi-reports-in-workspace-links.jpg`
- `powerbi-analytical-workspace.png`
- `powerbi-select-analytics-dialog.png`

**Sources:**
- https://learn.microsoft.com/en-us/dynamics365/fin-ops-core/dev-itpro/analytics/pin-power-bi-reports (01/15/2026)
- https://learn.microsoft.com/en-us/dynamics365/fin-ops-core/dev-itpro/analytics/embed-power-bi-workspaces
- https://learn.microsoft.com/en-us/dynamics365/fin-ops-core/dev-itpro/analytics/select-analytical-workspace
- https://learn.microsoft.com/en-us/dynamics365/fin-ops-core/dev-itpro/analytics/power-bi-integration
- https://learn.microsoft.com/en-us/dynamics365/fin-ops-core/dev-itpro/analytics/configure-power-bi-integration (admin)
- https://learn.microsoft.com/en-us/dynamics365/fin-ops-core/dev-itpro/analytics/bi-reporting-home-page

---

## 20. Choosing the right output: Microsoft's reporting experiences (and the "inquiry pages" concept)

Microsoft's "Information access and reporting" article sets out five reporting experiences. The guide can use them as a decision table:

| Need | Tool | Data | Sharing and printing |
|---|---|---|---|
| Look up and monitor records | **Operational views**: list pages, inquiry pages, workspaces, grids | Near real-time | Export to Excel / Open in Excel |
| A fixed document (invoice, statement, report to file) | **Business documents (SSRS)** | Real-time | PDF, Office export, email, printer, print archive, batch |
| Explore and analyse | **Power BI** (analytical workspaces, pinned reports) | Near real-time | Dashboards, tiles |
| A statutory or electronic file | **Electronic reporting** | Real-time | Excel export, batch jobs |
| Financial statements | **Financial reporting** | Cached views | Excel export, local printer (PDF) |

**Inquiry pages:** Microsoft has no single article on "inquiries" as a concept. Each module has **Inquiries and reports** menus (for example **General ledger > Inquiries and reports > Voucher transactions** and **Trial balance**; **Accounts receivable > Inquiries and reports**). The ledger settlement and other inquiry articles are module-specific. Treat this as a Getting Started explanation: inquiries are on-screen, filterable and exportable; reports are documents. Cross-reference the navigation team.

**Sources:**
- https://learn.microsoft.com/en-us/dynamics365/fin-ops-core/dev-itpro/analytics/information-access-reporting (10/22/2025)
- https://learn.microsoft.com/en-us/dynamics365/fin-ops-core/dev-itpro/analytics/bi-reporting-home-page

---

## 21. Data management (Data import/export) vs Excel: the end-user angle

**What it is.** The **Data management** workspace runs import and export *jobs* for data entities through staging tables. Supported formats include Excel, CSV and packages. It is used for bulk loads and large extracts, and it is usually limited to administrators or data owners.

**When to use which (Microsoft's guidance):**
- Users get data out with **Open in Excel** (entity security, refresh) or **Export to Excel** (grid as shown, up to 50k rows by default).
- **"When very large datasets must be exported from the system, data management is recommended."**
- DMF and DIXF "are often limited to administrators".

**Gotchas:**
- Only one Excel import or export can run at a time in DMF (error **DMF2039**). Use CSV for parallel jobs.
- DMF export to Excel has a 255-character limit.
- Do not refresh the browser during non-batch DMF jobs; use the form refresh icon.
- DMF jobs gained automatic retry on batch restarts in 10.0.40 and 10.0.42.

**For the guide:** one paragraph saying that bulk changes go through the data owner or BAU Support, not Open in Excel at volume.

**Sources:**
- https://learn.microsoft.com/en-us/dynamics365/fin-ops-core/fin-ops/data-entities/data-import-export-job (09/08/2026)
- https://learn.microsoft.com/en-us/dynamics365/fin-ops-core/dev-itpro/office-integration/office-integration-troubleshooting
- https://learn.microsoft.com/en-us/dynamics365/fin-ops-core/dev-itpro/data-entities/dm-error-descriptions
- https://learn.microsoft.com/en-us/dynamics365/fin-ops-core/fin-ops/get-started/whats-new-platform-updates-10-0-42

---

## 22. Message processor (Tasks / Message processor messages)

**What it is.** **System administration > Message processor > Message processor messages**: a framework that queues and processes event messages, with a log and manual reprocessing.

The queues documented are Supply Chain queues: Manufacturing Execution, Production, Warehouse, Shipment Orders, Source System Products, and External warehouse shipment order updates. **No finance (O2C, P2P, R2R or Tax) use is documented.** Leave it out of the finance Getting Started guide.

**Source:** https://learn.microsoft.com/en-us/dynamics365/supply-chain/message-processor/message-processor (05/05/2026)

---

## 23. What's new, deprecations and release plans relevant to this area (2024–2026)

| When | Change | Effect on users | Source |
|---|---|---|---|
| 10.0.38–10.0.39 | **Microsoft Graph email provider**; the **Exchange provider stopped 15 September 2024** | The "Use Exchange email server" option no longer works | whats-new 10.0.39; removed-deprecated |
| 10.0.39 | **Auto-blocking of high-volume notification rules** (on by default) | Chatty alert rules may be blocked; the user is notified | messaging-user |
| 10.0.39 | Batch job history keeps 2,500 of more than 5,000 tasks; Enhanced batch abort mandatory | Minor | create-batch-job; batch-abort |
| 10.0.40 / 10.0.42 | **SharePoint user authentication** (mandatory from 10.0.42; old connection ended 28 February 2025); **Export attachments** (10.0.40) | Users need SharePoint folder access for SharePoint-stored attachments | configure-document-management; removed-deprecated |
| 10.0.45 onward | **Batch history logging options** (INFO and PARAMETERS not stored in history) | Older run messages may be missing | batch-history-logging-options |
| 10.0.45 | Copilot chat file attachments | Copilot team | whats-new 10.0.45 |
| Financial reporting 10.0.45 | **Fact versioning removed**; 90-day report expiry | Export final statements to keep a fixed copy | financial-reporting-getting-started |
| 2026 | **Financial reporting delivered as an add-in** (Power Platform admin center) | Admin install; the user path is unchanged | financial-reporting-getting-started (09/28/2026) |
| From 20 January 2026 (10.0.46 note) | **Interactive query time-out cut from 30 to 5 minutes** | Use **Run in the background** for heavy reports and processes | whats-new 10.0.46 |
| 10.0.48 / 2026 wave 1 | ERP MCP attachment support (agents) | Copilot team | whats-new 10.0.48; release plan 2026 wave 1 |
| 10.0.49 | Office menu expansion deferred; output menu items for MCP | None visible to users | whats-new 10.0.49 |
| Ongoing | Embedded drill-through links removed from paginated documents | Links work only in preview | removed-deprecated |

The 2025 wave 2 and 2026 wave 1 cross-app release plans contain **no new Office integration, report, batch or alert features for users**; they are Copilot, agent and archive items. No 2026 wave 2 cross-app page exists yet (404).

**Sources:**
- https://learn.microsoft.com/en-us/dynamics365/fin-ops-core/fin-ops/get-started/whats-new-home-page
- https://learn.microsoft.com/en-us/dynamics365/fin-ops-core/fin-ops/get-started/whats-new-platform-updates-10-0-39 (and 10-0-40, 10-0-42, 10-0-45, 10-0-46, 10-0-48, 10-0-49, 10-0-50)
- https://learn.microsoft.com/en-us/dynamics365/fin-ops-core/fin-ops/get-started/removed-deprecated-features-platform-updates
- https://learn.microsoft.com/en-us/dynamics365/release-plan/2025wave2/enterprise-resource-planning/finance-operations-crossapp-capabilities/planned-features
- https://learn.microsoft.com/en-us/dynamics365/release-plan/2026wave1/enterprise-resource-planning/finance-operations-crossapp-capabilities/planned-features
- https://learn.microsoft.com/en-us/dynamics365/release-plan/2026wave1/enterprise-resource-planning/dynamics365-finance/

---

## (1) Suggested Getting Started topics from this area (ranked)

**Must have**
1. **Get data out to Excel: Export to Excel vs Open in Excel.** The most-used daily skill. Users must know which tool fits: a static copy of the grid as shown (50k-row default, 15-minute download) or a live, refreshable workbook.
2. **Run a report: the report dialog, Records to include and Destination.** Every O2C, P2P, R2R and Tax user runs reports. Microsoft has no current end-user article, so the guide fills a real gap.
3. **View, download, print and export a report (PDF viewer).** Screen is the default destination. Users need download, local print and export, and the drill-through limits.
4. **Run in the background, then find the result (My batch jobs, Print archive, Action center).** The interactive time-out is now 5 minutes, so large statements, aged balances and month-end runs must go to batch. Users need to know where the output lands.
5. **Attach and find documents (Attach button, Ctrl+Shift+A, types, preview, restore deleted).** Invoices, remittances and approvals evidence are attached across all streams. The badge count and focus-sensitive behaviour confuse new users.
6. **Read system messages: message bar, Action center, Message details.** Users must tell a validation warning from a background-job result, and copy error details for BAU Support.

**Should have**
7. **Enter or update lines with Open lines in Excel / Open in Excel and Publish.** High value for R2R journals, AP invoice registers and AR/AP payment journals. It includes the key/mandatory field rules, UTC dates and publish errors.
8. **Financial reports: open, generate, drill down, export.** Core for R2R and controllers. The 90-day expiry and "export to keep an exact copy" (no fact versioning) are important controls.
9. **Set up an alert rule and manage alerts.** Useful for P2P and O2C control (bank account changes, overdue deliveries). Users need to know that alerts depend on batch timing and can be missed.
10. **Batch job alerts and recurrence for your own jobs.** So users know when their scheduled runs fail, without polling.
11. **Sending documents by email from D365 (the "How would you like to send email" dialog).** Statements and collection letters (O2C) use it, and the first-run choice confuses users.

**Nice to have**
12. **Power BI analytical workspaces and pinning reports.** Helpful for managers; depends on our tenant's Power BI setup.
13. **Choosing the right output (inquiry vs report vs Power BI vs financial report vs ER).** A one-page orientation table drawn from Microsoft's reporting experiences.
14. **Electronic reporting outputs: Electronic reporting jobs > Show files.** Mainly Tax and AP payment-file users. A short "where your file is" note.
15. **Export to Word, and Excel templates (Document templates, Excel workbook designer).** Mostly template owners; mention only.
16. **Data management vs Excel (when to ask for a bulk load).** One paragraph that sets expectations.
17. Message processor: **exclude**. No finance use is documented.

---

## (2) Every URL consulted

**Microsoft Learn docs (live pages and their source files in MicrosoftDocs/dynamics-365-unified-operations-public):**

Office integration:
- https://learn.microsoft.com/en-us/dynamics365/fin-ops-core/dev-itpro/office-integration/office-integration
- https://learn.microsoft.com/en-us/dynamics365/fin-ops-core/dev-itpro/office-integration/use-excel-add-in
- https://learn.microsoft.com/en-us/dynamics365/fin-ops-core/dev-itpro/office-integration/office-integration-edit-excel
- https://learn.microsoft.com/en-us/dynamics365/fin-ops-core/dev-itpro/office-integration/office-integration-troubleshooting
- https://learn.microsoft.com/en-us/dynamics365/fin-ops-core/dev-itpro/office-integration/office-integration-tutorial
- https://learn.microsoft.com/en-us/dynamics365/fin-ops-core/dev-itpro/office-integration/customize-open-office-menu
- https://learn.microsoft.com/en-us/dynamics365/fin-ops-core/dev-itpro/user-interface/add-templates-open-lines-excel-menu
- https://learn.microsoft.com/en-us/dynamics365/finance/general-ledger/open-lines-excel-journals-documents
- https://learn.microsoft.com/en-us/dynamics365/fin-ops-core/dev-itpro/financial/add-dimensions-excel-templates

Grids, shortcuts and messaging:
- https://learn.microsoft.com/en-us/dynamics365/fin-ops-core/dev-itpro/get-started/grid-capabilities
- https://learn.microsoft.com/en-us/dynamics365/fin-ops-core/fin-ops/get-started/shortcut-keys
- https://learn.microsoft.com/en-us/dynamics365/fin-ops-core/fin-ops/get-started/user-interface-elements
- https://learn.microsoft.com/en-us/dynamics365/fin-ops-core/dev-itpro/user-interface/messaging-user
- https://learn.microsoft.com/en-us/dynamics365/fin-ops-core/dev-itpro/user-interface/messaging-api-center-bar-details

Export limits and security governance:
- https://learn.microsoft.com/en-us/dynamics365/fin-ops-core/fin-ops/sysadmin/security-gov-security-object-licenses-preview
- https://learn.microsoft.com/en-us/dynamics365/fin-ops-core/fin-ops/sysadmin/security-gov-user-dormant-report

Platform what's new (older):
- https://learn.microsoft.com/en-us/dynamics365/fin-ops-core/dev-itpro/get-started/whats-new-platform-update-22
- https://learn.microsoft.com/en-us/dynamics365/fin-ops-core/dev-itpro/get-started/whats-new-platform-update-23
- https://learn.microsoft.com/en-us/dynamics365/fin-ops-core/dev-itpro/get-started/whats-new-platform-update-7

Document management and email:
- https://learn.microsoft.com/en-us/dynamics365/fin-ops-core/fin-ops/organization-administration/configure-document-management
- https://learn.microsoft.com/en-us/dynamics365/fin-ops-core/dev-itpro/organization-administration/maintain-document-management-storage
- https://learn.microsoft.com/en-us/dynamics365/fin-ops-core/dev-itpro/organization-administration/configure-email
- https://learn.microsoft.com/en-us/dynamics365/finance/accounts-receivable/archive-printed-invoices
- https://learn.microsoft.com/en-us/dynamics365/finance/accounts-receivable/configure-customer-invoices
- https://learn.microsoft.com/en-us/dynamics365/finance/accounts-receivable/process-collection-letters-example
- https://learn.microsoft.com/en-us/dynamics365/finance/general-ledger/general-ledger-statement-by-main-account
- https://learn.microsoft.com/en-us/dynamics365/finance/budgeting/budget-control-account-detail-history-report
- https://learn.microsoft.com/en-us/dynamics365/finance/accounts-payable/vendor-aging-report

Reporting and printing:
- https://learn.microsoft.com/en-us/dynamics365/fin-ops-core/dev-itpro/analytics/print-documents
- https://learn.microsoft.com/en-us/dynamics365/fin-ops-core/dev-itpro/analytics/reporting-printing-preview-page-options
- https://learn.microsoft.com/en-us/dynamics365/fin-ops-core/dev-itpro/analytics/preview-pdf-documents
- https://learn.microsoft.com/en-us/dynamics365/fin-ops-core/dev-itpro/analytics/prevent-long-running-reports-timing-out
- https://learn.microsoft.com/en-us/dynamics365/fin-ops-core/dev-itpro/analytics/SSRS-report
- https://learn.microsoft.com/en-us/dynamics365/fin-ops-core/dev-itpro/analytics/document-reporting-services
- https://learn.microsoft.com/en-us/dynamics365/fin-ops-core/dev-itpro/analytics/create-nextgen-reporting-solutions
- https://learn.microsoft.com/en-us/dynamics365/fin-ops-core/dev-itpro/analytics/install-document-routing-agent
- https://learn.microsoft.com/en-us/dynamics365/fin-ops-core/dev-itpro/analytics/printing-capabilities-on-premises
- https://learn.microsoft.com/en-us/dynamics365/fin-ops-core/dev-itpro/sysadmin/sys-admin-tools-network-printer
- https://learn.microsoft.com/en-us/dynamics365/fin-ops-core/dev-itpro/analytics/information-access-reporting
- https://learn.microsoft.com/en-us/dynamics365/fin-ops-core/dev-itpro/analytics/bi-reporting-home-page

Power BI:
- https://learn.microsoft.com/en-us/dynamics365/fin-ops-core/dev-itpro/analytics/pin-power-bi-reports
- https://learn.microsoft.com/en-us/dynamics365/fin-ops-core/dev-itpro/analytics/embed-power-bi-workspaces
- https://learn.microsoft.com/en-us/dynamics365/fin-ops-core/dev-itpro/analytics/select-analytical-workspace
- https://learn.microsoft.com/en-us/dynamics365/fin-ops-core/dev-itpro/analytics/power-bi-integration
- https://learn.microsoft.com/en-us/dynamics365/fin-ops-core/dev-itpro/analytics/configure-power-bi-integration
- https://learn.microsoft.com/en-us/dynamics365/fin-ops-core/dev-itpro/analytics/financial-insights

Electronic reporting and BDM:
- https://learn.microsoft.com/en-us/dynamics365/fin-ops-core/dev-itpro/analytics/electronic-reporting-destinations
- https://learn.microsoft.com/en-us/dynamics365/fin-ops-core/dev-itpro/analytics/er-destination-type-screen
- https://learn.microsoft.com/en-us/dynamics365/fin-ops-core/dev-itpro/analytics/er-business-document-management
- https://learn.microsoft.com/en-us/dynamics365/fin-ops-core/dev-itpro/analytics/general-electronic-reporting

Financial reporting:
- https://learn.microsoft.com/en-us/dynamics365/fin-ops-core/fin-ops/analytics/generate-financial-report
- https://learn.microsoft.com/en-us/dynamics365/fin-ops-core/fin-ops/analytics/financial-reporting-intro
- https://learn.microsoft.com/en-us/dynamics365/finance/general-ledger/view-financial-reports
- https://learn.microsoft.com/en-us/dynamics365/finance/general-ledger/financial-reporting-getting-started
- https://learn.microsoft.com/en-us/dynamics365/finance/general-ledger/financial-reporting-faq
- https://learn.microsoft.com/en-us/dynamics365/finance/general-ledger/fin-reports-best
- https://learn.microsoft.com/en-us/dynamics365/finance/general-ledger/balance-sheet-financial-reports
- https://learn.microsoft.com/en-us/dynamics365/finance/general-ledger/income-statement-financial-report
- https://learn.microsoft.com/en-us/dynamics365/finance/general-ledger/trial-balance-financial-reports
- https://learn.microsoft.com/en-us/dynamics365/finance/general-ledger/financial-reporting-keyboard-shortcuts

Alerts:
- https://learn.microsoft.com/en-us/dynamics365/fin-ops-core/fin-ops/get-started/alerts-overview
- https://learn.microsoft.com/en-us/dynamics365/fin-ops-core/fin-ops/get-started/alerts-managing
- https://learn.microsoft.com/en-us/dynamics365/fin-ops-core/fin-ops/get-started/create-alerts
- https://learn.microsoft.com/en-us/dynamics365/fin-ops-core/fin-ops/get-started/alert-email-notifications
- https://learn.microsoft.com/en-us/dynamics365/fin-ops-core/dev-itpro/business-events/alerts-business-events
- https://learn.microsoft.com/en-us/dynamics365/fin-ops-core/fin-ops/get-started/alerts-managing-rules (returns 404)

Batch:
- https://learn.microsoft.com/en-us/dynamics365/fin-ops-core/dev-itpro/sysadmin/alerts
- https://learn.microsoft.com/en-us/dynamics365/fin-ops-core/dev-itpro/sysadmin/batch-processing-overview
- https://learn.microsoft.com/en-us/dynamics365/fin-ops-core/fin-ops/sysadmin/create-batch-job
- https://learn.microsoft.com/en-us/dynamics365/fin-ops-core/dev-itpro/sysadmin/enhanced-forms
- https://learn.microsoft.com/en-us/dynamics365/fin-ops-core/dev-itpro/sysadmin/batch-abort
- https://learn.microsoft.com/en-us/dynamics365/fin-ops-core/dev-itpro/sysadmin/retryable-batch
- https://learn.microsoft.com/en-us/dynamics365/fin-ops-core/dev-itpro/sysadmin/priority-based-batch-scheduling
- https://learn.microsoft.com/en-us/dynamics365/fin-ops-core/dev-itpro/sysadmin/runby
- https://learn.microsoft.com/en-us/dynamics365/fin-ops-core/dev-itpro/sysadmin/activeperiod
- https://learn.microsoft.com/en-us/dynamics365/fin-ops-core/dev-itpro/sysadmin/copy-batch-job
- https://learn.microsoft.com/en-us/dynamics365/fin-ops-core/dev-itpro/sysadmin/batch-history-logging-options
- https://learn.microsoft.com/en-us/dynamics365/fin-ops-core/dev-itpro/sysadmin/batch-history-cleanup

Data management and message processor:
- https://learn.microsoft.com/en-us/dynamics365/fin-ops-core/fin-ops/data-entities/data-import-export-job
- https://learn.microsoft.com/en-us/dynamics365/fin-ops-core/dev-itpro/data-entities/dm-error-descriptions
- https://learn.microsoft.com/en-us/dynamics365/supply-chain/message-processor/message-processor

Copilot (cross-reference):
- https://learn.microsoft.com/en-us/dynamics365/fin-ops-core/dev-itpro/copilot/copilot-attachments

What's new and deprecations:
- https://learn.microsoft.com/en-us/dynamics365/fin-ops-core/fin-ops/get-started/whats-new-home-page
- https://learn.microsoft.com/en-us/dynamics365/fin-ops-core/fin-ops/get-started/whats-new-changed
- https://learn.microsoft.com/en-us/dynamics365/fin-ops-core/fin-ops/get-started/whats-new-platform-updates-10-0-38 through -10-0-50 (13 pages)
- https://learn.microsoft.com/en-us/dynamics365/fin-ops-core/fin-ops/get-started/removed-deprecated-features-platform-updates
- https://learn.microsoft.com/en-us/dynamics365/fin-ops-core/dev-itpro/analytics/print-management (returns 404; no such article)

**Release plans:**
- https://learn.microsoft.com/en-us/dynamics365/release-plan/2025wave2/enterprise-resource-planning/finance-operations-crossapp-capabilities/planned-features
- https://learn.microsoft.com/en-us/dynamics365/release-plan/2026wave1/enterprise-resource-planning/finance-operations-crossapp-capabilities/planned-features
- https://learn.microsoft.com/en-us/dynamics365/release-plan/2026wave2/enterprise-resource-planning/finance-operations-crossapp-capabilities/planned-features (404)
- https://learn.microsoft.com/en-us/dynamics365/release-plan/2026wave1/enterprise-resource-planning/dynamics365-finance/
- https://learn.microsoft.com/en-us/dynamics365-release-plan/2021wave2/finance-operations/dynamics365-finance/configurable-business-documents--specific-destinations-via-printer-management-settings
- https://learn.microsoft.com/en-us/dynamics365-release-plan/2021wave1/finance-operations/dynamics365-finance/configurable-business-documents--preview-support-print-management

**Microsoft Learn training modules:**
- https://learn.microsoft.com/en-us/training/modules/implement-common-integration-features-finance-ops/ (units 2-office, 3-excel, 4-documents, 5-emails-exchange, 8-network-print)
- https://learn.microsoft.com/en-us/training/modules/build-reports-finance-operations/ (units 01-ssrs-reports, 03-excel-reports)
- https://docs.microsoft.com/learn/modules/build-reports-finance-operations/implement-business-document-management
- https://learn.microsoft.com/en-us/training/modules/setup-batch-jobs-finance-operations/ (units 2-batch-process-batch-servers, 3-reports-alerts)

**Archived Microsoft blog:**
- https://learn.microsoft.com/en-us/archive/blogs/dynamicsaxbi/viewing-reports-using-non-interactive-options (2018), with images from https://msdntnarchive.z22.web.core.windows.net/media/2018/04/

**Legacy (AX 2012, concepts only):**
- https://learn.microsoft.com/en-us/dynamicsax-2012/appuser-itpro/about-print-management-document-types-and-modules

**Repository:**
- https://github.com/MicrosoftDocs/dynamics-365-unified-operations-public (sparse clone of `articles/fin-ops-core`, `articles/finance/{general-ledger,accounts-receivable,accounts-payable,budgeting,cash-bank-management,get-started}` and `articles/supply-chain/message-processor`)

**Videos referenced in the docs (not watched):**
- https://youtu.be/RTicLb-6dbI
- https://www.youtube.com/watch?v=p4rl1CkiLN4
- https://youtu.be/ZYKMcv6kl9s
- https://youtu.be/cpzimwOjicM
- https://www.youtube.com/watch?v=gGWuNJDoi-M
- https://youtu.be/_8WlwmSggcQ
