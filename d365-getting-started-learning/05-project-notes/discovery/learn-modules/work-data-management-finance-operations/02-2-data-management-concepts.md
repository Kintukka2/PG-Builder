<!-- https://learn.microsoft.com/en-us/training/modules/work-data-management-finance-operations/2-concepts -->
<!-- refetched: original harvest URL returned 404 -->
# Data management concepts

Completed

* 6 minutes

The data management framework consists of the following concepts:

* **Data entities** – A data entity is a conceptual abstraction and encapsulation of one or more underlying tables. A data entity represents a common data concept or functionality, such as customers or vendors. Data entities are intended to be easily understood by users who are familiar with business concepts. After data entities are created, you can reuse them through the Excel add-in, use them to define import/export packages, or use them for integrations.
* **Data project** – A data project is automatically created when you select **Import** or **Export** from the workspace and should have at least one job. It contains configured data entities, which include mapping and default processing options. A data project allows users to set up the entities that should be part of the project and defines the format that is used for each entity. It allows users to define the mapping that is used from the source file to the staging and to specify the default processing options.
* **Data job** – Use a data job to perform the actual import or export operation. A data job contains an execution instance of the data project, uploaded files, the schedule or recurrence information, and the processing options to use for the job.

  A data job is created when the import or export operation is performed. The data job creates an instance of the data project and then runs it. If you're doing an unplanned import or export, then only one job for each data project typically exists. If it's being done multiple times with different data, then you can use the same data project to import data multiple times by using different jobs.

  Each data project can have one or more data jobs. For instance, if you're doing a single unplanned data import, then you might have one file that is being imported. In this case, a single data project will have one data job.

  Another scenario to consider is if you're importing data by using the same data project multiple times but with different data. In this case, more than one data job can exist for a single data project. Each data job can have one or more job histories.

  For instance, a data job might be run multiple times after errors have been fixed. The job history describes the details, such as the time taken to run the job, the number of records processed, and the errors that occurred during processing.
* **Job history** – Histories of source to staging and staging to target jobs. After a job has been run, you can view the job history, which contains the run history for each execution run of the data job and the history of the data move from source to staging and from staging to target.

  The **Job history** tab in the **Data management** workspace shows all job histories for the import and export data projects. From **Job history**, you can view the run history for the source to staging and staging to target steps. Each project can have multiple jobs, which in turn have executions. By using the job history, you can view the execution details and determine the time that it took to run the job, the number of records that were processed, and so on.
* **Data package** – Data packages are key concepts for many application lifecycle management (ALM) scenarios, such as copy configuration and data migration. A data package is a single compressed file that contains a data project manifest and data files. A data package is generated from a data job and is used for the importing or exporting of multiple files with the manifest. After you've defined a data project, including the data entities and the mapping and sequencing between these data entities, you can create a data package. Then, you can use the data package to move the definition of the data project from one environment to another.

  You can generate a data package from a data job. To create a data package, go to the **Data management** workspace, load the project that you want to create the data package for, and then select **Download**. This process will generate a zip file.

  [![Screenshot showing the Download option to create a data package.](media/02-dm-1.png)](media/dm-1.png#lightbox)

  The zip file contains the package header and the manifest. The manifest defines the settings of the data project. You can use the data package to copy the settings of your data project from one environment to another.

## Data management platform

By using the data management framework, you can quickly migrate reference, master, and document data from legacy or external systems. The framework provides features that help you import data into a staging environment, perform basic data quality services or validation operations on the data, and validate and cleanse the data.

With the data management platform features, you can map data from input to the target and do pre and post-processing on data. If you export data, the source is finance and operations apps, and if you import data, the target is finance and operations apps.

The framework is intended to help you quickly migrate data by using the following features:

* You can select only the entities that you need to migrate.
* If an import error occurs, you can skip selected records and choose to proceed with the import by using only the good data, opting then to fix and import the bad data later. You'll be able to partially continue and use errors to quickly find bad data.
* You can move data entities straight from one finance and operations apps system to another, without having to go through Excel or XML.
* Data imports can be scheduled by using a batch, which offers flexibility when it's required to run. For example, you can migrate customer groups, customers, vendors, and other data entities in the system anytime.

The data management framework supports using data entities in the following core data management scenarios:

* **Data migration** – You can migrate reference, master, and document data from legacy or external systems.
* **Set up and copy configurations** – Use this scenario to copy configurations between companies or environments and set up processes or modules by using the Lifecycle Services environment.
* **Integration** – Use this scenario when you need real-time, service-based integration or when you need an asynchronous integration. The real-time integration doesn't have a staging area and is directly processed by the services layer.

## Data migration

Data migration is an initial or unplanned data load that you can perform manually by using the user interface. A scenario where this pattern might be used is when a functional user has some data in a source, such as an Excel workbook that needs to be imported from a legacy system to finance and operations apps during data migration.

## Data flow

The first step is to load the file from the source to the central storage, such as Azure. Then, the data import/export framework picks up the data from the central storage and then pushes it into the staging tables of finance and operations apps. From staging, the data is moved to the target by using data entities that have been defined. This flow of data can be done row-by-row or by using a set base of the data entities for the entire underlying tables for each data entity. You can control the sequence and order in which the target tables will be populated by using the sequence entity feature of finance and operations apps.