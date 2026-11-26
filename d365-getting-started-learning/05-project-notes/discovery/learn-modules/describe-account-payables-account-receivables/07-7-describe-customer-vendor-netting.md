<!-- https://learn.microsoft.com/en-us/training/modules/describe-account-payables-account-receivables/7-describe-customer-vendor-netting -->
# Describe customer/vendor netting in Dynamics 365 Finance

Completed

* 8 minutes

Customer/vendor netting is a feature in Dynamics 365 Finance that allows organizations to **offset open customer and vendor balances** when the same party exists as both a customer and a vendor. Instead of handling separate payments and settlements, netting reduces the number of transactions by applying the balances against each other and settling only the remaining amount.

Netting is enabled by linking a customer account to a vendor account (or vice versa) in the party record. Once this customer-vendor relationship is defined, the system can automatically compare open customer invoices and vendor invoices during settlement. If both sides have open balances, the smaller balance is offset, and only the net difference is settled. This netting process helps reduce unnecessary cash movement, simplifies accounts payable and accounts receivable processing, and provides a clearer picture of a party’s true outstanding balance.

Netting can be performed during the normal settlement process or initiated directly from the **Settle transactions** page. Users can select invoices, preview the proposed netting impact, and post the settlement once confirmed. The system updates both accounts accordingly, decreasing the vendor liability and decreasing the customer receivable for the offset amount.

Because netting is fully integrated with settlements, it supports common financial scenarios such as credit memos, multi-currency transactions, and partial settlements. Without netting, each invoice must be paid or settled individually. With netting, Dynamics 365 Finance consolidates these steps, reduces payment volume, and ensures more efficient cash and balance management across the organization.

[![Diagram of a Customer/Vendor netting example.](media/07-6-7-netting.png)](media/6-7-netting.png#lightbox)

## Netting features

Dynamics 365 Finance includes several features that support structured and efficient customer/vendor balance netting.

### Netting agreements

A **netting agreement** defines which customer and vendor accounts can be netted together. Once activated, it controls which account pair is eligible for netting and ensures consistency during the process.

### Netting journals

When invoices are netted, the system automatically posts a **netting journal** to settle the customer and vendor balances using a temporary bridging account.

### Manual netting

Users can manually select open customer and vendor invoices to net. The system automatically calculates the nettable amount and posts a journal that settles both sides.

### Automatic netting

Organizations can automate netting by defining **netting rules** including invoice selection order and optional filters and running them manually, on demand, or through scheduled automation.

### Reversals and history

Posted netting transactions can be reversed, which automatically unsets both the customer and vendor invoices and reverses the journal. Users can also review **netting history** and print **netting advice** to share with customers or vendors.

### Intercompany netting

For organizations with multiple legal entities, Dynamics 365 supports **intercompany netting**, allowing customer/vendor pairs across entities to be netted while automatically generating the required intercompany accounting entries.