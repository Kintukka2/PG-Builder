<!-- https://learn.microsoft.com/en-us/training/modules/implement-common-integration-features-finance-ops/4-documents -->
<!-- refetched: original harvest URL returned 404 -->
# Document management

Completed

* 8 minutes

Document management supports saving record attachments in Azure Blob storage and SharePoint Online. Database storage is obsolete. Azure Blob storage is equivalent to storage in the database because documents can only be accessed through the application, and it offers the added benefit of providing storage that doesn't negatively affect the performance of the database.

[![Screenshot of the Document management parameters.](media/04-document-management-parameters.svg)](media/document-management-parameters.svg#lightbox)

Azure blob storage is the default and works immediately. SharePoint storage will work immediately if you have a Microsoft 365 license because it auto-discovers the SharePoint tenant, such as a user on the TenantA.onmicrosoft.com. Microsoft 365/Microsoft Entra tenant gets TenantA.sharepoint.com as the SharePoint site. If document management has been turned off by the user, turn it on by selecting **Common > Setup > User options > Preferences > Miscellaneous** and setting **Document handling active** to **Yes**.

On any page that has data, an **Attach** button will be available in the upper-right corner. The **Attachments** page provides a view of the attachments (documents) that are associated with the record that was selected on the previous page. You can add new attachments to the record by selecting the **New** button (**+**) in the app bar. For the **File** and **Image** document types, you will be prompted to provide the associated file.

A preview for supported file types is provided on the **Preview** FastTab. Basic document types, such as PNG images and text files, are supported by default. Office document types, such as Microsoft Word, Excel, and PowerPoint files, must use a production Office Web Apps Server, which might not be available in a OneBox configuration.

The automatically generated **Open in Excel** experiences that are created for entities have a single table binding.

A developer in your team can help you achieve the following by using Visual Studio.

* You can suppress the static Export to Excel mechanism for a grid or change the label that appears on the **Open in Microsoft Office** menu.
* The list of fields that are added to that table binding is defined by the **AutoReport** field group if the table binding contains fields. Otherwise, the key and mandatory fields for the entity are automatically added. The order of fields in the **AutoReport** group determines the order of fields in the table binding.
* Templates that are registered as system-defined templates are loaded at deployment. This behavior is useful for independent software vendors (ISVs) and partners that want to package templates together with other model artifacts.

### Preview documents

You can specify the destinations for various print management actions for configurable business documents. This means that for a preview, the scenario **Preview/Print > Original** can be used, and for email and printing, **Preview/Print > Use print management** can be used.

## Templates

When a template listed in the **Common > Common > Office integration > Document templates** page (DocuTemplate) has **ShowInOpenInOfficeMenu** set to **Yes** and has the same root datasource (table) as the current page, it will be added as an option in the **Open in Excel** section of the **Open in Microsoft Office** menu.

A template is an artifact that needs to be maintained and versioned.

Create a template if:

* You need additional content or formatting in the template.
* You want to combine multiple entities or data sources in the same workbook.

When creating a template for an entity that has country or region-specific fields, you should leave those region-specific fields out of the template. Otherwise, all users will see the country or region-specific fields.

Templates should cater to most users by default and region-specific users can add those fields by using the easy-to-use design experience of the Excel add-in. The region-specific fields and columns can be added by users as needed. That template can be either saved to local computer for reuse by a single user or uploaded via the **Document Templates** page for reuse by any user of that instance. A couple of other considerations:

* If a region has a country or region-specific entity, then a country or region-specific template could be created.
* If a region is important enough, then you could define a country or region-specific template and a country or region-generic template.

## Scan file attachments for malicious threats

When working with file attachments, your organization may want files to be scanned for any malicious threats before the document is uploaded to Dynamics 365. There is an extension point in the application that lets you integrate file scanning software of your choice into the file upload process. There are also similar extension points that are available for scanning attachments.

The **FileUploadResultBase** class exposes the **delegateScanStream()** delegate. The delegate applies to any file upload where the **Upload strategy** class has been specialized. If the scanning software determines that the upload is malicious, the upload process will fail.