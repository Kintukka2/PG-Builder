<!-- https://learn.microsoft.com/en-us/training/modules/perform-uat-finance-operations/02-uat-libraries -->
<!-- refetched: original harvest URL returned 404 -->
# Create user acceptance test libraries

Completed

* 3 minutes

Business process modeler (BPM) is a Lifecycle Services (LCS) tool that helps you define and organize business processes and user tasks. You can also use LCS to create and distribute BPM libraries across projects by using the Asset library.

Important

Lifecycle Services is being replaced by the Microsoft Power Platform admin center as the unified administration experience for Dynamics 365 Finance, Dynamics 365 Supply Chain Management, and Dynamics 365 Project Operations. Beginning February 16, 2026, new customers can't create cloud implementation projects in Lifecycle Services. Existing customers with active Lifecycle Services projects continue to have access to BPM. For more information, see [Lifecycle Services project creation freeze](/en-us/dynamics365/fin-ops-core/dev-itpro/lifecycle-services/lcs-project-creation-freeze?azure-portal=true) and [Overview of unified admin experience for finance and operations apps](/en-us/power-platform/admin/unified-experience/finance-operations-apps-overview?azure-portal=true).

### Create a BPM library

BPM libraries can be either global libraries or corporate libraries. Before you can edit a library, you must add it to your Lifecycle Services project. However, before you can edit and work with a BPM library, it
must be part of your Lifecycle Services project. Microsoft-published libraries appear under **Global libraries**. Libraries published by your organization appear under **Corporate libraries**.

BPM doesn't support localization. If you make changes in a language other than US English, those changes are visible only when you view BPM in that same language. To see changes that were made in US English, synchronize with Azure DevOps.

You can create a BPM library in multiple ways.

To create a library, sign in to Lifecycle Services and open **Business process modeler** from either the tile or the LCS menu. Then create a new library.

![Screenshot of the Business process modeler tile.](media/02-bpm-1.png)

You can also create a library by importing data from Microsoft Excel.

[![Screenshot of the Microsoft Excel import button.](media/02-bpm-import-excel.png)](media/bpm-import-excel.png#lightbox)