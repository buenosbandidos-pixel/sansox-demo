# Design-analyysi 21.9.2026

## Kansion sisältö

```
nykyinen/     26 kuvakaappausta — 13 sivua × desktop (1440) + mobiili (390)
kilpailijat/  6 kilpailijan etusivu (1440)
mockupit/     3 designsuuntaa HTML:nä + kuvakaappaukset
```

## Kuvakaappausten tekninen huomio

Desktop-kaappaukset ovat headless Chromella suoraan sivuista.

**Mobiilikaappaukset on otettu `_mobwrap.html`-kääreen kautta**, joka upottaa sivun
390 px:n iframeen. Syy: headless Chrome ei noudata `--window-size`-arvoa layout-viewportina
ilman laite-emulointia, vaan renderöi leveämmällä ja rajaa kuvan — jolloin näyttää siltä
että sivu vuotaa yli, vaikka se ei vuoda. Varmistin asian selaimen oikealla mobiiliemuloinnilla:
**sivu mahtuu 390 px:iin, vaakavieritystä ei ole.**

`_mobwrap.html` on apuväline. Se voi jäädä repoon tai sen voi poistaa — ei ole linkitetty mistään.

## Kilpailijat

| Tiedosto | Yritys | Huom |
|---|---|---|
| `01_oxymem.png` | OxyMem 🇮🇪 | DuPontin brändi, MABR-ilmastus |
| `02_landia.png` | Landia 🇩🇰 | perheyritys, sekoittimet ja ilmastimet |
| `03_invent.png` | INVENT 🇩🇪 | evästemuuri peittää koko sivun |
| `04_nijhuis.png` | Nijhuis Saur 🇳🇱 | Saur-konserni |
| `06_aquaporin.png` | — | **ei latautunut** (ERR_CONNECTION_REFUSED) |
| `07_grundfos.png` | — | **ei latautunut** (ERR_HTTP2_PROTOCOL_ERROR) |

Xylem torjui headless-selaimen; katsoin sen selainpaneelissa, kaappausta ei ole tiedostona.
Käyttökelpoisia kaappauksia on siis **4**, plus Xylem katsottuna. Se riitti kategorian
oletusdesignin tunnistamiseen, koska toistuvuus oli erittäin selvä.

## Mockupit

Avaa selaimessa:
```
http://localhost:9995/design_analyysi/mockupit/suunta_1_mittaustulos.html
http://localhost:9995/design_analyysi/mockupit/suunta_2_kolme_insinooria.html
http://localhost:9995/design_analyysi/mockupit/suunta_3_putki.html
```

Ne ovat **itsenäisiä tiedostoja** — eivät käytä sivuston CSS:ää eivätkä vaikuta siihen mitenkään.
Suunta 2:n kasvokuvat ovat paikkamerkkejä; oikeat kuvat ovat `assets/img/team_*.jpg`.
