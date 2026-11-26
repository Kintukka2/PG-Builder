<!-- https://learn.microsoft.com/en-us/training/modules/describe-account-payables-account-receivables/6-describe-core-accounts-receivable-components -->
# Describe core accounts receivable components

Completed

* 45 minutes

Accounts receivable is money owed to a business by its customers presented as an asset on a company's balance sheet. For example, an electric company that bills customers for electricity after the customer already received it would record an account receivable until the customer pays.

Customers in accounts receivable are similar to vendors in accounts payable. Both use groups to organize accounts and posting profiles to decide which ledger accounts are used for invoices, payments, discounts, and settlements. The main difference is that accounts payable tracks money owed to vendors, while accounts receivable tracks money owed by customers. These shared features help keep financial processes consistent across the system.

## Customers

When customers buy products or services, you can create customer invoices based on sales orders or packing slips. You can also enter free text invoices that aren't related to sales orders. You can receive payments by using several different payment types. These include bills of exchange, cash, checks, credit cards, and electronic payments. If your organization includes multiple legal entities, you can use centralized payments to record payments in a single legal entity on behalf of the other legal entities.

### Key types of information stored with a customer

A customer record stores all information needed to manage billing, receipts, collections, and reporting in accounts receivable. This includes basic data such as the customer’s name, address, contact details, and tax information, as well as financial and credit settings that control how transactions post. Customer records also store default values that flow to sales orders, invoices, payments, and settlements.

Typical customer master data includes:

* **Customer group**: Defines behavior for posting, settlement, reporting, and credit and collections
* **Posting profile**: Determines which ledger accounts customer transactions post to, like vendor posting profiles in Accounts payable
* **Credit and collections settings**: Credit limits, blocking rules, reason codes, and collection settings
* **Payment defaults**: Terms of payment, method of payment, payment schedule, payment day, and cash discounts
* **Financial dimensions**: Default values that flow automatically to transactions for reporting and analytics
* **Tax information**: Sales tax groups and item sales tax groups
* **Addresses and contact information**: Multiple addresses (invoice, delivery, business, etc.) and contact methods
* **Currency and language settings**: Control how invoices are generated and displayed

### Customer summary with Copilot

Finance and operations apps include an AI-generated **Summary by Copilot** FastTab that provides a quick overview of customer activity directly on the **All customers** details page. This summary helps users understand each customer’s financial status, outstanding balances, and recent activity without navigating multiple pages.

Copilot analyzes available data such as posted customer invoices, overdue amounts, payments, credit limits, and order activity. It then presents the most relevant insights in a single panel. For customers, this may include information such as:

* The total number of posted and overdue customer invoices.
* Outstanding balances and recent payment history.
* Active sales orders, packing slips, or delayed shipments.
* Customer credit limit, remaining credit, and any holds.
* Status indicators that highlight trends, risks, or unusual activity.

Because **Summary by Copilot** is personalized based on the user’s security roles and usage patterns, it delivers insights that are most meaningful to the receivables team. This enables users to quickly assess customer account health, identify potential collection issues, and take proactive action for follow-up or review.

## Customer invoices

To discuss customer invoices, we must first examine where they fit in with the business processes for accounts receivable.

[![Diagram of the Accounts receivable process and where Customer invoices fit in the process.](media/06-6-6-accounts-receivable.png)](media/6-6-accounts-receivable.png#lightbox)

The **Manage projects** and **Process sales orders** processes feed into accounts receivable in different steps of the **Collect for product or service** process. This process involves the following steps:

* Process customer prepayments.
* Invoice customers.
* Receive and enter customer payments.
* Settle invoices and payments.
* Manage and collect overdue customer invoices.

Three types of customer invoices are available:

* Customer invoices for sales orders
* Free text invoices
* Pro forma invoices

## Customer invoices for sales orders

A **customer invoice for a sales order** is a bill that is related to a sale and that an organization gives to a customer. This type of customer invoice is based on a sales order, which includes order lines and item numbers. Item numbers are specified and posted in the ledger.

To learn more about creating customer invoices for sales orders, access the corresponding links in the Summary and resources unit at the end of this module.

## Free text invoices

A free text invoice isn't related to a sales order. It contains order lines that include ledger accounts, free-text descriptions, and a sales amount that you enter. You can't enter an item number on this kind of invoice. You must enter the appropriate sales tax information. A main account for the sale is indicated on each invoice line, which you can distribute to multiple ledger accounts by selecting **Distribute amounts** on the **Free text invoice** page. Additionally, the customer balance is posted to the summary account from the posting profile used for the free text invoice.

## Accounting distributions

Accounting distributions are used to define how an amount is accounted for. For instance, to define how the revenue, tax, or charges are accounted for on a free text invoice. Every amount that must be accounted for when the free text invoice is journalized has one or more accounting distributions.

You can use the following buttons in the **Free text invoice** page to view, and possibly change, the accounting distributions for each amount on the free text invoice.

* **Distribute amounts**: View and change the accounting distributions for an individual line and any child lines, such as taxes or charges. You can also view and change the accounting distributions for the child line directly from the **Sales tax transactions** page or the **Charges transactions** page.

  + Change free text invoice header amounts, such as charges or currency rounding amounts.
  + Change free text invoice line amounts.
* **View distributions**: View the accounting distributions for all lines on the document. You can't change the accounting distributions from this view.

  + View header and line amounts.

## Pro forma invoices

A pro forma invoice is an invoice that is prepared as an estimate of the actual invoice amounts before the invoice is posted. You can print a pro forma invoice either for a customer invoice for a sales order or for a free text invoice.

## Settlement

To settle an accounts receivable transaction, you first create a customer payment journal by going to **Accounts receivable** > **Payments** > **Customer payment journal**.

In the journal lines, you can select **Payment proposal** > **Create payment proposal** to filter customer invoices to invoices you want to include in the payment journal. You can use filter criteria such as **From date** and **To date** for a specific date range of the selected invoices. You filter the invoices based on invoice amount limits. You can filter the invoices based on payment due date and cash discount date. You can also select other parameters like customer, method of payment, and currency to filter criteria.

[![Screenshot depicting filter options to select the customer invoice to add in the payment journal.](media/06-6-6-payment-proposal.png)](media/6-6-payment-proposal.png#lightbox)

Among the invoices that fit your filter criteria, you can select the invoice for which you're receiving the payment.

The selected invoices are added to the journal lines.

[![Screenshot depicting the customer payment journal.](media/06-6-6-payment-journal.png)](media/6-6-payment-journal.png#lightbox)

After you select the payment method, the payment journal is posted to settle the invoice.

## Workspaces for managing customer invoices and payments

Dynamics 365 Finance includes two workspaces that help accounts receivable teams efficiently manage customer billing and cash collection: **Customer invoicing** and **Customer payments**. These workspaces centralize key accounts receivable information, surface exceptions, and provide embedded **Power BI analytics** to help users monitor processing performance, identify delays, and follow up on outstanding items quickly.

### Customer invoicing workspace

The **Customer invoicing** workspace helps users create, review, and manage customer invoices from sales orders, packing slips, or free text invoices. It shows invoices waiting to be posted, those with missing data, credit or hold issues, or invoices needing review. Built-in Power BI charts display invoice counts, processing times, and aging, so teams can quickly spot and resolve issues.

[![Screenshot of the Customer invoicing workspace.](media/06-6-6-customer-workspace.png)](media/6-6-customer-workspace.png#lightbox)

### Customer payments workspace

The **Customer payments** workspace supports the end-to-end management of incoming customer payments. It provides visibility into open customer balances, unapplied payments, payment journals awaiting posting, and transactions requiring follow-up. Power BI analytics help teams monitor cash collection trends, overdue balances, and the effectiveness of collection efforts. These insights enable accounts receivable teams to improve cash flow forecasting, prioritize collection activity, and resolve settlement issues more efficiently.

View the following video for a demo on the Copilot-assisted accounts receivable process.