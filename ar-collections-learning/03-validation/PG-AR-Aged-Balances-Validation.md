# Validation Register: AR Collections Aged Balances

| Field | Value |
|---|---|
| Related PG (editable source) | [`../01-procedure-guides/TBC-AR Collections Aged Balances PG v0.1.docx`](../01-procedure-guides/TBC-AR%20Collections%20Aged%20Balances%20PG%20v0.1.docx) |
| Markdown preview | [`../01-procedure-guides/PG-AR-Aged-Balances-DRAFT.md`](../01-procedure-guides/PG-AR-Aged-Balances-DRAFT.md) |
| Screenshot register | [`../02-screenshot-registers/PG-AR-Aged-Balances-Screenshots.md`](../02-screenshot-registers/PG-AR-Aged-Balances-Screenshots.md) |
| Last updated | 2026-10-14 |
| Items | 23 total: 22 open (15 blocking, 7 non-blocking), 1 deferred |

This file is the guide's **question log** (decision D-016). The `VG-xx` IDs are scoped to this guide and never renumbered. Each open item that affects the text is also a Word review comment by "Validation register" (VR).

---

## 1. Evidence base

| Source | What it supports |
|---|---|
| 0, Topic 8 *Working with Age Balances* | Navigate to Age Balances; remove zero balances; sort balances; currency filtering; customer filtering; overdue review. Rated ready. Suggested PG `PG-AR-007`. |
| 0, Topic 9 *Understanding Ageing Indicators* | Green tick, red diamond, aging bands. Partial: a screenshot legend is needed. To be merged into this guide later. |
| 1, Module 3 | Sequences 3.3 (sort largest to smallest), 3.4 (exclude zero-balance accounts), 3.5 (filter by customer, currency or aging band), 3.7 (aging icons: gap), 3.8 (reporting currency: ready, validation recommended). Aged balances can show values in the ledger's reporting currency, which can differ from the customer transaction currency. |
| 1, Module 4 | Sequence 4.2: open a customer from Aged balances. Belongs to the *Investigate a customer account* guide. |
| 1, Module 6 critical control | Customer-facing account information should be provided as PDF rather than Excel. This was stated during the Aged balances demonstration. |
| 2, Release 1 item 7 | Scope: open Aged balances, exclude zero-value accounts, sort largest to smallest, filter by customer, filter by currency, select multiple customers, add currency information, interpret accounting currency. |
| 3.1, first drafting batch #3 | Scope: exclude zero balances using **not equal to 0**, sort, filter by customer or currency, add the **Currency** column, interpret balances carefully. Keep the aging-icon legend out of the first version. |
| Favorites guide | Aged balances is in the **Credit and collections** module. Its menu group is unconfirmed (Favorites VG-01, VG-03). |

**Not available:** a transcript excerpt, timestamps, or exact control labels for the Aged balances demonstration.

---

## 2. Drafting decisions for this guide

| # | Decision | Reason |
|---|---|---|
| A1 | Two standalone topics. **1. Review Customer Aged Balances** prepares the list: Currency column, zero-balance filter, descending sort. **2. Filter Aged Balances by Customer or Currency** narrows it. | Each is performed independently (T2 topic rules). Filtering is optional and depends on the prepared list. |
| A2 | Topic 1 uses the template's full navigation pattern: *Check* the **Entity**, *Click* **Modules**, *Navigate* to the page. Favorites is offered as an alternative route. | T2 standard navigation pattern. Links back to the Favorites guide. |
| A3 | Column steps follow the Personalized Views guide's wording, and the same unconfirmed controls are referenced. | Consistent actions across guides (D-020). |
| A4 | Aging indicators (green tick, red diamond) are excluded. | Source 3.1 gap note (`VG-10`). |
| A5 | Opening a customer account from this page is out of scope. | It belongs to the *Investigate a customer account* guide (`VG-23`). |
| A6 | The PDF-not-Excel rule is a Key concept, not a procedure step. | It is a general business rule (T2 "Separate rules from procedure"). |

---

## 3. Validation gap register

**Priority:** **B** = blocks publication. **N** = non-blocking.

**Method:** **Test** = D365 test in a clean session. **Rec** = recording or transcript review. **SME** = subject-matter expert or process owner. **Dec** = project decision.

| ID | Item to confirm | Location in Word guide | Word comment | Priority | Method | Status |
|---|---|---|---|---|---|---|
| VG-01 | Page label: **Aged balances** or **Age balances**. Shared with Favorites VG-01. | Key concepts | 4 | B | Test, Rec | Open |
| VG-02 | Menu group or submenu containing Aged balances in Credit and collections. Shared with Favorites VG-03. | Topic 1 Step 3 | 7 | B | Test | Open |
| VG-03 | Exact label of the balance column to filter and sort, for example a total balance compared with aging-period columns. | Topic 1 Step 7 | 9 | B | Test, Rec | Open |
| VG-04 | Location of **Insert columns** on this page. Shared with Personalized Views VG-03. | Topic 1 Step 4 | 8 | B | Test | Open |
| VG-05 | How a column filter is opened and applied on this page. Shared with Personalized Views VG-07 and VG-08. | Topic 1 Steps 7, 10 | 9, 10 | B | Test, Rec | Open |
| VG-06 | How a column is sorted, and the label of the sort option. | Topic 1 Step 11 | 11 | B | Test, Rec | Open |
| VG-07 | Exact label of the customer column. | Topic 2 Step 1 | 13 | B | Test | Open |
| VG-08 | That the demonstration selected multiple customers with **is one of**. | Topic 2 Step 2 | 14 | B | Rec | Open |
| VG-09 | Reporting-currency wording, and which legal entities differ. A currency interpretation reference is still to be developed (source 2). | Key concepts | 5 | N | SME, Rec | Open |
| VG-10 | Aging indicator icons and the bands each one represents. | Not in guide | — | N | Rec, SME | **Deferred.** Excluded from v0.1 (source 3.1). Add when validated. |
| VG-11 | Whether this page has an aging period or band selector that the guide should cover (source 1, sequence 3.5). | Not in guide | — | N | Test, Rec | Open |
| VG-12 | Whether the **Currency** column is shown by default. | Topic 1 Step 4 | 8 | N | Test | Open |
| VG-13 | Wording and owner of the PDF-not-Excel rule for customer-facing information. | Key concepts | 6 | N | SME | Open |
| VG-14 | Initiation events, for example a daily or weekly review. | Part 1 Initiation; topic Initiations; Process table *When* | 2, 12 | B | SME | Open |
| VG-15 | Stream, process area and business role name. Shared with the other AR Collections guides. | Stream table; Process table; Roles matrix | 3 | B | SME | Open |
| VG-16 | Business process owner (BPO). | Version history | 1 | B | SME | Open |
| VG-17 | Guide code and final title. Source 0 proposes `PG-AR-007`. | Cover; file name | 0 | B | Dec | Open |
| VG-18 | Whether any reports or inquiries apply. If none, "No applicable reports". | Part 3 | 15 | B | SME | Open |
| VG-19 | The security role needed for Aged balances, and a test with it. | PROCESS START | — | B | Test, SME | Open |
| VG-20 | SME factual review, a test by someone other than the author, and approval. | Whole guide | — | B | SME | Open |
| VG-21 | Recording timestamps for the Aged balances demonstration. | Screenshot register | — | N | Rec | Open |
| VG-22 | Whether the prepared list should be a standard saved view for AR Collections users. | Topic 1 Description | — | N | SME, Dec | Open |
| VG-23 | Confirm that opening a customer from Aged balances belongs in the *Investigate a customer account* guide. | Part Description (scope) | — | N | Dec | Open |

**Fastest route to closure:** one clean-session D365 test of the Aged balances page closes `VG-01` to `VG-07` and `VG-12`. That same session also closes the matching items in the Favorites and Personalized Views registers.

---

## 4. Publication readiness

| Check | Status |
|---|---|
| Template structure is complete; unused examples are removed | Met |
| Process table rows match the Part 2 topics (2 rows) | Met; values pending `VG-14` and `VG-15` |
| Standard navigation pattern | Met; menu group pending `VG-02` |
| Each procedure table restarts numbering at 1 | Met |
| Exact system labels | Open (`VG-01` to `VG-08`) |
| Business rules separate from procedure | Met (PDF rule in Key concepts) |
| Reports | Open (`VG-18`) |
| Roles, BPO, guide code | Open (`VG-15`, `VG-16`, `VG-17`) |
| Peer test, SME review, approval | Open (`VG-19`, `VG-20`) |
| Review comments resolved before release | Open (16 Word comments) |

---

## 5. Change log

| Date | Change |
|---|---|
| 2026-10-14 | Register created with the v0.1 SME review draft. |
