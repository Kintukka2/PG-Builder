# Tools

Scripts Claude uses to keep the board's question rounds pointing at the right place in a guide (D-079, D-080). They need Python 3 with `lxml`, LibreOffice (`soffice`) and `pdftotext`.

| Script | What it does |
|---|---|
| [`question_locations.py`](question_locations.py) | Reads a Word guide and returns, for each review comment, the section it sits in (Part 1 section, or topic and procedure number) and the step. `python3 tools/question_locations.py "<guide>.docx"` prints the list. |
| [`question_pages.py`](question_pages.py) | Renders the guide, reads the page numbers in its Contents, and turns a location such as `3.3.1 steps 3, 4` or `Part 1, Key concepts (Settlement)` into pages, for example `p. 46`. Whole sections get their page range from the Contents. |

Page numbers follow the guide as it is laid out now. When a guide changes, Claude recalculates the pages for its open rounds in the same turn.
