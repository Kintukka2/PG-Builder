<!-- https://learn.microsoft.com/en-us/training/modules/set-up-financial-dimensions-finance/exercise -->
# Exercise - Set up an account structure

Completed

* 10 minutes

# Scenario

In this lab, use the **USMF** company account in the Contoso demo data set to set up an account structure as follows.

1. Go to **General ledger > Chart of accounts > Structures > Configure account structures**.
2. Select **New**.
3. In the **Account structure** field, enter **USMF Expenses**.
4. In the **Description** field, enter **USMF Expenses**.
5. Set the **Add main account** toggle to **Yes**.
6. Select **Create**.
7. In the **Allowed value details** section, fill in the following values:

   * **Where** - MainAccount
   * **Operator** - is between and includes
   * **Value** - 600000
   * **through** 699999
8. Select **Apply**. Note how the **Segments and allowed values** FastTab populates with the proper syntax.
9. In the **Segments and allowed values** FastTab, select **Add segment**.
10. Select **Department** in the **Add segment** window, and then select **Add segment**.
11. Repeat the process for **Cost center** and **Customer**.
12. With your cursor on the **Department** column, enter **031..034**.
13. Enter **007..018** in the **Cost center** column.
14. With your cursor in the **Customer** column, in the **Allowed value details**, select the **Blank values are allowed** checkbox.
15. In the upper part of the page, select **Validate**.
16. When the system shows the **OK** message, select **Activate**. On the dialog, select **Activate** again.
17. The **Status** shows as **Activating**. The process takes a couple of minutes. If you keep selecting **Refresh**, the status soon changes to **Active**.