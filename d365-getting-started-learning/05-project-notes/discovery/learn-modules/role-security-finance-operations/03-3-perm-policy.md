<!-- https://learn.microsoft.com/en-us/training/modules/role-security-finance-operations/3-perm-policy -->
# Enforce permissions policy

Completed

* 5 minutes

Permissions policies are used in role-based security to grant access to
users for specific purposes. The most common type of security policy
originates from a query that is stored in the AOT.

A query specifies the criteria that each row or record must satisfy to be
returned by using the **Ranges** node in its data source. The **Fields**
node specifies which fields should be returned. You can create a field
security profile to use the permissions policies to restrict access to a
certain field. After you create the profile, you can assign users or teams to that profile and then set up specific read, create, or write permissions for the field.

You can use permissions policies to ensure that users can view and access all necessary areas of finance and operations apps, from pages within the navigation pane to specific buttons on a page. A new security policy is added to a project through the **Solution Explorer** window by following the same steps as adding a new role, duty, or privilege to a project. In the **Properties** window, you can specify the details of the policy, such as the query that is the basis for the policy and the **Primary Table**, which is the first data source in the query that is assigned to the policy. Additionally, you can specify the **Context Type**, which is used to determine whether the policy is applicable.

The following image shows the **Properties** window of the
`RetailCustomer` security policy that uses the
`RoleName` context type. The **Role Name** property has been filled in to specify that the `RetailStoreManager` role is
associated with this policy.

[![RetailCustomer security policy Properties window.](media/03-retail-policy.png)](media/retail-policy.png#lightbox)

The following image is the **Properties** window of the
`FMSelfServ` security policy that uses the
`ContextString` context type. Notice that different fields
are used as you select a different context type.

[![Properties window for the FMSelfServpolicy.](media/03-fm-policy.png)](media/fm-policy.png#lightbox)