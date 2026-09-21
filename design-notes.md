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

Vanha muistiinpano listasi kuusi poistettua maneeria. Tarkistettuna 21.9. **kolme niistä on yhä koodissa:**

| Maneeri | Tila | Missä |
|---|---|---|
| `·`-erottimet footerissa | ✅ poistettu, käyttää ` / ` | footer |
| Radial-hehkut | ⚠️ 2 jäljellä | `case-kuopio.html` heron tausta |
| Caps-eyebrow | ⚠️ 6 sääntöä | case-sivujen `.kick`, taulukoiden `th`, `.person span`, `.ph b` |
| `→`-nuolet | ⚠️ 19 kpl | `news.html` 15, `case-india.html` 4 |
| h1:n yhden sanan väri | 🔄 **palautettu tarkoituksella** | `h1 em{color:var(--aqua)}` |
| SaaS-korttisarja → spec-rivit | ✅ pysynyt | — |

**h1 em on Juhan päätös** (`661edee`, "valko+sininen kaksivärisyys takaisin v1:n tapaan").
Älä poista sitä design-puhtauden nimissä — se on valittu.

Loput kolme ovat avoimia: poistetaanko vai hyväksytäänkö? Ei päätöstä. Case-sivujen caps-eyebrow
kantaa oikeaa tietoa ("MEASURED RESULT · MUNICIPAL WASTEWATER · KUOPIO"), joten se ei ole tyhjä maneeri.

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
- `case-kuopio.html`:n CSS on yhä inline: se eroaa muista case-sivuista 28 säännön arvoissa.
  Yhdistäminen muuttaisi ulkoasua, joten se vaatii oman designkierroksen.
