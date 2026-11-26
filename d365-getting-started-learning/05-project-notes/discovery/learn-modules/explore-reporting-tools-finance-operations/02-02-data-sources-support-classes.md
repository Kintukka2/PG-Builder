<!-- https://learn.microsoft.com/en-us/training/modules/explore-reporting-tools-finance-operations/02-data-sources -->
<!-- refetched: original harvest URL returned 404 -->
# Create and modify report data sources and supporting classes

Completed

* 10 minutes

Reports use data sources to pull data. SQL Server Reporting Services
(SSRS) and Power BI are two reporting tools that use data sources. This unit covers the creation and modification of data sources for these reporting tools.

SSRS uses data sets that are defined by a data source. You can assign a data source to an SSRS report through Visual Studio.

![Diagram of Data sources that can be assigned to an S S R S report.](media/02-data-sources.png)

In the report parameters, you can select the data source for the data set and the data source type. The data source type can be the following:

* **Query** - A query data source type uses an existing query or a new query.
* **Business logic** – Use this type to get a data source other than finance and operations apps.
* **Report data provider class** – You can use this type when a query cannot be used alone. In this case, additional logic is needed to run the report. Along with the RDP class, a contract class is also needed to define the report parameters.
* **Enum provider** – An AX enum provider can be used when the report parameter is an Enum type to filter the report view.

If you need to modify a data source, you will
need to extend the tables or RDP classes to make modifications.

Power BI can connect to data sources, ranging from files, databases,
other Power BI semantic models and dataflows, Azure databases, online
services, and even web URLs.

![Diagram of the data sources that Power B I can connect to.](media/02-power-bi-data.png)

Use the following procedure to connect to a
data source to create a Power BI report.

1. On the Power BI Desktop **Home** ribbon, select the **Get data** button. The most
   common data sources are displayed, but you can select more to get
   access to the entire list.
2. After you have selected the data source, select **Connect**.
3. A connection window is displayed where you can specify the data
   connection and enter any required credentials. Select **OK**.
4. The **Navigator** page will appear. You can either select the **Load** button to load all the data, or you can select **Transform data** to open Power Query Editor and modify the query.

When you have completed these steps, Power BI will be connected to a data source that you can use to create reports and data visualizations.