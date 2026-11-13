# Project Context and Decisions: GL CW1 to D365 Migration Learning

| Field | Value |
|---|---|
| Topic | General ledger (GL) balance migration from CargoWise One (CW1) to D365, proposed for the Record-to-Report (R2R) stream (`CM-03`) |
| Guide | *D365 F&O: CW1 to D365 Migration Procedure Guide*, v0.1 working draft ([Word](../01-procedure-guides/CLAUDE-TBC-CW1%20to%20D365%20Migration%20PG%20v0.1.docx) · [PDF](../01-procedure-guides/CLAUDE-TBC-CW1%20to%20D365%20Migration%20PG%20v0.1.pdf) · [Preview](../01-procedure-guides/PG-CW1-to-D365-Migration-v0.1-DRAFT.md) · [Validation](../03-validation/CW1-to-D365-Migration-v0.1-Validation.md)) |
| Last updated | 2026-11-13 |

This topic follows the repository conventions in the [README](../../README.md) and the PG master template and authoring guide in [`templates/`](../../templates/). Decision IDs continue the repository sequence, so they never clash with the AR Collections or AP Vendor Invoices logs ([AR decisions](../../ar-collections-learning/05-project-notes/Project-Context-and-Decisions.md) · [AP decisions](../../ap-vendor-invoices-learning/05-project-notes/Project-Context-and-Decisions.md)).

---

## 1. Source documents

Held outside this repository and not modified.

| # | Source | Role |
|---|---|---|
| 1 | *CW1 to D365 Migration - Go-Live Manual*, version date October 2026, owner Maria Florencia Ruiz (Group Accounting Transformation Lead, WiseTech Global Finance). File `CW1_to_D365_Migration_-_Go-Live_Manual.docx`, supplied by the user on 2026-11-13. | The manual, in its own format (Steps 1 to 8 and a pre go-live checklist), with no version number and six open `[Confirm]` notes. Reference evidence for every v0.1 topic: no item closes on it alone. |

## 2. Guide structure (v0.1)

| # | Topic | Manual source | Pattern |
|---|---|---|---|
| 1 | Map the CW1 Ledger to TM1 | Step 1 | Off-system |
| 2 | Analyze the CW1 Closing Trial Balance | Step 2 | Off-system |
| 3 | Prepare the Breakdown Files | Step 3 | Off-system |
| 4 | Prepare the Opening Balance File: 4.1 Complete the TB OB Tab; 4.2 Add Breakdown Lines; 4.3 Complete the AMCS Upload Tab | Step 4 | Parent with subtopics (Excel rows shaded gray) |
| 5 | Reverse the Balances in CW1: 5.1 Flag the Ledgers; 5.2 Prepare the ADAW Clear-Out Journal; 5.3 Import the ADAW Journal into CW1; 5.4 Confirm the Migration-Month TB; 5.5 Disconnect the CW1 Feed to TM1 | Step 5 | Parent with subtopics (CW1, TM1 and Excel rows shaded gray) |
| 6 | Upload the SPE Balances at Historical Rates: 6.1 Change the Maximum Penny-Rounding Difference; 6.2 Redirect the Penny Difference Posting Account; 6.3 Revert the Original Configuration | Step 6 | Parent with subtopics (D365) |
| 7 | Book the Post-Upload Adjustment Journals | Step 7 | Standalone |
| 8 | Check the D365 Trial Balance After Go-Live: 8.1 to 8.6 | Step 8 (numbered 7.1 to 7.8 in the manual) | Parent with subtopics |
| 9 | Complete the Pre Go-Live Checklist | Pre go-live checklist | Off-system |
| Part 3 | Trial Balance; Chart of Accounts; Ledger Account Structures | Reports named in Steps 4 and 8 | Navigation to be confirmed |

## 3. Decisions log

| ID | Date | Decision | Basis | Status |
|---|---|---|---|---|
| D-058 | 2026-11-13 | **The CW1 to D365 Migration - Go-Live Manual is converted to the PG master template as a v0.1 working draft**, at the user's request ("convert this into the D365 PG format"). It sits in a new topic folder, `gl-cw1-migration-learning/`, because the balance migration is general ledger work, proposed for the R2R stream (`CM-03`), not AR Collections or AP. The conversion keeps the manual's content and changes its form: Steps 1 to 8 and the checklist become topics 1 to 9; the column guides, field tables and check tables become one action per row with the rule beside its field; Excel, TM1 and CW1 rows are shaded gray as off-system actions; D365 steps use the standard navigation pattern; the manual's section references become links; its six `[Confirm]` notes become items; staff names and customer codes are masked in two screenshots. **Version 0.1**, not 1.0, because the manual is unversioned and unfinished (the AP precedent, D-057, rebuilt a published v0.2 as v1.0). The file name uses `TBC` until the register owner allocates a code from the R2R numbering standard (`CM-01`) and `CLAUDE-` until publication (D-056). 37 items (`CM-01` to `CM-37`, 26 blocking) are in the [validation register](../03-validation/CW1-to-D365-Migration-v0.1-Validation.md), each also a Word review comment (96 comments). The largest gaps: the manual does not describe the OB upload to D365 (`CM-23`), the subledger uploads (`CM-24`), the SPE journal (`CM-29`) or the D365 steps for the adjustment journals (`CM-32`), and it has one direct conflict, the CC 50005 offset of CW1 department 870 against the Department 001 rule (`CM-18`). | User request; T1; T2; D-056 | Adopted |
| D-059 | 2026-11-13 | **Key concepts use the form their content needs** (repository rule, recorded in the [AR decisions log](../../ar-collections-learning/05-project-notes/Project-Context-and-Decisions.md) and [CLAUDE.md](../../CLAUDE.md)). In this guide: **Opening Balance Workbook** becomes a three-column table (Tab, Name, Purpose); **Opening Balance Checks** a three-column table (Check, Where, Passes when); **Department 001 in CW1** paragraphs and a bulleted list; **SPE Balances and Temporary D365 Settings** paragraphs and a three-column table (Setting, Normal value, For the SPE journal). The reconciled-breakdowns row of **Account Groups** becomes a paragraph after the table. No content or item changes. | User question about two-column key concepts | Adopted |
| D-060 | 2026-11-13 | **Notes to the author are marked with `ACTION: REVIEW REQUIREMENT`** (repository rule, recorded in the [AR decisions log](../../ar-collections-learning/05-project-notes/Project-Context-and-Decisions.md) and [CLAUDE.md](../../CLAUDE.md)). In this guide: yellow-box notes for the missing OB and subledger upload steps (Part 1), the unmarked roles for 6.1 to 6.3 (role matrix) and the report navigation (Part 3); highlighted phrases for the settings owner (Process table, topic 6, 6.1 to 6.3, checklist item 15), the OB upload in 4.3, the adjustment journal steps in topic 7 and each report's navigation. The roles note moves out of the standard Note box; the report navigation sentence moves out of the Part 3 Overview. No item changes. | User request | Adopted |

## 4. Next steps

1. **Code, stream and owner.** Ask the register owner for the R2R guide code (`CM-01`), and confirm the stream (`CM-03`), the BPO (`CM-02`) and whether a PG is the right home for this cutover task (`CM-04`).
2. **SME review.** Send the v0.1 draft to Maria Florencia Ruiz with the blocking items, starting with the gaps and conflicts that change the steps: the OB upload (`CM-23`), the subledger uploads (`CM-24`), the CC rule for P&L lines (`CM-18`), the journal structure for the highlighted items (`CM-14`), the dates (`CM-22`), the ADAW values (`CM-26`, `CM-27`), the SPE journal and the settings owner (`CM-29`, `CM-30`) and the adjustment journals (`CM-32`).
3. **Roles.** Confirm Ledger Owner (`CM-05`), the TM1 administrator for the mapping file (`CM-06`) and who runs the TM1 analysis (`CM-11`), then update the Stream table, Process table, role matrix and topics together.
4. **Tests.** Test the workbook check cells (`CM-19`), the CW1 ADAW path (`CM-28`), the D365 field label and screenshots (`CM-31`, `CM-37`), and the D365 report paths (`CM-33`, `CM-36`) in a clean session.
5. **Links.** Collect user-accessible links for the templates and workbooks (`CM-09`) and the Bug 11817 reference (`CM-10`).
