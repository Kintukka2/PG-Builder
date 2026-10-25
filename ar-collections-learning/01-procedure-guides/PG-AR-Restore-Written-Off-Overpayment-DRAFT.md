# D365 F&O: AR Collections Restore a Written-Off or Overpayment Amount Procedure Guide

> **WORKING DRAFT. Not validated, not approved, not for publication.**
>
> This is a working Markdown draft built from the *AR Training D365* Part 2 update pack. It follows the section order of the PG master template, but it has not been built in Word yet (decision D-037). The Word build follows once the Part 2 recording has been checked.
>
> **Higher-risk guide.** It reinstates an amount on a customer account, and it is related to write-offs. Do not use it on real customer accounts, and do not finalise it, until its blocking items close (source 3.1; README development gates).
>
> **Evidence.** The steps come from Teams AI-generated notes of the Part 2 session and the pack's working draft (sources 4.0 and 4.6). Neither has been checked against the recording (`SRC-01`). `[XX-nn]` markers point to items in the [validation register](../03-validation/Part2-CPJL-and-Transfers-Validation.md). Where the notes do not give a detail precisely enough, the step carries a **validation placeholder** instead of a guess. The [step evidence](#step-evidence) table shows the source of each step.

## Document control

| Field | Value |
|---|---|
| Guide code and final title | To be confirmed `[GOV-03]` |
| Version | 0.1 working draft, October 2026. Author: Daniel Moreira. |
| Business process owner | To be confirmed `[GOV-02]` |
| Status and gate | Working draft. Gate: Drafted (working Markdown). Next: check against the Part 2 recording, then build in the master template. |
| Roadmap | Part 2 roadmap item 18, Release 3A (proposed D-036). New to the backlog. |
| Shared controls | [Customer Payment Journal controls reference](../06-reference-guides/REF-AR-Customer-Payment-Journal-Controls-DRAFT.md) |
| Screenshot register | [PG-AR-Restore-Written-Off-Overpayment-Screenshots.md](../02-screenshot-registers/PG-AR-Restore-Written-Off-Overpayment-Screenshots.md) |

**Version history**

| ID | Date | Author/s | BPO | Description of change |
|---|---|---|---|---|
| 0.1 | October 2026 | Daniel Moreira | To be confirmed `[GOV-02]` | Working draft created from the AR Training D365 Part 2 update pack. Not validated or approved. |

---

## Part 1: What do I need to know? (AR Collections Restore a Written-Off or Overpayment Amount)

### High-level process

##### Part Description

This guide explains how to put an amount back on a customer account with a **Customer payment journal** (CPJL), including a written-off amount that needs to be reinstated. The journal has one line: a credit on the customer account, with the Overpayment ledger as the offset.

Moving funds between customer accounts is covered in the *Transfer Funds Between Customer Accounts* guide. Writing off a customer transaction is a separate backlog item (ranks 18 to 20; not drafted).

Out of scope until confirmed: when a write-off should be reversed or cancelled instead of restored (`RO-02`), approval (`CPJ-17`, `RO-03`) and correcting or reversing a posted journal (`CPJ-19`).

##### Initiation

- An overpayment or a written-off amount must be put back on a customer account. `[RO-04]`

##### Stream

| Stream | Process Area | Key Roles |
|---|---|---|
| Accounts Receivable `[GOV-01]` | AR Collections `[GOV-01]` | • To be confirmed `[GOV-01]` |

##### Process

| # | Action | Who | When | Where |
|---|---|---|---|---|
| 1 | [Restore an Amount to a Customer Account](#1-restore-an-amount-to-a-customer-account) | To be confirmed `[GOV-01]` | When an overpayment or written-off amount must be put back on a customer account | D365 |

### Roles and responsibilities

##### Overview

The sources do not say which business role prepares this journal, who authorizes a restoration (`RO-03`), which role may post it (`CPJ-16`) or whether it needs approval (`CPJ-17`).

| Tasks / Business Roles | To be confirmed `[GOV-01]` |
|---|---|
| [Restore an Amount to a Customer Account](#1-restore-an-amount-to-a-customer-account) | R |

### Key concepts

##### Overview

Before you start, you need to know which journal and offset account a restoration uses, and which fields to leave as they are.

##### Restoration entry

| Term | Description |
|---|---|
| **Customer payment journal (CPJL)** | The journal used to put a written-off or overpayment amount back on a customer account. `[CPJ-02]` |
| **Credit to the customer** | An amount being returned to the customer account is entered as a credit. `[CPJ-06]` |
| **Overpayment ledger** | The main account used as the offset for a restoration entry. `[RO-01]` |
| **Written-off or overpayment amount** | The notes cover both with the same entry. Whether they are always the same procedure is not confirmed. `[RO-02]` |

##### Before you post

| Rule | Description |
|---|---|
| **Authorization** | The notes do not say who authorizes a restoration, or what evidence is kept. Not confirmed. `[RO-03]` |
| **Use the original currency** | The currency must match the original transaction. `[CPJ-07]` |
| **Describe the entry** | Use a clear description that includes the customer code, for example "Overpayment put back on customer account". `[CPJ-03, CPJ-04]` |
| **Leave unsupported fields blank** | Do not enter financial tags, an invoice number or a bank account. `[CPJ-10]` |
| **Keep pre-populated dimensions** | Do not change the financial dimensions that fill in automatically. `[CPJ-11]` |
| **Simulate before posting** | Run Simulate Posting and resolve every error before you post. `[CPJ-14]` |

---

## Part 2: How do I do it? (AR Collections Restore a Written-Off or Overpayment Amount)

### 1. Restore an Amount to a Customer Account

##### Description

Use this topic to put a written-off or overpayment amount back on a customer account. You create a CPJL journal with one credit line for the customer, offset to the Overpayment ledger, then run Simulate Posting and post.

##### Responsibility

- To be confirmed: prepares and posts the restoration journal. `[GOV-01, CPJ-16]`

##### Initiation

- An overpayment or a written-off amount must be put back on a customer account. `[RO-04]`

##### Topic Overview

This topic includes these steps:

| Step | Description |
|---|---|
| [Create the Restoration Line](#11-create-the-restoration-line) | Create the CPJL and enter the customer credit with the Overpayment ledger offset. Output: the line is complete. |
| [Validate and Post the Journal](#12-validate-and-post-the-journal) | Run Simulate Posting, correct errors and post. Output: the amount is back on the customer account. |

#### 1.1 Create the Restoration Line

##### Procedure

Complete these steps to create the restoration line:

| Action | Description |
|---|---|
| *PROCESS START* (light blue) | *Pre-requisites:*<br>• Access to D365 and to **Customer payment journal**. `[CPJ-21]`<br>• The customer account, the amount and the currency of the original transaction.<br>• Whether the restoration needs authorization is not confirmed. `[RO-03]`<br>*Responsibility:*<br>• To be confirmed `[GOV-01]` |
| 1. *Check* the **Entity**. | Confirm you are signed into the correct **Legal Entity** (top-right). |
| 2. *Open* **Customer payment journal**. `[CPJ-01]` | The Favorites guide places **Customer payment journal** in the **Credit and collections** module. If you have added it to your favorites, open it from there.<br>**Validation placeholder (`CPJ-01`):** exact navigation path. |
| 3. *Create* a new journal. `[CPJ-01, CPJ-02]` | Start a new CPJL journal.<br>**Validation placeholder (`CPJ-01`, `CPJ-02`):** the control that creates the journal, and how the CPJL journal name is selected. |
| 4. *Enter* the journal description. `[CPJ-03, CPJ-04]` | Use a clear description that includes the customer code, for example "Overpayment put back on customer account". |
| 5. *Open* the journal lines. `[CPJ-01]` | **Validation placeholder (`CPJ-01`):** how the journal lines are opened from the journal. |
| 6. *Enter* the transaction date. `[CPJ-05]` | Use the current date, unless a valid prior-period date is required and the period is open.<br>**Validation placeholder (`CPJ-05`):** the date field label, whether the date is set on the journal or on the line, and who decides on a prior-period date. |
| 7. *Select* the customer account. | Select the customer account the amount is being returned to. The customer name fills in automatically. |
| 8. *Enter* the amount as a credit. `[CPJ-06]` | Enter the amount being returned to the customer account as a credit.<br>**Validation placeholder (`CPJ-06`):** how credits are entered. |
| 9. *Check* the currency. `[CPJ-07]` | Confirm the currency matches the original transaction. |
| 10. *Enter* the line description. `[CPJ-03, CPJ-04]` | Use the same clear description, so the entry can be identified in the customer's history. |
| 11. *Leave* the financial tags, invoice number and bank account blank. `[CPJ-10]` | Do not enter a value in these fields.<br>**Validation placeholder (`CPJ-10`):** the exact field labels. |
| 12. *Select* **Ledger** as the **Offset account type**. `[CPJ-08]` | Set the offset account type to **Ledger**. |
| 13. *Select* the Overpayment ledger. `[RO-01, CPJ-08]` | Search for the Overpayment ledger in the main account field, and select it.<br>**Validation placeholder (`RO-01`):** the account label, value and lookup term. |
| 14. *Leave* the financial dimensions unchanged. `[CPJ-11]` | Do not change the dimensions that fill in automatically. |
| 15. *Complete* the line. `[CPJ-12]` | Tab through every field in the line before you create another line, so that fields such as the voucher fill in correctly. |
| *STEP COMPLETE* (light blue) | • *The restoration line is complete.*<br>• *Continue to [Validate and Post the Journal](#12-validate-and-post-the-journal)* |

#### 1.2 Validate and Post the Journal

##### Procedure

Complete these steps to validate and post the journal:

| Action | Description |
|---|---|
| *PROCESS START* (light blue) | *Pre-requisites:*<br>• The restoration line is complete (see [Create the Restoration Line](#11-create-the-restoration-line)).<br>*Responsibility:*<br>• To be confirmed `[GOV-01]` |
| 1. *Run* **Simulate Posting**. `[CPJ-14]` | Check the journal before posting. The notes describe a blue result as ready to post.<br>**Validation placeholder (`CPJ-14`):** the control's label and location. |
| 2. *Correct* any errors. `[CPJ-15]` | If Simulate Posting shows an error, read it, correct the line, and run Simulate Posting again. If you cannot resolve the error, ask for help before you post.<br>**Validation placeholder (`CPJ-15`):** the support route. |
| 3. *Post* the journal. `[CPJ-16, CPJ-17]` | Post only when the line is complete and Simulate Posting succeeds.<br>**Validation placeholder (`CPJ-16`, `CPJ-17`):** the Post control, who may post, and whether approval is needed. |
| 4. *Verify* the restoration. `[CPJ-18]` | **Validation placeholder (`CPJ-18`):** how to confirm the amount is back on the customer account after posting. |
| *PROCESS COMPLETE* (light green) | *Outcomes:*<br>• A CPJL is posted with a credit on the customer account and the Overpayment ledger as the offset.<br>• The entry can be identified by its description in the customer's history.<br>• If the posted journal is wrong, the correction process is not yet confirmed. `[CPJ-19]` |

---

## Part 3: Reports (AR Collections Restore a Written-Off or Overpayment Amount)

##### Overview

Reports for this process are pending SME confirmation. `[GOV-04]`

---

## Related content

| Item | Relationship |
|---|---|
| [Customer Payment Journal controls reference](../06-reference-guides/REF-AR-Customer-Payment-Journal-Controls-DRAFT.md) | The shared CPJL controls this guide applies. |
| [Transfer Funds Between Customer Accounts](PG-AR-Transfer-Funds-Between-Customer-Accounts-DRAFT.md) | The other CPJL guide from Part 2. |
| Write off a customer transaction; validate and submit a write-off journal; cancel an unposted write-off (backlog ranks 18 to 20) | Not drafted. Related through `RO-02`. |
| [AR Collections Overdue Customers](PG-AR-Overdue-Customers-DRAFT.md) | Checks whether a low-value overdue balance is an overpayment. |
| [AR Collections Customer Account](PG-AR-Customer-Account-DRAFT.md) | Reviewing customer transactions. A possible way to check the result after posting; not confirmed (`CPJ-18`). |

## Step evidence

| Step | Source | Status |
|---|---|---|
| 1.1.1 | Template standard navigation pattern (D-015) | Pattern |
| 1.1.2 | Favorites guide (recording frame 00:33:51); Part 2 notes | Location from Part 1; path is a placeholder |
| 1.1.3, 1.1.5 | Implied by the Part 2 notes (header and lines) | Placeholders |
| 1.1.4, 1.1.6 to 1.1.9, 1.1.11 to 1.1.15 | Part 2 notes; pack draft steps 2 to 11 | Stated in notes; recording check pending |
| 1.1.10 | Shared CPJL control (line descriptions); not in the pack's restore draft | Stated in notes for CPJL generally |
| 1.2.1 to 1.2.3 | Part 2 notes; pack draft steps 12 and 13 | Stated in notes; controls and posting rules open |
| 1.2.4 | Listed as a gap in the pack draft | Placeholder |

## Draft validation notes

All items are in the [validation register](../03-validation/Part2-CPJL-and-Transfers-Validation.md).

- **Source:** recording check `SRC-01`; timestamps `SRC-02`.
- **Scope and authority:** written-off versus overpayment `RO-02`; who authorizes `RO-03`.
- **Labels and navigation:** `CPJ-01` to `CPJ-03`, `CPJ-08`, `CPJ-14`, `CPJ-16`.
- **Accounts:** Overpayment ledger `RO-01`; account numbers in guides `CPJ-09`.
- **Business rules:** dates and backdating `CPJ-05`, credit entry `CPJ-06`, currency `CPJ-07`, blank fields `CPJ-10`, dimension exceptions `CPJ-11`, description standard `CPJ-04`.
- **Controls:** errors and support `CPJ-15`, posting permission `CPJ-16`, approval `CPJ-17`, verification `CPJ-18`, reversal `CPJ-19`, security role `CPJ-21`.
- **Governance:** initiation `RO-04`, role `GOV-01`, BPO `GOV-02`, code and title `GOV-03`, reports `GOV-04`, review and approval `GOV-05`.
