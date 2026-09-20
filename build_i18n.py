#!/usr/bin/env python3
# build_i18n.py — generoi /es/ ja /fi/ -hakemistot juuren EN-sivuista (D2)
# + hreflang-tagit kaikkiin + lokalisoidut title/meta + privacy ES/FI + sitemap + robots (D4/D5)
# Aja: python3 build_i18n.py [--publish]   (--publish poistaa demo-bannerit myös juuresta)
import os, re, json, subprocess, sys, html as htmllib

BASE = "https://www.sansox.fi"   # [TARKISTETTAVA] — vaihda jos hosting-päätös tuo toisen domainin
R = os.path.dirname(os.path.abspath(__file__))
PUBLISH = "--publish" in sys.argv

PAGES = ["index.html","solutions.html","products.html","references.html","technology.html",
         "company.html","case-kuopio.html","case-philippines.html","case-carelian.html","case-india.html"]

META = {  # sivu → (es_title, es_desc, fi_title, fi_desc)
 "index.html":("SansOx — tecnología finlandesa de tratamiento de agua",
   "OxTube disuelve gas en el agua en menos de un segundo. 90 % de fármacos eliminados, medido y publicado.",
   "SansOx — suomalaista vedenkäsittelyteknologiaa",
   "OxTube liuottaa kaasun veteen alle sekunnissa. 90 % lääkejäämistä poistettu — mitattu ja julkaistu."),
 "solutions.html":("Soluciones | SansOx","Aguas naturales, agua potable, agua residual — un tubo, tres segmentos.",
   "Ratkaisut | SansOx","Luonnonvedet, juomavesi, jätevesi — yksi putki, kolme segmenttiä."),
 "products.html":("Productos — la familia OxTube | SansOx","OxTube, RadOx, IroX, UGOx, GasRemox y Lady Bug. Un principio, nueve productos.",
   "Tuotteet — OxTube-perhe | SansOx","OxTube, RadOx, IroX, UGOx, GasRemox ja Lady Bug. Yksi periaate, yhdeksän tuotetta."),
 "references.html":("Referencias | SansOx","Cuatro referencias medidas y trece crónicas desde el terreno.",
   "Referenssit | SansOx","Neljä mitattua referenssiä ja kolmetoista raporttia kentältä."),
 "technology.html":("Tecnología | SansOx","Cuatro etapas dentro de un tubo sellado, en menos de un segundo.",
   "Teknologia | SansOx","Neljä vaihetta suljetussa putkessa, alle sekunnissa."),
 "company.html":("Empresa | SansOx","Tres ingenieros en Lahti, Finlandia. Publicado en IWA, premiado por Water Europe.",
   "Yritys | SansOx","Kolme insinööriä Lahdessa. IWA-julkaisu, Water Europe -palkinto."),
 "case-kuopio.html":("Caso Kuopio — 90 % de fármacos eliminados en 0,7 s | SansOx","El ensayo publicado por IWA, sustancia por sustancia.",
   "Case Kuopio — 90 % lääkejäämistä 0,7 sekunnissa | SansOx","IWA:n julkaisema koe, aine aineelta."),
 "case-philippines.html":("Caso Filipinas — radón bajo 11 Bq/l | SansOx","Seis estaciones de bombeo bajo uno de los límites más estrictos del mundo.",
   "Case Filippiinit — radon alle 11 Bq/l | SansOx","Kuusi pumppaamoa maailman tiukimpiin kuuluvan rajan alla."),
 "case-carelian.html":("Caso Carelian Caviar — ozono en acuicultura | SansOx","Disolución completa de ozono en 3 segundos en una granja de esturiones.",
   "Case Carelian Caviar — otsoni vesiviljelyssä | SansOx","Otsonin täysi liukeneminen 3 sekunnissa sampilaitoksessa."),
 "case-india.html":("Caso Sukhrali — recuperación de un estanque | SansOx","Un estanque muerto revivido en Gurugram, India — y mantenido limpio.",
   "Case Sukhrali — lammen elvytys | SansOx","Kuollut lampi elvytetty Gurugramissa — ja pidetty puhtaana."),
}

PRIVACY = {
 "es":("Privacidad | SansOx","Este sitio no instala cookies ni ejecuta análisis o rastreo. Los únicos datos personales que recibimos son los que usted decide enviarnos por correo (info@sansox.fi), y se usan solo para responderle. Responsable: SansOx Oy, VAT FI24678326, Niemenkatu 73, FI-15140 Lahti, Finlandia.","Privacidad"),
 "fi":("Tietosuoja | SansOx","Tämä sivusto ei aseta evästeitä eikä käytä analytiikkaa tai seurantaa. Ainoat henkilötiedot ovat ne, jotka itse lähetät sähköpostitse (info@sansox.fi), ja niitä käytetään vain vastaamiseen. Rekisterinpitäjä: SansOx Oy, Y/VAT FI24678326, Niemenkatu 73, 15140 Lahti.","Tietosuoja"),
}

def extract_dict(h):
    i = h.find('const T=')
    if i < 0: return None
    j = h.find('{', i); depth=0; instr=None; esc=False
    for k in range(j, len(h)):
        c = h[k]
        if esc: esc=False; continue
        if c == '\\': esc=True; continue
        if instr:
            if c == instr: instr=None
            continue
        if c in '"\'': instr=c; continue
        if c == '{': depth+=1
        elif c == '}':
            depth-=1
            if depth==0: break
    js = h[j:k+1]
    out = subprocess.run(["node","-e","process.stdout.write(JSON.stringify(eval('('+require('fs').readFileSync(0,'utf8')+')')))"],
                         input=js, capture_output=True, text=True)
    if out.returncode != 0: raise RuntimeError(out.stderr[:300])
    return json.loads(out.stdout)

def hreflang(page):
    p = "" if page=="index.html" else page
    return (f'<link rel="alternate" hreflang="en" href="{BASE}/{p}">\n'
            f'<link rel="alternate" hreflang="es" href="{BASE}/es/{p}">\n'
            f'<link rel="alternate" hreflang="fi" href="{BASE}/fi/{p}">\n'
            f'<link rel="alternate" hreflang="x-default" href="{BASE}/{p}">\n')

def lang_links(page, cur):
    p = page
    up = "../" if cur!="en" else ""
    def cls(l): return ' class="on"' if l==cur else ""
    en = f'{up}{p}' if cur!="en" else p
    return ('<div class="lang">'
            f'<a{cls("en")} href="{up if cur!="en" else ""}{p}" style="padding:8px 10px;text-decoration:none;color:{"#04121c" if cur=="en" else "var(--dim)"};font:700 12px/1 -apple-system,sans-serif;{"background:var(--aqua)" if cur=="en" else ""}">EN</a>'
            f'<a{cls("es")} href="{up}es/{p}" style="padding:8px 10px;text-decoration:none;color:{"#04121c" if cur=="es" else "var(--dim)"};font:700 12px/1 -apple-system,sans-serif;{"background:var(--aqua)" if cur=="es" else ""}">ES</a>'
            f'<a{cls("fi")} href="{up}fi/{p}" style="padding:8px 10px;text-decoration:none;color:{"#04121c" if cur=="fi" else "var(--dim)"};font:700 12px/1 -apple-system,sans-serif;{"background:var(--aqua)" if cur=="fi" else ""}">FI</a></div>')

def bake(h, d, lang, page):
    # data-i18n → tekstisisältö; data-i18n-html → HTML-sisältö
    for key,val in d.get(lang,{}).items():
        h = re.sub(r'(<([a-z0-9]+)[^>]*data-i18n="'+re.escape(key)+r'"[^>]*>)[^<]*',
                   lambda m: m.group(1)+htmllib.escape(val,quote=False).replace("&amp;","&"), h)
        h = re.sub(r'(<([a-z0-9]+)[^>]*data-i18n-html="'+re.escape(key)+r'"[^>]*>).*?(</\2>)',
                   lambda m: m.group(1)+val+m.group(3), h, flags=re.S)
    # kielivalitsin linkeiksi
    h = re.sub(r'<div class="lang"[^>]*>.*?</div>', lang_links(page,lang), h, count=1, flags=re.S)
    # i18n-skriptit pois (T-dict, harvest, setLang, localStorage-init)
    h = re.sub(r'<script>(?:(?!</script>).)*?(?:const T=|setLang|sansox_lang)(?:(?!</script>).)*?</script>\n?','',h,flags=re.S)
    # lang-attribuutti + polkukorjaukset
    h = h.replace('<html lang="en">', f'<html lang="{lang}">',1)
    h = re.sub(r'(href|src|srcset)="(assets/|case-|index\.html|solutions\.html|products\.html|references\.html|technology\.html|company\.html|privacy\.html)',
               lambda m: f'{m.group(1)}="../{m.group(2)}' if m.group(2).startswith('assets/') else f'{m.group(1)}="{m.group(2)}', h)
    h = h.replace('url(assets/img/','url(../assets/img/').replace('image-set(url(assets/','image-set(url(../assets/')
    h = re.sub(r'(<source srcset=")assets/', r'\1../assets/', h)
    h = re.sub(r'((?:href|src)=")assets/', r'\1../assets/', h)
    # title + meta
    if page in META:
        est,esd,fit,fid = META[page]
        t,dsc = (est,esd) if lang=="es" else (fit,fid)
        h = re.sub(r'<title>[^<]*</title>', f'<title>{t}</title>', h)
        h = re.sub(r'(<meta name="description" content=")[^"]*', lambda m: m.group(1)+dsc, h)
        h = re.sub(r'(<meta property="og:title" content=")[^"]*', lambda m: m.group(1)+t, h)
        h = re.sub(r'(<meta property="og:description" content=")[^"]*', lambda m: m.group(1)+dsc, h)
    return h

def strip_banner(h):
    return re.sub(r'<div class="draft">[^<]*</div>\n?','',h)

os.makedirs(R+"/es",exist_ok=True); os.makedirs(R+"/fi",exist_ok=True)
for page in PAGES:
    src = open(R+"/"+page).read()
    d = extract_dict(src)
    if d is None:
        print("!! ei sanakirjaa:",page); continue
    for lang in ("es","fi"):
        out = bake(src, d, lang, page)
        out = hreflangize = out.replace('<meta name="viewport"', hreflang(page)+'<meta name="viewport"',1)
        if PUBLISH: out = strip_banner(out)
        open(R+f"/{lang}/{page}","w").write(out)
    # juurisivu: hreflang + kielivalitsin linkeiksi + localStorage-init pois
    root = src.replace('<meta name="viewport"', hreflang(page)+'<meta name="viewport"',1)
    root = re.sub(r'<div class="lang"[^>]*>.*?</div>', lang_links(page,"en"), root, count=1, flags=re.S)
    root = re.sub(r"\ndocument\.addEventListener\('DOMContentLoaded',function\(\)\{var sl=null;.*?\}\);",'',root,flags=re.S)
    if PUBLISH: root = strip_banner(root)
    open(R+"/"+page,"w").write(root)
    print("ok",page)

# privacy ES/FI
psrc = open(R+"/privacy.html").read()
for lang,(t,lede,h1) in PRIVACY.items():
    p = psrc.replace('<html lang="en">',f'<html lang="{lang}">')
    p = re.sub(r'<title>[^<]*</title>',f'<title>{t}</title>',p)
    p = re.sub(r'<h1>[^<]*</h1>',f'<h1>{h1}</h1>',p)
    p = re.sub(r'(<p class="lede">).*?(</p>)',lambda m: m.group(1)+lede+m.group(2),p,flags=re.S)
    p = re.sub(r'((?:href|src)=")assets/', r'\1../assets/', p)
    p = re.sub(r'((?:href)=")(index|solutions|products|references|technology|company|privacy)', r'\1../\2', p)
    p = p.replace('<meta name="description"', hreflang("privacy.html")+'<meta name="description"',1)
    if PUBLISH: p = strip_banner(p)
    open(R+f"/{lang}/privacy.html","w").write(p)
proot = psrc.replace('<meta name="description"', hreflang("privacy.html")+'<meta name="description"',1)
if PUBLISH: proot = strip_banner(proot)
open(R+"/privacy.html","w").write(proot)

# sitemap + robots
urls=[]
for page in PAGES+["privacy.html"]:
    p = "" if page=="index.html" else page
    for pre in ("","es/","fi/"):
        urls.append(f"  <url><loc>{BASE}/{pre}{p}</loc></url>")
open(R+"/sitemap.xml","w").write('<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n'+"\n".join(urls)+"\n</urlset>\n")
open(R+"/robots.txt","w").write(f"User-agent: *\nAllow: /\nSitemap: {BASE}/sitemap.xml\n")
print("valmis — es/ fi/ sitemap.xml robots.txt")
