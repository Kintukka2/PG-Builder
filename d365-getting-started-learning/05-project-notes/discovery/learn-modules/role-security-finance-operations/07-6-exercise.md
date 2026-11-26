<!-- https://learn.microsoft.com/en-us/training/modules/role-security-finance-operations/6-exercise -->
# Exercise - Create a new security role and add duties

Completed

* 20 minutes

## Scenario

The finance and operations apps developer has been asked by the Fleet
Management company to create a new role based on a new position that they are filling for a Fleet Service Manager. The manager needs duties to manage cars and customers, as well as the basic duties that are associated with Fleet Management.

## Create a new project

1. Minimize the Microsoft Edge window.
2. Open Visual Studio.
3. Select **Yes** in the **Do you want to allow this app to make changes to your device?** window.
4. Select **Continue without code**.
5. Open the **File** menu and select **New > Project**.
6. Ensure that **Finance Operations** is selected in the **Recent project templates** section, and then select **Next**.
7. In the **Configure your new project** dialog box, enter **FleetManagementSecurityProject** in the **Project name** field.
8. Select **Create**.
9. Select **Dynamics 365** in the **Extensions** menu.
10. Select **Options**.
11. Under the **Dynamics 365** node on the left pane, select
    **Projects**.
12. Ensure the check boxes for **Organize projects by element type** and **Synchronize database on build for newly created project** are selected.
13. Select **OK**.

## Create the FMServiceManager role

1. In the **Solution Explorer** window, right-click
   **FleetManagementSecurityProject**.
2. Select **Add > New Item**.
3. In the left column, under the **Dynamics 365 Items** node, select **Security**.
4. In the middle column, select **Security Role**.
5. In the **Name** field at the bottom of the page, enter **FMServiceManager**.
6. Select **Add** to add the new security role to your project. The **FMServiceManager** role will now be open in the element designer window.

## Add duties to the FMServiceManager role

1. Select **View**, and then **Application Explorer**.
2. In the **Application Explorer**, in the **AOT**, expand the **Security** node.
3. In the **Application Explorer** window, in the **AOT**, expand the **Security** node.
4. Expand the **Security Duties** node.
5. Select and drag the **FMBasicDuties** duty from the **AOT** in the **Application Explorer** window to the element designer window (in the middle of the page) in the **Duties** node beneath the **FMServiceManager** role.
6. Select and drag the **FMManageCars** duty from the **AOT** in the **Application Explorer** window to the element designer window in the **Duties** node beneath the **FMServiceManager** role.
7. Select and drag the **FMManageCustomers** duty from the **AOT** in the **Application Explorer** window to the element designer window in the **Duties** node beneath the **FMServiceManager** role. You should have three duties under the **Duties** node now, **FMBasicDuties**, and **FMManageCars**.
8. Perform a build by right-clicking the project
   **FleetManagementSecurityProject** in the **Solution Explorer** window and selecting **Build**.

You may see an error because the batch server needs to be turned off in the environment. However, this does not affect the build. This may be because of a batch job that is currently running in the environment that would be interfering with any of the objects, such as security privileges, in the current build. Stopping the batch server would prevent an error occurring because of any currently running batch jobs.