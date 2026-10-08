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

## Repository structure

Each topic has its own folder with the same internal structure:

```
<topic>-learning/
  01-procedure-guides/       PG working drafts (one file per PG)
  02-screenshot-registers/   Figure-to-step mapping, timestamps, captions, callouts
  03-validation/             Validation-gap registers, baseline reviews, terminology
  04-quality-assurance/      QA checklists applied before review and publication
  05-project-notes/          Project context, source summary, decisions log
```

## AR Collections: PG status tracker

Backlog rank and release come from the AR development roadmap. Drafting order follows the recommended first drafting batch.

| Rank | PG | Release | Draft batch | Gate | Files |
|---|---|---|---|---|---|
| 4 | Configure AR Collections Favourites in D365 | 1 | 1st (#1) | **Drafted** (v0.2): 29 open validation gaps, 14 blocking | [PG](ar-collections-learning/01-procedure-guides/PG-AR-Configure-Collections-Favourites-DRAFT.md) · [Screenshots](ar-collections-learning/02-screenshot-registers/PG-AR-Configure-Collections-Favourites-Screenshots.md) · [Validation](ar-collections-learning/03-validation/PG-AR-Configure-Collections-Favourites-Validation.md) |
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

**Evidence**

- The supplied source documents are the source of truth.
- No D365 step, label, business rule, approval requirement or system behaviour is invented.
- Anything unconfirmed is recorded as a validation gap with a PG-scoped ID (`VG-01`, `VG-02` …) in the PG's validation register.
- Unconfirmed items are never written as confirmed instructions.

**Procedure writing**

- Numbered steps in Step / Action / Description tables.
- One user action per step.
- **Bold** interface labels.
- Warnings go immediately before the consequential action.
- Business rules are kept separate from system instructions.

**Files**

- PG files are named `PG-<Area>-<Task-Name>-DRAFT.md` until a PG ID scheme is decided.
- Companion files share the same task name.

**Screenshots**

- Figures are numbered per PG and mapped in the screenshot register.
- Customer information is always masked.
- Publication screenshots are captured in a clean D365 session.

**Language**

- Prose uses UK/AU English.
- UI labels match the D365 screen exactly.

## Source material

Source documents for each topic are held outside this repository and are not modified. They are listed in each topic's `05-project-notes/Project-Context-and-Decisions.md`.
