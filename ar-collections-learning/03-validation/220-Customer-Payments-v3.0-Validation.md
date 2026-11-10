# Validation Register: 220 Customer Payments v3.0 (working draft)

| Field | Value |
|---|---|
| Guide (editable source) | [`220-Customer Payments PG v3.0.docx`](../01-procedure-guides/220-Customer%20Payments%20PG%20v3.0.docx) |
| Markdown preview | [`PG-220-Customer-Payments-v3.0-DRAFT.md`](../01-procedure-guides/PG-220-Customer-Payments-v3.0-DRAFT.md) |
| Status | Working draft v3.0 (D-055): consolidates version 2.1 and 221 Customer Payment Corrections v0.1. Not shared yet; needs BPO sign-off. Version 2.1 stays published until 3.0 passes its gates. |
| Last updated | 2026-11-10 |
| Items | 11 guide-level items (`G220`), all open: 10 blocking, 1 non-blocking. 111 carried review comments from 221 v0.1. |

This file is the guide's **question log** (D-016). It holds the guide-level items, which are scoped to this guide and never renumbered. Review comments carried from 221 keep their ID, for example *CPJ-14* or *G221-07*, and their source register stays the record for them: an answer recorded there applies here (D-048). Each open item that affects the text is a Word review comment by "Validation register" (VR).

---

## 1. Sources

| Source | Draft register | What this guide takes from it |
|---|---|---|
| 220 Customer Payments v2.1 (published, January 2026) | [Cross-comparison](Legacy-O2C-PG-Cross-Comparison.md) | Topics 1, 2.1 (with 2.1.1 to 2.1.3), 2.2 (with 2.2.1 and 2.2.2), 3.2 and 4 (4.1 to 4.5), with their screenshots; Part 1 key concepts on bank statements, ExFlow and matching; Part 3 reports; the troubleshooting table. Section 5 (direct debit) is now in 240 (D-053). |
| [221 Customer Payment Corrections v0.1](../01-procedure-guides/221-Customer%20Payment%20Corrections%20PG%20v0.1.docx) | [221-Customer-Payment-Corrections-Validation.md](221-Customer-Payment-Corrections-Validation.md) | Topics 2.3 (was 1), 3.1 (was 2) and 3.3 to 3.6 (were 3 to 6), with their review comments; Part 1 settlement terms and CPJL controls. Its own sources are the Transfers, Parent Payment Distribution and Restoration topic drafts, the CPJL controls reference and legacy 230 sections 6.5, 6.6 and 6.8 (see its register and the [Part 2 register](Part2-CPJL-and-Transfers-Validation.md)). |

---

## 2. Assembly decisions

| # | Decision | Reason |
|---|---|---|
| A1 | 221 Customer Payment Corrections is merged into 220, and code 221 is withdrawn (D-055). | Maria Pabalan confirmed on 10 November 2026 that Collections Officers do the tasks of both guides. 221 was proposed only for a split by role (D-046). |
| A2 | Topic 2 *Settle Customer Payments* holds the three settlement methods, each with its own procedure (2.1 bank statement, 2.2 manual payment journal, 2.3 open customer transactions), and a *Which method to use* table at the top. | SME request of 10 November 2026 (more than one way to settle); one task per subtopic (D-045, as in 230 v3.0). |
| A3 | Topic 3 *Correct Customer Payments* holds every correction made after posting: 221 topics 2 to 6 and v2.1 4.3 Reverse a Customer Payment Journal. | One stage for corrections; the reversal sits next to the other corrections. |
| A4 | v2.1 procedures and screenshots are kept as they are, with the role changed to Collections Officer and the section numbers in cross-references updated. Conflicts are `G220` items. | v2.1 is the published guide; same approach as 230 v3.0 (D-052). |
| A5 | 221 topics keep their steps and review comments, with item IDs unchanged. Answered items are applied (section 6). | Item IDs stay stable after a merge (suite plan section 1). |
| A6 | Topic 6 *Process Direct Debit Customer Payments* links to 240 topic 2 instead of repeating the steps. | D-053. |
| A7 | Topic 5 *Process Intercompany Customer Payments* is a placeholder marked *Being worked on*, for Receipting Officers. | SME, 10 November 2026: Receipting Officers process intercompany (ICO) payments only. |
| A8 | Rebuilt in the master template: the v2.1 *next page* callouts and blank page-break paragraphs are removed, and every topic and subtopic starts on a new page. | General cleanup of the v2.1 formatting (user request). |

---

## 3. Guide-level items (`G220`)

**Priority:** **B** = blocks publication. **N** = non-blocking. **Method:** **Test** = D365 test in a clean session. **Rec** = recording or transcript review. **SME** = subject-matter expert or process owner. **Dec** = project decision.

| ID | Item to confirm | Location | Priority | Method | Status |
|---|---|---|---|---|---|
| G220-01 | Version 3.0 consolidates 221 Customer Payment Corrections into this guide (D-055). Maria Pabalan confirmed on 10 November 2026 that Collections Officers do the tasks of both guides, so the split by role that 221 was proposed for (D-046) does not apply. Version 3.0 needs BPO sign-off; version 2.1 stays the published guide until 3.0 passes its gates. | Version history | B | Dec | Open |
| G220-02 | Confirm the events that start these tasks. They come from v2.1 (Part 1 Initiation) and from 221 (G221-04, TF-01, PC-06 and RO-04). | Part 1 High-level process | B | SME | Open |
| G220-03 | Confirm the roles. Maria Pabalan (10 November 2026): Collections Officers do the tasks of v2.1, which Receipting Officers did before the April go-live, and Receipting Officers process intercompany (ICO) payments only. The 9 November direct debit meeting (D-053) gave direct debit processing, adding new customers to eBanking and maintaining alternate names to the receiving team. Confirm topics 4.4, 4.5 and 6. | Part 1 Stream | B | SME | Open |
| G220-04 | Confirm this wording. In v2.1, payments that the receipting team could not resolve were referred to the Collections team; Collections Officers now process the payments themselves. | Part 1 Key concepts | B | SME | Open |
| G220-05 | Confirm the security role needed to post a CPJL. Maria Pabalan (10 November 2026) is not sure of it and suggests checking with Tony Chen (CPJ-21). | Part 1 Key concepts | B | SME | Open |
| G220-06 | Confirm the settlement methods that Collections Officers use and when each one is used. Maria Pabalan shows them several ways (10 November 2026); this guide documents three (2.1 to 2.3). Add a subtopic for any other method. | Topic 2 Settle Customer Payments | B | SME | Open |
| G220-07 | Some steps refer a transaction to the Collections team, or ask it to update the customer's eBanking reference. They date from when Receipting Officers did this work. Confirm what a Collections Officer does now in each case. | 2.1.3 Process Customer Settlements – Red Status | B | SME | Open |
| G220-08 | Confirm the approval steps. Version 2.1 says some journals need an approver's approval before posting (its roles table names the Accounts Receivable Manager). Maria Pabalan (10 November 2026): a CPJL needs no approval. Confirm which journal names, if any, still need approval, and who approves. | 2.2.1 Create a Customer Payment Journal | B | SME | Open |
| G220-09 | Confirm when the journal is posted. In v2.1, 4.1 (now 2.2.1) posts the journal, and 4.2 (now 2.2.2) settles it and posts it again. Confirm whether the journal is posted once, after it is settled. | 2.2.2 Settle the Customer Payment Journal | B | SME, Test | Open |
| G220-10 | Check topics 2.3, 3.1 and 3.6 against current D365 or a recording (they come from legacy 230, reference evidence only: D-044; was G221-03), and topics 3.3 to 3.5 and the CPJL controls against the AR Training D365 Part 2 recording (SRC-01). | Topic 3 Correct Customer Payments | B | Test, Rec | Open |
| G220-11 | Add the intercompany (ICO) payment steps from Maria Pabalan's session with Amy on Friday 6 November 2026 (recording). Confirm the example legal entities (101a and 238a). | Topic 5 Process Intercompany Customer Payments | N | Rec | Open |

---

## 4. Carried review comments by section

Every review comment in the Word guide, in document order. IDs not starting `G220` are carried from 221 v0.1.

| Section | Items |
|---|---|
| Cover and version history | `G220-01` |
| Part 1 High-level process | `G220-02`, `G220-03` |
| Part 1 Key concepts | `G220-04`, `G221-06`, `CPJ-02`, `TF-03 / CPJ-09`, `CPJ-14`, `CPJ-01 / CPJ-02`, `CPJ-03 / CPJ-04`, `CPJ-05`, `CPJ-07`, `CPJ-06`, `CPJ-08 / CPJ-09 / TF-03 / RO-01`, `CPJ-10`, `CPJ-11`, `CPJ-12`, `CPJ-13`, `CPJ-14 / CPJ-15`, `CPJ-16 / CPJ-17`, `PC-04`, `PC-01`, `PC-02`, `PC-04 / PC-05`, `CPJ-06`, `RO-01 / CPJ-09`, `TF-02`, `CPJ-07`, `CPJ-04`, `CPJ-07`, `CPJ-04`, `TF-03 / CPJ-09`, `RO-03`, `CPJ-07`, `CPJ-04`, `CPJ-10`, `CPJ-11`, `CPJ-16 to CPJ-21`, `G220-05` |
| Topic 2 Settle Customer Payments | `G220-06` |
| Topic 2.1 Settle Bank Statement Payments | `G220-07` |
| Topic 2.2 Record and Settle a Manual Payment Journal | `G220-08`, `G220-09` |
| Topic 2.3 Settle Open Customer Transactions | `G221-07`, `G221-08`, `G221-09`, `G221-10`, `G221-11` |
| Topic 3 Correct Customer Payments | `CPJ-17 / CPJ-19 / TF-05 / TF-06`, `PC-01 / CPJ-17 / CPJ-19`, `RO-02 / CPJ-17 / CPJ-19`, `G220-10` |
| Topic 3.1 Undo a Settlement | `G221-12`, `G221-13` |
| Topic 3.3 Transfer Funds Between Customer Accounts | `CPJ-21`, `TF-05`, `CPJ-01`, `CPJ-01 / CPJ-02`, `CPJ-03`, `CPJ-01`, `CPJ-05`, `CPJ-06`, `CPJ-03`, `CPJ-08`, `TF-03`, `CPJ-12`, `CPJ-01 / CPJ-05`, `CPJ-06`, `TF-04`, `CPJ-13`, `CPJ-14`, `CPJ-15`, `CPJ-16 / CPJ-17`, `CPJ-18`, `CPJ-19` |
| Topic 3.4 Distribute a Parent Account Payment Across Child Accounts | `CPJ-21`, `CPJ-01`, `CPJ-01 / CPJ-02`, `CPJ-03`, `CPJ-01`, `CPJ-05`, `CPJ-06`, `CPJ-03`, `CPJ-08`, `TF-03 / PC-03`, `CPJ-12`, `CPJ-01 / CPJ-05`, `CPJ-06`, `PC-03`, `CPJ-13`, `CPJ-14`, `CPJ-15`, `CPJ-16 / CPJ-17`, `PC-04`, `CPJ-18`, `CPJ-19` |
| Topic 3.5 Restore a Written-Off or Overpayment Amount | `CPJ-21`, `CPJ-01`, `CPJ-01 / CPJ-02`, `CPJ-03`, `CPJ-01`, `CPJ-05`, `CPJ-06 / CPJ-07`, `CPJ-03`, `CPJ-10`, `CPJ-08`, `RO-01`, `CPJ-11`, `CPJ-12`, `CPJ-14`, `CPJ-15`, `CPJ-16 / CPJ-17`, `CPJ-18`, `CPJ-19` |
| Topic 3.6 Write Off a Bank Fee or Small Residual | `G221-14`, `G221-15`, `G221-16`, `G221-17`, `G221-18`, `G221-19`, `G221-20` |
| Topic 5 Process Intercompany Customer Payments | `G220-11` |

---

## 5. 221 items not carried as comments

221 guide-level items that are not review comments in this guide, and where each one is answered. The other `G221` items are carried as review comments. Part 2 register items keep that register as their record (answers of 10 November 2026: section 6).

| Item | Disposition |
|---|---|
| `G221-01`: Guide code 221 and the title Customer Payment Corrections are proposed (D-046), with the split from 230 Collections (legacy sections 6.5 to 6.8 move here). The register owner records the code in the O2C PG numbering register, and the BPO confirms the scope and the split, before this guide circulates beyond the project team. | Superseded: 221 is withdrawn and merged into 220 (D-055; `G220-01`). |
| `G221-02`: Confirm the business process owner (BPO) for this guide. Christopher Clarke is the BPO of 220 Customer Payments and of 230 Collections, which held legacy sections 6.5 to 6.8. | Answered: Christopher Clarke is the BPO of 220 (version history). |
| `G221-03`: Check topics 1, 2 and 6 against current D365 or a recording. They come from legacy 230 v2.3, which is reference evidence only (D-044). | Replaced by `G220-10`. |
| `G221-04`: Confirm the events that start topics 1, 2 and 6. They come from legacy 230. | Replaced by `G220-02`. |
| `G221-05`: Confirm the roles. Legacy 230 assigns settling, undoing a settlement and the bank fee write-off to the Collections Officer, with the Group Billing and Credit Manager also named for write-off journals. The roles for topics 3 to 5 are not confirmed (GOV-01, CPJ-16). | Answered for topics 3.3 to 3.5: Collections Officer (SME, 10 November 2026). The write-off approver stays open as `G221-14`. |

---

## 6. SME answers applied (Maria Pabalan, 10 November 2026)

From Maria's review comments on 221 v0.1 and the Teams chat of 10 November 2026 (D-055).

| # | Source | Answer | Applied in v3.0 | Items |
|---|---|---|---|---|
| 1 | Chat | Collections Officers do the tasks of 220 v2.1 (*Collection officers only*). They were given the ability after the April go-live; Receipting Officers did it before. | Every v2.1 task is the Collections Officer's; Part 1 roles and a note on the change. | `G220-03` (conflict with D-053 to confirm) |
| 2 | Chat | Intercompany (ICO) payments are done by Receipting Officers only, for example a customer paying into a bank account in 101a for an invoice in 238a. Covered with Amy on Friday 6 November. | Topic 5 placeholder. | `G220-11` |
| 3 | Chat | Collections Officers settle in more than one way. | Topic 2 with three methods and *Which method to use*. | `G220-06` |
| 4 | 221 comments (topics 3 to 5) | *Collection Officer* prepares transfers, distributions and restorations. | Process, roles and Responsibility in 3.3 to 3.5. | `GOV-01`, `G221-05` |
| 5 | 221 comment (Key concepts) | Collections and Receipting Officers may post a CPJL. | *Posting and permissions* table. | `CPJ-16` (the **Post** label still to test) |
| 6 | 221 comment (Key concepts) | No approvals are required for a CPJL. | *Posting and permissions* table; roles overview. | `CPJ-17`; `G220-08` (v2.1 approval steps) |
| 7 | 221 comment (Key concepts) | A Collections Officer can delete an unposted journal that is no longer needed. | *Posting and permissions* table. | `CPJ-20` (steps still to confirm) |
| 8 | 221 comment (Key concepts) | Not sure of the security role needed to post a CPJL: check with Tony Chen. | *Posting and permissions* table. | `CPJ-21`; `G220-05` |

---

## 7. Change log

| Date | Change |
|---|---|
| 2026-11-10 | Register created with the v3.0 working draft: version 2.1 and 221 Customer Payment Corrections v0.1 consolidated, with Maria Pabalan's answers of 10 November 2026 applied (D-055). |
