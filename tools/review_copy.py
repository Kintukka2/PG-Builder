"""Build a review copy: comments removed; each [Qnn] comment becomes an ACTION tag ' [Qnn]' where it ended."""
import sys,shutil,re,zipfile,html,os
sys.path.insert(0,os.path.dirname(__file__))
from docx_edit import edit_docx
def build(src,dst):
    shutil.copy(src,dst)
    z=zipfile.ZipFile(dst); d=z.read('word/document.xml').decode('utf8'); c=z.read('word/comments.xml').decode('utf8'); z.close()
    tags={}
    for m in re.finditer(r'<w:comment w:id="(\d+)"[^>]*>(.*?)</w:comment>',c,re.S):
        t=html.unescape(re.sub(r'<[^>]+>','',m.group(2))).strip(); mm=re.match(r'\[(Q\d\d)\]',t)
        if mm: tags[m.group(1)]=mm.group(1)
    run=lambda q:'<w:r><w:rPr><w:rStyle w:val="ACTIONREVIEWREQUIREMENTChar"/></w:rPr><w:t xml:space="preserve"> [%s]</w:t></w:r>'%q
    done=set(); placed=0
    for cid,q in tags.items():
        mark='<w:commentRangeEnd w:id="%s"/>'%cid; i=d.find(mark); assert i!=-1,cid
        ps=max(d.rfind('<w:p>',0,i),d.rfind('<w:p ',0,i)); pe=d.rfind('</w:p>',0,i)
        if ps>pe:   # inside a paragraph
            pend=d.find('</w:p>',i); para=d[ps:pend]
            stm=re.search(r'<w:pStyle w:val="([^"]+)"',para)
            if stm and (stm.group(1).startswith('Heading') or stm.group(1)=='PGFurtherSubdivision'):
                # never inside a heading (it would reach the Contents): end of the next body paragraph instead
                k=pend
                while True:
                    m=re.compile(r'<w:p[ >](?:(?!</w:p>).)*?</w:p>',re.S).search(d,k)
                    if not m: break
                    sm=re.search(r'<w:pStyle w:val="([^"]+)"',m.group(0)); txt=''.join(re.findall(r'<w:t[^>]*>([^<]*)</w:t>',m.group(0))).strip()
                    if txt and not (sm and (sm.group(1).startswith('Heading') or sm.group(1)=='PGFurtherSubdivision')): break
                    k=m.end()
                key=(m.start(),q)
                if key in done: continue
                e=m.end()-len('</w:p>'); d=d[:e]+run(q)+d[e:]; done.add(key); placed+=1; continue
            key=(ps,q)
            if key in done: continue
            d=d[:i+len(mark)]+run(q)+d[i+len(mark):]; done.add(key); placed+=1
        else:       # range ends between paragraphs: tag the end of the previous paragraph
            key=(pe,q)
            if key in done: continue
            d=d[:pe]+run(q)+d[pe:]; done.add(key); placed+=1
    tmp=dst+'.tmp'; zi=zipfile.ZipFile(dst); zo=zipfile.ZipFile(tmp,'w',zipfile.ZIP_DEFLATED)
    for it in zi.infolist(): zo.writestr(it,d.encode('utf8') if it.filename=='word/document.xml' else zi.read(it.filename))
    zo.close(); zi.close(); os.replace(tmp,dst)
    ids=re.findall(r'<w:comment w:id="(\d+)"',c); left=edit_docx(dst,drop=ids)
    return placed,left
if __name__=='__main__':
    print(build(sys.argv[1],sys.argv[2]))
