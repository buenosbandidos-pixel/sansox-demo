# Design-muistiinpanot

**Päivitetty 2026-09-21.** Edellinen versio väitti asioita joita koodissa ei ollut (mm. Saira-fontti).
Alla on vain se mikä on oikeasti tiedostoissa — jokaisen kohdan voi tarkistaa annetulla komennolla.

---

## Tokenit

Määritelty kahdesti: `assets/css/site.css` ja `assets/css/case.css`. **Molemmat pidettävä synkassa.**

| Token | Arvo | Nimi | Kontrasti taustaa vasten |
|---|---|---|---|
| `--bg` | `#071019` | Syvänne | — |
| `--panel` | `#0a1826` | — | — |
| `--line` | `#16283a` | Teräs | 1,3:1 (vain koriste) |
| `--ink` | `#e9f2f9` | Vaahto | 16,9:1 |
| `--dim` | `#8aa3b8` | Sumu | 7,3:1 |
| `--aqua` | `#3ec6ff` | Happi | 9,8:1 |
| `--aqua-deep` | `#0f5f8f` | — | — |
| `--rust` | `#c96f3b` | Ruoste (hapettuminen = aihe) | 5,3:1 |

Koko paletti läpäisee WCAG AA:n. `--line` on alle rajan, mutta se on vain reunaviiva — ei tekstiä.

```bash
grep -h ':root' assets/css/site.css assets/css/case.css
```

⚠️ `--rust` puuttui `case.css`:n `:root`:sta 21.9. asti, jolloin `blockquote`-reuna renderöityi
tekstin valkoisella eikä ruosteella. Jos lisäät uuden tokenin, lisää se **molempiin** tiedostoihin.

---

## Typografia — järjestelmäfontti, ei Sairaa

```
font:16px/1.6 -apple-system, BlinkMacSystemFont, "Segoe UI", Helvetica, Arial, sans-serif
```

Otsikot: `font-weight:800`, tiukka `letter-spacing` (h1 −1,5px, isot luvut −2px), `text-wrap:balance`.

**Historia — älä käännä tätä takaisin vahingossa:**
- `119eb6b` Saira lisättiin takaisin ("se oli paras osa")
- `8c81b59` **Saira poistettiin — Juhan valinta rinnakkaisvertailussa.** Järjestelmäfontti voitti.

Sivusto näyttää siis eri fontilla Macillä ja Windowsilla. Se on tietoinen valinta, ei puute.
Jos Saira otetaan joskus käyttöön, se on hostattava itse (`assets/`), ei Google Fontsista.

```bash
grep -rl "Saira\|@font-face\|fonts.googleapis" *.html assets/css/   # pitää olla tyhjä
```

---

## "AI-tellit" — mitä oikeasti poistettiin, mitä tuli takaisin

Vanha muistiinpano listasi kuusi poistettua maneeria. Tarkistettuna 21.9. **kolme niistä on yhä koodissa
— ja kaikki kolme on päätetty jättää (perustelut alla).**

| Maneeri | Tila | Missä |
|---|---|---|
| `·`-erottimet footerissa | ✅ poistettu, käyttää ` / ` | footer |
| Radial-hehkut | 🔄 2 jäljellä — jää | `case-kuopio.html` heron tausta |
| Caps-eyebrow | 🔄 6 sääntöä — jää | case-sivujen `.kick`, taulukoiden `th`, `.person span`, `.ph b` |
| `→`-nuolet | 🔄 19 kpl — jää | `news.html` 15, `case-india.html` 4 |
| h1:n yhden sanan väri | 🔄 **palautettu tarkoituksella** | `h1 em{color:var(--aqua)}` |
| SaaS-korttisarja → spec-rivit | ✅ pysynyt | — |

**h1 em on Juhan päätös** (`661edee`, "valko+sininen kaksivärisyys takaisin v1:n tapaan").
Älä poista sitä design-puhtauden nimissä — se on valittu.

**PÄÄTETTY 21.9.2026 (Juha): kaikki kolme jäävät.** Perustelut tarkistettu koodista, ei listasta:

- **→-nuolet (19 kpl)** — jokainen on ulkoisen linkin merkki: `source: sansox.fi →`, `→ post`.
  Toiminnallinen affordanssi, ei koriste. Poistaminen heikentäisi sivua.
- **Caps-eyebrow (6 sääntöä)** — kantaa oikeaa tietoa: "MEASURED RESULT · MUNICIPAL WASTEWATER ·
  KUOPIO, FINLAND". Dateline, ei maneeri.
- **Radial-hehkut (2)** — opasiteetti .13 ja .18. Katsottu sivulta: käytännössä näkymättömiä.

Vanha muistiinpano leimasi nämä poistettaviksi luettelona, ei katsomalla. Älä poista niitä
"design-puhtauden" nimissä ilman uutta päätöstä.

---

## Rohkeus yhdessä paikassa

**3D-hero etusivulla** — käsin kirjoitettua 2D-canvasta, 145 riviä, ei Three.js:ää eikä mitään kirjastoa.
Se on sivuston ainoa efekti ja saa olla.

Ruoste vain pieninä annoksina: `.tag`-merkinnät (26 kpl) ja `blockquote`-reuna (3 sivua).
Ei ruostetta pinnoiksi eikä napeiksi.

---

## CTA-kuri

**Yksi tarjous, toistettuna:** "Book 30 min with an engineer" / "Varaa 30 min insinöörin kanssa" /
"Reserve 30 min con un ingeniero" — täytettynä `.btn`-nappina etusivun herossa ja loppupalkissa.
Kaikki muu on `.btn ghost` tai tekstilinkki.

Jos lisäät uuden täytetyn napin, poista jokin vanha. Kaksi kilpailevaa ensisijaista nappia = ei yhtään.

---

## Kuvat

Jokaisella `<img>`-tagilla on `width` + `height` (varaa tilan, estää sivun hyppimisen) ja
`loading="lazy"` paitsi taitteen yläpuolisilla, joilla on `fetchpriority="high"`.

⚠️ Mitat toimivat **vain** koska CSS:ssä on `img{max-width:100%;height:auto}`. Ilman sitä selain
ottaa `height`-attribuutin kirjaimellisesti ja kuvat venyvät. Jos kuvalla on inline-korkeus
(`max-height`, `height`), se tarvitsee lisäksi `width:auto`.

```bash
grep -c 'loading=\|width=' *.html        # jokaisella img:llä pitää olla molemmat
```

---

## Mikä on yhä kokeilematta

- Title-block-tyylinen sivunumerointi footerissa
- Ruoste "ennen/jälkeen"-koodauksena case-sivuilla (nyt vain `case-kuopio`in liukusäädin)

## Päätetty: case-kuopio.html pysyy inlinenä

Sen CSS eroaa muista case-sivuista **28 säännön arvoissa** (`:root`, `.btn`, `.hero`, `.num`…).
Se on lippulaivasivu omalla ennen/jälkeen-liukusäätimellä, joten haarautuminen on perusteltu.
Yhdistäminen muuttaisi ulkoasua eikä sitä kannata tehdä ennen kuin firma on vahvistanut sisällön.
**Päätetty 21.9.2026 (Juha): ei designkierrosta tälle sivulle nyt.**

## Domain esiintyy yhdessä paikassa

`build_i18n.py` → `BASE`. Skripti kirjoittaa sen mukaan `canonical`, `og:image` ja JSON-LD:n
joka ajolla. Hosting-päätöksen jälkeen vaihdat yhden rivin ja ajat buildin.

⚠️ **Sisältölinkkejä ei kosketa.** 38 linkkiä osoittaa `https://www.sansox.fi/post/...` eli elävään
Wix-blogiin. Sokea domain-korvaus rikkoisi ne, joten `set_meta_urls()` kohdistuu vain og:imageen ja
JSON-LD:hen. Testattu: BASE vaihdettuna `new.sansox.fi`:ksi metatiedot seurasivat, 0 sisältölinkkiä rikki.

🔴 **Avoin:** ne 38 `/post/`-linkkiä menevät rikki siinä vaiheessa kun domain käännetään uuteen
sivustoon, koska uudella sivustolla ei ole `/post/`-sivuja. Päätettävä ennen julkaisua: jäävätkö
blogit Wixiin (silloin linkkien on osoitettava vanhaan osoitteeseen eksplisiittisesti) vai
siirretäänkö ne.

## ⚠️ Yksiköt ja text-transform — älä toista tätä

`text-transform:uppercase` **rikkoo SI-etuliitteet**. "µg/l" muuttuu muotoon "ΜG/L" (kreikan iso My,
U+039C), joka näyttää tavallisella pääteviivattomalla fontilla täsmälleen samalta kuin "MG/L".
Ero on **tuhatkertainen**. Tämä ehti todella renderöityä ainetaulukon otsikoihin 21.9. ennen kuin se
huomattiin.

Sääntö: taulukossa jossa on yksiköitä, otsikoissa **ei** saa olla `text-transform:uppercase`.
Sama koskee `m` vs `M` ja `k` vs `K`.

```bash
grep -n "text-transform:uppercase" assets/css/*.css *.html   # tarkista ettei osu yksikkösoluihin
```

## Ainetaulukko (case-kuopio) — miten se on rakennettu

- Data: `assets/paper/table1_full.json` — 42 ainetta + summarivi, litteroitu paperin sivulta 4.
  **Tiedostossa on `source_anomalies_DO_NOT_SILENTLY_FIX`-lista** (Losartan kahdesti, Warfarinin
  jäännös > lähtö, puuttuvat lähtöarvot, lähteen kirjoitusvirheet). Niitä ei korjata.
- Verifiointi: lähtöpitoisuussarake summautuu **tasan** paperin ilmoittamaan 24.162 µg/l:aan, ja
  jokaisen rivin ilmoitettu reduktio vastaa laskettua. Jos muokkaat dataa, aja tarkistus uudelleen.
- HTML: `.subtab` — ensimmäinen sarake `position:sticky`, vaakavieritys `.tablewrap`issa,
  heikot tulokset (<50 %) ruosteella. **Heikkoja tuloksia ei piiloteta — se on koko pointti.**
- Desimaalierotin lokalisoidaan JS:llä (piste EN, pilkku FI/ES). Kanoninen arvo luetaan talteen
  latauksessa, joten toistuva kielenvaihto ei kerrytä muunnoksia. Testattu 7 vaihdolla.
