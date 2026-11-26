"""Minimal WordprocessingML builders that copy the PG master template parts (as used in 230 v3.1)."""
import re, html

def esc(t): return html.escape(t, quote=False).replace('§', '*')

class Doc:
    def __init__(self):
        self.bm = 6000          # bookmark ids
        self.cid = 0            # comment ids
        self.comments = []      # (id, text)
        self.nums = []          # (numId, abstractNumId)
        self.next_num = 500
        self.toc = []           # (level, anchor, text)
        self.anchors = {}       # anchor -> display text
    def num(self, abstract):
        n = self.next_num; self.next_num += 1; self.nums.append((n, abstract)); return n
    def comment(self, text):
        i = self.cid; self.cid += 1; self.comments.append((i, text)); return i
    def bmk(self, name):
        i = self.bm; self.bm += 1
        return f'<w:bookmarkStart w:id="{i}" w:name="{name}"/>', f'<w:bookmarkEnd w:id="{i}"/>'

D = Doc()

# ---------- inline markup ----------
# **bold**  *italic*  [[anchor|text]] internal link  {{note}} ACTION char style  ``code``->plain
TOK = re.compile(r'(\*\*.+?\*\*|\*[^*]+?\*|\[\[[^\]]+\]\]|\{\{.+?\}\})')
def runs(text, rpr='', link_rpr=None):
    out = []
    for part in TOK.split(text):
        if not part: continue
        if part.startswith('**'):
            out.append(f'<w:r><w:rPr><w:b/>{rpr}</w:rPr><w:t xml:space="preserve">{esc(part[2:-2])}</w:t></w:r>')
        elif part.startswith('[['):
            a, _, t = part[2:-2].partition('|')
            out.append(f'<w:hyperlink w:anchor="{a}" w:history="1"><w:r><w:rPr><w:rStyle w:val="Hyperlink"/>{rpr}</w:rPr><w:t xml:space="preserve">{esc(t)}</w:t></w:r></w:hyperlink>')
        elif part.startswith('{{'):
            out.append(f'<w:r><w:rPr><w:rStyle w:val="ACTIONREVIEWREQUIREMENTChar"/>{rpr}</w:rPr><w:t xml:space="preserve">{esc(part[2:-2])}</w:t></w:r>')
        elif part.startswith('*') and part.endswith('*') and len(part) > 2:
            out.append(f'<w:r><w:rPr><w:i/>{rpr}</w:rPr><w:t xml:space="preserve">{esc(part[1:-1])}</w:t></w:r>')
        else:
            out.append(f'<w:r>{"<w:rPr>"+rpr+"</w:rPr>" if rpr else ""}<w:t xml:space="preserve">{esc(part)}</w:t></w:r>')
    return ''.join(out)

def wrap_comment(inner, comment):
    if not comment: return inner
    i = D.comment(comment)
    return (f'<w:commentRangeStart w:id="{i}"/>{inner}<w:commentRangeEnd w:id="{i}"/>'
            f'<w:r><w:rPr><w:rStyle w:val="CommentReference"/></w:rPr><w:commentReference w:id="{i}"/></w:r>')

def p(text='', style=None, ppr='', rpr='', comment=None):
    st = f'<w:pStyle w:val="{style}"/>' if style else ''
    pp = f'<w:pPr>{st}{ppr}</w:pPr>' if (st or ppr) else ''
    return f'<w:p>{pp}{wrap_comment(runs(text, rpr), comment)}</w:p>'

def blank(): return '<w:p/>'
def body(text, comment=None): return p(text, 'PGBodyText', comment=comment)
def lead(text): return p(text, 'PGBodyText', ppr='<w:keepNext/>')
def bodyblank(): return '<w:p><w:pPr><w:pStyle w:val="PGBodyText"/></w:pPr></w:p>'
def bullet(text, comment=None): return p(text, 'Bullet12', comment=comment)
def note(text, comment=None): return p('**Note:** ' + text, 'PGNotesBox', ppr='<w:keepLines/>', comment=comment)
def important(text, comment=None): return p('**Important:** ' + text, 'PGImportantBox', ppr='<w:keepLines/>', comment=comment)
def action_note(text, comment=None): return p(text, 'ACTIONREVIEWREQUIREMENT', comment=comment)
def h5(text): return p(text, 'Heading5')
def h5b(text, anchor):
    s_, e_ = D.bmk(anchor)
    return f'<w:p><w:pPr><w:pStyle w:val="Heading5"/></w:pPr>{s_}<w:r><w:t xml:space="preserve">{esc(text)}</w:t></w:r>{e_}</w:p>'

def heading(level, title, anchor, numbered=True, pagebreak=True, toc_text=None):
    style = {2: 'Heading2', 3: 'Heading3', 4: 'Heading4', 'f': 'PGFurtherSubdivision'}[level]
    ilvl = {3: 0, 4: 1, 'f': 2}.get(level)
    ppr = (f'<w:pStyle w:val="{style}"/>' + ('<w:pageBreakBefore/>' if pagebreak else '') +
           (f'<w:numPr><w:ilvl w:val="{ilvl}"/><w:numId w:val="71"/></w:numPr>' if numbered and ilvl is not None else ''))
    s, e = D.bmk(anchor)
    D.toc.append(({2: 2, 3: 3, 4: 4, 'f': 4}[level], anchor, toc_text or title))
    return f'<w:p><w:pPr>{ppr}</w:pPr>{s}<w:r><w:t xml:space="preserve">{esc(title)}</w:t></w:r>{e}</w:p>'

# ---------- tables ----------
HDR = '<w:shd w:val="clear" w:color="auto" w:fill="1D1765"/>'
BOT = '<w:tcBorders><w:bottom w:val="single" w:sz="4" w:space="0" w:color="000000" w:themeColor="text1"/></w:tcBorders>'
BLUE = '<w:shd w:val="clear" w:color="auto" w:fill="DEEAF6" w:themeFill="accent5" w:themeFillTint="33"/>'
GREEN = '<w:shd w:val="clear" w:color="auto" w:fill="E2EFD9" w:themeFill="accent6" w:themeFillTint="33"/>'
LOOK = '<w:tblLook w:val="04A0" w:firstRow="1" w:lastRow="0" w:firstColumn="1" w:lastColumn="0" w:noHBand="0" w:noVBand="1"/>'

def tbl(widths, rows_xml, fixed=False):
    grid = ''.join(f'<w:gridCol w:w="{w}"/>' for w in widths)
    lay = '<w:tblLayout w:type="fixed"/>' if fixed else ''
    return (f'<w:tbl><w:tblPr><w:tblStyle w:val="TableGrid"/><w:tblW w:w="{sum(widths)}" w:type="dxa"/>{lay}{LOOK}</w:tblPr>'
            f'<w:tblGrid>{grid}</w:tblGrid>{"".join(rows_xml)}</w:tbl>')

def tc(w, content, tcpr=''):
    return f'<w:tc><w:tcPr><w:tcW w:w="{w}" w:type="dxa"/>{tcpr}</w:tcPr>{content}</w:tc>'

def header_row(widths, labels):
    cells = ''.join(tc(w, p(l, 'Table-Heading'), HDR) for w, l in zip(widths, labels))
    return f'<w:tr><w:trPr><w:cantSplit/><w:tblHeader/></w:trPr>{cells}</w:tr>'

def cell_paras(content, first_bold=False):
    """content: str or list of str. '- ' prefix = Bullet 1.2; '> ' = CW_Bullet 1 nav; 'NOTE:' = note line."""
    items = content if isinstance(content, list) else [content]
    out = []
    for k, t in enumerate(items):
        if t.startswith('- '): out.append(p(t[2:], 'Bullet12'))
        elif t.startswith('> '): out.append(p('**' + t[2:] + '**', 'CWBullet1'))
        else:
            out.append(p(('**' + t + '**') if (first_bold and k == 0 and '**' not in t) else t))
    return ''.join(out)

def concept_table(headers, rows, widths=None, bold_first=True):
    n = len(headers)
    widths = widths or {2: [2425, 6647], 3: [2268, 3402, 3402], 4: [1800, 2424, 2424, 2424]}[n]
    out = [header_row(widths, headers)]
    for r in rows:
        cells = ''.join(tc(w, cell_paras(c, first_bold=(bold_first and j == 0))) for j, (w, c) in enumerate(zip(widths, r)))
        out.append(f'<w:tr><w:trPr><w:cantSplit/></w:trPr>{cells}</w:tr>')
    return tbl(widths, out)

def overview_table(rows):
    """rows: (anchor, display, description)"""
    W = [3312, 5760]
    out = [header_row(W, ['Step', 'Description'])]
    for a, disp, desc in rows:
        c1 = f'<w:p><w:pPr><w:rPr><w:sz w:val="18"/></w:rPr></w:pPr>{runs("[[" + a + "|" + disp + "]]", "<w:sz w:val=\"18\"/>")}</w:p>'
        c2 = f'<w:p><w:pPr><w:rPr><w:sz w:val="18"/></w:rPr></w:pPr>{runs(desc, "<w:sz w:val=\"18\"/>")}</w:p>'
        out.append(f'<w:tr><w:trPr><w:cantSplit/></w:trPr>{tc(W[0], c1)}{tc(W[1], c2)}</w:tr>')
    return tbl(W, out)

PW = [2592, 6480]
def boundary_row(label, fill, paras_xml):
    c1 = p(label, 'PROCESSSTARTENDBody')
    return f'<w:tr><w:trPr><w:cantSplit/></w:trPr>{tc(PW[0], c1, BOT + fill)}{tc(PW[1], paras_xml, BOT + fill)}</w:tr>'

def procedure(prereqs, resp, steps, end):
    """steps: list of (action, desc, comment). desc str or list. end: ('complete', [outcomes]) or ('step', [outputs], (anchor, text))"""
    numid = D.num(64)
    hdr_cell = lambda t, jc: (f'<w:p><w:pPr>{"<w:jc w:val=\"center\"/>" if jc else ""}<w:rPr><w:b/><w:bCs/></w:rPr></w:pPr>'
                              f'<w:r><w:rPr><w:b/><w:bCs/></w:rPr><w:t>{t}</w:t></w:r></w:p>')
    rows = [f'<w:tr><w:trPr><w:cantSplit/><w:tblHeader/></w:trPr>{tc(PW[0], hdr_cell("Action", True))}{tc(PW[1], hdr_cell("Description", False))}</w:tr>']
    start = p('Pre-requisites:', 'PROCESSSTARTENDBody') + ''.join(p(x, 'Bullet12') for x in prereqs) + \
            p('Responsibility:', 'PROCESSSTARTENDBody') + p(resp, 'Bullet12')
    rows.append(boundary_row('PROCESS START', BLUE, start))
    for st in steps:
        action, desc = st[0], st[1]; com = st[2] if len(st) > 2 else None
        ap = (f'<w:p><w:pPr><w:pStyle w:val="ListParagraph"/><w:numPr><w:ilvl w:val="0"/><w:numId w:val="{numid}"/></w:numPr>'
              f'<w:ind w:left="360" w:hanging="360"/></w:pPr>{wrap_comment(runs(action), com)}</w:p>')
        rows.append(f'<w:tr><w:trPr><w:cantSplit/></w:trPr>{tc(PW[0], ap, BOT)}{tc(PW[1], cell_paras(desc), BOT)}</w:tr>')
    if end[0] == 'complete':
        rows.append(boundary_row('PROCESS COMPLETE', GREEN, p('Outcomes:', 'PROCESSSTARTENDBody') + ''.join(p(x, 'Bullet12') for x in end[1])))
    else:
        bl = lambda t: (f'<w:p><w:pPr><w:pStyle w:val="PROCESSSTARTENDBody"/><w:numPr><w:ilvl w:val="0"/><w:numId w:val="75"/></w:numPr></w:pPr>{runs(t)}</w:p>')
        a, t = end[2]
        rows.append(boundary_row('STEP COMPLETE', BLUE, ''.join(bl(x) for x in end[1]) + bl(f'Continue to [[{a}|{t}]]')))
    return tbl(PW, rows, fixed=True)

def stream_table(stream, area, roles):
    W = [1900, 3225, 4084]
    out = [header_row(W, ['Stream', 'Process Area', 'Key Roles'])]
    out.append('<w:tr>' + tc(W[0], p(stream)) + tc(W[1], p(area)) + tc(W[2], ''.join(p(r, 'Bullet12') for r in roles)) + '</w:tr>')
    return tbl(W, out)

def process_table(rows):
    W = [535, 2070, 2250, 2970, 1242]
    out = [header_row(W, ['#', 'Action', 'Who', 'When', 'Where'])]
    for n, a, disp, who, when, where in rows:
        cells = (tc(W[0], f'<w:p><w:pPr><w:jc w:val="center"/></w:pPr>{runs(str(n))}</w:p>') + tc(W[1], p(f'[[{a}|{disp}]]')) +
                 tc(W[2], p(who)) + tc(W[3], p(when)) + tc(W[4], p(where)))
        out.append(f'<w:tr><w:trPr><w:cantSplit/></w:trPr>{cells}</w:tr>')
    return tbl(W, out, fixed=True)

def roles_matrix(roles, rows):
    W = [9072 - 1170 * len(roles)] + [1170] * len(roles)
    sz = '<w:sz w:val="18"/><w:szCs w:val="18"/>'
    hdr = tc(W[0], '<w:p><w:r><w:rPr><w:b/></w:rPr><w:t>Tasks / Business Roles</w:t></w:r></w:p>')
    for w, r in zip(W[1:], roles):
        hdr += tc(w, f'<w:p><w:pPr><w:ind w:left="113" w:right="113"/></w:pPr><w:r><w:rPr>{sz}</w:rPr><w:t xml:space="preserve">{esc(r)}</w:t></w:r></w:p>',
                  '<w:textDirection w:val="btLr"/><w:vAlign w:val="center"/>')
    out = [f'<w:tr><w:trPr><w:cantSplit/><w:trHeight w:val="1700"/><w:tblHeader/></w:trPr>{hdr}</w:tr>']
    LB = '<w:shd w:val="clear" w:color="auto" w:fill="DEEAF6" w:themeFill="accent5" w:themeFillTint="33"/>'
    for a, disp, marks in rows:
        c = tc(W[0], f'<w:p><w:pPr><w:rPr>{sz}</w:rPr></w:pPr>{runs("[[" + a + "|" + disp + "]]", sz)}</w:p>')
        for w, m in zip(W[1:], marks):
            c += tc(w, f'<w:p><w:pPr><w:jc w:val="center"/><w:rPr>{sz}</w:rPr></w:pPr>' + (f'<w:r><w:rPr>{sz}</w:rPr><w:t>R</w:t></w:r>' if m else '') + '</w:p>', '' if m else LB)
        out.append(f'<w:tr><w:trPr><w:cantSplit/></w:trPr>{c}</w:tr>')
    return tbl(W, out)

def report_table(nav, desc):
    W = [4135, 4937]
    numid = D.num(REPORT_ABSTRACT)
    hdr = (tc(W[0], '<w:p><w:pPr><w:ind w:left="720"/><w:rPr><w:b/><w:bCs/></w:rPr></w:pPr><w:r><w:rPr><w:b/><w:bCs/></w:rPr><w:t>Navigation</w:t></w:r></w:p>', HDR) +
           tc(W[1], '<w:p><w:pPr><w:rPr><w:b/><w:bCs/></w:rPr></w:pPr><w:r><w:rPr><w:b/><w:bCs/></w:rPr><w:t>Description</w:t></w:r></w:p>', HDR))
    navp = ''
    for k, n in enumerate(nav):
        last = k == len(nav) - 1
        navp += (f'<w:p><w:pPr><w:pStyle w:val="ListParagraph"/><w:numPr><w:ilvl w:val="0"/><w:numId w:val="{numid}"/></w:numPr></w:pPr>'
                 f'<w:r><w:rPr><w:b/><w:bCs/><w:i/><w:iCs/></w:rPr><w:t xml:space="preserve">{esc(n)}</w:t></w:r>'
                 + ('' if last else '<w:r><w:rPr><w:i/><w:iCs/></w:rPr><w:t xml:space="preserve"> &gt; </w:t></w:r>') + '</w:p>')
    dp = ''.join(p(x) for x in (desc if isinstance(desc, list) else [desc]))
    return tbl(W, [f'<w:tr><w:trPr><w:cantSplit/><w:tblHeader/></w:trPr>{hdr}</w:tr>',
                   f'<w:tr><w:trPr><w:cantSplit/></w:trPr>{tc(W[0], navp)}{tc(W[1], dp)}</w:tr>'])

REPORT_ABSTRACT = None  # set by builder from numbering.xml (abstract of numId 132)

def topic_block(desc_paras, resp, init, overview=None):
    out = [blank(), h5('Description')] + [body(x) if isinstance(x, str) else x for x in desc_paras] + [bodyblank(),
           h5('Responsibility')] + [bullet(x) for x in resp] + [bodyblank(), h5('Initiation')] + [bullet(x) for x in init] + [bodyblank()]
    if overview:
        out += [h5('Topic Overview'), lead('This topic includes these steps:'), overview_table(overview)]
    return out
