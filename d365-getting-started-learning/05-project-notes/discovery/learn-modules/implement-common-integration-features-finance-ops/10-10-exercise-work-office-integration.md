<!-- https://learn.microsoft.com/en-us/training/modules/implement-common-integration-features-finance-ops/10-exercise-1 -->
<!-- refetched: original harvest URL returned 404 -->
# Exercise - Work with Microsoft Office integration

Completed

* 30 minutes

## Scenario - Use and build office integration in finance and operations

You want to use and build office integration in finance and operations.

### Load the Fleet management data set

1. In the company **USMF**, open **Fleet Management > Setup > Fleet setup**.
2. Select **Create**.
3. When the sample data is created, select **Close** in the **Sample data created** message.
4. **Close** the message.

### Static Export to Excel

1. Go to **Fleet Management > Customers > Customer**.
2. Select the **Open in Microsoft Office** icon in the top-right of the page, next to the Power Apps icon. it may take a couple of minutes in the virtual machine environment to open the list.
3. Select **Customers** in the **Export to Excel** section.
4. Download and open the workbook that is generated. Note that the columns in the workbook match the columns in the **Customer** grid.
5. Close the Excel file.
6. In finance and operations, select the first two rows by selecting in the left edge of the row, below the **Select all** check box in the **Customer** page.
7. Right-click in the grid to open the shortcut menu. Note that both **Export all rows** and **Export marked rows** are available as commands.
8. Select **Export marked rows**.
9. Download and open the workbook that is generated. Note that the columns in the workbook match the columns in the grid, and that the rows that are exported match the rows that you selected.
10. Close the Excel file.

### Generated Open in Excel

1. In **Fleet Management > Customers > Customer** select all customers.
2. Select the **Open in Microsoft Office** icon.
3. Select **Fleet Management Customers (unfiltered)** in the **Open in Excel** section.
4. Download and open the workbook that is generated. This workbook contains the Excel Data Connector App, a binding to the Fleet Management Customer entity, and a pointer to the server that the workbook was generated from.
5. Select **Enable Editing** in the excel file.
6. Select **Accept and Continue** in the **New Office Add-in** page on the right side of the Excel file.
7. Select **Sign-in**.
8. Use the credentials provided in the **Azure Portal** section of the **Resources** tab in the right pane of the online lab environment.
9. In the **Customer** page in finance and operations, select **Edit** (or press F2) and change the email address of one of the customers.
10. Select **Save**.
11. In Excel, in the **Data Connector** app, select **Refresh**. Note that the new email address is shown in Excel.
12. In Excel, change the email address of one of the customers.
13. In the **Data Connector** app in Excel, select **Publish**.
14. In finance and operations, select **Refresh** in the upper right of the page (or press Shift+F5).
15. Note that the new email address is shown on the **Customer** page in finance and operations apps.
16. In Excel, select the **Open options dialog** (gear) button in the upper-right corner of the **Data Connector** app. You can use the dialog box that appears to adjust the settings in the current workbook. Note that the **Server URL** value matches the start of the URL that is shown in an internet browser. Also note that the data refresh and data publish operations are listed in the **Data Connector** section.
17. Select **Cancel** to close the **Options** dialog box.
18. Select the **Open message center** (flag) button in the lower-right corner of the Excel app. The message center dialog box that appears provides information about what is occurring in the Excel app.
19. Select **Done**. Do not close Excel.

### Add and remove table columns from an existing table data source in the Excel app

1. In the **Data Connector** app in Excel, select **Design**. A list of table and field data sources appears.
2. Select the **Edit** (pencil) button next to the existing table data source. The data source details are shown.
3. Remove fields. In the **Selected fields** list, double-click a field. Alternatively, select a field, and then select **Remove**. To select multiple fields, hold down the Ctrl key while you select the fields. To select all fields, press Ctrl+A.
4. Add fields. In the **Available fields** list, double-click a field. Alternatively, select a field, and then select **Add**. To select multiple fields, hold down the Ctrl key while you select the fields. To select all fields, press Ctrl+A.
5. Change the field order. In the **Selected** list, select a field, and then select **Up** or **Down**.
6. Change a field label. In the **Selected** list, select a field, and then select the **Column label** field below the list. You can change the label to either a static string or a label identifier that will be translated to the active language (for example '@SYS129977').
7. To apply the changes that you made to data source fields, select **Update** to return to the data source list.
8. Select **Yes** to continue.
9. Select **Done**.
10. Select **Refresh** to make sure that any new fields are filled with data.
11. Select **Yes** in the **Confirm Refresh** window that appears.
12. Close the excel file, and don't save the changes.

## Scenario - Use the Excel workbook designer

You need to use the **Excel workbook designer** page to create an **Open in Excel** experience for the company **USMF**.

1. Go to **Common** > **Common** > **Office integration** > **Excel workbook designer** (it may take a few seconds to open).
2. Select the **FleetCustomer** entity (you can use the **Search** field on the left to find it).
3. Add all fields in the list of available fields to the list of selected fields, by using the **Add all** button.
4. Select **Create workbook**.
5. Select **Download** and then open the workbook that is generated.
6. Enable editing in the workbook. This workbook contains the Excel Data Connector App, a binding to the **Fleet Management Customer** entity, and a pointer to the server that the workbook was generated from.
7. Select **Enable Editing** in the excel file.
8. If a pop up shows, you must enable the Excel Data Connector App to load. Select **Trust this add-in** in **New Office add-in** window. If the pop-up does not appear, skip to step 12.
9. You will then be redirected to a **Sign-in** page.
10. Use the same credentials you used on the Microsoft **Sign-in** page to log in to finance and operations. You can find them in the **Resources** tab in the right pane.
11. After successful sign-in, customer data is read from the OData service on the server and added to the table.
12. Insert a blank row above the table headings row, and enter **Fleet Customers** as the title.
13. Rename the worksheet **FleetCustomers** by saving it on the desktop with the new name.

### Rearrange some of the fields in the table.

1. Select **Design** in the Data Connecter to open the designer experience.
2. Next to the **Fleet Management Customers** data source are buttons for editing and deleting the data source. Select **Edit** to view the field list. You might need to enlarge the Data Connector to see all sections.
3. Select fields from the **Selected fields** section and use the **Up** and **Down** buttons. Set the sequence for the first three fields to **FirstName, LastName**, and **DriverLicense**.
4. Select **Update**. Note that the field order in the Excel sheet is changed.
5. Select **Done**.
6. Select the **Open options dialog** (gear) button in the Data Connector.
7. Select **Clear binding data** in the **Data Connector** section, so that the workbook contains no bound data.
8. Select **OK**.
9. Save the workbook as **FleetCustomersBasic.xlsx** on the desktop.
10. In finance and operations, go to **Common** > **Common** > **Office integration** > **Document templates**.
11. Select **New**.
12. Browse to the **FleetCustomersBasic.xlsx** file that you just saved.
13. Select **Open** and then **OK**. The template is added as a line in the **Document templates** page.
14. In the **FleetCustomersBasic** row, change the **Template name** value to **Fleet Customers Basic**.
15. Select **Save**.
16. Close the **Document templates** page.
17. Go to **Fleet Management** > **Customers** > **Customer**.
18. Note that **Fleet Customers Basic** is now an option in the **Open in Excel** section, now select it.
19. Select **Download**, and then **Open**.
20. Select **Enable Editing** in the excel file.

You can also try to use the designer experience in the Excel add-in to add another data source to another worksheet.