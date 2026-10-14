# PG-Builder

Development workspace for granular **Microsoft Dynamics 365 (D365) Procedure Guides (PGs)** and supporting learning content.

Each PG covers **one** D365 task and its controls. PGs sit inside a learning architecture of modules, knowledge articles, reference guides and business rules.

> **Keep this README current.** Update the status tracker and conventions whenever a PG changes gate, a decision is made, or a new topic starts.

---

## Current focus

| Topic | Folder | Status |
|---|---|---|
| **Accounts Receivable (AR) Collections** | [`ar-collections-learning/`](ar-collections-learning/) | Active. First drafting batch complete; second batch in progress. Ten PGs in SME review draft. |
| *Further D365 topics* | *To be added as sibling folders* | Planned |

## PG template (governs every PG)

All PGs are produced in the current master Word template and follow its companion authoring guide. Both are stored unchanged in [`templates/`](templates/):

| File | Role |
|---|---|
| [`PG_Word_Template-MASTER TEMPLATE.docx`](templates/) | Master layout. Never edit it. Use **Save As** to start each PG. |
| [`PG_Template_Authoring_Guide_v1.docx`](templates/) | Content and formatting rules, and the final checklist. |

## Repository structure

```
templates/                   PG master template and authoring guide (unchanged)
command-centre/              Source for the PG Command Centre and Delivery Flow pages (claude.ai artifacts)
```

Each topic has its own folder with the same internal structure:

```
<topic>-learning/
  01-procedure-guides/       PG Word files (editable source) and Markdown previews
  02-screenshot-registers/   Figure-to-step mapping, timestamps, captions, callouts
  03-validation/             Validation-gap registers, baseline reviews, terminology
  04-quality-assurance/      QA checklists applied before review and publication
  05-project-notes/          Project context, source summary, decisions log
```

## AR Collections: PG status tracker

Backlog rank and release come from the AR development roadmap. Drafting order follows the recommended first and second drafting batches.

| Rank | PG | Release | Draft batch | Gate | Files |
|---|---|---|---|---|---|
| 4 | Configure AR Collections Favorites | 1 | 1st (#1) | **Drafted; SME review draft** (v0.2): 30 open validation gaps, 16 blocking | [Word PG](ar-collections-learning/01-procedure-guides/TBC-AR%20Collections%20Favorites%20PG%20v0.2.docx) · [Preview](ar-collections-learning/01-procedure-guides/PG-AR-Configure-Collections-Favourites-DRAFT.md) · [Screenshots](ar-collections-learning/02-screenshot-registers/PG-AR-Configure-Collections-Favourites-Screenshots.md) · [Validation](ar-collections-learning/03-validation/PG-AR-Configure-Collections-Favourites-Validation.md) |
| 5 | Create and save a personalised D365 view (*AR Collections Personalized Views*) | 1 | 1st (#2) | **Drafted; SME review draft** (v0.1): 29 open validation gaps, 23 blocking | [Word PG](ar-collections-learning/01-procedure-guides/TBC-AR%20Collections%20Personalized%20Views%20PG%20v0.1.docx) · [Preview](ar-collections-learning/01-procedure-guides/PG-AR-Personalized-Views-DRAFT.md) · [Screenshots](ar-collections-learning/02-screenshot-registers/PG-AR-Personalized-Views-Screenshots.md) · [Validation](ar-collections-learning/03-validation/PG-AR-Personalized-Views-Validation.md) |
| 7 | Review customer aged balances (*AR Collections Aged Balances*) | 1 | 1st (#3) | **Drafted; SME review draft** (v0.1): 22 open validation gaps, 15 blocking | [Word PG](ar-collections-learning/01-procedure-guides/TBC-AR%20Collections%20Aged%20Balances%20PG%20v0.1.docx) · [Preview](ar-collections-learning/01-procedure-guides/PG-AR-Aged-Balances-DRAFT.md) · [Screenshots](ar-collections-learning/02-screenshot-registers/PG-AR-Aged-Balances-Screenshots.md) · [Validation](ar-collections-learning/03-validation/PG-AR-Aged-Balances-Validation.md) |
| 11 | View and download a customer invoice (*AR Collections Customer Invoices*) | 2 | 1st (#4) | **Drafted; SME review draft** (v0.1): 22 open validation gaps, 14 blocking | [Word PG](ar-collections-learning/01-procedure-guides/TBC-AR%20Collections%20Customer%20Invoices%20PG%20v0.1.docx) · [Preview](ar-collections-learning/01-procedure-guides/PG-AR-Customer-Invoices-DRAFT.md) · [Screenshots](ar-collections-learning/02-screenshot-registers/PG-AR-Customer-Invoices-Screenshots.md) · [Validation](ar-collections-learning/03-validation/PG-AR-Customer-Invoices-Validation.md) |
| 17 | Export all rows from a D365 grid (*AR Collections Export to Excel*) | 2 | 1st (#5) | **Drafted; SME review draft** (v0.1): 20 open validation gaps, 12 blocking | [Word PG](ar-collections-learning/01-procedure-guides/TBC-AR%20Collections%20Export%20to%20Excel%20PG%20v0.1.docx) · [Preview](ar-collections-learning/01-procedure-guides/PG-AR-Export-to-Excel-DRAFT.md) · [Screenshots](ar-collections-learning/02-screenshot-registers/PG-AR-Export-to-Excel-Screenshots.md) · [Validation](ar-collections-learning/03-validation/PG-AR-Export-to-Excel-Validation.md) |
| 9 | Review customer notes and activities (*AR Collections Notes and Activities*) | 1 | 1st (#6) | **Drafted; SME review draft** (v0.1): 22 open validation gaps, 15 blocking | [Word PG](ar-collections-learning/01-procedure-guides/TBC-AR%20Collections%20Notes%20and%20Activities%20PG%20v0.1.docx) · [Preview](ar-collections-learning/01-procedure-guides/PG-AR-Notes-and-Activities-DRAFT.md) · [Screenshots](ar-collections-learning/02-screenshot-registers/PG-AR-Notes-and-Activities-Screenshots.md) · [Validation](ar-collections-learning/03-validation/PG-AR-Notes-and-Activities-Validation.md) |
| 2 | Switch between legal entities (*AR Collections Legal Entities*) | 1 | 2nd (#1) | **Drafted; SME review draft** (v0.1): 22 open validation gaps, 13 blocking | [Word PG](ar-collections-learning/01-procedure-guides/TBC-AR%20Collections%20Legal%20Entities%20PG%20v0.1.docx) · [Preview](ar-collections-learning/01-procedure-guides/PG-AR-Legal-Entities-DRAFT.md) · [Screenshots](ar-collections-learning/02-screenshot-registers/PG-AR-Legal-Entities-Screenshots.md) · [Validation](ar-collections-learning/03-validation/PG-AR-Legal-Entities-Validation.md) |
| 3 | Navigate the Customer Credit and Collections workspace (*AR Collections Workspace*) | 1 | 2nd (#2) | **Drafted; SME review draft** (v0.1): 22 open validation gaps, 14 blocking | [Word PG](ar-collections-learning/01-procedure-guides/TBC-AR%20Collections%20Workspace%20PG%20v0.1.docx) · [Preview](ar-collections-learning/01-procedure-guides/PG-AR-Workspace-DRAFT.md) · [Screenshots](ar-collections-learning/02-screenshot-registers/PG-AR-Workspace-Screenshots.md) · [Validation](ar-collections-learning/03-validation/PG-AR-Workspace-Validation.md) |
| 6 | Review overdue customers (*AR Collections Overdue Customers*) | 1 | 2nd (#3) | **Drafted; SME review draft** (v0.1): 22 open validation gaps, 16 blocking | [Word PG](ar-collections-learning/01-procedure-guides/TBC-AR%20Collections%20Overdue%20Customers%20PG%20v0.1.docx) · [Preview](ar-collections-learning/01-procedure-guides/PG-AR-Overdue-Customers-DRAFT.md) · [Screenshots](ar-collections-learning/02-screenshot-registers/PG-AR-Overdue-Customers-Screenshots.md) · [Validation](ar-collections-learning/03-validation/PG-AR-Overdue-Customers-Validation.md) |
| 8 | Investigate a customer account (*AR Collections Customer Account*) | 1 | 2nd (#4) | **Drafted; SME review draft** (v0.1): 24 open validation gaps, 17 blocking | [Word PG](ar-collections-learning/01-procedure-guides/TBC-AR%20Collections%20Customer%20Account%20PG%20v0.1.docx) · [Preview](ar-collections-learning/01-procedure-guides/PG-AR-Customer-Account-DRAFT.md) · [Screenshots](ar-collections-learning/02-screenshot-registers/PG-AR-Customer-Account-Screenshots.md) · [Validation](ar-collections-learning/03-validation/PG-AR-Customer-Account-Validation.md) |

Project visibility: the [PG Command Centre](https://claude.ai/artifact/G3PMkvp68jSbqULxECehCi) tracks every deliverable, gate and validation gap; its source is in [`command-centre/`](command-centre/).

Shared AR resources:

- [Project context and decisions](ar-collections-learning/05-project-notes/Project-Context-and-Decisions.md)
- [PG content QA checklist](ar-collections-learning/04-quality-assurance/PG-Content-QA-Checklist.md)

## Development gates

Every PG moves through these gates:

`Identified → Source reviewed → Gap validated → Drafted → System tested → SME validated → Process-owner approved → Published`

Higher-risk PGs (settlement, write-offs, customer maintenance, exclusions, payment terms, account transfers) are **not finalised** until their listed gaps are validated.

## Working conventions

**Format**

- Every PG is a Save As copy of the master template, completed according to the authoring guide.
- The Word file is the editable source.
- A Markdown preview sits beside it for review on GitHub. Update the preview after the Word file changes.

**Evidence**

- The supplied source documents are the source of truth for process content.
- No D365 step, label, business rule, approval, owner, role or system behavior is invented.
- Every unconfirmed item gets a stable PG-scoped ID (`VG-01` …) in the PG's validation register, which serves as its question log.
- Each one that affects the text is also a Word review comment on that text.

**Procedure writing (from the template)**

- Action | Description rows, one action per row.
- *Italic* verb; **bold** UI labels and business objects.
- PROCESS START, STEP COMPLETE and PROCESS COMPLETE boundary rows.
- The standard navigation pattern (*Check* the **Entity** → *Click* **Modules**).

**Files**

- Word PGs are named `NNN-Guide Title PG vX.docx`. Until a guide code is assigned, `TBC` replaces `NNN`.
- Companion Markdown files keep their `PG-<Area>-<Task-Name>` names.

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
