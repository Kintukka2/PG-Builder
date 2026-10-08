# PG-Builder

Development workspace for granular **Microsoft Dynamics 365 (D365) Procedure Guides (PGs)** and supporting learning content.

Each PG covers **one** D365 task and its controls. PGs sit inside a learning architecture of modules, knowledge articles, reference guides and business rules.

> **Keep this README current.** Update the status tracker and conventions whenever a PG changes gate, a decision is made, or a new topic starts.

---

## Current focus

| Topic | Folder | Status |
|---|---|---|
| **Accounts Receivable (AR) Collections** | [`ar-collections-learning/`](ar-collections-learning/) | Active. First PG in draft. |
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

Backlog rank and release come from the AR development roadmap. Drafting order follows the recommended first drafting batch.

| Rank | PG | Release | Draft batch | Gate | Files |
|---|---|---|---|---|---|
| 4 | Configure AR Collections Favorites | 1 | 1st (#1) | **Drafted; SME review draft** (v0.2): 30 open validation gaps, 16 blocking | [Word PG](ar-collections-learning/01-procedure-guides/TBC-AR%20Collections%20Favorites%20PG%20v0.2.docx) · [Preview](ar-collections-learning/01-procedure-guides/PG-AR-Configure-Collections-Favourites-DRAFT.md) · [Screenshots](ar-collections-learning/02-screenshot-registers/PG-AR-Configure-Collections-Favourites-Screenshots.md) · [Validation](ar-collections-learning/03-validation/PG-AR-Configure-Collections-Favourites-Validation.md) |
| 5 | Create and save a personalised D365 view | 1 | 1st (#2) | Not started | — |
| 7 | Review customer aged balances | 1 | 1st (#3) | Not started | — |
| 11 | View and download a customer invoice | 2 | 1st (#4) | Not started | — |
| 17 | Export all rows from a D365 grid | 2 | 1st (#5) | Not started | — |
| 9 | Review customer notes and activities | 1 | 1st (#6) | Not started | — |

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
