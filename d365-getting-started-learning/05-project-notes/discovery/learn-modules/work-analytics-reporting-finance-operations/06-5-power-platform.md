<!-- https://learn.microsoft.com/en-us/training/modules/work-analytics-reporting-finance-operations/5-power-platform -->
# Configure finance and operations apps for Microsoft Power Platform

Completed

* 8 minutes

finance and operations apps delivers interactive reports that are seamlessly integrated into application workspaces. Workspaces can use rich infographics and visuals that are supported by Microsoft Power BI.

You can also use Power Apps and Power Automate with finance and operations apps.

## Power Apps

You can embed Power Apps into finance and operations apps by using the **Personalize** toolbar that is available on most pages in the system. When you build a PowerApp, it’s important that you are logged in to Power Apps.com and your instance of finance and operations apps by using the same credentials.

By using Power Apps, you can build apps fast with a point-and-click approach to app design. Choose from a large selection of templates or start from a blank canvas. Easily connect your app to data and use Excel-like expressions to easily add logic. Publish your app to the web, iOS, Android, and Windows 10.

With Microsoft Dataverse built in, you get a powerful data service with rich customization, business logic, and security capabilities. Your data is stored in a standard format through Common Data Model so it’s ready to go and easy to use.

To read more about Power Apps in finance and operations apps, go to the following sources:

* [Embed Power Apps apps](/en-us/dynamics365/fin-ops-core/fin-ops/get-started/embed-power-apps/?azure-portal=true)
* [Power Apps Host control](/en-us/dynamics365/fin-ops-core/dev-itpro/user-interface/powerapps-host-control/?azure-portal=true)

## Power Automate

Power Automate includes powerful workflow automation that flows directly in your apps with a no-code approach that connects to hundreds of popular apps and services. You can create automated workflow between your favorite apps and services to get notifications, insights, synchronize files, collect data, and much more.

To read more about Power Automate in finance and operations apps, go to:

* [Business events in Power Automate](/en-us/dynamics365/fin-ops-core/dev-itpro/business-events/business-events-flow/?azure-portal=true)

## Power BI

Use the features of Power BI to unify data from many sources to create interactive, immersive dashboards, and reports that provide actionable insights and drive business results.

The following Power BI solutions are available in the **Shared assets library** of Lifecycle Services. Refer to the version information in the **Shared assets library** to download the correct version for your environment.

* **Actual vs. budget** - Individuals who are responsible for monitoring actual versus budget performance in their organization can use this Power BI content. It provides visibility into your budget variances.
* You can analyze budget for the current year by account category, budget code, main account, main account descriptions, or fiscal period to gain better understanding of the cause of any variances.
* **Cash overview** - Business users who are responsible for cash in their organization can have visibility into the business cash flow by using this Power BI content. It provides forecasts that can help financial leaders make better decisions and therefore improve the health of the business cash flow.
* You can analyze cash by legal entity, currency, and bank account to gain better understanding of surpluses and shortfalls. Reports from the **Cash overview Power BI** content are displayed in the **Cash overview** and **Bank management** workspaces.
* **Compensation and benefits** - Two reports are available in this Power BI content:

  + **Comp and Benefits Analysis** - Provides information for hourly and salaried employees by company, average hourly pay, average salaried pay, employees by employment type, and plan enrollment.
  + **Employee Benefits** - Provides information for employee enrollment by selected benefit so you can filter all employees by each benefit.
* **Cost accounting analysis** - This Power BI content is intended for cost controllers or anyone who is responsible for performing cost control of an organization.

  This report includes the key metrics, such as cost, magnitude, and cost rate by actual cost, budget cost, and flexible budget cost. It uses transaction data from the Cost accounting module and provides an aggregate view of costs for the whole organization in one reporting currency. Managers can filter the data by cost objects to perform cost control of their organizational units, even if the organization can have several legal entities.
* **Compensation** - This Power BI content is shown in the **Compensation management** workspace. The following reports are available:

  + **Compensation overview** – Provides a summary of other reports.
  + **Compensation analysis** - Hourly and salaried employees by company, total employees by compensation plan, male and female employees by compensation plan, and employee compensation by department.
  + **Position pay analysis** - Highest and lowest hourly and salary pay, positions with highest and lowest pay, and full-time and part-time positions.
  + **Compensation Plan Analysis** - Provides information regarding the employee enrollment by selected benefit.
* **Credit and collections management** - The credit and collections managers and collections clerks can benefit from this Power BI content. It provides key credit and collections metrics, such as days sales outstanding, balance overdue, credit exposure, and customers that are over their credit limit.

  It uses transactional data and provides aggregate views of credit and collections across all companies. It also provides a breakdown per company, customer group, and customer.
* **Employee competencies and development** - The following reports are available in this Power BI content:

  + **Competency & Development Analysis** - Provides information of the team member skills by type.
  + **Skill Profile** - Provides information regarding the skill profile for the selected employee.
  + **Skill Analysis** - Provides information regarding skills by type and rating.
* **Financial analysis (current company and all companies options)** - Describes the dashboard and reports that are included, and provides information about the data model and entities that were used to build the solution.

  Because organizations want liabilities and revenue amounts to appear as positive amounts on reports, the setup of the main accounts is important.
  For these main accounts to appear as positive amounts, the main account type must be set to **Liability** or **Revenue**. When these account types are used, reporting through Power BI will reverse the signs and show the amounts as positive.
* **Fixed asset management** – This workspace shows information that is related to fixed assets that are entered in the system. It includes a summary view and an analytics view. The **My work** tab shows summary tiles, fixed asset details, and related information about fixed assets in the current company.

  You can also add analytics to the **Power BI analytics** section directly in the workspace. **The Analytics – all companies** tab uses capabilities of Microsoft Power BI to show visuals that are related to fixed assets in all companies.
* **Organizational training** - Two reports are available in this Power BI content:

  + **Course Analysis** - Provides information for registration by location, course attendees by status, and registration list.
  + **Course Types** - Provides information on course types by skill.
* **Practice manager** - Practice managers and project managers can benefit from this Power BI content. It provides key metrics that are related to the projects that the organization is working on. The dashboard gives an overview of the projects and related customers.

  A report-level filter can be used to report for specific legal entities. This Power BI content pulls data from the project accounting aggregate measurements.
  The Practice manager Power BI content contains five report pages: one overview page, and four pages that provide details about project costs, revenues, earned value management, and hour metrics that are broken down across various dimensions.
  All the amounts in the content are shown in the system currency. You can set the system currency on the **System parameters** page.
* **Cost Management** - Inventory accountants and individuals who are responsible for or interested in the status of inventory or work in process (WIP), and people who analyze the standard cost variance benefit from this Power BI content.
* **Production performance** - Production managers can benefit from this Power BI content. It can monitor the performance of manufacturing operations for a timely running process, quality control, and cost analysis. This report uses transactional data from production orders and batch orders and provides an aggregate view of production metrics.
* **Purchase spend analysis** - This Power BI content helps purchasing managers make sure that the purchase spending is within the allocated budget over time.
* **Recruiting** - This Power BI content is shown on the **Recruitment management** workspace and contains information such as:

  + **Applicant Analysis** - Shows the total number of applicants, and then groups them by jobs, gender, and location.
  + **Applicant Status** – Shows applicants by type, status, and applicant status.
  + **Recruiting Analysis** - Shows net hire ratio, average days to hire, percentage of bad hires, recruiting costs, number of recruitment projects, hire to applied, and applicants versus openings by recruitment project.
* **Sales and profitability performance** - The sales managers can monitor the key sales metrics of revenue, gross profit, and profit margins by using this Power BI content. It uses sales transactional data and provides both an aggregate view of the company-wide sales figures and a breakdown of sales performance for customers and products.
* **Vendor payment** - This Power BI content shows information that is related to the processing of vendor payments. This workspace includes a **My work** view and an **Analytics** page.

  The **My work** view shows summary tiles, vendor transaction grids, and related vendor information. The **Analytics** page uses the capabilities of Power BI to show visuals that are related to vendor payments.
* **Warehouse performance** - The warehouse and operations managers can monitor important inbound, outbound, and inventory metrics by using this Power BI content.

  It uses warehouse management, product, and other transactional data from finance and operations apps and provides both an aggregate view of warehouse performance and a breakdown for vendors, product groups and products, and site and warehouses.
* **Workforce metrics** - This Power BI content provides information for headcount analysis by company, department, location, job, and more.

Read more about Power BI content in finance and operations apps in the [PowerBI.com solutions home page](/en-us/dynamics365/unified-operations/dev-itpro/analytics/power-bi-home-page?azure-portal=true&toc=/fin-and-ops/toc.json)