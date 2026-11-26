<!-- https://learn.microsoft.com/en-us/training/modules/describe-report-integration/6-describe-use-cases-business-events -->
<!-- refetched: original harvest URL returned 404 -->
# Describe capabilities and use cases for business events

Completed

* 8 minutes

Using a business event, you can send a notification to an external system from finance and operations apps. Based on the notification, business actions can be performed in the external application.

Before you review the details, consider the following simulation.

[![Screenshot of the landing page of the simulation.](media/06-business-events.png)](https://microsoftlearning.github.io/click-throughs/docs/AB-6002/business_events_in__dynamics_365_scorm/story.html)

You can trigger business events from finance and operations apps based on an activity. This includes triggering a workflow process, confirming a purchase order document, and posting a journal entry. Additionally, you can create, update, or delete a record on a table. Several standard business events are already available. You can find them under **System administration** > **Setup** > **Business events** > **Business events catalog**.

[![Screenshot of business events.](media/06-2-6-business-event-catalog.png)](media/2-6-business-event-catalog.png#lightbox)

You can create custom business events through code development. Each business event provides a JSON schema that you can download by selecting the **Download schema** option.

An external application can consume this JSON file and take appropriate actions based on business requirements. There are several endpoints that are exposed from the business event for external consumption. The following are the endpoints currently supported by finance and operations apps:

* Azure Service Bus Queue
* Azure Service Bus Topic
* Azure Event Grid
* Azure Event Hubs
* HTTPS
* Azure Blob Storage

To activate these endpoints, select the **Endpoints** tab and then select the **New** button. It provides you with the list of endpoints, from which you can select the one that's applicable for your requirements. Different endpoints have different configuration criteria. A finance and operations app triggers a business event, such as purchase order confirmation or journal posting, resulting in the generation of a JSON file. The selected endpoints receive the generated file.

Power Automate is another widely used endpoint for business events. To activate a Power Automate endpoint, you need to open the Power Apps maker portal and create a Power Automate trigger using the **Fin & Ops Apps (Dynamics 365)** data connector. Once you select the only available trigger. When a Business Event occurs, you're asked to enter the required information.

![Screenshot of the When a Business Event occurs trigger.](media/06-2-6-business-event.png)

* **Instance**: Enter the finance and operations app environment URL.
* **Category**: Select the business event category.
* **Business event**: Select the business event that you want Power Automate to consume.
* **Legal entity**: Select the legal entity for which the trigger is applicable.

The trigger consumes the JSON file received from the finance and operations app. The JSON file is then parsed and processed for further business actions.

The **Business event** page has a **Security** tab where you can define role-based security for the business events.

The following video demonstrates how finance and operations can be integrated into Power Automate using the finance and operations apps.

It's also possible to configure other endpoints to consume the JSON file triggered from finance and operations apps.