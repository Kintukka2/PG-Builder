import sys,zipfile,re,json
from lxml import etree
W='http://schemas.openxmlformats.org/wordprocessingml/2006/main'
q=lambda t:'{%s}%s'%(W,t)
def ptext(p): return ''.join(p.itertext()).strip()
def style(p):
    ps=p.find(q('pPr')); s=ps.find(q('pStyle')) if ps is not None else None
    return s.get(q('val')) if s is not None else ''
def locate(docx):
    z=zipfile.ZipFile(docx); root=etree.fromstring(z.read('word/document.xml')); body=root.find(q('body'))
    cm={}
    for e in etree.fromstring(z.read('word/comments.xml')).iter(q('comment')):
        t=''.join(e.itertext()).strip(); head=re.sub(r'\s*\(.*?\)','',t.split(':',1)[0]).strip(); cm[e.get(q('id'))]=head
    st={'part':0,'t':0,'s':0,'k':0,'sec':'Cover and version history','h5':'','label':''}
    out={}
    def lab():
        if st['part']==1: return 'Part 1, '+st['sec']+(' ('+st['h5']+')' if st['h5'] and st['sec']=='Key concepts' else '')
        if st['part']==3: return 'Part 3'+(' ('+st['h5']+')' if st['h5'] else '')
        if st['part']==2:
            n=str(st['t'])+('.'+str(st['s']) if st['s'] else '')+('.'+str(st['k']) if st['k'] else '')
            return n
        return st['sec']
    def record(p,where):
        for e in p.iter(q('commentRangeStart')):
            cid=e.get(q('id'))
            if cid in cm: out.setdefault(cm[cid],[]).append(where)
    def heading(p):
        s=style(p); t=ptext(p)
        if not t: return False
        if s=='Heading2':
            st.update(part=1 if t.startswith('Part 1') else 2 if t.startswith('Part 2') else 3 if t.startswith('Part 3') else 9,sec=t,h5='')
            return True
        if s=='Heading3' and st['part']==2: st.update(t=st['t']+1,s=0,k=0,h5=''); return True
        if s=='Heading4' and st['part']==2: st.update(s=st['s']+1,k=0,h5=''); return True
        if s=='Heading4' and st['part']==1: st.update(sec=t,h5=''); return True
        if s=='PGFurtherSubdivision' and st['part']==2: st.update(k=st['k']+1,h5=''); return True
        if s=='Heading5': st['h5']=t; return True
        return False
    for el in body:
        if el.tag==q('p'):
            if heading(el): record(el,{'sec':lab(),'what':'heading'}); continue
            sec=lab()
            what=st['h5'] if st['part']==2 and st['h5'] in ('Description','Responsibility','Initiation','Topic Overview') else ''
            record(el,{'sec':sec,'what':what})
        elif el.tag==q('tbl'):
            rows=el.findall(q('tr'))
            first=[ptext(tc) for tc in rows[0].findall(q('tc'))] if rows else []
            proc=first[:2]==['Action','Description']
            n=0
            for i,r in enumerate(rows):
                cells=r.findall(q('tc')); c0=ptext(cells[0]) if cells else ''
                if proc and i>0:
                    if c0.startswith('PROCESS START'): what='pre-requisites'
                    elif c0.startswith('STEP COMPLETE') or c0.startswith('PROCESS COMPLETE'): what='outcome'
                    else: n+=1; what='step %d'%n
                else:
                    what=st['h5'] if st['part']==2 and st['h5'] in ('Description','Responsibility','Initiation','Topic Overview') else ''
                for p in r.iter(q('p')): record(p,{'sec':lab(),'what':what})
    return out
def fmt(locs):
    # group steps by section
    order=[]; grp={}
    for l in locs:
        s=l['sec']
        if s not in grp: grp[s]=[]; order.append(s)
        if l['what'] and l['what']!='heading' and l['what'] not in grp[s]: grp[s].append(l['what'])
    parts=[]
    for s in order:
        w=grp[s]; steps=[x for x in w if x.startswith('step ')]; other=[x for x in w if not x.startswith('step ')]
        bits=[]
        if steps:
            nums=sorted(int(x.split()[1]) for x in steps)
            bits.append(('step ' if len(nums)==1 else 'steps ')+', '.join(map(str,nums)))
        bits+= [o if o!='pre-requisites' else 'pre-requisites' for o in other]
        bits=[b.lower() if b in ('Description','Responsibility','Initiation','Topic Overview') else b for b in bits]
        parts.append(s+(' '+', '.join(bits) if bits else ''))
    return '; '.join(parts)
if __name__=='__main__':
    loc=locate(sys.argv[1])
    for k,v in sorted(loc.items()): print(f'{k:32} -> {fmt(v)}')
