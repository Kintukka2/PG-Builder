# Validation Register: 230 Collections v2.4 (draft)

| Field | Value |
|---|---|
| Guide (editable source) | [`230-Collections PG v2.4.docx`](../01-procedure-guides/230-Collections%20PG%20v2.4.docx) · [PDF](../01-procedure-guides/230-Collections%20PG%20v2.4.pdf) |
| Based on | Published 230 Collections PG v2.3 (October 2026), held outside this repository |
| ADO | Task 16886 PG Update - Collections (O2C) |
| Status | Draft, pending BPO sign-off. Version 2.3 stays the published guide until 2.4 and 220 Customer Payments v3.0 are both signed off (D-051; D-055: the corrections first drafted as 221 are now in 220 v3.0). |
| Last updated | 2026-11-10 |
| Items | 4 guide-level items (`G230`), all open and blocking |

Version 2.4 applies the 230 split shared with the O2C stakeholders on 2026-11-03 (D-046, D-050). It does not yet merge the nine AR Collections topic drafts: that restructure ([suite plan](../05-project-notes/O2C-PG-Suite-Plan.md), section 4.2) is the next major version. Each item below is a Word review comment by "Validation register" (VR).

---

## 1. Changes from v2.3

| # | Where | Change |
|---|---|---|
| 1 | Version history | Row 2.4 added (BPO spelled Christopher Clarke, as in the O2C PG numbering standard). |
| 2 | Part 1 Overview, stage 6 | "Correct payment allocations" removed; a sentence points to 220 Customer Payments. |
| 3 | Roles and responsibilities | Rows 6.5 to 6.8 removed. |
| 4 | Key concepts, Customer Payment Management | The lead-in says these corrections are in 220 Customer Payments (version 3.0); each row names its 220 topic (2.3, 3.1, 3.3 and 3.6). |
| 5 | Topic 6 Topic Overview | Rows 6.5 to 6.8 removed; a note points to 220 topics 2.3, 3.1, 3.3 and 3.6 and keeps 6.4 Debt Write-off here. |
| 6 | 6.3 Change Customer Status | The three optional transaction-level steps (*Exclude Transaction from Credit Management*, *Review the Customer transactions*, *Enable Exclude from Credit management*) moved here from 6.5, as steps 19 to 21, with the navigation to **Customer > Transactions > Transactions** added. |
| 7 | 2.4 Maintain Customer Direct Debit & eBanking Details | A note says the topic is planned to move to 240 Direct Debit and stays here until 240 is published. Content unchanged. |
| 8 | 6.5 to 6.8 | Removed: Settling Customer Accounts, Unsettling Customer Accounts, Transferring Open / Closed Payments and Bank Fees Write-off Process. They are 220 v3.0 topics 2.3, 3.1, 3.3 (replaced by the recording-based transfer steps) and 3.6. |
| 9 | Contents | Entries for 6.5 to 6.8 removed; page numbers regenerated (52 pages to 45). |

Unchanged: 6.4 Debt Write-off, every other topic, Part 3 Reports and Additional Resources.

---

## 2. Guide-level items (`G230`)

**Priority:** **B** = blocks publication. **Method:** **SME** = subject-matter expert or process owner. **Test** = D365 test in a clean session.

| ID | Item to confirm | Location | Priority | Method | Status |
|---|---|---|---|---|---|
| G230-01 | Version 2.4 needs BPO sign-off. Version 2.3 stays published until 2.4 and 220 v3.0 are both signed off, so settling, unsettling, transfers and bank fee write-offs are never missing from the live guides. | Version history | B | SME | Open |
| G230-02 | Confirm the split: 6.5 to 220 topic 2.3, 6.6 to 3.1, 6.7 to 3.3 (replaced by the transfer steps from the recent training), 6.8 to 3.6. First drafted as 221, now merged into 220 (D-055). | Topic 6 note | B | SME | Open |
| G230-03 | Confirm the transaction-level exclusion steps moved from 6.5, and whether the checkbox saves on its own or needs **Save**. In 6.5 they ran just before posting the settlement. | 6.3, steps 19 to 21 | B | SME, Test | Open |
| G230-04 | Confirm when 2.4 moves to 240 Direct Debit. Maria Pabalan confirms the remaining 240 scope by the week of 9 November 2026 (D-049, D-050). | 2.4 note | B | SME | Closed: 9 November meeting (D-053). 230 keeps this topic as a link to 240 topic 1; the published guide keeps the steps until 240 is published. |

---

## 3. Change log

| Date | Change |
|---|---|
| 2026-11-03 | Register created with the v2.4 draft (ADO Task 16886). |
| 2026-11-09 | `G230-04` closed by the 9 November meeting (D-053). |
| 2026-11-10 | The corrections that moved out of 230 now point to 220 Customer Payments v3.0 (topics 2.3, 3.1, 3.3 and 3.6) instead of 221, which is merged into 220 (D-055). Word file and PDF rebuilt; `G230-01` and `G230-02` reworded. |
