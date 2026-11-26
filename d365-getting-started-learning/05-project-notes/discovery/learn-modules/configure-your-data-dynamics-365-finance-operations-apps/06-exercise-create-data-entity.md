<!-- https://learn.microsoft.com/en-us/training/modules/configure-your-data-dynamics-365-finance-operations-apps/exercise-add-field-data-entity -->
<!-- refetched: original harvest URL returned 404 -->
# Exercise – Add a field to a data entity

Completed

* 4 minutes

Often, we want to add a field to a data entity. Maybe it wasn’t deemed necessary
initially, or maybe it’s a new field.

1. Navigate to the **Data management** workspace and select the **Data
   entities** tile. The list of data entities may need to refresh itself.
2. Filter to the **Production orders** entity and highlight it. If you can't find it, return to the Data management workspace, Framework parameters, Entity settings, and refresh the entity list.
3. Select **Modify target mapping**.
4. All the fields in the Production orders entity are already mapped, so we’ll
   need to create our own task. Highlight the line which maps DELIVERYDATE and
   delete it.
5. Confirm the deletion.
6. Now we can add a field, pretending it’s the new field we need. Select
   **+New**.
7. Type or select DELIVERYDATE as the Staging field. It’s not case sensitive.
8. Type or select DELIVERYDATE as the Target field.
9. Select Generate mapping. You can say **No** to generating from scratch, and
   the system will only do changes.
10. Notice that the DeliveryDate is now in both the Mapping details list, and the
    Mapping visualization.
11. Delete the mapping, and redo it in the visualization by drawing a line
    between the fields.