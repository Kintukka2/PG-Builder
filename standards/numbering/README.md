# PG Numbering Standards

Guide codes and file names for every Procedure Guide (PG) follow these standards (D-070). They replace the O2C PG Numbering Standard v1.3, which was held outside this repository (D-046).

## What is here

| File | Role |
|---|---|
| [`PG_Numbering_Master_Register.json`](PG_Numbering_Master_Register.json) | **The authority.** The single allocation register for all six standards: families, assigned codes, withdrawn codes, historical mappings, the common rules and the test series. Version 2.1. |
| [`CLAUDE-O2C_PG_Numbering_Standard_v2.1.docx`](CLAUDE-O2C_PG_Numbering_Standard_v2.1.docx) | O2C (200-series), the readable view of the register. Version 2.1 records 221 as withdrawn. The `CLAUDE-` prefix comes off when it is published (D-056). |
| [`P2P_PG_Numbering_Standard_v2.0.docx`](P2P_PG_Numbering_Standard_v2.0.docx) | P2P (300-series, shared) |
| [`Procurement_PG_Numbering_Standard_v2.0.docx`](Procurement_PG_Numbering_Standard_v2.0.docx) | Procurement (300-series, shared) |
| [`RCTI_PG_Numbering_Standard_v2.0.docx`](RCTI_PG_Numbering_Standard_v2.0.docx) | RCTI (398 and 399, shared) |
| [`R2R_PG_Numbering_Standard_v2.0.docx`](R2R_PG_Numbering_Standard_v2.0.docx) | R2R (400-series) |
| [`Tax_PG_Numbering_Standard_v2.0.docx`](Tax_PG_Numbering_Standard_v2.0.docx) | Tax (500-series) |
| [`Audit_and_Read_Me.txt`](Audit_and_Read_Me.txt) | The audit note that came with the v2.0 pack, unchanged |

The register owner is Daniel Moreira. The Word standards are views of the register: when the register changes, the affected Word standard changes in the same pull request.

## Editions

| Version | Date | Change |
|---|---|---|
| 2.0 | 2026-11-17 | Supplied by the user. Aligns all six standards, records completed numbering, adds the 260–269 O2C Getting Started family, records 460 to 462, and replaces permanent code protection with controlled reuse. |
| 2.1 | 2026-11-17 | **221 Customer Payment Corrections is withdrawn**, with 220 Customer Payments as its successor, instead of on a consolidation hold (D-070). It is not released for reuse until 220 v3.0 is published and no maintained document refers to 221 as a current guide. **Test series added** (D-071). Only the O2C standard changes; the other five stay at v2.0. |

## Test series: T-NNNN

Trial conversions of documents that are not procedure guides get a T-number instead of a stream code (D-071).

- Numbered in order from **T-0001**. A T-number is never reused.
- T-numbers are internal. Nothing is published to the Training Hub under a T-number, and the six stream standards do not list them.
- If a test document goes live, it gets a code in its real series under the common rules, and its T-number is recorded as its predecessor.
- Working files are named `T-NNNN-Title PG vX.Y.docx`, with the `CLAUDE-` prefix while Claude maintains them.

| T-number | Document | Allocated | Status |
|---|---|---|---|
| T-0001 | CW1 to D365 Migration | 2026-11-17 | v0.1 working draft ([folder](../../gl-cw1-migration-learning/)) |
