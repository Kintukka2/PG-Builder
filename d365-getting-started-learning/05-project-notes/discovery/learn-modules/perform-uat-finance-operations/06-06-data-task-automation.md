<!-- https://learn.microsoft.com/en-us/training/modules/perform-uat-finance-operations/06-data-task-auto -->
<!-- refetched: original harvest URL returned 404 -->
# Data task automation

Completed

* 4 minutes

Data task automation in finance and operations apps lets you repeat many
types of data tasks and validate the outcome of each task. Data task
automation is useful for projects that are in the implementation phase.

For example, you can automate the creation and configuration of data
projects. You can also configure and activate the running of
import/export operations, such as the setup of demo data, golden
configuration data, and other tasks that are related to data migration.
You can also create automated testing of data entities by using task
outcome validation.

We recommend the following approach for data task automation:

1. **Identify the data-related tasks that will benefit from
   automation** - Implementation teams should review their
   configuration management plan and data migration plan to identify
   potential data tasks for automation and also to identify data
   entity test cases.
2. **Define tasks** - Tasks are defined in an XML manifest. You can
   keep your manifest under source control as part of configuration
   management in your application lifecycle management (ALM) strategy.
3. **Put the data packages that are related to data task automation in
   the Shared asset library of Lifecycle Services** - You can also use a specific Lifecycle Services
   project as you require. The Data task automation manager can consume
   packages from any sandbox and/or production environment that is
   related to the Lifecycle Services project.

   Note

   The user account that runs Data task automation manager in finance and operations apps must have access to Lifecycle Services and to the Lifecycle Services project that is referenced in the manifest for data packages.

   Although data task automation can be run in any environment in the cloud, we recommend that you not run any import/export tasks that use integration application programming interfaces (APIs) in a production environment. Data task automation that involves integration APIs should be used only for automated testing.
4. **Run the data tasks and then review the outcomes** - Data task
   automation manager provides the success or failure outcome for each
   task. It also provides insights into the reason why a task failed.

For more information, refer to [Data task automation](/en-us/dynamics365/fin-ops-core/dev-itpro/data-entities/data-task-automation/?azure-portal=true).