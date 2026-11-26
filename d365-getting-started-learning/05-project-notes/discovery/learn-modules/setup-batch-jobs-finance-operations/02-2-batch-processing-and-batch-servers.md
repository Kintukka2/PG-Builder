<!-- https://learn.microsoft.com/en-us/training/modules/setup-batch-jobs-finance-operations/2-batch-process-batch-servers -->
<!-- refetched: original harvest URL returned 404 -->
# Batch processing and batch servers

Completed

* 8 minutes

The batch framework provides an asynchronous, server-based batch processing environment that can process tasks across multiple instances of the Application Object Server (AOS). The AOS is the interface between the client application, such as a browser, and the finance and operations apps database.

In addition to the ability to create batch jobs with alerts and recurrences, you can also use server-based batch processing to process tasks across multiple instances of the AOS. There are several advantages to using server-based batch processing. You can add complex dependencies between batch tasks or among tasks. You can also run tasks in either serial or parallel steps depending on the needs of the business. It is important to remember that if a task has no dependencies, it is considered a parallel task.

The following graphic is an example of a job that has several tasks and task dependencies. In this scenario, there are seven tasks that are part of a job. The graphic shows how tasks are completed depending on the outcome of the dependent tasks:

![Diagram of an example of a job showing the seven tasks and task dependencies.](media/02-job-tasks.png)

Let’s get familiar with the following aspects of the batch framework:

* A **batch job** consists of one or more batch tasks.
* A **batch task** is an activity that is run by a batch job. You can add batch tasks that have multiple types of dependencies to a batch job. You can also configure AOS instances to run multiple threads, each of which runs a task. All batch tasks that are waiting to be run can be performed by any available AOS instance that is configured as a batch server. To improve throughput and reduce overall execution time, you can define a batch job as many tasks and then use a batch server to run the tasks against all available AOS instances.
* A **batch group** is an attribute of a batch task. A batch group lets the administrator determine or specify which AOS instance runs the task. When you create a new task, it's put in the default batch group. All batch servers are configured to process the default batch group and the waiting tasks from any job.

## Batch server topology planning

The capacity of a batch server is based on the maximum number of threads that can run concurrently on the AOS instance. Each thread runs one batch task. You can add complex dependencies between or among tasks. You can run these tasks in serial steps or parallel steps, depending on the business logic and requirements. All tasks that don't have any dependencies are considered parallel tasks. AOS instances that are configured as batch servers periodically check for tasks that are waiting to be processed. The batch server assigns each parallel task to a thread and starts to process the thread.

You can run multiple threads across multiple AOS instances. Each AOS instance automatically runs multiple threads, depending on that capacity that is defined in the configuration settings. Therefore, parallel tasks from a job can be run on multiple threads across multiple AOS instances.

A batch server checks for available threads one time per minute. Therefore, you might have to wait for a minute before you see that a waiting task is picked up for processing by an available thread.

## Batch server management planning

All batch servers can be managed from a single location. One typical use of batch servers is to load balance jobs across multiple servers. You can set the number of threads that the batch server will process.

Because batch servers are also active AOS instances that service requests from finance and operations apps clients and other associated components, you must carefully determine when an AOS instance should be available to process batches.

## Priority-based batch scheduling

You can eliminate the process of assigning batch jobs to batch servers by enabling the **Batch priority-based scheduling** feature in the **Feature management** workspace. Priority-based batch scheduling allows you to define priorities for batch groups by separating batch groups from the batch server. Relative scheduling priorities determined by business requirements are used to determine the sequence that tasks are run. To declare relative priorities and to determine the processing order of jobs and business processes, you can use the scheduling priority classifications.

The available values for scheduling priority are:

* Low
* Normal
* High
* Critical
* Reserved capacity

When the feature is enabled, **Normal** is the default value and is applied to all existing batch groups. Reserved capacity represents the highest priority. To set the batch reserved capacity level, navigate to **System administration** > **Setup** > **System parameters** and select the **Batch global settings** tab.
By enabling Priority-based batch scheduling, priorities are introduced up to the batch job level, batch jobs are not tied to a specific server, and it is a prerequisite for near-zero downtime servicing.