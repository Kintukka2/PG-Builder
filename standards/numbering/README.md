# PG Numbering Standards

Guide codes and file names for every Procedure Guide (PG) follow these standards (D-070). They replace the O2C PG Numbering Standard v1.3, which was held outside this repository (D-046).

## What is here

| File | Role |
|---|---|
| [`PG_Numbering_Master_Register.json`](PG_Numbering_Master_Register.json) | **The authority.** The single allocation register for all six standards: families, assigned codes, withdrawn codes, historical mappings, the common rules and the Other series. Version 2.2. |
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
| 2.2 | 2026-11-17 | **The test series becomes the Other series** (O-NNNN) for documents that are not procedure guides; T-0001 becomes O-0001 (D-076). No Word standard changes. |

## Other series: O-NNNN

Documents that are not procedure guides, such as go-live manuals and cutover runbooks, get an O-number instead of a stream code when they are converted to the PG master template (D-071, D-076).

- Numbered in order from **O-0001**. An O-number is never reused.
- O-numbers belong to the PG builder, not to a stream: the six stream standards do not list them.
- Where an O-series document is published is decided for each document. If one becomes a procedure guide in a stream, it gets a code in that series under the common rules, and its O-number is recorded as its predecessor.
- Working files are named `O-NNNN-Title PG vX.Y.docx`, with the `CLAUDE-` prefix while Claude maintains them.

| O-number | Document | Allocated | Status |
|---|---|---|---|
| O-0001 | CW1 to D365 Migration (allocated as T-0001, renumbered by D-076) | 2026-11-17 | v0.1 working draft ([folder](../../gl-cw1-migration-learning/)) |
