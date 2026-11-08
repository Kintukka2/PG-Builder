# PG-Builder

Development workspace for **Microsoft Dynamics 365 (D365) Procedure Guides (PGs)** and supporting learning content.

Each D365 task and its controls is **one topic** inside a process-level PG (D-045). Guides follow the O2C numbering standard (codes 200 to 299, one ten-number block per process family), and sit inside a learning architecture of modules, knowledge articles, reference guides and business rules.

> **Keep this README current.** Update the status tracker and conventions whenever a topic draft changes gate, a decision is made, or a new topic starts.

---

## Current focus

| Topic | Folder | Status |
|---|---|---|
| **Accounts Receivable (AR) Collections** | [`ar-collections-learning/`](ar-collections-learning/) | Active. Every topic draft is merged into a working draft: **260 O2C Getting Started** and **221 Customer Payment Corrections** (D-048) and **230 Collections v3.0** (D-052), with a 230 v2.4 draft for the 221 split (D-051). 240 Direct Debit is a required guide with no document yet (D-049). |
| *Further D365 topics* | *To be added as sibling folders* | Planned |

## PG template (governs every PG)

All PGs are produced in the current master Word template and follow its companion authoring guide. Both are stored unchanged in [`templates/`](templates/):

| File | Role |
|---|---|
| [`PG_Word_Template-MASTER TEMPLATE.docx`](templates/) | Master layout. Never edit it. Use **Save As** to start each PG. |
| [`PG_Template_Authoring_Guide_v1.docx`](templates/) | Content and formatting rules, and the final checklist. |

Guide codes and file names follow the **O2C PG Numbering Standard v1.3** and its register (`O2C_PG_Numbering_Register.json`), held outside this repository by the register owner (T3, D-046).

## Repository structure

```
templates/                   PG master template and authoring guide (unchanged)
```

Each topic has its own folder with the same internal structure:

```
<topic>-learning/
  01-procedure-guides/       Topic drafts and guides: Word files (editable source) and Markdown previews
  02-screenshot-registers/   Figure-to-step mapping, timestamps, captions, callouts
  03-validation/             Validation-gap registers, test plans and logs, terminology
  04-quality-assurance/      QA checklists applied before review and publication
  05-project-notes/          Project context, source summary, decisions log
  06-reference-guides/       Reference content shared by several PGs (for example journal controls)
```

## AR Collections: guides

The plan for these four guides went to the O2C stakeholders on 2026-11-03 (D-050): Daniel Moreira confirms each guide's scope and content with Maria Pabalan, reviews run through the ADO tickets below, and each guide needs BPO sign-off. Codes 221 and 260 are proposed (D-046). Both guides are shared with the SME for review only (SME review pack v2); neither circulates further until the register owner records its code and the BPO confirms its scope (D-048).

| Code | Guide | ADO | Gate | Topics | Files |
|---|---|---|---|---|---|
| 260 | O2C Getting Started | Task 16994 | **v0.1 working draft** (D-048): 6 guide-level items open (all blocking), plus 55 carried review comments | 1 Switch Legal Entity with the Selector; 2 Switch Legal Entity Using the Ledger Code; 3 Add Pages to Favorites; 4 Create a Personalized View; 5 Update a Saved View; 6 Export All Rows from a Grid | [Word PG](ar-collections-learning/01-procedure-guides/260-O2C%20Getting%20Started%20PG%20v0.1.docx) · [PDF](ar-collections-learning/01-procedure-guides/260-O2C%20Getting%20Started%20PG%20v0.1.pdf) · [Preview](ar-collections-learning/01-procedure-guides/PG-260-O2C-Getting-Started-DRAFT.md) · [Validation](ar-collections-learning/03-validation/260-O2C-Getting-Started-Validation.md) |
| 221 | Customer Payment Corrections | Task 16993 | **v0.1 working draft** (D-048): 20 guide-level items open (19 blocking), plus 106 carried review comments. Higher-risk: not used on live customer accounts until its blocking items close | 1 Settle Customer Transactions; 2 Undo a Settlement; 3 Transfer Funds Between Customer Accounts; 4 Distribute a Parent Account Payment Across Child Accounts; 5 Restore a Written-Off or Overpayment Amount; 6 Write Off a Bank Fee or Small Residual | [Word PG](ar-collections-learning/01-procedure-guides/221-Customer%20Payment%20Corrections%20PG%20v0.1.docx) · [PDF](ar-collections-learning/01-procedure-guides/221-Customer%20Payment%20Corrections%20PG%20v0.1.pdf) · [Preview](ar-collections-learning/01-procedure-guides/PG-221-Customer-Payment-Corrections-DRAFT.md) · [Validation](ar-collections-learning/03-validation/221-Customer-Payment-Corrections-Validation.md) |
| 230 | Collections | Task 16886 | **v2.4 draft** (D-051): the 221 split only, for sign-off with 221; 4 items open (all blocking). **v3.0 working draft** (D-052): rebuilt in the master template with the nine topic drafts, shared with the SME for review only (SME review pack of 8 November); 10 guide-level items open (all blocking), plus 127 carried review comments. v2.3 stays live until each passes its gates | v3.0: 1 Start the Collections Day; 2 Monitor Customers (2.1 to 2.8); 3 Manage Customer Pools and Collection Agents; 4 Contact the Customer; 5 Record a Customer Collection Activity; 6 Manage Customer Statements; 7 Resolve the Account (7.1 to 7.4); 8 Update and Close a Customer Activity | v2.4: [Word PG](ar-collections-learning/01-procedure-guides/230-Collections%20PG%20v2.4.docx) · [PDF](ar-collections-learning/01-procedure-guides/230-Collections%20PG%20v2.4.pdf) · [Validation](ar-collections-learning/03-validation/230-Collections-v2.4-Validation.md)<br>v3.0: [Word PG](ar-collections-learning/01-procedure-guides/230-Collections%20PG%20v3.0.docx) · [PDF](ar-collections-learning/01-procedure-guides/230-Collections%20PG%20v3.0.pdf) · [Preview](ar-collections-learning/01-procedure-guides/PG-230-Collections-v3.0-DRAFT.md) · [Validation](ar-collections-learning/03-validation/230-Collections-v3.0-Validation.md) |
| 240 | Direct Debit | Task 16894 | **Required; no document yet** (D-049). Maria Pabalan confirms the remaining scope by the week of 9 November 2026 (D-050) | Proposed: maintain direct debit set-up; process direct debit payments; change or remove direct debit | None |

## AR Collections: topic draft tracker

Backlog rank and release come from the AR development roadmap. Drafting order follows the recommended first and second drafting batches. Both batches are drafted. Each draft is a **topic draft** (D-045): the Destination column gives the guide and topic it merges into, from the [O2C PG suite plan](ar-collections-learning/05-project-notes/O2C-PG-Suite-Plan.md). Every draft is now merged into 260, 221 or 230 and **frozen** (D-048, D-052): edit the guide's Word file, and keep recording answers in the draft's register against the same IDs.

| Rank | Topic draft | Destination | Release | Draft batch | Gate | Files |
|---|---|---|---|---|---|---|
| 4 | Configure AR Collections Favorites | 260 topic 3; 230 Part 1 (both merged) | 1 | 1st (#1) | **Merged into 260 v0.1 and 230 v3.0; frozen** (v0.2): 30 open validation gaps, 16 blocking | [Word PG](ar-collections-learning/01-procedure-guides/TBC-AR%20Collections%20Favorites%20PG%20v0.2.docx) · [Preview](ar-collections-learning/01-procedure-guides/PG-AR-Configure-Collections-Favourites-DRAFT.md) · [Screenshots](ar-collections-learning/02-screenshot-registers/PG-AR-Configure-Collections-Favourites-Screenshots.md) · [Validation](ar-collections-learning/03-validation/PG-AR-Configure-Collections-Favourites-Validation.md) |
| 5 | Create and save a personalised D365 view (*AR Collections Personalized Views*) | 260 topics 4 and 5; 230 Part 1 (both merged) | 1 | 1st (#2) | **Merged into 260 v0.1 and 230 v3.0; frozen**: 29 open validation gaps, 23 blocking | [Word PG](ar-collections-learning/01-procedure-guides/TBC-AR%20Collections%20Personalized%20Views%20PG%20v0.1.docx) · [Preview](ar-collections-learning/01-procedure-guides/PG-AR-Personalized-Views-DRAFT.md) · [Screenshots](ar-collections-learning/02-screenshot-registers/PG-AR-Personalized-Views-Screenshots.md) · [Validation](ar-collections-learning/03-validation/PG-AR-Personalized-Views-Validation.md) |
| 7 | Review customer aged balances (*AR Collections Aged Balances*) | 230 topics 2.2 and 2.3 (merged) | 1 | 1st (#3) | **Merged into 230 v3.0; frozen**: 22 open validation gaps, 15 blocking | [Word PG](ar-collections-learning/01-procedure-guides/TBC-AR%20Collections%20Aged%20Balances%20PG%20v0.1.docx) · [Preview](ar-collections-learning/01-procedure-guides/PG-AR-Aged-Balances-DRAFT.md) · [Screenshots](ar-collections-learning/02-screenshot-registers/PG-AR-Aged-Balances-Screenshots.md) · [Validation](ar-collections-learning/03-validation/PG-AR-Aged-Balances-Validation.md) |
| 11 | View and download a customer invoice (*AR Collections Customer Invoices*) | 230 topic 7.1 (merged) | 2 | 1st (#4) | **Merged into 230 v3.0; frozen**: 22 open validation gaps, 14 blocking | [Word PG](ar-collections-learning/01-procedure-guides/TBC-AR%20Collections%20Customer%20Invoices%20PG%20v0.1.docx) · [Preview](ar-collections-learning/01-procedure-guides/PG-AR-Customer-Invoices-DRAFT.md) · [Screenshots](ar-collections-learning/02-screenshot-registers/PG-AR-Customer-Invoices-Screenshots.md) · [Validation](ar-collections-learning/03-validation/PG-AR-Customer-Invoices-Validation.md) |
| 17 | Export all rows from a D365 grid (*AR Collections Export to Excel*) | 260 topic 6 (merged) | 2 | 1st (#5) | **Merged into 260 v0.1; frozen**: 20 open validation gaps, 12 blocking | [Word PG](ar-collections-learning/01-procedure-guides/TBC-AR%20Collections%20Export%20to%20Excel%20PG%20v0.1.docx) · [Preview](ar-collections-learning/01-procedure-guides/PG-AR-Export-to-Excel-DRAFT.md) · [Screenshots](ar-collections-learning/02-screenshot-registers/PG-AR-Export-to-Excel-Screenshots.md) · [Validation](ar-collections-learning/03-validation/PG-AR-Export-to-Excel-Validation.md) |
| 9 | Review customer notes and activities (*AR Collections Notes and Activities*) | 230 topics 2.5 and 2.6 (merged) | 1 | 1st (#6) | **Merged into 230 v3.0; frozen**: 22 open validation gaps, 15 blocking | [Word PG](ar-collections-learning/01-procedure-guides/TBC-AR%20Collections%20Notes%20and%20Activities%20PG%20v0.1.docx) · [Preview](ar-collections-learning/01-procedure-guides/PG-AR-Notes-and-Activities-DRAFT.md) · [Screenshots](ar-collections-learning/02-screenshot-registers/PG-AR-Notes-and-Activities-Screenshots.md) · [Validation](ar-collections-learning/03-validation/PG-AR-Notes-and-Activities-Validation.md) |
| 2 | Switch between legal entities (*AR Collections Legal Entities*) | 260 topics 1 and 2 (merged) | 1 | 2nd (#1) | **Merged into 260 v0.1; frozen**: 22 open validation gaps, 13 blocking | [Word PG](ar-collections-learning/01-procedure-guides/TBC-AR%20Collections%20Legal%20Entities%20PG%20v0.1.docx) · [Preview](ar-collections-learning/01-procedure-guides/PG-AR-Legal-Entities-DRAFT.md) · [Screenshots](ar-collections-learning/02-screenshot-registers/PG-AR-Legal-Entities-Screenshots.md) · [Validation](ar-collections-learning/03-validation/PG-AR-Legal-Entities-Validation.md) |
| 3 | Navigate the Customer Credit and Collections workspace (*AR Collections Workspace*) | 230 topics 1.1 and 1.2 (merged) | 1 | 2nd (#2) | **Merged into 230 v3.0; frozen**: 22 open validation gaps, 14 blocking | [Word PG](ar-collections-learning/01-procedure-guides/TBC-AR%20Collections%20Workspace%20PG%20v0.1.docx) · [Preview](ar-collections-learning/01-procedure-guides/PG-AR-Workspace-DRAFT.md) · [Screenshots](ar-collections-learning/02-screenshot-registers/PG-AR-Workspace-Screenshots.md) · [Validation](ar-collections-learning/03-validation/PG-AR-Workspace-Validation.md) |
| 6 | Review overdue customers (*AR Collections Overdue Customers*) | 230 topics 2.1 and 4.1 (merged) | 1 | 2nd (#3) | **Merged into 230 v3.0; frozen**: 22 open validation gaps, 16 blocking | [Word PG](ar-collections-learning/01-procedure-guides/TBC-AR%20Collections%20Overdue%20Customers%20PG%20v0.1.docx) · [Preview](ar-collections-learning/01-procedure-guides/PG-AR-Overdue-Customers-DRAFT.md) · [Screenshots](ar-collections-learning/02-screenshot-registers/PG-AR-Overdue-Customers-Screenshots.md) · [Validation](ar-collections-learning/03-validation/PG-AR-Overdue-Customers-Validation.md) |
| 8 | Investigate a customer account (*AR Collections Customer Account*) | 230 topic 2.4 (merged) | 1 | 2nd (#4) | **Merged into 230 v3.0; frozen**: 24 open validation gaps, 17 blocking | [Word PG](ar-collections-learning/01-procedure-guides/TBC-AR%20Collections%20Customer%20Account%20PG%20v0.1.docx) · [Preview](ar-collections-learning/01-procedure-guides/PG-AR-Customer-Account-DRAFT.md) · [Screenshots](ar-collections-learning/02-screenshot-registers/PG-AR-Customer-Account-Screenshots.md) · [Validation](ar-collections-learning/03-validation/PG-AR-Customer-Account-Validation.md) |
| 10 | Record a collection activity (*AR Collections Collection Activities*) | 230 topic 5 (merged) | 1 | 2nd (#5) | **Merged into 230 v3.0; frozen**: 24 open validation gaps, 17 blocking | [Word PG](ar-collections-learning/01-procedure-guides/TBC-AR%20Collections%20Collection%20Activities%20PG%20v0.1.docx) · [Preview](ar-collections-learning/01-procedure-guides/PG-AR-Collection-Activities-DRAFT.md) · [Screenshots](ar-collections-learning/02-screenshot-registers/PG-AR-Collection-Activities-Screenshots.md) · [Validation](ar-collections-learning/03-validation/PG-AR-Collection-Activities-Validation.md) |
| 12 | Generate and send a customer statement (*AR Collections Statement Distribution*) | 230 topic 6.2 (merged) | 2 | 2nd (#7) | **Merged into 230 v3.0; frozen**: 25 open validation gaps, 19 blocking. Customer-facing: not tested on real customers until its control items close | [Word PG](ar-collections-learning/01-procedure-guides/TBC-AR%20Collections%20Statement%20Distribution%20PG%20v0.1.docx) · [Preview](ar-collections-learning/01-procedure-guides/PG-AR-Statement-Distribution-DRAFT.md) · [Screenshots](ar-collections-learning/02-screenshot-registers/PG-AR-Statement-Distribution-Screenshots.md) · [Validation](ar-collections-learning/03-validation/PG-AR-Statement-Distribution-Validation.md) |
| 13 | Preview and download a customer statement (*AR Collections Statement Preview*) | 230 topic 6.1 (merged) | 2 | 2nd (#6) | **Merged into 230 v3.0; frozen**: 24 open validation gaps, 16 blocking | [Word PG](ar-collections-learning/01-procedure-guides/TBC-AR%20Collections%20Statement%20Preview%20PG%20v0.1.docx) · [Preview](ar-collections-learning/01-procedure-guides/PG-AR-Statement-Preview-DRAFT.md) · [Screenshots](ar-collections-learning/02-screenshot-registers/PG-AR-Statement-Preview-Screenshots.md) · [Validation](ar-collections-learning/03-validation/PG-AR-Statement-Preview-Validation.md) |

### Part 2 drafts (Customer payment journal and transfers)

From the *AR Training D365* Part 2 update pack. These are **v0.1 SME review drafts** in the master template (decision D-041), built from AI-generated notes that are not yet checked against the Part 2 recording. They are higher-risk and are not finalised until their gaps are validated. One shared [validation register](ar-collections-learning/03-validation/Part2-CPJL-and-Transfers-Validation.md) covers all four (46 open items, 38 blocking). All four are merged into 221 v0.1 (D-048); the register stays the record for their items.

| Rank | Topic draft | Destination | Release | Gate | Files |
|---|---|---|---|---|---|
| 27 | Transfer funds between customer accounts (*AR Collections Customer Account Transfers*) | 221 topic 3 (merged) | 3 (moved from 4, proposed D-036) | **Merged into 221 v0.1; frozen** | [Word PG](ar-collections-learning/01-procedure-guides/TBC-AR%20Collections%20Customer%20Account%20Transfers%20PG%20v0.1.docx) · [Preview](ar-collections-learning/01-procedure-guides/PG-AR-Transfer-Funds-Between-Customer-Accounts-DRAFT.md) · [Screenshots](ar-collections-learning/02-screenshot-registers/PG-AR-Transfer-Funds-Between-Customer-Accounts-Screenshots.md) |
| 33 | Transfer a parent account payment across child accounts, with partial allocation (*AR Collections Parent Payment Distribution*) | 221 topic 4 (merged) | 3 | **Merged into 221 v0.1; frozen** | [Word PG](ar-collections-learning/01-procedure-guides/TBC-AR%20Collections%20Parent%20Payment%20Distribution%20PG%20v0.1.docx) · [Preview](ar-collections-learning/01-procedure-guides/PG-AR-Transfer-Parent-Payment-Across-Child-Accounts-DRAFT.md) · [Screenshots](ar-collections-learning/02-screenshot-registers/PG-AR-Transfer-Parent-Payment-Across-Child-Accounts-Screenshots.md) |
| 34 | Restore a written-off or overpayment amount (*AR Collections Overpayment and Write-Off Restoration*) | 221 topic 5 (merged) | 3 | **Merged into 221 v0.1; frozen** | [Word PG](ar-collections-learning/01-procedure-guides/TBC-AR%20Collections%20Overpayment%20and%20Write-Off%20Restoration%20PG%20v0.1.docx) · [Preview](ar-collections-learning/01-procedure-guides/PG-AR-Restore-Written-Off-Overpayment-DRAFT.md) · [Screenshots](ar-collections-learning/02-screenshot-registers/PG-AR-Restore-Written-Off-Overpayment-Screenshots.md) |
| 35 | Customer Payment Journal (CPJL) controls reference, including Simulate Posting (*AR Collections Customer Payment Journal Controls*) | 221 Part 1 Key concepts (merged) | 3 | **Merged into 221 v0.1; frozen** | [Word reference](ar-collections-learning/06-reference-guides/TBC-AR%20Collections%20Customer%20Payment%20Journal%20Controls%20Reference%20v0.1.docx) · [Preview](ar-collections-learning/06-reference-guides/REF-AR-Customer-Payment-Journal-Controls-DRAFT.md) |
| 36 | Customer Pools | 230 topic 3 (legacy topic) | 4 | **Validation backlog only**: no PG (D-035) | [Register](ar-collections-learning/03-validation/Customer-Pools-Validation.md) |

Shared AR resources:

- [O2C PG suite plan](ar-collections-learning/05-project-notes/O2C-PG-Suite-Plan.md): one task per topic; the destination guide and topic for every draft and backlog rank; proposed codes 221 and 260 (D-045, D-046); proposed 240 scope (D-049)
- [Project context and decisions](ar-collections-learning/05-project-notes/Project-Context-and-Decisions.md)
- [PG content QA checklist](ar-collections-learning/04-quality-assurance/PG-Content-QA-Checklist.md)
- [Clean-session D365 test plan](ar-collections-learning/03-validation/Clean-Session-Test-Plan.md) and its [results log](ar-collections-learning/03-validation/Clean-Session-Test-Log.xlsx): one session that tests 148 validation items across all 13 guides
- [SME question pack](ar-collections-learning/03-validation/SME-Question-Pack.md) and its [response sheet](ar-collections-learning/03-validation/SME-Question-Pack-Responses.xlsx): 31 questions that answer the 191 open items needing an SME, a recording or a project decision. 11 questions (46 items) carry a legacy PG proposal to confirm
- [SME question pack, Part 2 supplement](ar-collections-learning/03-validation/SME-Question-Pack-Part2-Supplement.md) and its [response sheet](ar-collections-learning/03-validation/SME-Question-Pack-Part2-Responses.xlsx): 27 questions that answer the 50 open Part 2 and Customer Pools items (42 blocking). 11 questions (16 items) carry a legacy PG proposal to confirm
- [Legacy O2C PG cross-comparison](ar-collections-learning/03-validation/Legacy-O2C-PG-Cross-Comparison.md): what the five legacy O2C procedure guides cover compared with the drafts, and which open items they help answer (184 of 364, 92 strong). Reference evidence only (D-044).

## Development gates

Every topic moves through these gates. A guide version is published only when every topic in it has passed them:

`Identified → Source reviewed → Gap validated → Drafted → System tested → SME validated → Process-owner approved → Published`

Higher-risk topics (settlement, write-offs, customer maintenance, exclusions, payment terms, account transfers) are **not finalised** until their listed gaps are validated.

## Working conventions

**Format**

- Every guide is a Save As copy of the master template, completed according to the authoring guide.
- Each task is one topic. Topic drafts merge into their destination guide, and a task never appears in two guides; other guides link to it (D-045).
- The Word file is the editable source.
- A Markdown preview sits beside it for review on GitHub. Update the preview after the Word file changes.

**Evidence**

- The supplied source documents are the source of truth for process content.
- No D365 step, label, business rule, approval, owner, role or system behavior is invented.
- Every unconfirmed item gets a stable ID (`VG-01` …) in its topic draft's validation register, which serves as the question log. IDs stay stable after a merge: the destination guide's log keeps the draft name with each ID (for example *Aged Balances VG-03*). Items that belong to a whole guide get the guide's prefix (`G260-01`, `G221-01`).
- Each one that affects the text is also a Word review comment on that text.

**Procedure writing (from the template)**

- Action | Description rows, one action per row.
- *Italic* verb; **bold** UI labels and business objects.
- PROCESS START, STEP COMPLETE and PROCESS COMPLETE boundary rows.
- The standard navigation pattern (*Check* the **Entity** → *Click* **Modules**).

**Files**

- Guides are named `NNN-Guide Title PG vX.docx` (working Word file) and `NNN-Guide Title PG.pdf` (published), with `NNN` from the O2C numbering standard (D-046). Topic drafts keep their `TBC-` working names until they merge.
- Companion Markdown files keep their `PG-<Area>-<Task-Name>` names; a guide's preview is `PG-NNN-<Guide-Title>-DRAFT.md`.

**Screenshots**

- Optional, and used only where they add context.
- Never left as placeholders in the Word PG.
- Mapped in the screenshot register, captured in a clean D365 session, with customer data masked.

**Language**

- PG text uses English (United States), as the template requires.
- UI labels match the D365 screen exactly.
- Internal working notes may use UK/AU spelling.

## Source material

Source documents for each topic are held outside this repository and are not modified. They are listed in each topic's `05-project-notes/Project-Context-and-Decisions.md`.
