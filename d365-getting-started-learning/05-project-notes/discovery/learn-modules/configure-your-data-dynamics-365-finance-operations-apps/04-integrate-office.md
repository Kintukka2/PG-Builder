<!-- https://learn.microsoft.com/en-us/training/modules/configure-your-data-dynamics-365-finance-operations-apps/integrate-office -->
# Integrate with Microsoft Office

Completed

* 2 minutes

The Dynamics 365 applications natively integrate with Microsoft Office so that
users will be more quickly productive. The familiar look and feel of Microsoft
Products allow for a more unified experience and smoother learning curve.

#### Excel

In forms in Dynamics, you will see the Office logo. It may have an option to
**Export to Excel** (which is a simple export). It may also have **Open in
Excel**, along with any entities available on the underlying form. **Open in
Excel** uses the Excel Data Connector add-in, which requires Microsoft Excel
2016 or later, and it lets you publish your changes back to the app.

Some great references are:

[Office integration overview](/en-us/dynamics365/fin-ops-core/dev-itpro/office-integration/office-integration?toc=/dynamics365/commerce/toc.json)

[View and update entity data with Excel](/en-us/dynamics365/fin-ops-core/fin-ops/mobile-apps/use-excel-add-in?toc=/dynamics365/commerce/toc.json)

[Excel Data Connector add-in](/en-us/dynamics365/fin-ops-core/dev-itpro/office-integration/office-integration#excel-data-connector-add-in)

#### Outlook

Finance and Operations apps give you the option to configure and send email
using several different types of providers. On the **Email parameters** page,
Microsoft Graph is the recommended provider for organizations that use Microsoft
365, and it replaces the deprecated Exchange provider. You can also send email
through SMTP. Once setup is done, you can configure notifications or alerts to
be sent, and external-facing documents to be sent to, say, vendors or customers.

For reference: [Configure and send email](/en-us/dynamics365/fin-ops-core/fin-ops/organization-administration/configure-email?toc=/dynamics365/commerce/toc.json)

#### Document management

Finance and Operations apps give you the option to attach documents to a record.
The document is stored externally, in Azure Blob storage or SharePoint
Online. Azure Blob storage is the default, and database storage is deprecated.
The documents can be in many different formats, like pictures,
documents, or spreadsheets.

For reference: [Document management](/en-us/dynamics365/fin-ops-core/dev-itpro/office-integration/office-integration?toc=/dynamics365/commerce/toc.json#document-management)