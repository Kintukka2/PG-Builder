# Screenshot Register: AR Collections Transfer Funds Between Customer Accounts

| Field | Value |
|---|---|
| Related PG | [`../01-procedure-guides/TBC-AR Collections Customer Account Transfers PG v0.1.docx`](../01-procedure-guides/TBC-AR%20Collections%20Customer%20Account%20Transfers%20PG%20v0.1.docx) (editable source) |
| Source recording | *AR Training D365*, Part 2. Timestamps have **not been supplied** (`SRC-02`). |
| Frames reviewed | None |
| Last updated | 2026-10-25 |

> **Template rule.** Screenshots are optional, and a clean guide has no placeholders (decision D-017). The Word guide has no figures. Capture only the candidates below that add context, once the labels are confirmed.

The capture limitations and clean-session recapture specification in the [AR Collections Favorites screenshot register](PG-AR-Configure-Collections-Favourites-Screenshots.md#4-clean-session-recapture-specification) apply here as well.

## Candidate figures

| Fig | Guide step | Screen content | Draft caption | Required callouts | Timestamp | Status |
|---|---|---|---|---|---|---|
| 1 | 1.1 Steps 5 to 13 | The journal with its description and the completed source line: customer, debit amount, line description, **Ledger** offset type and the clearing account | Figure 1. The source line of a transfer | Journal description; debit; **Offset account type**; clearing account (`CPJ-03`, `CPJ-08`, `TF-03`) | Not supplied | Placeholder; recommended if only one figure is used |
| 2 | 1.2 Steps 2 to 7 | Both lines: source debit and destination credit, same amount and currency | Figure 2. A balanced two-line transfer | Debit and credit amounts; currency (`CPJ-06`, `CPJ-07`, `TF-04`) | Not supplied | Placeholder |
| 3 | 1.3 Step 2 | The Simulate Posting result | Figure 3. Simulate Posting result | Result message (`CPJ-14`) | Not supplied | Placeholder |

**Privacy and safety.** Never capture by posting to a real customer account. Use a test environment and test customers, and do not post a journal only to take a screenshot. Mask customer account numbers, customer names, amounts, voucher numbers and ledger account numbers. The masking policy is still open as item VG-27 in the Favorites validation register.

## Change log

| Date | Change |
|---|---|
| 2026-10-23 | Register created with the working draft. There are no timestamps yet. |
| 2026-10-25 | Linked to the Word guide (v0.1). Step references updated. |
