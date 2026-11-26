<!-- https://learn.microsoft.com/en-us/training/modules/navigate-finance-operations/4-filtering-techniques -->
# Use filtering techniques

Completed

* 8 minutes

There are several filtering options that you can use in finance and operations apps.

## Filter pane

The Filter pane provides an easy-to-use interface for filtering full page lists. The Filter pane is an inline pane that slides in from the right side of the screen and pushes the page content to the left, so that users can see the data that they want to filter. You can open this filter mechanism by selecting the system-defined **Show filters** button on the right side of the page. After it has been opened, the Filter pane remains visible until you go to a new page, or until you close the **Filter** pane by using the **Hide filters** button (see area marked “1” in the following screenshot).

[![Screenshot of the Filter pane in finance and operations.](media/04-filtering.svg)](media/filtering.svg#lightbox)

## QuickFilter

In finance and operations apps, the QuickFilter is a modeled control that can be associated with any grid in the system. As the user starts to type, a column selector drop-down menu appears to guide the user toward the column that the filter will be applied to. The developer can also specify the default column for the QuickFilter. If no column is specified, the default column is the first field that can be filtered in the grid.

## Grid column header filtering/sorting

The grid filtering experience is more closely aligned with the experience in Microsoft Excel. When you click a column header (for columns that can be filtered), a drop-down menu appears, and you can use it to filter the column. The filtering experience here mimics the filtering experience in the Filter pane. Additionally, there are options to sort the grid based on the column that is currently selected (see area marked “2” in the previous screenshot).

You can also make use of advanced manipulation of grid controls via keyboard shortcuts, multiple record selection, and aggregate value views to efficiently view grid data in a page. For more information, see [Grid capabilities](/en-us/dynamics365/fin-ops-core/fin-ops/get-started/grid-capabilities/?azure-portal=true).

## Wildcards

You can use the asterisk to indicate that any value before or after this point is valid, which is great for searching for records that all start and/or have the same characters somewhere within the field.

To read more about filtering options and filtering expressions in [Filtering options](/en-us/dynamics365/fin-ops-core/dev-itpro/user-interface/filtering/?azure-portal=true).