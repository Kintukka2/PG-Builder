# Validation Register: Configure AR Collections Favorites

| Field | Value |
|---|---|
| Related PG (editable source) | [`../01-procedure-guides/TBC-AR Collections Favorites PG v0.2.docx`](../01-procedure-guides/TBC-AR%20Collections%20Favorites%20PG%20v0.2.docx) |
| Markdown preview | [`../01-procedure-guides/PG-AR-Configure-Collections-Favourites-DRAFT.md`](../01-procedure-guides/PG-AR-Configure-Collections-Favourites-DRAFT.md) |
| Related screenshot register | [`../02-screenshot-registers/PG-AR-Configure-Collections-Favourites-Screenshots.md`](../02-screenshot-registers/PG-AR-Configure-Collections-Favourites-Screenshots.md) |
| Last updated | 2026-10-08 |
| Items | 33 total: 30 open (16 blocking, 14 non-blocking), 1 deferred, 2 withdrawn |

This file is the **question log** that the PG Template Authoring Guide asks for. It is kept separate from the PG. Nothing in it may appear in the PG as confirmed guidance until its status is **Closed** and the Word file has been updated.

- **IDs are stable.** `VG-xx` serves as the guide's `Qxx` question ID. IDs are never renumbered or reused (decision D-016).
- **Word comments.** In the Word guide, each open item that affects the text is a review comment by "Validation register" (VR), anchored to the affected text. The *Word comment* column below gives the comment number.

---

## 1. Review of the baseline draft (source 3.2)

Assessment criteria are from the original task brief. These findings shaped v0.2 and still apply after the template conversion.

### 1.1 Consistency with the wider architecture

| # | Finding | Action |
|---|---|---|
| C1 | The PG title varies across all five sources. | Title held open (`VG-22`). The Word guide uses process name "AR Collections Favorites" and topic "Configure AR Collections Favorites" (D-014). |
| C2 | The baseline had no module, release, risk or gate metadata. | Recorded in this repo (README tracker and project notes). The Word template has no field for it, so it is kept out of the PG. |
| C3 | Legal entity confirmation was in the baseline as a procedure step. Its effect on Favorites is unconfirmed. | v0.2 Markdown made it a prerequisite. The template's standard navigation pattern restores it as Step 1, **Check the Entity** (D-015). Raised `VG-23`. |
| C4 | Related content listed PGs that are not in the backlog. | Removed. The template has no Related content section. Out-of-scope topics are named in the Part Description. |

### 1.2 Completeness

| # | Finding | Action |
|---|---|---|
| P1 | The baseline validation list omitted the location of **Aged balances**. | Added `VG-03`. |
| P2 | There was no scope statement. | Scope and exclusions are now in the Part Description. |
| P3 | There was no navigation path. | Covered by procedure steps 2–3 and 7–8, and the Key concepts table. Intermediate menu groups are not captured (`VG-02` to `VG-05`). |
| P4 | The expected response to clicking the star was unsupported. | Each step states only that the page is added to Favorites. Star appearance is `VG-07`. |
| P5 | There was no document control. | The template's version history is used. |

### 1.3 Unnecessary or duplicated content

| # | Finding | Action |
|---|---|---|
| D1 | Separate "Locate X" steps were not user actions. | Location is now in the Description column. |
| D2 | The final result was stated four times. | Stated once, in the PROCESS COMPLETE row. |
| D3 | Steps 17–19 overlapped. | Steps 11–12 now cover confirming the list and opening a page. |
| D4 | "Sign in" was a procedure step. | Now in PROCESS START prerequisites. |
| D5 | Drafting notes and the screenshot plan were in the PG body. | Moved to companion files. |

### 1.4 Unsupported claims (all removed from the PG)

| # | Baseline claim | Status |
|---|---|---|
| U1 | The module menu has a search for page names. | Removed. `VG-15` withdrawn (no Troubleshooting section). |
| U2 | Check whether the favorite star is selected. | Removed. `VG-07`. |
| U3 | Clear the star to remove a favorite. | Removed. `VG-14` deferred. |
| U4 | All customers gives access to statements, transactions and collection settings. | Reduced to supported wording. |
| U5 | Aged balances gives access to collection activities. | Removed. `VG-20`. |
| U6 | Open customer invoices: "related transaction details". | Reduced. `VG-19`. |
| U7 | Favorites is a star icon. | Not stated. `VG-09`. |
| U8 | "Approved access-support process." | Replaced with the template's D365 issue form route, pending `VG-16`. |

### 1.5 Terminology, granularity and usability

See section 4, Terminology register. The guide is a single standalone topic with one procedure table, which fits the template's *Standalone topic* pattern. Steps keep to one action each. Navigation follows the template's standard pattern.

---

## 2. Template conversion review (v0.2 Markdown → PG master template)

Changes made to follow `PG_Template_Authoring_Guide_v1.docx`:

| # | Template rule | Effect on this PG |
|---|---|---|
| T1 | Text is in English (United States). Exact UI labels are preserved. | Prose now uses US spelling: *favorites*, *personalized*, *aging*. The UI label **Favorites** is used provisionally until `VG-28` closes. |
| T2 | Fixed structure: cover, contents, version history, About this guide, Parts 1–3, Additional Resources. | The 16-section provisional structure is retired (D-013). |
| T3 | Choose standalone, parent with subtopics, or off-system for each topic. | Standalone topic. The other two template examples were removed. |
| T4 | Action \| Description rows, italic verb, bold UI labels, native numbering. | 12 numbered rows, between PROCESS START and PROCESS COMPLETE boundary rows. |
| T5 | Use the standard navigation pattern: Check the Entity, then Click Modules. | Added as Steps 1–2. Step 1 is anchored to `VG-23`. |
| T6 | Part 3 Reports is mandatory. Write "No applicable reports" only after explicit SME confirmation. | Part 3 kept, marked as pending SME confirmation (`VG-32`). |
| T7 | Do not add Troubleshooting or Keywords sections. | Troubleshooting removed. Its one supported route (D365 issue form) moved to Step 11. `VG-15` and `VG-29` withdrawn. `VG-14` deferred. |
| T8 | Screenshots are optional, and no placeholders are allowed in a clean guide. | No figures in the Word guide. The screenshot register is retained for the decision on which figures add value (D-017). |
| T9 | Keep working notes and the question log out of the PG. | Validation notes are now Word comments plus this register. |
| T10 | Do not invent an owner, approval or role. | BPO reads "To be confirmed" (`VG-33`). Stream and role labels are flagged (`VG-31`). |

---

## 3. Validation gap register

**Priority:** **B** = blocks publication. **N** = non-blocking.

**Method:** **Test** = D365 test in a clean session. **Rec** = recording review. **SME** = subject-matter expert or process owner. **Dec** = project decision.

| ID | Item to confirm | Location in Word guide | Word comment | Priority | Method | Status |
|---|---|---|---|---|---|---|
| VG-01 | Menu label: **Aged balances** or **Age balances**. Source 0 uses "Age Balances". | Key concepts (pages table); Step 5 | 4, 13 | B | Test, Rec | Open |
| VG-02 | Menu group or submenu for **All customers** in **Credit and collections**. | Step 4 | 11 | B | Test | Open |
| VG-03 | Menu group or submenu for **Aged balances** in **Credit and collections**. | Step 5 | 13 | B | Test | Open |
| VG-04 | Confirm **Customer payment journal** is available in **Credit and collections**, and its menu location. | Step 6 | 14 | B | Test, Rec | Open |
| VG-05 | Menu group or submenu for **Open customer invoices** in **Accounts receivable**. | Step 9 | 15 | B | Test | Open |
| VG-06 | Whether a submenu must be expanded first, and whether the star is always visible or only on hover. | Steps 4–6, 9 | 11 | B | Test | Open |
| VG-07 | Star appearance before and after it is clicked. Whether clicking a selected star removes the favorite. If it does, add a warning before Steps 4–6 and 9. | Steps 4–6, 9 | 12 | B | Test | Open |
| VG-08 | **Modules** icon and its label or tooltip. The trainer describes it as three dots with horizontal lines. | Step 2 | 10 | N | Test, Rec | Open |
| VG-09 | **Favorites** icon and its label or tooltip. | Step 10 | 16 | N | Test, Rec | Open |
| VG-10 | Whether favorites are the same across legal entities. | Step 1; PROCESS COMPLETE | 9, 18 | N | Test | Open |
| VG-11 | Whether favorites persist between sessions, browsers and devices. | PROCESS COMPLETE | 18 | N | Test | Open |
| VG-12 | How to show the **Navigation Pane** if it is hidden or collapsed. | PROCESS START | 8 | N | Test | Open |
| VG-13 | Order in which favorites are listed. | Step 11 | 17 | N | Test | Open |
| VG-14 | How to remove a favorite. | Not in guide | — | N | Test | **Deferred.** Out of scope for this guide; revisit if a removal topic is needed. |
| VG-15 | Whether the module menu has a search or filter. | — | — | — | — | **Withdrawn.** Only needed for the removed Troubleshooting section (T7). |
| VG-16 | Whether the D365 issue form is the correct route when a module or page is not available. | Step 11 | 17 | B | SME | Open. Candidate route identified from the template's User Support block. |
| VG-17 | The security role that grants access to these modules and pages, and a test with it. | PROCESS START | 7 | B | Test, SME | Open |
| VG-18 | What AR Collections users use **Customer payment journal** for. | Key concepts (pages table) | 5 | N | SME, Rec | Open |
| VG-19 | Wording for **Open customer invoices**, checked against the recording. | Key concepts (pages table) | 6 | N | Rec | Open |
| VG-20 | Baseline claim that **Aged balances** gives access to collection activities. | Not in guide (removed) | — | N | Rec, SME | Open |
| VG-21 | Label distinction between the **Credit and collections** module and the **Customer Credit and Collections** workspace. | Steps 3–6 | — | N | Test | Open |
| VG-22 | Guide code and final title. Source 0 proposes `PG-AR-010`. The authoring guide requires an assigned code (`NNN-Guide Title PG vX.docx`). | Cover; file name | 0 | B | Dec | Open |
| VG-23 | Whether the legal entity affects Favorites. If it does not, Step 1 can be removed. | Step 1 | 9 | N | Test | Open |
| VG-24 | Screenshots captured in a clean session, if screenshots are used (D-017). | — | — | N | Test | Open |
| VG-25 | SME factual review, designated reviewer, and process-owner approval. | Whole guide | — | B | SME | Open |
| VG-26 | D365 environment and sign-in method, if it needs to be referenced. | PROCESS START | — | N | SME | Open |
| VG-27 | Masking policy for the legal entity name, user name and customer data in screenshots. | — | — | N | Dec, SME | Open |
| VG-28 | UI label spelling users see: **Favorites** or **Favourites**. | Step 10; all UI references | 16 | B | Test | Open |
| VG-29 | Whether pages appear in other modules and create the same favorite. | — | — | — | — | **Withdrawn.** Only needed for the removed Troubleshooting section (T7). |
| VG-30 | Initiation events. Source supports only setup by a new AR Collections user. | Part 1 Initiation; Topic Initiation; Process table *When* | 2 | B | SME | Open |
| VG-31 | Stream name, process area and business role name ("Accounts Receivable", "AR Collections", "Collections Officer"). | Stream table; Process table; Roles matrix; Responsibility | 3 | B | SME | Open |
| VG-32 | Whether any reports or inquiries apply. If none, the section reads "No applicable reports". | Part 3 | 19 | B | SME | Open |
| VG-33 | Business process owner (BPO). | Version history | 1 | B | SME | Open |

---

## 4. Terminology register

| Term in PG | Variants in sources | Decision | Status |
|---|---|---|---|
| **Aged balances** | "Age Balances" (source 0) | Majority of sources. | Provisional (`VG-01`) |
| **Favorites** (UI label) / favorites (prose) | "Favourites" (all sources) | Prose uses US spelling per the template. The UI label is provisional. | Provisional (`VG-28`) |
| **Credit and collections** (module) | "Credit & Collections" (source 0) | Module name as shown in the module list. | Provisional (`VG-21`) |
| **Accounts receivable** (module) | — | As in sources. | Provisional |
| **Navigation Pane** | "navigation pane", "side navigation" | Template standard capitalization. | Adopted (template) |
| **Legal Entity** | "ledger", "business", "company" (source 0) | Template standard wording in Step 1. | Adopted (template) |
| favorite star | "favourite star" (source 3.2) | Control name unconfirmed. | Provisional (`VG-07`) |
| Collections Officer | "Collections officers" (source 2), "AR Collections users" (source 3.2) | Role name as in source 2. | Provisional (`VG-31`) |
| aging (prose) | "ageing" (sources) | US spelling per the template. | Adopted (template) |

---

## 5. Publication readiness

This combines the source 1 §4 gate with the authoring guide's final checklist.

| Check | Status |
|---|---|
| Cover, contents, version history, About this guide, Parts 1–3 and Additional Resources are present in order | Met |
| Every placeholder and author instruction is replaced or removed | Met. "To be confirmed" (BPO) and the Part 3 pending note are deliberate review-draft text (`VG-33`, `VG-32`). |
| Process table rows match the Part 2 topics, and Who/When/Where are complete | Met; values pending `VG-30` and `VG-31` |
| Each topic has Description, Responsibility and Initiation | Met |
| Exact system labels are used | Open (`VG-01`, `VG-08`, `VG-09`, `VG-28`) |
| The navigation path is confirmed | Partial (`VG-02` to `VG-06`) |
| Warnings precede risky actions | Open (`VG-07`) |
| Expected outcomes are confirmed | Partial (`VG-07`, `VG-13`) |
| Each report has its own heading, or "No applicable reports" is confirmed | Open (`VG-32`) |
| Roles and BPO reflect confirmed evidence | Open (`VG-31`, `VG-33`) |
| Access and escalation route are confirmed | Open (`VG-16`, `VG-17`) |
| Contents, footer title, page numbers and links are updated and tested | Met in the rendered review copy. Recheck in Word: accept the update-fields prompt, then Ctrl+click each link. |
| Tested by someone other than the author | Open (`VG-25`) |
| SME review, designated reviewer and process-owner approval | Open (`VG-25`) |
| Review comments resolved and draft notes removed from the release copy | Open (20 Word comments) |

---

## 6. Change log

| Date | Change |
|---|---|
| 2026-10-08 | Register created from the review of baseline draft v0.1 (source 3.2). |
| 2026-10-08 | Converted to the PG master template. Added `VG-30` to `VG-33`. Withdrew `VG-15` and `VG-29`. Deferred `VG-14`. Re-rated `VG-24` and `VG-27` as non-blocking (screenshots optional). Mapped items to Word comments. |
