<!-- https://learn.microsoft.com/en-us/training/modules/set-up-financial-dimensions-finance/create-entity-backed -->
# Create an entity-backed financial dimension

Completed

* 1 minute

To create an entity-backed financial dimension, in the **Use values from** field, select a system-defined entity to base the financial dimension on.

Then, the system creates financial dimension values from that entity.

For example, if you want to create dimension values for projects, select **Projects**. The system creates a dimension value for each project name. The **Financial dimension values** page shows the values for the entity. If those values are company-specific, the page also shows the company. Company-specific dimensions, which are also known as company-striped dimensions, are only visible when you access them as a user from the associated company.

You can't create, rename, or delete entity-backed dimension values on the **Financial dimension values** page. Make those changes on the source entity instead. For example, create a new project value on the **Project** page.

An entity-backed dimension value isn't available in the dimension framework until you use it in a transaction, posting profile, journal, or similar context. A record that exists in the source entity, such as a new customer, doesn't appear as a selectable dimension value until something references it.