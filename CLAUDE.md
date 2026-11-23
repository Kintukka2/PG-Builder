# Working rules for Claude in this repository

## File names: the `CLAUDE-` prefix (D-056)

Every file Claude creates or rebuilds for the user starts with `CLAUDE-`: Word guides, PDFs, Excel workbooks, review pack zips and any other file Claude sends. The rest of the name follows the PG numbering standards in `standards/numbering/` (D-070), for example `CLAUDE-260-O2C Getting Started PG v0.2.docx`. A document that is not a procedure guide uses its O-number from the Other series in place of the code, for example `CLAUDE-O-0001-CW1 to D365 Migration PG v0.1.docx` (D-071, D-076).

- The prefix marks a Claude working file. It is removed when the file is published, so a published guide never carries it.
- When Claude rebuilds an existing file that has no prefix, it renames the file with the prefix in the same change and updates every link to it.
- Markdown previews, validation registers and project notes in this repository keep their names. They are never published, and links depend on them.
- Source files from the user (legacy guides, transcripts) keep the names they arrived with.
- The **review copy** that goes to the SME with a question round starts with `REVIEW COPY-` instead (D-100), for example `REVIEW COPY-220-Customer Payments PG v3.1.docx`. The working copy, with the review comments that match the validation register, keeps `CLAUDE-`.

## Versions (D-092)

A draft keeps its version number once it goes out for review. When Claude applies a round of answers to it, the minor version goes up (v3.0 → v3.1 → v3.2), in the same change:

- The Word file is renamed (`CLAUDE-220-Customer Payments PG v3.1.docx`) and every link to it is updated. The PDF, the Markdown preview and the register keep their file names.
- The guide's version history gets a row for the new version: date, author, BPO and a short description. Earlier rows keep what those versions were.
- In a version history row Claude writes (D-095), **Author/s** lists the SME first, then the PG owner, separated by a semicolon (`Maria Pabalan; Daniel Moreira`), and **Description of change** is a few words, for example *SME round 1 answers (draft)*. The detail goes in the register's Versions section, so the table stays small.
- The register's **Versions of the guide** section lists what changed in the new version, and its change log has the entry.
- The board card's version and Word link change, and the review copy carries the new number.

Changes made before a draft first goes out keep its number.

## Deliverables: the Word file only (D-064)

Claude produces the Word guide (`.docx`) and its repository companions (Markdown preview, validation register, project notes). It does not create, update, commit or send a PDF of a guide: the user makes the PDFs.

- Claude may render a PDF in its own scratchpad to check the layout or refresh the Contents page numbers, but it deletes that file and never commits or sends it.
- PDFs already in the repository stay as they are. When Claude changes a Word guide that has a PDF beside it, it says that the PDF is now out of date and leaves it for the user to replace.

## Pull requests: Claude merges them (D-065)

Until the user says otherwise, Claude merges every pull request it opens, once the pull request is ready: no merge conflict, every check that runs on it passed, and no review comment left open. It opens the pull request, marks it ready for review, merges it with a merge commit, and tells the user. If anything blocks the merge, Claude leaves the pull request open and says what blocks it.

## Key concepts: use the form the content needs (D-059)

The master template shows each key concept as a two-column `[Heading] | [Body/ Description]` table. That table is an example, not a rule: the authoring guide says to adapt the concept table to the information. For each concept under its Heading 5, choose the form that reads best:

- A table with as many columns as the information has, for example **Setting | Normal value | For the SPE journal** or **Check | Where | Passes when**. Use two columns only when the content is pairs, such as terms and meanings.
- Paragraphs for an explanation or a reason.
- A bulleted list for rules or items in no particular order, and a numbered list when the order matters.
- A mix of these, for example a lead paragraph, a table and an Important box.

Keep the template's look: tables copy the concept table (dark blue header row), paragraphs use **PG Body Text**, bulleted lists use **Bullet 1.2** (D-061), and warnings use the **PG Important Box**. Size table columns so that no word breaks across lines.

## Bullets and topic links (D-061)

- **Bullets:** every bulleted list in body text uses the **Bullet 1.2** style: Part Description, Initiation, Responsibility, Task Overview and Key concepts. Do not use **CW_Bullet 1** for these lists, even though the authoring guide's style table names it for Responsibility and Initiation: it uses the theme font and looks wrong beside body text. Inside procedure tables, the template's own bullets stay (Bullet 1.2 in PROCESS START and Description cells, the PROCESS START/END Body bullets in STEP COMPLETE rows, and CW_Bullet 1 in the navigation path).
- **Topic links:** when a link names a topic, the topic number is part of the link's display text, written as the heading shows it: **1. Map the CW1 Ledger to TM1** for a topic, **4.1 Complete the TB OB Tab** for a subtopic. This applies to the roles matrix, Topic Overview tables, checklists, "Continue to" links and cross-references in text. The Process table keeps the number in its own **#** column and links the title only, as the template shows.

## Links to other guides (D-096)

Every reference in a guide to another procedure guide is a hyperlink to that guide's published file on the Training Hub, never plain text.

- **Link text:** the guide's code and title, as in **200 Customer Onboarding and Maintenance**. A topic or section after it stays plain text (", section 3.4"), because the link opens the published PDF, not the topic. Never refer to another guide by its code alone ("see 220 topic 2.3"): write the title too.
- **Where the links come from:** [`standards/training-hub/`](standards/training-hub/README.md), from Daniel's export of Training Hub > Procedure Guides. `tools/pg_links.py "<guide>.docx" --fix` adds a missing link; without `--fix` it reports every hyperlink and every reference.
- **No link known:** when a referenced guide is not on the Training Hub, or the guide refers to another document or artifact (a spreadsheet, a scheduling file, a recording) whose link Claude does not have, it is an action for the PG owner: a register item and a review comment at the main place, with the other places in the register.
- **AVA, the Procedure Guides library and the Training Hub** are linked in each guide's Additional Resources (template). Keep those links.
- **Before committing or sending a guide,** run `tools/pg_links.py` on it: every reference to another guide shows as linked or has its item. Then refresh the card's hyperlink data on the board (the Links pill).

## People: name the role, not the person (D-099)

A guide names roles, never individual people: **Group Billing and Credit Manager**, not Chris Clarke; **Collections Manager**, not Arash Najafi. People change jobs; the role stays.

- This covers everything the reader sees: steps, Responsibility, Key concepts, tables and notes. The version history (authors, BPO) and notes to the author in the ACTION: REVIEW REQUIREMENT style may name people, as may the register and the board.
- When a source or an SME names a person, write their role. If the role is not known, it is an action for the PG owner: an ACTION placeholder in the text, a register item and a review comment.
- Known roles (Daniel Moreira, 23 November 2026): Christopher Clarke, **Group Billing and Credit Manager**; Arash Najafi, **Collections Manager**.
- Before committing or sending a guide, search it for people's names.

## Security roles and access (D-083)

Users do not know their security roles, so a guide never names one or asks about one.

- Where a guide needs to say how a user gets access, it says that their manager requests their D365 profile, which gives them the access they need.
- For a missing page, module or control, or any other access or security role issue, the guide tells the user to contact the **BAU Support team**.
- Do not raise register items, review comments or SME questions about security roles. Close any that come in from a source, citing D-083.

## Favorites (D-084)

260 O2C Getting Started teaches Favorites. Other guides give the navigation path only and do not remind the user that a page can also be opened from Favorites. A guide may still list the pages worth adding to Favorites for its work, as 230 Part 1 does.

- This applies to every guide Claude drafts, converts or rebuilds from now on, and to legacy or SME content brought into a guide.
- Before committing or sending a guide, search it for "Favorites" and remove any line that only tells the user they can open a page from Favorites.

## Page breaks (D-086, D-087)

Part 1, Part 2 and Part 3 each start on a new page, as the master template does, and so does every topic and subtopic in Part 2: Heading 3 (**2. Monitor Customers**), Heading 4 (**6.1 Preview and Download a Customer Statement**) and PG Further Subdivision (**6.1.1 Generate the Statement Preview**) (D-086, D-087). A heading that directly follows its parent heading, with nothing in between, stays on that page, as the first topic does under the Part 2 heading. Use **Page break before** on the heading's paragraph rather than an empty paragraph with a manual break.

- This applies to every guide Claude drafts, converts or rebuilds from now on.
- Before committing or sending a guide, check that no Part, topic or subtopic heading follows on from the previous page, then refresh the Contents page numbers.

## Internal notes to the author: `ACTION: REVIEW REQUIREMENT` (D-060)

Any text in a draft guide that speaks to the author or reviewer rather than the reader uses the template's **ACTION: REVIEW REQUIREMENT** style (yellow fill, red text), so it stands out as a note to resolve, not guide content. Examples: "This guide does not yet describe…", "to be confirmed", "Navigation to be confirmed", "No role is marked until…".

- A standalone note is its own paragraph in the paragraph style (a yellow box).
- A phrase inside a sentence, list or table cell uses the linked character style, **ACTION: REVIEW REQUIREMENT Char**, on those words only.
- Keep the note short and keep its review comment and validation item: the comment and the register stay the record of the question.
- Remove every note in this style before publication, with its item closed. Search for the style as part of the final check.
- Text that stays in the published guide, such as a real step whose detail is still being confirmed, keeps its normal style and carries only the review comment.

## The PG board (D-068)

The [PG Builder Board](https://claude.ai/artifact/5GPzzPrEYyUSAn12EBgWLf) is the single status tracker for every guide in every stream. Its page code is [`board/PG-Board.html`](board/PG-Board.html); its data lives in the board's database. The user and Claude both edit it. See [`board/README.md`](board/README.md) for the data model.

- **Start of a session that touches guides:** read what changed on the board since `meta/sync.lastSyncAt`: `log` entries not written by `claude`, rounds with status `answered`, and meetings with `processed: false`. Carry them into the repository (registers, decision logs, Word guides when the change asks for it), then set `meta/sync.lastSyncAt`.
- **Every change Claude commits to a guide updates its card in the same turn:** lane, version, next action, item counts and links, plus a `log` entry with `by: "claude"`.
- **Lanes** (whose turn): Initial Ticket Created (user), Drafting (Claude), Waiting for SME feedback (SME), Updating draft (Claude), Sent for sign-off (approver and BPO), Ready to publish (user), Published; Blocked and Withdrawn open from pills above the board. Claude never moves a card to Sign-off, Ready to publish or Published, and never marks a round sent, unless the user says it happened. A lane Claude infers gets `confirmed: false`.
- **Numbering** is read-only on the board. When the register in `standards/numbering/` changes, Claude refreshes `meta/register` in the same turn.

## Question rounds (D-069, D-085)

Questions go to the SME in rounds, one message per SME, kept on the board as `rounds` documents and opened from the questions link on each card (D-077). A round asks only for what the guide needs and the sources cannot give, so it stays short and quick to answer: usually fewer than ten questions.

**Before asking, read all the evidence:** the draft (comments, tables and embedded images, not only the text), the published guide and the legacy guides, the ADO ticket, related guides, recordings and transcripts, and the user's decisions. AI-generated meeting or training notes are a starting point to check against the recording, not confirmation.

**Sort every open item by what the evidence says:**

| Evidence | What Claude does |
|---|---|
| A current, relevant source answers it | Use it and close the item. Do not ask. |
| Answered elsewhere, missing from the draft | Write it in or cross-reference it, then close the item. |
| Screen labels, navigation, control names | The clean-session test in D365 confirms them. Do not ask. |
| From AI-generated notes | Check it against the recording. Do not ask. |
| Only an editorial or drafting choice | Resolve it while drafting. |
| Explicitly out of scope | Record the decision and close it. |
| Ambiguous, contradictory, or missing and material | Ask. |
| An interpretation made during conversion that changes the process | Ask to confirm it. |

An item is material when the answer changes what the reader does or understands: scope, responsibility, initiation, a missing system step, values and how to choose them, approval, sequence, completion checks, exceptions in scope, conflicting terms, or the guide's boundary. A newer source overrides an older one only where it covers the same case.

**Roles stay separate:** source contributor, the person who does the task, the transaction approver, the BPO, and the PG approver (Maria Pabalan for O2C, Ken Lee for R2R). Being the PG approver does not make someone the approver of every transaction in the guide. Do not ask an SME to reconfirm content carried over faithfully from their own or a published source: their final review of the guide is the check.

**Write each question so it is easy to answer:**

```
Q01 — Short topic label (p. 13, topic 1.1, step 5)
One or two sentences on what the guide says or lacks. Then the specific decision or instruction needed.
```

- One coherent point per question. Combine closely connected points, including across topics; keep unrelated decisions apart. Lettered parts only when a question cannot be answered without them.
- Proportionate: if one control is missing, ask for that control. If a whole procedure is missing, ask for a demonstration covering the path, actions, fields and values, approvals and the result.
- Plain, neutral wording with the exact system labels. Offer alternatives only when the evidence supports them, for example "should step 30 send them to 4.5?". No vague asks such as "please clarify this section", and no editing preferences framed as process questions.
- No fixed number of questions, and no questions made up to fill a list. If nothing is left to ask, say so and ask for a factual review instead.
- **Across guides:** when the same gap sits in several guides, one question covers all of them, in one ADO ticket, and the other cards point to it.

**References:** each question names the page, the topic and the step (D-082, D-088, D-089). **Word's Contents is the authority for pages.** Before a round is sent, the user opens the review copy in Word, updates the Contents (*Update entire table*) and sends back the saved copy, or a screenshot of the whole Contents. Claude then takes each heading's page from Word's Contents and moves the step pages inside each subtopic by the same amount; every topic and subtopic starts on its own page (D-087), so a step stays on the same page relative to its heading unless Word lays that subtopic out differently. With the saved copy, `tools/question_pages.py --word` gives every page exactly. Until Word's Contents is in, pages come from the review copy's layout (LibreOffice with DM Sans) as a first estimate: in 220 the layout ran one page short of Word from topic 2.2 on. The round says which source its pages come from.

**The message:** address the SME, name the guide and say briefly what the answers are for. Then the questions, then: reply against each question number, say if any do not apply, and assign the ticket back to Daniel when done. The board's copy text follows this layout. Do not invent recipients, dates or ticket numbers.

**Send the guide with the questions:** a review copy of the Word guide with the review comments taken out (the questions replace them), named `REVIEW COPY-<code>-<title> PG v<x.y>.docx` (D-100). Notes to the author stay. The review copy is a send file, not committed (D-079).

**Keep the record:** the guide's register lists the round's questions and items, and the route for every open item that is not asked (D-085). In the Word guide, the review comment of each asked item starts with its question number, for example *[Q04]*. Question numbers are stable once the round is sent: follow-ups refer to the original number, and a closed number is never reused.

**Answers:** apply them to the Word guide and the register, close the items they answer, and carry anything still open into the next round. A reply closes an item only if it gives the missing fact; an explicit scope decision, another verified source, or an agreed decision to keep the source wording can also close one. After an answer, check the roles, prerequisites, approvals and reports it affects. Never ask again for what a source already confirms.

## Word review comments: open items that need an answer (D-067)

A draft guide carries one review comment per item, at the place it matters most, and only for open items that still need an answer.

- **One comment per item.** When an item affects several places, the comment sits at the main one and the register lists the others.
- **No comment** for answered items, items carried over from topic drafts that the guide no longer needs answered, or non-blocking items: they stay in the validation register and on the board.
- Every `ACTION: REVIEW REQUIREMENT` note keeps its comment (D-060).
