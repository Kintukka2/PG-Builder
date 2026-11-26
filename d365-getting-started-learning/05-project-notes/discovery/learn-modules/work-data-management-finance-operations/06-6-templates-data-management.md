<!-- https://learn.microsoft.com/en-us/training/modules/work-data-management-finance-operations/6-templates -->
<!-- refetched: original harvest URL returned 404 -->
# Use templates in data management

Completed

* 6 minutes

Default templates are delivered together with each new release of finance and operations apps. Our long-term goal is to provide the templates in Lifecycle Services so that you can push them to an instance of finance and operations apps. However, for the current releases, select the **Templates** tile in the **Data management** workspace, and then select **Load default templates** to load the templates. To see the **Load default templates** menu, you must use Enhanced view.

We recommend using the Enhanced views to have more features and flexibility while working with your projects.

After the templates are loaded, you can change them to suit your business requirements. If you ever want to retrieve the original default templates, you can use the **Load default templates** button to add them back to your system. The templates will then be replaced with the latest versions. If you've made changes to the templates, you can make a copy of the old templates by exporting them.

Note that system administrator access is required to load default templates and import templates. This requirement helps guarantee that all entities are correctly loaded into the template.

For the newly deployed environment of finance and operations apps, the default templates are not loaded. We recommend that you select the **Load default templates** button to view the default templates.

[![Screenshot of the Load default templates button.](media/06-template.png)](media/template.png#lightbox)

When the **Load default templates** dialog box appears, you can select single, multiple, or all templates to be loaded into your environment.

[![Screenshot of the Load default templates dialog box.](media/06-load-default-template.png)](media/load-default-template.png#lightbox)

Levels 10 to 22 are reserved for shared system entities so that those entities are processed first. Almost all systems also use the company-specific general ledger entities. Therefore, level 25 is reserved for those entities. These levels represent the minimum basic setup that is required for most shared data in a configuration.

After the basic setup is completed, many entities can be loaded in parallel across all the modules. These entities don't have to be loaded in silos by module. Instead, you can set up bands of dependencies between the data for different entities. Bands help establish execution timing between entities added to the groups because each band is defined by its execution level.

Entities that have no dependencies are added to band 30 in this example. Band 40 is added for entities that have a dependency on the entities in band 30. The same process is continued for bands 50 to 90, as shown in the table:

| Module | Unit | Execution Level |
| --- | --- | --- |
| Band 1 for dependencies | 1 | 30 |
| Band 2 for dependencies | 1 | 40 |
| Band 3 for dependencies | 1 | 50 |
| Band 4 for dependencies | 1 | 60 |
| Band 5 for dependencies | 1 | 70 |
| Band 6 for dependencies | 1 | 80 |
| Band 7 for dependencies | 1 | 90 |

After organizing the basic entities so that they can be processed in parallel, the remaining entities are organized by module, in the order that the modules should be processed in. However, many entities have many dependencies, some of which are complex.

For example, the Vendor posting profiles entity might require Vendors or Items entities. Although the Vendor posting profiles entity is in the Accounts payable module, it must be processed after the Product management module. In that case, if Vendors entities are 1.130.10 and Items entities are 1.300.10, the Vendor posting profiles entity must be moved so that it's after that sequence (for example, 1.310.20).

Note

The sequences that we have implemented are a guideline, not a requirement. There is no required relationship between a level and a module. You can rearrange the entities if the sequence doesn't work for your implementation. To add your own templates to a configuration, you can follow the preceding guidelines to help guarantee that your template is correctly merged into a project that uses default templates.

## Templates that have the same entity

Some entities are required in more than one template. For example, you must have payment terms in both the Accounts payable and Accounts receivable templates. However, you might require only the Accounts receivable template. We added the entity to both templates for situations where you require only one of them.

A data project can include only one instance of an entity. If you add a template, and the template contains an entity that already exists in a data project, the entity in that template replaces the entity that is currently in the project.

You can use this capability to override the default templates without changing them. For example, the worker field hasn't been mapped in your data project, but you have your own template that adds workers. In this case, you can build a template that includes the entities that have the worker field. In that template, you can map the worker field. Any entities in the data project that don't have the field mapped will then be replaced.

## Merged templates

We have created larger templates that cover multiple module areas. You can use the larger templates, or any combination of smaller templates, to build a data project. The following combined templates are available:

* **System and Shared** – Include system setup, global address book, shared general ledger, and workflow.
* **Financials** – Includes general ledger, bank, accounts payable, tax, accounts receivable, fixed assets, and budgeting.
* **Supply chain management** – Includes inventory management, product management, procurement, sales and marketing, limited warehouse management, production control, and costing.
* **Expense and Project Management** – These templates aren't included in a larger template. However, they are designed so that they can easily be merged into a project that uses other templates.
* **Workers** – Includes the entities needed to add workers and re-map entities where the worker mapping was removed.

## Master data

Many default templates include entities for master data, such as customers, vendors, and released products. These entities are included to indicate the correct sequence of entities that you will require after you've loaded parameters and reference data. Master entities are most often sequenced in the module bands that are numbered 100 and above. In the grid, the entity category for these entities will be Master. If you don't want to include master data or any other entities in your configuration, remove those entities from your project.

## Enable change tracking for entities

Change tracking enables incremental export of data from finance and operations apps by using Data management. In an incremental export, only records that have changed are exported. To enable incremental export, you must enable change tracking on entities.

[![Screenshot of the Change tracking button.](media/06-change-tracking.png)](media/change-tracking.png#lightbox)

If you don't enable change tracking on an entity, you can only enable a full export each time. For bring your own database (BYOD) use cases, change tracking can also track deletes, if the entity supports this.

For more information regarding BYOD, see [Prepare data for migration to finance and operations apps](/en-us/training/modules/prepare-data-migration-finance-operations/?azure-portal=true).