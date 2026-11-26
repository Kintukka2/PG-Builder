<!-- https://learn.microsoft.com/en-us/training/modules/plan-implement-legal-entities-finance-operations/9-purposes-policies -->
<!-- refetched: original harvest URL returned 404 -->
# Apply purposes and policies

Completed

* 10 minutes

When you create an organization hierarchy in finance and operations apps, you must assign a purpose to the hierarchy. The purpose that you assign to a hierarchy determines the types of organizations that can be included in the hierarchy. The purpose also defines the application scenarios that the hierarchy can be used in.

A hierarchy that is created for a purpose might not reflect the actual legal structure of the business. For example, the approval process for requisitions can involve multiple legal entities and positions that don’t report to each other. The Chief Financial Officer (CFO) might be required to approve a requisition of a certain amount, even though the organization that submits the requisition does not report to the CFO.

Watch this video to learn how to assign a purpose to an organization hierarchy.

Hierarchies can be used for the following purposes:

* **Procurement internal control**- Defines purchasing policies for a business. For example, you can use the built-in rule to control if a specific department must always buy computers from approved vendors.
  The procurement internal control or purchasing purpose, controls the requisition process for a group of requisitions. Purchasing policies help create a policy structure that is aligned with the organization's needs for strategic purchasing.
* **Expenditure internal control** - Defines travel and expense policies such as meals and travel.
* **Organization charts** - Defines the hierarchical organization for employees, for example it could address questions such as who reports to who.
* **Signature authority internal control** - Define policies that control the spending limits. For example, how much money can you spend without asking for an approval.
* **Vendor payment internal control** - Defines a policy that validates the vendor that the accounts payable clerks are authorized to generate payment for. For example, you could have a dispute with your vendor due to their late delivery of some perishable goods, and as a result some invoices cannot be paid until the issue is resolved.
* **Audit internal control** - Defines policies based on factors such as duplication or certain keywords. For example, you can use audit policies to evaluate expense reports, vendor invoices, and purchase orders to make sure that they comply with policy rules that you create. All the rules that are associated with an audit policy are run in batch mode, according to a schedule that you specify. Each policy rule is an instance of a policy rule type. For each policy rule type, only one policy rule can be active at a time.
* **Centralized payments** - This policy is only available for organization hierarchies that include only legal entity node. The concept of centralized payment means that one legal entity can process invoices, and payments for both accounts receivable and payable for another legal entity. It is required to set up intercompany accounting if you plan to use this policy.
* **Security** - Defines policies related to security role assignments.
* **Retail assortment** - This policy controls the availability of products in a specific time period, and perhaps on selected retail channels. In other words, it answers the questions such as which products, when, for how long, and where the products should be available.
* **Retail replenishment** - This policy defines rules for distribution and fulfillment for replenishment. You can use cross docking, for example, cross-docking from production to an outbound location is relevant for manufacturers who produce high volume and ideally want to ship the finished products as soon as they are reported as finished from the production lines.
  The purpose is to ship the products to distribution centers that are physically located close to the customer demand, rather than build up inventory at the manufacturing site.
* **Retail reporting** - Defines policies for generation of financial reports and creates a hierarchical structure for drill down and roll up within the report. This policy covers all transactions for all retail channels and the data is mostly summarized.
* **Benefit eligibility control** - Defines policies such as who should be getting parking passes or a dental plan benefit.
* **Budget planning** - An operating unit that is considered for the finance department’s budget plan. It is used for the management and allocation of funds across operating units of a legal entity.
* **Retail POS posting** - This policy is very similar to Retail reporting. However, this policy covers all transactions for all retail channels and the data is mostly detailed.
* **Project management**- Defines policies that control the association of worker, project, and category in a service industry, or project management and accounting.
* **Premium earning generation** - This policy defines rules such as overtime for a contractor.
* **Distributed order management** (DOM) – This policy, referred to DOM, optimizes order fulfillment across a complex network of systems and processes. Details about this policy will be covered in the next unit.