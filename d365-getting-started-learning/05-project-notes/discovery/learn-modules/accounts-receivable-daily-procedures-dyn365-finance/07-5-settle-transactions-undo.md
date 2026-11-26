<!-- https://learn.microsoft.com/en-us/training/modules/accounts-receivable-daily-procedures-dyn365-finance/5-settle-undo -->
<!-- refetched: original harvest URL returned 404 -->
# Settle transactions and undo settlements

Completed

* 13 minutes

You can use the **Settle transactions** page to make changes in transactions for
customers. Only unapplied transactions are available for editing. The
following procedures explain how to complete the following tasks:

* Settle invoices and payments
* Specify a cross rate between invoices and payments
* Reorganize transactions with new due dates

## Settling invoices and payments

You can settle invoices and payments in the **Settle open transaction**
page if, for example, the invoice and payment are not settled when you
create the payment.

The following information is relevant to settling invoices and payments:

* If the amount paid is more than the amount due, then the system
  settles the invoice and the payment transaction remains open for the
  amount by which the payment exceeded the amount due. If the
  over/underpayment feature is being used, it can force them to be
  equal and close the transaction.
* If the payment amount is less than the amount due, then the system
  subtracts the payment from the amount due and the invoice remains
  open.
* If the amount paid equals the amount due, then the system generates
  a payment transaction for the payment amount and then closes the
  transaction.

To enable automatic settlements, go to **Accounts receivable > Setup >
Accounts receivable parameters** and, on the **Settlement** tab, set the
**Automatic settlement** option to **Yes**. Transactions are then settled
automatically against other open transactions when you post them. If you
set this option to **No**, users settle transactions manually when they
enter payments, or later, by using the **Settle transactions** page.

In some cases, it is convenient to allow for an automatic settlement of
invoices and payments.

For example, if a company must handle numerous small customers who have
few payments, such as subscribers to magazines, automatic settlement can be an efficient
solution to posting payments.

You can use a cross rate when you settle a payment with an invoice and
the payment and invoice lines are in different currencies. When you
select an invoice and a primary payment, you can enter a cross rate for
the invoice line. The cross rate is the exchange rate between the
currencies for those transactions as of the settlement date.

### Settlement priority

You can control the order in which open transactions are selected during
settlement instead of relying on the default behavior. On the
**Settlement** tab of the **Accounts receivable parameters** page, set
the following options:

* **Prioritize settlement** - Set this option to **Yes** to enable the
  **Mark by priority** button on the **Enter customer payments** and
  **Settle transactions** pages, so that users can apply the
  predetermined settlement order to transactions. Users can still
  change the order and the payment allocation before posting.
* **Use priority for automatic settlements** - Set this option to
  **Yes** to use the defined priority order when transactions are
  settled automatically. This option is available only if
  **Prioritize settlement** and **Automatic settlement** are both set
  to **Yes**. Select **Manage priority** to define the rules.

On the **Settlement priority** page, you sequence the attributes that
the system evaluates when it selects transactions: **Transaction type**,
**Due date**, **Cash discount date**, **Transaction date**, **Transaction
amount**, and **Voucher**. For more information, see [Automatic
settlement and
prioritization](/en-us/dynamics365/finance/accounts-receivable/automatic-settlement-prioritization/?azure-portal=true).

## Process incomplete card payments

Card payments are external transactions that can't be rolled back if an
error occurs, so the card payment process is split into the following
stages:

* Create and post the customer invoice.
* Capture or refund the credit card.
* Post the payment journal.
* Authorize the remaining payment amount.

The status of each stage is centrally logged and monitored per invoice and sales order. Therefore, in case of failures in the process after the customer invoice is posted, you can check the failure reason and recover payment process.

To use this functionality, turn on the **Improve cards payment
processing flow in customer payment** feature in the **Feature
management** workspace. Then go to **Accounts receivable > Setup >
Accounts receivable parameters** and, on the **Credit card** tab, set the
**Cards payment status monitoring** option to **Yes**.

To review incomplete payments, go to **Accounts receivable > Invoices >
Open customer invoices** and, on the **Invoice** tab, select
**Incomplete cards payment**. On the **Incomplete cards payment** page,
select **Resume** to restart the process from the last failed stage, or
select **Terminate** to end it. Select **View history** to review the
processed payment stages and their execution logs.

For more information, see [Process incomplete credit card payments](/en-us/dynamics365/finance/accounts-receivable/credit-card-refactor/?azure-portal=true).

## Reorganizing open transactions

You or a customer might pay one invoice on multiple dates or use
multiple payment methods, such as a check and cash. In this instance,
you can reorganize an invoice into several parts and assign a separate
payment method to each part. After reorganizing the invoice, you can
settle each new invoice line with a separate payment.

Alternatively, you can reorganize the due dates by using a payment
schedule. Select the **Payment schedule** button, select a payment
schedule and a starting point, and then select **OK**. The **Payment
schedule** configuration key must be selected to reorganize transactions
according to a payment schedule.

## Placing an accounts receivable transaction on hold

To make data entry more flexible, you can enter a transaction on one
date, and then put it on hold to prevent users from posting it until a
specified date. This functionality is useful if you have an agreement
with a customer about when a transaction can be posted.

To prevent a transaction from being posted until a specified date, enter
a release date. The transaction is on hold until the release date
occurs. You can edit and save transactions that are on hold, but you
cannot post them unless you first remove the hold.

## On hold transactions in different time zones

If your organization includes users who work across different time
zones, the date and time when a transaction is released from a hold is
based on the time zone of the user who most recently modified the
**Release date** value. Because the transactions release at midnight on the
specified date in that user's time zone, the actual date and time of
the release adjust accordingly for users in other time zones.

For example, on December 31 in New York, a user puts a transaction on
hold at noon Eastern Time and enters a release date of January 1 (the
next day). The user sets up the transaction to be on hold until midnight
Eastern Time, so the user must wait 12 hours for the transaction to be
released.

Users in London, which is five hours ahead of New York, also must wait
12 hours. However, because the transaction was put on hold at 5:00 PM
Greenwich Mean Time on December 31, the transaction will not be released
until 5:00 AM Greenwich Mean Time on January 1.

For users in Seattle, which is three hours behind New York, the
transaction was put on hold at 9:00 AM Pacific Time on December 31. When
the transaction is released 12 hours later (at 9:00 PM Pacific Time), it
will still be December 31 for these users.

## Undo settlements

When you work with reverse settlements, consider the following information:

* You can use the **Closed-transaction editing** window to edit fully applied
  or settled transactions that are in history.
* You can use reverse settlements if the bank does not honor a payment, or if
  you used the wrong date or settlement amount.
* An unsettled invoice is considered unpaid and is handled together
  with collection letters.

Watch the following video to learn how to settle and undo settlements in Accounts
receivable: