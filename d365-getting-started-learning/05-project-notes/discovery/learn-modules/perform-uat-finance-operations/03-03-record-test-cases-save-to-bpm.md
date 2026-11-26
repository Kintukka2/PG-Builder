<!-- https://learn.microsoft.com/en-us/training/modules/perform-uat-finance-operations/03-record-test-cases-bpm -->
<!-- refetched: original harvest URL returned 404 -->
# Record test cases and save to the business process modeler (BPM)

Completed

* 30 minutes

After you have created a BPM library, you'll need to use the task
recorder to create your test cases and then upload the cases to BPM.
There are several ways to do this.

If you're using a BPM library that already has all the necessary task
recordings (test cases) attached, you can skip this step. Otherwise,
follow the subsequent instructions to create new task recordings.

To enable the effective running of your tests by using automation tools,
make sure that all your task recordings start on the main dashboard of
finance and operations apps.

For end-to-end processes that are performed by more than one user, we
recommend that you divide your task recordings into user-specific tasks.
This simplifies the maintenance of test cases and allows you to run
test cases in the context of security roles, which is a best practice.

Watch this video for a demonstration of how to use the task recorder to create a test case for the Regression suite automation tool (RSAT).

### Create and save a new task recording

Note

Starting in January 2026, you can only create, edit, or use task recordings in sandbox and production environments. Cloud-hosted environments no longer have this capability. For more information, see [Task recorder resources](/en-us/dynamics365/fin-ops-core/dev-itpro/user-interface/task-recorder?azure-portal=true).

1. Go to **Settings > Task recorder**.

   ![Screenshot of the Task recorder option in the settings menu.](media/03-task-recorder.png)
2. Select **Create recording**.

   ![Screenshot of the Create recording in the task recorder menu.](media/03-create-new-recording.png)
3. Enter a name for the recording and then select **Start**.

   ![Screenshot of the Start page with name and description fields.](media/03-start-1.png)
4. When the recording is complete, in the Task recorder pane, select
   **Stop**.
5. To save the task recording to an attached BPM, select **Save to Lifecycle Services**.

   ![Screenshot of the Save to Lifecycle Services feature.](media/03-lcs-1.png)
6. Select the library that you want to save the recording to and then select **OK**. This automatically saves the recording into Lifecycle Services. If you already have a business library, then identify that in **System administration > Setup > System Parameters > Help** tab.
7. If you also want to save the recording on your computer, select **Save to this PC**. The extension of the recording file is AXTR.

### Upload an AXTR file to BPM

If you have saved your recordings (AXTR files) to your PC, follow these
steps to upload them to BPM.

1. In Lifecycle Services, in your project, on the **Business process libraries** page, select the library to upload the task recording to.
2. In the right pane, select **Upload**.
3. Select **Browse** to find and select the file to upload, and then select **Upload**.

### Download a task recording

You can download a task recording (AXTR file) that has been uploaded to a BPM process.

1. In Lifecycle Services, in your project, on the **Business process libraries** page, select the library to download the task recording.
2. Select a process that has task recording uploaded.
3. On the **Overview** pane, select **Download** to save the task recording (AXTR).

### Save an existing task recording to BPM

1. To attach an existing task recording, sign in to the client.
2. Go to **Settings > Task recorder**.
3. Select **Edit Recording** and attach the file by either saving directly to Lifecycle Services or downloading the AXTR and then uploading to BPM.

   ![Screenshot of the Edit recording feature.](media/03-edit-recording.png)

### Guidelines for recording test cases

Follow these guidelines when writing and recording your test cases,
especially if you are planning to automate a test run. The process
and tools that are described in this article apply to business process acceptance
tests; they are not meant to replace component and unit testing that is
typically owned by developers.

* Write a limited number of test cases that, when combined, cover complete end-to-end processes.
* Focus on business processes that have been customized.
* An individual test case (recording) should cover one or two business tasks only, typically run by one person. This simplifies task recording maintenance. Do not combine a complete end-to-end business process, such as procure-to-pay or order-to-cash, into one large task recording.

  + For example, instead of having **RFQ > Purchase Order > Product Receipt > Vendor Invoice > Vendor Payment** as one test case, divide the process into three or four test cases. You will have the opportunity to combine these tests into an ordered test suite later.
* A test case should have at least one validation. Try to validate critical fields that cover the impact of other fields.

  + For example, validation of totals on sales or purchase orders cover the unit price/quantity/discount/tax.
* Avoid printing a report in a test case. If a test case needs to print a report, it should be selected on screen.
* 80+ percent of test cases should be of transactions or source documents. Master data should be limited to up to 20 percent of test cases only.

## Regression suite automation (RSAT) tool

Important

The Regression suite automation tool (RSAT) is marked for deprecation and isn't supported after May 15, 2027. For more information, see [Removed or deprecated platform features](/en-us/dynamics365/fin-ops-core/fin-ops/get-started/removed-deprecated-features-platform-updates?azure-portal=true).

To learn more about how to set up and use the Regression suite automation (RSAT) tool, visit [Regression suite automation tool (RSAT)](/en-us/dynamics365/fin-ops-core/dev-itpro/perf-test/rsat/rsat-overview/?azure-portal=true).