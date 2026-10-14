# Validation Register: AR Collections Collection Activities

| Field | Value |
|---|---|
| Related PG (editable source) | [`../01-procedure-guides/TBC-AR Collections Collection Activities PG v0.1.docx`](../01-procedure-guides/TBC-AR%20Collections%20Collection%20Activities%20PG%20v0.1.docx) |
| Markdown preview | [`../01-procedure-guides/PG-AR-Collection-Activities-DRAFT.md`](../01-procedure-guides/PG-AR-Collection-Activities-DRAFT.md) |
| Screenshot register | [`../02-screenshot-registers/PG-AR-Collection-Activities-Screenshots.md`](../02-screenshot-registers/PG-AR-Collection-Activities-Screenshots.md) |
| Last updated | 2026-10-14 |
| Items | 24 total, all open: 17 blocking, 7 non-blocking |

This file is the guide's **question log** (decision D-016). The `VG-xx` IDs are scoped to this guide and never renumbered. Each open item that affects the text is also a Word review comment by "Validation register" (VR).

---

## 1. Evidence base

| Source | What it supports |
|---|---|
| 0, Topic 4 *Recording Collection Activities* | New Activity; Event Type; Email Activity; Phone Activity; Notes Entry; customer-level activity logging. Rated ready. Suggested PG `PG-AR-003 Record Collection Activities Against a Customer`. |
| 0, Topic 3 *Using Customer Overdue Dashboard* | Lists "adding collection activities" from the overdue customers flow. |
| 1, Module 5 | Sequences 5.1 (create a new activity), 5.2 (select the activity type), 5.3 (record an email or telephone interaction) and 5.5 (record notes at customer rather than invoice level), all ready; 5.4 (enter useful collection notes: writing standard) and 5.7 (identify system-generated activity) partial. The trainer prefers customer-level notes because invoice-level notes are less visible in the account overview. |
| 1, open questions B | Approved activity types; whether "Action" should always be used or whether Activity, Event, Appointment and Task differ; mandatory content for email and telephone notes; invoice numbers; commitment-to-pay date; prohibited or sensitive information; naming and date convention; when to record against a transaction. Output needed: a collection-note standard. |
| 2, Release 1 item 10 | Scope: select the customer, create a new activity, select the activity type, record an email or telephone interaction, enter a concise summary, save the activity, verify that it is visible. Status: ready with minor gap (approved types, mandatory content, note standard, whether "Action" is the standard record type). |
| Earlier guides | All customers path (Favorites, Customer Account); View all activities (Notes and Activities). |

**Not available:** a transcript excerpt, timestamps, exact labels for New activity, the type, summary and notes fields or the save control, and the collection-note standard.

---

## 2. Drafting decisions for this guide

| # | Decision | Reason |
|---|---|---|
| A1 | One standalone topic, **1. Record a Customer Collection Activity**. | One task done in one sitting (source 2 scope). |
| A2 | The procedure opens the customer from **All customers**, matching the Customer Account guide. | One route to the customer account across guides. Other entry points are a question (`VG-03`). |
| A3 | The activity type step names email and phone as examples only. | The approved types and the role of "Action" are open (`VG-05`, `VG-06`). |
| A4 | No mandatory note content, prohibited content or naming convention is stated. | The collection-note standard is still to be written (`VG-09` to `VG-11`, `VG-24`). |
| A5 | The customer-level rule is a Key concept. | T2 "Separate rules from procedure". Shared with Notes and Activities VG-11. |

---

## 3. Validation gap register

**Priority:** **B** = blocks publication. **N** = non-blocking.

**Method:** **Test** = D365 test in a clean session. **Rec** = recording or transcript review. **SME** = subject-matter expert or process owner. **Dec** = project decision.

| ID | Item to confirm | Location in Word guide | Word comment | Priority | Method | Status |
|---|---|---|---|---|---|---|
| VG-01 | Menu group for **All customers**. Shared with Favorites VG-02. | Step 3 | 7 | B | Test | Open |
| VG-02 | How the customer account opens. Shared with Customer Account VG-02. | Step 4 | 8 | B | Test | Open |
| VG-03 | Whether activities can also be created from Customers overdue or other pages (source 0, Topic 3). | Step 3 | 7 | N | Test, Rec | Open |
| VG-04 | Exact label and location of **New activity** on the customer account. | Step 5 | 9 | B | Test, Rec | Open |
| VG-05 | Exact label of the activity type field (source 0: "Event Type") and the approved values. | Key concepts; Step 6 | 4, 10 | B | Test, SME | Open |
| VG-06 | Whether "Action" should always be used, and whether Activity, Event, Appointment and Task have different uses. | Key concepts | 4 | N | SME | Open |
| VG-07 | Exact label of the summary field. | Step 7 | 11 | B | Test | Open |
| VG-08 | Exact label of the notes field. | Step 8 | 12 | B | Test | Open |
| VG-09 | Mandatory content for email and telephone notes, for example invoice numbers or a commitment-to-pay date. | Key concepts; Step 8 | 5, 12 | B | SME | Open |
| VG-10 | Prohibited or sensitive information that must not be recorded. | Key concepts | 5 | B | SME | Open |
| VG-11 | Naming and date convention for activities. | Not in guide | — | N | SME | Open |
| VG-12 | Exact label and location of the save control. | Step 9 | 13 | B | Test | Open |
| VG-13 | Where the saved activity appears and how users check it, for example **View all activities**. Shared with Notes and Activities VG-09. | Step 10 | 14 | B | Test | Open |
| VG-14 | Wording and owner of the customer-level rule, and when an activity should be recorded against a specific transaction. Shared with Notes and Activities VG-11. | Key concepts | 6 | N | SME | Open |
| VG-15 | How system-generated activity differs from activities users record (source 1, sequence 5.7: partial). | Not in guide | — | N | SME, Test | Open |
| VG-16 | Initiation events for this task. | Part 1 Initiation; topic Initiation; Process table *When* | 2 | B | SME | Open |
| VG-17 | Stream, process area and business role name. Shared with the other AR Collections guides. | Stream table; Process table; Roles matrix | 3 | B | SME | Open |
| VG-18 | Business process owner (BPO). | Version history | 1 | B | SME | Open |
| VG-19 | Guide code and final title. Source 0 proposes `PG-AR-003 Record Collection Activities Against a Customer`. | Cover; file name | 0 | B | Dec | Open |
| VG-20 | Whether any reports or inquiries apply. If none, "No applicable reports". | Part 3 | 15 | B | SME | Open |
| VG-21 | The security role needed to create activities, and a test with it. | PROCESS START | — | B | Test, SME | Open |
| VG-22 | SME factual review, a test by someone other than the author, and approval. | Whole guide | — | B | SME | Open |
| VG-23 | Recording timestamps for the activity demonstration. | Screenshot register | — | N | Rec | Open |
| VG-24 | The AR collection-note writing standard and example notes (source 1 supporting references), to link from this guide when written. | Not in guide | — | N | SME | Open |

**Fastest route to closure:** one clean-session D365 test that records a mock activity on a test customer closes `VG-01`, `VG-02`, `VG-04`, `VG-05` (label), `VG-07`, `VG-08`, `VG-12` and `VG-13`. `VG-05` (values), `VG-06` and `VG-09` to `VG-11` need the collection-note standard from the SME.

---

## 4. Publication readiness

| Check | Status |
|---|---|
| Template structure is complete; unused examples are removed | Met |
| Process table rows match the Part 2 topics (1 row) | Met; values pending `VG-16` and `VG-17` |
| Standard navigation pattern | Met; menu group pending `VG-01` |
| Each procedure table restarts numbering at 1 | Met |
| Exact system labels | Open (`VG-01`, `VG-02`, `VG-04`, `VG-05`, `VG-07`, `VG-08`, `VG-12`) |
| Business rules separate from procedure | Met (customer-level rule in Key concepts) |
| Note content standard | Open (`VG-09`, `VG-10`) |
| Reports | Open (`VG-20`) |
| Roles, BPO, guide code | Open (`VG-17`, `VG-18`, `VG-19`) |
| Peer test, SME review, approval | Open (`VG-21`, `VG-22`) |
| Review comments resolved before release | Open (16 Word comments) |

---

## 5. Change log

| Date | Change |
|---|---|
| 2026-10-14 | Register created with the v0.1 SME review draft. |
