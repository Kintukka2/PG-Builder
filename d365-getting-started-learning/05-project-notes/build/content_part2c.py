from pgxml import *
from content_part2a import sub, topic, RESP, ENTITY, ACCESS, R

def part2c():
    o = []
    # ---------------- 9 Reports
    o += topic(9, 'GS_T9', 'Run a Report',
        ['Use this topic to run a D365 report: set its parameters and destination, view, download or print it, run it in the background when it is large, and find the output afterwards. '
         'Reports open from the **Inquiries and reports** menu of their module; each process guide names its reports in its Part 3.'],
        [f'{R}: runs the reports their role needs.'],
        ['A report is needed on screen, as a file, or in the background.'],
        overview=[('GS_T9_1', '9.1 Set the Report Parameters and Destination', 'Fill in the report dialog: parameters, records to include and destination.'),
                  ('GS_T9_2', '9.2 View, Download and Print a Report', 'Use the PDF viewer for a report sent to the screen.'),
                  ('GS_T9_3', '9.3 Run a Report in the Background', 'Optional. Send a large report to run in the background.'),
                  ('GS_T9_4', '9.4 Find Background Output', 'Find a background report in the Action center, My batch jobs and the Print archive.')])
    RESP['GS_T9_1'] = 'runs the reports their role needs.'
    o += sub('9.1', 'GS_T9_1', 'Set the Report Parameters and Destination',
        ['Use this procedure to fill in a report dialog. Most dialogs have the same sections: **Parameters** for the report’s options, **Records to include** to limit the records, **Destination** for where the report goes, and **Run in the background**.'],
        ['A user opens a report from a module’s Inquiries and reports menu.'],
        'Complete these steps to set the report parameters and destination:',
        ['Access to D365 and to the report.'],
        [ENTITY,
         ('*Navigate* to the report.', 'From the **Navigation Pane**, click **Modules**, select the module, then select the report under **Inquiries and reports**, using the path your process guide gives. The report dialog opens.',
          'GS-18: Confirm the report dialog sections and labels (Parameters, Records to include > Filter, Destination > Change, Run in the background) and the destinations available to users, in the clean-session test. Microsoft has no current end-user article for the report dialog; the labels come from an archived Microsoft blog.'),
         ('*Enter* the **Parameters**.', 'Enter the report options your process guide gives, such as dates or a customer range.'),
         ('*Click* **Filter**.', 'Optional. On the **Records to include** FastTab, click **Filter** to limit the records, for example to one account, then click **OK**.'),
         ('*Check* the **Destination**.', 'The **Destination** FastTab shows where the report goes. **Screen** is the default.'),
         ('*Click* **Change**.', 'Optional. To send the report elsewhere, click **Change**, select **File**, **Email**, **Printer** or **Print archive**, and click **OK**. See [[GS_KC_Reports|Report destinations]] in Part 1.'),
         ('*Click* **OK**.', 'Click **OK** to run the report.')],
        ('step', ['The report runs to the destination you chose.'], ('GS_T9_2', '9.2 View, Download and Print a Report')))
    RESP['GS_T9_2'] = 'views, downloads and prints the reports they run.'
    o += sub('9.2', 'GS_T9_2', 'View, Download and Print a Report',
        ['Use this procedure to work with a report sent to the screen. It opens in the PDF viewer, which shows the report as it will print. Links in a report work only while you preview it, not in a downloaded file.'],
        ['A report was run with the destination Screen.'],
        'Complete these steps to view, download and print a report:',
        ['The report was run to **Screen** (see [[GS_T9_1|9.1 Set the Report Parameters and Destination]]).'],
        [('*Review* the report.', 'Scroll through the report in the viewer, and use the page controls on its toolbar to move between pages.'),
         ('*Click* the download button.', 'Optional. On the viewer toolbar, click download to save the report as a PDF.'),
         ('*Click* **Print**.', 'Optional. Click **Print** on the viewer toolbar to print to your local printer.'),
         ('*Close* the viewer.', 'Close the viewer to return to D365.')],
        ('complete', ['The report has been reviewed, and downloaded or printed if needed.']),
        extra_after=[note('A report that runs too long while you wait can time out. Run large reports in the background (9.3) and split very large runs into smaller ranges.')])
    RESP['GS_T9_3'] = 'runs large reports in the background.'
    o += sub('9.3', 'GS_T9_3', 'Run a Report in the Background',
        ['Use this procedure to run a large report as a batch job, so you can keep working while it runs. A background report cannot go to **Screen** or **File**: send it to the **Print archive**, **Email** or a **Printer**. '
         'Skip this subtopic for reports that run quickly: continue to [[GS_T9_2|9.2 View, Download and Print a Report]].'],
        ['A report is large, or a process guide tells the user to run it in the background.'],
        'Complete these steps to run a report in the background:',
        ['The report dialog is open with its parameters set (see [[GS_T9_1|9.1 Set the Report Parameters and Destination]]).'],
        [('*Expand* **Run in the background**.', 'In the report dialog, expand the **Run in the background** FastTab.'),
         ('*Set* **Batch processing** to **Yes**.', 'Turn on **Batch processing**.'),
         ('*Enter* the **Task description**.', 'Enter a description you will recognize, for example the report name and date. You find the output by it later.'),
         ('*Select* the **Destination**.', 'On the **Destination** FastTab, click **Change** and select **Print archive**, then click **OK**.'),
         ('*Click* **Alerts**.', 'Optional. Click **Alerts** and select when to be told, for example when the job has **Ended** or has an **Error**.'),
         ('*Click* **OK**.', 'Click **OK**. The report is queued; it usually starts within a minute.')],
        ('step', ['The report is queued as a batch job.'], ('GS_T9_4', '9.4 Find Background Output')),
        extra_after=[note('Leave **Batch group** and the other background settings as they are unless your process guide gives a value.')])
    RESP['GS_T9_4'] = 'finds the output of their background reports.'
    o += sub('9.4', 'GS_T9_4', 'Find Background Output',
        ['Use this procedure to check a background report and open its output. The **Action center** tells you when it has finished, **My batch jobs** shows its status, and the **Print archive** holds the report.'],
        ['A report was run in the background.'],
        'Complete these steps to find background output:',
        ['A report was run in the background to the Print archive (see [[GS_T9_3|9.3 Run a Report in the Background]]).'],
        [('*Click* the **Action center**.', 'On the navigation bar, click the bell. A message shows when the job has finished.'),
         ('*Navigate* to the **My batch jobs** page.', ['If the job has not finished, from the **Navigation Pane**, *select*:', '> Modules >', '> Common >', '> Inquiries >', '> Batch jobs >', '> My batch jobs'],
          'GS-20: Confirm the paths of My batch jobs and the Print archive (Common > Inquiries) and the Print archive buttons (Print preview) in our environment. Microsoft has no current end-user article for either page.'),
         ('*Check* the job **Status**.', 'Find the job by its task description. **Waiting** or **Executing** means it is still running; **Ended** means it finished; **Error** means it failed: contact the BAU Support team.'),
         ('*Navigate* to the **Print archive** page.', ['From the **Navigation Pane**, *select*:', '> Modules >', '> Common >', '> Inquiries >', '> Print archive']),
         ('*Select* the report.', 'Select the report by its description.'),
         ('*Click* **Print preview**.', 'Click **Print preview** to open the report, then download or print it as in [[GS_T9_2|9.2 View, Download and Print a Report]].')],
        ('complete', ['The background report is open from the Print archive.']))
    # ---------------- 10 Attach
    o += topic(10, 'GS_T10', 'Attach a Document',
        ['Use this topic to attach a file, a note or a link to a record, such as a remittance to a payment journal or a supporting document to an invoice, and to open the attachments already there. '
         'The **Attach** button (paperclip) at the top right of a page shows how many attachments the record has.'],
        [f'{R}: attaches the supporting documents their process requires.'],
        ['A file, note or link must be kept with a record, as a process guide describes.'])
    o += [h5('Procedure'), lead('Complete these steps to attach a document:'),
          procedure(['The record is selected or open.', 'The file to attach, if attaching a file.'], R,
              [ENTITY,
               ('*Select* the record.', 'Select the record to attach to. On a page with a header and lines, click in the part (header or line) that the attachment belongs to.'),
               ('*Click* **Attach**.', 'Click **Attach** (the paperclip, top right), or press **Ctrl+Shift+A**. The **Attachments** page opens.'),
               ('*Click* **New**.', 'Click **New** and select the type: **File**, **Note** or **URL**.',
                '[Q05] GS-21: Confirm the attachment types users choose, the file types and maximum size allowed, where attachments are stored (Azure or SharePoint), and anything that must not be attached. These are admin settings.'),
               ('*Select* the file.', 'For a file, click **Browse**, select the file and open it. For a note or URL, enter it in **Notes**.'),
               ('*Enter* the **Description**.', 'Enter a description that says what the document is.'),
               ('*Confirm* the attachment is listed.', 'Check that the attachment is listed and its preview shows. Close the page: the **Attach** button now counts it.')],
              ('complete', ['The document is attached to the record and counted on the **Attach** button.'])),
          note('To open an attachment, click **Attach** on the record, select the attachment and review it in the **Preview** FastTab, or click **Open**. If the **Attach** button is missing, check **Enable document handling** in your user options (topic 1.2).')]
    # ---------------- 11 Workflow
    o += topic(11, 'GS_T11', 'Submit and Approve Workflow Items',
        ['Use this topic to send a document to workflow for approval, follow it, and act on the work items assigned to you. The **Workflow** button on the Action Pane shows the actions available to you at the current step; '
         'your process guide says which documents go through workflow and who approves them. See [[GS_KC_Workflow|Workflow]] in Part 1 for the terms.'],
        [f'{R}: submits their own documents and acts on the work items assigned to them.'],
        ['A document needs approval, or a work item is assigned to the user.'],
        overview=[('GS_T11_1', '11.1 Submit a Document to Workflow', 'Submit, follow and, if needed, recall your document.'),
                  ('GS_T11_2', '11.2 Act on a Work Item', 'Approve, reject, request a change or delegate a work item assigned to you.'),
                  ('GS_T11_3', '11.3 Delegate Your Work Items While Away', 'Optional. Send new work items to another user while you are away.')])
    RESP['GS_T11_1'] = 'submits their own documents to workflow.'
    o += sub('11.1', 'GS_T11_1', 'Submit a Document to Workflow',
        ['Use this procedure to submit a document, such as a journal, to its workflow. The comment you enter goes to the approver with the document. After submitting, follow the document in its workflow history; you can recall it to stop the workflow if you need to correct it.'],
        ['A document is ready for approval, as the process guide describes.'],
        'Complete these steps to submit a document to workflow:',
        ['The document is complete and saved.'],
        [ENTITY,
         ('*Open* the document.', 'Open the document to submit.'),
         ('*Click* **Workflow**.', 'On the Action Pane, click **Workflow**. The workflow message bar above the page shows the workflow’s instructions.',
          'GS-22: Confirm the Workflow button and its menu labels (Submit, View history, Recall, Approve, Reject, Request change, Delegate), the message bar and its instructions icon, and the Work items assigned to me path, in our environment. Microsoft documents them only from the setup side.'),
         ('*Click* **Submit**.', 'Click **Submit**.'),
         ('*Enter* the comment.', 'Enter a comment for the approver, then click **Submit**. The document’s approval status changes.'),
         ('*Click* **View history**.', 'Optional. Click **Workflow** > **View history** to see who the document is with and what has happened. To stop the workflow, click **Recall**, enter a comment and click **OK**.')],
        ('complete', ['The document is in workflow, waiting for approval.']))
    RESP['GS_T11_2'] = 'acts on the work items assigned to them.'
    o += sub('11.2', 'GS_T11_2', 'Act on a Work Item',
        ['Use this procedure to act on a work item assigned to you: approve, reject, request a change, or delegate it to another user. Work items show on the dashboard under **Work items assigned to me**. '
         'The actions offered depend on the workflow step.'],
        ['A work item is assigned to the user.'],
        'Complete these steps to act on a work item:',
        ['A work item is assigned to you.'],
        [('*Open* **Work items assigned to me**.', ['On the dashboard, find **Work items assigned to me**, or from the **Navigation Pane**, *select*:', '> Modules >', '> Common >', '> Work items >', '> Work items assigned to me']),
         ('*Click* the document link.', 'Click the document ID to open the document.'),
         ('*Review* the document.', 'Review the document, its attachments and the submitter’s comment. **Workflow** > **View history** shows its history.'),
         ('*Click* **Workflow**.', 'On the Action Pane, click **Workflow**.'),
         ('*Select* the action.', '**Approve** to approve; **Reject** to end the workflow; **Request change** to return it to the submitter; **Delegate** to give it to another user.'),
         ('*Enter* the comment.', 'Enter a comment, and for **Delegate** the user, then confirm. Your comment is kept in the workflow history.'),
         ('*Confirm* the work item is done.', 'Check that the item is no longer in **Work items assigned to me**.')],
        ('complete', ['The work item is completed and the document has moved on in its workflow.']))
    RESP['GS_T11_3'] = 'sets up delegation before planned absence.'
    o += sub('11.3', 'GS_T11_3', 'Delegate Your Work Items While Away',
        ['Use this procedure to send the work items assigned to you during an absence to another user automatically. The delegation applies to new work items in the period you set. Agree it with the person first.'],
        ['A user who receives work items will be away.'],
        'Complete these steps to delegate your work items while away:',
        ['The person you delegate to has agreed and has access to the documents.'],
        [('*Click* **Settings**.', 'On the navigation bar, click **Settings** (gear), then **User options**.'),
         ('*Click* the **Workflow** tab.', 'Click **Workflow** and expand **Delegation**.'),
         ('*Click* **Add**.', 'Click **Add**.'),
         ('*Select* the **Scope**.', 'Select **All** for every work item, or **Module** or **Workflow** for one kind, then select it in **Name**.'),
         ('*Select* the **Delegate**.', 'Select the user who acts for you.'),
         ('*Enter* the dates.', 'Enter the **Start date/time** and **End date/time** of your absence, and a **Comment**.'),
         ('*Select* **Enabled**.', 'Turn on **Enabled**, then click **Save**.')],
        ('complete', ['New work items assigned to you in the period go to your delegate.']),
        extra_after=[action_note('Company rules for delegation to be confirmed.', comment='[Q06] GS-27: Confirm whether users may set up delegation for every workflow, and whether their manager must agree it first. Microsoft documents the steps only.')])
    # ---------------- 12 Alert
    o += topic(12, 'GS_T12', 'Set Up an Alert',
        ['Use this topic to be told when a record changes or a date falls due, for example when a vendor’s bank account changes or an invoice is due. Alerts appear in the **Action center** and can also be emailed. '
         'They are created by a background job, so an alert can arrive some minutes after the change.'],
        [f'{R}: sets up alerts for the records they monitor.'],
        ['A user needs to know when a record changes or a date is due.'])
    o += [h5('Procedure'), lead('Complete these steps to set up an alert:'),
          procedure(['The page with the record is open.'], R,
              [ENTITY,
               ('*Select* the record and field.', 'Select the record, and click in the field the alert is about, for example **Due date**.'),
               ('*Click* the **Options** tab.', 'On the Action Pane, click **Options**.'),
               ('*Click* **Create alert rule**.', 'In the **Share** group, click **Create alert rule**. The **Create alert rule** dialog opens.',
                '[Q07] GS-23: Confirm the alert button label (Microsoft gives Create alert rule and Create a custom alert), that the alert batch jobs run in our environment and how often, and whether alert emails are sent.'),
               ('*Select* the event.', 'Under **Alert me when**, select the **Field** and the **Event**, for example **has changed** or **is due in**.'),
               ('*Select* the records.', 'Under **Alert me for**, select **Current selected record** or **All records** in the current view. Filter the page first to narrow **All records**.'),
               ('*Enter* the end date.', 'Under **Alert me until**, choose an end date or no end.'),
               ('*Enter* the **Subject**.', 'Under **Alert me with**, enter a **Subject** and **Message**. Turn on **Send email** to receive it by email too.'),
               ('*Click* **OK**.', 'Click **OK** to create the rule.')],
              ('complete', ['The alert rule is active; its alerts arrive in the **Action center**.'])),
          note('To change or delete your alerts, select **Options** > **Alert me** to open **Manage alert rules**.')]
    # ---------------- 13 Help
    o += topic(13, 'GS_T13', 'Get Help and Report a Problem',
        ['Use this topic to understand the messages D365 shows, find help for the page you are on, raise a problem with the BAU Support team, and reset your own settings when a page behaves oddly.'],
        [f'{R}: reads system messages, uses the help available and reports problems.'],
        ['A message appears, a user needs help with a page, or something does not work.'],
        overview=[('GS_T13_1', '13.1 Read System Messages', 'Read the message bar, message details and the Action center.'),
                  ('GS_T13_2', '13.2 Use the Help Pane', 'Open help for the current page.'),
                  ('GS_T13_3', '13.3 Raise a Problem with the BAU Support Team', 'Report a problem or an access issue, with the details support needs.'),
                  ('GS_T13_4', '13.4 Reset Your Usage Data', 'Optional. Clear your saved usage data and personalizations.')])
    RESP['GS_T13_1'] = 'reads and acts on the messages D365 shows.'
    o += sub('13.1', 'GS_T13_1', 'Read System Messages',
        ['Use this procedure to read the messages D365 shows: messages about the current page in the message bar, and messages from background work in the Action center. See [[GS_KC_Messages|System messages]] in Part 1.'],
        ['A message appears in the message bar, or the Action center bell shows new messages.'],
        'Complete these steps to read system messages:',
        [ACCESS],
        [('*Read* the message bar.', 'Read the message below the Action Pane. It names the field or record to fix.'),
         ('*Click* **Message details**.', 'Optional. If the message summarizes several messages, click **Message details** to see each one.'),
         ('*Fix* the cause.', 'Correct the value or the step the message names, then repeat the action.'),
         ('*Click* the **Action center**.', 'On the navigation bar, click the bell, or press **Ctrl+Shift+F7** (**Open message center**), to read messages from reports, batch jobs and alerts.'),
         ('*Copy* the message text.', 'If you cannot fix the cause, copy the full message text for the BAU Support team (13.3).')],
        ('complete', ['The message is understood and acted on, or ready to report.']))
    RESP['GS_T13_2'] = 'uses the Help pane for the page they are on.'
    o += sub('13.2', 'GS_T13_2', 'Use the Help Pane',
        ['Use this procedure to open help for the page you are on. The Help pane lists Microsoft articles for the current page; an article opens in a new browser tab. '
         'Hover over a field to see its description. Microsoft’s help describes standard D365: your process guide is the reference for how WiseTech Global uses it.'],
        ['A user needs to understand a page or field.'],
        'Complete these steps to use the Help pane:',
        [ACCESS],
        [('*Click* **Help & Support**.', 'On the navigation bar, click **Help & Support** (?).',
          'GS-24: Confirm the items on the Help & Support (?) menu in our build, the Help pane shortcut (Ctrl+Shift+? or Ctrl+?), and whether the Task guides tab is set up. Microsoft\'s own task guides stop at the December 2017 release.'),
         ('*Click* **Help**.', 'Click **Help**. The Help pane opens with articles for the current page.'),
         ('*Search* the help.', 'Optional. If no article fits, type keywords in the search box.'),
         ('*Select* an article.', 'Select an article. It opens in a new browser tab.')],
        ('complete', ['The help article for the page is open.']),
        extra_after=[important('If a task guide is offered in the Help pane, the data you enter while it plays is real. Do not play task guides in the live environment.')])
    RESP['GS_T13_3'] = 'reports problems and access issues to the BAU Support team.'
    o += sub('13.3', 'GS_T13_3', 'Raise a Problem with the BAU Support Team',
        ['Use this procedure to report a D365 problem, or a missing page, module, legal entity or button, to the BAU Support team. Do not use the **Support** option on the D365 Help menu: it goes to Microsoft’s support, not WiseTech Global’s. '
         'Give the details below so the team can find the problem quickly.'],
        ['Something in D365 does not work, a message cannot be resolved, or access is missing.'],
        'Complete these steps to raise a problem with the BAU Support team:',
        [ACCESS],
        [('*Note* the legal entity and page.', 'Note the legal entity (top-right), the page name and its URL from the address bar.'),
         ('*Note* the steps.', 'Note what you did, step by step, and what you expected to happen.'),
         ('*Copy* the message.', 'Copy the full text of any message, with its **Message details** (see [[GS_T13_1|13.1 Read System Messages]]).'),
         ('*Take* a screenshot.', 'Take a screenshot that shows the page and the message.'),
         ('*Raise* the issue.', 'Raise the issue with the BAU Support team through the D365 issue form in **Additional Resources**, with the details from steps 1 to 4. {{Confirm the route: the D365 issue form, the Atlas D365 User Support Hub or AVA.}}',
          '[Q08] GS-25: Confirm how users raise a D365 problem with the BAU Support team (the D365 issue form in Additional Resources, the Atlas D365 User Support Hub, or AVA), and the details the team needs (for example legal entity, URL, message, screenshot, time).')],
        ('complete', ['The problem is reported to the BAU Support team with the details they need.']))
    RESP['GS_T13_4'] = 'resets their own usage data when advised.'
    o += sub('13.4', 'GS_T13_4', 'Reset Your Usage Data',
        ['Use this procedure to see and delete the data D365 keeps about how you use it, such as saved personalizations, and to show again the feature pop-ups you dismissed. '
         'Use it when the BAU Support team advises it. Deleted personalizations cannot be restored.'],
        ['The BAU Support team advises resetting usage data, or a user wants to remove old personalizations.'],
        'Complete these steps to reset your usage data:',
        [ACCESS],
        [('*Click* **Settings**.', 'On the navigation bar, click **Settings** (gear), then **User options**.'),
         ('*Click* **Usage data**.', 'On the Action Pane, click **Usage data**.',
          'GS-26: Confirm the Usage data page, its tabs (Personalization) and the delete and reset buttons in our environment.'),
         ('*Click* the **Personalization** tab.', 'Click **Personalization** to see your saved personalizations.'),
         ('*Select* the data to delete.', 'Select the rows to remove, or use the option to reset feature callouts.'),
         ('*Click* **Delete**.', 'Click **Delete** and confirm.')],
        ('complete', ['The selected usage data is deleted.']))
    return o

def part3():
    o = [heading(2, 'Part 3: Reports (Getting Started)', 'GS_Part3', numbered=False, pagebreak=True), blank(), h5('Overview'),
         body('These inquiry pages support the tasks in this guide: they show the output of your background reports and the progress of the documents you submit to workflow. '
              'The reports for each process are in that process guide’s Part 3.'), bodyblank()]
    o += [h5('My batch jobs'), report_table(['Common', 'Inquiries', 'Batch jobs', 'My batch jobs'],
          ['Shows the batch jobs you created, such as reports run in the background, with their status: Waiting, Executing, Ended or Error. Use it after [[GS_T9_3|9.3 Run a Report in the Background]] to check that your job finished, and contact the BAU Support team if it shows **Error**.']), blank()]
    o += [h5('Print archive'), report_table(['Common', 'Inquiries', 'Print archive'],
          ['Holds the reports sent to the **Print archive**, including those run in the background. Find a report by its description and select **Print preview** to open, download or print it ([[GS_T9_4|9.4 Find Background Output]]).']), blank()]
    o += [h5('Workflow history'), report_table(['Common', 'Inquiries', 'Workflow', 'Workflow history'],
          ['Shows each document submitted to workflow: its status, who it is with, and every action and comment. Use it to follow a document you submitted ([[GS_T11_1|11.1 Submit a Document to Workflow]]), or open it from the document with **Workflow** > **View history**.']), blank()]
    o += [h5('Work items assigned to me'), report_table(['Common', 'Work items', 'Work items assigned to me'],
          ['Lists the workflow tasks and approvals waiting for you, with links to each document. The same list is on the dashboard. Check it daily if you approve documents ([[GS_T11_2|11.2 Act on a Work Item]]).']), blank()]
    return o
