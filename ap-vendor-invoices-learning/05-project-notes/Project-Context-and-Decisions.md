# Project Context and Decisions: AP Vendor Invoices Learning

| Field | Value |
|---|---|
| Topic | Accounts Payable (AP) Vendor Invoices, in the Purchase-to-Pay (P2P) stream |
| Guide | *D365 F&O: Vendor Invoices (NZ) Procedure Guide*, v1.0 working draft ([Word](../01-procedure-guides/CLAUDE-TBC-Vendor%20Invoices%20PG%20v1.0.docx) · [PDF](../01-procedure-guides/CLAUDE-TBC-Vendor%20Invoices%20PG%20v1.0.pdf) · [Preview](../01-procedure-guides/PG-Vendor-Invoices-v1.0-DRAFT.md) · [Validation](../03-validation/Vendor-Invoices-v1.0-Validation.md)) |
| Last updated | 2026-11-12 |

This topic follows the repository conventions in the [README](../../README.md) and the PG master template and authoring guide in [`templates/`](../../templates/). Decision IDs continue the repository sequence, so they never clash with the AR Collections log ([AR decisions](../../ar-collections-learning/05-project-notes/Project-Context-and-Decisions.md)).

---

## 1. Source documents

Held outside this repository and not modified.

| # | Source | Role |
|---|---|---|
| 1 | *D365 F&O: Vendor Invoices (NZ) Procedure Guide*, version 0.2, released 30 January 2025. Author Michael Thurlow; BPO Ghada Boulos. File `04-D365_FO_Vendor_Invoices_PG.docx`, supplied by the user on 2026-11-12. | Legacy guide in the earlier PG format. Reference evidence for every v1.0 topic: no item closes on it alone. |

## 2. Guide structure (v1.0)

| # | Topic | Legacy source |
|---|---|---|
| 0 | Vendor sends the invoice to `apanz@wisetechglobal.com` (Process table only) | High-level process row 1 |
| 1 | Create a Vendor Invoice: 1.1 Search for an Existing Purchase Order; 1.2 Create a Vendor Invoice from a Purchase Order; 1.3 Create a Manual Vendor Invoice; 1.4 Add an Attachment to a Vendor Invoice | Four legacy procedures |
| 2 | Submit a Vendor Invoice to the Workflow | Legacy procedure |
| 3 | Post a Vendor Invoice | Legacy procedure |
| 4 | Confirm a Purchase Order | Legacy procedure |
| Part 3 | 12 standard reports | Legacy Part 3 |

## 3. Decisions log

| ID | Date | Decision | Basis | Status |
|---|---|---|---|---|
| D-057 | 2026-11-12 | **Vendor Invoices (NZ) v0.2 is converted to the PG master template as a v1.0 working draft**, at the user's request ("convert this old guide to the new look standard"). It sits in a new topic folder, `ap-vendor-invoices-learning/`, because Vendor Invoices is in the P2P stream, not AR Collections. The conversion keeps the legacy content and changes its form: seven procedures become four major topics (1 with subtopics 1.1 to 1.4), steps become one action per row with the standard navigation pattern and process boundaries, each report gets its own table, the training units are removed, and one user name is masked in a screenshot. Version 1.0 follows the precedent of 220 v3.0 and 230 v3.0, where a rebuild in the master template takes the next major version. The file name uses `TBC` until the register owner allocates a P2P code (`VI-01`) and `CLAUDE-` until publication (D-056). 22 items (`VI-01` to `VI-22`, 17 blocking) are in the [validation register](../03-validation/Vendor-Invoices-v1.0-Validation.md), each that affects the text also a Word review comment. Version 0.2 stays the published guide until 1.0 passes its gates. | User request; T1; T2; D-056 | Adopted |

## 4. Next steps

1. **Code and owner.** Ask the register owner for the P2P guide code (`VI-01`) and confirm the BPO (`VI-02`).
2. **SME review.** Send the v1.0 draft to the Accounts Payable SME with the blocking items: scope and entity (`VI-03`), stream (`VI-04`), role (`VI-05`), trigger (`VI-06`), purchase requisition search and status (`VI-07`, `VI-08`), *Default from* (`VI-10`), failed matches (`VI-11`), manual invoice line rules (`VI-13`), workflow rules (`VI-14`), posting outcome and the posted-invoice path (`VI-15`, `VI-16`), the step after confirming a purchase order (`VI-17`), the reports (`VI-18`) and the workflow screenshots (`VI-20`).
3. **Clean-session test** of the items with a Test method, and recapture any screenshot that no longer matches D365 F&O (`VI-09`, `VI-12`, `VI-20`, `VI-22`).
4. **Related guides.** Confirm the titles and codes of the other P2P guides, then link to them from Part 1 (`VI-21`).
