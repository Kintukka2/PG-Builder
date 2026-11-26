<!-- https://learn.microsoft.com/en-us/training/modules/plan-implement-legal-entities-finance-operations/3-create-number-sequence -->
# Create a number sequence

Completed

* 12 minutes

Before you can create new records for a reference, you must set up a number sequence and associate it with the reference for a specific module in finance and operations apps.

Number sequences are used to generate readable, unique identifiers for master data records and transaction records that require identifiers. A master data record or transaction record that requires an identifier is referred to as a reference.

We recommend that you use the pages in **Organization administration** to set up number sequences. If module-specific settings are required, you can use the **Parameters** page in a module to specify number sequences for the references in that module. For example, in Accounts receivable and Accounts payable, you can set up number sequence groups to allocate specific number sequences to specific customers or vendors.

You can set up all required number sequences at the same time by using the **Set-up number sequences** wizard, or you can create or modify individual number sequences by using the **Number sequences** page.

When you set up a number sequence, you must specify a scope, which defines which organization uses the number sequence.

By default, the following scopes can be used:

* **Shared** - A single number sequence is used for all organizations. The *Shared scope* is available only for some references.
* **Company** - A separate number sequence is used for each company.
  Use the **Company** scope when the underlying table includes the **DataAreaId** field. For example, use this scope for the number sequence for the customer account number that is in the **Customer** table *CustTable*.
* **Legal entity** - A separate number sequence is used for each legal entity.
  Use the **Legal entity** scope when the underlying table does not include the **DataAreaId** field and has a foreign key to the legal entity table **CompanyInfo**. For example, use this scope for the number sequence for the expense report number that is in the expense report table **TrvExpTable**.
* **Operating unit** - A separate number sequence is used for each operating unit.
* **Company and Fiscal calendar period** - A separate number sequence is used for each company and fiscal calendar period combination.
* **Legal entity and Fiscal calendar period** - A separate number sequence is used for each legal entity and fiscal calendar period combination.
* **Operating unit type** - A separate number sequence is used for each type of operating unit.

For example, you can set up separate number sequences for cost centers and departments.

The scope defines which organizations use the number sequence. In addition, number sequence formats consist of segments. Number sequences with a scope other than Shared can contain segments that correspond to the scope. For example, a number sequence with a scope of Legal entity can contain a legal entity segment. By including a scope segment in the number sequence format, you can identify the scope of a record by looking at its number.

In addition to segments that correspond to scopes, number sequence formats can contain Constant and Alphanumeric segments. A Constant segment contains a set of letters, numbers, or symbols that does not change.

An Alphanumeric segment contains a set of letters or numbers that increment every time that a number is used. It uses a number sign (#) to represent incrementing numbers and an ampersand (&) to represent incrementing letters.

Watch this video to learn how to create a new number sequence by using a wizard.

After you have configured the system-required number sequences, you probably need to create additional number sequences that address the specific requirements to identify certain records with specific formats.

For example, you might need to create a number sequence with a format of GTL-APINV-&#######, which will result in a range of values like; GTL-APINV-A0000001 through GTL-APINV-Z9999999. When this number sequence is out of available values, as part of periodic processing, you need to create a new number sequence and replace it in any references where it has been assigned.

Often, some businesses, or country/region requirements, demand that you change number sequences even when there are still available values.

## Continuous and non-continuous number sequences

Number sequences can be continuous or non-continuous.

* **Continuous number sequence** - Doesn't skip any numbers, but numbers may not be used sequentially.
* **Non-continuous number sequence** - Numbers are used sequentially, but the number sequence can skip numbers.

For example, if a user cancels a transaction, a number is generated, but not used. In a continuous number sequence, that number is recycled later. In a non-continuous number sequence, the number is not used.

We do not recommend changing a non-continuous number sequence to a continuous number sequence. The number sequence will then not be truly continuous. This change can also cause duplicate key violations in the database. In addition, continuous number sequences have a larger effect on performance.

Continuous number sequences are typically required for external documents, such as purchase orders, sales orders, and invoices. However, continuous number sequences can adversely affect system response times because the system must request a number from the database every time that a new document or record is created.

If you use a non-continuous number sequence, you can enable **Pre-allocation** on the **Performance** FastTab on the **Number sequences** page. When you specify a quantity of numbers to pre-allocate, the system selects those numbers and stores them in memory. New numbers are requested from the database only after the pre-allocated quantity has been used.

Unless there is a regulatory requirement that you use continuous number sequences, we recommend that you use non-continuous number sequences for better performance.

## Chronological numbering

For available document references, you can create period-effective number sequence groups and connect them to unique number sequences. When creating similar documents based on document dates, a proper number sequence category will be automatically assigned.

When you post a document, the document is assigned to the appropriate number sequence category based on the document's posting date, which is then used to create a document number based on the detected number sequence. A notification about the number sequence group assignment is sent by the system.

Note

For some countries or regions, there is a specific logic already implemented for document numbering. In this case, country-specific or region-specific logic will override the Chronological numbering feature.

## Automatic cleanup of number sequences

In case of a power failure, an application error, or other unexpected failure, finance and operations apps cannot recycle numbers automatically for continuous number sequences. You can run the cleanup process manually or automatically to recover the lost numbers.

Carefully consider server usage when you plan the cleanup process. We recommend that you perform the cleanup as a batch job during non-peak hours.

After number sequences are configured, the next logical step is to plan and organize organization hierarchies.