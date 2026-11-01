# Validation Register: 221 Customer Payment Corrections

| Field | Value |
|---|---|
| Guide (editable source) | [`221-Customer Payment Corrections PG v0.1.docx`](../01-procedure-guides/221-Customer%20Payment%20Corrections%20PG%20v0.1.docx) |
| Markdown preview | [`PG-221-Customer-Payment-Corrections-DRAFT.md`](../01-procedure-guides/PG-221-Customer-Payment-Corrections-DRAFT.md) |
| Status | Working draft v0.1. Code 221 is proposed (D-046): not yet recorded in the numbering register or confirmed by the BPO. Shared with the SME for review only (SME review pack v2); do not circulate further until it is (D-048). |
| Last updated | 2026-11-01 |
| Items | 20 guide-level items (`G221`), all open: 19 blocking, 1 non-blocking. 106 carried review comments from the topic drafts. |

This file is the guide's **question log** (D-016). It holds the guide-level items, which are scoped to this guide and never renumbered. Review comments carried from the topic drafts keep their ID, and their source register stays the record for them: an answer recorded there applies here (D-048). Each open item that affects the text is a Word review comment by "Validation register" (VR).

---

## 1. Sources

| Source | Draft register | What this guide takes from it |
|---|---|---|
| [Customer Account Transfers](../01-procedure-guides/TBC-AR%20Collections%20Customer%20Account%20Transfers%20PG%20v0.1.docx) | [Part 2 register](Part2-CPJL-and-Transfers-Validation.md) | Topic 3 (subtopics 3.1 to 3.3); Key concepts *Customer payment journal* and *Before you post a transfer*. |
| [Parent Payment Distribution](../01-procedure-guides/TBC-AR%20Collections%20Parent%20Payment%20Distribution%20PG%20v0.1.docx) | [Part 2 register](Part2-CPJL-and-Transfers-Validation.md) | Topic 4 (subtopics 4.1 to 4.3), retitled *Distribute a Parent Account Payment Across Child Accounts*; Key concepts *Parent and child accounts* and *Before you post a distribution*. |
| [Overpayment and Write-Off Restoration](../01-procedure-guides/TBC-AR%20Collections%20Overpayment%20and%20Write-Off%20Restoration%20PG%20v0.1.docx) | [Part 2 register](Part2-CPJL-and-Transfers-Validation.md) | Topic 5 (subtopics 5.1 and 5.2), retitled *Restore a Written-Off or Overpayment Amount*; Key concepts *Restoration entry* and *Before you post a restoration*. |
| [Customer Payment Journal Controls reference](../01-procedure-guides/../06-reference-guides/TBC-AR%20Collections%20Customer%20Payment%20Journal%20Controls%20Reference%20v0.1.docx) | [Part 2 register](Part2-CPJL-and-Transfers-Validation.md) | Key concepts *Journal set-up*, *Line coding*, *Validation and posting*, *Allocations and amounts* and *Not yet confirmed*. |
| Legacy 230 Collections PG v2.3 | [Cross-comparison](Legacy-O2C-PG-Cross-Comparison.md) | Topics 1 (section 6.5), 2 (section 6.6) and 6 (section 6.8), and the Key concept *Settlement*. Reference evidence only (D-044): every step carries a `G221` item until checked. |

---

## 2. Assembly decisions

| # | Decision | Reason |
|---|---|---|
| C1 | Topics follow the suite plan: 1 Settle, 2 Undo a Settlement, 3 Transfer, 4 Distribute, 5 Restore, 6 Write Off a Bank Fee or Small Residual. | Suite plan section 4.3; predecessor mapping 230 §6.5 → 1, §6.6 → 2, §6.7 → 3, §6.8 → 6 (D-046). |
| C2 | Topic 3 replaces legacy 230 §6.7. The legacy transfer steps are not carried. | The recording-based topic draft governs where it and legacy content disagree (D-044); the conflicts are in the cross-comparison, section 5. |
| C3 | The legacy optional steps that exclude a transaction from credit management are not in topic 1. A note points to 230 Collections topic 7.3. | That task belongs to Change Customer Account Status (suite plan, 230 topic 7.3). |
| C4 | The legacy pre-requisite "the required account status and reason for the change must be confirmed" is not used in topics 1, 2 and 6. | It is copied unchanged across legacy 230 section 6 and does not fit these tasks (`G221-07`). |
| C5 | The CPJL controls reference becomes Part 1 Key concepts. Each draft's *Before you post* table stays, retitled by task; the duplicate CPJL definition in *Restoration entry* is removed. | One definition per term; the task checklists stay next to each other in Part 1. |
| C6 | Roles come from legacy 230 for topics 1, 2 and 6. Topics 3 to 5 keep "To be confirmed". | No source names the role that prepares or posts a CPJL (`GOV-01`, `CPJ-16`). |
| C7 | Topic 4 is retitled *Distribute ...* and topic 5 *Restore a Written-Off or Overpayment Amount*. | Suite plan titles: a clear verb and object (T2). |

---

## 3. Guide-level items (`G221`)

**Priority:** **B** = blocks publication. **N** = non-blocking. **Method:** **Test** = D365 test in a clean session. **Rec** = recording or transcript review. **SME** = subject-matter expert or process owner. **Dec** = project decision.

| ID | Item to confirm | Location | Priority | Method | Status |
|---|---|---|---|---|---|
| G221-01 | Guide code 221 and the title Customer Payment Corrections are proposed (D-046), with the split from 230 Collections (legacy sections 6.5 to 6.8 move here). The register owner records the code in the O2C PG numbering register, and the BPO confirms the scope and the split, before this guide circulates beyond the project team. | Cover | B | Dec | Open |
| G221-02 | Confirm the business process owner (BPO) for this guide. Christopher Clarke is the BPO of 220 Customer Payments and of 230 Collections, which held legacy sections 6.5 to 6.8. | Version history | B | SME | Open |
| G221-03 | Check topics 1, 2 and 6 against current D365 or a recording. They come from legacy 230 v2.3, which is reference evidence only (D-044). | Part 1 High-level process | B | Test, Rec | Open |
| G221-04 | Confirm the events that start topics 1, 2 and 6. They come from legacy 230. | Part 1 High-level process | B | SME | Open |
| G221-05 | Confirm the roles. Legacy 230 assigns settling, undoing a settlement and the bank fee write-off to the Collections Officer, with the Group Billing and Credit Manager also named for write-off journals. The roles for topics 3 to 5 are not confirmed (GOV-01, CPJ-16). | Part 1 Stream | B | SME | Open |
| G221-06 | Confirm the settlement terms. They come from legacy 230 (Key concepts, Customer Payment Management, and sections 6.5, 6.6 and 6.8). | Part 1 Key concepts | B | SME | Open |
| G221-07 | Confirm the pre-requisites for topics 1 and 2. Legacy 230 gives the same pre-requisite for every procedure in its section 6 ("the required account status and reason for the change must be confirmed"), which does not fit settlement. | Topics 1 and 2 Procedure | B | SME | Open |
| G221-08 | Confirm the menu path to All customers. Legacy 230 uses Accounts receivable > Customers > All customers; the Favorites topic draft places All customers in the Credit and collections module. | Topics 1 and 2 Procedure | B | Test | Open |
| G221-09 | Confirm the labels and location of Settlements and Settle transactions. | Topic 1 Procedure | B | Test | Open |
| G221-10 | Confirm the Amount to settle label and how a partial settlement is entered. | Topic 1 Procedure | B | Test | Open |
| G221-11 | Confirm that the total must be 0.00 before posting, and what to do when the payment and the invoices differ by a small amount (a residual: see topic 6). | Topic 1 Procedure | B | SME, Test | Open |
| G221-12 | Confirm the labels and location of the Voucher link, Settlements and Undo settlement. | Topic 2 Procedure | B | Test | Open |
| G221-13 | Confirm the Reverse control, and whether undoing a settlement needs approval or a recorded reason. | Topic 2 Procedure | B | Test, SME | Open |
| G221-14 | Confirm who approves the write-off journal. Legacy 230 names the Group Billing and Credit Manager as responsible for creating write-off journals once a request is approved, while its procedure has the Collections Officer create the journal and submit it for approval. | Topic 6 Responsibility | B | SME | Open |
| G221-15 | Confirm the write-off rules: the largest residual that may be written off, who may write it off, and what evidence is kept. Legacy 230 gives none. | Topic 6 Procedure | B | SME | Open |
| G221-16 | Confirm the menu path and label. Legacy 230 uses Credit and collections > Collections > Aged balances; the Favorites and Aged Balances topic drafts ask whether the label is Aged balances or Age balances. | Topic 6 Procedure | B | Test | Open |
| G221-17 | Confirm the Write off control's label and location on Aged balances. | Topic 6 Procedure | B | Test | Open |
| G221-18 | Confirm the current reason codes and the ledger account each one posts to. These four come from legacy 230. | Topic 6 Procedure | B | SME, Test | Open |
| G221-19 | Confirm what happens on OK: whether the write-off posts and settles at once, or only after the journal is approved. Legacy 230 says it settles on OK and then sends the journal for approval, which conflicts. | Topic 6 Procedure | B | Test, SME | Open |
| G221-20 | Confirm the aging update batch job and its frequency. Legacy 230 gives every 10 minutes. | Topic 6 Procedure | N | Test | Open |

---

## 4. Carried review comments by section

Every review comment in the Word guide, in document order. IDs not starting `G221` are carried from the topic drafts.

| Section | Items |
|---|---|
| Cover and version history | `G221-01`, `G221-02` |
| Part 1 High-level process | `CPJ-17 / CPJ-19 / TF-05 / TF-06`, `PC-01 / CPJ-17 / CPJ-19`, `RO-02 / CPJ-17 / CPJ-19`, `SRC-01`, `G221-03`, `G221-04`, `TF-01`, `PC-06`, `RO-04`, `GOV-01`, `G221-05` |
| Part 1 Roles and responsibilities | `CPJ-16 / CPJ-17` |
| Part 1 Key concepts | `G221-06`, `CPJ-02`, `TF-03 / CPJ-09`, `CPJ-14`, `CPJ-01 / CPJ-02`, `CPJ-03 / CPJ-04`, `CPJ-05`, `CPJ-07`, `CPJ-06`, `CPJ-08 / CPJ-09 / TF-03 / RO-01`, `CPJ-10`, `CPJ-11`, `CPJ-12`, `CPJ-13`, `CPJ-14 / CPJ-15`, `CPJ-16 / CPJ-17`, `PC-04`, `PC-01`, `PC-02`, `PC-04 / PC-05`, `CPJ-06`, `RO-01 / CPJ-09`, `TF-02`, `CPJ-07`, `CPJ-04`, `CPJ-07`, `CPJ-04`, `TF-03 / CPJ-09`, `RO-03`, `CPJ-07`, `CPJ-04`, `CPJ-10`, `CPJ-11`, `CPJ-16 to CPJ-21` |
| Topic 1 Settle Customer Transactions | `G221-07`, `G221-08`, `G221-09`, `G221-10`, `G221-11` |
| Topic 2 Undo a Settlement | `G221-12`, `G221-13` |
| Topic 3 Transfer Funds Between Customer Accounts | `GOV-01`, `CPJ-21`, `TF-05`, `CPJ-01`, `CPJ-01 / CPJ-02`, `CPJ-03`, `CPJ-01`, `CPJ-05`, `CPJ-06`, `CPJ-03`, `CPJ-08`, `TF-03`, `CPJ-12`, `CPJ-01 / CPJ-05`, `CPJ-06`, `TF-04`, `CPJ-13`, `CPJ-14`, `CPJ-15`, `CPJ-16 / CPJ-17`, `CPJ-18`, `CPJ-19` |
| Topic 4 Distribute a Parent Account Payment Across Child Accounts | `GOV-01`, `CPJ-21`, `CPJ-01`, `CPJ-01 / CPJ-02`, `CPJ-03`, `CPJ-01`, `CPJ-05`, `CPJ-06`, `CPJ-03`, `CPJ-08`, `TF-03 / PC-03`, `CPJ-12`, `CPJ-01 / CPJ-05`, `CPJ-06`, `PC-03`, `CPJ-13`, `CPJ-14`, `CPJ-15`, `CPJ-16 / CPJ-17`, `PC-04`, `CPJ-18`, `CPJ-19` |
| Topic 5 Restore a Written-Off or Overpayment Amount | `GOV-01`, `CPJ-21`, `CPJ-01`, `CPJ-01 / CPJ-02`, `CPJ-03`, `CPJ-01`, `CPJ-05`, `CPJ-06 / CPJ-07`, `CPJ-03`, `CPJ-10`, `CPJ-08`, `RO-01`, `CPJ-11`, `CPJ-12`, `CPJ-14`, `CPJ-15`, `CPJ-16 / CPJ-17`, `CPJ-18`, `CPJ-19` |
| Topic 6 Write Off a Bank Fee or Small Residual | `G221-14`, `G221-15`, `G221-16`, `G221-17`, `G221-18`, `G221-19`, `G221-20` |
| Part 3: Reports | `GOV-04` |

---

## 5. Draft items not carried as comments

Part 2 register items that are not anchored as a review comment in this guide. They stay open in the [Part 2 register](Part2-CPJL-and-Transfers-Validation.md), which remains their record.

| Item | Disposition |
|---|---|
| `SRC-02`: Recording timestamps for the restoration, two-line transfer, parent-to-multiple-child, partial allocation and Simulate Posting demonstrations. | Open in the Part 2 register; not tied to a line of the guide text |
| `SRC-03`: What "PG/Ava follow-up support" in the notes refers to, and whether the guides should point to it. The master template's *Additional Resources* already lists **AVA - Atlas Virtual Assistant** and **Procedure Guides** as self-service resources, which is probably what the notes mean. | Open in the Part 2 register; not tied to a line of the guide text |
| `SRC-04`: Whether to adopt the Part 2 roadmap's Release 3A placement for transfers and restoration. Source 2 ranks *Transfer funds between accounts* 27, in Release 4. Proposed in D-036. | Open in the Part 2 register; not tied to a line of the guide text |
| `GOV-02`: Business process owner (BPO) for each guide. | Guide-level: `G221-02` |
| `GOV-03`: Destination guide and topic for the three guides and the reference (D-045). Proposed: 221 Customer Payment Corrections, topics 3, 4 and 5, and its Part 1 Key concepts (D-046). Merged into the 221 v0.1 working draft (D-048). | Guide-level: `G221-01` |
| `GOV-05`: SME factual review, a test by someone other than the author, and approval. | Open in the Part 2 register; not tied to a line of the guide text |

---

## 6. Change log

| Date | Change |
|---|---|
| 2026-11-01 | Register created with the v0.1 working draft, assembled from the topic drafts (D-045, D-046, D-048). |
| 2026-11-01 | Guide added to the SME review pack (v2) for review only (D-048 amendment). |
