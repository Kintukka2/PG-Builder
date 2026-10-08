# PG Content QA Checklist

Use this checklist to review any D365 Procedure Guide (PG) before you submit it for SME review or publication. It is drawn from the publication gate and the definition of ready for publication (sources 1 and 2), and the project evidence rules.

**PG reviewed:** ________________ **Version:** ____ **Reviewer:** ________________ **Date:** ________

Mark each item: ✅ met · ❌ not met · N/A. For each ❌, record a validation ID or a fix in the review notes.

## A. Structure

- [ ] All 16 sections of the standard PG structure are present, in order.
- [ ] The Document status block shows module, release, risk, gate and status.
- [ ] The guide covers **one** D365 task with one outcome. Related tasks are linked, not included.
- [ ] Scope states what is in and what is out.

## B. Evidence

- [ ] Every step, label and system response can be traced to a source document or to a tested D365 session.
- [ ] No menu path, page behaviour, business rule or approval requirement is invented.
- [ ] Every unconfirmed item has a `VG-xx` ID and appears in the Draft validation notes and the validation register.
- [ ] No unvalidated item is worded as a confirmed instruction.
- [ ] Security access is described only as a *possible* cause, never as the diagnosis.

## C. Procedure writing

- [ ] Steps are numbered and use the Step / Action / Description format.
- [ ] Each step contains one user action.
- [ ] Each action starts with a verb (for example, *Select*, *Enter*, *Check*).
- [ ] Interface labels are in **bold** and exactly match the source evidence or the tested screen.
- [ ] The expected system response is stated where supported. Where it is not, it is omitted and has a VG ID.
- [ ] Business rules are kept separate from system instructions.
- [ ] Warnings appear immediately before the consequential action. Pending warnings are clearly marked as placeholders.
- [ ] Conditional steps state their condition (for example, "Do this only if…").

## D. Terminology

- [ ] Terms match the terminology register (for example, **Aged balances**, **Favourites**, **Credit and collections**).
- [ ] UK/AU English spelling is used in prose. UI labels match the D365 screen exactly.
- [ ] Module, workspace and page names are not used interchangeably.

## E. Results, verification and troubleshooting

- [ ] Expected results describe only confirmed outcomes.
- [ ] A verification checklist lets the learner confirm completion independently.
- [ ] Troubleshooting uses the Issue / Possible causes / What to do format, and covers missing modules, pages and results.
- [ ] Escalation or access-support routes are named, or held as placeholders with a VG ID.

## F. Screenshots

- [ ] Every figure placeholder in the PG has an entry in the screenshot register, and the numbers match.
- [ ] Each figure shows the state immediately before its action, with labels visible.
- [ ] No customer names, account numbers, balances, user names or other sensitive data are visible.
- [ ] Captions follow `Figure n. <Outcome or screen name>`. Each figure has alt text.
- [ ] Screenshots reflect the current D365 interface.

## G. Sign-off (publication only)

- [ ] Every blocking VG item is closed.
- [ ] Someone other than the author has tested every step in D365.
- [ ] The SME has validated the content and the process owner has approved publication.
- [ ] Related PGs, modules and references are cross-linked.
- [ ] The version history and document control fields are complete.

**Review notes**

| # | Section / step | Issue | VG ID or fix | Resolved |
|---|---|---|---|---|
| 1 | | | | |
