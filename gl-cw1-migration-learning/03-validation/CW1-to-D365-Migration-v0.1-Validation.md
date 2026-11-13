# Validation Register: CW1 to D365 Migration v0.1 (working draft)

| Field | Value |
|---|---|
| Guide (editable source) | [`CLAUDE-TBC-CW1 to D365 Migration PG v0.1.docx`](../01-procedure-guides/CLAUDE-TBC-CW1%20to%20D365%20Migration%20PG%20v0.1.docx) |
| Review PDF | [`CLAUDE-TBC-CW1 to D365 Migration PG v0.1.pdf`](../01-procedure-guides/CLAUDE-TBC-CW1%20to%20D365%20Migration%20PG%20v0.1.pdf) |
| Markdown preview | [`PG-CW1-to-D365-Migration-v0.1-DRAFT.md`](../01-procedure-guides/PG-CW1-to-D365-Migration-v0.1-DRAFT.md) |
| Status | Working draft v0.1 (D-058): the *CW1 to D365 Migration - Go-Live Manual* (version date October 2026) converted to the PG master template. Not shared yet; needs SME review and BPO sign-off. The manual stays the working reference until v0.1 passes its gates. |
| Last updated | 2026-11-13 |
| Items | 37 guide-level items (`CM`), all open: 26 blocking, 11 non-blocking. 96 Word review comments. |

This file is the guide's **question log**. Its items use the prefix `CM` (CW1 Migration), which does not depend on the guide code, so the IDs stay stable when the code is allocated (`CM-01`). Each item that affects the text is a Word review comment by "Validation register" (VR), and every item has at least one comment.

---

## 1. Source

| Source | What this guide takes from it |
|---|---|
| *CW1 to D365 Migration - Go-Live Manual*, version date October 2026, owner Maria Florencia Ruiz (Group Accounting Transformation Lead, WiseTech Global Finance). File `CW1_to_D365_Migration_-_Go-Live_Manual.docx`, supplied by the user on 2026-11-13 and held outside this repository. | Every step, the roles, the glossary, the process overview, the pre go-live checklist and seven screenshots. The manual has no version number and still holds six `[Confirm]` notes, so its content is **reference evidence**: no item closes on it alone, and a test, a recording or an SME answer governs where it disagrees (same rule as D-044). |

---

## 2. Conversion decisions

| # | Decision | Reason |
|---|---|---|
| C1 | Rebuilt in the PG master template with every fixed component kept: cover, contents, version history, *About this guide*, color key, Parts 1 to 3 and *Additional Resources*. | User request: convert the manual into the D365 PG format (T1, T2). |
| C2 | Steps 1 to 8 and the pre go-live checklist become topics 1 to 9, in the manual's order. Topics 4, 5, 6 and 8 are parents with subtopics (4.1 to 4.3, 5.1 to 5.5, 6.1 to 6.3, 8.1 to 8.6); topics 1, 2, 3 and 9 use the off-system pattern; topic 7 is standalone. The Process table has one row per topic. | T2 *Choose the topic structure*: related stages that deliver one outcome are subtopics; work outside D365 uses the off-system pattern. |
| C3 | The manual's reference tables (the TB OB column guide, the AMCS columns, the ADAW header and line fields, the migration bookings and the subledger checks) become **Action / Description** rows, one action per row, with the rule beside the field it governs. No label, value or field is added. | T2 *Write clear procedure rows* and *Separate rules from procedure*. |
| C4 | Rows done outside D365 (Excel, TM1, CW1) are shaded light gray (E7E6E6), as the color key defines; topics 1 to 5 and 9 carry the **Off-system** callout. | Template color key; precedent 220 v3.0. |
| C5 | The standard navigation pattern (*Check* the **Entity**, *Click* **Modules**, *Navigate*) is used for the D365 steps whose path the manual gives (6.1 to 6.3). The CW1 menu path in 5.3 keeps the manual's levels. The D365 trial balance page in 8.1 is not given (`CM-33`). | T2 *Use the standard navigation pattern*. |
| C6 | Each procedure opens with **PROCESS START** and closes with **STEP COMPLETE** (with *Continue to* links) or **PROCESS COMPLETE** (4.3, 5.5, 6.3, 7 and 8.6). Step 6.2 ends with *Post the SPE journal*, which the manual does not describe (`CM-29`). | T2 *Use process boundaries*. |
| C7 | **Ledger Owner (LO)** is used throughout (`CM-05`). 'Adam' is written as the role **TM1 administrator** (`CM-06`); the workbook label *From Adam's file* is kept. The role matrix has six roles; 6.1 to 6.3 are left unmarked until the owner of the D365 settings is confirmed (`CM-30`). | One role name across the Stream table, Process table, role matrix and topics (T2); role names, not people. |
| C8 | Key concepts come only from the manual: its glossary (with BU and TP added from its dimension list), the account groups and breakdown bases of Step 2, the OB workbook tabs and checks, the Department 001 rule, the ADAW workbook, the TM1 feed stages and the SPE background. Each concept uses the form its content needs (D-059): two- and three-column tables (for example **Setting / Normal value / For the SPE journal**), paragraphs, and a bulleted list for the Department 001 rules. | T2 *Key concepts*: no invented terms or rules; adapt the concept table to the information. |
| C9 | The manual's cross-references ("Step 5", "section 4.3") become links to topics. Its numbering conflicts are raised, not repeated (`CM-08`). Step 8 (vi), *Confirm the CW1 side*, repeats Step 5 (step 6), so step 1 of 8.6 checks the result of 5.4 and links to it, instead of repeating the procedure. | T2 *Create or repair an internal hyperlink*; a task appears once (D-045). |
| C10 | The six `[Confirm]` notes are removed from the text and raised as items: `CM-16`, `CM-17`, `CM-20`, `CM-27`, `CM-30` and `CM-32`. | No draft-only notes in the guide text (T2 final checklist). |
| C11 | The manual's seven screenshots are kept beside their text or step, with alt text and without figure numbers, as in the earlier guides. Staff names in the TM1 example and customer codes in the AMCS example are masked (`CM-37`). | Screenshots are optional and must not carry unneeded personal or customer data (T2; README). |
| C12 | Part 3 lists the three D365 reports the manual uses (trial balance, chart of accounts, ledger account structures), each with its own Heading 5 and table; their navigation is to be confirmed (`CM-36`). | T2 *Retain Part 3 Reports*: keep Part 3 and ask the SME when no path is supplied. |
| C13 | Prose is in English (United States): analyze, center, organization, dialog, unrealized. Exact labels are kept, including the template tab name **D356 CoA** (`CM-16`), workbook tab and column names, and the cell text **JOURNAL IS IN BALANCE**. | T2 language rule; README *UI labels match the screen exactly*. |
| C15 | Notes to the author are marked with the template's **ACTION: REVIEW REQUIREMENT** style (D-060): three standalone notes as yellow boxes (the OB and subledger uploads, the unmarked roles for 6.1 to 6.3, the report navigation) and eleven phrases in the linked character style (the settings owner, the OB upload in 4.3, the adjustment journal steps, checklist item 15's owner and the report navigation). Each keeps its review comment. They are removed before publication. | User request; the style is in the master template (T1). |
| C14 | File name `CLAUDE-TBC-CW1 to D365 Migration PG v0.1.docx`: `TBC` until the code is allocated (`CM-01`), and `CLAUDE-` until publication (D-056). Version 0.1, because the manual is unversioned and still has open `[Confirm]` notes (`CM-02`). | Numbering standard; D-056; T2 *Use the actual revision*. |

---

## 3. Source-to-guide mapping

| Manual section | v0.1 location |
|---|---|
| Purpose and scope | Part 1 Part Description |
| Glossary and abbreviations | Part 1 Key concepts: Terms and Abbreviations |
| Roles and responsibilities | Part 1 Stream, Roles and responsibilities; each topic's Responsibility |
| Process overview (phases 1 to 9) | Part 1 Part Description (stages) and Process table |
| Step 1 CW1 to TM1 ledger mapping | Topic 1 |
| Step 2 (2.1 to 2.5) and Figure 1 | Topic 2; Key concepts: Account Groups for the Migration, Breakdowns Required |
| Step 3 (3.1, 3.2) and Figure 2 | Topic 3 |
| Step 4 tab table | Key concepts: Opening Balance Workbook; 4.1 steps 1 to 4 |
| 4.1 Tab 2 TB OB column guide and warning | 4.1; Key concepts: Opening Balance Checks |
| 4.2 Adding breakdown lines | 4.2 |
| 4.3 AMCS upload tab | 4.3 |
| Step 5 introduction and procedure steps 1 to 7 | Topic 5; 5.1 to 5.5; Key concepts: Department 001 in CW1 |
| 5.1 The ADAW workbook | Key concepts: ADAW Workbook |
| 5.2 ADAW journal header; 5.3 ADAW journal lines | 5.2 |
| 5.4 Import into CW1 | 5.3 |
| 5.5 TM1 feed during the cutover month | Key concepts: CW1 Feed to TM1 Around Go-Live; 5.5 |
| Step 6.1 Background; 6.2 Current configuration | Topic 6 Description; Key concepts: SPE Balances and Temporary D365 Settings |
| 6.3 Step (i) and Figures 3, 4 | 6.1 |
| 6.4 Step (ii) and Figures 5 to 7 | 6.2 |
| 6.5 Step (iii) and warning | 6.3; topic 6 Important box |
| Step 7 (7.1 Purpose, 7.2 Timing) | Topic 7 |
| Step 8 (numbered 7.1 to 7.8) | Topic 8; 8.1 (i), 8.2 (ii), 8.3 (iii), 8.4 (iv), 8.5 (v), 8.6 (vi and vii) |
| Pre go-live checklist | Topic 9 |

---

## 4. Guide-level items (`CM`)

**Priority:** **B** = blocks publication. **N** = non-blocking. **Method:** **Test** = test in a clean session (D365, CW1 or the workbook). **SME** = subject-matter expert or process owner. **Dec** = project decision.

| ID | Item to confirm | Location | Priority | Method | Status |
|---|---|---|---|---|---|
| CM-01 | Guide code to be allocated. The source manual has no guide code. The PG authoring guide puts R2R guides in the 400-series of the R2R PG Numbering Standard, which is held outside this repository, and the register owner allocates the code. Until then the working file name uses TBC. | Cover and version history | B | Dec | Open |
| CM-02 | Version 0.1 is a working draft converted from the CW1 to D365 Migration - Go-Live Manual (version date October 2026). The manual has no version number and still holds six [Confirm] notes. Its content is reference evidence and is not validated: check each topic with the SME, and in CW1, TM1 and D365, before use. The manual names Maria Florencia Ruiz (Group Accounting Transformation Lead, WiseTech Global Finance) as its owner: confirm that she is the BPO. Version 0.1 needs BPO sign-off. | Version history | B | SME, Dec | Open |
| CM-03 | Confirm the stream. The source does not name one. This draft uses Record-to-Report (R2R), because the guide migrates general ledger balances. | Part 1 Stream | B | SME | Open |
| CM-04 | Confirm the scope and audience. The manual covers the pre go-live steps for one entity's migration, plus the post-upload journals and the post go-live check. Confirm which entities and go-live waves it applies to (its examples come from FI1, SDT, ZA8, CCES and AU Main Phase 2), and that a procedure guide is the right home for a cutover task that is done once per entity. | Part 1 Part Description | B | SME, Dec | Open |
| CM-05 | Confirm the role name. The manual's Purpose says 'Local Office accountants (LOs)', while its glossary and roles table say 'Ledger Owners (LOs)'. This draft uses Ledger Owner (LO). | Part 1 | B | SME | Open |
| CM-06 | Confirm who prepares and reviews the ledger mapping. The manual names 'Adam' for the CW1 to TM1 mapping file (Step 1, roles table and checklist item 1) and 'Adam Buckle' as the TM1 administrator (Step 5). This draft assumes they are the same person and uses the role TM1 administrator; the workbook label 'From Adam's file' is kept. The manual says the mapping file must be reviewed before it is used, but not by whom. | Part 1; topics 1 and 9 | B | SME | Open |
| CM-07 | Confirm the trigger and timing: what starts the migration for an entity, and when each deliverable is due relative to the go-live date. The manual gives no lead times. | Part 1 Initiation and Process | B | SME | Open |
| CM-08 | Source numbering. The manual's Process overview gives the post go-live check as Step 7, its Step 8 numbers its sections 7.1 to 7.8 (repeating Step 7's 7.1 and 7.2), and its TB OB column guide refers to a 'section 7.4' description prefix that the manual does not contain. This draft numbers the stages as topics 1 to 9 and replaces the section references with links. | Topic 8 (affects all of Part 2) | N | Dec | Open |
| CM-09 | Supply links that intended users can open: the example mapping file FI1 TB Mapping v2 (its SharePoint link is in a Phase 3.3 (WAVE_1) data migration folder: confirm that it is current and accessible), the AMCS template, the OB workbook template, the workbook 'ADAW Journal - Closing out balances for D365.xlsx', the SPE table and the reconciliation workbook. | Part 1 Key concepts; topic 1; 5.2 | N | SME | Open |
| CM-10 | The manual refers to ADO Bug 11817 for the temporary D365 settings. Confirm that users can open the link, or replace it with a user-facing reference. | Part 1 Key concepts | N | Dec | Open |
| CM-11 | Confirm who runs and analyzes the CW1 closing TB in TM1 (the manual's Step 2 names no role; checklist item 2 names the LO), and which TM1 report, period and entity selections are used. | Part 1 Process; topic 2 | B | SME | Open |
| CM-12 | Confirm how the breakdown work is split. Step 2 says the Reporting team prepares detailed, reconciled breakdowns and provides the pending items in the AMCS upload format; Step 3 says the LOs prepare the breakdown files on the AMCS template. Confirm what the Reporting team hands to the LO. | Part 1 Key concepts; topics 2 and 3 | B | SME | Open |
| CM-13 | Confirm how the last CW1 revaluation is separated from the SL and GL opening balance: who prepares the separate transaction, how it is uploaded to D365, and when and how it is reversed in the migration month (checklist item 6). | Part 1 Key concepts; topic 2; 8.3 | B | SME | Open |
| CM-14 | Confirm the journal structure. Step 3 says all items highlighted in red are combined into a single journal, which is reversed in D365; Step 7 says they are booked as separate, reviewed journals. | Topics 3, 7 and 8.3 | B | SME | Open |
| CM-15 | Confirm the file-name convention for the review status (the wording added to the file name after review), and where the breakdown files and the reconciliation workbook are saved. | Topics 3 and 8.6 | N | SME | Open |
| CM-16 | The OB workbook template names Tab 4 'D356 CoA'. The manual asks for it to be renamed 'D365 CoA' in the template. This draft keeps the current tab name. | Part 1 Key concepts; 4.1 | N | Dec | Open |
| CM-17 | Confirm who enables manual entry on a D365 main account when column G shows Yes, and that it is switched back after the upload (source [Confirm]). The D365 steps are not given. | 4.1 | B | SME | Open |
| CM-18 | Conflict: the column guide says P&L lines use CC 50005 - Finance 'to offset the CW1 Finance department (870) used for the reversal in Step 5', but Step 5 posts every line of the clear-out journal to Department 001. Confirm the CC rule for P&L lines, and whether the reference to department 870 is out of date. | 4.1 | B | SME | Open |
| CM-19 | Test the check cells. The Name match threshold is in cell J92, and total debits less total credits is in cell W92. Inserting breakdown lines above row 92 moves these cells. Confirm the cell references to quote (or name the cells), and that the Check row formulas include the inserted rows. | Part 1 Key concepts; 4.1 and 4.2 | N | Test | Open |
| CM-20 | Confirm the description date format: the template formula uses 'DD/MM D365 Migration', while the manual also gives 'DD/MM/YY D365 Migration' (source [Confirm]). | 4.1 and 4.2 | N | Dec | Open |
| CM-21 | Confirm the foreign currency replacement journal: who prepares it, how it is uploaded to D365, and when (column Y; checklist item 10). | 4.1 | B | SME | Open |
| CM-22 | Confirm the dates. The AMCS TransDate is the first day of the migration month (for example, 01/10/2026). The ADAW Post Date is 'the last day of the month', and the clear-out journal ties to the TB at the prior month end. Confirm which month's last day the ADAW Post Date is. | 4.3 and 5.2 | B | SME | Open |
| CM-23 | The manual does not describe how the OB file is uploaded to D365: who uploads it, how (for example, which import), and how the upload is checked, posted and approved. Topic 5 starts 'once the D365 TB has been loaded'. Supply the steps, or the guide that covers them. | Part 1; 4.3; topic 5 | B | SME | Open |
| CM-24 | The manual does not describe the subledger uploads (customers, vendors, fixed assets, banks and leases) or the GL reversal of the SL balances that 8.4 checks. Confirm who does them, and whether they belong in this guide or another. | Part 1; 8.4 | B | SME | Open |
| CM-25 | The examples of ledgers and go-lives (A71, A78, A92, AUY, SDT, CCES, and A95 taken off the TM1 001-only list in September 2026) come from earlier waves. Confirm whether to keep them in the guide, and who updates the TM1 001-only list for each go-live. | Part 1 Key concepts; 5.1 | N | SME | Open |
| CM-26 | Confirm which journal type the clear-out journal uses: GJL, or RJL with a Reversing Date, and when each applies. | 5.2 | B | SME | Open |
| CM-27 | Confirm the Upl value. The template Instructions say Upl must always be L, but the migration file lines use O (source [Confirm]). | 5.2 | B | SME | Open |
| CM-28 | Test the CW1 steps: the menu path to ADAW Journal Template A, and where the mandatory sub-account setting is on a revenue GL. Confirm who imports the journal (the manual names the CW1 administrator and the ledger owners), what to do if the migration-month TB already has transactions before clearing, and how an item found at month end is raised in D365. | Topic 5; 5.3 and 5.4 | B | Test, SME | Open |
| CM-29 | Confirm how the SPE journal is prepared and posted in D365 (journal type, upload method and who posts it), where the SPE table is held, and how the calculated value for the maximum penny-rounding difference is worked out. The manual describes the settings, not the journal. | Part 1 Key concepts; topic 6 | B | SME | Open |
| CM-30 | Confirm who changes and reverts the D365 settings for the SPE journal (source [Confirm: owner]), the security access they need, and whether other postings in the legal entity are held while the settings are changed. | Part 1; topics 6 and 9 | B | SME | Open |
| CM-31 | Test the field label. The screenshot shows 'Maximum penny-rounding in the...' (truncated) beside 'Maximum penny difference', which shows 10.00. Confirm the full label, and that the field to change is the reporting currency field. | 6.1 and 6.3 | B | Test | Open |
| CM-32 | Confirm the D365 steps for the post-upload adjustment journals: the journal name, how the journals are prepared (upload or manual entry), who posts them, and the deadline relative to go-live and the first D365 month-end close (source [Confirm]). | Topic 7 | B | SME | Open |
| CM-33 | Confirm the D365 page and settings used to extract the trial balance (proposed for test: General ledger > Inquiries and reports > Trial balance), and how it is exported. | 8.1 | B | Test | Open |
| CM-34 | Confirm the reconciliation workbook: its template, name and location. | 8.2 and 8.6 | N | SME | Open |
| CM-35 | Confirm the checklist. It is called a pre go-live checklist, but items 16 to 19 follow the TB upload or go-live, and it has no item for the OB upload or the subledger uploads (CM-23, CM-24). | Topic 9 | N | Dec | Open |
| CM-36 | Confirm the reports and their navigation paths in D365: the trial balance, the chart of accounts report used for Tab 4, and the ledger account structures used for Tab 5. | Part 3 | B | Test, SME | Open |
| CM-37 | The screenshots come from the source manual (October 2026). Staff names in the TM1 example and customer codes in the AMCS example are masked. Check that the D365 screenshots in topic 6 match current D365, and recapture any that do not. | Topics 2, 3 and 6 | N | Test | Open |

---

## 5. Review comments by section

Every review comment in the Word guide, in document order.

| Section | Items |
|---|---|
| Version history | `CM-02`, `CM-01` |
| Part 1 High-level process | `CM-04`, `CM-05`, `CM-06`, `CM-23`, `CM-24`, `CM-07`, `CM-03`, `CM-05`, `CM-06`, `CM-06`, `CM-07`, `CM-11`, `CM-30` |
| Part 1 Roles and responsibilities | `CM-05`, `CM-30` |
| Part 1 Key concepts | `CM-05`, `CM-24`, `CM-13`, `CM-12`, `CM-16`, `CM-19`, `CM-25`, `CM-09`, `CM-25`, `CM-29`, `CM-10` |
| Topic 1 Map the CW1 Ledger to TM1 | `CM-09`, `CM-06`, `CM-06` |
| Topic 2 Analyze the CW1 Closing Trial Balance | `CM-37`, `CM-11`, `CM-12`, `CM-11`, `CM-13`, `CM-12` |
| Topic 3 Prepare the Breakdown Files | `CM-37`, `CM-12`, `CM-14`, `CM-15` |
| 4.1 Complete the TB OB Tab | `CM-16`, `CM-19`, `CM-17`, `CM-18`, `CM-21`, `CM-20`, `CM-19` |
| 4.2 Add Breakdown Lines | `CM-20`, `CM-19`, `CM-19` |
| 4.3 Complete the AMCS Upload Tab | `CM-22`, `CM-23` |
| Topic 5 Reverse the Balances in CW1 | `CM-28`, `CM-23` |
| 5.1 Flag the Ledgers with CW1 Activity in the Cutover Month | `CM-25`, `CM-25` |
| 5.2 Prepare the ADAW Clear-Out Journal | `CM-09`, `CM-26`, `CM-22`, `CM-27` |
| 5.3 Import the ADAW Journal into CW1 | `CM-28`, `CM-28`, `CM-28`, `CM-28` |
| 5.4 Confirm the Migration-Month Trial Balance in CW1 | `CM-28` |
| Topic 6 Upload the SPE Balances at Historical Rates | `CM-29`, `CM-30`, `CM-29` |
| 6.1 Change the Maximum Penny-Rounding Difference | `CM-37`, `CM-29`, `CM-30`, `CM-31` |
| 6.2 Redirect the Penny Difference Posting Account | `CM-30`, `CM-29` |
| 6.3 Revert the Original Configuration | `CM-30`, `CM-31` |
| Topic 7 Book the Post-Upload Adjustment Journals | `CM-14`, `CM-32`, `CM-32`, `CM-32` |
| Topic 8 Check the D365 Trial Balance After Go-Live | `CM-08` |
| 8.1 Extract the D365 Trial Balance | `CM-33`, `CM-33` |
| 8.2 Compare with the Intended Migration Balances | `CM-34` |
| 8.3 Reconcile the Migration Journals | `CM-13`, `CM-14` |
| 8.4 Check the Subledger Balances | `CM-24` |
| 8.6 Confirm the CW1 Side and Sign Off | `CM-34`, `CM-15` |
| Topic 9 Complete the Pre Go-Live Checklist | `CM-35`, `CM-35`, `CM-06`, `CM-30` |
| Part 3 Reports | `CM-36`, `CM-36` |

---

## 6. Publication gate status

| Gate | Status |
|---|---|
| Identified | Done: the Go-Live Manual supplied for conversion (2026-11-13) |
| Source reviewed | Done: manual content mapped (section 3) and conflicts raised as items |
| Gap validated | Open: 37 items (26 blocking) |
| Drafted | Done: v0.1 working draft in the master template |
| System tested | Not started (`CM-19`, `CM-28`, `CM-31`, `CM-33`, `CM-36`, `CM-37`) |
| SME validated | Not started |
| Process-owner approved | Not started: BPO to confirm (`CM-02`) |
| Published | No. Remove the `CLAUDE-` prefix and allocate the code (`CM-01`) at publication |
