<!-- https://learn.microsoft.com/en-us/training/modules/accounts-receivable-daily-procedures-dyn365-finance/7-exercise-2 -->
<!-- refetched: original harvest URL returned 404 -->
# Exercise - Work with invoices from sales orders

Completed

* 11 minutes

In this exercise, you will:

1. Create an invoice from a sales order.
2. Combine orders into a single invoice.
3. Post invoices in a batch.

## Create an invoice from a sales order

1. In company USMF, go to **Accounts receivable > Orders > Shipped but not invoiced sales orders**.
2. Select a sales order in the list.
3. On the Action Pane, select **Invoice**.
4. Select **Invoice**. Note that this sales order has multiple packing
   slips associated with it. It will only show the word instead of the
   packing slip number.
5. Expand the **Parameters** section. Posting must be set to **Yes** to
   post the invoice. You can also turn off posting and just print the
   invoice. However, you can accomplish the same result by creating a
   pro forma invoice instead of an invoice. This option is used for
   batch jobs. The query is run when the batch job is run.
6. In the **Print** field, select **After**.
7. Select **Yes** for **Print invoice**.
   Print management can print multiple copies of the invoice and also send the invoice by email as a PDF file.
8. In the **Print charges** field, select **Summarize**.
9. In the **Check credit limit** field, select **Balance**.
10. Select **Cancel**.

## Combine orders into a single invoice

1. Go to **Accounts receivable > Orders > All sales orders**.
2. Locate a customer that has multiple invoices open.
3. Select an open sales order.
4. Select another open sales order for the same customer.
5. On the Action Pane, select **Invoice**.
6. Select **Invoice**.
7. Expand the **Parameters** section.
8. In the **Quantity** field, select **All**. Note that two invoices
   are listed in the overview section. Now, you can merge them into a
   single invoice.
9. In the **Summary update for field**, select **Invoice
   account**.
10. Select **Arrange** to merge the sales orders into a single invoice.
    The two sales orders are now merged into a single invoice.
11. Select **Cancel**.
12. Select **Yes**.

## Post invoices in a batch

1. Go to **Accounts receivable > Invoices > Batch invoicing >
   Invoice**.
2. Select the **Select** option.
3. Select **OK**.
4. Select **Batch**.
5. Select **Yes** to turn on batch processing.
6. Select **Recurrence**.
7. Select **Days**.
8. Select **OK**.
9. Select **OK**.
10. Select **Cancel**.
11. Select **Yes**.