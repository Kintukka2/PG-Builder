"""Markdown preview of a PG Word file: headings, paragraphs, tables, review-comment markers."""
import sys, re, docx
from docx.oxml.ns import qn
src, out = sys.argv[1], sys.argv[2]
d = docx.Document(src)
cmt = {}
try:
    cpart = d.part.package.part_related_by  # noqa
except Exception: pass
import zipfile
c = zipfile.ZipFile(src).read('word/comments.xml').decode()
for cid, body in re.findall(r'<w:comment w:id="(\d+)".*?>(.*?)</w:comment>', c, re.S):
    t = ''.join(re.findall(r'<w:t[^>]*>([^<]*)', body)); m = re.match(r'(GS-\d+)', t); cmt[cid] = m.group(1) if m else t[:20]
def ptext(p):
    out = []
    for el in p._p.iter():
        if el.tag == qn('w:r'):
            t = ''.join(x.text or '' for x in el.iter(qn('w:t')))
            if not t: continue
            rpr = el.find(qn('w:rPr'))
            b = rpr is not None and rpr.find(qn('w:b')) is not None and rpr.find(qn('w:b')).get(qn('w:val')) not in ('0','false')
            i = rpr is not None and rpr.find(qn('w:i')) is not None
            st = rpr.find(qn('w:rStyle')).get(qn('w:val')) if rpr is not None and rpr.find(qn('w:rStyle')) is not None else ''
            if st == 'ACTIONREVIEWREQUIREMENTChar': t = f'<mark>{t}</mark>'
            elif b and t.strip(): t = f'**{t}**'
            elif i and t.strip(): t = f'*{t}*'
            out.append(t)
        elif el.tag == qn('w:commentReference'):
            out.append(f' `[{cmt.get(el.get(qn("w:id")), "?")}]`')
    s = ''.join(out).replace('****', '')
    return s
lines = []
num = {'h3': 0, 'h4': 0}
started = False
for el in d.element.body.iterchildren():
    if el.tag == qn('w:p'):
        p = docx.text.paragraph.Paragraph(el, d); st = p.style.name; t = ptext(p).strip()
        if st == 'Heading 2' and t.startswith('Part 1'): started = True
        if not started or not t: continue
        if st == 'Heading 2': lines += ['', '---', '', '## ' + t]
        elif st == 'Heading 3': num['h3'] += 1; num['h4'] = 0; lines += ['', f'### {num["h3"]}. {t}']
        elif st == 'Heading 4':
            if t in ('High-level process', 'Roles and responsibilities', 'Key concepts'): lines += ['', '### ' + t]
            else: num['h4'] += 1; lines += ['', f'#### {num["h3"]}.{num["h4"]} {t}']
        elif st == 'Heading 5': lines += ['', '##### ' + t]
        elif st.startswith('Bullet') or st.startswith('CW_Bullet'): lines.append('- ' + t)
        elif st == 'PG Notes Box': lines += ['', '> ' + t]
        elif st == 'PG Important Box': lines += ['', '> ' + t]
        elif st.startswith('ACTION'): lines += ['', f'<mark>{t}</mark>']
        else: lines += ['', t]
        if st == 'Heading 2' and t.startswith('Additional'): break
    elif el.tag == qn('w:tbl') and started:
        t = docx.table.Table(el, d); rows = []
        for r in t.rows:
            cells = []
            for cell in r.cells:
                ps = []
                for p in cell.paragraphs:
                    s = ptext(p).strip()
                    if not s: continue
                    stn = p.style.name
                    if stn.startswith('Bullet') or stn.startswith('CW_Bullet'): s = '• ' + s
                    ps.append(s)
                cells.append('<br>'.join(ps).replace('|', '\\|'))
            rows.append(cells)
        if rows and rows[0] and rows[0][0] in ('Action', '**Action**'):
            n = 0
            for r in rows[1:]:
                if r[0].replace('*', '') in ('PROCESS START', 'PROCESS COMPLETE', 'STEP COMPLETE'): r[0] = f'*{r[0].replace("*","")}*'
                else: n += 1; r[0] = f'{n}. {r[0]}'
        lines += [''] + ['| ' + ' | '.join(rows[0]) + ' |', '|' + '---|' * len(rows[0])] + ['| ' + ' | '.join(r) + ' |' for r in rows[1:]]
hdr = open(sys.argv[3]).read() if len(sys.argv) > 3 else ''
open(out, 'w').write(hdr + '\n'.join(lines).lstrip() + '\n')
print('lines', len(lines))
