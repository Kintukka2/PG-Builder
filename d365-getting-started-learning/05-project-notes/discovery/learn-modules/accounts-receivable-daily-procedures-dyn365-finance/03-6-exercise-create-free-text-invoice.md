<!-- https://learn.microsoft.com/en-us/training/modules/accounts-receivable-daily-procedures-dyn365-finance/6-exercise-1 -->
<!-- refetched: original harvest URL returned 404 -->
# Exercise - Create and process a free text invoice

Completed

* 21 minutes

In this exercise, you will:

1. Create a free text invoice.
2. Assign a free text invoice template to a customer.
3. Generate and post recurring free text invoices.

## Before you begin

To get the most benefit from this and other exercises in this module, we
recommend that you have the standard sample data available in finance and operations that is installed by using Lifecycle Services.

## Create a free text invoice

1. In company **USMF**, go to **Accounts receivable > Invoices > All free text invoices**.
2. Select **New**.
3. In the **Customer account** field, select **US-003**. The invoice
   account will default to the same account that was used for the
   customer account.
4. Note the value of the **Accounting status** field. The accounting
   status starts with **In process** if the invoice is not posted and
   the invoice number will be assigned when the invoice is posted.
5. Under the **Invoice lines** FastTab, in the **Description** field, enter **Selling old computers**.
6. In the **Main account** field, specify account number **130700**.

   The sales tax group is populated from the customer. If the customer
   does not have a sales tax group, the sales tax group from the main
   account is used.

   The item sales tax group is populated from the main account. If the
   main account does not have an item sales tax group, then the item
   sales tax group in the General ledger sales tax parameters is used.
7. In the **Quantity** field, enter **15**. The value of quantity is optional.
8. In the **Unit** **price** field, enter **128**. The value of unit price is optional.
9. The amount is calculated as the quantity times the unit price.
   However, you can override that calculation and enter an amount.
10. On the menu at the top of the screen, select **Sales tax** to view the sales tax that was calculated for
    your invoice.
11. View the sales tax amounts on the **Sales tax** page, or
    override the amounts on the **Adjustment** tab.
12. Select **OK** to close the window.
13. On the menu at the top of the page, select **Charges** to add a charge to your invoice.
14. In the **Charges code** field, select **FREIGHT**.
15. In the **Charges value** field, enter **150**.
16. Select **Save** and close the page.
17. On the menu at the top of the page, select **Totals** to view the summary invoice details and totals.
18. Select **Close**.
19. Expand the **Line details** FastTab so you can add dimensions to
    your main account.
20. Select the **Financial dimensions line** tab.
21. In the **Cost center** field, select **007**. The dimension values
    are for the selected line only.
22. On the menu at the top of the page, select **Post** to post the invoice. You will be able to cancel
    before you post.
23. To change the timing of your invoice printing: in the **Print**
    field, select **Current** to print each invoice as it is updated, or
    select **After** to print after all invoices have been updated.
24. If you want to change how the customer's credit limit is checked
    before posting, change the **Credit limit type** field.
25. If you want to print the invoice, select **Yes**.
26. If the **Posting** field is enabled, the free text invoices that are
    selected will be posted when you select **OK**. To print a pro forma
    invoice, clear this option and select the **Print invoice** option.
27. Select **OK**.
28. On the Action Pane, select **New > Payment journal**.
29. Select **New**.
30. In the **Name** field, enter or select **CustPay**.
31. Select **Enter customer payments**.
32. In the **Customer** field, specify the values **US-003**.
33. In the list, find and select the row with the value of 2,209.20 in
    the **Amount available to pay** field.
34. Select **Mark selected**.
35. Set the **Amount** field to **2198.85**.
36. Select **Save in journal**. Close the page.
37. Select **Lines**.
38. Select the **Bank** tab.
39. Select **Yes** in the **Use a deposit slip** field.
40. In the **Payment reference** field, enter **FreeText Payment**.
41. Select **Post**.
42. Close all pages.

## Assign a free text invoice template to a customer

1. Go to **Accounts receivable > Customers > All customers**.
2. In the list, find and select the desired record.
3. On the Action Pane, select **Invoice**.
4. Select **Recurring invoices**. Use this page to assign free text invoice templates to customers and specify how frequently invoices will be sent to the customer.
5. Select **New** to assign a new template to the customer.
6. Select the free text invoice template that you want to assign to the customer.
7. In the list, find and select the desired record.
8. In the list, select the link in the selected row.
9. Enter the date when the first invoice will be generated.
10. Enter a recurring end date. Select one of the following options:

    * **No end date** - Invoices will be generated indefinitely until the template is removed from the customer account.
    * **Billing end date** - Select this option and enter the last date that the invoice can be generated.
11. Select the maximum cumulative amount after which invoice generation will stop. For example, if you enter 1,000.00 and generate monthly invoices for 100.00 each, invoices will stop generating after the tenth invoice is generated.
12. Generate recurring invoices by using the default values from either the free text invoice template or the customer account. Select the option that applies.
13. Select from the following recurrence patterns:

    * **Daily** - Select this option and enter the number of days in the **Per** field. For example, if you enter **15**, an invoice will be generated every 15 days for the customer.
    * **Weekly** - Select this option and enter the number of weeks in the **Per** field. For example, if you enter **2**, an invoice will be generated every two weeks for the customer.
    * **Monthly** - Select this option and enter the number of months in the **Per** field. For example, if you enter **6**, an invoice will be generated every six months for the customer.
    * **Yearly** - Select this option and enter the number of years in the **Per** field. For example, if you enter **2**, an invoice will be generated every two years for the customer.
14. In the **Per** field, enter a number.

## Generate and post recurring free text invoices

To generate and post recurring free text invoices, follow these steps:

1. Go to **Accounts receivable > Invoices > Recurring invoices > Generate recurring invoices**.
2. Select an **Invoice date** and **Template**.
3. Select **OK**.
4. Go to **Accounts receivable > Invoices > Recurring invoices >
   Post recurring invoices**. Use this page to view and print recurring
   invoices that have already been generated.
5. In the list, select the recurring invoice group.
6. Select **Totals**. Verify totals for the recurring invoice group.
7. Select **Close**.
8. Select **Validate**. Verify that the selected invoices do not have
   errors.
9. Select **Post** to post the selected invoices.