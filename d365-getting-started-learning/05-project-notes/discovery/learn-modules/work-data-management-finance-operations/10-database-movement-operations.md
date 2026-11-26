<!-- https://learn.microsoft.com/en-us/training/modules/work-data-management-finance-operations/database-movement-operations -->
# Database movement operations

Completed

* 10 minutes

Database movement operations are a suite of self-service actions that you can use as part of Data Application Lifecycle Management (also referred to as DataALM). These actions provide structured processes for common implementation scenarios such as golden configuration promotion, debugging/diagnostics, destructive testing, and general refresh for training purposes.

![Diagram of the Create request for database movement operation page in Lifecycle Services.](media/10-request-database-movement.png)

With database movement operations, you can:

* Run database movement operation from and to Tier-2+ environments directly in Microsoft Dynamics Lifecycle Services.
* Create requests for database operations for production environment in Lifecycle Services.

## Refresh database

You can use Lifecycle Services to perform a refresh of the database to a sandbox user acceptance testing (UAT) environment. A database refresh lets you copy the transactional and financial reporting databases of your production environment into the target, sandbox UAT environment. If you have another sandbox environment, you can also copy the databases from that environment to your target, sandbox UAT environment.

Note

Copying production data to your sandbox environment for the purpose of production reporting is not supported.

## Export database

You can use Lifecycle Services to export a database from a sandbox user acceptance testing (UAT) environment to the Asset library. The environment will be unavailable for other servicing operations, such as Sandbox refresh or package deployment during this time. The source environment will be usable from a Dynamics user perspective.

## Import database

You can import a database that is prepared from a developer environment to a standard user acceptance test (UAT), or a database previously exported from a UAT environment.

## Point-in-time restore

You can use Lifecycle Services to perform the point-in-time restore (PITR) for a sandbox user acceptance testing (UAT) environment or for a production environment. Microsoft maintains [automated backups](/en-us/azure/azure-sql/database/automated-backups-overview?tabs=single-database/?azure-portal=true) of the business and financial reporting databases for 28 days for Production environments and seven days for Sandbox environments.

Restoring a production database to a previous point in time isn't a common lifecycle operation. Consider it only for scenarios such as recovery from significant data corruption, because it can cause extended downtime and SQL data loss up to the time of the request.

## Point-in-time restore of the production database to a sandbox

You can use Lifecycle Services to do a point-in-time restore (PITR) of the production database to a user acceptance testing (UAT) sandbox environment. To provide customers with data application lifecycle management (DataALM) capabilities that do not rely on human or manual processes, the Lifecycle Services team has introduced an automated refresh database actions for this purpose.

## Database operations between Tier-1 and Tier-2+

You can use the following options to move databases between Tier-1 and Tier-2 customer/partner managed environments:

* Bacpac procedure: from SQL Server to Azure SQL or from Azure SQL to SQL Server
* SQL Server backup/restore between one-box environments (SQL Server)

![Diagram of the Tier-1 and Tier-2 environments.](media/10-tier-1-tier-2-database-operations.png)

See [Database movement operations home page](/en-us/dynamics365/fin-ops-core/dev-itpro/database/dbmovement-operations/?azure-portal=true) to learn more about database movement operations