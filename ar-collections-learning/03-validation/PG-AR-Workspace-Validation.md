# Validation Register: AR Collections Workspace

| Field | Value |
|---|---|
| Related PG (editable source) | [`../01-procedure-guides/TBC-AR Collections Workspace PG v0.1.docx`](../01-procedure-guides/TBC-AR%20Collections%20Workspace%20PG%20v0.1.docx) |
| Markdown preview | [`../01-procedure-guides/PG-AR-Workspace-DRAFT.md`](../01-procedure-guides/PG-AR-Workspace-DRAFT.md) |
| Screenshot register | [`../02-screenshot-registers/PG-AR-Workspace-Screenshots.md`](../02-screenshot-registers/PG-AR-Workspace-Screenshots.md) |
| Last updated | 2026-10-14 |
| Items | 22 total, all open: 14 blocking, 8 non-blocking |

This file is the guide's **question log** (decision D-016). The `VG-xx` IDs are scoped to this guide and never renumbered. Each open item that affects the text is also a Word review comment by "Validation register" (VR).

---

## 1. Evidence base

| Source | What it supports |
|---|---|
| 0, Topic 2 *Credit & Collections Workspace Overview* | The Customer Credit & Collections workspace; Summary section; Activities section; Open Cases; Customers Over Credit Limit; Payment Journals Not Posted; Collections Letters Not Printed; Balance Review area; Collections section. Rated ready; minor screenshots required. Suggested PG `PG-AR-001 Navigate and Interpret the Customer Credit & Collections Workspace`. |
| 1, Module 1 | Sequences 1.3 (navigate the workspace: PG, ready) and 1.4 (understand the workspace sections and indicators: system overview, ready with minor validation). |
| 1, sequences 3.9 and 7.1 | Identify payment journals not posted (ready); open payment journals from the workspace to investigate unallocated payments (ready). |
| 2, Release 1 item 3 | Scope: open the workspace, locate balances and collection information, review Customers overdue, identify payment journals not posted, locate Notes and Open payment journals, understand which workspace sections are not currently used. The recording identifies Customers overdue, payment journals not posted, Notes and Open payment journals as relevant to normal collection work. |
| 3.2, screenshot plan | At about 00:32:42 the trainer explains the Navigation Pane icons: Home, Favorites, Recents, **Workspaces** and Modules. |
| Favorites register | The labels that distinguish the Credit and collections module from the Customer Credit and Collections workspace are open (Favorites VG-21). |

**Not available:** a transcript excerpt or timestamps for the workspace walkthrough, the exact section labels, or which sections are not used.

---

## 2. Drafting decisions for this guide

| # | Decision | Reason |
|---|---|---|
| W1 | Two standalone topics: **1. Open the Customer Credit and Collections Workspace** and **2. Locate Collection Work in the Workspace**. | Opening the workspace is a short task on its own, and other guides depend on it (Notes and Activities). Locating the sections is a separate orientation task. |
| W2 | Topic 1 uses *Check* the **Entity**, then *Click* **Workspaces** in place of **Modules**. | The template pattern is applied to the workspace route. Source 3.2 names Workspaces in the Navigation Pane. |
| W3 | Topic 2 locates only the four sections source 2 names as relevant, and refers each one to its own guide. | Keeps the guide to one outcome. The work in each section belongs elsewhere (Review overdue customers, Notes and Activities, Investigate unallocated payments). |
| W4 | Other sections are named without saying whether they are used. Indicators are out of scope. | Which sections are unused was not captured (`VG-08`). Indicators belong to the system overview in source 1, sequence 1.4 (`VG-13`). |
| W5 | The workspace/module distinction is a Key concept. | Users meet both names in these guides. Labels are shared with Favorites VG-21 (`VG-11`). |

---

## 3. Validation gap register

**Priority:** **B** = blocks publication. **N** = non-blocking.

**Method:** **Test** = D365 test in a clean session. **Rec** = recording or transcript review. **SME** = subject-matter expert or process owner. **Dec** = project decision.

| ID | Item to confirm | Location in Word guide | Word comment | Priority | Method | Status |
|---|---|---|---|---|---|---|
| VG-01 | The **Workspaces** icon in the Navigation Pane and its label or tooltip. | Topic 1 Step 2 | 8 | B | Test, Rec | Open |
| VG-02 | Exact label of the **Customer credit and collections** workspace in the list. | Topic 1 Step 3 | 9 | B | Test | Open |
| VG-03 | What the workspace shows when it opens. | Topic 1 Step 4 | 10 | N | Test | Open |
| VG-04 | Exact label and location of **Customers overdue** in the workspace. | Key concepts; Topic 2 Step 1 | 5, 12 | B | Test, Rec | Open |
| VG-05 | Exact label and location of **Payment journals not posted**. | Key concepts; Topic 2 Step 2 | 5, 13 | B | Test, Rec | Open |
| VG-06 | Exact label and location of **Notes**. Shared with Notes and Activities VG-01 and VG-02. | Key concepts; Topic 2 Step 3 | 5, 14 | B | Test, Rec | Open |
| VG-07 | Exact label and location of **Open payment journals**. | Key concepts; Topic 2 Step 4 | 5, 15 | B | Test, Rec | Open |
| VG-08 | Which workspace sections are not currently used in AR Collections. | Key concepts | 6 | B | SME, Rec | Open |
| VG-09 | Wording of the workspace definition. | Key concepts | 4 | N | SME | Open |
| VG-10 | That workspace sections show data for the active legal entity only. | Topic 1 Step 4 | 10 | N | Test | Open |
| VG-11 | Labels that distinguish the workspace from the Credit and collections module. Shared with Favorites VG-21. | Key concepts | 7 | N | Test | Open |
| VG-12 | Whether the workspace can be added to Favorites or opened from the dashboard. | Not in guide | — | N | Test | Open |
| VG-13 | Confirm that workspace indicators (source 1, sequence 1.4) belong in a separate system overview. | Part Description (scope) | — | N | Dec | Open |
| VG-14 | Initiation events for this task. | Part 1 Initiation; topic Initiations; Process table *When* | 2, 11 | B | SME | Open |
| VG-15 | Stream, process area and business role name. Shared with the other AR Collections guides. | Stream table; Process table; Roles matrix | 3 | B | SME | Open |
| VG-16 | Business process owner (BPO). | Version history | 1 | B | SME | Open |
| VG-17 | Guide code and final title. Source 0 proposes `PG-AR-001 Navigate and Interpret the Customer Credit & Collections Workspace`. | Cover; file name | 0 | B | Dec | Open |
| VG-18 | Whether any reports or inquiries apply. If none, "No applicable reports". | Part 3 | 16 | B | SME | Open |
| VG-19 | The security role needed for the workspace, and a test with it. | PROCESS START (Topic 1) | — | B | Test, SME | Open |
| VG-20 | SME factual review, a test by someone other than the author, and approval. | Whole guide | — | B | SME | Open |
| VG-21 | Recording timestamps for the workspace walkthrough. The Navigation Pane explanation is at about 00:32:42 (source 3.2). | Screenshot register | — | N | Rec | Open |
| VG-22 | Which screenshots source 0 means by "minor screenshots required". | Screenshot register | — | N | SME | Open |

**Fastest route to closure:** one clean-session D365 test of the workspace closes `VG-01` to `VG-07` and `VG-10`. It also closes Notes and Activities VG-01 and VG-02, and Favorites VG-21. `VG-08` needs an SME answer or the recording.

---

## 4. Publication readiness

| Check | Status |
|---|---|
| Template structure is complete; unused examples are removed | Met |
| Process table rows match the Part 2 topics (2 rows) | Met; values pending `VG-14` and `VG-15` |
| Standard navigation pattern | Met in Topic 1 (Workspaces in place of Modules); `VG-01` |
| Each procedure table restarts numbering at 1 | Met |
| Exact system labels | Open (`VG-01`, `VG-02`, `VG-04` to `VG-07`) |
| Business rules separate from procedure | Not applicable: no business rules in scope |
| Reports | Open (`VG-18`) |
| Roles, BPO, guide code | Open (`VG-15`, `VG-16`, `VG-17`) |
| Peer test, SME review, approval | Open (`VG-19`, `VG-20`) |
| Review comments resolved before release | Open (17 Word comments) |

---

## 5. Change log

| Date | Change |
|---|---|
| 2026-10-14 | Register created with the v0.1 SME review draft. |
