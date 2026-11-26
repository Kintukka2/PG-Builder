<!-- https://learn.microsoft.com/en-us/training/modules/general-ledger-daily-procedures-dyn365-finance/6-voucher-templates -->
<!-- refetched: original harvest URL returned 404 -->
# Create voucher templates

Completed

* 15 minutes

A voucher template serves as the basis for future vouchers in other journal entries. You can use voucher templates with general journals and financial subledger journals, such as Accounts payable and Accounts receivable journals.

You can create a voucher template from a journal line (voucher) as either the **Percent** or **Amount**, but the same voucher cannot have both types.

If you save the voucher as **Percent**, the voucher amounts are converted to percentage factors. This conversion allows any amount to be applied when the voucher template is selected. To use this method, you must have multiple voucher lines that share the same voucher number.

When selecting a voucher template in a journal, the **Amount** field is only displayed if the voucher template is of type **Percent**.

If you save the voucher as **Amount**, the actual amounts are stored in the template and applied when you use the template in a journal entry.

To create a voucher template, start by creating a journal line. You don't need to post the voucher before creating the template. After you create the template as either **Percent** or **Amount**, it remains available in Finance unless the journal line is deleted.

You can also save a previously posted journal voucher as a template.

Watch this video to learn how you can create and use voucher templates as both **Amount** and **Percent** to be used within the same or other journals.

**To understand the voucher templates, consider the following scenario**:

An accounting manager enters a voucher to record interest expense on a fixed-rate long-term note. The voucher debits Interest expense and credits Interest payable for 350.00 US dollars (USD) each.

Because this voucher uses the same amount each month, the accounting manager saves it as an amount-based voucher template to reduce future data entry.

The next time the accounting manager records interest expense, they select **Functions** > **Select voucher template** and choose the interest entry. The original ledger accounts and amounts are loaded into the form automatically.

## Simulate posting

You can find **Simulate posting** on the **Validate** menu for most journals. When you validate a journal using the **Validate** function, Finance tests the journal for specific error conditions. If you use **Simulate posting**, Finance runs the same processes as posting without posting the journal. Review the posting messages, correct any errors, and then select **Post** to post the journal.