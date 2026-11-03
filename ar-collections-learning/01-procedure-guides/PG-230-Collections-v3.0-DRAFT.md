# D365 F&O: Collections Procedure Guide

> **WORKING DRAFT. Not validated or approved.**
>
> This is a Markdown preview of the Word guide [`230-Collections PG v3.0.docx`](230-Collections%20PG%20v3.0.docx). It was assembled from the topic drafts named in its version history, under D-045 and D-046. **The Word file is the editable source.**
>
> Markers such as `[G230-05]` or `[Aged Balances VG-03]` show unconfirmed items. In the Word file, each one is a review comment. Guide-level items and the index of carried items are in the [validation register](../03-validation/230-Collections-v3.0-Validation.md). The markers are not part of the guide text.

The fixed template content is not repeated here: cover, Contents, *About this guide* and *Additional Resources*.

**Version history**

| ID | Date | Author/s | BPO | Description of change |
|---|---|---|---|---|
| 2.0 | October 2025 | Daniel Moreira | Christoper Clarke | Version Upgrade |
| 2.1 | April 2026 | Suzanne Starr | Christoper Clarke | Content Update (DD + Bank) |
| 2.2 | May 2026 | Suzanne Starr | Christoper Clarke | Content Update (CW1) |
| 2.3 | October 2026 | Daniel Moreira | Christoper Clarke | Content Review |
| 2.4 | November 2026 | Daniel Moreira | Christopher Clarke | Content Update, draft (ADO 16886): 6.5 to 6.8 moved to 221; 2.4 to move to 240 |
| 3.0 | November 2026 | Daniel Moreira | Christopher Clarke | Working draft (ADO 16886): rebuilt in the PG master template; nine AR Collections topic drafts merged. Not validated or approved. `[G230-05]` |

Guide code, title and scope: `[]`.

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
- **Record a Customer Collection Activity**: record collection interactions, outcomes and agreed actions in D365, and attach relevant supporting correspondence and documents.
- **Manage Customer Statements**: preview, download and send customer statements.
- **Resolve the Account**: resend invoices, issue collection letters, update customer status or process approved debt write-offs. Payment corrections are in 221 Customer Payment Corrections.
- **Update and Close a Customer Activity**: update the activity record in D365 with the outcome and close it once the issue is resolved and no further follow-up is required.

General D365 tasks (switching legal entity, Favorites, personalized views and exporting grid data) are in 260 O2C Getting Started.

##### Initiation

- Customer balances remain unpaid beyond agreed payment terms. `[G230-06]`
- System reports or automated reminders identify accounts for follow-up, or the Group Billing & Credit Manager requests it.
- New customer groups, legal entities or team members need collections ownership, or existing pool criteria or assignments change.

##### Stream

| Stream | Process Area | Key Roles |
|---|---|---|
| Order to Cash (O2C) `[G230-07]` | Collections | • Collections Officer<br>• Group Billing and Credit Manager |

##### Process

The high-level Collections process is as follows:

| # | Action | Who | When | Where |
|---|---|---|---|---|
| 1 | [Start the Collections Day](#1-start-the-collections-day) | Collections Officer | At the start of each working day | D365 |
| 2 | [Monitor Customers](#2-monitor-customers) | Collections Officer | Following statement issues or weekly during debt review cycles | D365 |
| 3 | [Manage Customer Pools and Collection Agents](#3-manage-customer-pools-and-collection-agents) | Group Billing and Credit Manager | When new pools or agents are required, or pool criteria or ownership assignments change | D365 |
| 4 | [Contact the Customer](#4-contact-the-customer) | Collections Officer | Upon identification of overdue or disputed balances | D365; Outlook / Other |
| 5 | [Record a Customer Collection Activity](#5-record-a-customer-collection-activity) | Collections Officer | Immediately after customer contact or correspondence | D365 |
| 6 | [Manage Customer Statements](#6-manage-customer-statements) | Collections Officer | When a statement must be reviewed, copied or sent | D365 |
| 7 | [Resolve the Account](#7-resolve-the-account) | Collections Officer; Group Billing and Credit Manager | As required following escalation, dispute, or collection outcome | D365 / Outlook |
| 8 | [Update and Close a Customer Activity](#8-update-and-close-a-customer-activity) | Collections Officer | Once the issue is resolved, payment received, or case closed | D365 |

> **Note:** The high-level process includes new D365 F&O, new non-D365 F&O, and existing (BAU) activities. This procedure guide does not include BAU procedures.

### Roles and responsibilities

##### Overview

The roles come from legacy 230 and the topic drafts. For 7.4, the Collections Officer requests the write-off by email to the Group Billing and Credit Manager, who creates the write-off journal once the request is approved.

| **Tasks / Business Roles** | Collections Officer | Group Billing and Credit Manager |
|---|---|---|
| 1 [Start the Collections Day](#1-start-the-collections-day) | R |   |
| 1.1 [Open the Customer Credit and Collections Workspace](#11-open-the-customer-credit-and-collections-workspace) | R |   |
| 1.2 [Locate Collection Work in the Workspace](#12-locate-collection-work-in-the-workspace) | R |   |
| 2 [Monitor Customers](#2-monitor-customers) | R |   |
| 2.1 [Review Customers Overdue](#21-review-customers-overdue) | R |   |
| 2.2 [Review Customer Aged Balances](#22-review-customer-aged-balances) | R |   |
| 2.3 [Filter Aged Balances by Customer or Currency](#23-filter-aged-balances-by-customer-or-currency) | R |   |
| 2.4 [Investigate a Customer Account](#24-investigate-a-customer-account) | R |   |
| 2.5 [Review Customer Notes](#25-review-customer-notes) | R |   |
| 2.6 [Review All Customer Activities](#26-review-all-customer-activities) | R |   |
| 2.7 [Update Customer Details](#27-update-customer-details) | R |   |
| 2.8 [Maintain Customer Direct Debit & eBanking Details](#28-maintain-customer-direct-debit--ebanking-details) | R |   |
| 3 [Manage Customer Pools and Collection Agents](#3-manage-customer-pools-and-collection-agents) | R | R |
| 3.1 [Create Customer Pools for Collections](#31-create-customer-pools-for-collections) |   | R |
| 3.2 [Add a New Collections Agent](#32-add-a-new-collections-agent) |   | R |
| 4 [Contact the Customer](#4-contact-the-customer) | R |   |
| 4.1 [Check an Overdue Balance Before Contact](#41-check-an-overdue-balance-before-contact) | R |   |
| 5 [Record a Customer Collection Activity](#5-record-a-customer-collection-activity) | R |   |
| 6 [Manage Customer Statements](#6-manage-customer-statements) | R |   |
| 6.1 [Preview and Download a Customer Statement](#61-preview-and-download-a-customer-statement) | R |   |
| 6.2 [Generate and Send a Customer Statement](#62-generate-and-send-a-customer-statement) | R |   |
| 7 [Resolve the Account](#7-resolve-the-account) | R | R |
| 7.1 [View and Download a Customer Invoice](#71-view-and-download-a-customer-invoice) | R |   |
| 7.2 [Create and Send a Collection Letter](#72-create-and-send-a-collection-letter) | R |   |
| 7.3 [Change Customer Status](#73-change-customer-status) | R |   |
| 7.4 [Write Off an Uncollectible Debt](#74-write-off-an-uncollectible-debt) | R | R |
| 8 [Update and Close a Customer Activity](#8-update-and-close-a-customer-activity) | R |   |

\*R = Responsible

### Key concepts

##### Overview

Before you start, you need to know how to set up D365 for collections work, the Customer credit and collections workspace, the collections rules and automation, and the terms used in each task.

##### Set up D365 for collections work

Add these pages to your Favorites, and add these columns to the views you use for collection work. The general steps are in 260 O2C Getting Started (topic 3 Add Pages to Favorites and topic 4 Create a Personalized View).

| Page | Description |
|---|---|
| **All customers** | Located in the **Credit and collections** module. Used to open customer accounts and customer master details. |
| **Aged balances** | Located in the **Credit and collections** module. Used to review customer balances by aging period. `[Favorites VG-01]` |
| **Customer payment journal** | Located in the **Credit and collections** module. Identified in AR Collections training as a key page for AR Collections users. `[Favorites VG-18]` |
| **Open customer invoices** | Located in the **Accounts receivable** module. Used to review open customer invoices. `[Favorites VG-19]` |

| Column | Notes |
|---|---|
| **Recommended columns** | Customer account, Customer name, Transaction date, Due date, Description, Amount, Currency, Overdue balance and Email address. `[Personalized Views VG-01]` |

##### The Customer credit and collections workspace

| Term | Description |
|---|---|
| **Workspace** | A D365 page that brings together the information and tasks for one area of work. The **Customer credit and collections** workspace is the starting point for collection work. `[Workspace VG-09]` |
| **Sections used in AR Collections** | **Customers overdue**, **Payment journals not posted**, **Notes** and **Open payment journals**. `[Workspace VG-04 to VG-07]` |
| **Other sections** | The workspace also shows sections such as **Open cases**, **Customers over credit limit** and **Collections letters not printed**. Which of these are used in AR Collections is pending confirmation. `[Workspace VG-08]` |

##### Workspaces and modules

| Term | Description |
|---|---|
| **Workspace or module** | The **Customer credit and collections** workspace opens from **Workspaces**. The **Credit and collections** module opens from **Modules** and lists pages such as **All customers** and **Aged balances**. `[Workspace VG-11]` |

##### Collections Workflow

A customer’s overdue balance is subject to follow-up and activity tracking in D365 F&O:

| If… | Then… |
|---|---|
| The customer has overdue invoices within acceptable tolerance. | The Collections Officer will contact the customer to arrange payment and record the interaction in D365 F&O. |
| The customer is unresponsive or disputes the balance. | The issue will be escalated to the Group Billing & Credit Manager for review or resolution. |
| The customer debt is deemed uncollectible. | The Collections Officer will initiate a Debt Write-off request for approval and processing. |
| A payment has been applied incorrectly to a customer account. | The Collections Officer will transfer, settle, or unsettle transactions as required to correct the customer balance. |

**Collection Activities**

Each collection action is recorded as a Customer Activity in D365 F&O:

| Activity Type | Purpose |
|---|---|
| **Action** | Immediate follow-up, e.g., phone calls or reminders. |
| **Appointment** | Scheduling a future contact or meeting. |
| **Event** | Recording a general update or collection milestone. |
| **Task** | Internal reminders, e.g., follow-up next week. |

**Customer Activity Status**

A customer account status identifies the state of a customer account:

| Status | Description |
|---|---|
| **Open** | The activity is active and pending further action. |
| **In Progress** | The activity is being actioned (e.g., awaiting customer response). |
| **Resolved** | The issue has been addressed, or payment has been received. |
| **Closed** | The activity is complete, and no further follow-up is required. |

**Invoice Due Reminder Automation**

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

**Customer Payment Management**

Customer payments may require manual adjustment to ensure balances are correctly reflected. These corrections are in 221 Customer Payment Corrections:

| Action | Timing |
|---|---|
| **Settle Customer Accounts** | Match customer payments against outstanding invoices. See 221 topic 1. |
| **Unsettle Customer Accounts** | Reverse an incorrect settlement. See 221 topic 2. |
| **Transfer Open / Closed Payments** | Move payments between customer accounts when allocated incorrectly. See 221 topic 3. |
| **Bank Fee Write-off** | Clear small residual balances caused by fees, FX differences, or minor variances. See 221 topic 6. |

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
| Contact inactive / AR flag removed in CW1 |   | **D365**: Entire contact removed in D365 | Contact no longer used in collections communications. |
| Contact created in D365 (Business purpose) | D365 ↔ CW1 | **CW1**: New AR contact created in CW1 | Allows the collection team to add valid contacts. |
| Contact updated in D365 | D365 ↔ CW1 | **CW1**: Email / phone updates sync (name changes do not) | Maintains consistency across systems. |
| Email Purpose ≠ Business in D365 | D365 ↔ CW1 ↔ D365 | **D365**: AR flag removed → contact deleted | Contact excluded from all communications. |
| Primary flag changed in D365 | D365 ↔ CW1 | **CW1**: Official flag removed in CW1 | Impacts main contact designation. |
| Email deleted in D365 | D365 ↔ CW1 ↔ D365 | **D365**: AR flag removed → contact fully removed. | Contact removed from collections usage. |

##### Customers overdue

| Term | Description |
|---|---|
| **Customers overdue** | A page in the **Customer credit and collections** workspace that lists customers with overdue balances. `[Overdue Customers VG-01]` |
| **Aging period** | The page shows overdue balances for the aging period you select, for example **90+** or **61-90** days. `[Overdue Customers VG-02 / VG-03]` |
| **Balance due and overdue amount** | The balance due is the customer's total outstanding balance. The overdue amount is the part that is past its due date. The two can differ. `[Overdue Customers VG-04]` |

##### Before contacting a customer

| Rule | Description |
|---|---|
| **Check the balance first** | Investigate an overdue balance before you contact the customer. A low-value balance may represent fees or an overpayment rather than an unpaid invoice. `[Overdue Customers VG-09]` |

##### The Aged balances page

| Term | Description |
|---|---|
| **Aged balances** | A page in the **Credit and collections** module that shows customer balances by aging period. `[Aged Balances VG-01]` |
| **Reporting currency** | The page can show amounts in the ledger's reporting currency, which can differ from the currency of the customer's transactions. Add the **Currency** column so each account's currency is visible. `[Aged Balances VG-09]` |
| **Zero balances** | Accounts with a zero balance are listed unless you filter them out. Filtering the balance column to **not equal to** **0** removes them. |

##### Sharing balances with customers

| Rule | Description |
|---|---|
| **Use PDF, not Excel** | Provide customer-facing account information as a PDF. Do not send a customer an Excel export of this page. `[Aged Balances VG-13]` |

##### Transactions and settlements

| Term | Description |
|---|---|
| **Open and closed transactions** | Open transactions still have an amount outstanding. Closed transactions have been fully settled. You can show either set on the customer's transactions. `[Customer Account VG-06]` |
| **Currency revaluations** | Entries D365 creates when it revalues foreign currency balances. Hide them so the list shows only the customer's own transactions. `[Customer Account VG-07 / VG-08]` |
| **Settlement** | The matching of a payment or credit to the invoices it pays. A transaction's settlement history shows what it was settled against. `[Customer Account VG-12]` |

##### Reviewing without changing

| Rule | Description |
|---|---|
| **Do not undo settlements here** | This topic only reviews settlement history. Undoing a settlement changes financial records and is in 221 Customer Payment Corrections, topic 2 Undo a Settlement. `[Customer Account VG-13]` |

##### Notes and activities

| Term | Description |
|---|---|
| **Notes** | A page in the **Customer credit and collections** workspace that lists notes recorded against customer accounts. You filter it to see one customer's collection history. `[Notes and Activities VG-01 / VG-02]` |
| **System-generated entries** | The Notes page lists entries created by D365, such as statements and collection letters, alongside notes entered by users. `[Notes and Activities VG-05 / VG-06]` |
| **Customer activities** | Records of collection contact with a customer, such as an email or phone activity. **View all activities** on the customer account lists them. `[Notes and Activities VG-12]` |

##### Recording collection history (notes and activities)

| Rule | Description |
|---|---|
| **Record notes at customer level** | Collection notes are recorded against the customer account rather than against individual invoices, so the full history is in one place. `[Notes and Activities VG-11]` |

##### Collection activities

| Term | Description |
|---|---|
| **Collection activity** | A record on the customer account of a collection contact with the customer, such as an email or telephone call. It holds a summary and notes of the interaction. |
| **Activity type** | The kind of contact the activity records, for example email or phone. Use the approved activity types. `[Collection Activities VG-05 / VG-06]` |
| **Summary and notes** | A concise summary of the interaction, with notes that give the details another officer needs. `[Collection Activities VG-09 / VG-10]` |

##### Recording collection history (collection activities)

| Rule | Description |
|---|---|
| **Record at customer level** | Record collection activities against the customer account rather than against individual invoices, so the full history is visible in the account overview. `[Collection Activities VG-14]` |

##### Statements and destinations

| Term | Description |
|---|---|
| **Customer statement** | A document that lists a customer's transactions. With **Only open** selected, it lists only open transactions. `[Statement Preview VG-03]` |
| **Print management destination** | The destination used to deliver a statement to the customer. Clear it when you only want to preview the statement. `[Statement Preview VG-05]` |
| **Screen destination** | Displays the statement on screen so you can review it and download it, without sending it. `[Statement Preview VG-06]` |

##### Previewing safely

| Rule | Description |
|---|---|
| **Check the destination first** | Before you generate a preview, check that **Print management destination** is cleared and **Screen** is selected. `[Statement Preview VG-05]` |
| **Use PDF, not Excel** | Provide customer-facing account information as a PDF. Do not send a customer an Excel export. `[Statement Preview VG-15]` |

##### Statement distribution

| Term | Description |
|---|---|
| **Print management destination** | The destination that delivers the statement to the customer. When it is selected, generating the statement sends it. `[Statement Distribution VG-05 / VG-06]` |
| **Delivery message** | The message D365 shows after the statement is generated, which indicates whether it was sent. `[Statement Distribution VG-08]` |
| **Collections sent mailbox** | A mailbox where sent statements can be checked when required. `[Statement Distribution VG-09]` |

##### Before sending

| Rule | Description |
|---|---|
| **Check the customer can receive a statement** | Before you send, check that the customer is not excluded from statements and is not affected by the known multi-currency limitations. `[Statement Distribution VG-12 / VG-13]` |
| **Use the approved parameters** | Send statements only with the approved statement parameters. `[Statement Distribution VG-17]` |

##### Invoices and transactions

| Term | Description |
|---|---|
| **Original document** | The document D365 produced for a posted transaction, such as the customer invoice. You open it from the transaction it belongs to. `[Customer Invoices VG-03 / VG-04]` |
| **Print preview** | Shows the original document on screen so you can review it and download it as a PDF. |
| **Highlighted row** | Click a transaction row to highlight it before you open its original document. Highlighting a row is not the same as marking it with its checkbox. `[Customer Invoices VG-02]` |

##### Sending documents to customers

| Rule | Description |
|---|---|
| **Use PDF, not Excel** | Provide customer-facing account information as a PDF. Do not send a customer an Excel export. `[Customer Invoices VG-12]` |

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
| [Open the Customer Credit and Collections Workspace](#11-open-the-customer-credit-and-collections-workspace) | Open the workspace from the dashboard or the Navigation Pane. |
| [Locate Collection Work in the Workspace](#12-locate-collection-work-in-the-workspace) | Find the workspace section needed for the task. |

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
| *PROCESS START* (light blue) | *Pre-requisites:*<br>• Access to D365 and to the **Customer credit and collections** workspace.<br>*Responsibility:*<br>• Collections Officer |
| 1. *Check* the **Entity**. | Confirm you are signed into the correct **Legal Entity** (top-right). |
| 2. *Click* **Workspaces**. `[Workspace VG-01]` | From the left-hand **Navigation Pane**, click **Workspaces**. |
| 3. *Select* **Customer credit and collections**. `[Workspace VG-02]` | Select the **Customer credit and collections** workspace from the list. |
| 4. *Confirm* the workspace is open. `[Workspace VG-03 / VG-10]` | Check that the **Customer credit and collections** workspace is displayed for the legal entity you selected in step 1. |
| *PROCESS COMPLETE* (light green) | *Outcomes:*<br>• The **Customer credit and collections** workspace is open. |

#### 1.2 Locate Collection Work in the Workspace

##### Description

Use this procedure to find the workspace sections used in normal collection work. Each section links to work covered by its own topic in this guide.

##### Responsibility

- Collections Officer: finds the workspace section needed for the task.

##### Initiation

- A Collections Officer needs to find where a collection task starts in the workspace. `[Workspace VG-14]`

##### Procedure

Complete these steps to locate collection work in the workspace:

| **Action** | **Description** |
|---|---|
| *PROCESS START* (light blue) | *Pre-requisites:*<br>• The **Customer credit and collections** workspace is open (see [Open the Customer Credit and Collections Workspace](#11-open-the-customer-credit-and-collections-workspace)).<br>*Responsibility:*<br>• Collections Officer |
| 1. *Locate* **Customers overdue**. `[Workspace VG-04]` | Find **Customers overdue**. Use it to review customers with overdue balances. |
| 2. *Locate* **Payment journals not posted**. `[Workspace VG-05]` | Find **Payment journals not posted**. Use it to identify customer payment journals that have not been posted. |
| 3. *Locate* **Notes**. `[Workspace VG-06]` | Find **Notes**. Use it to review customer collection notes (see topics 2.5 and 2.6). |
| 4. *Locate* **Open payment journals**. `[Workspace VG-07]` | Find **Open payment journals**. Use it to start investigating unallocated customer payments. |
| 5. *Open* the section you need. | Open the section for your task and continue with the topic for that task. |
| *PROCESS COMPLETE* (light green) | *Outcomes:*<br>• The workspace section for the task is open. |

### 2. Monitor Customers

##### Description

**Monitoring customers** in D365 F&O enables the **Collections Officer** to proactively track overdue balances, review historical activities, and determine appropriate follow-up actions.This process ensures that all customer accounts are regularly assessed for outstanding amounts and recent interactions, supporting timely debt recovery and accurate account management.

Together, these steps provide a complete view of the customer’s financial position and interaction history, enabling informed and consistent collection decisions.

##### Responsibility

The **Collections Officer** is responsible for monitoring customer accounts daily in D365 F&O, ensuring that aged balances and activity records are reviewed and accurately maintained.They must identify overdue accounts requiring follow-up and ensure that all prior correspondence and actions are properly recorded before making new contact.

##### Initiation

This process is initiated as part of the **daily collection routine**, or when follow-up is required on specific overdue accounts. It may also be triggered by:

A scheduled collections review cycle; or

Customer or internal queries regarding account status or previous collection activity.

##### Topic Overview

This topic includes these steps:

| Step | Description |
|---|---|
| [Review Customers Overdue](#21-review-customers-overdue) | List customers with overdue balances and open an account to follow up. |
| [Review Customer Aged Balances](#22-review-customer-aged-balances) | Review customer balances by aging period. |
| [Filter Aged Balances by Customer or Currency](#23-filter-aged-balances-by-customer-or-currency) | Limit Aged balances to one customer or currency. |
| [Investigate a Customer Account](#24-investigate-a-customer-account) | Open the account and review its transactions and settlement history. |
| [Review Customer Notes](#25-review-customer-notes) | Read the notes recorded for a customer. |
| [Review All Customer Activities](#26-review-all-customer-activities) | Review previous collection activities for a customer. |
| [Update Customer Details](#27-update-customer-details) | Review and update customer contact and account details. |
| [Maintain Customer Direct Debit & eBanking Details](#28-maintain-customer-direct-debit--ebanking-details) | Maintain direct debit, banking and eBanking records. Moving to 240 Direct Debit. |

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
| *PROCESS START* (light blue) | *Pre-requisites:*<br>• Access to D365 and to the **Customer credit and collections** workspace.<br>*Responsibility:*<br>• Collections Officer |
| 1. *Check* the **Entity**. | Confirm you are signed into the correct **Legal Entity** (top-right). |
| 2. *Click* **Workspaces**. | From the **Navigation Pane**, click **Workspaces**, then select **Customer credit and collections**. |
| 3. *Click* **Customers overdue**. `[Overdue Customers VG-01]` | In the workspace, click **Customers overdue**. |
| 4. *Select* the aging period. `[Overdue Customers VG-02]` | Select the aging period you are working on, for example **90+**. |
| 5. *Sort* the overdue amount from largest to smallest. `[Overdue Customers VG-05]` | Sort the overdue amount column in descending order so the largest overdue amounts appear first. |
| 6. *Add* the email address column. `[Overdue Customers VG-06]` | Optional. Add the email column with **Insert columns** (see 260 O2C Getting Started, topic 4 Create a Personalized View). Otherwise, go to step 7. |
| 7. *Review* the balance due and overdue amount. `[Overdue Customers VG-04]` | Check the aging period, then compare each customer's balance due with the overdue amount, largest first. |
| *PROCESS COMPLETE* (light green) | *Outcomes:*<br>• **Customers overdue** shows the selected aging period, sorted from the largest overdue amount. |

#### 2.2 Review Customer Aged Balances

##### Description

Use this procedure to open the **Aged balances** page and prepare the list for collection work. You add the **Currency** column, remove accounts with a zero balance and sort the balances from largest to smallest, so the customers with the highest outstanding balances appear first. You can save the prepared layout as a view by following 260 O2C Getting Started, topic 4 Create a Personalized View.

##### Responsibility

- Collections Officer: reviews customer balances before collection work.

##### Initiation

- A Collections Officer needs to identify customers with outstanding balances before starting collection work.

##### Procedure

Complete these steps to prepare the aged balances list:

| **Action** | **Description** |
|---|---|
| *PROCESS START* (light blue) | *Pre-requisites:*<br>• Access to D365 and to the **Credit and collections** module.<br>*Responsibility:*<br>• Collections Officer |
| 1. *Check* the **Entity**. | Confirm you are signed into the correct **Legal Entity** (top-right). |
| 2. *Click* **Modules**. | From the left-hand **Navigation Pane**, click **Modules**. |
| 3. *Navigate* to the **Aged balances** page. `[Aged Balances VG-02]` | From the **Navigation Pane**, *select*:<br>• **Credit and collections >**<br>• **Aged balances**<br>If **Aged balances** is in your **Favorites** (see 260 O2C Getting Started, topic 3 Add Pages to Favorites), you can open it from **Favorites** instead. |
| 4. *Click* **Insert columns**. `[Aged Balances VG-04 / VG-12]` | Use **Insert columns** to add the **Currency** column if the grid does not already show it. |
| 5. *Select* the **Currency** column. | Select **Currency** in the list of columns. |
| 6. *Confirm* the **Currency** column is displayed. | Check that each account now shows its currency. |
| 7. *Open* the filter for the balance column. `[Aged Balances VG-03 / VG-05]` | Open the filter for the balance column you are reviewing. |
| 8. *Select* **not equal to**. | Select the **not equal to** operator. |
| 9. *Enter* **0**. | Enter **0** as the filter value. |
| 10. *Apply* the filter. `[Aged Balances VG-05]` | Apply the filter. Accounts with a zero balance are no longer listed. |
| 11. *Sort* the balance column from largest to smallest. `[Aged Balances VG-06]` | Sort the balance column in descending order so the largest balances appear first. |
| 12. *Confirm* the list is ready to review. | Check that the list shows only non-zero balances, largest first, with each account's currency. |
| *PROCESS COMPLETE* (light green) | *Outcomes:*<br>• The **Aged balances** list shows only customers with a non-zero balance, sorted from largest to smallest.<br>• Each account shows its currency. |

> **Note:** Legacy 230 (v2.3, 2.1 View Customer Aged Balances) also sorts **Amount due** largest first, reads the aging icons and opens the customer's Collections page by clicking the customer name. It also says aging balances refresh by a batch job every 10 minutes, so a change posted in the last 10 minutes can be missing. `[G230-08]`

#### 2.3 Filter Aged Balances by Customer or Currency

##### Description

Use this procedure when you need the aged balances for selected customers or for one or more currencies. You filter the customer column to the accounts you need, or filter the **Currency** column, or both. Start from the list prepared in Review Customer Aged Balances.

##### Responsibility

- Collections Officer: narrows the aged balances list to the customers or currencies under review.

##### Initiation

- Only selected customers or currencies need review. `[Aged Balances VG-14]`

##### Procedure

Complete these steps to filter the aged balances list:

| **Action** | **Description** |
|---|---|
| *PROCESS START* (light blue) | *Pre-requisites:*<br>• The prepared aged balances list (see [Review Customer Aged Balances](#22-review-customer-aged-balances)).<br>*Responsibility:*<br>• Collections Officer |
| 1. *Open* the filter for the customer column. `[Aged Balances VG-07]` | To review selected customers, open the filter for the customer account column. If you only need a currency filter, go to step 5. |
| 2. *Select* **is one of**. `[Aged Balances VG-08]` | Select the **is one of** operator so you can choose several customers. |
| 3. *Select* each customer account. | Select each customer account you want to review. |
| 4. *Apply* the customer filter. | Apply the filter. Only the selected customers are listed. |
| 5. *Open* the filter for the **Currency** column. | To review one or more currencies, open the filter for the **Currency** column. If you don't need a currency filter, go to step 9. |
| 6. *Select* **is one of**. | Select the **is one of** operator so you can choose one or more currencies. |
| 7. *Select* each currency. | Select each currency you want to review. |
| 8. *Apply* the currency filter. | Apply the filter. Only accounts in the selected currencies are listed. |
| 9. *Confirm* the filtered list. | Check that the list shows only the customers or currencies you selected, largest balance first. |
| *PROCESS COMPLETE* (light green) | *Outcomes:*<br>• The **Aged balances** list shows only the selected customers or currencies, largest balance first. |

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
| [Open the Customer Account](#241-open-the-customer-account) | Open the customer account and check the balance and overdue amount. Output: the account is open. |
| [Review Customer Transactions](#242-review-customer-transactions) | Review open and closed transactions without currency revaluations. Output: you know what makes up the balance. |
| [Review Settlement History](#243-review-settlement-history) | Optional. Review what a transaction was settled against. Output: you know how a payment or credit was applied. |

#### 2.4.1 Open the Customer Account

##### Procedure

Complete these steps to open the customer account:

| **Action** | **Description** |
|---|---|
| *PROCESS START* (light blue) | *Pre-requisites:*<br>• Access to D365 and to the **Credit and collections** module.<br>• The customer account number or name.<br>*Responsibility:*<br>• Collections Officer |
| 1. *Check* the **Entity**. | Confirm you are signed into the correct **Legal Entity** (top-right). |
| 2. *Click* **Modules**. | From the left-hand **Navigation Pane**, click **Modules**. |
| 3. *Navigate* to the **All customers** page. `[Customer Account VG-01 / VG-03]` | From the **Navigation Pane**, *select*:<br>• **Credit and collections >**<br>• **All customers**<br>You can also open **All customers** from your **Favorites** (see 260 O2C Getting Started, topic 3 Add Pages to Favorites). |
| 4. *Open* the customer account. `[Customer Account VG-02]` | Find the customer and open the account. |
| 5. *Review* the account balance. `[Customer Account VG-04]` | Check the customer's balance and overdue amount. |
| *STEP COMPLETE* (light blue) | • The customer account is open.<br>• Continue to [Review Customer Transactions](#242-review-customer-transactions) |

#### 2.4.2 Review Customer Transactions

##### Procedure

Complete these steps to review the customer's transactions:

| **Action** | **Description** |
|---|---|
| *PROCESS START* (light blue) | *Pre-requisites:*<br>• The customer account is open (see [Open the Customer Account](#241-open-the-customer-account)).<br>*Responsibility:*<br>• Collections Officer |
| 1. *Click* **Transactions**. `[Customer Account VG-05]` | Open the customer's transactions from the customer account. |
| 2. *Select* **Show open**. `[Customer Account VG-06]` | Show only open transactions. |
| 3. *Hide* currency revaluations. `[Customer Account VG-07]` | Hide currency revaluation entries so only the customer's own transactions are listed. |
| 4. *Review* the open transactions. `[Customer Account VG-09]` | For each transaction, check the due date, amount, currency and description. |
| 5. *Select* **Show closed**. | Optional. To see settled transactions, show closed transactions. Otherwise, go to step 6. |
| 6. *Confirm* you know what makes up the balance. `[Customer Account VG-15]` | Check that the transactions you reviewed explain the balance and overdue amount. |
| *STEP COMPLETE* (light blue) | • You have reviewed the customer's transactions.<br>• Continue to [Review Settlement History](#243-review-settlement-history) |

#### 2.4.3 Review Settlement History

##### Procedure

This subprocedure is optional. Complete it when you need to know what a payment, credit or invoice was settled against.

Complete these steps to review a transaction's settlement history:

| **Action** | **Description** |
|---|---|
| *PROCESS START* (light blue) | *Pre-requisites:*<br>• The customer's transactions are open (see [Review Customer Transactions](#242-review-customer-transactions)).<br>*Responsibility:*<br>• Collections Officer |
| 1. *Click* the transaction. `[Customer Account VG-10]` | Click the transaction so it is highlighted. Do not mark it. |
| 2. *Click* **View settlements**. `[Customer Account VG-11]` | Open the settlement history for the highlighted transaction. |
| 3. *Review* the settlement. `[Customer Account VG-12]` | Check which transactions it was settled against, and the amounts and dates. |
| 4. *Close* the settlement history. | Close the page without changing the settlement. |
| 5. *Continue* the investigation. | If needed, review the customer's notes and activities (see topics 2.5 and 2.6) or open an invoice (see topic 7.1 View and Download a Customer Invoice). |
| *PROCESS COMPLETE* (light green) | *Outcomes:*<br>• You have investigated the customer account and can contact the customer. |

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
| *PROCESS START* (light blue) | *Pre-requisites:*<br>• Access to D365 and to the **Customer credit and collections** workspace.<br>• The customer account number.<br>*Responsibility:*<br>• Collections Officer |
| 1. *Check* the **Entity**. | Confirm you are signed into the correct **Legal Entity** (top-right). |
| 2. *Open* the **Notes** page. `[Notes and Activities VG-01 / VG-02]` | Open **Notes** from the **Customer credit and collections** workspace. |
| 3. *Open* the filter for the customer column. `[Notes and Activities VG-03]` | Open the filter for the customer column. |
| 4. *Enter* the customer account. | Enter or select the customer account number. |
| 5. *Apply* the filter. | Apply the filter. Only notes for that customer are listed. |
| 6. *Filter* by creator, date or note type. `[Notes and Activities VG-04]` | Optional. Filter the creator, date or note type column in the same way. Otherwise, go to step 7. |
| 7. *Review* the notes. `[Notes and Activities VG-06]` | Read the notes. Check which entries were entered by users and which were created by D365. |
| 8. *Confirm* you have the customer's collection history. `[Notes and Activities VG-13]` | Check that the list shows only the customer you selected and covers the period you need. |
| *PROCESS COMPLETE* (light green) | *Outcomes:*<br>• You have reviewed the customer's collection notes. |

#### 2.6 Review All Customer Activities

##### Description

Use this procedure to review all recorded activities for a customer. You open the customer account from **All customers** and then open **View all activities** to see the customer's contact history.

##### Responsibility

- Collections Officer: reviews a customer's contact history before contacting them.

##### Initiation

- A Collections Officer needs to review previous contact with a customer before contacting them. `[Notes and Activities VG-14]`

##### Procedure

Complete these steps to review a customer's activities:

| **Action** | **Description** |
|---|---|
| *PROCESS START* (light blue) | *Pre-requisites:*<br>• Access to D365 and to the **Credit and collections** module.<br>• The customer account number.<br>*Responsibility:*<br>• Collections Officer |
| 1. *Check* the **Entity**. | Confirm you are signed into the correct **Legal Entity** (top-right). |
| 2. *Click* **Modules**. | From the left-hand **Navigation Pane**, click **Modules**. |
| 3. *Navigate* to the **All customers** page. `[Notes and Activities VG-07]` | From the **Navigation Pane**, *select*:<br>• **Credit and collections >**<br>• **All customers**<br>If **All customers** is in your **Favorites** (see 260 O2C Getting Started, topic 3 Add Pages to Favorites), you can open it from **Favorites** instead. |
| 4. *Open* the customer account. `[Notes and Activities VG-08]` | Find the customer and open the account. |
| 5. *Click* **View all activities**. `[Notes and Activities VG-09]` | Open the list of activities recorded for the customer. |
| 6. *Filter* the activities. `[Notes and Activities VG-10]` | Optional. Filter the list to the activities you need. If you don't need to filter, go to step 7. |
| 7. *Review* the customer's contact history. | Read the activities to see when and how the customer was contacted. |
| *PROCESS COMPLETE* (light green) | *Outcomes:*<br>• You have reviewed the customer's recorded activities. |

> **Note:** Legacy 230 (v2.3, 2.2 Review Customer Activity) opens activities with **All activities**, and also checks the attachments on each activity and corrects the record where needed. `[G230-09]`

#### 2.7 Update Customer Details

##### Procedure

Complete the steps below to Update Customer Details:

| **Action** | **Description** |
|---|---|
| *PROCESS START* | **Pre-requisite:**<br>1. *The customer account must exist in D365 F&O.*<br>*Note:*<br>2. *Customer contact details are synchronized between CW1 and D366. Users must ensure contact information is accurate, and that email Purpose is set to Business, so communications can be sent. Incorrect updates may result in contacts being excluded from communications.* |
| 3. *Check* the **Entity**. | Confirm you are signed into the correct **Legal Entity** (top-right). |
| 4. *Click* **Modules**. | From the left-hand **Navigation Pane**, click **Modules**. |
| 5. *Navigate* to the **All Customers** page. | From the Navigation pane, select;<br>6. **Accounts receivable >**<br>7. **Customers >**<br>8. **All customers.**<br>The **All customers** page is displayed. |
| 9. *Search* for the **Customer.** | In the **Filter** field, start *typing* the **customer’s** **name** or **account**.<br>If searching by customer name, select **Name** from the dropdown list (alternatively select Account or Invoice account as required).<br>The matching customer records are displayed in the list. |
| 10. *Open the* **Customer Record.** | *Click* the **Account** hyperlink for the selected customer to open the record. |
| 11. *Open* the **Contact Information** FastTab. | *Scroll* to and *expand* the **Contact information** FastTab.<br>Existing customer contact records are displayed. |
| 12. *Review* **Existing** **contact** **information.** | Review all contact information and confirm that email addresses and phone numbers are correct.<br>Some contract records may have been automatically synchronized from CargoWise1 (CW1).<br>Each contact detail is stored as a separate record in D366. Multiple contacts may exist for a single customer.<br>Confirm for each contact:<br>13. Contact details are valid (correct email address or phone number).<br>14. The Description clearly identifies the contact, i.e., name and role.<br>15. Email contacts used for collections emails have Purpose = Business.<br>Important:<br>Only contacts with Purpose = Business are used for AR activities, including invoices, statements, and collections communications.<br>If Purpose is changed from Business, the contact maybe removed from AR communications and deleted through integration. If a contact is missing or incorrect, check whether it exists in CW1 as customer contact information may be primarily maintained in CW1. |
| 16. *Add a* **New Contact.** | If the required contact does not exist, on the **Contact information** toolbar, *click* **+Add.** A new contact line is displayed. |
| 17. *Enter a* **Description.** | In the **Description** field, *enter* the **contact’s** **name**. |
| 18. *Select* the **Contact Type.** | In the **Type** field, *select* the required contact type from the dropdown list e.g., Email address or Phone. |
| 19. *Enter the* **Contact Details.** | In the **Contact number/address** field, *enter* the **email** **address** or **phone** **number**. |
| 20. *Set* **Primary** **contact**  *(if required).* | *Click* **Primary** checkbox if this is the main contact for the customer. Each customer should have one primary contact.<br>**Note:** Primary contact is used as the default for communication in D366. Only one contact is marked as **Primary**. |
| 21. *Set* **Communication Purpose** (if required). | On the Toolbar, *click* **Advanced**. The **Edit contact** **information** pane is displayed. *Click* the dropdown arrow in the **Purpose** field to select **Business.**<br>**Note**: The contact is enabled for AR communications such as invoices, statements, and collections. |
| 22. *Validate* **Contact setup.** | Confirm:<br>23. The correct contact(s) are set to **Purpose = Business**<br>24. No duplicate or incorrect contacts exists.<br>Important:<br>If Purpose does not equal Business, the contact may be excluded from AR communications and removed through integration.<br>Updates to email and phone may synchronize between D365 and CW1 (name changes may not). |
| 25. *Add* **Additional Email Addresses** *(if required).* | To add more email addresses, repeat the previous steps for each additional contact. |
| 26. *Remove* **Old Contact Details** *(if required).* | To delete a contact, select it, then *click* **Remove** on the toolbar. When the message *“You are about to delete a record appears*,” *click* **Yes**. |
| 27. *Click* **Save***.* | From the Main toolbar, *click* **Save**. The contact details are updated and synchronized where applicable. |
| *PROCESS COMPLETE* | *Customer contact details are correctly maintained for AR and Collections communications.* |

#### 2.8 Maintain Customer Direct Debit & eBanking Details

> **Note:** This topic is planned to move to **240 Direct Debit** (initial scope shared with the O2C stakeholders on 3 November 2026; ADO Task 16894). It stays in this guide until 240 is published. `[G230-04]`

##### Procedure

Complete the steps below to Maintain Customer Direct Debit & eBanking Details:

| **Action** | **Description** |
|---|---|
| *PROCESS START* | **Pre-requisite:**<br>1. *The customer account must exist in D365 F&O, and the approved customer authorisation form with current banking details must be available before creating or updating direct debit and eBanking records.* |
| 2. *Check* the **Entity**. | Confirm you are signed into the correct **Legal Entity** (top-right). |
| 3. *Click* **Modules**. | From the left-hand **Navigation Pane**, click **Modules**. |
| 4. *Navigate* to the **All Customers** page. | From the Navigation pane, select;<br>5. **Accounts receivable >**<br>6. **Customers >**<br>7. **All customers.**<br>The **All customers** page is displayed. |
| 8. *Search* for the **Customer.** | In the **Filter** field, start *typing* the **customer’s** **name** or **account**.<br>If searching by customer name, select **Name** from the dropdown list (alternatively *select* **Account** or **Invoice** **account** as required).<br>The matching customer records are displayed in the list. |
| 9. *Open the* **Customer Record.** | *Click* the **Account** hyperlink for the selected customer to open the record. |
| 10. *Open* the **Payment defaults** FastTab. | *Scroll* to and *expand* the **Payment defaults** FastTab.<br>This section controls how customer payments are processed in D366. |
| 11. *Edit* the **Payment defaults.** | On the Main Toolbar, *click* **Edit** to update the customer payment configuration fields. |
| 12. *Update* **Method of payment** field. | In the **Method of payment** field, *select* the required direct debit payment method from the dropdown list, e.g., DDHDBCAU, DDHSBCUS.<br>The Method of payment determines how customer payments are generated and processed during direct debit payment runs.<br>Important:<br>When Method of payment is selected, D365 may automatically populate the related Payment specification field based on the configured payment setup. |
| 13. *Validate* the **Payment specification** field. | Review the **Payment specification** and confirm that the automatically populated value is correct for the customer direct debit setup e.g., ACH-CCD = DDHSBCUS, DE = DDWBCAU.<br>The Payment specification identified the banking configuration and payment file format used during direct debit processing.<br>If the Payment specification field does not automatically populate, manually select the correct value from the dropdown list. |
| 14. *Save* the **Payment** **default** **changes.** | On the Main toolbar, *click* **Save** to save the update before continuing. |
| 15. *Click* **Modules**. | From the navigation pane, *click* **Modules** to expand the list of available functional areas. |
| 16. *Navigate* to the **Customer eBanking details** page. | From the Navigation pane, select;<br>17. **Treasury Automation Suite** ><br>18. **Common** ><br>19. **Customer eBanking details.**<br>The Customer eBanking details page is used to maintain customer eBanking records by Treasury Automation Suite for payment processing. |
| 20. *Search* for the **Customer** **eBanking** **record**. | Search for the customer using the customer account or customer name. If an existing customer eBanking record is displayed, review and update the existing information as required. |
| 21. *Create* a **New** **eBanking** **record** (If required). | If the customer does not already exist in Customer eBanking details, *click* **+New.** Populate the required fields:<br>Note: The Customer eBanking details record links the customer account to Treasury Automation Suite (TAS) payment processing functionality and is used during automated payment matching, direct debit processing, and customer settlement activities. Alternate customer names may assist TAS in identifying customer payments where the bank transaction narrative differs from the official customer’s name. |
| 22. *Configure* the **eSettlement / Lockbox settings***.* | Scroll to and expand the eSettlement / Lockbox section and complete the following fields:<br>Note: The eSettlement/lockbox settings control how imported customer payments and bank transactions are matched and settled against customer invoices during automated settlement processing. Incorrect settlement configuration may result in unmatched transactions, incorrect invoice allocations, or failed automated settlement processing. |
| 23. *Configure* the **Direct Debit settings**. | Scroll to the Direct Debits section and update the required fields to enable the customer for direct debit processing.<br>Note: The Direct debit settings section controls whether the customer is enabled for automated direct debit processing within TAS. If these settings are not configured correctly, the customer may not be included in direct debit payment proposal processing. |
| 24. *Create* a **Customer bank account.** | On the Main Toolbar, *click* **Customer bank accounts**.<br>The Customer bank accounts page is displayed. |
| 25. *Click* **+New***.* | On the Main Toolbar, *click* **+New** to create a customer bank record.<br>This stores the customer’s banking information used for direct debit processing. |
| 26. *Click* **Edit***.* | On the Main Toolbar, *click* **Edit**. |
| 27. *Enter* the **Customer Bank Account** fields*.* | Scroll to and expand the General section.<br>Complete the required bank account fields;<br>Important:<br>Banking details must match exactly the approved customer authorization form. Incorrect banking information may cause direct debit errors. |
| 28. *Add* **Address information***.* | Scroll to and expand the Address section. On the Address Toolbar, *click* +New. The New address pane will open.<br>Note: A full physical bank address is not required for this process. |
| 29. *Click* **Save***.* | On the Main toolbar, *click* **Save** to save the customer's bank account configuration. |
| 30. *Return* to **Customer eBanking details** screen. | On the Main Toolbar, *click* the **back arrow** to return to the **Customer eBanking details** screen. |
| 31. *Create* a **Payment specifications** record*.* | On the Main toolbar, *click* **Payment specifications** tab to open the Customer eBanking payment spec details. |
| 32. *Click* **+New***.* | On the Main Toolbar, *click* **+New** to create a new payment specification record used for direct debit processing. |
| 33. *Populate* the **Payment specifications** fields*.* | In the Customer eBanking spec details page, complete the following fields: |
| 34. *Save* the **Payment** **specification** **record***.* | On the Main toolbar, *click* Save to finalize the direct debit payment specification setup. |
| 35. *Validate the Direct Debit configuration.* | Review and confirm the following information is correctly configured:<br>36. Method of payment is correct.<br>37. Payment specifications are assigned.<br>38. Customer bank accounts exist.<br>39. The currency is correct. Direct debits are activated.<br>40. The company's bank account is assigned. |
| 41. *OPTIONAL:Update or Remove* **Direct Debit Details**. | If a customer changes payment method or opts out of direct debit processing:<br>42. Update or remove the Method of payment<br>43. Update or remove the Payment specification<br>44. Remove direct debit related banking details where required.<br>45. Update the customer to a new agreed payment arrangement.<br>Examples include:<br>46. Customer changing from Direct Debit to EFT<br>47. Customer moving to Credit Card payments<br>48. Customer temporarily opting out of direct debit processing. |
| *PROCESS COMPLETE* | **Outcomes***:*<br>49. *Customer direct debit and eBanking details are correctly configured in D365 F&O and TAS.*<br>50. *Customer payment methods and banking information are accurately maintained for direct debit processing.*<br>51. *Customer records reflect current payment arrangements and direct debit status.* |

### 3. Manage Customer Pools and Collection Agents

##### Description

Customer Pools group customer accounts using defined criteria, such as customer group, legal entity or financial dimensions. Assigning these pools to Collection Agents in D365 F&O establishes customer ownership and supports consistent follow-up and workload allocation. This topic covers creating pools, validating membership, configuring agents and maintaining assignments as responsibilities change.

##### Responsibility

**Managers** are responsible for creating and maintaining Customer Pools, validating pool criteria and membership, and configuring Collection Agents and their pool assignments. Before configuration, the agent must exist as a Worker linked to a User ID, and the Customer Pool must exist before assignment.

##### Initiation

This process is initiated when a new customer group, business area, legal entity or acquisition requires collections ownership; a Collections Officer joins or leaves the team; or existing pool criteria, agent assignments or ownership responsibilities change.

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
| *PROCESS START* | **Pre-requisite:**<br>1. *Customer grouping criteria (e.g., customer group, legal entity or financial dimensions) must be defined in line with approved business rules.* |
| 2. *Check* the **Entity**. | Confirm that you are signed into the correct legal entity. The entity name is shown in the top-right corner of the screen. |
| 3. *Click* **Modules**. | From the navigation pane, *click* **Modules** to expand the list of available functional areas. |
| 4. *Navigate* to **Customer Pools**. | 5. **Credit and collections** ><br>6. **Setup** ><br>7. **Customer pools**. |
| 8. *Click* **New**. | Create a new **Customer Pool** **Record**. |
| 9. *Enter* the **Pool ID**. | In the **Pool ID** field, enter the unique code for the Customer Pool. |
| 10. *Enter the* **Pool Description***.* | In the **Pool description** field, enter a clear description of the Customer Pool. |
| 11. *Select* the **Pool Type**. | In the **Pool type** field, select **Collections**. |
| 12. *Click* **Select Pool Criteria**. | Open the **Advanced Query** window to define which customer accounts are included in the Customer Pool. |
| 13. *Add* **Criteria Range**. | On the **Range** tab, click **Add**. |
| 14. *Define* the **Criteria**. | Select the required **Table**, **Field**, and **Criteria** based on the approved business rules. For example, this may include customer group, state, credit limit, or financial dimension. |
| 15. *Click* **OK**. | Save the selected criteria and return to the **Customer pools** page. |
| 16. *Preview* the **Customer Pool**. | Click **Preview pool customers** to confirm that the correct customer accounts are included. |
| 17. *Click* **Save**. | If the preview is correct, close the preview and click **Save**. |
| *PROCESS COMPLETE* |   |

#### 3.2 Add a New Collections Agent

##### Procedure

Complete the steps below to Add a New Collections Agent.

| **Action** | **Description** |
|---|---|
| *PROCESS START* | **Pre-requisite:**<br>1. *A customer pool must already be created before it can be assigned to a Collections Agent.* |
| 2. *Check* the **Entity**. | Confirm that you are signed into the correct legal entity. The entity name is shown in the top-right corner of the screen. |
| 3. *Click* **Modules**. | From the navigation pane, *click* **Modules** to expand the list of available functional areas. |
| 4. *Navigate* to the **Collections Agents** page. | 5. **Credit and collections** ><br>6. **Setup** ><br>7. **Collections agents**. |
| 8. Click **New**. | Create a new **Collections Agent Record**. |
| 9. *Add* the **Worker** to the Collections Team. | Scroll to **Team members**, search for and select the worker’s name, then click **Add**. |
| 10. *Select* the **New Agent**. | Return to **Credit and collections > Setup > Collections agents** and select the newly added agent. |
| 11. *Expand* the **Customer Pools FastTab**. | Open the **Customer pools** section for the selected agent. |
| 12. *Click* **Add**. | Add a **New Customer Pool** assignment line. |
| 13. *Select* the **Pool ID**. | Select the **Pool ID** the agent will manage. |
| 14. *Set* the **Default Pool**. | If applicable, set **Default pool = Yes** for the agent’s primary customer pool. |
| 15. *Repeat* for additional pools. | If the agent manages multiple customer pools, repeat the pool assignment steps as required. |
| 16. *Click* **Save**. | Save the **Collections Agent** and assigned **Customer Pools**. |
| *PROCESS COMPLETE* |   |

### 4. Contact the Customer

**Off-system**: this step is completed outside the D365 system.

##### Description

The **Contact Customer** process involves reaching out to customers with outstanding balances to discuss overdue amounts and agree on the next steps toward resolution.Using information gathered from the aged balances and prior activity history, the **Collections Officer** contacts the customer by phone or email to:

Discuss overdue invoices and payment status,

Confirm if there are any disputes or payment delays, and

Determine an appropriate resolution (e.g., payment arrangement, resend of statement, or escalation for further action).

> **Note:** All customer contact must be recorded in D365 F&O as a new customer activity, including call notes or email correspondence, to maintain a complete communication history.

##### Responsibility

The **Collections Officer** is responsible for contacting customers regarding overdue balances, ensuring all communication is professional, accurate, and documented in D365 F&O.They must follow up on unresolved accounts and take appropriate action based on the customer’s response — such as initiating payment arrangements, resending statements, or escalating to the next stage of the collections process.

##### Initiation

This process is initiated when the Collections Officer, after reviewing aged balances and customer activity, **identifies an overdue account requiring follow-up**.

Customer contact may also occur:

In response to a customer’s request for account details; or

As part of routine collection monitoring to ensure timely payment.

##### Topic Overview

This topic includes these steps:

| Step | Description |
|---|---|
| [Check an Overdue Balance Before Contact](#41-check-an-overdue-balance-before-contact) | Confirm the overdue balance before contacting the customer. |

#### 4.1 Check an Overdue Balance Before Contact

##### Description

Use this procedure to check that a customer's overdue balance is valid before you contact the customer. You open the customer account from **Customers overdue**, review what makes up the overdue amount and check low-value balances for fees or overpayments.

##### Responsibility

- Collections Officer: confirms an overdue balance is valid before contact.

##### Initiation

- A Collections Officer is about to contact a customer about an overdue balance. `[Overdue Customers VG-14]`

##### Procedure

Complete these steps to check an overdue balance:

| **Action** | **Description** |
|---|---|
| *PROCESS START* (light blue) | *Pre-requisites:*<br>• **Customers overdue** is open (see [Review Customers Overdue](#21-review-customers-overdue)).<br>*Responsibility:*<br>• Collections Officer |
| 1. *Select* the customer. | In **Customers overdue**, select the customer whose balance you are checking. |
| 2. *Open* the customer account. `[Overdue Customers VG-07]` | Open the customer account from the list. |
| 3. *Review* the overdue balance. `[Overdue Customers VG-08]` | Check which transactions make up the overdue amount. |
| 4. *Check* a low-value balance. | If the overdue amount is low, check whether it represents fees or an overpayment rather than an unpaid invoice. |
| 5. *Confirm* the balance is valid. `[Overdue Customers VG-10]` | Contact the customer only when the overdue balance is valid. If it is not, do not contact the customer and investigate the balance first. |
| *PROCESS COMPLETE* (light green) | *Outcomes:*<br>• You have confirmed whether the overdue balance is valid before contacting the customer. |

### 5. Record a Customer Collection Activity

##### Description

Use this procedure to record an email or telephone contact as a collection activity on the customer account.

##### Responsibility

- Collections Officer: records each collection contact at customer level.

##### Initiation

- A Collections Officer has contacted a customer, or been contacted by them, about their account.

##### Procedure

Complete these steps to record a collection activity:

| **Action** | **Description** |
|---|---|
| *PROCESS START* (light blue) | *Pre-requisites:*<br>• Access to D365 and to the **Credit and collections** module.<br>*Responsibility:*<br>• Collections Officer |
| 1. *Check* the **Entity**. | Confirm you are signed into the correct **Legal Entity** (top-right). |
| 2. *Click* **Modules**. | From the left-hand **Navigation Pane**, click **Modules**. |
| 3. *Navigate* to the **All customers** page. `[Collection Activities VG-01 / VG-03]` | From the **Navigation Pane**, *select*:<br>• **Credit and collections >**<br>• **All customers** |
| 4. *Open* the customer account. `[Collection Activities VG-02]` | Find the customer and open the account. |
| 5. *Click* **New activity**. `[Collection Activities VG-04]` | Create a new activity for the customer. |
| 6. *Select* the activity type. `[Collection Activities VG-05]` | Select the type of contact, for example email or phone. |
| 7. *Enter* a summary. `[Collection Activities VG-07]` | Enter a concise summary of the interaction. |
| 8. *Enter* the notes. `[Collection Activities VG-08 / VG-09]` | Enter the details of the contact. |
| 9. *Save* the activity. `[Collection Activities VG-12]` | Save the activity. |
| 10. *Check* the activity is listed. `[Collection Activities VG-13]` | Check that the activity appears in the customer's activities. |
| *PROCESS COMPLETE* (light green) | *Outcomes:*<br>• The collection activity is recorded on the customer account and is visible in the customer's activities. |

> **Note:** Legacy 230 (v2.3, 5 Record New Customer Activity) also sets the activity type (**Action**, **Appointment**, **Event** or **Task**), **Purpose**, **Priority**, **Type** (for example **Phone call**) and **Description**, and makes attaching supporting documents mandatory. `[G230-11]`

### 6. Manage Customer Statements

##### Description

Use this topic to give a customer their statement. Preview and download a statement on screen without sending it, or generate and send it to the customer through **Print management destination** and verify that it was delivered.

##### Responsibility

- Collections Officer: previews and sends customer statements.

##### Initiation

- A customer statement must be reviewed, copied or sent to the customer.

##### Topic Overview

This topic includes these steps:

| Step | Description |
|---|---|
| [Preview and Download a Customer Statement](#61-preview-and-download-a-customer-statement) | Generate the statement on screen and download it as a PDF. |
| [Generate and Send a Customer Statement](#62-generate-and-send-a-customer-statement) | Send the statement and verify delivery. |

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
| [Generate the Statement Preview](#611-generate-the-statement-preview) | Set the statement options and generate it with Screen as the destination. Output: the statement is shown on screen. |
| [Download the Statement as PDF](#612-download-the-statement-as-pdf) | Optional. Download the statement as a PDF with a meaningful file name. Output: a PDF copy of the statement. |

#### 6.1.1 Generate the Statement Preview

##### Procedure

Complete these steps to generate the statement preview:

| **Action** | **Description** |
|---|---|
| *PROCESS START* (light blue) | *Pre-requisites:*<br>• Access to D365 and to customer statements.<br>• The customer account number.<br>*Responsibility:*<br>• Collections Officer |
| 1. *Check* the **Entity**. | Confirm you are signed into the correct **Legal Entity** (top-right). |
| 2. *Open* the **Statements** page. `[Statement Preview VG-01]` | Open the customer statement page. |
| 3. *Select* the customer. `[Statement Preview VG-02]` | Select the customer account the statement is for. |
| 4. *Select* **Only open**. `[Statement Preview VG-03]` | Include only open transactions. |
| 5. *Include* the company logo. `[Statement Preview VG-04]` | Select the option that includes the company logo. |
| 6. *Clear* **Print management destination**. `[Statement Preview VG-05]` | Clear this option so the statement is not delivered to the customer. |
| 7. *Select* **Screen** as the destination. `[Statement Preview VG-06]` | Set the destination to **Screen**. |
| 8. *Generate* the statement. `[Statement Preview VG-07]` | Generate the statement. It opens on screen. |
| 9. *Review* the statement. `[Statement Preview VG-08]` | Check that it shows the correct customer and their open transactions. |
| *STEP COMPLETE* (light blue) | • The statement is open on screen.<br>• Continue to [Download the Statement as PDF](#612-download-the-statement-as-pdf) |

#### 6.1.2 Download the Statement as PDF

##### Procedure

This subprocedure is optional. Complete it when you need a copy of the statement. If you only needed to review it, the task is complete.

Complete these steps to download the statement as a PDF:

| **Action** | **Description** |
|---|---|
| *PROCESS START* (light blue) | *Pre-requisites:*<br>• The statement is open on screen (see [Generate the Statement Preview](#611-generate-the-statement-preview)).<br>*Responsibility:*<br>• Collections Officer |
| 1. *Download* the statement as a PDF. `[Statement Preview VG-09]` | From the on-screen statement, download it as a PDF file. |
| 2. *Enter* a meaningful file name. `[Statement Preview VG-10 / VG-12]` | Name the file so the customer and the statement date can be identified. |
| 3. *Save* the PDF. `[Statement Preview VG-11]` | Save the PDF file. |
| 4. *Confirm* the PDF shows the correct statement. | Open the PDF and check that it shows the statement you reviewed. |
| *PROCESS COMPLETE* (light green) | *Outcomes:*<br>• The statement is saved as a PDF and has not been sent to the customer. `[Statement Preview VG-24]` |

#### 6.2 Generate and Send a Customer Statement

##### Description

Use this topic to send a customer statement and check that it was delivered. You set the statement options, select **Print management destination**, generate the statement and then verify delivery. To review a statement before sending it, use topic 6.1 Preview and Download a Customer Statement.

##### Responsibility

- Collections Officer: sends customer statements and verifies delivery.

##### Initiation

- A customer statement must be sent to the customer.

##### Topic Overview

This topic includes these steps:

| Step | Description |
|---|---|
| [Send the Statement](#621-send-the-statement) | Set the statement options and generate it with Print management destination. Output: the statement is sent. |
| [Verify Statement Delivery](#622-verify-statement-delivery) | Check the delivery message and, where required, the Collections sent mailbox. Output: delivery is confirmed. |

#### 6.2.1 Send the Statement

##### Procedure

Complete these steps to send the statement:

| **Action** | **Description** |
|---|---|
| *PROCESS START* (light blue) | *Pre-requisites:*<br>• Access to D365 and to customer statements.<br>• The customer account number.<br>• The customer can receive a statement (see **Key concepts**).<br>*Responsibility:*<br>• Collections Officer |
| 1. *Check* the **Entity**. | Confirm you are signed into the correct **Legal Entity** (top-right). |
| 2. *Open* the **Statements** page. `[Statement Distribution VG-01]` | Open the customer statement page. |
| 3. *Select* the customer. `[Statement Distribution VG-02]` | Select the customer account the statement is for. |
| 4. *Select* **Only open**. `[Statement Distribution VG-03]` | Include only open transactions. |
| 5. *Include* the company logo. `[Statement Distribution VG-04]` | Select the option that includes the company logo. |
| 6. *Select* **Print management destination**. `[Statement Distribution VG-05 / VG-06]` | Select this option so the statement is delivered to the customer. |
| 7. *Generate* the statement. `[Statement Distribution VG-07]` | Generate the statement. D365 sends it to the customer. |
| *STEP COMPLETE* (light blue) | • The statement has been generated and sent.<br>• Continue to [Verify Statement Delivery](#622-verify-statement-delivery) |

#### 6.2.2 Verify Statement Delivery

##### Procedure

Complete these steps to verify statement delivery:

| **Action** | **Description** |
|---|---|
| *PROCESS START* (light blue) | *Pre-requisites:*<br>• The statement has been sent (see [Send the Statement](#621-send-the-statement)).<br>*Responsibility:*<br>• Collections Officer |
| 1. *Check* the delivery message. `[Statement Distribution VG-08]` | Read the message D365 shows after the statement is generated, and check that it confirms the statement was sent. |
| 2. *Check* the Collections sent mailbox. `[Statement Distribution VG-09]` | Optional. Where required, check that the statement appears in the Collections sent mailbox. Otherwise, go to step 3. |
| 3. *Confirm* the statement was delivered. `[Statement Distribution VG-10]` | If the delivery message or mailbox shows that the statement was not sent, follow the failed-delivery process. |
| *PROCESS COMPLETE* (light green) | *Outcomes:*<br>• The statement has been sent to the customer and its delivery confirmed. `[Statement Distribution VG-11]` |

> **Note:** Legacy 230 (v2.3, 1 Send Customer Statement (ad hoc)) sends ad hoc statements only, because monthly statements go out automatically on the 5th. It sets **Date interval** and **Balance other than zero**, and runs the send as a batch job with a future start time and **Maximum retries** set to 0, or the customer can receive several copies. It warns that a blank **Records to include** sends statements to every customer, and only email contacts with **Purpose** = **Business** receive statements. `[G230-12]`

### 7. Resolve the Account

##### Description

The **Action / Resolution** stage in the Collections process captures potential steps taken to resolve an outstanding customer balance following contact and activity review. Depending on the outcome, the **Collections Officer** may choose one or more of the following resolution of actions.

##### Responsibility

The **Collections Officer** is responsible for determining the appropriate resolution action based on customer response and account status. They execute or initiate the relevant process in D365 F&O and must ensure that all actions are documented through customer activity records.

The **Group Billing & Credit Manager** is responsible for reviewing and approving any debt write-off requests and ensuring compliance with WiseTech’s credit control policies.

##### Initiation

This process is initiated following customer contact and review of the account’s aged balance and activity history. Actions are taken based on the outcome of customer communication. E.g., when a customer requests supporting documents, disputes a charge, or fails to make payment.

##### Topic Overview

This topic includes these steps:

| Step | Description |
|---|---|
| [View and Download a Customer Invoice](#71-view-and-download-a-customer-invoice) | Open an invoice copy and download it as a PDF. |
| [Create and Send a Collection Letter](#72-create-and-send-a-collection-letter) | Generate and issue a formal collection letter. Only required if automation fails. |
| [Change Customer Status](#73-change-customer-status) | Update the customer's account status, or exclude the customer or a transaction from credit management. |
| [Write Off an Uncollectible Debt](#74-write-off-an-uncollectible-debt) | Initiate and process the write-off once management approval has been obtained. |

> **Note:** Settling and unsettling customer accounts, transferring open or closed payments, and writing off bank fees or small residuals are in **221 Customer Payment Corrections** (topics 1, 2, 3 and 6).

#### 7.1 View and Download a Customer Invoice

##### Description

Use this topic to open a customer invoice and, when you need a copy, download it as a PDF. You highlight the invoice transaction, open its **Original document**, review the invoice in **Print preview** and then download it with a file name that identifies the customer and invoice.

##### Responsibility

- Collections Officer: retrieves and reviews customer invoices.

##### Initiation

- A customer or colleague needs a copy of an invoice, or the invoice must be reviewed before contacting the customer.

##### Topic Overview

This topic includes these steps:

| Step | Description |
|---|---|
| [Open the Invoice Preview](#711-open-the-invoice-preview) | Highlight the invoice transaction and open the invoice in Print preview. Output: the invoice is shown on screen. |
| [Download the Invoice as PDF](#712-download-the-invoice-as-pdf) | Optional. Download the invoice as a PDF with a meaningful file name. Output: a PDF copy of the invoice. |

#### 7.1.1 Open the Invoice Preview

##### Procedure

Complete these steps to open the invoice in print preview:

| **Action** | **Description** |
|---|---|
| *PROCESS START* (light blue) | *Pre-requisites:*<br>• Access to D365 and to the customer account.<br>• The customer account and the invoice you need.<br>*Responsibility:*<br>• Collections Officer |
| 1. *Check* the **Entity**. | Confirm you are signed into the correct **Legal Entity** (top-right). |
| 2. *Open* the customer's transactions. `[Customer Invoices VG-01]` | Open the transactions for the customer account, for example from **All customers** in your **Favorites**. |
| 3. *Click* the invoice transaction. `[Customer Invoices VG-02]` | Click the row for the invoice so it is highlighted. |
| 4. *Click* **Original document**. `[Customer Invoices VG-03]` | Open the original document for the highlighted transaction. |
| 5. *Select* the invoice. `[Customer Invoices VG-04]` | Select the invoice in the list of original documents. |
| 6. *Click* **Print preview**. `[Customer Invoices VG-05]` | The invoice opens in print preview. |
| 7. *Confirm* it is the invoice you need. `[Customer Invoices VG-06]` | Review the invoice information in the preview and check that it is the invoice you selected. |
| *STEP COMPLETE* (light blue) | • The invoice is open in print preview.<br>• Continue to [Download the Invoice as PDF](#712-download-the-invoice-as-pdf) |

#### 7.1.2 Download the Invoice as PDF

##### Procedure

This subprocedure is optional. Complete it when you need a copy of the invoice, for example to send to a customer. If you only needed to review the invoice, the task is complete.

Complete these steps to download the invoice as a PDF:

| **Action** | **Description** |
|---|---|
| *PROCESS START* (light blue) | *Pre-requisites:*<br>• The invoice is open in print preview (see [Open the Invoice Preview](#711-open-the-invoice-preview)).<br>*Responsibility:*<br>• Collections Officer |
| 1. *Download* the invoice as a PDF. `[Customer Invoices VG-07]` | From the print preview, download the invoice as a PDF file. |
| 2. *Enter* a meaningful file name. `[Customer Invoices VG-08 / VG-10]` | Name the file so the customer and the invoice can be identified. |
| 3. *Save* the PDF. `[Customer Invoices VG-09]` | Save the PDF file. |
| 4. *Confirm* the PDF shows the correct invoice. | Open the PDF and check that it shows the invoice you selected. |
| *PROCESS COMPLETE* (light green) | *Outcomes:*<br>• The invoice is saved as a PDF with a file name that identifies the customer and invoice. `[Customer Invoices VG-21]` |

> **Note:** Legacy 230 (v2.3, 6.1 Resend Statement or Invoice) reaches the invoice copy from **Open customer invoices** or the **Tax invoice journal** > **Document** > **View** > **Copy preview**, and also covers resending the invoice to the customer. `[G230-13]`

#### 7.2 Create and Send a Collection Letter

##### Procedure

Complete the steps below to Create & Send Collection Letter:

| **Action** | **Description** |
|---|---|
| *PROCESS START* | **Pre-requisite:**<br>1. *The customer must have overdue invoices requiring a collection letter and a valid recipient email address set to Purpose = Business. Manual processing is only required if automated collection letter processing fails.* |
| 2. *Check* the **Entity**. | Confirm you are signed into the correct **Legal Entity** (top-right). |
| 3. *Click* **Modules**. | From the left-hand **Navigation Pane**, click **Modules**. |
| 4. *Navigate* to the **Create Collection Letter** page. | From the **Navigation Pane**, *select*:<br>5. **Credit and Collections** ><br>6. **Collection Letter** ><br>7. **Create Collection Letter.** |
| 8. *Populate* the **Create Collection Letter** form. | Enter the required fields: |
| 9. *Click* **OK**. | The system will process and generate the collection letter. |
| 10. *Navigate* to the **Review and Process Collection Letters** page. | From the **Navigation Pane**, *select*:<br>11. **Modules** ><br>12. **Credit and Collections** ><br>13. **Collection Letter** ><br>14. **Review and Process Collection Letters.** |
| 15. *Select* the relevant **Collection Letter/s**. | *Click* the checkbox to the left for one or more collection letters. |
| 16. *Click* **Post**. | This will open the **Post collection letter note** form. |
| 17. *Click* **OK**. | This will post the collection letter. |
| 18. *Click* **Collection letter note**. | On the Main Toolbar, *click* **Print** > **Collection letter note**. |
| 19. *Set* **Use print management destination** to **Yes**. | This will apply the specific print management settings that have been configured for the customer, and output has been automated. |
| 20. *Click* **OK**. | Once completed, the collection letter will be generated and delivered according to the output selection. |
| 21. *Send* the **Collection Letter** to **the Customer**. | Export the collection letter as a .PDF file and send it to the customer using Outlook. |
| *PROCESS COMPLETE* | **Outcomes***:*<br>22. *Collection letters are successfully generated and issued to the customers.*<br>23. *Collection letter delivery settings are applied correctly.*<br>24. *Customers receive formal overdue payment notifications.* |

#### 7.3 Change Customer Status

##### Procedure

Complete the steps below to Change Customer Status:

| **Action** | **Description** |
|---|---|
| *PROCESS START* | **Pre-requisite:**<br>1. *The customer account must exist in D365 F&O, and the required account status and reason for the change must be confirmed before updating the record.* |
| 2. *Check* the **Entity**. | Confirm you are signed into the correct **Legal Entity** (top-right). |
| 3. *Click* **Modules**. | From the left-hand **Navigation Pane**, click **Modules**. |
| 4. *Navigate* to the **All Customers** page. | From the **Navigation Pane**, *select*:<br>5. **Credit and Collections** ><br>6. **Customers** ><br>7. **All Customers.** |
| 8. *Select* the relevant **Customer**. | In the **Account** field, enter or search for the customer whose account status needs to be changed.<br>*Click* the **Account** hyperlink to open the customer record. |
| 9. *Enable* **Edit** in the **Account Status** field. | Under the **Credit and collections** FastTab, *hover* over the **Account** **status** field. When the pencil (edit) icon appears, *click* the **Edit** icon to enable editing. |
| 10. *Select* the new **Account Status**. | From the **Account** **status** drop-down list, select the most relevant status based on the customer’s condition.<br>Typical options include:<br>11. *Account on Hold* – used when further invoicing or delivery should be paused.<br>12. *Collection Agency* – used when the debt has been referred to an external collection agency.<br>13. *Legal Process* – used when legal action is underway. |
| 14. *Select* the **Account Status Reason**. | In the **Account** **status** reason drop-down, *select* the appropriate reason for the change (e.g., Bad Debt, Account Dispute, Insolvency Issue). |
| 15. *Verify* **dependent fields**. | Check that the **Confirmation**, **Delivery**, and **Invoicing** fields have been automatically updated based on the selected account status. This ensures that business rules tied to that status are enforced. |
| 16. *Click* **Save**. | On the Main Toolbar, *click* **Save** to apply the change. |
| 17. [Record Customer Activity.](#5-record-a-customer-collection-activity) | Go to **General** > **Activities** > **Activities** > **All Activities**.<br>*Click* **+ New,** select **Action**, and record details. |
| 18. *Notify* relevant **Stakeholders**. | Send an **email** or **Teams** message to the **Group Billing and Credit Manager** or **Finance team** to inform them of the account status change. Include:<br>19. Customer name and account number<br>20. New account status and reason<br>21. Summary of actions taken<br>22. Reference to the activity note created. |
| 23. *Update* **Local systems**  (if applicable). | Where applicable, notify the operational or billing team to block the customer account in local systems, ensuring the hold is enforced consistently across platforms. |
| 24. *Confirm* **Completion**. | Ensure the customer’s account now reflects the correct status and that relevant parties have acknowledged the change.<br>**Note:** *ensure to document this in the Customer Activity record.* |
| *OPTIONAL:* Add visibility to the customer list view. | On the **All customers** grid, right-*click* the column header and select Insert columns. Add:<br>25. **Account status**,<br>26. **Account status reason**, then<br>27. *Click* **Update**.<br>These columns will display directly on the All Customers grid, allowing for quick visibility of customers on hold or in collection. |
| 28. *OPTIONAL*<br>*Exclude* **Customer from Credit Management** | If the customer should not be included in automated collection activities or Direct Debit processing, navigate to the Customer record.<br>From the Navigation pane, select:<br>29. **Modules** ><br>30. **Credit and collections** ><br>31. **Customers** ><br>32. **All** **customers** |
| 33. *Search* for the **Customer**. | In the Customer account field, enter or search for the customer account requiring exclusion for collections processing.<br>*Click* the **account** **hyperlink** to open the customer record |
| 34. *Open* the **Credit and collections fasttab***.* | *Scroll* down and *expand* the **Credit and collections** fasttab. |
| 35. *Enable* **Exclude from Credit Management.** | In the Credit and collections fasttab, *click* the **Exclude from credit management** checkbox. |
| 36. *Click* **Save***.* | To apply the update to the customer account. |
| 37. *OPTIONAL* `[G230-03]`<br>*Exclude* **Transaction from Credit Management.** | If a specific invoice or transactions should not be included in automated collection activities or Direct Debit processing, navigate to the customer transaction page for the customer account being reviewed.<br>From the customer record, on the Main Toolbar, select **Customer > Transactions > Transactions**. |
| 38. *Review* the **Customer** **transactions**. | *Locate* and *review* the **transaction requiring exclusion** **from** **collections processing**. Confirm the invoice number, outstanding balance and transactions are correct before continuing. |
| 39. *Enable* **Exclude from Credit management.** | On the transaction line, *locate* the **Exclude from credit management** column and *click* the **checkbox** for the required transaction.<br>This setting excludes the transaction from automated collections letters and automated credit management processing activities. |
| *PROCESS COMPLETE* |   |

#### 7.4 Write Off an Uncollectible Debt

##### Procedure

Complete the steps below to Write-off Debt:

| **Action** | **Description** |
|---|---|
| *PROCESS START* | **Pre-requisites:**<br>*When all reasonable collection efforts have failed, send a Debt Write-off Request to the Group Billing & Credit Manager via Outlook email. Include:*<br>1. *customer account,*<br>2. *outstanding balance,*<br>3. *collection history summary, and*<br>4. *justification for the write-off.*<br>*The Group Billing & Credit Manager reviews the request and determines write-off eligibility. If approved, Group Billing & Credit Manager will complete the below steps.* |
| 5. *Check* the **Entity**. | Confirm you are signed into the correct **Legal Entity** (top-right). |
| 6. *Click* **Modules**. | From the left-hand **Navigation Pane**, click **Modules**. |
| 7. *Navigate* to the **Aged Balances** page. | From the **Navigation Pane**, *select*:<br>8. **Credit and Collections** ><br>9. **Collections** ><br>10. **Aged balances.** |
| 11. *Select* the relevant **Customer**. | In the **Account** field, enter or search for the customer account.<br>*Click* the **Account** hyperlink to open the customer record. |
| 12. *Review* the **Outstanding Balance**. | Verify the **Overdue Transactions** to confirm the correct amount and ensure it aligns with the approved write-off value. |
| 13. *Navigate* to **Open Transactions**. | From the customer record, *click* **Open** transactions to view the individual invoices or balances eligible for write-off. |
| 14. *Select* **Transactions** to write off. | Select the specific **Invoice/s** or **Transaction/s** to be written off. Ensure that only the approved amounts are selected. |
| 15. *Click* **Write-off**. | On the toolbar, *click* **Write-off**. |
| 16. *Enter* **Write-off details.** | In the **Write-off Details** window, complete the required fields:<br>17. Write-off date – Enter the date of approval.<br>18. Reason code – Select the appropriate reason (e.g., Bad Debt, Unrecoverable, Customer Bankrupt, Over/Short). |
| 19. *Verify* **Posting Details**. | Review that the correct main account and offset account for write-off are applied based on configuration. If required, update the posting layer or dimension. |
| 20. *Confirm* **the Write-off**. | *Click* **OK** to post the write-off journal. |
| 21. *Review* the **Write-off Journal**. | Navigate to **General Ledger** > **Journal** **entries** > **General Journals**.<br>Open the newly created write-off journal and verify that the debit and credit entries are balanced and posted correctly. |
| 22. *Validate* the **Journal.** | On the Main **T**oolbar, *click* **Validate** > **Simulate** **posting** to confirm there are no errors.<br>If validation errors are displayed, review the error message, correct the issue, and repeat validation before continuing. |
| 23. [Record the Write-off activity.](#5-record-a-customer-collection-activity) | Navigate to **Modules** > **Credit** **&** **Collections** > **Customers** > **All** **customers**.<br>Search for and open the relevant **Customer** **account**.<br>From the customer page, on the Main Toolbar, go to **General** > **Activities** > **Activities** > **All activities**.<br>*Click* **+ New**, select Action (Type), and record:<br>24. **Purpose**: Debt Write-off approved<br>25. **Description**: $X written off on [date] due to [reason] for the write-off.<br>*Click* Save to record the activity.<br>Note: The write-off activity must be recorded before submitting the journal for approval to ensure the request is documented and auditable. |
| 26. *Submit* the **Journal** for **Approval**. | On the Main Toolbar, *click* **Approval** > **Report** **as** **ready**.<br>The journal has been submitted for approval. The approver will receive a notification to review and approve the journal. Once approved, notification is sent confirming approval. |
| 27. *Notify* **Stakeholders**. | Email or message the relevant stakeholders confirming the write-off completion. |
| *PROCESS COMPLETE* |   |

### 8. Update and Close a Customer Activity

##### Description

Updating and closing customer activity in **D365 F&O** ensures that all collection tasks and interactions are accurately finalized and recorded for audit and reporting purposes. Once a customer's query or collection action has been resolved, the **Collections Officer** must update the corresponding activity record to reflect the outcome and mark it as complete.

Each activity update should include:

**Resolution details** summarize the outcome of the activity (e.g., payment received, collection letter sent, account on hold).

**Supporting attachments**, such as confirmation emails, payment receipts, or correspondence.

**Completion status**, confirming that no further follow-up is required.

It is a **mandatory requirement** to attach any relevant supporting documents—such as emails or evidence of resolution—to the activity record before closure.This ensures all collection activities are fully documented, traceable, and compliant with audit and recordkeeping requirements.

##### Responsibility

The **Collections Officer** is responsible for reviewing, updating, and closing customer activity records once the related action has been completed. They must ensure that the activity accurately reflects the outcome and that all supporting documentation is attached in **D365 F&O** before marking the activity as complete. Failure to close activities or attach relevant evidence may result in incomplete records and reduced visibility of customer resolution history.

##### Initiation

This process is initiated **after completing any collection-related action** (e.g., sending a collection letter, confirming payment, changing customer status, or processing a write-off). Closing the activity ensures that all actions taken are finalized in **D365 F&O**, maintaining accurate and up-to-date records of customer interactions and collection outcomes.

**Procedure**: Follow the steps on the next page to execute this task in-system.

##### Procedure

Complete the steps below to Update & Close Customer Activity:

| **Action** | **Description** |
|---|---|
| *PROCESS START* | **Pre-requisite:**<br>1. *The customer account must exist in D365 F&O, and the required account status and reason for the change must be confirmed before updating the record.* |
| 2. *Check* the **Entity**. | Confirm you are signed into the correct **Legal Entity** (top-right). |
| 3. *Click* **Modules**. | From the left-hand **Navigation Pane**, click **Modules**. |
| 4. *Navigate* to the **All Customers** page. | From the **Navigation Pane**, *select*:<br>5. **Modules** ><br>6. **Credit and Collections** ><br>7. **Customers** ><br>8. **All Customers.** |
| 9. *Select* the relevant **Customer**. | In the **Customer** account field, enter or search for the customer whose account status needs to be changed.<br>*Click* the **Account number** to open the customer record. |
| 10. *Navigate* to **All Activities > Record Event.** | From the **Main Toolbar**, *select*:<br>11. **General** ><br>12. **Activities** ><br>13. **Activities** ><br>14. **All Activities**.<br>A list of customer activities will be displayed. |
| 15. *Select* the relevant **Activity** from the list. | Identify and open the activity to be updated and closed. |
| 16. *Populate* the **Resolution** section. | Enter the outcome or resolution details, such as payment received, collection letter sent, or debt written off. Ensure all notes are clear and concise. |
| 17. *Attach* **Supporting Documentation**. | Upload any relevant attachments (e.g., confirmation emails, invoices, or correspondence) to the activity record before closure. |
| 18. *Click* **Set as complete**. | Mark the activity as complete to close it. The activity will move from an active to a closed status. |
| *PROCESS COMPLETE* | The customer activity is now closed and recorded as part of the collection's history. |

---

## Part 3: Reports (Collections)

##### Page Overview

This page contains various reports related to the **Credit Collections process**. `[G230-14]`

##### Customer Ageing Report

| **Navigation** | **Description** |
|---|---|
| 1. **Credit and Collections** *>*<br>2. **Enquiries and reports** *>*<br>3. **Customers** *>*<br>4. **Customer ageing report***.* | The Customer aging report displays the balances that are due from customers, sorted by date interval, or aging period. |

##### Customer Report

| **Navigation** | **Description** |
|---|---|
| 1. **Credit and Collections** *>*<br>2. **Enquiries and reports** *>*<br>3. **Customers** *>*<br>4. **Customer report***.* | The customer report displays detailed insights on customer data such as contact information, purchasing history, and payment details. |

##### Customer Balance list

| **Navigation** | **Description** |
|---|---|
| 1. **Credit and Collections** *>*<br>2. **Enquiries and reports** *>*<br>3. **Customers** *>*<br>4. **Customer balance list report***.* | The customer balance list report displays side by side customer balances for the defined periods. This report helps you quickly analyses changes in accounts receivable. |

##### Customer Account Statement

| **Navigation** | **Description** |
|---|---|
| 1. **Credit and Collections** *>*<br>2. **Enquiries and reports** *>*<br>3. **Customers** *>*<br>4. **Customer account statement.** | The customer statement outlines a customer’s financial transactions over a certain period and highlights the current outstanding balance. |

---

## Additional Resources

The standard template block, unchanged.
