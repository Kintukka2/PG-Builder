<!-- https://learn.microsoft.com/en-us/training/modules/describe-report-integration/5-describe-power-platform-integration -->
<!-- refetched: original harvest URL returned 404 -->
# Describe integration options for Microsoft Power Platform

Completed

* 8 minutes

The current versions of finance and operations apps are hosted on Azure, which helps increase the integration scope of these products. These apps can connect to several other products hosted in Azure. They can also connect to the on-premises applications by using a gateway. The following sections explore the finance and operations apps integration capabilities with Microsoft Power Platform.

## Microsoft Power Platform

Microsoft Power Platform provides a suite of capabilities for finance and operations apps. Features like dual-write and virtual entity can establish direct integration between Microsoft Dataverse and data entities of finance and operations apps.

Microsoft Power Platform is made up of tools like canvas apps, Power Automate, and Power BI. All these tools can be individually integrated with finance and operations apps.

## Integration with Dataverse

Dataverse is the default data storage option for Microsoft Power Platform, where you can securely store your business data in tabular format, maintaining key and table relationships. Finance and operations apps, such as Finance, Supply Chain Management, and Commerce, store data in Azure SQL. However, you can integrate finance and operations apps with Dataverse by using the data entity framework. Several technologies are involved to achieve this integration.

### Dual-write

Dual-write is a standard integration platform that provides near-real-time interaction between Dataverse and finance and operations apps. It provides a tightly coupled, bidirectional integration capability, delivering a user-friendly experience across the apps.

Dual-write infrastructure follows a no-code/low-code principle, minimizing engineering effort to map standard or custom tables between apps. Dual-write supports both online and offline modes of operations.

![Diagram that shows how dual-write supports both online and offline modes of operation.](media/05-2-5-dataverse.png)

### Virtual entity

Virtual entities let you access data from external systems in Dataverse as if it were stored there, without copying the data. Finance and operations app data can be used as virtual entities in Dataverse, allowing full create, read, update, and delete (CRUD) operations directly from Dataverse.

All OData entities in finance and operations apps are available as virtual entities in Dataverse and therefore also in Microsoft Power Platform. You can create a model-driven app by using the virtual entities and perform the CRUD operations directly on the finance and operations data source from your model-driven app.

[![Diagram that shows how to execute the CRUD operation directly on the finance and operations data source from your model-driven app.](media/05-2-5-dual-write.png)](media/2-5-dual-write.png#lightbox)

## Integration with a Power Apps canvas app

A Power Apps canvas app is a no-code app development platform in Microsoft Power Platform. It has the capability to connect to various data sources using the built-in or custom connectors. To build a canvas app, you need to drag the control elements and drop them onto the canvas, designed for a mobile device or tablet. You can achieve canvas app integration with finance and operations apps in the following two ways.

### Embed a canvas app in finance and operations apps

To embed a canvas app, first navigate to the desired page in the finance and operations app. In the upper-right corner, select the **Power Apps** icon, then choose **Add an app**. This option allows you to connect a Power Apps canvas app to the current page.

![Screenshot of the options available in the upper-right corner of the page with the icon to embed a Microsoft Power Apps canvas app highlighted.](media/05-2-5-power-app-button.png)

You can select the **Add an app** button under the **Power Apps** icon to embed the canvas app into the finance and operations apps. The following dialog box appears in the right panel of the finance and operations apps.

![Screenshot of the dialog box to provide the Power Apps canvas app details.](media/05-2-5-power-apps.png)

You need to enter the following information:

* **Name**: The name of the canvas app.
* **App ID**: The app ID of the canvas app. You can select your canvas app to embed and select the **Details** button in the Action Pane of the Power Apps maker portal to get the app ID of the canvas app.
* **Input context for the app**: You can select a column from the data source of the current page of the finance and operations app. This field value is passed as a parameter to the canvas app for further data processing.
* **Application size**: You can select **Thin** or **Wide**. The canvas app is embedded in the finance and operations apps user interface based on your selection.

You can perform CRUD operations in the canvas app, which is embedded in the finance and operations app. The record in the canvas app will be related to the record selected in the finance and operations apps.

### Connect a finance and operations data source from a canvas app

You can directly connect to a finance and operations data source from the Power Apps canvas app by using the **Fin & Ops Apps (Dynamics 365)** data connector.

This capability enables you to create a mobile app using a Power Apps canvas app that has finance and operations as the back-end data source. This mobile app can perform all CRUD operations directly in the finance and operations apps database. All OData entities in finance and operations apps are available as data sources for the canvas app. For custom tables, you can create custom OData endpoints, which can be connected to the canvas app for the mobile app development activity.

The following video demonstrates how Power Apps can be integrated with finance and operations apps.

This integration is possible even if the back-end data source of the canvas app is any third-party application.

## Integration with Power Automate

Power Automate is an online workflow service that automates actions across the most common apps and services. It can connect to multiple applications using data connectors and passes parameters across apps and services. Power Automate has a connector for finance and operations apps, which helps connect all the OData entities in finance and operations apps and performs CRUD operations on those entities. Power Automate primarily has two components: trigger and actions.

### Trigger

The **Fin & Ops Apps (Dynamics 365)** connector for Power Automate has a single trigger that can be initiated from a business event.

Business events provide a mechanism that lets external systems receive notifications from finance and operations apps. In this way, the systems can perform business actions in response to business events.

Business events occur when a business process is run. During a business process, users who participate in it perform business actions to complete the tasks that make up the business process.

### Action

The **Fin & Ops Apps (Dynamics 365)** connector for Power Automate supports several actions to perform on finance and operations apps.

You can create, update, and delete data in your finance and operations apps. You can also read records and perform custom actions on the records based on business requirements. You can also connect other data connectors, such as Dataverse, SharePoint, and Outlook, with the **Fin & Ops Apps (Dynamics 365)** connector. This capability enables you to pass on data between the finance and operations apps and the other connected apps.

You can perform the following list of actions from Power Automate in finance and operations apps.

* **Create Record**: This action can be used to create a new record in finance and operations apps. Once the data entity is selected, all the columns of the selected entity are available to be updated in the connector. The values to be inserted in each column can be updated in Power Automate. Once Power Automate executes, a new record is created in the finance and operations underlying tables of the data entity.
* **Lists items present in table**: This action can be used to get the list of records from an entity. This action supports cross-company reading of data.
* **Delete record**: This action can be used to delete an existing data record for a data entity. The usage is the same as the Get a record action.
* **Execute action**: This action can be used to invoke methods on a data entity to perform a business action.
* **Get a record**: This action can be used to fetch a record for a specific data entity from the target instance.
* **Get list of entities**: This action can be used to get the list of entities for further use in the app that's being developed.
* **Update a record**: This action can be used to update an existing data record for a data entity. The usage is the same as for the **Create Record** action.