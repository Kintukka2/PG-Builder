# Legacy O2C PG Cross-Comparison: AR Collections Drafts

| Field | Value |
|---|---|
| Compares | The five legacy O2C procedure guides (200, 210, 211, 220, 230) with the 16 AR Collections guides, the Customer Payment Journal controls reference and the Customer Pools register |
| Covers | 34 draft topics, and the 364 unresolved validation items (open or deferred) in the 15 registers |
| Evidence grade | Reference only (D-044). A legacy statement is a candidate answer: an item closes only on a D365 test, the recording or an SME answer |
| Status | Analysis complete. No guide, register or SME pack has been changed |
| Last updated | 2026-10-25 |

The drafts come from the recent *AR Training D365* recordings, so their topics are current. The legacy PGs are about a year old and under review, so they are reference material, not a source of truth. This analysis answers three questions:

1. Which current draft topics the legacy PGs cover fully, partly, or not at all (section 3).
2. Which open validation items the legacy PGs help answer (section 4).
3. What the legacy PGs cover that the drafts do not (sections 6 and 7).

---

## Summary

- **Topics.** Of 34 draft topics, the legacy PGs cover **10**, partly cover **7** and do not cover **17**. By deliverable: 3 covered, 8 partial and 7 missing. Setup and navigation topics are missing or nearly so (Favorites, views, export, legal entity switching, workspace, Customers overdue, the Notes page, statement preview), and so are two of the three Part 2 guides. The legacy PGs cover record and review activities, open a customer account, send a statement, transfer funds between customers and Customer Pools.
- **Gaps.** The legacy PGs give evidence for **184 of the 364** unresolved items: **92 strong** candidate answers, **81 partial**, and **11** where they contradict the draft and a test or the recording must decide. 150 of the 184 are blocking, and 41 of them are three shared governance answers repeated in every guide (stream, BPO and guide code).
- **Most valuable finds:**
  1. **Two statement controls the drafts lack.** The legacy send runs as a batch job with a future start time and **Maximum retries = 0**, because otherwise "the system will send multiple copies to the customer". And a blank **Records to include** sends the statement to **all customers**. Both affect the customer-facing Statement Distribution guide and the gated test station S13.
  2. **Customer Pools is documented.** Collections PG v2.3 (October 2026) has full Customer Pools and Collections agents procedures, while the project sources describe none (D-035). P2-E1 to P2-E4 can go to the SME with that topic as evidence.
  3. **Customer payment journal labels, approval and reversal.** The legacy PGs give the CPJL control labels, separate Debit and Credit fields, currency behavior, a clearing account number (100949), the approval route (Report as ready, then the Receipting team approves) and a full reversal procedure. They give proposed answers for P2-A1 and P2-A3 (the supplement's second priority) and for P2-B9.
  4. **Aging indicator legend.** A legacy screenshot gives every aging period and its icon, so the two deferred items (Aged Balances VG-10, Overdue Customers VG-12) can be reopened.
  5. **Activity model.** The legacy PGs separate the activity type (Action, Appointment, Event, Task) from the interaction Type (Phone call), name the fields (Purpose, Priority, Type, Description) and make attachments mandatory. The Collection Activities draft treats email or phone as the activity type.
- **Conflicts.** 13 places where the legacy PGs and the drafts disagree (section 5). Each needs a D365 test, the recording or the SME.
- **Legacy-only content.** The legacy PGs hold full procedures for 9 backlog items that are not drafted yet (settle, undo settlement, write-offs and their journals, contacts, addresses, credit management exclusion, payment terms, direct debit) and part of 4 more. They also cover 7 tasks and topics that are not in the backlog at all (section 7).

---

## 1. Legacy sources

Sources 5.1 to 5.5 in the [project notes](../05-project-notes/Project-Context-and-Decisions.md). Like the other sources, they are held outside this repository; they were converted to text for this analysis and are not modified.

| Code | Guide | Last version | Last change | BPO | Relevance to AR Collections |
|---|---|---|---|---|---|
| 200 | Customer Onboarding and Maintenance | 2.1 | December 2025 | Not recorded | Medium: contacts, addresses, credit and collections fields, payment terms, CW1 contact sync. Owned by License Management. |
| 210 | Customer Invoices | 2.0 | September 2025 | Not recorded | Low: sending and previewing invoices, credit notes. Owned by Billing. |
| 211 | Subscription Billing | File v3.0 (history 2.1) | July 2026 | Christoper Clarke | None: billing schedules only. |
| 220 | Customer Payments | 2.1 | January 2026 | Not recorded | High: settlements, Customer payment journal create, settle and reverse, direct debit. Owned by Receipting. |
| 230 | Collections | 2.3 | October 2026 | Christoper Clarke | Highest: the same process area as the drafts. |

References such as "230 §6.7" point to a legacy guide and its Part 2 topic number.

## 2. How to read this

| Coverage | Meaning |
|---|---|
| **Covered** | A legacy topic does the same task, though labels or details may differ. |
| **Partial** | A legacy topic does part of the task, or the same task by another route. |
| **Missing** | No legacy topic does the task. |

| Evidence | Meaning |
|---|---|
| **Strong** | The legacy PG states the label, path, value or rule directly. Put it to the test or SME as the proposed answer. |
| **Partial** | The legacy PG answers part of the item, or gives an analogous rule. |
| **Conflicts** | The legacy PG says something different from the draft. The test, recording or SME decides. |

*Effect* says what the legacy answer would do to the draft if confirmed: confirm it, add detail, or change it. *Route* gives the SME pack question and the test station that will confirm each item. (B) marks a blocking item.

---

## 3. Draft topic coverage

### 3.1 By deliverable

| Deliverable | Coverage | Topics covered / partial / missing |
|---|---|---|
| Favorites | **Missing** | 0 / 0 / 1 |
| Personalized Views | **Missing** | 0 / 0 / 2 |
| Aged Balances | **Partial** | 0 / 1 / 1 |
| Customer Invoices | **Partial** | 0 / 2 / 0 |
| Export to Excel | **Missing** | 0 / 0 / 1 |
| Notes and Activities | **Partial** | 1 / 0 / 1 |
| Legal Entities | **Partial** | 0 / 1 / 1 |
| Workspace | **Missing** | 0 / 0 / 2 |
| Overdue Customers | **Partial** | 0 / 1 / 1 |
| Customer Account | **Partial** | 1 / 1 / 1 |
| Collection Activities | **Covered** | 1 / 0 / 0 |
| Statement Preview | **Missing** | 0 / 0 / 2 |
| Statement Distribution | **Partial** | 1 / 0 / 1 |
| Customer Account Transfers | **Covered** | 3 / 0 / 0 |
| Parent Payment Distribution | **Missing** | 0 / 0 / 1 |
| Overpayment and Write-Off Restoration | **Missing** | 0 / 0 / 1 |
| CPJL Controls reference | **Partial** | 2 / 1 / 1 |
| Customer Pools (validation only) | **Covered** | 1 / 0 / 0 |

### 3.2 By topic

| Deliverable | Draft topic | Coverage | Legacy location | What differs |
|---|---|---|---|---|
| Favorites | Configure AR Collections Favorites | **Missing** | — | No Favorites task. The legacy PGs do give the menu path of all four pages. |
| Personalized Views | Create a personalized view (columns, filter, footer total, save and pin) | **Missing** | 230 §6.3 optional step | Only Insert columns > Update appears. No filters, totals, saving or pinning. |
| Personalized Views | Update a saved view | **Missing** | — | — |
| Aged Balances | Review customer aged balances | **Partial** | 230 §2.1 | Opens Aged balances, sorts amount due largest first, reads the aging icons, opens the customer's Collections page. No Currency column or zero-balance filter. |
| Aged Balances | Filter aged balances by customer or currency | **Missing** | 230 §2.1 step 4 | Sort by customer only. |
| Customer Invoices | Open the invoice preview | **Partial** | 210 §1.4; 230 §6.1 | Different route: Open customer invoices or Tax invoice journal > Document > View > Copy preview. |
| Customer Invoices | Download the invoice as PDF | **Partial** | 210 §1.4 | Copy preview opens a PDF to download or save. No naming or location rule. |
| Export to Excel | Export all rows from a grid | **Missing** | — | — |
| Notes and Activities | Review customer notes (workspace Notes page) | **Missing** | — | The legacy PGs never use the Notes page. |
| Notes and Activities | Review all customer activities | **Covered** | 230 §2.2 | Control label differs (All activities). Legacy also checks attachments and corrects the record. |
| Legal Entities | Switch legal entity with the selector | **Partial** | Step 1 of every legacy procedure; 200 §3.2 | Only "confirm the entity, top-right". No switching steps. |
| Legal Entities | Switch legal entity using the ledger code | **Missing** | — | — |
| Workspace | Open the Customer credit and collections workspace | **Missing** | — | Legacy navigation uses Modules only. |
| Workspace | Locate collection work in the workspace | **Missing** | — | — |
| Overdue Customers | Review Customers overdue | **Missing** | — | Legacy uses Aged balances for this, never Customers overdue. |
| Overdue Customers | Check an overdue balance before contact | **Partial** | 230 Key concepts; §2; §4 | Gives the escalation rules and the pre-contact review, not a step list. |
| Customer Account | Open the customer account | **Covered** | 230 §2.3 steps 3 to 5; §5 | Same route, plus the Customers menu group. |
| Customer Account | Review customer transactions | **Partial** | 230 §6.5 steps 5 to 6 | Show = Open or All. No Hide FX revaluations. |
| Customer Account | Review settlement history | **Missing** | 230 §6.5, §6.6 (settle and undo only) | No review-only route. |
| Collection Activities | Record a customer collection activity | **Covered** | 230 §5 | Legacy is fuller: activity types, Purpose, Priority, Type, Description and mandatory attachments. |
| Statement Preview | Generate the statement preview (Screen) | **Missing** | — | Legacy only sends. No Screen destination. |
| Statement Preview | Download the statement as PDF | **Missing** | — | — |
| Statement Distribution | Send the statement | **Covered** | 230 §1 | Legacy adds Date interval, Balance other than zero, batch processing, a future start time and Maximum retries 0. |
| Statement Distribution | Verify statement delivery | **Missing** | 230 §1 steps 12 to 21 (batch job only) | No delivery message, mailbox or failed-delivery steps. |
| Customer Account Transfers | Create the journal and enter the source line | **Covered** | 230 §6.7 steps 1 to 14 | Path differs (Accounts receivable > Payments). Offset Ledger 100949. |
| Customer Account Transfers | Enter the destination line | **Covered** | 230 §6.7 steps 15 to 21 | Legacy offset is Bank, not the clearing account (see section 5). |
| Customer Account Transfers | Validate and post the journal | **Covered** | 230 §6.7 steps 22 to 25 | Legacy adds approval: Report as ready, Receipting approves, then Post. |
| Parent Payment Distribution | All three subprocedures, including partial allocation | **Missing** | 220 §4 (use case named only) | — |
| Overpayment and Write-Off Restoration | Both subprocedures | **Missing** | — | Legacy covers creating write-offs, not restoring them. |
| CPJL Controls reference | Journal set-up | **Covered** | 230 §6.7; 220 §4.1 | Gives labels for Name, Description and Journal batch number. |
| CPJL Controls reference | Line coding | **Partial** | 230 §6.7 | Debit and Credit, Currency, Offset. No blank-field, dimension or tab-through rules. No Overpayment ledger. |
| CPJL Controls reference | Validation and posting | **Covered** | 230 §6.7; 220 §4.1 to 4.3 | Adds the approval workflow and reversal. |
| CPJL Controls reference | Allocations and amounts (partial allocation) | **Missing** | — | — |
| Customer Pools (validation only) | Create pools and assign Collections agents | **Covered** | 230 §3.1, §3.2 | Full manager procedures. |

---

## 4. Open gaps the legacy PGs help answer

### 4.1 Totals

| Register scope | Unresolved items | With legacy evidence | Strong | Partial | Conflicts | Blocking items with evidence |
|---|---|---|---|---|---|---|
| 13 guides (first and second batches) | 311 | 148 | 74 | 65 | 9 | 117 |
| Part 2 guides and reference | 46 | 29 | 14 | 13 | 2 | 26 |
| Customer Pools | 7 | 7 | 4 | 3 | 0 | 7 |
| **Total** | **364** | **184** | **92** | **81** | **11** | **150** |

An item is counted once, at its strongest evidence. Items that also have conflicting evidence are listed in section 5.

Nothing in the legacy PGs answers these SME questions: A5 (security role), A6 (review and approval), A8 (screenshots), B2 (exported data), B4.1 (balance due and overdue amount), B5.3 (multi-currency and statement exclusions), B10 (workspace sections), C1 (recording timestamps), D2.3 (custom transaction report scope), D2.4 (export scope), D2.5 (export navigation), D2.6 (invoice search scope), D2.9 (preview and send split), D2.12 (workspace indicators), P2-A6 (review and approval), P2-B5 (blank fields and dimensions), P2-B8 (restoration scope), P2-C1 (recording check), P2-C4 (timestamps), P2-D3 (release placement).

### 4.2 Governance and scope

| Topic | Items | Legacy PG says | Source | Evidence | Effect | Route |
|---|---|---|---|---|---|---|
| Initiation: aged balances | Aged Balances VG-14 (B) | Monitoring is part of the **daily collection routine**. Also triggered by a weekly debt review cycle, after statements are issued, and by customer or internal queries about an account. | 230 §2 Initiation; Part 1 Process | **Strong** | Adds detail | SME A1 |
| Initiation: overdue customers | Overdue Customers VG-14 (B) | Collections starts when **balances remain unpaid beyond agreed payment terms**, after system reports or automated reminders, or at the Group Billing and Credit Manager's request. | 230 Part 1 Initiation | **Strong** | Adds detail | SME A1 |
| Initiation: notes and activities | Notes and Activities VG-14 (B) | Review previous activities in the daily routine, and make sure prior correspondence is recorded **before making new contact**. | 230 §2, §2.2 | **Strong** | Confirms draft | SME A1 |
| Initiation: record an activity | Collection Activities VG-16 (B) | **Immediately after customer contact** by phone or email, or after any collection action that needs documenting. | 230 §5 Initiation | **Strong** | Adds detail | SME A1 |
| Initiation: send a statement | Statement Distribution VG-18 (B) | Statements go out **automatically on the 5th of each month**. Send ad hoc only when a customer asks for a copy, or when a Collections Officer must give updated balance information. | 230 §1 | **Strong** | Changes draft | SME A1 |
| Initiation: preview a statement | Statement Preview VG-16 (B) | Same triggers as the ad hoc send. The legacy PGs have no preview-only task. | 230 §1 | **Partial** | Adds detail | SME A1 |
| Initiation: investigate an account | Customer Account VG-16 (B) | After reviewing aged balances and activity history, when an overdue account needs follow-up, or when a customer asks for account details. | 230 §4 | **Partial** | Confirms draft | SME A1 |
| Initiation: invoice copy | Customer Invoices VG-13 (B) | When a customer requests supporting documents, as a resolution action after contact. | 230 §6, §6.1 | **Partial** | Confirms draft | SME A1 |
| Stream, process area and role | Favorites VG-31 (B), Personalized Views VG-22 (B), Aged Balances VG-15 (B), Customer Invoices VG-14 (B), Export to Excel VG-13 (B), Notes and Activities VG-15 (B), Legal Entities VG-15 (B), Workspace VG-15 (B), Overdue Customers VG-15 (B), Customer Account VG-17 (B), Collection Activities VG-17 (B), Statement Preview VG-17 (B), Statement Distribution VG-19 (B) | Stream **O2C** (Order-to-Cash), process area **Collections**, roles **Collections Officer** and **Group Billing and Credit Manager**. The same O2C stream holds Onboarding and Maintenance, Invoices, Payments and Subscription Billing. The drafts say Accounts Receivable and AR Collections. | 230 and 210 Part 1 Stream | **Strong** | Changes draft | SME A2 |
| Business process owner | Favorites VG-33 (B), Personalized Views VG-23 (B), Aged Balances VG-16 (B), Customer Invoices VG-15 (B), Export to Excel VG-14 (B), Notes and Activities VG-16 (B), Legal Entities VG-16 (B), Workspace VG-16 (B), Overdue Customers VG-16 (B), Customer Account VG-18 (B), Collection Activities VG-18 (B), Statement Preview VG-18 (B), Statement Distribution VG-20 (B), GOV-02 (B) | BPO on every version of the Collections PG (2.0 to 2.3) and the Subscription Billing PG: **Christoper Clarke** (spelled this way in both version histories). | 230, 211 version history | **Strong** | Adds detail | SME A3, P2-A2 |
| Reports: balances | Aged Balances VG-18 (B), Overdue Customers VG-18 (B) | **Customer ageing report** (balances by aging period) and **Customer balance list report** (balances side by side for defined periods), under Credit and collections > Enquiries and reports > Customers. | 230 Part 3 | **Partial** | Adds detail | SME A4 |
| Reports: transactions and invoices | Customer Account VG-20 (B), Customer Invoices VG-17 (B) | **Open transactions report**, **Transactions report** and **Customer report** (contact, purchasing and payment details). | 230, 220, 210 Part 3 | **Partial** | Adds detail | SME A4 |
| Reports: statements | Statement Preview VG-20 (B), Statement Distribution VG-22 (B) | **Customer account statement** is listed as a Collections report. | 230 Part 3 | **Partial** | Adds detail | SME A4 |
| Reports: payment journals | GOV-04 (B) | **Customer posted payment journal report** (Accounts receivable > Enquiries and reports > Payments), **Customer to ledger reconciliation report** and **Transactions report**. | 220, 200 Part 3 | **Partial** | Adds detail | SME P2-A5 |
| Support route | Favorites VG-16 (B) | Every legacy PG sends users to the **D365 issue form** on the Atlas D365 User Support Hub, worded for "go-live and early adoption". | 230, 200 Additional Resources | **Strong** | Confirms draft | SME A7 |
| AVA and Procedure Guides | SRC-03 | **AVA - Atlas Virtual Assistant**: "Your AI assistant for navigating the Procedure Guides". This is the "PG/Ava follow-up support" in the Part 2 notes. | 230, 200 Additional Resources | **Strong** | Confirms draft | SME P2-B10 |
| Guide codes | Favorites VG-22 (B), Personalized Views VG-24 (B), Aged Balances VG-17 (B), Customer Invoices VG-16 (B), Export to Excel VG-15 (B), Notes and Activities VG-17 (B), Legal Entities VG-17 (B), Workspace VG-17 (B), Overdue Customers VG-17 (B), Customer Account VG-19 (B), Collection Activities VG-19 (B), Statement Preview VG-19 (B), Statement Distribution VG-21 (B), GOV-03 (B) | O2C guides use three-digit codes: 200 Onboarding and Maintenance, 210 Invoices, 211 Subscription Billing, 220 Payments, 230 Collections. A sub-guide takes the next number in its family (211 under 210). This gives D-006 a third option: codes in the 23x range. | Legacy file names | **Partial** | Adds detail | SME D1, P2-D1 |
| Scope: open a customer from Aged balances | Aged Balances VG-23 | The legacy monitoring task opens the customer from **Aged balances**: click the customer **Name** to open the **Collections** page, then review **Open transactions** (toolbar: Change status, Show, Write off, Settle, Reprint, View collections history). | 230 §2.1 steps 5 to 6; §6.8 screenshot | **Conflicts** | Changes draft | SME D2.1 |
| Opening customers from Aged balances | Customer Account VG-03 | Yes for Aged balances: the legacy monitoring task opens the customer's **Collections** page from it. Customers overdue is not used in the legacy PGs. | 230 §2.1 step 5 | **Strong** | Adds detail | SME B9 · Test S8.1 |
| Scope: undo settlement | Customer Account VG-13 | Undo settlement is its own legacy topic (6.6), done by the Collections Officer "only when done in error or the wrong invoices were selected". | 230 §6.6 | **Partial** | Confirms draft | SME D2.2 |
| Scope: review, contact and record | Notes and Activities VG-22, Overdue Customers VG-23 | Review activity (2.2), contact the customer (4, off-system) and record the activity (5) are separate legacy topics. | 230 §2.2, §4, §5 | **Partial** | Confirms draft | SME D2.7, D2.8 |
| Scope: several accounts on one statement | Statement Preview VG-14, Statement Distribution VG-14 | **Records to include** takes several customer accounts in one run. If it is left blank, the statement runs for **all customers**. | 230 §1 step 5 | **Partial** | Adds detail | SME D2.10, D2.11 |

### 4.3 Business rules

| Topic | Items | Legacy PG says | Source | Evidence | Effect | Route |
|---|---|---|---|---|---|---|
| PDF for customer documents | Aged Balances VG-13, Customer Invoices VG-12, Export to Excel VG-09, Statement Preview VG-15 | Customer documents leave D365 as PDF through print management (invoices by Email (PDF); collection letters exported as PDF and sent in Outlook). No legacy PG states the Excel prohibition. | 210 §1.4; 230 §6.2 step 13 | **Partial** | Confirms draft | SME B1 |
| Activity types | Collection Activities VG-05 (B), Collection Activities VG-06 | On **+ New**, pick the activity type: **Action** (a follow-up that has happened, such as a call or reminder), **Appointment** (a future call or meeting), **Event** (a general update or milestone), **Task** (an internal reminder). Then set **Type** to the interaction, for example **Phone call**. The drafts treat email or phone as the activity type. | 230 Key concepts; §5 steps 6 to 7 | **Strong** | Changes draft | SME B3.1 · Test S11.4 |
| Activity content | Collection Activities VG-09 (B) | Each activity records **Purpose** (for example Outstanding debt), **Priority** (defaults to Normal), **Type** and a detailed **Description** (for example "Customer has promised to pay by 1 April 2026"). Attaching supporting documents (customer emails, payment confirmations, dispute correspondence) is **mandatory** for audit. | 230 §5 | **Partial** | Adds detail | SME B3.2 |
| Activity naming and note standard | Collection Activities VG-11, Collection Activities VG-24 | One worked format: Purpose "Debt Write-off approved", Description "$X written off on [date] due to [reason]". Closing an activity needs resolution details, attachments and a completion status. | 230 §6.4 step 14; §7 | **Partial** | Adds detail | SME B3.2 |
| Customer-level recording | Notes and Activities VG-11, Collection Activities VG-14 | Every legacy activity is created and reviewed from the customer record. No transaction-level recording is described. | 230 §2.2, §5 | **Partial** | Confirms draft | SME B3.3 |
| Checks before contact | Overdue Customers VG-08 (B), Customer Account VG-15 | Before contact, review the aged balance, its open transactions and aging icons, and the previous activities, and make sure earlier correspondence is recorded. | 230 §2, §2.1 step 6, §4 | **Partial** | Confirms draft | SME B4.2 |
| Low-value balances | Overdue Customers VG-09 (B) | Small residual balances from bank fees, FX differences or minor variances are cleared with a **bank fee write-off** (reason codes BANK FEE, FOREX, OVER/SHORT, PENNY DIFF). No value threshold is stated. | 230 Key concepts; §6.8 | **Partial** | Adds detail | SME B4.2 |
| When a balance is not valid | Overdue Customers VG-10 (B) | Collections workflow: within tolerance, contact and record; unresponsive or disputed, escalate to the **Group Billing and Credit Manager**; uncollectible, raise a write-off request; payment applied incorrectly, transfer, settle or unsettle. | 230 Key concepts (Collections workflow) | **Partial** | Adds detail | SME B4.2 |
| Order of work | Overdue Customers VG-11 | Aged balances are sorted by amount due, largest first. Automated letters follow a fixed timeline: pre-due reminder 5 days before the due date, then letters 3, 11 and 18 days after it. | 230 §2.1 step 4; Key concepts | **Partial** | Confirms draft | SME B4.3 |
| Print management destination | Statement Preview VG-05 (B), Statement Distribution VG-05 (B) | Exact label: **Use print management destination** (a toggle). Set to Yes, it applies the delivery settings configured for the customer and sends automatically. | 230 §1 step 4; §6.2 step 11 | **Strong** | Changes draft | SME B5.1 · Test S12.4, S13.1 |
| Recipient source | Statement Distribution VG-06 (B) | Recipients are the customer's email contacts with **Purpose = Business** (Contact information FastTab), synchronized with CargoWise. Only Business contacts receive statements, invoices and letters. Changing the Purpose removes the contact through the integration. | 230 Key concepts, §1, §2.3; 200 §3.4 | **Strong** | Adds detail | SME B5.1 |
| Only open | Statement Preview VG-03 (B), Statement Distribution VG-03 (B) | Label **Only open**, set to Yes in every ad hoc statement. | 230 §1 step 4 | **Strong** | Confirms draft | SME B5.2 · Test S12.3 |
| Company logo | Statement Preview VG-04 (B), Statement Distribution VG-04 (B) | Label **Include company logo**, set to Yes. | 230 §1 step 4 | **Strong** | Confirms draft | SME B5.2 · Test S12.3 |
| Approved statement parameters | Statement Distribution VG-17 (B) | Use print management destination = Yes; **Date interval** (for example Current year, or From and To dates); Only open = Yes; **Balance other than zero** = Yes; Include company logo = Yes. Then **Batch processing** = Yes, a **Recurrence** start time in the future (+1 hour) and **Maximum retries** = 0 on the batch job. | 230 §1 steps 4 to 19 | **Strong** | Changes draft | SME B5.2 |
| Failed delivery causes | Statement Distribution VG-10 (B) | Invoices fail to send when the customer has no email contact or the contact has the wrong Purpose, and go to the wrong person when several emails are marked Business. The fix is in Contact information. Statements use the same contacts. | 200 Troubleshooting | **Partial** | Adds detail | SME B5.4 |
| Manual sending and format | Statement Distribution VG-15, Statement Distribution VG-16 | When automation fails, collection letters are exported as PDF and sent from Outlook. The legacy PGs give no manual route for statements. | 230 §6.2 step 13 | **Partial** | Adds detail | SME B5.5 |
| Sending an invoice | Customer Invoices VG-21 | **Resend an invoice** (Collections Officer): open the customer > **Invoice > Journals > Tax invoice journal** > select the invoice > **Document > Send > Copy** > check **Print management** > **OK**. First sends belong to Billing (License Management Administrator). | 230 §6.1; 210 §1.4 | **Strong** | Adds detail | SME B6 |
| Checks before sharing an invoice | Customer Invoices VG-06 | Before resending, confirm the Print management delivery method and recipient. | 230 §6.1 step 9 | **Partial** | Adds detail | SME B6 |
| Credit notes | Customer Invoices VG-11 | Credit notes are sent with the same **Invoice > Document > Send > Copy** controls as invoices. | 210 §3.1 | **Partial** | Adds detail | SME B6 · Test S10.5 |
| Confirm the legal entity first | Legal Entities VG-10 | Every legacy procedure starts with *Check* the **Entity**: "Confirm you are signed into the correct Legal Entity (top-right)." Troubleshooting fixes a customer created in the wrong entity by switching entity first. | All legacy PGs; 200 Troubleshooting | **Strong** | Confirms draft | SME B7 |
| Legal entity codes | Legal Entities VG-06 (B) | Codes appear only as examples (115A; voucher prefix 230A). There is no code list. | 220 §3.5 step 8; 230 §6.8 screenshot | **Partial** | Adds detail | SME B7 |
| Entity-scoped pages | Legal Entities VG-22 | "Customer account not found... does not exist in current legal entity". eBanking records carry their own Legal entity field. | 220 Troubleshooting; 230 §2.4 | **Partial** | Confirms draft | SME B7 · Test S15.2 |
| System-created entries | Notes and Activities VG-05 | D365 sends the pre-due reminder email, three collection letters and the monthly statement run automatically. These automated sends are the candidates for the system-created entries. | 230 Key concepts; §1 | **Partial** | Adds detail | SME B8 |
| Settlement history | Customer Account VG-12 (B) | After a settlement posts, the payment and invoices show as Settled in history. Undo settlement lists the settled payment and invoice lines. | 230 §6.5 step 14; §6.6 step 9 | **Partial** | Adds detail | SME B9 · Test S9.3 |
| What Customer payment journal is for | Favorites VG-18 | CPJL moves open or closed payments between customer accounts (Collections). It also records payments automated settlement can't: cheques and failed imports, backdated adjustments, parent-child batch payments, payments across several accounts, intercompany transfers (Receipting). | 230 §6.7; 220 §4 | **Strong** | Confirms draft | SME B11 |
| Aged balances and collection history | Favorites VG-20 | The Collections page opened from Aged balances has **View collections history** on its Open transactions toolbar. | 230 §6.8 screenshot | **Partial** | Adds detail | SME B11 |
| Recommended columns | Personalized Views VG-01 (B) | Add **Account status** and **Account status reason** to All customers. Add **Text** to sales order lines and save the view. | 230 §6.3 optional step; 210 §1.1 | **Partial** | Adds detail | SME B11 |
| Open customer invoices wording | Favorites VG-19 | "The list of open, unpaid invoices is displayed." | 210 §1.4 step 2 | **Partial** | Adds detail | SME C2 |

### 4.4 Labels and navigation

| Topic | Items | Legacy PG says | Source | Evidence | Effect | Route |
|---|---|---|---|---|---|---|
| All customers menu group | Favorites VG-02 (B), Customer Account VG-01 (B), Notes and Activities VG-07 (B), Collection Activities VG-01 (B) | **Credit and collections > Customers > All customers**. Some legacy topics use Accounts receivable > Customers > All customers. | 230 §2.2, §5, §6.1, §6.3, §7 | **Strong** | Adds detail | Test S2.2 |
| Aged balances label and menu group | Favorites VG-01 (B), Favorites VG-03 (B), Aged Balances VG-01 (B), Aged Balances VG-02 (B) | **Credit and collections > Collections > Aged balances**. | 230 §2.1, §6.4, §6.8 | **Strong** | Adds detail | Test S2.3 |
| Customer payment journal path | Favorites VG-04 (B), CPJ-01 (B) | **Accounts receivable > Payments > Customer payment journal(s)**. No legacy PG opens it from Credit and collections, where the drafts put it. | 230 §6.7 step 3; 220 §4.1, §4.3, §5 | **Conflicts** | Changes draft | SME P2-C2 · Test S2.4 |
| Open customer invoices menu group | Favorites VG-05 (B) | **Accounts receivable > Invoices > Open customer invoices**. | 210 §1.4 step 2 | **Strong** | Adds detail | Test S2.5 |
| Insert columns | Aged Balances VG-04 (B), Personalized Views VG-03 (B), Personalized Views VG-04 (B), Overdue Customers VG-06 (B) | Right-click a column header, select **Insert columns**, add the columns, then click **Update**. | 230 §6.3 optional step | **Strong** | Adds detail | Test S6.2, S5.5 |
| Balance column and sort | Aged Balances VG-03 (B), Aged Balances VG-06 (B), Overdue Customers VG-05 (B) | Sort the **amount due** balance from largest to smallest. | 230 §2.1 step 4 | **Partial** | Confirms draft | Test S6.4, S6.5, S5.4 |
| Aging periods | Overdue Customers VG-02 (B) | Aging periods are **Current, 1-30, 31-60, 61-90 and 90+** days. | 230 §2.1 screenshot (Periods set-up) | **Strong** | Confirms draft | Test S5.2 |
| Aging indicator legend (deferred items) | Aged Balances VG-10 (deferred), Overdue Customers VG-12 (deferred) | 90+ red diamond; 61-90 red X; 31-60 yellow exclamation point; 1-30 yellow triangle; Current green check mark. | 230 §2.1 step 3 screenshot | **Strong** | Adds detail | Reopen, then test S6 and S5 |
| Opening the customer account | Collection Activities VG-02 (B), Notes and Activities VG-08 (B), Customer Account VG-02 (B) | Click the customer's **Account** hyperlink in All customers. Search with the **Filter** field by Name, Account or Invoice account. | 230 §2.2 step 4; §2.3 steps 4 to 5 | **Strong** | Confirms draft | Test S8.1 |
| Activity controls | Collection Activities VG-04 (B), Notes and Activities VG-09 (B) | Customer page Main toolbar: **General > Activities > Activities > All activities**, then **+ New** to create one. The drafts say New activity and View all activities. | 230 §2.2 step 5; §5 steps 5 to 6 | **Conflicts** | Changes draft | Test S11.3, S11.1 |
| Activity summary field | Collection Activities VG-07 (B) | The short field is **Purpose** ("the Purpose of the interaction", for example Outstanding debt). | 230 §5 step 7 | **Partial** | Adds detail | Test S11.4 |
| Activity notes field | Collection Activities VG-08 (B) | The detailed note goes in **Description**. | 230 §5 step 7 | **Partial** | Adds detail | Test S11.4 |
| Saving an activity | Collection Activities VG-12 (B) | **Save**. The activity then appears in the customer activity log. | 230 §5 step 10 | **Strong** | Confirms draft | Test S11.5 |
| Where a saved activity appears | Collection Activities VG-13 (B) | In the customer's **All activities** list (the customer activity log). | 230 §5 step 10 | **Partial** | Adds detail | Test S11.5 |
| Customer transactions | Customer Account VG-05 (B), Customer Invoices VG-01 (B) | Customer page Main toolbar: **Customer > Transactions > Transactions**. | 230 §6.5 step 5; §6.6 step 5 | **Strong** | Adds detail | Test S8.3 |
| Open and closed filter | Customer Account VG-06 (B) | A **Show** field: **Open** for open items, **All** to include settled ones. The drafts say Show open and Show closed. | 230 §6.5 step 6; §6.6 step 6 | **Conflicts** | Changes draft | Test S8.4 |
| Highlight, not mark | Customer Account VG-10 (B), Customer Invoices VG-02 (B) | Click a voucher to highlight it. Tick the **Mark** column only to settle. | 230 §6.5 steps 7 and 9 | **Partial** | Confirms draft | Test S9.1 |
| View settlements | Customer Account VG-11 (B) | The Main toolbar has a **Settlements** menu (Settle transactions, Undo settlement). No View settlements control is named. | 230 §6.5 step 8; §6.6 step 8 | **Partial** | Adds detail | Test S9.2 |
| Invoice preview route | Customer Invoices VG-03 (B), Customer Invoices VG-04 (B), Customer Invoices VG-05 (B), Customer Invoices VG-07 (B) | Open customer invoices > select the invoice > **Invoice > Document > View > Copy preview** opens a PDF to review, download or save. No legacy PG uses Original document or Print preview. | 210 §1.4 steps 2 to 5 | **Conflicts** | Changes draft | Test S10.1, S10.2, S10.3, S10.4 |
| Statement page | Statement Preview VG-01 (B), Statement Distribution VG-01 (B) | **Credit and collections > Enquiries and reports > Customers > Customer account statement**. The drafts call it the Statements page. | 230 §1 step 3; Part 3 | **Strong** | Changes draft | Test S12.1 |
| Selecting the statement customer | Statement Preview VG-02 (B), Statement Distribution VG-02 (B) | Expand **Records to include**, click **Filter**, enter the customer account in **Criteria**. Left blank, the statement runs for **all customers**. | 230 §1 step 5 | **Strong** | Adds detail | Test S12.2 |
| Statement generate control | Statement Preview VG-07 (B), Statement Distribution VG-07 (B) | **OK**. In the legacy send, OK creates a batch job. | 230 §1 steps 9 to 11 | **Strong** | Confirms draft | Test S12.5, S13.2 |
| Statement delivery check | Statement Distribution VG-08 (B) | Check the job in **Common > Enquiries > Batch jobs > My batch jobs** (status Waiting until its start time). No delivery message is described. | 230 §1 steps 11 to 21 | **Partial** | Changes draft | Test S13.3 |
| Legal entity selector | Legal Entities VG-01 (B), Legal Entities VG-04 (B) | The active legal entity shows top-right. One legacy topic says to select the entity on the Home dashboard toolbar. | All legacy PGs step 1; 200 §3.2 step 1 | **Partial** | Confirms draft | Test S1.1, S1.3 |

### 4.5 Customer payment journals (Part 2)

| Topic | Items | Legacy PG says | Source | Evidence | Effect | Route |
|---|---|---|---|---|---|---|
| Journal set-up controls | CPJ-01 (B), CPJ-02 (B), CPJ-03 (B) | **+New** creates the journal header. **Name** = **CPJL** (journal type Customer payments). **Description** fills in and is overwritten with the purpose. The **Journal batch number** hyperlink opens the lines, and **+New** adds a line with its own **Description**. "The journal name controls posting behavior and approval workflow." | 230 §6.7 steps 4 to 17; 220 §4.1 steps 4 to 7 | **Strong** | Adds detail | SME P2-C2 |
| Description examples | CPJ-04 | Header "Transfer from CUST001 to CUST002"; lines "Transfer out to CUST002" and "Transfer in from CUST001"; payments "Customer payment received - ABC Logistics". | 230 §6.7; 220 §4.1 | **Partial** | Adds detail | SME P2-B3 |
| Date | CPJ-05 (B) | **Date**: keep today's date, or select the posting date the transfer should be recorded on. No rule says who decides. | 230 §6.7 step 8 | **Partial** | Confirms draft | SME P2-B1 |
| Debit and credit | CPJ-06 (B) | Separate **Debit** and **Credit** fields. | 230 §6.7 steps 11 and 18; 220 §4.1 | **Strong** | Adds detail | Controlled CPJL test (not planned yet) |
| Currency | CPJ-07 (B) | **Currency** fills in from the Account. Confirm it matches the original receipt. If currencies differ, stop and escalate. | 230 §6.7 steps 12, 19; 220 §4.2 step 9 | **Strong** | Adds detail | SME P2-B2 |
| Offset fields | CPJ-08 (B) | **Offset account type** and **Offset account** on each line. | 230 §6.7 steps 13 to 14, 20 to 21 | **Strong** | Confirms draft | Controlled CPJL test (not planned yet) |
| Clearing account value | CPJ-09 (B), TF-03 (B) | Source line: Offset account type **Ledger**, Offset account **100949** "to ensure no impact to the bank". The legacy PG prints the account number. | 230 §6.7 steps 13 to 14 | **Strong** | Adds detail | SME P2-D2, P2-B4 |
| Offset on the receiving lines | TF-04 (B), PC-03 (B) | Destination line: Offset account type **Bank**, "the same Bank account (e.g., 1001) used on the debit line". That contradicts the Ledger 100949 offset on the debit line, so the legacy PG cannot settle this item. | 230 §6.7 steps 20 to 21 | **Conflicts** | Changes draft | SME P2-C3 |
| Simulate posting | CPJ-14 (B) | Main toolbar **Validate > Simulate posting**. If an error message appears, correct the data and validate again. | 230 §6.7 step 22; 220 §4.1 step 8 | **Strong** | Confirms draft | SME P2-C2 |
| Errors and support | CPJ-15 (B) | A journal does not post while approval is pending or a validation error remains. Unresolved issues go to the D365 issue form. | 220 Troubleshooting; 230 Additional Resources | **Partial** | Confirms draft | SME P2-B10 |
| Approval and posting | CPJ-16 (B), CPJ-17 (B) | **Approval > Report as ready** routes the journal. A non-approver asks the **Receipting team** to approve (share the page with Options > Share > Get a link). After **Approve**, click **Post**. Journals that need approval show the Approval button and hide Post. | 230 §6.7 steps 23 to 25; 220 §4.1 steps 9 to 11 | **Strong** | Changes draft | SME P2-A1, P2-A3 |
| Who prepares the journals | GOV-01 (B) | The Collections Officer is responsible for transfers (230 §6.7). The Receipting Officer creates manual payment journals (220 §4). The Accounts Receivable Manager approves direct debit journals. | 230 Roles; 220 Roles | **Partial** | Adds detail | SME P2-A1 |
| After posting | CPJ-18 (B) | Check that both sides balance to zero and the transaction appears under both customer accounts. A system message confirms the posting. | 230 §6.7 step 25; 220 §4.1 step 11 | **Partial** | Confirms draft | SME P2-B9 |
| Reverse a posted journal | CPJ-19 (B) | Customer payment journals > open the batch > select the line > **Voucher** > **Reverse transactions** > **Use existing date for reversal** or **Reversal date** > **Reason comment** > **Reverse** > **Post**. | 220 §4.3 | **Strong** | Adds detail | SME P2-B9 |
| Transfer trigger | TF-01 (B) | A payment applied to the wrong customer account. Transfers move payments "when allocated incorrectly". | 230 Key concepts | **Partial** | Confirms draft | SME P2-A4 |
| Payment already settled | TF-05 (B) | The legacy topic covers **Open / Closed** payments, and Undo settlement (6.6) returns settled items to Open. The order of the two is not stated. | 230 §6.6, §6.7 | **Partial** | Adds detail | SME P2-B6 |
| Cross-entity transfers | TF-06 | Intercompany transfers are processed manually through a customer payment journal (Receipting). | 220 §4 | **Partial** | Adds detail | SME P2-B6 |
| Parent-child payments | PC-02 (B), PC-06 (B) | Batch payments across parent-child accounts are posted with a manual payment journal. For combined payments, use the bank batch file or payment platform for the breakdown. | 220 §4; §2.2 step 10 | **Partial** | Adds detail | SME P2-B7, P2-A4 |
| Authorizing a restoration | RO-03 (B) | Write-offs need Group Billing and Credit Manager approval after an emailed request (account, balance, history, justification). Restoration authority is not stated. | 230 §6.4 | **Partial** | Adds detail | SME P2-A3 |

### 4.6 Customer Pools

| Topic | Items | Legacy PG says | Source | Evidence | Effect | Route |
|---|---|---|---|---|---|---|
| Use, purpose and owner | CP-01 (B), CP-02 (B), CP-03 (B) | Collections PG v2.3 (October 2026) has a Customer Pools topic. Pools group customers by criteria (customer group, legal entity, financial dimensions) and are assigned to Collections agents to set ownership and workload. Managers (Group Billing and Credit Manager) create and maintain them. | 230 §3 | **Strong** | Changes draft | SME P2-E1 |
| Assignment | CP-04 (B) | Credit and collections > Setup > **Customer pools** > New: **Pool ID**, **Pool description**, **Pool type** = Collections, **Select pool criteria** (Advanced query, Range tab: Table, Field, Criteria), **Preview pool customers**, Save. Then Setup > **Collections agents** > New: add the Worker, add **Pool ID** lines, set **Default pool**. | 230 §3.1, §3.2 | **Strong** | Adds detail | SME P2-E2 |
| Demonstration, daily effect and content type | CP-05 (B), CP-06 (B), CP-07 (B) | Documented steps exist, but no demonstration. The daily effect is stated only as "ownership and workload allocation". The legacy library treats pools as a manager-level PG topic. | 230 §3 | **Partial** | Adds detail | SME P2-E3, P2-E2, P2-E4 |

---

## 5. Conflicts to resolve

Where the legacy PGs and the drafts disagree. Do not change a draft on legacy evidence alone: record what D365 shows at the test station, or what the recording or SME says.

| # | Topic | Drafts | Legacy PGs | Items | Resolve by |
|---|---|---|---|---|---|
| 1 | Customer payment journal path | Credit and collections > Customer payment journal (Favorites recording frame). | Accounts receivable > Payments > Customer payment journal(s). | Favorites VG-04, CPJ-01 | Test S2.4: check both menus. |
| 2 | Activity controls | New activity; View all activities. | General > Activities > Activities > All activities, then + New. | Collection Activities VG-04, Notes and Activities VG-09 | Test S11.1 and S11.3. |
| 3 | Activity type | Email or phone. | Activity type Action, Appointment, Event or Task; interaction Type such as Phone call. | Collection Activities VG-05, VG-06 | SME B3.1 and test S11.4. |
| 4 | Statement page | The Statements page. | Customer account statement, under Enquiries and reports > Customers. | Statement Preview VG-01, Statement Distribution VG-01 | Test S12.1. |
| 5 | Statement sending | Select Print management destination and generate: D365 sends it. | Run as a batch job with a future start time and Maximum retries 0, or the customer gets several copies. | Statement Distribution VG-05, VG-07, VG-17 | SME B5.1 and B5.2 before test S13. |
| 6 | Transfer offsets | Ledger offset and the clearing account on every line. | Source line Ledger 100949; destination line Bank 1001. The legacy topic contradicts itself. | TF-04, PC-03 | Recording P2-C3. |
| 7 | Transfer approval | Approval not confirmed and out of scope. | Approval > Report as ready; the Receipting team approves; then Post. | CPJ-16, CPJ-17 | SME P2-A3. |
| 8 | Who prepares transfers | To be confirmed. | Collections Officer (230 §6.7). Receipting Officer for manual payment journals (220 §4). | GOV-01 | SME P2-A1. |
| 9 | Open and closed transactions | Show open; Show closed. | One Show field with Open and All. | Customer Account VG-06 | Test S8.4. |
| 10 | Invoice copy route | Highlight the transaction > Original document > Print preview. | Open customer invoices or Tax invoice journal > Document > View > Copy preview. | Customer Invoices VG-03 to VG-05, VG-07 | Test S10.1: record both routes. |
| 11 | Stream and process area | Accounts Receivable; AR Collections. | O2C; Collections. | A2 items in all 13 guides | SME A2. |
| 12 | Opening a customer from Aged balances | Out of the Aged Balances guide (proposed D2.1). | Part of the legacy monitoring task: click the customer name to open the Collections page. | Aged Balances VG-23, Customer Account VG-03 | Decision D2.1. |
| 13 | Customer Pools | No source covers Customer Pools (D-035). | Collections PG §3 covers pools and agents. | CP-01 to CP-07 | SME P2-E1. |

---

## 6. Legacy controls the drafts don't have yet

Rules or checks in the legacy PGs with no counterpart in the drafts, highest risk first. Each needs SME confirmation before it goes into a guide.

| # | Control | Legacy source | Draft it belongs in | Why it matters |
|---|---|---|---|---|
| 1 | Set the statement batch job's start time in the future and **Maximum retries** to 0. | 230 §1 steps 6 to 19 | Statement Distribution | Without it, "the system will send multiple copies to the customer". |
| 2 | A blank **Records to include** sends statements to every customer. | 230 §1 step 5 | Statement Distribution, Statement Preview | One missed filter sends statements to the whole ledger. |
| 3 | Monthly statements go out automatically on the 5th. The task is for ad hoc sends only. | 230 §1 | Statement Distribution | Stops duplicate or unnecessary sends near the monthly run. |
| 4 | Only email contacts with **Purpose = Business** receive statements, invoices and letters. | 230 Key concepts; 200 §3.4 | Statement Distribution; contacts backlog item (rank 21) | It answers the recipient source (Statement Distribution VG-06) and explains the failed-delivery causes in 200 Troubleshooting. |
| 5 | Customer payment journals go through approval (Report as ready); the journal name decides whether approval applies. | 230 §6.7; 220 §4.1 | All three Part 2 guides; CPJL reference | The drafts post directly, with approval unconfirmed. |
| 6 | If the currencies differ, stop and escalate. | 220 §4.2 step 9 | CPJL reference | Fills the open half of CPJ-07. |
| 7 | Attaching supporting documents to an activity is mandatory. | 230 §5, §7 | Collection Activities | Audit requirement stated as mandatory. |
| 8 | Record the write-off activity before submitting the journal for approval. | 230 §6.4 step 14 | Write-off backlog items (ranks 18 to 19) | Keeps the approval auditable. |
| 9 | Aging balances refresh by batch job every 10 minutes. | 230 §6.8 step 13 | Aged Balances | A change posted in the last 10 minutes can be missing from the page. |

---

## 7. Legacy content not in the drafts

### 7.1 Backlog items not yet drafted

| Rank | Backlog item | Legacy coverage | Legacy source | Notes |
|---|---|---|---|---|
| 14 | Investigate unallocated payments | **Partial** | 220 §2.2; Key concepts | Receipting posts unresolved payments On account and refers them to Collections. The Collections side is not described. |
| 15 | Settle customer transactions | **Covered** | 230 §6.5; 220 §4.2 | Show Open, Settlements, Mark, Total settlement amount 0.00, Post. |
| 16 | Review and undo settlements | **Covered** | 230 §6.6 | Show All, open the voucher, Settlements > Undo settlement, Mark, Reverse. |
| 18 | Write off a customer transaction | **Covered** | 230 §6.4, §6.8 | Debt write-off (emailed request, Group Billing and Credit Manager processes) and bank fee write-off, with reason codes. |
| 19 | Validate and submit a write-off journal | **Covered** | 230 §6.4 steps 12 to 15; §6.8 steps 10 to 12 | General journals, Simulate posting, Approval > Report as ready. |
| 20 | Cancel an unposted write-off | **Missing** | — | — |
| 21 | Maintain customer contacts | **Covered** | 230 §2.3; 200 §3.4 | Full steps, plus the CW1 sync rules. |
| 22 | Maintain customer addresses | **Covered** | 200 §3.3 | Written for the License Management Administrator. |
| 23 | Add an invoice-only address | **Partial** | 200 §3.3 | Address Purpose includes Invoice; no invoice-only steps. |
| 24 | Exclude a customer from credit management | **Covered** | 230 §6.3 steps 14 to 18; §6.5 steps 11 to 13 | Customer and transaction level. Excludes collection letters and direct debit runs. |
| 25 | Exclude a customer from statements | **Missing** | — | The credit management exclusion is a different setting. |
| 26 | Identify parent-child accounts | **Missing** | — | — |
| 28 | Search the custom transaction report | **Partial** | 230, 210 Part 3 | Standard Transactions and Open transactions reports only. |
| 29 | Review daily bank statements | **Partial** | 220 §2 | BankFabric import and Process customer settlements, owned by Receipting. |
| 30 | Change customer payment terms | **Covered** | 200 §3.7 | Terms of payment (standard NET14 or NET30). |
| 31 | Maintain direct debit | **Covered** | 230 §2.4; 220 §5 | Since v2.1 (April 2026), the Collections PG gives Collections Officers direct debit and eBanking maintenance. The training excluded direct debit, so the scope decision is still open. |
| 32 | Maintain credit cards | **Missing** | — | Named only as a direct debit opt-out example. |

### 7.2 Legacy tasks not in the backlog

| Legacy topic | Source | Suggested treatment |
|---|---|---|
| Change customer account status (on hold, collection agency, legal process), with status and reason lists | 230 §6.3 | New PG candidate. Higher-risk: it blocks invoicing and delivery. |
| Create and send a collection letter when automation fails | 230 §6.2 | New PG candidate. |
| Update and close a customer activity (resolution, attachments, Set as complete; statuses Open, In Progress, Resolved, Closed) | 230 §7; Key concepts | Add to Collection Activities as a second topic, or a new PG. |
| Resend an invoice to a customer | 230 §6.1 | Answers Customer Invoices VG-21. New PG candidate. |
| Reverse a customer payment journal | 220 §4.3 | Answers CPJ-19. A topic in the CPJL set, or a new PG. |
| Collections timeline and automation: pre-due reminder, three letters, exclusion effects | 230 Key concepts | Knowledge article for Module 2. |
| CW1 and D365 contact integration rules | 230, 200 Key concepts | Reference for Module 3 (D365 and CargoWise synchronisation). |

### 7.3 Outside AR Collections scope

Owned by other teams, so not needed in this pathway: ExFlow remittance exceptions, settlement and parse rules, and alternate customer names (Receipting, 220 §1 to §3); onboarding after CW1 sync, sales order defaults and tax details (License Management, 200); invoicing, bulk upload and credit notes (Billing, 210); subscription billing (211). Process customer settlements matters only as the source of the unallocated payments in rank 14.

---

## 8. Issues found in the legacy PGs

For the legacy review. None of these changes the analysis above.

- **230 §6.7 offsets contradict each other.** The source line uses Ledger 100949. The destination line uses Bank and "the same Bank account (e.g., 1001) used on the debit line".
- **230 roles matrix.** Row 2.5 gives the Collections Officer responsibility for Customer Pool configuration; §3 gives it to managers.
- **230 §6.1** is titled "Resend Statement or Invoice" but covers invoices only. The roles matrix calls it "Send Individual Invoice to Customer".
- **230 prerequisites copied across topics.** §6.5 to §6.8 and §7 all say "the required account status and reason for the change must be confirmed".
- **230 Key concepts.** The activity status table describes "a customer account status". The Customer Payment Management table labels its description column "Timing".
- **230 §1.** Step 13 refers to "steps 2-10". Step 19 says "After you have deleted the Maximum retries field" (it is set to 0, not deleted).
- **"D366"** appears in place of D365 several times in 230.
- **220.** The roles table links rows 3 and 4 to the wrong topics, and the Process table has no *When* for steps 3 and 4. "Receiving Officer" appears for Receipting Officer. The topic list numbers direct debit 4.4 but the topic is 5. The ExFlow link points to a test sign-up URL.
- **200.** Topic 1 Responsibility reads "The XXX is responsible for XXXX". The topic list cites 3.8 Financial dimensions and 3.9 Tax, but 3.8 is Tax and there is no Financial dimensions topic. Troubleshooting has "Warehouse = DFF".
- **Screenshots show real customer names and vouchers** (for example in 230 §2.1 and §6.8). They can't be reused without masking (SME question A8).
- **Additional Resources** still say "during go-live and early adoption".

---

## 9. Recommended next steps

1. **Raise the two statement controls now** (section 6, rows 1 and 2) with SME questions B5.1 and B5.2, and add them to the S13 gate in the [clean-session test plan](Clean-Session-Test-Plan.md).
2. **Use the strong legacy answers as proposed answers in the SME packs.** For A1, A2, A3, A7, B3.1, B5.1, B5.2, B6, B7, B9, B11, P2-A1, P2-A2, P2-A3, P2-B2, P2-B4, P2-B9, P2-B10, P2-C2, P2-D2, P2-E1, P2-E2, the SME then confirms or corrects instead of writing from scratch.
3. **Give the test the legacy labels as expected values.** Where they differ from the drafts (section 5: Customer payment journal path, activity controls, statement page, open and closed transactions, invoice copy route), record which one D365 shows.
4. **Reopen Customer Pools** (D-035) with Collections PG §3 as evidence. If P2-E1 is yes, Customer Pools meets most of the definition of ready.
5. **Reopen the deferred aging-indicator items** (Aged Balances VG-10, Overdue Customers VG-12) with the legacy legend, and add a check of the icons to test station S6.
6. **Settle the transfer offsets from the recording** (TF-04, PC-03). The legacy topic contradicts itself, so it can't decide this.
7. **Update the backlog.** Mark the ranks in section 7.1 that have legacy content as source-reviewed against the legacy PGs, and decide whether the tasks in section 7.2 join the backlog.

## Change log

| Date | Change |
|---|---|
| 2026-10-25 | Analysis created from the five legacy O2C PGs and the 15 validation registers. |
