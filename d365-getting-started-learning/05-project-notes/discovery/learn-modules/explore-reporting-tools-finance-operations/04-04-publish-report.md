<!-- https://learn.microsoft.com/en-us/training/modules/explore-reporting-tools-finance-operations/04-publish-report -->
# Publish a report

Completed

* 10 minutes

After you create an SSRS report, deploy it before it can be accessed in finance and operations apps.

You can deploy reports by using PowerShell or Visual Studio. PowerShell deployment is useful in environments where Visual Studio isn't available. Don't use this approach in a production environment.

PowerShell can deploy all reports or a single report.

To deploy all reports, open PowerShell as an administrator and run the following command:

```
C:\AosService\PackagesLocalDirectory\Plugins\AxReportVmRoleStartupTask\DeployAllReportsToSsrs.ps1 -PackageInstallLocation "C:\AosService\PackagesLocalDirectory"
```

The drive letter varies by environment. Common values include C:, L:, and K:.

To deploy a specific report, identify the report name first. Then open PowerShell as an administrator and run the following command:

```
C:\AosService\PackagesLocalDirectory\Plugins\AxReportVmRoleStartupTask\DeployAllReportsToSsrs.ps1 -Module ApplicationSuite -ReportName TaxVatRegister.Report
```

To deploy a report from Visual Studio, add the report to your project. Then right-click the report and select **Deploy**.

[![Screenshot of the Visual Studio Solution Explorer page showing the Deploy Reports option.](media/04-deploy-report.png)](media/deploy-report.png#lightbox)