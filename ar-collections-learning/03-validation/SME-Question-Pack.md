# SME Question Pack: AR Collections Guides

| Field | Value |
|---|---|
| Covers | 191 open validation items across the 13 AR Collections validation registers (119 blocking) that need an SME answer, a recording or a project decision |
| Questions | 31, grouped so each rule is answered once and applied to every guide that uses it |
| Response sheet | [`SME-Question-Pack-Responses.xlsx`](SME-Question-Pack-Responses.xlsx): one row per answer, plus an index of every item |
| Companion | The [clean-session test plan](Clean-Session-Test-Plan.md) covers the items that a D365 test can answer. 31 items here also have a test part; the test confirms the label, and this pack confirms the intended behavior or rule. |
| Status | Draft for SME review. No answers yet. |
| Last updated | 2026-10-15 |

## How to answer

- Answer in the response sheet or directly in this document, quoting the question ID (for example **B5.1**).
- "Don't know" or "Ask someone else" is a useful answer: name who to ask.
- Where a document exists, attach it rather than summarising it (for example the legal entity code reference or a note standard).
- Nothing here is final until answered. The guides show these items as review comments, and nothing is invented to fill them.

## Answer these first

| Priority | Questions | Why |
|---|---|---|
| 1 | **A1 to A6** | 78 items, all blocking, repeated across every guide. |
| 2 | **B5.1 to B5.4** | Statement controls. They gate test station S13 and decide whether the statement guides are safe to use. |
| 3 | **B7** | The legal entity code reference, which every guide's *Check the Entity* step depends on. |
| 4 | **B3.1 to B3.3** and **B4.1 to B4.3** | The collection-note standard and the overdue-account rules. |
| 5 | **D1** and **D2** | Guide codes and scope boundaries. The project team decides these with the BPO. |

---

## Part A: Governance (the BPO or SME lead)

Shared across all 13 guides. Answer once per guide where a table is given.

### A1 Initiation

What events start this task? Confirm or correct the draft wording.

| ID | Guide | Item | Current draft | Answer |
|---|---|---|---|---|
| A1.FAV | Favorites | VG-30 (B) | A new AR Collections user is setting up D365 before starting routine AR Collections work. | |
| A1.VIEW | Personalized Views | VG-21 (B) | A page does not show the information needed for collection work, such as due dates, currencies or overdue balances. | |
| A1.AGED | Aged Balances | VG-14 (B) | A Collections Officer needs to identify customers with outstanding balances before starting collection work. | |
| A1.INV | Customer Invoices | VG-13 (B) | A customer or colleague needs a copy of an invoice, or the invoice must be reviewed before contacting the customer. | |
| A1.EXP | Export to Excel | VG-12 (B) | A Collections Officer needs D365 grid data in Excel for internal analysis. | |
| A1.NOTE | Notes and Activities | VG-14 (B) | A Collections Officer needs to review previous collection notes and contact with a customer before contacting them. | |
| A1.LE | Legal Entities | VG-14 (B) | A Collections Officer needs to work in a legal entity other than the one that is active. | |
| A1.WS | Workspace | VG-14 (B) | A Collections Officer starts their collection work for the day. | |
| A1.OD | Overdue Customers | VG-14 (B) | A Collections Officer needs to identify which customers to contact about overdue balances. | |
| A1.ACCT | Customer Account | VG-16 (B) | A Collections Officer needs to understand a customer's account before contacting them. | |
| A1.ACT | Collection Activities | VG-16 (B) | A Collections Officer has contacted a customer, or been contacted by them, about their account. | |
| A1.SP | Statement Preview | VG-16 (B) | A Collections Officer needs to review a customer statement, or needs a copy of it, without sending it to the customer. | |
| A1.SD | Statement Distribution | VG-18 (B) | A customer statement must be sent to the customer. | |

### A2 Stream, process area and role

Confirm the Stream, Process Area and business role name.

| ID | Guide | Item | Current draft | Answer |
|---|---|---|---|---|
| A2.FAV | Favorites | VG-31 (B) | Accounts Receivable · AR Collections · Collections Officer | |
| A2.VIEW | Personalized Views | VG-22 (B) | Accounts Receivable · AR Collections · Collections Officer | |
| A2.AGED | Aged Balances | VG-15 (B) | Accounts Receivable · AR Collections · Collections Officer | |
| A2.INV | Customer Invoices | VG-14 (B) | Accounts Receivable · AR Collections · Collections Officer | |
| A2.EXP | Export to Excel | VG-13 (B) | Accounts Receivable · AR Collections · Collections Officer | |
| A2.NOTE | Notes and Activities | VG-15 (B) | Accounts Receivable · AR Collections · Collections Officer | |
| A2.LE | Legal Entities | VG-15 (B) | Accounts Receivable · AR Collections · Collections Officer | |
| A2.WS | Workspace | VG-15 (B) | Accounts Receivable · AR Collections · Collections Officer | |
| A2.OD | Overdue Customers | VG-15 (B) | Accounts Receivable · AR Collections · Collections Officer | |
| A2.ACCT | Customer Account | VG-17 (B) | Accounts Receivable · AR Collections · Collections Officer | |
| A2.ACT | Collection Activities | VG-17 (B) | Accounts Receivable · AR Collections · Collections Officer | |
| A2.SP | Statement Preview | VG-17 (B) | Accounts Receivable · AR Collections · Collections Officer | |
| A2.SD | Statement Distribution | VG-19 (B) | Accounts Receivable · AR Collections · Collections Officer | |

### A3 Business process owner

Who is the business process owner (BPO) for this guide?

| ID | Guide | Item | Current draft | Answer |
|---|---|---|---|---|
| A3.FAV | Favorites | VG-33 (B) | To be confirmed | |
| A3.VIEW | Personalized Views | VG-23 (B) | To be confirmed | |
| A3.AGED | Aged Balances | VG-16 (B) | To be confirmed | |
| A3.INV | Customer Invoices | VG-15 (B) | To be confirmed | |
| A3.EXP | Export to Excel | VG-14 (B) | To be confirmed | |
| A3.NOTE | Notes and Activities | VG-16 (B) | To be confirmed | |
| A3.LE | Legal Entities | VG-16 (B) | To be confirmed | |
| A3.WS | Workspace | VG-16 (B) | To be confirmed | |
| A3.OD | Overdue Customers | VG-16 (B) | To be confirmed | |
| A3.ACCT | Customer Account | VG-18 (B) | To be confirmed | |
| A3.ACT | Collection Activities | VG-18 (B) | To be confirmed | |
| A3.SP | Statement Preview | VG-18 (B) | To be confirmed | |
| A3.SD | Statement Distribution | VG-20 (B) | To be confirmed | |

### A4 Reports

Do any reports or inquiries apply to this process? If none, the section will read "No applicable reports".

| ID | Guide | Item | Current draft | Answer |
|---|---|---|---|---|
| A4.FAV | Favorites | VG-32 (B) | Reports for this process are pending SME confirmation. | |
| A4.VIEW | Personalized Views | VG-20 (B) | Reports for this process are pending SME confirmation. | |
| A4.AGED | Aged Balances | VG-18 (B) | Reports for this process are pending SME confirmation. | |
| A4.INV | Customer Invoices | VG-17 (B) | Reports for this process are pending SME confirmation. | |
| A4.EXP | Export to Excel | VG-16 (B) | Reports for this process are pending SME confirmation. | |
| A4.NOTE | Notes and Activities | VG-18 (B) | Reports for this process are pending SME confirmation. | |
| A4.LE | Legal Entities | VG-18 (B) | Reports for this process are pending SME confirmation. | |
| A4.WS | Workspace | VG-18 (B) | Reports for this process are pending SME confirmation. | |
| A4.OD | Overdue Customers | VG-18 (B) | Reports for this process are pending SME confirmation. | |
| A4.ACCT | Customer Account | VG-20 (B) | Reports for this process are pending SME confirmation. | |
| A4.ACT | Collection Activities | VG-20 (B) | Reports for this process are pending SME confirmation. | |
| A4.SP | Statement Preview | VG-20 (B) | Reports for this process are pending SME confirmation. | |
| A4.SD | Statement Distribution | VG-22 (B) | Reports for this process are pending SME confirmation. | |

### A5 Security role and access

Which security role gives AR Collections users access to the pages and controls in this guide, and who grants it? The clean-session test (S15) checks access in D365; this question confirms the intended role.

| ID | Guide | Item | Current draft | Answer |
|---|---|---|---|---|
| A5.FAV | Favorites | VG-17 (B) | Access to D365 and to the pages the guide uses (PROCESS START). | |
| A5.VIEW | Personalized Views | VG-25 (B) | Access to D365 and to the pages the guide uses (PROCESS START). | |
| A5.AGED | Aged Balances | VG-19 (B) | Access to D365 and to the pages the guide uses (PROCESS START). | |
| A5.INV | Customer Invoices | VG-18 (B) | Access to D365 and to the pages the guide uses (PROCESS START). | |
| A5.EXP | Export to Excel | VG-17 (B) | Access to D365 and to the pages the guide uses (PROCESS START). | |
| A5.NOTE | Notes and Activities | VG-19 (B) | Access to D365 and to the pages the guide uses (PROCESS START). | |
| A5.LE | Legal Entities | VG-19 (B) | Access to D365 and to the pages the guide uses (PROCESS START). | |
| A5.WS | Workspace | VG-19 (B) | Access to D365 and to the pages the guide uses (PROCESS START). | |
| A5.OD | Overdue Customers | VG-19 (B) | Access to D365 and to the pages the guide uses (PROCESS START). | |
| A5.ACCT | Customer Account | VG-21 (B) | Access to D365 and to the pages the guide uses (PROCESS START). | |
| A5.ACT | Collection Activities | VG-21 (B) | Access to D365 and to the pages the guide uses (PROCESS START). | |
| A5.SP | Statement Preview | VG-21 (B) | Access to D365 and to the pages the guide uses (PROCESS START). | |
| A5.SD | Statement Distribution | VG-23 (B) | Access to D365 and to the pages the guide uses (PROCESS START). | |

### A6 Review, test and approval

Who does the SME factual review, who tests the guide (not the author), and who approves it?

| ID | Guide | Item | Current draft | Answer |
|---|---|---|---|---|
| A6.FAV | Favorites | VG-25 (B) | Not yet assigned. | |
| A6.VIEW | Personalized Views | VG-26 (B) | Not yet assigned. | |
| A6.AGED | Aged Balances | VG-20 (B) | Not yet assigned. | |
| A6.INV | Customer Invoices | VG-19 (B) | Not yet assigned. | |
| A6.EXP | Export to Excel | VG-18 (B) | Not yet assigned. | |
| A6.NOTE | Notes and Activities | VG-20 (B) | Not yet assigned. | |
| A6.LE | Legal Entities | VG-20 (B) | Not yet assigned. | |
| A6.WS | Workspace | VG-20 (B) | Not yet assigned. | |
| A6.OD | Overdue Customers | VG-20 (B) | Not yet assigned. | |
| A6.ACCT | Customer Account | VG-22 (B) | Not yet assigned. | |
| A6.ACT | Collection Activities | VG-22 (B) | Not yet assigned. | |
| A6.SP | Statement Preview | VG-22 (B) | Not yet assigned. | |
| A6.SD | Statement Distribution | VG-24 (B) | Not yet assigned. | |

### A7 Support and environment

**Question.** Is the D365 issue form the correct route when a module or page is not available? Should guides name the D365 environment and sign-in method?

**Current draft or evidence.** The Favorites guide points users to the D365 issue form (from the template's Additional Resources). No environment is named.

**Answers:** Favorites VG-16 (B), Favorites VG-26.

**Answer:**

> 

### A8 Screenshots

**Question.** What is the masking policy for legal entity names, user names and customer data in screenshots? Which screenshots does source 0 mean by "minor screenshots required" for the workspace?

**Current draft or evidence.** Every screenshot register requires mock or masked data; no policy is confirmed. No figures are in the Word guides yet.

**Answers:** Favorites VG-27, Workspace VG-22.

**Answer:**

> 

---

## Part B: Business rules and controls (the AR Collections SME)

Grouped by theme so each rule is answered once and applied to every guide that uses it.

### B1 Customer-facing documents

**Question.** Confirm the wording and owner of the rule "Provide customer-facing account information as a PDF; do not send a customer an Excel export".

**Current draft or evidence.** Stated as a Key concept rule in four guides. Source 1 records it as a critical control from the Aged balances demonstration.

**Answers:** Aged Balances VG-13, Customer Invoices VG-12, Export to Excel VG-09, Statement Preview VG-15.

**Answer:**

> 

### B2 Exported data

**Question.** What export volume limits apply and what should users do when one is reached? What is the rule for storing, sharing and deleting exported files that contain customer data? Which pages do AR Collections users export most often?

**Current draft or evidence.** The Export guide says limits apply but states no figure, and asks users to follow the approved data handling rules.

**Answers:** Export to Excel VG-06 (B), Export to Excel VG-08 (B), Export to Excel VG-11.

**Answer:**

> 

### B3.1 Collection-note standard

**Question.** Which activity types are approved? Should "Action" always be used, or do Activity, Event, Appointment and Task have different uses?

**Current draft or evidence.** The Collection Activities guide gives email and phone as examples only.

**Answers:** Collection Activities VG-05 (B), Collection Activities VG-06.

**Answer:**

> 

### B3.2 Collection-note standard

**Question.** What must an email note and a telephone note contain (for example invoice numbers or a commitment-to-pay date)? What must never be recorded? Is there a naming and date convention?

**Current draft or evidence.** No mandatory or prohibited content is stated. Source 1 lists a collection-note standard with examples as still to be written.

**Answers:** Collection Activities VG-09 (B), Collection Activities VG-10 (B), Collection Activities VG-11, Collection Activities VG-24.

**Answer:**

> 

### B3.3 Collection-note standard

**Question.** Confirm the rule "Record collection notes and activities at customer level, not against individual invoices", its owner, and when a transaction-level note is right instead.

**Current draft or evidence.** Stated as a Key concept rule in two guides, from the trainer's preference in source 1.

**Answers:** Notes and Activities VG-11, Collection Activities VG-14.

**Answer:**

> 

### B4.1 Overdue accounts

**Question.** What do the balance due and overdue amount columns on Customers overdue mean?

**Current draft or evidence.** Draft: balance due is the total outstanding balance; the overdue amount is the part past its due date.

**Answers:** Overdue Customers VG-04 (B).

**Answer:**

> 

### B4.2 Overdue accounts

**Question.** What must users check before contacting a customer, to decide that an overdue balance is valid? Is there a value threshold for a "low-value" balance? What should users do, and whom should they tell, when a balance is not valid?

**Current draft or evidence.** Draft: check which transactions make up the overdue amount, check low-value balances for fees or overpayments, and contact the customer only when the balance is valid.

**Answers:** Overdue Customers VG-08 (B), Overdue Customers VG-09 (B), Overdue Customers VG-10 (B), Customer Account VG-15.

**Answer:**

> 

### B4.3 Overdue accounts

**Question.** What is the approved order for working overdue accounts (value, aging, customer risk or other)? When should users contact the receiving team, and after how many business days?

**Current draft or evidence.** No order or escalation timing is given in the guides.

**Answers:** Overdue Customers VG-11, Overdue Customers VG-13.

**Answer:**

> 

### B5.1 Statement controls

**Question.** What does Print management destination do, and what happens if it is left set when a user only wants to preview? Where does the recipient address come from?

**Current draft or evidence.** Preview guide: clear it and select Screen. Send guide: select it so the statement is delivered.

**Answers:** Statement Preview VG-05 (B), Statement Distribution VG-05 (B), Statement Distribution VG-06 (B).

**Answer:**

> 

### B5.2 Statement controls

**Question.** What are the approved statement parameters? Must Only open always be selected? When must the company logo be included?

**Current draft or evidence.** Both statement guides select Only open and include the company logo.

**Answers:** Statement Preview VG-03 (B), Statement Preview VG-04 (B), Statement Distribution VG-03 (B), Statement Distribution VG-04 (B), Statement Distribution VG-17 (B).

**Answer:**

> 

### B5.3 Statement controls

**Question.** What are the multi-currency statement limitations, and which customers must be excluded because of them? How do users check whether a customer is excluded from statements?

**Current draft or evidence.** The send guide asks users to check this before sending but cannot say how.

**Answers:** Statement Preview VG-13, Statement Distribution VG-12 (B), Statement Distribution VG-13.

**Answer:**

> 

### B5.4 Statement controls

**Question.** When must the Collections sent mailbox be checked, where is it, and who can access it? How is failed delivery identified, and what is the process? Where are sent statements retained?

**Current draft or evidence.** The send guide names these checks but cannot describe them.

**Answers:** Statement Distribution VG-09 (B), Statement Distribution VG-10 (B), Statement Distribution VG-11.

**Answer:**

> 

### B5.5 Statement controls

**Question.** May statements ever be emailed manually? What file format is required? Which statement details must users check before relying on a preview?

**Current draft or evidence.** Not stated in the guides.

**Answers:** Statement Distribution VG-15, Statement Distribution VG-16, Statement Preview VG-08.

**Answer:**

> 

### B6 Invoice and statement PDFs

**Question.** Which invoice details must users check before sharing an invoice? Is there a file naming convention, and where should invoice and statement PDFs be saved? Do the invoice steps also apply to credit notes? Which process covers sending an invoice to the customer?

**Current draft or evidence.** Both guides ask for a meaningful file name and do not give a location.

**Answers:** Customer Invoices VG-06, Customer Invoices VG-08, Customer Invoices VG-09, Customer Invoices VG-11, Customer Invoices VG-21, Statement Preview VG-10, Statement Preview VG-11.

**Answer:**

> 

### B7 Legal entities

**Question.** Please provide the legal entity name and code reference (business name and D365 ledger code). When is switching through the URL appropriate? Which legal entities do AR Collections users need? Confirm the wording of: ledger codes differ between CargoWise and D365; work with business names; confirm the active legal entity before processing. Do any AR Collections pages show data from more than one legal entity?

**Current draft or evidence.** Rules come from source 0 and source 2. No code list or URL format is in the guide.

**Answers:** Legal Entities VG-06 (B), Legal Entities VG-07 (B), Legal Entities VG-08, Legal Entities VG-09, Legal Entities VG-10, Legal Entities VG-13, Legal Entities VG-22.

**Answer:**

> 

### B8 Notes and activities

**Question.** Which entry types does D365 create on the Notes page, and how do users tell them from user-entered notes? How do activities relate to Notes entries, and how does system-generated activity differ from activities users record?

**Current draft or evidence.** The Notes guide names statements and collection letters as examples only.

**Answers:** Notes and Activities VG-05, Notes and Activities VG-06 (B), Notes and Activities VG-12, Collection Activities VG-15.

**Answer:**

> 

### B9 Balances and transactions

**Question.** Confirm the wording on reporting currency on Aged balances (and which legal entities differ), the currency revaluation definition, and how to read a settlement history. Should users also open customer accounts from Aged balances or Customers overdue?

**Current draft or evidence.** Drafts: amounts may show in the ledger's reporting currency; revaluations are entries D365 creates when it revalues foreign currency balances; settlement history shows what a transaction was settled against.

**Answers:** Aged Balances VG-09, Customer Account VG-08, Customer Account VG-12 (B), Customer Account VG-03.

**Answer:**

> 

### B10 Workspace

**Question.** Which Customer credit and collections workspace sections are not used in AR Collections? Confirm the workspace definition wording.

**Current draft or evidence.** The guide names Customers overdue, Payment journals not posted, Notes and Open payment journals as used, and lists others without saying whether they are used.

**Answers:** Workspace VG-08 (B), Workspace VG-09.

**Answer:**

> 

### B11 Favorites and views

**Question.** What do AR Collections users use Customer payment journal for? Does Aged balances give access to collection activities? Which page did the views demonstration use, and which recommended columns exist on each page? Is there a view naming convention, and should the prepared Aged balances list be a standard saved view? Are saved views personal? Should Update a Saved View stay a separate topic?

**Current draft or evidence.** These points come from the baseline drafts and are not confirmed.

**Answers:** Favorites VG-18, Favorites VG-20, Personalized Views VG-01 (B), Personalized Views VG-12, Personalized Views VG-19, Personalized Views VG-28, Aged Balances VG-22.

**Answer:**

> 

---

## Part C: Recording (whoever holds AR Training D365)

Transcript excerpts and timestamps, used to check wording and to capture screenshots.

### C1 Recording timestamps

Provide the transcript excerpt and timestamps for this guide's demonstration in *AR Training D365*.

| ID | Guide | Item | Source or current text | Answer |
|---|---|---|---|---|
| C1.VIEW | Personalized Views | VG-27 | Recording timestamps for the views demonstration. These are needed for frame review and screenshots. | |
| C1.AGED | Aged Balances | VG-21 | Recording timestamps for the Aged balances demonstration. | |
| C1.INV | Customer Invoices | VG-20 | Recording timestamps for the invoice demonstration. | |
| C1.EXP | Export to Excel | VG-19 | Recording timestamps for the export demonstration. | |
| C1.NOTE | Notes and Activities | VG-21 | Recording timestamps for the Notes and activities demonstration. | |
| C1.LE | Legal Entities | VG-21 | Recording timestamps for the legal entity demonstration. | |
| C1.WS | Workspace | VG-21 | Recording timestamps for the workspace walkthrough. The Navigation Pane explanation is at about 00:32:42 (source 3.2). | |
| C1.OD | Overdue Customers | VG-21 | Recording timestamps for the Customers overdue demonstration. | |
| C1.ACCT | Customer Account | VG-23 | Recording timestamps for the customer account demonstration. | |
| C1.ACT | Collection Activities | VG-23 | Recording timestamps for the activity demonstration. | |
| C1.SP | Statement Preview | VG-23 | Recording timestamps for the statement demonstration. | |
| C1.SD | Statement Distribution | VG-25 | Recording timestamps for the statement demonstration. | |

### C2 Recording checks

**Question.** From the recording: did the Aged balances demonstration select several customers with "is one of"? What wording does the trainer use for Open customer invoices?

**Current draft or evidence.** Both are inferences in the drafts.

**Answers:** Aged Balances VG-08 (B), Favorites VG-19.

**Answer:**

> 

---

## Part D: Project decisions (project team and BPO)

Each decision has a proposed default: the drafts' current choice. Confirm or change it.

### D1 Guide code and final title

Assign the guide code and confirm the final title (decision D-006).

| ID | Guide | Item | Source or current text | Answer |
|---|---|---|---|---|
| D1.FAV | Favorites | VG-22 (B) | Guide code and final title. Source 0 proposes PG-AR-010. The authoring guide requires an assigned code (NNN-Guide Title PG vX.docx). | |
| D1.VIEW | Personalized Views | VG-24 (B) | Guide code and final title. Source 0 proposes PG-AR-004. | |
| D1.AGED | Aged Balances | VG-17 (B) | Guide code and final title. Source 0 proposes PG-AR-007. | |
| D1.INV | Customer Invoices | VG-16 (B) | Guide code and final title. Source 0 proposes PG-AR-016. | |
| D1.EXP | Export to Excel | VG-15 (B) | Guide code and final title. Source 0 proposes PG-AR-019 Export D365 Customer Data to Excel; source 2 uses "Export all rows from a D365 grid". | |
| D1.NOTE | Notes and Activities | VG-17 (B) | Guide code and final title, and whether notes and activities stay in one guide. Source 0 proposes PG-AR-008 and PG-AR-022. | |
| D1.LE | Legal Entities | VG-17 (B) | Guide code and final title. Source 0 gives no code; source 2 uses "Switch to the required legal entity in D365". | |
| D1.WS | Workspace | VG-17 (B) | Guide code and final title. Source 0 proposes PG-AR-001 Navigate and Interpret the Customer Credit & Collections Workspace. | |
| D1.OD | Overdue Customers | VG-17 (B) | Guide code and final title. Source 0 proposes PG-AR-002 Review and Manage Overdue Customers. | |
| D1.ACCT | Customer Account | VG-19 (B) | Guide code and final title, and whether source 0's three suggested guides (PG-AR-005, -015, -017) stay combined here. | |
| D1.ACT | Collection Activities | VG-19 (B) | Guide code and final title. Source 0 proposes PG-AR-003 Record Collection Activities Against a Customer. | |
| D1.SP | Statement Preview | VG-19 (B) | Guide code and final title, and whether preview and send are separate guides (source 0 proposes one: PG-AR-018). | |
| D1.SD | Statement Distribution | VG-21 (B) | Guide code and final title. Source 0 proposes PG-AR-018 Generate and Send Customer Statements. | |

### D2 Scope boundaries

Confirm each scope boundary, or say which to change. Each is the drafts' current choice.

| ID | Guide | Item | Proposed default | Answer |
|---|---|---|---|---|
| D2.1 | Aged Balances | VG-23 | Opening a customer from Aged balances belongs in the Investigate a customer account guide, not the Aged Balances guide. | |
| D2.2 | Customer Account | VG-13 | Undo settlement stays out of the Customer Account guide (higher-risk; its own gated guide). | |
| D2.3 | Customer Account | VG-24 | The custom all-customer transaction report is a separate guide, once its access path is captured. | |
| D2.4 | Export to Excel | VG-20 | The custom all-customer transaction report and daily bank statements are separate guides. | |
| D2.5 | Export to Excel | VG-10 | The Export guide opens "the page that holds the data" instead of one fixed Modules/Navigate path. | |
| D2.6 | Customer Invoices | VG-22 | Finding an invoice with Show closed or Hide FX revaluations belongs in the transactions guide, not the Invoices guide. | |
| D2.7 | Notes and Activities | VG-22 | Recording a new activity belongs in the Record a collection activity guide. | |
| D2.8 | Overdue Customers | VG-23 | Recording the contact and using the email address belong in the Record a collection activity guide. | |
| D2.9 | Statement Preview | VG-24 | Sending a statement is covered by the Generate and send a customer statement guide, not the preview guide. | |
| D2.10 | Statement Preview | VG-14 | Statements for multiple related accounts are out of the Statement Preview guide (source 1: partial). | |
| D2.11 | Statement Distribution | VG-14 | Statements for multiple related accounts are out of the Statement Distribution guide (source 1: partial). | |
| D2.12 | Workspace | VG-13 | Workspace indicators belong in a separate system overview, not the Workspace guide. | |

---

## After the answers

1. Record each answer in the response sheet with the person and date.
2. In each affected validation register, close the item with the answer as evidence (for example "Closed: SME pack B5.2, 2026-10-xx"), or keep it open with the partial answer.
3. Update the Word guides, remove the matching review comments, and move the changed guides to v0.2 together with the clean-session test results.
4. Update the Command Centre gaps and the project notes decisions.

## Change log

| Date | Change |
|---|---|
| 2026-10-15 | Pack created from the 13 validation registers. |
