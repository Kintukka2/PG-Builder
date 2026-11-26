<!-- https://learn.microsoft.com/en-us/training/modules/create-use-workflows-finance-operations/2-types -->
<!-- refetched: original harvest URL returned 404 -->
# Workflow types for business processes

Completed

* 15 minutes

Workflows are available throughout many different areas of finance and operations apps.

In finance and operations apps, the term workflow is defined in two ways:

* **Workflow as a System** - This system provides functionality that can be used to create individual workflows or business processes.
* **Workflow as a Business Process** - This business process defines how a document flows through the system by displaying who must process and approve it.

As mentioned, a workflow represents a business process. It defines how a document flows, or moves, through the system by showing who must complete a task, make a decision either by using a manual or conditional decision controls, or approve a document. To first start the workflow, configure either an approval element, sub-workflow, or a task. Then, it will be submitted for approval to complete the workflow.

To better understand workflows, consider the following scenario.
Suppose that Sam submits an expense report for USD 8,000.00. In this scenario, Ivan must review the receipts that Sam routes to him. Then Frank and Sue must approve the expense report.

You can have multiple workflows of the same type. For example, suppose you are creating purchase requisition workflows for each country or region in which you operate. You might want to name a purchase requisition workflow as Purchase Requisitions Denmark or Purchase Requisitions Spain.

## Defining workflow types

A workflow configuration is based on a workflow type. You can create multiple workflow configurations for each workflow type.

Workflow types are available for numerous modules throughout the system. For example, in **General ledger > Journal setup > General ledger workflows** page, select **New** to view available workflow types.

[![Screenshot of the  General ledger workflows page.](media/02-gl-workflows.png)](media/gl-workflows.png#lightbox)

Each type of workflow corresponds to a journal type in a specific module. One workflow configuration must be created for each journal type that is used with workflow approvals.

By design, some of the workflows are shared across multiple legal entities, which we know as organization-wide workflows, while the other types of workflows are legal entity specific.

You can identify the workflow association with your organization by the value of the field in the workflows list page of each module in finance and operations apps, as shown in the screenshot.

[![Screenshot of the  the workflows list page highlighting the Association field.](media/02-workflow-association.png)](media/workflow-association.png#lightbox)

Some modules do not have any workflow type at all. Alternatively, the type of workflow that you need to have to address a certain business requirement does not exist. If this is the case, your development team can create new workflow types in finance and operations apps by using Visual Studio.

Before you plan to create a new workflow, it is always a good idea to see if any out-of-the-box workflows in finance and operations apps can be used instead of creating a new one.
You can always create a new version of an existing workflow and modify it in a way that addresses the customer’s business requirements.

If no workflow exists for a specific requirement, or no out-of-the-box workflows exist that can address the requirement, your development team can create new workflow templates.

Several types of out-of-the-box workflow templates are available in finance and operations apps.

## General ledger workflow types

The following workflow types are available for General ledger. Each type corresponds to a journal type:

* **Ledger daily journal workflow** - Use this type to create approval workflows for daily journals.
* **Ledger allocations journal workflow** - Use this type to create approval workflows for allocation journals.
* **Ledger eliminations journal workflow** - Use this type to create approval workflows for eliminations journal.
* **Advanced ledger entry workflow** - Use this type to create approval workflows for advanced ledger entries.

## Accounts payable workflow types

The following workflow types are available for Accounts payable:

* **Freight Invoice Approval** - This workflow supports invoice approval.
* **Vendor invoice line workflow** - Use this type to create review workflows for vendor invoice lines.
* **Vendor invoice approval journal workflow** - Use this type to create approval workflows for vendor invoice approval journals.
* **Proposed vendor changes workflow** - Approve the proposed vendor change.
* **Vendor disbursement journal workflow** - Use this type to create approval workflows for vendor disbursement journals.
* **Vendor invoice journal workflow** - Use this type to create approval workflows for vendor invoice recording journals.
* **Vendor settle promissory note journal workflow** - Use this type to create approval workflows for vendor settle promissory note journals.
* **Vendor redraw promissory note journal workflow** - Use this type to create approval workflows for vendor redraw promissory note journals.
* **Vendor invoice workflow** - Use this type to create review workflows for vendor invoices.
* **Vendor bank remittance journal workflow** - Use this type to create approval workflows for vendor bank remittance journals.
* **Vendor invoice register journal workflow** - Use this type to create approval workflows for vendor invoice register journals.
* **Vendor draw promissory note journal workflow** - Use this type to create approval workflows for vendor draw promissory note journals.

## Accounts receivable workflow types

The following workflow types are available for Accounts receivable:

* **Customer free text invoice workflow** - Use this type to create approval workflows for free text invoices.
* **Customer draw bill of exchange workflow** - Use this type to create approval workflows for customer draw bill of exchange journals.
* **Customer settle bill of exchange workflow** - Use this type to create approval workflows for customer settle bill of exchange journals.
* **Customer redraw bill of exchange workflow** - Use this type to create approval workflows for customer redraw bill of exchange journals.
* **Customer payment workflow** - Use this type to create approval workflows for customer payment journals.
* **Customer protest bill of exchange workflow** - Use this type to create approval workflows for customer protest bill of exchange journals.
* **Proposed customer change workflow** - Approve the proposed customer change.
* **Customer recurring invoice workflow** - Use this type to create approval workflows for recurring invoices.
* **Customer bank remittance workflow** - Use this type to create approval workflows for customer bank remittance journals.
* **Credit management release workflow** – Use this to control the release of credit management holds from sales orders.
* **Credit limit adjustment workflow** – Use this to approve credit limit adjustments for all customers or customer credit groups in the credit adjustment.
* **Credit limit adjustment line workflow** – Use this to approve credit limit adjustments for each individual customer or customer credit group in the credit adjustment.

## Budgeting workflow types

The following workflow types are available for Budgeting:

* **Budget plan workflow** - Use this type to create and review workflows for budget plans.
* **Budget register entry workflow** - Use this type to create review workflows for budget register entries.
* **Budget account entry workflow** - Use this type to create review workflows for budget account entries.
* **Commitments approval workflow** - Use this template to create approval workflows for commitment documents.
* **General budget reservation workflow** - Use this template to review general budget reservation documents.

## Cash and bank management workflow types

The following workflow type is available for cash and bank management:

* **Bank reconciliation journal approval workflow** - Use this type to create approval workflows for Bank Reconciliation journals.

## Expense management workflow types

The following workflow types are available for expense management:

* **Travel requisition workflow** - Use this type to create approval workflows for travel requisitions.
* **Expense line item auto posting** - Use this type to create line item automatic posting workflows for expense reports.
* **Expense report auto posting** - Use this type to create document automatic posting workflows for expense reports.
* **Expense line item** - Use this type to create line item approvals for expense reports.
* **VAT tax recovery** - Use this type to create approval workflows for VAT tax recover.
* **Cash advance request** - Use this type to create approval workflows for cash advance requests.
* **Expense report** - Use this type to create document approvals for expense reports.

## Fixed asset management workflow types

The following workflow types are available for fixed assets:

* **Ledger post fixed assets journal workflow** - Use this type to create approval workflows for post fixed asset journals.
* **Ledger fixed assets budget journal workflow** - Use this type to create approval workflows for fixed asset budget journals.

## Human resources workflow types

The following workflow types are available for human resources:

* **Worker project experience** - Use this type to create workflows for worker project experiences from employee self-service.
* **Transfer worker** - Use this type to create workflows for transferring workers using Personnel actions.
* **Human resources actions workflow** - Use this type to create workflows for personnel actions, such as to create new positions or to modify positions.
* **Change worker fixed compensation** - Use this type to create workflows for requesting fixed compensation changes for workers by using Personnel actions.
* **Worker position of trust** - Use this type to create workflows for worker positions of trust from employee self-service.
* **Worker courses** - Use this type to create workflows for worker courses from employee self-service.
* **Worker loaned amount** - Use this type to create workflows for worker loaned items from employee self-service.
* **Worker review** - Use this type to create workflows for worker review.
* **Worker image** - Use this type to create workflows for worker images from employee self-service.
* **Worker education** - Use this type to create workflows for worker education from employee self-service.
* **Worker identification number** - Use this type to create workflows for worker identification number from employee self-service.
* **Worker skills** - Use this type to create workflows for worker skills from employee self-service.
* **Worker certificates** - Use this type to create workflows for worker certificates from employee self-service.
* **Hire worker** - Use this type to create workflows for hiring workers by using Personnel actions.
* **Worker professional experience** - Use this type to create workflows for worker professional experiences from employee self-service.
* **Worker course registration** - Use this type to create workflows for worker course registration.
* **Terminate worker** - Use this type to create workflows for terminating workers by using Personnel actions.

## Organization workflow types

The following workflow types are available for organization:

* **Signing limits workflow** - Use this template to create a workflow for review of signing limit requests.
* **Case management workflow** - Use this type to create a workflow for cases.
* **Document handling** - Workflow type for document handling.

## Procurement and sourcing workflow types

The following workflow types are available for procurement and sourcing:

* **Invoice received notification workflow** - Use this type to create invoice received notification workflows for unconfirmed product receipts.
* **Product receipt failed notification workflow** - Use this type to create notification workflows for failed product receipts.
* **Vendor rebate approval** - Vendor rebate workflow approval type.
* **Purchase agreement approval workflow** - Use this type to create approval workflows for purchase agreements.
* **Purchase order line workflow** - Use this type to create review and approval workflows for purchase order lines.
* **Unconfirmed product receipt rejection notification workflow** - Use this type to create notification workflows for rejected unconfirmed product receipts.
* **Purchase requisition line review** Use this type to create review workflows for purchase requisition lines.
* **Catalog import approval** - Use this type to create review workflows for imported catalogs.
* **Delivery due date notification workflow** - Use this type to create delivery due date notification workflows for unconfirmed product receipts.
* **Vendor add application workflow** - Use this type to create approval workflows for vendor add application requests.
* **Purchase order workflow** - Use this type to create review and approval workflows for purchase orders.
* **Catalog import product approval** Use this type to create review workflows for imported catalog products.
* **Purchase requisition review** - Use this type to create review workflows for purchase requisitions.

## Project management and accounting workflow types

The following workflow types are available for project management and accounting:

* **Review original budget workflow** - Use this type to review an original budget.
* **Review timesheet line workflow** - Use this type to review a timesheet line.
* **Request for quotes workflow** - Use this type to review request for quotes.
* **Resource request line workflow** - Use this type to review resource request lines.
* **Review timesheet workflow** - Use this type to review a timesheet.
* **Review project invoice proposal workflow** - Use this type to review project invoice proposals.
* **Review project quotation workflow** - Use this type to review project quotations.
* **Review budget revision workflow** - Use this type to review a budget revision.

## Inventory management workflow types

* **Inventory Adjustment Journal** - Create approval workflow for adjustment journals.
* **Inventory BOM Journal** - Create approval workflow for BOM journals.
* **Inventory Counting Journal** - Create approval workflow for counting journals.
* **Inventory Movement Journal** - Create approval workflow for movement journals.
* **Inventory Ownership Change Journal** - Create approval workflow for ownership change journals.
* **Inventory Tag Counting Journal** - Create approval workflow for tag counting journals.
* **Inventory Transfer Journal** - Create approval workflow for transfer journals.

## Commerce workflow types

The following workflow types are available for Commerce:

* **Retail sales line workflow** - Use this type to review retail sales line price override.
* **Retail catalog line workflow** - Retail catalog approval workflow type.
* **Retail sales quotation line workflow** - Use this type to review retail sales quotation line price override.

## Sales and marketing workflow types

The following workflow type is available for sales and marketing:

* **Create customer rebate workflow** - Customer rebate workflow type

## Time and attendance workflow types

The following workflow types are available for time and attendance:

* **Time and attendance journal registration workflow** - Use this type to create approval workflows for time and attendance journal registration records
* **Time and attendance days total workflow** - Use this type to create approval workflows for time and attendance days total records.

Note

To keep up to date with the list of workflows that are available, refer to [Workflow types report](/en-us/dynamics365/fin-ops-core/fin-ops/organization-administration/workflow-types-report?azure-portal=true&toc=/dynamics365/supply-chain/toc.json).