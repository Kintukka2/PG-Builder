# D365 F&O: AR Collections Customer Payment Journal Controls Reference Guide

> **SME REVIEW DRAFT. Not validated or approved.**
>
> This is a Markdown preview of the Word reference [`TBC-AR Collections Customer Payment Journal Controls Reference v0.1.docx`](TBC-AR%20Collections%20Customer%20Payment%20Journal%20Controls%20Reference%20v0.1.docx). That reference was built from the PG master template in [`/templates`](../../templates/). **The Word file is the editable source.**
>
> **Built from AI-generated notes.** The content comes from Teams AI-generated notes of the *AR Training D365* Part 2 session and has not yet been checked against the recording (`SRC-01`). It supports three higher-risk guides and is not finalised until its items close.
>
> `[XX-nn]` markers show unconfirmed items. In the Word file, each one is a review comment. Full details are in the [validation register](../03-validation/Part2-CPJL-and-Transfers-Validation.md). The markers are not part of the reference text.

The fixed template content is not repeated here: cover, Contents, *About this guide* and *Additional Resources*.

**Version history**

| ID | Date | Author/s | BPO | Description of change |
|---|---|---|---|---|
| 0.1 | October 2026 | Daniel Moreira | To be confirmed `[GOV-02]` | SME review draft created from the PG master template. Built from the Part 2 notes; not yet checked against the recording, validated or approved. `[SRC-01]` |

Reference code and final title: `[GOV-03]`.

---

## Part 1: What do I need to know? (AR Collections Customer Payment Journal Controls)

### High-level process

##### Part Description

This reference lists the controls that apply when you prepare a **Customer payment journal** (CPJL) to transfer funds between customer accounts, distribute a parent-account payment across child accounts, or restore a written-off or overpayment amount. It includes only the controls demonstrated in Part 2 of the AR Training D365 session. The steps are in the three guides listed in Part 2.

Posting permission, approval, checking the result after posting, and correcting or reversing a posted journal are not covered until confirmed. `[CPJ-16 to CPJ-19]`

##### Initiation

- You are preparing a CPJL to transfer or restore customer funds.

##### Stream

| Stream | Process Area | Key Roles |
|---|---|---|
| Accounts Receivable `[GOV-01]` | AR Collections | • To be confirmed |

##### Process

| # | Action | Who | When | Where |
|---|---|---|---|---|
| 1 | [AR Collections Customer Account Transfers](#part-2-how-do-i-do-it-ar-collections-customer-payment-journal-controls) | To be confirmed | When a payment is on the wrong customer account, or funds must move to a confirmed related account | D365 |
| 2 | [AR Collections Parent Payment Distribution](#part-2-how-do-i-do-it-ar-collections-customer-payment-journal-controls) | To be confirmed | When a payment on a parent account must be distributed to confirmed child accounts | D365 |
| 3 | [AR Collections Overpayment and Write-Off Restoration](#part-2-how-do-i-do-it-ar-collections-customer-payment-journal-controls) | To be confirmed | When an overpayment or written-off amount must be put back on a customer account | D365 |

### Roles and responsibilities

##### Overview

The business roles that prepare and post these journals are not yet confirmed. `[CPJ-16, CPJ-17]`

| Tasks / Business Roles | To be confirmed |
|---|---|
| [AR Collections Customer Account Transfers](#part-2-how-do-i-do-it-ar-collections-customer-payment-journal-controls) | R |
| [AR Collections Parent Payment Distribution](#part-2-how-do-i-do-it-ar-collections-customer-payment-journal-controls) | R |
| [AR Collections Overpayment and Write-Off Restoration](#part-2-how-do-i-do-it-ar-collections-customer-payment-journal-controls) | R |

### Key concepts

##### Overview

These controls apply to every CPJL entry in the three guides, unless a row says otherwise. The amounts used in the training are examples only, not thresholds.

##### Journal set-up

| Control | What to do |
|---|---|
| **Use CPJL** | Use the Customer payment journal (CPJL) to transfer funds between customer accounts and to restore written-off or overpayment amounts. `[CPJ-01, CPJ-02]` |
| **Describe the journal and every line** | Enter a clear description on the journal and on each line, including the relevant customer code, so the entry can be identified in each customer's history. `[CPJ-03, CPJ-04]` |
| **Use the right date** | The current date is the default. A wrong-account correction may use the original customer payment date when appropriate. Use a prior-period date only when it is required and the period is open. `[CPJ-05]` |
| **Keep the original currency** | Enter every line in the currency of the original payment or transaction. `[CPJ-07]` |

##### Line coding

| Control | What to do |
|---|---|
| **Debit to remove, credit to return** | Funds removed from a customer account are a debit. Funds placed on a customer account are a credit. `[CPJ-06]` |
| **Offset to the correct ledger account** | Set **Offset account type** to **Ledger**. For a transfer between customer accounts, use the bank-to-bank transfer clearing account, never a bank account. For a restoration, use the Overpayment ledger. `[CPJ-08, CPJ-09, TF-03, RO-01]` |
| **Leave unsupported fields blank** | For a restoration, do not enter financial tags, an invoice number or a bank account. `[CPJ-10]` |
| **Keep pre-populated dimensions** | For a restoration, do not change the financial dimensions that fill in automatically. `[CPJ-11]` |
| **Complete each line before the next** | Tab through every field in a line before you start the next one, so that fields such as the voucher fill in correctly. `[CPJ-12]` |

##### Validation and posting

| Control | What to do |
|---|---|
| **Balance the journal** | For a transfer or distribution, total debits must equal total credits. In a distribution, the child credits must add up to the parent debit. `[CPJ-13]` |
| **Simulate before posting** | Run Simulate Posting. A blue result means the journal is ready to post. A red result shows errors to read and correct. If you cannot resolve an error, log a request through the D365 issue form (see **Additional Resources**). `[CPJ-14, CPJ-15]` |
| **Post only when complete and validated** | Post only after every line is complete, the journal balances and Simulate Posting succeeds. `[CPJ-16, CPJ-17]` |

##### Allocations and amounts

| Term | Description |
|---|---|
| **Partial allocation** | In a parent-account distribution, move only the confirmed amount. The rest stays on the parent account, with a note that explains its purpose. `[PC-04]` |
| **Example amounts** | The training uses example amounts: $100, and a $10,000 receipt with $8,000 distributed and $2,000 left on the parent account. They are examples only, not thresholds, limits or approval levels. |

##### Not covered by this reference `[CPJ-16 to CPJ-21]`

| Topic | Status |
|---|---|
| **Who may post a CPJL** | To be confirmed. |
| **Whether approval is needed** | To be confirmed. |
| **Checking the result after posting** | To be confirmed. The AR Collections Customer Account guide covers reviewing customer transactions. |
| **Correcting or reversing a posted journal** | To be confirmed. |
| **An unposted journal that is no longer needed** | To be confirmed. |
| **The security role needed** | To be confirmed. If a page or control is missing, a security setting is a possible cause, not a confirmed one. |

---

## Part 2: How do I do it? (AR Collections Customer Payment Journal Controls)

The procedures that apply these controls are in these guides:

- [**AR Collections Customer Account Transfers**](../01-procedure-guides/PG-AR-Transfer-Funds-Between-Customer-Accounts-DRAFT.md): transfer funds between customer accounts.
- [**AR Collections Parent Payment Distribution**](../01-procedure-guides/PG-AR-Transfer-Parent-Payment-Across-Child-Accounts-DRAFT.md): distribute a parent-account payment across child accounts, including a partial allocation.
- [**AR Collections Overpayment and Write-Off Restoration**](../01-procedure-guides/PG-AR-Restore-Written-Off-Overpayment-DRAFT.md): put a written-off or overpayment amount back on a customer account.

Each guide includes the Simulate Posting and posting steps, so this reference has no procedures of its own.

---

## Part 3: Reports (AR Collections Customer Payment Journal Controls)

##### Overview

Reports for these processes are pending SME confirmation. `[GOV-04]`

---

## Additional Resources

The standard template block, unchanged.
