# executed from build2.py (shares HEAD, nav, FOOT, CAL)
P="../"
NOTION="https://mehdimouatqdir.notion.site/YouTube-Ecosystem-187c3f47797980c5b700f3e0bcb21c4b?source=copy_link"
LESSONS=[
 dict(t="Thumbnail System",d="40 editable Canva thumbnail templates, plus how to cut out, relight and A/B test them.",v="course_thumbnails",links=[("https://www.canva.com/design/DAGTHPXnmAc/ueqbW5tL3FkT9sL0cObcFg/view?utm_content=DAGTHPXnmAc&utm_campaign=designshare&utm_medium=link&utm_source=publishsharelink&mode=preview","Thumbnail templates"),("https://www.craiyon.com/en/background-remover","Background remover"),("https://clipdrop.co/relight","Relight"),("https://ytvote.com/","A/B testing")]),
 dict(t="Branding Ecosystem",d="A walkthrough of the YouTube Ecosystem in Notion.",drive="1aIn5-pKPEeTaiwHzP2iT89IVUPMclZiu",poster="course_branding.jpg",links=[(NOTION,"The system")]),
 dict(t="Idea Template",d="Video ideas proven to work, sorted into top, middle and bottom of funnel.",v="course_ideas",links=[("https://mehdimouatqdir.notion.site/Video-Ideas-Proven-to-Work-187c3f47797980b5adf9c135a706e750?pvs=74","Ideas template")]),
 dict(t="Ideation System",d="How to come up with ideas and check them before you film.",v="course_ideation",links=[("https://mehdimouatqdir.notion.site/187c3f47797980e4b18efa1380da6ce1?v=187c3f477979804db3fa000cbf73599a","The system")]),
]
N=len(LESSONS)

PLAY_SVG='<svg width="28" height="28" viewBox="0 0 24 24" fill="#fff"><path d="M8 5v14l11-7z"/></svg>'

def player(i, L):
    if L.get("drive"):
        media=('<div class="media dv" style="aspect-ratio:16/9;position:relative;cursor:pointer" data-fid="%s" onclick="playDrive(this)">'
               '<img src="%sassets/%s" alt="" style="width:100%%;height:100%%;object-fit:contain;background:#000">'
               '<div style="position:absolute;inset:0;display:grid;place-items:center"><div class="playbtn">%s</div></div></div>') % (L['drive'], P, L['poster'], PLAY_SVG)
    else:
        media=('<div class="media" style="aspect-ratio:16/9"><video src="%sassets/%s.mp4" poster="%sassets/%s.jpg" controls preload="none" playsinline '
               'style="object-fit:contain" onended="done(%d)"></video></div>') % (P, L['v'], P, L['v'], i)
    ls=''.join('<a class="res" href="%s" target="_blank" rel="noopener">%s ↗</a>' % (h, x) for h, x in L['links'])
    if i+1 < N:
        nxt='<button class="btn sm" onclick="done(%d);show(%d)">Next: %s →</button>' % (i, i+1, LESSONS[i+1]['t'])
    else:
        nxt='<button class="btn sm" onclick="done(%d);show(\'end\')">Finish →</button>' % i
    return ('<section class="lesson" data-i="%d" hidden>%s'
            '<div style="display:flex;flex-wrap:wrap;gap:16px;justify-content:space-between;align-items:center;margin-top:22px">'
            '<div><div class="eyebrow" style="margin-bottom:6px">Lesson %d of %d</div><h2 class="d" style="font-size:clamp(26px,3vw,36px)">%s</h2></div>%s</div>'
            '<p style="color:var(--mu);margin:14px 0 18px">%s</p>'
            '<div><div class="reslbl">Resources</div>%s</div></section>') % (i, media, i+1, N, L['t'], nxt, L['d'], ls)

mods=''.join('<button class="mod" data-i="%d" onclick="show(%d)"><span class="num"><span>%d</span></span><span>%s</span></button>' % (i, i, i+1, L['t']) for i, L in enumerate(LESSONS))

CSS='''.course{display:grid;grid-template-columns:260px 1fr 300px;gap:24px;align-items:start}
.side{position:sticky;top:96px}
.mod{display:flex;align-items:center;gap:12px;width:100%;text-align:left;background:none;border:0;border-left:3px solid transparent;color:var(--tx);font:600 15px Inter,sans-serif;padding:12px;border-radius:12px;cursor:pointer}
.mod:hover{background:var(--s2)}
.mod.on{background:rgba(242,180,23,.1);border-left-color:var(--gold)}
.num{width:30px;height:30px;flex:none;border-radius:50%;display:grid;place-items:center;font-size:13px;font-weight:800;background:var(--s2);border:1px solid var(--line);color:var(--mu)}
.mod.on .num{background:var(--gold);color:#111;border-color:var(--gold)}
.mod.dn .num{background:var(--green);color:#0a0a0a;border-color:var(--green)}
.mod.dn .num span{display:none}.mod.dn .num::after{content:"✓"}
.res{display:inline-flex;align-items:center;gap:6px;margin:0 10px 10px 0;padding:10px 16px;border-radius:999px;border:1px solid var(--line);background:var(--s1);color:var(--tx);text-decoration:none;font-weight:600;font-size:14px}
.res:hover{border-color:var(--gold)}
.reslbl{font-size:12px;font-weight:700;letter-spacing:.14em;text-transform:uppercase;color:var(--dim);margin-bottom:10px}
.playbtn{width:76px;height:76px;border-radius:50%;background:rgba(255,59,48,.92);display:grid;place-items:center;box-shadow:0 8px 30px rgba(0,0,0,.5)}
@media (max-width:1060px){.course{grid-template-columns:1fr}.side,.cta{position:static !important}}
</style>'''

GATE='<script>(function(){var ok=false;try{ok=localStorage.getItem("tos_optin")==="1"}catch(e){}if(!ok&&location.search.indexOf("fit=")<0){location.replace("../#free")}})();</script>'

JS='''<script>
var N=%d;
function get(){try{return JSON.parse(localStorage.getItem('tos_done')||'[]')}catch(e){return[]}}
function done(i){var d=get();if(d.indexOf(i)<0){d.push(i);try{localStorage.setItem('tos_done',JSON.stringify(d))}catch(e){}}paint()}
function paint(){var d=get();document.querySelectorAll('.mod[data-i]').forEach(function(m){m.classList.toggle('dn',d.indexOf(+m.dataset.i)>=0)});var p=Math.round(d.length/N*100);document.getElementById('pct').textContent=p+'%%';document.getElementById('pbar').style.width=p+'%%'}
function show(i,init){document.querySelectorAll('.lesson').forEach(function(s){s.hidden=s.dataset.i!=String(i)});document.querySelectorAll('.mod[data-i]').forEach(function(m){m.classList.toggle('on',m.dataset.i==String(i))});document.querySelectorAll('video').forEach(function(v){v.pause()});try{localStorage.setItem('tos_cur',i)}catch(e){}if(!init&&window.innerWidth<1060)document.querySelector('main').scrollIntoView({behavior:'smooth'})}
function playDrive(el){if(el.dataset.on)return;el.dataset.on=1;el.style.cursor='default';el.innerHTML='<iframe src="https://drive.google.com/file/d/'+el.dataset.fid+'/preview?autoplay=1" allow="autoplay; fullscreen" allowfullscreen style="width:100%%;height:100%%;border:0;display:block"></iframe>';done(1)}
if(location.search.indexOf('fit=1')>=0)document.getElementById('fitbar').hidden=false;
var c='0';try{c=localStorage.getItem('tos_cur')||'0'}catch(e){}show(c==='end'?'end':+c,1);paint();
</script>''' % N

f=HEAD.replace("{title}","The YouTube OS Essentials · The Organic System").replace("{desc}","Free thumbnail templates, video idea templates and the ideation system I use with clients.")
f=f.replace('</style>',CSS,1)
f+=nav()+GATE
f+='''
<header style="background:linear-gradient(180deg,rgba(242,180,23,.07),transparent);padding:64px 0 36px">
<div class="wrap center" style="display:flex;flex-direction:column;align-items:center;gap:14px">
<span class="pill"><span class="dot"></span>Free · YouTube OS Essentials</span>
<h1 class="d" style="font-size:clamp(36px,5vw,64px)">Start here: <span class="hl">package videos that get&nbsp;clicked.</span></h1>
<p class="lead center">The same templates and systems I use with clients. %d short lessons, each with the resource to use today.</p>
</div></header>
<div class="wrap" style="max-width:1240px;padding-bottom:90px">
<div id="fitbar" hidden class="card" style="margin-bottom:24px;padding:18px 22px;display:flex;flex-wrap:wrap;gap:16px;align-items:center;justify-content:space-between;border-color:rgba(242,180,23,.5)"><div><b>From your answers, you look like a fit for the Sprint.</b><div style="color:var(--mu);font-size:15px">A 30-minute call is free, and you leave with a plan either way.</div></div><a class="btn sm" href="%s">Book a call →</a></div>
<div class="course">
<aside class="card side" style="padding:18px">
<div class="eyebrow" style="padding:4px 12px 10px">Modules</div>
%s
<div style="padding:16px 12px 6px"><div style="display:flex;justify-content:space-between;font-size:13px;color:var(--mu);margin-bottom:8px"><span>Your progress</span><span id="pct">0%%</span></div>
<div style="height:8px;border-radius:99px;background:var(--s2);overflow:hidden"><div id="pbar" style="height:100%%;width:0;background:var(--green);transition:width .4s"></div></div></div>
<div style="border-top:1px solid var(--line);margin:14px 0 6px"></div>
<a class="mod" href="%s" target="_blank" rel="noopener" style="text-decoration:none"><span class="num">★</span><span>Full YouTube Ecosystem (Notion)</span></a>
</aside>
<main>
%s
<section class="lesson card" data-i="end" hidden style="padding:clamp(28px,5vw,56px);text-align:center">
<h2 class="d" style="margin:0 0 10px">You finished the <span class="hl">Essentials.</span></h2>
<p class="lead center" style="margin-bottom:24px">Want me to apply all of this to your channel, every week, for 6 weeks?</p>
<a class="btn" href="%s">Book a call →</a></section>
</main>
<aside class="card cta" style="overflow:hidden;position:sticky;top:96px">
<img src="%sassets/riley_chart.jpg" alt="Riley's views after the new title and thumbnail" style="width:100%%;display:block;border-bottom:1px solid var(--line)">
<div style="padding:22px;text-align:center;display:flex;flex-direction:column;gap:10px;align-items:center">
<div class="eyebrow">For founders</div>
<div class="d" style="font-size:24px;line-height:1.15">Want this done for your channel?</div>
<p style="margin:0;color:var(--mu);font-size:15px">Riley changed one title and thumbnail and booked 8 calls. The Founder Channel Sprint does that every week for 6 weeks.</p>
<a class="btn sm" href="%s" style="width:100%%;margin-top:6px">Book a call →</a>
<a class="tlink" href="../#results" style="font-size:14px">See the results</a>
</div></aside>
</div></div>
''' % (N, CAL, mods, NOTION, ''.join(player(i, L) for i, L in enumerate(LESSONS)), CAL, P, CAL)
f+=JS
f+=FOOT
open('free/index.html','w').write(f.replace('@@FREE@@','./').replace('@@HOME@@','../').replace('@@BOOK@@',CAL).replace('@@FREEOPT@@','../#free'))
print('ok')
