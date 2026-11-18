# Tools

Scripts Claude uses to keep the board's question rounds pointing at the right place in a guide (D-079, D-080, D-082). They need Python 3 with `lxml`, LibreOffice (`soffice`) and `pdftotext`.

| Script | What it does |
|---|---|
| [`install_fonts.sh`](install_fonts.sh) | Installs DM Sans, the font of the PG master template, from Google Fonts. Run it once per session before any render: without it LibreOffice uses another font and the pages fall well short of Word's. |
| [`review_copy.py`](review_copy.py) | Builds the review copy that goes to the SME with the questions (D-079): every review comment is taken out, and each comment that starts with a question number, for example *[Q04]*, becomes a small yellow **[Q04]** tag at the end of the text it marked (never inside a heading). `python3 tools/review_copy.py "<guide>.docx" "<review copy>.docx"`. Uses [`docx_edit.py`](docx_edit.py). |
| [`question_locations.py`](question_locations.py) | Reads a Word guide and returns, for each review comment, the section it sits in (Part 1 section, or topic and procedure number) and the step. `python3 tools/question_locations.py "<guide>.docx"` prints the list. |
| [`question_pages.py`](question_pages.py) | Turns a location such as `3.3.1 steps 3, 4` or `Part 1, Key concepts (Settlement)` into pages, for example `p. 46`. Whole sections get their page range. `python3 tools/question_pages.py "<guide>.docx" "3.6 step 9" --contents` prints where each Contents entry falls and the pages for each location. Add `--word` for a copy saved in Word, or `--pdf "<file>.pdf"` for a PDF the user exported from Word. |

## Where the pages come from

Questions carry the pages of the review copy that goes with them (D-088): run the script on that copy and write the same pages into its Contents with `--write-contents`. A copy saved in Word or a PDF exported from it replaces them with Word's own pages.

- **A copy saved in Word (exact).** Word records its page breaks in the file when it saves. With `--word`, the script reads them. It refuses a file whose breaks do not add up to the page count Word saved with it (a file edited after Word saved it).
- **A PDF exported from Word (exact).** With `--pdf`, the script reads the pages of that PDF and the structure of the Word file.
- **A LibreOffice render.** Without either, the script renders the guide with DM Sans. Every topic and subtopic starts on its own page (D-087), so the render and Word can differ only inside a long subtopic.

`--write-contents` writes the page numbers found into the guide's Contents. A heading is placed on the first page where its title stands on a line of its own, so a Contents line or an overview-table entry does not count. If any heading cannot be placed, nothing is written.

Page numbers follow the guide as it is laid out now. When a guide changes, Claude recalculates the pages for its open rounds in the same turn.
