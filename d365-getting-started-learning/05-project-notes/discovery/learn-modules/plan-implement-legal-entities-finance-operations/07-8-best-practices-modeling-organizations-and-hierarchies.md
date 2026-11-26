<!-- https://learn.microsoft.com/en-us/training/modules/plan-implement-legal-entities-finance-operations/8-best-practices -->
<!-- refetched: original harvest URL returned 404 -->
# Best practices for modeling organizations and hierarchies

Completed

* 5 minutes

Consider the following best practices when you implement an organization hierarchy:

* Create a department to model the intersection between a legal entity and a business unit. You can then roll up data from a department to a legal entity for statutory reporting, and from a department to a business unit for internal reporting. Departments can serve as profit centers. If you use departments, you do not have to only use legal entities and business units as dimensions in the account structure, you can use departments as a dimension. However, you must use both cost centers and departments as dimensions in the account structure if cost centers are used only as cost accumulators, and departments are used for revenue recognition.
* Model multiple hierarchies for operating units if you have complex requirements for reporting profit and loss.
* In a single legal entity, do not model multiple hierarchies for the same hierarchy purpose.
* Do not create a hierarchy for every purpose. Usually, you can use one hierarchy for multiple purposes. For example, one hierarchy of operating units can be assigned to all policy-related purposes.
* Create balanced hierarchies. In a hierarchy, all nodes that are the same distance from the root node are defined as a level. In a balanced hierarchy, only one type of operating unit can occur at each level, and the distance from the root node to each level is consistent. If there are intermediate levels between a department and a legal entity or a business unit, placeholder organizations may be required to create a balanced hierarchy.
* Do not model a separate hierarchy of operating units if the structure for legal entities is also your operating structure. A mixed hierarchy of legal entities and operating units can serve both purposes.
* Before you model major restructuring scenarios, use the hierarchy's effective dates to perform an impact analysis and a validation test.
* Use draft mode to change a hierarchy before you publish a new version in a production environment.
* Limit the number of people who have permissions to add or remove organizations from a hierarchy in a production environment. A smaller number reduces the chance of costly mistakes and the need for corrections.