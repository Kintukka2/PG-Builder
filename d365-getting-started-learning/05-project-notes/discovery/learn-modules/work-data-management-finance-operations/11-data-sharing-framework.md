<!-- https://learn.microsoft.com/en-us/training/modules/work-data-management-finance-operations/data-sharing-framework -->
# Data sharing framework

Completed

* 5 minutes

Cross-company data sharing lets you replicate (share) reference and group data among companies. Data integrity is verified before replication occurs.

Examples of cross-company data sharing and the basic logic:

* The same payment terms and payment day definitions are used across fifteen legal entities.
* The same terms of delivery are used across seven legal entities in three countries/regions.
* Records created, updated, and deleted in any of the companies within the policy will be replicated immediately, across all the companies.
* Fields that are not selected for sharing are maintained in each company and will not trigger any replication.
* As part of enabling a policy, it is optional to copy any existing records.

## Cross-company sharing framework important aspects

The following aspects need to be considered before using cross-company data sharing.

* Use to replicate (share) reference, parameter, and group data between companies within an environment.
* Cannot be used for transactional data between companies.
* Data integrity must be verified before replication.
* Data sharing policy should be enabled after importing data in seeding company.
* Apply to production only after testing and validation sandbox environment.
* Data sharing policy can be updated or disabled.
* Cannot be used with dual write.
* Fields that reference financial dimensions, such as **Ledger** or **Default** dimension, cannot be shared across companies.
* Replication supports fewer than 2 million total records per job (the number of shared records multiplied by the number of shared companies) and up to 300 companies per policy.
* Customer and vendor master data can be shared by turning on the **Customer and vendor master data sharing** feature in **Feature management**.

## When to use cross-company data sharing feature?

Use cross-company data sharing for the following business scenarios:

* Sharing of simple reference and group data in a single deployment.
* Sharing among companies that have similar configurations.
* Sharing scenarios that have been explicitly evaluated by Microsoft.

Cross-company data sharing is not supported for the following scenarios:

* Franchising solutions, where thousands of records are shared across thousands of companies.
* Sharing of transactional records for reporting or management purposes, such as consolidations.
* Sharing across deployments.
* Complex scenarios, such as replication of subtype/supertype tables or tables that have date effectivity rules.
* Tables that do not have a unique index.

## Other tools for data management

Other tools for data management are:

* **Bring your own database (BYOD)** – Export entities to your own database.
* **Entity store refresh** – For embedded Power BI reports.
* **Process data package** – A wizard functionality that consolidates multiple data packages in one bundle.
* **Data validation checklist workspace** –To track data validation processes across companies, areas, and people.
* **Office add-in** – Export and import data via Excel add-in using data entities.