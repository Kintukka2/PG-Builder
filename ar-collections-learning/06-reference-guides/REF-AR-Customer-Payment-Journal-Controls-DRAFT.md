# Reference: Customer Payment Journal (CPJL) Controls

> **WORKING DRAFT. Not validated, not approved, not for publication.**
>
> This reference lists the controls shared by the three Part 2 working guides. It includes **only** controls the *AR Training D365* Part 2 notes support (sources 4.0, 4.3 to 4.6). Those notes are Teams AI-generated and have not been checked against the recording (`SRC-01`). Anything the notes do not cover is listed under [Not covered by the sources](#not-covered-by-the-sources), not filled in. `[XX-nn]` markers point to the [validation register](../03-validation/Part2-CPJL-and-Transfers-Validation.md).

## Document control

| Field | Value |
|---|---|
| Reference code and final title | To be confirmed `[GOV-03]` |
| Version | 0.1 working draft, October 2026. Author: Daniel Moreira. |
| Business process owner | To be confirmed `[GOV-02]` |
| Status | Working draft (Part 2 roadmap item 14, Release 3A). Not a procedure: the steps are in the guides below. |
| Content type | Reference guide (source 0 content types). |

## Purpose and use

Use this reference to check that a Customer payment journal (CPJL) entry follows the controls demonstrated in Part 2 of the AR Training D365 session. It supports these guides:

| Code | Guide | Journal pattern |
|---|---|---|
| TF | [Transfer Funds Between Customer Accounts](../01-procedure-guides/PG-AR-Transfer-Funds-Between-Customer-Accounts-DRAFT.md) | Debit the source customer, credit the destination customer. Offset: bank-to-bank transfer clearing account. |
| PC | [Transfer a Parent Account Payment Across Child Accounts](../01-procedure-guides/PG-AR-Transfer-Parent-Payment-Across-Child-Accounts-DRAFT.md) | Debit the parent account, credit each child account. Offset: bank-to-bank transfer clearing account. |
| RO | [Restore a Written-Off or Overpayment Amount](../01-procedure-guides/PG-AR-Restore-Written-Off-Overpayment-DRAFT.md) | Credit the customer. Offset: Overpayment ledger. |

## Controls

**Applies to:** ● = the notes state the control for this entry type, or for CPJL entries generally. ○ = the guide applies it, but the notes state it only for the other entry types (see the open item in the row). — = not stated.

| # | Control | What to do | TF | PC | RO | Open items |
|---|---|---|---|---|---|---|
| 1 | **Use CPJL** | Use the Customer payment journal (CPJL) to transfer funds between customer accounts and to restore written-off or overpayment amounts. | ● | ● | ● | Navigation and journal name `CPJ-01`, `CPJ-02` |
| 2 | **Describe the journal and every line** | Enter a clear description on the journal header and on each line, so the entry can be identified in each customer's history. Include the relevant customer code. | ● | ● | ● | Field labels `CPJ-03`; wording standard `CPJ-04` |
| 3 | **Use the right date** | The current date is the default. A wrong-account correction may use the original customer payment date when appropriate. A prior-period date is used only when required and the period is open. | ● | ○ | ● | Field label and backdating rule `CPJ-05` |
| 4 | **Keep the original currency** | Enter every line in the currency of the original payment or transaction. | ● | ● | ● | Field and behavior `CPJ-07` |
| 5 | **Debit to remove, credit to return** | Funds removed from a customer account are a debit. Funds placed on a customer account are a credit. | ● | ● | ● | How debits and credits are shown `CPJ-06` |
| 6 | **Offset to the correct ledger account** | Set **Offset account type** to **Ledger**. For a transfer between customer accounts, use the bank-to-bank transfer clearing account; do not post directly to a bank account. For a restoration, use the Overpayment ledger. | ● | ● | ● | Labels and per-line entry `CPJ-08`; clearing account `TF-03`, `TF-04`, `PC-03`; Overpayment ledger `RO-01`; account numbers `CPJ-09` |
| 7 | **Leave unsupported fields blank** | Do not enter financial tags, an invoice number or a bank account. | ○ | ○ | ● | Labels, and whether this applies to transfers `CPJ-10` |
| 8 | **Keep pre-populated dimensions** | Do not change the financial dimensions that fill in automatically. | ○ | ○ | ● | Exceptions, and whether this applies to transfers `CPJ-11` |
| 9 | **Complete each line before the next** | Tab through every field in a line before you start the next line, so that fields such as the voucher fill in correctly. | ● | ● | ● | Which fields complete `CPJ-12` |
| 10 | **Balance the journal** | Total debits must equal total credits. In a distribution, the child credits must add up to the parent debit. | ● | ● | — | Where totals are shown `CPJ-13` |
| 11 | **Simulate before posting** | Run Simulate Posting. The notes describe a blue result as ready to post, and red results as errors to read and correct, or to get help with. | ● | ● | ● | Label and results `CPJ-14`; errors and support route `CPJ-15` |
| 12 | **Post only when complete and validated** | Post only after every line is complete, the journal balances and Simulate Posting succeeds. | ● | ● | ● | Post control and permission `CPJ-16`; approval `CPJ-17` |

The notes do not state a balance check for a restoration. The pack's restore draft enters the customer credit and its offset on the same line.

### Partial allocation (PC only)

Move only the confirmed amount. The rest stays on the parent account, with a note that explains its purpose. Where the note goes is open (`PC-04`).

### Example amounts

The Part 2 material uses example amounts: $100 (named in the handover, source 4.7), and a $10,000 receipt with $8,000 distributed and $2,000 left on the parent account. They are **examples only**. They are not thresholds, limits or approval levels (`CPJ-17`).

## Not covered by the sources

Do not infer these. Each is an open validation item.

| Topic | Item |
|---|---|
| Who may post a CPJL | `CPJ-16` |
| Whether approval is required, and any threshold | `CPJ-17` |
| How to verify the result after posting | `CPJ-18` |
| How to correct or reverse a posted journal | `CPJ-19` |
| What to do with an unposted journal that is no longer needed | `CPJ-20` |
| The security role needed to create a CPJL | `CPJ-21` |
| Account numbers for the Overpayment ledger and the clearing account | `CPJ-09`, `RO-01`, `TF-03` |
| The support route for unresolved Simulate Posting errors (the notes mention "SYD" during training) | `CPJ-15` |
| What "PG/Ava follow-up support" refers to | `SRC-03` |

## Glossary

| Term | Meaning in this reference |
|---|---|
| **CPJL** | The Customer payment journal, as named in the Part 2 notes. How the code appears in D365 is open (`CPJ-02`). |
| **Offset account** | The ledger account on the other side of a customer line. |
| **Bank-to-bank transfer clearing account** | The ledger account used as the offset for transfers between customer accounts. |
| **Overpayment ledger** | The main account used as the offset for restoring an amount to a customer account. |
| **Simulate Posting** | A check run on the journal before posting, which shows whether it is ready or has errors (`CPJ-14`). |

## Related content

- [Part 2 validation register](../03-validation/Part2-CPJL-and-Transfers-Validation.md)
- [AR Collections Favorites](../01-procedure-guides/PG-AR-Configure-Collections-Favourites-DRAFT.md): adds **Customer payment journal** to favorites.
- [AR Collections Workspace](../01-procedure-guides/PG-AR-Workspace-DRAFT.md): **Payment journals not posted** and **Open payment journals**.

## Change log

| Date | Change |
|---|---|
| 2026-10-23 | Reference created from the AR Training D365 Part 2 update pack. |
