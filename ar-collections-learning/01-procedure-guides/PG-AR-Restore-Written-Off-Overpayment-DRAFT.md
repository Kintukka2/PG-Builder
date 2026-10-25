# D365 F&O: AR Collections Overpayment and Write-Off Restoration Procedure Guide

> **SME REVIEW DRAFT. Not validated or approved.**
>
> This is a Markdown preview of the Word guide [`TBC-AR Collections Overpayment and Write-Off Restoration PG v0.1.docx`](TBC-AR%20Collections%20Overpayment%20and%20Write-Off%20Restoration%20PG%20v0.1.docx). That guide was built from the PG master template in [`/templates`](../../templates/). **The Word file is the editable source.**
>
> **Built from AI-generated notes.** The content comes from Teams AI-generated notes of the *AR Training D365* Part 2 session and has not yet been checked against the recording (`SRC-01`). This is a higher-risk guide: do not use it on real customer accounts, and do not finalise it, until its blocking items close.
>
> `[XX-nn]` markers show unconfirmed items. In the Word file, each one is a review comment. Full details are in the [validation register](../03-validation/Part2-CPJL-and-Transfers-Validation.md). The markers are not part of the guide text.

The fixed template content is not repeated here: cover, Contents, *About this guide* and *Additional Resources*.

**Version history**

| ID | Date | Author/s | BPO | Description of change |
|---|---|---|---|---|
| 0.1 | October 2026 | Daniel Moreira | To be confirmed `[GOV-02]` | SME review draft created from the PG master template. Built from the Part 2 notes; not yet checked against the recording, validated or approved. `[SRC-01]` |

Guide code and final title: `[GOV-03]`.

---

## Part 1: What do I need to know? (AR Collections Overpayment and Write-Off Restoration)

### High-level process

##### Part Description

This guide explains how to put an amount back on a customer account with a **Customer payment journal** (CPJL), including a written-off amount that needs to be reinstated. The journal has one line: a credit on the customer account, with the Overpayment ledger as the offset. Moving funds between customer accounts is covered by the AR Collections Customer Account Transfers guide.

When a write-off should be reversed or cancelled instead of restored, approval, and correcting or reversing a posted journal are outside the scope of this guide until confirmed. `[RO-02, CPJ-17, CPJ-19]`

##### Initiation

- An overpayment or a written-off amount must be put back on a customer account. `[RO-04]`

##### Stream

| Stream | Process Area | Key Roles |
|---|---|---|
| Accounts Receivable `[GOV-01]` | AR Collections | • To be confirmed |

##### Process

| # | Action | Who | When | Where |
|---|---|---|---|---|
| 1 | [Restore an Amount to a Customer Account](#1-restore-an-amount-to-a-customer-account) | To be confirmed | When an overpayment or written-off amount must be put back on a customer account | D365 |

### Roles and responsibilities

##### Overview

The business role that prepares and posts this journal is not yet confirmed. `[CPJ-16, CPJ-17]`

| Tasks / Business Roles | To be confirmed |
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
| **Overpayment ledger** | The main account used as the offset for a restoration entry. `[RO-01, CPJ-09]` |

##### Before you post `[RO-03]`

| Rule | Description |
|---|---|
| **Use the original currency** | The currency must match the original transaction. `[CPJ-07]` |
| **Describe the entry** | Use a clear description that includes the customer code, for example "Overpayment put back on customer account". `[CPJ-04]` |
| **Leave unsupported fields blank** | Do not enter financial tags, an invoice number or a bank account. `[CPJ-10]` |
| **Keep pre-populated dimensions** | Do not change the financial dimensions that fill in automatically. `[CPJ-11]` |
| **Simulate before posting** | Run Simulate Posting and resolve every error before you post. |

---

## Part 2: How do I do it? (AR Collections Overpayment and Write-Off Restoration)

### 1. Restore an Amount to a Customer Account

##### Description

Use this topic to put a written-off or overpayment amount back on a customer account. You create a CPJL journal with one credit line for the customer, offset to the Overpayment ledger, then run Simulate Posting and post.

##### Responsibility

- To be confirmed: prepares and posts the restoration journal. `[GOV-01]`

##### Initiation

- An overpayment or a written-off amount must be put back on a customer account.

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
| *PROCESS START* (light blue) | *Pre-requisites:*<br>• Access to D365 and to **Customer payment journal**. `[CPJ-21]`<br>• The customer account, amount and original currency.<br>*Responsibility:*<br>• To be confirmed |
| 1. *Check* the **Entity**. | Confirm you are signed into the correct **Legal Entity** (top-right). |
| 2. *Click* **Modules**. | From the left-hand **Navigation Pane**, click **Modules**. |
| 3. *Navigate* to the **Customer payment journal** page. `[CPJ-01]` | From the **Navigation Pane**, *select*:<br>• **Credit and collections >**<br>• **Customer payment journal**<br>You can also open **Customer payment journal** from your **Favorites** (see the AR Collections Favorites guide). |
| 4. *Create* a new journal. `[CPJ-01, CPJ-02]` | Start a new CPJL journal. |
| 5. *Enter* the journal description. `[CPJ-03]` | Use a clear description that includes the customer code, for example "Overpayment put back on customer account". |
| 6. *Open* the journal lines. `[CPJ-01]` | Open the lines of the new journal. |
| 7. *Enter* the transaction date. `[CPJ-05]` | Use the current date, unless a valid prior-period date is required and the period is open. |
| 8. *Select* the customer account. | Select the customer the amount is returned to. The name fills in automatically. |
| 9. *Enter* the amount as a credit. `[CPJ-06, CPJ-07]` | Enter the amount as a credit, in the currency of the original transaction. |
| 10. *Enter* the line description. `[CPJ-03]` | Use the same description, so the entry shows in the customer's history. |
| 11. *Leave* the other fields blank. `[CPJ-10]` | Do not enter financial tags, an invoice number or a bank account. |
| 12. *Select* **Ledger** as the **Offset account type**. `[CPJ-08]` | Set the offset account type to **Ledger**. |
| 13. *Select* the Overpayment ledger. `[RO-01]` | Search for and select the Overpayment ledger in the main account field. |
| 14. *Keep* the dimensions. `[CPJ-11]` | Do not change the financial dimensions that fill in automatically. |
| 15. *Complete* the line. `[CPJ-12]` | Tab through every field, so fields such as the voucher fill in. |
| *STEP COMPLETE* (light blue) | • *The restoration line is complete.*<br>• *Continue to [Validate and Post the Journal](#12-validate-and-post-the-journal)* |

#### 1.2 Validate and Post the Journal

##### Procedure

Complete these steps to validate and post the journal:

| Action | Description |
|---|---|
| *PROCESS START* (light blue) | *Pre-requisites:*<br>• The restoration line is complete (see [Create the Restoration Line](#11-create-the-restoration-line)).<br>*Responsibility:*<br>• To be confirmed |
| 1. *Run* **Simulate Posting**. `[CPJ-14]` | Check the journal before posting. A blue result means the journal is ready to post. |
| 2. *Correct* any errors. `[CPJ-15]` | If Simulate Posting shows an error, read it, correct the line it names and run Simulate Posting again. If you cannot resolve the error, log a request through the D365 issue form (see **Additional Resources**) before you post. |
| 3. *Post* the journal. `[CPJ-16, CPJ-17]` | Post only when the line is complete and Simulate Posting succeeds. |
| 4. *Verify* the restoration. `[CPJ-18]` | Check that the amount appears with its description on the customer account. |
| *PROCESS COMPLETE* (light green) | *Outcomes:*<br>• A CPJL is posted with a credit on the customer account and the Overpayment ledger as the offset. `[CPJ-19]`<br>• The entry can be identified by its description in the customer's history. |

---

## Part 3: Reports (AR Collections Overpayment and Write-Off Restoration)

##### Overview

Reports for this process are pending SME confirmation. `[GOV-04]`

---

## Additional Resources

The standard template block, unchanged.

---

## Step evidence

*Working note for reviewers; not part of the Word guide.* It shows where each step comes from, so you can see what the notes state and what is still open.

| Step | Source | Status |
|---|---|---|
| 1.1.1, 1.1.2 | Template standard navigation pattern (D-015) | Pattern |
| 1.1.3 | Favorites guide (recording frame 00:33:51) | Module from Part 1; menu group open (`CPJ-01`) |
| 1.1.4, 1.1.6 | Implied by the Part 2 notes (journal header and lines) | Action named without a label (D-020) |
| 1.1.5, 1.1.7 to 1.1.9, 1.1.11 to 1.1.15 | Part 2 notes; pack draft steps 2 to 11 | Stated in notes; recording check pending |
| 1.1.10 | Shared CPJL control (line descriptions); not in the pack's restore draft | Stated in notes for CPJL generally |
| 1.2.1 to 1.2.3 | Part 2 notes; pack draft steps 12 and 13; template support route (D-018) | Stated in notes; controls and posting rules open |
| 1.2.4 | Listed as a gap in the pack draft | Action named; method open (`CPJ-18`) |

