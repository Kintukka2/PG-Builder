# D365 F&O: Vendor Invoices (NZ) Procedure Guide

> **WORKING DRAFT. Not validated or approved.**
>
> This is a Markdown preview of the Word guide [`CLAUDE-TBC-Vendor Invoices PG v1.0.docx`](CLAUDE-TBC-Vendor%20Invoices%20PG%20v1.0.docx). It converts legacy version 0.2 (January 2025) to the PG master template (D-057). **The Word file is the editable source.**
>
> Markers such as `[VI-05]` show unconfirmed items. In the Word file, each one is a review comment. The items are in the [validation register](../03-validation/Vendor-Invoices-v1.0-Validation.md). The markers are not part of the guide text.

The fixed template content is not repeated here: cover, Contents, *About this guide* and *Additional Resources*.

**Version history**

| **ID** | **Date** | **Author/s** | **BPO** | **Description of change** |
|---|---|---|---|---|
| 0.2 | January 2025 | Michael Thurlow | Ghada Boulos | Version 0.2 (NZ), released 30 January 2025, in the earlier PG format. |
| 1.0 | November 2026 | Daniel Moreira | Ghada Boulos `[VI-02]` | Working draft (D-057): converted from version 0.2 to the PG master template. Topics grouped into four, one action per row, the standard navigation pattern, and each report in its own table. Not validated or approved. `[VI-01]` |

---

## Part 1: What do I need to know? (Vendor Invoices)

### High-level process

##### Part Description

**Vendor Invoices** is part of the Purchase-to-Pay (P2P) stream. This guide sets out the D365 F&O procedures that the Accounts Payable team uses to create, submit and post vendor invoices for New Zealand. `[VI-03]`

Vendors send their invoices by email to **apanz@wisetechglobal.com**. For each invoice, the Accounts Payable Specialist searches D365 F&O for the purchase order that the invoice relates to. If an existing purchase order is located, the vendor invoice is created from the purchase order and matched against it. If no purchase order can be located, a manual vendor invoice is created. The invoice file received by email is then attached to the invoice in D365 F&O.

Every vendor invoice is submitted to the workflow, regardless of its amount; the workflow notifies Treasury of any amount over $100,000. When the workflow status is **Completed**, the invoice is posted. If the invoice is still displayed on the **Pending vendor invoices** page after posting, its purchase order is confirmed.

At a high level, the Vendor Invoices process follows these stages:

- **Create a Vendor Invoice**: search for the purchase order, create the invoice from it or manually, and attach the invoice file.
- **Submit a Vendor Invoice to the Workflow**: submit every invoice, and check that its workflow status is **Completed**.
- **Post a Vendor Invoice**: post the invoice from the **Pending vendor invoices** page.
- **Confirm a Purchase Order**: confirm the purchase order when a posted invoice is still displayed on the **Pending vendor invoices** page.

This guide covers the new D365 F&O activities only; existing business-as-usual (BAU) activities are not included. The other process areas of the P2P stream are Vendor Onboarding and Maintenance (Accounts Payable), Purchase Requisitions (Business User / Requestor) and Vendor Payments (Accounts Payable). `[VI-21]`

##### Initiation

- A vendor sends an invoice to **apanz@wisetechglobal.com**. `[VI-06]`

##### Stream

| **Stream** | **Process Area** | **Key Roles** |
|---|---|---|
| Purchase-to-Pay (P2P) `[VI-04]` | Vendor Invoices | • Accounts Payable Specialist `[VI-05]` |

##### Process

The high-level Vendor Invoices process is as follows:

| **#** | **Action** | **Who** | **When** | **Where** |
|---|---|---|---|---|
| **0** | Send a vendor invoice to **apanz@wisetechglobal.com** | Vendor | Ad hoc | Email |
| **1** | [Create a Vendor Invoice](#1-create-a-vendor-invoice) | Accounts Payable Specialist | When a vendor invoice is received `[VI-06]` | D365 F&O |
| **2** | [Submit a Vendor Invoice to the Workflow](#2-submit-a-vendor-invoice-to-the-workflow) | Accounts Payable Specialist | When a vendor invoice is created in D365 F&O | D365 F&O |
| **3** | [Post a Vendor Invoice](#3-post-a-vendor-invoice) | Accounts Payable Specialist | When the workflow status is **Completed** | D365 F&O |
| **4** | [Confirm a Purchase Order](#4-confirm-a-purchase-order) | Accounts Payable Specialist | When a posted invoice is still displayed on the **Pending vendor invoices** page | D365 F&O |

### Roles and responsibilities

##### Overview

The Accounts Payable Specialist creates vendor invoices, attaches the invoice files, submits the invoices to the workflow and posts them, and confirms a purchase order when an invoice stays pending. Vendors send their invoices to the Accounts Payable mailbox, and the workflow notifies Treasury of any amount over $100,000. `[VI-05]`

| **Tasks / Business Roles** | **Accounts Payable Specialist** |
|---|---|
| 1 [Create a Vendor Invoice](#1-create-a-vendor-invoice) | R |
| 1.1 [Search for an Existing Purchase Order](#11-search-for-an-existing-purchase-order) | R |
| 1.2 [Create a Vendor Invoice from a Purchase Order](#12-create-a-vendor-invoice-from-a-purchase-order) | R |
| 1.3 [Create a Manual Vendor Invoice](#13-create-a-manual-vendor-invoice) | R |
| 1.4 [Add an Attachment to a Vendor Invoice](#14-add-an-attachment-to-a-vendor-invoice) | R |
| 2 [Submit a Vendor Invoice to the Workflow](#2-submit-a-vendor-invoice-to-the-workflow) | R |
| 3 [Post a Vendor Invoice](#3-post-a-vendor-invoice) | R |
| 4 [Confirm a Purchase Order](#4-confirm-a-purchase-order) | R |

\*R = Responsible

> **Note:** The business roles shown above are responsible for completing D365 F&O tasks on a day-to-day basis; however, other business roles may also have access to the same functionality to complete these tasks when required.

### Key concepts

##### Overview

Before you start, you need to know how a vendor invoice is linked to a purchase order, which type of invoice to create, what the match status shows, and what the workflow does.

##### Purchase Orders and Requisitions

| **Term** | **Description** |
|---|---|
| **Purchase order number** | The vendor invoice provides the purchase order number. Use it to find the purchase order in D365 F&O. |
| **Purchase requisition** | The Accounts Payable Specialist finds the purchase order from the **All purchase requisitions** page. The **Purchase order** field on the **Purchase requisition lines** shows the purchase order number. `[VI-07]`<br>The purchase requisition status should be **Closed**. `[VI-08]` |

##### Vendor Invoice Types

| **Invoice type** | **When it is used** |
|---|---|
| **Vendor invoice from a purchase order** | A physical invoice is received from a vendor and an existing purchase order is located in D365 F&O: a purchase order number is shown in the **Purchase order** field. See [1.2 Create a Vendor Invoice from a Purchase Order](#12-create-a-vendor-invoice-from-a-purchase-order). |
| **Manual vendor invoice** | A physical invoice is received from a vendor and an existing purchase order cannot be located in D365 F&O: the **Purchase order** field is blank. See [1.3 Create a Manual Vendor Invoice](#13-create-a-manual-vendor-invoice). |

##### Match Status

| **Status** | **What to do** |
|---|---|
| **Not performed** | Shown after the invoice details are entered, before the match status is updated. |
| **Passed** | Save the invoice and continue. |
| **Failed** | Open the **Matching details** to find the reason for the failure, and correct the invoice before you continue. `[VI-11]` |

##### Vendor Invoice Workflow

| **Rule** | **Description** |
|---|---|
| **Submit every invoice** | All vendor invoices must be submitted to the workflow, regardless of the amount. |
| **Treasury notification** | The workflow notifies Treasury of any amount over $100,000. `[VI-14]` |
| **Completed status** | The workflow status must be **Completed** before the invoice is posted. Check it in **Workflow** > **Workflow history**. |

##### Pending Vendor Invoices

| **Term** | **Description** |
|---|---|
| **Pending vendor invoices page** | Lists the existing pending vendor invoices. A posted invoice is no longer displayed on this page. |
| **Invoice still displayed after posting** | Confirm its purchase order: see [4 Confirm a Purchase Order](#4-confirm-a-purchase-order). `[VI-15]` |

---

## Part 2: How do I do it? (Vendor Invoices)

### 1. Create a Vendor Invoice

##### Description

A vendor invoice is created in D365 F&O for each invoice that a vendor sends to **apanz@wisetechglobal.com**. The Accounts Payable Specialist first searches for the purchase order that the invoice relates to. If an existing purchase order is located, the invoice is created from the purchase order and its match status is updated; if not, a manual vendor invoice is created. In both cases, the invoice file received by email is attached to the invoice, which is then ready to submit to the workflow.

##### Responsibility

- Accounts Payable Specialist: creates the vendor invoice and attaches the invoice file. `[VI-05]`

##### Initiation

- A vendor invoice is received in the **apanz@wisetechglobal.com** mailbox.

##### Topic Overview

This topic includes these steps:

| **Step** | **Description** |
|---|---|
| [1.1 Search for an Existing Purchase Order](#11-search-for-an-existing-purchase-order) | Find the purchase order number on the purchase requisition, to decide which type of invoice to create. |
| [1.2 Create a Vendor Invoice from a Purchase Order](#12-create-a-vendor-invoice-from-a-purchase-order) | Used when an existing purchase order is located. Output: a saved vendor invoice with an updated match status. |
| [1.3 Create a Manual Vendor Invoice](#13-create-a-manual-vendor-invoice) | Used when no purchase order can be located. Output: a saved manual vendor invoice. |
| [1.4 Add an Attachment to a Vendor Invoice](#14-add-an-attachment-to-a-vendor-invoice) | Attach the invoice file received by email. Output: a vendor invoice ready to submit to the workflow. |

#### 1.1 Search for an Existing Purchase Order

##### Procedure

Complete these steps to search for an existing purchase order:

| **Action** | **Description** |
|---|---|
| *PROCESS START* | *Pre-requisites:*<br>• The vendor invoice received by email, with the purchase order number it provides.<br>*Responsibility:*<br>• Accounts Payable Specialist |
| 1. *Check* the **Entity**. | Confirm you are signed into the correct **Legal Entity** (top-right). |
| 2. *Click* **Modules**. | From the left-hand **Navigation Pane**, click **Modules**. |
| 3. *Navigate* to the **All purchase requisitions** page. | From the **Navigation Pane**, *select*:<br>• **Procurement and sourcing >**<br>• **Purchase requisitions >**<br>• **All purchase requisitions**<br>The **All purchase requisitions** page opens and displays a list of existing purchase requisitions. |
| 4. *Select* the **Purchase Requisition**. | Click the purchase requisition for the vendor invoice. `[VI-07]`<br>The purchase requisition status should be **Closed**. `[VI-08]`<br>The **Purchase requisitions** page opens. |
| 5. *Check* the **Purchase order** column. | Under **Purchase requisition lines**, check that the **Purchase order** column is displayed.<br>If it is displayed, go to step 11. If it is not displayed, continue with step 6. `[VI-09]` |
| 6. *Right-click* the line header. | Right-click anywhere on the line header of **Purchase requisition lines**. |
| 7. *Click* **Insert columns**. | Click **Insert columns**. |
| 8. *Select* **Purchase order**. | In the list of fields, select **Purchase order**. |
| 9. *Click* **Update**. | Click **Update** to add the **Purchase order** field to the line. |
| 10. *Move* the **Purchase order** column. | Optional: click and drag the **Purchase order** field to the location you want. |
| 11. *Locate* the **Purchase Order** number. | Under **Purchase requisition lines**, locate the purchase order number in the **Purchase order** field. `[VI-22]`<br>**Tip:** Use the purchase order number provided on the vendor invoice.<br>*[Screenshot: Purchase requisition lines showing the Purchase order column with a purchase order number]* |
| *STEP COMPLETE* | • If a purchase order number is shown in the **Purchase order** field, an existing purchase order is located. Continue to [1.2 Create a Vendor Invoice from a Purchase Order](#12-create-a-vendor-invoice-from-a-purchase-order).<br>• If the **Purchase order** field is blank, no purchase order can be located. Continue to [1.3 Create a Manual Vendor Invoice](#13-create-a-manual-vendor-invoice). |

#### 1.2 Create a Vendor Invoice from a Purchase Order

##### Procedure

Complete these steps to create a vendor invoice from a purchase order:

| **Action** | **Description** |
|---|---|
| *PROCESS START* | *Pre-requisites:*<br>• The purchase order number is shown on the purchase requisition lines ([1.1 Search for an Existing Purchase Order](#11-search-for-an-existing-purchase-order)).<br>• The vendor invoice, with its invoice number, description and date.<br>*Responsibility:*<br>• Accounts Payable Specialist |
| 1. *Click* the **Purchase Order** number. | Under **Purchase requisition lines**, click the purchase order number in the **Purchase order** field.<br>The **Purchase order** page opens. |
| 2. *Click* **Invoice** > **Generate** > **Invoice**. | On the **Main Toolbar**, click **Invoice** > **Generate** > **Invoice**.<br>The invoice is generated and the **Vendor invoice** page opens. |
| 3. *Select* **Default from**. | On the **Main Toolbar**, set **Default from** to **Ordered quantity**. `[VI-10]`<br>*[Screenshot: Default from list on the Vendor invoice page, showing the Default quantity for lines options]* |
| 4. *Click* **OK**. | The default quantity is updated according to the selection. |
| 5. *Enter* **Number**. | Enter the invoice number from the vendor's invoice. |
| 6. *Enter* **Invoice description**. | Enter the invoice description from the vendor's invoice. |
| 7. *Enter* **Invoice date**. | Enter the invoice date from the vendor's invoice.<br>**Note:** The **Match status** shows **Not performed**.<br>*[Screenshot: Match status field showing Not performed]* |
| 8. *Click* **Update match status**. | On the **Main Toolbar**, click **Update match status**. The **Match status** is updated.<br>If the **Match status** is **Passed**, go to step 11.<br>If the **Match status** is **Failed**, go to step 9. |
| 9. *Click* **Review** > **Matching** > **Matching details**. | On the **Main Toolbar**, click **Review** > **Matching** > **Matching details**.<br>**Note:** If **Review** is not visible on the **Main Toolbar**, click the ellipsis (**...**).<br>The **Invoice matching details** page opens.<br>*[Screenshot: Invoice matching details page comparing the invoice and purchase order unit price]* |
| 10. *Review* the **Matching Details**. | Review the available details to find the reason for the failure, and correct the invoice as required before you continue. `[VI-11]` |
| 11. *Click* **Save**. | On the **Main Toolbar**, click **Save**. The changes are saved. |
| 12. *Click* **Back**. | On the **Main Toolbar**, click **Back** (arrow). You return to the **Vendor invoice** page. `[VI-12]` |
| *STEP COMPLETE* | • The vendor invoice is created from the purchase order and saved.<br>• Continue to [1.4 Add an Attachment to a Vendor Invoice](#14-add-an-attachment-to-a-vendor-invoice). |

#### 1.3 Create a Manual Vendor Invoice

##### Procedure

Complete these steps to create a manual vendor invoice:

| **Action** | **Description** |
|---|---|
| *PROCESS START* | *Pre-requisites:*<br>• No purchase order can be located: the **Purchase order** field is blank ([1.1 Search for an Existing Purchase Order](#11-search-for-an-existing-purchase-order)).<br>• The vendor invoice, with its vendor, invoice number, description, date and line details.<br>*Responsibility:*<br>• Accounts Payable Specialist `[VI-05]` |
| 1. *Check* the **Entity**. | Confirm you are signed into the correct **Legal Entity** (top-right). |
| 2. *Click* **Modules**. | From the left-hand **Navigation Pane**, click **Modules**. |
| 3. *Navigate* to the **Pending vendor invoices** page. | From the **Navigation Pane**, *select*:<br>• **Accounts payable >**<br>• **Invoices >**<br>• **Pending vendor invoices**<br>The **Pending vendor invoices** page opens and displays a list of existing pending vendor invoices. |
| 4. *Click* **New**. | On the **Main Toolbar**, click **New**. The **Vendor invoice** page opens. |
| 5. *Select* **Invoice account**. | Under the **Vendor invoice header** section, select the vendor's invoice account. |
| 6. *Enter* **Number**. | Enter the invoice number from the vendor's invoice. |
| 7. *Enter* **Invoice description**. | Enter the invoice description from the vendor's invoice. |
| 8. *Enter* **Invoice date**. | Enter the invoice date from the vendor's invoice. |
| 9. *Click* **Add line**. | Under **Lines**, click **Add line**. |
| 10. *Select* **Procurement category**. | Select the procurement category, for example **PRIN** > **Printing and Stationery**. `[VI-13]` |
| 11. *Click* **OK**. | Click **OK** to confirm the procurement category. |
| 12. *Enter* **Quantity**. | Enter the quantity, for example **10**. |
| 13. *Select* **Unit**. | Select **Each**. |
| 14. *Enter* **Unit price**. | Enter the unit price, for example **10**. |
| 15. *Click* **Save**. | On the **Main Toolbar**, click **Save**. The changes are saved. |
| *STEP COMPLETE* | • The manual vendor invoice is saved.<br>• Continue to [1.4 Add an Attachment to a Vendor Invoice](#14-add-an-attachment-to-a-vendor-invoice). |

#### 1.4 Add an Attachment to a Vendor Invoice

##### Procedure

Complete these steps to add an attachment to a vendor invoice:

| **Action** | **Description** |
|---|---|
| *PROCESS START* | *Pre-requisites:*<br>• The vendor invoice is saved and open on the **Vendor invoice** page ([1.2 Create a Vendor Invoice from a Purchase Order](#12-create-a-vendor-invoice-from-a-purchase-order) or [1.3 Create a Manual Vendor Invoice](#13-create-a-manual-vendor-invoice)).<br>• The vendor invoice file received by email.<br>*Responsibility:*<br>• Accounts Payable Specialist `[VI-05]` |
| 1. *Click* **Attachments**. | On the **Main Toolbar**, click **Attachments**. The **Attachments for Vendor invoices** page opens. |
| 2. *Click* **New** > **File**. | On the **Main Toolbar**, click **New** > **File**. The **Upload document** pane opens. |
| 3. *Click* **Browse**. | In the **Upload document** pane, click **Browse**. |
| 4. *Select* the **Vendor Invoice** file. | Locate and select the vendor invoice file.<br>The vendor invoice file is uploaded and displayed in the left-hand pane. |
| 5. *Enter* **Description**. | Optional: update the **Description** as required. |
| 6. *Click* **Save**. | On the **Main Toolbar**, click **Save**. The changes are saved. |
| 7. *Click* **Back**. | On the **Main Toolbar**, click **Back** (arrow). You return to the **Vendor invoice** page. |
| *STEP COMPLETE* | • The vendor invoice file is attached to the vendor invoice.<br>• Continue to [2 Submit a Vendor Invoice to the Workflow](#2-submit-a-vendor-invoice-to-the-workflow). |

### 2. Submit a Vendor Invoice to the Workflow

##### Description

Every vendor invoice is submitted to the workflow, regardless of its amount. The workflow notifies Treasury of any amount over $100,000. The workflow status must be **Completed** before the invoice is posted. `[VI-14]`

##### Responsibility

- Accounts Payable Specialist: submits the vendor invoice to the workflow and checks its status. `[VI-05]`

##### Initiation

- A vendor invoice is created in D365 F&O and its invoice file is attached ([1.4 Add an Attachment to a Vendor Invoice](#14-add-an-attachment-to-a-vendor-invoice)).

##### Procedure

Complete these steps to submit a vendor invoice to the workflow:

| **Action** | **Description** |
|---|---|
| *PROCESS START* | *Pre-requisites:*<br>• The vendor invoice is open on the **Vendor invoice** page, with its invoice file attached ([1.4 Add an Attachment to a Vendor Invoice](#14-add-an-attachment-to-a-vendor-invoice)).<br>*Responsibility:*<br>• Accounts Payable Specialist |
| 1. *Click* **Workflow**. | On the **Main Toolbar**, click **Workflow**. The **Vendor invoice workflow** pop-up appears. |
| 2. *Click* **Submit**. | Click **Submit**. The **Submit** pane opens. |
| 3. *Enter* **Comment**. | Optional: enter a comment, if required. |
| 4. *Click* **Submit**. | In the **Submit** pane, click **Submit**. The vendor invoice is submitted to the workflow. |
| 5. *Click* **Workflow** > **Workflow history**. | On the **Main Toolbar**, click **Workflow** > **Workflow history** to check the status. `[VI-20]`<br>*[Screenshot: Workflow menu open on the Main Toolbar, showing the Workflow history button (user name masked)]* |
| 6. *Confirm* the **Status** is **Completed**. | The workflow status must be **Completed** before you continue. `[VI-14]`<br>*[Screenshot: Workflow history showing the workflow Status as Completed]* |
| *STEP COMPLETE* | • The vendor invoice is submitted to the workflow, and its workflow status is **Completed**.<br>• Continue to [3 Post a Vendor Invoice](#3-post-a-vendor-invoice). |

### 3. Post a Vendor Invoice

##### Description

A vendor invoice is posted once it has been submitted to the workflow and its workflow status is **Completed**. After posting, the invoice is no longer displayed on the **Pending vendor invoices** page. If it is still displayed, its purchase order must be confirmed: see [4 Confirm a Purchase Order](#4-confirm-a-purchase-order).

##### Responsibility

- Accounts Payable Specialist: posts the vendor invoice. `[VI-05]`

##### Initiation

- The workflow status of a vendor invoice is **Completed** ([2 Submit a Vendor Invoice to the Workflow](#2-submit-a-vendor-invoice-to-the-workflow)).

##### Procedure

Complete these steps to post a vendor invoice:

| **Action** | **Description** |
|---|---|
| *PROCESS START* | *Pre-requisites:*<br>• The workflow status of the vendor invoice is **Completed** ([2 Submit a Vendor Invoice to the Workflow](#2-submit-a-vendor-invoice-to-the-workflow)).<br>*Responsibility:*<br>• Accounts Payable Specialist |
| 1. *Check* the **Entity**. | Confirm you are signed into the correct **Legal Entity** (top-right). |
| 2. *Click* **Modules**. | From the left-hand **Navigation Pane**, click **Modules**. |
| 3. *Navigate* to the **Pending vendor invoices** page. | From the **Navigation Pane**, *select*:<br>• **Accounts payable >**<br>• **Invoices >**<br>• **Pending vendor invoices**<br>The **Pending vendor invoices** page opens and displays a list of existing pending vendor invoices. |
| 4. *Select* the **Vendor Invoice**. | Click the vendor invoice. The **Invoice** page opens. |
| 5. *Click* **Post**. | On the **Main Toolbar**, click **Post**.<br>The pop-up message **Processing operation – Purchase invoice** appears. When it is complete, the system message **Operation completed** is displayed and the invoice is posted. |
| 6. *Check* the **Pending vendor invoices** page. | Check whether the invoice is still displayed on the **Pending vendor invoices** page. `[VI-15]`<br>If it is no longer displayed, the invoice is posted.<br>**Note:** The invoice can be viewed under **Accounts payable** > **Purchase orders** > **All purchase orders**, then, on the **Main Toolbar**, click **Invoice** > **Generate** > **Invoice**. `[VI-16]`<br>If it is still displayed, go to [4 Confirm a Purchase Order](#4-confirm-a-purchase-order). |
| *PROCESS COMPLETE* | *Outcomes:*<br>• The vendor invoice is posted and is no longer displayed on the **Pending vendor invoices** page. |

### 4. Confirm a Purchase Order

##### Description

A purchase order is confirmed to enable a vendor invoice to be processed. Confirm the purchase order when a vendor invoice is still displayed on the **Pending vendor invoices** page after it is posted ([3 Post a Vendor Invoice](#3-post-a-vendor-invoice)).

##### Responsibility

- Accounts Payable Specialist: confirms the purchase order. `[VI-05]`

##### Initiation

- A posted vendor invoice is still displayed on the **Pending vendor invoices** page.

##### Procedure

Complete these steps to confirm a purchase order:

| **Action** | **Description** |
|---|---|
| *PROCESS START* | *Pre-requisites:*<br>• A posted vendor invoice is still displayed on the **Pending vendor invoices** page ([3 Post a Vendor Invoice](#3-post-a-vendor-invoice)).<br>• The purchase order number of that invoice.<br>*Responsibility:*<br>• Accounts Payable Specialist |
| 1. *Check* the **Entity**. | Confirm you are signed into the correct **Legal Entity** (top-right). |
| 2. *Click* **Modules**. | From the left-hand **Navigation Pane**, click **Modules**. |
| 3. *Navigate* to the **All purchase orders** page. | From the **Navigation Pane**, *select*:<br>• **Procurement and sourcing >**<br>• **Purchase orders >**<br>• **All purchase orders**<br>The **All purchase orders** page opens and displays a list of existing purchase orders. |
| 4. *Select* the **Purchase Order**. | Click the purchase order. The purchase order opens. `[VI-17]` |
| 5. *Click* **Purchase** > **Actions** > **Confirm**. | On the **Main Toolbar**, click **Purchase** > **Actions** > **Confirm**. The purchase order is confirmed. |
| *PROCESS COMPLETE* | *Outcomes:*<br>• The purchase order is confirmed, so that the vendor invoice can be processed. `[VI-17]` |

---

## Part 3: Reports (Vendor Invoices)

##### Overview

The following D365 F&O standard reports are available in the Accounts Payable module. They show vendor balances, invoices, transactions and purchase spending. For instructions to run a standard report, refer to the **D365 F&O Reports: Run a Standard Report** Quick Reference Card. `[VI-18]`

##### Vendor Ageing Report

| **Navigation** | **Description** |
|---|---|
| • **Accounts payable >**<br>• **Enquiries and reports >**<br>• **Vendor ageing report** | The **Vendor ageing report** shows the balances that are due to vendors. Balances on the report are sorted either by date interval or by ageing period definition. |

##### Purchase Orders Received but Not Invoiced

| **Navigation** | **Description** |
|---|---|
| • **Accounts payable >**<br>• **Purchase orders >**<br>• **Purchase orders received but not invoiced** | This report displays the accrued purchases linked to purchase orders that have been received but not invoiced. It is displayed in a grid, where the transactions can be processed and exported to Microsoft Excel. |

##### Vendor Base Data

| **Navigation** | **Description** |
|---|---|
| • **Accounts payable >**<br>• **Enquiries and reports >**<br>• **Vendor reports >**<br>• **Vendor base data** | This report can be printed for the periodic tax review. It includes the **Tax Group**, **WHT Tax Group**, **Address** (**Location**) and other relevant data fields.<br>Alternatively, the vendor master form can be personalized to include the fields required for the periodic tax review, and then exported to Excel. |

##### Vendor/Item Statistics

| **Navigation** | **Description** |
|---|---|
| • **Procurement and sourcing >**<br>• **Enquiries and reports >**<br>• **Vendor statistics >**<br>• **Vendor/Item statistics** | The **Vendor/Item statistics** report displays a summary of the products purchased from each vendor during the specified date range. A second date range can be added for comparison. |

##### Vendor Transactions Report

| **Navigation** | **Description** |
|---|---|
| • **Accounts payable >**<br>• **Enquiries and reports >**<br>• **Vendor transactions report** | Use this report to print the vendor voucher transactions, that is, the records posted to the Accounts Payable subledger. |

##### Vendor Tax Invoice Journal Report

| **Navigation** | **Description** |
|---|---|
| • **Accounts payable >**<br>• **Enquiries and reports >**<br>• **Invoice >**<br>• **Vendor tax invoice journal report** | Use this report to print a list of vendor invoices. |

##### Vendor Posted Payment Journal Report

| **Navigation** | **Description** |
|---|---|
| • **Accounts payable >**<br>• **Enquiries and reports >**<br>• **Payment >**<br>• **Vendor posted payment journal report** | The **Vendor posted payment journal report** shows the details of posted vendor accounts and vendor payments for individual vendors. It displays the payment amount, original transaction amount, discount amount and write-off amount, with the original transaction currency and the payment currency.<br>The report also displays the type of journal posted, the vendor account, the payment reference, and whether any journal vouchers are canceled. |

##### Purchase and Spend Analysis

| **Navigation** | **Description** |
|---|---|
| • **Procurement and sourcing >**<br>• **Enquiries and reports >**<br>• **Purchase performance analysis >**<br>• **Purchase and spend analysis** | The Purchase spend analysis Power BI content helps purchasing managers, and managers who are responsible for budgets, keep track of purchase spending. Managers can analyze purchase spending by:<br>• Year-to-date purchases (by vendor group and individual vendor, procurement category and individual product, and vendor location).<br>• Year-over-year purchase change (by vendor group and procurement category). |

##### Payment Times Reporting Scheme (PTRS)

| **Navigation** | **Description** |
|---|---|
| • **Accounts payable >**<br>• **Periodic tasks >**<br>• **Statistics on invoices**, then select **Payment times report** | The Australian government established the PTRS to help improve payment times for Australian small businesses. Under the scheme, large businesses and government enterprises must report their small business payment terms and times every six months of an income year. Legal entities must also include payment information about the goods and services they procured from small business suppliers under a trade credit arrangement. `[VI-03]` |

##### Account Statement

| **Navigation** | **Description** |
|---|---|
| • **Accounts payable >**<br>• **Enquiries and reports >**<br>• **Vendor reports >**<br>• **Account statement** | Use this report to print and view internal account statements for each vendor account. Each statement includes basic vendor information, such as the vendor's name, address and terms of payment, and transaction information, such as the transaction date, voucher number, invoice number, due date and amounts. |

##### Vendor to Ledger Reconciliation

| **Navigation** | **Description** |
|---|---|
| • **Accounts payable >**<br>• **Enquiries and reports >**<br>• **Vendor reports >**<br>• **Vendor to ledger reconciliation** | Use this report to reconcile the balances of vendor and ledger accounts. The sum of all vendor transactions is compared with the sum of all the ledger transactions posted to the related vendor summary accounts. You can specify intervals for dates, vouchers and vendor accounts, according to the vendor posting profile. |

##### Vendor Balance List

| **Navigation** | **Description** |
|---|---|
| • **Accounts payable >**<br>• **Enquiries and reports >**<br>• **Vendor reports >**<br>• **Vendor balance list** | Use this report to show, side by side, how vendor balances have changed during a defined subperiod, such as last month, and a defined period, such as the current year. The report shows credit totals, which often represent the amounts that were invoiced, and debit totals, which are usually the amounts that were paid. |

