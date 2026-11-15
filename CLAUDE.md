# Working rules for Claude in this repository

## File names: the `CLAUDE-` prefix (D-056)

Every file Claude creates or rebuilds for the user starts with `CLAUDE-`: Word guides, PDFs, Excel workbooks, review pack zips and any other file Claude sends. The rest of the name follows the O2C PG Numbering Standard, for example `CLAUDE-260-O2C Getting Started PG v0.2.docx`.

- The prefix marks a Claude working file. It is removed when the file is published, so a published guide never carries it.
- When Claude rebuilds an existing file that has no prefix, it renames the file with the prefix in the same change and updates every link to it.
- Markdown previews, validation registers and project notes in this repository keep their names. They are never published, and links depend on them.
- Source files from the user (legacy guides, transcripts) keep the names they arrived with.

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
