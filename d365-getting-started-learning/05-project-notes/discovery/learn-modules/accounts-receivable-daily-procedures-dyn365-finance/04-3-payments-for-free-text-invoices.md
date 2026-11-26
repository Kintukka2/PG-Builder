<!-- https://learn.microsoft.com/en-us/training/modules/accounts-receivable-daily-procedures-dyn365-finance/3-pay-free-text-inv -->
<!-- refetched: original harvest URL returned 404 -->
# Recurring free text invoices

Completed

* 4 minutes

## Set up and process recurring invoices

Recurring free text invoices are used when a customer is to be billed on
a recurring basis.

To create a recurring free text invoice, follow these steps:

1. Create a free text invoice template.
2. Assign the template to a customer.
3. Generate and post the recurring invoice.

You can use recurring invoices if you invoice customers for the
same amount on a regular basis.

## Create a recurring free text invoice template

To invoice customers for the same services on a regular basis, you need
to define a free text invoice template that can be reused to create the
invoices. This template contains the following information:

* Header information, such as tax groups, terms of payment, and the
  method of payment
* Line information, such as the service description, revenue accounts,
  unit price, and invoice amount
* Charges for shipping or handling
* Accounting distributions, together with financial dimension
  information, such as cost centers and business units

Essentially, you're creating an entire invoice and saving it as a
template. You can set up the templates by using the **Recurring invoices** page.

## Generate the recurring invoices

The **Generate recurring invoices** page contains a task that
processes recurring invoice templates, where you specify the invoice
date and the template to generate the invoices from. Invoices will be
generated and assigned a single recurrence ID number for each group of
invoices that is processed.

## Assign a free text invoice template to a customer and enter recurrence details

After the template is created, you need to assign the template to the
customers that you want to invoice. Additionally, you should specify
when and how often the invoice will be used. You can assign the
templates on the **Invoice** tab of the **Customers** page. Add the
template to the list, and update the following information:

* The start date and, optionally, the end date for the recurring
  billing
* The frequency of the recurring billing (for example, every day or
  once a month)
* The maximum billing amount (if this information is required)

[![Screenshot of the Invoice tab of the Customers page.](media/04-customers-invoice-tab.png)](media/customers-invoice-tab.png#lightbox)

A customer can have multiple templates that have different frequencies.

## Post recurring free text invoices

After recurring invoices are generated the invoice recurrence IDs
appear in a posting task on the **Recurring invoices** page.

[![Screenshot highlighting the Options tab on the Post recurring invoices page.](media/04-post-recurring-invoices.svg)](media/post-recurring-invoices.svg#lightbox)

You can view all invoices for a recurrence ID by selecting the link.
During your review of the invoices for the recurrence ID, you can delete
individual invoices. The customer's recurrence settings will be reset
for that template so that it can be regenerated later. You can post one,
many, or all of the invoices for a recurrence ID. If workflows are
enabled, select **Submit** before you post the invoices.

## Print recurring free text invoices

After recurring invoices are posted, you can print the invoices from the
**Free text invoice** list page. You can print the invoices that are
selected, or you can select a range of invoices to print.

## Subledger journals for free text invoices

Before you post a free text invoice, you can view the full accounting
entry of the invoice, which includes debits and credits, to verify that
the invoice is being posted to the correct accounts. This view of the
full accounting entry is called a subledger journal.

If the subledger journal entry is incorrect when you preview it before
journalizing the free text invoice, you can't change the subledger
journal entry. Instead, you must change the accounting distributions or
the posting profile. The accounting distributions are used to define one
side of the accounting entry, the debit or the credit. The offsetting
subledger journal account entry is created from the posting profiles,
such as from the customer account or the tax.