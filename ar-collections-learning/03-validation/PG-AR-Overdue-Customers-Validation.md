# Validation Register: AR Collections Overdue Customers

| Field | Value |
|---|---|
| Related PG (editable source) | [`../01-procedure-guides/TBC-AR Collections Overdue Customers PG v0.1.docx`](../01-procedure-guides/TBC-AR%20Collections%20Overdue%20Customers%20PG%20v0.1.docx) |
| Markdown preview | [`../01-procedure-guides/PG-AR-Overdue-Customers-DRAFT.md`](../01-procedure-guides/PG-AR-Overdue-Customers-DRAFT.md) |
| Screenshot register | [`../02-screenshot-registers/PG-AR-Overdue-Customers-Screenshots.md`](../02-screenshot-registers/PG-AR-Overdue-Customers-Screenshots.md) |
| Last updated | 2026-10-14 |
| Items | 23 total: 22 open (16 blocking, 6 non-blocking), 1 deferred |

This file is the guide's **question log** (decision D-016). The `VG-xx` IDs are scoped to this guide and never renumbered. Each open item that affects the text is also a Word review comment by "Validation register" (VR).

---

## 1. Evidence base

| Source | What it supports |
|---|---|
| 0, Topic 3 *Using Customer Overdue Dashboard* | Accessing overdue customers; viewing 90+; switching to 61-90; reviewing overdue balances; adding collection activities; retrieving customer email; reviewing balances before collection. Rated ready. Suggested PG `PG-AR-002 Review and Manage Overdue Customers`. |
| 0, Topic 9 *Understanding Ageing Indicators* | Green tick, red diamond, aging bands. Partial. |
| 1, Module 3 | Sequences 3.1 (review Customers overdue: ready), 3.2 (change the aging period: ready), 3.3 (sort largest to smallest), 3.6 (interpret balance due versus overdue amount: knowledge note, ready), 3.7 (aging icons: gap), 3.10 (when to contact the receiving team: validation recommended). |
| 1, SME checklist A | Open questions: aging icons and bands, the approved order for working overdue accounts, what takes priority (value, aging, risk), and business days before contacting the receiving team. |
| 2, Release 1 item 6 | Scope: open Customers overdue, select an aging period, review balance due and overdue amount, sort overdue values, add customer email where required, open the customer account, confirm validity before contacting the customer. The trainer warns users to investigate the balance before contact, including low-value balances that may represent fees or overpayments. Dependency: the aging indicator legend needs validation. |
| 3.1 | Held for the second drafting batch. Keep the aging-icon legend out until the icons and bands are validated. |
| Workspace guide | Customers overdue is a section of the Customer credit and collections workspace (Workspace VG-04). |

**Not available:** a transcript excerpt, timestamps, exact column and control labels, the meanings of balance due and overdue amount, or the approved prioritization rules.

---

## 2. Drafting decisions for this guide

| # | Decision | Reason |
|---|---|---|
| O1 | Two standalone topics: **1. Review Customers Overdue** and **2. Check an Overdue Balance Before Contact**. | Reviewing the list and checking one customer are separate tasks. The check is the control source 2 asks for. |
| O2 | Topic 1 opens Customers overdue through **Workspaces**, matching the Workspace guide. | One route to the page across guides. |
| O3 | Reviewing balance due against the overdue amount is the final step of Topic 1. | It is a review of the sorted list, and keeps the table on one page. |
| O4 | No order for working overdue accounts is given. | The approved order and priority factors are open (`VG-11`). |
| O5 | Aging indicators are deferred. | Source 3.1 gap note (`VG-12`). |
| O6 | Recording the contact, retrieving email for sending, investigating the full account and contacting the receiving team are out of scope. | Each belongs to its own guide or business-rule reference (`VG-13`, `VG-23`). |

---

## 3. Validation gap register

**Priority:** **B** = blocks publication. **N** = non-blocking.

**Method:** **Test** = D365 test in a clean session. **Rec** = recording or transcript review. **SME** = subject-matter expert or process owner. **Dec** = project decision.

| ID | Item to confirm | Location in Word guide | Word comment | Priority | Method | Status |
|---|---|---|---|---|---|---|
| VG-01 | Exact label and location of **Customers overdue** in the workspace. Shared with Workspace VG-04. | Key concepts; Topic 1 Step 3 | 4, 8 | B | Test, Rec | Open |
| VG-02 | Label and location of the aging period control, and the periods available. | Key concepts; Topic 1 Step 4 | 5, 9 | B | Test, Rec | Open |
| VG-03 | The default aging period when the page opens. | Key concepts | 5 | N | Test | Open |
| VG-04 | Exact labels and meanings of the balance due and overdue amount columns. | Key concepts; Topic 1 Step 7 | 6, 12 | B | Test, SME | Open |
| VG-05 | How the overdue amount column is sorted on this page. See Aged Balances VG-06. | Topic 1 Step 5 | 10 | B | Test | Open |
| VG-06 | Exact label of the email column and that it can be added on this page. See Personalized Views VG-03. | Topic 1 Step 6 | 11 | B | Test | Open |
| VG-07 | How the customer account opens from Customers overdue. | Topic 2 Step 2 | 14 | B | Test | Open |
| VG-08 | What users must review to decide that an overdue balance is valid. | Topic 2 Step 3 | 15 | B | SME | Open |
| VG-09 | Wording and owner of the check-the-balance-first rule, and whether a value threshold defines a low-value balance. | Key concepts; Topic 2 Step 4 | 7 | B | SME | Open |
| VG-10 | What users should do, and who they should tell, when an overdue balance is not valid. | Topic 2 Step 5 | 16 | B | SME | Open |
| VG-11 | The approved order for working overdue accounts, and whether value, aging, customer risk or another factor takes priority. | Not in guide | — | N | SME | Open |
| VG-12 | Aging indicator icons and the bands each one represents. | Not in guide | — | N | Rec, SME | **Deferred.** Excluded from v0.1 (source 3.1). Add when validated. |
| VG-13 | When to contact the receiving team, including the number of business days (source 1, sequence 3.10). | Not in guide | — | N | SME | Open |
| VG-14 | Initiation events for this task. | Part 1 Initiation; topic Initiations; Process table *When* | 2, 13 | B | SME | Open |
| VG-15 | Stream, process area and business role name. Shared with the other AR Collections guides. | Stream table; Process table; Roles matrix | 3 | B | SME | Open |
| VG-16 | Business process owner (BPO). | Version history | 1 | B | SME | Open |
| VG-17 | Guide code and final title. Source 0 proposes `PG-AR-002 Review and Manage Overdue Customers`. | Cover; file name | 0 | B | Dec | Open |
| VG-18 | Whether any reports or inquiries apply. If none, "No applicable reports". | Part 3 | 17 | B | SME | Open |
| VG-19 | The security role needed for Customers overdue, and a test with it. | PROCESS START (Topic 1) | — | B | Test, SME | Open |
| VG-20 | SME factual review, a test by someone other than the author, and approval. | Whole guide | — | B | SME | Open |
| VG-21 | Recording timestamps for the Customers overdue demonstration. | Screenshot register | — | N | Rec | Open |
| VG-22 | Whether the Aged Balances filters (zero balances, currency, customer) also apply on Customers overdue (source 1, sequences 3.4–3.5). | Not in guide | — | N | Test, Dec | Open |
| VG-23 | Confirm that recording the contact and using the email address belong in the *Record a collection activity* guide. | Part Description (scope) | — | N | Dec | Open |

**Fastest route to closure:** one clean-session D365 test of Customers overdue closes `VG-01` to `VG-07` (except the meanings in `VG-04`). It can run in the same session as the Workspace test. `VG-04` (meanings) and `VG-08` to `VG-10` need SME answers, ideally with the prioritization rules (`VG-11`).

---

## 4. Publication readiness

| Check | Status |
|---|---|
| Template structure is complete; unused examples are removed | Met |
| Process table rows match the Part 2 topics (2 rows) | Met; values pending `VG-14` and `VG-15` |
| Standard navigation pattern | Met (Entity, then Workspaces, as in the Workspace guide) |
| Each procedure table restarts numbering at 1 | Met |
| Exact system labels | Open (`VG-01`, `VG-02`, `VG-04` to `VG-07`) |
| Business rules separate from procedure | Met (check-the-balance rule in Key concepts) |
| Reports | Open (`VG-18`) |
| Roles, BPO, guide code | Open (`VG-15`, `VG-16`, `VG-17`) |
| Peer test, SME review, approval | Open (`VG-19`, `VG-20`) |
| Review comments resolved before release | Open (18 Word comments) |

---

## 5. Change log

| Date | Change |
|---|---|
| 2026-10-14 | Register created with the v0.1 SME review draft. |
