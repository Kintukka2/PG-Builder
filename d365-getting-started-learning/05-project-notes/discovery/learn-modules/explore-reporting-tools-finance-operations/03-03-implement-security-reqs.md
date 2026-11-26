<!-- https://learn.microsoft.com/en-us/training/modules/explore-reporting-tools-finance-operations/03-security-reqs -->
<!-- refetched: original harvest URL returned 404 -->
# Implement reporting security requirements

Completed

* 10 minutes

Finance and operations apps have several ways to restrict user access to
reports. Authorization is used to grant access to elements of the
program through security permissions. Security permissions are combined
into privileges, which are then combined into duties. Permissions,
privileges, and duties can be added to a role and assigned to a user.
You can use this role-based security to grant user access to reports that are based on roles.

You can view security roles that are assigned to users from the **Security configuration** page in finance and operations apps. By
selecting a role on this page, you can view the duties, privileges, and
permissions that are related to the role. You can access the Security configuration page by going to **System administration > Security > Security configuration**

[![Screenshot of the Security configuration page.](media/03-security-1.svg)](media/security-1.svg#lightbox)

To review who can access reports and data, go to **System administration > Security > Security governance**, where reports such as **Security analysis** and **Role audit trail** show role membership, privilege access levels, and the history of role assignments.

Data security is used to deny user access to tables,
fields, and rows in the database. Data security uses the extensible data
security framework (XDS) to control access to transactional data by
assigning data security policies to security roles. These policies can
restrict access to data, based on either the effective date or user
data. We recommend that you use the extensible data security to help secure data.

In addition to these security options, the Table Permissions Framework
can help protect data and is enforced by the Application Object Server (AOS). The Table Permissions Framework allows you to grant or deny Create, Read, Update, or Delete (CRUD) permissions to the data in a table. You can use this to give certain roles access to view and manipulate certain datasets.

For instance, you might want a salesperson to be able to view
and update a customer, but might want to deny them access to create
new customers or delete existing customers. To do this, you need to
grant the Read and Update permissions and deny Create and Delete
permissions for that role on the customer table.

## Table permissions framework example

Table Permissions Framework adds table-level security that verifies user
rights regardless of the request origin. For example, consider
the following scenario:

1. ABC Corporation implemented finance and operations apps. Users can access data within the application.
2. The administrator configured a security role named Management.
   Members of this role have access to sensitive financial data. One of
   the tables that stores the sensitive financial data is named
   ManagerFinancialData. Previously, this table was added as part of a
   customization for the application.
3. The administrator configures the ManagerFinancialData table so that
   AOS must authorize all operations for that table.
4. Before allowing Read access to data in the ManagerFinancialData
   table, AOS will verify that the user is a member of the
   Management role and that members of that role have permissions to
   read the data. If the user is not a member of the Management role,
   AOS will deny the read operation.