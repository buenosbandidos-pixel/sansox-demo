#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Generoi uutisartikkelien sivut posts/*.json-datasta.

Miksi generaattori eikä 13 kasin kirjoitettua sivua: rakenne on joka sivulla
sama, ja kasin kirjoitettuna 13 sivua ajautuisi erilleen ensimmaisessa
muutoksessa. Sisalto on datassa, rakenne taalla, kerran.

AJOJARJESTYS ON TARKEA:
    1. python3 build_posts.py    (kirjoittaa post-*.html ja posts/_meta.json)
    2. python3 build_i18n.py     (tekee /fi/ ja /es/, hreflangit, sitemapin)
Jalkimmainen muuttaa juuritiedostojen kielivalitsimen napeista linkeiksi.
Jos ajat vain build_posts.py:n, artikkelisivut palaavat JS-valitsimeen ja
niiden hreflangit katoavat — aja silloin myos build_i18n.py.
"""
import json, os, re, html

BASE = "https://www.sansox.fi"
OUT_PREFIX = "post-"

# Kategoria-avaimet vastaavat news.html:n tg_*-avaimia, jotta kaannokset ovat samat.
CATS = {
    "ww": {"en": "Wastewater",    "fi": "Jätevesi",     "es": "Aguas residuales"},
    "nw": {"en": "Natural water", "fi": "Luonnonvedet",      "es": "Aguas naturales"},
    "tx": {"en": "Textile water", "fi": "Tekstiilivesi",     "es": "Agua textil"},
    "ev": {"en": "Events",        "fi": "Tapahtumat",        "es": "Eventos"},
    "pr": {"en": "Press",         "fi": "Lehdistö",     "es": "Prensa"},
    "bs": {"en": "Baltic Sea",    "fi": "Itämeri",      "es": "Mar Báltico"},
}

UI = {
    "en": {"back": "\u2190 News", "orig": "Originally published on sansox.fi",
           "author": "Author", "prev": "Previous", "next": "Next",
           "skip": "Skip to content", "read": "Read more news"},
    "fi": {"back": "\u2190 Uutiset", "orig": "Julkaistu alun perin sansox.fi-sivustolla",
           "author": "Kirjoittaja", "prev": "Edellinen", "next": "Seuraava",
           "skip": "Siirry sisältöön", "read": "Lisää uutisia"},
    "es": {"back": "\u2190 Noticias", "orig": "Publicado originalmente en sansox.fi",
           "author": "Autor", "prev": "Anterior", "next": "Siguiente",
           "skip": "Ir al contenido", "read": "Más noticias"},
}

MONTHS = {
    "en": ["January","February","March","April","May","June","July","August",
           "September","October","November","December"],
    "fi": ["tammikuuta","helmikuuta","maaliskuuta","huhtikuuta","toukokuuta","kesäkuuta",
           "heinäkuuta","elokuuta","syyskuuta","lokakuuta","marraskuuta","joulukuuta"],
    "es": ["enero","febrero","marzo","abril","mayo","junio","julio","agosto",
           "septiembre","octubre","noviembre","diciembre"],
}


def fmt_date(iso, lang):
    y, m, d = iso.split("-")
    mn = MONTHS[lang][int(m) - 1]
    if lang == "en":
        return f"{mn} {int(d)}, {y}"
    if lang == "fi":
        return f"{int(d)}. {mn} {y}"
    return f"{int(d)} de {mn} de {y}"


def blocks_html(body, keyprefix):
    """Muuntaa lohkolistan HTML:ksi ja palauttaa (html, {avain: teksti})."""
    out, keys = [], {}
    for n, b in enumerate(body, 1):
        k = f"{keyprefix}{n}"
        if "h" in b:
            out.append(f'<h2 data-i18n="{k}">{b["h"]}</h2>')
            keys[k] = b["h"]
        elif "ul" in b:
            items = []
            for i, li in enumerate(b["ul"], 1):
                kk = f"{k}_{i}"
                items.append(f'<li data-i18n="{kk}">{li}</li>')
                keys[kk] = li
            out.append('<ul class="bullets">' + "".join(items) + "</ul>")
        elif "img" in b:
            cap = b.get("cap", "")
            kk = f"{k}_c"
            stem = b["img"].rsplit(".", 1)[0]
            out.append(
                f'<figure><picture><source srcset="{stem}.webp" type="image/webp">'
                f'<img class="photo" src="{b["img"]}" alt="{html.escape(b.get("alt", cap))}" '
                f'width="{b.get("w", 640)}" height="{b.get("h", 400)}" loading="lazy" decoding="async">'
                f'</picture>' + (f'<figcaption class="cap" data-i18n="{kk}">{cap}</figcaption>' if cap else "")
                + "</figure>")
            if cap:
                keys[kk] = cap
        else:
            attr = "data-i18n-html" if "<" in b["p"] else "data-i18n"
            out.append(f'<p {attr}="{k}">{b["p"]}</p>')
            keys[k] = b["p"]
    return "\n      ".join(out), keys


def build(a, prev, nxt):
    en = a["en"]
    body_html, body_keys = blocks_html(en["body"], "b")
    cat = CATS[a["cat"]]

    # Kaannostaulu: sama avainjoukko jokaiselle kielelle.
    T = {}
    for lang in ("fi", "es"):
        loc = a[lang]
        _, lk = blocks_html(loc["body"], "b")
        T[lang] = {
            "skip": UI[lang]["skip"], "back": UI[lang]["back"],
            "kick": f'{cat[lang]} · {fmt_date(a["date"], lang)}',
            "h1": loc["title"], "lede": loc["lede"],
            "orig": UI[lang]["orig"], "read": UI[lang]["read"],
            "prevl": prev[lang] if prev else "", "nextl": nxt[lang] if nxt else "",
        }
        T[lang].update(lk)

    nav = []
    if prev:
        nav.append(f'<a href="{prev["file"]}" data-i18n="prevl">← {prev["en"]}</a>')
    if nxt:
        nav.append(f'<a href="{nxt["file"]}" data-i18n="nextl">{nxt["en"]} →</a>')
    nav_html = ('<nav class="postnav" aria-label="More news">' + "".join(nav) + "</nav>") if nav else ""

    hero_img = ""
    if a.get("img"):
        stem = a["img"].rsplit(".", 1)[0]
        hero_img = (f'<picture><source srcset="{stem}.webp" type="image/webp">'
                    f'<img class="photo hero-img" src="{a["img"]}" alt="{html.escape(a.get("alt",""))}" '
                    f'width="{a.get("w",640)}" height="{a.get("h",400)}" fetchpriority="high" decoding="async">'
                    f'</picture>')

    return f'''<!DOCTYPE html><html lang="en"><head><meta charset="utf-8">
<title>{html.escape(en["title"])} | SansOx</title>
<meta name="description" content="{html.escape(en["lede"])[:300]}">
<meta property="og:title" content="{html.escape(en["title"])}">
<meta property="og:description" content="{html.escape(en["lede"])[:300]}">
<meta property="og:type" content="article">
<meta property="og:url" content="{BASE}/{a["file"]}">
<meta property="og:site_name" content="SansOx">
<meta property="og:locale" content="en">
<meta property="og:locale:alternate" content="es">
<meta property="og:locale:alternate" content="fi">
<link rel="canonical" href="{BASE}/{a["file"]}">
<meta name="viewport" content="width=device-width, initial-scale=1">
<link rel="stylesheet" href="assets/css/case.css">
<script type="application/ld+json">
{json.dumps({"@context": "https://schema.org", "@type": "NewsArticle",
             "headline": en["title"], "datePublished": a["date"], "inLanguage": "en",
             "author": {"@type": "Person", "name": a["author"]},
             "publisher": {"@type": "Organization", "name": "SansOx Oy", "url": BASE + "/"},
             "mainEntityOfPage": BASE + "/" + a["file"]}, ensure_ascii=False)}
</script>
</head><body>
<a class="skip" href="#main" data-i18n="skip">Skip to content</a>
<div class="draft">DEMO · not published · content mirrored from sansox.fi · design study</div>
<header><div class="wrap posthead">
  <a href="index.html" class="logo">Sans<b>Ox</b></a>
  <span class="crumb"><a href="news.html" data-i18n="back">\u2190 News</a></span>
  <div class="lang"><button id="l-en" class="on">EN</button><button id="l-es">ES</button><button id="l-fi">FI</button></div>
</div></header>
<main id="main"><div class="wrap">
  <div class="hero">
    <div class="kicker" data-i18n="kick">{cat["en"]} · {fmt_date(a["date"], "en")}</div>
    <h1 data-i18n="h1">{en["title"]}</h1>
    <p class="lede" data-i18n="lede">{en["lede"]}</p>
  </div>
  {hero_img}
  <article class="post">
      {body_html}
  </article>
  <p class="src"><span data-i18n="orig">Originally published on sansox.fi</span>
     · {a["author"]}</p>
  {nav_html}
</div></main>
<footer class="site"><div class="wrap">
  <p><a href="index.html">SansOx</a> · <a href="news.html" data-i18n="read">Read more news</a></p>
  <p style="margin-top:8px">SansOx Oy / VAT FI24678326 / c/o Lahti Science Park, Niemenkatu 73, FI-15140 Lahti, Finland
     · <a href="tel:+358500603020">+358 500 603 020</a> / info@sansox.fi</p>
</div></footer>
<script>const T={json.dumps(T, ensure_ascii=False)};</script>
<script>
(function(){{
  function apply(l){{
    document.documentElement.lang=l;
    var d=T[l];
    document.querySelectorAll('[data-i18n]').forEach(function(e){{
      var k=e.getAttribute('data-i18n'); if(d&&d[k]!=null&&d[k]!=='') e.textContent=d[k];
      else if(!d&&e.dataset.en!=null) e.textContent=e.dataset.en;
    }});
    document.querySelectorAll('[data-i18n-html]').forEach(function(e){{
      var k=e.getAttribute('data-i18n-html'); if(d&&d[k]!=null&&d[k]!=='') e.innerHTML=d[k];
      else if(!d&&e.dataset.enh!=null) e.innerHTML=e.dataset.enh;
    }});
    ['en','es','fi'].forEach(function(x){{
      var b=document.getElementById('l-'+x); if(b) b.classList.toggle('on',x===l);
    }});
    try{{localStorage.setItem('sansox_lang',l);}}catch(e){{}}
  }}
  document.querySelectorAll('[data-i18n]').forEach(function(e){{e.dataset.en=e.textContent;}});
  document.querySelectorAll('[data-i18n-html]').forEach(function(e){{e.dataset.enh=e.innerHTML;}});
  ['en','es','fi'].forEach(function(x){{
    var b=document.getElementById('l-'+x); if(b) b.addEventListener('click',function(){{apply(x);}});
  }});
  var s=null; try{{s=localStorage.getItem('sansox_lang');}}catch(e){{}}
  if(s&&s!=='en') apply(s);
}})();
</script>
</body></html>
'''


def main():
    arts = []
    for f in sorted(os.listdir("posts")):
        if f.endswith(".json"):
            arts += json.load(open(os.path.join("posts", f), encoding="utf-8"))
    arts.sort(key=lambda x: x["date"], reverse=True)
    for a in arts:
        a["file"] = OUT_PREFIX + a["slug"] + ".html"
    for i, a in enumerate(arts):
        prev = nxt = None
        # prev = vanhempi juttu (nuoli vasemmalle), nxt = uudempi (nuoli oikealle).
        # Nuolen suunnan on oltava sama joka kielella, joten se kirjoitetaan
        # myos kaannoksiin — muuten EN nayttaa "Otsikko →" ja FI "← Otsikko".
        if i > 0:
            newer = arts[i - 1]
            nxt = {"file": newer["file"], "en": newer["en"]["title"],
                   "fi": newer["fi"]["title"] + " →", "es": newer["es"]["title"] + " →"}
        if i < len(arts) - 1:
            older = arts[i + 1]
            prev = {"file": older["file"], "en": older["en"]["title"],
                    "fi": "← " + older["fi"]["title"], "es": "← " + older["es"]["title"]}
        open(a["file"], "w", encoding="utf-8").write(build(a, prev, nxt))
        print("  ", a["file"])

    # Sivuotsikot ja kuvaukset kieliversioille. Ilman tata build_i18n.py jattaa
    # /fi/- ja /es/-sivujen <title>- ja description-tagit englanniksi, jolloin
    # hakukone indeksoi suomenkielisen sivun englanninkielisella otsikolla.
    meta = {a["file"]: [a["es"]["title"] + " | SansOx", a["es"]["lede"][:300],
                        a["fi"]["title"] + " | SansOx", a["fi"]["lede"][:300]]
            for a in arts}
    with open("posts/_meta.json", "w", encoding="utf-8") as f:
        json.dump(meta, f, ensure_ascii=False, indent=1)
    print(f"{len(arts)} artikkelisivua + posts/_meta.json")
    return arts


if __name__ == "__main__":
    main()
