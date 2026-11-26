<!-- https://learn.microsoft.com/en-us/training/modules/role-security-finance-operations/5-security -->
# Apply security permissions

Completed

* 10 minutes

Users are assigned to security roles in the System administration module in finance and operations apps. To review and customize the security elements themselves, go to **System administration > Security > Security configuration**.

[![Screenshot of the Security configuration page.](media/05-security-1.png)](media/security-1.png#lightbox)

You can automatically assign users to roles by using queries from Visual Studio, or you can manually assign an individual user to a role. Additionally, you can choose to have a user excluded from automatic role assignment by resetting her or his status.

Follow these steps to assign users to roles automatically:

1. In finance and operations apps, open the
   Navigation pane by selecting the menu icon in the top-left corner of the page.
2. Under the **Modules** node, select **System administration**.
3. Select **Security** to expand the node, and then select **Assign users to roles**.
4. In the left column, select the role that you want to assign users to, such as **Accounts payable clerk**.
5. In the middle column, beneath the **Rules for dynamically assigning users to role** heading, select **Add rule**.
6. Select your desired query name for the rule, such as
   **LedgerJournalPostControl**.
7. To modify the query, such as removing a company from the rule or adding a table join, select **Edit query**.
8. In the Action Pane, select **Run automatic role assignment**. You will see the users that have been added in the middle column under the **Users assigned to role** heading.