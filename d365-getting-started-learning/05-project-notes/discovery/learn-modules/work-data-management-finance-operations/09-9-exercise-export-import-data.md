<!-- https://learn.microsoft.com/en-us/training/modules/work-data-management-finance-operations/9-exercise-2 -->
<!-- refetched: original harvest URL returned 404 -->
# Exercise - Export data using the Data management workspace

Completed

* 15 minutes

## Scenario

In this exercise, you export data from the **All customers** entity by using the **Data management** workspace.

1. In the company **USMF**, go to **Workspaces > Data management**.
2. You will see the message **Execution history was successful** in the **Action center**.
3. Select **Export** in the **Data management** workspace.
4. Specify the following information on the page:
   * **Group name** - Customers Export
   * **Description** - Customer Export
   * **Data project operation type** - Export
   * **Project category** - Project
   * **Generate data package** - Yes
5. Select **Save** in the Action Pane.
6. In the **Selected entities** FastTab, select **Add entity**.
7. Specify the following information in the **Add entity** dialog:
   * **Entity name** - Select any of the Entity names from the drop-down list.
   * **Target data format** - EXCEL
   * **Select fields** - Importable fields
8. Select **Add**. A new line will be created with the entity information you defined.
9. Review any warnings, and then select **Close**.
10. Select the entity line, and then select **Export** in the Action Pane. The data job will run.
11. When the **Batch job is scheduled** dialog box appears. select **Close**.
12. Select **Refresh** when the job is complete (if the **Refresh** button is not displayed return to the previous page by using **Click to go back** on the browser page, and again select **Export**. Now the **Refresh** button will appear on the **Execution summary** page). You will receive a notification that the export is completed.
13. Select **Download package** in the Action Pane. A .zip file will download.
14. Open the .zip file and then open the Excel file that is in the .zip file.
15. Here you will see all the data that exported from finance and operations.