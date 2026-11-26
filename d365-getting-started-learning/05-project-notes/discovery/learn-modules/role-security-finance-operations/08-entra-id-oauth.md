<!-- https://learn.microsoft.com/en-us/training/modules/role-security-finance-operations/entra-id-oauth -->
# Microsoft Entra ID and OAuth 2.0 authentication

Completed

* 10 minutes

Finance and operations apps use Microsoft Entra ID (formerly Microsoft Azure Active Directory) for authentication. OAuth 2.0 authentications allow integrations on behalf of a user. OAuth is an abbreviation for “Open Authorization.”

To access finance and operations apps and be assigned to a role, a user must have an authenticated Microsoft Entra ID account. By default, only authenticated users with user rights can establish a connection.

Microsoft Entra ID is a primary identity provider. To access the system, users must be provisioned into a finance and operations apps instance and should have a valid Microsoft Entra ID account in an authorized tenant.

OAuth 2.0 is a standard that allows a website or application to access resources, on behalf of a user, that other web apps are hosting, as shown in the following diagram.

[![Diagram of how Microsoft Entra ID and OAuth 2.0 work with data security in finance and operations apps.](media/08-diagram-security.png)](media/diagram-security.png#lightbox)

For finance and operations apps, OAuth 2.0 provides authentication for the web application programming interface (API), services, and integrations.

## OAuth 2.0

In finance and operations apps, OAuth 2.0 is used for integrations to allow external systems to access it in the following scenarios:

* Batch data API
* OData
* Custom services
* Data management package API
* Other integration scenarios

To register finance and operations apps with OAuth 2.0 in Microsoft Entra ID, follow these steps:

1. Go to portal.azure.com.
2. Search for **App Registrations** and then select **New registration**.
3. Choose the appropriate option under **Supported Account Type**. The most common option is **Single tenant**.
4. Enter the applicable Redirect URI, which should be your environment’s URL and your environment’s URL + /OAuth, as the following image depicts.

   [![Screenshots of Redirect URLs.](media/08-redirect-urls.png)](media/redirect-urls.png#lightbox)
5. Select **Register**, and then select **Certificates & secrets** in the navigation pane.
6. Select **New client secret**, and then enter a description and expiration period.
7. Select **Add** to create the secret.
8. Copy the value to a text document. Remember to save the value because you won’t be able to copy it later.
9. Select **API permissions** in the navigation pane and then select **Add a permission** > **Dynamics ERP**.
10. Select **Delegated permissions** and then enable **Ax.FullAccess**, **CustomService.FullAccess**, and **Odata.FullAccess**.
11. Select **Add permissions** to close the dialog.
12. Select **Overview** in the navigation pane.
13. Copy the **Application (client) ID** and the **Directory (tenant)** to the same text document in which the **Directory (tenant) ID** value resides.

Now setup continues in finance and operation apps.

## Set up finance and operations apps

Follow these steps to set up finance and operations apps:

1. Sign in to the finance and operations apps environment, and then select **System Administration** > **Setup** >**Microsoft Entra ID Applications**.
2. Enter the client ID from the app registration in Azure.
3. Enter a name and a user ID, and then select **Save**.

Now, you can generate an authentication token based on the value from the secret, the Application (client) ID, and the Directory (tenant) ID.