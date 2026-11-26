<!-- https://learn.microsoft.com/en-us/training/modules/setup-batch-jobs-finance-operations/6-exercise -->
<!-- refetched: original harvest URL returned 404 -->
# Exercise - Work with batch jobs and set up alerts

Completed

* 25 minutes

## Scenario

You have been asked to work with some batch jobs and alerts. To do this, you must perform the following tasks:

1. Create a batch job
2. Create a recurrence
3. Add alerts
4. Copy a batch job
5. Enable the batch job
6. Assign the **Batch job manager** role to a user

## Create a batch job

1. Go to **System administration > Inquiries > Batch jobs**.
2. Select **New**.
3. In the **Job description** field, enter a value, such as **Data cache refresh batch**.
4. In the **Scheduled start date/time** field, enter a date and time.
5. Select **Save**.

## Create a recurrence

1. On the **Action Pane**, select **Recurrence** and use the options to enter a range and pattern for the recurrence.
2. Select **OK**.

## Add alerts

1. On the **Action Pane**, select **Alerts**.
2. Indicate if you want alert messages sent when the batch job ends, has an error, or is canceled. Then specify if you want the alerts to be displayed as pop-up messages.
3. Select **OK**.

## Copy a batch job

1. Select **System administration** > **Inquiries** > **Batch jobs**.
2. Select the job that you want to copy, and on the **Action Pane**, select **Copy batch job**.
3. Enter or add any changes. If you set **View tasks for the new batch job** to **Yes**, when you select **OK** you will go directly to the **Batch tasks** page for the copied job. The copied batch job will be created with a **Withhold** status. The **Run by** user can also be set to give this user the privilege to run the job without being a system administrator.
4. Close the page.

## Enable the batch job

1. On the **Batch jobs** page, on the Action Pane, select **Change status**.
2. Select the **Waiting** status, and then select **OK**.

## Assign the Batch job manager role to a user

1. Select **System administration** > **Security** > **Assign users to roles**.
2. Select **Batch Job Manager**, and on the right pane, notice how there is a user assigned to the role.
3. Close the page.