<!-- https://learn.microsoft.com/en-us/training/modules/setup-batch-jobs-finance-operations/1-introduction -->
<!-- refetched: original harvest URL returned 404 -->
# Overview of batch processing

Completed

* 8 minutes

If you want to run tasks such as printing reports, performing maintenance, sending electronic documents, or additional scheduled tasks, then a batch job is a good approach. By using batch jobs, you can reduce performance impacts on your computer or server during standard working hours.

Batch jobs can run either sequentially or concurrently all while spreading the workload across the server(s). You can create dependencies between tasks as well. This will allow you to sequence tasks based on the succession or failure of the previous task.

An additional feature is recurrence patterns for the batch jobs. This will allow you to schedule the same job to run periodically such as a common maintenance job or processing invoices. To monitor these batch jobs you can set up alerts. These are sent when the batch job succeeds, fails, or finishes. After this batch job is processed, you can view the history, which includes logs and details that were encountered while the job was running.

## Scenarios

There are numerous reasons why your organization would want to implement batch processing. Here are some examples:

* By using recurrence patterns for batch jobs, Contoso Electronics wants to set a recurrence for all their invoices to process automatically on the last day of every month. Recurrences can be set up to run by the minute, hour, day, week, month, or year.
* Contoso Retail USA updates their discount offering daily, to automate the Retail distribution schedule jobs. They set up a batch job to run every day at 12 AM Eastern Standard Time. This allows all the point of sale stations to have the updated discounts every day.
* The IT team at Contoso Electronics wants to be notified when their monthly invoice batch job runs. They want notifications when the job runs, fails, or succeeds, so they use alerts to receive these notifications.
* The Contoso Electronics controllers want to receive the balance sheet financial report on a weekly basis. They can use batch jobs and set up a recurrence to specify which day of the week they want the report to run and be sent to them.

## Batch groups

Use batch groups to categorize batch tasks and run them on specific servers. The servers in your environment might have different software installed, or they might be available at different times of the day. Batch groups are used to direct batch tasks to the most appropriate server. Tasks in the same batch job can belong to different batch groups.

For example, server A is set up to print reports, and server B is set up to send electronic documents. You can use batch groups to make sure that reporting tasks are run on server A and electronic documents are processed by server B.

Administrators and batch managers can perform common tasks including creating and copying batch jobs, changing a batch job user, and specifying a time interval in which a job should not execute.

## Active batch periods

Administrators can provide information for an additional active period, such as in the following scenarios:

* Specifying time ranges during which jobs within a batch group can start execution.
* Selecting to run batch jobs outside of office hours only.
* Setting the recurrence for anytime within the active period. For example, your administrator might select to run the batch jobs every hour, but only between the hours of 6:00 PM and 8:00 AM.