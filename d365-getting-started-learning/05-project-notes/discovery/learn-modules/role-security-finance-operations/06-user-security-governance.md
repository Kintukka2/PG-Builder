<!-- https://learn.microsoft.com/en-us/training/modules/role-security-finance-operations/user-security-governance -->
# Monitor user licensing with user security governance

Completed

* 10 minutes

Because a user's assigned security roles determine which Dynamics 365 license that user requires, security configuration and licensing compliance are closely related. *User security governance* is the set of features in finance and operations apps that helps system administrators, licensing managers, and compliance officers analyze that relationship.

User security governance provides the following capabilities:

* Detailed reporting about segregation of duties and separation of privileges.
* Process-based security roles, duties, and privileges.
* Creation of new roles and duties from existing objects through import processes.
* Temporary role assignment and privileged user management, which grant time-bound access to dedicated accounts.
* Version management for roles, duties, and privileges, so that you can compare and restore previous versions.
* Reports that include license indicators by role, duty, privilege, and entry point.

## Turn on user security governance

The user security governance features are available in version 10.0.43 and later, and they must be turned on before the workspace appears.

1. Sign in to your finance and operations apps environment as a **System administrator**.
2. Go to **System administration > Feature management**.
3. Turn on the **User security governance** and **User security governance license usage summary report** features.
4. Go to **System administration > Security > Security governance** to confirm that the reports are available.

## Review license requirements

Open **System administration > Security > Security governance > License usage summary** to see which license each user requires, based on the security roles that are assigned to them. The page contains the following views:

| View | What it shows |
| --- | --- |
| **User Role Licenses** | The licenses that a user requires, based on all of the roles that are assigned to them. |
| **Role Licenses** | The minimum license that is required for a security role. |
| **Duty Licenses** | License requirements for individual duties. |
| **Privilege Licenses** | License requirements for individual privileges or menu items, for the most detailed analysis. |

In the **User Role Licenses** view, the **License quantity** column indicates how many licenses a user needs. One row that is marked with **1** means that only a base license is required. Each extra row that is marked with **1** indicates that an attach license is also required.

When you drill into a role, each securable object is tagged so that you can see what drives the license requirement:

* **Entitled** – The privilege is covered by the current license and doesn't trigger a higher license.
* **Not Entitled** – The privilege isn't covered and requires a higher or different license.
* **Not Required** – The privilege is inherited from the system user and isn't included in the license calculation.

By locating **Not Entitled** privileges, you can decide whether to remove the privilege from the role in **Security configuration**, or to assign the user a higher license. Use the **Security analysis** report to find every role that includes a problematic entry point before you make a change.

Note

License usage summary is a reporting tool only. It doesn't assign licenses or change a user's access. Changes to role assignments or to a role's security objects typically take two to eight hours to appear in security governance reporting.

## Review licensing across environments

License usage summary focuses on a single environment. If your organization has multiple finance and operations apps environments, use the **User License Consumption** report in the Power Platform admin center for a tenant-wide view. To open the report, sign in to the Power Platform admin center, select **Licensing**, and then, under **Products**, select **Finance and Operations**.

The report compares required, purchased, and assigned licenses per product and highlights unlicensed, under-licensed, and over-licensed users, so that you can close gaps before per-user license validation begins. Licenses themselves are always assigned in the Microsoft 365 admin center.

Note

License consumption reporting and related licensing insights apply only to cloud-hosted environments that are connected to Microsoft Entra ID and the Power Platform admin center. They aren't available for on-premises deployments.