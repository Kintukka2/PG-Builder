# D365 F&O: Collections Procedure Guide

> **WORKING DRAFT. Not validated or approved.**
>
> This is a Markdown preview of the Word guide [`CLAUDE-230-Collections PG v3.1.docx`](CLAUDE-230-Collections%20PG%20v3.1.docx). It was assembled from the topic drafts named in its version history, under D-045 and D-046. **The Word file is the editable source.**
>
> Markers such as `[G230-05]` or `[Aged Balances VG-03]` show the open items that have a review comment in the Word file: one per open blocking item, at the place it matters most (D-067). The register lists every item, the non-blocking ones included, and where each applies. Guide-level items and the index of carried items are in the [validation register](../03-validation/230-Collections-v3.0-Validation.md). Notes marked **ACTION: REVIEW REQUIREMENT**, and <mark>highlighted</mark> phrases, are internal notes to the author (yellow in the Word file); they are removed before publication (D-060). The markers are not part of the guide text.

The fixed template content is not repeated here: cover, Contents, *About this guide* and *Additional Resources*.

**Version history**

| ID | Date | Author/s | BPO | Description of change |
|---|---|---|---|---|
| 2.0 | October 2025 | Daniel Moreira | Christoper Clarke | Version Upgrade |
| 2.1 | April 2026 | Suzanne Starr | Christoper Clarke | Content Update (DD + Bank) |
| 2.2 | May 2026 | Suzanne Starr | Christoper Clarke | Content Update (CW1) |
| 2.3 | October 2026 | Daniel Moreira | Christoper Clarke | Content Review |
| 2.4 | November 2026 | Daniel Moreira | Christopher Clarke | Draft: 6.5 to 6.8 moved to 220 |
| 3.0 | November 2026 | Maria Pabalan; Daniel Moreira | Christopher Clarke | Template rebuild (draft) |
| 3.1 | November 2026 | Maria Pabalan; Daniel Moreira | Christopher Clarke | SME round 1 answers (draft) |

---

## Part 1: What do I need to know? (Collections)

### High-level process

##### Part Description

The Collections process manages overdue customer balances in D365. It covers starting the collections day in the **Customer credit and collections** workspace, monitoring customers, customer ownership through Customer Pools and Collection Agent assignments, contacting customers, recording activities, managing statements, resolving accounts and closing activities. The process supports timely follow-up and business cash flow, helps minimize bad debt exposure, and provides visibility of collection actions in D365.

At a high level, the Collections process follows these stages:

- **Start the Collections Day**: open the **Customer credit and collections** workspace and find the day's collection work.
- **Monitor Customers**: review customers overdue, aged balances, the customer account, and notes and activities; update customer details.
- **Manage Customer Pools and Collection Agents**: create Customer Pools, validate membership and assign pools to Collection Agents to establish customer ownership and allocate collections workloads.
- **Contact the Customer**: check the overdue balance, then engage with the customer by phone or email to discuss overdue invoices, confirm payment status or disputes, and agree on next steps.
- Record a Customer Collection Activity: record each interaction with the customer, and each internal email about the account, as a collection activity in D365. Supporting documents stay in CW1.
- Manage Customer Statements: preview and download statements, and send an ad hoc statement when a customer asks for one. Monthly statements are sent automatically on the 5th of each month.
- **Resolve the Account**: resend invoices, issue collection letters, update customer status or process approved debt write-offs. Payment corrections are made by Receipting Officers ([220 Customer Payments](https://wisetechglobal.sharepoint.com/sites/Atlas/Training/D365%20Procedure%20Guides/220-Customer%20Payments%20PG.pdf)).
- **Update and Close a Customer Activity**: update the activity record in D365 with the outcome and close it once the issue is resolved and no further follow-up is required.

General D365 tasks (switching legal entity, Favorites, personalized views and exporting grid data) are in [260 O2C Getting Started](https://wisetechglobal.sharepoint.com/sites/Atlas/Training/D365%20Procedure%20Guides/260-O2C%20Getting%20Started%20PG.pdf).

##### Initiation

- Customer balances remain unpaid beyond agreed payment terms.
- System reports or automated reminders identify accounts for follow-up, or the Group Billing & Credit Manager requests it.
- New customer groups, legal entities or team members need collections ownership, or existing pool criteria or assignments change.

##### Stream

| Stream | Process Area | Key Roles |
|---|---|---|
| Order to Cash (O2C) | Collections | • Collections Officer<br>• Group Billing and Credit Manager |

##### Process

The high-level Collections process is as follows:

| # | Action | Who | When | Where |
|---|---|---|---|---|
| 1 | [Start the Collections Day](#1-start-the-collections-day) | Collections Officer | At the start of each working day | D365 |
| 2 | [Monitor Customers](#2-monitor-customers) | Collections Officer | Following statement issues or weekly during debt review cycles | D365 |
| 3 | [Manage Customer Pools and Collection Agents](#3-manage-customer-pools-and-collection-agents) | Group Billing and Credit Manager | When new pools or agents are required, or pool criteria or ownership assignments change | D365 |
| 4 | [Contact the Customer](#4-contact-the-customer) | Collections Officer | Upon identification of overdue or disputed balances | D365; Outlook / Other |
| 5 | [Record a Customer Collection Activity](#5-record-a-customer-collection-activity) | Collections Officer | Immediately after customer contact or correspondence | D365 |
| 6 | [Manage Customer Statements](#6-manage-customer-statements) | Collections Officer | When a customer asks for a statement, or one must be reviewed or copied | D365 |
| 7 | [Resolve the Account](#7-resolve-the-account) | Collections Officer; Group Billing and Credit Manager | As required following escalation, dispute, or collection outcome | D365 / Outlook |
| 8 | [Update and Close a Customer Activity](#8-update-and-close-a-customer-activity) | Collections Officer | Once the issue is resolved, payment received, or case closed | D365 |

> **Note:** The high-level process includes new D365 F&O, new non-D365 F&O, and existing (BAU) activities. This procedure guide does not include BAU procedures.

### Roles and responsibilities

##### Overview

<mark>The roles come from legacy 230 and the topic drafts.</mark> For 7.4, the Collections Officer requests the write-off by email to the Group Billing and Credit Manager, who creates the write-off journal once the request is approved.

| **Tasks / Business Roles** | Collections Officer | Group Billing and Credit Manager |
|---|---|---|
| [1. Start the Collections Day](#1-start-the-collections-day) | R |  |
| [1.1 Open the Customer Credit and Collections Workspace](#11-open-the-customer-credit-and-collections-workspace) | R |  |
| [1.2 Locate Collection Work in the Workspace](#12-locate-collection-work-in-the-workspace) | R |  |
| [2. Monitor Customers](#2-monitor-customers) | R |  |
| [2.1 Review Customers Overdue](#21-review-customers-overdue) | R |  |
| [2.2 Review Customer Aged Balances](#22-review-customer-aged-balances) | R |  |
| [2.3 Filter Aged Balances by Customer or Currency](#23-filter-aged-balances-by-customer-or-currency) | R |  |
| [2.4 Investigate a Customer Account](#24-investigate-a-customer-account) | R |  |
| [2.5 Review Customer Notes](#25-review-customer-notes) | R |  |
| [2.6 Review All Customer Activities](#26-review-all-customer-activities) | R |  |
| [2.7 Update Customer Details](#27-update-customer-details) | R |  |
| [2.8 Maintain Customer Direct Debit & eBanking Details](#28-maintain-customer-direct-debit--ebanking-details) | R |  |
| [3. Manage Customer Pools and Collection Agents](#3-manage-customer-pools-and-collection-agents) | R | R |
| [3.1 Create Customer Pools for Collections](#31-create-customer-pools-for-collections) |  | R |
| [3.2 Add a New Collections Agent](#32-add-a-new-collections-agent) |  | R |
| [4. Contact the Customer](#4-contact-the-customer) | R |  |
| [4.1 Check an Overdue Balance Before Contact](#41-check-an-overdue-balance-before-contact) | R |  |
| [5. Record a Customer Collection Activity](#5-record-a-customer-collection-activity) | R |  |
| [6. Manage Customer Statements](#6-manage-customer-statements) | R |  |
| [6.1 Preview and Download a Customer Statement](#61-preview-and-download-a-customer-statement) | R |  |
| [6.2 Generate and Send a Customer Statement](#62-generate-and-send-a-customer-statement) | R |  |
| [7. Resolve the Account](#7-resolve-the-account) | R | R |
| [7.1 View and Download a Customer Invoice](#71-view-and-download-a-customer-invoice) | R |  |
| [7.2 Create and Send a Collection Letter](#72-create-and-send-a-collection-letter) | R |  |
| [7.3 Change Customer Status](#73-change-customer-status) | R |  |
| [7.4 Write Off an Uncollectible Debt](#74-write-off-an-uncollectible-debt) | R | R |
| [8. Update and Close a Customer Activity](#8-update-and-close-a-customer-activity) | R |  |

\*R = Responsible

### Key concepts

##### Overview

Before you start, you need to know how to set up D365 for collections work, the Customer credit and collections workspace, the collections rules and automation, and the terms used in each task.

##### Set up D365 for collections work

Add these pages to your Favorites, and add these columns to the views you use for collection work. The general steps are in [260 O2C Getting Started](https://wisetechglobal.sharepoint.com/sites/Atlas/Training/D365%20Procedure%20Guides/260-O2C%20Getting%20Started%20PG.pdf) (topic 3 Add Pages to Favorites and topic 4 Create a Personalized View).

| Page | Description |
|---|---|
| **All customers** | Located in the **Credit and collections** module. Used to open customer accounts and customer master details. |
| **Aged balances** | Located in the **Credit and collections** module. Used to review customer balances by aging period. `[Favorites VG-01]` |
| **Customer payment journal** | Located in the **Credit and collections** module. Identified in AR Collections training as a key page for AR Collections users. |
| **Open customer invoices** | Located in the **Accounts receivable** module. Used to review open customer invoices. |

**Recommended columns**: Customer account, Customer name, Transaction date, Due date, Description, Amount, Currency, Overdue balance and Email address. `[Personalized Views VG-01]`

##### The Customer credit and collections workspace

| Term | Description |
|---|---|
| **Workspace** | A D365 page that brings together the information and tasks for one area of work. The **Customer credit and collections** workspace is the starting point for collection work. |
| **Sections used in AR Collections** | **Customers overdue**, **Payment journals not posted**, **Notes** and **Open payment journals**. |
| **Other sections** | The workspace also shows sections such as Open cases, Customers over credit limit and Collections letters not printed. The procedures in this guide use only the four sections above. |

##### Workspaces and modules

**Workspace or module**: The **Customer credit and collections** workspace opens from **Workspaces**. The **Credit and collections** module opens from **Modules** and lists pages such as **All customers** and **Aged balances**.

##### Collections Workflow

A customer’s overdue balance is subject to follow-up and activity tracking in D365 F&O:

| If… | Then… |
|---|---|
| The customer has overdue invoices within acceptable tolerance. | The Collections Officer will contact the customer to arrange payment and record the interaction in D365 F&O. |
| The customer is unresponsive or disputes the balance. | The issue will be escalated to the Group Billing & Credit Manager for review or resolution. |
| The customer debt is deemed uncollectible. | The Collections Officer will initiate a Debt Write-off request for approval and processing. |
| A payment has been applied incorrectly to a customer account. | Ask the Receipting team to correct it: Receipting Officers transfer, settle or unsettle payments, in [220 Customer Payments](https://wisetechglobal.sharepoint.com/sites/Atlas/Training/D365%20Procedure%20Guides/220-Customer%20Payments%20PG.pdf). |

##### Collection Activities

Each collection action is recorded as a Customer Activity in D365 F&O:

| Activity Type | Purpose |
|---|---|
| **Action** | Immediate follow-up, e.g., phone calls or reminders. |
| **Appointment** | Scheduling a future contact or meeting. |
| **Event** | Recording a general update or collection milestone. |
| **Task** | Internal reminders, e.g., follow-up next week. |

##### Customer Activity Status

A customer account status identifies the state of a customer account:

| Status | Description |
|---|---|
| **Open** | The activity is active and pending further action. |
| **In Progress** | The activity is being actioned (e.g., awaiting customer response). |
| **Resolved** | The issue has been addressed, or payment has been received. |
| **Closed** | The activity is complete, and no further follow-up is required. |

##### Invoice Due Reminder Automation

D365 F&O includes an automated Invoice Due Reminder email as part of the updated Credit Collections strategy. The reminder is sent five (5) days before an invoice is due, helping reduce overdue balances and manual follow-up. Specifications include:

- A new automated collection process (“Pre-due reminder – 5 days”) that triggers when the invoice due date minus 5 days is reached.
- Only invoices that are **Open**, have a **balance > 0**, and are **not disputed** or on **collection hold** are included.
- The rule automatically sends an email using a designated email template.

This reminder forms part of the revised collections timeline:

| Action | Timing |
|---|---|
| **Pre-Due Reminder** | 5 days before invoice due date |
| **1st Collection Letter** | 3 days after invoice due date |
| **2nd Collection Letter** | 11 days after the invoice due date |
| **3rd Collection Letter** | 18 days after the invoice due date |

##### Exclusion from Credit Management

Specific customer accounts or individual transactions can be excluded from automated credit and collections processing activities, including;

- Collections letters, and
- Direct debit (DD) processing runs.

Customer or transactions excluded from credit management may not be included in automated collections follow-up or Direct Debit processing activities.

##### Customer Payment Management

Customer payments may require manual adjustment to ensure balances are correctly reflected. Receipting Officers make these corrections, in [220 Customer Payments](https://wisetechglobal.sharepoint.com/sites/Atlas/Training/D365%20Procedure%20Guides/220-Customer%20Payments%20PG.pdf); ask the Receipting team when one is needed:

| **Action** | **Description** |
|---|---|
| 1. **Settle Customer Accounts** | Match customer payments against outstanding invoices. See [220 Customer Payments](https://wisetechglobal.sharepoint.com/sites/Atlas/Training/D365%20Procedure%20Guides/220-Customer%20Payments%20PG.pdf), topic 2.3. |
| 2. **Unsettle Customer Accounts** | Reverse an incorrect settlement. See [220 Customer Payments](https://wisetechglobal.sharepoint.com/sites/Atlas/Training/D365%20Procedure%20Guides/220-Customer%20Payments%20PG.pdf), topic 3.1. |
| 3. **Transfer Open / Closed Payments** | Move payments between customer accounts when allocated incorrectly. See [220 Customer Payments](https://wisetechglobal.sharepoint.com/sites/Atlas/Training/D365%20Procedure%20Guides/220-Customer%20Payments%20PG.pdf), topic 3.3. |
| 4. **Bank Fee Write-off** | Clear small residual balances caused by fees, FX differences, or minor variances. See [220 Customer Payments](https://wisetechglobal.sharepoint.com/sites/Atlas/Training/D365%20Procedure%20Guides/220-Customer%20Payments%20PG.pdf), topic 3.6. |

##### Customer Contact Integration (CW1 ↔ D365 F&O)

Customer contact information is managed across both CargoWise (CW1) and D365 F&O with bi-directional integration ensuring that contact details used for invoicing, statements and collections activities remain consistent across both systems.

Contacts are typically created and primarily maintained in CW1, then synchronized to D366. However, updates can also occur in D365 with certain changes flowing back to CW1 depending on the field and configuration. In D365:

- Each contact detail, e.g., email, and/or phone, is stored as a separate record.
- One email and one phone number can be marked as Primary.
- Emails with Purpose = Business are used for:
- Customer statements
- Invoices
- Collection letters

This integration is critical to the Collections process, as it ensures:

- Communications are sent to the correct recipient.
- Contact details remain accurate and up to date.
- Changes made during collections activities are reflected across systems.

##### High Level Integration Rules

| Scenario | Source System | Integration Outcome | Collections Impact |
|---|---|---|---|
| Created contact in CW1 | CW1 ↔ D365 | **D365**: Contact details created as separate records (Email, CC, BCC Phone). | Contact available for statements, invoices, and collections. |
| Contact updated in CW1 | CW1 ↔ D365 | **D365**: Changes reflected; new details added | Ensure the latest contact info used for follow-ups. |
| Contact details deleted in CW1 | CW1 ↔ D365 | **D365**: Corresponding details removed in D365 | Prevents outdated contact usage |
| Contact inactive / AR flag removed in CW1 |  | **D365**: Entire contact removed in D365 | Contact no longer used in collections communications. |
| Contact created in D365 (Business purpose) | D365 ↔ CW1 | **CW1**: New AR contact created in CW1 | Allows the collection team to add valid contacts. |
| Contact updated in D365 | D365 ↔ CW1 | **CW1**: Email / phone updates sync (name changes do not) | Maintains consistency across systems. |
| Email Purpose ≠ Business in D365 | D365 ↔ CW1 ↔ D365 | **D365**: AR flag removed → contact deleted | Contact excluded from all communications. |
| Primary flag changed in D365 | D365 ↔ CW1 | **CW1**: Official flag removed in CW1 | Impacts main contact designation. |
| Email deleted in D365 | D365 ↔ CW1 ↔ D365 | **D365**: AR flag removed → contact fully removed. | Contact removed from collections usage. |

##### Customers overdue

| Term | Description |
|---|---|
| **Customers overdue** | A page in the **Customer credit and collections** workspace that lists customers with overdue balances. |
| **Aging period** | The page shows overdue balances for the aging period you select, for example **90+** or **61-90** days. |
| **Balance due and overdue amount** | The balance due is the customer's total outstanding balance. The overdue amount is the part that is past its due date. The two can differ. |

##### Before contacting a customer

**Check the balance first**: Investigate an overdue balance before you contact the customer. A low-value balance may represent fees or an overpayment rather than an unpaid invoice. `[Overdue Customers VG-09]`

##### The Aged balances page

| Term | Description |
|---|---|
| **Aged balances** | A page in the **Credit and collections** module that shows customer balances by aging period. `[Aged Balances VG-01]` |
| **Reporting currency** | The page can show amounts in the ledger's reporting currency, which can differ from the currency of the customer's transactions. Add the **Currency** column so each account's currency is visible. |
| **Zero balances** | Accounts with a zero balance are listed unless you filter them out. Filtering the balance column to **not equal to** **0** removes them. |

##### Sharing balances with customers

**Use PDF, not Excel**: Provide customer-facing account information as a PDF. Do not send a customer an Excel export of this page.

##### Transactions and settlements

| Term | Description |
|---|---|
| **Open and closed transactions** | Open transactions still have an amount outstanding. Closed transactions have been fully settled. You can show either set on the customer's transactions. |
| **Currency revaluations** | Entries D365 creates when it revalues foreign currency balances. Hide them so the list shows only the customer's own transactions. |
| **Settlement** | The matching of a payment or credit to the invoices it pays. A transaction's settlement history shows what it was settled against. |

##### Reviewing without changing

**Do not undo settlements here**: This topic only reviews settlement history. Undoing a settlement changes financial records and is in [220 Customer Payments](https://wisetechglobal.sharepoint.com/sites/Atlas/Training/D365%20Procedure%20Guides/220-Customer%20Payments%20PG.pdf), topic 3.1 Undo a Settlement.

##### Notes and activities

| Term | Description |
|---|---|
| **Notes** | A page in the **Customer credit and collections** workspace that lists notes recorded against customer accounts. You filter it to see one customer's collection history. |
| **System-generated entries** | The Notes page lists entries created by D365, such as statements and collection letters, alongside notes entered by users. |
| **Customer activities** | Records of collection contact with a customer, such as an email or phone activity. **View all activities** on the customer account lists them. |

##### Recording collection history (notes and activities)

**Record notes at customer level**: Collection notes are recorded against the customer account rather than against individual invoices, so the full history is in one place.

##### Collection activities

| Term | Description |
|---|---|
| **Collection activity** | A record on the customer's Collections page of one interaction with the customer, such as an email or a phone call: its Type, Purpose and a note. |
| **Type** | The interaction the activity records: Email or Phone call. The activity type (Action, Appointment, Event or Task) is a separate choice: see *Collection Activities*. |
| **Purpose and note** | The Purpose is a short title, for example "Overdue chaser – payment requested". The note is the record of what happened (see *Writing a collection note*). |

##### Recording collection history (collection activities)

**Record at customer level**: Record collection activities against the customer account rather than against individual invoices, so the full history is visible in the account overview.

##### Writing a collection note

Write one note for each interaction, as the record of what happened. Incoming contact (from the customer) and outgoing contact (your email or call) get separate notes. An internal email about the account, for example to Receipting or Support, also gets a note, on every account involved.

The note must include:

- who you spoke to or emailed (name or address), and the date
- the invoices discussed, with amount and currency
- any promised payment date or dispute
- what you sent or agreed
- any follow-up action
- your initials

Do not attach documents to the activity. Supporting documents are kept in CW1, so the note must say enough to stand on its own.

> **Important:** Never record card numbers, bank account or BSB numbers, or other payment credentials, and no personal opinions about the customer.

##### Statements and destinations

| Term | Description |
|---|---|
| **Customer statement** | A document that lists a customer's transactions. With **Only open** selected, it lists only open transactions. |
| **Print management destination** | The destination used to deliver a statement to the customer. Clear it when you only want to preview the statement. |
| **Screen destination** | Displays the statement on screen so you can review it and download it, without sending it. |

##### Previewing safely

| Rule | Description |
|---|---|
| **Check the destination first** | Before you generate a preview, check that **Print management destination** is cleared and **Screen** is selected. |
| **Use PDF, not Excel** | Provide customer-facing account information as a PDF. Do not send a customer an Excel export. |

##### Statement distribution

| Term | Description |
|---|---|
| **Print management destination** | The destination that delivers the statement to the customer. When it is selected, generating the statement sends it. |
| **Delivery banner** | The banner D365 shows at the top of the page after a statement is sent. It confirms that the statement was sent and who it went to. |
| **Monthly statements** | Sent automatically on the 5th of each month. Officers send an ad hoc statement only when a customer asks for one. |

##### Before sending

| Rule | Description |
|---|---|
| **Send to every customer who asks** | Send a statement to any customer who asks for one, including direct debit and card customers, customers in dispute and customers with balances in more than one currency (their statement is split by currency). |
| **Use the 6.2.1 options and today's date** | Send with Only open, Include company logo and Print management destination. Date an ad hoc statement today, even if the customer asks for a month-end date. |

##### Invoices and transactions

| Term | Description |
|---|---|
| **Original document** | The document D365 produced for a posted transaction, such as the customer invoice. You open it from the transaction it belongs to. |
| **Print preview** | Shows the original document on screen so you can review it and download it as a PDF. |
| **Highlighted row** | Click a transaction row to highlight it before you open its original document. Highlighting a row is not the same as marking it with its checkbox. |

##### Sending documents to customers

**Use PDF, not Excel**: Provide customer-facing account information as a PDF. Do not send a customer an Excel export.

---

## Part 2: How do I do it? (Collections)

### 1. Start the Collections Day

##### Description

Use this topic to start collection work: open the **Customer credit and collections** workspace and find the sections used in normal collection work, such as **Customers overdue**, **Payment journals not posted**, **Notes** and **Open payment journals**. The work done in each section is a topic of its own in this guide.

##### Responsibility

- Collections Officer: starts collection work in the workspace.

##### Initiation

- A Collections Officer starts their collection work for the day.

##### Topic Overview

This topic includes these steps:

| Step | Description |
|---|---|
| [1.1 Open the Customer Credit and Collections Workspace](#11-open-the-customer-credit-and-collections-workspace) | Open the workspace from the dashboard or the Navigation Pane. |
| [1.2 Locate Collection Work in the Workspace](#12-locate-collection-work-in-the-workspace) | Find the workspace section needed for the task. |

#### 1.1 Open the Customer Credit and Collections Workspace

##### Description

Use this procedure to open the **Customer credit and collections** workspace from **Workspaces** in the **Navigation Pane**.

##### Responsibility

- Collections Officer: opens the workspace to start collection work.

##### Initiation

- A Collections Officer starts their collection work for the day.

##### Procedure

Complete these steps to open the workspace:

| **Action** | **Description** |
|---|---|
| *PROCESS START* (light blue) | Pre-requisites:<br>• Access to D365 and to the **Customer credit and collections** workspace.<br>Responsibility:<br>• Collections Officer |
| 1. *Check* the **Entity**. | Confirm you are signed into the correct **Legal Entity** (top-right). |
| 2. *Click* **Workspaces**. `[Workspace VG-01]` | From the left-hand **Navigation Pane**, click **Workspaces**. |
| 3. *Select* **Customer credit and collections**. `[Workspace VG-02]` | Select the **Customer credit and collections** workspace from the list. |
| 4. *Confirm* the workspace is open. | Check that the **Customer credit and collections** workspace is displayed for the legal entity you selected in step 1. |
| *PROCESS COMPLETE* (light green) | Outcomes:<br>• The **Customer credit and collections** workspace is open. |

#### 1.2 Locate Collection Work in the Workspace

##### Description

Use this procedure to find the workspace sections used in normal collection work. Each section links to work covered by its own topic in this guide.

##### Responsibility

- Collections Officer: finds the workspace section needed for the task.

##### Initiation

- A Collections Officer needs to find where a collection task starts in the workspace.

##### Procedure

Complete these steps to locate collection work in the workspace:

| **Action** | **Description** |
|---|---|
| *PROCESS START* (light blue) | Pre-requisites:<br>• The **Customer credit and collections** workspace is open (see [1.1 Open the Customer Credit and Collections Workspace](#11-open-the-customer-credit-and-collections-workspace)).<br>Responsibility:<br>• Collections Officer |
| 1. *Locate* **Customers overdue**. `[Workspace VG-04]` | Find **Customers overdue**. Use it to review customers with overdue balances. |
| 2. *Locate* **Payment journals not posted**. `[Workspace VG-05]` | Find **Payment journals not posted**. Use it to identify customer payment journals that have not been posted. |
| 3. *Locate* **Notes**. `[Workspace VG-06]` | Find **Notes**. Use it to review customer collection notes (see topics 2.5 and 2.6). |
| 4. *Locate* **Open payment journals**. `[Workspace VG-07]` | Find **Open payment journals**. Use it to start investigating unallocated customer payments. |
| 5. *Open* the section you need. | Open the section for your task and continue with the topic for that task. |
| *PROCESS COMPLETE* (light green) | Outcomes:<br>• The workspace section for the task is open. |

### 2. Monitor Customers

##### Description

**Monitoring customers** in D365 F&O enables the **Collections Officer** to proactively track overdue balances, review historical activities, and determine appropriate follow-up actions.  
This process ensures that all customer accounts are regularly assessed for outstanding amounts and recent interactions, supporting timely debt recovery and accurate account management.

Together, these steps provide a complete view of the customer’s financial position and interaction history, enabling informed and consistent collection decisions.

##### Responsibility

- The **Collections Officer** is responsible for monitoring customer accounts daily in D365 F&O, ensuring that aged balances and activity records are reviewed and accurately maintained.  

They must identify overdue accounts requiring follow-up and ensure that all prior correspondence and actions are properly recorded before making new contact.
##### Initiation

This process is initiated as part of the **daily collection routine**, or when follow-up is required on specific overdue accounts.  
It may also be triggered by:

- A scheduled collections review cycle; or
- Customer or internal queries regarding account status or previous collection activity.

##### Topic Overview

This topic includes these steps:

| Step | Description |
|---|---|
| [2.1 Review Customers Overdue](#21-review-customers-overdue) | List customers with overdue balances and open an account to follow up. |
| [2.2 Review Customer Aged Balances](#22-review-customer-aged-balances) | Review customer balances by aging period. |
| [2.3 Filter Aged Balances by Customer or Currency](#23-filter-aged-balances-by-customer-or-currency) | Limit Aged balances to one customer or currency. |
| [2.4 Investigate a Customer Account](#24-investigate-a-customer-account) | Open the account and review its transactions and settlement history. |
| [2.5 Review Customer Notes](#25-review-customer-notes) | Read the notes recorded for a customer. |
| [2.6 Review All Customer Activities](#26-review-all-customer-activities) | Review previous collection activities for a customer. |
| [2.7 Update Customer Details](#27-update-customer-details) | Update customer contact details with [200 Customer Onboarding and Maintenance](https://wisetechglobal.sharepoint.com/sites/Atlas/Training/D365%20Procedure%20Guides/200-Customer%20Onboarding%20and%20Maintenance%20PG.pdf), section 3.4. |
| [2.8 Maintain Customer Direct Debit & eBanking Details](#28-maintain-customer-direct-debit--ebanking-details) | See [240 Direct Debit and Credit Card Payments](https://wisetechglobal.sharepoint.com/sites/Atlas/Training/D365%20Procedure%20Guides/240-Direct%20Debit%20PG.pdf), topic 1. |

#### 2.1 Review Customers Overdue

##### Description

Use this procedure to open **Customers overdue**, select an aging period and sort the list so the largest overdue amounts appear first.

##### Responsibility

- Collections Officer: identifies customers with overdue balances.

##### Initiation

- A Collections Officer needs to identify which customers to contact about overdue balances.

##### Procedure

Complete these steps to review customers overdue:

| **Action** | **Description** |
|---|---|
| *PROCESS START* (light blue) | Pre-requisites:<br>• Access to D365 and to the **Customer credit and collections** workspace.<br>Responsibility:<br>• Collections Officer |
| 1. *Check* the **Entity**. | Confirm you are signed into the correct **Legal Entity** (top-right). |
| 2. *Click* **Workspaces**. | From the **Navigation Pane**, click **Workspaces**, then select **Customer credit and collections**. |
| 3. *Click* **Customers overdue**. `[Overdue Customers VG-01]` | In the workspace, click **Customers overdue**. |
| 4. *Select* the aging period. `[Overdue Customers VG-02]` | Select the aging period you are working on, for example **90+**. |
| 5. *Sort* the overdue amount from largest to smallest. `[Overdue Customers VG-05]` | Sort the overdue amount column in descending order so the largest overdue amounts appear first. |
| 6. *Add* the email address column. `[Overdue Customers VG-06]` | Optional. Add the email column with **Insert columns** (see [260 O2C Getting Started](https://wisetechglobal.sharepoint.com/sites/Atlas/Training/D365%20Procedure%20Guides/260-O2C%20Getting%20Started%20PG.pdf), topic 4 Create a Personalized View). Otherwise, go to step 7. |
| 7. *Review* the balance due and overdue amount. `[Overdue Customers VG-04]` | Check the aging period, then compare each customer's balance due with the overdue amount, largest first. |
| *PROCESS COMPLETE* (light green) | Outcomes:<br>• **Customers overdue** shows the selected aging period, sorted from the largest overdue amount. |

#### 2.2 Review Customer Aged Balances

##### Description

Use this procedure to open the **Aged balances** page and prepare the list for collection work. You add the **Currency** column, remove accounts with a zero balance and sort the balances from largest to smallest, so the customers with the highest outstanding balances appear first. You can save the prepared layout as a view by following [260 O2C Getting Started](https://wisetechglobal.sharepoint.com/sites/Atlas/Training/D365%20Procedure%20Guides/260-O2C%20Getting%20Started%20PG.pdf), topic 4 Create a Personalized View.

##### Responsibility

- Collections Officer: reviews customer balances before collection work.

##### Initiation

- A Collections Officer needs to identify customers with outstanding balances before starting collection work.

##### Procedure

Complete these steps to prepare the aged balances list:

| **Action** | **Description** |
|---|---|
| *PROCESS START* (light blue) | Pre-requisites:<br>• Access to D365 and to the **Credit and collections** module.<br>Responsibility:<br>• Collections Officer |
| 1. *Check* the **Entity**. | Confirm you are signed into the correct **Legal Entity** (top-right). |
| 2. *Click* **Modules**. | From the left-hand **Navigation Pane**, click **Modules**. |
| 3. *Navigate* to the **Aged balances** page. `[Aged Balances VG-02]` | From the **Navigation Pane**, *select*:<br>**Credit and collections >**<br>**Aged balances** |
| 4. *Click* **Insert columns**. `[Aged Balances VG-04 / VG-12]` | Use **Insert columns** to add the **Currency** column if the grid does not already show it. |
| 5. *Select* the **Currency** column. | Select **Currency** in the list of columns. |
| 6. *Confirm* the **Currency** column is displayed. | Check that each account now shows its currency. |
| 7. *Open* the filter for the balance column. `[Aged Balances VG-03 / VG-05]` | Open the filter for the balance column you are reviewing. |
| 8. *Select* **not equal to**. | Select the **not equal to** operator. |
| 9. *Enter* **0**. | Enter **0** as the filter value. |
| 10. *Apply* the filter. | Apply the filter. Accounts with a zero balance are no longer listed. |
| 11. *Sort* the balance column from largest to smallest. `[Aged Balances VG-06]` | Sort the balance column in descending order so the largest balances appear first. |
| 12. *Confirm* the list is ready to review. | Check that the list shows only non-zero balances, largest first, with each account's currency. |
| *PROCESS COMPLETE* (light green) | Outcomes:<br>• The **Aged balances** list shows only customers with a non-zero balance, sorted from largest to smallest.<br>• Each account shows its currency. |

> **Note:** Click a customer's name to open their Collections page. Aged balances are refreshed by a batch job every 10 minutes, so a transaction posted in the last 10 minutes may not show yet.

#### 2.3 Filter Aged Balances by Customer or Currency

##### Description

Use this procedure when you need the aged balances for selected customers or for one or more currencies. You filter the customer column to the accounts you need, or filter the **Currency** column, or both. Start from the list prepared in Review Customer Aged Balances.

##### Responsibility

- Collections Officer: narrows the aged balances list to the customers or currencies under review.

##### Initiation

- Only selected customers or currencies need review.

##### Procedure

Complete these steps to filter the aged balances list:

| **Action** | **Description** |
|---|---|
| *PROCESS START* (light blue) | Pre-requisites:<br>• The prepared aged balances list (see [2.2 Review Customer Aged Balances](#22-review-customer-aged-balances)).<br>Responsibility:<br>• Collections Officer |
| 1. *Open* the filter for the customer column. `[Aged Balances VG-07]` | To review selected customers, open the filter for the customer account column. If you only need a currency filter, go to step 5. |
| 2. *Select* **is one of**. `[Aged Balances VG-08]` | Select the **is one of** operator so you can choose several customers. |
| 3. *Select* each customer account. | Select each customer account you want to review. |
| 4. *Apply* the customer filter. | Apply the filter. Only the selected customers are listed. |
| 5. *Open* the filter for the **Currency** column. | To review one or more currencies, open the filter for the **Currency** column. If you don't need a currency filter, go to step 9. |
| 6. *Select* **is one of**. | Select the **is one of** operator so you can choose one or more currencies. |
| 7. *Select* each currency. | Select each currency you want to review. |
| 8. *Apply* the currency filter. | Apply the filter. Only accounts in the selected currencies are listed. |
| 9. *Confirm* the filtered list. | Check that the list shows only the customers or currencies you selected, largest balance first. |
| *PROCESS COMPLETE* (light green) | Outcomes:<br>• The **Aged balances** list shows only the selected customers or currencies, largest balance first. |

#### 2.4 Investigate a Customer Account

##### Description

Use this topic to investigate a customer account before you contact the customer. You open the account and check its balances, review the customer's transactions and, where needed, review how a transaction was settled.

##### Responsibility

- Collections Officer: investigates the customer account before contact.

##### Initiation

- A Collections Officer needs to understand a customer's account before contacting them.

##### Topic Overview

This topic includes these steps:

| Step | Description |
|---|---|
| [2.4.1 Open the Customer Account](#241-open-the-customer-account) | Open the customer account and check the balance and overdue amount. Output: the account is open. |
| [2.4.2 Review Customer Transactions](#242-review-customer-transactions) | Review open and closed transactions without currency revaluations. Output: you know what makes up the balance. |
| [2.4.3 Review Settlement History](#243-review-settlement-history) | Optional. Review what a transaction was settled against. Output: you know how a payment or credit was applied. |

#### 2.4.1 Open the Customer Account

##### Procedure

Complete these steps to open the customer account:

| **Action** | **Description** |
|---|---|
| *PROCESS START* (light blue) | Pre-requisites:<br>• Access to D365 and to the **Credit and collections** module.<br>• The customer account number or name.<br>Responsibility:<br>• Collections Officer |
| 1. *Check* the **Entity**. | Confirm you are signed into the correct **Legal Entity** (top-right). |
| 2. *Click* **Modules**. | From the left-hand **Navigation Pane**, click **Modules**. |
| 3. *Navigate* to the **All customers** page. `[Customer Account VG-01 / VG-03]` | From the **Navigation Pane**, *select*:<br>**Credit and collections >**<br>**All customers** |
| 4. *Open* the customer account. `[Customer Account VG-02]` | Find the customer and open the account. |
| 5. *Review* the account balance. `[Customer Account VG-04]` | Check the customer's balance and overdue amount. |
| *STEP COMPLETE* (light blue) | • The customer account is open.<br>• Continue to [2.4.2 Review Customer Transactions](#242-review-customer-transactions) |

#### 2.4.2 Review Customer Transactions

##### Procedure

Complete these steps to review the customer's transactions:

| **Action** | **Description** |
|---|---|
| *PROCESS START* (light blue) | Pre-requisites:<br>• The customer account is open (see [2.4.1 Open the Customer Account](#241-open-the-customer-account)).<br>Responsibility:<br>• Collections Officer |
| 1. *Click* **Transactions**. `[Customer Account VG-05]` | Open the customer's transactions from the customer account. |
| 2. *Select* **Show open**. `[Customer Account VG-06]` | Show only open transactions. |
| 3. *Hide* currency revaluations. `[Customer Account VG-07]` | Hide currency revaluation entries so only the customer's own transactions are listed. |
| 4. *Review* the open transactions. `[Customer Account VG-09]` | For each transaction, check the due date, amount, currency and description. |
| 5. *Select* **Show closed**. | Optional. To see settled transactions, show closed transactions. Otherwise, go to step 6. |
| 6. *Confirm* you know what makes up the balance. | Check that the transactions you reviewed explain the balance and overdue amount. |
| *STEP COMPLETE* (light blue) | • You have reviewed the customer's transactions.<br>• Continue to [2.4.3 Review Settlement History](#243-review-settlement-history) |

#### 2.4.3 Review Settlement History

##### Procedure

This subprocedure is optional. Complete it when you need to know what a payment, credit or invoice was settled against.

Complete these steps to review a transaction's settlement history:

| **Action** | **Description** |
|---|---|
| *PROCESS START* (light blue) | Pre-requisites:<br>• The customer's transactions are open (see [2.4.2 Review Customer Transactions](#242-review-customer-transactions)).<br>Responsibility:<br>• Collections Officer |
| 1. *Click* the transaction. `[Customer Account VG-10]` | Click the transaction so it is highlighted. Do not mark it. |
| 2. *Click* **View settlements**. `[Customer Account VG-11]` | Open the settlement history for the highlighted transaction. |
| 3. *Review* the settlement. `[Customer Account VG-12]` | Check which transactions it was settled against, and the amounts and dates. |
| 4. *Close* the settlement history. | Close the page without changing the settlement. |
| 5. *Continue* the investigation. | If needed, review the customer's notes and activities (see topics 2.5 and 2.6) or open an invoice (see topic 7.1 View and Download a Customer Invoice). |
| *PROCESS COMPLETE* (light green) | Outcomes:<br>• You have investigated the customer account and can contact the customer. |

#### 2.5 Review Customer Notes

##### Description

Use this procedure to filter the **Notes** page to one customer, narrow it if needed, and review the customer's collection notes.

##### Responsibility

- Collections Officer: reviews a customer's collection notes before contacting them.

##### Initiation

- A Collections Officer needs to review previous collection notes before contacting a customer.

##### Procedure

Complete these steps to review a customer's notes:

| **Action** | **Description** |
|---|---|
| *PROCESS START* (light blue) | Pre-requisites:<br>• Access to D365 and to the **Customer credit and collections** workspace.<br>• The customer account number.<br>Responsibility:<br>• Collections Officer |
| 1. *Check* the **Entity**. | Confirm you are signed into the correct **Legal Entity** (top-right). |
| 2. *Open* the **Notes** page. `[Notes and Activities VG-01 / VG-02]` | Open **Notes** from the **Customer credit and collections** workspace. |
| 3. *Open* the filter for the customer column. `[Notes and Activities VG-03]` | Open the filter for the customer column. |
| 4. *Enter* the customer account. | Enter or select the customer account number. |
| 5. *Apply* the filter. | Apply the filter. Only notes for that customer are listed. |
| 6. *Filter* by creator, date or note type. `[Notes and Activities VG-04]` | Optional. Filter the creator, date or note type column in the same way. Otherwise, go to step 7. |
| 7. *Review* the notes. `[Notes and Activities VG-06]` | Read the notes. Check which entries were entered by users and which were created by D365. |
| 8. *Confirm* you have the customer's collection history. | Check that the list shows only the customer you selected and covers the period you need. |
| *PROCESS COMPLETE* (light green) | Outcomes:<br>• You have reviewed the customer's collection notes. |

#### 2.6 Review All Customer Activities

##### Description

Use this procedure to review all recorded activities for a customer. You open the customer account from **All customers** and then open **View all activities** to see the customer's contact history.

##### Responsibility

- Collections Officer: reviews a customer's contact history before contacting them.

##### Initiation

- A Collections Officer needs to review previous contact with a customer before contacting them.

##### Procedure

Complete these steps to review a customer's activities:

| **Action** | **Description** |
|---|---|
| *PROCESS START* (light blue) | Pre-requisites:<br>• Access to D365 and to the **Credit and collections** module.<br>• The customer account number.<br>Responsibility:<br>• Collections Officer |
| 1. *Check* the **Entity**. | Confirm you are signed into the correct **Legal Entity** (top-right). |
| 2. *Click* **Modules**. | From the left-hand **Navigation Pane**, click **Modules**. |
| 3. *Navigate* to the **All customers** page. `[Notes and Activities VG-07]` | From the **Navigation Pane**, *select*:<br>**Credit and collections >**<br>**All customers** |
| 4. *Open* the customer account. `[Notes and Activities VG-08]` | Find the customer and open the account. |
| 5. *Click* **View all activities**. `[Notes and Activities VG-09]` | Open the list of activities recorded for the customer. |
| 6. *Filter* the activities. | Optional. Filter the list to the activities you need. If you don't need to filter, go to step 7. |
| 7. *Review* the customer's contact history. | Read the activities to see when and how the customer was contacted. |
| 8. *Check* the record is complete. | Check that each activity has its Type, Purpose and a note that stands on its own (see Key concepts, *Writing a collection note*). If details are missing or wrong, update the record. |
| *PROCESS COMPLETE* (light green) | Outcomes:<br>• You have reviewed the customer's recorded activities. |

#### 2.7 Update Customer Details

##### Description

Customer details are maintained in [200 Customer Onboarding and Maintenance](https://wisetechglobal.sharepoint.com/sites/Atlas/Training/D365%20Procedure%20Guides/200-Customer%20Onboarding%20and%20Maintenance%20PG.pdf), section 3.4, so the steps are in one place.

Collections Officers update a customer's contact details when the customer sends new ones, for example a new accounts payable (AP) contact or a new statement email address. Follow [200 Customer Onboarding and Maintenance](https://wisetechglobal.sharepoint.com/sites/Atlas/Training/D365%20Procedure%20Guides/200-Customer%20Onboarding%20and%20Maintenance%20PG.pdf), section 3.4.

> **Important:** Collections Officers do not change a customer's name, address, VAT ID or country in D365. Any change to these goes to License Management.

#### 2.8 Maintain Customer Direct Debit & eBanking Details

##### Description

Direct debit and credit card details are maintained in [240 Direct Debit and Credit Card Payments](https://wisetechglobal.sharepoint.com/sites/Atlas/Training/D365%20Procedure%20Guides/240-Direct%20Debit%20PG.pdf), topic 1 Maintain a Customer's Direct Debit Details. <mark>This topic stays here as the way in from Collections (D-053).</mark>

Customer alternate names for payment matching are maintained by the receiving team ([220 Customer Payments](https://wisetechglobal.sharepoint.com/sites/Atlas/Training/D365%20Procedure%20Guides/220-Customer%20Payments%20PG.pdf)).

### 3. Manage Customer Pools and Collection Agents

##### Description

Customer Pools group customer accounts using defined criteria, such as customer group, legal entity or financial dimensions. Assigning these pools to Collection Agents in D365 F&O establishes customer ownership and supports consistent follow-up and workload allocation. This topic covers creating pools, validating membership, configuring agents and maintaining assignments as responsibilities change.

##### Responsibility

- **Managers** are responsible for creating and maintaining Customer Pools, validating pool criteria and membership, and configuring Collection Agents and their pool assignments. Before configuration, the agent must exist as a Worker linked to a User ID, and the Customer Pool must exist before assignment.

##### Initiation

- This process is initiated when a new customer group, business area, legal entity or acquisition requires collections ownership; a Collections Officer joins or leaves the team; or existing pool criteria, agent assignments or ownership responsibilities change.

##### Topic Overview

The **Customer Pool and Collection Agent Configuration topic** includes these steps:

| Step | Description |
|---|---|
| [3.1 Create Customer Pools for Collections](#31-create-customer-pools-for-collections) | Create a Customer Pool with a unique ID, description and pool type of Collections. Define the approved criteria, preview the included customers to validate membership, and save. |
| [3.2 Add a New Collections Agent](#32-add-a-new-collections-agent) | Add the Worker to the Collections team, select the agent and assign one or more existing Customer Pools. Set a default pool where applicable and save the assignments. |

#### 3.1 Create Customer Pools for Collections

##### Procedure

Complete the steps below to Create Customer Pools for Collections.

| **Action** | **Description** |
|---|---|
| *PROCESS START* (light blue) | ***Pre-requisite:***<br>• *Customer grouping criteria (e.g., customer group, legal entity or financial dimensions) must be defined in line with approved business rules.* |
| 1. *Check* the **Entity**. | Confirm that you are signed into the correct legal entity. The entity name is shown in the top-right corner of the screen. |
| 2. *Click* **Modules**. | From the navigation pane, *click* **Modules** to expand the list of available functional areas. |
| 3. *Navigate* to **Customer Pools**. | • **Credit and collections** ><br>• **Setup** ><br>• **Customer pools**. |
| 4. *Click* **New**. | Create a new **Customer Pool** **Record**. |
| 5. *Enter* the **Pool ID**. | In the **Pool ID** field, enter the unique code for the Customer Pool. |
| 6. *Enter the* ***Pool Description****.* | In the **Pool description** field, enter a clear description of the Customer Pool. |
| 7. *Select* the **Pool Type**. | In the **Pool type** field, select **Collections**. |
| 8. *Click* **Select Pool Criteria**. | Open the **Advanced Query** window to define which customer accounts are included in the Customer Pool. |
| 9. *Add* **Criteria Range**. | On the **Range** tab, click **Add**. |
| 10. *Define* the **Criteria**. | Select the required **Table**, **Field**, and **Criteria** based on the approved business rules. For example, this may include customer group, state, credit limit, or financial dimension. |
| 11. *Click* **OK**. | Save the selected criteria and return to the **Customer pools** page. |
| 12. *Preview* the **Customer Pool**. | Click **Preview pool customers** to confirm that the correct customer accounts are included. |
| 13. *Click* **Save**. | If the preview is correct, close the preview and click **Save**. |
| *PROCESS COMPLETE* (light green) |  |

#### 3.2 Add a New Collections Agent

##### Procedure

Complete the steps below to Add a New Collections Agent.

| **Action** | **Description** |
|---|---|
| *PROCESS START* (light blue) | ***Pre-requisite:***<br>• *A customer pool must already be created before it can be assigned to a Collections Agent.* |
| 1. *Check* the **Entity**. | Confirm that you are signed into the correct legal entity. The entity name is shown in the top-right corner of the screen. |
| 2. *Click* **Modules**. | From the navigation pane, *click* **Modules** to expand the list of available functional areas. |
| 3. *Navigate* to the **Collections Agents** page. | • **Credit and collections** ><br>• **Setup** ><br>• **Collections agents**. |
| 4. Click **New**. | Create a new **Collections Agent Record**. |
| 5. *Add* the **Worker** to the Collections Team. | Scroll to **Team members**, search for and select the worker’s name, then click **Add**. |
| 6. *Select* the **New Agent**. | Return to **Credit and collections > Setup > Collections agents** and select the newly added agent. |
| 7. *Expand* the **Customer Pools FastTab**. | Open the **Customer pools** section for the selected agent. |
| 8. *Click* **Add**. | Add a **New Customer Pool** assignment line. |
| 9. *Select* the **Pool ID**. | Select the **Pool ID** the agent will manage. |
| 10. *Set* the **Default Pool**. | If applicable, set **Default pool = Yes** for the agent’s primary customer pool. |
| 11. *Repeat* for additional pools. | If the agent manages multiple customer pools, repeat the pool assignment steps as required. |
| 12. *Click* **Save**. | Save the **Collections Agent** and assigned **Customer Pools**. |
| *PROCESS COMPLETE* (light green) |  |

### 4. Contact the Customer

**Off-system**: this step is completed outside the D365 system.

##### Description

The **Contact Customer** process involves reaching out to customers with outstanding balances to discuss overdue amounts and agree on the next steps toward resolution.  
Using information gathered from the aged balances and prior activity history, the **Collections Officer** contacts the customer by phone or email to:

- Discuss overdue invoices and payment status,
- Confirm if there are any disputes or payment delays, and
- Determine an appropriate resolution (e.g., payment arrangement, resend of statement, or escalation for further action).

> **Note:** All customer contact must be recorded in D365 F&O as a new customer activity, including call notes or email correspondence, to maintain a complete communication history.

##### Responsibility

- The **Collections Officer** is responsible for contacting customers regarding overdue balances, ensuring all communication is professional, accurate, and documented in D365 F&O.  

They must follow up on unresolved accounts and take appropriate action based on the customer’s response — such as initiating payment arrangements, resending statements, or escalating to the next stage of the collections process.
##### Initiation

- This process is initiated when the Collections Officer, after reviewing aged balances and customer activity, **identifies an overdue account requiring follow-up**.

Customer contact may also occur:

- In response to a customer’s request for account details; or
- As part of routine collection monitoring to ensure timely payment.

##### Topic Overview

This topic includes these steps:

| Step | Description |
|---|---|
| [4.1 Check an Overdue Balance Before Contact](#41-check-an-overdue-balance-before-contact) | Confirm the overdue balance before contacting the customer. |

#### 4.1 Check an Overdue Balance Before Contact

##### Description

Use this procedure to check that a customer's overdue balance is valid before you contact the customer. You open the customer account from **Customers overdue**, review what makes up the overdue amount and check low-value balances for fees or overpayments.

##### Responsibility

- Collections Officer: confirms an overdue balance is valid before contact.

##### Initiation

- A Collections Officer is about to contact a customer about an overdue balance.

##### Procedure

Complete these steps to check an overdue balance:

| **Action** | **Description** |
|---|---|
| *PROCESS START* (light blue) | Pre-requisites:<br>• **Customers overdue** is open (see [2.1 Review Customers Overdue](#21-review-customers-overdue)).<br>Responsibility:<br>• Collections Officer |
| 1. *Select* the customer. | In **Customers overdue**, select the customer whose balance you are checking. |
| 2. *Open* the customer account. `[Overdue Customers VG-07]` | Open the customer account from the list. |
| 3. *Review* the overdue balance. | Check which transactions make up the overdue amount: open invoices, payments, credits and fees (see [2.4 Investigate a Customer Account](#24-investigate-a-customer-account)). |
| 4. *Check* a low-value balance. | If the overdue amount is low, check whether it represents fees or an overpayment rather than an unpaid invoice. |
| 5. *Confirm* the balance is valid. | Contact the customer only when the overdue balance is valid. If it is not, do not contact the customer:<br>• If a payment was applied to the wrong invoice or account, ask the Receipting team to correct it ([220 Customer Payments](https://wisetechglobal.sharepoint.com/sites/Atlas/Training/D365%20Procedure%20Guides/220-Customer%20Payments%20PG.pdf)).<br>• If the customer disputes the balance or does not respond, escalate it to the Group Billing and Credit Manager (see Key concepts, *Collections Workflow*). |
| *PROCESS COMPLETE* (light green) | Outcomes:<br>• You have confirmed whether the overdue balance is valid before contacting the customer. |

### 5. Record a Customer Collection Activity

##### Description

Use this procedure to record each email or phone contact with a customer as a collection activity on the customer's Collections page: its Type, Purpose and a note that is the record of what happened. Incoming and outgoing contact are separate activities, and an internal email about the account is recorded on every account involved.

##### Responsibility

- Collections Officer: records each collection contact at customer level.

##### Initiation

- A Collections Officer has contacted a customer, or been contacted by them, about their account.
- You email someone internally about the account, for example the Receipting team or Support.

##### Procedure

Complete these steps to record a collection activity:

| **Action** | **Description** |
|---|---|
| *PROCESS START* (light blue) | Pre-requisites:<br>• Access to D365 and to the **Credit and collections** module.<br>• The details of the interaction.<br>Responsibility:<br>• Collections Officer |
| 1. *Check* the **Entity**. | Confirm you are signed into the correct **Legal Entity** (top-right). |
| 2. *Click* **Modules**. | From the left-hand **Navigation Pane**, click **Modules**. |
| 3. *Navigate* to the **Aged balances** page. | From the **Navigation Pane**, *select*:<br>**Credit and collections >**<br>**Aged balances** |
| 4. *Open* the customer's **Collections** page. | Click the customer's name to open their Collections page. |
| 5. *Click* **New activity**. `[Collection Activities VG-04]` | On the Collections page, create a new activity for the customer. |
| 6. *Select* the activity type. | Select the activity type that fits: Action, Appointment, Event or Task (see Key concepts, *Collection Activities*). Action is used for a call or email that has happened. |
| 7. *Enter* the **Purpose**. | Enter a short title for the interaction, for example:<br>• Email from customer – statement request<br>• Reply to customer – invoice copy sent<br>• Overdue chaser – payment requested |
| 8. *Check* the **Priority**. | Priority defaults to Normal. Update it if needed. |
| 9. *Select* the **Type**. | Select the interaction: Email or Phone call. |
| 10. *Enter* the **Notes**. `[Collection Activities VG-08]` | Write the record of what happened. Include:<br>• who you spoke to or emailed (name or address), and the date<br>• the invoices discussed, with amount and currency<br>• any promised payment date or dispute<br>• what you sent or agreed<br>• any follow-up action<br>• your initials<br>Do not record card numbers, bank account or BSB numbers, other payment credentials or personal opinions about the customer. Do not attach documents: supporting documents are kept in CW1. |
| 11. *Save* the activity. `[Collection Activities VG-12]` | Save the activity. |
| 12. *Check* the activity is listed. `[Collection Activities VG-13]` | Check that the activity appears on the customer's Collections page. |
| *PROCESS COMPLETE* (light green) | Outcomes:<br>• The collection activity is recorded on the customer's Collections page, with its Type, Purpose and a note that stands on its own. |

### 6. Manage Customer Statements

##### Description

Use this topic to give a customer their statement. Preview and download a statement on screen without sending it, or generate and send it to the customer through **Print management destination** and verify that it was delivered.

##### Responsibility

- Collections Officer: previews and sends customer statements.

##### Initiation

- A customer asks for a statement, or a statement must be reviewed or copied. Monthly statements are sent automatically on the 5th of each month.

##### Topic Overview

This topic includes these steps:

| Step | Description |
|---|---|
| [6.1 Preview and Download a Customer Statement](#61-preview-and-download-a-customer-statement) | Generate the statement on screen and download it as a PDF. |
| [6.2 Generate and Send a Customer Statement](#62-generate-and-send-a-customer-statement) | Send the statement and verify delivery. |

#### 6.1 Preview and Download a Customer Statement

##### Description

Use this topic to generate a customer statement on screen and, when you need a copy, download it as a PDF. You set the statement options, clear **Print management destination**, select **Screen**, review the statement and then download it.

##### Responsibility

- Collections Officer: previews customer statements without sending them.

##### Initiation

- A Collections Officer needs to review a customer statement, or needs a copy of it, without sending it to the customer.

##### Topic Overview

This topic includes these steps:

| Step | Description |
|---|---|
| [6.1.1 Generate the Statement Preview](#611-generate-the-statement-preview) | Set the statement options and generate it with Screen as the destination. Output: the statement is shown on screen. |
| [6.1.2 Download the Statement as PDF](#612-download-the-statement-as-pdf) | Optional. Download the statement as a PDF with a meaningful file name. Output: a PDF copy of the statement. |

#### 6.1.1 Generate the Statement Preview

##### Procedure

Complete these steps to generate the statement preview:

| **Action** | **Description** |
|---|---|
| *PROCESS START* (light blue) | Pre-requisites:<br>• Access to D365 and to customer statements.<br>• The customer account number.<br>Responsibility:<br>• Collections Officer |
| 1. *Check* the **Entity**. | Confirm you are signed into the correct **Legal Entity** (top-right). |
| 2. *Open* the **Statements** page. `[Statement Preview VG-01]` | Open the customer statement page. |
| 3. *Select* the customer. `[Statement Preview VG-02]` | Select the customer account the statement is for. |
| 4. *Select* **Only open**. | Include only open transactions. |
| 5. *Include* the company logo. | Select the option that includes the company logo. |
| 6. *Clear* **Print management destination**. | Clear this option so the statement is not delivered to the customer. If it stays selected, D365 sends the statement to the customer straight away. |
| 7. *Select* **Screen** as the destination. `[Statement Preview VG-06]` | Set the destination to **Screen**. |
| 8. *Generate* the statement. `[Statement Preview VG-07]` | Generate the statement. It opens on screen. |
| 9. *Review* the statement. | Check that it shows the correct customer and their open transactions. |
| *STEP COMPLETE* (light blue) | • The statement is open on screen.<br>• Continue to [6.1.2 Download the Statement as PDF](#612-download-the-statement-as-pdf) |

#### 6.1.2 Download the Statement as PDF

##### Procedure

This subprocedure is optional. Complete it when you need a copy of the statement. If you only needed to review it, the task is complete.

Complete these steps to download the statement as a PDF:

| **Action** | **Description** |
|---|---|
| *PROCESS START* (light blue) | Pre-requisites:<br>• The statement is open on screen (see [6.1.1 Generate the Statement Preview](#611-generate-the-statement-preview)).<br>Responsibility:<br>• Collections Officer |
| 1. *Download* the statement as a PDF. `[Statement Preview VG-09]` | From the on-screen statement, download it as a PDF file. |
| 2. *Enter* a meaningful file name. `[Statement Preview VG-10 / VG-12]` | Name the file so the customer and the statement date can be identified. |
| 3. *Save* the PDF. | Save the PDF file. |
| 4. *Confirm* the PDF shows the correct statement. | Open the PDF and check that it shows the statement you reviewed. |
| *PROCESS COMPLETE* (light green) | Outcomes:<br>• The statement is saved as a PDF and has not been sent to the customer. |

#### 6.2 Generate and Send a Customer Statement

##### Description

Use this topic to send an ad hoc statement when a customer asks for one, and to confirm it was sent. Monthly statements are sent automatically on the 5th of each month. You set the statement options, select Print management destination, which sends the statement straight away, check the banner that confirms who it went to, and record a note on the customer's Collections page.

##### Responsibility

- Collections Officer: sends customer statements and verifies delivery.

##### Initiation

- A customer asks for a statement.

##### Topic Overview

This topic includes these steps:

| Step | Description |
|---|---|
| [6.2.1 Send the Statement](#621-send-the-statement) | Set the statement options and generate it with Print management destination. Output: the statement is sent. |
| [6.2.2 Verify Statement Delivery](#622-verify-statement-delivery) | Check the banner that confirms the statement was sent, and record a note on the customer's Collections page. |

#### 6.2.1 Send the Statement

##### Procedure

Complete these steps to send the statement:

| **Action** | **Description** |
|---|---|
| *PROCESS START* (light blue) | Pre-requisites:<br>• Access to D365 and to customer statements.<br>• The customer account number.<br>• A customer has asked for a statement.<br>Responsibility:<br>• Collections Officer |
| 1. *Check* the **Entity**. | Confirm you are signed into the correct **Legal Entity** (top-right). |
| 2. *Open* the **Statements** page. `[Statement Distribution VG-01]` | Open the customer statement page. |
| 3. *Select* the customer. `[Statement Distribution VG-02]` | Select the customer account the statement is for. |
| 4. *Select* **Only open**. | Include only open transactions. |
| 5. *Include* the company logo. | Select the option that includes the company logo. |
| 6. *Check* the statement date. | The statement is dated today. Keep today's date, even if the customer asks for a month-end date. `[G230-15]` |
| 7. *Select* **Print management destination**. | Select this option. D365 sends the statement straight away to the customer's statement contacts: the email contacts with Purpose = Business (see Key concepts, *Customer Contact Integration*). |
| 8. *Generate* the statement. `[Statement Distribution VG-07]` | Generate the statement. D365 sends it to the customer. |
| *STEP COMPLETE* (light blue) | • The statement has been generated and sent.<br>• Continue to [6.2.2 Verify Statement Delivery](#622-verify-statement-delivery) |

#### 6.2.2 Verify Statement Delivery

##### Procedure

Complete these steps to verify statement delivery:

| **Action** | **Description** |
|---|---|
| *PROCESS START* (light blue) | Pre-requisites:<br>• The statement has been sent (see [6.2.1 Send the Statement](#621-send-the-statement)).<br>Responsibility:<br>• Collections Officer |
| 1. *Check* the banner. | After the statement is sent, D365 shows a banner at the top of the page. Check that it confirms the statement was sent and names the right recipient. |
| 2. *Record* a note. | On the customer's Collections page, record the statement as a collection activity (see [5. Record a Customer Collection Activity](#5-record-a-customer-collection-activity)), with the note: Statement dated <date> sent to <email>. |
| 3. *Act* on a failed delivery. `[Statement Distribution VG-10]` | If the banner shows that the statement was not sent, or names the wrong recipient, follow the failed-delivery process. <mark>The failed-delivery process is to be confirmed.</mark> |
| *PROCESS COMPLETE* (light green) | Outcomes:<br>• The statement has been sent to the customer, the banner confirmed who it went to, and a note is recorded on the customer's Collections page. |

### 7. Resolve the Account

##### Description

The **Action / Resolution** stage in the Collections process captures potential steps taken to resolve an outstanding customer balance following contact and activity review. Depending on the outcome, the **Collections Officer** may choose one or more of the following resolution of actions.

##### Responsibility

- The **Collections Officer** is responsible for determining the appropriate resolution action based on customer response and account status. They execute or initiate the relevant process in D365 F&O and must ensure that all actions are documented through customer activity records.
- The **Group Billing & Credit Manager** is responsible for reviewing and approving any debt write-off requests and ensuring compliance with WiseTech’s credit control policies.

##### Initiation

- This process is initiated following customer contact and review of the account’s aged balance and activity history. Actions are taken based on the outcome of customer communication. E.g., when a customer requests supporting documents, disputes a charge, or fails to make payment.

##### Topic Overview

This topic includes these steps:

| Step | Description |
|---|---|
| [7.1 View and Download a Customer Invoice](#71-view-and-download-a-customer-invoice) | Open an invoice copy and download it as a PDF. |
| [7.2 Create and Send a Collection Letter](#72-create-and-send-a-collection-letter) | Generate and issue a formal collection letter. Only required if automation fails. |
| [7.3 Change Customer Status](#73-change-customer-status) | Update the customer's account status, or exclude the customer or a transaction from credit management. |
| [7.4 Write Off an Uncollectible Debt](#74-write-off-an-uncollectible-debt) | Initiate and process the write-off once management approval has been obtained. |

> **Note:** Receipting Officers settle and unsettle customer accounts, transfer open or closed payments, and write off bank fees or small residuals, in [220 Customer Payments](https://wisetechglobal.sharepoint.com/sites/Atlas/Training/D365%20Procedure%20Guides/220-Customer%20Payments%20PG.pdf) (topics 2.3, 3.1, 3.3 and 3.6). Ask the Receipting team when one of these is needed.

#### 7.1 View and Download a Customer Invoice

##### Description

Use this topic to open a customer invoice and, when you need a copy, download it as a PDF, or to send the invoice to the customer again. You highlight the invoice transaction, open its Original document and preview it; to resend it, you send a copy from the Tax invoice journal with the customer's print management settings.

##### Responsibility

- Collections Officer: retrieves and reviews customer invoices.

##### Initiation

- A customer or colleague needs a copy of an invoice, or the invoice must be reviewed before contacting the customer.

##### Topic Overview

This topic includes these steps:

| Step | Description |
|---|---|
| [7.1.1 Open the Invoice Preview](#711-open-the-invoice-preview) | Highlight the invoice transaction and open the invoice in Print preview. Output: the invoice is shown on screen. |
| [7.1.2 Download the Invoice as PDF](#712-download-the-invoice-as-pdf) | Optional. Download the invoice as a PDF with a meaningful file name. Output: a PDF copy of the invoice. |
| 7.1.3 Resend the Invoice to the Customer | Optional. Send a copy of the invoice to the customer from the Tax invoice journal. Output: the invoice is sent to the customer. |

#### 7.1.1 Open the Invoice Preview

##### Procedure

Complete these steps to open the invoice in print preview:

| **Action** | **Description** |
|---|---|
| *PROCESS START* (light blue) | Pre-requisites:<br>• Access to D365 and to the customer account.<br>• The customer account and the invoice you need.<br>Responsibility:<br>• Collections Officer |
| 1. *Check* the **Entity**. | Confirm you are signed into the correct **Legal Entity** (top-right). |
| 2. *Open* the customer's transactions. `[Customer Invoices VG-01]` | Open the transactions for the customer account, for example from **All customers**. |
| 3. *Click* the invoice transaction. `[Customer Invoices VG-02]` | Click the row for the invoice so it is highlighted. |
| 4. *Click* **Original document**. `[Customer Invoices VG-03]` | Open the original document for the highlighted transaction. |
| 5. *Select* the invoice. `[Customer Invoices VG-04]` | Select the invoice in the list of original documents. |
| 6. *Click* **Print preview**. `[Customer Invoices VG-05]` | The invoice opens in print preview. |
| 7. *Confirm* it is the invoice you need. | Review the invoice information in the preview and check that it is the invoice you selected. |
| *STEP COMPLETE* (light blue) | • The invoice is open in print preview.<br>• Continue to [7.1.2 Download the Invoice as PDF](#712-download-the-invoice-as-pdf) |

#### 7.1.2 Download the Invoice as PDF

##### Procedure

This subprocedure is optional. Complete it when you need a copy of the invoice, for example to send to a customer. If you only needed to review the invoice, the task is complete.

Complete these steps to download the invoice as a PDF:

| **Action** | **Description** |
|---|---|
| *PROCESS START* (light blue) | Pre-requisites:<br>• The invoice is open in print preview (see [7.1.1 Open the Invoice Preview](#711-open-the-invoice-preview)).<br>Responsibility:<br>• Collections Officer |
| 1. *Download* the invoice as a PDF. `[Customer Invoices VG-07]` | From the print preview, download the invoice as a PDF file. |
| 2. *Enter* a meaningful file name. `[Customer Invoices VG-08 / VG-10]` | Name the file so the customer and the invoice can be identified. |
| 3. *Save* the PDF. | Save the PDF file. |
| 4. *Confirm* the PDF shows the correct invoice. | Open the PDF and check that it shows the invoice you selected. |
| *PROCESS COMPLETE* (light green) | Outcomes:<br>• The invoice is saved as a PDF with a file name that identifies the customer and invoice. |

#### 7.1.3 Resend the Invoice to the Customer

##### Procedure

This subprocedure is optional. Complete it when the customer needs the invoice sent to them again.

Complete these steps to resend the invoice:

| **Action** | **Description** |
|---|---|
| *PROCESS START* (light blue) | Pre-requisites:<br>• The customer account and the invoice to resend.<br>Responsibility:<br>• Collections Officer |
| 1. *Check* the **Entity**. | Confirm you are signed into the correct Legal Entity (top-right). |
| 2. *Click* **Modules**. | From the left-hand Navigation Pane, click Modules. |
| 3. *Navigate* to the **All customers** page. | From the **Navigation Pane**, *select*:<br>**Credit and collections >**<br>**All customers** |
| 4. *Open* the customer account. | In the **Account** field, enter or search for the customer account, then click the **Account** link to open the customer record. |
| 5. *Navigate* to the **Tax invoice journal** page. | On the Main Toolbar, select:<br>**Invoice >**<br>**Journals >**<br>**Tax invoice journal** |
| 6. *Select* the tax invoice. | A list of the customer's tax invoice journals is displayed. Click the invoice to highlight the line. |
| 7. *Click* **Document**. | On the Action Pane, click **Document** to open the invoice output options. |
| 8. *Select* **Send** > **Copy**. | Select **Send** > **Copy** to prepare the invoice for delivery with the customer's print management settings. |
| 9. *Review* the **Print management** settings. | Click **Print management** and check the delivery method (for example email) and the recipient details. Update them if required. |
| 10. *Click* **OK**. | Click **OK** to send the invoice to the customer with the configured delivery method. |
| 11. *Record* the contact. | Record the invoice you sent as a collection activity (see [5. Record a Customer Collection Activity](#5-record-a-customer-collection-activity)), for example with the Purpose "Reply to customer – invoice copy sent". |
| *PROCESS COMPLETE* (light green) | Outcomes:<br>• The invoice is sent to the customer again, with the delivery details checked before sending.<br>• The contact is recorded on the customer's Collections page. |

#### 7.2 Create and Send a Collection Letter

##### Procedure

Complete the steps below to Create & Send Collection Letter:

| **Action** | **Description** |
|---|---|
| *PROCESS START* (light blue) | ***Pre-requisite:***<br>• *The customer must have overdue invoices requiring a collection letter and a valid recipient email address set to Purpose = Business. Manual processing is only required if automated collection letter processing fails.* |
| 1. *Check* the **Entity**. | Confirm you are signed into the correct **Legal Entity** (top-right). |
| 2. *Click* **Modules**. | From the left-hand **Navigation Pane**, click **Modules**. |
| 3. *Navigate* to the **Create Collection Letter** page. | From the **Navigation Pane**, *select*:<br>• **Credit and Collections** ><br>• **Collection Letter** ><br>• **Create Collection Letter.** |
| 4. *Populate* the **Create Collection Letter** form. | Enter the required fields:<br>***Field***<br>***What to do?***<br>*Collection letter date*<br>*Enter the relevant date.*<br>*Use Posting Profile from*<br>*Ensure this field is set to ‘Account’*<br>*Posting Profile*<br>*Ensure this field is set to ‘DEF’*<br>*Customer account*<br>*Under Records to include, click the Filter (funnel) icon and select a specific Customer/s.* |
| 5. *Click* **OK**. | The system will process and generate the collection letter. |
| 6. *Navigate* to the **Review and Process Collection Letters** page. | From the **Navigation Pane**, *select*:<br>• **Modules** ><br>• **Credit and Collections** ><br>• **Collection Letter** ><br>• **Review and Process Collection Letters.** |
| 7. *Select* the relevant **Collection Letter/s**. | *Click* the checkbox to the left for one or more collection letters.<br>**7**<br>**7** |
| 8. *Click* **Post**. | This will open the **Post collection letter note** form. |
| 9. *Click* **OK**. | This will post the collection letter. |
| 10. *Click* **Collection letter note**. | On the Main Toolbar, *click* **Print** > **Collection letter note**. |
| 11. *Set* **Use print management destination** to **Yes**. | This will apply the specific print management settings that have been configured for the customer, and output has been automated. |
| 12. *Click* **OK**. | Once completed, the collection letter will be generated and delivered according to the output selection. |
| 13. *Send* the **Collection Letter** to **the Customer**. | Export the collection letter as a .PDF file and send it to the customer using Outlook. |
| *PROCESS COMPLETE* (light green) | ***Outcomes****:*<br>• *Collection letters are successfully generated and issued to the customers.*<br>• *Collection letter delivery settings are applied correctly.*<br>• *Customers receive formal overdue payment notifications.* |

#### 7.3 Change Customer Status

##### Procedure

Complete the steps below to Change Customer Status:

| **Action** | **Description** |
|---|---|
| *PROCESS START* (light blue) | ***Pre-requisite:***<br>• *The customer account must exist in D365 F&O, and the required account status and reason for the change must be confirmed before updating the record.* |
| 1. *Check* the **Entity**. | Confirm you are signed into the correct **Legal Entity** (top-right). |
| 2. *Click* **Modules**. | From the left-hand **Navigation Pane**, click **Modules**. |
| 3. *Navigate* to the **All Customers** page. | From the **Navigation Pane**, *select*:<br>• **Credit and Collections** ><br>• **Customers** ><br>• **All Customers.** |
| 4. *Select* the relevant **Customer**. | In the **Account** field, enter or search for the customer whose account status needs to be changed.<br>*Click* the **Account** hyperlink to open the customer record. |
| 5. *Enable* **Edit** in the **Account Status** field. | Under the **Credit and collections** FastTab, *hover* over the **Account** **status** field. When the pencil (edit) icon appears, *click* the **Edit** icon to enable editing. |
| 6. *Select* the new **Account Status**. | From the **Account** **status** drop-down list, select the most relevant status based on the customer’s condition.<br>Typical options include:<br>• *Account on Hold* – used when further invoicing or delivery should be paused.<br>• *Collection Agency* – used when the debt has been referred to an external collection agency.<br>• *Legal Process* – used when legal action is underway. |
| 7. *Select* the **Account Status Reason**. | In the **Account** **status** reason drop-down, *select* the appropriate reason for the change (e.g., Bad Debt, Account Dispute, Insolvency Issue). |
| 8. *Verify* **dependent fields**. | Check that the **Confirmation**, **Delivery**, and **Invoicing** fields have been automatically updated based on the selected account status. This ensures that business rules tied to that status are enforced. |
| 9. *Click* **Save**. | On the Main Toolbar, *click* **Save** to apply the change. |
| 10. [Record Customer Activity.](#5-record-a-customer-collection-activity) | Go to **General** > **Activities** > **Activities** > **All Activities**.<br>*Click* **+ New,** select **Action**, and record details. |
| 11. *Notify* relevant **Stakeholders**. | Send an **email** or **Teams** message to the **Group Billing and Credit Manager** or **Finance team** to inform them of the account status change. Include:<br>• Customer name and account number<br>• New account status and reason<br>• Summary of actions taken<br>• Reference to the activity note created. |
| 12. *Update* **Local systems** <br>(if applicable). | Where applicable, notify the operational or billing team to block the customer account in local systems, ensuring the hold is enforced consistently across platforms. |
| 13. *Confirm* **Completion**. | Ensure the customer’s account now reflects the correct status and that relevant parties have acknowledged the change.<br>***Note:*** *ensure to document this in the Customer Activity record.* |
| 14. *OPTIONAL:*<br>Add visibility to the customer list view. | On the **All customers** grid, right-*click* the column header and select Insert columns. Add:<br>• **Account status**,<br>• **Account status reason**, then<br>• *Click* **Update**.<br>These columns will display directly on the All Customers grid, allowing for quick visibility of customers on hold or in collection. |
| 15. *OPTIONAL*<br>*Exclude* **Customer from Credit Management** | If the customer should not be included in automated collection activities or Direct Debit processing, navigate to the Customer record.<br>From the Navigation pane, select:<br>• **Modules** ><br>• **Credit and collections** ><br>• **Customers** ><br>• **All** **customers** |
| 16. *Search* for the **Customer**. | In the Customer account field, enter or search for the customer account requiring exclusion for collections processing.<br>*Click* the **account** **hyperlink** to open the customer record |
| 17. *Open* the **Credit and collections fasttab***.* | *Scroll* down and *expand* the **Credit and collections** fasttab. |
| 18. *Enable* **Exclude from Credit Management.** | In the Credit and collections fasttab, *click* the **Exclude from credit management** checkbox. |
| 19. *Click* **Save***.* | To apply the update to the customer account. |
| 20. *OPTIONAL* `[G230-03]`<br>*Exclude* **Transaction from Credit Management.** | If a specific invoice or transactions should not be included in automated collection activities or Direct Debit processing, navigate to the customer transaction page for the customer account being reviewed.<br>From the customer record, on the Main Toolbar, select **Customer > Transactions > Transactions**. |
| 21. *Review* the **Customer** **transactions**. | *Locate* and *review* the **transaction requiring exclusion** **from** **collections processing**. Confirm the invoice number, outstanding balance and transactions are correct before continuing. |
| 22. *Enable* **Exclude from Credit management.** | On the transaction line, *locate* the **Exclude from credit management** column and *click* the **checkbox** for the required transaction.<br>This setting excludes the transaction from automated collections letters and automated credit management processing activities. |
| *PROCESS COMPLETE* (light green) |  |

#### 7.4 Write Off an Uncollectible Debt

##### Procedure

Complete the steps below to Write-off Debt:

| **Action** | **Description** |
|---|---|
| *PROCESS START* (light blue) | ***Pre-requisites:***<br>*When all reasonable collection efforts have failed, send a Debt Write-off Request to the Group Billing & Credit Manager via Outlook email. Include:*<br>• *customer account,*<br>• *outstanding balance,*<br>• *collection history summary, and*<br>• *justification for the write-off.*<br>*The Group Billing & Credit Manager reviews the request and determines write-off eligibility. If approved, Group Billing & Credit Manager will complete the below steps.* |
| 1. *Check* the **Entity**. | Confirm you are signed into the correct **Legal Entity** (top-right). |
| 2. *Click* **Modules**. | From the left-hand **Navigation Pane**, click **Modules**. |
| 3. *Navigate* to the **Aged Balances** page. | From the **Navigation Pane**, *select*:<br>• **Credit and Collections** ><br>• **Collections** ><br>• **Aged balances.** |
| 4. *Select* the relevant **Customer**. | In the **Account** field, enter or search for the customer account.<br>*Click* the **Account** hyperlink to open the customer record. |
| 5. *Review* the **Outstanding Balance**. | Verify the **Overdue Transactions** to confirm the correct amount and ensure it aligns with the approved write-off value. |
| 6. *Navigate* to **Open Transactions**. | From the customer record, *click* **Open** transactions to view the individual invoices or balances eligible for write-off. |
| 7. *Select* **Transactions** to write off. | Select the specific **Invoice/s** or **Transaction/s** to be written off. Ensure that only the approved amounts are selected. |
| 8. *Click* **Write-off**. | On the toolbar, *click* **Write-off**. |
| 9. *Enter* **Write-off details.** | In the **Write-off Details** window, complete the required fields:<br>• Write-off date – Enter the date of approval.<br>• Reason code – Select the appropriate reason (e.g., Bad Debt, Unrecoverable, Customer Bankrupt, Over/Short). |
| 10. *Verify* **Posting Details**. | Review that the correct main account and offset account for write-off are applied based on configuration. If required, update the posting layer or dimension. |
| 11. *Confirm* **the Write-off**. | *Click* **OK** to post the write-off journal. |
| 12. *Review* the **Write-off Journal**. | Navigate to **General Ledger** > **Journal** **entries** > **General Journals**.<br>Open the newly created write-off journal and verify that the debit and credit entries are balanced and posted correctly. |
| 13. *Validate* the **Journal.** | On the Main **T**oolbar, *click* **Validate** > **Simulate** **posting** to confirm there are no errors.<br>If validation errors are displayed, review the error message, correct the issue, and repeat validation before continuing. |
| 14. [Record the Write-off activity.](#5-record-a-customer-collection-activity) | Navigate to **Modules** > **Credit** **&** **Collections** > **Customers** > **All** **customers**.<br>Search for and open the relevant **Customer** **account**.<br>From the customer page, on the Main Toolbar, go to **General** > **Activities** > **Activities** > **All activities**.<br>*Click* **+ New**, select Action (Type), and record:<br>• **Purpose**: Debt Write-off approved<br>• **Description**: $X written off on [date] due to [reason] for the write-off.<br>*Click* Save to record the activity.<br>Note: The write-off activity must be recorded before submitting the journal for approval to ensure the request is documented and auditable. |
| 15. *Submit* the **Journal** for **Approval**. | On the Main Toolbar, *click* **Approval** > **Report** **as** **ready**.<br>The journal has been submitted for approval. The approver will receive a notification to review and approve the journal. Once approved, notification is sent confirming approval. |
| 16. *Notify* **Stakeholders**. | Email or message the relevant stakeholders confirming the write-off completion. |
| *PROCESS COMPLETE* (light green) |  |

### 8. Update and Close a Customer Activity

##### Description

Updating and closing customer activity in **D365 F&O** ensures that all collection tasks and interactions are accurately finalized and recorded for audit and reporting purposes.  
Once a customer's query or collection action has been resolved, the **Collections Officer** must update the corresponding activity record to reflect the outcome and mark it as complete.

Each activity update should include:

- **Resolution details** summarize the outcome of the activity (e.g., payment received, collection letter sent, account on hold).
- A note that stands on its own: supporting documents are kept in CW1, not attached in D365.
- **Completion status**, confirming that no further follow-up is required.

Do not attach documents to the activity record. Supporting documents are kept in CW1, so the resolution details must say enough to stand on their own.

##### Responsibility

- The Collections Officer is responsible for reviewing, updating, and closing customer activity records once the related action has been completed. They must ensure that the activity accurately reflects the outcome before marking the activity as complete. Failure to close activities may result in incomplete records and reduced visibility of customer resolution history.

##### Initiation

- This process is initiated **after completing any collection-related action** (e.g., sending a collection letter, confirming payment, changing customer status, or processing a write-off).  

Closing the activity ensures that all actions taken are finalized in **D365 F&O**, maintaining accurate and up-to-date records of customer interactions and collection outcomes.
**Procedure**: Follow the steps on the next page to execute this task in-system.

##### Procedure

Complete the steps below to Update & Close Customer Activity:

| **Action** | **Description** |
|---|---|
| *PROCESS START* (light blue) | ***Pre-requisite:***<br>• *The customer account must exist in D365 F&O, and the required account status and reason for the change must be confirmed before updating the record.* |
| 1. *Check* the **Entity**. | Confirm you are signed into the correct **Legal Entity** (top-right). |
| 2. *Click* **Modules**. | From the left-hand **Navigation Pane**, click **Modules**. |
| 3. *Navigate* to the **All Customers** page. | From the **Navigation Pane**, *select*:<br>• **Modules** ><br>• **Credit and Collections** ><br>• **Customers** ><br>• **All Customers.** |
| 4. *Select* the relevant **Customer**. | In the **Customer** account field, enter or search for the customer whose account status needs to be changed.<br>*Click* the **Account number** to open the customer record. |
| 5. *Navigate* to **All Activities > Record Event.** | From the **Main Toolbar**, *select*:<br>• **General** ><br>• **Activities** ><br>• **Activities** ><br>• **All Activities**.<br>A list of customer activities will be displayed. |
| 6. *Select* the relevant **Activity** from the list. | Identify and open the activity to be updated and closed. |
| 7. *Populate* the **Resolution** section. | Enter the outcome or resolution details, such as payment received, collection letter sent, or debt written off. Ensure all notes are clear and concise. |
| 8. *Click* **Set as complete**. | Mark the activity as complete to close it. The activity will move from an active to a closed status. |
| *PROCESS COMPLETE* (light green) | The customer activity is now closed and recorded as part of the collection's history. |

---

## Part 3: Reports (Collections)

##### Page Overview

This page contains various reports related to the **Credit Collections process**.

##### Customer Ageing Report

| **Navigation** | **Description** |
|---|---|
| • ***Credit and Collections*** *>*<br>• ***Enquiries and reports*** *>*<br>• ***Customers*** *>*<br>• ***Customer ageing report****.* | The Customer aging report displays the balances that are due from customers, sorted by date interval, or aging period. |

##### Customer Report

| **Navigation** | **Description** |
|---|---|
| • ***Credit and Collections*** *>*<br>• ***Enquiries and reports*** *>*<br>• ***Customers*** *>*<br>• ***Customer report****.* | The customer report displays detailed insights on customer data such as contact information, purchasing history, and payment details. |

##### Customer Balance list

| **Navigation** | **Description** |
|---|---|
| • ***Credit and Collections*** *>*<br>• ***Enquiries and reports*** *>*<br>• ***Customers*** *>*<br>• ***Customer balance list report****.* | The customer balance list report displays side by side customer balances for the defined periods. This report helps you quickly analyses changes in accounts receivable. |

##### Customer Account Statement

| **Navigation** | **Description** |
|---|---|
| • ***Credit and Collections*** *>*<br>• ***Enquiries and reports*** *>*<br>• ***Customers*** *>*<br>• ***Customer account statement.*** | The customer statement outlines a customer’s financial transactions over a certain period and highlights the current outstanding balance. |

---

## Additional Resources

The standard template block, unchanged.
