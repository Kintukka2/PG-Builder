# Tools

Scripts Claude uses to keep the board's question rounds pointing at the right place in a guide (D-079, D-080, D-082). They need Python 3 with `lxml`, LibreOffice (`soffice`) and `pdftotext`.

| Script | What it does |
|---|---|
| [`install_fonts.sh`](install_fonts.sh) | Installs DM Sans, the font of the PG master template, from Google Fonts. Run it once per session before any render: without it LibreOffice uses another font and the pages fall well short of Word's. |
| [`question_locations.py`](question_locations.py) | Reads a Word guide and returns, for each review comment, the section it sits in (Part 1 section, or topic and procedure number) and the step. `python3 tools/question_locations.py "<guide>.docx"` prints the list. |
| [`question_pages.py`](question_pages.py) | Turns a location such as `3.3.1 steps 3, 4` or `Part 1, Key concepts (Settlement)` into pages, for example `p. 46`. Whole sections get their page range. `python3 tools/question_pages.py "<guide>.docx" "3.6 step 9" --contents` prints where each Contents entry falls and the pages for each location. Add `--word` for a copy saved in Word, or `--pdf "<file>.pdf"` for a PDF the user exported from Word. |

## Where the pages come from

Only pages verified in Word are shown to an SME (D-082, D-085). Until then a question names the topic and step only.

- **A copy saved in Word (exact).** Word records its page breaks in the file when it saves. With `--word`, the script reads them. It refuses a file whose breaks do not add up to the page count Word saved with it (a file edited after Word saved it).
- **A PDF exported from Word (exact).** With `--pdf`, the script reads the pages of that PDF and the structure of the Word file.
- **A LibreOffice render (estimate, for Claude only).** Without either, the script renders the guide. With DM Sans installed, short guides match Word (260: 237 of 238 paragraphs on the same page), but long tables fall differently (220 runs 2 pages short from topic 3). Use it to check a layout, never as a reference for the SME.

`--write-contents` writes the page numbers found into the guide's Contents, so the Contents agrees with the pages the questions give.

Page numbers follow the guide as it is laid out now. When a guide changes, Claude recalculates the pages for its open rounds in the same turn.
