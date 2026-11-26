<!-- https://learn.microsoft.com/en-us/training/modules/describe-dynamics-365-finance-core-capabilities/5-describe-cost-accounting-concepts -->
<!-- refetched: original harvest URL returned 404 -->
# Describe cost accounting concepts in Dynamics 365 Finance

Completed

* 12 minutes

Cost accounting is a branch of managerial accounting that identifies both variable and fixed costs associated with a company's production process. It helps measure financial performance and informs future business decisions.

Cost accounting in Finance provides important insights into the cost efficiency and capacity of the managerial decision-making processes. It empowers cost controllers and cost center managers to control, classify, allocate, and analyze costs of current operations and plan for future changes.

The analysis content in the Cost accounting module highlights variances between the actual costs and budgeted costs. Based on the analysis, managers can be notified about positive and negative trends for their operational units. Managers can drill down to the cost element hierarchies or individual cost elements. In this way, managers can gain detailed insight into how cost variances occurred, and then take effective action.

The **Cost control** workspace in **Cost accounting** > **Cost control** is designed as a page. Therefore, you can grant access to all managers who are responsible for a cost object. You can control access to the page and data in the form.

Control the list of reports available for users, such as managers, by setting the **Published** option on the **Cost control** **workspace configurations** page.

A manager can select the fiscal calendar period to view. The session date is used to determine the default current period.

The values in the fiscal calendar period are determined by the report name and the fiscal calendar selected for the cost accounting ledger that is associated with the report name on the **Cost control workspace configurations** page.

In the cost object dimension hierarchy, users can select the aggregation level at which balances should be displayed. By enabling access-level security, you control the permissions so users can view the entire hierarchy. However, users are only able to view balances for chief officers, such as the Chief Executive Officer (CEO) and Chief Financial Officer (CFO), who were granted access.

Users can customize the columns on a report to fit their requirements. The customizations affect only the user that makes the changes after the new format is saved.

[![Screenshot depicts the Cost Control Window with View details function highlighted.](media/05-04-cost-control-12-new.png)](media/04-cost-control-12-new.png#lightbox)

A grid displays each cost element that is associated with the cost element dimension hierarchy node and its values, as depicted in the following screenshot. The columns that appear in the grid match the workspace settings. Two charts present a summary of actual versus budget and budget variance by period.

[![Screenshot depicts the cost element details.](media/05-04-cost-elements-13-new.png)](media/04-cost-elements-13-new.png#lightbox)

Users can select **Cost entries** to drill down into the entry details as required, shown in the following screenshot, by selecting **View details** and then selecting **Cost entries** in the **Cost accounting > Cost control** workspace.

[![Screenshot depicts the Cost entries view and allows users to drill down into the entry details.](media/05-04-cost-entries-14-new.png)](media/04-cost-entries-14-new.png#lightbox)

For example, rent is an expenditure that is distributed to cost centers. Users who want to understand the rent cost that their cost center must carry can drill down to view how rent is calculated.

You can create a new Cost control workspace configuration for a different legal entity and financial dimension by using the built-in configuration steps in the **Cost accounting** module of Finance. Select the **Get started** link on the **Setup** menu. The system asks you to select the legal entity, chart of account, financial dimension (cost object that you want to estimate or allocate cost to), and budget model. You can select the following options:

* **Legal entity**: DEMF
* **Chart of accounts**: Shared
* **Financial dimension**: Cost center
* **Budget model**: Main
* **Budget type**: Original budget

After you complete all the steps, a new Cost control workspace configuration is created automatically. The workspace is available in the Cost control workspace. It pulls required data from the DEMF company to populate data.

[![Screenshot of the newly created Cost control workspace configuration for the DEMF company.](media/05-04-actual-vs-budget-15-new.png)](media/04-actual-vs-budget-15-new.png#lightbox)

To learn more about cost accounting, access the corresponding links in the Summary and resources unit at the end of this module.