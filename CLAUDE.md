# Working rules for Claude in this repository

## File names: the `CLAUDE-` prefix (D-056)

Every file Claude creates or rebuilds for the user starts with `CLAUDE-`: Word guides, PDFs, Excel workbooks, review pack zips and any other file Claude sends. The rest of the name follows the PG numbering standards in `standards/numbering/` (D-070), for example `CLAUDE-260-O2C Getting Started PG v0.2.docx`. A document that is not a procedure guide uses its O-number from the Other series in place of the code, for example `CLAUDE-O-0001-CW1 to D365 Migration PG v0.1.docx` (D-071, D-076).

- The prefix marks a Claude working file. It is removed when the file is published, so a published guide never carries it.
- When Claude rebuilds an existing file that has no prefix, it renames the file with the prefix in the same change and updates every link to it.
- Markdown previews, validation registers and project notes in this repository keep their names. They are never published, and links depend on them.
- Source files from the user (legacy guides, transcripts) keep the names they arrived with.

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

## Question rounds (D-069)

Questions go to the SME in rounds, one message per SME, kept on the board as `rounds` documents and opened from the questions link on each card (D-077).

- **Combine:** one question covers as many register items as one answer can close. Group by theme (approvals, roles, navigation, configuration values, scope) and by who answers.
- **Lettered parts** keep a big question answerable; each part lists the item IDs it closes.
- **Where to look:** each part ends with the pages to look at, for example *(see p. 16-37)* (D-080). Pages come from where the part's items sit in the guide and from the page numbers in its Contents; a whole section gets its page range. Recalculate them with [`tools/question_pages.py`](tools/question_pages.py) whenever the guide changes.
- **Send the guide with the questions:** a review copy of the Word guide with the review comments taken out (the questions replace them). Notes to the author stay. The review copy is a send file, not committed (D-079).
- **Across guides:** when the same gap sits in several guides, one question covers all of them, in one ADO ticket, and the other cards point to it.
- **Split only when** different people answer or the items have nothing in common.
- **Answers:** apply them to the Word guide and the register, close the items they answer, and carry anything still open into the next round. An answer that does not close the gap leaves the item open; an explicit scope decision can close one. Never ask again for what a source already confirms.

## Word review comments: open items that need an answer (D-067)

A draft guide carries one review comment per item, at the place it matters most, and only for open items that still need an answer.

- **One comment per item.** When an item affects several places, the comment sits at the main one and the register lists the others.
- **No comment** for answered items, items carried over from topic drafts that the guide no longer needs answered, or non-blocking items: they stay in the validation register and on the board.
- Every `ACTION: REVIEW REQUIREMENT` note keeps its comment (D-060).
