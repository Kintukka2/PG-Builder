"""Build a local preview of a command-centre page with a mock tracker.

Usage: python3 make_preview.py <page.html> <tracker-seed.json> <out.html>

The published pages read live data through the claude.ai viewer. This wraps a page in the
same skeleton the viewer uses and injects a small in-memory stand-in for the tracker, so the
page can be opened or screenshotted locally (see screenshot.js).
"""
import json, sys
page = open(sys.argv[1], encoding="utf-8").read()
seed = json.load(open(sys.argv[2], encoding="utf-8"))
fake='''<script>
window.__SEED=%s;
(function(){const store={};for(const c in __SEED){store[c]=Object.assign({},__SEED[c]);}
const subs={};const emit=c=>(subs[c]||[]).forEach(f=>f({docs:Object.entries(store[c]||{}).map(([id,d])=>({id,exists:true,data:()=>d})),metadata:{fromCache:false,hasPendingWrites:false}}));
const db={collection:c=>({onSnapshot:(n)=>{(subs[c]=subs[c]||[]).push(n);setTimeout(()=>emit(c),50);return()=>{}},add:async d=>{store[c]=store[c]||{};store[c]['x'+Math.random()]=d;emit(c)}}),
doc:p=>{const [c,id]=p.split('/');return{get:async()=>({exists:!!(store[c]&&store[c][id]),data:()=>store[c]&&store[c][id]}),set:async d=>{(store[c]=store[c]||{})[id]=d;emit(c)},update:async d=>{Object.assign(store[c][id],d);emit(c)}}}};
window.claude={use:async n=>n==='db'?db:null};})();
</script>'''%json.dumps(seed)
open(sys.argv[3], 'w', encoding='utf-8').write('<!doctype html><html><head><meta charset=utf-8><meta name=viewport content="width=device-width,initial-scale=1,viewport-fit=cover"><style>:root{color-scheme:light}body{margin:0;font:14px system-ui}img{max-width:100%}[hidden]{display:none!important}</style></head><body>'+fake+page+'</body></html>')
