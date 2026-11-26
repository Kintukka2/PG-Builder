<!-- https://learn.microsoft.com/en-us/training/modules/role-security-finance-operations/8-summary -->
# Summary

Completed

* 10 minutes

The security structure in finance and operations apps is role-based, and all users must be assigned a role to gain access to the application.

Role-based security uses a hierarchy, with permissions representing the most granular security control and roles representing the least granular
control. Permissions are assigned to privileges, privileges are assigned
to duties, and duties are assigned to roles. A role represents the broad,
daily responsibilities for a job. A duty correlates to a business
process. A privilege represents access to perform a job task. Lastly, a
permission represents access to a securable object, such as a specific
button, field, or page in the user interface.

While users are assigned to roles in the finance and operations apps
application by using the System administration module, new roles,
duties, privileges, and permissions are created in Visual Studio. A data
security policy denies access to certain elements in the user interface.
By using the XDS framework, you can assign data security policies to roles.

Security permissions policies define access to various parts of the
system and are created based on queries. Many security policies exist in the AOT, but like other security elements, you can create new security
policies by adding an item to your project in the **Solution Explorer**
window.

Finally, because a user's assigned roles determine the license that the user requires, you can use the user security governance reports at **System administration > Security > Security governance** to review license requirements for each user, role, duty, and privilege, and the User License Consumption report in the Power Platform admin center for a tenant-wide view.

## Links to related modules (and sites) for specific topics

| Topic | Link |
| --- | --- |
| Role-based security overview | [Role-based security](/en-us/dynamics365/fin-ops-core/dev-itpro/sysadmin/role-based-security/?azure-portal=true) |
| User security governance | [User security governance overview](/en-us/dynamics365/fin-ops-core/fin-ops/sysadmin/security-gov-overview/?azure-portal=true) |
| License usage reporting | [License usage summary overview](/en-us/dynamics365/fin-ops-core/fin-ops/sysadmin/security-gov-license-usage-summary/?azure-portal=true) |