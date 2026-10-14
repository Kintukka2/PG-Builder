# Validation Register: AR Collections Export to Excel

| Field | Value |
|---|---|
| Related PG (editable source) | [`../01-procedure-guides/TBC-AR Collections Export to Excel PG v0.1.docx`](../01-procedure-guides/TBC-AR%20Collections%20Export%20to%20Excel%20PG%20v0.1.docx) |
| Markdown preview | [`../01-procedure-guides/PG-AR-Export-to-Excel-DRAFT.md`](../01-procedure-guides/PG-AR-Export-to-Excel-DRAFT.md) |
| Screenshot register | [`../02-screenshot-registers/PG-AR-Export-to-Excel-Screenshots.md`](../02-screenshot-registers/PG-AR-Export-to-Excel-Screenshots.md) |
| Last updated | 2026-10-14 |
| Items | 20 total, all open: 12 blocking, 8 non-blocking |

This file is the guide's **question log** (decision D-016). The `VG-xx` IDs are scoped to this guide and never renumbered. Each open item that affects the text is also a Word review comment by "Validation register" (VR).

---

## 1. Evidence base

| Source | What it supports |
|---|---|
| 0, Topic 23 *Export Data to Excel* | Right-click column header, Export All Rows, download data. Rated ready. Suggested PG `PG-AR-019 Export D365 Customer Data to Excel`. |
| 1, Module 12 | Sequences 12.1 (export all rows from a D365 grid: ready), 12.2 (prepare columns before exporting: ready), 12.3 (export volume limitations: **partial**). The recording shows right-clicking a grid header, selecting Export all rows and downloading the export. Learning outcome: export for operational analysis, not as a customer-facing document. |
| 1, Module 12 (gaps) | A custom all-customer transaction report (12.4) and daily bank statements in SharePoint (12.7) are mentioned, but their access paths were not captured. |
| 2, Release 2 item 17 | Scope: prepare the visible columns, right-click the grid header, select Export all rows, download the export, validate that the required fields are included. The trainer notes that the export reflects the configured columns. Control: Excel exports are for internal analysis and should not replace approved PDF customer documents. |
| 3.1, first drafting batch #5 | Scope: configure the required columns, right-click a grid heading, select Export all rows, download the output, confirm the required fields were exported. Control note: the export is for internal analysis. Risk: low. Ready to draft. |
| Personalized Views guide | Adding columns with **Insert columns** (its labels are still unconfirmed). |

**Not available:** a transcript excerpt, timestamps, the export volume limit, or the screen D365 shows while preparing the download.

---

## 2. Drafting decisions for this guide

| # | Decision | Reason |
|---|---|---|
| E1 | One standalone topic, **1. Export All Rows from a Grid**. Preparing columns is a step, not a separate topic. | Source 1 rates column preparation as a *PG section*, not a separate PG. The task is done in one sitting. |
| E2 | The procedure starts with *Check* the **Entity**, then *Open* the page that holds the data. It does not give one *Click* **Modules** / *Navigate* path. | This is a utility task performed on many pages (`VG-10`). Aged balances from Favorites is given as an example. |
| E3 | Column preparation refers to the Personalized Views guide instead of repeating its steps. | One source of truth for Insert columns. |
| E4 | Export volume is a Key concept with no limit stated. | Source 1 rates it partial. No figure is invented (`VG-06`). |
| E5 | The internal-analysis rule uses the same wording as the Aged Balances and Customer Invoices guides. A data handling row is added for exported files. | One rule wording across guides. The file holds customer data (`VG-08`). |
| E6 | The custom all-customer transaction report and bank statements are out of scope. | Their access paths were not captured. Each one is a separate guide once validated (`VG-20`). |
| E7 | Process name **AR Collections Export to Excel**. | Sources 0 and 1 both name the guide around Excel export. The final title is open (`VG-15`). |

---

## 3. Validation gap register

**Priority:** **B** = blocks publication. **N** = non-blocking.

**Method:** **Test** = D365 test in a clean session. **Rec** = recording or transcript review. **SME** = subject-matter expert or process owner. **Dec** = project decision.

| ID | Item to confirm | Location in Word guide | Word comment | Priority | Method | Status |
|---|---|---|---|---|---|---|
| VG-01 | Exact label of the **Export all rows** menu option. | Key concepts; Step 5 | 4, 11 | B | Test, Rec | Open |
| VG-02 | Where to right-click: any column heading, or a specific part of the grid header. | Step 4 | 10 | B | Test, Rec | Open |
| VG-03 | What D365 displays after **Export all rows** is selected, and the label of the control that downloads the file. | Step 6 | 12 | B | Test, Rec | Open |
| VG-04 | That columns hidden from the grid are left out of the export. Source 2 states that the export reflects the configured columns. | Key concepts | 5 | N | Test | Open |
| VG-05 | Whether rows hidden by a grid filter are included in the export. | Key concepts | 4 | N | Test | Open |
| VG-06 | Export volume limitations, and what users should do when a limit applies. | Key concepts | 6 | B | SME, Test | Open |
| VG-07 | The file format, and where the downloaded file is saved. | Step 7 | 13 | N | Test | Open |
| VG-08 | The rule for storing, sharing and deleting exported files that contain customer data. | Key concepts | 8 | B | SME | Open |
| VG-09 | Wording and owner of the internal-analysis rule. Shared with Aged Balances VG-13 and Customer Invoices VG-12. | Key concepts | 7 | N | SME | Open |
| VG-10 | That a utility guide may replace the standard *Click* **Modules** / *Navigate* rows with "Open the page that holds the data". | Step 2 | 9 | N | Dec | Open |
| VG-11 | Which pages AR Collections users export most often, to use as examples. | Step 2 | 9 | N | SME | Open |
| VG-12 | Initiation events for this task. | Part 1 Initiation; topic Initiation; Process table *When* | 2 | B | SME | Open |
| VG-13 | Stream, process area and business role name. Shared with the other AR Collections guides. | Stream table; Process table; Roles matrix | 3 | B | SME | Open |
| VG-14 | Business process owner (BPO). | Version history | 1 | B | SME | Open |
| VG-15 | Guide code and final title. Source 0 proposes `PG-AR-019 Export D365 Customer Data to Excel`; source 2 uses "Export all rows from a D365 grid". | Cover; file name | 0 | B | Dec | Open |
| VG-16 | Whether any reports or inquiries apply. If none, "No applicable reports". | Part 3 | 14 | B | SME | Open |
| VG-17 | Whether exporting needs a specific security role or permission, and a test with it. If the option is missing for a user, security access is a possible cause, not a confirmed one. | PROCESS START | — | B | Test, SME | Open |
| VG-18 | SME factual review, a test by someone other than the author, and approval. | Whole guide | — | B | SME | Open |
| VG-19 | Recording timestamps for the export demonstration. | Screenshot register | — | N | Rec | Open |
| VG-20 | Confirm that the custom all-customer transaction report and daily bank statements belong in separate guides. | Part Description (scope); Part 3 | 14 | N | Dec | Open |

**Fastest route to closure:** one clean-session D365 export from any grid closes `VG-01` to `VG-05` and `VG-07`. It can be part of the same session as the Favorites, Personalized Views, Aged Balances and Customer Invoices tests. `VG-06` and `VG-08` need SME answers.

---

## 4. Publication readiness

| Check | Status |
|---|---|
| Template structure is complete; unused examples are removed | Met |
| Process table rows match the Part 2 topics (1 row) | Met; values pending `VG-12` and `VG-13` |
| Standard navigation pattern | Partial: Entity check, then open the page (`VG-10`) |
| Each procedure table restarts numbering at 1 | Met |
| Exact system labels | Open (`VG-01` to `VG-03`) |
| Business rules separate from procedure | Met (internal-analysis and data handling rules in Key concepts) |
| Reports | Open (`VG-16`) |
| Roles, BPO, guide code | Open (`VG-13`, `VG-14`, `VG-15`) |
| Peer test, SME review, approval | Open (`VG-17`, `VG-18`) |
| Review comments resolved before release | Open (15 Word comments) |

---

## 5. Change log

| Date | Change |
|---|---|
| 2026-10-14 | Register created with the v0.1 SME review draft. |
