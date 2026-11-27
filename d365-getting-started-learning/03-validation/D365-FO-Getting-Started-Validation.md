# Validation Register: D365 F&O Getting Started

| Field | Value |
|---|---|
| Guide (editable source) | [`CLAUDE-TBC-D365 F&O Getting Started PG v0.1.docx`](../01-procedure-guides/CLAUDE-TBC-D365%20F%26O%20Getting%20Started%20PG%20v0.1.docx) |
| Markdown preview | [`PG-D365-FO-Getting-Started-DRAFT.md`](../01-procedure-guides/PG-D365-FO-Getting-Started-DRAFT.md) |
| Ticket | ADO 15454 *PG Creation - D365 F&O Getting Started* |
| Status | **Working draft v0.1** (27 November 2026), drafted from the [discovery map](../05-project-notes/Discovery-Map.md). Not yet checked in our D365 environment, not sent for review. |
| Roles | BPO and PG approver Ken Lee; source Microsoft documentation, confirmed by Daniel Moreira (D-106) |
| Code | None yet: a 100-series code once 460 to 462 are approved (D-102). Files use `TBC`. |
| Items | 33 items (`GS`): 26 open and blocking, each with one Word review comment (D-067); 3 open and non-blocking; 4 closed. Round 1 (8 questions) drafted on the board (section 4). |
| Last updated | 2026-11-27 (round 1) |

This file is the guide's question log. Item IDs are stable and never reused. Each open blocking item has one review comment in the Word guide, at the place it matters most, starting with its ID.

---

## 1. Sources

| Source | What the guide takes from it |
|---|---|
| [Discovery map](../05-project-notes/Discovery-Map.md) and research [A to F](../05-project-notes/discovery/) | The outline (section 3, split under D-101) and every step, label and limit, from Microsoft Learn and the D365 documentation |
| [260 O2C Getting Started v0.2](../../ar-collections-learning/01-procedure-guides/PG-260-O2C-Getting-Started-DRAFT.md) | The steps of topics 3.1 and 3.2 (legal entity), 2.3 (Favorites), 6.1 and 6.4 (views), 7.1 (update a saved view) and 8.1 (export), reviewed by the O2C SME, made general for every stream |
| [230 Collections v3.2](../../ar-collections-learning/01-procedure-guides/CLAUDE-230-Collections%20PG%20v3.2.docx) | The master template parts (front matter, styles, tables, boundary rows), copied unchanged |

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
| A8 | Microsoft Learn screenshots stand in for the WTG screenshots (35, listed in GS-28): each sits where the WTG screenshot goes, with a highlighted caption saying what it shows and to replace it. They show Microsoft's demo company (Contoso, USMF). | The user, 27 November 2026: placeholders make it easy to see what each screenshot must capture and to swap them. |

---

## 3. Guide-level items (`GS`)

**Priority:** **B** = blocks publication. **N** = non-blocking. **Method:** **Test** = clean-session test in our D365 environment. **IT** = configuration fact from IT. **Dec** = PG owner or BPO decision.

| ID | Item to confirm | Location | Priority | Method | Status |
|---|---|---|---|---|---|
| GS-01 | Guide code: a 100-series code once 460 to 462 are approved and the legacy 100 documents are retired (D-102). Rename the files from `TBC` then. | Cover, file names | B | Dec | Open (decided, waiting). No review comment: nothing to answer now. |
| GS-02 | Every procedure is written from Microsoft's documentation. The clean-session test confirms the labels, paths and results in our environment, and takes the screenshots. | Part 1, Part Description | B | Test | Open |
| GS-03 | D365 Finance Basics (ADO 15455) is not published, so its reference has no Training Hub link (D-096). Add the link when it is published. | Part 1, Part Description | B | Dec | Open |
| GS-04 | The sign-in steps (work account, any multifactor authentication prompt) and how users sign out. Microsoft has no end-user article on signing in. | 1.1 step 2; step 5 | B | Test | Open. **The production URL is confirmed:** https://wtg.operations.dynamics.com/ (Daniel Moreira, 27 November 2026); 1.1 step 2 updated. |
| GS-05 | The values of **Default view/edit mode** (Microsoft shows Auto only) and which the company recommends. | 1.2 step 6 | B | Test | Open |
| GS-06 | The company rule on changing the session date: who may, for which tasks, and whether it must be reset. | 1.3, Important box | B | Dec | Open. Asked in round 1, **Q02**. |
| GS-07 | Test the four field and grid shortcuts (Ctrl+G, Alt+Down arrow, T / D, Ctrl+Shift+A), which come from Microsoft's list. | Part 1, Keyboard shortcuts | B | Test | Open. **The main table is confirmed** from our environment's View shortcuts list (Daniel Moreira's UAT screenshots, 27 November 2026): Alt+G for page search and Alt+Q for action search (Ctrl+/ and Ctrl+' are not listed), Alt+S to save, Alt+Delete to delete, Alt+M, F for the filter pane, Ctrl+Shift+F7 for the message center. Right-click > **View shortcuts** shows the page's list (Navigate, Act on data, Close, Other); Alt+Shift+K starts with Shortcuts for selected element and changes with focus. Topics 2.2, 4.1, 4.2, 5.3, 5.4 and 13.1 updated. |
| GS-08 | Whether Immersive Home is switched on (10.0.44 or later). It replaces the dashboard as the start page. Also in 1.1 step 4 and 11.2 step 1. | 2.4, Note | N | Test | **Closed 2026-11-27:** UAT opens on the default dashboard (`mi=DefaultDashboard`, with the WiseTech Global banner, calendar, Work items assigned to me, Apps and Workspaces; Daniel Moreira's screenshots). The clean-session test checks production is the same. Review comment removed. |
| GS-09 | What happens to unsaved changes when a user moves to another record or closes the page, and where **Revert** is. | 4.1 step 4 | B | Test | Open |
| GS-10 | The delete confirmation message and its buttons. | 4.2, Delete a Record, step 3 | B | Test | Open |
| GS-11 | The side the Filter pane opens on (Microsoft's training and article disagree) and the label of its reset control. | 5.3 step 2 | B | Test | Open |
| GS-12 | The menu label and place of advanced filtering, the dialog title and its tabs. | 5.4 step 1 | B | Test | Open. The shortcut's label in our environment is **Open advanced filtering and sorting options** (Ctrl+Shift+F3); 5.4 step 1 uses it. |
| GS-13 | The footer total labels (**View column totals**: Total, Minimum, Maximum, Average; or **Total this column**), and whether the extended totals feature is on. 260 uses "+" and "Calculate column". | 6.2 step 2 | B | Test, IT | Open |
| GS-14 | The out-of-box view name (**Standard**) and the legal entity choice in **Save view as** and **Pin as default**. Same question as `G260-07`. | 6.4 step 5 | B | Test | Open |
| GS-15 | The personalization toolbar labels (Microsoft's article says **Add fields**, its screenshot **Add a field**). | 7.3 step 1 | B | Test | Open |
| GS-16 | The export row limit in our environment (Microsoft's default 50,000; up to 1,000,000). Same as 260 *Export to Excel VG-06*. | 8.1 step 5 | B | IT | Open. Asked in round 1, **Q03**. |
| GS-17 | Whether users may publish changes from Excel, for which pages, and with what check. | 8.2 step 6 | B | Dec, IT | Open. Asked in round 1, **Q04**. |
| GS-18 | The report dialog sections and labels, and the destinations available to users. Microsoft has no current end-user article; the labels come from an archived Microsoft blog. | 9.1 step 2 | B | Test | Open |
| GS-19 | The company rule for exported data: where files may be kept and shared. | Part 1, Getting data into Excel, Important box | B | Dec | Open. Asked in round 1, **Q01**. |
| GS-20 | The paths of **My batch jobs** and **Print archive** (Common > Inquiries) and the Print archive buttons. Also Part 3. | 9.4 step 2 | B | Test | Open |
| GS-21 | Attachment types, allowed file types and size, storage (Azure or SharePoint), and anything that must not be attached. | 10 step 4 | B | IT, Dec | Open. Asked in round 1, **Q05**. |
| GS-22 | The **Workflow** button and its menu labels, the workflow message bar, and the path of **Work items assigned to me**. Also 11.2 and Part 3. | 11.1 step 3 | B | Test | Open |
| GS-23 | The alert button label (**Create alert rule** or **Create a custom alert**), whether the alert batch jobs run and how often, and whether alert emails are sent. | 12 step 4 | B | Test, IT | Open. Asked in round 1, **Q07**. The alert button label is for the test. |
| GS-24 | The **Help & Support** menu items in our build, the Help pane shortcut, and whether the Task guides tab is set up. | 13.2 step 1 | B | Test | Open |
| GS-25 | How users raise a problem with the BAU Support team (the D365 issue form, the Atlas D365 User Support Hub or AVA) and the details the team needs. | 13.3 step 5 | B | Dec | Open. Asked in round 1, **Q08**. |
| GS-26 | The **Usage data** page, its **Personalization** tab and its delete and reset buttons. | 13.4 step 2 | B | Test | Open |
| GS-27 | Whether users may set up delegation for every workflow, and whether their manager must agree it. | 11.3, ACTION note | B | Dec | Open. Asked in round 1, **Q06**. |
| GS-28 | Replace the 35 Microsoft Learn example screenshots (demo data) with screenshots from our environment, without customer data, and remove each caption. Places: Part 1 (the parts of the screen: ui_labelled, navbar; system messages: msgbar); 1.1 step 4 (dash_default); 1.2 step 3 (useropt); 2.1 step 3 (modules); 2.2 step 2 (search); 2.3 step 4 (favstar); 2.4 step 4 (workspace); 3.1 step 2 (picker); 4.1 step 2 (actionpane); 5.1 step 2 (quickfilter); 5.2 step 2 (colfilter); 5.3 step 2 (filterpane); 5.4 step 2 (advfilter); 6.1 step 3, 8.1 step 5 (gridmenu); 6.2 step 2 (footer); 6.3 step 2 (grouping); 7.3 step 2 (ptoolbar); 8.2 step 3 (officemenu); 8.2 step 5 (addin); 9.1 step 3 (repdialog); 9.1 step 6 (repdest); 9.2 step 1 (pdfview); 9.3 step 2 (repbatch); 9.4 step 3 (batchstatus); 9.4 step 5 (printarchive); 10 step 4 (attach); 11.2 step 1 (workitems); 11.3 step 2 (delegation); 12 step 5 (alert); 13.1 step 2 (msgdetails); 13.1 step 4 (actioncenter); 13.2 step 2 (helppane). | Part 1, The parts of the screen (first screenshot) | B | Test | Open. Inserted 27 November 2026 at the user's request (A8). |
| GS-29 | Whether the organization publishes standard views to users. If so, 7.1 and 7.2 add the padlock and publishing notes. | 7.1, 7.2 | N | Dec | Open |
| GS-30 | Bulk edit and pasting from Excel into grids are left out of v0.1; add them if the company allows them. | 6, 8 | N | Dec | Open |
| GS-31 | Copilot and the other AI features are out of this guide (D-104); the research is kept for the parked guide (ADO 17798). | Part 1 | N | Dec | **Closed 2026-11-26** (D-104) |
| GS-32 | The finance concepts (dimensions, journals, vouchers, periods, posted transactions) are in D365 Finance Basics (D-101). | Part 1 | N | Dec | **Closed 2026-11-26** (D-101) |
| GS-33 | Security roles are not named (D-083); access goes through the D365 profile and the BAU Support team. | Part 1, What you can see in D365 | N | Dec | **Closed 2026-11-27** (D-083) |

**Screenshots from Microsoft Learn:** used as placeholders until the WTG screenshots replace them (A8, GS-28). They are for the working draft only: Microsoft's documentation images are under an open licence with attribution, but the training-module images are under Microsoft's terms of use, so none stays in the published guide.

The discovery also found points in 260 to check (discovery map, section 4). They are not applied to 260 (D-103); GS-13 and GS-14 test them here.

---

## 4. Question rounds (D-069, D-085)

### Round 1: drafted 27 November 2026

On the board as *D365 F&O Getting Started Round 1* (`r-d365-getting-started-1`), ADO 15454, for Daniel Moreira to answer or route to IT or the best-placed person. Not sent. Pages are estimates from the review copy's layout (LibreOffice with DM Sans); Word's Contents is the authority before sending (D-089). The review comment of each asked item starts with its question number.

| Q | Item | Topic | Page | Question |
|---|---|---|---|---|
| Q01 | GS-19 | Part 1, Key concepts | p. 12 | **Where exported files may be kept.** The guide's Important box says exported files hold confidential data, must be kept in an approved WiseTech Global location and deleted when no longer needed. Is there a company rule for where exported D365 files may be saved and shared, and who may receive them? If so, what should the box say? |
| Q02 | GS-06 | topic 1.3, step 5 | p. 20 | **Changing the session date.** Topic 1.3 shows how to change the session date, which becomes the default date for new journals and documents. Who may change it, for which tasks, and must it be reset straight after? If users should not change it at all, the topic can be removed. |
| Q03 | GS-16 | topic 8.1, step 5 | p. 63 | **Export to Excel row limit.** Microsoft's default limit for Export to Excel is 50,000 rows; an administrator can raise it to 1,000,000 (System administration > Setup > Client performance options > Maximum number of rows to export to Excel). What limit is set in production, so the guide can state it? |
| Q04 | GS-17 | topic 8.2, step 6 | p. 65 | **Publishing changes from Excel.** Open in Excel lets users change records in a linked workbook and publish them back to D365. May users publish changes this way? If yes, for which pages or processes, and is a check needed afterwards? If no, the guide keeps Open in Excel for viewing only. |
| Q05 | GS-21 | topic 10, step 4 | p. 75 | **Attachment rules.** Which attachment types should users choose (File, Note, URL, or a company type), which file types and maximum size are allowed, where are attachments stored (Azure or SharePoint), and is there anything users must not attach (for example bank or card details)? |
| Q06 | GS-27 | topic 11.3 | p. 81 | **Delegating work items while away.** Topic 11.3 shows how users set up automatic delegation of their workflow work items while away (User options > Workflow > Delegation). May users set it up for every workflow, and must their manager agree it first? |
| Q07 | GS-23 | topic 12, step 4 | p. 83 | **Alerts in production.** Alerts depend on two batch jobs, Change based alerts and Due date alerts. Do they run in production, and how often? Can alerts also be sent by email (Send email), or only to the Action center? |
| Q08 | GS-25 | topic 13.3, step 5 | p. 90 | **Raising a problem with the BAU Support team.** Step 5 sends users to the D365 issue form in Additional Resources. Is that the right route for a D365 problem or missing access, or should users use the Atlas D365 User Support Hub or AVA? Which details does the BAU Support team need (for example legal entity, page URL, message text, screenshot, time)? |

**Open items not asked, and their route (D-085):**

| Route | Items |
|---|---|
| Clean-session test (screen labels, navigation, results, screenshots) | GS-02, GS-04, GS-05, GS-07, GS-09 to GS-15, GS-18, GS-20, GS-22, GS-23 (button label), GS-24, GS-26, GS-28 |
| PG owner decision, waiting | GS-01 (code, D-102), GS-03 (Finance Basics link, when published) |
| Non-blocking, later | GS-29, GS-30 |

---

## 5. Change log

| Date | Change |
|---|---|
| 2026-11-27 | v0.1 drafted from the discovery map: 13 topics, 42 procedures, Part 1 key concepts, Part 3 inquiry pages; 26 review comments (GS-02 to GS-27). Contents page numbers from the LibreOffice layout with DM Sans (a first estimate; Word's Contents is the authority, D-089). |
| 2026-11-27 | Production URL and the shortcut list confirmed from Daniel Moreira's UAT screenshots: 1.1, 2.2, 4.1, 4.2, 5.3, 5.4, 13.1 and the Part 1 shortcut and screen tables updated; GS-08 closed (default dashboard). Round 1 drafted (Q01 to Q08). Still v0.1: the draft has not gone out (D-092). |
| 2026-11-27 | 35 Microsoft Learn screenshots added as placeholders for the WTG screenshots, with highlighted captions (A8); GS-28 becomes blocking, with its review comment. The guide grows to 93 pages; Contents and round 1 pages recalculated (LibreOffice estimate). |
