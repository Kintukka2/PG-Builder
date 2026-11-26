<!-- https://learn.microsoft.com/en-us/training/modules/mobile-experiences-finance-operations/enable-virtual-entities -->
# Enable virtual entities

Completed

* 12 minutes

Now that you've set up Dataverse virtual entities, you can enable the virtual entities in the Dataverse environment. Make sure that you enable virtual entities in Dataverse because all entities in finance and operations apps aren't available as virtual entities by default. When enabling virtual entities in Dataverse, you can determine which entities are exposed as virtual entities and used in Dataverse.

Watch the following video for a demonstration of how to enable virtual entities.

Your first task is to create general virtual entities.

1. Go to [https://admin.powerplatform.microsoft.com](https://admin.powerplatform.microsoft.com/?azure-portal=true) and sign in.
2. Select **Environments** in the left pane.
3. Select the environment that's associated with your finance and operations apps environment.
4. In the **Details** section of the **Environment** page, select the **Environment URL** link to open the Microsoft Power Platform environment.
5. Select the gear icon in the upper-right corner of the page, and then select **Advanced settings**.
6. In the upper right of the **Settings** page, select the **Advanced find** filter icon.
7. On the **Advanced Find** page, select **Available Finance and Operations Entities** in the **Look for** dropdown list.
8. Add more filter criteria as needed if you're looking for a specific entity.

   [![Screenshot of the look for filter menu.](media/05-filter.svg)](media/filter.svg#lightbox)
9. For any entity that you want to enable for virtual entities, select the entity in the list and then select the **Visible** checkbox.

   [![Screenshot of the entity with the visible button selected.](media/05-enable-entity.svg)](media/enable-entity.svg#lightbox)