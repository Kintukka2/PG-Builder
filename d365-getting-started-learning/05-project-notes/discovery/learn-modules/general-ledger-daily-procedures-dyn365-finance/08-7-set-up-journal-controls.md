<!-- https://learn.microsoft.com/en-us/training/modules/general-ledger-daily-procedures-dyn365-finance/7-journal-controls -->
<!-- refetched: original harvest URL returned 404 -->
# Set up journal controls

Completed

* 10 minutes

You can set up restrictions on the company, account type, and segment values.

For example, by using the journal control for a journal name, you can only allow the journal to be used for adjustments. In this case, you can specify that only the **Ledger** account type is valid across all companies or a specific company.

One or more of the following accounts types can be selected in the journal control:

* **All** - Includes all account types.
* **Ledger** - Select this account type if you want to use a specific value or a range of values for the main accounts, or financial dimensions defined in the selected account structure only. The Ledger and All types are the only two options that allow you to select which segment values (financial dimensions) are valid for the selected journal.
* **Bank**
* **Customer**
* **Vendor**
* **Fixed assets**
* **Project**

After you’ve completed the setup of the journal control on a journal name, when you use the journal name, the journal control first checks the validity of the account types as well as any values defined for either accounts or segments (financial dimensions). If the validation fails upon posting, you will receive an error.

Watch this video to learn how you can use journal control for a journal name.

To set up a journal control, follow these steps:

1. Go to **General ledger > Journal setup > Journal names**.
2. In the list, find and select a record.
3. **Journal control**.
4. Select **Add**.
5. In the **Company accounts** field, select the drop-down button to open the lookup.
6. In the list, find and select a record.
7. Select **Add**.
8. In the **Account structure** field, select the drop-down button to open the lookup.
9. In the list, find and select a record.
10. In the **Segment** field, select the drop-down button to open the lookup.
11. In the list, select a financial dimension.
12. In the **From value** field, select the drop-down button to open the lookup.
13. In the list, find and select a record.
14. In the **To value** field, select the drop-down button to open the lookup.
15. In the list, find and select a record.