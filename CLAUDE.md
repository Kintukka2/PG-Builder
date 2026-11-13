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

Keep the template's look: tables copy the concept table (dark blue header row), paragraphs use **PG Body Text**, bulleted lists use the **List Paragraph** bullets from *About this guide* (**CW_Bullet 1** stays for Responsibility and Initiation), and warnings use the **PG Important Box**. Size table columns so that no word breaks across lines.
