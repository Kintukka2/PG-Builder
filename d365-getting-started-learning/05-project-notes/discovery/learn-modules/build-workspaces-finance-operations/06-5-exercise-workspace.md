<!-- https://learn.microsoft.com/en-us/training/modules/build-workspaces-finance-operations/5-exercise -->
<!-- refetched: original harvest URL returned 404 -->
# Exercise - Create a workspace and add a tile, list, link, and Power BI element

Completed

* 25 minutes

Watch this video to see how to build a custom workspace.

## Scenario

As a customer relations manager, you want to create a workspace to quickly view certain information. You want to see the total number of customers and be able to drill through to see more details on customers. You also want to see a list of all the leads that you can filter. You only need to see the date that the lead was opened, the lead ID, status of the lead, the subject of the lead, and comments made on the lead. A chart of the sales of customer groups would be useful, as would having a way to quickly go from the workspace to the quotations page.

## Before you begin

To complete this exercise, you will need access to an environment that has a standard sample of data in finance and operations apps, and is connected to Power BI.

To connect your environment to Power BI, a system administrator must first register an application in Microsoft Entra ID for the environment and grant it delegated Power BI Service permissions. The registration provides the **Application (client) ID** and a client secret value that are required in the following steps.

1. Go to **System administration > Setup > PowerBI.com configuration**.
2. Select **Edit** and set the **Enabled** option to **Yes**.
3. In the **Application ID** field, enter the **Application (client) ID** value from the Microsoft Entra ID app registration.
4. In the **Application key** field, enter the client secret value from the app registration.
5. Select **Save**.

## Create a new workspace

1. Open the user interface.
2. On the **Home** screen, right-click in the workspace area.
3. Select the **Personalize: Workspaces** option.
4. Select the **Add a Workspace** option. If the **Full-page apps** feature is turned on, select **Add an app** instead, and then select the option to add a tile for a new workspace.
5. Right-click the **My Workspace 1** tile.
6. Select the **Personalize: My Workspace 1** option.
7. In the **Text** field, enter **CRM**.

## Add a tile to your workspace

1. Open **Sales and marketing > Customers > All customers**.
2. Select the **Options** tab on the Action Pane.
3. In the **Personalize** section, select **Add to workspace**.
4. In the drop-down form, select **CRM** in the **Workspace** field.
5. Select the **Tile** option in the **Presentation** field.
6. Select the **Configure** button.
7. On the **Add as tile** form, enter **Customers** in the **Name on
   tile** field.
8. Select **Yes** on the **Show count on the tile** field and then select **OK**.

## Add a list to your workspace

1. Open **Sales and marketing > Relationships > Leads > All leads**.
2. Select the **Options** tab on the Action Pane.
3. In the **Personalize** section, select **Add to workspace**.
4. In the drop-down form, select **CRM** in the **Workspace** field.
5. Select **List** in the **Presentation** field.
6. Select the **Configure** button.
7. On the **Add as list** form, enter **Leads** in the **Name for tab**
   field.
8. In the **List style** field, select the **Tabular (up to 8
   columns)** option.
9. Select the check box for the following columns:
   * Date opened
   * Lead ID
   * Status
   * Subject
   * Name
   * Comments
10. Select **OK**.

## Add a link to your workspace

1. Open **Sales and marketing > Relationships > Opportunities > All opportunities**.
2. Select the **Options** tab on the Action Pane.
3. In the **Personalize** section, select **Add to workspace**.
4. In the drop-down form, select **CRM** in the **Workspace** field.
5. Select **Link** in the **Presentation** field.
6. Select the **Configure** button.
7. On the **Add as link** form, enter **Opportunities** in the **Name**
   field.
8. On the **Group name** field, enter **Favorites**.
9. Select the **OK** button.
10. Close the page.

## Embed a Power BI report

1. To embed a Power BI report, open your CRM workspace.
2. On the Action Pane, select the **Options** tab.
3. Select **Personalize this page**.
4. A personalization menu will appear. Select the **Add a field** button.
5. Select an open area on the workspace form.
6. A **Workspace options** sidebar will appear. Set the **Allow Power BI
   Control** option to **Yes** and then select **OK**.
7. In the workspace, the Power BI tile will be available. In the **Power
   BI** tile, select **Get started**.
8. When prompted on the Authorize Power BI side pane, select **Click here to provide authorization to Power BI**.
9. When you are connected, you will have a list of available Power BI
   reports. Select the **Sales** tab.
10. Select the **Sales by Customer Group** chart.
11. Select **OK** to embed the Power BI reports to your workspace.