# SME Question Pack: Part 2 Supplement (Customer Payment Journals and Transfers)

| Field | Value |
|---|---|
| Covers | 50 open items (42 blocking): 43 from the [Part 2 validation register](Part2-CPJL-and-Transfers-Validation.md) and 7 from the [Customer Pools register](Customer-Pools-Validation.md) |
| Questions | 27, grouped so each rule is answered once for every guide that uses it |
| Guides | AR Collections Customer Account Transfers, Parent Payment Distribution and Overpayment and Write-Off Restoration, and the Customer Payment Journal Controls reference (v0.1 SME review drafts) |
| Response sheet | [`SME-Question-Pack-Part2-Responses.xlsx`](SME-Question-Pack-Part2-Responses.xlsx): one row per answer, plus an index of every item |
| Companion | The main [SME question pack](SME-Question-Pack.md) covers the first 13 guides. This supplement uses `P2-` IDs so the two never clash. |
| Not in this pack | `CPJ-06`, `CPJ-08`, `CPJ-13` need a D365 test only. The clean-session test plan has no Customer payment journal station yet; they need a controlled test in a test environment. |
| Legacy PG proposals | 11 questions (16 items) show a proposed answer from the legacy O2C procedure guides, where the [legacy cross-comparison](Legacy-O2C-PG-Cross-Comparison.md) rates the evidence strong. |
| Status | Draft for SME review. No answers yet. Legacy PG proposals added 2026-10-26. |
| Last updated | 2026-10-26 |

## Why this matters

These guides move or reinstate customer funds. They were built from Teams AI-generated notes of the Part 2 session, which no one has yet checked against the recording. Until the blocking items here are answered, the guides are not used on real customer accounts and not finalised.

## How to answer

- Answer in the response sheet or directly in this document, quoting the question ID (for example **P2-B4**).
- "Don't know" or "Ask someone else" is a useful answer: name who to ask.
- A **Legacy PG proposal** comes from the legacy O2C procedure guides, which are reference evidence only (D-044; see the [legacy cross-comparison](Legacy-O2C-PG-Cross-Comparison.md)). Confirm it, correct it, or say it no longer applies. A proposal is not an answer: an item closes only on your answer.
- Where a document exists (an account list, a journal procedure, an approval policy), attach it rather than summarising it.
- Nothing here is final until answered. The guides show these items as review comments, and nothing is invented to fill them.

## Answer these first

| Priority | Questions | Why |
|---|---|---|
| 1 | **P2-C1** | The recording check. Every step depends on it. |
| 2 | **P2-A1** and **P2-A3** | Who may post and what needs approval. Without them, no one can use the guides on a real account. |
| 3 | **P2-B4**, **P2-B1** and **P2-B5** | The account values, the date rule and the fields to leave alone. Every journal needs them. |
| 4 | **P2-B7**, **P2-B8** and **P2-B9** | The parent-child method, the restoration scope, and correcting a posted journal. |
| 5 | **P2-E1** | One answer on Customer Pools decides whether the rest of Part E is needed. |

---

## Part A: Governance and control (the BPO or SME lead)

Who does this work, who may post, and what needs approval. These answers decide whether the guides can ever be used on real customer accounts.

### P2-A1 Role, posting and access

**Question.** Which team and business role prepare these journals: Collections Officers or another team? Which role may post a Customer payment journal (CPJL)? Which security role is needed to create and post one?

**Current draft or evidence.** All three guides show the role as "To be confirmed". The notes do not say who may post. The guides do not name a security role.

**Legacy PG proposal (CPJ-16; confirm or correct).** **Post** is on the Main toolbar. A journal that needs approval shows the **Approval** button and hides **Post** until it is approved; the journal is posted after approval. As partial evidence only, the legacy PGs have the Collections Officer prepare transfers between customer accounts and the Receipting Officer create manual payment journals. The security role (CPJ-21) is not covered. *Source: 230 §6.7 steps 23 to 25 and Roles; 220 §4.1 steps 9 to 11 and Roles.*

**Answers:** GOV-01 (B), CPJ-16 (B), CPJ-21 (B).

**Answer:**

> 

### P2-A2 Business process owner

**Question.** Who is the business process owner (BPO) for each of the three guides and the reference?

**Current draft or evidence.** To be confirmed in all four documents.

**Legacy PG proposal (confirm or correct).** **Christoper Clarke**, the BPO on every version of the legacy Collections PG, which includes the transfer procedure (230 §6.7). The version history spells the name this way: please confirm the spelling. *Source: 230 version history.*

**Answers:** GOV-02 (B).

**Answer:**

> 

### P2-A3 Approval and authorization

**Question.** Do CPJL transfers, distributions or restorations need approval (for example a workflow)? Is there a value threshold? Who authorizes putting a written-off or overpayment amount back on a customer account, and what evidence is kept?

**Current draft or evidence.** The guides say approval is not confirmed. The amounts in the training ($100; $10,000, $8,000 and $2,000) are treated as examples, not thresholds.

**Legacy PG proposal (CPJ-17; confirm or correct).** Yes. After Simulate posting, **Approval > Report as ready** routes the journal. A user who is not an approver asks the **Receipting team** to approve it (Options > Share > Get a link gives a link to the journal). The approver clicks **Approve**, then the journal is posted. The journal name decides whether approval applies: "The journal name controls posting behavior and approval workflow." No value threshold is stated, and who authorizes a restoration (RO-03) is not covered. *Source: 230 §6.7 steps 22 to 25; 220 §4.1 steps 5 and 9 to 11.*

**Answers:** CPJ-17 (B), RO-03 (B).

**Answer:**

> 

### P2-A4 When each task starts

**Question.** What events start each task? Confirm or add to the triggers the notes give.

**Current draft or evidence.** Transfer: a payment posted to the wrong customer account, or funds to move to a confirmed related account. Distribution: a parent-account payment to distribute to confirmed child accounts. Restoration: an overpayment or written-off amount to put back on a customer account (the notes give no trigger).

**Answers:** TF-01 (B), PC-06 (B), RO-04 (B).

**Answer:**

> 

### P2-A5 Reports

**Question.** Do any reports or inquiries support these processes? If none, the guides will say "No applicable reports".

**Current draft or evidence.** Pending in all four documents.

**Answers:** GOV-04 (B).

**Answer:**

> 

### P2-A6 Review, test and approval

**Question.** Who reviews the four documents for accuracy, who tests them (someone other than the author), and who approves them?

**Current draft or evidence.** Not assigned.

**Answers:** GOV-05 (B).

**Answer:**

> 

---

## Part B: Business rules (the AR Collections SME)

The rules the Part 2 notes state only partly, or not at all.

### P2-B1 Dates and backdating

**Question.** Which date should a CPJL use? When may a wrong-account correction use the original payment date, when may a prior-period date be used, and who decides? Is the date set on the journal or on each line?

**Current draft or evidence.** Notes: the current date is the default. Transfer notes: the original payment date "when appropriate". Restoration notes: a prior-period date only when required and the period is open. The parent-payment notes give no date rule.

**Answers:** CPJ-05 (B).

**Answer:**

> 

### P2-B2 Currency

**Question.** How does the currency field behave on a CPJL line? What should a user do if the original currency cannot be used?

**Current draft or evidence.** Every line uses the currency of the original payment or transaction.

**Legacy PG proposal (confirm or correct).** **Currency** fills in from the line's **Account**. Confirm it matches the currency of the original receipt. If the currencies differ, stop and escalate before going on. *Source: 230 §6.7 steps 12 and 19; 220 §4.2 step 9.*

**Answers:** CPJ-07 (B).

**Answer:**

> 

### P2-B3 Descriptions

**Question.** Is there a standard for journal and line descriptions (wording, customer codes, references)?

**Current draft or evidence.** Examples only: "Transfer funds from customer A to customer B"; "Overpayment put back on customer account".

**Answers:** CPJ-04.

**Answer:**

> 

### P2-B4 Account values

**Question.** What are the exact name and value of the bank-to-bank transfer clearing account, and of the Overpayment ledger (main account)? What lookup term do users search for?

**Current draft or evidence.** Transfers and distributions use the bank-to-bank transfer clearing account. Restorations use the Overpayment ledger. No account values are in the guides.

**Legacy PG proposal (TF-03; confirm or correct).** The legacy transfer procedure sets the source line's **Offset account type** to **Ledger** and its **Offset account** to **100949**, "to ensure no impact to the bank". It does not give the account's name. Its destination line uses Bank instead, which contradicts this (see P2-C3). The Overpayment ledger (RO-01) is not covered. *Source: 230 §6.7 steps 13 to 14 and 20 to 21.*

**Answers:** TF-03 (B), RO-01 (B).

**Answer:**

> 

### P2-B5 Blank fields and dimensions

**Question.** Which fields must be left blank (financial tags, invoice number, bank account) and what are their exact labels? Must pre-populated financial dimensions never be changed, and are there exceptions? Do both rules also apply to transfers and distributions?

**Current draft or evidence.** The notes state both rules for restoration entries only. The Restore guide applies them; the two transfer guides ask the question.

**Answers:** CPJ-10 (B), CPJ-11 (B).

**Answer:**

> 

### P2-B6 Checks before a transfer

**Question.** How is the correct destination account confirmed, and what evidence is kept? What should a user do when the payment is already settled against invoices on the wrong account? Are transfers between customers in different legal entities in scope?

**Current draft or evidence.** The transfer guide makes these prerequisites and puts the last two outside its scope until confirmed.

**Answers:** TF-02 (B), TF-05 (B), TF-06.

**Answer:**

> 

### P2-B7 Parent and child accounts

**Question.** How do users confirm that accounts are parent and child, given that D365 has no reliable indicator? What evidence confirms each child's share? In a partial allocation, where, how and when is the note on the residual added, and who follows up the residual?

**Current draft or evidence.** Part 1 notes: D365 has no reliable parent-child indicator; do not rely on account names. Notes: confirm from remittance, customer confirmation or other validated evidence; leave the residual on the parent with a note.

**Answers:** PC-01 (B), PC-02 (B), PC-04 (B), PC-05.

**Answer:**

> 

### P2-B8 Restoration scope

**Question.** Are restoring a written-off amount and putting an overpayment back the same procedure? When should a write-off be reversed or cancelled instead of restored?

**Current draft or evidence.** The Restore guide covers both with one entry: a customer credit offset to the Overpayment ledger. Write-off processing is a separate backlog item (ranks 18 to 20).

**Answers:** RO-02 (B).

**Answer:**

> 

### P2-B9 After posting

**Question.** How should users check the result after posting? How is a posted journal corrected or reversed? What should a user do with an unposted journal that is no longer needed?

**Current draft or evidence.** The guides end with a check step whose method is open, and state that correction is not yet confirmed. Unposted journals appear under Payment journals not posted in the workspace.

**Legacy PG proposal (CPJ-19; confirm or correct).** To reverse a posted journal: **Accounts receivable > Payments > Customer payment journals**, open the journal batch, select the payment line, click **Voucher**, then **Reverse transactions**. Set **Use existing date for reversal** (Yes keeps the original posting date) or enter a **Reversal date**, and enter a **Reason comment**. Click **Reverse**, then **Post**. Checking the result (CPJ-18) and unposted journals (CPJ-20) are not covered. *Source: 220 §4.3.*

**Answers:** CPJ-18 (B), CPJ-19 (B), CPJ-20.

**Answer:**

> 

### P2-B10 Errors and support

**Question.** What are the common Simulate Posting errors and their fixes? Where should users go when they cannot resolve one? Does "PG/Ava follow-up support" in the notes mean the Procedure Guides and AVA (Atlas Virtual Assistant)?

**Current draft or evidence.** During training, errors were escalated to "SYD". The guides point to the D365 issue form, the template's standard route. The template already lists AVA and Procedure Guides under Additional Resources.

**Legacy PG proposal (SRC-03; confirm or correct).** Yes. The legacy PGs list **AVA - Atlas Virtual Assistant**, "your AI assistant for navigating the Procedure Guides", and the **Procedure Guides** as self-service resources. Simulate Posting errors (CPJ-15) are covered only as "a journal does not post while approval is pending or a validation error remains". *Source: 230 and 200 Additional Resources; 220 Troubleshooting.*

**Answers:** CPJ-15 (B), SRC-03.

**Answer:**

> 

---

## Part C: Recording (whoever holds the AR Training D365 Part 2 recording)

The Part 2 notes are Teams AI-generated. These checks compare them with the recording, and capture the labels the notes do not give.

### P2-C1 Check the guides against the recording

**Question.** Compare each step in the three guides and each control in the reference with the Part 2 recording or transcript. Mark any step that differs, is missing or was not demonstrated.

**Current draft or evidence.** Every step comes from Teams AI-generated notes. The step-evidence table in each guide preview shows the source of each step.

**Answers:** SRC-01 (B).

**Answer:**

> 

### P2-C2 Labels and navigation in the recording

**Question.** From the recording, note the exact labels of: the menu path to Customer payment journal; the control that creates a journal; how the CPJL journal name is selected; how the journal lines are opened and a new line is added; the header and line Description fields; and Simulate Posting, with how its result is shown.

**Current draft or evidence.** The guides name these actions without labels (D-020). Simulate Posting results are described as blue (ready) and red (errors).

**Legacy PG proposal (CPJ-01, CPJ-02, CPJ-03, CPJ-14; check against the recording).** **+New** creates the journal header. The journal name is selected in the **Name** field (**CPJL**, journal type Customer payments). The header **Description** fills in and is overwritten with the purpose. The **Journal batch number** hyperlink opens the lines, and **+New** adds a line, which has its own **Description**. Simulate Posting is **Validate > Simulate posting** on the Main toolbar; errors appear as messages to correct before validating again. The legacy menu path is **Accounts receivable > Payments > Customer payment journal(s)**, not Credit and collections as in the guides, so check both. *Source: 230 §6.7 steps 3 to 17 and 22; 220 §4.1 steps 3 to 8.*

**Answers:** CPJ-01 (B), CPJ-02 (B), CPJ-03 (B), CPJ-14 (B).

**Answer:**

> 

### P2-C3 Line entry in the recording

**Question.** From the recording: which fields fill in when the trainer tabs through a line; and whether each transfer line (source, destination, parent and each child) takes the Ledger offset and the clearing account.

**Current draft or evidence.** The guides apply the offset to every line, as the pack drafts imply.

**Answers:** CPJ-12, TF-04 (B), PC-03 (B).

**Answer:**

> 

### P2-C4 Timestamps

**Question.** Record the start and end times of the restoration, two-line transfer, parent-to-child distribution, partial allocation and Simulate Posting demonstrations.

**Current draft or evidence.** Not supplied.

**Answers:** SRC-02.

**Answer:**

> 

---

## Part D: Project decisions (project team and BPO)

Decisions the project team makes with the BPO.

### P2-D1 Guide codes and titles

**Question.** Assign codes and confirm final titles for the three guides and the reference (D-006).

**Current draft or evidence.** Working process names: AR Collections Customer Account Transfers, Parent Payment Distribution, Overpayment and Write-Off Restoration, and Customer Payment Journal Controls.

**Answers:** GOV-03 (B).

**Answer:**

> 

### P2-D2 Account numbers in guides

**Question.** Should the guides show the account numbers of the clearing account and the Overpayment ledger, or only the names to search for?

**Current draft or evidence.** No account numbers are shown.

**Legacy PG proposal (confirm or correct).** The legacy Collections PG prints the account number (**100949**) in its transfer steps, so the legacy precedent is to show account numbers. *Source: 230 §6.7 step 14.*

**Answers:** CPJ-09 (B).

**Answer:**

> 

### P2-D3 Release placement

**Question.** Confirm moving *Transfer funds between accounts* (source 2 rank 27) from Release 4 to Release 3, with the new Part 2 items (ranks 33 to 35).

**Current draft or evidence.** Proposed in D-036.

**Answers:** SRC-04.

**Answer:**

> 

---

## Part E: Customer Pools (the AR Collections SME)

Customer Pools is not covered by the Part 1 or Part 2 notes, so no guide is drafted (D-035). One "no" to E1 closes most of this part.

### P2-E1 Use, purpose and owner

**Question.** Does the AR Collections team use Customer Pools? If so, what are they for, and who owns and maintains them?

**Current draft or evidence.** No source describes Customer Pools.

**Legacy PG proposal (confirm or correct).** Yes. The legacy Collections PG v2.3 (October 2026) has a Customer Pools topic. Pools group customer accounts by defined criteria (customer group, legal entity or financial dimensions) and are assigned to Collections agents, to establish customer ownership and support follow-up and workload allocation. Managers (the Group Billing and Credit Manager) create and maintain the pools and the agent assignments. *Source: 230 §3 and Roles.*

**Answers:** CP-01 (B), CP-02 (B), CP-03 (B).

**Answer:**

> 

### P2-E2 Assignment and daily work

**Question.** If they are used: how are customers assigned to a pool, and how do pools affect which customers a user works each day?

**Current draft or evidence.** Not described.

**Legacy PG proposal (CP-04; confirm or correct).** A pool's criteria decide which customers it holds: **Credit and collections > Setup > Customer pools**, **New**, enter the **Pool ID** and **Pool description**, set **Pool type** = Collections, then **Select pool criteria** (Advanced query, **Range** tab: Table, Field, Criteria), **Preview pool customers** and **Save**. Pools reach a user through **Credit and collections > Setup > Collections agents**: add the Worker, add each **Pool ID** and set the **Default pool**. How pools change the daily work list (CP-06) is stated only as "ownership and workload allocation". *Source: 230 §3.1 and §3.2.*

**Answers:** CP-04 (B), CP-06 (B).

**Answer:**

> 

### P2-E3 Demonstration

**Question.** If creating or editing pools is in learner scope, can it be demonstrated or recorded?

**Current draft or evidence.** Not demonstrated in Part 1 or Part 2.

**Answers:** CP-05 (B).

**Answer:**

> 

### P2-E4 Content decision

**Question.** Should Customer Pools be a PG, a knowledge article, or left out of the pathway?

**Current draft or evidence.** Kept as a validation backlog item only (D-035).

**Answers:** CP-07 (B).

**Answer:**

> 

---

## After the answers

1. Record each answer in the response sheet with the person and date.
2. Close each item in the Part 2 or Customer Pools register with the answer as evidence (for example "Closed: SME pack P2-B4, 2026-11-xx"), or keep it open with the partial answer.
3. Update the Word guides and the reference, remove the matching review comments, and move them to v0.2.
4. If P2-E1 confirms that Customer Pools are used, draft them only once they meet the definition of ready (source 2).
5. Update the Command Centre gaps and the project notes decisions.

## Change log

| Date | Change |
|---|---|
| 2026-10-25 | Supplement created from the Part 2 and Customer Pools registers. |
| 2026-10-26 | Legacy PG proposals added to 11 questions (16 items) from the strong evidence in the legacy cross-comparison. The response sheet has a matching column. No answers recorded. |
