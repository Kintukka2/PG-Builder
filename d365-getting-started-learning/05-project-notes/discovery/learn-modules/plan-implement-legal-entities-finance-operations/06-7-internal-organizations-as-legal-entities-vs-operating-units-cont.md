<!-- https://learn.microsoft.com/en-us/training/modules/plan-implement-legal-entities-finance-operations/7-legal-entities-vs-oper-units-2 -->
<!-- refetched: original harvest URL returned 404 -->
# Decide whether to model internal organizations as legal entities or operating units (cont.)

Completed

* 5 minutes

## Local tax requirements

**If the organization is modeled as a legal entity** - A legal entity is subject to the tax laws of the tax authority in the country/region where the legal entity is registered.
For example, a legal entity that is registered in Denmark is subject to Danish tax laws and regulations.

In finance and operations apps, a legal entity can belong to only one country/region. The country/region that you select for the primary address of the legal entity controls the country/region-specific features that are available to that legal entity.

Therefore, if your organizations are in different countries/regions and require different local tax options, you must set up the organizations as separate legal entities.

**If the organization is modeled as an operating unit** - Operating units use the country/region context of the parent legal entity. Operating units in the same legal entity cannot have different country/region-specific requirements. If your organizations are in the same country/region and use the same tax options, you can set them up as operating units.

## Statutory reporting for a country/region

**If the organization is modeled as a legal entity** - For countries/regions that are supported by finance and operations apps, most statutory reports can be created.
For information about which reports are available for each country/region, see [Globalization resources](/en-us/dynamics365/fin-ops-core/dev-itpro/lcs-solutions/country-region/?azure-portal=true).
In finance and operations apps, a posting layer in the general ledger allows you to make adjusting entries to a parent company that uses a different accounting standard than the child company.

**If the organization is modeled as an operating unit** - Statutory reports must be created by using another application. You must ensure that data is captured in finance and operations apps to support the requirements of each operating unit, where they differ from the requirements of headquarters.

## Currency

**If the organization is modeled as a legal entity** - If your organizations must use different functional currencies, you must model the organizations as legal entities. Functional currencies are set up for each legal entity. However, you can enter transactions in multiple currencies.

**If the organization is modeled as an operating unit** - If your organizations can use a single functional currency, you can model the organizations as operating units. Operating units must share a functional currency. However, you can enter transactions and create reports in multiple currencies.

## Year-end closing

**If the organization is modeled as a legal entity** - If laws and accounting practices differ among the countries/regions where your organizations are located, you might require different year-end procedures for each organization. This means that you must model the organizations as legal entities. Each legal entity has its own year-end procedures.

**If the organization is modeled as an operating unit** - If laws and accounting practices are the same among the countries/regions where your organizations are located, you can use a single set of year-end procedures. This means that you can model the organizations as operating units. All operating units must use the same year-end closing procedure.

## Number sequences

**If the organization is modeled as a legal entity** - Number sequences for some references can be set up for each legal entity. Some number sequences can be shared.

**If the organization is modeled as an operating unit** - Number sequences for some references can be set up for each operating unit. Some number sequences can be shared.

## Products

**If the organization is modeled as a legal entity** - Product definitions are shared, and they must be released to individual legal entities before they can be included in transactions. Each legal entity has its own set of released products that can be included in transaction documents. If your internal organizations must use different sets of products, you must model the organizations as legal entities.

Note

Even though product definitions are shared, in each legal entity where a product has been released, you can specify different sales, purchase, and stocking parameters for the item at each inventory site.

**If the organization is modeled as an operating unit** - All operating units share the same set of products. If your internal organizations can share the same set of products, you can model the organizations as operating units.

## Inquiry and reporting

**If the organization is modeled as a legal entity** - You must manually change companies to enter transactions and perform inquiries in multiple legal entities. Because of data security boundaries, consolidated inquiry and reporting can be resource-intensive and time-consuming.

**If the organization is modeled as an operating unit** - You do not need to change companies to access data from multiple operating units. Consolidated inquiry and reporting and individual regional inquiry is easier and faster.