<!-- https://learn.microsoft.com/en-us/training/modules/describe-general-ledger-cash-bank-management/8-describe-cash-bank-management -->
<!-- refetched: original harvest URL returned 404 -->
# Describe cash and bank management in Dynamics 365 Finance

Completed

* 30 minutes

You can use the Cash and bank management module in Dynamics 365 Finance to maintain the legal entity’s bank accounts and the financial instruments associated with those bank accounts.

These instruments include deposit slips, checks, bills of exchange, and promissory notes. You can also reconcile bank statements and print bank data on standard reports.

The Cash and bank management module is intricately connected to the accounts receivable and accounts payable modules.

## Business processes

Cash and bank management includes four major business processes:

* Deposit bank funds.
* Reconcile bank accounts.
* Transfer bank funds.
* Manage letters of guarantee.

## Deposit bank funds

By using the Cash and bank management module in Dynamics 365 Finance, you can maintain your legal entity's bank accounts and the financial instruments that are associated with those accounts. These instruments might include deposit slips, bills of exchange, promissory notes, or checks.

A deposit slip is a document used to deposit checks, credit card notes, and cash into a bank account. Use the **Deposit slip** page to view and manage deposit slips for payments into bank accounts.

You can cancel a deposit slip payment if a customer payment is invalid. If you already reconciled the deposit slip in the bank statement, you can't cancel the payment.

## Reconcile a bank account

When you receive a bank statement, you should periodically reconcile the legal entity bank transactions with the transactions on the bank statement.

You can't reconcile a bank statement with a bank account if any of the checks or deposit slip payments listed on the statement currently have a status of **Pending cancellation**. After a reviewer posts or rejects a check reversal or deposit slip payment cancellation, the status is no longer **Pending cancellation**, and you can reconcile the bank account.

## Modern bank reconciliation

Modern bank reconciliation in Dynamics 365 Finance makes it easier to match bank statements with posted bank transactions. It uses automated matching, flexible rules, and supports different reconciliation methods. Organizations can quickly compare electronic bank statements (like ISO20022, BAI2, or MT940) to their bank transactions in Dynamics 365 Finance and easily see which items match or don't match.

Organizations can import electronic bank statements using the standard data entity. Matching rules are then applied to automatically reconcile statement lines with bank transactions. These rules use criteria such as dates, amounts, transaction codes, or references. You can group matching rules into rule sets that run in sequence during reconciliation. Transaction code mapping helps improve accuracy by aligning bank transaction types with finance transaction types before applying the rules. Users can also manually match or adjust transactions when needed.

When the **Modern bank reconciliation** feature is enabled, Dynamics 365 Finance supports more matching types, such as one-to-many, many-to-one, and many-to-many matches, providing greater flexibility for real-world reconciliation scenarios. Organizations can also enable the **Reconcile after import** option to automatically validate the statement, create the reconciliation worksheet, and run the default matching rule set immediately after import. Validation parameters such as allowable date differences or required transaction type mappings help maintain consistency and prevent incorrect matches. Bank statement amounts can be displayed as debit/credit columns or as a single signed amount based on configuration.

After automatic and manual matching is complete, users can post the reconciliation and generate a reconciliation statement. Modern bank reconciliation reduces manual effort, improves accuracy, and provides a clear, side-by-side view of bank statement lines and finance transactions to help ensure cash balances remain accurate throughout each financial period.

## Manage letters of guarantee

A **letter of guarantee** is an agreement by a bank (the guarantor) to pay a set amount of money to someone (the beneficiary) if a bank customer (the principal) defaults on a payment or an obligation to the beneficiary. Letters of guarantee aren't transferable. They apply only to the beneficiary who is named in the agreement. The principal can request an increase or decrease in the value of a letter of guarantee, subject to the terms of the agreement.

You can use the **Letter of guarantee** page to complete these tasks:

* Create correct ledger entries and eliminate manual entry.
* Record all monetary and nonmonetary transactions and track balances of letters of guarantee.
* Record and track the status and expiration of letters of guarantee.
* Generate a report that lists the banks that are holding letters of guarantee.

## Settlements

During settlement, the transactions on one document are applied to the transactions on another document to increase or decrease the balance of each document. For example, a payment can be applied to an invoice. Various types of transactions can be settled at different times through different methods. The settlement process can also generate new transactions.

Settlement can occur between any transaction type that affects the vendor balance or customer balance. These transaction types can include invoices, payments, credit memos, and fees. Any transaction type can be settled against any other transaction type.

The following transaction types are available for use in single-company and cross-company settlements:

* Settlement
* Cash discount
* Foreign currency revaluations (includes realized and unrealized foreign currency revaluations)
* Penny difference
* Overpayment/underpayment

## Cash flow forecasting

Dynamics 365 Finance provides the cash flow forecasting tool to analyze the current cash flow status and future need for cash. The cash flow forecasting process integrates all major finance modules. These modules include:

* General ledger
* Accounts payable
* Accounts receivable
* Budgeting
* Inventory management

The cash flow forecasting tool considers the following transactions while calculating the current cash flow:

* Noninvoiced sales orders, resulting in physical and financial sale
* Unposted free text invoices, resulting financial sale
* Noninvoiced purchase orders and resulting physical and financial purchases
* Unpaid customer invoices
* Unpaid vendor invoices
* Ledger transactions specifying future posting
* Budget register entries selected for cash flow forecast
* Inventory forecast model lines selected for cash flow forecast
* Predicted tax payment amount and time

You need to first complete the configurations on the **Cash and bank management module** > **Cash flow forecasting** > **Cash flow forecast setup** page.

[![Screenshot of the Cash flow forecast setup page with the General ledger tab selected.](media/08-5-8-general-ledger-setup.png)](media/5-8-general-ledger-setup.png#lightbox)

You need to complete the configurations related to all modules in the respective tabs. First, you need to identify the liquidity accounts, which are the bank and cash accounts that influence the cash inflow or outflow.

In the accounts payable and accounts receivable, you need to define the default payment terms to consider for the cash flow forecast. You can also define the default payment terms based on the vendor groups or customer groups.

[![Screenshot of the Cash flow forecast setup page with the Accounts payable tab selected.](media/08-5-8-accounts-payable-setup.png)](media/5-8-accounts-payable-setup.png#lightbox)

On the **Budgeting** tab, you can define the default Budget models to be considered for the Cash flow forecast.

[![Screenshot of the Cash flow forecast setup page with the Budgeting tab selected.](media/08-5-8-setup.png)](media/5-8-setup.png#lightbox)

The cash flow process is run from the **Cash and bank management module** > **Cash flow forecasting** > **Cash flow forecast automation** page. You can select the **Create new process automation** button in the Action pane of the **Cash flow forecast automation** page followed by entering the schedule type and company to create a new series of forecasts.

When the new automation series is created, you can define the run schedule for the process. The name, schedule start date, and time can be defined here. This is one of the steps to create the process automation for cash flow forecast.

[![Screenshot of the creation of a new run schedule for process automation.](media/08-5-8-automation.png)](media/5-8-automation.png#lightbox)

## Financial Reconciliation Agent

The Financial reconciliation agent, delivered through Finance agents (formerly known as Copilot for Finance), provides AI-assisted automation to streamline the reconciliation of ledger transactions in Dynamics 365 Finance. It reduces manual review by analyzing financial data, detecting patterns, identifying potential matches, and highlighting discrepancies that require attention.

Finance agents accelerate time-to-impact for finance professionals by surfacing insights that support decision-making and significantly reducing time spent on repetitive reconciliation activities. Because Finance agents connect Microsoft 365 tools such as Excel directly with financial systems, users can stay in the flow of work while validating data, resolving differences, and preparing reconciliation support.

When used within Microsoft 365 Excel, the Financial Reconciliation agent provides intelligent prompts as data structures are compared, automatically generates a reconciliation report, and offers AI-based suggestions for resolving mismatches. It prepares a summarized reconciliation package, including suggested actions and documentation that can be saved for audit and period-close requirements. The Excel-based experience works with financial data from multiple systems, including Dynamics 365 Finance and other ERP or Financial Planning and Analysis (FP&A) solutions.

In addition to Excel, Finance agents also enhance productivity in Microsoft 365 Outlook, where finance users especially those involved in collections, can access ERP insights, draft responses with AI assistance, and save communication summaries and action items. For Outlook, Finance agents integrate with Dynamics 365 Finance and other ERP systems.

By combining machine learning, natural language processing, and deep ERP connectivity, the Financial Reconciliation agent helps organizations close books faster, improve accuracy, and shift focus from manual matching to higher-value analysis and decision support.