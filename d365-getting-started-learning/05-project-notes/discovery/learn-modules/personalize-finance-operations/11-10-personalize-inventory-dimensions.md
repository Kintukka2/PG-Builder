<!-- https://learn.microsoft.com/en-us/training/modules/personalize-finance-operations/10-personalize-inv-dim -->
<!-- refetched: original harvest URL returned 404 -->
# Personalize inventory dimensions

Completed

* 5 minutes

When you personalize the setup of inventory dimensions on a page, consider the settings that have been created by using the **Display dimension** option.

For example, you use personalization to hide a column for the Batch number inventory dimension, but the column appears the next time that the page is opened. This behavior occurs because the **Dimension display** settings control the inventory dimension columns that are shown.

The **Dimension display** settings apply across all pages and override any personalized setup of inventory dimension fields on individual pages.

As a result, in the preceding example, if you don't want the column for the Batch number inventory dimension to appear, you must clear that dimension as part of the **Display dimensions** option for the table on the **General ledger > Ledger setup > General ledger parameters** page. Eventually, this change will apply not only on one specific page but across all pages.

[![Screenshot of Inventory dimensions set to display Site.](media/11-dim-display.svg)](media/dim-display.svg#lightbox)