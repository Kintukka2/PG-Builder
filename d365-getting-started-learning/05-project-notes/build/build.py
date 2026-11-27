import re, json, os, shutil, zipfile, sys, html
sys.path.insert(0, os.path.dirname(__file__))
import pgxml
from pgxml import D, esc

SRC = '/home/user/PG-Builder/ar-collections-learning/01-procedure-guides/CLAUDE-230-Collections PG v3.1.docx'
OUT = sys.argv[1]
B = os.path.dirname(os.path.abspath(__file__))
import tempfile; work = tempfile.mkdtemp()
with zipfile.ZipFile(SRC) as z: z.extractall(work)

num = open(f'{work}/word/numbering.xml').read()
pgxml.REPORT_ABSTRACT = re.search(r'<w:num w:numId="132"[^>]*><w:abstractNumId w:val="(\d+)"', num).group(1)
assert re.search(r'<w:num w:numId="82"[^>]*><w:abstractNumId w:val="64"', num)

from content_part1 import part1
from content_part2a import part2a
from content_part2b import part2b
from content_part2c import part2c, part3
middle = part1() + part2a() + part2b() + part2c() + part3()

doc = open(f'{work}/word/document.xml').read()
bstart = doc.index('<w:body>') + 8; bend = doc.rindex('<w:sectPr')
head, body, tail = doc[:bstart], doc[bstart:bend], doc[bend:]
def split(body):
    els=[]; stack=[]; start=None
    for m in re.finditer(r'<(/?)w:(p|tbl|sdt|bookmarkStart|bookmarkEnd)\b[^>]*?(/?)>', body):
        close, tag, selfc = m.groups()
        if not stack and not close:
            if selfc: els.append(body[m.start():m.end()]); continue
            start = m.start(); stack.append(tag)
        elif close:
            if stack and stack[-1] == tag:
                stack.pop()
                if not stack: els.append(body[start:m.end()])
        elif not selfc: stack.append(tag)
    return els
els = split(body)
assert ''.join(els) == body, 'element split mismatch'
assert 'Part 1: What do I need to know?' in re.sub('<[^>]+>', '', els[49]) and re.sub('<[^>]+>', '', els[670]).startswith('Additional Resources')
prefix, suffix = els[:49], els[670:]

def nocomments(s):
    s = re.sub(r'<w:commentRange(Start|End) w:id="\d+"/>', '', s)
    return re.sub(r'<w:r>(?:(?!</w:r>).)*?<w:commentReference w:id="\d+"/></w:r>', '', s, flags=re.S)
prefix = [nocomments(x) for x in prefix]; suffix = [nocomments(x) for x in suffix]

# cover title
t = prefix[9]; assert 'Collections' in t
prefix[9] = t.replace('Collections', 'Getting Started', 1)
assert 'Collections' not in re.sub('<[^>]+>', '', prefix[9])
# About this guide sentence
assert 'D365 F&amp;O: Collections process' in prefix[27]
prefix[27] = prefix[27].replace('D365 F&amp;O: Collections process', 'D365 F&amp;O: Getting Started guide')
# any other 'Collections' text left in prefix?
for i, x in enumerate(prefix):
    txt = re.sub('<[^>]+>', '', x)
    if 'Collections' in txt and i != 20: print('WARN prefix', i, txt[:80])

# version history: header row + one row
vt = prefix[21]
rows = re.findall(r'<w:tr\b.*?</w:tr>', vt, re.S)
def set_cells(row, texts):
    cells = re.findall(r'<w:tc>.*?</w:tc>', row, re.S); assert len(cells) == len(texts)
    for c, t in zip(cells, texts):
        tcpr = re.search(r'<w:tcPr>.*?</w:tcPr>', c, re.S).group(0)
        ppr = re.search(r'<w:pPr>.*?</w:pPr>', c, re.S); ppr = ppr.group(0) if ppr else ''
        paras = ''.join(f'<w:p>{ppr}{pgxml.runs(x)}</w:p>' for x in t.split('\n'))
        row = row.replace(c, f'<w:tc>{tcpr}{paras}</w:tc>', 1)
    return row
newrow = set_cells(rows[1], ['0.1', 'November 2026', 'Daniel Moreira', 'Ken Lee', 'First draft from the discovery (draft)'])
prefix[21] = vt[:vt.index(rows[0])] + rows[0] + newrow + vt[vt.index(rows[-1]) + len(rows[-1]):]

# Contents (TOC)
sdt = prefix[20]
ps = list(re.finditer(r'<w:p\b(?:(?!<w:p\b).)*?</w:p>|<w:p/>', sdt, re.S))
first_entry = next(m for m in ps if 'TOC \\o' in m.group(0))
end_para = ps[-1]
entry_tpl = {lvl: re.search(r'<w:pPr><w:pStyle w:val="TOC%d"/>.*?</w:pPr>' % lvl, sdt, re.S).group(0) for lvl in (2, 3, 4)}
def entry(lvl, anchor, text, first=False):
    fld = ('<w:r><w:fldChar w:fldCharType="begin"/><w:instrText xml:space="preserve">TOC \\o "2-4" \\t "PG Further Subdivision,4" \\h \\* MERGEFORMAT</w:instrText><w:fldChar w:fldCharType="separate"/></w:r>' if first else '')
    return (f'<w:p>{entry_tpl[lvl]}{fld}<w:hyperlink w:anchor="{anchor}" w:history="1"><w:r><w:rPr><w:rStyle w:val="Hyperlink"/></w:rPr><w:t xml:space="preserve">{esc(text)}</w:t></w:r>'
            f'<w:r><w:tab/><w:fldChar w:fldCharType="begin"/><w:instrText xml:space="preserve"> PAGEREF {anchor} \\h </w:instrText><w:fldChar w:fldCharType="separate"/><w:t>1</w:t><w:fldChar w:fldCharType="end"/></w:r></w:hyperlink></w:p>')
about = re.search(r'w:anchor="(_Toc\d+)"[^>]*><w:r><w:rPr><w:rStyle w:val="Hyperlink"/></w:rPr><w:t xml:space="preserve">About this guide', sdt).group(1)
addl = re.search(r'w:name="(_Toc\d+)"', suffix[0]).group(1)
entries = [entry(2, about, 'About this guide', first=True)] + [entry(l, a, t) for l, a, t in D.toc] + [entry(2, addl, 'Additional Resources')]
prefix[20] = sdt[:first_entry.start()] + ''.join(entries) + sdt[end_para.start():]

newbody = ''.join(prefix) + ''.join(middle) + ''.join(suffix)
doc = head + newbody + tail
open(f'{work}/word/document.xml', 'w').write(doc)

# numbering
add = ''.join(f'<w:num w:numId="{n}"><w:abstractNumId w:val="{a}"/><w:lvlOverride w:ilvl="0"><w:startOverride w:val="1"/></w:lvlOverride></w:num>' for n, a in D.nums)
num = num.replace('</w:numbering>', add + '</w:numbering>')
open(f'{work}/word/numbering.xml', 'w').write(num)

# comments
c = open(f'{work}/word/comments.xml').read()
root_open = re.search(r'<w:comments\b[^>]*>', c).group(0)
cm = ''.join(
    f'<w:comment w:id="{i}" w:author="Validation register" w:date="2026-11-27T00:00:00Z" w:initials="VR"><w:p><w:r><w:rPr><w:rStyle w:val="CommentReference"/></w:rPr><w:annotationRef/></w:r>'
    f'<w:r><w:rPr><w:color w:val="000000"/><w:sz w:val="20"/><w:szCs w:val="20"/></w:rPr><w:t xml:space="preserve">{esc(t)}</w:t></w:r></w:p></w:comment>' for i, t in D.comments)
c = c[:c.index(root_open) + len(root_open)] + cm + '</w:comments>'
open(f'{work}/word/comments.xml', 'w').write(c)
for extra in ('commentsExtended.xml', 'commentsIds.xml', 'commentsExtensible.xml'):
    assert not os.path.exists(f'{work}/word/{extra}'), extra

# core properties title
core = open(f'{work}/docProps/core.xml').read()
core = re.sub(r'<dc:title>.*?</dc:title>', '<dc:title>D365 F&amp;O: Getting Started</dc:title>', core)
open(f'{work}/docProps/core.xml', 'w').write(core)

# zip in original order
with zipfile.ZipFile(SRC) as zs, zipfile.ZipFile(OUT, 'w', zipfile.ZIP_DEFLATED) as zo:
    for info in zs.infolist():
        zo.write(os.path.join(work, info.filename), info.filename)
json.dump({'comments': D.comments, 'toc': D.toc}, open(os.path.join(B, 'build_meta.json'), 'w'), indent=1)
print('built', OUT, 'comments', len(D.comments), 'tables nums', len(D.nums), 'toc', len(D.toc))
