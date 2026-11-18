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
def layout_lines(pdf):
    """Each page as a list of normalized lines (pdftotext -layout), for finding headings that stand on their own line."""
    t=subprocess.run(['pdftotext','-layout',pdf,'-'],capture_output=True,text=True).stdout
    return [[norm(l) for l in p.split('\n') if l.strip()] for p in t.split('\f')]
def structure(docx):
    root=etree.fromstring(zipfile.ZipFile(docx).read('word/document.xml')); body=root.find(q('body'))
    toc=[]
    for p in body.iter(q('p')):
        s=style(p)
        m=re.match(r'TOC(\d)',s)
        if m:
            # the page number is the last run that holds only digits (the PAGEREF result), so a title
            # that ends in a digit, such as "to TM1", is not run into its page number
            ts=[t.text or '' for t in p.iter(q('t'))]
            k=max((i for i,x in enumerate(ts) if x.strip().isdigit()),default=None)
            if k is not None:
                title=''.join(ts[:k]).strip()
                if title: toc.append((int(m.group(1)),title,int(ts[k].strip())))
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
def word_pages(docx):
    """Pages as Word last laid them out, from the page breaks Word records when it saves (w:lastRenderedPageBreak).
    Returns (page texts, [(style, text, page)] for headings), or None when the file was not saved by Word or its
    breaks are stale (they must add up to the page count Word saved in docProps/app.xml)."""
    z=zipfile.ZipFile(docx)
    app=z.read('docProps/app.xml').decode('utf8') if 'docProps/app.xml' in z.namelist() else ''
    if 'Microsoft' not in app: return None
    m=re.search(r'<Pages>(\d+)</Pages>',app); saved=int(m.group(1)) if m else None
    body=etree.fromstring(z.read('word/document.xml')).find(q('body'))
    texts=[[]]; heads=[]; pending=False; seen_text=True; cur_p=None
    for el in body.iter(q('p'),q('lastRenderedPageBreak'),q('br'),q('pageBreakBefore'),q('t')):
        tag=etree.QName(el).localname
        if tag=='p':
            cur_p=el; s=style(el)
            if (s.startswith('Heading') or s=='PGFurtherSubdivision') and ptext(el): heads.append([s,ptext(el),None,el])
        elif tag=='pageBreakBefore' and el.get(q('val')) not in ('0','false'):
            texts.append([]); pending=True; seen_text=False
        elif tag=='br' and el.get(q('type'))=='page':
            texts.append([]); pending=True; seen_text=False
        elif tag=='lastRenderedPageBreak':
            if not (pending and not seen_text): texts.append([])
            pending=False
        elif tag=='t' and el.text:
            texts[-1].append(el.text)
            if el.text.strip(): seen_text=True
            if heads and heads[-1][3] is cur_p and heads[-1][2] is None: heads[-1][2]=len(texts)
    if saved is not None and len(texts)!=saved: return None
    return [norm(' '.join(t)) for t in texts],{id(e):pg for s,t,pg,e in heads},heads
def heading_list(docx):
    """Headings in document order: (style, text, text of the next paragraph)."""
    body=etree.fromstring(zipfile.ZipFile(docx).read('word/document.xml')).find(q('body'))
    ps=[p for p in body.iter(q('p')) if ptext(p)]; out=[]
    for i,p in enumerate(ps):
        s=style(p)
        if (s.startswith('Heading') or s=='PGFurtherSubdivision') and not re.match(r'TOC',s):
            out.append((s,ptext(p),ptext(ps[i+1]) if i+1<len(ps) else ''))
    return out
UNFOUND=[]
def relocate(toc,pages,heads,lines=None):
    """Page of each Contents entry as the pages fall now, not as the Contents last recorded them.
    heads: [(style, text, next text, page or None)] in document order. With a page (Word mode) it is used as is.
    Without one, the heading is found on the first page, from the previous entry's page on, where its title
    stands on a line of its own (lines from pdftotext -layout), with or without its number, or wrapped over
    two lines; a link in the Contents or an overview table shares its line with other text, so it does not count."""
    out=[]; hi=0; lo=1
    for lv,t,pg in toc:
        core=norm(re.sub(r'^\d+(?:\.\d+)*\.?\s+','',t)); full=norm(t); found=None
        for i in range(hi,len(heads)):
            h=norm(heads[i][1])
            if h==core or h==full or h.endswith(core):
                hi=i+1; found=heads[i][3]; break
        if found is None and lines is not None:
            want={core,full}
            for j in range(max(lo,1),len(lines)+1):
                L=lines[j-1]
                if any(L[k] in want or re.sub(r'^\d+(?:\.\d+)*\.?\s+','',L[k]) in want or
                       (k+1<len(L) and (L[k]+' '+L[k+1]) in want) for k in range(len(L))):
                    found=j; break
        if found is None: UNFOUND.append(t)
        pg2=found or max(pg,lo); lo=pg2; out.append((lv,t,pg2))
    return out
def context(docx,work=None,word=False,pdf=None):
    """word=True: use the page breaks of a copy saved in Word (exact). pdf: a PDF the user exported from Word
    (exact). Otherwise render with LibreOffice (an estimate: install DM Sans first with tools/install_fonts.sh)."""
    toc,secs,kc=structure(docx)
    if pdf:
        pages=pdf_pages(pdf); toc=relocate(toc,pages,[h+(None,) for h in heading_list(docx)],layout_lines(pdf))
    elif word:
        wp=word_pages(docx)
        if wp is None: raise SystemExit('Not a fresh Word save: its page breaks do not add up to its page count.')
        pages,_,wh=wp; toc=relocate(toc,pages,[(s_,t_,'',pg_) for s_,t_,pg_,_ in wh])
    else:
        if 'DM Sans' not in subprocess.run(['fc-list'],capture_output=True,text=True).stdout:
            print('warning: DM Sans is not installed (tools/install_fonts.sh); pages will be further off',file=sys.stderr)
        work=work or tempfile.mkdtemp(); pages=render(docx,work)
        toc=relocate(toc,pages,[h+(None,) for h in heading_list(docx)],layout_lines(os.path.join(work,'g.pdf')))
    rng=ranges(toc,pages)
    return (toc,secs,kc,pages,rng)
def write_contents(docx,toc,out=None):
    """Write the page numbers of toc (level, title, page) into the cached results of the guide's Contents."""
    import shutil
    z=zipfile.ZipFile(docx); d=z.read('word/document.xml').decode('utf8')
    want=[pg for _,_,pg in toc]; i=0
    def fix(m):
        nonlocal i
        p=m.group(0)
        if not re.search(r'<w:pStyle w:val="TOC\d"',p): return p
        ts=list(re.finditer(r'(<w:t(?: [^>]*)?>)\s*(\d+)\s*(</w:t>)',p))
        if not ts or not ''.join(re.findall(r'<w:t(?: [^>]*)?>([^<]*)</w:t>',p[:ts[-1].start()])).strip(): return p
        if not ts or i>=len(want): return p
        t=ts[-1]; new=p[:t.start()]+t.group(1)+str(want[i])+t.group(3)+p[t.end():]; i+=1
        return new
    d2=re.sub(r'<w:p[ >](?:(?!</w:p>).)*?</w:p>',fix,d,flags=re.S)
    assert i==len(want),(i,len(want))
    out=out or docx; tmp=out+'.tmp'; zo=zipfile.ZipFile(tmp,'w',zipfile.ZIP_DEFLATED)
    for it in z.infolist(): zo.writestr(it,d2.encode('utf8') if it.filename=='word/document.xml' else z.read(it.filename))
    zo.close(); z.close()
    if [pg for _,_,pg in structure(tmp)[0]]!=want:
        os.remove(tmp); raise SystemExit('Contents not written: the page numbers did not read back as expected.')
    os.replace(tmp,out)
if __name__=='__main__':
    import argparse
    ap=argparse.ArgumentParser(description='Pages for question references in a PG Word guide.')
    ap.add_argument('docx'); ap.add_argument('refs',nargs='*',help='for example "3.6 step 9" or "Part 1, Key concepts (Settlement)"')
    ap.add_argument('--word',action='store_true',help='the file is a fresh Word save: use its own page breaks (exact)')
    ap.add_argument('--pdf',help='a PDF of the same guide exported from Word: take the pages from it (exact)')
    ap.add_argument('--contents',action='store_true',help='print where each Contents entry falls')
    ap.add_argument('--write-contents',action='store_true',help='write those page numbers into the Contents of the file')
    a=ap.parse_args(); ctx=context(a.docx,word=a.word,pdf=a.pdf)
    if a.contents:
        for lv,t,pg in ctx[0]: print(pg,t,'(not found: Contents value kept)' if t in UNFOUND else '')
    if a.write_contents and UNFOUND:
        raise SystemExit('Contents not written: these headings were not found: '+'; '.join(UNFOUND))
    if a.write_contents: write_contents(a.docx,ctx[0]); print('Contents page numbers written')
    for r in a.refs: print(fmt(pages_for(r,ctx)),'<-',r)
