<!-- https://learn.microsoft.com/en-us/training/modules/accounts-receivable-daily-procedures-dyn365-finance/reimburse-customer -->
# Reimburse a customer

Completed

* 10 minutes

Consider the following information when you work with the reimbursement feature:

* You can use the feature to repay customers who have credit amounts because of
  overpayment or credit notes.
* Before you run the process, set the **Minimum reimbursement** amount
  on the **General** tab of the **Accounts receivable parameters**
  page. Run the process from **Accounts receivable > Periodic tasks >
  Reimbursement**.
* The feature transfers the balance to a vendor account. The vendor account is
  assigned on the **Miscellaneous details** FastTab of the
  **Customers** page; otherwise, a one-time vendor
  account is created automatically.
* The Accounts Payable Coordinator can create an ordinary payment when
  the balance amount transfers to a vendor account.

Consider an alternative option, where you would use the **Accounts
receivable payment journal** and debit the customer for the value of
refund, generate payment, and then post.

You can also refund customers directly from the customer payment journal
by using the International Organization for Standardization (ISO) 20022
credit transfer format, which avoids the transfer to a vendor account.
This approach supports refunds with a credit note, refunds of a
prepayment by using a payment proposal, and manual refunds. To use it,
import the **Payment model mapping for refunds to customers** Electronic
reporting configuration, set up a method of payment that has the
**Payment type** field set to **Electronic Payment** and the **Export
format for refunds** option turned on, and then select **Functions >
Generate payments** in the customer payment journal. For more
information, see [Refund payment processing in the customer payment
journal](/en-us/dynamics365/finance/accounts-receivable/refund-customers/?azure-portal=true).

This video uses Contoso demo data to explain how to create reimbursement transactions for a customer. If a customer has a credit balance, you can reimburse them for the balance. Through the video demonstration, you learn how to create a reimbursement transaction for a customer and how to connect a vendor account to a customer account for the reimbursement process.

For more information, refer to [Reimburse customers](/en-us/dynamics365/finance/accounts-receivable/reimburse-customers/?azure-portal=true).