<!-- https://learn.microsoft.com/en-us/training/modules/work-analytics-reporting-finance-operations/6-exercise-1 -->
<!-- refetched: original harvest URL returned 404 -->
# Exercise - Work with reports

Completed

* 15 minutes

## Scenario - Generate and explore a financial report

You need to generate and explore an existing default financial report.
The report includes all accounts and contains account properties (attributes) for the accounts.
You'll be drilling into transaction detail, applying a dimension filter, and changing the currency on the report.

### Display the order of dimensions for financial reporting

Displaying the order of dimensions for financial reporting lets you select how the dimensions are displayed.

1. In the company **USMF**, go to **General ledger > Chart of Accounts > Dimensions > Financial dimension configuration for integrating applications**.
2. Expand the **Financial dimensions** FastTab of the **Default dimension format**.
3. Arrange the dimensions so that the **MainAccount** is first on the list - you will need to select **MainAccount** from the **AVAILABLE** list and use the right arrow to move it to the **SELECTED** list.
4. Arrange the dimensions so that the **BusinessUnit** is second on the list.
5. Arrange the dimensions so that the **CostCenter** is third on the list.
6. Arrange the dimensions so that the **Department** is fourth on the list.
7. Select **Save** and **Yes** to save the changes.
8. Close the page.

### Generate a report and explore the data in the report

1. Go to **General ledger** > **Inquiries and reports** > **Financial reports**.
2. Select the row for the report named **Ledger Transaction List – Default**.
3. Select **Edit**.
4. In the **Do you want to open ReportDesigner.application from usnconeboxax1aos.cloud.onebox.dynamics.com?** prompt, select **Open**.
5. Select **Run** in the **Microsoft Dynamics 365 Finance: Financial Report Designer** box to download the Report designer.
6. Use the same credentials to log in, as you used to log in to finance and operations, located in the **Azure Portal** section in the right side of the lab page. The log-in window may appear behind the finance and operations window. The Report designer will now open in another window.
7. In the Report designer, change the **Base year** to **2016** and select **Generate** in the top right of the Report designer page.
8. When the report is completed, close the **Report Queue Status** page.
9. Return to the **Financial reports** page in finance and operations. You will need to refresh the screen until the report you generated appears.
10. Select the report, and then select **View**.
11. In the opened report, select **All accounts**.
12. Select **Accounts Receivable - Domestic - Home** to drill into the account detail for the report.
13. At the report transaction level, you can view the properties (attributes) that are included in the design of this report. Depending on the transaction and account, some or all the attributes might be displayed.
14. Close the report transaction level by using the back arrow at the top of the report.

Within a financial report, you can view the data either for a different period and year, or with different attributes and dimensions applied. This is done by using **Report options**.

1. While on **All accounts** select **Report options**.
2. Select **Add a dimension filter**, select **BusinessUnit** and then type **001** in the **BusinessUnit is** field.
3. Select **OK**. The report now displays only the data for the **001 Business Unit**. This is a personalized view of the report and isn't available for others to view.
4. Close the filtered report.

Financial reports can be displayed in any currency that has been added to finance and operations apps.

1. Select **Currency** and then select **Euro (EUR)**. The report now displays in Euros. Any currency codes or currency symbols that are included in the report design now display in the applied currency. If no currency symbol is defined for a currency, the currency symbol is not displayed.
2. Close the **Ledger Transaction List - Default (EUR)** report.