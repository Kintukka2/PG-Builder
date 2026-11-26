<!-- https://learn.microsoft.com/en-us/training/modules/describe-general-ledger-cash-bank-management/10-describe-periodic-financial-processes -->
<!-- refetched: original harvest URL returned 404 -->
# Describe periodic financial processes in Dynamics 365 Finance

Completed

* 12 minutes

Periodic financial processes in Dynamics 365 Finance help organizations complete month-end and year-end activities, ensure data accuracy, and prepare the system for the next accounting period. These processes support adjustments, reconciliations, revaluations, and financial consolidation across legal entities.

In Dynamics 365 Finance, you can complete closing procedures for a period, such as a day, month, or year. Closing processes prepare the system for a new period.

## Prepare for financial period close

Each organization has different processes and steps that it performs for the end of a period. Optional steps for period end include:

* Settle invoices and payments.
* Post all transactions for period end.
* Verify that all journals are posted.
* Run foreign currency revaluation for the general ledger to generate any unrealized gain or loss amounts.
* Run foreign currency revaluation for accounts payable and accounts receivable.
* Settle ledger transactions.
* Process any required allocations.
* Reconcile the subledgers to the general ledger.
* Post period-end adjustments manually.
* Journalize transactions and review the Ledger journal report.
* Perform a consolidation by using a consolidation company or financial reporting.
* Generate period-end financial statements by using financial reporting.
* Set ledger periods to **On hold** so that no further posting occurs. For better control, you can also restrict a period to a specific user group while period-end activities are occurring. As a best practice, don't use the **Permanently closed** status, because you can't reopen a period that was set to **Permanently closed**. This status could be used at a much later time.

Let's take a deeper look at the financial period close processes in the following simulation.

[![Screenshot of the landing page of the simulation.](media/10-period-close.png)](https://microsoftlearning.github.io/click-throughs/docs/AB-6002/explore_the_period_close_workplace_in_dynamics_365_finance_scorm/story.html)

## Financial period close workspace

The **Financial period close** workspace lets you track your financial closing processes across companies, areas, and people. Depending on the security role assigned to your user profile to view the **Financial period close** workspace, either all tasks and statuses for a closing schedule are displayed or only the tasks that are assigned to you.

You can find the **Financial period close** workspace by accessing **General ledger** > **Workspaces** > **Financial period close**. You can use the workspace to organize and track required tasks for various period-end processes.

You must first select a closing schedule at the top of the workspace. The selected closing schedule filters all presented data on the workspace.

Summary tiles in the workspace, shown in the following screenshot, provide an overview of the process, and indicators help you keep the closing process on track. They list out the tasks that are past due, remaining tasks for today, tasks that are due today but blocked because of dependencies, and all remaining tasks for the process. This information is for all companies included in the selected closing schedule.

[![Screenshot of the Financial period close place with the summary highlighted.](media/10-5-10-period-close.png)](media/5-10-period-close.png#lightbox)

To learn more about configuring the financial period close, review the links to further resources at the end of this module.

## Month-end closing

View this video to learn how to process month-end close.

## Create and post a closing sheet

A company might print a trial balance sheet to look for inconsistencies and make any adjustments necessary before closing the period. To make adjustments in Dynamics 365 Finance, you can perform either of the following tasks:

* Make typical journal entries, depending on adjustment.
* Use the **Closing period adjustments** page.

Consider the following information when you use the **Closing period adjustments** page:

* It presents an advanced view of the balances on accounts, and you can perform year-end postings directly from it.
* The postings to the page typically occur in the closing period of the fiscal year.
* You can create several specific closing sheets (for revenue, expenses, balance accounts, and so on) and then load the balances from the general ledger into the closing sheet. After you load the transactions, make transfers from one account to another.
* It resembles a journal, because you can create as many new closing sheets as needed, and you can post several lines of entries.

It's not possible to make transactions to the **Opening** period in a closing sheet; use the **Opening** option only for a beginning balance transaction. You can make adjustments, however, to one or more regular periods and to one or more closing periods. Usually, this field is set to **Closing**.

Which columns populate depends on the **Close** option that is selected when you set up each account in the chart of accounts.

## Post the closing period adjustment

After you complete the necessary transfers or adjustments, select the **Post** button to post the closing period adjustment. The closing period adjustment only posts to the closing period.

Before closing the period and transferring ending balances into the new year as opening balances, run reports and verify results.

To post the closing sheet, open the closing period on the **Periods** page. After you post the closing sheet, ensure that you change the period back to **On hold**.

## Year-end close

At the end of a fiscal year, you must run the year-end close process to transfer opening balances to the new year. Most companies run the year-end close process multiple times. The first time would be to move the balances into the new fiscal year. You can then run the year-end close again, as many times as required, to move the balances from adjusting entries into the new fiscal year.

You can create two types of transactions during the year-end close process. An Opening transaction is always generated and is used to create the opening balances in the new fiscal year. In the new fiscal year, the Opening transaction displays balance sheet ledger account balances and profit and loss ledger account balances in the retained earnings ledger account, excluding intercompany transactions.

Optionally, you can create a Closing transaction to bring the balances of the profit and loss accounts down to zero in the fiscal year that you're closing.

## Process year-end close

At year end, you need to complete the following tasks:

* Make adjustment entries that reflect transactions from the previous year.
* Print reports, including financial statements.
* Back up data.
* Create a new fiscal year, and transfer opening balances.

## Foreign currency revaluation

If you are in business with multiple countries/regions, you must consider multi-currency transactions in your day-to-day business. For instance, exchange rate fluctuations can cause the book value of open transactions in foreign currency to vary over time.

For example, suppose you work for an Indian company whose default currency is INR and you have a customer based in the United States. You conduct transactions with this US customer in USD. In May, you issue a sales invoice for US $1,000 when the exchange rate is USD 1 = INR 83. By June, your accounts receivable total INR 83,000. The customer makes the payment in the following month, when the exchange rate changes to USD 1 = INR 83.50. When you run the currency revaluation process using the new exchange rate, you recognize an unrealized gain of INR 500. When you post the settlement, the system balances the unrealized gain by posting to the realized gain account. If the exchange rate decreases, you incur both realized and unrealized losses.

You must set up some areas in the **General ledger module** > **Currency** > **Currency revaluation posting profile** page.

You can define realized and unrealized gains/losses for general ledger transactions on the **General ledger** tab and define a specific account for a specific currency. For accounts payable transactions, you can define realized/unrealized gain/loss accounts in the combination of currency and vendor/vendor group on the **Accounts** **payable** tab. Similarly, for accounts receivable transactions, you can define realized/unrealized gain/loss accounts in the combination of currency and customer/customer group.

At the close of a period, you might have to adjust the balances of general ledger accounts in foreign currencies using various exchange rate types. For instance, one accounting standard mandates that assets and liabilities be revalued using the current exchange rate, fixed assets at the historical rate, and income statement accounts at the monthly average. When you run the revaluation process, the balance in each main account posted in a foreign currency is revalued. The unrealized gain or loss transactions created during the revaluation process are posted in the main account.

[![Screenshot of the Currency revaluation posting profile page.](media/10-5-10-currency.png)](media/5-10-currency.png#lightbox)

You can also define the realized/unrealized gain/loss accounts from the **General ledger module** > **Ledger setup** > **Ledger** page. If you don't define realized/unrealized gain/loss accounts in the posting profile, the accounts defined on the Ledger page are used for the transaction posting.

[![Screenshot of the ledger page where the currency revaluation posting types are highlighted.](media/10-5-10-ledger.png)](media/5-10-ledger.png#lightbox)

## Perform financial consolidation

In a consolidation, it's possible to gather transactions from several company accounts into a single set of company accounts. You can print reports, such as financial statements, from the consolidation company, but you can't use this company for daily transactions.

Before you perform a consolidation at the close of a period, you must perform the period-closing preparatory activities, but don't close the subsidiary accounts until the consolidation is complete.

You can consolidate data from companies with databases that are external to the consolidation company database, or you can consolidate data from companies in the same database, a so-called "online" consolidation.

Consolidations don't necessarily require that you set up the consolidation company in advance. However, if you want to use the consolidation conversion principles to convert subsidiary data in foreign currencies, you must set up the consolidation company main accounts.

To prepare a consolidation company (the company that collects the results and balances of the subsidiaries), you should have a legal entity created with the **Use for financial consolidation process** option enabled. Like any other legal entity, you should complete the **General ledger module configuration** for the consolidation company.

After you complete the setup process in the consolidation company, you can focus on the subsidiary company. The amount of setup that is needed in a subsidiary depends on how closely the chart of accounts and dimensions for the consolidation company and subsidiary are aligned.

You can perform consolidation by using a shared or blank chart of accounts.

## Account Reconciliation Agent

The Account Reconciliation agent in Dynamics 365 Finance automates reconciliation of the general ledger with subledgers such as bank, accounts payable, accounts receivable, and tax. It uses AI to identify mismatches, recommend corrective actions, and learn from past resolutions. This agent eliminates the need to manually run multiple reconciliation reports, especially in organizations with many legal entities, and helps ensure that subledger balances align with the general ledger.

Typical use cases include:

* Reconciling bank subledger to the general ledger
* Identifying and resolving discrepancies in AP/AR balances
* Automating journal entries for corrections within defined tolerances
* Supporting continuous reconciliation across multiple legal entities

View the following video for a demo of the Account Reconciliation Agent.

## Intercompany eliminations

Elimination transactions are required when a parent company conducts business with one or more subsidiary companies and uses consolidated financial reporting.

Finance teams eliminate all intercompany transactions—including downstream, upstream, and lateral dealings—when preparing consolidated financial statements. This process ensures that the financial statements accurately reflect the group’s economic reality as a single entity, rather than as separate companies. As a result, you must remove transactions between a parent company and its subsidiaries.

Predefined elimination rules create elimination transactions in a company that is specified as the destination company for eliminations. You can generate the elimination journals during the consolidation process or by using an elimination journal proposal.