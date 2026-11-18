import sys,zipfile,re,subprocess,os,shutil,tempfile
from lxml import etree
W='http://schemas.openxmlformats.org/wordprocessingml/2006/main'
q=lambda t:'{%s}%s'%(W,t)
norm=lambda s:re.sub(r'\s+',' ',s.replace('’',"'").replace('–','-')).strip().lower()
def ptext(p): return ''.join(t.text or '' for t in p.iter(q('t'))).strip()
def style(p):
    ps=p.find(q('pPr')); s=ps.find(q('pStyle')) if ps is not None else None
    return s.get(q('val')) if s is not None else ''
def render(docx,work):
    os.makedirs(work,exist_ok=True); dst=os.path.join(work,'g.docx'); shutil.copy(docx,dst)
    subprocess.run(['soffice','--headless','--convert-to','pdf','--outdir',work,dst],capture_output=True,timeout=400)
    t=subprocess.run(['pdftotext',os.path.join(work,'g.pdf'),'-'],capture_output=True,text=True).stdout
    return [norm(p) for p in t.split('\f')]
def structure(docx):
    root=etree.fromstring(zipfile.ZipFile(docx).read('word/document.xml')); body=root.find(q('body'))
    toc=[]
    for p in body.iter(q('p')):
        s=style(p)
        m=re.match(r'TOC(\d)',s)
        if m:
            t=ptext(p); mm=re.match(r'^(.*?)(\d+)$',t)
            if mm: toc.append((int(m.group(1)),mm.group(1).strip(),int(mm.group(2))))
    # section labels as used by locate.py, with their steps
    st={'part':0,'t':0,'s':0,'k':0,'sec':'','h5':''}; secs={}; kc=[]
    def lab():
        if st['part']==1: return 'Part 1, '+st['sec']
        if st['part']==3: return 'Part 3'
        if st['part']==2: return str(st['t'])+('.'+str(st['s']) if st['s'] else '')+('.'+str(st['k']) if st['k'] else '')
        return st['sec']
    for el in body:
        if el.tag==q('p'):
            s=style(el); t=ptext(el)
            if not t: continue
            if s=='Heading2': st.update(part=1 if t.startswith('Part 1') else 2 if t.startswith('Part 2') else 3 if t.startswith('Part 3') else 9,sec=t,h5='')
            elif s=='Heading3' and st['part']==2: st.update(t=st['t']+1,s=0,k=0)
            elif s=='Heading4' and st['part']==2: st.update(s=st['s']+1,k=0)
            elif s=='Heading4' and st['part']==1: st.update(sec=t)
            elif s=='PGFurtherSubdivision' and st['part']==2: st.update(k=st['k']+1)
            elif s=='Heading5':
                if st['part']==1 and st['sec']=='Key concepts':
                    nxt=el.getnext()
                    while nxt is not None and not ''.join(x.text or '' for x in nxt.iter(q('t'))).strip(): nxt=nxt.getnext()
                    nt=' '.join(ptext(pp) for pp in (nxt.iter(q('p')) if nxt.tag==q('tbl') else [nxt]) if ptext(pp)) if nxt is not None else ''
                    kc.append((t,nt))
            secs.setdefault(lab(),{'title':t if s.startswith('Heading') or s=='PGFurtherSubdivision' else '','tables':[]})
        elif el.tag==q('tbl'):
            rows=el.findall(q('tr')); first=[ptext(tc) for tc in rows[0].findall(q('tc'))] if rows else []
            if first[:2]!=['Action','Description']: continue
            steps=[]; n=0
            for r in rows[1:]:
                cells=r.findall(q('tc')); c0=ptext(cells[0]) if cells else ''
                if c0.startswith(('PROCESS START','STEP COMPLETE','PROCESS COMPLETE')): continue
                n+=1; steps.append((n,c0))
            secs.setdefault(lab(),{'title':'','tables':[]})['tables'].append(steps)
    return toc,secs,kc
def toc_label(title):
    m=re.match(r'^(\d+(?:\.\d+)*)\.?\s',title)
    if m: return m.group(1)
    if title.startswith('Part 1'): return 'Part 1'
    if title.startswith('Part 2'): return 'Part 2'
    if title.startswith('Part 3'): return 'Part 3'
    if title.startswith('About'): return 'About'
    if title.startswith('Additional'): return 'Additional'
    return 'Part 1, '+title
def ranges(toc,pages):
    out={}
    labs=[(lv,toc_label(t),t,pg) for lv,t,pg in toc]
    def depth(l):
        if re.match(r'^\d',l): return l.count('.')+3
        return 2 if not l.startswith('Part 1, ') else 4
    for i,(lv,l,t,pg) in enumerate(labs):
        d=depth(l); end=len(pages)
        for lv2,l2,t2,pg2 in labs[i+1:]:
            if depth(l2)<=d or (l.startswith('Part 1, ') and l2.startswith('Part 1, ')) or not re.match(r'^\d',l2) and re.match(r'^\d',l):
                # next section at the same or a higher level
                txt=pages[pg2-1] if pg2-1<len(pages) else ''
                title2=norm(re.sub(r'^\d+(?:\.\d+)*\.?\s','',t2))
                at_top=txt.find(title2)!=-1 and txt.find(title2)<250
                end=max(pg, pg2-1 if at_top else pg2); break
        out[l]=(pg,end)
    return out
def find_page(text,pages,lo,hi):
    key=norm(text)[:40]
    for i in range(lo,hi+1):
        if i-1<len(pages) and key and key in pages[i-1]: return i
    key=norm(text)[:20]
    for i in range(lo,hi+1):
        if i-1<len(pages) and key and key in pages[i-1]: return i
    return None
def pages_for(ref,ctx):
    toc,secs,kc,pages,rng=ctx; out=set()
    for seg in [s.strip() for s in ref.split(';') if s.strip()]:
        if seg.startswith('Cover'): out.add(1); continue
        m=re.match(r'^Part 1, Key concepts \((.*)\)$',seg)
        if m:
            lo,hi=rng.get('Part 1, Key concepts',(1,len(pages))); name=m.group(1)
            nt=next((n for t,n in kc if t==name),'')
            key=norm(name+' '+nt)[:45]; pg=None
            for i in range(lo,hi+1):
                if key in pages[i-1]: pg=i; break
            if pg is None:
                for i in range(lo,hi+1):
                    if norm(nt)[:30] and norm(nt)[:30] in pages[i-1]: pg=i; break
            out.add(pg or lo); continue
        if seg.startswith('Part 1, '):
            name=seg.split(' (')[0]; lo,hi=rng.get(name,(1,1)); out.update(range(lo,hi+1)); continue
        if seg.startswith('Part 3'):
            lo,hi=rng.get('Part 3',(len(pages),len(pages))); out.update(range(lo,hi+1)); continue
        m=re.match(r'^(?:Topic )?(\d+(?:\.\d+)*) to (\d+(?:\.\d+)*)$',seg)
        if m:
            a=rng.get(m.group(1)); b=rng.get(m.group(2))
            if a and b: out.update(range(a[0],b[1]+1)); continue
        m=re.match(r'^(?:Topic )?(\d+(?:\.\d+)*)(?:,)?\s*(.*)$',seg)
        if not m: continue
        sec,rest=m.group(1),m.group(2).strip()
        lo,hi=rng.get(sec,(None,None))
        if lo is None: continue
        if not rest: out.update(range(lo,hi+1)); continue
        rest=rest.lstrip(', ')
        # named sub-procedure, e.g. "Remove a Page from Favorites"
        if not re.search(r'step|description|responsibility|initiation|pre-requisites|outcome|topic overview',rest):
            pg=find_page(rest,pages,lo,hi); out.add(pg or lo); continue
        steps=[int(x) for x in re.findall(r'\d+',re.search(r'steps? ([\d, ]+)',rest).group(1))] if re.search(r'steps? [\d]',rest) else []
        tbls=secs.get(sec,{}).get('tables',[])
        for n in steps:
            txt=next((t for tb in tbls for k,t in tb if k==n),None)
            pg=find_page(txt,pages,lo,hi) if txt else None; out.add(pg or lo)
        if re.search(r'description|responsibility|initiation|topic overview',rest): out.add(lo)
        if 'pre-requisites' in rest:
            pg=find_page('PROCESS START',pages,lo,hi); out.add(pg or lo)
        if 'outcome' in rest:
            pg=None
            for i in range(hi,lo-1,-1):
                if 'complete' in pages[i-1]: pg=i; break
            out.add(pg or hi)
    return out
def fmt(ps):
    ps=sorted(p for p in ps if p); out=[]; i=0
    while i<len(ps):
        j=i
        while j+1<len(ps) and ps[j+1]==ps[j]+1: j+=1
        out.append(str(ps[i]) if i==j else f'{ps[i]}-{ps[j]}'); i=j+1
    return 'p. '+', '.join(out) if out else ''
def context(docx,work):
    pages=render(docx,work); toc,secs,kc=structure(docx); rng=ranges(toc,pages)
    return (toc,secs,kc,pages,rng)
