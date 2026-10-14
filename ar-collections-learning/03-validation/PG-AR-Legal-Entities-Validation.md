# Validation Register: AR Collections Legal Entities

| Field | Value |
|---|---|
| Related PG (editable source) | [`../01-procedure-guides/TBC-AR Collections Legal Entities PG v0.1.docx`](../01-procedure-guides/TBC-AR%20Collections%20Legal%20Entities%20PG%20v0.1.docx) |
| Markdown preview | [`../01-procedure-guides/PG-AR-Legal-Entities-DRAFT.md`](../01-procedure-guides/PG-AR-Legal-Entities-DRAFT.md) |
| Screenshot register | [`../02-screenshot-registers/PG-AR-Legal-Entities-Screenshots.md`](../02-screenshot-registers/PG-AR-Legal-Entities-Screenshots.md) |
| Last updated | 2026-10-14 |
| Items | 22 total, all open: 13 blocking, 9 non-blocking |

This file is the guide's **question log** (decision D-016). The `VG-xx` IDs are scoped to this guide and never renumbered. Each open item that affects the text is also a Word review comment by "Validation register" (VR).

---

## 1. Evidence base

| Source | What it supports |
|---|---|
| 0, Topic 1 *Switching Between Legal Entities* | Ledger/business switching; navigate via the company selector; navigate by editing the URL with the ledger code; ledger codes differ between CargoWise and D365; users should work in business names rather than ledger codes. Rated ready, confidence high. No PG code suggested. |
| 1, Module 1 | Sequences 1.1 (legal entities and ledger selection: knowledge lesson, ready) and 1.2 (switch to the required legal entity: PG, ready). The recording shows switching through the company selector or the ledger code in the URL. A legal entity name and code reference is listed as supporting material. |
| 1, publication gate | Every PG must state the correct legal entity requirement. |
| 2, Release 1 item 2 | Scope: use the legal entity selector, identify the business name, navigate using the ledger code where appropriate, confirm that the correct entity is active before processing. Control: users must confirm the active legal entity before performing a transaction. |
| 2, Release 1 item 1 | Orientation content includes the relationship between legal entities and customer accounts, and one legal entity reference. |
| 3.1 | Held for the second drafting batch: limited validation needed before finalisation. |
| PG master template | The standard navigation pattern starts with *Check* the **Entity** in the top-right. |

**Not available:** a transcript excerpt, timestamps, the exact selector label, the URL format, or a list of legal entities with their business names and codes.

---

## 2. Drafting decisions for this guide

| # | Decision | Reason |
|---|---|---|
| L1 | Two standalone topics: **1. Switch Legal Entity with the Selector** and **2. Switch Legal Entity Using the Ledger Code**. | They are alternative methods, each complete on its own (sources 0 and 2). |
| L2 | Neither topic starts with the standard *Check* the **Entity** / *Click* **Modules** rows. | The task is the entity switch itself. Each topic ends with an explicit check of the active legal entity instead. |
| L3 | The selector is described as being in the D365 header, top-right. | The template's standard Entity row places the legal entity there. The exact label is open (`VG-01`). |
| L4 | No URL parameter name or example code is given. | The URL format was not captured (`VG-05`, `VG-06`). |
| L5 | The business-name and confirm-before-processing rules are Key concepts. | T2 "Separate rules from procedure". |
| L6 | Whether Favorites and views carry over to the new legal entity is not stated. | The brief requires that persistence is not assumed (`VG-12`). |

---

## 3. Validation gap register

**Priority:** **B** = blocks publication. **N** = non-blocking.

**Method:** **Test** = D365 test in a clean session. **Rec** = recording or transcript review. **SME** = subject-matter expert or process owner. **Dec** = project decision.

| ID | Item to confirm | Location in Word guide | Word comment | Priority | Method | Status |
|---|---|---|---|---|---|---|
| VG-01 | Exact label and location of the legal entity selector (the recording calls it the company selector). | Topic 1 Step 1 | 8 | B | Test, Rec | Open |
| VG-02 | What the selector list shows (business names, ledger codes or both) and whether it can be searched. | Topic 1 Step 2 | 9 | B | Test | Open |
| VG-03 | What D365 displays after the switch, for example the same page or the dashboard. | Topic 1 Step 3 | 10 | N | Test | Open |
| VG-04 | How the active legal entity is shown, so users can check it. | Topic 1 Step 4; Topic 2 Step 5 | 11 | B | Test | Open |
| VG-05 | Which part of the D365 URL holds the ledger code, and how users recognise it. | Topic 2 Step 2 | 13 | B | Test, Rec | Open |
| VG-06 | Where users find the D365 ledger code for each legal entity (the legal entity name and code reference in source 1). | Topic 2 Step 3 | 14 | B | SME | Open |
| VG-07 | When switching through the URL is appropriate. | Topic 2 Initiation | 12 | B | SME | Open |
| VG-08 | Wording of the statement that D365 and CargoWise ledger codes differ. | Key concepts | 5 | N | SME | Open |
| VG-09 | Wording and owner of the business-name rule. | Key concepts | 6 | N | SME | Open |
| VG-10 | Wording and owner of the confirm-before-processing control. | Key concepts | 7 | N | SME | Open |
| VG-11 | Whether switching legal entity affects open pages or unsaved work. | Not in guide | — | N | Test | Open |
| VG-12 | Whether Favorites and personalized views carry over to the new legal entity. Shared with Favorites and Personalized Views registers. | Not in guide | — | N | Test | Open |
| VG-13 | Which legal entities AR Collections users need access to. | Not in guide | — | N | SME | Open |
| VG-14 | Initiation events for this task. | Part 1 Initiation; topic Initiations; Process table *When* | 2 | B | SME | Open |
| VG-15 | Stream, process area and business role name. Shared with the other AR Collections guides. | Stream table; Process table; Roles matrix | 3 | B | SME | Open |
| VG-16 | Business process owner (BPO). | Version history | 1 | B | SME | Open |
| VG-17 | Guide code and final title. Source 0 gives no code; source 2 uses "Switch to the required legal entity in D365". | Cover; file name | 0 | B | Dec | Open |
| VG-18 | Whether any reports or inquiries apply. If none, "No applicable reports". | Part 3 | 15 | B | SME | Open |
| VG-19 | How access to a legal entity is granted, and a test with a standard AR Collections role. If a legal entity is missing from the selector, missing access is a possible cause, not a confirmed one. | PROCESS START (both topics) | — | B | Test, SME | Open |
| VG-20 | SME factual review, a test by someone other than the author, and approval. | Whole guide | — | B | SME | Open |
| VG-21 | Recording timestamps for the legal entity demonstration. | Screenshot register | — | N | Rec | Open |
| VG-22 | The legal entity definition, including whether any AR Collections pages show data from more than one legal entity. | Key concepts | 4 | N | SME, Test | Open |

**Fastest route to closure:** one clean-session D365 test that switches legal entity both ways closes `VG-01` to `VG-05` and `VG-11`. The same test also closes the persistence item `VG-12` and the matching Favorites and Personalized Views items. `VG-06` and `VG-07` need an SME answer, ideally with the legal entity name and code reference.

---

## 4. Publication readiness

| Check | Status |
|---|---|
| Template structure is complete; unused examples are removed | Met |
| Process table rows match the Part 2 topics (2 rows) | Met; values pending `VG-14` and `VG-15` |
| Standard navigation pattern | Not applicable: the task is the entity switch itself (decision L2) |
| Each procedure table restarts numbering at 1 | Met |
| Exact system labels | Open (`VG-01`, `VG-02`, `VG-05`) |
| Business rules separate from procedure | Met (both rules in Key concepts) |
| Reports | Open (`VG-18`) |
| Roles, BPO, guide code | Open (`VG-15`, `VG-16`, `VG-17`) |
| Peer test, SME review, approval | Open (`VG-19`, `VG-20`) |
| Review comments resolved before release | Open (16 Word comments) |

---

## 5. Change log

| Date | Change |
|---|---|
| 2026-10-14 | Register created with the v0.1 SME review draft. |
