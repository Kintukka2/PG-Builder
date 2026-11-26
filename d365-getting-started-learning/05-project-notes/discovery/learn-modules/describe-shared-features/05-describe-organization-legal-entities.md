<!-- https://learn.microsoft.com/en-us/training/modules/describe-shared-features/5-describe-organization-legal-entities -->
<!-- refetched: original harvest URL returned 404 -->
# Manage organizations and legal entities

Completed

* 8 minutes

An organization is a group of people who are working together to carry out a business process or achieve a goal. Organizational hierarchies represent the relationships between the organizations that make up your business.

## Organizations

You can define the following types of internal organizations: legal entities, operating units, and teams.

All internal organizations are types of the **Party** entity because they have associated addresses. Each entry in the **global address book** is called a party. The global address book contains all people and organizations defined within finance and operations apps and includes postal addresses and contact information such as phone number and email address. These internal organizations use the global address book to store their address and contact information.

### Legal entities

A legal entity is an organization that has a registered or legislated legal structure. Legal entities can enter into legal contracts and are required to prepare statements that report on their performance.

A company is a type of legal entity. Currently, companies are the only type of legal entity that you can create, and every legal entity is associated with a company ID. This association exists because some functional areas in the program use a company ID, or DataAreaId, in their data models. In these functional areas, companies are used as a boundary for data security. Users can access data only for the company that they're currently logged on to.

### Operating units

An operating unit is an organization that is used to divide the control of economic resources and operational processes in a business. People in an operating unit have a duty to maximize the use of scarce resources, improve processes, and account for their performance.

The types of operating units include cost centers, business units, value streams, departments, and commerce channels. The following table provides more information about each type of operating unit.

| **Operating unit type** | **Description** | **Purpose** |
| --- | --- | --- |
| Cost center | An operating unit in which managers are accountable for budgeted and actual expenditures. | Used for the management and operational control of business processes that span legal entities. |
| Business unit | A semi-autonomous operating unit that is created to meet strategic business objectives. | Used for financial reporting that is based on industries or product lines that the organization serves independently of legal entities. |
| Value stream | An operating unit that controls one or more production flows. | Commonly used in lean manufacturing to control the activities and flows that are required to supply a product or service to consumers. |
| Department | An operating unit that represents a category or functional part of an organization that performs a specific task, such as sales or accounting. | Used to report on functional areas. A department may have profit and loss responsibility, and may consist of a group of cost centers. |
| Retail channel | An operating unit that represents a brick and mortar store, an online store, or call center. | Used for the management and operational control of one or more stores within or across legal entities. |

## Organizational hierarchies

Set up organizational hierarchies to view and report on your business from different perspectives. For example, you can set up a hierarchy of legal entities for tax, legal, or statutory reporting. Set up a hierarchy that is based on operating units to report financial information that isn't legally required, but that is used for internal control. For example, you can create a purchasing hierarchy to control purchasing policies, rules, and business processes.

Each hierarchy is assigned a purpose. The purpose of a hierarchy determines the types of organizations that can be included in the hierarchy. The purpose also determines which application scenarios a hierarchy can be used in. Security is a common purpose. Users can be restricted to work only with data in specific legal entities or operating units based on their assignment to nodes within an organizational hierarchy with the **Security** purpose.

Organizations in a hierarchy can share parameters, policies, and transactions. An organization can inherit or override the parameters of its parent organization. However, shared master data, such as products and address books, applies to the whole organization and can't be overridden for individual organizations. Creating organizations and hierarchies requires careful planning. For more information, go to [Plan your organizational hierarchy](/en-us/dynamics365/fin-ops-core/fin-ops/organization-administration/plan-organizational-hierarchy).

An organization may exist in many hierarchies but can appear only once within a specific hierarchy.

Organizational hierarchies are date effective. When you modify a hierarchy, you must publish it to make it effective on the date you specify as part of the publishing process. You can publish a hierarchy to be effective on a future date or a prior date, but you can never publish to a date earlier than the last one published.

## Using organizational hierarchies in financial reporting

Organizational hierarchies can be selected as a **Tree type** option in Financial Reporting. Financial reporting uses the current effective version of the hierarchy.