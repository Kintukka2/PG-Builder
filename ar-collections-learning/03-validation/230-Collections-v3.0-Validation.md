# Validation Register: 230 Collections v3.0 (working draft)

| Field | Value |
|---|---|
| Guide (editable source) | [`230-Collections PG v3.0.docx`](../01-procedure-guides/230-Collections%20PG%20v3.0.docx) |
| Markdown preview | [`PG-230-Collections-v3.0-DRAFT.md`](../01-procedure-guides/PG-230-Collections-v3.0-DRAFT.md) |
| Status | Working draft v3.0 (D-052; ADO Task 16886). Internal to the project team until it is reviewed with Maria Pabalan; needs BPO sign-off. Version 2.3, then 2.4, stays published until 3.0 passes its gates. |
| Last updated | 2026-11-03 |
| Items | 10 guide-level items (`G230`), all open: 10 blocking, 0 non-blocking. 127 carried review comments from the topic drafts. |

This file is the guide's **question log** (D-016). It holds the guide-level items, which are scoped to this guide and never renumbered. Review comments carried from the topic drafts keep their ID and draft name, for example *Aged Balances VG-03*, and their source register stays the record for them: an answer recorded there applies here (D-048). Each open item that affects the text is a Word review comment by "Validation register" (VR).

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
| V2 | Where a topic draft and a legacy section cover the same task (2.2, 2.6, 5, 6.2 and 7.1), the draft's procedure is the topic and the legacy-only content is a note with a `G230` item. No legacy steps are mixed into draft procedures. | The recording governs (D-044); every legacy-only fact still needs confirming. |
| V3 | Legacy topics keep their procedures, screenshots and numbering unchanged, under template headings with automatic numbers. | D-052: rebuilt in the master template; content changes wait for the SME and the test. |
| V4 | Legacy 2.3 Update Customer Details stays as topic 2.7 until the BPO decides whether to link to 200 §3.4 instead (`G230-10`). | D-052 decision 4. |
| V5 | Legacy 2.4 Direct Debit stays as topic 2.8 until 240 Direct Debit is published. | D-049, D-051. |
| V6 | Carried review comments keep their draft name and ID, for example *Aged Balances VG-03*. | Suite plan section 1. |

---

## 3. Guide-level items (`G230`)

**Priority:** **B** = blocks publication. **N** = non-blocking. **Method:** **Test** = D365 test in a clean session. **Rec** = recording or transcript review. **SME** = subject-matter expert or process owner. **Dec** = project decision.

| ID | Item to confirm | Location | Priority | Method | Status |
|---|---|---|---|---|---|
| G230-05 | Version 3.0 is a working draft for ADO Task 16886, assembled from v2.4 and the nine AR Collections topic drafts (D-052). It stays inside the project team until it is reviewed with Maria Pabalan, and it needs BPO sign-off. Version 2.3, then 2.4, stays the published guide until 3.0 passes its gates. | Version history | B | SME | Open |
| G230-06 | Confirm the events that start the Collections process. These come from legacy 230; the topic drafts add the start of each working day (Workspace) and customer requests for statements and invoices. | Part 1 High-level process | B | SME | Open |
| G230-07 | Confirm the stream and process area. Legacy 230 uses O2C and Collections; the topic drafts use Accounts Receivable and AR Collections (cross-comparison conflict 11; SME question A2). | Part 1 Stream | B | SME | Open |
| G230-08 | Confirm which legacy Aged balances content belongs in this topic: sorting by amount due, the aging icon legend, opening the customer's Collections page (cross-comparison conflict 12) and the 10-minute refresh (legacy control 9). | 2.2 Review Customer Aged Balances | B | SME, Test | Open |
| G230-09 | Confirm the activity control label (cross-comparison conflict 2) and whether reviewing attachments and correcting the record belong in this topic. | 2.6 Review All Customer Activities | B | SME, Test | Open |
| G230-10 | Decide whether to keep this topic or replace it with a link to 200 Customer Onboarding and Maintenance §3.4, which covers the same task. | 2.7 Update Customer Details | B | Dec | Open |
| G230-11 | Confirm the activity fields and types, and whether supporting documents are mandatory (cross-comparison conflicts 2 and 3; legacy control 7; SME question B3.1). | 5 Record a Customer Collection Activity | B | SME, Test | Open |
| G230-12 | Confirm these statement controls before anyone sends a statement with this topic (legacy controls 1 to 4; cross-comparison conflicts 4 and 5; SME questions B5.1 to B5.4; test station S13). | 6.2 Generate and Send a Customer Statement | B | SME, Test | Open |
| G230-13 | Confirm the invoice copy route (cross-comparison conflict 10; test station S10.1) and whether resending an invoice belongs in this topic (answers Customer Invoices VG-21). | 7.1 View and Download a Customer Invoice | B | Test, SME | Open |
| G230-14 | Confirm the reports. Legacy 230 lists these four; the topic drafts each asked whether any reports apply. | Part 3 | B | SME | Open |

---

## 4. Carried review comments by section

Every review comment in the Word guide, in document order. IDs not starting `G230` are carried from the topic drafts.

| Section | Items |
|---|---|
| Cover and version history | `G230-05` |
| Part 1 High-level process | `G230-06`, `G230-07` |
| Part 1 Key concepts | `Favorites VG-01`, `Favorites VG-18`, `Favorites VG-19`, `Personalized Views VG-01`, `Workspace VG-09`, `Workspace VG-04 to VG-07`, `Workspace VG-08`, `Workspace VG-11`, `Overdue Customers VG-01`, `Overdue Customers VG-02 / VG-03`, `Overdue Customers VG-04`, `Overdue Customers VG-09`, `Aged Balances VG-01`, `Aged Balances VG-09`, `Aged Balances VG-13`, `Customer Account VG-06`, `Customer Account VG-07 / VG-08`, `Customer Account VG-12`, `Customer Account VG-13`, `Notes and Activities VG-01 / VG-02`, `Notes and Activities VG-05 / VG-06`, `Notes and Activities VG-12`, `Notes and Activities VG-11`, `Collection Activities VG-05 / VG-06`, `Collection Activities VG-09 / VG-10`, `Collection Activities VG-14`, `Statement Preview VG-03`, `Statement Preview VG-05`, `Statement Preview VG-06`, `Statement Preview VG-05`, `Statement Preview VG-15`, `Statement Distribution VG-05 / VG-06`, `Statement Distribution VG-08`, `Statement Distribution VG-09`, `Statement Distribution VG-12 / VG-13`, `Statement Distribution VG-17`, `Customer Invoices VG-03 / VG-04`, `Customer Invoices VG-02`, `Customer Invoices VG-12` |
| Topic 1.1 Open the Customer Credit and Collections Workspace | `Workspace VG-01`, `Workspace VG-02`, `Workspace VG-03 / VG-10` |
| Topic 1.2 Locate Collection Work in the Workspace | `Workspace VG-14`, `Workspace VG-04`, `Workspace VG-05`, `Workspace VG-06`, `Workspace VG-07` |
| Topic 2.1 Review Customers Overdue | `Overdue Customers VG-01`, `Overdue Customers VG-02`, `Overdue Customers VG-05`, `Overdue Customers VG-06`, `Overdue Customers VG-04` |
| Topic 2.2 Review Customer Aged Balances | `Aged Balances VG-02`, `Aged Balances VG-04 / VG-12`, `Aged Balances VG-03 / VG-05`, `Aged Balances VG-05`, `Aged Balances VG-06`, `G230-08` |
| Topic 2.3 Filter Aged Balances by Customer or Currency | `Aged Balances VG-14`, `Aged Balances VG-07`, `Aged Balances VG-08` |
| Topic 2.4 Investigate a Customer Account | `Customer Account VG-01 / VG-03`, `Customer Account VG-02`, `Customer Account VG-04`, `Customer Account VG-05`, `Customer Account VG-06`, `Customer Account VG-07`, `Customer Account VG-09`, `Customer Account VG-15`, `Customer Account VG-10`, `Customer Account VG-11`, `Customer Account VG-12` |
| Topic 2.5 Review Customer Notes | `Notes and Activities VG-01 / VG-02`, `Notes and Activities VG-03`, `Notes and Activities VG-04`, `Notes and Activities VG-06`, `Notes and Activities VG-13` |
| Topic 2.6 Review All Customer Activities | `Notes and Activities VG-14`, `Notes and Activities VG-07`, `Notes and Activities VG-08`, `Notes and Activities VG-09`, `Notes and Activities VG-10`, `G230-09` |
| Topic 2.7 Update Customer Details | `G230-10` |
| Topic 2.8 Maintain Customer Direct Debit & eBanking Details | `G230-04` |
| Topic 4.1 Check an Overdue Balance Before Contact | `Overdue Customers VG-14`, `Overdue Customers VG-07`, `Overdue Customers VG-08`, `Overdue Customers VG-10` |
| Topic 5 Record a Customer Collection Activity | `Collection Activities VG-01 / VG-03`, `Collection Activities VG-02`, `Collection Activities VG-04`, `Collection Activities VG-05`, `Collection Activities VG-07`, `Collection Activities VG-08 / VG-09`, `Collection Activities VG-12`, `Collection Activities VG-13`, `G230-11` |
| Topic 6.1 Preview and Download a Customer Statement | `Statement Preview VG-01`, `Statement Preview VG-02`, `Statement Preview VG-03`, `Statement Preview VG-04`, `Statement Preview VG-05`, `Statement Preview VG-06`, `Statement Preview VG-07`, `Statement Preview VG-08`, `Statement Preview VG-09`, `Statement Preview VG-10 / VG-12`, `Statement Preview VG-11`, `Statement Preview VG-24` |
| Topic 6.2 Generate and Send a Customer Statement | `Statement Distribution VG-01`, `Statement Distribution VG-02`, `Statement Distribution VG-03`, `Statement Distribution VG-04`, `Statement Distribution VG-05 / VG-06`, `Statement Distribution VG-07`, `Statement Distribution VG-08`, `Statement Distribution VG-09`, `Statement Distribution VG-10`, `Statement Distribution VG-11`, `G230-12` |
| Topic 7.1 View and Download a Customer Invoice | `Customer Invoices VG-01`, `Customer Invoices VG-02`, `Customer Invoices VG-03`, `Customer Invoices VG-04`, `Customer Invoices VG-05`, `Customer Invoices VG-06`, `Customer Invoices VG-07`, `Customer Invoices VG-08 / VG-10`, `Customer Invoices VG-09`, `Customer Invoices VG-21`, `G230-13` |
| Topic 7.3 Change Customer Status | `G230-03` |
| Part 3: Reports | `G230-14` |

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

## 6. Change log

| Date | Change |
|---|---|
| 2026-11-03 | Register created with the v3.0 working draft, assembled from v2.4 and the nine topic drafts (D-052, ADO Task 16886). |
