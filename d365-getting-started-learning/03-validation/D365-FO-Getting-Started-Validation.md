# Validation Register: D365 F&O Getting Started

| Field | Value |
|---|---|
| Guide (editable source) | [`CLAUDE-TBC-D365 F&O Getting Started PG v0.1.docx`](../01-procedure-guides/CLAUDE-TBC-D365%20F%26O%20Getting%20Started%20PG%20v0.1.docx) |
| Markdown preview | [`PG-D365-FO-Getting-Started-DRAFT.md`](../01-procedure-guides/PG-D365-FO-Getting-Started-DRAFT.md) |
| Ticket | ADO 15454 *PG Creation - D365 F&O Getting Started* |
| Status | **Working draft v0.1** (27 November 2026), drafted from the [discovery map](../05-project-notes/Discovery-Map.md). Not yet checked in our D365 environment, not sent for review. |
| Roles | BPO and PG approver Ken Lee; source Microsoft documentation, confirmed by Daniel Moreira (D-106) |
| Code | None yet: a 100-series code once 460 to 462 are approved (D-102). Files use `TBC`. |
| Items | 33 items (`GS`): 26 open and blocking, each with one Word review comment (D-067); 4 open and non-blocking; 3 closed. |
| Last updated | 2026-11-27 |

This file is the guide's question log. Item IDs are stable and never reused. Each open blocking item has one review comment in the Word guide, at the place it matters most, starting with its ID.

---

## 1. Sources

| Source | What the guide takes from it |
|---|---|
| [Discovery map](../05-project-notes/Discovery-Map.md) and research [A to F](../05-project-notes/discovery/) | The outline (section 3, split under D-101) and every step, label and limit, from Microsoft Learn and the D365 documentation |
| [260 O2C Getting Started v0.2](../../ar-collections-learning/01-procedure-guides/PG-260-O2C-Getting-Started-DRAFT.md) | The steps of topics 3.1 and 3.2 (legal entity), 2.3 (Favorites), 6.1 and 6.4 (views), 7.1 (update a saved view) and 8.1 (export), reviewed by the O2C SME, made general for every stream |
| [230 Collections v3.1](../../ar-collections-learning/01-procedure-guides/CLAUDE-230-Collections%20PG%20v3.1.docx) | The master template parts (front matter, styles, tables, boundary rows), copied unchanged |

## 2. Drafting decisions

| # | Decision | Reason |
|---|---|---|
| A1 | The cover reads *D365 F&O: Getting Started*; the guide's name elsewhere is D365 F&O Getting Started. | Avoids "D365 F&O: D365 F&O Getting Started" on the cover and in the footer. |
| A2 | One role, **D365 End-user**, throughout; the stream is *All streams*. | The audience is every D365 user (D-101). |
| A3 | 13 topics, from the discovery outline: topics 8 and 9 of the outline (dimensions, posted transactions) move to D365 Finance Basics, and Ask Copilot is removed (D-101, D-104). | Project notes, section 1. |
| A4 | Part 1 key concepts use the form each needs (D-059): tables for the screen parts, page types, messages, operators, query symbols, relative dates, views, Excel tools, destinations, workflow terms and shortcuts; bullets for the legal entity rules; paragraphs for access (D-083). | D-059 |
| A5 | Part 3 lists the four inquiry pages the topics use (My batch jobs, Print archive, Workflow history, Work items assigned to me). | Part 3 is mandatory; these are the pages a new user checks. |
| A6 | Favorites is taught here (topic 2.3) as well as in 260. | This is the general Getting Started guide (D-084); 260 stays as it is until this guide is approved (D-103). |
| A7 | Where Microsoft's documentation and 260 differ, the guide follows Microsoft and the item asks the clean-session test to confirm (for example GS-13, GS-14). | Discovery map, section 4. |
| A8 | No screenshots in v0.1. Microsoft's images show demo data; the guide's screenshots come from the clean-session test (GS-28). | Discovery map, section 1. |

---

## 3. Guide-level items (`GS`)

**Priority:** **B** = blocks publication. **N** = non-blocking. **Method:** **Test** = clean-session test in our D365 environment. **IT** = configuration fact from IT. **Dec** = PG owner or BPO decision.

| ID | Item to confirm | Location | Priority | Method | Status |
|---|---|---|---|---|---|
| GS-01 | Guide code: a 100-series code once 460 to 462 are approved and the legacy 100 documents are retired (D-102). Rename the files from `TBC` then. | Cover, file names | B | Dec | Open (decided, waiting). No review comment: nothing to answer now. |
| GS-02 | Every procedure is written from Microsoft's documentation. The clean-session test confirms the labels, paths and results in our environment, and takes the screenshots. | Part 1, Part Description | B | Test | Open |
| GS-03 | D365 Finance Basics (ADO 15455) is not published, so its reference has no Training Hub link (D-096). Add the link when it is published. | Part 1, Part Description | B | Dec | Open |
| GS-04 | The D365 URL users open, the sign-in method (work account, multifactor authentication), and how users sign out. Microsoft has no end-user article on signing in. | 1.1 step 2; step 5 | B | Test, IT | Open |
| GS-05 | The values of **Default view/edit mode** (Microsoft shows Auto only) and which the company recommends. | 1.2 step 6 | B | Test | Open |
| GS-06 | The company rule on changing the session date: who may, for which tasks, and whether it must be reset. | 1.3, Important box | B | Dec | Open |
| GS-07 | Test every shortcut in the Key concepts table. Microsoft gives Ctrl+' and Ctrl+/ for action search and Ctrl+Shift+? and Ctrl+? for the Help pane. | Part 1, Keyboard shortcuts | B | Test | Open |
| GS-08 | Whether Immersive Home is switched on (10.0.44 or later). It replaces the dashboard as the start page. Also in 1.1 step 4 and 11.2 step 1. | 2.4, Note | B | IT | Open |
| GS-09 | What happens to unsaved changes when a user moves to another record or closes the page, and where **Revert** is. | 4.1 step 4 | B | Test | Open |
| GS-10 | The delete confirmation message and its buttons. | 4.2, Delete a Record, step 3 | B | Test | Open |
| GS-11 | The side the Filter pane opens on (Microsoft's training and article disagree) and the label of its reset control. | 5.3 step 2 | B | Test | Open |
| GS-12 | The label and place of **Advanced filter or sort**, the dialog title and its tabs. | 5.4 step 1 | B | Test | Open |
| GS-13 | The footer total labels (**View column totals**: Total, Minimum, Maximum, Average; or **Total this column**), and whether the extended totals feature is on. 260 uses "+" and "Calculate column". | 6.2 step 2 | B | Test, IT | Open |
| GS-14 | The out-of-box view name (**Standard**) and the legal entity choice in **Save view as** and **Pin as default**. Same question as `G260-07`. | 6.4 step 5 | B | Test | Open |
| GS-15 | The personalization toolbar labels (Microsoft's article says **Add fields**, its screenshot **Add a field**). | 7.3 step 1 | B | Test | Open |
| GS-16 | The export row limit in our environment (Microsoft's default 50,000; up to 1,000,000). Same as 260 *Export to Excel VG-06*. | 8.1 step 5 | B | IT | Open |
| GS-17 | Whether users may publish changes from Excel, for which pages, and with what check. | 8.2 step 6 | B | Dec, IT | Open |
| GS-18 | The report dialog sections and labels, and the destinations available to users. Microsoft has no current end-user article; the labels come from an archived Microsoft blog. | 9.1 step 2 | B | Test | Open |
| GS-19 | The company rule for exported data: where files may be kept and shared. | Part 1, Getting data into Excel, Important box | B | Dec | Open |
| GS-20 | The paths of **My batch jobs** and **Print archive** (Common > Inquiries) and the Print archive buttons. Also Part 3. | 9.4 step 2 | B | Test | Open |
| GS-21 | Attachment types, allowed file types and size, storage (Azure or SharePoint), and anything that must not be attached. | 10 step 4 | B | IT, Dec | Open |
| GS-22 | The **Workflow** button and its menu labels, the workflow message bar, and the path of **Work items assigned to me**. Also 11.2 and Part 3. | 11.1 step 3 | B | Test | Open |
| GS-23 | The alert button label (**Create alert rule** or **Create a custom alert**), whether the alert batch jobs run and how often, and whether alert emails are sent. | 12 step 4 | B | Test, IT | Open |
| GS-24 | The **Help & Support** menu items in our build, the Help pane shortcut, and whether the Task guides tab is set up. | 13.2 step 1 | B | Test | Open |
| GS-25 | How users raise a problem with the BAU Support team (the D365 issue form, the Atlas D365 User Support Hub or AVA) and the details the team needs. | 13.3 step 5 | B | Dec | Open |
| GS-26 | The **Usage data** page, its **Personalization** tab and its delete and reset buttons. | 13.4 step 2 | B | Test | Open |
| GS-27 | Whether users may set up delegation for every workflow, and whether their manager must agree it. | 11.3, ACTION note | B | Dec | Open |
| GS-28 | Screenshots for the guide, from the clean-session test. | All topics | N | Test | Open |
| GS-29 | Whether the organization publishes standard views to users. If so, 7.1 and 7.2 add the padlock and publishing notes. | 7.1, 7.2 | N | Dec | Open |
| GS-30 | Bulk edit and pasting from Excel into grids are left out of v0.1; add them if the company allows them. | 6, 8 | N | Dec | Open |
| GS-31 | Copilot and the other AI features are out of this guide (D-104); the research is kept for the parked guide (ADO 17798). | Part 1 | N | Dec | **Closed 2026-11-26** (D-104) |
| GS-32 | The finance concepts (dimensions, journals, vouchers, periods, posted transactions) are in D365 Finance Basics (D-101). | Part 1 | N | Dec | **Closed 2026-11-26** (D-101) |
| GS-33 | Security roles are not named (D-083); access goes through the D365 profile and the BAU Support team. | Part 1, What you can see in D365 | N | Dec | **Closed 2026-11-27** (D-083) |

The discovery also found points in 260 to check (discovery map, section 4). They are not applied to 260 (D-103); GS-13 and GS-14 test them here.

---

## 4. Change log

| Date | Change |
|---|---|
| 2026-11-27 | v0.1 drafted from the discovery map: 13 topics, 42 procedures, Part 1 key concepts, Part 3 inquiry pages; 26 review comments (GS-02 to GS-27). Contents page numbers from the LibreOffice layout with DM Sans (a first estimate; Word's Contents is the authority, D-089). |
