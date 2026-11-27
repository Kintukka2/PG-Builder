# Builder for D365 F&O Getting Started v0.1

The scripts that built `CLAUDE-TBC-D365 F&O Getting Started PG v0.1.docx` from the master template parts in 230 Collections v3.1, kept so the first draft can be rebuilt or audited. Later versions are edited in the Word file, not rebuilt.

| File | Role |
|---|---|
| `pgxml.py` | Template parts: headings with numbering and bookmarks, PG Body Text, Bullet 1.2, Notes and Important boxes, ACTION notes, concept, Topic Overview, procedure, Process, Stream, roles and report tables, review comments |
| `content_part1.py`, `content_part2a.py`, `content_part2b.py`, `content_part2c.py` | The guide's content: Part 1, topics 1 to 3, 4 to 8, and 9 to 13 with Part 3 |
| `build.py` | Takes the front matter and Additional Resources from 230 v3.1, replaces Part 1 to Part 3, rebuilds the Contents, numbering and comments: `python3 build.py "<out>.docx"` |
| `to_md.py`, `md_head.md` | Builds the Markdown preview from the Word file |

After a build, run `tools/question_pages.py "<guide>.docx" --contents --write-contents` for the Contents page numbers and `tools/pg_links.py` for the links (D-096).

**Screenshots (27 November 2026).** `img_map.py` lists the 35 Microsoft Learn images used as placeholders and their captions; `STEP_IMG` in `pgxml.py` places each in its step. They were converted to PNG (SVGs rendered with Chromium) into a scratch folder set as `IMGDIR` in `build.py`. The images themselves are in the Word file and, for most, in [`../discovery/media/`](../discovery/media/); the training-module ones came from the full Learn harvest, which is not kept.
