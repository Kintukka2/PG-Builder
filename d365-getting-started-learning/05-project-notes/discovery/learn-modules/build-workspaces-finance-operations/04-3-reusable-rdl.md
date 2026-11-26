<!-- https://learn.microsoft.com/en-us/training/modules/build-workspaces-finance-operations/3-reusable-rdl -->
# Create custom reusable report functions by using RDL

Completed

* 5 minutes

Report Definition Language (RDL) is an XML representation of an SQL Server Reporting Services (SSRS) report definition. A report definition contains data retrieval and layout information for a report. You can add your own custom functions for controlling report item values, styles, and formatting by accessing code assemblies within report definition files.

RDL can be used to define charts, graphs, calculations, text, images, and other report objects. RDLs can be created by using the Microsoft .Net Framework classes. Specifically, the XmlTextWriter class can write an RDL. You can also extend existing RDLs to add items with custom properties. The reports that are created by using RDL can be exported as a .rdl file, which contains the report data, calculations, and report layout. All SSRS reports generate a .rdl file.