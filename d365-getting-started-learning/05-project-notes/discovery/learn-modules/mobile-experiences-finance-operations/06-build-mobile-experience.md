<!-- https://learn.microsoft.com/en-us/training/modules/mobile-experiences-finance-operations/build-mobile-experience -->
# Build a mobile experience

Completed

* 10 minutes

After you've completed setting up the connection between Microsoft Power Platform and finance and operations apps, you can build mobile experiences by using finance and operations apps data.

We recommend that you have a functional knowledge of Microsoft Power Platform before you begin building mobile experiences. For more information, see the following resources.

* [Get started using Dataverse](/en-us/training/paths/get-started-cds/?azure-portal=true)
* [Create a canvas app in Power Apps](/en-us/training/paths/create-powerapps/?azure-portal=true)
* [Create a model-driven application in Power Apps](/en-us/training/paths/create-app-models-business-processes/?azure-portal=true)

## Connect to finance and operations apps data

You need to determine which data you need to connect to and the type of Microsoft Power Apps application that you plan to build. Then, you can connect to your finance and operations apps data and build a mobile experience.

To create a new canvas app and connect to finance and operations apps data, follow these steps.

1. Go to [https://make.powerapps.com](https://make.powerapps.com/?azure-portal=true) and sign in.
2. Select **Create** in the left pane.
3. On the **Create your app** page, select the **More data sources** button.

   [![Screenshot of the create an app page.](media/06-create.svg)](media/create.svg#lightbox)
4. Begin setting up your connection to finance and operations apps by selecting **New connection**.
5. Select the **Fin & Ops Apps (Dynamics 365)** connection and then select **Create**.

   [![Screenshot of the connections with a create button.](media/06-connections.svg)](media/connections.svg#lightbox)
6. The system prompts you to sign in. Use the credentials that you use to sign in to finance and operations apps.
7. After you've signed in, select a dataset. The dataset represents your finance and operations apps environment deployments. Select the environment that you want to connect to.
8. On the **Choose a table** page, select the data that you want to connect to. Then, select **Connect** in the lower-right corner of the page. You can connect to other datasets if needed.

Note

The datasets that show on the **Choose a table** page are data entities within your finance and operations apps environments. If you can't locate a dataset, make sure that the data entity that you need to connect to is enabled for Public API. For more information, see [Build and consume data entities](/en-us/dynamics365/fin-ops-core/dev-itpro/data-entities/build-consuming-data-entities/?azure-portal=true).