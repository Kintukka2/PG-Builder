<!-- https://learn.microsoft.com/en-us/training/modules/create-use-workflows-finance-operations/6-exercise -->
<!-- refetched: original harvest URL returned 404 -->
# Exercise - Create a purchase requisition workflow

Completed

* 20 minutes

## Scenario

The finance and operations module that you're working in determines the types of workflow that you can create.
In this lab, you will create a purchase requisition workflow. Before a purchase requisition can be submitted for review, you need to configure the workflow.

## Create and set up workflows

1. In the company **USMF**, go to **Procurement and sourcing > Setup > Procurement and sourcing workflows**.
2. On the list page that appears, on the Action Pane, select **New**.
3. On the **Create workflow** page, select the **Purchase requisition line review**.
4. For the first time, the browser will show a dialog box to open the **Microsoft.Dynamics.AX.Framework.WorkflowEditorHost** page. Select **Open**.
5. In the **Do you want to run this application?** dialog box, select **Run**. It takes a few minutes for the workflow editor to be downloaded. When it has finished the download, it automatically opens the **Sign in** dialog box in the background.
6. Enter your credentials and password (found in the **Resources** tab on the lab side bar, in the **Azure portal** section)
7. Select **OK** to stay signed in to all apps, and select **Done**.
8. The workflow editor appears (this can take a couple of minutes and may open behind the browser window).

## Drag workflow elements onto the canvas

The **Workflow elements** area of the workflow editor contains the elements that you can add to your workflow.

1. To add elements to the workflow, drag **Review purchase requisition lines** and **Approve purchase requisition lines** onto the canvas.
2. Connect **Start** to **Review purchase requisition lines**. To connect one workflow element to another, hold the pointer over an element until connection points appear (small boxes around the edges of the elements). Select a connection point and drag it to another element. Be sure to connect all the elements.
3. Connect **Review purchase requisition lines** to **Approve purchase requisition lines**.
4. Connect **Approve purchase requisition lines** to **End**, at the bottom of the page.

## Configure workflow properties

1. In the workflow editor canvas, select **Review purchase requisition lines** and, from the Action Pane, select **Properties** to open the **Properties** page.
2. Enter a value in the **Name** field or accept the default.
3. Enter a value in the **Work item subject** field, for example **Work item test**. Alternatively, you can also include a place holder and concatenate the text with the place holder.
4. Enter a value in the **Work item instructions** field, for example "Review this purchase requisition".
5. Select **Assignment** on the left section.
6. In the **Assignment type** tab select **User**.
7. Select the **User** tab, and select a user, for example **ALICIA**, and add it to the **Selected users** section by using the arrow.
8. Select **Close**. The workflow editor may hide behind the browser window, if so – then just select it from the Windows task bar to open it.
9. On the pane at the bottom of the page, you will have three errors or warnings. Select each one.

   * Double-click the next error, **Selected assignment type “None” is not supported**. On the screen that opens, select **User**. On the **User** tab, select **Admin** or any other user, and move it over to the **Selected users** and select **Close**The error will then disappear and you can close the screen from the first step.
   * The next message is **You must enter a message text for language en-us**. Double-click the message and then enter a text (for example, Test message 1) in the **Work item subject** and **Work item instructions** fields, and select **Close**. This removes all error messages and your workflow is now complete.
10. Select **Save and close** in the workflow editor.
11. Specify version notes, for example **New workflow**.
12. Select **OK**.
13. Select **Activate the new version**.
14. Select **OK**. It might take a few minutes for the workflow editor to finish its activation process, and then it will close automatically.
15. Select **Close** in the **Create workflow** page.
16. Refresh the **Procurement and sourcing workflows** page in finance and operations if you don't see your new workflow. You'll see a new **Purchase requisition line review** at the end of the list.