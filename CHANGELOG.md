# CHANGELOG — SansOx site v2 (demo)

Vaihe 2 toteutettu 20.9.2026 Juhan hyväksymän vaihe 1 -analyysin pohjalta.
Alkuperäinen sansox.fi (Wix) on koskematon — tämä repo on rinnakkaisversio.

## A — välttämättömät korjaukset
| # | Analyysin kohta | Toteutus |
|---|---|---|
| A1 | IWA-paperi + Taulukko 1 piilossa | `case-kuopio.html`: tuloskortit, ainekohtainen taulukko (8 ainetta vs. 2 nykymenetelmää), PDF ladattavissa nimellä, IWA-leima. Koko taulukko kuvana `assets/paper/table1_substances.png` — **[TARKISTETTAVA] täysi litterointi ennen julkaisua** |
| A2 | Meta description vain etusivulla, OG puuttui | Kaikilla 11 sivulla description + og:title/description/type/image. **[TARKISTETTAVA] og:image absoluuttiseksi URL:ksi julkaisussa** |
| A3 | /oxtube ↔ /products ristissä | Ratkennut rakenteella: `technology.html` = tuote, `projects.html` = projektit |
| A4 | 6,6 Mt kuva; ei optimointia | Kaikki kuvat rajattu + pakattu; **WebP + JPG-fallback** `<picture>`-elementillä (talvikuva 316→196 kt, prototyyppi 74→29 kt) |
| A5 | Hintasuodatin (€0–€1) + tyhjä Book Online | Ei kumpaakaan uudessa rakenteessa |
| A6 | Tekoälykuva blogissa | Jätetty pois; suositus poistaa myös Wixistä |
| A7 | Alt-tekstit puuttuivat (mm. 9/12), /blog ilman H1:tä | Kaikilla img-elementeillä kuvaava alt; jokaisella sivulla yksi H1 |

## B — selvät parannukset (toteutettu samalla)
- Arvolupaus luvuilla (90 % · 0,7 s · 1 s · 6) + yritysfaktarivi: rek. 2012 (PRH) · IWA 2021 · Water Europe 2014 · **"yli 100 asennusta ~20 maassa" [TARKISTETTAVA firmalta — lähde Karjalainen-artikkeli]**
- Yksi CTA joka sivulla: "Book 30 min with our engineers"
- Rakenne alkuperäisen mallin mukaan: lyhyt hubi + Solutions / Projects / Technology / Company / News
- 5 referenssisivua samalla rungolla (lähtötilanne → asennus → mitatut tulokset → mitä seuraa); puuttuvat kuvat merkitty 📷-paikanpitäjin = kuvauslista
- Kolme kieltä etusivulla (EN/ES/FI) — **alasivujen ES/FI-käännökset tekemättä**
- EU-jätevesidirektiivi (tuottajavastuu ≥80 %) Kuopio-caseen · Baltic Sea -konsortio (Salo·THL·Savonia) Companyyn · Bangladesh-JV faktoineen Solutionsiin · Intian instituutiot + 4 postauksen aikajana caseen
- News: 13 oikeaa postausta feedistä (linkit alkuperäisiin kunnes sisältö siirretään)

## Brändi
- Ilme: tumma + aqua — **tietoinen poikkeama** Wixin vaaleasta (Juhan hyväksymä suunta; erottuu Moleaerista ja Mazzeista)
- Logo: talteen `assets/img/sansox_logo_from_screenshot.png` — **[TARKISTETTAVA] pyydä vektori + negatiiviversio tummalle pohjalle; siihen asti tekstilogo**
- Ei keksittyjä faktoja: jokainen luku on Pylkkäsen paperista, PRH:sta tai firman omista julkaisuista

## Kuvakaappaukset
`docs/screenshots/ennen_sansox-fi_etusivu.jpg` · `docs/screenshots/jalkeen_uusi_etusivu.jpg`
Mobiili: CSS on mobile-first ja testattu artifact-esikatselussa; **erillinen laitetesti Juhan puhelimella tekemättä** (ikkunan pienennys ei tallentunut kaappaukseen).

## Auki (C-lista + kysyttävät)
Mitoitustyökalu (vaatii Pylkkäsen luvut: virtaama, kgO₂/kWh, painehäviö) · hero-video · kuvat kumppaneilta (Unique Water, Caviar, Elixiirin "jälkeen") · Pylkkäsen titteli (paperissa CTO, sivulla Chief Engineer) · patenttinumerot · ClariOx-tuotteen paikka · hosting + domain-siirto (firman päätös)
