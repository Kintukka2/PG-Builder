<!-- https://learn.microsoft.com/en-us/training/modules/describe-account-payables-account-receivables/2-describe-payment-setup -->
# Describe payment setup

Completed

* 15 minutes

Before processing invoices and payments in Accounts payable, you need to set up vendor information that controls how each vendor is handled in financial processes. The system stores details such as business identity, tax registration, payment methods, posting rules, and settlement behavior on the vendor record. This setup ensures that all vendor transactions follow consistent rules across the organization.

The **Vendors** page is the central location for creating and maintaining vendor accounts. Here, you define the vendor’s name, address, contact information, tax authority assignments, and default values that help automate Accounts payable processes. Many of these values flow directly into purchase orders, product receipts, vendor invoices, and payments, which reduces manual entry and supports accurate reporting.

## Key types of information stored with a vendor

### Terms of payment

Each vendor can have default payment terms that determine due dates for invoices and purchase orders. These terms flow directly into vendor documents, helping organizations control cash flow and manage payment schedules.

### Methods of payment – vendors

The vendor record stores how the organization pays the vendor—for example, by electronic payment, check, or other payment method. These settings determine how payment journals and proposals are generated.

### Vendor groups

Vendors can be assigned to groups that share similar parameters. Vendor groups drive posting rules, settlement behavior, reporting, and forecasting. Setting defaults at the group level helps streamline setup and ensures vendors with similar characteristics use consistent accounting rules.

### Vendor posting profiles

Posting profiles determine which ledger accounts are used when vendor invoices, payments, prepayments, and settlements are posted. The vendor record can reference a specific posting profile, or it can inherit rules from its vendor group or the **All vendors** default. These rules ensure that financial transactions follow the organization's chart of accounts structure.

### Vendor bank accounts

You store one or more bank accounts on the vendor record for use during payment processing. When you generate payments, the system uses these accounts to determine where to send funds and to ensure it uses the correct account identifiers for electronic payment methods.

### Accounts payable parameters

Although not stored directly on the vendor record, these parameters interact with vendor settings to define default behaviors such as settlement rules, number sequences, payment validation, and invoice matching. Vendor specific values are combined with legal entity-wide Accounts payable settings to determine the final processing behavior.

### Vendor-specific tax and regulatory information

Vendor accounts also store tax registrations, 1,099 classifications (for U.S. organizations), sales tax groups, and reporting authorities. These values help ensure that invoices calculate taxes correctly and that the organization meets statutory reporting requirements.