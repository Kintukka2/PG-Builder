<!-- https://learn.microsoft.com/en-us/training/modules/plan-implement-legal-entities-finance-operations/6-legal-entities-vs-oper-units -->
<!-- refetched: original harvest URL returned 404 -->
# Decide whether to model internal organizations as legal entities or operating units

Completed

* 12 minutes

You must have at least one legal entity to represent your business in finance and operations apps. A legal entity can enter legal contracts and is required to prepare financial statements that report on its performance.

Legal entities can be used for transactional business or for consolidation. This means that a legal entity in finance and operations apps does not necessarily represent a real entity in your business.

Internal organizations in your business, such as regional offices, can be represented as additional legal entities, or as operating units of the main legal entity. An operating unit is not required to be a legally defined organization. Operating units are used to control economic resources and operational processes in the business. For example, departments and cost centers are operating units.
Some functionality in finance and operations apps works differently depending on whether the organization is a legal entity or an operating unit.

## Operating units

An operating unit is an organization that is used to divide the control of economic resources and operational processes in a business. People in an operating unit have a duty to maximize the use of scarce resources, improve processes, and account for their performance.

The operating units in finance and operations apps are:

* **Cost center** - An operating unit in which managers are accountable for budgeted and actual expenditures. It is used for the management and operational control of business processes that span legal entities.
* **Business unit** - A semi-autonomous operating unit that is created to meet strategic business objectives. It is used for financial reporting that is based on industries or product lines that the organization serves independently of legal entities.
* **Value stream**- An operating unit that controls one or more production flows. It is commonly used in lean manufacturing to control the activities and flows that are required to supply a product or service to consumers.
* **Department** - An operating unit that represents a category or functional part of an organization that performs a specific task, such as sales or accounting. It is used to report on functional areas. A department can have profit and lose responsibility and consist of a group of cost centers.
* **Retail channel** - An operating unit that represents a brick and mortar store, an online store, or an online marketplace. Used for the management and operational control of one or more stores within or across legal entities.
* **Branch** - An operating unit that represents a branch location, outside of the main location of the business. This is a part of Fleet management sample module and is not installed as part of production environment.
* **Rental Location** - An operating unit that represents a rental location of the business. This is a part of Fleet management sample module and is not installed as part of production environment.
* **Region** - An operating unit that represents a geographical area of the business. This is a part of Fleet management sample module and is not installed as part of production environment.
* **Teams** - A team is an organization in which the members share a common responsibility, interest, or objective. Teams cannot be used in organizational hierarchies.

## Master data

**If the organization is modeled as a legal entity** - Some master data, such as customers, payment terms, tax authorities, and site-specific stock ordering, must be set up for each legal entity. Some master data, such as users, products, and most human resources data, is shared among all legal entities.

**If the organization is modeled as an operating unit** - Master data is shared among operating units.

## Module parameters

**If the organization is modeled as a legal entity** - Parameters for modules, such as Accounts receivable parameters, Accounts payable parameters, and Cash and bank management parameters, must be set for each legal entity. Because the module setup for legal entities is separate, each subsidiary can comply with local statutory requirements and business practices.

For example, a professional services legal entity and a manufacturing legal entity can have different module parameters even though they report to the same parent company.

**If the organization is modeled as an operating unit** - Module parameters are shared among operating units.

## Data security

**If the organization is modeled as a legal entity** - Most data is automatically secured by company ID. A company ID is a unique identifier for the data that is associated with a legal entity. A company can be associated with only one legal entity, and a legal entity can be associated with only one company. Users can access data only for the companies that they have access to. You do not need to customize finance and operations apps to secure data by company ID.

**If the organization is modeled as an operating unit** - Data can be secured for each operating unit by creating customized data security policies. Data security policies are used to limit access to data. For example, assume that a user can create purchase orders only in a particular operating unit. Data security policies can be created to prevent the user from accessing purchase order data from any other operating unit. The volume of transactions and the number of security policies can affect performance. When you design security policies, keep performance in mind.

## Ledgers

**If the organization is modeled as a legal entity** - Each legal entity requires a ledger that provides a chart of accounts, accounting currency, reporting currency, and fiscal calendar. A balance sheet can be created only for a legal entity. Main accounts, dimensions, account structures, charts of accounts, and account rules can be used by more than one legal entity.

**If the organization is modeled as an operating unit** - An operating unit can't have its own ledger information. If your internal organizations do not require unique ledgers, you can model them as operating units. Ledger information will be set up for the parent legal entity in the hierarchy. Income statements can be created for operating units within a legal entity or for the parent legal entity.

## Fiscal calendars

**If the organization is modeled as a legal entity** - Each legal entity has its own fiscal calendar. If your internal organizations use different fiscal years and fiscal calendars, you must model the organizations as legal entities.

**If the organization is modeled as an operating unit** - Operating units must share a fiscal calendar.
If your internal organizations can use the same fiscal years and fiscal calendars, you can model the organizations as operating units.

## Consolidation

**If the organization is modeled as a legal entity** - You must consolidate the financial results for regional offices into a single, consolidated company to prepare financial statements.

**If the organization is modeled as an operating unit** - Consolidation is not required, because data is already shared among operating units.

## Centralized payments

**If the organization is modeled as a legal entity** - Centralized payments must be set up so that invoices for all child legal entities can be paid to or from a single parent legal entity.

**If the organization is modeled as an operating unit** - Centralized payments are not required because all invoices are recorded in a single legal entity.

### Example - Headquarters provides services to regional offices and must charge the costs of those services to the regional offices.

If you model the regional office as a legal entity, you have the following options:

* Headquarters creates a journal entry to cross-charge the regional office for the expense. The transactions cannot be aged.
* Regional offices send a purchase order for the services to Headquarters. A sales order is automatically created in the legal entity for the Headquarter, with intercompany sub-ledger transactions.

## Intercompany transactions

The following example shows how intercompany transactions are handled.

### Example -Headquarters procures and pays for a service that is delivered to a regional office

If you model the regional office as an operating unit, the invoice and payment follow the regulatory requirements of headquarters.

The invoice can be coded to the regional office. On the income statement, use a balancing financial dimension to report costs for the regional office.