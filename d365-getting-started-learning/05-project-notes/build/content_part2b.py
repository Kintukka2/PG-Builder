from pgxml import *
from content_part2a import sub, topic, RESP, ENTITY, ACCESS, R

def part2b():
    o = []
    # ---------------- 4 Records
    o += topic(4, 'GS_T4', 'Work with Records',
        ['Use this topic to change, create and delete records, to enter values with lookups and date pickers, and to run any button on a page with action search. '
         'Most pages open locked for viewing, so that data is not changed by accident: you switch to Edit mode to make changes.'],
        [f'{R}: views and maintains the records their role allows.'],
        ['A user needs to change, create or delete a record, or to run an action on a page.'],
        overview=[('GS_T4_1', '4.1 Edit, Save and Revert a Record', 'Switch to Edit mode, change a record and save it, or undo unsaved changes.'),
                  ('GS_T4_2', '4.2 Create and Delete a Record', 'Add a new record, or delete one.'),
                  ('GS_T4_3', '4.3 Enter Values with Lookups and Date Pickers', 'Choose valid values from a lookup and dates from a date picker.'),
                  ('GS_T4_4', '4.4 Run an Action with Action Search', 'Find and run a button on the page by typing its name.')])
    RESP['GS_T4_1'] = 'changes records their role allows them to change.'
    o += sub('4.1', 'GS_T4_1', 'Edit, Save and Revert a Record',
        ['Use this procedure to change a record and save the change, or to undo changes you have not saved. In View mode the Action Pane shows **Edit**; in Edit mode it shows **Save**.'],
        ['A record needs to change, as a process guide describes.'],
        'Complete these steps to edit and save a record:',
        ['The record is open (see [[GS_T2_1|2.1 Open a Page from the Navigation Pane]]).'],
        [ENTITY,
         ('*Click* **Edit**.', 'On the Action Pane, click **Edit**, or press **F2**. The fields you can change become editable. If **Edit** is not shown, the page is always editable or always read-only.'),
         ('*Enter* the change.', 'Change the fields your process guide gives. Read any message that appears in the message bar.'),
         ('*Click* **Save**.', 'On the Action Pane, click **Save**, or press **Alt+S**.',
          'GS-09: Confirm what happens to unsaved changes when a user moves to another record or closes the page (Microsoft does not document it), and the label and place of Revert (Options tab). Step 4 tells users to save explicitly until this is confirmed.'),
         ('*Confirm* the record is saved.', 'Check that no error shows in the message bar and the changed values remain. To undo changes you have not saved, select **Revert** on the **Options** tab of the Action Pane, or press **Ctrl+Shift+F5**.')],
        ('complete', ['The record shows the change, saved.']))
    RESP['GS_T4_2'] = 'creates and deletes records their role allows.'
    o += sub('4.2', 'GS_T4_2', 'Create and Delete a Record',
        ['Use this procedure to add a new record, or to delete one, on a page where your process guide tells you to. A deleted record cannot be restored, so check it before you delete.'],
        ['A process guide tells the user to create or delete a record.'],
        'Complete these steps to create a record:',
        ['The page is open in the required legal entity.'],
        [ENTITY,
         ('*Click* **New**.', 'On the Action Pane, click **New**, or press **Alt+N**. A new record or row opens; on some pages a dialog opens instead.'),
         ('*Enter* the required fields.', 'Enter the values your process guide gives. Required fields are marked; D365 shows a message for any that are missing.'),
         ('*Click* **Save**.', 'Click **Save**, or **OK** in a dialog.'),
         ('*Confirm* the record is created.', 'Check that the new record appears in the list with the values you entered.')],
        ('complete', ['The new record is saved in the active legal entity.']),
        extra_after=[h5('Delete a Record'), lead('Complete these steps to delete a record:'),
                     procedure(['Your process guide tells you to delete the record.'], R,
                               [('*Select* the record.', 'Select the record in the list, or open it.'),
                                ('*Click* **Delete**.', 'On the Action Pane, click **Delete**, or press **Alt+Delete**.'),
                                ('*Confirm* the deletion.', 'Read the message and click **Yes** to delete the record.',
                                 'GS-10: Confirm the delete confirmation message and its buttons in our environment.')],
                               ('complete', ['The record is deleted and no longer in the list.']))])
    RESP['GS_T4_3'] = 'enters values in the records they work on.'
    o += sub('4.3', 'GS_T4_3', 'Enter Values with Lookups and Date Pickers',
        ['Use this procedure to fill a field from its list of valid values (a lookup), and a date field from the date picker. '
         'Many lookups accept the name as well as the code: in a customer account field you can type the customer’s name instead of the account number.'],
        ['A field with a drop-down arrow needs a value.'],
        'Complete these steps to enter a value with a lookup:',
        ['The record is in Edit mode (see [[GS_T4_1|4.1 Edit, Save and Revert a Record]]).'],
        [('*Type* the start of the value.', 'Type the first characters of the code or name. After a short pause the lookup opens, showing values that begin with what you typed. Keep typing to narrow the list.'),
         ('*Select* the value.', 'Use the **Up** and **Down** arrow keys, then press **Enter**, or click the value. To see the whole list, click the arrow or press **Alt+Down arrow**.'),
         ('*Filter* the lookup if the value is not found.', 'Optional. To find a value by other text, clear the field, open the lookup, then filter a lookup column as in [[GS_T5_2|5.2 Filter and Sort a Column]].'),
         ('*Enter* a date.', 'In a date field, type the date, or click the calendar icon (**Alt+Down arrow**) and pick it. Type **T** for today, or **D** for the session date.'),
         ('*Confirm* the values are accepted.', 'Check that no error shows beside the field or in the message bar.')],
        ('complete', ['The fields hold valid values.']),
        extra_after=[note('In a numeric field you can type a calculation starting with an equals sign, for example **=15§4**, and D365 enters the result.')])
    RESP['GS_T4_4'] = 'runs page actions by name.'
    o += sub('4.4', 'GS_T4_4', 'Run an Action with Action Search',
        ['Use this procedure to find and run a button on the current page by typing its name, instead of looking through the Action Pane tabs. It finds buttons on the Action Pane and toolbars that the page shows.'],
        ['A user needs a button but does not know which tab holds it.'],
        'Complete these steps to run an action with action search:',
        ['The page is open.'],
        [('*Click* **Action search**.', 'At the right of the Action Pane, click the magnifying glass, or press **Alt+Q**.'),
         ('*Type* the button name.', 'Type all or part of the button name. Each result shows where the button sits, for example its tab.'),
         ('*Select* the button.', 'Select the button in the results. It runs as if you had clicked it on the Action Pane.'),
         ('*Confirm* the action ran.', 'Check the result on the page or in the message bar.')],
        ('complete', ['The action has run on the current page.']))
    # ---------------- 5 Filters
    o += topic(5, 'GS_T5', 'Find Records with Filters',
        ['Use this topic to find the records you need on a list page. D365 has four filter tools: the **Filter** box above a grid (QuickFilter), the filter on a column header, the **Filter pane**, and **Advanced filter or sort**. '
         'The operators and symbols they accept are in Part 1, [[GS_KC_Filters|Filter operators]].'],
        [f'{R}: filters the lists they work with.'],
        ['A list shows more records than the task needs.'],
        overview=[('GS_T5_1', '5.1 Filter with the QuickFilter', 'Filter one column by typing in the Filter box.'),
                  ('GS_T5_2', '5.2 Filter and Sort a Column', 'Filter or sort from a column header.'),
                  ('GS_T5_3', '5.3 Filter with the Filter Pane', 'Filter several fields at once, including fields not shown in the grid.'),
                  ('GS_T5_4', '5.4 Use Advanced Filter or Sort', 'Optional. Build a filter on several fields, or sort by more than one column.')])
    RESP['GS_T5_1'] = 'filters the lists they work with.'
    o += sub('5.1', 'GS_T5_1', 'Filter with the QuickFilter',
        ['Use this procedure to filter a list quickly on one column, by typing in the **Filter** box above the grid.'],
        ['A user needs to find a record or a few records quickly.'],
        'Complete these steps to filter with the QuickFilter:',
        ['The list page is open.'],
        [ENTITY,
         ('*Type* the value in the **Filter** box.', 'Type the value in the **Filter** box above the grid. A list of columns appears below the box.'),
         ('*Select* the column.', 'Select the column the value belongs to, for example **Name** or **Account**. D365 remembers the column you choose.'),
         ('*Press* **Enter**.', 'Press **Enter**. The grid shows only the matching rows.'),
         ('*Clear* the filter when you finish.', 'Delete the text in the **Filter** box and press **Enter** to see all rows again.')],
        ('complete', ['The grid shows the rows that match the value.']))
    RESP['GS_T5_2'] = 'filters and sorts the lists they work with.'
    o += sub('5.2', 'GS_T5_2', 'Filter and Sort a Column',
        ['Use this procedure to filter a column with an operator, such as **contains** or **greater than**, or to sort the grid by a column. A column whose header cannot be clicked cannot be filtered or sorted.'],
        ['A user needs to limit or order the rows by one column.'],
        'Complete these steps to filter and sort a column:',
        ['The list page is open.'],
        [ENTITY,
         ('*Click* the column header.', 'Click the header of the column, or select a cell in it and press **Ctrl+G**. The column filter opens.'),
         ('*Select* the filter operator.', 'Select the operator next to the field name, for example **contains**. See [[GS_KC_Filters|Filter operators]] in Part 1.'),
         ('*Enter* the filter value.', 'Enter the value. For example, to exclude zero balances, select **is not equal to** and enter **0**.'),
         ('*Click* **Apply**.', 'Click **Apply**, or press **Enter**. The grid shows only the matching rows. **Clear** removes this column’s filter.'),
         ('*Sort* the column.', 'Optional. In the same drop-down, select **Sort A to Z** or **Sort Z to A** (for numbers and dates, smallest or largest first).'),
         ('*Confirm* the rows shown.', 'Check that the grid shows only the rows you need, in the order you need.')],
        ('complete', ['The grid is filtered and sorted by the column.']))
    RESP['GS_T5_3'] = 'filters the lists they work with.'
    o += sub('5.3', 'GS_T5_3', 'Filter with the Filter Pane',
        ['Use this procedure to filter several fields at once, including fields that the grid does not show. The Filter pane applies to the main list of the page, not to lines grids.'],
        ['A user needs to filter on more than one field, or on a field that is not in the grid.'],
        'Complete these steps to filter with the Filter pane:',
        ['The list page is open.'],
        [ENTITY,
         ('*Click* **Show filters**.', 'Click **Show filters** (the funnel icon at the side of the page), or press **Alt+M, F**. The Filter pane opens.',
          'GS-11: Confirm which side the Filter pane opens on (Microsoft\'s training says right; the current article says left) and the label of its reset control.'),
         ('*Enter* a value for each field.', 'For each field, select the operator and enter the value.'),
         ('*Click* **Add a filter field**.', 'Optional. To filter on a field that is not listed, click **Add a filter field** and select it.'),
         ('*Click* **Apply**.', 'Click **Apply**. The grid shows only the rows that match every filter.'),
         ('*Confirm* the rows shown.', 'Check the rows, then close the pane with **Hide filters** or **Esc**.')],
        ('complete', ['The grid shows the rows that match all the filters.']))
    RESP['GS_T5_4'] = 'builds advanced filters when a simple filter is not enough.'
    o += sub('5.4', 'GS_T5_4', 'Use Advanced Filter or Sort',
        ['Use this procedure to build a filter from several criteria, on fields the page does not show, or to sort by more than one column. '
         'The dialog uses the names of the underlying tables and fields, which can differ from the page labels. Most users need it rarely.'],
        ['A filter needs more criteria than the Filter pane offers, or the list must be sorted by more than one column.'],
        'Complete these steps to use advanced filter or sort:',
        ['The list page is open.'],
        [('*Press* **Ctrl+Shift+F3**.', 'Press **Ctrl+Shift+F3** (**Open advanced filtering and sorting options**). The advanced filter dialog opens on the **Range** tab.',
          'GS-12: Confirm the menu label and location of Advanced filter or sort in our environment (historically on the Options tab under Page options), the dialog\'s title and its tabs (Range, Sorting).'),
         ('*Click* **Add**.', 'On the **Range** tab, click **Add** to add a line.'),
         ('*Select* the **Field**.', 'Select the table and field to filter on.'),
         ('*Enter* the **Criteria**.', 'Enter the value, using the symbols in [[GS_KC_Filters|Filter operators]] in Part 1.'),
         ('*Click* **OK**.', 'Click **OK**. The page shows the rows that match the criteria.')],
        ('complete', ['The grid shows the rows that match the advanced criteria.']))
    # ---------------- 6 Personalized view
    o += topic(6, 'GS_T6', 'Create a Personalized View',
        ['Use this topic to set up a page so it shows the columns, filters and totals you need, and save that layout as a view that opens by default. '
         'Each process guide lists the columns recommended for its pages.'],
        [f'{R}: creates personal views for the pages they use.'],
        ['A page does not show the information needed in the way it is needed.'],
        overview=[('GS_T6_1', '6.1 Arrange the Columns', 'Add, hide, move, freeze and size columns. Output: the grid shows the columns you need.'),
                  ('GS_T6_2', '6.2 Add a Footer Total', 'Optional. Show a total, minimum, maximum or average under a numeric column.'),
                  ('GS_T6_3', '6.3 Group Rows', 'Optional. Group the rows by a column, with subtotals.'),
                  ('GS_T6_4', '6.4 Save and Pin the View', 'Save the layout as a named view and pin it as your default.')])
    RESP['GS_T6_1'] = 'arranges the grids they use.'
    o += sub('6.1', 'GS_T6_1', 'Arrange the Columns',
        ['Use this procedure to show the columns you need in the order you need them. Changes to columns are kept only when you save the view (6.4); column widths are remembered automatically.'],
        ['A grid lacks a column the task needs, or shows columns it does not.'],
        'Complete these steps to arrange the columns:',
        ['Access to D365 and to the page.'],
        [ENTITY,
         ('*Open* the page you want to personalize.', 'Open the list page whose layout you want to save.'),
         ('*Right-click* a column header.', 'Right-click the header of any column. The menu shows the column options.'),
         ('*Click* **Insert columns**.', 'Click **Insert columns**, select each column you need, then click **Update**. The columns are added to the grid.'),
         ('*Hide* each column you do not need.', 'Right-click the header of the column and click **Hide this column**.'),
         ('*Move* the columns into the order you need.', 'Drag a column header to its new position.'),
         ('*Freeze* the key column.', 'Optional. Right-click the header of the column you always need to see, such as the account, and click **Freeze column**. It stays in view as you scroll.'),
         ('*Size* the columns.', 'Drag the edge of a column header to resize it, or double-click the edge to fit the column to its content.')],
        ('step', ['The grid shows the columns you need, in your order.'], ('GS_T6_2', '6.2 Add a Footer Total')))
    RESP['GS_T6_2'] = 'adds totals to the grids they use.'
    o += sub('6.2', 'GS_T6_2', 'Add a Footer Total',
        ['Use this procedure to show a calculated value at the foot of a numeric column, such as the total of an amount column. With more than one row selected, the footer shows the value for the selected rows. '
         'Footer totals are remembered automatically for the view; they do not need to be saved.'],
        ['A user needs the total of a numeric column at a glance.'],
        'Complete these steps to add a footer total:',
        ['The grid shows the column to total (see [[GS_T6_1|6.1 Arrange the Columns]]).'],
        [('*Right-click* in the numeric column.', 'Right-click a value in the amount or balance column.'),
         ('*Click* **View column totals**.', 'Click **View column totals**, then the value you need: **Total**, **Minimum**, **Maximum** or **Average**. The footer opens below the grid.',
          'GS-13: Confirm the footer total labels in our environment: Microsoft documents View column totals (Total, Minimum, Maximum, Average, with the extended totals feature) or Total this column without it, and Show total / Select calculated value in the footer. 260 uses "+" and "Calculate column", which this replaces if the test confirms it.'),
         ('*Click* **Calculate**.', 'If the footer shows a dash, the list is too large to total automatically: click **Calculate** in the footer.'),
         ('*Confirm* the total is displayed.', 'Check that the footer shows the value under the column.')],
        ('step', ['The footer shows the value for the column.'], ('GS_T6_3', '6.3 Group Rows')),
        extra_after=[note('To show or hide the footer, select **Grid options** (the three dots at the right of the grid header) and **Show footer** or **Hide footer**.')])
    RESP['GS_T6_3'] = 'groups the grids they use.'
    o += sub('6.3', 'GS_T6_3', 'Group Rows',
        ['Use this procedure to group the rows by the values of a column, for example by customer or currency. Each group has a header row with its row count and any footer totals as subtotals. Skip it if you do not need groups: continue to [[GS_T6_4|6.4 Save and Pin the View]].'],
        ['A user needs subtotals or rows organized by a value.'],
        'Complete these steps to group rows:',
        ['The grid shows the column to group by.'],
        [('*Right-click* the column header.', 'Right-click the header of the column to group by.'),
         ('*Click* **Group by this column**.', 'Click **Group by this column**. A header row starts each group. Group by another column to add a level, up to five.'),
         ('*Expand* or collapse a group.', 'Click the arrow in a group header to show or hide its rows.'),
         ('*Confirm* the grouping.', 'Check the groups and their subtotals. To remove grouping, select **Grid options** > **Ungroup all**.')],
        ('step', ['The rows are grouped, with subtotals.'], ('GS_T6_4', '6.4 Save and Pin the View')))
    RESP['GS_T6_4'] = 'saves and pins their own views.'
    o += sub('6.4', 'GS_T6_4', 'Save and Pin the View',
        ['Use this procedure to save the layout as a named view and pin it as your default, so the page opens with your columns, filters and grouping each time.'],
        ['The page layout is ready to keep.'],
        'Complete these steps to save and pin the view:',
        ['The grid shows the columns, and any filters, totals and grouping, you need.'],
        [('*Open* the view selector.', ['Above the grid, click the current view name, for example **Standard**.', 'Note: An asterisk (§) beside the view name means the layout has unsaved changes.']),
         ('*Click* **Save as**.', 'Click **Save as**. The **Save view as** pane opens.'),
         ('*Enter* the view name.', 'Enter a name that identifies the page and the purpose of the view. Add a description if it helps.'),
         ('*Select* **Pin as default**.', 'Select **Pin as default** so the page opens in this view.'),
         ('*Select* the legal entities.', 'Keep the view for all legal entities, or limit it to the legal entities you select.',
          'GS-14: Confirm the name of the out-of-box view (Standard), and the label and place of the legal entity choice in Save view as and in Pin as default (current or all legal entities). Same question as 260 G260-07.'),
         ('*Click* **Save**.', 'Click **Save**.'),
         ('*Confirm* the view is saved and pinned.', 'Check that the view name shows above the grid without an asterisk, and that the view is marked as the default in the view selector.')],
        ('complete', ['The page has a saved view with your layout, pinned as your default.']))
    # ---------------- 7 Manage views
    o += topic(7, 'GS_T7', 'Manage Saved Views and Personalizations',
        ['Use this topic to change a saved view, organize your views, personalize the fields of a page, and reset a page you have personalized.'],
        [f'{R}: manages their own views and personalizations.'],
        ['A saved view needs to change, a page layout needs tidying, or a page needs to return to its default layout.'],
        overview=[('GS_T7_1', '7.1 Update a Saved View', 'Change a saved view and save it.'),
                  ('GS_T7_2', '7.2 Manage My Views', 'Rename, reorder, pin or delete your views.'),
                  ('GS_T7_3', '7.3 Personalize a Page', 'Hide, move or add fields on a page with the personalization toolbar.'),
                  ('GS_T7_4', '7.4 Clear a Personalization', 'Return a view or page to its default layout.')])
    RESP['GS_T7_1'] = 'updates their own saved views.'
    o += sub('7.1', 'GS_T7_1', 'Update a Saved View',
        ['Use this procedure to change a view you saved, for example to add a column or change a filter. A view you cannot edit shows a padlock: use **Save as** to make your own copy.'],
        ['A saved view needs a further change.'],
        'Complete these steps to update a saved view:',
        ['A saved view for the page (see [[GS_T6|6. Create a Personalized View]]).'],
        [ENTITY,
         ('*Open* the page that has the saved view.', 'Open the page whose view you want to change.'),
         ('*Select* the saved view.', 'Open the view selector above the grid and select the view.'),
         ('*Make* the change to the layout.', 'Change the columns, filters or grouping as in [[GS_T6|6. Create a Personalized View]]. An asterisk shows beside the view name.'),
         ('*Click* **Save**.', 'Open the view selector and click **Save**.'),
         ('*Confirm* the view shows the change.', 'Check that the view name shows without an asterisk and the change is kept when you reopen the page.')],
        ('complete', ['The saved view includes the change.']))
    RESP['GS_T7_2'] = 'organizes their own views.'
    o += sub('7.2', 'GS_T7_2', 'Manage My Views',
        ['Use this procedure to rename your views, change their order in the view selector, pin one as default, or delete those you no longer use. A deleted view cannot be restored. Views published to you can be pinned but not renamed or deleted.'],
        ['A user’s views for a page need organizing.'],
        'Complete these steps to manage your views:',
        ['The page has views you saved.'],
        [('*Open* the view selector.', 'Above the grid, click the view name.'),
         ('*Click* **More**.', 'Click **More**, then **Manage my views**.'),
         ('*Select* a view.', 'Under **My views**, select the view to change.'),
         ('*Click* the action you need.', 'Click **Pin as default**, **Move up**, **Move down**, **Rename** or **Delete**.'),
         ('*Click* **Update**.', 'Click **Update** to apply the changes.')],
        ('complete', ['Your views are named, ordered and pinned as you need.']))
    RESP['GS_T7_3'] = 'personalizes the pages they use.'
    o += sub('7.3', 'GS_T7_3', 'Personalize a Page',
        ['Use this procedure to change the fields shown on a page, such as a details page or a FastTab, with the personalization toolbar. Changes made with the toolbar are kept only when you save them to a view.'],
        ['A page shows fields the user does not need, or lacks one they do.'],
        'Complete these steps to personalize a page:',
        ['The page is open.'],
        [('*Open* the personalization toolbar.', 'On the Action Pane, select **Options** > **Personalize this page**, or press **Ctrl+Shift+P**. The toolbar opens and the page becomes read-only.',
          'GS-15: Confirm the personalization toolbar tool labels in our environment (Microsoft\'s article and screenshot differ: Add fields / Add a field).'),
         ('*Click* the tool you need.', 'Click **Hide** to hide a field, **Move** to drag it to another place, or **Add a field** to add one.'),
         ('*Select* the field.', 'Select the field or section on the page. Hidden fields show shaded while the toolbar is open: select one again to show it.'),
         ('*Click* **Close**.', 'Close the toolbar. An asterisk shows beside the view name.'),
         ('*Save* the view.', 'Save the change to your view as in [[GS_T7_1|7.1 Update a Saved View]], or with **Save as**.')],
        ('complete', ['The page shows the fields you need, saved in your view.']))
    RESP['GS_T7_4'] = 'resets their own personalizations.'
    o += sub('7.4', 'GS_T7_4', 'Clear a Personalization',
        ['Use this procedure to return the current view, or a page without views, to its default layout. Clearing cannot be undone. To discard only unsaved changes, switch back to the saved view instead.'],
        ['A personalized page is not working as expected, or needs to return to its default.'],
        'Complete these steps to clear a personalization:',
        ['The page is open in the view to reset.'],
        [('*Open* the personalization toolbar.', 'Select **Options** > **Personalize this page**, or press **Ctrl+Shift+P**.'),
         ('*Click* the more options button.', 'On the toolbar, click **…** (more options).'),
         ('*Click* **Clear**.', 'Click **Clear** and confirm. The personalizations of the current view are removed.'),
         ('*Confirm* the default layout.', 'Check that the page shows its default fields and columns.')],
        ('complete', ['The view or page is back to its default layout.']))
    # ---------------- 8 Excel
    o += topic(8, 'GS_T8', 'Export Data and Work in Excel',
        ['Use this topic to get data from a page into Excel: as a one-off export of the grid, or as a workbook linked to D365. See [[GS_KC_Excel|Getting data into Excel]] in Part 1 to choose between them.'],
        [f'{R}: exports or opens the data their role allows.'],
        ['Page data is needed in Excel.'],
        overview=[('GS_T8_1', '8.1 Export All Rows from a Grid', 'Export the grid, as shown, to an Excel file.'),
                  ('GS_T8_2', '8.2 Open a Page in Excel and Publish Changes', 'Open a linked workbook, refresh it and, where your process guide allows, publish changes to D365.')])
    RESP['GS_T8_1'] = 'exports grid data for internal analysis.'
    o += sub('8.1', 'GS_T8_1', 'Export All Rows from a Grid',
        ['Use this procedure to export the rows of a grid to an Excel file. The export contains the columns and rows the grid shows, with its filters, so arrange and filter the grid first. '
         'The export is a copy: it does not change when the data in D365 changes.'],
        ['Grid data is needed in Excel for internal analysis.'],
        'Complete these steps to export all rows from a grid:',
        ['Access to D365 and to the page that holds the data.'],
        [ENTITY,
         ('*Open* the page that holds the data.', 'Open the list page whose grid holds the data you need.'),
         ('*Confirm* the grid shows the columns and rows you need.', 'The export contains the columns and filters of the grid. Add any column you need first (see [[GS_T6_1|6.1 Arrange the Columns]]).'),
         ('*Right-click* the grid header.', 'Right-click the header of any column in the grid.'),
         ('*Select* **Export all rows**.', ['Select **Export all rows**. To export only some rows, select them first and choose **Export marked rows**.', 'Note: You can also select **Open in Microsoft Office** > **Export to Excel** on the Action Pane, or press **Ctrl+Shift+E**.'],
          '[Q03] GS-16: Confirm the export row limit set for our environment (Microsoft\'s default is 50,000 rows, configurable up to 1,000,000). Same as 260 Export to Excel VG-06.'),
         ('*Download* the export.', 'Download the file when D365 has prepared it. The download link works for 15 minutes.'),
         ('*Open* the exported file.', 'Open the file in Excel.'),
         ('*Confirm* the required fields were exported.', 'Check that the file holds every field and row you need.')],
        ('complete', ['The grid rows are in an Excel file with the grid’s columns, for internal use.']))
    RESP['GS_T8_2'] = 'opens linked workbooks, and publishes changes only where their process guide allows.'
    o += sub('8.2', 'GS_T8_2', 'Open a Page in Excel and Publish Changes',
        ['Use this procedure to open the data of a page in an Excel workbook that stays linked to D365 through the Microsoft Dynamics Office Add-in. '
         'You can refresh the workbook with current data and, where your process guide says so, change rows and publish them back to D365. The add-in does not run on Excel for Mac.'],
        ['A process guide tells the user to view or update records in Excel.'],
        'Complete these steps to open a page in Excel:',
        ['Access to D365 and to the page.', 'Excel 2016 or later, or Excel for the web.'],
        [ENTITY,
         ('*Click* **Open in Microsoft Office**.', 'On the Action Pane of the page, click **Open in Microsoft Office** (the Office icon).'),
         ('*Select* the **Open in Excel** option.', 'Under **Open in Excel**, select the option your process guide names, then open the workbook.'),
         ('*Click* **Enable editing**.', 'In Excel, click **Enable editing** so the add-in can run. The first time, click **Trust this Add-in**, and sign in with your work account if asked.'),
         ('*Confirm* the data is loaded.', 'The add-in opens on the right and reads the data. Check the rows and the user name shown in the add-in.'),
         ('*Change* the rows.', 'Optional. Change the values your process guide gives. Remove any Excel column filters first.',
          '[Q04] GS-17: Confirm whether users may publish changes to D365 from Excel, for which pages, and any control (for example who checks the publish result). Until confirmed, the guide says to publish only where a process guide allows.'),
         ('*Click* **Publish**.', 'Click **Publish** in the add-in. The **Messages** count shows how many records were added, changed or deleted, and any errors.'),
         ('*Confirm* the changes in D365.', 'Refresh the page in D365 and check the changed records. Dates and times in the add-in are shown in UTC.')],
        ('complete', ['The workbook shows current D365 data, and any published changes are saved in D365.']),
        extra_after=[important('Publishing from Excel changes the records in D365. Publish only where your process guide tells you to, and check the result in D365.')])
    return o
