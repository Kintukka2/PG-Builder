<!-- https://learn.microsoft.com/en-us/training/modules/configure-ledgers-journals-dyn365-finance/reverse-journal-posting -->
# Reverse journal posting

Completed

* 4 minutes

This unit describes capabilities in Dynamics 365 Finance that allow you to reverse an entire journal or reverse one or more vouchers from the voucher transaction list, regardless of their origin.

Before you can use any feature that's described in this unit, you'll need to turn on the feature in your system. Admins can use the **Feature management** workspace to check the status of the feature and turn on the feature, if required. The feature is listed on the workspace as follows:

* **Module** - General ledger
* **Feature name** - Mass reversals for multiple documents
* **Default** - enabled

You should also turn on the **Automatic split of large financial journals** feature, which improves performance during journal posting and journal reversal. The feature is listed on the **Feature management** workspace as follows:

* **Module** - General ledger
* **Feature name** - Automatic split of large financial journals

## Reverse journals

You can reverse journal lines individually. With reverse journal posting, you can also reverse an entire financial journal.

To reverse a journal, follow these steps:

1. Filter on the posted journals and open the **Lines** view on the journal.
2. Select the **Reverse entire journal** menu in the upper part of the page. The total number of vouchers and voucher lines and the total amount of the lines that are being reversed will display.
3. Select **Yes** to use the existing transaction dates or **No** to enter a new one. Occasionally, the period of the original transaction might be closed, so you'll need to enter a new transaction date for the reversal.
4. If you select **No**, enter a transaction date for the reversal.
5. Enter a comment that you want added to the reversal transaction.
6. Select the **Reverse** button.

When you're finished, the transactions should show as reversed.

If the voucher contains more than 100 lines, the reversal process will run by using the batch process. You can review the results
by viewing the comments in the batch job. Transactions that couldn't be reversed will be listed in the batch job history.

If the voucher contains 100 lines or fewer, the reversal process will run immediately. The results are presented in a dialog that shows vouchers that couldn't be reversed. The dialog also displays the reason why it couldn't be reversed.

### Reverse related journals that were automatically split

When the **Automatic split of large financial journals** feature is turned on, journals that contain more than 1,000 lines are automatically split into multiple related journals. When you reverse one of those journals, all related journals are reversed. You can view the count of related journals and the total number of lines that are affected before you confirm the reversal.

The reversal of related journals is supported only at the journal level, and it runs as a background process. You can review the results in the message log of the batch job history. You can still reverse individual lines without affecting other lines.

Note

The reversal of related journals isn't possible when you reverse vouchers from the **Voucher transaction** inquiry page. In that case, only the selected vouchers are reversed.

## Reverse vouchers from the voucher transaction list

You can reverse vouchers from the **Voucher transaction list** across all subledgers. In addition, you can reverse more than one
voucher at a time.

To reverse one or more vouchers, follow these steps:

1. Select the **Reverse entire journal** dropdown menu in the upper part of the page. The total number of vouchers and voucher lines and the total amount of lines that are being reversed will display.
2. Select **Yes** to use the existing transaction dates or **No** to enter a new one. Occasionally, the period of the original transaction might be closed, so you'll need to enter a new transaction date to reverse it.
3. If you select **No**, enter a transaction date for the reversal.
4. Enter a comment to describe the reversal transaction.
5. Select the **Reverse** button.

When you're finished, the transactions should show as reversed.

If the number of voucher lines exceeds 100, the reversal process will run by using the batch process. You can review the results
by viewing the comments in the batch job. Transactions that couldn't be reversed will be noted in the batch job history.

If the number of voucher lines is 100 lines or fewer, the reversal process will run immediately. The results will display in a dialog that shows vouchers that couldn't be reversed, along with the reason why. Select **OK** to close the dialog.

The preceding functionalities are the standard for reversing a voucher, and you can use them for transactions by using following account types:

* Ledger
* Customer
* Vendor
* Fixed asset

If an account or offset account in a journal involves the **Bank** or **Project** account types, reversal functionality won't be supported.

You can only reverse transactions if they meet the business rules for reversing them. You can't reverse vendor payments by using the capability that's described in this article. You'll need to reverse vendor payments by following the steps that are listed in [Reverse a vendor payment](/en-us/dynamics365/finance/accounts-payable/reverse-vendor-payment/?azure-portal=true).