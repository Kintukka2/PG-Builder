<!-- https://learn.microsoft.com/en-us/training/modules/setup-batch-jobs-finance-operations/5-batch-manager-role -->
# Batch job manager role

Completed

* 4 minutes

By assigning a user to the **Batch job manager** security role, the user has permissions to copy batch jobs, change who will execute jobs, and specify the time ranges during which jobs can execute. The batch Maintain batch jobs security privilege is part of the Batch job manager security role and it allows a user to create an unplanned batch job and grant privileges to other users.

To just be able to manage batch jobs, a user should be assigned to the **Batch job manager** role, and not to the System admin or IT admin security.

## Run by feature

The **Run by** feature allows Batch job managers to specify a user to run the batch job. For example, when you want to change the user who is currently assigned to run the job, or if you want to quickly set a user while copying the batch jobs from one company to another. You can also use this functionality to copy batch jobs.

Below you can see the **Run by** option found on **System administration > Inquires > Batch jobs**.

[![Screenshot of the Batch jobs page with the Run by field highlighted.](media/05-run-by-user.svg)](media/run-by-user.svg#lightbox)