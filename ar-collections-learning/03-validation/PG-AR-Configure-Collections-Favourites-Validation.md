# Validation Register: Configure AR Collections Favourites in D365

| Field | Value |
|---|---|
| Related PG | [`../01-procedure-guides/PG-AR-Configure-Collections-Favourites-DRAFT.md`](../01-procedure-guides/PG-AR-Configure-Collections-Favourites-DRAFT.md) (v0.2) |
| Related screenshot register | [`../02-screenshot-registers/PG-AR-Configure-Collections-Favourites-Screenshots.md`](../02-screenshot-registers/PG-AR-Configure-Collections-Favourites-Screenshots.md) |
| Last updated | 2026-10-08 |
| Open items | 29 |

This file holds everything that is not yet confirmed for this PG. Nothing in this file may appear in the PG as a confirmed instruction until its status is **Closed** and the PG has been updated.

---

## 1. Review of the baseline draft (source 3.2)

Assessment criteria are from the task brief. Each finding records what changed in v0.2.

### 1.1 Consistency with the wider architecture

| # | Finding | Evidence | Action in v0.2 |
|---|---|---|---|
| C1 | The PG title varies across the sources: "Configure Required AR Favourites" (source 0), "Add required AR pages to Favourites" / "Configure AR Collections favourites" (source 1), "Configure D365 favourites for AR Collections" (source 2), "Configure AR Collections favourites" (source 3.1). | Sources 0, 1, 2, 3.1 | Used the title from the task brief. Final title and ID raised as `VG-22`. |
| C2 | The baseline had no module, release, risk or gate metadata. | Source 1 Module 1 seq 1.5; source 2 rank 4; source 3.1 risk Low | Added a Document status block. |
| C3 | The baseline put **Confirm the active legal entity** in the procedure as Step 2. The source control (source 2) applies "before performing a transaction"; adding favourites is not a transaction, and the effect of legal entity on Favourites is unconfirmed. | Source 2 item 2 control | Moved to Prerequisites, with a pointer to the legal entity PG. Raised `VG-23`. |
| C4 | Related content listed "Review open customer invoices" and "Review customer payment journals". Neither is in the architecture or backlog. | Sources 1, 2 | Removed. Replaced with backlog items, with backlog status shown. |

### 1.2 Completeness

| # | Finding | Action in v0.2 |
|---|---|---|
| P1 | The baseline validation list covered the locations of All customers, Customer payment journal and Open customer invoices, but not **Aged balances**. | Added `VG-03`. |
| P2 | There was no Scope or out-of-scope statement. | Added section 5. |
| P3 | There was no Navigation path section. | Added section 7. Intermediate menu groups are marked as not captured. |
| P4 | The expected system response to selecting a favourite star (visual change) was not stated and is not supported by the source. | Left unstated. Raised `VG-07`. |
| P5 | There was no document control. | Added section 16 placeholders. |

### 1.3 Unnecessary or duplicated content

| # | Finding | Action in v0.2 |
|---|---|---|
| D1 | Each page took two steps: "Locate X" then "Add X". "Locate" is not a user action. This inflated the procedure to 19 steps. | Merged location information into the Description of the add step. Procedure now has 11 steps. |
| D2 | The final result appeared four times: Part 1 expected result, Part 2 expected result, Verification checklist, Final outcome. | Kept short part-level results. One Expected results section and one Verification checklist. |
| D3 | Part 3 Step 19 ("Return to Favourites. Confirm you can access the remaining pages") repeated Steps 17–18. | Removed. |
| D4 | Step 1 "Sign in to D365" is a prerequisite, not part of the task. | Moved to Prerequisites. |
| D5 | The "Drafting approach" note and the screenshot plan were inside the PG body. | Moved to the screenshot register and project notes. |

### 1.4 Unsupported procedural claims

| # | Baseline claim | Why it is unsupported | Action in v0.2 |
|---|---|---|---|
| U1 | Troubleshooting: "Use the module menu to search for the page name." | No source shows a module-menu search. | Removed. Raised `VG-15`. |
| U2 | Troubleshooting: "Check whether its favourite star is selected." | Star state indicators are not shown in the source. The recording has pre-existing favourites. | Kept as a flagged draft action. Raised `VG-07`. |
| U3 | Troubleshooting: "Clear its selected favourite star" to remove a favourite. | Removal is not demonstrated. | Removed. Raised `VG-14`. |
| U4 | Page usage: **All customers** gives access to "customer transactions, statements, contact information and customer-level collection settings". | Only opening customer accounts and customer master details is supported by the architecture (source 1 seq 4.1; source 2 item 21). The starting page for statements and collection settings is not stated. | Reduced to supported wording. |
| U5 | Page usage: **Aged balances** gives access to "customer collection activities". | Not supported by sources 0–3.1. | Removed. Raised `VG-20`. |
| U6 | Page usage: **Open customer invoices**, "Review open customer invoices and related transaction details". | Supported only by the baseline draft's own statement. | Reduced to "Reviewing open customer invoices". Raised `VG-19`. |
| U7 | Step 16: Favourites is "the star icon". | Only the baseline states this. | Kept as a validation item only. Raised `VG-09`. |
| U8 | "Follow the approved access-support process." | No process is defined in the sources. | Kept as an explicit placeholder. Raised `VG-16`. |

### 1.5 Terminology consistency

See section 3, Terminology register. Main issues: **Aged balances** / **Age balances** (`VG-01`), **Favourites** / **Favorites** (`VG-28`), and **Credit and collections** (module) / **Customer Credit and Collections** (workspace) / "Credit & Collections" (source 0) (`VG-21`).

### 1.6 Suitability as a granular PG

- The baseline was close to granular. The main issue was step padding (D1).
- v0.2 keeps one outcome, with four parts: open module, add pages, add the Accounts receivable page, verify.
- Business-rule content (why each page matters) is kept to the Pages to add table, separate from system instructions.
- No business rules or approvals apply to this task in the source material.

### 1.7 Usability for a new AR Collections user

- Navigation paths were added so a learner can orient themselves before starting.
- The **Modules** icon description (three dots with horizontal lines) comes from the trainer and is kept. The icon still needs a visual check (`VG-08`).
- Troubleshooting was restructured into Issue / Possible causes / What to do. Security access is presented only as a possible cause.
- The learner is not told anything about persistence or legal-entity scope. This avoids an unvalidated expectation.

---

## 2. Validation gap register

**Priority:** **B** = blocks publication. **N** = non-blocking (publish with the item excluded or worded neutrally).

**Resolution method:** **Test** = D365 system test in a clean session. **Rec** = recording review. **SME** = subject-matter expert or process owner. **Dec** = project decision.

| ID | Item to confirm | Raised from | Affects (PG section/step) | Priority | Method | Owner | Status |
|---|---|---|---|---|---|---|---|
| VG-01 | Exact label: **Aged balances** or **Age balances**. | Source 0 uses "Age Balances"; sources 1, 2, 3.1, 3.2 use "Aged balances". | §7, §8, Step 4, §11, Fig 4 | B | Test, Rec | [TBC] | Open |
| VG-02 | Exact location (menu group or submenu) of **All customers** within **Credit and collections**. | Baseline validation list | §7, Step 3, Fig 3 | B | Test | [TBC] | Open |
| VG-03 | Exact location (menu group or submenu) of **Aged balances** within **Credit and collections**. | Missing from baseline (finding P1) | §7, Step 4, Fig 4 | B | Test | [TBC] | Open |
| VG-04 | Exact location of **Customer payment journal**. Confirm it is reached from **Credit and collections**. | Baseline validation list | §7, Step 5, Fig 5 | B | Test, Rec | [TBC] | Open |
| VG-05 | Exact location of **Open customer invoices** within **Accounts receivable**. | Baseline validation list | §7, Step 8, Fig 7 | B | Test | [TBC] | Open |
| VG-06 | Whether a submenu must be expanded before the favourite star is available. Whether the star is always visible or only on hover. | Baseline validation list | Steps 3–5, 8 | B | Test | [TBC] | Open |
| VG-07 | Star appearance before and after selection (the expected system response). Whether selecting a star that is already selected removes the favourite. If it does, add a confirmed warning before Steps 3 and 8 and finalise troubleshooting row 3. | Findings P4, U2. Pre-existing favourites in the recording. | Part 2 and Part 3 warning placeholders; §12 row 3; Figs 3–5, 7 | B | Test | [TBC] | Open |
| VG-08 | Appearance and label or tooltip of the **Modules** icon. The trainer describes it as three dots with horizontal lines. | Source 3.2 Step 3 | Step 1, Fig 1 | N | Test, Rec | [TBC] | Open |
| VG-09 | Appearance and label or tooltip of the **Favourites** icon. The baseline says it is a star icon. | Finding U7 | Step 9, Fig 8 | N | Test, Rec | [TBC] | Open |
| VG-10 | Whether Favourites are retained across legal entities. | Baseline validation list; task evidence rules | §6, §10, §12 row 4 | N (kept out of PG) | Test | [TBC] | Open |
| VG-11 | Whether Favourites persist between sessions, browsers and devices. | Baseline validation list; task evidence rules | §10, §12 row 4 | N (kept out of PG) | Test | [TBC] | Open |
| VG-12 | How to display the navigation pane if it is hidden or collapsed. | Prerequisite in baseline with no method | §6 | N | Test | [TBC] | Open |
| VG-13 | Order in which favourites are listed (for example, order added or alphabetical). | Needed to describe the expected result | Step 10, §10, Fig 8 | N | Test | [TBC] | Open |
| VG-14 | How to remove a favourite. | Finding U3 | §5, §12 row 5 | N | Test | [TBC] | Open |
| VG-15 | Whether the module menu or navigation pane has a search or filter for page names. | Finding U1 | §12 | N | Test | [TBC] | Open |
| VG-16 | The approved access-support process and its owner, for missing modules or pages. | Finding U8 | §12 rows 1–2 | B | SME | [TBC] | Open |
| VG-17 | Test the procedure with the standard AR Collections security role, and confirm the role name. | Baseline validation list; publication gate | Whole PG, §16 | B | Test, SME | [TBC] | Open |
| VG-18 | The purpose of **Customer payment journal** for AR Collections users. Do not expand beyond "required favourite" until confirmed. | Source 3.2 page usage note | §8 | N | SME, Rec | [TBC] | Open |
| VG-19 | Wording for the purpose of **Open customer invoices**, checked against the recording. | Finding U6 | §8 | N | Rec | [TBC] | Open |
| VG-20 | Baseline claim that **Aged balances** gives access to customer collection activities. | Finding U5 | §8 (removed) | N | Rec, SME | [TBC] | Open |
| VG-21 | Label distinction between the **Credit and collections** module and the **Customer Credit and Collections** workspace. Also source 0's "Credit & Collections". | Terminology review | §5, §7, §13, Fig 2 | N | Test | [TBC] | Open |
| VG-22 | PG ID and final title. Source 0 proposes `PG-AR-010`, but its numbering does not match the roadmap ranks. | Finding C1 | §1, §2, file name | B | Dec | [TBC] | Open |
| VG-23 | Whether the active legal entity affects this task. This decides whether it stays a prerequisite. Linked to `VG-10`. | Finding C3 | §6 | N | Test | [TBC] | Open |
| VG-24 | Clean publication screenshots captured in a clean D365 session. The recording shows pre-existing favourites. | Source 3.2 recording limitation | All figures | B | Test | [TBC] | Open |
| VG-25 | SME validation, a test by someone other than the author, and process-owner approval. | Publication gate (source 1 §4) | Whole PG | B | SME | [TBC] | Open |
| VG-26 | D365 environment name or URL and sign-in method to reference in Prerequisites. Not in the sources. | Baseline Step 1 | §6 | N | SME | [TBC] | Open |
| VG-27 | Masking policy for the legal entity name, user name or initials in the D365 header, and any customer data visible behind menus. | Task privacy rule; capture standards (source 2) | All figures | B | Dec, SME | [TBC] | Open |
| VG-28 | UI spelling in the users' D365 language setting: **Favourites** or **Favorites**. The PG must match the screen exactly. | Terminology review | Title, §3, Step 9, §11 | B | Test | [TBC] | Open |
| VG-29 | Whether any of the four pages also appears in another module, and whether favouriting it there creates the same favourite. Supports the "do not substitute a similarly named page" guidance. | Baseline troubleshooting | §12 row 2 | N | Test | [TBC] | Open |

**Summary:** 29 open.

- **Blocking (14):** VG-01, 02, 03, 04, 05, 06, 07, 16, 17, 22, 24, 25, 27, 28.
- **Non-blocking (15):** VG-08 to 15, 18 to 21, 23, 26, 29.

---

## 3. Terminology register

| Term used in PG | Variants in sources | Decision | Status |
|---|---|---|---|
| **Aged balances** | "Age Balances", "Age balances" (source 0); "Aged balances" (sources 1, 2, 3.1, 3.2) | Use **Aged balances** (majority of sources and baseline) until `VG-01` closes. | Provisional |
| **Favourites** | "favourites", "Favourites" (all sources); possible UI label "Favorites" | Use **Favourites** for the UI label and "favourite" for the noun and verb in prose, until `VG-28` closes. | Provisional |
| **Credit and collections** (module) | "Credit & Collections" (source 0) | Use **Credit and collections** for the module. | Provisional (`VG-21`) |
| **Customer Credit and Collections workspace** | "Customer Credit & Collections workspace" (source 0); "Credit & Collections Workspace" (source 0) | Use only when referring to the workspace. Not used in this PG's steps. | Provisional (`VG-21`) |
| **All customers** | "All Customers" (source 0) | Sentence case per sources 1, 2, 3.1, 3.2. | Provisional |
| **Customer payment journal** | "Customer Payment Journal" (source 0) | Sentence case per later sources. | Provisional |
| **Open customer invoices** | "Open Customer Invoices" (source 0) | Sentence case per later sources. | Provisional |
| **Modules** | — | As in source 3.2. | Provisional (`VG-08`) |
| **navigation pane** | "side navigation" (source 3.2 screenshot plan) | Use "navigation pane". | Provisional |
| favourite star | "favourite star", "its favourite star" (source 3.2) | Use "favourite star". The exact control name is unconfirmed. | Provisional (`VG-07`) |
| legal entity | "ledger", "business", "company" (source 0) | Use "legal entity". Keep the other terms for the legal entity PG and its glossary. | Provisional |

---

## 4. Publication gate status (source 1 §4)

| Gate check | Status for this PG |
|---|---|
| The task name matches the current D365 label | Open (`VG-22`, `VG-28`) |
| The starting navigation path is documented | Partial (`VG-02` to `VG-06`) |
| The correct legal entity requirement is stated | Partial (`VG-10`, `VG-23`) |
| Preconditions and required access are defined | Partial (`VG-17`, `VG-26`) |
| Every user action is captured in sequence | Drafted; not tested |
| Fields, buttons, tabs and options use exact system labels | Open (`VG-01`, `VG-08`, `VG-09`, `VG-28`) |
| Decision points and alternative paths are documented | Drafted (Step 6 conditional) |
| Business rules are separated from system instructions | Met (none apply) |
| Warnings appear immediately before the risky action | Open (`VG-07`) |
| Expected system outcomes are documented | Partial (`VG-07`, `VG-13`) |
| Verification steps are included | Met |
| Error and recovery steps are included | Partial (`VG-07`, `VG-14`, `VG-16`) |
| Escalation conditions and owner are confirmed | Open (`VG-16`) |
| Screenshots represent the current interface | Open (`VG-24`) |
| Live customer details are removed from screenshots | Open (`VG-27`) |
| Cross-system impacts are validated | Not applicable (none identified) |
| Approval requirements are confirmed | Not applicable to the task. Publication approval is open (`VG-25`). |
| The PG has been tested by someone other than the author | Open (`VG-25`) |
| The process owner has approved publication | Open (`VG-25`) |
| Related learning modules, references and PGs are cross-linked | Partial (linked PGs not yet drafted) |

---

## 5. Change log

| Date | Change |
|---|---|
| 2026-10-08 | Register created from the review of baseline draft v0.1 (source 3.2). |
