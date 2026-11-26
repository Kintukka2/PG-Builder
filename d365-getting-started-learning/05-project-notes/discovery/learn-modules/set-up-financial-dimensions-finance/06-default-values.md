<!-- https://learn.microsoft.com/en-us/training/modules/set-up-financial-dimensions-finance/default-values -->
# Default dimension values

Completed

* 2 minutes

You can use values from master records, such as customer and vendor records, as default values in new dimensions. When you create the new dimensions, the system enters the master record ID into the dimension values for those master records. For example, when you create a new customer, the system enters the customer ID in the customer dimension. When you create sales orders, invoices, or other documents that require a customer ID, the system uses the existing defaulting rules and then adds the customer ID to the document.

**General ledger** > **Chart of accounts** > **Dimensions** > **Financial dimensions** > **Dimension values**

[![Screenshot of the Financial dimensions values - CUSTOMER page.](media/06-customer-dimension-values.png)](media/customer-dimension-values.png#lightbox)

You can control this default dimension feature through a setting on the **Financial dimensions** page named **Copy values to this dimension on each new DimensionName created**. In this setting, **DimensionName** is the name of the dimension. By default, the feature is turned off. However, you can turn on the feature any time.

[![Screenshot of the Financial dimensions page with the Copy values setting highlighted.](media/06-copy-values.png)](media/copy-values.png#lightbox)

If records already exist for the dimension, the system updates the master records when you turn on the feature. However, the system doesn't update existing documents and transactions.