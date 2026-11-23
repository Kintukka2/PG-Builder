# Validation Register: 220 Customer Payments v3.1 (working draft)

| Field | Value |
|---|---|
| Guide (editable source) | [`CLAUDE-220-Customer Payments PG v3.1.docx`](../01-procedure-guides/CLAUDE-220-Customer%20Payments%20PG%20v3.1.docx) |
| Review PDF | [`CLAUDE-220-Customer Payments PG v3.0.pdf`](../01-procedure-guides/CLAUDE-220-Customer%20Payments%20PG%20v3.0.pdf) (out of date since 2026-11-17, D-064) |
| Markdown preview | [`PG-220-Customer-Payments-v3.0-DRAFT.md`](../01-procedure-guides/PG-220-Customer-Payments-v3.0-DRAFT.md) |
| Status | Working draft **v3.1** (D-092; versions below). v3.0 (D-055) consolidates version 2.1 and 221 Customer Payment Corrections v0.1. Formatting brought in line with D-059 to D-061 on 2026-11-16 (D-062); no content or item changes. Review comments cut to one per open blocking item on 2026-11-17 (D-067, D-074). Three items closed on 2026-11-18 (roles confirmed and Part 3 kept as a quick-access summary, D-081; no security roles in guides, D-083). Round 1 rebuilt as seven questions (D-085, section 7) and sent to Maria Pabalan in ADO Task 16993 on 18 November, with the review copy. **Maria answered round 1 on 19 November** (section 7.3) and the answers are applied (D-091): Receipting Officers are the audience again, as in v2.1; the direct debit customer payment journal is topic 6; a copy-paste method is 2.4; 3.5 covers overpayments only; write-offs follow the manual approval. Round 2 (three questions, section 8) is drafted on the board. Needs BPO sign-off. Version 2.1 stays published until 3.0 passes its gates. |
| Last updated | 2026-11-23 |
| Items | 20 guide-level items (`G220`): 11 open (8 blocking, 3 non-blocking) and 9 closed (`G220-02` to `G220-09`, `G220-12`). **30 Word review comments** (D-067): 13 guide-level and 17 carried from 221 v0.1; 70 removed under D-067 (section 4.1), 9 when their items closed before round 1 (sections 6.1 and 7) and 21 when round 1 was answered (section 7.3). Comments for items asked in round 2 start with the question number, for example *[Q08]*. |

This file is the guide's **question log** (D-016). It holds the guide-level items, which are scoped to this guide and never renumbered. Review comments carried from 221 keep their ID, for example *CPJ-14* or *G221-07*, and their source register stays the record for them: an answer recorded there applies here (D-048). Each open item that affects the text is a Word review comment by "Validation register" (VR).

---

## Versions of the guide

Each version that goes out for review keeps its number; when a round of answers is applied, the minor version goes up (D-092). The guide's own version history has a row for each version. The board card shows the current one.

| Version | Date | Sent to | What it is |
|---|---|---|---|
| 3.0 | 10 to 18 November 2026 | Maria Pabalan, with round 1 (ADO Task 16993, 18 November) | v2.1 rebuilt in the master template and consolidated with 221 Customer Payment Corrections (D-055); Collections Officer roles; settlement methods in topic 2; direct debit linked to 240. Review comments cut to one per open blocking item (D-067, D-074); round 1 rebuilt under D-085. |
| 3.1 | 22 November 2026 | Maria Pabalan, with round 2 (not sent yet) | Maria's round 1 answers applied (D-091). What changed is listed below. |

### What changed in v3.1

From Maria Pabalan's round 1 answers (ADO Task 16993, 19 November 2026; section 7.3, D-091).

- **Roles:** the guide is for Receipting Officers again, as in v2.1. Collections Officers appear only where a step hands work to the Collections team. In 2.1.3, step 21 now has the officer tag the Collections Officer in the receipting spreadsheet for the customer code, and step 30 sends the officer to 4.5 to update the alternate name. Part 1 (Stream, Process, roles matrix with Receipting Officer and Approver columns) and every Responsibility follow; the note about the April go-live is gone.
- **Topic 6:** now the direct debit customer payment journal (DD-CPJL) procedure: the v2.1 section 5 steps, which had moved to 240 topic 2.1, with the approval step and the approvers Maria Pabalan, Arash Najafi, Chris Clarke and Zi Chen. The Collections team maintains direct debit bank details.
- **Ways to settle:** the *Which method to use* table is rewritten, with rows for 2.4 and topic 6. 2.2 is limited to Maria's two cases (not pushed into Process customer settlements; received into a bank not connected to TAS), has no approval steps, and posts the journal once, after it is settled. The v2.1 *Notify the approver* step moved to 3.6.
- **New 2.4 Paste Payment Lines into a Customer Payment Journal:** the copy-paste method, a placeholder until Maria's steps come back (round 2, Q08). It comes after 2.3, so the numbers Maria confirmed do not change.
- **3.5** is renamed *Restore an Overpayment Amount*. Topic 3 now says that a payment settled on the wrong account is undone (3.1), transferred (3.3) and settled again, and that a write-off posted in error is reversed instead of restored (steps in round 2, Q09).
- **3.6 write-offs:** the write-off journal (WOJL) is approved by Chris Clarke or Arash Najafi, with a placeholder for limits until CR 16959. It has the reason codes (BANK FEE, FOREX, OVER/SHORT, SHORT PAY, OVER PAY; not PENNY DIFF; BADDEBTS for Chris Clarke only), the steps to mark the journal ready and notify the approver, and the rule that the invoice settles only when the journal posts. For write-off access the officer contacts the BAU Support team; the user group is not named (D-083).
- **Corrections:** transfers, distributions and restorations list the checks and evidence Maria described (written evidence, matching customer codes in CW1 and D365, the original voucher; evidence kept in CW1; no sign-off). Each of them, and undoing a settlement, ends with a note on the customer's Collections page.
- **Account numbers:** 100949 Bank to bank transfer clearing, 200060 Customer overpayments and 540052 Discounts & write offs are shown.
- **Formatting:** the notes in the undefined *NoteText* style are plain cell notes with a bold **Note:**, as the template's own are. The Contents page numbers are refreshed.
- **Records:** 22 items closed and five opened (`G220-14` to `G220-18`); review comments 44 → 28.

---

## 1. Sources

| Source | Draft register | What this guide takes from it |
|---|---|---|
| 220 Customer Payments v2.1 (published, January 2026) | [Cross-comparison](Legacy-O2C-PG-Cross-Comparison.md) | Topics 1, 2.1 (with 2.1.1 to 2.1.3), 2.2 (with 2.2.1 and 2.2.2), 3.2 and 4 (4.1 to 4.5), with their screenshots; Part 1 key concepts on bank statements, ExFlow and matching; Part 3 reports; the troubleshooting table. Section 5 (direct debit) was moved to 240 (D-053) and is back as topic 6, taken from 240 topic 2.1 (D-091). |
| [221 Customer Payment Corrections v0.1](../01-procedure-guides/221-Customer%20Payment%20Corrections%20PG%20v0.1.docx) | [221-Customer-Payment-Corrections-Validation.md](221-Customer-Payment-Corrections-Validation.md) | Topics 2.3 (was 1), 3.1 (was 2) and 3.3 to 3.6 (were 3 to 6), with their review comments; Part 1 settlement terms and CPJL controls. Its own sources are the Transfers, Parent Payment Distribution and Restoration topic drafts, the CPJL controls reference and legacy 230 sections 6.5, 6.6 and 6.8 (see its register and the [Part 2 register](Part2-CPJL-and-Transfers-Validation.md)). |

---

## 2. Assembly decisions

| # | Decision | Reason |
|---|---|---|
| A1 | 221 Customer Payment Corrections is merged into 220, and code 221 is withdrawn (D-055). | One role does the tasks of both guides, so the split by role that 221 was proposed for (D-046) does not apply. Maria Pabalan's round 1 answer (19 November 2026) names that role: the Receipting Officer (D-091). |
| A2 | Topic 2 *Settle Customer Payments* holds the settlement methods, each with its own procedure (2.1 bank statement, 2.2 manual payment journal, 2.3 open customer transactions, 2.4 copy-paste into a CPJL), and a *Which method to use* table at the top that also points to topic 6 for direct debit receipts. | SME request of 10 November 2026 (more than one way to settle); one task per subtopic (D-045, as in 230 v3.0). 2.4 added from the round 1 answer (D-091), after 2.3 so the numbers Maria confirmed stay. |
| A3 | Topic 3 *Correct Customer Payments* holds every correction made after posting: 221 topics 2 to 6 and v2.1 4.3 Reverse a Customer Payment Journal. | One stage for corrections; the reversal sits next to the other corrections. |
| A4 | v2.1 procedures and screenshots are kept as they are, with the section numbers in cross-references updated. The role is the Receipting Officer, as in v2.1 (D-091; from 10 to 22 November the draft named the Collections Officer). Conflicts are `G220` items. | v2.1 is the published guide; same approach as 230 v3.0 (D-052). |
| A5 | 221 topics keep their steps and review comments, with item IDs unchanged. Answered items are applied (section 6). | Item IDs stay stable after a merge (suite plan section 1). |
| A6 | Topic 6 *Process Direct Debit Customer Payments* is the direct debit customer payment journal (DD-CPJL) procedure: the v2.1 section 5 steps, taken from 240 topic 2.1, with the approval workflow and its approvers. | Maria Pabalan, round 1 (19 November 2026): direct debit receipts use their own journal name, covered in Customer Payments. Amends D-053 for this procedure (D-091); was a link to 240 topic 2. |
| A7 | Topic 5 *Process Intercompany Customer Payments* is a placeholder marked *Being worked on*, for Receipting Officers. | SME, 10 November 2026. |
| A8 | Rebuilt in the master template: the v2.1 *next page* callouts and blank page-break paragraphs are removed, and every topic and subtopic starts on a new page. | General cleanup of the v2.1 formatting (user request). |

---

## 3. Guide-level items (`G220`)

**Priority:** **B** = blocks publication. **N** = non-blocking. **Method:** **Test** = D365 test in a clean session. **Rec** = recording or transcript review. **SME** = subject-matter expert or process owner. **Dec** = project decision.

| ID | Item to confirm | Location | Priority | Method | Status |
|---|---|---|---|---|---|
| G220-01 | Version 3.0 consolidates 221 Customer Payment Corrections into this guide (D-055). It needs BPO sign-off; version 2.1 stays the published guide until 3.0 passes its gates. | Version history | B | Dec | Open |
| G220-02 | Confirm the events that start these tasks. They come from v2.1 (Part 1 Initiation) and from 221 (G221-04, TF-01, PC-06 and RO-04). | Part 1 High-level process | B | SME | Closed 2026-11-18 (D-085): the events come from v2.1, the published guide, and are not asked again. The events that came from the training notes (TF-01, PC-06, RO-04) are checked with the recording under `G220-10`. |
| G220-03 | Confirm the roles. Maria Pabalan (10 November 2026): Collections Officers do the tasks of v2.1, which Receipting Officers did before the April go-live, and Receipting Officers process intercompany (ICO) payments only. The 9 November direct debit meeting (D-053) gave direct debit processing, adding new customers to eBanking and maintaining alternate names to the receiving team. Confirm topics 4.4, 4.5 and 6. | Part 1 Stream | B | SME | Closed 2026-11-22 (replaces the close of 18 November; D-091): Maria Pabalan, round 1 (ADO 16993, 19 November 2026): customer payments are done by **Receipting Officers**, not Collections Officers, and the audience of 220 stays the Receipting Officer, as in v2.1. Collections Officers come in only where a step hands something to the Collections team: in 2.1.3 they supply the customer code. Applied in Part 1 (Stream, Process, roles), every Responsibility and procedure, and topic 6, which is now in 220. |
| G220-04 | Confirm this wording. In v2.1, payments that the receipting team could not resolve were referred to the Collections team; Collections Officers now process the payments themselves. | Part 1 Key concepts | B | SME | Closed 2026-11-22 (Q02): Maria Pabalan, round 1 (ADO 16993, 19 November 2026). *Collections Investigation* now says unresolved payments are referred to the Collections team, as in v2.1, and that the Collections Officer supplies the customer code the Receipting Officer cannot find. |
| G220-05 | Confirm the security role needed to post a CPJL. Maria Pabalan (10 November 2026) is not sure of it and suggests checking with Tony Chen (CPJ-21). | Part 1 Key concepts | B | SME | Closed 2026-11-18 (D-083): guides do not name security roles. Your manager requests your D365 profile, which gives you the access you need; for any access or security role issue, contact the BAU Support team. Applied in Part 1 (*Posting and permissions*: the row *Access to D365*); `CPJ-21` is closed with it. |
| G220-06 | Confirm the settlement methods that Collections Officers use and when each one is used. Maria Pabalan shows them several ways (10 November 2026); this guide documents three (2.1 to 2.3). Add a subtopic for any other method. | Topic 2 Settle Customer Payments | B | SME | Closed 2026-11-22 (Q01): Maria Pabalan, round 1 (ADO 16993, 19 November 2026). The three methods are confirmed; 2.2 is limited to transactions not pushed into Process customer settlements and receipts into banks not connected to TAS; 2.1 is the default (TAS matches automatically). Added: 2.4, the copy-paste method (steps open as `G220-14`), and the direct debit journal as topic 6. |
| G220-07 | Some steps refer a transaction to the Collections team, or ask it to update the customer's eBanking reference. They date from when Receipting Officers did this work. Confirm what a Collections Officer does now in each case. | 2.1.3 Process Customer Settlements – Red Status | B | SME | Closed 2026-11-22 (Q02): Maria Pabalan, round 1 (ADO 16993, 19 November 2026). Step 21: tag the Collections Officer against the payment in the receipting spreadsheet; they reply with the customer code and the Receipting Officer posts. Step 30: the Receipting Officer updates the alternate name with 4.5; the only eBanking change the Collections team makes is direct debit bank details (topic 6). The other v2.1 referrals to the Collections team stay. |
| G220-08 | Confirm the approval steps. Version 2.1 says some journals need an approver's approval before posting (its roles table names the Accounts Receivable Manager). Maria Pabalan (10 November 2026): a CPJL needs no approval. Confirm which journal names, if any, still need approval, and who approves. | 2.2.1 Create a Customer Payment Journal | B | SME | Closed 2026-11-22 (Q03): Maria Pabalan, round 1 (ADO 16993, 19 November 2026). A CPJL needs no approval: the v2.1 approval steps are removed from 2.2.1 and 2.2.2. The DD-CPJL goes through the approval workflow before the direct debit file is sent (topic 6; Maria Pabalan, Arash Najafi, Chris Clarke or Zi Chen). The write-off journal needs approval (3.6). The *Report as ready* and Teams message steps apply to write-off journals only: the Teams step moved to 3.6. |
| G220-09 | Confirm when the journal is posted. In v2.1, 4.1 (now 2.2.1) posts the journal, and 4.2 (now 2.2.2) settles it and posts it again. Confirm whether the journal is posted once, after it is settled. | 2.2.2 Settle the Customer Payment Journal | B | SME, Test | Closed 2026-11-22 (Q03): Maria Pabalan, round 1 (ADO 16993, 19 November 2026). The CPJL is settled first (Settle transactions in the journal) and posted once: 2.2.1 no longer posts, and 2.2.2 posts once. |
| G220-10 | Check topics 2.3, 3.1 and 3.6 against current D365 or a recording (they come from legacy 230, reference evidence only: D-044; was G221-03), and topics 3.3 to 3.5 and the CPJL controls against the AR Training D365 Part 2 recording (SRC-01). | Topic 3 Correct Customer Payments | B | Test, Rec | Open |
| G220-11 | Add the intercompany (ICO) payment steps from Maria Pabalan's session with Amy on Friday 6 November 2026 (recording). Confirm the example legal entities (101a and 238a). | Topic 5 Process Intercompany Customer Payments | N | Rec | Open |
| G220-12 | Complete Part 3 Reports. The five reports carried from version 2.1 have names and navigation paths but no description, and version 2.1 highlighted the Part 3 heading for review. For each report, describe what it shows, when Collections Officers use it and the check it supports, and confirm its navigation path in current D365 (the paths mix Inquiries and Enquiries). Confirm whether all five reports belong in this guide. | Part 3 Reports | B | SME, Test | Closed 2026-11-18 (scope decision, Daniel Moreira; D-081): Part 3 is a quick-access summary so Collections Officers can run the reports easily. How and when each report is used is up to the officer, so the guide does not describe it. The path check moves to `G220-13`. |
| G220-13 | Check the five report paths in Part 3 in current D365: they mix *Inquiries and Reports* and *Enquiries and Reports*. | Part 3 Reports | N | Test | Open |
| G220-14 | Add the copy-paste method: payment lines pasted into a CPJL in bulk. Maria Pabalan, round 1 (ADO 16993, 19 November 2026) asked for it as its own method, with when to use it. The steps and when to use it are not in any source. | 2.4 Paste Payment Lines into a Customer Payment Journal | B | SME | Open: round 2, Q08 |
| G220-15 | Confirm in D365 how a note is added on the customer's **Collections** page (the path and the control). The round 1 answers add such a note in 3.1 (the reason for undoing a settlement), 3.3.3, 3.4.3 and 3.5.2 (voucher, amount, currency, reason and where the evidence is). Legacy 230 opens the Collections page by clicking the customer name in Aged balances. | 3.1 step 12 | B | Test | Open |
| G220-16 | Add the steps to reverse a write-off journal (WOJL) posted in error. Maria Pabalan, round 1 (ADO 16993, 19 November 2026): reverse the original WOJL, with no approval; not 3.5 or a new journal. | Topic 3 Description | B | SME | Open: round 2, Q09 |
| G220-17 | 2.1.3 step 37 (v2.1) settles the invoice and leaves a bank fee for the Financial accountant to post during bank reconciliation; 3.6 has the officer write off a bank fee with the BANK FEE reason code, which Maria Pabalan, round 1 (ADO 16993, 19 November 2026) lists for officers. Confirm which applies to a bank fee deducted from a bank statement payment. | 2.1.3 step 37 | B | SME | Open: round 2, Q10. Marked in the guide as a placeholder (D-097) |
| G220-18 | Topic 6 comes from v2.1 section 5 by way of 240 topic 2.1, where `G240-08` checks it against the 11 November direct debit recording. Check it there too, and have 240 topic 2.1 link to 220 topic 6 when 240 is next updated (D-091). | 6 Process Direct Debit Customer Payments | N | Rec | Open |
| G220-19 | PG owner: add the link to the receipting spreadsheet, which the guide references without one (D-096), or record that it is an internal working file the guide does not link. | 2.1.3 step 21; Part 1 *Collections Investigation* | B | Owner | Open |
| G220-20 | PG owner: give the role titles of Maria Pabalan and Zi Chen, who also approve the DD-CPJL (D-099: guides name roles, not people). Topic 6 shows two ACTION placeholders until then. | 6 Process Direct Debit Customer Payments (Responsibility) | B | Owner | Open |

---

## 4. Review comments by section

Every review comment in the Word guide, in document order, after D-067 (one comment per item, open blocking items only; D-074), as of 22 November 2026 (28 comments). IDs not starting `G220` are carried from 221 v0.1 and its topic drafts.

| Section | Items |
|---|---|
| Cover and version history | `G220-01` |
| Part 1 Key concepts | `CPJ-16 to CPJ-20` |
| Topic 2.1 Settle Bank Statement Payments | `G220-17` (2.1.3 step 37) |
| Topic 2.3 Settle Open Customer Transactions | `G221-08`, `G221-09`, `G221-10` |
| Topic 2.4 Paste Payment Lines into a Customer Payment Journal | `G220-14` |
| Topic 3 Correct Customer Payments | `G220-16`, `G220-10` |
| Topic 3.1 Undo a Settlement | `G221-12`, `G220-15` |
| Topic 3.3 Transfer Funds Between Customer Accounts | `CPJ-01`, `CPJ-01 / CPJ-02`, `CPJ-03`, `CPJ-05`, `CPJ-06`, `CPJ-08`, `TF-04`, `CPJ-13`, `CPJ-14` |
| Topic 3.4 Distribute a Parent Account Payment Across Child Accounts | `PC-03` |
| Topic 3.5 Restore an Overpayment Amount | `CPJ-06`, `CPJ-10`, `CPJ-11` |
| Topic 3.6 Write Off a Bank Fee or Small Residual | `G221-15`, `G221-16`, `G221-17` |
| Topic 5 Process Intercompany Customer Payments | `G220-11` |

### 4.1 Comments removed under D-067 (17 November 2026)

The items stay open in their registers; only the Word comment is gone. The CPJL control items (`CPJ`) were commented in Part 1 and again in each of topics 3.3, 3.4 and 3.5: they keep one comment each, at the first procedure step that needs the answer.

| Item | Where the comment was | Why it was removed |
|---|---|---|
| `CPJ-02` | Part 1 Key concepts | Duplicate: the comment in Topic 3.3 Transfer Funds Between Customer Accounts covers it |
| `CPJ-14` | Part 1 Key concepts | Duplicate: the comment in Topic 3.3 Transfer Funds Between Customer Accounts covers it |
| `CPJ-01 / CPJ-02` | Part 1 Key concepts | Duplicate: the comment in Topic 3.3 Transfer Funds Between Customer Accounts covers it |
| `CPJ-03 / CPJ-04` | Part 1 Key concepts | Duplicate: the comment in Topic 3.3 Transfer Funds Between Customer Accounts covers it |
| `CPJ-05` | Part 1 Key concepts | Duplicate: the comment in Topic 3.3 Transfer Funds Between Customer Accounts covers it |
| `CPJ-07` | Part 1 Key concepts | Duplicate: the comment in Topic 3.5 Restore a Written-Off or Overpayment Amount covers it |
| `CPJ-06` | Part 1 Key concepts | Duplicate: the comment in Topic 3.3 Transfer Funds Between Customer Accounts covers it |
| `CPJ-08 / CPJ-09 / TF-03 / RO-01` | Part 1 Key concepts | Duplicate: the comment in Part 1 Key concepts and Topic 3.3 Transfer Funds Between Customer Accounts and Topic 3.5 Restore a Written-Off or Overpayment Amount covers it |
| `CPJ-10` | Part 1 Key concepts | Duplicate: the comment in Topic 3.5 Restore a Written-Off or Overpayment Amount covers it |
| `CPJ-11` | Part 1 Key concepts | Duplicate: the comment in Topic 3.5 Restore a Written-Off or Overpayment Amount covers it |
| `CPJ-12` | Part 1 Key concepts | Non-blocking: stays open in this register |
| `CPJ-13` | Part 1 Key concepts | Duplicate: the comment in Topic 3.3 Transfer Funds Between Customer Accounts covers it |
| `CPJ-14 / CPJ-15` | Part 1 Key concepts | Duplicate: the comment in Topic 3.3 Transfer Funds Between Customer Accounts covers it |
| `CPJ-16 / CPJ-17` | Part 1 Key concepts | Non-blocking or closed: stays open in this register |
| `PC-04` | Part 1 Key concepts | Duplicate: the comment in Topic 3.4 Distribute a Parent Account Payment Across Child Accounts covers it |
| `PC-01` | Part 1 Key concepts | Duplicate: the comment in Topic 3 Correct Customer Payments covers it |
| `PC-04 / PC-05` | Part 1 Key concepts | Duplicate: the comment in Topic 3.4 Distribute a Parent Account Payment Across Child Accounts covers it |
| `CPJ-06` | Part 1 Key concepts | Duplicate: the comment in Topic 3.3 Transfer Funds Between Customer Accounts covers it |
| `RO-01 / CPJ-09` | Part 1 Key concepts | Duplicate: the comment in Part 1 Key concepts and Topic 3.5 Restore a Written-Off or Overpayment Amount covers it |
| `CPJ-07` | Part 1 Key concepts | Duplicate: the comment in Topic 3.5 Restore a Written-Off or Overpayment Amount covers it |
| `CPJ-04` | Part 1 Key concepts | Non-blocking: stays open in this register |
| `CPJ-07` | Part 1 Key concepts | Duplicate: the comment in Topic 3.5 Restore a Written-Off or Overpayment Amount covers it |
| `CPJ-04` | Part 1 Key concepts | Non-blocking: stays open in this register |
| `TF-03 / CPJ-09` | Part 1 Key concepts | Duplicate: the comment in Part 1 Key concepts covers it |
| `CPJ-07` | Part 1 Key concepts | Duplicate: the comment in Topic 3.5 Restore a Written-Off or Overpayment Amount covers it |
| `CPJ-04` | Part 1 Key concepts | Non-blocking: stays open in this register |
| `CPJ-10` | Part 1 Key concepts | Duplicate: the comment in Topic 3.5 Restore a Written-Off or Overpayment Amount covers it |
| `CPJ-11` | Part 1 Key concepts | Duplicate: the comment in Topic 3.5 Restore a Written-Off or Overpayment Amount covers it |
| `TF-05` | Topic 3.3 Transfer Funds Between Customer Accounts | Duplicate: the comment in Topic 3 Correct Customer Payments covers it |
| `CPJ-01` | Topic 3.3 Transfer Funds Between Customer Accounts | Duplicate: the comment in Topic 3.3 Transfer Funds Between Customer Accounts covers it |
| `CPJ-03` | Topic 3.3 Transfer Funds Between Customer Accounts | Duplicate: the comment in Topic 3.3 Transfer Funds Between Customer Accounts covers it |
| `CPJ-12` | Topic 3.3 Transfer Funds Between Customer Accounts | Non-blocking: stays open in this register |
| `CPJ-01 / CPJ-05` | Topic 3.3 Transfer Funds Between Customer Accounts | Duplicate: the comment in Topic 3.3 Transfer Funds Between Customer Accounts covers it |
| `CPJ-06` | Topic 3.3 Transfer Funds Between Customer Accounts | Duplicate: the comment in Topic 3.3 Transfer Funds Between Customer Accounts covers it |
| `CPJ-16 / CPJ-17` | Topic 3.3 Transfer Funds Between Customer Accounts | Non-blocking or closed: stays open in this register |
| `CPJ-19` | Topic 3.3 Transfer Funds Between Customer Accounts | Duplicate: the comment in Topic 3 Correct Customer Payments covers it |
| `CPJ-21` | Topic 3.4 Distribute a Parent Account Payment Across Child Accounts | Duplicate: the comment in Topic 3.3 Transfer Funds Between Customer Accounts covers it |
| `CPJ-01` | Topic 3.4 Distribute a Parent Account Payment Across Child Accounts | Duplicate: the comment in Topic 3.3 Transfer Funds Between Customer Accounts covers it |
| `CPJ-01 / CPJ-02` | Topic 3.4 Distribute a Parent Account Payment Across Child Accounts | Duplicate: the comment in Topic 3.3 Transfer Funds Between Customer Accounts covers it |
| `CPJ-03` | Topic 3.4 Distribute a Parent Account Payment Across Child Accounts | Duplicate: the comment in Topic 3.3 Transfer Funds Between Customer Accounts covers it |
| `CPJ-01` | Topic 3.4 Distribute a Parent Account Payment Across Child Accounts | Duplicate: the comment in Topic 3.3 Transfer Funds Between Customer Accounts covers it |
| `CPJ-05` | Topic 3.4 Distribute a Parent Account Payment Across Child Accounts | Duplicate: the comment in Topic 3.3 Transfer Funds Between Customer Accounts covers it |
| `CPJ-06` | Topic 3.4 Distribute a Parent Account Payment Across Child Accounts | Duplicate: the comment in Topic 3.3 Transfer Funds Between Customer Accounts covers it |
| `CPJ-03` | Topic 3.4 Distribute a Parent Account Payment Across Child Accounts | Duplicate: the comment in Topic 3.3 Transfer Funds Between Customer Accounts covers it |
| `CPJ-08` | Topic 3.4 Distribute a Parent Account Payment Across Child Accounts | Duplicate: the comment in Topic 3.3 Transfer Funds Between Customer Accounts covers it |
| `CPJ-12` | Topic 3.4 Distribute a Parent Account Payment Across Child Accounts | Non-blocking: stays open in this register |
| `CPJ-01 / CPJ-05` | Topic 3.4 Distribute a Parent Account Payment Across Child Accounts | Duplicate: the comment in Topic 3.3 Transfer Funds Between Customer Accounts covers it |
| `CPJ-06` | Topic 3.4 Distribute a Parent Account Payment Across Child Accounts | Duplicate: the comment in Topic 3.3 Transfer Funds Between Customer Accounts covers it |
| `PC-03` | Topic 3.4 Distribute a Parent Account Payment Across Child Accounts | Duplicate: the comment in Topic 3.4 Distribute a Parent Account Payment Across Child Accounts covers it |
| `CPJ-13` | Topic 3.4 Distribute a Parent Account Payment Across Child Accounts | Duplicate: the comment in Topic 3.3 Transfer Funds Between Customer Accounts covers it |
| `CPJ-14` | Topic 3.4 Distribute a Parent Account Payment Across Child Accounts | Duplicate: the comment in Topic 3.3 Transfer Funds Between Customer Accounts covers it |
| `CPJ-15` | Topic 3.4 Distribute a Parent Account Payment Across Child Accounts | Duplicate: the comment in Topic 3.3 Transfer Funds Between Customer Accounts covers it |
| `CPJ-16 / CPJ-17` | Topic 3.4 Distribute a Parent Account Payment Across Child Accounts | Non-blocking or closed: stays open in this register |
| `CPJ-18` | Topic 3.4 Distribute a Parent Account Payment Across Child Accounts | Duplicate: the comment in Topic 3.3 Transfer Funds Between Customer Accounts covers it |
| `CPJ-19` | Topic 3.4 Distribute a Parent Account Payment Across Child Accounts | Duplicate: the comment in Topic 3 Correct Customer Payments covers it |
| `CPJ-21` | Topic 3.5 Restore a Written-Off or Overpayment Amount | Duplicate: the comment in Topic 3.3 Transfer Funds Between Customer Accounts covers it |
| `CPJ-01` | Topic 3.5 Restore a Written-Off or Overpayment Amount | Duplicate: the comment in Topic 3.3 Transfer Funds Between Customer Accounts covers it |
| `CPJ-01 / CPJ-02` | Topic 3.5 Restore a Written-Off or Overpayment Amount | Duplicate: the comment in Topic 3.3 Transfer Funds Between Customer Accounts covers it |
| `CPJ-03` | Topic 3.5 Restore a Written-Off or Overpayment Amount | Duplicate: the comment in Topic 3.3 Transfer Funds Between Customer Accounts covers it |
| `CPJ-01` | Topic 3.5 Restore a Written-Off or Overpayment Amount | Duplicate: the comment in Topic 3.3 Transfer Funds Between Customer Accounts covers it |
| `CPJ-05` | Topic 3.5 Restore a Written-Off or Overpayment Amount | Duplicate: the comment in Topic 3.3 Transfer Funds Between Customer Accounts covers it |
| `CPJ-03` | Topic 3.5 Restore a Written-Off or Overpayment Amount | Duplicate: the comment in Topic 3.3 Transfer Funds Between Customer Accounts covers it |
| `CPJ-08` | Topic 3.5 Restore a Written-Off or Overpayment Amount | Duplicate: the comment in Topic 3.3 Transfer Funds Between Customer Accounts covers it |
| `CPJ-12` | Topic 3.5 Restore a Written-Off or Overpayment Amount | Non-blocking: stays open in this register |
| `CPJ-14` | Topic 3.5 Restore a Written-Off or Overpayment Amount | Duplicate: the comment in Topic 3.3 Transfer Funds Between Customer Accounts covers it |
| `CPJ-15` | Topic 3.5 Restore a Written-Off or Overpayment Amount | Duplicate: the comment in Topic 3.3 Transfer Funds Between Customer Accounts covers it |
| `CPJ-16 / CPJ-17` | Topic 3.5 Restore a Written-Off or Overpayment Amount | Non-blocking or closed: stays open in this register |
| `CPJ-18` | Topic 3.5 Restore a Written-Off or Overpayment Amount | Duplicate: the comment in Topic 3.3 Transfer Funds Between Customer Accounts covers it |
| `CPJ-19` | Topic 3.5 Restore a Written-Off or Overpayment Amount | Duplicate: the comment in Topic 3 Correct Customer Payments covers it |
| `G221-20` | Topic 3.6 Write Off a Bank Fee or Small Residual | Non-blocking: stays open in this register |

---

## 5. 221 items not carried as comments

221 guide-level items that are not review comments in this guide, and where each one is answered. The other `G221` items are carried as review comments. Part 2 register items keep that register as their record (answers of 10 November 2026: section 6).

| Item | Disposition |
|---|---|
| `G221-01`: Guide code 221 and the title Customer Payment Corrections are proposed (D-046), with the split from 230 Collections (legacy sections 6.5 to 6.8 move here). The register owner records the code in the O2C PG numbering register, and the BPO confirms the scope and the split, before this guide circulates beyond the project team. | Superseded: 221 is withdrawn and merged into 220 (D-055; `G220-01`). |
| `G221-02`: Confirm the business process owner (BPO) for this guide. Christopher Clarke is the BPO of 220 Customer Payments and of 230 Collections, which held legacy sections 6.5 to 6.8. | Answered: Christopher Clarke is the BPO of 220 (version history). |
| `G221-03`: Check topics 1, 2 and 6 against current D365 or a recording. They come from legacy 230 v2.3, which is reference evidence only (D-044). | Replaced by `G220-10`. |
| `G221-04`: Confirm the events that start topics 1, 2 and 6. They come from legacy 230. | Replaced by `G220-02`. |
| `G221-05`: Confirm the roles. Legacy 230 assigns settling, undoing a settlement and the bank fee write-off to the Collections Officer, with the Group Billing and Credit Manager also named for write-off journals. The roles for topics 3 to 5 are not confirmed (GOV-01, CPJ-16). | Answered: the Receipting Officer for every topic (Maria Pabalan, round 1, 19 November 2026; D-091), which replaces the answer of 10 November (Collections Officer). The write-off approver is Chris Clarke or Arash Najafi (`G221-14` closed). |

---

## 6. SME answers applied (Maria Pabalan, 10 November 2026)

From Maria's review comments on 221 v0.1 and the Teams chat of 10 November 2026 (D-055).

| # | Source | Answer | Applied in v3.0 | Items |
|---|---|---|---|---|
| 1 | Chat | Collections Officers do the tasks of 220 v2.1 (*Collection officers only*). They were given the ability after the April go-live; Receipting Officers did it before. | **Superseded 2026-11-22** by Maria's round 1 answer (section 7.3): Receipting Officers, as in v2.1. | `G220-03` |
| 2 | Chat | Intercompany (ICO) payments are done by Receipting Officers only, for example a customer paying into a bank account in 101a for an invoice in 238a. Covered with Amy on Friday 6 November. | Topic 5 placeholder. | `G220-11` |
| 3 | Chat | Collections Officers settle in more than one way. | Topic 2 with three methods and *Which method to use*. | `G220-06` |
| 4 | 221 comments (topics 3 to 5) | *Collection Officer* prepares transfers, distributions and restorations. | **Superseded 2026-11-22** (section 7.3): the Receipting Officer. | `GOV-01`, `G221-05` |
| 5 | 221 comment (Key concepts) | Collections and Receipting Officers may post a CPJL. | *Posting and permissions* table; since 2026-11-22 it names Receipting Officers only (section 7.3). | `CPJ-16` (the **Post** label still to test) |
| 6 | 221 comment (Key concepts) | No approvals are required for a CPJL. | *Posting and permissions* table; roles overview. | `CPJ-17`; `G220-08` (v2.1 approval steps) |
| 7 | 221 comment (Key concepts) | A Collections Officer can delete an unposted journal that is no longer needed. | *Posting and permissions* table, with the Receipting Officer since 2026-11-22. | `CPJ-20` (steps still to confirm) |
| 8 | 221 comment (Key concepts) | Not sure of the security role needed to post a CPJL: check with Tony Chen. | *Posting and permissions* table. | `CPJ-21`; `G220-05` (both closed 2026-11-18, D-083) |

### 6.1 Answers applied, 18 November 2026

From Daniel Moreira, reviewing round 1 on the board before it is sent.

| # | Source | Answer | Applied in v3.0 | Items |
|---|---|---|---|---|
| 1 | Teams chat, 10 November 2026 (Maria Pabalan), confirmed by Daniel Moreira | Collections Officers only do the tasks in the v2.1 Contents, and **Collections Officer** is the role name. Receipting Officers process intercompany payments only. | Part 1 roles already say this. The review comment on the *Stream* table is removed; round 1 question 1 (a) is dropped. **Superseded 2026-11-22** (section 7.3). | `G220-03` closed |
| 2 | Daniel Moreira (scope decision, D-081) | Part 3 is a quick-access summary of the reports. How and when they are used is up to the officer; what matters is easy access to run them. | The ACTION note and the review comment in Part 3 are removed; the empty Description cells stay as they are. Round 1 question 7 (c) is dropped. | `G220-12` closed; `G220-13` opened for the paths |
| 3 | Daniel Moreira (D-083) | Security roles are not known to users and are not named in the guides. Users get the access they need when their manager requests a D365 profile for them; for any security role issue they contact the BAU Support team. | Part 1 *Posting and permissions*: the row *The security role needed* becomes *Access to D365* with that guidance, and its ACTION note goes. The review comments for `G220-05` and `CPJ-21` are removed. Round 1 question 3 (b) is dropped. | `G220-05` and `CPJ-21` closed |

---

## 7. Round 1 plan (D-085)

Round 1 asks Maria Pabalan only what the sources cannot answer and what changes what a Collections Officer does: seven questions, one coherent point each, with the topic and step to look at. Every other open item has a route that does not need her. This section is the clarification record for round 1; the board holds the question text.

### 7.1 Asked in round 1

| Question | Items | Where |
|---|---|---|
| Q01 Settlement methods | `G220-06` | Topic 2 |
| Q02 Steps that still send work to the Collections team | `G220-07`, `G220-04` | 2.1.3 steps 21 and 30; Part 1 *Collections Investigation* |
| Q03 Approval before posting | `G220-08`, `G220-09`, `G221-13` | 2.2.1 steps 9 to 11; 2.2.2 steps 14 to 17; 3.1 step 10 |
| Q04 Write-off approval and limits | `G221-14`, `G221-15`, `G221-18`, `G221-19` | 3.6 steps 7, 9 and 12 |
| Q05 Checks before a transfer, distribution or restoration | `TF-02`, `PC-01`, `PC-02`, `RO-03`, `PC-04` | Part 1 Key concepts; 3.3, 3.4 (3.4.3 step 5) and 3.5 |
| Q06 Choosing the correction | `TF-05`, `RO-02` | 3.1, 3.3 and 3.5 |
| Q07 Overpayment ledger and clearing account | `CPJ-09`, `TF-03`, `RO-01` | Part 1 Key concepts; 3.3.1 step 12; 3.5.1 step 13 |

### 7.2 Not asked

| Route | Items | What happens |
|---|---|---|
| Answered by a source: closed | `G220-02` (v2.1 initiation), `G221-06` (legacy 230 settlement terms), `G221-11` (legacy 230 §6.5: total 0.00; a residual is written off in 3.6), `CPJ-15` (the D365 issue form route is in the guide, from 220 v2.1 Troubleshooting), `CPJ-18` (legacy 230 §6.7 step 25 and 220 §4.1 step 11: the journal balances to zero and the transaction shows on each account), `CPJ-19` (3.2 Reverse a Customer Payment Journal, from 220 §4.3) | The guide keeps or now uses the source wording; `CPJ-18` and `CPJ-19` are written into Part 1 *Posting and permissions*. Their review comments are removed. |
| Use the legacy wording when drafting | `CPJ-07` (legacy 220 §4.2 step 9: the currency fills in from the account and must match the original receipt), `G221-07` (pre-requisites for 2.3 and 3.1 that fit settling: the account and the transactions) | Drafting changes, made without the SME. Done 2026-11-22: 3.5.1 step 9 now says the currency fills in from the account; the 2.3 and 3.1 pre-requisites already fit settling. Both closed. |
| Check against the AR Training D365 Part 2 recording | `G220-10`, `CPJ-05`, `CPJ-10`, `CPJ-11`, `TF-04`, `PC-03` (and the initiation events `TF-01`, `PC-06`, `RO-04`) | The training notes are AI-generated: the recording confirms them. |
| Check in D365 (clean-session test) | `CPJ-01`, `CPJ-02`, `CPJ-03`, `CPJ-06`, `CPJ-08`, `CPJ-13`, `CPJ-14`, `G221-08`, `G221-09`, `G221-10`, `G221-12`, `G221-16`, `G221-17` | Screen labels and navigation: the [clean-session test](Clean-Session-Test-Plan.md) confirms them. |
| Sign-off | `G220-01` | BPO sign-off of v3.0. |

### 7.3 Round 1 answers (Maria Pabalan, ADO Task 16993, 19 November 2026)

Maria answered every question and assigned the ticket back. The answers are applied to the Word guide, which becomes v3.1 (D-091, D-092). Her opening point applies to the whole guide: customer payments are done by **Receipting Officers**, not Collections Officers, and the audience of 220 stays the Receipting Officer, as in v2.1. Collections Officers come in only where a step hands something to the Collections team.

| Question | Answer | Applied in v3.1 | Items |
|---|---|---|---|
| Roles (whole guide) | Receipting Officers, as in v2.1. | Part 1 Stream, Process, roles matrix (Receipting Officer and Approver columns) and overview; every Responsibility and procedure. The note about the April go-live is removed. | `G220-03` closed again; `GOV-01`, `G221-05` and the 10 November answers superseded (section 6) |
| Q01 Settlement methods | The three methods are right. 2.1 bank statement is the default: TAS matches automatically, and the officer works the unmatched lines with the alternate name and the payment reference. 2.2 only for transactions not pushed into Process customer settlements, or receipts into banks not connected to TAS. 2.3 when the payment is already on the account, unsettled. Add a copy-paste method (payment lines pasted into a CPJL in bulk) as its own method, with when to use it. Add the DD-CPJL to the table and as its own topic in 220: direct debit receipts use their own journal name. | *Which method to use* table rewritten, with rows for 2.4 and topic 6; 2.2 Description and 2.2.1 pre-requisite limited to the two cases; new 2.4 *Paste Payment Lines into a Customer Payment Journal* (placeholder); topic 6 rebuilt as the DD-CPJL procedure. | `G220-06` closed; `G220-14` opened (round 2) |
| Q02 Steps that sent work to the Collections team | They stay Receipting Officer steps. Step 21: tag the Collections Officer against the payment in the receipting spreadsheet; they reply with the customer code; the Receipting Officer posts. Step 30: no Collections referral; the Receipting Officer updates the alternate name with 4.5. The only eBanking change Collections makes is direct debit bank details, which belong in the direct debit topic. | 2.1.3 steps 21 and 30 and the step 10 table; Part 1 *Collections Investigation* and the matching table; topic 6 says the Collections team maintains direct debit bank details; Troubleshooting points to 4.5. | `G220-07`, `G220-04` closed |
| Q03 Approval before posting | A CPJL needs no approval: settle it (Settle transactions in the journal), then post it once. The DD-CPJL goes through the approval workflow before the direct debit file is sent (approvers Maria Pabalan, Arash Najafi, Chris Clarke, Zi Chen). The WOJL needs approval. Undoing a settlement has no approval step; record the reason as a note on the customer's Collections page (what was unsettled, why, what it will be re-settled against). The v2.1 *Report as ready* and Teams steps apply only to the WOJL. | 2.2.1 steps 9 to 11 removed (the journal is validated, then settled in 2.2.2); 2.2.2 steps 14 to 16 removed and step 17 posts once; the Teams step moved to 3.6; 3.1 new step 12 records the reason; Part 1 *Journals and accounts* and *Posting and permissions*. | `G220-08`, `G220-09`, `G221-13` closed; `G220-15` opened (D365 test of the note) |
| Q04 Write-off approval and limits | A write-off from Aged balances or Collections creates a WOJL. Approval is manual: mark it ready and notify the approver by Teams or email; CR 16959 (Proposed) will automate the notification and post under a threshold. The CR 8769 approval matrix is not live and is not to be published: leave a placeholder for limits until CR 16959 is agreed and configured. For now Chris Clarke or Arash Najafi approves every WOJL. Officers can create write-offs only with write-off access, requested through a BAU ticket that Chris Clarke approves (16470). OK creates the WOJL with the transactions marked; the invoice settles only when the journal posts, automatically once approved (16838); until then it shows as open. Reason codes: BANK FEE, FOREX, OVER/SHORT, SHORT PAY and OVER PAY for officers; PENNY DIFF not to be used; BADDEBTS for Chris Clarke only. | 3.6 rewritten: Description, Responsibility (Approver: Chris Clarke or Arash Najafi), a limits placeholder (ACTION note), the access pre-requisite (contact the BAU Support team, D-083: the user group is not named), reason codes, the WOJL, *Report as ready*, notify the approver, posting and settlement after approval. Part 1 *Residual write-off* and *Journals and accounts*. | `G221-14`, `G221-18`, `G221-19` closed; `G221-15` open, waiting for CR 16959 |
| Q05 Checks before a transfer, distribution or restoration | Transfer: confirm the destination from written evidence (the remittance, or a customer email naming the invoices) and check that the destination customer code matches in CW1 and D365 (same legal entity and currency). Parent-child: D365 cannot track it, so no hierarchy references; work it out from the remittance or the history of previous paid receipts from the same payer. Restoration: confirm the original overpayment voucher and why it is put back. No sign-off for any of them. Evidence: keep the remittance or email in CW1 (documents are not attached in D365) and add a note on the Collections page of every account involved (voucher, amount, currency, reason, where the evidence is). 3.4.3 step 5: note on the parent account, for example "USD x left unallocated: awaiting remittance for remaining invoices". | Part 1 *Parent and child accounts* and the three *Before you post* tables; pre-requisites of 3.3.1, 3.4.1 and 3.5.1; note steps in 3.3.3, 3.4.3 (step 5) and 3.5.2. | `TF-02`, `PC-01`, `PC-02`, `RO-03`, `PC-04` closed; `TF-06` closed (transfers stay within one legal entity and currency) |
| Q06 Choosing the correction | Settled on the wrong account: undo (3.1), transfer (3.3), then settle against the correct invoices, with a note on both accounts at each step. An overpayment is restored with 3.5. A write-off posted in error is fixed by reversing the original WOJL (no approval), not with 3.5 or a new journal. | Topic 3 Description (the out-of-scope sentence is replaced); 3.5 renamed *Restore an Overpayment Amount*, with its Description, Initiation, Contents line, roles matrix and overview; 3.3.1 pre-requisite. | `TF-05`, `RO-02` closed; `G220-16` opened (round 2) |
| Q07 Overpayment ledger and clearing account | Show both: 100949 Bank to bank transfer clearing (an asset account) is still the offset for transfers; 200060 Customer overpayments (a liability account) is the Overpayment ledger. Write-offs post to 540052 Discounts & write offs (SHORT PAY confirmed in 16838). | Part 1 *Journals and accounts* and *Restoration entry*; 3.3.1 step 12; 3.4.1 step 12; 3.5.1 step 13; 3.6 steps 7 and 11. | `CPJ-09`, `TF-03`, `RO-01` closed |

The round also checked the rest of the guide against the answers. The other v2.1 referrals to the Collections team in 2.1.3 (an invoice that matches no open invoice, an amount that differs for an unclear reason) stay: they are hand-offs to the Collections team, which is where Maria places the Collections Officer. One new conflict came up: `G220-17`, the bank fee in 2.1.3 step 37 (round 2).

---

## 8. Round 2 plan (D-085)

Round 2 goes to Maria Pabalan with v3.1 and asks only what her round 1 answers opened and no source can give: three questions. Pages come from Word's Contents, updated by Daniel in the v3.1 review copy on 22 November (D-089); step pages keep their place within each subtopic. The board holds the question text.

### 8.1 Asked in round 2

| Question | Items | Where |
|---|---|---|
| Q08 Copy-paste method (follows Q01) | `G220-14` | 2.4 (p. 40) |
| Q09 Reversing a write-off posted in error (follows Q06) | `G220-16` | Topic 3 Description (p. 41) |
| Q10 Bank fee on a bank statement payment | `G220-17` | 2.1.3 step 37 (p. 31) |

### 8.2 Not asked

| Route | Items | What happens |
|---|---|---|
| Waiting for a change request | `G221-15` (write-off limits: CR 16959) | The ACTION note in 3.6 stays until the CR is agreed and configured. |
| Check in D365 (clean-session test) | `G220-15` (the note on the Collections page), `G220-13` (report paths, non-blocking), `CPJ-01`, `CPJ-02`, `CPJ-03`, `CPJ-06`, `CPJ-08`, `CPJ-13`, `CPJ-14`, `CPJ-16`, `CPJ-20`, `G221-08`, `G221-09`, `G221-10`, `G221-12`, `G221-16`, `G221-17` | Screen labels, navigation and controls. |
| Check against the AR Training D365 Part 2 recording | `G220-10`, `CPJ-05`, `CPJ-10`, `CPJ-11`, `TF-04`, `PC-03` (and `TF-01`, `PC-06`, `RO-04`) | Unchanged from round 1. |
| Check against the 11 November direct debit recording | `G220-18` | With `G240-08`, when 240 is updated. |
| Recording of the intercompany session | `G220-11` | Non-blocking. |
| Sign-off | `G220-01` | BPO sign-off of v3.0. |

---

## 9. Change log

| Date | Change |
|---|---|
| 2026-11-10 | Register created with the v3.0 working draft: version 2.1 and 221 Customer Payment Corrections v0.1 consolidated, with Maria Pabalan's answers of 10 November 2026 applied (D-055). |
| 2026-11-16 | Formatting brought in line with D-059 to D-061 (D-062): Bullet 1.2 bullets, topic numbers in link text, notes to the author in the ACTION: REVIEW REQUIREMENT style. The legacy yellow highlight on the Part 3 heading is replaced by an ACTION note and item `G220-12` (empty report descriptions). Files renamed with the `CLAUDE-` prefix (D-056). |
| 2026-11-17 | Review comments cut under D-067 (D-074): 123 → 53, one per open blocking item at the place it matters most; the 70 removed are listed in section 4.1 and their items stay open in their registers. First question round prepared on the board (D-069). The PDF beside the Word file is out of date (D-064). |
| 2026-11-18 | Version history dates for 1.0, 2.0 and 2.1 shortened to month and year (February 2025, November 2025, January 2026), as in Daniel Moreira’s Word copy of the 16 November build; no other change. His copy predates the comment cut of D-074, so the repository copy stays the current one. |
| 2026-11-18 | Round 1 review: `G220-03` closed (roles confirmed by Maria Pabalan's reply of 10 November and Daniel Moreira) and `G220-12` closed by a scope decision (D-081); `G220-13` added (non-blocking, the Part 3 paths). Their two review comments and the Part 3 ACTION note are removed: 53 → 51 comments. The PDF beside the Word file is out of date (D-064). |
| 2026-11-18 | `G220-05` and `CPJ-21` closed (D-083): the guides do not name security roles; Part 1 *Posting and permissions* now says the manager requests the D365 profile and to contact the BAU Support team. Two review comments removed: 51 → 49. |
| 2026-11-18 | Round 1 rebuilt under D-085 as seven questions (section 7): 20 items asked; `G220-02`, `G221-06`, `G221-11`, `CPJ-15`, `CPJ-18` and `CPJ-19` closed from the sources, with `CPJ-18` and `CPJ-19` written into Part 1 *Posting and permissions*; the rest routed to drafting, the recording or the D365 test. Review comments 49 → 44; comments for asked items carry the question number. Favorites reminders removed from four navigation steps (D-084). |
| 2026-11-18 | Page breaks (D-086): the Part 2 and Part 3 headings now start on a new page and topic 1 shares the Part 2 heading's page; the Contents page numbers are refreshed. No item changes. |
| 2026-11-18 | Page breaks (D-087): procedures 2.1.1 to 2.1.3, 2.2.1 and 2.2.2 now start on a new page, like every other subtopic; the Contents page numbers are refreshed. No item changes. |
| 2026-11-18 | The Contents now carries Word's numbers (D-089). Against the LibreOffice layout, Word runs Key concepts one page longer, 2.1.1 one page shorter and 2.1.3 one page longer, so every heading from 2.2 on is one page later. |
| 2026-11-18 | Round 1 (seven questions, section 7) sent to Maria Pabalan by Daniel Moreira in ADO Task 16993 (the 221 task, now used for 220), with the review copy. Page references from Word's Contents for every heading (D-089). |
| 2026-11-22 | Round 1 answered by Maria Pabalan (ADO Task 16993, 19 November) and applied (section 7.3, D-091): the Receipting Officer is the role again, as in v2.1; topic 6 is the direct debit customer payment journal (DD-CPJL) procedure, taken from 240 topic 2.1 with its approval workflow and approvers; new 2.4 copy-paste method (placeholder); 2.2 limited to two cases and posted once, without approval steps; 3.5 renamed *Restore an Overpayment Amount*; 3.6 rewritten for the write-off journal (WOJL) and its manual approval, with a limits placeholder for CR 16959; checks, evidence and Collections-page notes in 3.1, 3.3, 3.4 and 3.5; account numbers 100949, 200060 and 540052. 22 items closed (`G220-04`, `G220-06` to `G220-09`, `G221-07`, `G221-13`, `G221-14`, `G221-18`, `G221-19`, `TF-02`, `TF-03`, `TF-05`, `TF-06`, `PC-01`, `PC-02`, `PC-04`, `RO-01`, `RO-02`, `RO-03`, `CPJ-07`, `CPJ-09`) and `G220-03` closed again; five opened (`G220-14` to `G220-18`). Review comments 44 → 28. The eight notes in the undefined *NoteText* style are now plain cell notes with a bold **Note:**, as the template's own are (LibreOffice dropped the tables around them). Round 2 (three questions, section 8) drafted on the board. Contents page numbers refreshed from the layout. The PDF beside the Word file is out of date (D-064). |
| 2026-11-22 | Version 3.1 (D-092): the Word file is renamed `CLAUDE-220-Customer Payments PG v3.1.docx`, every link is updated, and the guide's version history has a 3.1 row; the 3.0 row again says what v3.0 was. New section *Versions of the guide* lists what changed in v3.1. The extra row moves every heading one page later in the layout: the Contents and the round 2 pages are refreshed (Q08 p. 41, Q09 p. 42, Q10 p. 32). The register and preview keep their file names (CLAUDE.md). |
| 2026-11-22 | Word's Contents for v3.1 (Daniel Moreira, 22 November) written into the guide: Word matches the layout to 3.5.1 and is one page earlier from 3.5.2 on, and does not add a page for the 3.1 version row. Round 2 pages from Word: Q08 p. 40, Q09 p. 41, Q10 p. 31. Round 2 is ready to send. |
| 2026-11-22 | Version history (D-095): rows 3.0 and 3.1 list Maria Pabalan, then Daniel Moreira, as authors, with descriptions of a few words. The table already fitted on its page in Word, so the pages do not change. |
| 2026-11-22 | Links to other guides (D-096): the 7 references to 230 Collections, 240 Direct Debit and 260 O2C Getting Started now link to their published files on the Training Hub. `G220-19` added for the receipting spreadsheet, which has no link (review comment at 2.1.3 step 21; comments 28 → 29). The pages do not change. |
| 2026-11-23 | Roles, not people (D-099): Chris Clarke is now the Group Billing and Credit Manager and Arash Najafi the Collections Manager in 3.6 (approver, write-off access, BADDEBTS, notify step), in Part 1 (the WOJL row) and in topic 6. The Part 1 DD-CPJL row and the topic 6 description and step 22 point to the approvers under Responsibility instead of listing names. `G220-20` added for the roles of Maria Pabalan and Zi Chen (review comment; comments 29 → 30). The pages do not change. |
| 2026-11-23 | Placeholders for the review cycle (D-097): the bank-fee row in 2.1.3 step 37 (`G220-17`, Q10) now ends with a note in the **ACTION: REVIEW REQUIREMENT Char** style, *To be confirmed: this row, or a write-off with 3.6 Write Off a Bank Fee or Small Residual.* Q08 and Q09 were already marked. The pages do not change. |
