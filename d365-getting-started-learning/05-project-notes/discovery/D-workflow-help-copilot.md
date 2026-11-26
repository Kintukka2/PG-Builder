# D. Workflow, help, Copilot/AI, collaboration and user troubleshooting (D365 F&O)

Discovery research for the "D365 F&O Getting Started" procedure guide. End-user point of view; admin setup noted only where it decides what users see.

- **Researched:** 26 November 2026, against the live Microsoft Learn site and the source repository `MicrosoftDocs/dynamics-365-unified-operations-public` (main branch, sparse checkout of the article Markdown). Each feature lists the article's `ms.date` where it matters.
- **URL convention:** a repository path `articles/<path>.md` is published at `https://learn.microsoft.com/en-us/dynamics365/<path>`. Full URLs are in the final section.
- **Screenshots:** saved in `media/workflow-help-copilot/` (28 files). Many Microsoft screenshots are old (2017 client, "Finance and Operations Preview" banner). Use them to see the layout, not as current captures. Retake in our own environment for the guide.
- **Cross-references to other researchers:** navigation bar, search, Favorites, workspaces and "Open in new window" (UI shell); grids, filters and saved views (grids); Excel, reports, alerts, batch jobs and the Action center for batch results (Excel/reports/alerts).

---

## PART A: WORKFLOW (END USER)

### A1. Workflow: what it is and who takes part

**Plain English:** a workflow is a business process that D365 runs on a document (a journal, a vendor invoice, a purchase requisition, a customer change). It decides who must do a task, make a decision or approve, in what order and under what conditions. Your organisation configures each workflow, so the steps, approvers and buttons you see depend on that configuration.

**Key concepts (Workflow system overview; Workflow elements; Actions in workflow approval processes):**

| Term | Meaning |
|---|---|
| Workflow (system) | Functionality on the AOS that lets an organisation build business processes. |
| Workflow (business process) | How a document moves through the system: who completes a task, makes a decision or approves. |
| Workflow instance | One run of a workflow for one submitted document. It is created when you submit. |
| Originator | The person who submits the document (for example, selects **Submit** on the **Expense report** page). |
| Task assignee | A person (or a member of a work item queue) who must complete a manual task, such as reviewing receipts. Only one person can complete a task. |
| Decision maker | A person who answers a question (Yes/No, True/False). The answer picks the branch the workflow follows. |
| Approver | A person in an approval step who can approve, reject, request change or delegate. |
| Work item | The item that the workflow assigns to you to act on: a task, a decision or an approval. |
| Work item queue | A shared queue monitored by several people. One member accepts the item and the others no longer need to act on it. |
| Manual task / automated task | Work done by a user / work done by the system with no user (for example, a credit check). |
| Approval process / approval step | A sequence of approval steps. At each step the user can approve, reject, request change or assign the document to another user. |
| Manual decision / conditional decision | A branch point decided by a user / decided by the system from conditions. |
| Parallel activity / subworkflow | Branches that run at the same time / a workflow that runs inside another workflow. |
| Line-item workflow | Each line of a document is submitted to its own workflow, for example timesheet lines routed by project ID. |

Benefits named by Microsoft: consistent processes, process visibility (status, history, metrics) and a **centralized work list** of tasks and approvals assigned to you.

- **Screenshots:** `workflow-diagram-expense-report-users.gif` (expense report flow, users per element), `workflow-diagram-originator-task-decision-approvers.gif` (originator, queue, decision maker, approvers), `workflow-diagram-line-item-workflow.gif`.
- **Sources:** overview-workflow-system (ms.date 03/10/2026), workflow-elements, workflow-actions (03/10/2026).

### A2. The workflow message bar and instructions

**What users see:** when a document is under workflow, a message bar on the page shows the workflow information.

- **Originator:** the workflow can have **Submission instructions**. *"To view instructions, the originator selects the icon in the workflow message bar."* (Configure workflow properties.)
- **Assignee/approver/decision maker:** each step has a **Work item subject** and **Work item instructions**. *"The subject line appears in a message bar on the page. The user can then select the icon in the message bar to see the instructions."* (Configure approval steps; Configure manual tasks; Configure manual decisions.)
- Instructions can contain placeholders (for example, *Last Notes: %Workflow.Last note%* shows the comment from the previous step), and they can be translated per language.

**Gotcha:** Microsoft documents the message bar only from the configuration side. No end-user article shows the bar's layout or the exact label of its icon. A clean-session check in our environment is needed to name it.

### A3. The **Workflow** button and its actions

**How it appears:** on a page whose document is enabled for workflow, the Action Pane shows a **Workflow** button (a menu). Its items depend on your role in the current step and on how the workflow was configured. Documented paths: **Workflow** > **Submit**, **Approve**, **Reject**, **Request change**, **Delegate**, **Resubmit**, **Cancel**, **View history**, **Recall** (vendor bank account, customer workflow, lease workflow, vendor invoice, free text invoice, general journal articles).

**Submit (originator).** Select **Workflow** > **Submit**. A dialog box asks for a comment. The approver sees this comment with the document. Select **Submit**. *(Use lease approval workflows: "In the dialog box that appears, add a comment. The designated approver sees this comment together with the lease.")*

**Actions by role (Actions in workflow approval processes):**

| Role | Action | What happens |
|---|---|---|
| Originator | **Submit** | Starts the workflow instance. |
| Originator | **Resubmit** | After a rejection or a change request. The originator can change the document first or resubmit the original. After a rejection, the workflow restarts at the step that was rejected (task or approval process). After a request change, it goes back to the first approver/queue. |
| Originator / any user | **Recall** | Stops the workflow so the document isn't processed. From the **Workflow history** page: select **Recall**, enter a comment, select **OK** (lease article). Also resets documents in **Unrecoverable** status to **Draft** (see A4). |
| Any user (documented for vendor bank accounts) | **Cancel** | Cancels the workflow in progress. The record returns to its pre-submission status so it can be edited and resubmitted. *"The original submitter might use this function to correct an error."* |
| Task assignee | **Complete** | The document goes to the next user, or the workflow ends. |
| Task assignee / approver | **Reject** | The workflow process ends. The originator can resubmit. |
| Task assignee / approver / decision maker | **Delegate** | The task goes to another user, who acts on your behalf. The workflow continues as if you had acted. |
| Task assignee / approver | **Request change** | The document goes back to the originator. |
| Queue member | **Reassign** | Moves the document to another queue (or, on the **Workflow history** page, the **Reassign** button reassigns a work item to another user). |
| Queue member who accepted a task | **Release** | Returns the document to the queue so another member can complete it. |
| Approver | **Approve** | The document goes to the next approver, or the workflow ends. |
| Decision maker | **[Choice 1]** / **[Choice 2]** (for example **Yes**/**No**) | The answer picks the branch. |
| Anyone with access | **View history** | Opens the **Workflow history** page for the document (A6). |

- After choosing an action, the user enters a comment in a dialog box and confirms (lease article).
- *"The available actions vary, depending on how the software developer designed the task."* The workflow configuration also switches each action on or off: **Advanced settings** has check boxes for **Complete**, **Reject**, **Request change**, **Delegate**, **Reassign** and **Release** (Configure manual tasks).
- Lease workflow labels in the article are inconsistent ("**Rejected**", "**Canceled**", "select the **Approved** action"). The button labels should be confirmed in the client.
- **Screenshot:** none from Microsoft shows the Workflow menu in the current client. Capture our own.

### A4. Workflow status meanings

There is no single Microsoft table of workflow statuses. Each document type shows its own status field. Documented values:

**Purchase order Approval status (change management on), Purchase order approval and confirmation:**

| Approval status | Meaning | Request change enabled |
|---|---|---|
| Draft | Not yet submitted to the PO workflow. | No |
| In review | Submitted; approval pending. | No |
| Rejected | Rejected during approval. | No |
| Approved | Approved. (Orders created without a workflow are Approved immediately.) | Yes |
| In external review | Sent to the vendor to confirm terms (purchase inquiry or confirmation request). | n/a |
| Confirmed | Confirmed; can't be confirmed before approval. | Yes |
| Finalized | Financially closed; can't be changed. | No |

**Vendor bank account Review status (Vendor bank account workflow):** **Draft**; **Approved**; **Approved, changes not submitted**; **Approved, pending changes**. Reject or Cancel returns the record to **Draft** or **Approved, changes not submitted**.

**Customer and vendor change proposals:** after **Workflow** > **Submit**, the status changes to **Changes pending approval** (Customer workflow; Vendor workflow).

**Journals:** the **Approval status** field shows the workflow status of the journal or line (credit limit adjustment journal article). The general journal article does not list the values.

**Workflow instance events** (for notifications, Configure workflow properties): **Started**, **Stopped** (stopped because of an error), **Completed**, **Unrecoverable** (stopped because of an unrecoverable error), **Terminated**.

**Unrecoverable, and resetting to Draft:** *"A workflow instance that stops because of an unrecoverable error has a workflow status of Unrecoverable."* To reset to **Draft** so the document can be edited, select **Recall** on the **Workflow history** page (open it from the document or from **Common > Inquiries > Workflow**), or select **Recall** on the document's list page. This needs a feature switched on in **Feature management**:
- **Resetting the workflow status for vendor invoices from Unrecoverable to Draft** (vendor invoice; also the **Pending vendor invoices** page)
- **Resetting the workflow status for free text invoices from Unrecoverable to Draft**
- **Resetting the workflow status for journals** (general journals; select the **Workflow** button on a journal on the **Workflow history** page)

**Gap:** statuses such as *Not submitted*, *Submitted*, *Change requested* on journals and vendor invoices aren't tabled anywhere on Learn. Confirm them in our environment per document type.

### A5. Work items assigned to me (the work list)

- **Dashboard:** the default dashboard has a **Work items assigned to me** area: *"a view of all work items that were generated and assigned to you from a workflow. The list provides an overview and links to the relevant pages where you can take action."* (Default dashboard, ms.date 03/10/2026.)
- **Page:** **Common > Common > Work items > Work items assigned to me** (Delegate work items), also written **Modules > Common > Work items > Work items assigned to me** (lease article). Select the document link (for example, the **Lease ID**) to open the record, then use the **Workflow** button there.
- **Immersive Home** (10.0.44+, feature switched on) also lists workflow work items as activity cards and often lets you act without leaving the page (C4).
- **Gap:** no Microsoft article lists the other work item pages (for example, queue items or items you submitted) or the columns of **Work items assigned to me**. Check the **Common > Work items** menu in our environment.
- **Screenshot:** `default-dashboard-work-items.png` (current default dashboard); `help-support-menu-support-search.png` (2017 dashboard with the **Work items assigned to me** list, for example "Expense reports : Record returned").

### A6. Workflow history (and Summary by Copilot)

**Open it:** **Workflow** > **View history** on the document, or **Common > Inquiries > Workflow > Workflow history** (View workflow history; the vendor invoice article spells it "Inquires").

**Fields on the page (View workflow history):**

| Field / button | Meaning |
|---|---|
| **Instance ID** | ID of the workflow instance processing the document. |
| **Status** | The document's workflow status. |
| **Workflow ID** | ID of the workflow. |
| **Document** | ID of the document. |
| **Document type** | Type of document submitted. |
| **Workflow** | Name of the workflow. |
| **Version** | Version of the workflow. |
| **Created date and time** | When you submitted. |
| **Elapsed time** | Time since you submitted. |
| **Resume** | Resumes the workflow for the selected document. |
| **Recall** | Recalls the document so that it isn't processed. |
| **Work items** section | Work items for the document (tasks still to complete, approvals). **Reassign** opens a dialog to reassign a work item to another user. |
| **Tracking details** section | The history of the document in the workflow. |

**Summary by Copilot (Workflow history summary):**
- *"The Summary by Copilot field appears at the top of any Workflow history page if you submit the workflow."* First line: submitter, submitted date, current status, comments. Then the most recent actions (approvals, delegations, rejections, change requests) with dates, users and comments. Long comments might be summarised.
- Purpose: a concise summary that helps approvers decide faster.
- **On by default** from 10.0.40 and in the 10.0.39 PQUs (Feature management: **Workflow history summary**). Needs the latest PQU on 10.0.39/10.0.40 and the **Copilot in Microsoft Dynamics 365 Finance** app in Dataverse. Role: anyone who can view workflow history.
- Languages: see Microsoft's "Explore Copilot features by geography and languages" report. *"Although you can use the feature in other languages, it might not work as intended."*
- **Contradiction in Microsoft's FAQ:** the page says comments are summarised; the Transparency FAQ says *"Comments that are entered during the approval process aren't processed."* The FAQ also carries a stray line about the **Collections coordinator summary** feature. Flag before quoting.
- **Sources:** view-workflow-history; workflow-history-summary (03/10/2026); workflow-history-summary-FAQ (03/12/2026).

### A7. Delegating work items (including while away)

**One work item (Delegate work items):** select **Workflow** > **Delegate**, enter the user to delegate to and a comment. The work item is reassigned to that user.

**Several work items at once:**
1. Go to **Common > Common > Work items > Work items assigned to me**.
2. Select the work items.
3. Select the **Delegate work items** menu.
4. In **User**, select the user.
5. In **Comment**, enter why.
6. Select **Delegate work items**.
- Only for **Purchase agreement approval workflow**, **Purchase order workflow**, **Purchase requisition review** and **Vendor invoice workflow**. The **Delegate multiple work items** feature is **off by default**; an administrator enables it in **Workspaces > Feature management**.

**Automatic delegation while away (your own settings):**
1. Go to **Common > Setup > User options** (also reachable from **Settings** (gear) > **User options**).
2. Select the **Workflow** tab and expand **Delegation**.
3. Select **Add**.
4. **Scope:** **All** (all work items assigned to you), **Module** (one type of workflow; pick it in **Name**) or **Workflow** (one workflow; pick it in **Name**).
5. **Delegate:** the user to delegate to.
6. **Start date/time** and **End date/time**.
7. Select **Enabled**.
8. **Comment:** why you're delegating.
- Applies to **new** work items assigned during the period ("automatically delegate new work items").
- The delegate acts on your behalf; the workflow continues as if you had acted (A3).

### A8. Workflow notifications and email

- **Per-user notification settings (Enable users to receive workflow-related email messages):** **System administration > Users > Users** > select the user > **User options** > **Workflow** tab > **Notifications** section:
  - **Line-item workflow notification type:** **Grouped** (one email for all line items) or **Individual** (one email per line item).
  - **Send notifications in email** check box. *(The article's sentence is garbled: "If you want the user to receive notifications in the client, select the Send notifications in email check box." Confirm what the box does in our environment.)*
  - The same **Workflow** tab appears in each user's own **User options** (Personalize the user experience lists the tabs **Visual**, **Preferences**, **Account**, **Workflow**).
- **What triggers notifications:** the workflow owner chooses events (**Started**, **Stopped**, **Completed**, **Unrecoverable**, **Terminated**), the recipients (participant role/group, workflow user, or named users) and the notification text, and selects an **Email template for workflow notifications**. Email templates come from system or organisation email templates, depending on whether the workflow is system-level or company-specific.
- **Workflow FAQ, end-user points:**
  - *Why multiple notifications when a work item is rejected?* Rejecting completes your work item as rejected and creates a new "change requested" work item for the originator; each item sends its own notification.
  - *Workflow emails don't create Action Center messages:* "Workflows have built-in email notifications ... Those notifications don't result in Action Center messages for users." A future update is planned to add one. Organisations can use workflow business events with Power Automate for other notifications.
  - Alerts on records changed by workflow are possible but "not ideal".
- **Setup dependency:** email sending must be configured by IT (cross-ref the Excel/reports/alerts researcher for email setup and alert emails).

### A9. Due dates, escalation and multiple approvers (what users experience)

From Configure approval steps (configuration, but it explains what users see):
- **Time limit:** each step can have a **Duration** (hours, days, weeks, months, years, using the organisation's calendar). *"If the user doesn't take action on the document in the allotted time, the document is overdue."*
- **Escalation:** an overdue document can be reassigned automatically along an escalation path (for example Donna, then Erin, then the final action **Reject**). After the path, the system takes an end action automatically.
- **Completion policy** when a step is assigned to several people: **Single approver** (first response wins), **Majority of approvers**, **Percentage of approvers**, **All approvers**.
- **Conditions:** a step can run always, or only when conditions are met (for example amount > USD 10,000).
- **Screenshot:** `workflow-diagram-multiple-approvers-completion-policy.gif`.

### A10. Can the submitter approve their own document?

Workflow FAQ: *"Yes, a submitter of a workflow can approve the workflow unless the setting Disallow approval by submitter is enabled for the workflow."* Path (admin): **System administration > Workflow > Workflow parameters > General > Approver**.

### A11. Line-item workflow

Each line of a document can be submitted to its own workflow (one workflow for all lines, or a workflow per line based on conditions). Users may receive line-level work items. The per-user notification setting **Line-item workflow notification type** (Grouped/Individual) controls the emails.

### A12. Mobile approvals

- The **Finance and operations (Dynamics 365) mobile app** and its workspaces, including **Invoice approvals**, **Purchase order approval** and **My team**, are deprecated (announced June 2022, end of support targeted October 2024). Current banner: *"The finance and operations (Dynamics 365) mobile app and platform are no longer supported ... The mobile app has also been removed from app stores. Previously installed instances of the app will continue to work."*
- Replacement: mobile experiences built with **Power Apps** over virtual tables (Building mobile experiences over finance and operations data).
- **Do not teach the mobile app.** If our organisation offers mobile approvals, it will be a custom Power App or Power Automate approvals.

### A13. Teams and Outlook approvals

- Nothing out of the box in finance and operations apps. Microsoft documents a pattern: a **workflow business event** (category **Workflow workitem**) triggers a **Power Automate** flow that starts a **Start and wait for an approval (v2)** approval, which users answer in Teams/Outlook/Power Automate. The outcome completes the work item with **WorkflowWorkitem-complete** (Business events and workflow approvals).
- Only relevant if our IT built such flows. Ask IT before mentioning it.
- **Expense Agent** (Project Operations, preview) does put expense report review and submission in a Teams interface (C7).

### A14. Workflow: admin/feature summary

| Item | Who | Notes |
|---|---|---|
| Workflows configured per document type | Admin/BPO | Workflow editor (ClickOnce app; see E3). |
| **Delegate multiple work items** | Feature management | Off by default. |
| **Workflow history summary** | Feature management | On by default 10.0.40+. |
| **Resetting the workflow status ...** (vendor invoices, free text invoices, journals) | Feature management | Enables Recall from Unrecoverable. |
| **Disallow approval by submitter** | Workflow parameters | Blocks self-approval. |
| Workflow email notifications | Admin | User options > Workflow > Notifications; email templates. |
| Workflow Message Processing batch job | Admin | Can be set as critical (dev-itpro article). Delays in this job delay work items. |

---

## PART B: HELP AND LEARNING

### B1. The Help & Support (?) menu

- The navigation bar contains **Dynamics 365 portal**, **Search**, the company picker, **Action center**, **Settings**, **Help & Support** and the user profile (User interface elements).
- Documented items on the **?** menu:
  - **Help**: opens the **Help** pane (B2).
  - **Support**: *"Select the Help button (?) in the upper-right corner of the app, and then select Support."* (Get support for finance and operations apps.) The Help menu item is also called **Contact your support team** (Support experience; controlled by the *SysLCSCPSIssueEntry* privilege on the System user role) (B8).
  - **About**: documented inconsistently as **Settings > About** (gear), **Settings > Help & Support > About** (with a **Licenses** tab showing tenant name and ID), and "**System administration** > **About**" in one finance article (B9).
- **Task recorder** is on the **Settings** (gear) menu, not the ? menu: **Settings > Task recorder** (B4).
- **Screenshot:** `help-support-menu-support-search.png` (2017 client: ? menu with **Help** and **Support**).
- **Gap:** no current Learn article lists the full ? menu. Check our environment for items such as **Help**, **Task guides**, **Support**, **About** and any custom links.

### B2. The Help pane

- **Open:** select **Help** (**?**) > **Help**, or press **Ctrl+Shift+?** (Help system article). The Keyboard shortcuts article lists **Ctrl+?** for "Open the help pane". Test which one works.
- **Tabs:** **Help** (articles for the current page) and **Task guides** (when task guide libraries are connected). Custom help can add another tab (Connect a custom Help website). The 2017-era screenshot also shows a **Search** box and a **RESOURCES** list (**Help**, **Ask the community**, **CustomerSource**).
- **Behaviour:** *"When you first open the Help pane, the Help tab shows the topics that apply to the page that you're currently on. If no topics are found, you can enter keywords to refine your search. When you select an article in the Help pane, it's opened on a new tab in your browser."*
- Help content comes from Microsoft Learn (and any custom help site).
- **Screenshot:** `help-pane-help-tab.png` (Help pane beside a sales order; shows the **Help** and **Task Guides** tabs, "Showing help content for the current page", publisher "Microsoft").

### B3. Task guides (playing them to learn)

- *"A task guide is a controlled, guided, interactive experience that leads you through the steps of a task, or business process."*
- **Play:** open the **Help** pane > **Task guides** tab > select a guide. The pane shows the steps. Select **Start task guide** at the bottom of the pane. *"A black pointer shows you where to go first. Follow the instructions that appear in the user interface (UI), and enter data as directed."*
- **IMPORTANT (quote for the guide):** *"The data that you enter when you play a task guide is real. If you're in a production environment, the data will be entered in the company that you're currently using."* Only play task guides in a sandbox/training environment.
- **Shortcuts while playing:** **Alt+R,L** Rails mode; **Alt+R,P** previous step; **Alt+R,N** next step; **Alt+R,F** focus between page and pop-up; **Alt+R,C** expand/collapse pop-up; **Alt+R,M** show more/less (Keyboard shortcuts).
- **Language:** translated task guides are in libraries titled "All languages". Each user changes the task guide language under **Options > Preferences** (user language). Untranslated guides show only the control text in your language.
- **Availability gotchas:**
  - *"Microsoft released task guide libraries for product versions through the December 2017 release."* Microsoft's own task guides are old.
  - The **Task guides** tab only works after an admin connects BPM libraries in Lifecycle Services on **System parameters** > **Help** (Configure the Help experience).
  - Task recordings can only be created, edited or used in **Sandbox and Production** environments from January 2026 (Task recorder resources).
  - Lifecycle Services (LCS) is being consolidated into Power Platform admin center; LCS-dependent help may change. (The LCS freeze banner include is empty in the source, so Microsoft's wording isn't available.)
- **Screenshots:** `help-pane-task-guide-reading-view.png`, `task-guide-step-pointer.png`, `task-guide-playback-1.png` to `task-guide-playback-4.png`.

### B4. Task Recorder (end-user view: playing a recording)

- **Open:** **Settings > Task recorder**.
- **Main menu (Task recorder quick reference):** **Create recording**; **Play recording as guide** (see the recording as a Help article or play it as a task guide); **Edit recording**; **Playback recording** (automatically run the steps).
- **Open options:** **Open from this PC** (an .axtr file someone gave you), **Open from Lifecycle Services**, **Open from recents**.
- Playing a guide from a file: **Settings > Task recorder** > **Play recording as guide** > **Open from this PC** > choose the .axtr file > **Start**.
- Tip from Microsoft: refresh the browser before recording or playing back; a refresh creates a new session and restarts Task recorder.
- Training authors (not end users) can **Export as Word document** to produce printable guides; screenshots need a prerelease Chrome extension (System requirements).
- **Relevance:** useful if our training team ships .axtr files; otherwise mention only briefly. Data entered during playback is real.

### B5. Field descriptions (tooltips)

- *"Some of the more complex fields have field descriptions. These descriptions appear when you hover over a field. If no description is available, you see the field name when you hover over the field."*
- **Field descriptions** page: **Select a page** (UI name, or AOT name shown by right-clicking a page, for example **CustTable**), optional **Include fields without a description**; export with **Open in Microsoft Office** > **FieldDescriptionTmp**. (The article does not give a menu path; find it with search.)
- Companies can customise field descriptions (developer task).
- **Screenshot:** `field-description-tooltip.png` (hover text for **Lock items during count**).

### B6. Microsoft Learn and other resources

- Help on Microsoft Learn: use a site search, for example **site:learn.microsoft.com dynamics 365 "search term"**; on the site, use **Filter by title** in the table of contents or the **Search** box.
- **RSS feeds** of updated articles (all finance and operations apps, or per app such as Finance).
- **Feedback** action below each article's title; **Edit** (pencil) to contribute (English only).
- Resources table: Dynamics 365 documentation, Microsoft Learn training, LCS*, Previous versions, Dynamics Community, Microsoft.com/dynamics365, Dynamics 365 guidance hub.
- **Videos** article: Microsoft Dynamics 365 YouTube channel (mostly admin/dev videos).
- Learn pages now offer **Ask Learn** ("Want to try using Ask Learn to clarify or guide you through this topic?").

### B7. Custom help (admin)

Organisations can connect their own help website to the Help pane (an extra tab), using Microsoft's toolkit (Azure Search, Visual Studio extension), and create custom task guides with Task Recorder saved to an LCS BPM library. **Implication for our guide:** if we want our own procedure guides surfaced in the Help pane, that is an IT project; otherwise link from the Training Hub.

### B8. Support: reporting a problem

- **In the client:** **?** > **Support**. Connect to Lifecycle Services if prompted. **Search** for Microsoft published updates and fixes (and Azure DevOps work items your IT tagged **#SearchableInFinanceAndOperations**). If no fix, select **Create** to create an issue. Non-admins see a **Request view** (request a hotfix); admins see a **Download view**.
- Issues go to the Azure DevOps project behind the LCS project's **Support** tile; IT can **Submit to Microsoft**.
- **Migration:** the LCS **Support** page is being retired; support requests move to **Power Platform admin center > Help + Support**, which needs an admin role (Service Support Administrator or Helpdesk Administrator) (Migration of LCS Support to PPAC, 03/06/2026).
- Admins can remove the ability to create issues from the client (privilege *SysLCSCPSIssueEntry*), and limit fix search (duty *SearchExistingFixes*).
- **Get support (summary table):** ask the Dynamics Community; licensing questions to partner/Microsoft; LCS **Issue search**; **?** > **Support**; LCS **Support** tile to open a Microsoft incident; feature requests at Dynamics 365 Application Ideas.
- **Implication for our guide:** end users should follow the company's own route (our BAU Support team, D-083), not the Microsoft route. Say what to capture (E8) and where to send it.
- **Screenshots:** `help-support-menu-support-search.png`, `help-support-connect-to-lcs-prompt.png`.

### B9. The About box

- **Settings** (gear) > **About**: shows **Loaded Packages and their Models** (versions) and a **Links** section (Microsoft user rights, privacy and cookies, plus the organisation's privacy statement if set in **System parameters**) (Version models; Legal terms; Privacy guide).
- **Settings > Help & Support > About** with a **Licenses** tab showing tenant name and ID (ISV licensing).
- **Gap:** Microsoft doesn't document an **Activity ID** or **Session ID** in the About box for end users. Check our build before telling users to copy anything from it.

---

## PART C: COPILOT AND AI IN FINANCE AND OPERATIONS APPS

### C1. Types of Copilot experience

From the Copilot overview (ms.date 08/04/2026) and Enable Copilot capabilities (03/05/2026):
- **Sidecar:** a chat pane on the right of the page; *"the primary Copilot interface in finance and operations apps"*. Example: generative help and guidance.
- **Embedded:** AI built into pages: summaries (**Summary by Copilot** FastTabs/fields), the Confirmed purchase orders with changes workspace, reminder email drafts.
- **Outside:** agents outside the client that work with F&O data: Microsoft 365 Copilot / Work IQ, Copilot Cowork, Copilot Studio agents, Finance Agent in Outlook/Excel.

**Features available in all finance and operations apps (Microsoft table):**

| Feature | What it does | Status |
|---|---|---|
| Generative help and guidance | Conversational sidecar that answers questions from documentation. | GA |
| Workflow history summary | AI summary on the **Workflow history** page. | GA, on by default 10.0.40+ |
| Enhanced user feedback for Copilot and related experiences | Thumbs up/down plus written feedback. | 10.0.43+ |
| Chat with finance and operations data | Ask an agent about F&O data the user can access (Copilot Studio knowledge sources). | Preview |
| Immersive Home | AI-first landing page with work items and agents. | Production-ready preview in docs; GA 13 March 2026 per 2025 wave 2 plan |
| Dynamics 365 ERP MCP server / Build an agent | For agents built by developers/makers. | Admin/dev |

**Dynamics 365 Finance:** Collections coordinator summary; Customer page summary; Workflow history summary; Agent management (production-ready preview); **Account Reconciliation Agent** (production-ready preview).

**Supply Chain Management features that finance users meet (P2P):** Vendor summary, Purchase order summary, Released product details summary, Product hover summaries; Confirmed purchase orders with changes; Procurement Agent (production-ready preview).

### C2. Copilot sidecar: generative help and guidance

**Open it:** select the **Copilot** button at the top of each page (the Copilot icon in the navigation bar). The pane opens on the right: *"Have a question about this app? Ask Copilot. Copilot can answer questions about app functionality and features, including troubleshooting guidance."* Type in the box (*"Ask a question about the data in this app, or tell me what you're looking for"*, 500 characters) and send. Footer: *"Make sure AI-generated content is accurate and appropriate before using."*

**What it can do (documented):**
- Answers questions about using finance and operations apps, grounded in Microsoft's **public documentation** on learn.microsoft.com, with citations (query rewrite > Bing search of learn.microsoft.com > LLM answer with citations).
- Admins can add **custom knowledge** in Copilot Studio (PDF, RTF, Word files, SharePoint), so it can answer from company documents such as our procedure guides, and can allow **general knowledge** (the language model and Bing web content) after custom sources are exhausted.
- **Questions about data**, **client actions** (such as navigation) and **automation** are documented as *extension* scenarios. Makers build them in Copilot Studio (Chat with finance and operations data; Create client plugins). Out of the box the sidecar is a help assistant. *"Future enhancements are expected to expand the system's capabilities so that they include direct navigation and proactive action suggestions."*
- **File and screenshot attachments** (10.0.45+, features **Enable user attachments in Copilot sidecar** and **Enable ability for user to attach a screenshot to Copilot sidecar**): select **Attach** > **Browse...** > file > **Open**, or **Attach** > **Add screenshot** > **Allow**. By default Copilot does **not** use the attachments unless makers extend it (for example, a topic that reads a screenshot of an error and suggests a fix).
- **Zero prompt** (preview): makers can show suggested prompts when the pane opens (feature **Enables zero prompt experience extensibility**).

**Limitations and responsible use (Responsible AI FAQ for generative help, 05/08/2026):**
- *"The generated guidance should always be used with a critical eye to identify if the answer provided is correct and sufficient to complete your task."*
- *"Always review generated content, help and guidance before commencing the steps."* *"Follow reference links to the source documentation."*
- Intended use: help new users onboard, solve problems, reduce training needs.
- Microsoft's answers reflect standard D365, not our configuration, unless custom knowledge is added. That's the key teaching point for our users.
- Report inappropriate content at msrc.microsoft.com/report.

**Feedback:** thumbs-up/thumbs-down buttons in the sidecar and under summary cards. With **Enhanced user feedback** on (10.0.43+, feature *Enable user feedback for Copilot and related experiences*; on by default from 10.0.44 per the article; also needs tenant and Dataverse settings), a **Submit feedback to Microsoft** dialog asks for written comments and can attach the conversation history (the user can review and remove attachments). Admins read feedback in Microsoft 365 admin center > **Health** > **Product feedback**.

**Admin/availability:**
- Needs Power Platform Integration (a linked Dataverse environment) and the **Copilot for finance and operations apps** app; usually deployed automatically.
- Needs Bing Search, and cross-region data movement where the AI services are not in the Dataverse region. *"If Bing Search is disabled, or if cross-region data movement is required but is disabled, users won't be able to open the Copilot sidecar, or the Copilot sidecar won't provide answers."*
- Tenant setting **Publish Copilots with AI features** must be enabled.
- The feature *User experience for Copilot in Finance and Operations* is mandatory from 10.0.40 (could be switched off only in 10.0.38/10.0.39). To hide the sidecar, admins turn off Bing Search or Copilot for Power Apps.
- Not supported in LCS-deployed developer environments.
- **User troubleshooting tip (documented):** *"In your finance and operations app, you might have to refresh the browser before you can use Copilot."*
- **Screenshots:** `copilot-button-icon.png`, `copilot-sidecar-welcome.png` (sidecar labelled PREVIEW beside the Confirmed purchase orders with changes workspace; shows "AI-generated content may be incorrect" and thumbs on embedded cards), `copilot-sidecar-explain-workflow-answer.png` (sidecar answering a workflow question), `copilot-feedback-thumbs.png`, `copilot-feedback-dialog.png`.

### C3. Embedded AI summaries relevant to our streams

**Customer page summary (O2C; ms.date 08/05/2026):**
- Open **All customers** and select a customer: the AI text is on the **Summary** FastTab (customer account status and insights).
- Inputs: customer invoices, payments, sales orders, sales agreements, rebates, outstanding invoices, delayed order lines, from the past year starting at the session date. *"All calculations are done in Finance."*
- Needs 10.0.39 latest hotfix; a menu item such as CustTrans or SalesTable. Feature management: **Customer summary – Customer page summary**, on by default.

**Collections coordinator summary (O2C; 06/04/2026):**
- **Credit and collections > Workspaces > Collections coordinator** > select a customer name (or **View customer details**). The **Collections coordinator details** page has a **Summary by Copilot** field under **Balances and payment history**: payment history for the past year, outstanding debt, invoices for the last six months.
- **Create reminder email**: prompt *"A reminder email is created by using AI. Make sure AI-generated content is complete, accurate, and appropriate before using. Do you want to create the email?"*; **Yes** opens a draft in your default email service, **No** cancels.
- *"It's your responsibility to review and edit the suggested content to ensure that it's complete, accurate, and appropriate before you send the email."*
- Features **Collections coordinator workspace** and **Collections coordinator summary**, on by default; needs the **Copilot in Microsoft Dynamics 365 Finance** app.

**Workflow history summary (all streams):** A6.

**Vendor summary and Purchase order summary (P2P; SCM article 05/07/2026):** **All vendors** details > **Summary by Copilot** FastTab (vendor currency, hold status, number of POs, posted invoices, payment status, overdue vendor invoices ...); **All purchase orders** details > **Summary by Copilot** FastTab (Status and Insights sections with filter buttons such as **Not fully received**, **Fully received, not fully invoiced**). Feature management: **Vendor summary**, **Purchase order summary** (on by default). Information is limited by the user's security roles.

**Common admin prerequisite (Enable Copilot in Dynamics 365 Finance, 06/04/2026):** Finance 10.0.38+, Power Platform Integration, the **Copilot in Microsoft Dynamics 365 Finance** app, cross-region data movement where needed, and the Dataverse security role **Finance and Operations AI** for users who need the features. (D-083: users aren't told about security roles; the guide says to contact BAU Support if a feature is missing.)

**Gotcha:** if cross-region movement is required and not allowed, *"users can't see the copilot summary, or the copilot summary doesn't provide answers."*

### C4. Immersive Home

- **What it is (ms.date 05/07/2026):** *"a modern, AI-first landing page that adapts to your most important work, aids decision making, and reduces the need to navigate elsewhere to complete common tasks."* An option for your initial page.
- **Areas:**
  - **Greeting and summary** (welcomes you by name and summarises work).
  - **Suggestions** (for example, enrol an agent for a task).
  - **Work items**: priority-ranked activity cards, including **workflow work items** such as expense approvals and agent-prepared items. Similar items can be collapsed into one card; most can be completed on the card; add long-running ones to **Pinned items**. A card shows the activity type, a summary, action buttons and a navigation link. Completed activities disappear.
  - **Agent activity** (only when agents are enabled): metrics per agent, **View activity** and **View agents**.
  - **Workspaces**: tiles ranked by recent use, favourites first; tiles show information you pinned (**Personalize: <tile name>** > **Pin to dashboard**).
- **Prerequisites:** version 10.0.44+; feature **Immersive Home** in Feature management; privilege *View immersive home* (duty with the same name, in the System User role by default).
- **Limitation (RAI FAQ):** *"Immersive Home doesn't yet use AI to rank work or identify the most relevant tasks."* Review AI-generated work items before acting.
- **Set as initial page:** cross-ref the UI shell researcher (Set the preferred initial page).
- **Version notes:** the 2025 wave 2 plan lists "Stay focused and simplify tasks with Immersive Home and adaptive experiences": preview 6 June 2025, GA 13 March 2026, "Users by admins". The documentation still says "production ready preview" in places.
- **Screenshot:** `immersive-home.png`.

### C5. Agents in the client: Agents page and Agent activity

- **Agent management** (production-ready preview; ms.date 05/07/2026): users discover, configure and manage agents.
  - **Agents** page with **Library** (templates, preview, configure) and **Manage** (active agents, edit configurations, activate/deactivate tasks).
  - **Agent activity** page: a log of agent actions, kept 90 days by default.
  - **Get there:** from **Immersive Home** (**View activity** / **View agents**) or search for **Agents** / **Agent activity**. The Account Reconciliation Agent article also says **Modules > Agents**.
- First activation opens a configuration wizard.
- **Prerequisites:** 10.0.44 (10.0.2263.30)+, Immersive Home on, Dataverse linked, **Copilot for Finance and Operations apps** solution 1.0.03021.3+, **Copilot** feature flag in Power Platform admin center, **Copilot Studio billing (credits)**; then **Agent management** in Feature management.
- **End-user facts:** *"Your organization is billed for each deployed agent. If your organization exhausts its allocated credits, agents might be temporarily deactivated."* Admins can cancel agent actions by deleting the agent's batch jobs.

### C6. Account Reconciliation Agent (R2R)

- **What it is (ms.date 11/02/2026; production-ready preview):** the **Account reconciliation** workspace raises exceptions between subledgers and the general ledger, and the agent evaluates them and recommends an action, moving reconciliation from SSRS reports to a continuous process.
- **User steps (documented):**
  - Turn on **(Preview) Account reconciliation agent**; **Modules > Agents** > **Account reconciliation** template; start date; modules in priority order; daily/monthly exception limits; optional alerts (**Enable balance alert**, **Enable daily/monthly limit alert** at 50/75/90%, **Notify if a run is skipped due to limit**); review, confirm, activate.
  - Recommendations: for **Voucher amount mismatch**, for example **Create journal entry**; alternatives **Reverse**, **Link transactions**, **Accept without change**.
  - Exception types processed: **Voucher amount mismatch**; **Pending accounting transferred to general ledger**.
  - **Suggested action** shows a summary only when the user language is **EN-US**.
  - Activity: **Addressed exceptions** > **Activity** pane timeline (**Fix suggested by agent**, **Reconciled** with an undo option); the **Account reconciliation agent** card shows the number of suggestions.
- **Admin:** Finance 10.0.46+; features Immersive Home, Agent management and (Production ready preview) Account reconciliation agent; packages **Copilot for finance and operations apps** 1.0.3048.2+ and **Copilot in Microsoft Dynamics 365 Finance** 1.0.3049.1+; a dedicated agent identity user (roles such as *Account reconciliation agent* and *System user*); deployment through the **Agent deployment wizard** in Copilot Hub (Power Platform admin center); **Move data across regions** may be needed.
- **Notes:** *"Microsoft might automatically update the AI model used by the service."*
- **Release plans:** "Reconcile accounts faster using the enhanced Account reconciliation agent" (2025 wave 2, preview 24 Oct 2025). "Enhancements to Account reconciliation agent" (2026 wave 1, GA Sep 2026): refreshed workspace, bulk approve/reject, fuzzy matching, agent feed, MCP, inventory module; later fixed assets, project accounting, intercompany.
- **Decision for us:** include only if our organisation has deployed it; otherwise one line in "AI features you may see later".

### C7. Other agents finance staff may meet

| Agent | Where | Stream | Status / licensing (as documented) |
|---|---|---|---|
| **Finance Agent in Outlook: Collections in Outlook** | Outlook add-in (**All Apps** > **Finance Agent** > **Connect with your ERP** > **Dynamics 365 Finance** > environment > **Get Started**) | O2C | Preview. Summarises customer emails, shows customer details, outstanding invoices, account statements and contacts from D365 Finance, drafts replies and new emails, saves notes/summaries to Dataverse. Needs Tier 2+ Finance with Power Platform Integration, the same tenant, and Finance permissions on listed entities. AI content and UI **en-US only**. "Finance is a capability included with Microsoft Copilot." |
| **Financial Reconciliation agent** | Excel (Finance Agent sidecar) | R2R | Prerelease docs. Reconciles two tables in a workbook, AI-suggested rules and mappings, report of unmatched / potentially matched / perfectly matched, AI summary. Assistive or autonomous. |
| **Finance Agent in Microsoft Copilot chat (Frontier)** | Microsoft 365 Copilot chat | O2C/P2P | Frontier preview programme only. Finance Home, business intelligence Q&A, business briefs, AR/AP ERP Q&A and actions through MCP. |
| **Expense Agent** | Outlook shared mailbox, Expense mobile app, D365, Microsoft **Teams** for report review/submission | P2P/expenses | Production-ready preview; Dynamics 365 **Project Operations** (Integrated with ERP / for manufacturing). Creates and itemises expense lines from receipts, auto-matches card transactions, groups reports, flags policy violations; users submit in Teams or **Open in Expense**. |
| **Procurement Agent** | SCM: **Emails from vendors** workspace, impact analysis | P2P | Production-ready preview. Classifies vendor emails (confirmation vs change request), applies PO changes after purchaser review, analyses downstream impact. |
| **Copilot Cowork with the Dynamics 365 ERP apps plugin** | Microsoft 365 Copilot Cowork (m365.cloud.microsoft) > **Sources & Skills** > **Dynamics 365 ERP apps** > **Finance & Operations** connector > **Configure** | All | 2026 wave 1 (preview 1 Jun 2026, GA 16 Jun 2026 per plan, "selected preview customers"). Needs a Microsoft 365 Copilot licence plus a qualifying D365 F&O licence, Copilot Credits, version 10.0.47 (or 10.0.46 PQU-2 / 10.0.45 PQU-7). Asks for approval before acting; **Always allow** applies only within the conversation. MCP guidance in US English; dates and numbers in ISO format. |
| **Dynamics 365 ERP in Work IQ** | Microsoft Copilot / agents | All | Preview (ms.date 11/17/2026). "ERP data in Ask" (read-only natural-language questions) and ERP MCP in Work IQ (agents can update records and run processes across F&O, Outlook and Teams). Business skills encode company procedure. |

**Common principle across all agents (quote-worthy):** *"Users can't access data or operations through Copilot Cowork that they can't access through the application."* and Work IQ: *"the agent can't do more than the user can do in the finance and operations apps client."*

### C8. What end users should know about AI (synthesis for a Getting Started topic)

1. **Verify everything.** Every AI surface carries "AI-generated content may be incorrect" or "Make sure AI-generated content is accurate and appropriate before using". Microsoft's FAQs tell users to review before acting and to follow source links.
2. **Your permissions apply.** Copilot, summaries and agents see only what your security roles allow. A missing summary or button usually means a feature, licence or access setting, so contact BAU Support (D-083).
3. **Help answers are generic.** Generative help is grounded in Microsoft's public documentation, not our setup, unless IT adds company knowledge. Our procedure guides take precedence.
4. **Data and privacy.** Summary calculations run in Finance; text is generated by Azure OpenAI through Dataverse. Cross-region processing may be enabled by admins. Feedback with attachments goes to Microsoft and is visible to admins in Microsoft 365 admin center.
5. **Language and region.** Features are validated for specific languages (Microsoft's geography/language report); some agent output is en-US only (Account reconciliation suggested-action summary; Finance Agent).
6. **Preview means preview.** Many agent features are "production-ready preview" under supplemental terms. They can change.
7. **Costs.** Agents and MCP calls consume Copilot Credits; agents can be paused when credits run out.
8. **Turning features on is an admin task** (Feature management, Power Platform admin center). Users don't enable Copilot themselves.

### C9. Release plan items in this area

The 2025 wave 2 and 2026 wave 1 plans are **archived as of October 2026** (moved to learn.microsoft.com/previous-versions). There is no 2026 wave 2 page (`/dynamics365/release-plan/2026wave2/` returns 404); Microsoft points to the Microsoft roadmap instead. Relevant items:

| Wave | Feature | Enabled for | Preview | GA |
|---|---|---|---|---|
| 2025 w2 (cross-app) | Stay focused and simplify tasks with Immersive Home and adaptive experiences | Users by admins | 6 Jun 2025 | 13 Mar 2026 |
| 2025 w2 (cross-app) | Ask about your ERP data in natural language | Admins, automatically | 21 Feb 2025 | 26 Jan 2026 |
| 2025 w2 (cross-app) | Connect AI agents to F&O data and business logic (expanded MCP server) | Admins | 18 Nov 2025 | 27 Jan 2026 |
| 2025 w2 (cross-app) | AI actions for F&O business logic | Admins | 15 Jul 2024 | 26 Jan 2026 |
| 2025 w2 (cross-app) | Build agents for F&O with Model Context Protocol | Admins | 19 May 2025 | 27 Jan 2026 |
| 2025 w2 (Finance) | Reconcile accounts faster using the enhanced Account reconciliation agent | Users by admins | 24 Oct 2025 | - |
| 2025 w2 (Finance) | Empower users with generative help and guidance within Business performance analytics | Users, automatically | 30 Aug 2024 | 31 Oct 2025 |
| 2026 w1 (Finance) | Enhancements to Account reconciliation agent | Users by admins | 30 Apr 2025 | Sep 2026 |
| 2026 w1 (cross-app) | Extend Copilot in F&O apps with client actions | Admins | 26 Apr 2024 | 24 Apr 2026 |
| 2026 w1 (cross-app) | Use Copilot Cowork to orchestrate insights and actions across Dynamics 365 ERP | Users by admins | 1 Jun 2026 | 16 Jun 2026 |
| 2026 w1 (cross-app) | Open records in Dynamics 365 ERP applications with deep links from copilot responses | Admins | 22 May 2026 | 18 Aug 2026 |
| 2026 w1 (cross-app) | Enable agents to work with attachments through Dynamics 365 ERP MCP server | Admins | 24 Apr 2026 | 3 Jul 2026 |

**Platform "What's new" (user-visible in this area):** 10.0.45 file attachments in the Copilot chat; 10.0.48 deep links in MCP responses, attachment support; 10.0.49 many ERP MCP enhancements, including human-in-the-loop tool annotations.

---

## PART D: COLLABORATION AND APPS

### D1. Microsoft Teams

- **No end-user Teams integration for finance and operations apps is documented** on Learn (no Teams app, no "share to Teams", no record chat). Searches of the F&O, Finance and dev-itpro documentation found only:
  - Collections coordinator workspace: *"Use the phone symbol to call the customer in Microsoft Teams, for example."* and an **Email** button for a blank email to the customer contact.
  - Expense Agent: generated reports in an interactive Teams interface.
  - Work IQ / ERP MCP agents running workflows across F&O, Outlook and Teams.
- **Deep links:** shareable, secured URLs to a record are a **developer** feature (URL Generator, `SysEntityNavigation`). From 10.0.48 Copilot responses built on the ERP MCP server include deep links to the records used.
- **Gap:** there is no Microsoft article for a user-level **Share**/**Copy link** button. Users share the browser URL (which carries the company `cmp=` and page `mi=`). Check whether our environment shows a share/link control before writing a step.

### D2. Outlook

- Finance Agent in Outlook (Collections) (C7).
- Collections page/workspace emails open Outlook (Outlook synchronisation set up by admins).
- Workflow email notifications (A8); alert emails (cross-ref the alerts researcher).
- Email "Use an email app, such as Outlook" choice when sending documents (Office integration; cross-ref).

### D3. Mobile

- Finance and operations mobile app: **deprecated and removed from app stores** (A12). Don't teach it.
- Power Apps mobile apps built by the organisation; Dynamics 365 **Expense** mobile app (Project Operations Expense Management) for receipts.
- The Warehouse Management mobile app is out of scope for finance.

### D4. Embedded Power Apps (brief)

Canvas apps can be embedded through the **Power Apps** button on the Action Pane (opens in a side pane), as a tab/FastTab/workspace section, or as a full-page dashboard tile. Users with personalisation rights can add them (**Options** > **Personalize this page** > **More** > **Add a page**, or **Power Apps** > **Add an app**). A single field can be passed as context. Model-driven apps can't be embedded. Mention only if our organisation ships embedded apps.

---

## PART E: USER TROUBLESHOOTING AND SESSION BASICS

### E1. Sign-in, sign-out and session timeouts

- **Session inactivity timeout (Set the session inactivity timeout):** default **30 minutes**, settable 5 to 60 (admin: **System administration > Setup > System parameters** > **General** > **Session management**). Countdown warnings before closing: **5 minutes** before if the timeout is over 30 minutes; **2 minutes** if 10 to 30 minutes; **30 seconds** if under 10 minutes. *"... to help prevent users from losing any unsaved changes ... Give users an opportunity to reconnect."*
- **Maximum user session:** 10.0.16 introduced an admin-set maximum session length (1 to 2,160 hours), after which the user must sign in again. The "User session management" article now redirects to the Finance hub (retired).
- **Gap:** Microsoft has no end-user article on signing in (URL, Microsoft Entra ID, MFA), signing out (user profile menu) or what happens with several browser tabs/sessions. Write these from our environment. (Cross-ref: "Open in new window" / side-by-side pages, UI shell researcher.)

### E2. Supported browsers and browser settings

- **Supported (System requirements):** latest **Microsoft Edge** (recommended, Chromium-based), **Google Chrome**, **Apple Safari**. Internet Explorer 11 is blocked from 10.0.25. Old Edge/Chrome (83 and earlier) prompt users to update (10.0.21+).
- **Special considerations:** Task Recorder screenshots in Word need a prerelease Chrome extension; the **Workflow Editor** and the Financial reporting **Report Designer** are ClickOnce apps (Edge supports them out of the box; Chrome needs an extension); PDF preview in Edge or Chrome.
- **Network:** designed for latency of 250 to 300 ms or less; most scenarios need > 50 KBps.
- **Pop-ups:** no Learn article tells users to allow pop-ups for F&O. Help articles open in a new browser tab, and some reports open in new tabs. Check whether our build needs pop-ups allowed (export, print preview).
- **Client FAQ (ms.date 12/31/2024, old):**
  - *Symbols not loaded:* browser security may block font download; add the site to trusted sites.
  - *Different right-click menus:* in an editable field or selected text you get the browser menu (**Cut**/**Copy**/**Paste**); on a field label or read-only value you get the app's shortcut menu.
  - *View details:* values with details show as hyperlinks; **View details** is also on the shortcut menu.

### E3. Messages: message bars, Action center, message boxes

From Messaging system (dev-itpro, 03/12/2026) and User interface elements:

| Where | When | Severity | User behaviour |
|---|---|---|---|
| **Message bar** (beneath the Action Pane, on pages, drop dialogs and slider dialogs) | Result of a synchronous action on the current page; data validation; page/data state (for example, date effectivity) | **info**, **warning**, **error** | Tied to the page: leaves when you navigate away, returns when you come back. Validation messages clear when the value is fixed (field level) or at the next save (table level). Expand an error bar to see the detail list. |
| **Action center** (navigation bar) | Asynchronous/background results (batch jobs, report completion) | info, warning, error | Shows a count of messages since last opened; holds **up to 500 messages**, first in first out. |
| **Message box** (modal) | Errors that need immediate attention; you can't continue until you dismiss it | error | Bold main instruction plus details; it should state the error, cause and fix. |
| **Feature callout** | Next to a field/tab/button: introduces a new feature | - | Can be reset (E5). |

- **Severity meanings:** *Notification (info)*: informs, typically no action. *Warning*: data in an incorrect state that might cause an issue later. *Error*: an action has failed, either non-interrupting (fix later) or interrupting (must fix before continuing, for example saving invalid data).
- Grouped results (**SetPrefix**) show the most severe message's type.
- **Shortcuts:** **Ctrl+F7** go to the Message Bar; **Ctrl+Shift+F7** go to the Message Center (Action center).
- **High-volume notifications:** from 10.0.39, notification processes over a threshold (default 100 per hour) can be auto-blocked; users are notified if a process tied to them is blocked.
- **Screenshots:** `message-bar-types-info-warning-error.jpg`, `message-box-error-dialog.jpg`, `message-bar-info-message-details.jpg`, `message-bar-warning-message-details.jpg`, `message-bar-error-message-details.jpg`.
- **Gap:** no Learn article on the client "Something went wrong" error page or on client reconnect messages. Capture examples in our environment if we want them.

### E4. Refreshing

- **Shift+F5** Data refresh (Keyboard shortcuts); the page refresh button on the Action Pane (UI shell).
- Browser refresh is Microsoft's documented fix for Copilot not appearing, and good practice before Task Recorder playback (a new session).

### E5. Usage data, personalisation reset, feature callouts

- **Settings > User options** > **Usage data** (Action Pane): view and delete your usage data. **Personalization** tab: view and manage your page personalisations; reset feature callouts (they show again).
- Feature callouts aren't reset by clearing personalisations; use the actions on the **Usage data** > **Personalization** tab. Admins use the **Manage per user** tab on the **Personalization** page.
- **Clear** tool (in personalisation) resets the page or current view; it can't be undone.
- Personalisations don't need resetting after updates, except where a page changed.
- (Saved views, personalisation detail: grids researcher.)

### E6. Session date

**Common > Common > Session date and time** > **Date** > **OK**; or the session date picker on the default dashboard. Affects the default date for journals and source documents (back-dating). Shortcut **D** enters the session date in a date field.

### E7. What to capture for a support ticket (synthesis)

Microsoft doesn't publish an end-user checklist, and doesn't document an **Activity ID** or **Session ID** for users. Documented, reliable items:
- Environment URL and company (from the browser address bar and company picker).
- Page name and the action taken.
- The exact message text (message bar details expanded; message box; Action center message).
- Date and time, and the session date if relevant.
- Version info from **Settings** > **About** (loaded packages and models).
- A screenshot (also attachable to a Copilot chat when that feature is on).
- For workflow problems: document ID, **Instance ID** and **Status** from **Workflow history**.
- Route: the company's BAU Support team (D-083), not Microsoft directly.

### E8. Data validation checklist (brief)

The **Data validation checklist** workspace tracks validation tasks across companies, areas and people (implementation, upgrade or migration). Users see their assigned tasks, open the linked page from the task name, select **Edit task** to change status or assignee, and use **Attachments**. **Completed by** and **Completed date** fill in automatically. Configured on **Configure data validation project**. Only relevant if our go-live uses it for user acceptance.

---

## (1) Suggested Getting Started topics from this area (ranked)

**Must have**
1. **Approve, reject or delegate a workflow item**: the Workflow button actions (Approve, Reject, Request change, Delegate, Complete, Reassign/Release), comments, the message bar instructions. Every stream has approvals (journals, vendor invoices, customer changes).
2. **Find your work items**: Work items assigned to me on the dashboard and page; open the document and act. (Also Immersive Home if turned on.) This is the daily entry point for approvers.
3. **Submit, resubmit, recall or cancel your own document and track it**: Workflow > Submit with a comment; statuses; View history; Recall; what Unrecoverable means and who to call. Originators in all streams need this.
4. **Read system messages**: message bar vs Action center vs message box; info/warning/error; expanding error details; Ctrl+F7. New users struggle most with errors.
5. **Get help and report a problem**: the ? menu, Help pane, field hover descriptions, and our BAU Support route with the information to capture. This replaces Microsoft's LCS route for our users.
6. **Delegate while you're away**: User options > Workflow > Delegation rule. It prevents stuck approvals during leave.

**Should have**
7. **Using Copilot safely**: open the sidecar, what it answers (Microsoft docs, not our process), verify outputs, thumbs feedback, data privacy, and what to do if it's missing. Copilot is GA and visible on every page.
8. **AI summaries you'll see in your stream**: Customer page summary and Collections coordinator summary/reminder email (O2C), Vendor/PO summary (P2P), Workflow history summary (all). On by default, so users will see them.
9. **Session basics**: sign in/out, inactivity timeout and countdown, supported browsers (Edge), refresh, session date. Needs our own content because Microsoft has gaps.
10. **Workflow notifications**: what emails you get, why rejection sends two, and that workflow items don't appear in the Action center. This answers a common confusion.
11. **Reset your settings**: Usage data, personalisation reset, feature callouts. A self-fix before raising a ticket.

**Nice to have**
12. **Immersive Home and agents**: only if enabled (10.0.44+). It may become the landing page.
13. **Task guides and Task Recorder playback**: only if our training team publishes task guides; warn that the data is real.
14. **Agents in your stream (overview)**: Account Reconciliation Agent (R2R), Finance Agent Collections in Outlook (O2C), Procurement/Expense Agents (P2P). One "what's coming" box; preview, licence-dependent.
15. **Microsoft Learn self-study**: site search, Ask Learn, RSS. Low priority for end users.
16. **Mobile and Teams**: one line saying the F&O mobile app is retired and that approvals in Teams/Outlook exist only if IT built them.
17. **Data validation checklist**: only for go-live UAT.

**Open questions to resolve in the clean-session test or with IT:** the exact ? menu items in our build; the message bar icon label; the Work items menu pages; the status values per document type; the help-pane shortcut (Ctrl+Shift+? vs Ctrl+?); whether Copilot, attachments, Immersive Home and agents are enabled; whether Delegate multiple work items is on; whether IT built Power Automate approvals; whether an Activity/Session ID is shown anywhere; whether pop-ups must be allowed; whether there's a Share/Copy link control.

---

## (2) Every URL consulted

**Workflow**
- https://learn.microsoft.com/en-us/dynamics365/fin-ops-core/fin-ops/organization-administration/overview-workflow-system
- https://learn.microsoft.com/en-us/dynamics365/fin-ops-core/fin-ops/organization-administration/workflow-elements
- https://learn.microsoft.com/en-us/dynamics365/fin-ops-core/fin-ops/organization-administration/workflow-actions
- https://learn.microsoft.com/en-us/dynamics365/fin-ops-core/fin-ops/organization-administration/configure-workflow-properties
- https://learn.microsoft.com/en-us/dynamics365/fin-ops-core/fin-ops/organization-administration/configure-approval-step-workflow
- https://learn.microsoft.com/en-us/dynamics365/fin-ops-core/fin-ops/organization-administration/configure-manual-task-workflow
- https://learn.microsoft.com/en-us/dynamics365/fin-ops-core/fin-ops/organization-administration/configure-manual-decision-workflow
- https://learn.microsoft.com/en-us/dynamics365/fin-ops-core/fin-ops/organization-administration/configure-line-item-workflow
- https://learn.microsoft.com/en-us/dynamics365/fin-ops-core/fin-ops/organization-administration/workflow-faq
- https://learn.microsoft.com/en-us/dynamics365/fin-ops-core/fin-ops/organization-administration/workflow-history-summary
- https://learn.microsoft.com/en-us/dynamics365/fin-ops-core/fin-ops/organization-administration/tasks/delegate-work-items-workflow
- https://learn.microsoft.com/en-us/dynamics365/fin-ops-core/fin-ops/organization-administration/tasks/view-workflow-history
- https://learn.microsoft.com/en-us/dynamics365/fin-ops-core/fin-ops/organization-administration/tasks/users-receive-workflow-related-email-messages
- https://learn.microsoft.com/en-us/dynamics365/fin-ops-core/fin-ops/organization-administration/tasks/change-date-session
- https://learn.microsoft.com/en-us/dynamics365/fin-ops-core/fin-ops/organization-administration/tasks/set-up-electronic-signatures
- https://learn.microsoft.com/en-us/dynamics365/fin-ops-core/fin-ops/copilot/workflow-history-summary-faq
- https://learn.microsoft.com/en-us/dynamics365/fin-ops-core/dev-itpro/business-events/how-to/how-to-workflow
- https://learn.microsoft.com/en-us/dynamics365/finance/accounts-payable/vendor-bank-account-workflow
- https://learn.microsoft.com/en-us/dynamics365/finance/accounts-payable/vendor-workflow
- https://learn.microsoft.com/en-us/dynamics365/finance/accounts-payable/vendor-invoices-overview
- https://learn.microsoft.com/en-us/dynamics365/finance/accounts-payable/vendor-invoices-workspace
- https://learn.microsoft.com/en-us/dynamics365/finance/accounts-payable/mobile-invoice-approvals
- https://learn.microsoft.com/en-us/dynamics365/finance/accounts-receivable/customer-workflow
- https://learn.microsoft.com/en-us/dynamics365/finance/accounts-receivable/create-free-text-invoice-new
- https://learn.microsoft.com/en-us/dynamics365/finance/accounts-receivable/cm-credit-limit-adjustments
- https://learn.microsoft.com/en-us/dynamics365/finance/general-ledger/general-journal-processing
- https://learn.microsoft.com/en-us/dynamics365/finance/asset-leasing/use-create-lease-wrkflw
- https://learn.microsoft.com/en-us/dynamics365/finance/budgeting/budget-plan
- https://learn.microsoft.com/en-us/dynamics365/supply-chain/procurement/purchase-order-approval-confirmation
- https://learn.microsoft.com/en-us/dynamics365/supply-chain/procurement/purchase-order-overview
- https://learn.microsoft.com/en-us/dynamics365/fin-ops-core/fin-ops/get-started/default-dashboard

**Help, Task guides, Task Recorder, support**
- https://learn.microsoft.com/en-us/dynamics365/fin-ops-core/fin-ops/get-started/help-overview
- https://learn.microsoft.com/en-us/dynamics365/fin-ops-core/dev-itpro/get-started/help-connect
- https://learn.microsoft.com/en-us/dynamics365/fin-ops-core/dev-itpro/help/custom-help-overview
- https://learn.microsoft.com/en-us/dynamics365/fin-ops-core/dev-itpro/help/connect-help-pane
- https://learn.microsoft.com/en-us/dynamics365/fin-ops-core/dev-itpro/get-started/view-export-field-descriptions
- https://learn.microsoft.com/en-us/dynamics365/fin-ops-core/dev-itpro/user-interface/customize-field-help
- https://learn.microsoft.com/en-us/dynamics365/fin-ops-core/dev-itpro/user-interface/task-recorder
- https://learn.microsoft.com/en-us/dynamics365/fin-ops-core/dev-itpro/user-interface/task-recorder-quick-reference
- https://learn.microsoft.com/en-us/dynamics365/fin-ops-core/fin-ops/user-interface/task-recorder-training-docs
- https://learn.microsoft.com/en-us/dynamics365/fin-ops-core/fin-ops/get-started/videos
- https://learn.microsoft.com/en-us/dynamics365/fin-ops-core/fin-ops/lcs/lcs-support
- https://learn.microsoft.com/en-us/dynamics365/fin-ops-core/dev-itpro/lifecycle-services/support-experience
- https://learn.microsoft.com/en-us/dynamics365/fin-ops-core/dev-itpro/lifecycle-services/support-migration-to-ppac
- https://learn.microsoft.com/en-us/dynamics365/fin-ops-core/dev-itpro/sysadmin/legal-terms-privacy-statement
- https://learn.microsoft.com/en-us/dynamics365/fin-ops-core/dev-itpro/privacy/privacy-guide
- https://learn.microsoft.com/en-us/dynamics365/fin-ops-core/dev-itpro/dev-tools/version-models-build
- https://learn.microsoft.com/en-us/dynamics365/fin-ops-core/dev-itpro/dev-tools/isv-licensing
- https://learn.microsoft.com/en-us/dynamics365/fin-ops-core/fin-ops/get-started/user-interface-elements
- https://learn.microsoft.com/en-us/dynamics365/fin-ops-core/fin-ops/get-started/shortcut-keys

**Copilot and AI (finance and operations)**
- https://learn.microsoft.com/en-us/dynamics365/fin-ops-core/fin-ops/copilot/copilot-for-finance-operations
- https://learn.microsoft.com/en-us/dynamics365/fin-ops-core/fin-ops/copilot/copilot-generative-help
- https://learn.microsoft.com/en-us/dynamics365/fin-ops-core/fin-ops/copilot/faq-copilot-generative-help
- https://learn.microsoft.com/en-us/dynamics365/fin-ops-core/fin-ops/copilot/immersive-home
- https://learn.microsoft.com/en-us/dynamics365/fin-ops-core/fin-ops/copilot/faq-immersive-home
- https://learn.microsoft.com/en-us/dynamics365/fin-ops-core/fin-ops/copilot/agent-mgmt
- https://learn.microsoft.com/en-us/dynamics365/fin-ops-core/fin-ops/copilot/faq-agent-mgmt
- https://learn.microsoft.com/en-us/dynamics365/fin-ops-core/fin-ops/copilot/use-copilot-cowork-erp
- https://learn.microsoft.com/en-us/dynamics365/fin-ops-core/dev-itpro/copilot/enable-copilot
- https://learn.microsoft.com/en-us/dynamics365/fin-ops-core/dev-itpro/copilot/enable-copilot-generative-help
- https://learn.microsoft.com/en-us/dynamics365/fin-ops-core/dev-itpro/copilot/extend-copilot-generative-help
- https://learn.microsoft.com/en-us/dynamics365/fin-ops-core/dev-itpro/copilot/enable-copilot-feedback
- https://learn.microsoft.com/en-us/dynamics365/fin-ops-core/dev-itpro/copilot/copilot-attachments
- https://learn.microsoft.com/en-us/dynamics365/fin-ops-core/dev-itpro/copilot/copilot-zero-prompt
- https://learn.microsoft.com/en-us/dynamics365/fin-ops-core/dev-itpro/copilot/extend-copilot
- https://learn.microsoft.com/en-us/dynamics365/fin-ops-core/dev-itpro/copilot/copilot-application-context
- https://learn.microsoft.com/en-us/dynamics365/fin-ops-core/dev-itpro/copilot/copilot-client-plugins
- https://learn.microsoft.com/en-us/dynamics365/fin-ops-core/dev-itpro/copilot/chat-with-fno-data
- https://learn.microsoft.com/en-us/dynamics365/fin-ops-core/dev-itpro/copilot/erp-in-work-iq
- https://learn.microsoft.com/en-us/dynamics365/fin-ops-core/dev-itpro/copilot/enable-copilot-cowork-erp
- https://learn.microsoft.com/en-us/dynamics365/fin-ops-core/dev-itpro/copilot/copilot-mcp
- https://learn.microsoft.com/en-us/dynamics365/fin-ops-core/dev-itpro/copilot/agent-deployment
- https://learn.microsoft.com/en-us/dynamics365/fin-ops-core/dev-itpro/copilot/agent-feed-api
- https://learn.microsoft.com/en-us/dynamics365/fin-ops-core/dev-itpro/responsible-ai/responsible-ai-overview
- https://learn.microsoft.com/en-us/dynamics365/finance/accounts-receivable/enable-copilot-in-finance
- https://learn.microsoft.com/en-us/dynamics365/finance/accounts-receivable/customerpagesummary
- https://learn.microsoft.com/en-us/dynamics365/finance/accounts-receivable/customerpagesummaryfaq
- https://learn.microsoft.com/en-us/dynamics365/finance/accounts-receivable/collectionscoordinatorsummary
- https://learn.microsoft.com/en-us/dynamics365/finance/accounts-receivable/collections-coordinator-summary-faq
- https://learn.microsoft.com/en-us/dynamics365/finance/accounts-receivable/collectionsworkspace
- https://learn.microsoft.com/en-us/dynamics365/finance/accounts-receivable/set-up-collections
- https://learn.microsoft.com/en-us/dynamics365/finance/general-ledger/acct-rec-agent
- https://learn.microsoft.com/en-us/dynamics365/finance/general-ledger/configure-acct-recon-agent
- https://learn.microsoft.com/en-us/dynamics365/finance/transparency-note
- https://learn.microsoft.com/en-us/dynamics365/supply-chain/get-started/copilot-summaries-overview
- https://learn.microsoft.com/en-us/dynamics365/supply-chain/procurement/procurement-agent-overview
- https://learn.microsoft.com/en-us/dynamics365/project-operations/expense/expense-agent-overview
- https://learn.microsoft.com/en-us/dynamics365/copilot/ai-get-started
- https://learn.microsoft.com/en-us/copilot/finance/welcome
- https://learn.microsoft.com/en-us/copilot/finance/collections/collections-overview
- https://learn.microsoft.com/en-us/copilot/finance/collections/dynamics-finance-permissions
- https://learn.microsoft.com/en-us/copilot/finance/collections/sign-in-to-erp
- https://learn.microsoft.com/en-us/copilot/finance/reconcile/reconcile-overview
- https://learn.microsoft.com/en-us/copilot/finance/agent-in-copilot-chat/agent-chat-overview
- https://learn.microsoft.com/en-us/copilot/finance/get-started/deployment-guide
- https://learn.microsoft.com/en-us/copilot/finance/get-started/sign-up-faq
- https://learn.microsoft.com/en-us/copilot/finance/toc.json (Finance Agent table of contents)

**Release plans and What's new**
- https://learn.microsoft.com/en-us/dynamics365/release-plan/ (redirects to the archived 2025 wave 2 overview)
- https://learn.microsoft.com/en-us/previous-versions/dynamics365/release-plan/2025wave2/
- https://learn.microsoft.com/en-us/previous-versions/dynamics365/release-plan/2025wave2/enterprise-resource-planning/dynamics365-finance/planned-features
- https://learn.microsoft.com/en-us/previous-versions/dynamics365/release-plan/2025wave2/enterprise-resource-planning/finance-operations-crossapp-capabilities/planned-features
- https://learn.microsoft.com/en-us/previous-versions/dynamics365/release-plan/2025wave2/enterprise-resource-planning/finance-operations-crossapp-capabilities/stay-focused-simplify-tasks-immersive-home-adaptive-experiences
- https://learn.microsoft.com/en-us/previous-versions/dynamics365/release-plan/2026wave1/
- https://learn.microsoft.com/en-us/previous-versions/dynamics365/release-plan/2026wave1/enterprise-resource-planning/dynamics365-finance/planned-features
- https://learn.microsoft.com/en-us/previous-versions/dynamics365/release-plan/2026wave1/enterprise-resource-planning/dynamics365-finance/enhancements-account-reconciliation-agent
- https://learn.microsoft.com/en-us/previous-versions/dynamics365/release-plan/2026wave1/enterprise-resource-planning/finance-operations-crossapp-capabilities/planned-features
- https://learn.microsoft.com/en-us/previous-versions/dynamics365/release-plan/2026wave1/enterprise-resource-planning/finance-operations-crossapp-capabilities/use-copilot-cowork-orchestrate-insights-actions-across-dynamics-365-erp
- https://learn.microsoft.com/en-us/previous-versions/dynamics365/release-plan/2026wave1/enterprise-resource-planning/finance-operations-crossapp-capabilities/open-records-dynamics-365-erp-applications-deep-links-copilot-responses
- https://learn.microsoft.com/en-us/dynamics365/release-plan/2026wave2/ (404)
- https://learn.microsoft.com/en-us/dynamics365/fin-ops-core/fin-ops/get-started/whats-new-platform-updates-10-0-45 (and 10-0-44, 10-0-46 to 10-0-50)

**Collaboration, mobile, apps**
- https://learn.microsoft.com/en-us/dynamics365/fin-ops-core/fin-ops/mobile-apps/mobile-app-home-page
- https://learn.microsoft.com/en-us/dynamics365/fin-ops-core/fin-ops/mobile-apps/invoice-approval-mobile-workspace
- https://learn.microsoft.com/en-us/dynamics365/fin-ops-core/fin-ops/get-started/removed-deprecated-features-platform-updates
- https://learn.microsoft.com/en-us/dynamics365/fin-ops-core/dev-itpro/power-platform/build-mobile-experiences
- https://learn.microsoft.com/en-us/dynamics365/fin-ops-core/dev-itpro/get-started/embed-power-apps
- https://learn.microsoft.com/en-us/dynamics365/fin-ops-core/dev-itpro/user-interface/create-deep-links
- https://learn.microsoft.com/en-us/dynamics365/fin-ops-core/dev-itpro/user-interface/adaptive-cards

**Troubleshooting and session basics**
- https://learn.microsoft.com/en-us/dynamics365/fin-ops-core/fin-ops/get-started/client-faq
- https://learn.microsoft.com/en-us/dynamics365/fin-ops-core/dev-itpro/get-started/system-requirements
- https://learn.microsoft.com/en-us/dynamics365/fin-ops-core/dev-itpro/sysadmin/session-idle-timeout
- https://learn.microsoft.com/en-us/dynamics365/fin-ops-core/dev-itpro/sysadmin/user-session-management (301 to the Finance hub: retired)
- https://learn.microsoft.com/en-us/dynamics365/fin-ops-core/dev-itpro/get-started/whats-new-platform-updates-10-0-16
- https://learn.microsoft.com/en-us/dynamics365/fin-ops-core/fin-ops/get-started/whats-new-platform-update-29
- https://learn.microsoft.com/en-us/dynamics365/fin-ops-core/dev-itpro/user-interface/messaging-user
- https://learn.microsoft.com/en-us/dynamics365/fin-ops-core/dev-itpro/user-interface/feature-callouts
- https://learn.microsoft.com/en-us/dynamics365/fin-ops-core/dev-itpro/get-started/personalize-user-experience
- https://learn.microsoft.com/en-us/dynamics365/fin-ops-core/fin-ops/user-interface/data-validation-workspace
- https://learn.microsoft.com/en-us/troubleshoot/dynamics-365/finance/toc.json (Finance troubleshooting TOC: nothing client/user-level)
- https://learn.microsoft.com/api/search (Learn search API, used for discovery queries on Teams, Outlook, sign-in, browser cache, multiple tabs, agents)
- https://github.com/MicrosoftDocs/dynamics-365-unified-operations-public (source Markdown, main branch)
