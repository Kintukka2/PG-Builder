# Validation Register: AR Collections Personalized Views

| Field | Value |
|---|---|
| Related PG (editable source) | [`../01-procedure-guides/TBC-AR Collections Personalized Views PG v0.1.docx`](../01-procedure-guides/TBC-AR%20Collections%20Personalized%20Views%20PG%20v0.1.docx) |
| Markdown preview | [`../01-procedure-guides/PG-AR-Personalized-Views-DRAFT.md`](../01-procedure-guides/PG-AR-Personalized-Views-DRAFT.md) |
| Screenshot register | [`../02-screenshot-registers/PG-AR-Personalized-Views-Screenshots.md`](../02-screenshot-registers/PG-AR-Personalized-Views-Screenshots.md) |
| Last updated | 2026-10-14 |
| Items | 29 open: 23 blocking, 6 non-blocking |

This file is the guide's **question log**, as the PG Template Authoring Guide requires (decision D-016). The `VG-xx` IDs are scoped to this guide and never renumbered. Each open item that affects the text is also a Word review comment by "Validation register" (VR), anchored to that text.

---

## 1. Evidence base

| Source | What it supports |
|---|---|
| 0, Topic 5 *Customising Views* | Insert Columns, Save View, Save As, Set Default View, Persist Views Across Legal Entities. Rated ready. Suggested PG `PG-AR-004`. |
| 1, Module 2 *Configure D365 for efficient AR work* | Learning outcome: configure reusable views that expose the information required for collection work. Sequences 2.1–2.9: add/remove columns, reorder, column filters, exclude zero-balance accounts, footer totals, save, Save As, pin as default, view scope (ready with validation). The recording shows the operators "not equal to" and "is one of", a sum footer, Save As and pinning, and states that views are configured separately for different screens. |
| 2, Release 1 item 5 | Scope: insert, remove and reorder columns; add a footer and a sum; save; Save as; pin as default; separate views per page. Lists the recommended columns. |
| 3.1, first drafting batch #2 | Scope: insert and rearrange columns, apply filters, insert a footer and sum, Save as, name the view, pin it as the default, save subsequent changes. Caution: "a saved default may be available across legal entities" must be phrased exactly as demonstrated and validated. |

**Not available:** a transcript excerpt, recording timestamps, or exact click paths for any views step. The sources give the actions and some labels, but not where each control sits or what D365 shows after each click. Most items below come from that gap.

---

## 2. Drafting decisions for this guide

| # | Decision | Reason |
|---|---|---|
| V1 | **Topic 1, Create a Personalized View**, is a parent topic with four subtopics: 1.1 Arrange the Columns, 1.2 Filter the List (optional), 1.3 Add a Footer Total (optional) and 1.4 Save and Pin the View. | T2: "related stages that together achieve one outcome belong under it as subtopics". The stages match sources 1, 2 and 3.1. |
| V2 | **Topic 2, Update a Saved View**, is a standalone topic. | Source 3.1 lists "save subsequent changes". T2 keeps a task standalone when it is performed independently. Open question `VG-28`. |
| V3 | The procedure uses a generic page ("the page you want to personalize") rather than a named AR page. | The demonstrated page was not captured (`VG-01`). Views apply to any grid page. |
| V4 | Navigation is *Check* the **Entity** → *Open* the page, not the full Modules path. | The page is generic. Step 2 points to Favorites, which the AR Collections Favorites guide sets up. |
| V5 | Legal entity scope is **not stated** in the guide text. | Source 3.1 says to phrase it exactly as demonstrated and validated (`VG-02`). |
| V6 | Where a control label was not captured, the step names the action, not a label, and carries a comment. Examples: *Show* the grid footer; *Save* the new view. | T2: the author cannot infer a menu path or control. |
| V7 | The zero-balance filter example (`not equal to` 0) is reused from the Aged balances scope in source 3.1. | It illustrates the operator, using source wording (`VG-29`). |

---

## 3. Validation gap register

**Priority:** **B** = blocks publication. **N** = non-blocking.

**Method:** **Test** = D365 test in a clean session. **Rec** = recording or transcript review. **SME** = subject-matter expert or process owner. **Dec** = project decision.

| ID | Item to confirm | Location in Word guide | Word comment | Priority | Method | Status |
|---|---|---|---|---|---|---|
| VG-01 | Which page the training demonstration used. Whether the guide should name a page. Which recommended columns are available on each page. | 1.1 Step 2; Key concepts (recommended columns) | 8, 10 | B | Rec, SME | Open |
| VG-02 | Whether views and the pinned default are available across legal entities. Source 3.1 requires exact demonstrated wording. Whether Step 1 (Check the Entity) is needed. | Key concepts (View scope); 1.1 Step 1; Topic 2 Step 1 | 6, 9, 27 | N | Rec, Test | Open |
| VG-03 | Exact label and location of **Insert columns**, and what D365 displays after it is clicked. | 1.1 Step 3 | 11 | B | Test, Rec | Open |
| VG-04 | The control that applies the column selection. | 1.1 Step 5 | 12 | B | Test | Open |
| VG-05 | How a column is removed, and the control label. | 1.1 Step 6 | 13 | B | Test, Rec | Open |
| VG-06 | How columns are repositioned. | 1.1 Step 7 | 14 | B | Test, Rec | Open |
| VG-07 | How a column filter is opened, and the control label. | 1.2 Step 1 | 15 | B | Test, Rec | Open |
| VG-08 | Exact operator labels (**not equal to**, **is one of**) and the control that applies the filter. | Key concepts (Filter operators); 1.2 Step 2 | 7, 16 | B | Test, Rec | Open |
| VG-09 | How the grid footer is shown, and the control label. | 1.3 Step 1 | 18 | B | Test, Rec | Open |
| VG-10 | How a sum is added, the exact label, and which columns support a sum. | 1.3 Step 2 | 19 | B | Test, Rec | Open |
| VG-11 | Exact label and location of **Save as**. | 1.4 Step 1 | 20 | B | Test, Rec | Open |
| VG-12 | Whether a view naming convention applies. Source 1 lists a recommended AR view naming convention as a reference still to be developed. | 1.4 Step 2 | 21 | N | SME, Dec | Open |
| VG-13 | The control that completes Save as. | 1.4 Step 3 | 22 | B | Test | Open |
| VG-14 | Exact label and location of **Pin as default** (source 0 says "Set Default View"), and what pinning does. | Key concepts (Default view); 1.4 Step 4 | 5, 23 | B | Test, Rec | Open |
| VG-15 | How D365 shows a saved view and the pinned default. | 1.4 Step 5 | 24 | B | Test | Open |
| VG-16 | How a saved view is selected on a page. | Topic 2 Step 3 | 28 | B | Test | Open |
| VG-17 | Exact label and location of the control that saves changes to an existing view (source 0 says "Save View"). | Topic 2 Step 5 | 29 | B | Test, Rec | Open |
| VG-18 | That filters and footer totals are saved as part of the view. | Key concepts (View); 1.4 PROCESS COMPLETE | 4, 25 | B | Test | Open |
| VG-19 | Whether a saved view is personal or visible to other users. | 1.4 PROCESS COMPLETE | 25 | N | Test, SME | Open |
| VG-20 | Whether any reports or inquiries apply. If none, "No applicable reports". | Part 3 | 30 | B | SME | Open |
| VG-21 | Initiation events. | Part 1 Initiation; topic Initiations; Process table *When* | 2 | B | SME | Open |
| VG-22 | Stream, process area and business role name. Shared with the AR Collections Favorites guide (its VG-31). | Stream table; Process table; Roles matrix; Responsibility | 3 | B | SME | Open |
| VG-23 | Business process owner (BPO). | Version history | 1 | B | SME | Open |
| VG-24 | Guide code and final title. Source 0 proposes `PG-AR-004`. | Cover; file name | 0 | B | Dec | Open |
| VG-25 | The security role needed, and whether view personalization can be restricted. Test with the standard AR Collections role. | PROCESS START (1.1) | — | B | Test, SME | Open |
| VG-26 | SME factual review, a test by someone other than the author, designated reviewer and process-owner approval. | Whole guide | — | B | SME | Open |
| VG-27 | Recording timestamps for the views demonstration. These are needed for frame review and screenshots. | Screenshot register | — | N | Rec | Open |
| VG-28 | Whether Update a Saved View stays a separate topic or merges into Create a Personalized View. | Topic 2 Initiation | 26 | N | SME | Open |
| VG-29 | Which balance column the zero-balance example applies to on each page. | 1.2 Step 3 | 17 | N | Test | Open |

**Fastest route to closure:** the transcript excerpt and timestamps for the views demonstration (`VG-27`) would answer most of `VG-01` to `VG-17`. A single clean-session D365 test would confirm the rest.

---

## 4. Terminology register

The terms shared with the AR Collections Favorites guide (Navigation Pane, Legal Entity, Collections Officer, US spelling) follow that guide's register.

| Term in PG | Variants in sources | Decision | Status |
|---|---|---|---|
| personalized view | "personalised view" (sources) | US spelling, as the template requires. | Adopted (template) |
| **Insert columns** | "Insert Columns" (source 0), "inserting columns" (source 1) | Sentence case. | Provisional (`VG-03`) |
| **Save as** | "Save As" (sources 0, 1), "Save as" (sources 2, 3.1) | Sentence case. | Provisional (`VG-11`) |
| **Pin as default** | "Pin a view as default" (sources 1, 2), "Set Default View" (source 0), "pin it as the default" (source 3.1) | Uses the most frequent source wording. | Provisional (`VG-14`) |
| **Save** (existing view) | "Save View" (source 0), "save subsequent changes" (source 3.1) | | Provisional (`VG-17`) |
| **not equal to**, **is one of** | As in source 1 | | Provisional (`VG-08`) |
| footer, **Sum** | "footer", "sum", "sum footer", "table footers and totals" | | Provisional (`VG-09`, `VG-10`) |
| grid | "grid" (source 2, export scope) | Used for the list area of a page. | Provisional |

---

## 5. Publication readiness

| Check | Status |
|---|---|
| Template structure is complete; unused examples are removed | Met. The off-system and report example blocks are removed. |
| Every placeholder and author instruction is replaced | Met. "To be confirmed" (BPO) and the Part 3 pending note are deliberate review-draft text. |
| Process table rows match the Part 2 topics (2 rows) | Met; values pending `VG-21` and `VG-22` |
| Topic Overview, continuation links and optional-subtopic skip links | Met. Links resolve in the rendered review copy. |
| Each procedure table restarts numbering at 1 | Met |
| Exact system labels | Open (`VG-03` to `VG-17`) |
| Expected outcomes are confirmed | Open (`VG-15`, `VG-18`) |
| Reports | Open (`VG-20`) |
| Roles, BPO, guide code | Open (`VG-22`, `VG-23`, `VG-24`) |
| Peer test, SME review, approval | Open (`VG-25`, `VG-26`) |
| Review comments resolved before release | Open (31 Word comments) |

---

## 6. Change log

| Date | Change |
|---|---|
| 2026-10-14 | Register created with the v0.1 SME review draft. |
