<!-- https://learn.microsoft.com/en-us/training/modules/plan-config-global-address-book-finance-operations/2-gab-function -->
<!-- refetched: original harvest URL returned 404 -->
# How the global address book works

Completed

* 8 minutes

A party record can belong to one or more address books. Each party record can store one or more locations, or addresses, and is assigned a party role. The role that is assigned to the party record can have specific transactions types associated with it. The following sections provide more information about party roles, locations, and transaction types.

The global address book can help you understand the relationships among people and organizations that are associated with your organization.

For example, a customer can also be a vendor in a marketing campaign, or a worker in your organization can also be a vendor.

## Creating new party records

There are two ways to enter party records in the global address book:

* **Creating a party record when you don't know the role** - When you create a party record and don't know the role type (for example, you don't know whether the party is a customer or an opportunity), you create the record in the global address book. You can select the role type later.
* **Creating a party record when you know the role** - If you know the role type for the party, you can create a record on the appropriate page for that type. For example, if the party is a customer, you create a record on the **Customer** page. When you create and save a record by using the page for the party's role type, the record is automatically created in the global address book.

For transactions that are a part of the business processes, multiple parties might be associated with each transaction. An example is a customer that needs to be referenced on project quotations.

Each party record’s addresses, locations, and contact information are shared across all the party roles that are associated with that party. Therefore, when any of this information is changed, all other associated records are updated accordingly. When a party role is included in a transaction, the location, address, or contact information of the party can be accessed when transaction details are entered.

You can check for duplicate records directly from the **Global address book** list page. On the **Action Pane**, on the **Party** tab, in the **Maintain** group, click **Check for duplicates**. Then select the values to include in the check for duplicates.

[![Screenshot of check duplicates page with values selected.](media/02-check-for-duplicates.png)](media/check-for-duplicates.png#lightbox)

To add multiple party records to an address book, on the **Global address book** list page, select the parties in the list. Then, on the **Action Pane**, on the **Party** tab, in the **Maintain** group, click **Assign parties**. Select the address books to add the selected party records to, and then click **OK**. All the selected party records are added to the address books that you selected.

To remove multiple party records from an address book, on the **Global address book** list page, select the parties in the list. Then, on the **Action Pane**, on the **Party** tab, in the **Maintain** group, click **Remove parties**. Select the address books to remove the parties from, and then click **OK**. All the selected party records are removed from the address books that you selected.

Sometimes, you might have to change the party type of a record from person to organization or from organization to person. To change a party record from one party type to another, you must first create a new party record of the correct type in the global address book. You then associate the old party record with this new record. After you have made the new party association, delete the original party record that has the incorrect record type.

To update the name of a party record, open the party record, and then, on the **Action Pane**, click **Edit**. On the **General** FastTab, enter the new name for the party, and then save the record.

To update an address for a party record, open the party record, and then, on the **Addresses** FastTab, select the address to update. Click **Edit**, and then, on the **Edit address** page, make the required changes to the address or address parameters.

Occasionally, you might want to merge two or more party records into a single record. This can occur if you create one or more duplicate party records, either on purpose or unintentionally. When you merge party records, you select one record to keep.

The information from the other records is then merged into this record. You can’t merge party records that are associated with the same party role, such as customer or vendor, in the same legal entity. You can’t merge internal party organization records in the same legal entity, team, or operating unit.

You can enter party records either in the global address book or on the appropriate entity page. When you add a record in one location, the same record is always added in the other location. For example, if you add a party record for a customer in the global address book, the record is also added on the **Customer** page. Likewise, if you add a party record for a customer on the **Customer** page, the record is also added in the global address book.

If you need to create a party record but don't know the entity type (for example, you don't know whether the entity is a customer or an opportunity), create the record in the global address book. You can select the entity type later.

If you know the entity type for the party, you can create a record on the applicable page for that type. For example, create a record for a customer on the **Customer** page. When you create and save a record by using the appropriate entity page, the record is automatically created in the global address book.

You can set up translations of address information, so that the information appears in your user language (system language) in Microsoft finance and operations apps but in another language on documents such as sales orders. You can enter translations for country/region names, addresses, and name sequences.

For example, your system language is Italian, and you create a sales order for a customer in Germany. In this case, you can view the customer record in Italian in finance and operations apps but display the address information in German on the printed sales order.

When you set up translations, you should enter a translation for every item in the list. Any items that you don't enter a translation for will appear in the system language.

For example, your system language is French, and you send a document to a customer in Spain. If you haven't entered Spanish (ESP) translations for the address information, that information will appear in French both in finance and operations apps and on the printed document.