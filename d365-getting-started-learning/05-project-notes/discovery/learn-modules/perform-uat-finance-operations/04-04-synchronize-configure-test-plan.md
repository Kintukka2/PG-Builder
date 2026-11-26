<!-- https://learn.microsoft.com/en-us/training/modules/perform-uat-finance-operations/04-synchronize-test-plan -->
<!-- refetched: original harvest URL returned 404 -->
# Synchronize and configure your test plan in Azure DevOps

Completed

* 4 minutes

An acceptance test library is your starting point. It typically contains
all test cases (task recordings) of an application that is organized by business
processes.

During a test pass, you usually do not need to run all test cases. The
test cases that you select depend on the phase of your implementation or the
nature of the update that you are planning to apply to your production
environment.

Azure DevOps enables you to organize your test cases in test plans and
test suites. A test plan contains one or more test suites (a subset of
your test library). Test cases can belong to more than one test suite.

When you have selected your acceptance testing BPM library, synchronize
it with Azure DevOps and create your test plan and test suites.

### Sync with Azure DevOps

Synchronize your BPM library with your Azure DevOps project. For more
information, see [Synchronize a BPM library with an Azure DevOps project](/en-us/dynamics365/fin-ops-core/dev-itpro/lifecycle-services/synchronize-bpm-vsts?azure-portal=true#synchronize-a-bpm-library-with-a-azure-devops-project).

After configuration is complete, you can synchronize the BPM library with an
Azure DevOps project.

1. On the **Business process libraries** page, on the tile for the library that you want to synchronize, select the ellipsis button (...) and then select **Azure DevOps sync** (VSTS sync). You can also start Azure DevOps synchronization from the toolbar in a BPM library. Select the ellipsis button (...) and then select **Azure DevOps sync**.
2. After Azure DevOps synchronization is complete, select the ellipsis button (...) and then select **Sync test cases**. When this step is complete, your task recordings will become test cases in Azure DevOps and a link will appear under the **Requirements** tab.

[![Screenshot showing the Sync test cases.](media/04-sync-test-cases.png)](media/sync-test-cases.png#lightbox)

In addition to the test steps, the task recording XML file is attached
to the Azure DevOps test case. This file will be needed if you want to
automate test runs.