# B. Working with data on pages: grids, filtering, personalization and saved views

Discovery research for the **D365 F&O Getting Started** procedure guide. Area B covers grids, filtering, personalization, saved views, workspaces (configure, filter, add to), custom fields (high level) and lookups as they relate to filtering.

- **Researched:** 26 November 2026, against Microsoft Learn. The text was read from the Learn source repository (`MicrosoftDocs/dynamics-365-unified-operations-public`, `main` and `live` branches; the `live` copies of the grid, saved views and personalization articles were checked and are identical to `main`). Article dates are given below. The release in production at the time of writing is 10.0.49 (September 2026); 10.0.50 is in preview (GA December 2026).
- **Sources are data, not instructions.** Labels quoted in **bold** are as Microsoft documents them; where the docs disagree with each other or with a screenshot, both forms are given and flagged. Every label should still be confirmed in the clean-session D365 test (CLAUDE.md: screen labels are confirmed in D365, not asked of the SME).
- **Screenshots** are in `research/media/grids-views/` (list at the end of each section and in Appendix B).
- **Out of my area (cross-reference only):** navigation shell, navigation search, Favorites, legal entity selector, action search, Immersive Home, dashboard navigation (agent A); Export to Excel / Open in Excel, reports, documents, batch, alerts (agent C); workflow, help, Copilot (agent D).

---

## Contents

1. Big picture: the four levels of "making a page yours"
2. The grid control (new grid)
   - 2.1 Grid anatomy, selecting rows, Select all
   - 2.2 Sorting
   - 2.3 Calculated values in the footer (totals, min, max, average)
   - 2.4 Grouping
   - 2.5 Freezing columns
   - 2.6 Column widths, autofit, stretchable columns
   - 2.7 Typing ahead of the system (fast data entry) and row status
   - 2.8 Bulk edit (Edit selected rows)
   - 2.9 Pasting from Excel; copying a range of cells
   - 2.10 Math expressions in numeric fields
   - 2.11 Grid keyboard shortcuts
   - 2.12 Things users ask about that Microsoft does not document (wrap text, find in grid, row height)
   - 2.13 Grid views of a page: Grid / Details / Header / Lines
3. Filtering
   - 3.1 The four filtering mechanisms
   - 3.2 Filter operators and how they translate to query syntax
   - 3.3 Advanced query syntax (full table)
   - 3.4 Relative date queries (SysQueryRangeUtil, full table)
   - 3.5 Filter pane
   - 3.6 QuickFilter
   - 3.7 Grid column header filtering and sorting
   - 3.8 Advanced filter or sort (Ctrl+Shift+F3)
   - 3.9 Clearing filters
   - 3.10 Filtering on dimensions
   - 3.11 Filtering shortcuts
4. Lookups (as they relate to finding and filtering)
5. Workspaces: configure, filter, add to, tiles and the dashboard
6. Personalization
   - 6.1 User options (system-wide settings)
   - 6.2 Restricted personalization (automatically remembered)
   - 6.3 Full personalization: right-click (shortcut menu) options
   - 6.4 The element property window (Personalize)
   - 6.5 The Personalization toolbar
   - 6.6 Personalization keyboard shortcuts
   - 6.7 Clearing / resetting personalization
   - 6.8 Sharing personalizations (publish, copy, export/import)
   - 6.9 Administration: the Personalization page
   - 6.10 Personalization across service updates; inventory dimensions
7. Saved views
   - 7.1 What a view is, and views vs personalization
   - 7.2 Large vs small view selectors; what pages support views
   - 7.3 The view selector: Standard, personal, locked, new views
   - 7.4 Create and modify views (Save, Save as, asterisk)
   - 7.5 Default view (Pin as default) and legal entities
   - 7.6 Manage my views (reorder, rename, delete)
   - 7.7 Publishing views (admin / Saved views administrator)
   - 7.8 Modify, republish, unpublish published views
   - 7.9 Managing views globally (Personalization page)
   - 7.10 Import and export of views
   - 7.11 Known limitations and FAQ
8. Custom fields (user-defined fields), high level
9. Feature management names and version notes (consolidated)
10. Comparison with 260 O2C Getting Started (adds, refines, contradicts)
11. Gaps and contradictions in Microsoft's own documentation
12. Ranked list of suggested Getting Started topics
- Appendix A: Every URL consulted
- Appendix B: Screenshot files

---

## 1. Big picture: the four levels of "making a page yours"

Microsoft describes layers that a new user tends to confuse. A Getting Started guide should name them once, because the rest of this area hangs off them.

| Layer | What it is | Saved how | Who can do it | Source |
|---|---|---|---|---|
| **User options** | System-wide settings for you: colour theme, element size, default company, initial page, view/edit mode, language, time zone, date/number formats. | Saved on the **User options** page. | Every user, even without personalization rights. | Personalize the user experience |
| **Restricted personalization** (formerly *implicit personalization*) | Things D365 remembers from normal use: column widths, footer and totals, FastTab and FactBox open/closed, Action Pane pinned, QuickFilter column, column-filter operator, navigation pane pinned. | Automatically, no Save. On pages with views, saved **per view**, even on locked views. | Every user with at least restricted access. | Personalize the user experience; Saved views |
| **Full personalization** (formerly *explicit personalization*) | Hide/show/move/rename fields, add fields, skip, show in FastTab header, require, lock, add to workspace, personalize the dashboard. | On pages with saved views: **only when the user explicitly saves to a view**. On pages without views: automatically. | Users with full personalization access. | Personalize the user experience |
| **Saved views** | Named sets of personalizations (and, on list pages, filters, sorts and grouping) that you switch between. Can be published to roles and legal entities. | Explicit **Save** / **Save as**. | Create: users with personalization rights. Publish: System administrator or **Saved views administrator** role. | Saved views |

Key consequence for the guide: on a page with a view selector, a user who hides a column or adds a filter and walks away has **not** saved anything; the asterisk (\*) after the view name says so. But column widths and footer totals **are** remembered without a save (see 2.3 and 7.4).

---

## 2. The grid control (new grid)

**Source:** Grid capabilities (ms.date 26 March 2026). The "new grid control" has been **mandatory since 10.0.29**, so every user now has it; the article still says "You must enable the new grid feature to have access to these capabilities" in its description, which is out of date for a current environment. Pages that a developer has opted out with `forceLegacyGrid()` (or that contain a non-React extensible control) fall back to the legacy grid, so the capabilities below may be missing on an odd page; the first time this happens the user gets a message that the page needs to be refreshed.

### 2.1 Grid anatomy, selecting rows, Select all

- **Row selection column**: the first column. Selecting the check box **at the top of the first column** selects or clears all rows in the grid. With grouping on, a check box in each group header row selects or clears the rows in that group, and shows a mixed state when only some are selected.
- **Row status column** (edit mode only): to the right of the row selection column; shows the save state of each row (see 2.7).
- The row selection and row status columns are **always frozen** as the first two columns and can't be reordered.
- **Grid options** button in the grid header (the "⋮" at the right end of the header row in the screenshot): menu holding **Show footer** / **Hide footer**, **Ungroup all**, **Hide group column name**, **Edit selected rows** (bulk edit).
- **Footer**: hidden by default. When shown it can give the number of selected rows (when more than one is selected), calculated values under numeric columns, and the number of rows in the dataset.
- Keyboard: **Ctrl+Shift+M** selects or clears all rows; **Ctrl+Space** or **Ctrl+Click** selects/clears the current row; **Shift+Click** adds a range; **Shift+Space** adds the next/previous row (multi-select grids only). See 2.11.
- When more than one row is selected, the footer calculated values recalculate **for the selected rows only** (10.0.32 improvement).

Gotcha for the guide: there is no documented "Select all rows in the database" control: the header check box selects the rows the grid holds. Export of *all* rows is a separate Export to Excel option (agent C; 260 topic 6).

### 2.2 Sorting

- Click a column header to open the column header drop-down, which has **Sort A to Z** / **Sort Z to A** (labels from the screenshot; for numbers and dates the labels differ, for example smallest to largest; confirm in D365). Single-column sorting only from the header.
- Multi-column sorting: **Advanced filter or sort** (3.8).
- With grouping: changing a grouping column's sort in its header changes the group order; sorting a non-grouped column sorts **inside** each group and keeps the grouping.
- Columns computed by code (display methods) are not filterable or sortable: their header isn't clickable.
- On pages with large view selectors, a sort is part of the view if you save it.

### 2.3 Calculated values in the footer (totals, min, max, average)

**What it is:** a value at the foot of each numeric column, for the whole dataset, for each group (as subtotals) and for the selected rows.

**Calculated values available:** before 10.0.29 only **Total**. From 10.0.29 with **Extended grid aggregation capabilities**: **Minimum**, **Maximum**, **Total**, **Average**. One type per column; each column can have a different type. (The footer itself labels a total **Sum** in Microsoft's screenshot, and shows **Maximum** under a column set to maximum.)

**Steps as documented**

Show the footer:
1. Select **Grid options** in the grid header.
2. Select **Show footer**. (Hide it again with **Hide footer**.) The setting is remembered for that grid until you hide it.

Configure a column, method 1 (shortcut menu):
1. Right-click (or select and hold) in the numeric column.
2. Select **View column totals**, then the calculated value you want (**Minimum**, **Maximum**, **Total**, **Average**). Without the extended feature the option is **Total this column**.
3. Result: the footer becomes visible, the preference is saved, and the calculation runs for this and any other configured columns.

Configure a column, method 2 (footer):
1. With the footer showing, select **Show total** (or **Select calculated value** with the extended feature) in the footer under the column. When no column is configured yet, this button shows in every numeric column; once one column is configured, it appears only on hover or focus (this is the "+" that 260 describes; see section 10).
2. A dash in the footer means the preference is saved but not yet calculated.

Remove a calculated value: right-click in the column and select **Hide total** (or **View column totals > None**), or select **Hide total** (or **Hide calculated value**) in the footer.

Large datasets:
- Dashes under configured columns mean the dataset is too large to calculate automatically. Select **Calculate** in the footer (or use the right-click option again). **Cancel** stops a long calculation.
- Above an organization limit, the user is told to filter the data more. Admin setting: **Maximum number of local records for each grid** on the **Client performance options** page, default **25,000**; Microsoft recommends not more than 50,000 (memory on the user's machine).
- Calculated values update automatically as rows are created, updated or deleted.

**Key concepts / gotchas**
- No column shows a calculated value by default; set-up is a one-time activity, remembered like column widths (restricted personalization, so **no Save is needed**, and on a page with views it is stored per view automatically).
- Only numeric columns.
- With grouping, the same calculated value shows for each group (subtotals).

Shortcuts (10.0.32+): **Alt+T, V** change the type of calculated value for the current column; **Alt+T, F** show/hide the footer; **Alt+T, O** open the grid options menu.

Screenshot: `grid-footer-calculated-values-totals.png` (Aged balances, footer showing "Total / 32 rows", **Sum** 1,450,654.41 and **Maximum** 531,250.00; note the large view selector "Standard view" and the QuickFilter **Filter** box).

### 2.4 Grouping

**What it is:** organise the rows by the values in one or more columns, with header rows per group and subtotals. Feature **Grouping in grids** (mandatory since 10.0.29).

**Steps**
1. Right-click the column to group by and select **Group by this column**. The data is sorted by that column, a **Group by** column is added at the start of the grid, and a header row is inserted at the start of each group.
2. Each group header shows the group value, the column name, the number of rows and any calculated values (subtotals).
3. For more levels, select **Group by this column** on another column. Maximum **5** nested levels.
4. To remove: right-click the column and select **Ungroup**, or **Grid options > Ungroup all**.
5. Expand/collapse a group with the chevron (**>**) in its header row.
6. **Grid options > Hide group column name** hides the column name in group headers.
7. Date/DateTime columns: group by **year**, **month** or **day**; DateTime and Time also by **hour**, **minute**, **second**.

**Gotchas**
- The expanded/collapsed state of groups is **not** saved.
- After grouping on a segment of a date or time column, you can't add another grouping column (Important note in the article).
- Grouping is saved to a view only on pages with a **large view selector** (list pages).

Shortcut (10.0.32+): **Alt+T, G** group/ungroup the current column.

Screenshot: `grid-grouping-with-subtotals.png`.

### 2.5 Freezing columns

Feature **Freezing columns in grids** (mandatory since 10.0.29).

1. Right-click in the column header and select **Freeze column**. The first frozen column becomes the first column and stops scrolling out of view; each further frozen column is added to the right of the last frozen one.
2. Reorder frozen columns with the normal Move personalization, but frozen and unfrozen columns can't be mixed.
3. To undo: right-click the frozen column's header and select **Unfreeze column**.

Shortcut (10.0.32+): **Alt+T, P**.

Screenshot: `grid-freeze-columns.gif` (animated).

### 2.6 Column widths, autofit, stretchable columns

- **Resize:** drag the sizing bar to the left or right of the column header. Remembered automatically (restricted personalization; per view on pages with views).
- **Autofit:** double-click (double-tap) the column's sizing handle, or put focus in the column header and press **A**.
- **Keyboard:** with focus in the header row, **Right arrow / Left arrow** make the current column larger/smaller; **Ctrl+Shift+Right/Left arrow** move the column to the next/previous position.
- **Stretchable columns** (developer setting `WidthMode = SizeToAvailable`): such columns share extra grid width; once a user resizes one manually, it becomes fixed.
- Default sizes come from discrete sizing (XS/S/M/L; grid columns default to 75 % of the input control size). Developer detail only; the user-relevant point is that "the end user decides which columns are most important to view and the ideal viewing width", and the client keeps that preference.

### 2.7 Typing ahead of the system (fast data entry) and row status

**What it is:** in edit mode the grid lets you move to another row, or create new rows, while the server is still validating and saving earlier rows.

Row status column values:

| Status | Meaning | What the user does |
|---|---|---|
| **Blank** | The row is saved. | Nothing. |
| **Processing pending** | Changes queued, not yet saved; text in italics. | Wait for all pending rows before acting outside the grid. |
| **Invalid state** | A warning or message during processing may have stopped the save. Processing of later rows stops until it is resolved. | Move back to the row, or select **Fix this issue**. |
| **Paused** | Validation raised a dialog that needs input; a notification appears. | Select **Resume processing** to see the dialog. |

Differences while ahead of the system: no lookup drop-downs, no field validation on leaving a column, no default values until the server catches up (a value you typed overrides the default). A new row created with **Down arrow** opens all columns as editable, with focus in the first column, which may differ from **New**; reorder columns by personalization so the first column is the one you start typing in.

Shortcuts (10.0.32+): **Alt+T, A** go to the row in an invalid or paused state; **Ctrl+Shift+F5** revert a new unsaved row; **Alt+Del** delete the current row. **Down arrow** from the last row creates a new row.

Developer opt-out exists (`allowPreemptiveClient(false)`); in those grids, pasting from Excel doesn't work.

Screenshot: `grid-typing-ahead-fast-entry.gif`.

Relevance: moderate for finance users (journal line entry), but General journal lines use the segmented entry control, where paste from Excel is not supported (see 2.9).

### 2.8 Bulk edit (Edit selected rows)

Version **10.0.38+**, feature **Bulk editing in grids** (Feature management; not listed as mandatory in the sources).

1. In the grid, select the rows to update.
2. Select **Grid options > Edit selected rows**.
3. In the **Edit rows** dialog, choose the columns (only editable fields) and the new values. The order in the dialog, top to bottom, is the order the columns are updated in, which can affect field validations. Select **Apply**.
4. The grid shows the changes in italics as a preview. Select **Save** to save or **Discard** to cancel.
5. Rows are saved one at a time with all validations (typing-ahead model); check each row's status.

Admin note for the guide: whether this is on, and whether the business wants users to bulk-edit, is a policy question for the PG owner.

### 2.9 Pasting from Excel; copying a range of cells

- **Paste:** copy a table in Excel and paste into a grid in edit mode; pasting starts at the selected cell and overwrites. Extra columns beyond the grid are ignored (user is told). Extra rows are inserted as new rows at the bottom.
- **Limit:** doesn't work in some grids, "for example, in grids using the segmented entry control like General journal lines".
- **Copy:** grids support Excel-like range selection with the keyboard (multiple rows and columns) for copy and paste (10.0.32).
- Not documented: the exact key combination for range selection (Shift+arrow keys is the Excel convention; confirm in D365).

### 2.10 Math expressions in numeric fields

- Start the value with **=**, for example **=15\*4**, then **Tab** (or **Enter**): D365 saves **60**.
- Works in grid cells and, from **10.0.29**, in numeric controls outside the grid.
- Supported operators: Microsoft links to an external library page (math-expression-evaluator "Supported maths symbols"); not reproduced in Learn.

Screenshot: `grid-math-expression.gif`.

### 2.11 Grid keyboard shortcuts (full table from Keyboard shortcuts, ms.date 2026)

| To do this | Press |
|---|---|
| Vertical scrolling | Mouse wheel |
| Horizontal scrolling | Shift + Mouse wheel |
| Move to the next/previous column | Tab / Shift+Tab |
| Move to the next/previous row | Down arrow / Up arrow |
| Move to the next/previous row without selecting (multi-select only) | Ctrl+Up arrow / Ctrl+Down arrow |
| Select/clear the current row (multi-select only) | Ctrl+Space / Ctrl+Click |
| Add the next/previous row to the selected set (multi-select only) | Shift+Space |
| Add a range of rows to the selected set (multi-select only) | Shift+Click |
| Go to the next/previous page of data | Page up / Page down |
| Create a new row at the bottom of the grid | Down arrow (from the last row) |
| Move to the first record | Ctrl+Home |
| Move to the last record | Ctrl+End |
| Select or clear all rows | Ctrl+Shift+M |
| Move to the first marked row | Alt+Shift+M, F |
| Move to the next marked row | Alt+Shift+M, L |
| Move to the previous marked row | Alt+Shift+M, P |
| Move to the last marked row | Alt+Shift+M, N |
| Execute the default action in a grid (focus on a hyperlink cell, all cells in the column are hyperlinks) | Enter |
| Toggle focus between the selected row and the header row | Alt+T,H or Alt+Shift+H |
| Make the current column larger/smaller (focus in header row) | Right arrow / Left arrow |
| Move the current column to the next/previous position (focus in header row) | Ctrl+Shift+Right arrow / Ctrl+Shift+Left arrow |
| Open grid filtering for the current column (focus in header row) | Enter |
| Resize the current column to fit the contents (focus in header row) | A (or double-click the column sizing handle) |
| Open the grid options menu\* | Alt+T, O |
| Change the type of calculated value for the current column\* | Alt+T, V |
| Show/hide the grid footer\* | Alt+T, F |
| Group/ungroup the current column\* | Alt+T, G |
| Freeze/unfreeze the current column\* | Alt+T, P |
| Go to the row in an invalid or paused state (fast data entry)\* | Alt+T, A |
| Revert changes in a newly created but unsaved row\* | Ctrl+Shift+F5 |
| Delete the current row\* | Alt+Del |

\* 10.0.32 and later. Microsoft's table labels "next/previous marked row" with L and P, and "last" with N; reproduced as published (the letters look swapped against the wording, a likely doc error to check in D365).

Related: **Alt+Shift+K** (or right-click > **View shortcuts**) shows the shortcuts available where you are; press it twice for all shortcuts on the page. **Ctrl+Shift+G / D / H / L** switch to grid / details / header / lines view. Key chords such as "Alt+T, O" mean press Alt+T, release, then O.

### 2.12 Things users ask about that Microsoft does not document

I searched the grid, personalization, saved views, shortcut, client FAQ, accessibility and what's-new articles (10.0.29 to 10.0.50) and the 2025 wave 1, 2025 wave 2 and 2026 wave 1 release plans:

- **Wrap text in grid cells / column headers:** not documented. No user setting is described.
- **Find in grid (search within loaded rows):** not documented as a D365 feature. The documented ways to find rows are the QuickFilter, column header filter, Filter pane and Advanced filter. (Browser Ctrl+F only searches what is rendered and is not documented by Microsoft; don't teach it.)
- **Row height / cell size / density:** the only documented control is **User options > Visual**: "Select a color theme and the default size of elements on pages." No per-grid row height.
- **2025 to 2026 changes:** no new end-user grid, filter or view features in 10.0.41 to 10.0.50 or in the 2025 wave 1, 2025 wave 2 or 2026 wave 1 release plans for cross-app capabilities. The changes in that period are in agents/MCP (agent tools can now read and filter grids, including hierarchical grids: 10.0.49), Immersive Home (GA 13 March 2026) and Copilot. The grid, view and filter docs were refreshed (26 March 2026, filtering options 12 March 2026) but describe features from 10.0.29 to 10.0.38. The 2026 wave 2 plan page wasn't available (404); Microsoft says the release-plan pages are archived as of October 2026 and points to the roadmap.

### 2.13 Page views: Grid, Details, Header, Lines

From the Learn training module *Navigate finance and operations apps*, unit "Compare views" (overlaps with navigation agent A): **Grid view** (many records; update several lines without opening each record), **Details view** (one record from a list page), **Header view** and **Line view** (header/lines documents such as sales orders). Shortcuts Ctrl+Shift+G/D/H/L. Relevant here because the views selector differs between the grid part and the details part of the same page (see 7.2). Note the naming clash: these "views" are page layouts, not *saved views*. A guide should say so.

---

## 3. Filtering

**Sources:** Filtering options (developer article, ms.date 12 March 2026; contains the user-facing operator table); Advanced filtering and query syntax (Application User, 9 June 2024); Personalize the user experience; Keyboard shortcuts; Saved views.

### 3.1 The four filtering mechanisms

| Mechanism | What it is | Where | Works on |
|---|---|---|---|
| **Filter pane** | Inline pane with several filter fields at once, operators and **Apply**. | **Show filters** button; slides in from the **left**; closes with **Hide filters** or when you leave the page. Shortcut **Ctrl+F3** or **Alt+M, F**. | Full-page lists: the first primary data source and tables directly joined to it. |
| **QuickFilter** | A **Filter** box above a grid for fast single-column filtering; a column selector drop-down appears as you type. | Above many grids (and in workspace sections). **Enter** applies. | One column at a time; the grid it is attached to. |
| **Grid column header filter** | Excel-like drop-down from a column header with operator, value, **Apply**, **Clear** and sort options. | Click the column header; **Ctrl+G** from a cell; **Enter** with focus in header. | Any filterable column (fields stored in SQL tables). |
| **Advanced filter or sort** | Dialog for complex criteria: columns not on the page, joined tables, multi-column sort. | **Ctrl+Shift+F3**; historically on the Action Pane **Options** tab. Opens the **Inquiry** page in Microsoft's example. | The page query. |

Training module note: Learn's *Use filtering techniques* unit says the Filter pane "slides in from the right ... selecting the system-defined **Show filters** button on the right side"; the current Filtering options article says **left**. Treat the article (2026) as correct and confirm in D365.

Screenshots: `learn-module-filter-pane-and-column-filter.svg` (training module, Filter pane and column filter marked 1 and 2), `quickfilter-column-selector.png`, `grid-column-header-filter.png` (older styling).

### 3.2 Filter operators and how they translate to query syntax

The Filter pane and column header filter show **operators**; the operator implies the query symbols, which aren't shown. **Query symbols only work with the matches operator.** With any other operator they are taken literally: `First name MATCHES A` finds names that start with A; `First name IS A*` finds names literally equal to "A\*".

Table from Filtering options (reproduced as published):

| Filter operator | Finance and operations apps query syntax |
|---|---|
| Is exactly `circle` / Is equal to `circle` | `circle` |
| Is not `circle` / Is not equal to `circle` | `!circle` |
| Is one of `circle`, `square`, `circlesquare` | `circle,square,circlesquare` |
| Contains `circle` | `*circle*` |
| Does not contain `circle` | `!*circle*` |
| Begins with `circle` | `circle*` |
| After `circle` / Greater than `circle` | `>circle` |
| Greater than or equal `circle` | `circle..` |
| Before `circle` / Less than `circle` | `<circle` |
| Less than or equal `circle` | `..circle` |
| Between `square` and `circle` | `square..circle` |

"The client interprets any query syntax that doesn't match the preceding templates as the **matches** operator."

Operator sets depend on the data type (text, number, date, enum); the article doesn't list them per type. The pairs in the table ("Is exactly / Is equal to", "After / Greater than", "Before / Less than") are the text vs number/date labels. **Ends with** and **matches** appear in the D365 UI but not in this table (260 lists "ends with"; confirm in D365).

Other frequent expressions:
- **Blank values:** with **matches** or **is equal to**, type `""`. Finds only empty strings, **not** NULL or 0.
- **"Is not one of":** not an operator; use **matches** with each value negated: `!circle, !square`.
- The operator you last used in a column header filter is remembered for that column (restricted personalization).
- **"Is one of"** uses an improved experience since Platform update 22 (legacy experience removed April 2020).

### 3.3 Advanced query syntax (full table)

From *Advanced filtering and query syntax*. Applies in the **Advanced filter/sort** dialog and with the **matches** operator in the Filter pane or column header filters.

| Syntax | Character description | Description | Example |
|---|---|---|---|
| *value* | Equal to the value that is entered | Type the value to find. | **Smith** finds "Smith". |
| !*value* (exclamation point) | Not equal to the value that is entered | Type an exclamation point and then the value to exclude. | **!Smith** finds all values except "Smith". |
| *from-value*..*to-value* (double period) | Between the two values that are separated by double periods | Type the from-value, then two periods, and then the to-value. | **1..10** finds all values from 1 through 10. However, in a string field, **A..C** finds all values that start with "A" and "B", and values that are exactly equal to "C". For example, this query won't find "Ca". To find all values from "A\*" through "C\*", type **A..D**. |
| ..*value* (double period) | Less than or equal to the value that is entered | Type two periods and then the value. | **..1000** finds any number that is less than or equal to 1000, such as "100", "999.95", and "1,000". |
| *value*.. (double period) | Greater than or equal to the value that is entered | Type the value and then two periods. | **1000..** finds any number that is greater than or equal to 1000, such as "1,000", "1,000.01", and "1,000,000". |
| >*value* (greater than sign) | Greater than the value that is entered | Type a greater than sign (**>**) and then the value. | **>1000** finds any number that is greater than 1000, such as "1000.01", "20,000", and "1,000,000". |
| <*value* (less than sign) | Less than the value that is entered | Type a less than sign (**<**) and then the value. | **<1000** finds any number that is less than 1000, such as "999.99", "1", and "-200". |
| *value*\* (asterisk) | Starting from the value that is entered | Type the starting value and then an asterisk (**\***). | **S\*** finds any string that starts with "S", such as "Stockholm", "Sydney", and "San Francisco". |
| \**value* (asterisk) | Ending with the value that is entered | Type an asterisk and then the ending value. | **\*east** finds any string that ends with "east", such as "Northeast" and "Southeast". |
| \**value*\* (asterisk) | Containing the value that is entered | Type an asterisk, then a value, and then another asterisk. | **\*th\*** finds any string that contains "th", such as "Northeast" and "Southeast". |
| ? (question mark) | Having one or more unknown characters | Type a question mark at the position of the unknown character in the value. | **Sm?th** finds "Smith" and "Smyth". |
| *value*,*value* (comma) | Matching the values that are separated by commas | Type all your criteria, and separate them by using commas. | **A, D, F, G** finds exactly "A", "D", "F", and "G". **10, 20, 30, 100** finds exactly "10, 20, 30, 100". |
| "" (two double quotes) | Matching a blank value | Type two consecutive double quotes to filter for blank values in that field. | Two consecutive double quotes (**""**) finds rows with no value for the current column. |
| (*Finance and operations query*) (query between parentheses) | Matching a defined query | Type a query as an SQL statement between parentheses using the finance and operations query language. | **((AccountNum LIKE "US\*") && (DirPartyTable.Name LIKE "Cont\*"))** as an example of a filter condition on a field from the root data source and a field from another data source (All customers page). |
| T | Today's date | Type **T**. | **T** matches today's date. |
| (methodName(parameters)) (**SysQueryRangeUtil** method between parentheses) | Matching the value or range of values that are specified by the parameters of the **SysQueryRangeUtil** method | Type a **SysQueryRangeUtil** method that has parameters that specify the value or range of values. | 1. Click **Accounts receivable > Invoices > Open customer invoices**. 2. Press **Ctrl+Shift+F3** to open the **Inquiry** page. 3. On the **Range** tab, click **Add**. 4. In the **Table** field, select **Open customer transactions**. 5. In the **Field** field, select **Due date**. 6. In the **Criteria** field, enter **(yearRange(-2,0))**. 7. Click **OK**. The list shows invoices due in the previous two years. |

Notes:
- "?" is documented as "one or more unknown characters" but the example (Sm?th) shows a single character. 260 says "? represents one character". The example supports 260; the wording is Microsoft's. Flag for the D365 test.
- **T** for today also works in date fields; in a date field **D** enters the session date and **T** the current date (Input control shortcuts). In the date picker, **T** picks today, **C** clears, **N** picks Never (max date).

### 3.4 Relative date queries (SysQueryRangeUtil methods, full table)

| Method | Description | Example |
|---|---|---|
| Day (_relativeDays=0) | Find a date relative to the session date. Positive values indicate future dates, and negative values indicate past dates. | **Tomorrow**: **(Day(1))**. **Today**: **(Day(0))**. **Yesterday**: **(Day(-1))**. |
| DayRange (_relativeDaysFrom=0, _relativeDaysTo=0) | Find a range of dates relative to the session date. Positive values indicate future dates, and negative values indicate past dates. | **Last 30 days**: **(DayRange(-30,0))**. **Previous 30 days and next 30 days**: **(DayRange(-30,30))**. |
| GreaterThanDate (_relativeDays=0), GreaterThanUtcDate (_relativeDays=0) | Find all dates after the specified relative date. | **More than 30 days from now**: **(GreaterThanDate(30))**. |
| GreaterThanUtcNow () | Find all date/time entries after the current time. | **All future date/times**: **(GreaterThanUtcNow())**. |
| LessThanDate (_relativeDays=0), LessThanUtcDate (_relativeDays=0) | Find all dates before the specified relative date. | **Less than seven days from now**: **(LessThanDate(7))**. |
| LessThanUtcNow () | Find all date/time entries before the current time. | **All past date/times**: **(LessThanUtcNow())**. |
| MonthRange (_relativeFrom=0, _relativeTo=0) | Find a range of dates, based on months relative to the current month. | **Previous two months**: **(MonthRange(-2,0))**. **Next three months**: **(MonthRange(0,3))**. |
| YearRange (_relativeFrom=0, _relativeTo=0) | Find a range of dates, based on years relative to the current year. | **Next year**: **(YearRange(0, 1))**. **Previous year**: **(YearRange(-1,0))**. |

Further relative values from *Build forms that fully utilize saved views* (usable by users with the **matches** operator):

| Description | Filter value |
|---|---|
| Current user | (currentUserId()) |
| Current legal entity | (currentCompany()) |
| Today | (Day(0)) |
| Yesterday | (Day(-1)) |

**Why this matters for saved views (key tip for the guide):** a filter with a fixed date (for example due date ≤ 30/11/2026) saved in a view keeps that date for ever. A relative filter in parentheses, such as `(DayRange(-30,0))` or `(LessThanDate(0))`, is evaluated each time the view runs, so the view stays current and can be shared. Microsoft: "Users in the user interface can use this same syntax with the 'matches' operator to achieve the same effect." The Day-based methods use the **session date** (which a user can change on the dashboard date picker; agent A).

### 3.5 Filter pane

- Open: **Show filters** (left side of the page) or **Ctrl+F3** / **Alt+M, F** (also switches focus between pane and page). Close: **Hide filters**, **Esc** with focus in the pane, or leave the page.
- Use: for each field choose an operator (list depends on data type), enter a value, select **Apply**.
- **Add a filter field**: adds any filterable field from the page's first master data source, including fields not shown in the grid. **Recommended fields** (fields others in the organization added) also appear when adding filter fields, refreshed by the **Recommendation batch job**.
- Initial fields: existing (non-hidden) ranges on the query; otherwise the primary index fields; otherwise the table's title fields.
- Some filters can be **Locked** (visible, not changeable) or **Hidden** by the developer.
- Not available on: drop dialogs, dialogs, enhanced previews, lookups, page parts, parts, table-of-contents pages, pages with no data source.
- Doesn't filter secondary collections (for example, lines grids under a header). Use the QuickFilter or column header filter there.
- Not documented in the article: the **Reset** button in the pane (exists in the product; confirm label in D365).

### 3.6 QuickFilter

- Type in the **Filter** box above the grid; a column selector drop-down shows which column the value applies to; choose the column and press **Enter**.
- The default column is set by the developer or is the first filterable column. The column you last chose is remembered (restricted personalization).
- No column selector means the QuickFilter isn't tied to a grid, or no columns are filterable (images and display methods aren't).
- Workspace sections often have a QuickFilter-style free-text **Filter** field (section 5).

### 3.7 Grid column header filtering and sorting

1. Select a column header (or **Ctrl+G** from a cell in that column, or **Enter** with focus in the header row). Focus goes straight to the filter value field.
2. Choose the operator (the drop-down next to the field name, for example **is**), type the value, press **Enter** or select **Apply**. **Clear** removes this column's filter.
3. **Sort A to Z** / **Sort Z to A** at the top of the drop-down.
4. Close with **Esc**.
- Columns whose values are computed by code can't be filtered or sorted: their header isn't clickable.
- Inside lookups, the column header filter is the way to search on anything other than "begins with ID or name" (section 4).

Screenshot: `grid-column-header-filter.png` (legacy look: **Sort A to Z**, **Sort Z to A**, *Last name* **is** drop-down, value box, **Apply**, **Clear**).

### 3.8 Advanced filter or sort (Ctrl+Shift+F3)

- Opens a dialog for "filter on columns (not on the form), join additional data sources, and sort by multiple columns". In Microsoft's worked example it is called the **Inquiry** page, with a **Range** tab (**Add**, **Table**, **Field**, **Criteria**) and **OK**. A **Sorting** tab is implied by "sort by multiple columns" but not described.
- Accepts the full query syntax (3.3, 3.4) in **Criteria**.
- Microsoft calls the feature "Advanced filter or sort" (Filtering options) and "Advanced filter/sort" (Advanced filtering article); the menu label, historically **Advanced filter or sort** on the Action Pane **Options** tab under **Page options**, is not in the current articles. Confirm in D365.
- Gotcha: the dialog uses table and field names that may differ from page labels.

### 3.9 Clearing filters

What is documented:
- Column header filter: **Clear** in the drop-down.
- Filter pane: change or remove values and **Apply** (the pane's reset control isn't described).
- Saved views: switching to another view (or back to **Standard**) reloads that view's query; unsaved filter changes show as an asterisk and are discarded when you switch.
- A tile opens a page with the tile's query; a menu item with its own query (for example **Customers on hold**) overrides the default view's query.

Not documented: a single "clear all filters" command. Reverting to the saved view is the practical route.

### 3.10 Filtering on dimensions

- No Microsoft end-user article covers filtering list pages by financial dimensions. Learn search returned nothing for it.
- What applies by inference: financial dimension columns shown in a grid can be filtered like other columns if they are stored fields; a ledger account combination ("segmented entry") column such as journal line **Account** uses the segmented entry control (its own shortcuts: **Alt+W** switches "Show valid"/"Show all") and doesn't support paste from Excel. The **matches** operator with `*` patterns on the display value (for example `*-110-*`) is a common practice but isn't documented by Microsoft.
- **Inventory dimensions** (not finance, but documented): the **Display dimensions** setting overrides personalization of inventory dimension columns on every page; hide a dimension there, not by personalization.
- Recommendation: treat dimension filtering as a clean-session D365 test item, and an SME/PG-owner item if the guide wants a worked R2R example.

### 3.11 Filtering shortcuts

| To do this | Press |
|---|---|
| Open grid filtering for the current column | Ctrl+G |
| Close grid filtering for the current column | Esc |
| Open the Filter pane (or switch focus between the Filter pane and the main page if it is already open) | Alt+M, F, or Ctrl+F3 |
| Close the Filter pane (focus in the Filter pane) | Esc |
| Open advanced filtering/sort | Ctrl+Shift+F3 |
| Apply the Quick Filter (focus in Quick Filter) | Enter |
| Apply the grid filter (focus in the filter field of the column header) | Enter |
| Move focus to the page content (focus in the Filter pane) | Alt+M, M, or Ctrl+F3 |

---

## 4. Lookups (as they relate to finding and filtering)

**Source:** Find information by using lookups (Application User); Contextual data entry for lookups (developer, appendix of scenarios); Keyboard shortcuts.

- **Responsive lookups:** the lookup opens automatically after a short pause in typing, filtered to values that **begin with** what you typed. The cursor stays in the field; **Up/Down arrow** move through the list; **Enter** selects. Typing an asterisk (\*) to open the lookup is **deprecated**.
- **Typing a name instead of an ID** (contextual data entry; many but not all lookups): for example, type "Forest Wholesales" instead of "US-003" in **Customer account**. The **Name** column moves first and the list sorts and filters by name. Behaviour: a full ID is taken as is; a full unique name is converted to its ID; a unique partial ID or name ("Micro") is completed; several matches open a disambiguation lookup; no choice means validation fails.
- **Advanced search in a lookup:** when "begins with" isn't enough (for example item names containing "cable"), clear the field, open the lookup, then filter with the **grid column header** in the lookup. Keyboard: **Alt+Down arrow** opens the lookup; **Alt+Down arrow** again moves focus into it; **Tab** to the column; **Ctrl+G** opens the column header filter.
- **Enter** opens a lookup or combo box when the feature **Standardize keyboard interaction for combo box and lookup controls** is on (GA in 10.0.30); otherwise **Alt+Down arrow**. **Align combo box interactions with lookup controls** is mandatory since 10.0.29.
- **Alt+Up arrow** opens the control's enhanced preview (hover card); **Ctrl+Enter** opens the hyperlink (View details).
- Lookups, drop dialogs and enhanced previews **don't support saved views** or the Filter pane.

Getting Started relevance: high. Every O2C/P2P/R2R user enters customer, vendor and main account values; "type the name" and "filter inside the lookup" are big time-savers.

---

## 5. Workspaces: configure, filter, add to, tiles and the dashboard

**Sources:** Configure and filter workspaces; Personalize the user experience; Saved views; Default dashboard; Immersive Home overview; training module unit "See how workspaces drive productivity".

### 5.1 Configure a workspace

Some workspaces have an Action Pane button that opens a configuration dialog of predefined settings for the whole workspace (settings vary by workspace). Microsoft gives no example label; in finance workspaces this is typically **Configure my workspace** (for example Collections coordinator, Vendor invoice entry). Confirm per workspace; the specific settings belong in each process guide.

### 5.2 Filter a workspace

- **Workspace-wide filter**: top left of the workspace; a drop-down whose value filters all content. Screenshot `workspace-wide-filter-expanded.png`.
- **Section filters**: per section (tab/list), often a free-text **Filter** field. Screenshot `workspace-section-filters.png`.
- Filters can be lookups, combo boxes or text fields; all behave the same way.

### 5.3 Add to workspace (list, tile or link)

Path: **Options** tab of the Action Pane > **Personalize** group > **Add to workspace** (on some list pages).

1. Filter and sort the list as you want it shown. If the page has a large view selector, **save it to a view** first (with saved views on, the workspace element is linked to the view: its query feeds the workspace and opening it opens the page in that view; updating the view updates the element).
2. Select **Add to workspace**, choose the **Workspace**, choose **Presentation**: **List**, **Tile** or **Link**.
3. Select **Configure**:
   - **List:** choose the columns and the label.
   - **Tile:** label, whether to **show a count**, and one of four tile sizes (changeable later in the workspace).
   - **Link:** label and optionally a section label (a new section is created if needed).
   - With **Saved views support for workspaces** on: choose the workspace view in **Workspace options**.
4. Open the workspace and rearrange elements as needed.

Screenshot: `personalize-add-to-workspace-dialog.png`.

### 5.4 Tiles: pin to dashboard, change size

- **Pin to dashboard:** in a workspace, right-click a count tile > **Personalize** (the property window title shows **Personalize: <tile name>**) > **Pin to dashboard**. The count appears under that workspace's tile on the dashboard after it refreshes; clear the check box to remove it. The same text appears in the Immersive Home article for its **Workspaces** area.
- **Tile size:** right-click a non-KPI tile > **Personalize** > **Tile size**. Feature **Allow users to select and change tile sizes** (on by default since 10.0.29). With workspace views, the size can be saved to a workspace view.
- **Alt+Up arrow** on a count tile shows its refresh information. (Tile counts may be cached; developer article "Tile and list caching for workspaces".)

### 5.5 Personalize the dashboard

- The dashboard can be personalized like any page (hide, move, rename tiles). It doesn't support saved views.
- **Add a workspace** (right-click an element; when **Full-page apps** is off) creates a new, empty personal workspace tile at the bottom, which you rename and then fill with **Add to workspace**. With **Full-page apps** on, it is **Add an app**, then choose a new workspace, a Power Apps app or a website.
- Published workspace views appear as new dashboard tiles, not in the original workspace's view selector.
- Immersive Home (feature **Immersive Home**, GA March 2026) may replace the classic dashboard as the start page; its Workspaces area ranks workspaces and shows pinned counts. Agent A covers it.

Screenshot: `default-dashboard.png`, `learn-module-customer-invoicing-workspace.svg` (training module: summary tiles, Filter box, tabbed lists, Links).

### 5.6 Navigation pane personalization

Documented only as restricted personalization: the navigation pane's pinned/collapsed state is remembered (**Expand the navigation pane** button; **Alt+F1** toggles open/pinned/closed). Favorites (**Shift+F** with focus on a page in the pane) are 260 topic 3 / agent A. No other navigation pane personalization is documented.

---

## 6. Personalization

**Source:** Personalize the user experience (ms.date 26 March 2026) unless stated.

### 6.1 User options (system-wide settings)

Path: **Settings** (gear) on the navigation bar > **User options**. Tabs:

| Tab | Holds |
|---|---|
| **Visual** | Colour theme; default size of elements on pages. |
| **Preferences** | Default company, initial page, default view/edit mode, language, time zone, date/time/number formats, miscellaneous preferences that vary by release. |
| **Account** | User name and account options. |
| **Workflow** | Workflow options (agent D). |
| **Personalization** | Your personalizations to pages: view, manage, **Export**; reset feature callouts. |

Action Pane **Usage data**: view and delete your usage data and personalizations. Agent A likely covers Visual/Preferences; the **Personalization** tab and **Usage data** belong here.

### 6.2 Restricted personalization (remembered automatically)

No save action. List as documented:

- **Grid column widths.**
- **Grid footer and column totals** (new grid only).
- **FastTabs** expanded/collapsed (collapsing can improve performance because data isn't fetched until expanded). FastTab order can also be changed (full personalization).
- **FactBoxes** and the **Related information** pane expanded/collapsed (same performance note).
- **Action Panes** pinned open or collapsed; if pinned, the last tab used is shown.
- **QuickFilters**: the column last filtered on.
- **Column header filters**: the operator last used per column.
- **Navigation pane** pinned or collapsed.

On pages with saved views these are saved to the **current view automatically, even locked views** (Standard, published).

### 6.3 Full personalization: right-click (shortcut menu) options

Right-click a column header: **Insert columns**, **Hide this column**, and the grid options from section 2 (**Group by this column**, **Freeze column**, **View column totals**). Right-click an element: **Personalize** opens its property window. **Shift+F10** simulates a right-click; **Ctrl+F10** opens the context menu.

### 6.4 The element property window (Personalize)

Right-click an element > **Personalize** (title "Personalize: <element>"). Options:
- Change the element's **label** (rename).
- **Hide** the element (data is not deleted).
- Include it in the FastTab **summary** section (if on a FastTab).
- **Skip** it in the tab sequence.
- Prevent editing (**lock**) for any record.
- Make it **required** (red border and asterisk). Feature **Designate fields as required using personalization** (mandatory since 10.0.29).
- Element-specific extras: **Pin to dashboard** and **Tile size** for tiles; **Add a workspace** / **Add an app** on the dashboard.
- **Personalize this page** opens the toolbar.

Screenshot: `personalize-element-property-window.png`.

Gotcha: there is no documented personalization to change a numeric field's "Total" behaviour other than the grid footer calculated value (2.3). The brief's "editing field 'Total' options" equals **View column totals** / **Select calculated value**.

### 6.5 The Personalization toolbar

Open with any of:
- **Ctrl+Shift+P** from any element.
- **Personalize this page** in an element's property window.
- Action Pane **Options** tab > **Personalize** group > **Personalize this page**.
- **Settings** (gear) on the navigation bar > **Personalize**.

While open, the page is read-only but you can still switch tabs and expand/collapse sections; hover or focus on a section shows a button to personalize that section (for example to hide a FastTab).

| Tool (label in the article) | Label in Microsoft's toolbar screenshot | What it does |
|---|---|---|
| **Select** | Select | Select an element to open its property window. Some properties may be unavailable (you can't lock a required field). |
| **Hide** | Hide | Hide an element. Hidden elements show in a shaded container while the tool is active; select one to show it again. |
| **Add fields** | **Add a field** | Select the grid or section first; a dialog lists fields that belong to the page definition, under **Recommended fields** (added by others, refreshed by the **Recommendation batch job**) or **All fields**. Select fields and **Update**. To remove an added field, clear it in the same dialog. New fields need custom fields (section 8). |
| **Move** | Move | Drag an element within its parent group; drop zones show as coloured bold lines. Can't move outside the parent group. Keyboard: Tab/arrows then Space/Enter. |
| **Skip** | Skip | Remove from or add to the tab sequence. |
| **Show in header** | Show in header | Add/remove a field in the FastTab summary. |
| **Require** | (under "…") | Make an element required. |
| **Lock** | Lock | Make an element editable or not editable. A padlock marks fields that can't be locked. |
| **Add an app** / **Add an app from Power Apps** | (under "…") | Embed a Power Apps or third-party app (the Power Apps-only variant appears only when Saved views is off, which can no longer happen since 10.0.29). |
| **Clear** | (under "…") | Reset to default. Applies to **the current view** on pages with views, or all personalizations on the page otherwise. **Can't be undone.** |
| **Import** | (under "…") | Load a personalization file; it becomes a view. If a view with the same name exists: skip, replace or rename. |
| **Export** | (under "…") | Save the current view to a file to share. |
| **Close** | Close | Close the toolbar. |

Key rule: "When you use the **Personalization** toolbar, you must explicitly save personalizations to a view for them to be persisted." A padlock next to an element means that property can't be changed for it.

Screenshot: `personalization-toolbar.png` (tools Select, Hide, Add a field, Move, Skip, Show in header, Lock, "…", Close; the Move help text "Select an element and drag to a new location, or use tab and the arrow keys to choose the new location and space/enter to confirm.").

### 6.6 Personalization keyboard shortcuts

| To do this | Press |
|---|---|
| Transition the page into personalization mode | Ctrl+Shift+P |
| Use the Select tool | S |
| Open the selected control's quick personalization dialog box (Select tool) | Space or Enter |
| Use the Move tool | M |
| Select the current control to move (Move tool) | Space or Enter |
| Clear the control to move (Move tool) | Esc |
| Move the selected control to the next position | Tab or Right arrow or Down arrow |
| Move the selected control to the previous position | Shift+Tab or Left arrow or Up arrow |
| Use the Hide tool | H |
| Switch whether the current control is visible or hidden (Hide tool) | Space or Enter |
| Use the Skip tool | K |
| Switch whether the current control is in the tab sequence (Skip tool) | Space or Enter |
| Use the Edit tool | E |
| Switch whether the current control is editable or read-only (Edit tool) | Space or Enter |
| Use the Summary tool | U |
| Switch whether the current control is a summary field in the current FastTab (Summary tool) | Space or Enter |
| Use the Add tool | A |
| Select the control whose container is used to insert the new fields (Add tool) | Space or Enter |
| Import a personalization | I |
| Export a personalization | X |
| Clear this page's personalizations | Ctrl+C |
| Move focus between the personalization toolbar and the page | T |
| Exit personalization mode | Esc |

Note the shortcut table calls the Lock tool **Edit** and the Show in header tool **Summary** (older names).

### 6.7 Clearing / resetting personalization

| Scope | How | Who |
|---|---|---|
| One view or one page (no views) | Personalization toolbar > **Clear** (Ctrl+C in personalization mode). Irreversible. | User |
| Revert unsaved view changes | Switch to another view, or back to the saved one; the asterisk changes are discarded. | User |
| Delete a personal view | View selector > **More** > **Manage my views** > **Delete** > **Update**. Irreversible. | User |
| Your personalizations on all pages | **Settings > User options > Personalization** tab: view, manage, export or delete them. **Usage data** on the Action Pane. | User |
| Reset feature callouts | **User options > Personalization** tab. | User or admin (User settings) |
| All personalizations for one user | **System administration > Setup > Personalization > User settings**: delete all for that user. | Admin |
| Turn personalization off for a user (system-wide or per page) | Same page, **User settings**. | Admin |
| Turn personalization off for everyone (temporarily) | **System settings**: all pages reset to default; turning it back on reapplies personalizations. | Admin |
| Permanently delete all personalizations for all users | **System settings**. Irreversible; export first. | Admin |

### 6.8 Sharing personalizations

Microsoft's order of preference:
1. **Publish views** to security roles and legal entities (7.7).
2. **Copy** views or personalizations to users (admin): **System administration > Setup > Personalization**.
   - Personal views: **Personal views** > select views > **Copy to users** > select users.
   - Pages without views: **User settings** > select the user > **Manage all personalizations** > select > **Copy to users** > select users.
3. **Export and import**:
   - Export your own: Personalization toolbar > **Export**, or **Settings > User options > Personalization** > select > **Export**.
   - Admin export for another user: **System administration > Setup > Personalization > Users** tab > select user > select personalization > **Export**.
   - Import your own: Personalization toolbar > **Import**.
   - Admin import to many users: **System administration > Setup > Personalization** > Action Pane **Import views > User views** > import mode **Select specific users** or **Import as-is** > **Browse** > **Next** > (select users) > **Import** > resolve conflicts.
   - **Important:** don't re-import personalizations after a service update; they persist.

Gotcha: an admin applying personalizations to a user **without** personalization rights has no effect.

### 6.9 Administration: the Personalization page

Path: **System administration > Setup > Personalization**. Access: System administrators and **Saved views administrator**. Sections: **Published views**, **Unpublished views** (with **Quick publish**, 10.0.12), **Personal views** (publish, copy to users, export, delete), **User settings** (rights per user or page, view/delete a user's personalizations, reset callouts), **System settings** (turn personalization off for all users; delete all). **Import views** on the Action Pane (personal or organization views; **Publish immediately** for organization views). Admin content: the Getting Started guide should only say that standard views can be published by the system administrators and that requests go to the BAU Support team (CLAUDE.md D-083: don't name security roles in the guide; the **Saved views administrator** role name is for the register, not the reader).

### 6.10 Personalization across service updates; inventory dimensions

- Personalizations and views survive updates; no reset needed. Exceptions: a control removed from the form, or a change to the form's base query that no longer matches the view query.
- Inventory dimensions: **Display dimensions** settings override personalization of dimension columns on every page.

---

## 7. Saved views

**Source:** Saved views (ms.date 26 March 2026), Build forms that fully utilize saved views (developer), Personalize the user experience. The **Saved views** feature has been **mandatory since 10.0.29** (with **Improved legal entity support for saved views**, also mandatory). **Saved views support for dialogs** is on by default (10.0.29). **Saved views support for workspaces** is a separate Feature management feature. **Saved views performance enhancement** (10.0.29) loads the default view's query more efficiently.

### 7.1 What a view is, and views vs personalization

- Several **named** sets of personalizations per page, to switch between for different tasks.
- On list pages a view also holds **user filters, sorts and grouping**.
- Can be published to roles and legal entities; users then get them even without personalization rights.
- **Not saved automatically**: explicit save. Page-usage items (column widths, FastTab state, footer totals) **are** saved automatically, per view.
- Can be added to workspaces as tiles, lists or links (5.3).
- Personalizations on FactBoxes and form parts inside a page belong to that page's view (not shared with other pages that use the same part, which is how classic personalization behaved).
- On master/details pages (for example **All customers**), the grid part and the details part have **separate** view selectors and views; only the grid views hold filters.

### 7.2 Large vs small view selectors; what pages support views

| Selector | Where | What a view can hold |
|---|---|---|
| **Large** | Pages that feature a list (list pages, simple lists, the grid part of master/details pages, task single/double pages) | Personalizations **plus** filters, sorts and grouping |
| **Small** (next to the page caption) | All other full-screen pages except workspaces and the dashboard | Personalizations only |

Not supported: dashboards; drop dialogs, lookups, enhanced previews. Workspaces only with **Saved views support for workspaces**. Dialogs with **Saved views support for dialogs**.

### 7.3 The view selector

Select the view name (top of the page; for example "Standard view" with a chevron in the screenshot) to open it. Up to two sections: views for the current legal entity (only shown if there are any), then views for all legal entities.

| Entry | Meaning |
|---|---|
| **Standard** view | The out-of-box view, no personalizations. Locked. |
| Personal views (no padlock) | Views you created or an administrator gave you. Editable. |
| Locked views (padlock) | **Standard** and views published to your role. Can't be edited, but usage items (widths, FastTabs) still save; **Save as** makes a personal copy. |
| New views (spark symbol) | Published views you haven't opened yet. |

Switch by selecting the view in the selector.

### 7.4 Create and modify views

An **asterisk (\*)** after the view name means unsaved changes.

1. Select the view name to open the view selector.
2. To update the current view: **Save** (not available for locked views).
3. To create a new view:
   1. **Save as**.
   2. In the **Save view as** pane, enter a **name** and optionally a **description**.
   3. Optionally **Pin as default**.
   4. Optionally limit the view to a subset of **legal entities** (default: global).
   5. **Save**.

You can create the view before or after making the changes.

### 7.5 Default view (Pin as default) and legal entities

1. Switch to the view.
2. Open the view selector.
3. **More** > **Pin as default**.

Or set **Pin as default** in **Save as**.

- A legal-entity-specific view becomes the default for those legal entities.
- A global view becomes the default for legal entities that have no legal-entity-specific default.
- In **Manage my views**, **Pin as default** on a view in **Global views** asks whether it is the default for the **current legal entity** or **all legal entities**.

**Warning (why the default view sometimes doesn't apply):** if you open the page from a **tile**, the tile's query runs; if the entry point (menu item) carries its own query (secondary list pages such as **Customers on hold**), that query runs instead and an informational message offers an action to load the default view's query. Switching views after the page loads runs the view's query normally.

### 7.6 Manage my views

View selector > **More** > **Manage my views**. **My views** section (legal entity sections plus **Global views**). Actions: **Pin as default**, **Move up** / **Move down** (order in the selector), **Rename** (personal views only), **Delete** (permanent). Changes take effect on **Update**.

Users with publish rights also see an **Organization views** tab (7.8).

### 7.7 Publishing views (admin)

Who: System administrators by default, and users with the **Saved views administrator** role (D-083: don't name roles in a user guide).

1. Create and save a personal view.
2. With it loaded, open the view selector > **More** > **Publish**.
3. Enter a **Name** (unique among published views for the page). Optional **Translations** and default language.
4. Optional **description**.
5. Choose whether it is published **as the default view**. Notes: default for all legal entities overrides any legal-entity default the user set; to a subset of legal entities changes those defaults for every targeted user; with several defaults published to a user's roles, the last published wins; **publishing doesn't work for role assignments made through Microsoft Entra groups**. Users can still change their default afterwards.
6. Add **security roles**; optionally **Include child roles**.
7. Add **legal entities**.
8. **Publish**. Can take up to an hour to appear.

Users who get a published view see it locked, with a spark until opened; new users in those roles get it automatically; users who leave the role lose it.

### 7.8 Modify, republish, unpublish

- Change only parameters: switch to the view > view selector > **Republish** (10.0.12 and earlier: **Publish** then **Yes**) > update > **Publish**.
- Change contents: load the view, make changes, **Republish** > **Yes** (publish with unsaved changes) > **Publish**.
- **Manage my views > Organization views** tab: **Republish**, **Publish**, **Unpublish** (inactive, kept), **Save as personal**, **Delete** (removes for all users; takes effect on **Save**).

### 7.9 Managing views globally

**System administration > Setup > Personalization** (section 6.9): **Published views**, **Unpublished views**, **Personal views**, **User settings**, **System settings**, **Import views**.

### 7.10 Import and export of views

- User: Personalization toolbar > **Export** (the current view to a file) / **Import** (becomes a view; skip / replace / rename on a name clash).
- **User options > Personalization**: select and **Export**.
- Admin: Personalization page > **Import views** > **User views** (to selected users or as-is) or organization views (**Publish immediately**); **Export** from Published/Unpublished/Personal views.
- Moving custom fields between environments includes exporting/importing the personalizations that show them (section 8).

### 7.11 Known limitations and FAQ (as documented)

- **Why can't I save filters with this view?** The page has a small view selector (no queries in views), or the page ignores the view query or uses a temporary table.
- **What data do I see?** Small selector: the usual data. Large selector: the default view's query, except from a tile (tile query; a tile created after views were enabled opens its view) or an entry point with its own query (message shown).
- Published workspace views appear as dashboard tiles, not in the workspace's selector.
- Publishing ignores roles assigned through Microsoft Entra groups.
- Up to an hour for published views to appear.
- A view with hard-coded filter values (a fixed date, user or company) may give wrong results or errors when shared; use relative values in parentheses (3.4).
- Grouping is saved only on large-selector pages; group expand/collapse state isn't saved.
- Developers can opt a form out of views (`disableSavedViewsOnForm()`); then there is no selector.
- Microsoft plans to replace secondary list pages (for example **Customers on hold**) with views and may rename captions such as "All customers" to "Customers" to avoid confusion with view names.

---

## 8. Custom fields (user-defined fields), high level

**Source:** Create and work with custom fields.

- Lets an authorised user add a new field to a table from the UI, then place it on a page through personalization. **Only users with special permissions**: System administrators by default, or the **Runtime customization power user** role (register only; D-083). Everyone else can see and use fields others added.
- Steps as documented: open the page > Personalization toolbar (the article says **Options > Personalize this form**, then **Insert > Field**; the current toolbar has **Add fields**/**Add a field**) > select the region > check the field isn't already in the list > **Create new field** (missing button = no permission) > choose the **table**, the **data type** (checkbox, date, date time, decimal, number, picklist, text; length for text, values for picklist), **name**, **label**, **help text** > **Save** or **Save and new** > back in **Insert fields**, **Insert** > optionally **Move**.
- Limit: **20 custom fields per table**. Only some table groups (Group, WorksheetHeader, Main, Miscellaneous, Parameter, Reference, TransactionHeader), not extended, system or temporary tables.
- Read-only tables make custom fields read-only too.
- Sharing: publish a saved view that includes the field (recommended) or export/import personalizations.
- Management: **Custom fields** page (System administration): view, edit label/help text/length only (not name or type), add/reorder picklist values (can't remove), expose on **data entities** (Entities > **Edit** > **Enabled** > **Apply changes**), **Translations**, **Delete** (permanently deletes the data; irreversible).
- Moving between environments: recreate manually, then export/import the personalizations.

Getting Started relevance: low (awareness only: "if you need a field that doesn't exist, ask the BAU Support team"). Not end-user content.

---

## 9. Feature management names and version notes (consolidated)

| Feature (Feature management name as published) | Version | State in sources | What it gives users |
|---|---|---|---|
| **New grid control** | PU33 / 10.0.x | **Mandatory** (10.0.29) | All of section 2 |
| **Grouping in grids** | | **Mandatory** (10.0.29) | 2.4 |
| **Freezing columns in grids** | | **Mandatory** (10.0.29) | 2.5 |
| **Extended grid aggregation capabilities** | 10.0.29 | Feature management (not listed as mandatory) | Min/Max/Average in footer; **View column totals** label |
| (Improvements to the grid control) | 10.0.32 | Default | Range copy, keyboard improvements, aggregates for selected rows, Alt+T shortcuts |
| New grid support for grouped and multi-column card lists | 10.0.30 | On by default | Fewer pages fall back to legacy grid |
| **Bulk editing in grids** | 10.0.38 | Feature management | **Edit selected rows** |
| Evaluating math expressions outside the grid | 10.0.29 | Default | 2.10 |
| **Saved views** | 10.0.x | **Mandatory** (10.0.29) | Section 7 |
| **Improved legal entity support for saved views** | | **Mandatory** (10.0.29) | Legal-entity-specific views and defaults |
| **Saved views support for dialogs** | | On by default (10.0.29) | Views in dialogs |
| **Saved views support for workspaces** | | Feature management | Workspace views; published workspace views as dashboard tiles |
| **Saved views performance enhancement** | 10.0.29 | Feature management | Faster default view loading |
| Extension methods for default queries with views | 10.0.32 | Default (developer) | Fewer "default view query not loaded" messages |
| **Designate fields as required using personalization** | | **Mandatory** (10.0.29) | **Require** tool |
| **Allow users to select and change tile sizes** | | On by default (10.0.29) | **Tile size** |
| **Full-page apps** | | Feature management | **Add an app** on dashboard |
| **Align combo box interactions with lookup controls** | | **Mandatory** (10.0.29) | Consistent combo box/lookup behaviour |
| **Standardize keyboard interaction for combo box and lookup controls** | GA 10.0.30 | Feature management | **Enter** opens lookups/combo boxes |
| **Streamline tabbing behavior in full-page forms** | 10.0.26 | On by default (10.0.29) | Tab through all page regions |
| **Immersive Home** | GA March 2026 | Feature management | New start page (agent A) |
| Legacy "is one of" filtering | PU22 | Removed April 2020 | Improved "is one of" only |
| Legacy default action behaviour | PU21 | Removed April 2020 | "Sticky" default action (hyperlink column follows reordering) |

Admin settings mentioned: **Client performance options** > **Maximum number of local records for each grid** (default 25,000; recommended ≤ 50,000); **Recommendation batch job** (Recommended fields); **System administration > Setup > Personalization**; **Custom fields** page.

What's new 10.0.41 to 10.0.50 and release plans 2025 wave 1, 2025 wave 2 and 2026 wave 1 contain **no** end-user changes to grids, filters, personalization or views (only agent/MCP tools that operate grids and filters, Immersive Home and Copilot).

---

## 10. Comparison with 260 O2C Getting Started (v0.2)

260 covers: switch legal entity (two ways), Favorites, 4. Create a Personalized View (4.1 arrange columns, 4.2 filter, 4.3 footer total, 4.4 save and pin), 5. Update a Saved View, 6. Export All Rows from a Grid, plus Key concepts "What a view contains" and "Filter operators".

### 10.1 Where Microsoft refines or contradicts 260

| 260 says | Microsoft documents | Suggested handling |
|---|---|---|
| 4.3: hover over the column footer until "+" appears, click **+**, open **Calculate column** options, select **Sum**. | Footer button is **Show total** or, with Extended grid aggregation, **Select calculated value**; right-click option **View column totals** > **Minimum / Maximum / Total / Average** (or **Total this column**). The footer label in Microsoft's screenshot reads **Sum**. The button shows on hover only once one column is configured. "Calculate column" isn't a documented label. | Confirm labels in the clean-session D365 test. Add the right-click route, the four value types, the **Calculate** button for large datasets and "totals of selected rows". |
| 4.3 implies the total is part of the saved view (key concept "View = columns, filters and footer totals"). | Footer visibility and column totals are **restricted personalization**: saved automatically, per view, **without Save**, even on locked views. | Refine the concept: totals are remembered automatically; Save as still needed to create the named view. |
| 4.4 step 1: "open the current view name (**My View** for a new personal view)". | The out-of-box view is **Standard**; a view you create is named by you in **Save view as**. "My view" isn't a documented default name. | Check in D365; likely "Standard view". |
| 4.4 step 5–6: Pin as default, choose current legal entity or all legal entities; "ensure to also select the toggle to make this view the default view for all legal entities". | In **Save as**: **Pin as default** plus an optional legal entity subset (default global). A global view becomes default only where no legal-entity-specific default exists. The current/all choice is offered when pinning a **global** view in **Manage my views**. | Steps 5 and 6 are inconsistent (step 5 says choose; step 6 says always choose all). Raise with PG owner ([G260-07] already open). |
| Key concept "View scope: views are set up separately for each page". | Correct; plus the grid and details parts of a master/details page have separate views, and only large-selector pages save filters. | Add "filters save only on list pages". |
| 4.1: **Insert columns** to add columns; remove columns; move columns. | Right-click header > **Insert columns** / **Hide this column**; or toolbar **Add fields**, **Hide**, **Move**; keyboard **Ctrl+Shift+Left/Right** moves a column. Hidden is not deleted. **Recommended fields** list. | Consistent. Add that changes need **Save** on view pages. |
| 4.2 filter: open the filter for the column, select operator, enter value. | Consistent (column header filter). Adds: **Ctrl+G**; operators depend on data type; query symbols work **only with matches**; `""` for blanks; `!a, !b` for "not one of"; relative dates in parentheses; operator remembered per column. | Add the "matches" rule and relative dates as key concepts. |
| Filter operators table: Number "equals", "does not equal"; Text "ends with"; "? represents one character". | Microsoft's labels: **Is equal to** / **Is not equal to** (numbers), **Is exactly** / **Is not** (text); **ends with** not in Microsoft's table; "?" documented as "one or more unknown characters" with a one-character example. | Confirm each operator label per data type in D365. |
| 5: select saved view, change, **Save**; asterisk shows unsaved changes. | Consistent. Adds: **Save** isn't available on locked views (Standard, published), use **Save as**; **Manage my views** for rename, reorder, delete. | Add locked views and Manage my views. |
| 6: Export all rows (right-click grid header). | Agent C. Grid capabilities mentions "**Export to Excel** mechanism"; shortcut **Ctrl+Shift+E**. | Cross-reference only. |

### 10.2 What Microsoft documents beyond 260 (candidates)

Selecting rows and Select all; sorting; grouping and subtotals; freezing columns; autofit and resizing; min/max/average and selected-row totals; Filter pane; QuickFilter; Advanced filter or sort; query syntax and relative dates; clearing/reverting filters; lookups (type the name, filter in the lookup); math in numeric fields; paste from Excel and range copy; bulk edit; fast data entry row status; personalization toolbar (hide, move, rename, skip, show in header, require, lock); clearing personalization; Manage my views (rename, reorder, delete); published views (what users see: padlock, spark); views from tiles/menu items not applying the default; workspaces (filter, configure, Add to workspace, tile size, pin to dashboard); User options > Personalization tab; keyboard shortcuts (Alt+Shift+K to find them).

---

## 11. Gaps and contradictions in Microsoft's own documentation

1. **Filter pane side:** Filtering options (2026) says left; Learn training module says right.
2. **Personalization tool names:** article **Add fields** vs screenshot **Add a field**; article **Lock** vs shortcut table **Edit tool**; article **Show in header** vs shortcut table **Summary tool**.
3. **Custom fields article is out of date:** **Options > Personalize this form**, **Insert > Field**, **Manage** (export/import) vs current **Personalize this page**, **Add fields**, **Import/Export**.
4. **Calculated value labels:** article **Total** vs screenshot footer **Sum**.
5. **"?" wildcard:** "one or more unknown characters" vs one-character example.
6. **Marked-row shortcuts:** next = L, previous = P, last = N (looks swapped).
7. **Grid capabilities description** still says the new grid must be enabled (mandatory since 10.0.29).
8. **Not documented:** wrap text, find in grid, row height, clear-all-filters, Filter pane **Reset**, financial dimension filtering, the exact Advanced filter or sort menu path and its tabs, range-selection keys, the list of operators per data type.
9. **Personalize article** mentions **Add an app from Power Apps** only "when the Saved views feature is turned off", which can't happen since Saved views is mandatory.

---

## 12. Ranked list of suggested Getting Started topics (my area)

Must have (every finance user, every day):

| # | Topic | Why | Overlap with 260 |
|---|---|---|---|
| 1 | **Find records with filters**: QuickFilter, column header filter (operators, Ctrl+G), Filter pane (Add a filter field, Apply), clear a filter | The first thing every user does on every list page; three tools look alike and new users mix them up. | Extends 260 4.2 (column filter only). |
| 2 | **Filter operators and query syntax** (key concept): the "matches" rule, `*`, `?`, `..`, `!`, `,`, `""`, `T`, relative dates such as `(DayRange(-30,0))` | Decides whether a filter returns the right rows; relative dates keep saved views current. | Refines 260 Key concepts "Filter operators" (labels and "?" to confirm; add "matches" rule). |
| 3 | **Saved views: create, save, Save as, pin as default, switch, update** | Core of how users keep their working lists. | Same as 260 topics 4.4 and 5; merge or reuse, fix the legal entity default wording. |
| 4 | **Arrange a grid**: insert/hide/move columns, resize and autofit, freeze columns, sort | Needed before any view is worth saving; freezing keeps the account/name in sight on wide finance grids. | Extends 260 4.1 (freeze, autofit, sort are new). |
| 5 | **Footer totals and calculated values** (Show footer, View column totals: Total/Min/Max/Average, selected-row totals, Calculate on large lists) | Finance users check sums constantly (aged balances, journals, invoices). | Same as 260 4.3; correct labels, add selected-row totals and Calculate. |
| 6 | **Lookups**: type a name instead of an ID, filter inside a lookup | Every user enters customers, vendors, accounts; saves time and errors. | New. |

Should have:

| # | Topic | Why | Overlap |
|---|---|---|---|
| 7 | **Select rows** (check box, Select all, Ctrl/Shift) and selected-row totals | Needed for settlement, posting and marking tasks across O2C/P2P. | New. |
| 8 | **Group rows and subtotals** | Quick ad-hoc analysis without Excel (by customer, by currency, by month). | New. |
| 9 | **Manage my views** and **locked/published views** (padlock, spark, Save as from Standard, rename, reorder, delete) | Users will get organization views; must know why Save is greyed out. | Extends 260 5. |
| 10 | **Personalize a page with the toolbar** (hide, move, rename, show in FastTab header, skip) and **Clear** | Detail pages (customer, vendor, journal header) need tidying too; Clear is the safe undo. | New (260 is grid-only). |
| 11 | **Workspaces**: filter a workspace, Configure my workspace, open lists from tiles, Add to workspace, pin a count to the dashboard | Finance roles work from workspaces (Collections, Vendor invoice entry, Period close). | New; coordinate with agent A (dashboard/Immersive Home). |
| 12 | **Why my default view didn't open** (tiles and menu items with their own query) | Common confusion; one short note. | Note for 260 4.4. |
| 13 | **Keyboard shortcuts for grids and filters** (Alt+Shift+K, Ctrl+G, Ctrl+F3, Ctrl+Shift+F3, Ctrl+Shift+M, Alt+T chords) | Big productivity gain; Alt+Shift+K lets users discover the rest. | New; coordinate with agent A's shortcut list. |

Nice to have:

| # | Topic | Why | Overlap |
|---|---|---|---|
| 14 | **Math in numeric fields** (=15\*4) | One-line tip for journal and invoice amounts. | New. |
| 15 | **Advanced filter or sort** (multi-column sort, filter on fields not shown) | Power users; dialog uses table names. | New. |
| 16 | **Paste from Excel / copy a range of cells** | Useful for some entry grids; not for General journal lines (segmented entry). | New; check policy. |
| 17 | **Bulk edit (Edit selected rows)** | Only if the feature is on and the business allows it. | New; PG owner decision. |
| 18 | **Fast data entry row status** (pending, invalid, paused) | Explains italics and warning icons during line entry. | New. |
| 19 | **User options > Personalization tab** (see/export/delete your personalizations; reset callouts) | Self-service tidy-up. | New. |
| 20 | **Export/import a view to share with a colleague** | Publishing is the recommended route; export/import is a fallback. | New. |
| 21 | **Custom fields** (awareness only: who to ask) | Not an end-user task. | New; one line. |

Not for the guide (admin): publishing views, Personalization page, Copy to users, System settings, Client performance options, Feature management, custom field administration. Per D-083, the guide shouldn't name the **Saved views administrator** or **Runtime customization power user** roles; requests go to the BAU Support team.

Open questions for the PG owner (not SME): whether the organization publishes standard views (if yes, the guide should show the padlock/spark and Save as); whether **Bulk editing in grids** and **Extended grid aggregation capabilities** are enabled in production; whether paste from Excel is allowed; whether Immersive Home is on (it changes where pinned counts appear).

---

## Appendix A: Every URL consulted

Learn articles (rendered URLs; text read from the matching `.md` in `https://raw.githubusercontent.com/MicrosoftDocs/dynamics-365-unified-operations-public/main/articles/fin-ops-core/...`):

- https://learn.microsoft.com/en-us/dynamics365/fin-ops-core/dev-itpro/get-started/grid-capabilities
- https://learn.microsoft.com/en-us/dynamics365/fin-ops-core/fin-ops/get-started/advanced-filtering-query-options
- https://learn.microsoft.com/en-us/dynamics365/fin-ops-core/dev-itpro/get-started/personalize-user-experience
- https://learn.microsoft.com/en-us/dynamics365/fin-ops-core/dev-itpro/get-started/saved-views
- https://learn.microsoft.com/en-us/dynamics365/fin-ops-core/fin-ops/get-started/configure-filter-workspaces
- https://learn.microsoft.com/en-us/dynamics365/fin-ops-core/fin-ops/get-started/user-defined-fields
- https://learn.microsoft.com/en-us/dynamics365/fin-ops-core/fin-ops/get-started/use-lookups-to-find-information
- https://learn.microsoft.com/en-us/dynamics365/fin-ops-core/fin-ops/get-started/shortcut-keys
- https://learn.microsoft.com/en-us/dynamics365/fin-ops-core/fin-ops/get-started/default-dashboard
- https://learn.microsoft.com/en-us/dynamics365/fin-ops-core/fin-ops/get-started/client-faq
- https://learn.microsoft.com/en-us/dynamics365/fin-ops-core/fin-ops/get-started/user-interface-elements
- https://learn.microsoft.com/en-us/dynamics365/fin-ops-core/fin-ops/get-started/accessibility-features
- https://learn.microsoft.com/en-us/dynamics365/fin-ops-core/fin-ops/get-started/videos
- https://learn.microsoft.com/en-us/dynamics365/fin-ops-core/fin-ops/get-started/feature-management/feature-management-overview
- https://learn.microsoft.com/en-us/dynamics365/fin-ops-core/fin-ops/get-started/whats-new-home-page
- https://learn.microsoft.com/en-us/dynamics365/fin-ops-core/fin-ops/get-started/whats-new-platform-updates-10-0-29 through -10-0-50 (each of 10.0.29 to 10.0.50)
- https://learn.microsoft.com/en-us/dynamics365/fin-ops-core/fin-ops/copilot/immersive-home
- https://learn.microsoft.com/en-us/dynamics365/fin-ops-core/dev-itpro/user-interface/filtering
- https://learn.microsoft.com/en-us/dynamics365/fin-ops-core/dev-itpro/user-interface/understanding-saved-views
- https://learn.microsoft.com/en-us/dynamics365/fin-ops-core/dev-itpro/user-interface/sizing-input-controls-grid-columns
- https://learn.microsoft.com/en-us/dynamics365/fin-ops-core/dev-itpro/user-interface/contextual-data-entry-lookups
- https://learn.microsoft.com/en-us/dynamics365/fin-ops-core/dev-itpro/user-interface/lookups-controls
- https://learn.microsoft.com/en-us/dynamics365/fin-ops-core/dev-itpro/user-interface/build-workspace
- https://learn.microsoft.com/en-us/dynamics365/fin-ops-core/dev-itpro/user-interface/keyboard-shortcuts-controls
- https://learn.microsoft.com/en-us/dynamics365/fin-ops-core/dev-itpro/migration-upgrade/deprecated-features

Training (Learn):
- https://learn.microsoft.com/en-us/training/paths/get-started-finance-operations/
- https://learn.microsoft.com/en-us/training/modules/navigate-finance-operations/ (units 3-workspaces-driving-productivity, 4-filtering-techniques, 6-comparing-views, 7-view-and-edit-mode)

Release plans:
- https://learn.microsoft.com/en-us/dynamics365/release-plan/ (redirects to previous-versions 2025 wave 2)
- https://learn.microsoft.com/en-us/dynamics365/release-plan/2025wave1/finance-supply-chain/finance-operations-crossapp-capabilities/planned-features
- https://learn.microsoft.com/en-us/dynamics365/release-plan/2025wave2/enterprise-resource-planning/finance-operations-crossapp-capabilities/planned-features
- https://learn.microsoft.com/en-us/dynamics365/release-plan/2025wave2/enterprise-resource-planning/finance-operations-crossapp-capabilities/stay-focused-simplify-tasks-immersive-home-adaptive-experiences
- https://learn.microsoft.com/en-us/dynamics365/release-plan/2026wave1/enterprise-resource-planning/finance-operations-crossapp-capabilities/planned-features
- https://learn.microsoft.com/en-us/dynamics365/release-plan/2026wave2/ (404)

Search: https://learn.microsoft.com/api/search (queries on grid wrap text, saved views release plan, grid release plan 2025, filter release plan 2026, filtering on financial dimensions, training modules).

Images: raw GitHub `.../articles/fin-ops-core/fin-ops/get-started/media/` and `.../dev-itpro/user-interface/media/`; training module `.../navigate-finance-operations/media/`.

Repository: `ar-collections-learning/01-procedure-guides/PG-260-O2C-Getting-Started-DRAFT.md` (260 v0.2 preview, for comparison).

## Appendix B: Screenshot files

All in `media/grids-views/`:

| File | Shows | Source article |
|---|---|---|
| grid-footer-calculated-values-totals.png | Aged balances grid, footer with Sum and Maximum, row count; Standard view selector; QuickFilter | Grid capabilities |
| grid-grouping-with-subtotals.png | Grouped grid with group header rows and subtotals | Grid capabilities |
| grid-freeze-columns.gif | Freezing columns (animated) | Grid capabilities |
| grid-typing-ahead-fast-entry.gif | Fast data entry and row status (animated) | Grid capabilities |
| grid-math-expression.gif | =15\*4 evaluated (animated) | Grid capabilities |
| personalization-toolbar.png | Personalization toolbar (Select, Hide, Add a field, Move, Skip, Show in header, Lock, …, Close) | Personalize the user experience |
| personalize-element-property-window.png | Element property window | Personalize the user experience |
| personalize-add-to-workspace-dialog.png | Add to workspace dialog | Personalize the user experience |
| workspace-wide-filter-expanded.png | Workspace-wide filter drop-down | Configure and filter workspaces |
| workspace-section-filters.png | Section free-text Filter | Configure and filter workspaces |
| default-dashboard.png | Default dashboard | Default dashboard |
| quickfilter-column-selector.png | QuickFilter with column selector | Filtering options |
| grid-column-header-filter.png | Column header filter (legacy styling) | Filtering options |
| learn-module-filter-pane-and-column-filter.svg | Filter pane and column filter, numbered | Training module unit 4 |
| learn-module-customer-invoicing-workspace.svg | Customer invoicing workspace areas | Training module unit 3 |
