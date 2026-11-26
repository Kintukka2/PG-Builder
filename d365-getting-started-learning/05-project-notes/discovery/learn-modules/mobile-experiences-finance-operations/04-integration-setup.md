<!-- https://learn.microsoft.com/en-us/training/modules/mobile-experiences-finance-operations/integration-setup -->
# Integration setup

Completed

* 20 minutes

After the **Finance and Operations Virtual Entity** app is installed and you've verified that the necessary solutions are installed in your environment, you need to set up Dataverse and finance and operations apps so that they can connect to each other.

Dataverse will call finance and operations apps by using S2S authentication, which is based on a Microsoft Entra ID application. This Microsoft Entra ID application is a single instance of your Dataverse environment.

[![Diagram of the Azure authentication.](media/04-azure-authentication.png)](media/azure-authentication.png#lightbox)

To register the app in the Azure portal, follow these steps.

Note

Make sure that you set up the Microsoft Entra ID application on the same tenant as your finance and operations apps instance.

1. Go to [https://portal.azure.com](https://portal.azure.com/?azure-portal=true).
2. Go to **All services > App registrations**, and then select **New registration**.
3. Enter the following information on the page:

   * **Name** - Unique name for the app registration
   * **Account type** - Select who you want to use the application or have access to the API
   * **Redirect URI** - Leave blank
4. Select **Register**.
5. Note the **Application (client) ID** value because you use it later.
6. Create a symmetric key for the application, which you use to encrypt and decrypt information.
7. Select **Certificates & secrets** in the left pane.
8. Select **New client secret**.
9. Enter a **Description** and then specify an expiration period.
10. Select **Add**.
11. Copy and save the **Value** and **Secret ID** for later.

## Grant app permissions in finance and operations apps

Dataverse uses the Microsoft Entra ID application that you created to call finance and operations apps. You need to set up the application as trusted by finance and operations apps and as associated with a user account that has correct rights.

Next, you need to create a special service user who has rights to only the virtual entity functionality; the user must have no other rights. After you've completed these tasks, any application that has the Microsoft Entra ID application secret that you created can call this finance and operations apps environment and access the virtual entity functionality.

To set up the new user, follow these steps:

1. In finance and operations apps, go to **System administration > Users > Users**.
2. Select **New** in the Action Pane.
3. For the new user record, enter the following information:

   * **User ID** - dataverseintegration
   * **User name** - Dataverse Integration
   * **Provider** - NonAAD
   * **Email** - dataverseintegration (or any value you that you want; it doesn't need to be a valid email)
4. Select **Save**.
5. On the **User roles** FastTab, select **Assign roles**.
6. Select the **Dataverse Virtual entity integration app** role and then select **OK**.
7. Remove other roles that are assigned to the user, including the System user role.
8. Select the role to remove and then select **Remove role**.
9. Go to **System administration > Setup > Microsoft Entra ID applications**.
10. Select **New** in the Action Pane.
11. Enter the **Client ID** that you previously saved. The **Client ID** is the Microsoft Entra ID application that you created.
12. Enter a name in the **Name** field.
13. Select the **User ID** that you previously created.
14. Select **Save** and then close the page.

## Set up the virtual entity data source

The last step in the configuration process is to provide Dataverse with the finance and operations apps instance to connect to. You complete this task in Microsoft Power Platform.

1. Go to [https://powerapps.microsoft.com](https://powerapps.microsoft.com/?azure-portal=true) and sign in.
2. In the upper-right corner of the page, select the gear icon and then select **Advanced settings**.
3. Select the **Settings** menu and then select **Administration > Virtual Entity Data Sources**.

   [![Screenshot of the admin settings.](media/04-admin-settings.svg)](media/admin-settings.svg#lightbox)
4. Locate and select the **Finance and Operations** data source in the list.
5. Enter the information in the following fields. (You saved these values in previous steps).

   * **Target URL** - The URL that you use to access finance and operations apps
   * **OAuth URL** - `https://login.windows.net/`
   * **Tenant ID** - Your tenant, such as **contoso.com**
   * **AAD Application ID** - The **Application (client) ID** that you previously created
   * **AAD Application Secret** - The secret that you previously generated
   * **AAD Resource** - Enter **00000015-0000-0000-c000-000000000000** (this value is the Microsoft Entra ID application that represents finance and operations apps; it should always be this same value)
6. Save your changes.