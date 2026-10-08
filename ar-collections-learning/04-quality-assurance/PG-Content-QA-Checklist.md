# PG Content QA Checklist

Use this checklist to review any D365 Procedure Guide (PG) before it goes to SME review, and again before publication.

It combines:

- the final checklist in [`PG_Template_Authoring_Guide_v1.docx`](../../templates/PG_Template_Authoring_Guide_v1.docx), which governs format and authoring rules;
- the publication gate in source 1 §4 and the definition of ready for publication in source 2;
- this project's evidence rules.

Where they differ, the authoring guide governs format and this project's evidence rules govern content.

**PG reviewed:** ________________ **Version:** ____ **Reviewer:** ________________ **Date:** ________

Mark each item: ✅ met · ❌ not met · N/A. For each ❌, record a `VG-xx` ID or a fix in the review notes.

## A. Template structure

- [ ] The guide is a **Save As** copy of the untouched master. The master itself is unchanged.
- [ ] Cover, contents, version history, About this guide, Parts 1–3 and Additional Resources are present, in order.
- [ ] `[Process Name]` is replaced everywhere, including the **Title** property (File > Info > Properties). The footer shows the title.
- [ ] Unused template examples (standalone, parent with subtopics, off-system, report blocks) are removed.
- [ ] Every placeholder and author instruction is replaced or removed. Search for `[`, "Process Name", "Role A" and "Fill the empty cell".
- [ ] The file name follows `NNN-Guide Title PG vX.docx`, using the assigned guide code and the actual revision.

## B. Part 1

- [ ] Part Description covers the purpose, scope, systems, result and exclusions.
- [ ] Initiation uses a native bullet for each confirmed trigger, even when there is only one.
- [ ] Stream table: stream, process area and key roles are confirmed.
- [ ] Process table: one row per major Part 2 topic, in matching order. Who, When and Where are complete. Each Action links to its heading.
- [ ] Roles matrix: one column per role, **R** for each confirmed responsible role, and **DEEAF6** shading in blank cells.
- [ ] Key concepts: an Overview, then a Heading 5 and table for each concept. Table headings are adapted to the content.

## C. Part 2 procedures

- [ ] Each in-system topic has Description, Responsibility and Initiation. Responsibility and Initiation use native bullets.
- [ ] The procedure opens with PROCESS START (prerequisites and responsibility) and ends with PROCESS COMPLETE (a verifiable outcome) or STEP COMPLETE (with a working Continue to link).
- [ ] Each row has one action. The verb is *italicized*. UI labels and business objects are **bold**, with exact on-screen spelling.
- [ ] Navigation follows the standard pattern (*Check* the **Entity** → *Click* **Modules** → path), using a confirmed route.
- [ ] The Description states the location, the exact value or selection rule, and the expected result. No further user action is hidden in a Description.
- [ ] Alternative and conditional paths state their condition and where they rejoin.
- [ ] Warnings appear immediately before the consequential action.
- [ ] Native numbering is used, with the 0.25-inch hanging indent intact. Boundary rows are unnumbered. Shading is correct: DEEAF6 (start/step), E2EFD9 (complete), E7E6E6 (off-system).

## D. Part 3 and Additional Resources

- [ ] Each report has its own Heading 5 and its own Navigation | Description table. "No applicable reports" is used only after explicit SME confirmation.
- [ ] Additional Resources is unchanged: wording, order and links. No Troubleshooting or Keywords section has been added.

## E. Evidence (project rule)

- [ ] Every step, label, role, trigger and system response traces to a source document or a tested D365 session.
- [ ] Nothing is invented: menu paths, approvals, owners, roles, system behavior or report results.
- [ ] Every unconfirmed item has a `VG-xx` ID in the validation register and a Word comment on the affected text.
- [ ] Security access is described only as a *possible* cause.

## F. Language and screenshots

- [ ] English (United States) is used throughout the guide text, including tables, headers and footers. UI labels and identifiers are exact.
- [ ] Acronyms are spelled out at first use, for example *business process owner (BPO)*.
- [ ] Screenshots are used only where they add context. They are current and readable, with customer and user data masked. There are no screenshot placeholders.

## G. Final checks and handoff

- [ ] Contents, fields, footer title, date and page numbers are updated (Update Table > Update entire table, then F9). There are no "Error!" results.
- [ ] Every internal link (Process table, roles matrix, Continue to) and every external link has been Ctrl+clicked and tested.
- [ ] An exported review PDF has been checked page by page for clipping, split content and footers.
- [ ] Before release: blocking VG items are closed, comments and tracked changes are resolved, and draft notes are removed.
- [ ] Someone other than the author has tested the procedure. The SME, the designated reviewer and the process owner have approved it, with the evidence recorded.
- [ ] Handoff: the editable Word file, its review or approval status, the question log (validation register) and a review PDF if required.

**Review notes**

| # | Section / step | Issue | VG ID or fix | Resolved |
|---|---|---|---|---|
| 1 | | | | |
