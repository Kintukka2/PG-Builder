# Project Context and Decisions: AR Collections Learning

| Field | Value |
|---|---|
| Topic | D365 Accounts Receivable (AR) Collections |
| Last updated | 2026-10-08 |
| Current focus | First PG: *Configure AR Collections Favourites in D365* |

This file records the project context drawn from the source documents, inconsistencies found between them, and decisions made during development. Update it whenever a decision is made or a source is added.

---

## 1. Source documents

The source documents are the source of truth for this topic. They are held outside this repository and must not be overwritten.

| Ref | File | Content | Primary use |
|---|---|---|---|
| 0 | `0. Recommended Learning Structure.txt` | Three-layer learning structure. Inventory of 27 topics with documentation readiness. Proposed PG IDs `PG-AR-001` to `PG-AR-022`. Biggest information gaps. | Topic inventory and initial readiness |
| 1 | `1. Prioritised learning architectur.txt` | P1–P4 priority definitions. Modules 1–12 with learning outcomes, sequences, deliverable types and readiness. Recommended development sequence. Gap-validation checklist (A–L). Publication gate. | Learning architecture, publication gate |
| 2 | `2. D365 AR learning development roadmap.txt` | Release 1–4 roadmap. 32-item prioritised master backlog. Cross-release workstreams (screenshots, business rules, references, assurance). Development gates. Definitions of ready. | Delivery roadmap and gates |
| 3.1 | `3.1 Recommended first drafting batch.txt` | First drafting batch (6 PGs), second batch hold list, "do not draft as final" list. | Drafting order |
| 3.2 | `3.2 Configure AR Collections Favour.txt` | Baseline draft v0.1 of the Favourites PG. Screenshot plan with timestamps, captions and callouts. | Baseline for the first PG |

The underlying evidence for all sources is the *AR Training D365* session recording and transcript.

---

## 2. Project objective

Build a role-based AR Collections learning pathway in D365. It is made of granular Procedure Guides (PGs) and supporting learning content. It enables learners to:

1. Navigate the correct D365 environment.
2. Identify and prioritise collection work.
3. Investigate customer accounts.
4. Contact customers and record collection activity.
5. Process allocations and settlements.
6. Perform controlled financial adjustments.
7. Maintain customer information and manage exceptions.

(Source 2, roadmap objective.)

Each PG covers **a single granular D365 task and its associated controls**. Learning modules stay learner-focused (source 1).

## 3. Intended audience

- **Primary:** New AR Collections users (Collections officers) learning to perform routine AR Collections work in D365.
- **Entry point:** Release 1 gives a new AR Collections user enough capability to enter the correct legal entity, configure their workspace, review overdue accounts, investigate a customer and record collection activity (source 2).
- **Out of scope for this audience until confirmed:** Direct debit and credit card administration. These were explicitly excluded from the training session (source 1, checklist L).

## 4. Learning architecture

### 4.1 Content types (source 0)

- Learning modules
- Procedure Guides (PGs)
- Knowledge articles
- Reference guides
- Business rules

Source 1 also uses: system overview, guided practice, microlearning, knowledge note or lesson, decision aid, template and critical control.

### 4.2 Three-layer structure (source 0)

| Layer | Focus |
|---|---|
| Learning Module 1: D365 AR Collections Fundamentals | Legal entities, workspaces, Credit and Collections workspace, Favourites and personalisation, views, customer navigation |
| Learning Module 2: AR Collections Operations | Overdues, activities, accounts, transactions, statements, ageing, settlement, allocation, unallocated payments, write-offs, notes, exclusions, maintenance, reporting |
| Learning Module 3: Advanced AR Administration | Customer master, contacts, addresses, letter and statement controls, payment terms, D365 ↔ CargoWise synchronisation, journal approval workflow |

### 4.3 Prioritised modules (source 1)

| Priority | Definition | Modules |
|---|---|---|
| P1 | Day-one capability. Needed before a user can safely begin routine AR work. | 1 Navigate the AR Collections environment; 2 Configure D365 for efficient AR work |
| P2 | Core operational capability. Needed to manage collections and allocations independently. | 3 Review the AR collections workload; 4 Investigate a customer account; 5 Record and manage collection activity; 6 Generate customer documents; 7 Investigate unallocated payments; 8 Settle customer transactions |
| P3 | Controlled financial processing. Higher-risk tasks involving settlement, write-offs or approvals. | 9 Process customer write-offs |
| P4 | Administration and exceptions. Less frequent work needing more business knowledge or validation. | 10 Maintain customer contact and address details; 11 Manage customer collection controls; 12 Reference, reporting and data extraction |

The Favourites PG sits in **Module 1, sequence 1.5** ("Add required AR pages to Favourites"). It is supported by **1.6**, a guided practice that opens each of the four pages.

## 5. Development priorities

### 5.1 Releases (source 2)

| Release | Goal | Backlog ranks |
|---|---|---|
| 1 | Minimum viable AR Collections pathway | 1–10 (orientation, legal entities, workspace, favourites, views, overdues, aged balances, account investigation, notes and activities, record activity) |
| 2 | Payment, settlement and customer documents | 11–17 |
| 3 | Financial controls and customer administration | 18–25 |
| 4 | Exceptions and specialist processes | 26–32 |

### 5.2 Drafting order (source 3.1)

**First batch:**

1. Configure AR Collections favourites ← **in progress**
2. Create and save a personalised D365 view
3. Review customer aged balances
4. View and download a customer invoice
5. Export all rows from a D365 grid
6. Review customer notes and activities

**Second batch (limited validation needed):** switch legal entities, navigate the workspace, review overdue customers, investigate a customer account, record a collection activity, preview and download a statement, generate and send a statement.

**Do not draft as final:** settle or undo transactions, write-offs, write-off journal submission, customer contact or address maintenance, customer exclusions, payment terms, parent-child fund transfers, direct debit and credit cards.

## 6. Draft-ready vs validation-blocked content

| Category | Meaning | Rule |
|---|---|---|
| **Ready to draft** | Meets the definition of ready for drafting (source 2): clear task boundary, known starting path, actions demonstrated, exact labels available, gaps recorded, module assigned. | May be drafted. Gaps go into the validation register. |
| **Draft ready, publication blocked** | Can be drafted from the recording, but has unresolved business rules, approvals or cross-system effects. Examples: unallocated payments, write-offs, contact maintenance. | Draft only as a working draft. Do **not** finalise until the listed gaps are validated. |
| **System steps ready, governance blocked** | The system steps are demonstrated, but reasons, approvals, documentation or review controls are missing. Example: exclude from credit management. | Same as above. |
| **Partial / Not ready** | The process was discussed but not demonstrated in enough detail. Examples: parent-child transfers, bank statements, payment terms. | Do not draft a PG. Collect evidence first (SME playback or a new recording). |
| **Ready for publication** | Meets the definition of ready for publication and passes the 20-point publication gate (sources 1 and 2). | May be published after process-owner approval. |

Development gates (source 2): Identified → Source reviewed → Gap validated → Drafted → System tested → SME validated → Process-owner approved → Published.

---

## 7. Source inconsistencies identified

| # | Inconsistency | Sources | Working position |
|---|---|---|---|
| I-01 | Readiness ratings differ. Source 0 marks write-offs, customer master maintenance, synchronisation and exclusions as "✅ Yes". Sources 1, 2 and 3.1 mark them as publication-blocked or partial. | 0 vs 1, 2, 3.1 | The stricter, later assessment governs (D-004). |
| I-02 | Release placement differs. Source 1's "Release 1" includes statements, unallocated payments and settlement. Source 2 puts these in Release 2. | 1 vs 2 | Source 2 governs release packaging (D-004). |
| I-03 | Drafting order differs from backlog rank. Source 3.1 drafts some Release 2 items (invoice, export) before Release 1 items (legal entities, workspace). | 2 vs 3.1 | Source 3.1 governs drafting order. Source 2 governs release packaging (D-005). |
| I-04 | PG IDs. Source 0 numbers PGs `PG-AR-001` to `022` in topic order (Favourites = `PG-AR-010`). This does not match the source 2 backlog ranks (Favourites = rank 4). | 0 vs 2 | ID scheme not yet decided (D-006). |
| I-05 | "Age Balances" (source 0) vs "Aged balances" (sources 1, 2, 3.1, 3.2). | 0 vs others | "Aged balances" is provisional. Validate (`VG-01`). |
| I-06 | "Credit & Collections" (source 0) vs "Credit and collections" (module) vs "Customer Credit and Collections" (workspace). | 0, 1, 2, 3.2 | Module and workspace are kept distinct. Validate (`VG-21`). |
| I-07 | The Favourites PG title varies across all five sources. | 0, 1, 2, 3.1, 3.2 | Title from the task brief is used (D-002). |
| I-08 | Source 0 lists "Persist Views Across Legal Entities" as covered. Source 1 marks view scope "Ready with validation". Source 3.1 says to phrase it exactly as demonstrated and validate it. | 0 vs 1, 3.1 | Treat as a validation item in the Views PG. Do not carry it into the Favourites PG. |

---

## 8. Decisions log

| ID | Date | Decision | Rationale | Status |
|---|---|---|---|---|
| D-001 | 2026-10-08 | The attached source documents are the source of truth. No D365 steps, labels, business rules, approvals or behaviour are added without evidence. Anything uncertain becomes a `VG-xx` validation gap. | Task brief evidence rules | Adopted |
| D-002 | 2026-10-08 | Working title for the first PG: **Configure AR Collections Favourites in D365**. | Task brief; reconciles I-07 | Adopted (final title under `VG-22`) |
| D-003 | 2026-10-08 | Folder structure: `01-procedure-guides`, `02-screenshot-registers`, `03-validation`, `04-quality-assurance`, `05-project-notes`, under a topic folder (`ar-collections-learning`). | Task brief | Adopted |
| D-004 | 2026-10-08 | Where readiness or release placement conflicts, the later and stricter assessment governs (sources 1 and 2 over source 0). | Conservative publication control | Adopted |
| D-005 | 2026-10-08 | Source 3.1 governs drafting order. Source 2 governs release packaging. | I-03 | Adopted |
| D-006 | 2026-10-08 | PG ID scheme to be decided. Option A: keep source 0 IDs (`PG-AR-010`). Option B: renumber to the source 2 backlog rank. Until decided, files use descriptive names (`PG-AR-<Task-Name>`). | I-04 | **Open** |
| D-007 | 2026-10-08 | Validation gaps use IDs scoped to each PG (`VG-01`…). Each PG has its own validation register. | Traceability | Adopted |
| D-008 | 2026-10-08 | Figures are numbered per PG and mapped to steps in a separate screenshot register. The PG holds placeholders until frames are approved. | Task brief | Adopted |
| D-009 | 2026-10-08 | Working format is editable Markdown. Prose uses UK/AU English. UI labels match the D365 screen exactly. | Task brief; source spelling | Adopted (UI spelling under `VG-28`) |
| D-010 | 2026-10-08 | Legal entity confirmation is a **prerequisite**, not a procedure step, in non-transactional PGs. It stays a procedure step in transactional PGs (source 2 control). | Source 2 control applies "before performing a transaction" | Proposed |
| D-011 | 2026-10-08 | Do not create separate "Locate X" steps. Location information goes in the Description of the action step. | One-action-per-step rule; finding D1 | Proposed for template |
| D-012 | 2026-10-08 | Recording frames confirm locations. Publication screenshots are recaptured in a clean session unless a frame fully supports the step. | Pre-existing favourites in recording | Adopted |

---

## 9. Proposed reusable PG template elements

These elements came from the Favourites PG. They are candidates for the standard PG template, to confirm after the second PG (*Create and save a personalised D365 view*) tests them against a more complex task.

1. **Draft banner.** A "DRAFT — NOT FOR PUBLICATION" notice that points to the validation notes.
2. **Document status block.** PG ID, version, status, development gate, learning module and sequence, release and backlog rank, risk rating, evidence source with timestamp range, last updated.
3. **The 16-section structure** from the task brief.
4. **Scope table** with in-scope bullets and an out-of-scope table that points to where each topic is covered.
5. **Prerequisites** in the standard order: sign-in, legal entity (with its D-010 placement), module or page access, interface state. Includes a standard security-access note phrased as a possibility.
6. **Navigation path table** (Page | Path), with a standard note when intermediate menu groups are not captured.
7. **Procedure in parts.** Each part has a short heading and a Step / Action / Description table. Steps are numbered continuously across parts. Each part ends with a one-line **Part result**.
8. **Step-writing rules.** One action per step, starting with a verb. **Bold** UI labels. Location in the Description. Expected system response only where supported. VG IDs inline.
9. **Figure placeholder block.** `> **[Figure n placeholder]** <caption text>. See screenshot register.`, placed directly after its step.
10. **Warning placeholder block.** For warnings that depend on an unresolved VG item, placed immediately before the consequential step.
11. **Expected results** with a "Not yet confirmed" line for excluded behaviour.
12. **Verification checklist** using Markdown checkboxes.
13. **Troubleshooting table.** Issue | Possible causes | What to do, with standard rows: missing module, missing page, action did not take effect. Includes the standard "do not substitute a similarly named page" guidance.
14. **Related learning content table.** Item | Type | Backlog status.
15. **Draft validation notes** grouped by theme (labels, locations, behaviour, persistence, purpose, access and governance, screenshots), linked to a full validation register.
16. **Companion files** for each PG: screenshot register (summary table, per-figure detail, recapture specification) and validation register (baseline review, VG register, terminology register, publication gate status).
17. **Document control.** Roles, test context (D365 version, security role, legal entity) and version history.

## 10. Next steps

1. Review the Favourites PG v0.2 and close or confirm the blocking VG items, starting with a clean-session D365 test (`VG-01` to `VG-07`, `VG-17`, `VG-24`, `VG-28`).
2. Review the recording frames listed in the screenshot register and update each figure's status.
3. Decide D-006 (PG ID scheme) and the screenshot masking policy (`VG-27`).
4. Then start the second first-batch PG, *Create and save a personalised D365 view*, using the proposed template elements, and refine the template from it.
