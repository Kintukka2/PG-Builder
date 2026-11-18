"""Edit a Word guide in place: drop review comments, replace text in document.xml, or reword comments."""
import zipfile,re,os,html
def edit_docx(path,drop=(),doc_replace=(),comment_text=None):
    """drop: comment ids to remove; doc_replace: (old,new,count) on document.xml; comment_text: {cid: new plain text}"""
    z=zipfile.ZipFile(path); d=z.read('word/document.xml').decode('utf8'); c=z.read('word/comments.xml').decode('utf8')
    for cid in drop:
        m=re.findall(r'<w:comment w:id="%s"[ >].*?</w:comment>'%cid,c,re.S); assert len(m)==1,(cid,len(m)); c=c.replace(m[0],'')
        for pat in ['<w:commentRangeStart w:id="%s"/>'%cid,'<w:commentRangeEnd w:id="%s"/>'%cid]:
            assert d.count(pat)==1,(pat,d.count(pat)); d=d.replace(pat,'')
        rr=re.findall(r'<w:r>(?:(?!</w:r>).)*?<w:commentReference w:id="%s"/></w:r>'%cid,d,re.S); assert len(rr)==1,(cid,'ref',len(rr)); d=d.replace(rr[0],'')
    for old,new,count in doc_replace:
        assert d.count(old)==count,(old[:80],d.count(old)); d=d.replace(old,new)
    for cid,txt in (comment_text or {}).items():
        m=re.findall(r'(<w:comment w:id="%s"[ >].*?</w:comment>)'%cid,c,re.S); assert len(m)==1
        body=m[0]; ts=re.findall(r'<w:t(?: [^>]*)?>[^<]*</w:t>',body); assert ts
        nb=body.replace(ts[0],'<w:t xml:space="preserve">'+html.escape(txt,quote=False)+'</w:t>',1)
        for t in ts[1:]: nb=nb.replace(t,'<w:t></w:t>',1)
        c=c.replace(body,nb)
    tmp=path+'.tmp'; zo=zipfile.ZipFile(tmp,'w',zipfile.ZIP_DEFLATED)
    for i in z.infolist():
        data={'word/document.xml':d.encode('utf8'),'word/comments.xml':c.encode('utf8')}.get(i.filename) or z.read(i.filename)
        zo.writestr(i,data)
    zo.close(); z.close(); os.replace(tmp,path)
    return len(re.findall(r'<w:comment ',c))
