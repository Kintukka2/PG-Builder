<!-- https://learn.microsoft.com/en-us/training/modules/describe-dynamics-365-finance-core-capabilities/6-describe-electronic-payment-formats -->
<!-- refetched: original harvest URL returned 404 -->
# Describe electronic payment formats in Dynamics 365 Finance

Completed

* 8 minutes

In Finance, you can make electronic payments to vendors. The system provides various out-of-the-box electronic payment formats. If necessary, you can adjust existing payment formats and set up new ones. Two primary ways are available for getting file formats that you can use for methods of payment: a generic electronic export format and a built-in export format. The advantage of the generic electronic export format is that it can be changed from the finance and operations apps user interface, whereas the built-in export formats require a developer to make changes.

## Configuration

To process electronic payments, you must complete the following configurations:

* The bank account you’re making the payment from must have the identifying information required by the payment type. This information is often a combination of account number and routing number or other identifying code. Bank accounts are configured at **Cash and bank management > Bank accounts > Bank accounts**.
* You must set up a payment method for each electronic payment type. You configure the payment methods at **Accounts payable > Payment setup > Methods of payment**. The configuration is different for Electronic reporting versus built-in exports.

  + The Electronic reporting configuration requires an administrator in the system to import the format before it can be used.
  + To use the built-in format, first select the File format and add it to the list of available formats by using the **Setup** menu item on the **File formats** FastTab of the **Method of payment**.

    Once the format is available, set the **Generic electronic Export format** switch to **Yes** if using Electronic reporting or set it to **No** if using built-in exports. Then select the appropriate format in the **Export format** drop-down.

    Automated Clearing House (ACH) payments require you to select the **Payment specification** menu item on the **Method of payment** page. Then add a new payment specification to indicate the exact format:

    - Cash Concentration and Disbursement (CCD): A type of business-to-business (B2B) payment that consolidates funds from multiple accounts into a central account
    - Corporate Trade Exchange (CTX): Like CCD, but designed for large, complex payments that require detailed remittance data
    - Prearranged Payment and Deposit (PPD): An ACH type for consumer accounts that is commonly used for payroll direct deposits or recurring debits
    - **Payroll PPD**: A specific type of PPD used for direct deposits of employee wages into personal bank accounts.

      [![Screenshot of ACH Method of payment configuration.](media/06-04-method-of-payment-16-new.png)](media/04-method-of-payment-16-new.png#lightbox)
* You need to add the vendor’s bank account to which you transfer the payment. With a vendor selected on the **All vendors** page or from the **Vendor details** page, navigate to **Vendor > Set up > Bank accounts**. Enter the bank account information. Once entered, you must select this bank account in the **Bank account** field on the **Vendor details** page, FastTab **Payment**.

## Creating the payment

The process to create a payment is the same for Electronic reporting and built-in formats. Navigate to **Accounts payable** > **Payments** > **Vendor payment journal**. Create a new journal. You can add payment lines directly or use payment proposals. The important part of the line for electronic payment is the **Method of payment** field. Once you have the vendor and amount entered on the line, select the method of payment you use for this vendor. Often the default method of payment is set on the **Payment** FastTab of the **Vendor detail** page, but this setting isn't required.
[![Screenshot of a vendor payment journal using an ACH method of payment.](media/06-04-payment-journal-17-new.png)](media/04-payment-journal-17-new.png#lightbox)

Once you entered the method of payment, select the **Generate payments** menu item. In the dialog, you must select either **Payment method** or **Export format** and the Bank account. This filters the lines in the journal and only generates payment for those that match.

[![Screenshot of the Generate payments dialog for creating an electronic payment file.](media/06-04-generate-payments-18.png)](media/04-generate-payments-18.png#lightbox)

The payment file is downloaded for the user to either send to the bank or upload to the bank portal.