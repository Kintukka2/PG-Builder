from pgxml import *

R = 'D365 End-user'
TOPICS = [  # n, anchor, title, when, where
    (1, 'GS_T1', 'Set Up Your D365 Session', 'When a user starts using D365, and when their settings need to change', 'D365'),
    (2, 'GS_T2', 'Open a Page', 'Whenever a page or workspace is needed for a task', 'D365'),
    (3, 'GS_T3', 'Switch Legal Entity', 'When work is needed in a legal entity other than the active one', 'D365'),
    (4, 'GS_T4', 'Work with Records', 'When a record needs to be viewed, created, changed or deleted', 'D365'),
    (5, 'GS_T5', 'Find Records with Filters', 'When a list shows more records than the task needs', 'D365'),
    (6, 'GS_T6', 'Create a Personalized View', 'When a page does not show the information needed in the way it is needed', 'D365'),
    (7, 'GS_T7', 'Manage Saved Views and Personalizations', 'When a saved view or a page layout needs to change, or be reset', 'D365'),
    (8, 'GS_T8', 'Export Data and Work in Excel', 'When page data is needed in Excel', 'D365; Excel'),
    (9, 'GS_T9', 'Run a Report', 'When a report is needed on screen, as a file or in the background', 'D365'),
    (10, 'GS_T10', 'Attach a Document', 'When a file, note or link must be kept with a record', 'D365'),
    (11, 'GS_T11', 'Submit and Approve Workflow Items', 'When a document needs approval, or a work item is assigned to the user', 'D365'),
    (12, 'GS_T12', 'Set Up an Alert', 'When the user needs to know that a record has changed or a date is due', 'D365'),
    (13, 'GS_T13', 'Get Help and Report a Problem', 'When a message appears, help is needed, or something does not work', 'D365'),
]

def part1():
    o = []
    o.append(heading(2, 'Part 1: What do I need to know? (Getting Started)', 'GS_Part1', numbered=False, pagebreak=False))
    o.append(blank())
    o.append(heading(4, 'High-level process', 'GS_P1_HLP', numbered=False, pagebreak=False))
    o += [blank(), h5('Part Description'),
          body('This guide covers the D365 skills that every D365 user needs before starting process work, whatever their stream: '
               'finding their way around the screen, opening pages, switching legal entity, working with records, filtering lists, '
               'saving personalized views, exporting to Excel, running reports, attaching documents, taking part in workflow approvals, '
               'setting up alerts and getting help. These tasks are not steps in a business process. Each process guide links to them '
               'and lists its own pages, workspaces, columns and views.'),
          body('The steps come from Microsoft’s documentation and training for finance and operations apps (Microsoft Learn), '
               'checked against WiseTech Global’s D365 environment. Screen labels can differ slightly from one D365 release to the next.',
               comment='GS-02: Every procedure in this v0.1 is written from Microsoft Learn and the D365 documentation (discovery, 26 November 2026). '
                       'The clean-session test in our D365 environment confirms the labels, paths and results, and gives the screenshots. '
                       'The points to check are in the register, section 3.'),
          body('The finance concepts that finance users need next (financial dimensions, journals, vouchers, posting periods and finding posted '
               'transactions) are in the D365 Finance Basics guide. {{Link to D365 Finance Basics when it is published.}}',
               comment='GS-03: D365 Finance Basics (ADO 15455) is not published yet, so this reference has no Training Hub link (D-096). '
                       'Add the link when it is published.'),
          body('This guide does not cover Copilot or the other AI features in D365.'),
          bodyblank(), h5('Initiation'),
          bullet('A new user is setting up D365 before starting routine process work.'),
          bullet('A user needs a general D365 skill that their process guide refers to.'),
          bodyblank(), h5('Stream'),
          stream_table('All streams', 'D365 F&O Getting Started, for Order to Cash (O2C), Procure to Pay (P2P), Record to Report (R2R) and Tax', [R]),
          blank(), h5('Process'), body('The high-level process is as follows:'),
          process_table([(n, a, t, R, w, wh) for n, a, t, w, wh in TOPICS]),
          note('The topics can be read in any order. A new user should read topics 1 to 5 first: they are used in every other topic and in every process guide.'),
          blank()]
    o.append(heading(4, 'Roles and responsibilities', 'GS_P1_Roles', numbered=False, pagebreak=False))
    o += [blank(), h5('Overview'),
          body('Every D365 user completes these tasks in their own D365 session. In workflow, the same user can be the person who submits a document '
               'or the person a work item is assigned to; topic 11 covers both.'),
          roles_matrix([R], [(a, f'{n}. {t}', [True]) for n, a, t, w, wh in TOPICS]),
          p('*R = Responsible', 'Tableinfo'), blank()]
    o.append(heading(4, 'Key concepts', 'GS_P1_KC', numbered=False, pagebreak=False))
    o += [blank(), h5('Overview'),
          body('Before you start, you need to know the parts of the D365 screen, how legal entities work, what the system messages mean, '
               'how filters and views behave, and the difference between the ways of getting data out of D365. Each concept below supports one or more topics in Part 2.'),
          bodyblank()]
    # --- parts of the screen
    o += [h5('The parts of the screen'),
          body('Every procedure in this guide and in the process guides uses these names. Learn them first.'),
          concept_table(['Element', 'Where it is', 'What it is for'], [
              ['Navigation bar', 'The bar across the top of the screen', 'Holds the legal entity selector (it shows the active ledger code, for example **100A**), **Search for a page** (magnifying glass), the **Action center** (bell), **Settings** (gear), **Help & Support** (?) and your initials.'],
              ['Navigation Pane', 'The pane on the left', 'Opens any page: **Home**, **Favorites**, **Recent**, **Workspaces** and **Modules**.'],
              ['Dashboard', 'The first page after you sign in', 'Shows a calendar, your **Work items assigned to me**, and tiles for apps and workspaces. Return to it from the **Home** button in the **Navigation Pane**.'],
              ['Workspace', 'Opened from a tile or from **Workspaces**', 'An activity page for one area of work: summary tiles with counts, tabbed lists and links to related pages.'],
              ['Action Pane', 'The bar below the navigation bar, on every page', 'Holds the buttons and tabs for the page, such as **Edit**, **New**, **Delete** and **Options**, and **Action search**.'],
              ['Message bar', 'Below the Action Pane', 'Shows information, warnings and errors about the page you are on.'],
              ['Grid', 'The centre of a list page', 'Rows of records and columns of data. You filter, sort and select rows here.'],
              ['FastTab', 'On a record’s details page', 'A section of fields that expands and collapses.'],
              ['FactBox', 'The pane on the right of some pages', 'Related information about the selected record, such as balances or contacts.'],
          ], widths=[1800, 2700, 4572])]
    o += [blank(), h5('Pages and views'),
          concept_table(['Page type or view', 'What it shows', 'Use it to'], [
              ['List page (Grid view)', 'Many records in a grid', 'Find, filter and select records, and change several records without opening each one.'],
              ['Details page (Details view)', 'One record, in FastTabs', 'Review or change one record. A narrow list on the left moves between records.'],
              ['Header view and Lines view', 'A document such as a journal or an order', '**Header** holds the document’s main fields; **Lines** holds its lines.'],
              ['Dialog', 'A pane that opens over the page', 'Enter the details of an action, then select **OK** or **Cancel**.'],
          ], widths=[2268, 3000, 3804])]
    # --- legal entities
    o += [blank(), h5('Legal entities'),
          concept_table(['Term', 'Description'], [
              ['Legal entity', 'A company set up in D365. The pages you open show the data of the active legal entity only, and the records you create belong to it.'],
              ['Business name', 'The name of the business a legal entity represents. Use it to identify the legal entity you need.'],
              ['Ledger code', 'The code D365 uses for a legal entity. It appears in the legal entity selector and in the D365 URL after **cmp=**. D365 ledger codes differ from CargoWise ledger codes.'],
              ['Default company', 'The legal entity D365 opens in when you sign in. You set it in your user options (topic 1.2).'],
          ]),
          blank(), h5('Working in the correct legal entity'),
          bullet('Check the active legal entity before you create, change or post anything. A record created in the wrong legal entity belongs to that entity.'),
          bullet('Identify legal entities by their business names rather than their ledger codes.'),
          bullet('A page opened in a new window keeps the legal entity it was opened in, so two windows can show different legal entities.')]
    o += [blank(), h5('What you can see in D365'),
          body('The pages, workspaces, legal entities and buttons you see depend on your D365 profile, which your manager requests for you. '
               'It gives you the access your role needs. If a page, module, legal entity or button that your process guide mentions is missing, '
               'or a message says you do not have access, contact the BAU Support team (topic 13.3).')]
    # --- messages
    o += [blank(), h5b('System messages', 'GS_KC_Messages'),
          body('D365 tells you about problems and results in four places. Where a message appears tells you what caused it.'),
          concept_table(['Where it appears', 'What it tells you', 'What to do'], [
              ['Message bar (below the Action Pane)', 'Information, a warning or an error about the page you are on, usually about the data you entered.', 'Read it before you continue. Fix the field it names, then save again. Select **Message details** where shown to see every message.'],
              ['Message box (over the page)', 'An error that stops the action.', 'Read it, select the button it offers, then fix the cause.'],
              ['Action center (bell on the navigation bar)', 'The result of work that ran in the background, such as a report or a batch job, and your alerts.', 'Open the bell to read new messages. It keeps up to 500 messages.'],
              ['Feature callout', 'A short pop-up next to a control that introduces a new feature.', 'Select **Got it** to close it.'],
          ], widths=[2400, 3336, 3336]),
          bodyblank(),
          concept_table(['Message type', 'Meaning'], [
              ['Information', 'Tells you something. Usually no action is needed.'],
              ['Warning', 'The data may cause a problem later. Check it before you continue.'],
              ['Error', 'The action failed. Fix the cause before you try again.'],
          ])]
    # --- filters
    o += [blank(), h5b('Filter operators', 'GS_KC_Filters'),
          body('The column filter and the Filter pane offer operators. The operators shown depend on whether the column holds text, numbers or dates.'),
          concept_table(['Operator', 'What it finds', 'Typed as (with matches)'], [
              ['is exactly / is equal to', 'The exact value.', 'circle'],
              ['is not / is not equal to', 'Every value except this one.', '!circle'],
              ['is one of', 'Any of several values, separated by commas.', 'circle,square'],
              ['contains', 'Values that contain the text.', '§circle§'],
              ['does not contain', 'Values that do not contain the text.', '!§circle§'],
              ['begins with', 'Values that start with the text.', 'circle§'],
              ['after / greater than', 'Values above the one entered.', '>100'],
              ['greater than or equal', 'Values from the one entered upwards.', '100..'],
              ['before / less than', 'Values below the one entered.', '<100'],
              ['less than or equal', 'Values up to the one entered.', '..100'],
              ['between', 'Values from the first to the second.', '100..200'],
              ['matches', 'The pattern you type, using the symbols in the next table.', 'See below'],
          ], widths=[2268, 3969, 2835], bold_first=True),
          blank(), h5('Query symbols'),
          body('The symbols below work only with the **matches** operator. With any other operator, D365 searches for the symbol as plain text: '
               '**matches A§** finds names that start with A, while **is exactly A§** finds only the text “A§”.'),
          concept_table(['Type', 'Finds', 'Example'], [
              ['value§', 'Values that start with the text.', '**S§** finds Sydney and San Francisco.'],
              ['§value', 'Values that end with the text.', '**§east** finds Northeast.'],
              ['§value§', 'Values that contain the text.', '**§th§** finds Northeast and Southeast.'],
              ['?', 'An unknown character at that position.', '**Sm?th** finds Smith and Smyth.'],
              ['!value', 'Every value except this one.', '**!Smith**'],
              ['value,value', 'Any of the values listed.', '**A,D,F**'],
              ['from..to', 'Values from the first to the second.', '**1..10**; for text, **A..C** finds values starting with A or B, and exactly C.'],
              ['""', 'Blank values.', 'Two double quotes find rows with no value in the column.'],
              ['T', 'Today’s date.', '**T** in a date column.'],
          ], widths=[1800, 3402, 3870])]
    o += [blank(), h5('Relative dates'),
          body('A filter with a fixed date keeps that date in a saved view for ever. A relative date, typed with **matches** and in brackets, is worked out again each time the view opens, so the view stays current.'),
          concept_table(['Type', 'Finds'], [
              ['(Day(0))', 'Today. (Day(-1)) is yesterday and (Day(1)) tomorrow.'],
              ['(DayRange(-30,0))', 'The last 30 days, up to today.'],
              ['(LessThanDate(0))', 'Dates before today, for example overdue due dates.'],
              ['(GreaterThanDate(30))', 'Dates more than 30 days from today.'],
              ['(MonthRange(-2,0))', 'The previous two months and this month.'],
              ['(YearRange(-1,0))', 'The previous year and this year.'],
          ])]
    # --- views
    o += [blank(), h5('Views and personalization'),
          concept_table(['Term', 'Description'], [
              ['View', 'A named, saved layout of a page. On a list page it also holds filters, sorting and grouping. The view name shows above the grid.'],
              ['Standard view', 'The view D365 provides. It cannot be changed: save your changes as a new view.'],
              ['Asterisk (§) after the view name', 'The page has changes that are not saved in the view yet. Switching to another view discards them.'],
              ['Locked view (padlock)', 'A view that cannot be edited, such as **Standard** or a view published to you. **Save as** makes your own copy.'],
              ['Default view', 'The view a page opens in. You set it with **Pin as default**, for the current legal entity or for all legal entities.'],
              ['Saved for you automatically', 'Column widths, footer totals and expanded or collapsed FastTabs are remembered for each view without saving.'],
              ['Saved only when you save the view', 'Columns added, hidden or moved, filters, sorting and grouping.'],
          ]),
          note('A page opened from a workspace tile, or from a menu item that has its own filter (for example a list of customers on hold), opens with that filter instead of your default view.')]
    # --- excel
    o += [blank(), h5b('Getting data into Excel', 'GS_KC_Excel'),
          concept_table(['Tool', 'What you get', 'Use it when'], [
              ['Export to Excel (Export all rows)', 'A one-off copy of the grid as it is shown: the same columns, filter and values. It cannot be refreshed or sent back to D365.', 'You need the data for analysis or a report outside D365.'],
              ['Open in Excel', 'A live workbook linked to D365 through the Microsoft Dynamics Office Add-in. You can refresh it, and change rows and publish them back.', 'Your process guide tells you to update records from Excel.'],
          ], widths=[2268, 3969, 2835]),
          important('Exported files can hold confidential company and customer data. Keep them in an approved WiseTech Global location and delete them when you no longer need them.',
                    comment='[Q01] GS-19: Confirm the company rule for exported D365 data: where exported files may be kept and shared, and who may receive them. The Important box states a general rule until the PG owner confirms it.')]
    # --- reports
    o += [blank(), h5b('Report destinations', 'GS_KC_Reports'),
          concept_table(['Destination', 'What happens', 'In the background?'], [
              ['Screen', 'The report opens in the PDF viewer, where you can download or print it. This is the default.', 'No'],
              ['File', 'The report is saved in the format you choose, such as PDF or Excel, and downloaded.', 'No'],
              ['Print archive', 'A copy is stored in the **Print archive**, where you open it later.', 'Yes'],
              ['Email', 'The report is sent as an attachment.', 'Yes'],
              ['Printer', 'The report prints on a network printer set up for D365.', 'Yes'],
          ], widths=[1900, 5372, 1800])]
    # --- workflow
    o += [blank(), h5b('Workflow', 'GS_KC_Workflow'),
          body('A workflow routes a document, such as a journal or a vendor invoice, to the people who must review or approve it. '
               'The steps, approvers and buttons you see depend on how each workflow is set up, so your process guide says which workflow applies.'),
          concept_table(['Term', 'Description'], [
              ['Originator', 'The person who submits the document to workflow.'],
              ['Work item', 'A task, review or approval that the workflow assigns to you. It appears in **Work items assigned to me**.'],
              ['Approver', 'A person who approves, rejects, requests a change or delegates the work item.'],
              ['Workflow history', 'The record of the document in workflow: who submitted and acted on it, when, and their comments.'],
              ['Delegate', 'Give a work item to another user, who acts on your behalf.'],
          ]),
          note('Workflow email notifications do not appear in the **Action center**. Check **Work items assigned to me** on the dashboard.')]
    # --- shortcuts
    o += [blank(), h5('Keyboard shortcuts'),
          body('To see the shortcuts for a page, right-click anywhere on the page and select **View shortcuts**. The list groups them under **Navigate**, **Act on data**, **Close** and **Other**. '
               'Pressing **Alt+Shift+K** shows a similar list that starts with **Shortcuts for selected element**: it changes with the part of the page you are on. **View all product shortcuts** opens Microsoft’s full list.'),
          concept_table(['Shortcut', 'What it does (as D365 labels it)'], [
              ['Alt+G', 'Search for a page'],
              ['Alt+Q', 'Search for an action'],
              ['Ctrl+Shift+O', 'Change company (legal entity)'],
              ['Alt+Shift+Home', 'Go to the dashboard'],
              ['Alt+F1', 'Open navigation pane'],
              ['F2', 'Switch to edit mode'],
              ['Alt+N', 'Create a new record'],
              ['Alt+S', 'Save record'],
              ['Alt+Delete', 'Delete record'],
              ['Ctrl+Shift+F5', 'Revert any changes'],
              ['Shift+F5', 'Refresh data'],
              ['Ctrl+Shift+M', 'Select or clear all rows'],
              ['Ctrl+Shift+G / Ctrl+Shift+D', 'Switch to grid view / details view'],
              ['Alt+M, F', 'Go to the filter pane'],
              ['Ctrl+Shift+F3', 'Open advanced filtering and sorting options'],
              ['Ctrl+Shift+P', 'Personalize this page'],
              ['Ctrl+Shift+E', 'Export to Excel'],
              ['Ctrl+Shift+F7', 'Open message center'],
              ['Esc', 'Close the page'],
              ['Shift+Esc', 'Save changes and close the page'],
              ['Alt+Shift+Q', 'Close the page and discard any unsaved changes'],
          ], widths=[3000, 6072]),
          blank(),
          body('These shortcuts work inside a field or a grid:',
               comment='GS-07: The main table is from the View shortcuts list in our environment (Daniel Moreira, 27 November 2026). Test the four field and grid shortcuts below, which come from Microsoft\'s list, in the clean-session test.'),
          concept_table(['Shortcut', 'What it does'], [
              ['Ctrl+G', 'Filter the current grid column'],
              ['Alt+Down arrow', 'Open a lookup or date picker'],
              ['T / D', 'In a date field: today / the session date'],
              ['Ctrl+Shift+A', 'Attach a document to the record'],
          ], widths=[3000, 6072])]
    o.append(blank())
    return o
