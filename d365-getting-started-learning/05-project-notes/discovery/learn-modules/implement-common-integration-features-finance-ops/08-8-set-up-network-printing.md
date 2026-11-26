<!-- https://learn.microsoft.com/en-us/training/modules/implement-common-integration-features-finance-ops/8-network-print -->
<!-- refetched: original harvest URL returned 404 -->
# Print management

Completed

* 20 minutes

For printing requirements, consider the following capabilities that are available for designing and printing business documents:

* To access local and network printers, install the **Document Routing Agent** feature. You can use Document Routing Agent for interactive and non-interactive printing. However, we recommend that you use it for non-interactive printing (high-volume printing labels, invoices, and more).
* Use the embedded PDF preview option for interactive printing. To do so, open the SSRS report directly in PDF format and then download it or print it on an available local/network printer.
* Many SSRS reports are available for business documents that support printing. For specific scenarios, the option to install modern design templates from Microsoft Dynamics 365 Lifecycle Services is available for some reports.
* For warehouse operations, you can customize and print license plate labels and barcodes in different formats.
* Consider the Financial report designer and Electronic Reporting capabilities to set up reports that you can print. Use configurable business documents options for Electronic reporting to change layouts of the reports to meet business needs.
* Often, you can use Excel and Word templates for print management for some default business documents templates.

# Network printing

Finance and operations apps provide integrated services and client applications to help make it easier for you to generate, store, and distribute documents that support business activity.

You can print documents by using a local printer or a network-connected device. You can also export finance and operations apps pages and reports directly from the client as PDF files or Microsoft Office documents.

With the distributed workload, you can print business documents directly from a mobile device by using network resources. Though printing requirements might vary, all industries typically must create hard copies of business documents by using finance and operations apps.

Printing documents on network devices from hosted applications presents a unique set of challenges, such as:

* Print drivers might not be available on the user's device.
* The user's device might not be connected to the corporate network.

By using a dedicated host and following a few simple steps, system administrators can set up deployments so that users can print directly from business applications on network devices.

## Printing scenarios

The following scenarios describe the various types of printing that you can accomplish with finance and operations apps:

* **Printing what's shown** – To print what's currently shown in the internet browser, when you print, the system will generate a "print-friendly" version of the webpage for the browser. This capability is supported by the browser's rendering of the HTML5 client.
* **Interactive printing** – You can export a PDF version of the report and download it to the browser to print a precision document on a locally connected device. This capability uses client applications and Microsoft 365 services. To view the PDF files, you'll need to install Adobe Acrobat Reader.
* **Printing on a network device** – You can send a precision document to a domain printer device. The system will send the precision document to a client application that runs on a server that's hosted in the customer's domain. This capability requires support from client applications and from services that are hosted in Microsoft Azure.

In addition to the platform that's deployed to the Azure subscription, finance and operations apps provide customers with an integrated, Microsoft Azure application that helps them use domain-hosted devices to print documents.

All legal entities (also known as companies) that are defined in the environment can use network printers that are registered for finance and operations apps. Network printer settings are company-specific. Therefore, administrators can restrict access based on the user's active company.

For example, users in the active company might have access to all network printers that are registered by the Document Routing Agent. However, users in another company won't have access to those printers until access is explicitly enabled for that company.

## Service overview

While documents that are produced by the hosted applications are waiting to be printed on a network-connected device, they're stored in Microsoft Azure Blob Storage.
The implementation sequence is as follows:

1. Microsoft SQL Server Reporting Services (SSRS) generates the report and stores it in Azure Blob Storage. Attached printer settings are stored together with the document.
2. The Document Routing Agent queries the Azure Service Bus queue for active jobs.
3. The document is downloaded by the Document Routing Agent and spooled to the network printer.

With the client-based solution, customers can manage the scale of their printing needs. Customers who have heavy-volume printing workloads can install many document routing agents to increase the number of concurrent printing operations. Alternatively, some customers require few installations of a document routing agent to handle their anticipated printing needs.

## Install the Document Routing Agent to enable network printing

You can enable network printers for specific companies by using in-client administrative pages. However, to access the network printing resources, you'll require Microsoft Active Directory Domain Services (AD DS) authentication. The Microsoft Entra account that's used to set up the Document Routing Agent must share the same domain as the Azure tenant.

## Install the Document Routing Agent

Finance and operations apps uses the Document Routing Agent feature to manage the spooling of documents to network printer devices. You can obtain the client by using direct links that are embedded in the web application. Use the following procedure to download the application to your local computer. Then, you can access local and network printers, which are connected to your computer, from a single deployment of finance and operations apps.

1. Open the **Manage network printers** page by going to **Organization administration > Setup > Network printers**.
2. On the **Options** tab, in the **Application** group, select **Download document routing agent installer**.
3. If you haven't installed Adobe Acrobat Reader, you'll need to do so prior to proceeding to the next step.
4. Run the downloaded file to begin the installation process.
5. Complete the setup process.

After the application has been installed, you can begin to register local printers as network printers for finance and operations apps.

## Set up the Document Routing Agent

Use the following procedure to set up the client application so that it can communicate with the Azure services that host the documents that are in progress.

1. Close all browser instances that are running finance and operations apps. This step resets the local Azure authentication tokens.
2. From your computer, run **Document Routing** by selecting the shortcut on your desktop or by running *Microsoft.Dynamics.AX.Framework.DocumentRouting.Agent.exe*.
3. On the toolbar, select **Settings**.
   The system automatically enters the **Application ID**, which is unique to the application.
4. In the **finance and operations apps URL** field, enter the base URL of the finance and operations apps instance that you're using.
5. In the **Microsoft Entra tenant** field, enter the domain name of the Microsoft Entra ID instance.
6. Select **Register**.
7. Select **Exit**.
8. From your computer, run **Document Routing** by selecting the shortcut on your desktop or by running *Microsoft.Dynamics.AX.Framework.DocumentRouting.Agent.exe*.
9. Select **Sign In** to sign in to your account.

Now, you have registered the Document Routing Agent.

The account must share the same domain as the Microsoft Entra ID that's associated with finance and operations apps. The Document Routing Agent is now ready to process documents. After you've successfully signed in, the **Printers** button becomes available on the toolbar.

![Screenshot of the document routing agent showing the Printers button on the toolbar.](media/08-register.png)

## Register network printers

Before you complete this procedure, make sure that you've installed all network printers on the local host computer. All printer devices that are installed will be available for service registration. Be sure to select only those printers that you want to expose in finance and operations apps.

1. On the toolbar, select **Printers**.
2. Select the printers that you want to make available in finance and operations apps.
3. Specify a default name for the printer.
4. Select **OK**.

After you've completed this procedure, the selected printer devices will be registered in the finance and operations apps' network printer catalog. System administrators can now enable the printers for access from within the application.

## Administer network printers

You can use client pages to manage access to the network printers that have been registered by one or more document routing agents. Network printers are uniquely identified by their path. Therefore, printers are listed one time, even if they've been registered by more than one document routing agent.

Use this procedure to activate the Application Object Server (AOS) network printers.

1. To open the **Manage network printers** page, go to **Organization administration > Setup > Network printers**.
2. Edit the existing entries that are mapped to each network printer. As part of your changes, edit the connection path.
3. To include a printer as an option in the **Print Destinations** field, set the **Active** field to **Yes**.

Now, you can use the network printers in finance and operations apps.

Individuals who access the provisioned finance and operations apps environment can share client installations of the Document Routing Agent. Therefore, make sure that you install the Document Routing Agent on each computer where a user connects by using a browser.

We recommend that you install agents on one or more print servers or other domain-hosted clients that have access to network printers. The Document Routing Agent supports running in the background as a service. You need to ensure that you've downloaded the latest version of the client.

The number of supported network printers depends on the number of legal entities and the number of network printers that have been deployed. If you have fifty printers and one legal entity, a single document routing agent can handle the load. To ensure high availability, consider having more than one routing agent.

To continue running the Document Routing Agent as a Microsoft Windows service, you'll need to have the user name and password of the domain account that's used to run the service. This information must be available after the upgrade is completed. To find the information for the active service account, start the Microsoft Management Console (MMC) Services snap-in and then select **Microsoft Dynamics 365 Document Routing Service** in the list.

## Uninstall an existing document routing agent

To uninstall a document routing agent, open **Programs and Features** and then find and uninstall **Microsoft finance and operations apps: Document Routing**.

During the uninstallation process, if you're prompted to close the Microsoft Dynamics 365 Document Routing Service application, select **Automatically close applications and attempt to restart them after setup is complete**.

## Financial report designer

You can use the Financial report designer to view, create, or change traditional financial statements, such as income statements and balance sheets. It moves beyond traditional reporting constraints to help you efficiently design various types of reports. You can share the results with other members of the organization. Examples of financial reporting include balance sheets, cash flow, and summary trial balance year over year.

You can map the following entities to gain better insight of financial data:

* Main accounts
* Financial dimensions
* Combinations of the two

For example, you can create financial structures to focus on cost accounts. You can set up unlimited financial dimensions that allow for cost detail. The following financial dimensions are examples that might be associated with cost accounts:

* Cost centers
* Departments
* Combinations of the two

The Financial reporting database is deployed to its own SQL Azure database on the same SQL Azure service as the finance and operations apps instance. Basically, the database is preconfigured when you deploy finance and operations apps, and it automatically links to available databases so that the Financial report designer can connect to it.

## Electronic reporting

Electronic reporting is a tool that you can use to set up formats for incoming and outgoing electronic documents that follow the legal requirements of various countries/regions. For example, you can adopt new regulatory requirements and generate business documents in the required format to electronically exchange information with government bodies, banks, and other parties.

The Electronic reporting engine targets business users instead of developers. Microsoft Regulatory Configuration Services (RCS) can be used to share Electronic reporting configurations which can then be published to external organizations.

For more information, see [Share Electronic reporting (ER) configurations in Regulatory Configuration Services (RCS) Global repository with external organizations](/en-us/dynamics365/finance/localizations/global/rcs-global-repo-share-configuration/?azure-portal=true).