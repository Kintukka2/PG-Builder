<!-- https://learn.microsoft.com/en-us/training/modules/set-up-financial-dimensions-finance/activate-delete -->
# Activate and delete financial dimensions

Completed

* 5 minutes

When you activate a financial dimension, the system updates the table so that it includes the name of the financial dimension. The system also removes the dimensions. You can enter dimension values before you activate a financial dimension.

You can't use a financial dimension in Finance until it's activated.

For example, you can't add a financial dimension to an account structure until you activate the financial dimension. When you select **Activate**, the system updates all dimensions and then updates the **Status** field to **Active**.

**General ledger** > **Chart of accounts** > **Dimensions** > **Financial dimensions**

[![Screenshot of the Financial dimensions page with Activate highlighted.](media/05-activate-dimension.png)](media/activate-dimension.png#lightbox)

## Translations

On the **Text translations** page, you can enter text for the selected financial dimension in various languages. On any page in Finance that has a **Translations** button, such as on the **Main account translation** page, you can enter this text.

[![Screenshot of the finance and operations Text translations page.](media/05-translation.png)](media/translation.png#lightbox)

## Legal entity overrides

Not all dimensions are valid for all legal entities. Also, some dimensions might be relevant for a specific period only. In these cases, you can use the **Legal entity overrides** section to specify the companies that the dimension should be suspended for, the owner, and the period when the dimension is active.

Go to **General ledger > Chart of accounts > Dimensions > Financial dimensions**, select a financial dimension, and then select **Dimension values**.

[![Screenshot of the Legal entity overrides section on the Financial dimensions page.](media/05-legal-entity-overrides.png)](media/legal-entity-overrides.png#lightbox)

## Delete a financial dimension

To help maintain referential integrity of the data, you can delete financial dimensions only on rare occasions. You can't delete a financial dimension after you use it in any of the following ways, even if you later remove the reference:

* The financial dimension is used on posted or unposted transactions or it's in any type of dimension value combination.
* The financial dimension is used in any active account structure, advanced rule structure, or financial dimension set.
* The financial dimension is part of a default financial dimension integration format.
* The financial dimension is set up as a default dimension, such as in ledger setup, module parameters, or posting profiles.
* The financial dimension is used in the Financial Reporting setup.
* Any dimension value was created for the dimension, even if you never used that value on a transaction.

If the financial dimension meets any of these criteria, you can't delete it. The restriction applies even when no posted transactions exist, journals were never posted, or you removed the dimension from the account structure. This behavior is by design and preserves reporting accuracy and audit integrity.

To retire a financial dimension or dimension value that you no longer need, rename or suspend it instead:

* **Rename** the dimension or value to indicate that it shouldn't be used, such as **\_\_\_DONOTUSE\_DimensionName**. You can rename and reuse the value later, which also improves application performance compared to creating new values.
* **Suspend** a dimension value to prevent its use on new transactions. Suspended values are hidden from lookups, but you can rename and reuse them later.

For more information, see [Modifying and deleting financial dimensions](/en-us/dynamics365/finance/general-ledger/modifying-deleting-financial-dimensions/?azure-portal=true).