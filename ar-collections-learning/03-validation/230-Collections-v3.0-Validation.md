# Validation Register: 230 Collections v3.1 (working draft)

| Field | Value |
|---|---|
| Guide (editable source) | [`CLAUDE-230-Collections PG v3.1.docx`](../01-procedure-guides/CLAUDE-230-Collections%20PG%20v3.1.docx) |
| Review PDF | [`CLAUDE-230-Collections PG v3.0.pdf`](../01-procedure-guides/CLAUDE-230-Collections%20PG%20v3.0.pdf) (out of date, D-064) |
| Markdown preview | [`PG-230-Collections-v3.0-DRAFT.md`](../01-procedure-guides/PG-230-Collections-v3.0-DRAFT.md) |
| Status | Working draft **v3.1** (D-092; versions below). **Maria Pabalan answered round 1 on 19 November** and the answers are applied (D-093), with the legacy 230 write-ins that waited for them; round 2 (one question, section 7) is ready on the board. v3.0 (D-052; ADO Task 16886): Shared with the SME for review only (SME review pack of 8 November; D-052 amendment); needs BPO sign-off. Formatting brought in line with D-059 to D-061 on 2026-11-16 (D-063); no content or item changes. Review comments cut to one per open blocking item on 2026-11-17 (D-067, D-075). Round 1 rebuilt as three questions (D-085, section 6). Version 2.3, then 2.4, stays published until 3.0 passes its gates. |
| Last updated | 2026-11-22 |
| Items | 12 guide-level items (`G230`): 2 open (both blocking: `G230-05`, `G230-15`) and 10 closed (`G230-06` to `G230-14`, `G230-16`). **63 Word review comments** (D-067): 3 guide-level and 60 carried from the topic drafts; 43 removed under D-067 (section 4.1), 11 when round 1 was rebuilt (section 6) and 20 when it was answered (section 6.3). Comments for items asked in round 2 start with the question number, for example *[Q04]*. |

This file is the guide's **question log** (D-016). It holds the guide-level items, which are scoped to this guide and never renumbered. Review comments carried from the topic drafts keep their ID and draft name, for example *Aged Balances VG-03*, and their source register stays the record for them: an answer recorded there applies here (D-048). Each open item that affects the text is a Word review comment by "Validation register" (VR).

---

## Versions of the guide

Each version that goes out for review keeps its number; when a round of answers is applied, the minor version goes up (D-092). The guide's own version history has a row for each version. The board card shows the current one.

| Version | Date | Sent to | What it is |
|---|---|---|---|
| 3.0 | 3 to 18 November 2026 | Maria Pabalan, with round 1 (ADO Task 16886, 18 November) | Legacy 230 (v2.4) rebuilt in the master template with the nine AR Collections topic drafts (D-052); formatting under D-059 to D-061 (D-063); review comments cut to one per open blocking item (D-067, D-075); round 1 rebuilt under D-085. |
| 3.1 | 22 November 2026 | Maria Pabalan, with round 2 (not sent yet) | Maria's round 1 answers applied (D-093), with the legacy 230 write-ins that waited for them. What changed is listed below. |

### What changed in v3.1

From Maria Pabalan's round 1 answers (ADO Task 16886, 19 November 2026; section 6.3, D-093), and the legacy 230 write-ins planned in round 1 (section 6.2).

- **2.7 Update Customer Details:** the legacy steps are replaced by a pointer to 200 Customer Onboarding and Maintenance, section 3.4, so there is one source of truth. 2.7 keeps a short line on when Collections Officers update customer details (a new AP contact or statement email from the customer), and an Important box: a change to a customer's name, address, VAT ID or country goes to License Management, not into D365. The guide does not name a channel for it (D-094).
- **5. Record a Customer Collection Activity:** follows the legacy 230 method on the customer's Collections page: activity type, Purpose (short title, with Maria's examples), Priority, Type (Email or Phone call) and Notes. The note must say who, when, which invoices (amount and currency), any promised payment date or dispute, what was sent or agreed, any follow-up and the officer's initials. One note per interaction (incoming and outgoing separate); internal emails get a note on every account involved; never record card numbers, bank account or BSB numbers, other payment credentials or personal opinions; no attachments in D365 (documents are kept in CW1). Key concepts gets *Writing a collection note*; the legacy comparison note is gone.
- **No attachments anywhere:** the legacy "attaching supporting documents is mandatory" requirement is removed from 2.6 and topic 8 too (topic 8 loses its *Attach Supporting Documentation* step); 2.6 gains a step to check that each activity has its Type, Purpose and a note that stands on its own.
- **6. Statements:** monthly statements are automated on the 5th, so officers send ad hoc statements only, when a customer asks. 6.2.1 sends straight away with Print management destination, to the contacts with Purpose = Business, dated today even if the customer asks for a month-end date. No customer is left out (direct debit, card, disputed and multi-currency customers included; statements split by currency). 6.2.2 checks the banner at the top of the page and records a note on the Collections page: "Statement dated <date> sent to <email>"; the Collections sent mailbox step is gone. 6.1.1 says that leaving Print management destination selected sends the statement. The legacy batch method note is gone.
- **New 7.1.3 Resend the Invoice to the Customer:** from legacy 230 §6.1 (Tax invoice journal > Document > Send > Copy, check Print management, OK), ending with the contact recorded as a collection activity.
- **Other legacy write-ins:** 2.2 has a note on opening the Collections page from the customer name and the 10-minute refresh; 4.1 says what to review and what to do when a balance is not valid; the workspace concept says which sections the guide uses.
- **Payment corrections are Receipting Officer work** (Maria Pabalan's 220 answers, D-091): the Collections workflow, *Customer Payment Management*, Part 1 and the topic 7 note now say to ask the Receipting team, and point to 220 v3.1.
- **Records:** 27 items closed and two opened (`G230-15`, `G230-16`, which closed before round 2 went out); review comments 82 → 63. The Contents page numbers are refreshed.

---

## 1. Sources

| Source | Draft register | What this guide takes from it |
|---|---|---|
| [Workspace](../01-procedure-guides/TBC-AR%20Collections%20Workspace%20PG%20v0.1.docx) | [PG-AR-Workspace-Validation.md](PG-AR-Workspace-Validation.md) | Topics 1.1 and 1.2; two Key concepts tables. |
| [Overdue Customers](../01-procedure-guides/TBC-AR%20Collections%20Overdue%20Customers%20PG%20v0.1.docx) | [PG-AR-Overdue-Customers-Validation.md](PG-AR-Overdue-Customers-Validation.md) | Topics 2.1 and 4.1; two Key concepts tables. |
| [Aged Balances](../01-procedure-guides/TBC-AR%20Collections%20Aged%20Balances%20PG%20v0.1.docx) | [PG-AR-Aged-Balances-Validation.md](PG-AR-Aged-Balances-Validation.md) | Topics 2.2 and 2.3; two Key concepts tables. |
| [Customer Account](../01-procedure-guides/TBC-AR%20Collections%20Customer%20Account%20PG%20v0.1.docx) | [PG-AR-Customer-Account-Validation.md](PG-AR-Customer-Account-Validation.md) | Topic 2.4 with 2.4.1 to 2.4.3; two Key concepts tables. |
| [Notes and Activities](../01-procedure-guides/TBC-AR%20Collections%20Notes%20and%20Activities%20PG%20v0.1.docx) | [PG-AR-Notes-and-Activities-Validation.md](PG-AR-Notes-and-Activities-Validation.md) | Topics 2.5 and 2.6; two Key concepts tables. |
| [Collection Activities](../01-procedure-guides/TBC-AR%20Collections%20Collection%20Activities%20PG%20v0.1.docx) | [PG-AR-Collection-Activities-Validation.md](PG-AR-Collection-Activities-Validation.md) | Topic 5; two Key concepts tables. |
| [Statement Preview](../01-procedure-guides/TBC-AR%20Collections%20Statement%20Preview%20PG%20v0.1.docx) | [PG-AR-Statement-Preview-Validation.md](PG-AR-Statement-Preview-Validation.md) | Topic 6.1 with 6.1.1 and 6.1.2; two Key concepts tables. |
| [Statement Distribution](../01-procedure-guides/TBC-AR%20Collections%20Statement%20Distribution%20PG%20v0.1.docx) | [PG-AR-Statement-Distribution-Validation.md](PG-AR-Statement-Distribution-Validation.md) | Topic 6.2 with 6.2.1 and 6.2.2; two Key concepts tables. |
| [Customer Invoices](../01-procedure-guides/TBC-AR%20Collections%20Customer%20Invoices%20PG%20v0.1.docx) | [PG-AR-Customer-Invoices-Validation.md](PG-AR-Customer-Invoices-Validation.md) | Topic 7.1 with 7.1.1 and 7.1.2; two Key concepts tables. |
| [Favorites (AR Collections pages only)](../01-procedure-guides/TBC-AR%20Collections%20Favorites%20PG%20v0.2.docx) | [PG-AR-Configure-Collections-Favourites-Validation.md](PG-AR-Configure-Collections-Favourites-Validation.md) | Key concept *Set up D365 for collections work*: the four AR Collections pages. The general steps are 260 topic 3. |
| [Personalized Views (AR Collections columns only)](../01-procedure-guides/TBC-AR%20Collections%20Personalized%20Views%20PG%20v0.1.docx) | [PG-AR-Personalized-Views-Validation.md](PG-AR-Personalized-Views-Validation.md) | Key concept *Set up D365 for collections work*: the recommended columns. The general steps are 260 topics 4 and 5. |
| [230 Collections v2.4 (draft, from published v2.3)](../01-procedure-guides/230-Collections%20PG%20v2.4.docx) | [230-Collections-v2.4-Validation.md](230-Collections-v2.4-Validation.md) | Part 1 Key concepts (Collections Workflow to High Level Integration Rules); topics 2 (description), 2.7, 2.8, 3, 4, 7 (description), 7.2 to 7.4 and 8; Part 3 Reports. Items `G230-03` and `G230-04` carry over. Legacy 1, 2.1, 2.2, 5 and 6.1 merge into 6.2, 2.2, 2.6, 5 and 7.1, with their extra content in notes. |

---

## 2. Assembly decisions

| # | Decision | Reason |
|---|---|---|
| V1 | Eight top-level topics, one per stage of the high-level process; each task is a subtopic (D-045). Draft topics become subtopics, and draft subtopics a third level (*PG Further Subdivision*, numbered N.M.K). | Suite plan section 4.2; legacy 230 already groups tasks under stage topics. |
| V2 | Where a topic draft and a legacy section cover the same task (2.2, 2.6, 5, 6.2 and 7.1), the draft's procedure is the topic and the legacy-only content was a note with a `G230` item. Since v3.1 those notes are resolved: topic 5 follows the legacy method (Maria Pabalan), and the rest is written in or dropped (D-093). | The recording governs (D-044); every legacy-only fact needed confirming. |
| V3 | Legacy topics keep their procedures, screenshots and numbering unchanged, under template headings with automatic numbers. | D-052: rebuilt in the master template; content changes wait for the SME and the test. |
| V4 | Topic 2.7 Update Customer Details points to 200 Customer Onboarding and Maintenance §3.4 instead of repeating legacy 2.3, with a short line on when Collections Officers update customer details and the License Management rule. | Maria Pabalan, round 1 (19 November 2026; D-093). Was: legacy 2.3 kept until decided (D-052 decision 4). |
| V5 | Legacy 2.4 Direct Debit stays as topic 2.8 until 240 Direct Debit is published. | D-049, D-051. |
| V6 | Carried review comments keep their draft name and ID, for example *Aged Balances VG-03*. | Suite plan section 1. |

---

## 3. Guide-level items (`G230`)

**Priority:** **B** = blocks publication. **N** = non-blocking. **Method:** **Test** = D365 test in a clean session. **Rec** = recording or transcript review. **SME** = subject-matter expert or process owner. **Dec** = project decision.

| ID | Item to confirm | Location | Priority | Method | Status |
|---|---|---|---|---|---|
| G230-05 | Version 3 is a working draft for ADO Task 16886, assembled from v2.4 and the nine AR Collections topic drafts (D-052). It needs BPO sign-off. Version 2.3, then 2.4, stays the published guide until version 3 passes its gates. | Version history | B | SME | Open |
| G230-06 | Confirm the events that start the Collections process. These come from legacy 230; the topic drafts add the start of each working day (Workspace) and customer requests for statements and invoices. | Part 1 High-level process | B | SME | Closed 2026-11-18 (D-085): the events come from legacy 230 Part 1 and the training; not asked. |
| G230-07 | Confirm the stream and process area. Legacy 230 uses O2C and Collections; the topic drafts use Accounts Receivable and AR Collections (cross-comparison conflict 11; SME question A2). | Part 1 Stream | B | SME | Closed 2026-11-18 (D-085): O2C and Collections, as in legacy 230 and the O2C numbering standard (D-070); the guide already shows them. |
| G230-08 | Confirm which legacy Aged balances content belongs in this topic: sorting by amount due, the aging icon legend, opening the customer's Collections page (cross-comparison conflict 12) and the 10-minute refresh (legacy control 9). | 2.2 Review Customer Aged Balances | B | SME, Test | Closed 2026-11-22 (legacy write-in, D-085): 2.2 has a note that clicking the customer name opens the Collections page and that aged balances refresh every 10 minutes; sorting by amount due is already step 11. The aging icon legend is an image in legacy 230 with no text to carry, so it is not added. |
| G230-09 | Confirm the activity control label (cross-comparison conflict 2) and whether reviewing attachments and correcting the record belong in this topic. | 2.6 Review All Customer Activities | B | SME, Test | Closed 2026-11-22: 2.6 checks that each activity has its Type, Purpose and a note, and corrects the record (legacy 230 §2.2). Attachments are not reviewed: Maria Pabalan, round 1 (ADO 16886, 19 November 2026): documents are not attached in D365. The control label stays with the D365 test (`Notes and Activities VG-07`). |
| G230-10 | Decide whether to keep this topic or replace it with a link to 200 Customer Onboarding and Maintenance §3.4, which covers the same task. | 2.7 Update Customer Details | B | Dec | Closed 2026-11-22 (Q01): Maria Pabalan, round 1 (ADO 16886, 19 November 2026): replace the steps with a link to 200 §3.4; keep a short line on when Collections Officers update details; changes to name, address, VAT ID or country go to License Management (`G230-16` asks how). |
| G230-11 | Confirm the activity fields and types, and whether supporting documents are mandatory (cross-comparison conflicts 2 and 3; legacy control 7; SME question B3.1). | 5 Record a Customer Collection Activity | B | SME, Test | Closed 2026-11-22 (Q02): Maria Pabalan, round 1 (ADO 16886, 19 November 2026): the legacy 230 method on the Collections page (Type, Purpose, Notes), with the note rules; no attachments in D365. |
| G230-12 | Confirm these statement controls before anyone sends a statement with this topic (legacy controls 1 to 4; cross-comparison conflicts 4 and 5; SME questions B5.1 to B5.4; test station S13). | 6.2 Generate and Send a Customer Statement | B | SME, Test | Closed 2026-11-22 (Q03): Maria Pabalan, round 1 (ADO 16886, 19 November 2026): monthly statements are automated (5th of the month); ad hoc statements go straight away with Print management destination, dated today; no customer is left out; delivery is confirmed from the banner and recorded as a note. The legacy batch method is removed. Failed delivery is round 2, Q04. |
| G230-13 | Confirm the invoice copy route (cross-comparison conflict 10; test station S10.1) and whether resending an invoice belongs in this topic (answers Customer Invoices VG-21). | 7.1 View and Download a Customer Invoice | B | Test, SME | Closed 2026-11-22 (legacy write-in, D-085): new 7.1.3 Resend the Invoice to the Customer from legacy 230 §6.1. The copy route of 7.1.1 (Original document) stays with the D365 test (`Customer Invoices VG-01` to `VG-05`). |
| G230-14 | Confirm the reports. Legacy 230 lists these four; the topic drafts each asked whether any reports apply. | Part 3 | B | SME | Closed 2026-11-18 (D-081, D-085): Part 3 is a quick-access summary for running the reports, so the four legacy 230 reports stand and how they are used is not described. |
| G230-15 | Confirm the label and location of the statement date field on the Statements page. Maria Pabalan, round 1 (ADO 16886, 19 November 2026): an ad hoc statement is dated today, even if the customer asks for a month-end date. | 6.2.1 step 5 | B | Test | Open |
| G230-16 | Confirm how a Collections Officer sends a change to a customer's name, address, VAT ID or country to License Management (for example an email address or a ticket). Maria Pabalan, round 1 (ADO 16886, 19 November 2026): these changes go to License Management, not into D365. | 2.7 Update Customer Details | B | SME | Closed 2026-11-22 (Daniel Moreira, D-094): specific clarification not required. The method is flexible and follows how officers already pass information to License Management; naming one channel could make another valid one look wrong. The Important box in 2.7 stays as it is. Dropped from round 2 before it was sent (Q05 is not reused). |

---

## 4. Review comments by section

Every review comment in the Word guide, in document order, after D-067 (one comment per item, open blocking items only; D-075), as of 22 November 2026 (64 comments). IDs not starting `G230` are carried from the topic drafts.

| Section | Items |
|---|---|
| Cover and version history | `G230-05` |
| Part 1 Key concepts | `Favorites VG-01`, `Personalized Views VG-01`, `Overdue Customers VG-09`, `Aged Balances VG-01` |
| Topic 1.1 Open the Customer Credit and Collections Workspace | `Workspace VG-01`, `Workspace VG-02` |
| Topic 1.2 Locate Collection Work in the Workspace | `Workspace VG-04`, `Workspace VG-05`, `Workspace VG-06`, `Workspace VG-07` |
| Topic 2.1 Review Customers Overdue | `Overdue Customers VG-01`, `Overdue Customers VG-02`, `Overdue Customers VG-05`, `Overdue Customers VG-06`, `Overdue Customers VG-04` |
| Topic 2.2 Review Customer Aged Balances | `Aged Balances VG-02`, `Aged Balances VG-04 / VG-12`, `Aged Balances VG-03 / VG-05`, `Aged Balances VG-06` |
| Topic 2.3 Filter Aged Balances by Customer or Currency | `Aged Balances VG-07`, `Aged Balances VG-08` |
| Topic 2.4 Investigate a Customer Account | `Customer Account VG-01 / VG-03`, `Customer Account VG-02`, `Customer Account VG-04`, `Customer Account VG-05`, `Customer Account VG-06`, `Customer Account VG-07`, `Customer Account VG-09`, `Customer Account VG-10`, `Customer Account VG-11`, `Customer Account VG-12` |
| Topic 2.5 Review Customer Notes | `Notes and Activities VG-01 / VG-02`, `Notes and Activities VG-03`, `Notes and Activities VG-04`, `Notes and Activities VG-06` |
| Topic 2.6 Review All Customer Activities | `Notes and Activities VG-07`, `Notes and Activities VG-08`, `Notes and Activities VG-09` |
| Topic 2.7 Update Customer Details | `G230-16` |
| Topic 4.1 Check an Overdue Balance Before Contact | `Overdue Customers VG-07` |
| Topic 5 Record a Customer Collection Activity | `Collection Activities VG-04`, `Collection Activities VG-08`, `Collection Activities VG-12`, `Collection Activities VG-13` |
| Topic 6.1 Preview and Download a Customer Statement | `Statement Preview VG-01`, `Statement Preview VG-02`, `Statement Preview VG-06`, `Statement Preview VG-07`, `Statement Preview VG-09`, `Statement Preview VG-10 / VG-12` |
| Topic 6.2 Generate and Send a Customer Statement | `Statement Distribution VG-01`, `Statement Distribution VG-02`, `G230-15`, `Statement Distribution VG-07`, `Statement Distribution VG-10` |
| Topic 7.1 View and Download a Customer Invoice | `Customer Invoices VG-01`, `Customer Invoices VG-02`, `Customer Invoices VG-03`, `Customer Invoices VG-04`, `Customer Invoices VG-05`, `Customer Invoices VG-07`, `Customer Invoices VG-08 / VG-10` |
| Topic 7.3 Change Customer Status | `G230-03` |

### 4.1 Comments removed under D-067 (17 November 2026)

The items stay open in their registers; only the Word comment is gone. Items commented in Part 1 Key concepts and again in a procedure keep the procedure comment.

| Item | Where the comment was | Why it was removed |
|---|---|---|
| `Favorites VG-18` | Part 1 Key concepts | Non-blocking: stays open in the [Favorites register](PG-AR-Configure-Collections-Favourites-Validation.md) |
| `Favorites VG-19` | Part 1 Key concepts | Non-blocking: stays open in the [Favorites register](PG-AR-Configure-Collections-Favourites-Validation.md) |
| `Workspace VG-09` | Part 1 Key concepts | Non-blocking: stays open in the [Workspace register](PG-AR-Workspace-Validation.md) |
| `Workspace VG-04 to VG-07` | Part 1 Key concepts | Duplicate: the four items have their own comments in 1.2 |
| `Workspace VG-11` | Part 1 Key concepts | Non-blocking: stays open in the [Workspace register](PG-AR-Workspace-Validation.md) |
| `Overdue Customers VG-01` | Part 1 Key concepts | Duplicate: the comment in Topic 2.1 Review Customers Overdue covers it |
| `Overdue Customers VG-02 / VG-03` | Part 1 Key concepts | Duplicate: the comment in Topic 2.1 Review Customers Overdue covers it |
| `Overdue Customers VG-04` | Part 1 Key concepts | Duplicate: the comment in Topic 2.1 Review Customers Overdue covers it |
| `Aged Balances VG-09` | Part 1 Key concepts | Non-blocking: stays open in the [Aged Balances register](PG-AR-Aged-Balances-Validation.md) |
| `Aged Balances VG-13` | Part 1 Key concepts | Non-blocking: stays open in the [Aged Balances register](PG-AR-Aged-Balances-Validation.md) |
| `Customer Account VG-06` | Part 1 Key concepts | Duplicate: the comment in Topic 2.4 Investigate a Customer Account covers it |
| `Customer Account VG-07 / VG-08` | Part 1 Key concepts | Duplicate: the comment in Topic 2.4 Investigate a Customer Account covers it |
| `Customer Account VG-12` | Part 1 Key concepts | Duplicate: the comment in Topic 2.4 Investigate a Customer Account covers it |
| `Customer Account VG-13` | Part 1 Key concepts | Non-blocking: stays open in the [Customer Account register](PG-AR-Customer-Account-Validation.md) |
| `Notes and Activities VG-01 / VG-02` | Part 1 Key concepts | Duplicate: the comment in Topic 2.5 Review Customer Notes covers it |
| `Notes and Activities VG-05 / VG-06` | Part 1 Key concepts | Duplicate: the comment in Topic 2.5 Review Customer Notes covers it |
| `Notes and Activities VG-12` | Part 1 Key concepts | Non-blocking: stays open in the [Notes and Activities register](PG-AR-Notes-and-Activities-Validation.md) |
| `Notes and Activities VG-11` | Part 1 Key concepts | Non-blocking: stays open in the [Notes and Activities register](PG-AR-Notes-and-Activities-Validation.md) |
| `Collection Activities VG-05 / VG-06` | Part 1 Key concepts | Duplicate: the comment in Topic 5 Record a Customer Collection Activity covers it |
| `Collection Activities VG-14` | Part 1 Key concepts | Non-blocking: stays open in the [Collection Activities register](PG-AR-Collection-Activities-Validation.md) |
| `Statement Preview VG-03` | Part 1 Key concepts | Duplicate: the comment in Topic 6.1 Preview and Download a Customer Statement covers it |
| `Statement Preview VG-05` | Part 1 Key concepts | Duplicate: the comment in Topic 6.1 Preview and Download a Customer Statement covers it |
| `Statement Preview VG-06` | Part 1 Key concepts | Duplicate: the comment in Topic 6.1 Preview and Download a Customer Statement covers it |
| `Statement Preview VG-05` | Part 1 Key concepts | Duplicate: the comment in Topic 6.1 Preview and Download a Customer Statement covers it |
| `Statement Preview VG-15` | Part 1 Key concepts | Non-blocking: stays open in the [Statement Preview register](PG-AR-Statement-Preview-Validation.md) |
| `Statement Distribution VG-05 / VG-06` | Part 1 Key concepts | Duplicate: the comment in Topic 6.2 Generate and Send a Customer Statement covers it |
| `Statement Distribution VG-08` | Part 1 Key concepts | Duplicate: the comment in Topic 6.2 Generate and Send a Customer Statement covers it |
| `Statement Distribution VG-09` | Part 1 Key concepts | Duplicate: the comment in Topic 6.2 Generate and Send a Customer Statement covers it |
| `Customer Invoices VG-03 / VG-04` | Part 1 Key concepts | Duplicate: the comment in Topic 7.1 View and Download a Customer Invoice covers it |
| `Customer Invoices VG-02` | Part 1 Key concepts | Duplicate: the comment in Topic 7.1 View and Download a Customer Invoice covers it |
| `Customer Invoices VG-12` | Part 1 Key concepts | Non-blocking: stays open in the [Customer Invoices register](PG-AR-Customer-Invoices-Validation.md) |
| `Workspace VG-03 / VG-10` | Topic 1.1 Open the Customer Credit and Collections Workspace | Non-blocking: stays open in the [Workspace register](PG-AR-Workspace-Validation.md) |
| `Aged Balances VG-05` | Topic 2.2 Review Customer Aged Balances | Duplicate: the comment in Topic 2.2 Review Customer Aged Balances covers it |
| `Customer Account VG-15` | Topic 2.4 Investigate a Customer Account | Non-blocking: stays open in the [Customer Account register](PG-AR-Customer-Account-Validation.md) |
| `Notes and Activities VG-13` | Topic 2.5 Review Customer Notes | Non-blocking: stays open in the [Notes and Activities register](PG-AR-Notes-and-Activities-Validation.md) |
| `Notes and Activities VG-10` | Topic 2.6 Review All Customer Activities | Non-blocking: stays open in the [Notes and Activities register](PG-AR-Notes-and-Activities-Validation.md) |
| `Statement Preview VG-08` | Topic 6.1 Preview and Download a Customer Statement | Non-blocking: stays open in the [Statement Preview register](PG-AR-Statement-Preview-Validation.md) |
| `Statement Preview VG-11` | Topic 6.1 Preview and Download a Customer Statement | Non-blocking: stays open in the [Statement Preview register](PG-AR-Statement-Preview-Validation.md) |
| `Statement Preview VG-24` | Topic 6.1 Preview and Download a Customer Statement | Non-blocking: stays open in the [Statement Preview register](PG-AR-Statement-Preview-Validation.md) |
| `Statement Distribution VG-11` | Topic 6.2 Generate and Send a Customer Statement | Non-blocking: stays open in the [Statement Distribution register](PG-AR-Statement-Distribution-Validation.md) |
| `Customer Invoices VG-06` | Topic 7.1 View and Download a Customer Invoice | Non-blocking: stays open in the [Customer Invoices register](PG-AR-Customer-Invoices-Validation.md) |
| `Customer Invoices VG-09` | Topic 7.1 View and Download a Customer Invoice | Non-blocking: stays open in the [Customer Invoices register](PG-AR-Customer-Invoices-Validation.md) |
| `Customer Invoices VG-21` | Topic 7.1 View and Download a Customer Invoice | Non-blocking: stays open in the [Customer Invoices register](PG-AR-Customer-Invoices-Validation.md) |

---

## 5. Draft items not carried as comments

Review comments in the nine topic drafts that are not review comments in this guide, and where each one is answered. Draft register items that were never Word comments (tests, recording checks, approval) stay open in the draft registers.

| Draft | Item | Disposition |
|---|---|---|
| Workspace | `VG-17`: Destination guide and topic (D-045). Proposed: 230 Collections, topic 1 Start the Collections Day. Merged into the 230 v3.0 working draft (D-052). | Guide-level: `G230-05` |
| Workspace | `VG-16`: Confirm the business process owner (BPO) for this guide. | Guide-level: `G230-05` |
| Workspace | `VG-15`: Confirm the stream name, process area and business role name. These match the other AR Collections guides, where the same question is open. | Guide-level: `G230-07` |
| Workspace | `VG-18`: Confirm whether any reports or inquiries apply to this process. If none apply, this section will read "No applicable reports". | Guide-level: `G230-14` |
| Overdue Customers | `VG-17`: Destination guide and topic (D-045). Proposed: 230 Collections, topics 2.1 Review Customers Overdue and 4.1 Check an Overdue Balance Before Contact. Merged into the 230 v3.0 working draft (D-052). | Guide-level: `G230-05` |
| Overdue Customers | `VG-16`: Confirm the business process owner (BPO) for this guide. | Guide-level: `G230-05` |
| Overdue Customers | `VG-15`: Confirm the stream name, process area and business role name. These match the other AR Collections guides, where the same question is open. | Guide-level: `G230-07` |
| Overdue Customers | `VG-18`: Confirm whether any reports or inquiries apply to this process. If none apply, this section will read "No applicable reports". | Guide-level: `G230-14` |
| Aged Balances | `VG-17`: Destination guide and topic (D-045). Proposed: 230 Collections, topics 2.2 Review Customer Aged Balances, merged with legacy topic 2.1, and 2.3 Filter Aged Balances by Customer or Currency. Merged into the 230 v3.0 working draft (D-052). | Guide-level: `G230-05` |
| Aged Balances | `VG-16`: Confirm the business process owner (BPO) for this guide. | Guide-level: `G230-05` |
| Aged Balances | `VG-15`: Confirm the stream name, process area and business role name. These match the other AR Collections guides, where the same question is open. | Guide-level: `G230-07` |
| Aged Balances | `VG-18`: Confirm whether any reports or inquiries apply to this process. If none apply, this section will read "No applicable reports". | Guide-level: `G230-14` |
| Customer Account | `VG-19`: Destination guide and topic (D-045). Proposed: 230 Collections, topic 2.4 Investigate a Customer Account, with its three subtopics kept together (2.4.1 to 2.4.3). Merged into the 230 v3.0 working draft (D-052). | Guide-level: `G230-05` |
| Customer Account | `VG-18`: Confirm the business process owner (BPO) for this guide. | Guide-level: `G230-05` |
| Customer Account | `VG-16`: Confirm the events that start this task. Source 1 supports investigating account history before contacting a customer. | Guide-level: `G230-06` |
| Customer Account | `VG-17`: Confirm the stream name, process area and business role name. These match the other AR Collections guides, where the same question is open. | Guide-level: `G230-07` |
| Customer Account | `VG-20`: Confirm whether any reports or inquiries apply to this process. If none apply, this section will read "No applicable reports". The custom all-customer transaction report is a separate guide (VG-24). | Guide-level: `G230-14` |
| Notes and Activities | `VG-17`: Destination guide and topic (D-045). Proposed: 230 Collections, topics 2.5 Review Customer Notes and 2.6 Review All Customer Activities, merged with legacy topic 2.2. Merged into the 230 v3.0 working draft (D-052). | Guide-level: `G230-05` |
| Notes and Activities | `VG-16`: Confirm the business process owner (BPO) for this guide. | Guide-level: `G230-05` |
| Notes and Activities | `VG-15`: Confirm the stream name, process area and business role name. These match the other AR Collections guides, where the same question is open. | Guide-level: `G230-07` |
| Notes and Activities | `VG-18`: Confirm whether any reports or inquiries apply to this process. If none apply, this section will read "No applicable reports". | Guide-level: `G230-14` |
| Collection Activities | `VG-19`: Destination guide and topic (D-045). Proposed: 230 Collections, topic 5 Record a Customer Collection Activity, merged with legacy topic 5. Merged into the 230 v3.0 working draft (D-052). | Guide-level: `G230-05` |
| Collection Activities | `VG-18`: Confirm the business process owner (BPO) for this guide. | Guide-level: `G230-05` |
| Collection Activities | `VG-16`: Confirm the events that start this task, for example after each email or telephone contact. Source 2 supports recording email or phone contact at customer level. | Guide-level: `G230-06` |
| Collection Activities | `VG-17`: Confirm the stream name, process area and business role name. These match the other AR Collections guides, where the same question is open. | Guide-level: `G230-07` |
| Collection Activities | `VG-20`: Confirm whether any reports or inquiries apply to this process. If none apply, this section will read "No applicable reports". | Guide-level: `G230-14` |
| Statement Preview | `VG-19`: Destination guide and topic (D-045). Proposed: 230 Collections, topic 6.1 Preview and Download a Customer Statement. Preview and send stay separate subtopics of topic 6. Merged into the 230 v3.0 working draft (D-052). | Guide-level: `G230-05` |
| Statement Preview | `VG-18`: Confirm the business process owner (BPO) for this guide. | Guide-level: `G230-05` |
| Statement Preview | `VG-16`: Confirm the events that start this task. Source 1 lists previewing rather than sending a statement as a ready PG section. | Guide-level: `G230-06` |
| Statement Preview | `VG-17`: Confirm the stream name, process area and business role name. These match the other AR Collections guides, where the same question is open. | Guide-level: `G230-07` |
| Statement Preview | `VG-20`: Confirm whether any reports or inquiries apply to this process. If none apply, this section will read "No applicable reports". | Guide-level: `G230-14` |
| Statement Distribution | `VG-21`: Destination guide and topic (D-045). Proposed: 230 Collections, topic 6.2 Generate and Send a Customer Statement, merged with legacy topic 1. Merged into the 230 v3.0 working draft (D-052). | Guide-level: `G230-05` |
| Statement Distribution | `VG-20`: Confirm the business process owner (BPO) for this guide. | Guide-level: `G230-05` |
| Statement Distribution | `VG-18`: Confirm the events that start this task, for example a statement cycle or a customer request. Source 1 supports generating statements through the correct distribution method. | Guide-level: `G230-06` |
| Statement Distribution | `VG-19`: Confirm the stream name, process area and business role name. These match the other AR Collections guides, where the same question is open. | Guide-level: `G230-07` |
| Statement Distribution | `VG-22`: Confirm whether any reports or inquiries apply to this process. If none apply, this section will read "No applicable reports". | Guide-level: `G230-14` |
| Customer Invoices | `VG-16`: Destination guide and topic (D-045). Proposed: 230 Collections, topic 7.1 View and Download a Customer Invoice, merged with legacy topic 6.1. Merged into the 230 v3.0 working draft (D-052). | Guide-level: `G230-05` |
| Customer Invoices | `VG-15`: Confirm the business process owner (BPO) for this guide. | Guide-level: `G230-05` |
| Customer Invoices | `VG-13`: Confirm the events that start this task. The source material supports retrieving invoices for customers and reviewing documents before collection contact. | Guide-level: `G230-06` |
| Customer Invoices | `VG-14`: Confirm the stream name, process area and business role name. These match the other AR Collections guides, where the same question is open. | Guide-level: `G230-07` |
| Customer Invoices | `VG-17`: Confirm whether any reports or inquiries apply to this process. If none apply, this section will read "No applicable reports". | Guide-level: `G230-14` |

---

## 6. Round 1 plan (D-085)

Round 1 asks Maria Pabalan only what the sources cannot answer and what changes what a Collections Officer does: three questions, with the topic and step to look at. Every other item from the earlier round has a route that does not need her. The board holds the question text.

### 6.1 Asked in round 1

| Question | Items | Where |
|---|---|---|
| Q01 Update Customer Details | `G230-10` | Topic 2.7 |
| Q02 Recording a collection activity | `G230-11`, `Collection Activities VG-05`, `Collection Activities VG-09`, `Collection Activities VG-10` | Topic 5 steps 6 and 8; Part 1 *Collection activities* |
| Q03 Sending a statement | `G230-12`, `Statement Distribution VG-17`, `Statement Distribution VG-05`, `Statement Preview VG-05`, `Statement Distribution VG-12`, `Statement Distribution VG-09`, `Statement Distribution VG-10` | Part 1 *Before sending*; 6.2.1 steps 4 to 6; 6.2.2 steps 2 and 3 |

### 6.2 Not asked

| Route | Items | What happens |
|---|---|---|
| Answered by a source: closed | `G230-06`, `Workspace VG-14`, `Aged Balances VG-14`, `Notes and Activities VG-14`, `Overdue Customers VG-14`, `G230-07`, `G230-14`, `Statement Distribution VG-03`, `Statement Distribution VG-04`, `Statement Preview VG-03`, `Statement Preview VG-04` | Start events from legacy 230 Part 1 and the training; stream and process area as shown (O2C, Collections); Part 3 under D-081; **Only open** and **Include company logo** set to Yes, from legacy 230 §1 step 4. Their review comments are removed. |
| Asked in another guide's round | `Overdue Customers VG-09` (220 round 1 Q04, the write-off limit); `Personalized Views VG-01` (260 round 1 Q05, the training page; the recommended columns come from legacy 230 §6.3: **Account status** and **Account status reason**) | One question covers both guides (D-069). |
| Write in from legacy 230 while drafting | `G230-08` (sort by amount due, the aging icon legend, the 10-minute refresh), `G230-09` (whether reviewing attachments belongs in 2.6), `G230-13` (resending an invoice: legacy 230 §6.1), `Statement Distribution VG-06` (recipients are contacts with Purpose = Business), `Overdue Customers VG-08`, `Overdue Customers VG-10` (the legacy Collections workflow: check, contact and record, escalate to the Group Billing and Credit Manager, raise a write-off request), `Workspace VG-08` (describe the sections the procedures use) | Drafting changes, made without the SME. Done 2026-11-22 in v3.1 (section 6.3): all seven closed. |
| Check in D365 (clean-session test) | 64 items: the screen labels and navigation of topics 1, 2, 5, 6 and 7, plus `G230-03` (the 7.3 exclusion steps and whether the checkbox saves on its own), `Customer Account VG-12`, `Overdue Customers VG-04` and `Notes and Activities VG-06` | The [clean-session test](Clean-Session-Test-Plan.md) confirms them. |
| Sign-off | `G230-05` | BPO sign-off of v3.0. |

### 6.3 Round 1 answers (Maria Pabalan, ADO Task 16886, 19 November 2026)

Maria answered all three questions and assigned the ticket back. The answers are applied to the Word guide, which becomes v3.1 (D-093, D-092), together with the legacy write-ins in section 6.2.

| Question | Answer | Applied in v3.1 | Items |
|---|---|---|---|
| Q01 Update Customer Details | Replace the 230 steps with a link to 200 Customer Onboarding and Maintenance §3.4, so there is one source of truth. Keep a short line on when Collections Officers update customer details, for example a new AP contact or statement email from the customer. Any change to a customer's name, address, VAT ID or country goes to License Management; Collections Officers don't make those changes in D365. | 2.7 now has a Description with the pointer and the line, and an Important box with the License Management rule; the 18-step legacy procedure is removed. Topic 2 overview updated. | `G230-10` closed; `G230-16` opened and then closed (D-094: no channel named) |
| Q02 Recording a collection activity | Follow the legacy 230 method: an activity on the Collections page with Type set to the interaction (Email, Phone call), plus Purpose and Notes. One note per interaction, written as the record of what happened, with separate notes for incoming and outgoing. Purpose: a short title, for example "Email from customer – statement request", "Reply to customer – invoice copy sent", "Overdue chaser – payment requested". Notes must include who (address or name) and the date, the invoices discussed with amount and currency, any promised payment date or dispute, what was sent or agreed, any follow-up action and the officer's initials. Internal emails (for example to Receipting or Support) also get a note, on every account involved. Never record card numbers, bank account or BSB numbers or other payment credentials, and no personal opinions. Remove the legacy "attaching supporting documents is mandatory" step: documents are not attached in D365 but kept in CW1, and the note must stand on its own. | Topic 5 rewritten on the Collections page (Aged balances > customer name > new activity; activity type, Purpose, Priority, Type, Notes); Key concepts *Collection activities* updated and *Writing a collection note* added (with an Important box for what never to record); attachment requirements removed from Part 1, 2.6 and topic 8. | `G230-11`, `Collection Activities VG-02`, `VG-03`, `VG-05`, `VG-06`, `VG-07`, `VG-09`, `VG-10` closed; `G230-09` closed with the write-in |
| Q03 Sending a statement | Monthly statements are automated (5th of each month; 16984), so remove the legacy batch method. An ad hoc statement requested by a customer is sent straight away with Print management destination, as in the training recording, dated today even if the customer asks for a month-end date. No customers are left out (DD and card customers, customers in dispute, multi-currency customers; CR 15801 splits statements by currency, in PROD). After sending, D365 shows a banner at the top of the page confirming the statement was sent and who it went to; the officer checks it, then records a note on the customer's Collections page: "Statement dated <date> sent to <email>". | Part 1, topic 6 and 6.2 descriptions; Key concepts *Statement distribution* (delivery banner, monthly statements) and *Before sending* (every customer who asks; the 6.2.1 options and today's date); 6.1.1 step 6 (what happens if the destination stays set); 6.2.1 (date step, recipients); 6.2.2 (banner, note, failed delivery); the legacy batch note and the mailbox step are removed. | `G230-12`, `Statement Distribution VG-05`, `VG-08`, `VG-09`, `VG-12`, `VG-13`, `VG-17`, `Statement Preview VG-05`, `VG-13` closed; `Statement Distribution VG-06` closed with the write-in; `G230-15` opened (D365 test of the date field); `Statement Distribution VG-10` asked in round 2 (Q04) |

Two interpretations to note. The note recorded after sending a statement is entered as a collection activity (topic 5), since sending the statement is an outgoing email and Maria's Q02 answer records each email as an activity with a note. The Collections sent mailbox check is dropped, since Maria's answer on confirming delivery is the banner and the note.

Maria's 220 answers (D-091) also apply here: payment corrections are Receipting Officer work, so 230's Collections workflow, *Customer Payment Management*, Part 1 and the topic 7 note now say to ask the Receipting team.

---

## 7. Round 2 plan (D-085)

Round 2 goes to Maria Pabalan with v3.1 and asks only what her round 1 answers left open: one question. Q05 (how to send a change to License Management) was dropped before sending: the guide does not name a channel (D-094). Pages come from Word's Contents, updated by Daniel in the v3.1 review copy on 22 November (D-089), less one page since the version history table was shortened (D-095); step pages keep their place within each subtopic. The board holds the question text.

### 7.1 Asked in round 2

| Question | Items | Where |
|---|---|---|
| Q04 Failed statement delivery (follows Q03) | `Statement Distribution VG-10` | 6.2.2 step 3 (p. 46) |

### 7.2 Not asked

| Route | Items | What happens |
|---|---|---|
| Check in D365 (clean-session test) | `G230-15` (the statement date field), `G230-03`, `Collection Activities VG-04`, `VG-08`, `VG-12`, `VG-13`, and the other screen-label items in section 4 | The [clean-session test](Clean-Session-Test-Plan.md) confirms them. |
| Asked in another guide's round | `Overdue Customers VG-09` (the write-off limit: 220 round 1 Q04 answered that limits wait for CR 16959), `Personalized Views VG-01` (260 round 1 Q05) | One question covers both guides (D-069). |
| Not needed | `G230-16` (how to send a change to License Management) | Closed by Daniel Moreira (D-094): the method is flexible and follows current practice, so the guide does not name one. |
| Sign-off | `G230-05` | BPO sign-off. |

---

## 8. Change log

| Date | Change |
|---|---|
| 2026-11-03 | Register created with the v3.0 working draft, assembled from v2.4 and the nine topic drafts (D-052, ADO Task 16886). |
| 2026-11-08 | Guide added to the SME review pack for review only (D-052 amendment). |
| 2026-11-09 | Topic 2.8 now links to 240 Direct Debit and Credit Card Payments, topic 1, instead of repeating the steps (D-053). `G230-04` closed: decided at the 9 November meeting. |
| 2026-11-10 | References to 221 Customer Payment Corrections now point to 220 Customer Payments v3.0 (topics 2.3, 3.1, 3.3 and 3.6), which absorbed 221 (D-055). |
| 2026-11-16 | Formatting brought in line with D-059 to D-061 (D-063): Bullet 1.2 bullets (nested items keep their level), topic numbers in link text, the five *Legacy 230* comparison notes and three phrases in the ACTION: REVIEW REQUIREMENT style, four bold pseudo-headings in Key concepts made Heading 5, eight one-row concept tables made paragraphs, and the *Customer Payment Management* column header corrected from Timing to Description. Files renamed with the `CLAUDE-` prefix (D-056). The SME review copy of 8 November is the earlier file: merge any comments from it into this one. |
| 2026-11-17 | Review comments cut under D-067 (D-075): 136 → 93, one per open blocking item at the place it matters most; the 43 removed are listed in section 4.1 and their items stay open in their registers. First question round drafted on the board (D-069), on hold until the SME review of the 8 November pack comes back. The PDF beside the Word file is out of date (D-064). |
| 2026-11-18 | Favorites reminders removed from three navigation steps and one step description (D-084): 260 O2C Getting Started covers Favorites. The Part 1 list of pages to add to Favorites stays. The PDF beside the Word file is out of date (D-064). |
| 2026-11-18 | Round 1 rebuilt under D-085 as three questions (section 6): 12 items asked; `G230-06`, `G230-07`, `G230-14` and eight topic-draft items closed from the sources; two items covered by the 220 and 260 rounds; seven go to drafting and 64 to the D365 test. Review comments 93 → 82; comments for asked items carry the question number. |
| 2026-11-18 | Page breaks (D-086): topics 2, 3, 5, 6 and 7 and the Part 2 heading now start on a new page; the Contents page numbers are refreshed. No item changes. |
| 2026-11-18 | Page breaks (D-087): ten subtopics now start on a new page; the Contents page numbers are refreshed. No item changes. |
| 2026-11-18 | Round 1 (three questions, section 6) sent to Maria Pabalan in ADO 16886 by Daniel Moreira, with the review copy. Its pages came from the review copy's layout (D-088); Word's Contents may put the later topics one page further on (D-089). |
| 2026-11-18 | Round 1 page references corrected from Word's Contents (D-089): Q01 p. 30-32, Q02 p. 13, 40, Q03 p. 14, 47-48. From topic 2.4 on, Word lays the guide out one page earlier than the LibreOffice layout (topic 2.3 is one page in Word). The Contents now carries Word's numbers. |
| 2026-11-22 | Round 1 answered by Maria Pabalan (ADO 16886, 19 November) and applied, with the seven legacy write-ins (section 6.3, D-093); the guide becomes **v3.1** (D-092): file renamed `CLAUDE-230-Collections PG v3.1.docx`, a 3.1 row in its version history, and a *Versions of the guide* section here. 26 items closed (`G230-08` to `G230-13` and 20 topic-draft items) and two opened (`G230-15`, `G230-16`); review comments 82 → 64. Payment corrections now go to the Receipting team (D-091). Round 2 (two questions, section 7) drafted on the board. Contents page numbers refreshed. The PDF beside the Word file is out of date (D-064). |
| 2026-11-22 | Word's Contents for v3.1 (Daniel Moreira, 22 November) written into the guide, with the 7.1.3 line Word added: Word is one page earlier than the layout from 2.4 on, as in round 1. Round 2 pages from Word: Q04 p. 47, Q05 p. 31. Round 2 is ready to send. |
| 2026-11-22 | `G230-16` closed by Daniel Moreira (D-094): specific clarification is not required, because officers pass changes to License Management through the channels they already use, and naming one could make another look wrong. Its review comment and the [Q05] tag are removed; the Important box in 2.7 stays as it is. Round 2 is now one question (Q04). Review comments 64 → 63. |
| 2026-11-22 | Version history (D-095): rows 3.0 and 3.1 list Maria Pabalan, then Daniel Moreira, as authors, and rows 2.4, 3.0 and 3.1 have descriptions of a few words. The table no longer runs onto a second page, so every heading is one page earlier: the Contents carries Word's numbers less one, and round 2 Q04 is p. 46. |
