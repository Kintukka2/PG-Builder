<!-- https://learn.microsoft.com/en-us/training/modules/set-up-financial-dimensions-finance/ledger-account-aliases -->
# Ledger account aliases

Completed

* 4 minutes

In most organizations, the account structure in General ledger is a combination of the main account and several financial dimensions. You need to populate the account and all required dimensions in the journal lines. The more dimensions that you have, the more tedious the journal line creation becomes.

**Ledger account alias** is primarily a usability feature. It simplifies the journal line creation by making a short alphanumeric value instead of the entire main account and dimension combination. You can define this alphanumeric value on the **Ledger account alias** page under **Chart of accounts > Accounts** sub menu of the **General ledger** module. This feature is useful for commonly used account combinations.

[![Screenshot of the Ledger account alias page.](media/10-ledger-account-alias.png)](media/ledger-account-alias.png#lightbox)

The **Type** field defines to whom this alias is available. If the value is **Shared**, this alias is available to all users. If you select **User group** in the **Type** field, you are asked to select the user group. The users in the selected group are eligible to use the ledger account alias. You can also select **User** in the **Type** field, where you are asked to select the user who's eligible to use the ledger account alias.

In the **Initial focus** field, you need to choose the dimension that should be selected when you enter the ledger account alias in the journal line.

In the **Account** column of the general journal line, you can enter the ledger account alias.

[![Screenshot of the location to enter the ledger account alias in General journal.](media/10-enter-alias-general-journal.png)](media/enter-alias-general-journal.png#lightbox)

When you leave the field, the application automatically picks up the actual account and dimensions.

[![Screenshot of Alias replaced by account.](media/10-alias-replaced-account.png)](media/alias-replaced-account.png#lightbox)

You can further update the account and dimensions according to business requirements.