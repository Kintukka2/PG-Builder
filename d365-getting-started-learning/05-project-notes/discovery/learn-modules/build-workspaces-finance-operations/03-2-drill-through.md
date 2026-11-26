<!-- https://learn.microsoft.com/en-us/training/modules/build-workspaces-finance-operations/2-drill-through -->
# Create drill-through workspace elements

Completed

* 15 minutes

Drill-through elements might be necessary in a workspace to help you view
additional data within the page. For instance, you might have a view on
your workspace to see the total number of sales, but by selecting a link
in the data, you can access a more detailed view of each sale.

Tiles are buttons added to a workspace that allow the user to view data.
Tiles can display a record count of data, and they can also provide
drill-through access to view more record details. You can create tiles
and add them to a workspace through X++ development. To create a new tile
for a workspace, you first need to create a query to pull the
information and a menu item that uses that query. Then, you must create a
tile that uses the menu item. On the **Workspace** form, you can add a
**Tile** button to the workspace that points at the tile.

[![Screenshot of the Personnel management workspace page.](media/03-tiles.svg)](media/tiles.svg#lightbox)

## Add a tile button to your workspace in the user interface

To add a **Tile** button to your workspace in the user interface, follow these steps:

1. Right-click the dashboard below the header image and select
   **Personalize**.
2. Select the **+Add a workspace** button. A new workspace will be
   created, titled **My Workspace 1**. If the **Full-page apps** feature is turned on, select **Add an app** instead, and then select the option to add a tile for a new workspace.
3. Right-click **My Workspace 1** and enter a new name for your
   workspace.
4. Open the navigation pane and go to **Modules > Accounts
   Receivable > Customers > All customers**.
5. On the Action Pane, select the **Options** tab.
6. In the **Personalize button** group, select **Add to workspace**.
7. In the **Workspace** drop-down menu, select your workspace.
8. In the **Presentation** drop-down menu, select **Tile**.
9. Select **Configure**.
10. In the **Add as** list pane, keep all defaults and select **OK**.
11. Select the **finance and operations** button to return to the
    dashboard.
12. Select your workspace. The tile now shows the properties that you configured.

## Add a tile button to an existing workspace in the developer environment

To add a **Tile** button to an existing workspace, follow these steps:

1. Create a new project in Visual Studio and make sure that the model that your project is in references "Fleet Management." Verify that the model that your project is in references "Fleet Management" by following these steps:
   1. Select the **Dynamics 365** menu. In Visual Studio 2022, select **Extensions > Dynamics 365**.
   2. Select **Model management > Update model parameters**.
   3. Select the model that you are using in the **Model name** drop-down list.
   4. Select **Next**.
   5. Ensure that the **Fleet Management** model is selected in the **References models** screen.
2. With the new project open in the Solution Explorer, right-click the
   project and select **Add > New item**.
3. In the **Add new item** window, select **User Interface** on the left
   pane.
4. Select **Tile** on the middle pane.
5. Name the new tile **MyTile**.
6. Select **Add**.
7. In the **Properties** window for the new MyTile object, select
   **Wide** in the **Size** field.
8. Select **My Tile** in the **Label** field.
9. Select **Display** in the **Menu item type** field.
10. Select **FMSetup** in the **Menu item name** field.
11. Select **Save**.
12. By linking this tile to the FMSetup menu display item, when the tile is selected in the application, it will open the **Fleet Management Setup** page.
13. Now, you will extend the **Reservation management** workspace and add the tile to the **Summary** section.
14. In **Application Explorer**, find the **FMClerkWorkspace** page.
15. Right-click **FMClerkWorkspace** and select **Create extension**.
16. A new form is added to your project called
    **FMClerkWorkspace.Extension**.
17. Right-click **FMClerkWorkspace.Extension**, select **Rename**, and rename the object to **FMClerkWorkspace.myExtension**.
18. Double-click **FMClerkWorkspace.myExtension** to open it in the element designer.
19. On the design pane of the form designer, open **FormTabControl1 > Workspace > PanoramaBody > SummaryTileSection**.
20. Right-click **SummaryTileSection** and select **New > Tile button**.
21. A new control will be added to the form called
    **TileButtonControl1**.
22. Select **TileButtonControl1** and go to the properties window.
23. Select **MyTile** in the **Name** field.
24. Select **MyTile** in the **Tile** field.
25. Select **My Tile** in the **Tile text** field.
26. Save and build the project.
27. To view the new tile, open finance and operations apps, and go to the **Reservation management** workspace. The tile should display in the **Summary** section.