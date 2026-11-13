# D365 F&O: CW1 to D365 Migration Procedure Guide

> **WORKING DRAFT. Not validated or approved.**
>
> This is a Markdown preview of the Word guide [`CLAUDE-TBC-CW1 to D365 Migration PG v0.1.docx`](CLAUDE-TBC-CW1%20to%20D365%20Migration%20PG%20v0.1.docx). It converts the *CW1 to D365 Migration - Go-Live Manual* (version date October 2026) to the PG master template (D-058). **The Word file is the editable source.**
>
> Markers such as `[CM-05]` show unconfirmed items. In the Word file, each one is a review comment. The items are in the [validation register](../03-validation/CW1-to-D365-Migration-v0.1-Validation.md). The markers are not part of the guide text. Rows of a procedure that happen outside D365 (in Excel, TM1 or CW1) are shaded gray in the Word file.
>
> Notes marked **ACTION: REVIEW REQUIREMENT**, and <mark>highlighted</mark> phrases, are internal notes to the author (yellow, in the Word style of the same name). They are removed before publication (D-060).

The fixed template content is not repeated here: cover, Contents, *About this guide* and *Additional Resources*.

**Version history**

| **ID** | **Date** | **Author/s** | **BPO** | **Description of change** |
|---|---|---|---|---|
| 0.1 | November 2026 | Daniel Moreira | Maria Florencia Ruiz `[CM-02]` | Working draft (D-058): converted from the CW1 to D365 Migration - Go-Live Manual (version date October 2026) to the PG master template. Steps 1 to 8 and the pre go-live checklist become topics 1 to 9, with one action per row, process boundaries and links. Not validated or approved. `[CM-01]` |

---

## Part 1: What do I need to know? (CW1 to D365 Migration)

### High-level process

##### Part Description

**CW1 to D365 Migration** sets out the steps to migrate an entity's accounting balances from CargoWise One (CW1), as reported in TM1, to Microsoft Dynamics 365 Finance (D365). It covers the ledger mapping, the analysis of the closing trial balance (TB), the balance breakdowns and the opening balance (OB) file, the reversal of the balances in CW1, the upload of SPE balances at historical rates, the post-upload adjustment journals, and the check of the D365 TB after go-live. `[CM-04]`

The Ledger Owners (LOs) prepare the migration files, and the Regional Accounting Manager (RAM) reviews them. `[CM-05]` The Reporting team prepares reconciled breakdowns of the closing balances. The TM1 administrator prepares the ledger mapping and manages the CW1 feed to TM1, and the CW1 administrator opens and closes the cutover department in CW1. `[CM-06]` The work uses CW1, TM1, Excel workbooks (the AMCS template, the OB workbook and the ADAW workbook) and D365.

At a high level, the migration follows these stages:

- **Map the CW1 Ledger to TM1**: prepare and review the CW1 to TM1 ledger mapping file.
- **Analyze the CW1 Closing Trial Balance**: identify the accounts to upload to the subledger, the accounts that need a breakdown, the SPE accounts and the monetary items to revalue.
- **Prepare the Breakdown Files**: prepare reconciled breakdowns on the AMCS template, and highlight the items to reverse in D365.
- **Prepare the Opening Balance File**: complete the OB workbook, including the AMCS upload tab.
- **Reverse the Balances in CW1**: clear out the migrated balances in CW1 with an ADAW journal posted to Department 001.
- **Upload the SPE Balances at Historical Rates**: change two D365 settings temporarily, post the SPE journal, then revert the settings.
- **Book the Post-Upload Adjustment Journals**: book and review the journals for the items highlighted in the breakdown files.
- **Check the D365 Trial Balance After Go-Live**: reconcile the D365 TB with the balances intended to be migrated, and sign off.
- **Complete the Pre Go-Live Checklist**: track each deliverable to completion.

> **ACTION: REVIEW REQUIREMENT.** This guide does not yet describe how the OB file `[CM-23]` and the subledger balances `[CM-24]` are uploaded to D365.

##### Initiation

- An entity is scheduled to go live in D365, and its accounting balances are to be migrated from CW1. `[CM-07]`

##### Stream

| **Stream** | **Process Area** | **Key Roles** |
|---|---|---|
| Record-to-Report (R2R) `[CM-03]` | CW1 to D365 Migration | • Ledger Owner (LO) `[CM-05]`<br>• Regional Accounting Manager (RAM)<br>• Reporting team<br>• TM1 administrator `[CM-06]`<br>• CW1 administrator<br>• Finance Transformation |

##### Process

The high-level CW1 to D365 Migration process is as follows:

| **#** | **Action** | **Who** | **When** | **Where** |
|---|---|---|---|---|
| **1** | [Map the CW1 Ledger to TM1](#1-map-the-cw1-ledger-to-tm1) | TM1 administrator `[CM-06]` | Before go-live `[CM-07]` | Excel; SharePoint |
| **2** | [Analyze the CW1 Closing Trial Balance](#2-analyze-the-cw1-closing-trial-balance) | Ledger Owner (LO) `[CM-11]`; Reporting team | When the CW1 closing TB is available in TM1 | TM1; Excel |
| **3** | [Prepare the Breakdown Files](#3-prepare-the-breakdown-files) | Ledger Owner (LO) prepares; Regional Accounting Manager (RAM) reviews | When the accounts that need a breakdown are identified | Excel; TM1 |
| **4** | [Prepare the Opening Balance File](#4-prepare-the-opening-balance-file) | Ledger Owner (LO) | When all the breakdown files are complete | Excel |
| **5** | [Reverse the Balances in CW1](#5-reverse-the-balances-in-cw1) | Ledger Owner (LO); CW1 administrator; TM1 administrator; Finance Transformation | When the D365 TB has been loaded | CW1; TM1; Excel |
| **6** | [Upload the SPE Balances at Historical Rates](#6-upload-the-spe-balances-at-historical-rates) | Ledger Owner (LO) prepares the SPE workings; <mark>the owner of the D365 settings is to be confirmed</mark> `[CM-30]` | As part of the TB upload | Excel; D365 |
| **7** | [Book the Post-Upload Adjustment Journals](#7-book-the-post-upload-adjustment-journals) | Ledger Owner (LO) prepares; Regional Accounting Manager (RAM) reviews | After the TB/OB upload is posted in D365, in the migration month | D365; Excel |
| **8** | [Check the D365 Trial Balance After Go-Live](#8-check-the-d365-trial-balance-after-go-live) | Ledger Owner (LO) prepares; Regional Accounting Manager (RAM) reviews | After go-live, before the first D365 month-end close | D365; Excel; CW1 |
| **9** | [Complete the Pre Go-Live Checklist](#9-complete-the-pre-go-live-checklist) | The owner of each deliverable | Throughout the migration, until each deliverable is complete | This guide |

### Roles and responsibilities

##### Overview

The Ledger Owner (LO) prepares the migration files, the reversal in CW1, the SPE workings, the adjustment journals and the post go-live reconciliation. The Regional Accounting Manager (RAM) reviews the breakdown files, the adjustment journals and the reconciliation. The Reporting team provides reconciled breakdowns of the closing balances. The TM1 administrator prepares the ledger mapping and manages the CW1 feed to TM1, the CW1 administrator activates the cutover department in CW1 for the reversal, and Finance Transformation flags the ledgers that keep CW1 activity in the cutover month. `[CM-05]`

| **Tasks / Business Roles** | **Ledger Owner (LO)** | **Regional Accounting Manager (RAM)** | **Reporting Team** | **TM1 Administrator** | **CW1 Administrator** | **Finance Transformation** |
|---|---|---|---|---|---|---|
| [1. Map the CW1 Ledger to TM1](#1-map-the-cw1-ledger-to-tm1) |  |  |  | R |  |  |
| [2. Analyze the CW1 Closing Trial Balance](#2-analyze-the-cw1-closing-trial-balance) | R |  | R |  |  |  |
| [3. Prepare the Breakdown Files](#3-prepare-the-breakdown-files) | R | R |  |  |  |  |
| [4. Prepare the Opening Balance File](#4-prepare-the-opening-balance-file) | R |  |  |  |  |  |
| [4.1 Complete the TB OB Tab](#41-complete-the-tb-ob-tab) | R |  |  |  |  |  |
| [4.2 Add Breakdown Lines](#42-add-breakdown-lines) | R |  |  |  |  |  |
| [4.3 Complete the AMCS Upload Tab](#43-complete-the-amcs-upload-tab) | R |  |  |  |  |  |
| [5. Reverse the Balances in CW1](#5-reverse-the-balances-in-cw1) | R |  |  | R | R | R |
| [5.1 Flag the Ledgers with CW1 Activity in the Cutover Month](#51-flag-the-ledgers-with-cw1-activity-in-the-cutover-month) |  |  |  | R |  | R |
| [5.2 Prepare the ADAW Clear-Out Journal](#52-prepare-the-adaw-clear-out-journal) | R |  |  |  |  |  |
| [5.3 Import the ADAW Journal into CW1](#53-import-the-adaw-journal-into-cw1) | R |  |  |  | R |  |
| [5.4 Confirm the Migration-Month Trial Balance in CW1](#54-confirm-the-migration-month-trial-balance-in-cw1) | R |  |  |  |  |  |
| [5.5 Disconnect the CW1 Feed to TM1](#55-disconnect-the-cw1-feed-to-tm1) |  |  |  | R |  |  |
| [6. Upload the SPE Balances at Historical Rates](#6-upload-the-spe-balances-at-historical-rates) | R |  |  |  |  |  |
| [6.1 Change the Maximum Penny-Rounding Difference](#61-change-the-maximum-penny-rounding-difference) |  |  |  |  |  |  |
| [6.2 Redirect the Penny Difference Posting Account](#62-redirect-the-penny-difference-posting-account) |  |  |  |  |  |  |
| [6.3 Revert the Original Configuration](#63-revert-the-original-configuration) |  |  |  |  |  |  |
| [7. Book the Post-Upload Adjustment Journals](#7-book-the-post-upload-adjustment-journals) | R | R |  |  |  |  |
| [8. Check the D365 Trial Balance After Go-Live](#8-check-the-d365-trial-balance-after-go-live) | R | R |  |  |  |  |
| [8.1 Extract the D365 Trial Balance](#81-extract-the-d365-trial-balance) | R |  |  |  |  |  |
| [8.2 Compare with the Intended Migration Balances](#82-compare-with-the-intended-migration-balances) | R |  |  |  |  |  |
| [8.3 Reconcile the Migration Journals](#83-reconcile-the-migration-journals) | R |  |  |  |  |  |
| [8.4 Check the Subledger Balances](#84-check-the-subledger-balances) | R |  |  |  |  |  |
| [8.5 Check the Reporting Currency Balances](#85-check-the-reporting-currency-balances) | R |  |  |  |  |  |
| [8.6 Confirm the CW1 Side and Sign Off](#86-confirm-the-cw1-side-and-sign-off) | R | R |  |  |  |  |
| [9. Complete the Pre Go-Live Checklist](#9-complete-the-pre-go-live-checklist) | R | R | R | R |  |  |

\*R = Responsible

> **ACTION: REVIEW REQUIREMENT.** No role is marked for 6.1 to 6.3 until the owner of the D365 settings is confirmed. `[CM-30]`

> **Note:** The business roles shown above are responsible for completing these tasks on a day-to-day basis; however, other business roles may also have access to the same functionality to complete these tasks when required.

### Key concepts

##### Overview

Before you start, you need to know the terms used in this guide, the groups of accounts that the migration treats differently, the structure of the OB workbook and its checks, the Department 001 rule and the ADAW workbook for the reversal in CW1, how the CW1 feed to TM1 changes around go-live, and why SPE balances need temporary D365 settings.

##### Terms and Abbreviations

| **Term** | **Meaning** |
|---|---|
| **ADAW** | Advanced Data Automation Wizard: the CW1 tool used to upload GL journals from an Excel template ([5. Reverse the Balances in CW1](#5-reverse-the-balances-in-cw1)). |
| **AMCS** | The D365 general ledger upload template (multi-ledger journal import), used for the breakdown and OB uploads. |
| **BU** | Business unit (the **BusinessUnit** dimension). |
| **CC** | Cost center (the **CostCenter** dimension). |
| **CoA** | Chart of accounts. |
| **CW1** | CargoWise One: the legacy accounting system that the balances are migrated from. |
| **D365** | Microsoft Dynamics 365 Finance: the target system. |
| **FCTR** | Foreign Currency Translation Reserve (account **314200**). |
| **FX** | Foreign exchange. |
| **GJL / RJL** | General journal / reversing journal (ADAW journal types). |
| **GL** | General ledger. |
| **LO** | Ledger Owner. `[CM-05]` |
| **OB** | Opening balance. |
| **P&L** | Profit and loss. |
| **PPE** | Property, plant and equipment. |
| **RAM** | Regional Accounting Manager. |
| **SL** | Subledger. |
| **SPE** | Balances converted to reporting currency at the historical rates recorded in the SPE table. |
| **TB** | Trial balance. |
| **TP** | Trading partner (the **TradingPartner** dimension). |
| **YTD** | Year to date. |

##### Account Groups for the Migration

| **Group** | **How it is migrated** |
|---|---|
| **Subledger (SL) accounts** | Balances uploaded to the SL: trade receivables, trade creditors, inter-business receivables and payables, subscription billing, prepayments, PPE, leases and banks. Each SL balance is uploaded to the GL as part of the OB, that GL upload is reversed, and the balance is re-uploaded to the SL: see [8.4 Check the Subledger Balances](#84-check-the-subledger-balances). `[CM-24]` |
| **Accounts that need a breakdown** | Uploaded in more detail than their TM1 closing balance: see [Breakdowns Required](#breakdowns-required). |
| **SPE accounts** | Need a special FX rate for conversion to reporting currency: see [SPE Balances and Temporary D365 Settings](#spe-balances-and-temporary-d365-settings). |
| **Monetary items to be revalued** | The last CW1 revaluation is separated from the SL and GL OB, uploaded as a separate transaction, and reversed in the month of migration. `[CM-13]` |
| **P&L accounts** | Little to do, unless D365 dimensions are needed for balances that pre-date D365. |
| **Functional currency items** | For items held in the functional currency that need no revaluation or settlement, uploading the closing balance is sufficient. |

Every account identified in the analysis needs a detailed, reconciled breakdown of its closing balance. The Reporting team prepares these breakdowns and provides the pending items in the AMCS upload format. `[CM-12]`

##### Breakdowns Required

| **Account type** | **Breakdown required** |
|---|---|
| Accruals | By vendor |
| Customer-related balances | By customer |
| Tax accounts with no clearly defined fiscal year | By activity and fiscal year |
| REM accounting entries | By period or quarter |
| Rental bond | By property |
| GST clearing | Balance and reconciling items |
| Any other reconciling items | By reconciling item |

##### Opening Balance Workbook

Prepare one OB workbook per entity. The workings tab is named with the D365 company code, and the tabs appear in this order:

| **Tab** | **Name** | **Purpose** |
|---|---|---|
| 1 | **AMCSMultiLedgerJournalImport_GL** | The AMCS upload file. It is formula-linked to the TB OB tab, so the data flows into this tab once Tab 2 is complete: see [4.3 Complete the AMCS Upload Tab](#43-complete-the-amcs-upload-tab). |
| 2 | **&lt;company code> TB OB** (for example, **234A TB OB**) | The main working tab for the opening balance: see [4.1 Complete the TB OB Tab](#41-complete-the-tb-ob-tab). Row 1 labels the source of each column (**From TM1 Report**, **From Adam's file**, **From D365 report**, **Check** and **To be populated by LO**), and row 2 holds the column headers. |
| 3 | **CW1 CoA Structure** | The TM1 report of the CW1 chart of accounts structure. |
| 4 | **D356 CoA** | The D365 chart of accounts, with columns including **Main account**, **Name**, **Main account category**, **Main account type**, **Posting type**, **Do not allow manual entry** and **Foreign currency revaluation**. `[CM-16]` |
| 5 | **LedgerAccountStructureContains** | The D365 ledger account structures (**Ledger Account Structure**), which define the dimensions required for each account, in the order **MainAccount**, **BusinessUnit**, **CostCenter**, **Product**, **Activity**, **TradingPartner**, **Segment**. Only **Active** structures are used by the lookups. |
| 6 | **New dimensions** | New **BusinessUnit** and **Product** dimension values to be created in D365. |
| 7 | **TB TM1 &lt;period>** (for example, **TB TM1 P03**) | The TM1 TB report by CW1 company, showing the balances to be migrated. |

##### Opening Balance Checks

| **Check** | **Where** | **Passes when** |
|---|---|---|
| **Level 6 check** | TB OB column I | **YES**: the CW1 Level 6 (column C) equals the D365 Level 6 (column H). |
| **Account Name Check** | TB OB column J | **YES**: the CW1 and D365 account names share enough key words, that is, the word-match score is at or above the **Name match threshold** in cell J92 (default **0.5**). This is a sense check only. `[CM-19]` |
| **FD Check** | TB OB column V | **YES** on every line: each dimension in columns Q to U falls within the allowed values in columns L to P. Otherwise it returns **NO:** followed by the failing dimensions. |
| **Check** row | TB OB, below the data | The sum of column D is **0**. The row sums columns D, W and X. |
| Total debits less total credits | TB OB cell W92 | The cell shows **0**. |
| **AMCS totals** | Tab 1 | Total debits equal total credits, and both totals agree to the TB OB totals in columns W and X. |
| **All N Elements with FCTR** | Tab 7 check row | Zero for each company. |

> **Important:** Do not upload the OB file until every line shows **YES** in the FD Check (column V), the sum of column D in the Check row is **0**, and cell W92 (total debits less total credits) is **0**.

##### Department 001 in CW1

Post every line of the ADAW clear-out journal to Department 001 (**D365 cutover use only**): balance sheet and P&L lines, in every ledger. A single coding rule for every ledger means that nobody has to decide which department to use. That decision is what went wrong for CCES and South Africa.

The rule matters because some ledgers keep billing in CW1 after go-live, for example A71, A78, A92 and AUY in AU Main Phase 2, and South Africa (SDT). D365 already reports that billing, so without a filter it would reach TM1 twice. Because only the clear-out journal uses Department 001, TM1 can keep the journal and drop all other CW1 activity on those ledgers in the cutover month (see [CW1 Feed to TM1 Around Go-Live](#cw1-feed-to-tm1-around-go-live)). `[CM-25]`

Two more rules apply:

- Department 001 stays inactive in CW1. The CW1 administrator activates it only for this posting, and deactivates it immediately afterwards.
- To reverse an ADAW journal, reverse the signs of the amounts in the template and import it again. Any reversal or repost must also use Department 001: the CCES reversal was not posted to 001, so TM1 ignored it.

##### ADAW Workbook

Prepare the reversal in the workbook **ADAW Journal - Closing out balances for D365.xlsx**. ADAW (Advanced Data Automation Wizard) is the CW1 tool for uploading GL journals from an Excel template. `[CM-09]`

| **Tab** | **Purpose** |
|---|---|
| **ADAW Journal Template A** | The import tab. Template A has one journal header per company, and can post to several CW1 companies in one upload. It must remain the first tab in the workbook. |
| **CW1 Confirmation** | The CW1 confirmation dialog, pasted in after the import for audit purposes. |
| **Instructions**, **Key** and **Version control** | Reference tabs supplied with the template. |
| **TB evidence tabs** | One tab per CW1 company, grouped behind the divider tabs **P03 TBs >>**, **P04 TBs prior clearing >>** and **P04 TBs post clearing >>**: see [5.2 Prepare the ADAW Clear-Out Journal](#52-prepare-the-adaw-clear-out-journal), [5.3 Import the ADAW Journal into CW1](#53-import-the-adaw-journal-into-cw1) and [5.4 Confirm the Migration-Month Trial Balance in CW1](#54-confirm-the-migration-month-trial-balance-in-cw1). |

##### CW1 Feed to TM1 Around Go-Live

| **Stage** | **When** | **CW1 feed to TM1** |
|---|---|---|
| 1 | Before the cutover month | Connected, all departments. |
| 2 | Cutover month | Flagged ledgers: Department 001 only. Other ledgers: all departments. |
| 3 | From the following month | Disconnected. |

TM1 applies the 001-only rule only to the ledgers flagged in [5.1 Flag the Ledgers with CW1 Activity in the Cutover Month](#51-flag-the-ledgers-with-cw1-activity-in-the-cutover-month). Review and update the TM1 001-only list for each go-live (for example, A95 was taken off the list in September 2026). `[CM-25]`

##### SPE Balances and Temporary D365 Settings

The TB is uploaded in each entity's functional currency, ignoring the FX rate used to convert to reporting currency. All accounts are then converted to reporting currency at the current month P&L rate, so the upload creates no difference from a reporting currency perspective.

SPE balances are the exception. Their historical rates in the SPE table are preserved, in case D365 consolidation functionality is used in future. A separate journal reverses each SPE balance in functional currency (converted at the migration-month rate) and rebooks it in the respective currencies, converted to reporting currency at the historical rates. The difference in reporting currency is posted to FCTR. LOs prepare the workings using the information in the SPE table. `[CM-29]`

In the current configuration, a variance of USD 10.00 or less between the debit and credit in reporting currency (USD), from FX rate rounding or different exchange rates, posts automatically to a rounding account. Because the SPE journal posts a movement in USD reporting currency, two D365 settings are changed for the posting and reverted immediately afterwards:

| **Setting** | **Normal value** | **For the SPE journal** |
|---|---|---|
| **Maximum penny-rounding difference in the reporting currency** (**General ledger parameters**, **Ledger** tab) | **10.00** (USD) | The calculated value: the difference between the SPE accounts converted to reporting currency at the migration-date rate and their values at historical rates. |
| Main account for **Penny difference in reporting currency** (**Accounts for automatic transactions**) | **551404** - Rounding Difference Reporting Currency | **314200** - Foreign Currency Translation Reserve, so that the movement is recorded as a foreign currency translation rather than a rounding difference. |

The steps are in [6. Upload the SPE Balances at Historical Rates](#6-upload-the-spe-balances-at-historical-rates). Details are in [Bug 11817](https://dev.azure.com/wtg-finance/Atlas%20D365/_workitems/edit/11817). `[CM-10]`

---

## Part 2: How do I do it? (CW1 to D365 Migration)

### 1. Map the CW1 Ledger to TM1

> Off-system: this activity is completed outside D365, in Excel.

##### Task Overview

Before go-live, the CW1 to TM1 ledger mapping file is prepared. The OB file takes the initial D365 GL account (column E of the TB OB tab) and the TM1 mapping (column K) from it, labeled **From Adam's file** in row 1.

An example mapping file, [FI1 TB Mapping v2](https://wisetechglobal.sharepoint.com/sites/Atlas/Shared%20Documents/05%20Data%20Migration/Phase%203.3%20(WAVE_1)/2.%20Extracted%20files/Trial%20Balances/FI1%20TB%20Mapping%20v2.xlsx?web=1), is available on SharePoint. It is a good starting point for the initial CW1 to TM1 mapping, but it must be reviewed before it is used. `[CM-09]`

##### Responsibility

- TM1 administrator: prepares the CW1 to TM1 ledger mapping file. `[CM-06]`

##### Summary

| **Step** | **Description** |
|---|---|
| Prepare the Mapping File | • Start from the example mapping file (**FI1 TB Mapping v2**) on SharePoint.<br>• Prepare the CW1 to TM1 mapping for the entity. |
| Review the Mapping File | • Review the mapping before it is used. `[CM-06]` |
| Handoff to the OB File | • The reviewed mapping file supplies the initial D365 mapping for the OB file.<br>• The Ledger Owner uses it in [4.1 Complete the TB OB Tab](#41-complete-the-tb-ob-tab). |

### 2. Analyze the CW1 Closing Trial Balance

> Off-system: this activity is completed outside D365, in TM1.

##### Task Overview

Run the CW1 closing TB in TM1 and analyze the accounts, to find how each balance is migrated. The analysis identifies four groups of accounts: the accounts to upload to the subledger, the accounts that need a breakdown, the SPE accounts that need a special FX rate, and the monetary items to revalue (see [Account Groups for the Migration](#account-groups-for-the-migration)). For every account identified, a detailed and reconciled breakdown of the closing balance is required.

The example below shows a TM1 closing TB annotated with the migration status of each account. `[CM-37]`

*[Screenshot: TM1 closing trial balance by entity (SDT, ZA8, FI1) with a migration status note against each account, such as SPE, PPE upload or File ready. Staff names are masked.]*

##### Responsibility

- Ledger Owner (LO): runs and analyzes the CW1 closing TB in TM1. `[CM-11]`
- Reporting team: prepares detailed, reconciled breakdowns of the closing balances, and provides the pending items in the AMCS upload format. `[CM-12]`

##### Summary

| **Step** | **Description** |
|---|---|
| Run the Closing TB | • Run the CW1 closing TB in TM1. `[CM-11]` |
| Identify the SL Accounts | • Identify the accounts whose balances are uploaded to the SL: trade receivables, trade creditors, inter-business receivables and payables, subscription billing, prepayments, PPE, leases and banks. |
| Identify the Accounts That Need a Breakdown | • Identify the accounts that need a breakdown for the upload, and the basis of each breakdown: see [Breakdowns Required](#breakdowns-required). |
| Identify the SPE Accounts | • Identify the accounts that need a special FX rate for conversion to reporting currency. These are the SPE balances: see [6. Upload the SPE Balances at Historical Rates](#6-upload-the-spe-balances-at-historical-rates). |
| Identify the Monetary Items to Revalue | • Identify the monetary items that need to be revalued.<br>• Separate the last CW1 revaluation from the SL and GL opening balance: it is uploaded as a separate transaction, which is then reversed in the month of migration. `[CM-13]` |
| Obtain the Reconciled Breakdowns | • For every account identified, obtain a detailed, reconciled breakdown of the closing balance from the Reporting team, with the pending items in the AMCS upload format. `[CM-12]`<br>• For P&L accounts there is little to do, unless D365 dimensions are needed for balances that pre-date D365. For items held in the functional currency that need no revaluation or settlement, uploading the closing balance is sufficient. |
| Handoff to the Breakdown Files | • The migration status of each account (for example, SPE, PPE upload or file ready).<br>• Continue to [3. Prepare the Breakdown Files](#3-prepare-the-breakdown-files). |

### 3. Prepare the Breakdown Files

> Off-system: this activity is completed outside D365, in Excel.

##### Task Overview

Prepare the required breakdowns on the AMCS template, adding extra tabs for the supporting workings. Breakdown files can be grouped by level 4 account, and every breakdown is checked against the TM1 balance. Transactions that need to be reversed once the balances are in D365 are highlighted in red; they are booked in D365 in [7. Book the Post-Upload Adjustment Journals](#7-book-the-post-upload-adjustment-journals).

The example below shows a breakdown on the AMCS template, with an item to be reversed highlighted in red. `[CM-37]`

*[Screenshot: AMCS multi-ledger journal import template populated with breakdown lines, with one rounding variance line highlighted in red and the total checked to the TM1 balance. Customer codes are masked.]*

##### Responsibility

- Ledger Owner (LO): prepares the breakdown files.
- Regional Accounting Manager (RAM): reviews the breakdown files.

##### Summary

| **Step** | **Description** |
|---|---|
| Prepare Each Breakdown File | Each breakdown file contains:<br>• A TM1 report showing the closing balances being migrated.<br>• A support tab showing how the breakdown was prepared, which also provides support for audit purposes.<br>• The final breakdown on the AMCS template, ready for upload. `[CM-12]` |
| Check to TM1 | • Check every breakdown against the TM1 balance. |
| Highlight the Items to Reverse | • Highlight in red the transactions that need to be reversed once the balances are in D365, for example unrealized FX, rounding differences and write-offs.<br>• All highlighted items are combined into a single journal, which is reversed in D365: see [7. Book the Post-Upload Adjustment Journals](#7-book-the-post-upload-adjustment-journals). `[CM-14]` |
| Review the Breakdown File | • The RAM reviews each breakdown file.<br>• Add a comment to the name of each file showing its review status, so that the review can be tracked. `[CM-15]` |
| Handoff to the OB File | • Reviewed breakdown files, checked to TM1.<br>• Continue to [4. Prepare the Opening Balance File](#4-prepare-the-opening-balance-file). |

### 4. Prepare the Opening Balance File

> Off-system: this activity is completed outside D365, in Excel, in the OB workbook.

##### Description

Once all the breakdowns are complete, prepare the OB file: one OB workbook per entity. The workings tab, Tab 2, is named with the D365 company code (for example, **234A TB OB**) and is the most important tab. Once it is complete, its data flows by formula to Tab 1, **AMCSMultiLedgerJournalImport_GL**, which is the file uploaded to D365. The tabs are described in [Opening Balance Workbook](#opening-balance-workbook).

##### Responsibility

- Ledger Owner (LO): prepares the OB workbook.

##### Initiation

- All the breakdown files are complete ([3. Prepare the Breakdown Files](#3-prepare-the-breakdown-files)).

##### Topic Overview

This topic includes these steps:

| **Step** | **Description** |
|---|---|
| [4.1 Complete the TB OB Tab](#41-complete-the-tb-ob-tab) | Complete each column of the TB OB tab, and check that every line passes the FD Check. Output: a TB OB tab that balances. |
| [4.2 Add Breakdown Lines](#42-add-breakdown-lines) | Required only when an account is uploaded in more detail than its TM1 closing balance; otherwise, go to [4.3 Complete the AMCS Upload Tab](#43-complete-the-amcs-upload-tab). Output: breakdown lines that add up to the TM1 balance. |
| [4.3 Complete the AMCS Upload Tab](#43-complete-the-amcs-upload-tab) | Extend the AMCS rows to every TB OB line, and check the totals. Output: an OB file ready for upload to D365. |

#### 4.1 Complete the TB OB Tab

##### Procedure

Complete these steps to fill in the TB OB tab:

| **Action** | **Description** |
|---|---|
| *PROCESS START* | *Pre-requisites:*<br>• The OB workbook for the entity, with its tabs in the order set out in [Opening Balance Workbook](#opening-balance-workbook).<br>• The TM1 TB report of the balances to be migrated, and the reviewed CW1 to TM1 ledger mapping file ([1. Map the CW1 Ledger to TM1](#1-map-the-cw1-ledger-to-tm1)).<br>• The reviewed breakdown files ([3. Prepare the Breakdown Files](#3-prepare-the-breakdown-files)).<br>*Responsibility:*<br>• Ledger Owner (LO) |
| 1. *Refresh* the **CW1 CoA Structure** tab. | Tab 3 is the TM1 report of the CW1 chart of accounts structure. Refresh the TM1 report if new accounts need to be added. |
| 2. *Update* the **D356 CoA** tab. | Tab 4 is the D365 chart of accounts. Update it with the latest D365 report to include any new accounts. `[CM-16]` |
| 3. *Update* the **New dimensions** tab. | Tab 6 lists the new **BusinessUnit** and **Product** dimension values to be created in D365. Update it to include any new dimensions. |
| 4. *Check* the **TB TM1** tab. | Tab 7 (**TB TM1 &lt;period>**, for example **TB TM1 P03**) is the TM1 TB report by CW1 company. Check that the check row **All N Elements with FCTR** is zero for each company. |
| 5. *Open* the **TB OB** tab. | Open Tab 2, **&lt;company code> TB OB** (for example, **234A TB OB**). Row 1 labels the source of each column, and row 2 holds the column headers. |
| 6. *Paste* the **TM1 Balances**. | From the TM1 report, paste **GL Account** and **GL Description** (columns A and B), and the TM1 closing balance (column D, headed with the CW1 company code, for example **FI1**), as values only.<br>The balances are hard-coded so that breakdown lines can be added ([4.2 Add Breakdown Lines](#42-add-breakdown-lines)). Column C (**CW1 Level 6**) looks up the CW1 level 6 account on the **CW1 CoA Structure** tab. |
| 7. *Enter* the **D365 GL account** (column E). | Enter the initial D365 mapping from the CW1 to TM1 ledger mapping file (**From Adam's file**).<br>Columns F to H look up the **D356 CoA** tab: **D365 Name**, **Does manual entry need to be enabled?** and **D365 Level 6**.<br>Column K (**TM1 Mapping**, from the mapping file) can be ignored. It describes the mechanism used to map the D365 balances back to CW1, for example one-to-one or account + TP. |
| 8. *Check* the **Level 6 check** (column I). | Column I shows **YES** if the CW1 Level 6 (column C) equals the D365 Level 6 (column H). Review any line that does not show **YES**. |
| 9. *Check* the **Account Name Check** (column J). | Column J shows **YES** if the CW1 and D365 account names share enough key words, that is, the word-match score is at or above the **Name match threshold** in cell J92 (default **0.5**). This is a sense check only. `[CM-19]` |
| 10. *Check* **Does manual entry need to be enabled?** (column G). | Column G shows the D365 **Do not allow manual entry** flag. If it is **Yes**, manual entry must be enabled on that main account in D365 before the upload. `[CM-17]` |
| 11. *Enter* the **Dimensions** (columns Q to U). | Enter **BU**, **CC**, **Product**, **Activity** and **TP** for each line. Columns L to P show the allowed values or ranges for each dimension of the D365 account, for example **10000** or **10000..99998**. **Not found** means there is no active structure for the account.<br>• P&L lines: use CC **50005** - Finance, to offset the CW1 Finance department (870) used for the reversal in [5. Reverse the Balances in CW1](#5-reverse-the-balances-in-cw1). `[CM-18]` Revenue accounts use CC **10000**: in the template, revenue and professional-services accounts take CC from column M, because their structure fixes CC 10000. Put the entity's BU (and Product where needed) on P&L lines.<br>• Balance sheet lines: use the default values (BU **9999**, CC **99999**, Product **999999**, Activity **999999**, TP **9999**), unless the structure needs a specific value. |
| 12. *Check* the **FD Check** (column V). | Column V shows **YES** if every dimension in columns Q to U falls within the allowed values in columns L to P. Otherwise it shows **NO:** followed by the failing dimensions. Correct the dimensions until every line shows **YES**. |
| 13. *Check* the **Debit** and **Credit** (columns W and X). | A formula takes the balance from column D: positive balances flow to **Debit** and negative balances to **Credit**. For breakdown lines, see [4.2 Add Breakdown Lines](#42-add-breakdown-lines). |
| 14. *Enter* the **Currency** (column Y). | Enter the ledger (functional) currency. Balances needed in a foreign currency are uploaded separately: upload the functional currency balance first, then book an extra journal that reverses the functional currency amount and replaces it with the transaction currency amounts. `[CM-21]` |
| 15. *Check* the **Description** (column Z). | A formula builds the description: **DD/MM D365 Migration - OB Upload - &lt;CW1 account> - &lt;CW1 description>**. `[CM-20]` |
| 16. *Enter* **FinTag 2 (Vendor name)** (column AA), where needed. | For vendor organizations, enter the vendor name, not the code. |
| 17. *Enter* **FinTag 3 (Customer Code)** (column AB), where needed. | Enter the customer code. Names are not accepted. |
| 18. *Check* the **Check** row and cell **W92**. | The **Check** row below the data sums columns D, W and X: the sum of column D must be **0**. Cell W92 shows total debits less total credits, which must be **0**. `[CM-19]` |
| *STEP COMPLETE* | • The TB OB tab is complete: every line shows **YES** in the FD Check, the sum of column D is 0, and cell W92 is 0.<br>• If an account is uploaded in more detail than its TM1 closing balance, continue to [4.2 Add Breakdown Lines](#42-add-breakdown-lines).<br>• Otherwise, continue to [4.3 Complete the AMCS Upload Tab](#43-complete-the-amcs-upload-tab). |

#### 4.2 Add Breakdown Lines

##### Procedure

Complete these steps to add breakdown lines to the TB OB tab:

| **Action** | **Description** |
|---|---|
| *PROCESS START* | *Pre-requisites:*<br>• An account that is uploaded in more detail than its TM1 closing balance, for example by customer, vendor or transaction ([2. Analyze the CW1 Closing Trial Balance](#2-analyze-the-cw1-closing-trial-balance)).<br>• The reviewed breakdown file for the account ([3. Prepare the Breakdown Files](#3-prepare-the-breakdown-files)).<br>*Responsibility:*<br>• Ledger Owner (LO) |
| 1. *Keep* the **Original Line**. | Keep the account's original TM1 line, with its TM1 balance in column D unchanged. This keeps the column D check (sum of column D = 0) intact. |
| 2. *Enter* the **First Breakdown Item**. | On the original line, overwrite the formula in column W (**Debit**) or X (**Credit**) with the amount of the first breakdown item. |
| 3. *Complete* the **Original Line**. | Complete its dimensions (columns Q to U), description (column Z), and **FinTag 2** / **FinTag 3** (columns AA and AB).<br>Breakdown lines use free text that refers to the specific transaction, for example **DD/MM D365 Migration - &lt;period>-&lt;reference>-MATCH NO. &lt;match no.>**. `[CM-20]` |
| 4. *Insert* a **Row** for each remaining breakdown item. | Insert the rows directly below the original line, with the same CW1 account in column A. `[CM-19]` |
| 5. *Enter* the **Amount** on each inserted row. | Leave column D blank, and enter the amount directly in column W or X. |
| 6. *Complete* each **Inserted Row**. | Complete columns Q to U, Y, Z and AA/AB. |
| 7. *Check* the **Breakdown Total**. | Check that the breakdown lines (the original line plus the inserted rows) add up to the TM1 balance in column D for that account. |
| 8. *Check* cell **W92**. | Check that cell W92 (total debits less total credits) is still **0**, and that the debit and credit totals agree to the column D total. `[CM-19]` |
| *STEP COMPLETE* | • The breakdown lines add up to the TM1 balance of each account, and cell W92 is 0.<br>• Continue to [4.3 Complete the AMCS Upload Tab](#43-complete-the-amcs-upload-tab), where the AMCS rows are extended to the inserted rows. |

#### 4.3 Complete the AMCS Upload Tab

##### Procedure

Complete these steps to complete the AMCS upload tab:

| **Action** | **Description** |
|---|---|
| *PROCESS START* | *Pre-requisites:*<br>• The TB OB tab is complete ([4.1 Complete the TB OB Tab](#41-complete-the-tb-ob-tab)), with any breakdown lines added ([4.2 Add Breakdown Lines](#42-add-breakdown-lines)).<br>*Responsibility:*<br>• Ledger Owner (LO) |
| 1. *Open* the **AMCSMultiLedgerJournalImport_GL** tab. | Tab 1 is the file uploaded to D365. Row 1 holds the import headers, and each row below it is a formula that points to one TB OB row. |
| 2. *Extend* the **AMCS Rows**. | When lines are added to the TB OB tab, extend or copy the AMCS rows so that every TB OB line, including the inserted rows, has a matching AMCS row. Keep the AMCS row references aligned, with no row offsets. |
| 3. *Check* the **Column Links**. | Check that each AMCS row picks up its TB OB row:<br>• **Company**, **CompanyLine**, **OffsetCompanyLine**: the D365 company code.<br>• **AccountType**: **Ledger**.<br>• **AccountNum**: TB OB column E (D365 GL account).<br>• **Dimension1** to **Dimension5**: TB OB columns Q to U (BU, CC, Product, Activity, TP).<br>• **Dimension6**: fixed value **10** (Segment).<br>• **Txt**: TB OB column Z (Description).<br>• **AmountCurDebit**, **AmountCurCredit**: TB OB columns W and X.<br>• **CurrencyCode**: TB OB column Y. |
| 4. *Link* **FinTag2** and **FinTag3**. | FinTag2 and FinTag3 link to TB OB columns AA and AB only on lines where they are needed. Link them on the breakdown lines that you added. |
| 5. *Check* the **TransDate**. | TransDate is the migration date: the first day of the migration month (for example, **01/10/2026**). `[CM-22]` |
| 6. *Leave* the **Unused Columns** blank. | Leave **PostingProfile**, **FinTag1**, **ExchRate**, **ReverseDate** and **ReverseEntry** blank for the OB upload. |
| 7. *Check* the **AMCS Totals**. | Check that total debits equal total credits on the AMCS tab, and that both totals agree to the TB OB totals in columns W and X.<br>**Important:** Do not upload the OB file until every line shows **YES** in the FD Check (column V), the sum of column D in the Check row is **0**, and cell W92 (total debits less total credits) is **0**. |
| *PROCESS COMPLETE* | *Outcomes:*<br>• The OB file is complete and ready for upload to D365: every line shows **YES** in the FD Check, the TB OB checks equal zero, and the AMCS totals agree to the TB OB totals.<br>• <mark>The upload of the OB file to D365 is not described in this guide yet.</mark> `[CM-23]` |

### 5. Reverse the Balances in CW1

> Off-system: this activity is completed outside D365, in CW1, TM1 and Excel.

##### Description

Once the D365 TB has been loaded, reverse the YTD balance in CW1 with an ADAW clear-out journal. Post every line of the clear-out journal to Department 001 (**D365 cutover use only**), for balance sheet and P&L lines in every ledger: see [Department 001 in CW1](#department-001-in-cw1).

The journal is prepared in the ADAW workbook, which holds the evidence for each step (see [ADAW Workbook](#adaw-workbook)). After the journal is posted, the CW1 migration-month TB is confirmed to be nil, and the CW1 feed to TM1 is disconnected from the following month.

##### Responsibility

- Finance Transformation and TM1 administrator: flag the ledgers with CW1 activity in the cutover month.
- Ledger Owner (LO): prepares the clear-out journal, and confirms the CW1 TB.
- CW1 administrator: activates and deactivates Department 001, and imports the journal with the LOs. `[CM-28]`
- TM1 administrator: maintains the TM1 001-only list, and disconnects the CW1 feed to TM1.

##### Initiation

- The D365 TB has been loaded for the entity. `[CM-23]`

##### Topic Overview

This topic includes these steps:

| **Step** | **Description** |
|---|---|
| [5.1 Flag the Ledgers with CW1 Activity in the Cutover Month](#51-flag-the-ledgers-with-cw1-activity-in-the-cutover-month) | Send the list of ledgers that keep CW1 billing or other AR activity to the TM1 administrator. Output: the TM1 001-only list. |
| [5.2 Prepare the ADAW Clear-Out Journal](#52-prepare-the-adaw-clear-out-journal) | Reverse the closing balances on the ADAW template, with every line posted to Department 001. Output: a journal in balance. |
| [5.3 Import the ADAW Journal into CW1](#53-import-the-adaw-journal-into-cw1) | Import the journal into CW1 while Department 001 is active. Output: the posted journal and its CW1 confirmation. |
| [5.4 Confirm the Migration-Month Trial Balance in CW1](#54-confirm-the-migration-month-trial-balance-in-cw1) | At month end, confirm that the CW1 migration-month TB is nil. Output: the post-clearing TB evidence. |
| [5.5 Disconnect the CW1 Feed to TM1](#55-disconnect-the-cw1-feed-to-tm1) | Refresh TM1, and disconnect the CW1 feed from the following month. |

#### 5.1 Flag the Ledgers with CW1 Activity in the Cutover Month

##### Procedure

Complete these steps to flag the ledgers with CW1 activity in the cutover month:

| **Action** | **Description** |
|---|---|
| *PROCESS START* | *Pre-requisites:*<br>• The list of the entity's CW1 ledgers, and the go-live date.<br>*Responsibility:*<br>• Finance Transformation<br>• TM1 administrator |
| 1. *Flag* the **Ledgers**. | Flag the ledgers that will still have CW1 billing or other AR activity in the cutover month, for example A71, A78, A92 and AUY in AU Main Phase 2, and South Africa (SDT). `[CM-25]` |
| 2. *Send* the **Ledger List** to the TM1 administrator. | Send the list to the TM1 administrator. Keep the list: it is not held in the ADAW workbook. |
| 3. *Add* the **Flagged Ledgers** to the TM1 001-only list. | The TM1 administrator adds only the flagged ledgers to the TM1 001-only list. Review and update the list for each go-live. `[CM-25]` |
| *STEP COMPLETE* | • The TM1 001-only list holds only the flagged ledgers. In the cutover month, TM1 keeps only the Department 001 activity on those ledgers (see [CW1 Feed to TM1 Around Go-Live](#cw1-feed-to-tm1-around-go-live)).<br>• Continue to [5.2 Prepare the ADAW Clear-Out Journal](#52-prepare-the-adaw-clear-out-journal). |

#### 5.2 Prepare the ADAW Clear-Out Journal

##### Procedure

Complete these steps to prepare the ADAW clear-out journal:

| **Action** | **Description** |
|---|---|
| *PROCESS START* | *Pre-requisites:*<br>• The workbook **ADAW Journal - Closing out balances for D365.xlsx**. `[CM-09]`<br>• The TM1 TB of the balances to be migrated.<br>*Responsibility:*<br>• Ledger Owner (LO) |
| 1. *Extract* the **Pre-Migration Closing TB** from CW1. | Extract the closing TB for each CW1 company, and keep it behind the **P03 TBs >>** divider tab, one tab per CW1 company (for example, **SDT P03**). |
| 2. *Open* the **ADAW Journal Template A** tab. | It must remain the first tab in the workbook. |
| 3. *Enter* **File**. | In the header row, enter **F**. |
| 4. *Enter* the **Journal Type**. | Enter **GJL**, or **RJL** with a **Reversing Date**. `[CM-26]` |
| 5. *Enter* the **Post Date**. | Enter the last day of the month, in **yyyymmdd** format. `[CM-22]` |
| 6. *Enter* the **Journal Description**. | The description must start with **ADAW -**, for example **ADAW - Closing out balances as at &lt;YYYYPP> for D365**. |
| 7. *Add* a **Journal Line** for each account with a balance. | Include only accounts with a balance, and reverse each balance in the opposite direction. Source the balances from the TM1 TB, and cross-check them to the CW1 closing TB extracted in step 1.<br>• Year-start cutover (for example, CCES): tie the journal to the 30 June closing balance.<br>• Mid-year cutover (for example, AU Main Phase 2): tie it to the full TB, including YTD P&L, at the prior month end. |
| 8. *Enter* **Upl**. | The upload indicator. The template **Instructions** say **Upl** must always be **L**, but the migration file lines use **O**. `[CM-27]` |
| 9. *Enter* the **Ref. Line**. | The line reference number. |
| 10. *Enter* the **GL Account**. | The CW1 GL account. |
| 11. *Enter* the **Company Code**. | The CW1 company code (for example, **FI1**). **Branch Code** is optional. |
| 12. *Enter* **Department Code** **001**. | Enter **001** on every line (balance sheet and P&L, in every ledger). Do not use any other department on the clear-out journal: otherwise TM1 drops the line for the flagged ledgers. |
| 13. *Enter* the **Currency**. | The currency code of the balance. |
| 14. *Enter* the **Amount**. | The TB balance with the sign reversed, rounded to 2 decimals. |
| 15. *Enter* the **Journal Line Description**. | It must start with **ADAW -**. |
| 16. *Enter* the **Sub Account** values, if required. | Optional: **Sub Account Type 1** / **Value 1** and **Type 2** / **Value 2**. The types are **ORG** (Organization) and **STR** (Staff and Resources). |
| 17. *Check* the **Journal Lines** are values only. | Journal lines must be values only, because CW1 does not read formulas. Insert any new lines above the check row. |
| 18. *Check* cell **H2**. | Check that cell H2 shows **JOURNAL IS IN BALANCE** before the journal is imported. |
| *STEP COMPLETE* | • The ADAW clear-out journal is prepared and in balance, with every line posted to Department 001.<br>• Continue to [5.3 Import the ADAW Journal into CW1](#53-import-the-adaw-journal-into-cw1). |

#### 5.3 Import the ADAW Journal into CW1

##### Procedure

Complete these steps to import the ADAW journal into CW1:

| **Action** | **Description** |
|---|---|
| *PROCESS START* | *Pre-requisites:*<br>• The ADAW clear-out journal is in balance ([5.2 Prepare the ADAW Clear-Out Journal](#52-prepare-the-adaw-clear-out-journal)).<br>*Responsibility:*<br>• CW1 administrator<br>• Ledger Owner (LO) `[CM-28]` |
| 1. *Extract* the **Migration-Month TB** from CW1. | Confirm that no transactions have been booked in CW1 in the migration month, other than AR activity on the ledgers flagged in [5.1 Flag the Ledgers with CW1 Activity in the Cutover Month](#51-flag-the-ledgers-with-cw1-activity-in-the-cutover-month). Keep the TB behind the **P04 TBs prior clearing >>** divider tab (for example, **SDT pre P04**). `[CM-28]` |
| 2. *Activate* **Department 001**. | Ask the CW1 administrator to activate Department 001. |
| 3. *Navigate* to **ADAW Journal Template A**. | In CW1, *select*: `[CM-28]`<br>• **Manage >**<br>• **General Ledger >**<br>• **Journals >**<br>• **Actions >**<br>• **Upload GL Journals using ADAW >**<br>• **ADAW Journal Template A** |
| 4. *Select* the **ADAW Workbook**. | Select the .xlsx file to import it. CW1 saves the posted file automatically in eDocs. |
| 5. *Untick* the **Mandatory Sub-Account** setting, if the import is rejected. | If the import is rejected because a revenue GL requires a sub-account, untick the mandatory sub-account setting on that GL for the posting, then import the file again (step 4). `[CM-28]` |
| 6. *Copy* the **CW1 Confirmation**. | Copy the CW1 confirmation dialog, including the JE numbers for each company, into the **CW1 Confirmation** tab of the workbook, so that it provides support for audit purposes. |
| 7. *Deactivate* **Department 001**. | Immediately after the posting, the CW1 administrator deactivates Department 001 and restores any sub-account settings that were changed.<br>**Note:** To reverse an ADAW journal, reverse the signs of the amounts in the template and import it again. Any reversal or repost must also use Department 001. |
| *STEP COMPLETE* | • The clear-out journal is posted in CW1 to Department 001, the CW1 Confirmation tab holds the JE numbers, and Department 001 is inactive again.<br>• Continue to [5.4 Confirm the Migration-Month Trial Balance in CW1](#54-confirm-the-migration-month-trial-balance-in-cw1). |

#### 5.4 Confirm the Migration-Month Trial Balance in CW1

##### Procedure

Complete these steps to confirm the migration-month TB in CW1:

| **Action** | **Description** |
|---|---|
| *PROCESS START* | *Pre-requisites:*<br>• The clear-out journal is posted ([5.3 Import the ADAW Journal into CW1](#53-import-the-adaw-journal-into-cw1)).<br>• The migration month has ended.<br>*Responsibility:*<br>• Ledger Owner (LO) |
| 1. *Extract* the **Migration-Month TB** from CW1. | At month end, re-extract the migration-month TB, and keep it behind the **P04 TBs post clearing >>** divider tab (for example, **SDT post P04**). |
| 2. *Confirm* the **TB** is nil. | The only expected balances are that month's AR on the billing ledgers flagged in [5.1 Flag the Ledgers with CW1 Activity in the Cutover Month](#51-flag-the-ledgers-with-cw1-activity-in-the-cutover-month). |
| 3. *Reverse* any **Other Balance** in CW1. | Reverse anything else in CW1, and raise it in D365. `[CM-28]` |
| *STEP COMPLETE* | • The CW1 migration-month TB is nil, apart from the AR on the flagged billing ledgers.<br>• Continue to [5.5 Disconnect the CW1 Feed to TM1](#55-disconnect-the-cw1-feed-to-tm1). |

#### 5.5 Disconnect the CW1 Feed to TM1

##### Procedure

Complete these steps to disconnect the CW1 feed to TM1:

| **Action** | **Description** |
|---|---|
| *PROCESS START* | *Pre-requisites:*<br>• The CW1 migration-month TB is confirmed ([5.4 Confirm the Migration-Month Trial Balance in CW1](#54-confirm-the-migration-month-trial-balance-in-cw1)).<br>*Responsibility:*<br>• TM1 administrator |
| 1. *Refresh* **TM1**. | Refresh TM1 and confirm the results. |
| 2. *Disconnect* the **CW1 Feed**. | Disconnect the CW1 feed to TM1 from the following month (see [CW1 Feed to TM1 Around Go-Live](#cw1-feed-to-tm1-around-go-live)). |
| *PROCESS COMPLETE* | *Outcomes:*<br>• The CW1 balances are cleared out with the ADAW journal, and the CW1 migration-month TB is nil apart from the AR on the flagged ledgers.<br>• The CW1 feed to TM1 is disconnected from the month after the cutover month. |

### 6. Upload the SPE Balances at Historical Rates

##### Description

As part of the TB upload, balances are uploaded in the entity's functional currency. For SPE accounts, the historical rates in the SPE table are preserved with a separate journal: it reverses the SPE balance in functional currency and rebooks it in the respective currencies at the historical rates, and the difference in reporting currency is posted to FCTR (**314200**).

So that this journal can be posted, two D365 settings are changed manually and temporarily, and reverted immediately after the journal is posted. See [SPE Balances and Temporary D365 Settings](#spe-balances-and-temporary-d365-settings).

##### Responsibility

- Ledger Owner (LO): prepares the SPE workings and journal from the SPE table. `[CM-29]`
- Owner of the D365 settings, <mark>to be confirmed</mark> `[CM-30]`: changes the D365 settings and reverts them.

##### Initiation

- The SPE workings and journal are ready to post, as part of the TB upload. `[CM-29]`

##### Topic Overview

This topic includes these steps:

| **Step** | **Description** |
|---|---|
| [6.1 Change the Maximum Penny-Rounding Difference](#61-change-the-maximum-penny-rounding-difference) | Raise the maximum penny-rounding difference in the reporting currency to the calculated value. |
| [6.2 Redirect the Penny Difference Posting Account](#62-redirect-the-penny-difference-posting-account) | Post reporting currency penny differences to 314200 - Foreign Currency Translation Reserve. Then post the SPE journal. |
| [6.3 Revert the Original Configuration](#63-revert-the-original-configuration) | Immediately after the SPE journal is posted, set both settings back. Output: the original configuration. |

> **Important:** These settings are temporary and must be reverted. Immediately after the SPE journal is posted, **Maximum penny-rounding difference in the reporting currency** must be set back to **10.00** (USD), and the reporting currency posting account must be set back to **551404** - Rounding Difference Reporting Currency.

#### 6.1 Change the Maximum Penny-Rounding Difference

##### Procedure

Complete these steps to change the maximum penny-rounding difference: `[CM-37]`

| **Action** | **Description** |
|---|---|
| *PROCESS START* | *Pre-requisites:*<br>• The calculated value: the difference between the SPE accounts converted to reporting currency at the migration-date rate and their values in reporting currency at historical rates (SPE workings). `[CM-29]`<br>*Responsibility:*<br>• Owner of the D365 settings, <mark>to be confirmed</mark> `[CM-30]` |
| 1. *Check* the **Entity**. | Confirm you are signed into the correct **Legal Entity** (top-right). |
| 2. *Click* **Modules**. | From the left-hand **Navigation Pane**, click **Modules**. |
| 3. *Navigate* to the **General ledger parameters** page. | From the **Navigation Pane**, *select*:<br>• **General ledger >**<br>• **Ledger setup >**<br>• **General ledger parameters**<br>*[Screenshot: D365 Finance and Operations menu with General ledger selected and Ledger setup expanded, highlighting General ledger parameters.]* |
| 4. *Click* the **Ledger** tab. | Click **Ledger**. |
| 5. *Enter* **Maximum penny-rounding difference in the reporting currency**. | Change the value from **10.00** to the calculated value. `[CM-31]`<br>*[Screenshot: General ledger parameters, Ledger tab, with the Maximum penny-rounding difference in the reporting currency field highlighted.]* |
| 6. *Click* **Save**. | Save your changes. |
| *STEP COMPLETE* | • **Maximum penny-rounding difference in the reporting currency** is set to the calculated value.<br>• Continue to [6.2 Redirect the Penny Difference Posting Account](#62-redirect-the-penny-difference-posting-account). |

#### 6.2 Redirect the Penny Difference Posting Account

##### Procedure

Complete these steps to redirect the penny difference posting account:

| **Action** | **Description** |
|---|---|
| *PROCESS START* | *Pre-requisites:*<br>• The maximum penny-rounding difference is changed ([6.1 Change the Maximum Penny-Rounding Difference](#61-change-the-maximum-penny-rounding-difference)).<br>*Responsibility:*<br>• Owner of the D365 settings, <mark>to be confirmed</mark> `[CM-30]` |
| 1. *Check* the **Entity**. | Confirm you are signed into the correct **Legal Entity** (top-right). |
| 2. *Click* **Modules**. | From the left-hand **Navigation Pane**, click **Modules**. |
| 3. *Navigate* to the **Accounts for automatic transactions** page. | From the **Navigation Pane**, *select*:<br>• **General ledger >**<br>• **Posting setup >**<br>• **Accounts for automatic transactions**<br>*[Screenshot: D365 Finance and Operations menu with General ledger selected and Posting setup expanded, highlighting Accounts for automatic transactions.]* |
| 4. *Click* **Edit**. | Click **Edit** at the top of the page. |
| 5. *Enter* the **Main account** for **Penny difference in reporting currency**. | Change the main account from **551404** - Rounding Difference Reporting Currency to **314200** - Foreign Currency Translation Reserve.<br>*[Screenshot: Accounts for automatic transactions with the Edit button highlighted, and Penny difference in reporting currency set to main account 314200, Foreign Currency Translation Reserve.]* |
| 6. *Click* **Save**. | Save the change.<br>*[Screenshot: Accounts for automatic transactions toolbar with the Save button highlighted.]* |
| *STEP COMPLETE* | • **Penny difference in reporting currency** posts to **314200** - Foreign Currency Translation Reserve.<br>• Post the SPE journal. `[CM-29]`<br>• Immediately after the SPE journal is posted, continue to [6.3 Revert the Original Configuration](#63-revert-the-original-configuration). |

#### 6.3 Revert the Original Configuration

##### Procedure

Complete these steps to revert the original configuration:

| **Action** | **Description** |
|---|---|
| *PROCESS START* | *Pre-requisites:*<br>• The SPE journal is posted.<br>*Responsibility:*<br>• Owner of the D365 settings, <mark>to be confirmed</mark> `[CM-30]` |
| 1. *Check* the **Entity**. | Confirm you are signed into the correct **Legal Entity** (top-right). |
| 2. *Click* **Modules**. | From the left-hand **Navigation Pane**, click **Modules**. |
| 3. *Navigate* to the **General ledger parameters** page. | From the **Navigation Pane**, *select*:<br>• **General ledger >**<br>• **Ledger setup >**<br>• **General ledger parameters** |
| 4. *Click* the **Ledger** tab. | Click **Ledger**. |
| 5. *Enter* **Maximum penny-rounding difference in the reporting currency**. | Set the value back to **10.00** (USD). `[CM-31]` |
| 6. *Click* **Save**. | Save your changes. |
| 7. *Navigate* to the **Accounts for automatic transactions** page. | From the **Navigation Pane**, *select*:<br>• **General ledger >**<br>• **Posting setup >**<br>• **Accounts for automatic transactions** |
| 8. *Click* **Edit**. | Click **Edit** at the top of the page. |
| 9. *Enter* the **Main account** for **Penny difference in reporting currency**. | Change the main account back to **551404** - Rounding Difference Reporting Currency. |
| 10. *Click* **Save**. | Save the change. |
| *PROCESS COMPLETE* | *Outcomes:*<br>• The SPE journal is posted at historical rates, with the reporting currency difference in FCTR (314200).<br>• **Maximum penny-rounding difference in the reporting currency** is back to 10.00 (USD), and **Penny difference in reporting currency** posts to 551404 - Rounding Difference Reporting Currency again. |

### 7. Book the Post-Upload Adjustment Journals

##### Description

Once the opening TB has been uploaded to D365, book adjustment journals in D365 for the items identified during the breakdown work and highlighted in red in the breakdown files ([3. Prepare the Breakdown Files](#3-prepare-the-breakdown-files)). These include unrealized FX and revaluation amounts to be reversed, rounding differences to be written off, write-offs needed, and other reconciling items to be cleared.

Booking them as separate, reviewed journals keeps each adjustment traceable to its breakdown file and its supporting workings. `[CM-14]`

##### Responsibility

- Ledger Owner (LO): prepares the adjustment journals in D365.
- Regional Accounting Manager (RAM): reviews the adjustment journals before posting.

##### Initiation

- The TB/OB upload is posted in D365, in the migration month. `[CM-32]`

##### Procedure

Complete these steps to book the post-upload adjustment journals:

| **Action** | **Description** |
|---|---|
| *PROCESS START* | *Pre-requisites:*<br>• The TB/OB upload is posted in D365.<br>• The breakdown files, with the items to reverse highlighted in red ([3. Prepare the Breakdown Files](#3-prepare-the-breakdown-files)).<br>*Responsibility:*<br>• Ledger Owner (LO): prepares<br>• Regional Accounting Manager (RAM): reviews |
| 1. *Collect* the **Highlighted Items**. | From the breakdown files, collect the items highlighted in red: unrealized FX and revaluation amounts to be reversed, rounding differences to be written off, write-offs needed, and other reconciling items to be cleared. |
| 2. *Prepare* the **Adjustment Journals** in D365. | Prepare the journals in the migration month, so that they are included in the post go-live check ([8. Check the D365 Trial Balance After Go-Live](#8-check-the-d365-trial-balance-after-go-live)). Keep each journal traceable to its breakdown file and supporting workings.<br><mark>The D365 steps to prepare and post these journals are to be confirmed.</mark> `[CM-32]` |
| 3. *Review* the **Adjustment Journals**. | The RAM reviews the journals before they are posted. |
| 4. *Post* the **Adjustment Journals**. | Post the reviewed journals in the migration month. `[CM-32]` |
| *PROCESS COMPLETE* | *Outcomes:*<br>• The adjustment journals are reviewed and posted in D365 in the migration month, each traceable to its breakdown file and supporting workings. |

### 8. Check the D365 Trial Balance After Go-Live

##### Description

After go-live, check that the TB in D365 equals the balances that were intended to be migrated. The check confirms that every opening balance, migration journal and subledger upload has been booked once, to the right account and with the right dimensions, before the first D365 month-end close. `[CM-08]`

Investigate and correct any difference before the first D365 month-end close, so that the first close starts from balances that agree to the intended migration balances.

##### Responsibility

- Ledger Owner (LO): prepares the post go-live reconciliation.
- Regional Accounting Manager (RAM): reviews the reconciliation.

##### Initiation

- The entity has gone live in D365, and the migration journals are posted.

##### Topic Overview

This topic includes these steps:

| **Step** | **Description** |
|---|---|
| [8.1 Extract the D365 Trial Balance](#81-extract-the-d365-trial-balance) | Extract the D365 TB as at the migration date. Output: the D365 TB. |
| [8.2 Compare with the Intended Migration Balances](#82-compare-with-the-intended-migration-balances) | Compare the D365 TB with the TB OB tab and the AMCS upload, by D365 main account. Output: every difference explained. |
| [8.3 Reconcile the Migration Journals](#83-reconcile-the-migration-journals) | Reconcile each migration journal to its workings. |
| [8.4 Check the Subledger Balances](#84-check-the-subledger-balances) | Check the GL upload, reversal and SL re-upload of each SL balance. |
| [8.5 Check the Reporting Currency Balances](#85-check-the-reporting-currency-balances) | Check the reporting currency balances, and that the temporary D365 settings were reverted. |
| [8.6 Confirm the CW1 Side and Sign Off](#86-confirm-the-cw1-side-and-sign-off) | Confirm the CW1 side, then save, review and sign off the reconciliation. Output: the signed-off reconciliation. |

#### 8.1 Extract the D365 Trial Balance

##### Procedure

Complete these steps to extract the D365 trial balance:

| **Action** | **Description** |
|---|---|
| *PROCESS START* | *Pre-requisites:*<br>• The OB upload and the migration journals are posted in D365.<br>*Responsibility:*<br>• Ledger Owner (LO) |
| 1. *Check* the **Entity**. | Confirm you are signed into the correct **Legal Entity** (top-right). |
| 2. *Click* **Modules**. | From the left-hand **Navigation Pane**, click **Modules**. |
| 3. *Open* the **Trial Balance**. | Open the D365 TB for the entity. `[CM-33]` |
| 4. *Enter* the **Migration Date**. | Run the TB as at the migration date. |
| 5. *Select* the **Ledger Currency**. | Run it in the ledger (functional) currency. |
| 6. *Select* the **Main Account** and **Dimensions**. | Run it by main account and, where relevant, by the dimensions used in the upload (columns Q to U of the TB OB tab). |
| 7. *Extract* the **Trial Balance**. | Extract the TB for the comparison. `[CM-33]` |
| *STEP COMPLETE* | • The D365 TB for the entity is extracted as at the migration date.<br>• Continue to [8.2 Compare with the Intended Migration Balances](#82-compare-with-the-intended-migration-balances). |

#### 8.2 Compare with the Intended Migration Balances

##### Procedure

Complete these steps to compare the D365 TB with the intended migration balances:

| **Action** | **Description** |
|---|---|
| *PROCESS START* | *Pre-requisites:*<br>• The D365 TB ([8.1 Extract the D365 Trial Balance](#81-extract-the-d365-trial-balance)).<br>• The OB file ([4. Prepare the Opening Balance File](#4-prepare-the-opening-balance-file)).<br>*Responsibility:*<br>• Ledger Owner (LO) |
| 1. *Compare* the **D365 TB** with the intended migration balances. | The intended balances are the TM1 debit and credit balances in columns W and X of the TB OB tab, and the lines in Tab 1 (AMCS upload). |
| 2. *Trace* each **D365 Balance** to its CW1 and TM1 account. | Compare by D365 main account, using the CW1/TM1 mapping in the OB file (column E, checked against the D365 CoA in columns F to H). |
| 3. *Explain* each **Difference**. | The expected difference is zero. Document and explain every difference in the reconciliation workbook, with a reference to the journal or breakdown file that causes it. `[CM-34]` |
| *STEP COMPLETE* | • The D365 TB is compared with the intended migration balances, and every difference is documented.<br>• Continue to [8.3 Reconcile the Migration Journals](#83-reconcile-the-migration-journals). |

#### 8.3 Reconcile the Migration Journals

##### Procedure

The comparison must cover everything booked as part of the migration, not only the OB upload. Some of these journals are expected to change the net balance against the intended OB; others should have no net effect in functional currency.

Complete these steps to reconcile each migration journal to its workings:

| **Action** | **Description** |
|---|---|
| *PROCESS START* | *Pre-requisites:*<br>• The comparison of the D365 TB with the intended balances ([8.2 Compare with the Intended Migration Balances](#82-compare-with-the-intended-migration-balances)).<br>• The workings for each migration journal.<br>*Responsibility:*<br>• Ledger Owner (LO) |
| 1. *Reconcile* the **OB Upload**. | The OB upload (Tab 1, AMCS upload) forms the intended balance. It should agree line by line to the TB OB tab (columns W and X). Reconcile it to the OB file, Tabs 1 and 2. |
| 2. *Reconcile* the **Separate Revaluation Transaction**. | Together with the OB upload, it brings the revalued monetary items back to the TM1 closing balance. Reconcile it to the last CW1 revaluation. `[CM-13]` |
| 3. *Reconcile* the **Revaluation Reversal**. | The reversal of the revaluation in the migration month is expected to change the net balance against the intended OB by the amount of the last CW1 revaluation. Reconcile it to the last CW1 revaluation. |
| 4. *Reconcile* the **Foreign Currency Replacement Journal**. | The journal for balances needed in a foreign currency (column Y) has no net change in functional currency: the functional currency amount is reversed and rebooked in transaction currency. Reconcile it to the foreign currency workings. |
| 5. *Reconcile* the **SPE Historical-Rate Journal**. | The SPE journal ([6. Upload the SPE Balances at Historical Rates](#6-upload-the-spe-balances-at-historical-rates)) has no net change in functional currency. In reporting currency, the difference is posted to FCTR (314200). Reconcile it to the SPE workings and the SPE table. |
| 6. *Reconcile* the **Combined Reversal Journal**. | The journal for the items highlighted in red ([3. Prepare the Breakdown Files](#3-prepare-the-breakdown-files)), booked and reviewed in [7. Book the Post-Upload Adjustment Journals](#7-book-the-post-upload-adjustment-journals), is expected to change the net balance by the total of the highlighted items (unrealized FX, rounding differences and write-offs). Reconcile it to the breakdown files (items in red). `[CM-14]` |
| *STEP COMPLETE* | • Each migration journal is reconciled to its workings.<br>• Continue to [8.4 Check the Subledger Balances](#84-check-the-subledger-balances). |

#### 8.4 Check the Subledger Balances

##### Procedure

SL balances need special attention because each one passes through three postings: the balance is first uploaded to the GL as part of the OB, that GL upload is then reversed, and the balance is re-uploaded to the SL. An error at any stage can leave a balance counted twice, a reversal missing, or a GL control account that no longer agrees with its subledger. `[CM-24]`

Complete these steps for each SL account:

| **Action** | **Description** |
|---|---|
| *PROCESS START* | *Pre-requisites:*<br>• The SL accounts identified in [2. Analyze the CW1 Closing Trial Balance](#2-analyze-the-cw1-closing-trial-balance): trade receivables, trade creditors, inter-business receivables and payables, subscription billing, prepayments, PPE, leases and banks.<br>*Responsibility:*<br>• Ledger Owner (LO) |
| 1. *Check* the **GL Upload**. | Agree the SL account balance uploaded to the GL as part of the OB to the TB OB tab of the OB file. Expected result: it agrees to the intended balance. |
| 2. *Check* the **GL Reversal**. | Compare the reversal of the GL upload with the GL upload. Expected result: they net to zero, with no double count and no missing reversal. |
| 3. *Check* the **SL Re-Upload**. | Compare the balance re-uploaded to the SL with the intended balance. Expected result: the SL re-upload equals the intended balance. |
| 4. *Check* the **GL Control Account** against the SL detail. | Compare the D365 GL control account with the SL detail or aging report (customer, vendor, fixed asset, bank, lease), and check the counts and totals by customer and vendor against the breakdown files. Expected result: the GL control account equals the SL report, and the counts and totals agree to the breakdown files. |
| 5. *Check* the **Dimensions** and **FinTags**. | Check the dimensions on each SL balance, FinTag 2 (vendor name) and FinTag 3 (customer code). Expected result: the dimensions are valid for the account structure, FinTag 2 holds vendor names, and FinTag 3 holds customer codes. |
| *STEP COMPLETE* | • Each SL balance is uploaded, reversed and re-uploaded once, and each GL control account agrees to its subledger.<br>• Continue to [8.5 Check the Reporting Currency Balances](#85-check-the-reporting-currency-balances). |

#### 8.5 Check the Reporting Currency Balances

##### Procedure

Complete these steps to check the reporting currency balances:

| **Action** | **Description** |
|---|---|
| *PROCESS START* | *Pre-requisites:*<br>• The SL balances are checked ([8.4 Check the Subledger Balances](#84-check-the-subledger-balances)).<br>*Responsibility:*<br>• Ledger Owner (LO) |
| 1. *Check* the **Reporting Currency Balances**. | Balances should be converted at the migration-month rate, except SPE balances, which should carry the historical rates from the SPE table, with the difference posted to FCTR (314200), as described in [6. Upload the SPE Balances at Historical Rates](#6-upload-the-spe-balances-at-historical-rates). |
| 2. *Confirm* the **Maximum Penny-Rounding Difference** is reverted. | **Maximum penny-rounding difference in the reporting currency** is back to **10.00** (USD): see [6.3 Revert the Original Configuration](#63-revert-the-original-configuration). |
| 3. *Confirm* the **Posting Account** is reverted. | The main account for **Penny difference in reporting currency** is back to **551404** - Rounding Difference Reporting Currency. |
| *STEP COMPLETE* | • The reporting currency balances are as expected, and the temporary D365 settings are reverted.<br>• Continue to [8.6 Confirm the CW1 Side and Sign Off](#86-confirm-the-cw1-side-and-sign-off). |

#### 8.6 Confirm the CW1 Side and Sign Off

##### Procedure

Complete these steps to confirm the CW1 side and sign off the reconciliation:

| **Action** | **Description** |
|---|---|
| *PROCESS START* | *Pre-requisites:*<br>• The reporting currency balances are checked ([8.5 Check the Reporting Currency Balances](#85-check-the-reporting-currency-balances)).<br>• The CW1 migration-month TB ([5.4 Confirm the Migration-Month Trial Balance in CW1](#54-confirm-the-migration-month-trial-balance-in-cw1)).<br>*Responsibility:*<br>• Ledger Owner (LO): prepares<br>• Regional Accounting Manager (RAM): reviews |
| 1. *Confirm* the **CW1 Migration-Month TB**. | Confirm that the re-extracted CW1 migration-month TB nets to zero after the ADAW reversal (the **P04 TBs post clearing >>** tabs of the ADAW workbook, [5.4 Confirm the Migration-Month Trial Balance in CW1](#54-confirm-the-migration-month-trial-balance-in-cw1)). The only expected differences are AR-related transactions where CW1 is the billing engine. |
| 2. *Save* the **Reconciliation Workbook**. | Save the reconciliation workbook together with its supporting workings, so that it also provides support for audit purposes. `[CM-34]` |
| 3. *Review* the **Reconciliation**. | The RAM reviews the reconciliation prepared by the LO. |
| 4. *Add* the **Review Status** to the file name. | As for the breakdown files, add a comment to the file name showing its review status, so that the review can be tracked. `[CM-15]` |
| *PROCESS COMPLETE* | *Outcomes:*<br>• The D365 TB at the migration date is reconciled to the intended migration balances (TB OB tab and AMCS upload), covering all migration journals and the SL GL upload, reversal and re-upload, with every difference explained.<br>• The reconciliation is reviewed by the RAM, and its review status is in the file name. |

### 9. Complete the Pre Go-Live Checklist

> Off-system: this activity is completed outside D365.

##### Task Overview

Use this checklist to track the completion of each deliverable. Each deliverable links to the topic where it is produced. `[CM-35]`

##### Responsibility

- The owner of each deliverable, as shown in the checklist.

##### Summary

| **Step** | **Description** |
|---|---|
| Track Each Deliverable | • Tick the status box when the deliverable is complete. |
| Confirm Completion | • Every deliverable in the checklist is complete. `[CM-35]` |

##### Checklist

| **#** | **Deliverable** | **Owner** | **Topic** | **Status** |
|---|---|---|---|---|
| 1 | CW1 to TM1 ledger mapping file prepared and reviewed | TM1 administrator `[CM-06]` | [1. Map the CW1 Ledger to TM1](#1-map-the-cw1-ledger-to-tm1) | ☐ |
| 2 | CW1 closing TB in TM1 analyzed (SL uploads, breakdowns, SPE and revaluation) | LO | [2. Analyze the CW1 Closing Trial Balance](#2-analyze-the-cw1-closing-trial-balance) | ☐ |
| 3 | Detailed, reconciled breakdowns of closing balances provided, with pending items in AMCS format | Reporting team | [2. Analyze the CW1 Closing Trial Balance](#2-analyze-the-cw1-closing-trial-balance) | ☐ |
| 4 | Breakdown files prepared on the AMCS template, checked to TM1, with items to reverse highlighted in red | LO | [3. Prepare the Breakdown Files](#3-prepare-the-breakdown-files) | ☐ |
| 5 | Breakdown files reviewed and review status added to each file name | RAM | [3. Prepare the Breakdown Files](#3-prepare-the-breakdown-files) | ☐ |
| 6 | Last CW1 revaluation uploaded as a separate transaction and reversed in the migration month | LO | [2. Analyze the CW1 Closing Trial Balance](#2-analyze-the-cw1-closing-trial-balance) | ☐ |
| 7 | OB file completed (all seven tabs updated, Level 6 and account name checks reviewed, AMCS tab extended to every TB OB line) | LO | [4. Prepare the Opening Balance File](#4-prepare-the-opening-balance-file) | ☐ |
| 8 | FD Check (column V of the TB OB tab) shows YES on every line before upload | LO | [4.1 Complete the TB OB Tab](#41-complete-the-tb-ob-tab) | ☐ |
| 9 | TB OB checks equal zero (sum of column D in the Check row; cell W92, total debits less total credits), and AMCS totals agree to the TB OB totals | LO | [4.3 Complete the AMCS Upload Tab](#43-complete-the-amcs-upload-tab) | ☐ |
| 10 | Foreign currency replacement journal prepared, where needed | LO | [4.1 Complete the TB OB Tab](#41-complete-the-tb-ob-tab) | ☐ |
| 11 | Reversal journal for items highlighted in red prepared for D365 | LO | [7. Book the Post-Upload Adjustment Journals](#7-book-the-post-upload-adjustment-journals) | ☐ |
| 12 | CW1 reversal booked with the ADAW journal and migration-month TB confirmed to net to zero | LO | [5. Reverse the Balances in CW1](#5-reverse-the-balances-in-cw1) | ☐ |
| 13 | CW1 Confirmation tab of the ADAW workbook completed with the JE numbers for each CW1 company | LO | [5.3 Import the ADAW Journal into CW1](#53-import-the-adaw-journal-into-cw1) | ☐ |
| 14 | SPE workings and journal prepared from the SPE table | LO | [6. Upload the SPE Balances at Historical Rates](#6-upload-the-spe-balances-at-historical-rates) | ☐ |
| 15 | D365 settings temporarily changed for the SPE journal, then reverted to the original configuration (maximum penny-rounding difference 10.00 USD; posting account 551404) immediately after posting | <mark>To be confirmed</mark> `[CM-30]` | [6. Upload the SPE Balances at Historical Rates](#6-upload-the-spe-balances-at-historical-rates) | ☐ |
| 16 | Post-upload adjustment journals (FX reversals, rounding write-offs, other) prepared in D365 | LO | [7. Book the Post-Upload Adjustment Journals](#7-book-the-post-upload-adjustment-journals) | ☐ |
| 17 | Adjustment journals reviewed before posting | RAM | [7. Book the Post-Upload Adjustment Journals](#7-book-the-post-upload-adjustment-journals) | ☐ |
| 18 | Post go-live check prepared: D365 TB at the migration date reconciled to the intended migration balances (TB OB tab and AMCS upload), covering all migration journals and the SL GL upload, reversal and re-upload, with any difference explained | LO | [8. Check the D365 Trial Balance After Go-Live](#8-check-the-d365-trial-balance-after-go-live) | ☐ |
| 19 | Post go-live reconciliation reviewed and review status added to the file name | RAM | [8.6 Confirm the CW1 Side and Sign Off](#86-confirm-the-cw1-side-and-sign-off) | ☐ |

---

## Part 3: Reports (CW1 to D365 Migration)

##### Overview

The source manual refers to the following D365 reports, which support the OB file and the post go-live check. The TM1 reports used in topics 2 and 4 (the CW1 closing TB, the CW1 CoA structure and the TB by CW1 company) are run in TM1, outside D365.

> **ACTION: REVIEW REQUIREMENT.** The navigation paths of these reports are not given in the source and are to be confirmed. `[CM-36]`

##### Trial Balance

| **Navigation** | **Description** |
|---|---|
| • <mark>Navigation to be confirmed</mark> `[CM-36]` | The D365 trial balance shows the entity's balances by main account. Run it as at the migration date, in the ledger (functional) currency, by main account and, where relevant, by the dimensions used in the upload (columns Q to U of the TB OB tab). Use it after go-live to check that the D365 balances equal the balances intended to be migrated: see [8.1 Extract the D365 Trial Balance](#81-extract-the-d365-trial-balance). |

##### Chart of Accounts

| **Navigation** | **Description** |
|---|---|
| • <mark>Navigation to be confirmed</mark> | The D365 chart of accounts report lists the main accounts with their **Name**, **Main account category**, **Main account type**, **Posting type**, **Do not allow manual entry** and **Foreign currency revaluation** settings. Use the latest report to update Tab 4 of the OB workbook (**D356 CoA**), so that the lookups in columns F to H of the TB OB tab find any new accounts. Column G uses the **Do not allow manual entry** flag to show whether manual entry must be enabled before the upload. |

##### Ledger Account Structures

| **Navigation** | **Description** |
|---|---|
| • <mark>Navigation to be confirmed</mark> | The D365 ledger account structures define the dimensions required for each account, in the order **MainAccount**, **BusinessUnit**, **CostCenter**, **Product**, **Activity**, **TradingPartner**, **Segment**. They are held in Tab 5 of the OB workbook (**LedgerAccountStructureContains**), where only **Active** structures are used by the lookups. Columns L to P of the TB OB tab show the allowed values for each dimension, and the FD Check (column V) checks the entered dimensions against them. |
