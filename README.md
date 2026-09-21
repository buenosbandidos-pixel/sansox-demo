# SansOx — uusi sivusto (demo → tuotanto)

Rakennettu rinnalle; Wix-sivusto pysyy pystyssä kunnes tämä on valmis ja domain käännetään.

## Rakenne
- `index.html` — etusivu, 3 kieltä (EN/ES/FI) JS-vaihdolla, mobile-first, tumma ilme
- `case-kuopio.html` — ensimmäinen referenssisivu (IWA 2021 -datalla)
- `assets/img/` — paperista irrotetut aidot koekuvat (rajattu, muuten käsittelemättä)
- `assets/paper/` — Pylkkänen, IWA Milano 2021 (lähde kaikille luvuille)

## Esikatselu
    cd ~/Documents/sansox-site && python3 -m http.server 9990
    → http://localhost:9990

## Periaatteet (sovittu 20.9.2026)
1. Todiste edellä: isot mitatut luvut, lähde aina näkyvissä — ei yhtään keksittyä arvoa
2. Kuvat vain aitoja (koekuvat, prototyyppi historiakuvana) — ei kuvapankkia
3. Mobile first · 4-osainen referenssirunko: lähtötilanne → asennus → mitatut tulokset → mitä seuraa
4. Yksi CTA: "30 min insinöörin kanssa"
5. Kolme kieltä alusta asti

## Seuraavat
- [ ] 4 muuta referenssisivua (Filippiinit, Carelian Caviar, Intia, Siuntio/Kokkola)
- [ ] Kuva-/videomateriaalikysely Seppälälle/Pylkkäselle (nykyinen moduuli ilman Gardenaa!)
- [ ] Tekniset luvut Pylkkäseltä: virtaama-alue, kgO2/kWh, painehäviö
- [ ] GitHub-repo + hosting (SansOxin tili — EI luoda ilman firman päätöstä)
- [ ] Domain-siirto vasta kun sisältö on Wixiä parempi

## Rakennusskriptit (ajojärjestys on tärkeä)

```bash
python3 build_posts.py    # 1. uutisartikkelit posts/*.json:sta -> post-*.html + posts/_meta.json
python3 build_i18n.py     # 2. /fi/ ja /es/, hreflangit, canonicalit, sitemap.xml, robots.txt
```

`build_i18n.py` **muokkaa juuritiedostoja paikan päällä**: se lisää hreflang-tagit
ja vaihtaa kielivalitsimen JS-napeista oikeiksi linkeiksi `/fi/`- ja `/es/`-versioihin.
Siksi se ajetaan viimeisenä. Jos ajat vain `build_posts.py`:n, artikkelisivut palaavat
JS-valitsimeen ja niiden hreflangit katoavat — aja silloin myös `build_i18n.py`.

Verkkotunnus on `BASE`-muuttujassa `build_i18n.py`:n alussa ja `build_posts.py`:ssä.
Kun hosting on päätetty, muuta se molempiin ja aja skriptit uudelleen.
