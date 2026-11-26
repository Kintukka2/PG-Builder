<!-- https://learn.microsoft.com/en-us/training/modules/mobile-experiences-finance-operations/set-up-dataverse-virtual-entities -->
# Set up Dataverse virtual entities

Completed

* 15 minutes

To build and deploy mobile experiences, you can start by installing the **Finance and Operations Virtual Entity** application. This application makes all OData entities in finance and operations apps available as virtual entities in Dataverse and Microsoft Power Platform. As a result, you can access the data that you need when building and using mobile experiences.

To install the application, follow these steps.

1. Go to [Finance and Operations Virtual Entity](https://appsource.microsoft.com/en-us/product/dynamics-365/mscrm.finance_and_operations_virtual_entity/?azure-portal=true) to download the app.

   Note

   The system will ask you to sign in with your organization credentials to download the app. Ensure that you use the credentials for the Microsoft Power Platform environment that's set up for dual-write in finance and operations apps.
2. Go to **Data management > Dual-write**, and then select the **Environment details** button in the Action Pane.

   [![Screenshot of the Environment details function.](media/03-environment-details.svg)](media/environment-details.svg#lightbox)
3. On the **Environment details** page, the environment name will show in the **Target** section.

   [![Screenshot of the environment name.](media/03-view-environment.svg)](media/view-environment.svg#lightbox)
4. After you've signed in, the system directs you to the Power Platform admin center to install the app.
5. On the **Install Finance and Operations Virtual Entity** page, select the environment that you're installing the app in. This environment name is the one that you identified in the first step.
6. Agree to the terms and then select **Install**.

   [![Screenshot of the environment menu and install button.](media/03-install-app.png)](media/install-app.png#lightbox)

   The install will begin and might take several minutes.
7. Check the status of the install by opening the environment in the Power Platform admin center. Select **Resources > Dynamics 365 apps**.

## Validate Dataverse solutions

To use virtual entities, make sure that you install the following solutions in your environment. Otherwise, virtual entities won't work with finance and operations apps. These solutions are packaged together to allow for easier portability across environments.

* **Dynamics365Company** - This solution adds the Company entity, which all finance and operations apps entities reference with a PrimaryCompanyContext metadata value.
* **MicrosoftOperationsVESupport** - This solution provides the core support for the **Finance and Operations Virtual Entity** feature.
* **MicrosoftOperationsERPCatalog** - This solution provides a list of available finance and operations apps entities through the mserp\_financeandoperationsentity virtual entity.
* **MicrosoftOperationsERPVE** - This solution is the API-managed solution, which contains the generated virtual entities as they're made visible.

To validate the solutions that are installed in Dataverse, follow these steps:

1. Go to [https://make.powerapps.com](https://make.powerapps.com/?azure-portal=true) and sign in.
2. Ensure that you're working in the environment where you installed the app.
3. In the left pane, select **Solutions**.
4. Select the **Managed** tab on the **Solutions** page, where you can view the installed solutions.

   [![Screenshot of the Managed tab on the solutions page.](media/03-solutions.png)](media/solutions.png#lightbox)

Make sure that the solutions and applications that are installed in your environment are being managed and that updates are installed as needed. For more information, see [Manage Dynamics 365 apps](/en-us/power-platform/admin/manage-apps/?azure-portal=true).