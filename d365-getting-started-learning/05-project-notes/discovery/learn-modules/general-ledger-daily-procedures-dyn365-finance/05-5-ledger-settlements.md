<!-- https://learn.microsoft.com/en-us/training/modules/general-ledger-daily-procedures-dyn365-finance/5-ledger-settlements -->
# Ledger settlements

Completed

* 10 minutes

Ledger settlements let you match debit and credit transactions in the General ledger and mark them as settled. In this way, you can make sure that related transactions have been cleared. You can also reverse settlements if they were made by mistake.

## Settle transactions

To settle ledger transactions, follow these steps.

1. Go to **General ledger > Periodic tasks > Ledger settlements**.
2. Set the filters at the top of the page:

   * Select a date range, or select **Date interval code** to automatically fill in the date range.
   * Change the posting layer, if needed. You can't settle transactions that are in different posting layers.
   * To show the main account and dimensions separately, select a financial dimension set.

   Note

   When the **Enable advanced awareness options** parameter is turned on (**General ledger parameters > Ledger settlements**), settlement must be completed within a single fiscal year and for transactions in a single main account, so **Main account** becomes a required filter.
3. Select **Display transactions** to show all the transactions that match the filters that you set and the list of accounts that you specified when you set up the chart of accounts list in the previous section. If you change any of the filters or the dimension sets, you must select **Display transactions** again.
4. Select one or more lines that you're considering for settlement. The value of the **Selected amount** field at the top of the page increases or decreases by the total amount on the lines that you selected.
5. After you've finished selecting transactions, select **Mark selected**. A check mark appears in the **Marked** column for each transaction that you selected. Additionally, the value of the **Marked amount** field above the grid increases or decreases by the total amount on the lines that you marked.
6. When the **Marked amount** value is **0** (zero), select **Settle marked transactions**. The status of the marked transactions is updated to **Settled**.

## Make transactions easier to find

The **Ledger settlements** page includes the following capabilities that make it easier to see the transactions that you need for settlement:

* **Unmark selected** - Clears the Marked field for all lines that are selected.
* **Unmark for selected users** - Unmarks ledger settled transactions for all legal entities by user ID, so that another user can mark those transactions for settlement.
* **Unmark all transactions** - Unmarks all ledger settled transactions for all users and all legal entities. This action is available for the Administrator role.
* **Marked** - Lets you filter transactions based on whether the Marked field is selected or cleared.
* **Status** - Lets you filter transactions based on whether their status is Settled, Partially settled, or Not settled.
* **Sort by absolute amount** - Lets you sort the amounts by an absolute value, so that you can group debits and credits that have the same amount.
* **Review cross-year settlements** - Lets you view and unsettle ledger transactions that were settled across fiscal years.
* **Review missing settlement accounts** - Lets you find ledger accounts that have ledger settlements but are missing from the ledger settlement account list, and add them. Missing accounts can cause the year-end close to fail.

## Reverse a settlement

You can reverse a settlement that was made by mistake by following these steps:

1. Follow steps 1 through 3 in the "Settle transactions" section to show the transactions that you're looking for.
2. In the **Status** filter, select **Settled**.
3. Highlight one line, and then select **View settlements** to open the **Ledger settlements history** page.
4. Select the lines that you want to reverse. When you select a transaction, the corresponding transaction that has the same settlement ID is selected automatically.
5. Select **Reverse marked transactions**, select the reversal date options, enter a comment if needed, and then select **Reverse**. The status of all transactions that have the same settlement ID is updated to **Not settled**.
6. Select the back arrow to return to the **Ledger settlements** page. The reversed transactions have a check mark in the **History** column to indicate that they were settled and then unsettled.

Important

All transactions that have the same settlement ID are reversed, even if you don't mark them. For example, if you settled four lines under one settlement ID and then reverse one of them, all four lines are reversed.

## Partially settle transactions

Ledger settlements must be completed within a fiscal year, which makes it difficult to clear accruals that span fiscal years. Partial ledger settlements let you settle part of a transaction at the end of a period or fiscal year and carry the remaining amount forward. For example, if a 12,000 USD prepaid insurance debit is cleared by 1,000 USD monthly credits, you can settle the debit against the first three credits at year end and carry the remaining 9,000 USD into the next year.

When partial settlement is turned on, the **Status** filter includes a **Partially settled** status, remaining amount columns are added to the grid, and settlement history is tracked for all transactions. The **Subledger to ledger auto settlement** parameter also lets settlements that originate in Accounts payable or Accounts receivable be settled automatically in the general ledger.

## Update the list of accounts that are included in the list of transactions

Select **Ledger settlement accounts** to open a dialog box where you can edit the accounts that are included in the list of transactions. Select **New** to add new accounts to the list. This list is used to filter the list of transactions that appears on the **Ledger settlements** page.

## Learn more

For more information about ledger settlements, see [Ledger settlements](/en-us/dynamics365/finance/general-ledger/ledger-settlements/?azure-portal=true), for more information about automating ledger settlements, see [Automate ledger settlements](/en-us/dynamics365/finance/general-ledger/auto-settle/?azure-portal=true), and for more information about settling part of a transaction, see [Partial ledger settlements](/en-us/dynamics365/finance/general-ledger/ledger-settlements-partial/?azure-portal=true).