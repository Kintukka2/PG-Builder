# Validation Register: 240 Direct Debit and Credit Card Payments

| Field | Value |
|---|---|
| Guide (editable source) | [`240-Direct Debit and Credit Card Payments PG v0.1.docx`](../01-procedure-guides/240-Direct%20Debit%20and%20Credit%20Card%20Payments%20PG%20v0.1.docx) · [PDF](../01-procedure-guides/240-Direct%20Debit%20and%20Credit%20Card%20Payments%20PG%20v0.1.pdf) |
| Markdown preview | [`PG-240-Direct-Debit-and-Credit-Card-Payments-DRAFT.md`](../01-procedure-guides/PG-240-Direct-Debit-and-Credit-Card-Payments-DRAFT.md) |
| ADO | Task 16894 PG Creation - Direct Debit |
| Status | Working draft skeleton v0.1 (D-053). Draft ready for review from 16 November 2026, after Maria Pabalan's training recording of 11 November. |
| Last updated | 2026-11-09 |
| Items | 9 guide-level items (`G240`), all open: 8 blocking, 1 non-blocking |

This file is the guide's **question log** (D-016). Each item is a Word review comment by "Validation register" (VR). The open scoping questions and the answers from the 9 November meeting are in the doc *240 Direct Debit Scoping Questions* (https://claude.ai/artifact/SegmHCWvsPWuHYeJiLEQdo).

---

## 1. Sources

| Source | What this guide takes from it |
|---|---|
| Scoping meeting, 9 November 2026 (Teams transcript and AI notes; held outside the repository) | Scope, structure, roles, approval, failed payments, eBanking ownership, placement, credit cards, dates (D-053). |
| Maria Pabalan's training recording, 11 November 2026 (pending) | The steps for every topic; replaces the legacy steps in topics 1 and 2.1. |
| [230 Collections v2.4](../01-procedure-guides/230-Collections%20PG%20v2.4.docx), topic 2.4 (legacy, v2.1 April 2026) | Topic 1 steps, until the recording confirms them (D-044). |
| 220 Customer Payments v2.1, section 5 (legacy; held outside the repository) | Topic 2.1 steps and screenshots, until the recording confirms them (D-044). |

---

## 2. Structure (agreed 9 November)

Context first (Part 1), then short how-to topics, then exceptions; credit cards follow with their own topics and exceptions, and can move to their own guide later. Topics not ready yet stay in as placeholders marked **Being worked on**, so the structure stays stable while content is added.

| Topic | Content in v0.1 | Comes from |
|---|---|---|
| 1. Maintain a Customer's Direct Debit Details | Legacy steps, flagged | Recording, 11 November |
| 2.1 Run the Mid-Month Direct Debit Batch | Legacy steps, flagged | Recording, 11 November |
| 2.2 Run an Ad Hoc Direct Debit | Placeholder | Recording, 11 November |
| 3. Approve a Direct Debit Run | Description; placeholder procedure | Recording, 11 November |
| 4.1 Follow Up a Failed Direct Debit | Description; placeholder procedure | Recording, 11 November |
| 4.2 Fix Direct Debit Errors | Placeholder | Recording, 11 November |
| 4.3 Process a Direct Debit Reversal | Placeholder | A later session with Maria Pabalan |
| 5.1 to 5.4 Credit card topics | Placeholders | When credit card payments go live |

---

## 3. Guide-level items (`G240`)

**Priority:** **B** = blocks publication. **N** = non-blocking. **Method:** **Rec** = recording. **Test** = D365 test. **SME** = subject-matter expert or process owner. **Dec** = project decision.

| ID | Item to confirm | Location | Priority | Method | Status |
|---|---|---|---|---|---|
| G240-01 | Code 240 exists in the O2C numbering standard; the title Direct Debit and Credit Card Payments is proposed. Confirm the title, and whether credit cards stay in this guide or move to their own guide in the 240-249 family later (meeting 9 November). | Cover | B | Dec | Open |
| G240-02 | Confirm the BPO. The meeting transcript says "AP will be Chris Clarke"; the AI notes read it as Chris Clarke's role alongside the approvers. | Version history | B | SME | Open |
| G240-03 | Check topics 1 and 2.1 against the 11 November recording. Their steps come from legacy 230 Collections 2.4 (v2.1, April 2026) and 220 Customer Payments 5 (v2.1), which are reference evidence only (D-044). | Part 1 High-level process | B | Rec | Open |
| G240-04 | Confirm the events that start these tasks from the 11 November recording. | Part 1 High-level process | B | Rec | Open |
| G240-05 | Confirm the role names. The meeting called them the receiving team, collection officers and the approvers Chris and Arash; 220 Customer Payments calls the receiving role Receipting Officer. | Part 1 Stream | B | SME | Open |
| G240-06 | Add the links: Maria Pabalan's scheduling file, the latest direct debit user story in ADO (its acceptance criteria), and the 11 November training recording. Long documents go in Additional Resources or the training hub, not in this guide. | Part 1 Key concepts | N | SME | Open |
| G240-07 | Check these steps against the 11 November recording, including who creates a new eBanking record: the meeting said the receiving team adds new customers to eBanking, while the legacy steps let the Collections Officer create one. | Topic 1 | B | Rec, Test | Open |
| G240-08 | Check these steps against the 11 November recording, and confirm they describe the mid-month batch (legacy 220 5 is a general direct debit run). | Topic 2.1 | B | Rec, Test | Open |
| G240-09 | Confirm when credit card payments go live and who owns each step, and whether they stay in this guide (meeting 9 November: direct debit first). | Topic 5 | B | SME | Open |

---

## 4. Change log

| Date | Change |
|---|---|
| 2026-11-09 | Register created with the v0.1 skeleton, built from the 9 November scoping meeting (D-053). |
