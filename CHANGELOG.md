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

## Täydennys 20.9. ilta — demo valmis
- Kielikytkin (EN/ES/FI) nyt **kaikilla 11 sivulla**
- Hubisivut (Solutions/Projects/Technology/Company/News): otsikot, ingressit ja osiot käännetty kokonaan
- Case-sivut: nelivaiheisen rungon otsikot, pääotsikot ja CTA käännetty; **leipätekstikappaleet EN — käännetään sisällön lukituttua** (turha kääntää tekstiä joka muuttuu kun firman luvut saadaan)
- Kuopio-casen oma CTA ("Talk to the engineer who ran this trial") jäi EN — poikkeaa vakiorungosta

## [2026-09-20] Korjauskierros 2 — tuotekuvat, 3D, Products, täydet käännökset
- **Tuotekuvat löydetty vanhalta sivustolta** (Juhan huomio — olin missannut): OxTube-renderöinti (/products) + korkearesoluutioinen asennuskuva (pystyasennus suomalaisella laitoksella, 3648×2736). Käsitelty → `oxtube_installed_vertical.jpg/webp`, `oxtube_module_render.png`.
- **Etusivulle proseduraalinen 3D-tuotemalli** (canvas, ei kirjastoja): laipat, venturi-kavennus, hidas pyöritys + slogan "Improving Water Quality". prefers-reduced-motion kunnioitetaan, IntersectionObserver pysäyttää näkymättömissä.
- **Koko vanha sivusto kartoitettu sivukartasta**: 8 sivua + 18 tuotesivua + 13 blogia + 3 varattavaa palvelua. Rakennevastaus: uusi sivusto = alkuperäinen hub-rakenne (ei BB:n); aukko oli Products-taso → korjattu.
- **products.html luotu**: tuoteperhe OxTube/RadOx/IroX/UGOx/GasRemox/Lady Bug + palvelut (konsultaatio, kurssi, koulutus), 3 kielellä. ClariOx [TARKISTETTAVA]. Navigaatioon + footeriin kaikilla sivuilla.
- **Case-sivujen TÄYDET ES/FI-käännökset** (kicker, lede, mittarit, leipätekstit, taulukot, sitaatit, napit). Kuopiosta puuttui koko kielivalitsin → lisätty. Kuopion kuollut CTA-linkki (#) → mailto.
- **Faktakorjaus case-india**: pilotti oli Sukhrali (Gurugram), Sadpura on laajennus — lede väitti väärin.
- **Siuntion 📷-paikanpitäjä korvattu oikealla asennuskuvalla** ("nykyinen sukupolvi" prototyypin rinnalla).
- **News: 13 tiivistelmää paikan päälle 3 kielellä** (lähdelinkit säilyvät pieninä). Ei enää pelkkiä linkkejä vanhalle Wixille.
- Aiemman kierroksen A-lista: footer (VAT FI24678326 + osoitteet + navigaatio + privacy.html), og:image absoluuttiseksi, CTA-nauha Technology/Projects/News, EU-lukujen lähdemerkintä, tekstiparannukset ①–⑩, "world's strictest" -toisto purettu, ristilinkit casien välille.
- QA: 0 löydöstä, kaikki 13 sivua HTTP 200. Selainverifiointi: 3D piirtyy, FI-kieli jättää vain palkintojen erisnimet englanniksi.
- [TARKISTETTAVA]: ClariOx-kuvaus · GasRemox-rooli · palvelusivujen sisällöt (Wix-varauskuvaukset ohuita)

## [2026-09-20] Korjauskierros 3 — 3D renderin mukaiseksi + käännösten loppusiivous
- 3D-malli rakennettu tuoterenderin geometrian mukaan: laippaparit, kaksi materiaalia (tumma putki + kiiltävä rst spekulaarijuovalla), kartiolaajennus + paksu moduuli, keltaiset anturisondit, solakat mittasuhteet.
- Kuvatekstit joissa oli englantia FI/ES-kielillä → käännetty: technology (pr2_*, 4 prosessivaihetta, prototyyppiteksti), kuopio (jakajan kuvateksti), company (talvilampi), CTA-nauhat (projects/news/technology).
- Päänavigaatio + footerin linkit käännetty kaikilla sivuilla (Ratkaisut/Tuotteet/…).
- Bugikorjaus: index+products EN-harvesteri ei tavoittanut skriptin jälkeistä footeria → kielen paluu EN:ään olisi jättänyt footerin suomeksi. Harvest ajetaan nyt myös DOMContentLoadedissa.
- Jäljelle jäävä englanti FI/ES-näkymissä: palkintojen ja julkaisujen erisnimet (tarkoituksella).

## [2026-09-20] RAKENNE A — hyväksytty ja toteutettu
- Navigaatio 7 → 5 ovea: `Solutions · Products · References · Technology · Company`
- **references.html** = Projects + News yhdistettynä: 4 näyttöcasea (kaikilla mitattu tulos) + 13 uutistiivistelmää "Kentältä"-virtana. Otsikot, tagit ja lähdelinkit käännetty; tupla-kielivalitsin siivottu.
- **case-siuntio poistettu referenssinä** — alkuperätarina EI ole asiakascase. Sisältö siirtyi company.html#story-osioksi "Mistä kaikki alkoi" (prototyyppi → Kokkola → Siuntio → Water Europe 2014/2015), 3 kielellä.
- **Technology**: erillinen "Where it started" -osio pois; prototyyppi jäi yhdeksi riviksi tuoteosioon linkillä koko tarinaan.
- **Etusivu ohennettu yhteen näytölliseen**: 3D + slogan, faktarivi, numerot, 3 segmenttiovea, CTA. Ennen/jälkeen-jakaja poistettu (elää Kuopio-casessa) → tilalle linkki "Katso mitä yhdessä sekunnissa tapahtuu →". IWA-leima siirtyi Kuopion paperilinkin viereen.
- projects.html, news.html, case-siuntio.html poistettu; kaikki linkit päivitetty. QA 0 löydöstä, 11 sivua HTTP 200, FI/EN-kielikierros verifioitu selaimessa.
- Perustelu (vertailu A vs B kirjattu keskusteluun): ostajan sanasto (References/Technology), julkaistut luvut pääsivuna, A→B-tiivistys mahdollinen myöhemmin halvalla.

## [2026-09-20] 3D-hero v3 — realismi + kehyskorjaus
- Ongelma: täysi 360°-pyöritys + voimakas perspektiivi → päät karkasivat canvasista ja putki osoitti ajoittain kohti kameraa muodottomana.
- Korjaus: heilurikääntö ±32° sivuprofiilin ympäri; sovitus lasketaan etukäteen pahimman kulman yli (sondien kärjet mukana); perspektiivi 5.5 → 12.
- Realismi: normaalipohjainen valaistus (diffuusi + spekulaari + fresnel-reunaheijastus), täytevalo ettei mikään kulma jää pimeäksi, materiaalikohtaiset kiillot (rst-jaksolla terävä kiiltojuova), SEG 32→48, saumaton pinta, pehmeä pohjavarjo.
