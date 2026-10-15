"""Concise static-delivery, navigation, translation and SEO checks."""
from pathlib import Path
from html.parser import HTMLParser
import json,re
R=Path(__file__).resolve().parents[1]
class Page(HTMLParser):
    def __init__(self):super().__init__();self.tags=[]
    def handle_starttag(self,tag,attrs):self.tags.append((tag,dict(attrs)))
s=(R/'index.html').read_text();p=Page();p.feed(s)
assert '<html lang="en">'in s
assets=[];ids={a['id']for _,a in p.tags if 'id'in a};i18n=[];cards=[]
for tag,a in p.tags:
    if 'data-i18n'in a:i18n.append(a['data-i18n'])
    if tag=='a'and'campus-card'in a.get('class',''):cards.append(a)
    for key in ['src','href']:
        v=a.get(key,'')
        if v.startswith('#'):assert v[1:]in ids,v
        elif v and not re.match(r'^[a-z]+:',v):assert(R/v).is_file(),v;assets.append(v)
    if a.get('target')=='_blank':assert'noopener'in a.get('rel','')
    if tag=='img':assert'alt'in a and 'width'in a and 'height'in a
expected={f'https://{k}.arch.songming.org/'for k in ['uchi','umich','uw','ucsb']}
assert len(cards)==4 and {a['href']for a in cards}==expected
D=json.loads(re.search(r'<script type="application/json" id="site-data">(.*?)</script>',s,re.S)[1])
for lang in ['en','zh']:assert all(k in D['translations'][lang]for k in i18n)
for c in D['campuses']:
    assert c['url']in expected
    assert(R/f'assets/images/{c["id"]}.webp').is_file()
    assert all(c['id']+'.'+k in D['translations']['zh']for k in ['name','campus','location','description'])
assert D['translations']['zh']['umich.name']=='密西根大学'
assert D['translations']['zh']['ucsb.name']=='加州大学圣巴巴拉分校'
js=(R/'assets/site.js').read_text();assert not re.search(r'\b(fetch|XMLHttpRequest|import|navigator|setInterval)\b',js)
assert '<script type="module"'not in s
for url in re.findall(r'url\(([^)]+)\)',(R/'assets/site.css').read_text()):assert url.startswith('data:font/') or (R/'assets'/url.strip('"\'')).is_file(),url
assert(R/'CNAME').read_text().strip()=='arch.songming.org'
assert any(t=='link'and a.get('rel')=='canonical'and a.get('href')=='https://arch.songming.org/'for t,a in p.tags)
schema=json.loads(re.search(r'<script type="application/ld\+json" id="schema">(.*?)</script>',s,re.S)[1]);collection=schema['@graph'][1]
assert collection['mainEntity']['numberOfItems']==4
assert {x['url']for x in collection['mainEntity']['itemListElement']}==expected
assert 'https://arch.songming.org/'in(R/'sitemap.xml').read_text()
assert 'Sitemap: https://arch.songming.org/sitemap.xml'in(R/'robots.txt').read_text()
v=(R/'VERSION').read_text().strip();assert re.fullmatch(r'\d{2}\.\d{1,2}\.\d{1,2}\.\d+',v);assert'## '+v+' 'in(R/'CHANGELOG.md').read_text()
print('Passed: 4 campus destinations; local HTML/CSS/JS/image/font paths; both translations; no runtime network/module dependency; canonical/schema/sitemap/domain; release files.')
