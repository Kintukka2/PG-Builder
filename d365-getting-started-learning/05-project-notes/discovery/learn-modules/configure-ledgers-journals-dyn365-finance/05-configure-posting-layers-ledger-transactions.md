<!-- https://learn.microsoft.com/en-us/training/modules/configure-ledgers-journals-dyn365-finance/configure-posting-layers -->
<!-- refetched: original harvest URL returned 404 -->
# Configure posting layers for ledger transactions

Completed

* 5 minutes

Posting layers are separate slots in the general ledger that you use to record the same transactions by using different accounting methods within a single system. Each layer maintains an independent set of numbers, and you can run reports against each layer separately.

Organizations often report the same financial activity in different ways for different audiences. Tax authorities might expect one set of depreciation calculations. International Financial Reporting Standards (IFRS) might require another. Local statutory frameworks might require a third. Posting layers let you manage these requirements at the same time in Dynamics 365 Finance without maintaining separate systems or datasets.

## Understand posting layers

Dynamics 365 Finance provides 10 posting layers:

| Posting layer | Typical use |
| --- | --- |
| **Current** | The default layer for day-to-day financial operations. Most transactions post to this layer. |
| **Operations** | Operational adjustments that you need to track separately from the Current layer. |
| **Tax** | Entries that affect tax reporting, such as tax-specific depreciation calculations. |
| **Custom 1-7** | Seven configurable layers for specific reporting frameworks, such as IFRS 16, local generally accepted accounting principles (GAAP), or other statutory requirements. |

There's also a special **None** option for asset books that shouldn't write to the general ledger. Use this option to track depreciation for calculation purposes without creating ledger entries.

[![Diagram showing one fixed asset connected to Financial, Tax, and IFRS books, which post to the Current, Tax, and Custom 1 layers, respectively.](media/05-posting-layers-concept.svg)](media/posting-layers-concept.svg#lightbox)

Note

Posting layers are primarily associated with the **Fixed assets** and **Asset leasing** modules, where books are the core configuration unit. General ledger journals also support posting layers for adjustment scenarios, but their use outside these modules is limited.

## Configure posting layers for fixed assets

Assign each fixed asset book to one posting layer, and all transactions for that book post to that layer. This separation structure lets you maintain different depreciation schedules for financial reporting, tax purposes, and internal management without duplicating the asset.

To set up a fixed asset book with a posting layer, follow these steps:

1. Go to **Fixed assets** > **Setup** > **Books**.
2. Select or create a book.
3. In the **Posting layer** field, select the layer where transactions for this book should post.
4. To prevent the book from writing to the general ledger, set **Post to general ledger** to **No**. Finance automatically sets the posting layer to **None**.

Each journal name associates with a single posting layer. You can't change this association after you create the journal, which helps keep transactions for each layer separate.

To create a journal name for a posting layer, follow these steps:

1. Go to **General ledger** > **Journal setup** > **Journal names**.
2. Select **New**.
3. In the **Posting layer** field, select the layer for this journal.
4. Configure the other journal settings as needed.

[![Screenshot of the Journal names page showing a fixed asset journal with the Posting layer field set to Current.](media/05-fixed-assets-journal-name.png)](media/fixed-assets-journal-name.png#lightbox)

Note

Most organizations create one journal name for each posting layer instead of one for each operation. You can specify only one default journal name for each posting layer in the fixed asset parameters. If you create a journal name for each layer and operation, users often need to change the default journal name.

Important

Create at least one journal name for every posting layer that you use. For books assigned to **None**, you can create a journal name with its posting layer set to **None**, but it isn't required. Set **Post to general ledger** to **No** for these books. Their transactions remain in the subledger.

## Configure posting layers for asset leasing

Asset leasing uses posting layers to support **dual reporting**, which maintains compliance with two accounting frameworks at the same time, such as IFRS 16 and a local statutory framework.

A typical dual-reporting setup requires three books:

* **Statutory book (Current layer)** - Records lease payments by using the local statutory method, which is often cash basis.
* **IFRS 16 book (Custom layer)** - Records the right-of-use (ROU) asset and lease liability entries required under IFRS 16.
* **Statutory reversal book (same Custom layer)** - Reverses the statutory entries in the custom layer so the combined view of both layers reflects IFRS reporting.

The **Current** layer shows the statutory view. The combined **Current + Custom** layers show the IFRS view.

[![Diagram showing how statutory and IFRS 16 postings use different layers to provide statutory and IFRS financial views.](media/05-dual-reporting-flow.svg)](media/dual-reporting-flow.svg#lightbox)

To set up books for dual reporting in Asset leasing, follow these steps:

1. Go to **Asset leasing** > **Setup** > **Book setup**.
2. Create or open a book.
3. In the **Posting layer** field, assign the appropriate Current or Custom layer.
4. Set the **Accounting framework** to the applicable standard, such as IFRS 16 or cash basis.
5. Associate all three books with the same lease record.

Note

You enter a lease only once. Finance applies the correct journal entries to each book and posts each entry to its designated layer.

## Use posting layers in general ledger journals

You can post adjustments that shouldn't appear in the standard Current-layer view directly to another layer by using a general ledger journal. All lines in a journal post to the same layer because the journal name specifies the layer. You can't mix layers in one journal.

For example, different legal entities might close their books by using different calendars. If one legal entity makes an adjustment after its parent entity closes the period, it can post the adjustment to the correct period in a local-only layer and to the current open period in the Current layer for the parent company. A legal entity can also post country-specific statutory adjustments to a local-only layer and exclude that layer when it consolidates results into the parent company.

To post a general ledger adjustment to a specific layer, follow these steps:

1. Go to **General ledger** > **Journal entries** > **General journals**.
2. Select **New**, and then choose a journal name configured for the target posting layer.
3. Enter the adjustment lines.
4. Post the journal.

The adjustment is visible when you report on or filter by that posting layer. On the trial balance, you can select a layer. In Financial reporting, you can include specific layers in each column. Consolidation rolls up each layer separately, so you can include only the layers that are appropriate for consolidated reporting.