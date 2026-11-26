<!-- https://learn.microsoft.com/en-us/training/modules/accounts-receivable-daily-procedures-dyn365-finance/2-free-text-inv -->
<!-- refetched: original harvest URL returned 404 -->
# Create free text invoices

Completed

* 6 minutes

This unit explains the operations of processing orders, recording
invoices, and processing payments to demonstrate the process of Invoice-to-cash.

The difference between a free text invoice and a standard invoice is described in the following sections.

### Sales order invoice

The sales order invoice differs from free text invoices in the following ways:

* The user specifies the item number, and the system posts the
  item-related transactions in the ledger. Users can also
  create sales orders with non-inventory items.
* A sales order makes inventory transactions, but a free text invoice
  never uses item inventory because it does not create stock
  transactions. Frequently, free text invoices are used to sell fixed
  assets because the free text invoices calculate the costs or income
  when you depreciate and sell the asset. Refer to the Fixed Assets
  training manuals to learn more about the fixed asset topic.

### Free text invoice

Free text invoices differ from the sales order invoice in the following ways:

* No item numbers are specified by the user.
* The user selects a ledger account for the sale, which is
  displayed on each order line. The system posts the customer balance
  to the summary ledger account for the posting profile that was
  inherited from the customer, unless the user specifies a different
  posting profile on the free text invoice.

## Free text invoices

Use free text invoices to create a sales invoice with order lines that
include, but are not limited to, the following elements:

* Ledger accounts
* Free-text descriptions
* The entry of a sales amount

You cannot enter an item number on this kind of invoice; however, you
can enter the appropriate sales tax information.

Frequently, a free text invoice line can be used to sell a quantity of
some type of goods, services, or rights. For this reason, enabling the
quantity to be identified on the line might be necessary. Similarly, if
a good, service, or right has a unit price, it is important to capture
this information on the free text invoice line. Providing this
information to the user and a basic amount calculation helps identify
and explain charges to customers.

You can enter quantity and unit price to automatically calculate the
amount; however, if you have a unit price and modify the **Amount**
field, the unit price value is deleted, regardless of the value in the
**Quantity** field. Consequently, you have a total amount for the
quantity indicated in the line.

### Copy lines on a free text invoice

To copy lines on a free text invoice, select one or more lines and then
select **Copy selected lines**. You can specify the number of copies to
make, and then copy notes and attachments. You can either copy the
distributions or let them be re-created when you post.

**Accounts receivable > Invoices > All free text invoices**

[![Screenshot of the Free text invoice with Copy selected lines selected.](media/02-copy-lines.png)](media/copy-lines.png#lightbox)

After copying lines, you can edit the information as you require.

### Create a free text invoice from a template

You can create a free text invoice from a template. When selecting **New
from template** on the **Invoice** tab, you can select a template name
and the customer account for the new free text invoice. Default values,
such as the terms of payment and method of payment, can be automatically
filled in by the customer, or you can use the values that were saved
in the template.

[![Screenshot of the New from template on the Invoice tab.](media/02-create-invoice-from-template.png)](media/create-invoice-from-template.png#lightbox)

As a result, a new free text invoice is created, and you can edit the values as you
require.

### Accounting distributions

You can use the following buttons on the **Free text invoice** page to
view, and possibly change, the accounting distributions for each amount
on the free text invoice.

* **Distribute amounts** - View and change the accounting
  distributions for an individual line and any child lines, such as
  taxes or charges. You can also view and change the accounting
  distributions for the child line directly from the **Sales tax
  transactions** page or the **Charges transactions** page.
  + Change free text invoice header amounts, such as charges or
    currency rounding amounts.
  + Change free text invoice line amounts.
* **View distributions** - View the accounting distributions for all
  lines on the document. You can't change the accounting
  distributions from this view.
  + View header amounts.
  + View line amounts.

### Distributing taxes

Accounting distributions for taxes cannot be created until taxes are
calculated. To calculate sales taxes, complete one of the following
tasks on the **Free text invoice** page:

* View the sales tax
* View the invoice total
* View the cash flow
* View accounting distributions for the whole free text invoice
* View the subledger journal

### Accounting distributions and subledger journal entries for free text invoices

Accounting distributions are used to define how an amount is
accounted for, such as how the revenue, tax, or charges are
accounted for on a free text invoice. Every amount that must be
accounted for when the free text invoice is journalized has one or
more accounting distributions.

### Correct a free text invoice

Enter corrections to modify a free text invoice that has been posted.
When you correct an invoice that has been posted, a corrected invoice is
created where you can modify the invoice and post it with the new
values. When you post the corrected invoice, a canceling invoice is
created, which brings the combined balance of the original invoice and
the canceling invoice to a zero amount.

For example, if you correct an original posted invoice that has a
balance of 500.00, a corrected invoice is created that has a
balance of 500.00. You can change the information for the invoice and
then post it. When the corrected invoice is posted, a canceling invoice
is created that has a balance of -500.00. This process brings the combined
balance of the original and canceling invoices to 0.00.

To correct a free text invoice that has already been posted, open the
posted free text invoice. On the **Invoice** page, select **Cancel**
and then select **Correct invoice**. Select a reason code, add comments,
and select the date for a new corrected invoice. You can modify the
corrected invoice and post it.

When you post the corrected invoice, a canceling invoice is created for
a credit amount that equals the original invoice amount. Therefore, the
combined balance of the original invoice and the canceling invoice is 0
(zero). The canceling invoice is settled against the original invoice.

After posting the corrected invoice, you have three invoices:

* **Original invoice** - The invoice that includes the information
  that you're correcting.
* **Canceling invoice** - The system-generated credit invoice that
  was created to cancel the invoice that was most recently
  corrected.
* **Corrected invoice** - The invoice that contains the corrected
  invoice information.

You can identify canceling and correcting invoices in two ways:

* The **All free text invoices** page includes a **Correction** column, where you can view which invoices are canceling invoices and corrected invoices.
* The header of the free text invoice shows a status of **Canceling invoice '[invoice number]'** or **Corrected invoice '[invoice number]'**.

This feature is available only if the **Free text invoice
correction** configuration key is selected. To change configuration
keys, the environment must be in maintenance mode. For more information,
see [Maintenance
mode](/en-us/dynamics365/fin-ops-core/dev-itpro/sysadmin/maintenance-mode/?azure-portal=true).

**System administration > Setup > License configuration**

[![Screenshot of the License configuration page with the Free text invoice correction option highlighted.](media/02-free-text-invoice-corrections.png)](media/free-text-invoice-corrections.png#lightbox)

### Save a free text invoice as a template

You can also save an existing free text invoice as a template. When you
select **Save to template** from the **Invoice** tab, provide a name and
a description for the template. If a template with the name already
exists, you see a notification that a template with that name
already exists. You can still select **OK** to replace it.

[![Screenshot highlighting  the Save to template selected from the Invoice tab.](media/02-save-as-template.png)](media/save-as-template.png#lightbox)