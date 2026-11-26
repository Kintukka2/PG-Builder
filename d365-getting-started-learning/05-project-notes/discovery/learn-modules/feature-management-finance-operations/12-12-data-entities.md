<!-- https://learn.microsoft.com/en-us/training/modules/feature-management-finance-operations/12-data-entities -->
# Data entities

Completed

* 5 minutes

The **Feature management** data entity lets you export the Feature management settings from one environment and then import them into another environment. This entity updates only existing features. The business logic in the entity also helps guarantee that the same rules that are used on the **Feature management** workspace will be applied when the import is done. For example, you can't override a mandatory feature setting by removing the date during import.

The following examples describe what occurs when you use the **Feature management** entity to import data.

* If you change the value of the **Enabled** field to **Yes**, the feature is enabled and the **Enable date** field is set to the current date.
* If you change the value of the **Enabled** field to **No** or leave the **Enable date** field blank, the feature is disabled and the **Enable date** field is cleared. You can't disable a mandatory feature or a feature that can't be disabled after it's been enabled.
* If you change the value of the **Enable date** field to a future date, the feature is scheduled for that date.
* If you change the value of the **Enabled** field to **Yes** and change the value of the **Enable date** field to a future date, the feature is scheduled for that date.
* If you change the value of the **Enabled** field to **No**, but you also change the value of the **Enable date** field to a future date, the feature is scheduled for that date.
* If a feature is enabled, and you add an **Enable date** field that is set to a future date, the feature remains enabled. To reschedule the feature, you need to change the value of the **Enabled** field to **No**.