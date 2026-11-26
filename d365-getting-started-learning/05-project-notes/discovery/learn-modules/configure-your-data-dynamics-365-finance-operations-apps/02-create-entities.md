<!-- https://learn.microsoft.com/en-us/training/modules/configure-your-data-dynamics-365-finance-operations-apps/create-entities -->
# Create entities

Completed

* 3 minutes

Data management is a workspace in the Finance and Operations apps. In it, we
can configure entities to be used for data in and out. We can also set up jobs,
which will import or export data, either one-time or on a regular basis.

The data management framework has been evolving over several years. Initially,
only several commonly used entities were created. While the engineers were
creating more entities for us, they also gave us the capability to create
entities of our own.

While Dynamics 365 relies upon a normalized database, data in external
systems is often non-normalized. Often, we need to flatten our data to send it
out, or to receive flattened data. A data entity consists of one or more related
tables. For example, the sales order header and sales lines comprise a composite
entity.

Dynamics optionally uses staging tables so that we may validate before putting
data into our database, or before sending it externally.

New data entities are built by a developer in Visual Studio, either with the data
entity wizard or by right-clicking a table and selecting **Addins > Create data
entity**. Because several thousand entities already exist, this task is most
often done for custom tables.

More commonly we modify an existing entity, to add a field. You can do this task in
the **Data management** workspace by selecting the **Data entities** tile.
The entity list refreshes automatically the first time that you open the **Data
management** workspace in a new environment. After you deploy code packages or
change configuration keys, refresh it manually from
**Data management > Framework parameters > Entity settings > Refresh entity list**,
and wait for the refresh to finish before you run jobs.

![The entities grid](media/02-m3-l2-p1.png)

You’ll see the following:

* Entity name
* Staging table
* Target entity
* Entity type – May be entity or composite entity
* Change tracking – We can set an entity up to detect and send changed records
* Type – The underlying query
* Set-based processing – Set-based is faster but misses some business logic
* Configuration key – May be set for security

If you highlight an entity and select Modify target mapping, you can see the
individual fields in the entity and their mappings, from staging to target.

![Map staging to target screen, mapping details tab](media/02-m3-l2-p2.png)

You’ll specifically see these options on the Mapping details tab:

* Staging field
* Mapping type:

  | **Type** | **What it does** |
  | --- | --- |
  | = | Setting |
  | () | Function |
* Function name (if selected earlier)
* Target field
* Sequence – Often fields should be entered in a particular order
* Return parameter sequence
* Call validate Field method checkbox – If validation is necessary. Know that
  we take a performance hit for large migrations

You can also switch over to the Mapping visualization tab and see the field
mapping graphically depicted. The fields are on the sides, and there are lines
going between the two. Required fields are indicated with an asterisk. Changes
here are as easy as drawing a line with your mouse.

![Map staging to target screen, mapping visualization tab](media/02-m3-l2-p3.png)

To study this topic further, try: [Work with data management in Finance and Operations apps](/en-us/training/modules/work-data-management-finance-operations/)