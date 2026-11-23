"""Hyperlinks in a PG Word guide (D-096).

Counts every hyperlink, finds each reference to another procedure guide, and says whether it links to that
guide's published file on the Training Hub (standards/training-hub/training-hub-pgs.json).

  python3 tools/pg_links.py "<guide>.docx"            # report
  python3 tools/pg_links.py "<guide>.docx" --json     # the data the board shows (guides/<id>.hyperlinks)
  python3 tools/pg_links.py "<guide>.docx" --fix      # add the Training Hub link to every reference that has none

A reference is a guide code followed by its title (published, numbered or known alias), or by "topic",
"section", "version" or "v<digit>". The guide's own code, the Contents, and text in the ACTION: REVIEW
REQUIREMENT styles are left out. --fix links the code and title only; a reference with no title is reported
for rewording, because a link that reads "220" alone does not tell the reader what it opens.
"""
import sys, os, re, json, zipfile, copy, argparse, datetime
from lxml import etree

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
W = 'http://schemas.openxmlformats.org/wordprocessingml/2006/main'
R = 'http://schemas.openxmlformats.org/officeDocument/2006/relationships'
PR = 'http://schemas.openxmlformats.org/package/2006/relationships'
HL_TYPE = 'http://schemas.openxmlformats.org/officeDocument/2006/relationships/hyperlink'
ns = {'w': W}
def q(t): return '{%s}%s' % (W, t)

HUB = json.load(open(os.path.join(ROOT, 'standards', 'training-hub', 'training-hub-pgs.json')))
REG = json.load(open(os.path.join(ROOT, 'standards', 'numbering', 'PG_Numbering_Master_Register.json')))
# titles a guide is known by besides its published and numbered titles (proposed new titles)
ALIASES = {'240': ['Direct Debit and Credit Card Payments'], '420': ['Intercompany Accounting & Reconciliation']}

def titles():
    t = {}
    for g in HUB['guides']: t.setdefault(g['code'], set()).add(g['title'])
    def walk(o):
        if isinstance(o, dict):
            if 'code' in o and 'title' in o: yield o
            for v in o.values(): yield from walk(v)
        elif isinstance(o, list):
            for v in o: yield from walk(v)
    for g in walk(REG):
        if re.fullmatch(r'\d{3}', str(g['code'])): t.setdefault(str(g['code']), set()).add(g['title'])
    for c, a in ALIASES.items(): t.setdefault(c, set()).update(a)
    return {c: sorted(v, key=len, reverse=True) for c, v in t.items()}
TITLES = titles()
HUBURL = {g['code']: g['url'] for g in HUB['guides']}
HUBTITLE = {g['code']: g['title'] for g in HUB['guides']}

def norm(u): return re.sub(r'[?#].*$', '', (u or '').replace('&amp;', '&')).rstrip('/').lower()
def style(p):
    s = p.find('w:pPr/w:pStyle', ns); return s.get(q('val')) if s is not None else ''
def ptext(el): return ''.join(t.text or '' for t in el.iter(q('t')))

def segments(p, rels):
    """Text runs of a paragraph in order: (run, text, link, action). link is None, ('anchor', name) or ('url', target)."""
    out = []
    pact = style(p) == 'ACTIONREVIEWREQUIREMENT'
    def walk(node, link):
        for ch in node:
            tag = etree.QName(ch).localname
            if tag == 'hyperlink':
                a = ch.get(q('anchor')); rid = ch.get('{%s}id' % R)
                walk(ch, ('anchor', a) if a else ('url', rels.get(rid, '')))
            elif tag == 'r':
                rs = ch.find('w:rPr/w:rStyle', ns)
                act = pact or (rs is not None and 'ACTIONREVIEW' in rs.get(q('val')))
                t = ''.join((x.text or '') if etree.QName(x).localname == 't' else ('\t' if etree.QName(x).localname == 'tab' else '') for x in ch)
                out.append((ch, t, link, act))
            elif tag in ('smartTag', 'ins', 'sdt', 'sdtContent', 'fldSimple'):
                walk(ch, link)
    walk(p, None)
    return out

def find_refs(text, own):
    """(start, end, code, titled) for each reference to another guide in text."""
    found = []
    for m in re.finditer(r'(?<![\w.§/-])(\d{3})(?![\w.%/-])', text):
        code = m.group(1)
        if code == own or code not in TITLES: continue
        rest = text[m.end():]
        hit = None
        for t in TITLES[code]:
            mm = re.match(r'[  ]+' + re.escape(t) + r'(?![\w])', rest, re.I)
            if mm: hit = (m.start(), m.end() + mm.end(), code, True); break
        if not hit and re.match(r'[  ]*(,\s*)?(topic|section|§|version|v\d|\(v\d)', rest, re.I):
            hit = (m.start(), m.end(), code, False)
        if hit: found.append(hit)
    return found

def where_map(body):
    """Location label for every top-level body element, and a function giving the step for a table row."""
    labels = {}; keep = list(body); part = 0; t = s = k = 0; topic = 'Cover and version history'; h5 = ''
    for el in body:
        tag = etree.QName(el).localname
        if tag == 'p':
            st = style(el); tx = ptext(el).strip()
            if st == 'Heading2':
                part = 1 if tx.startswith('Part 1') else 2 if tx.startswith('Part 2') else 3 if tx.startswith('Part 3') else 9
                topic = tx.split(':')[0] if part in (1, 2, 3) else tx; h5 = ''
            elif st == 'Heading3' and part == 2: t += 1; s = k = 0; topic = '%d. %s' % (t, tx); h5 = ''
            elif st == 'Heading4' and part == 2: s += 1; k = 0; topic = '%d.%d %s' % (t, s, tx); h5 = ''
            elif st == 'PGFurtherSubdivision' and part == 2: k += 1; topic = '%d.%d.%d %s' % (t, s, k, tx); h5 = ''
            elif st == 'Heading4' and part == 1: topic = 'Part 1, ' + tx; h5 = ''
            elif st == 'Heading5': h5 = tx
        labels[el] = (topic, h5)
    labels['_keep'] = keep
    return labels

def step_of(tbl, tr):
    rows = tbl.findall('w:tr', ns)
    first = [ptext(c).strip() for c in rows[0].findall('w:tc', ns)]
    if first[:2] != ['Action', 'Description'] or 'PROCESS START' not in ptext(tbl): return None
    if 'PROCESS START' in ptext(tr): return 'PROCESS START'
    if 'COMPLETE' in ptext(tr.findall('w:tc', ns)[0]): return 'outcomes'
    n = 0
    for r in rows[1:rows.index(tr) + 1]:
        p = r.find('w:tc/w:p', ns)
        if p is not None and p.find('w:pPr/w:numPr', ns) is not None: n += 1
    return 'step %d' % n

def scan(path):
    z = zipfile.ZipFile(path)
    doc = etree.fromstring(z.read('word/document.xml'))
    relx = etree.fromstring(z.read('word/_rels/document.xml.rels'))
    rels = {r.get('Id'): r.get('Target') for r in relx}
    own = (re.search(r'CLAUDE-(\d{3})-', os.path.basename(path)) or re.search(r'(?:^|/)(\d{3})-', path) or [None, None])[1]
    body = doc.find('w:body', ns)
    labels = where_map(body)
    counts = {'all': 0, 'contents': 0, 'internal': 0, 'external': 0}
    for h in body.iter(q('hyperlink')):
        counts['all'] += 1
        p = next(h.iterancestors(q('p')))
        if style(p).startswith('TOC'): counts['contents'] += 1
        elif h.get(q('anchor')): counts['internal'] += 1
        else: counts['external'] += 1
    refs, other = [], []
    for p in body.iter(q('p')):
        if style(p).startswith('TOC'): continue
        anc = p
        while anc.getparent() is not body: anc = anc.getparent()
        topic, h5 = labels[anc]
        tr = next(p.iterancestors(q('tr')), None)
        if tr is not None:
            tbl = tr.getparent()
            while tbl.getparent() is not body and next(tbl.iterancestors(q('tr')), None) is not None:
                tr = next(tbl.iterancestors(q('tr'))); tbl = tr.getparent()
            st = step_of(tbl, tr)
        else: st = None
        where = topic + (' (%s)' % h5 if topic.startswith('Part 1') and h5 else '') + (', ' + st if st else '')
        segs = segments(p, rels)
        text = ''.join(s[1] for s in segs)
        pos = []; o = 0
        for s in segs: pos.append((o, o + len(s[1]), s)); o += len(s[1])
        for a, b, s in pos:
            if s[2] and s[2][0] == 'url' and s[1].strip():
                if not other or other[-1]['url'] != s[2][1] or other[-1]['where'] != where:
                    other.append({'text': s[1].strip(), 'url': s[2][1], 'where': where})
                else: other[-1]['text'] += s[1]
        for a, b, code, titled in find_refs(text, own):
            cover = [s for (x, y, s) in pos if x < b and y > a]
            if any(s[3] for s in cover): continue
            links = {s[2] for s in cover if s[2]}
            url = next((l[1] for l in links if l[0] == 'url'), None)
            hub = HUBURL.get(code)
            if url: status = 'linked' if hub and norm(url) == norm(hub) else 'other-link'
            elif not hub: status = 'not-published'
            else: status = 'missing'
            refs.append({'ref': text[a:b], 'code': code, 'title': HUBTITLE.get(code, TITLES[code][0]), 'titled': titled,
                         'where': where, 'status': status, 'url': url, 'hubUrl': hub, '_p': p, '_span': (a, b)})
    other = [o for o in other if not any(o['url'] == r['url'] for r in refs if r['url'])]
    return doc, z, relx, refs, other, counts, own

def summary(path, version=None):
    doc, z, relx, refs, other, counts, own = scan(path)
    items = [{k: v for k, v in r.items() if not k.startswith('_')} for r in refs]
    for i, r in enumerate(items, 1): r['n'] = i
    return {'scannedAt': datetime.datetime.now(datetime.timezone.utc).strftime('%Y-%m-%dT%H:%M:%SZ'),
            'file': os.path.basename(path), 'version': version, 'total': counts['all'], 'contents': counts['contents'],
            'internal': counts['internal'], 'external': counts['external'],
            'pgRefs': len(items), 'pgLinked': sum(r['status'] == 'linked' for r in items),
            'pgMissing': sum(r['status'] != 'linked' for r in items), 'items': items, 'other': other}

def split_run(run, at):
    """Split run so that the first part holds `at` characters of its text. Returns (left, right)."""
    ts = run.findall('w:t', ns)
    if len(ts) != 1 or any(etree.QName(x).localname not in ('rPr', 't') for x in run): return None
    t = ts[0].text or ''
    if at <= 0 or at >= len(t): return None
    right = copy.deepcopy(run); run.addnext(right)
    ts[0].text = t[:at]; right.find('w:t', ns).text = t[at:]
    for x in (ts[0], right.find('w:t', ns)): x.set('{http://www.w3.org/XML/1998/namespace}space', 'preserve')
    return run, right

def fix(path, out=None):
    doc, z, relx, refs, other, counts, own = scan(path)
    todo = [r for r in refs if r['status'] == 'missing' and r['titled']]
    rid_for = {}
    done = 0
    for r in todo:
        p = r['_p']; a, b = r['_span']
        segs = segments(p, {})
        o = 0; runs = []
        for run, t, link, act in segs:
            runs.append((o, o + len(t), run, link)); o += len(t)
        if any(l for (x, y, run, l) in runs if x < b and y > a): continue
        # split at a and b
        for cut in (a, b):
            for (x, y, run, l) in runs:
                if x < cut < y:
                    if split_run(run, cut - x) is None: break
            segs = segments(p, {}); o = 0; runs = []
            for run, t, link, act in segs: runs.append((o, o + len(t), run, link)); o += len(t)
        cover = [run for (x, y, run, l) in runs if x >= a and y <= b and y > x]
        if not cover or ''.join(ptext(c) for c in cover) != r['ref'] or any(c.getparent() is not p for c in cover): continue
        code = r['code']
        if code not in rid_for:
            rid = 'rIdHub%s' % code
            if not any(x.get('Id') == rid for x in relx):
                e = etree.SubElement(relx, '{%s}Relationship' % PR); e.set('Id', rid); e.set('Type', HL_TYPE); e.set('Target', r['hubUrl']); e.set('TargetMode', 'External')
            rid_for[code] = rid
        h = etree.Element(q('hyperlink')); h.set('{%s}id' % R, rid_for[code]); h.set(q('history'), '1')
        cover[0].addprevious(h)
        for c in cover:
            rp = c.find('w:rPr', ns)
            if rp is None: rp = etree.Element(q('rPr')); c.insert(0, rp)
            for x in rp.findall('w:rStyle', ns): rp.remove(x)
            st = etree.Element(q('rStyle')); st.set(q('val'), 'Hyperlink'); rp.insert(0, st)
            h.append(c)
        done += 1
    data = {'word/document.xml': etree.tostring(doc, xml_declaration=True, encoding='UTF-8', standalone=True),
            'word/_rels/document.xml.rels': etree.tostring(relx, xml_declaration=True, encoding='UTF-8', standalone=True)}
    out = out or path; tmp = out + '.tmp'
    zo = zipfile.ZipFile(tmp, 'w', zipfile.ZIP_DEFLATED)
    for i in z.infolist(): zo.writestr(i, data.get(i.filename) or z.read(i.filename))
    zo.close(); z.close(); os.replace(tmp, out)
    return done, [r for r in refs if r['status'] == 'missing' and not r['titled']]

if __name__ == '__main__':
    ap = argparse.ArgumentParser(description='Hyperlinks and references to other PGs in a Word guide (D-096).')
    ap.add_argument('docx'); ap.add_argument('--json', action='store_true'); ap.add_argument('--fix', action='store_true')
    ap.add_argument('--version')
    a = ap.parse_args()
    if a.fix:
        n, untitled = fix(a.docx)
        print('links added:', n)
        for r in untitled: print('  needs the guide title before it can be linked:', repr(r['ref']), '@', r['where'])
    s = summary(a.docx, a.version)
    if a.json: print(json.dumps(s, indent=1, ensure_ascii=False))
    else:
        print('%s: %d hyperlinks (Contents %d, within the guide %d, external %d); %d references to other PGs, %d linked, %d to fix'
              % (s['file'], s['total'], s['contents'], s['internal'], s['external'], s['pgRefs'], s['pgLinked'], s['pgMissing']))
        for r in s['items']: print('  %-12s %-45s %s' % (r['status'], r['ref'][:45], r['where']))
        for o in s['other']: print('  external     %-45s %s' % (o['text'][:45], o['where']))
