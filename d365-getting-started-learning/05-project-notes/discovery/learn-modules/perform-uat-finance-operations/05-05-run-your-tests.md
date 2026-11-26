<!-- https://learn.microsoft.com/en-us/training/modules/perform-uat-finance-operations/05-run-tests -->
<!-- refetched: original harvest URL returned 404 -->
# Run user acceptance tests

Completed

* 17 minutes

To run your user acceptance tests, you will need to create a test plan and test suite in
Azure DevOps. This will allow you to run an ordered suite of test cases
and easily manage, investigate, and track the results.

1. Sign in to Azure DevOps and select the project and test plan that you want to test in.
2. On the toolbar, select **Test > Test Plans**.
3. On the left pane, select the drop-down next to the green plus **+** sign and then select **Static suite**.
4. Enter a name for the suite.
5. Select **Add existing** and query the tag **Lifecycle Services:Test Cases**.
6. Select **Run > Add test cases**.
7. Select the test case to view details and the attached XML file.

Create various test suites under the same test plan and then
use custom queries to add specific test cases to a test suite. A test
case can belong to more than one test suite.

### Run manual test cases

When you have a test suite, you are ready to use it for regression
testing after updates have been made to your finance and operations apps
application in a sandbox or test environment. You can run the test cases
in your test suite manually. Alternatively, you can play the task recordings that are part of
the test suite and use Azure DevOps to denote the test cases as passed or failed.

![Screenshot of the manual tests outcome field.](media/05-manual-tests.png)

Azure DevOps also provides a tool, named Test Runner, to manage manual
test case runs. For more information about using Test Runner,
see [Run manual tests](/en-us/azure/devops/test/run-manual-tests?azure-portal=true).

We recommend that you take advantage of Azure DevOps because it provides a
rich set of management features that are not only for testing but also for result
management and mitigation.

### Run automated test cases

The platform for finance and operations apps provides developers with
tools to write test cases based on task recordings and use Azure DevOps
to manage the automated running of these test cases.

Developers can use the build and test automation capabilities of build
and test environments. For more information, see [Continuous delivery home page](/en-us/dynamics365/fin-ops-core/dev-itpro/dev-tools/continuous-delivery-home-page/?azure-portal=true).

The Regression suite automation tool (RSAT) significantly reduces the time and cost of user acceptance testing (UAT). RSAT lets functional power users record business tasks by using Task recorder and then convert the recordings into a suite of automated tests, without having to write source code. RSAT is fully integrated with Microsoft Azure DevOps for test execution, reporting, and investigation. Test parameters are decoupled from test steps and stored in Microsoft Excel files.

Important

RSAT is marked for deprecation and isn't supported after May 15, 2027. Plan your long-term regression testing strategy accordingly. For more information, see [Removed or deprecated platform features](/en-us/dynamics365/fin-ops-core/fin-ops/get-started/removed-deprecated-features-platform-updates?azure-portal=true).

Download the tool and user manual from [finance and operations apps, Regression Suite Automation Tool](https://www.microsoft.com/download/details.aspx?id=57357).

#### Trial without Azure DevOps license

If your organization currently does not have a subscription to the Azure DevOps Test plan user license, there are still options for running a trial of the RSAT tool without the connection to Azure DevOps. This will allow you to gain insight and personally experience the test automation abilities of RSAT before fully committing to the subscription in Azure DevOps.

With the ability to run RSAT on a trial basis without a subscription to Azure DevOps, a user can manually upload the task recordings they have made into RSAT. Since this a trial, only the user who is uploading the task recordings will have the ability to run the test automations through the tool. Running the trial will enable the user to see the benefits of the tool for their organization before a commitment to an Azure DevOps subscription. For full access and to be able to run RSAT as normal along with the connection to Azure DevOps.

For information about purchasing a license, see [Pricing for Azure](https://azure.microsoft.com/pricing/details/devops/azure-devops-services).

To see how to create a test plan in Azure DevOps to use with RSAT, watch this video.

To see how to use RSAT, watch this video:

### RSAT supports parallel execution

One of the benefits that RSAT tool provides is that a user can run multiple instances of RSAT on the same environment. This saves both time and money since multiple environments are not required to run test scripts, but instead they can be parallelly executed. An example of this in practice may include one user running a fairly large number of test cases at the same time, instead of having to run them sequentially. Another user would also be able to work out of the same environment and run separate test cases, to maximize environment resources.

There's an option to configure how many concurrent instances the environment can process concurrently. The option can optimize use of environment resources.

This feature can also be used when executing tests from Azure DevOps pipelines, by running multiple pipelines scheduled to run at the same time. This way, multiple test runs can execute in parallel on one environment to help process all tests faster.

### Investigate test runs

When an automated run is complete, on the Azure DevOps toolbar, select **Test > Runs** (or **Test Plans > Runs**) to investigate your test run. Select the desired test run to investigate test case failures
and errors.

You can also go to your test suite in Azure DevOps to see the latest results that are associated with your test cases.

For more information on testing and test management in Azure DevOps, see [Azure DevOps documentation](/en-us/azure/devops/?azure-portal=true).