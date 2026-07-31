# Politika zasebnosti aplikacije Plume

**Zadnja posodobitev: 31. julij 2026** — Različica 1.0

---

## Kdo je upravljavec vaših podatkov

**SASU RedLine Music**
SIREN 938 277 100 — SIRET `938 277 100 00013`
Abbaye 208-1, 208 Résidence Lavoisier, 18100 Vierzon, France
Kontakt: sogacmoi7@gmail.com

Aplikacija je objavljena v Google Play pod imenom izdajatelja **openfunword**.

Ta politika opisuje, kaj aplikacija Plume počne v svoji trenutni različici. Napisana je bila z branjem kode aplikacije, ne po splošni predlogi.

---

## V eni minuti

Plume vam pomaga pisati: vaše besedilo preoblikuje neposredno v aplikaciji, v kateri pravkar tipkate, in zna prevesti besedilo, prikazano na zaslonu.

Tri stvari, ki si jih velja zapomniti:

1. **Plume na svojih strežnikih ne hrani nobenega vašega besedila.** Ne vaših preoblikovanih besedil ne besedila, prebranega z zaslona. Ne hranimo niti kopije niti dnevniškega zapisa.
2. **Glede na izbrani pogon vaše besedilo zapusti telefon ali pa ne.** Dva pogona (Lokalni komplet in Lokalna umetna inteligenca) delujeta v celoti na napravi. Tretji (Umetna inteligenca v oblaku) besedilo pošlje storitvi umetne inteligence, ki je **zunaj Evropske unije**. Izbirate vi, Umetna inteligenca v oblaku pa se nikoli ne vklopi brez vaše izrecne privolitve.
3. **Plume potrebuje močna dovoljenja** (branje vsebine, prikazane v drugih aplikacijah, zajem zaslona). Spodaj natančno pojasnjujemo, čemu služijo in čemu ne.

---

## 1. Kaj Plume bere na vašem zaslonu in kdaj

### 1.1 Storitev za dostopnost

Da lahko vaše besedilo prepiše prav tam, kjer ga pišete, Plume uporablja Androidovo storitev za dostopnost. To je dovoljenje, ki ga vklopite sami, v nastavitvah telefona, po pojasnilnem zaslonu, ki vam ga Plume pokaže, **preden** ga zahteva.

Konkretno:

- **V mirovanju** Plume ve le, katera aplikacija je odprta in v katerem trenutku postavite kazalec v vnosno polje. Prav to sproži prikaz lebdeče kapsule — in to izključno v aplikacijah, ki ste jih sami nastavili.
- **Vsebina polja se prebere le v natančnem trenutku, ko se dotaknete kapsule**, da se prepiše in nato zamenja na mestu.
- **Polja za geslo so izključena.** Aplikacija zazna polja vrste geslo (vključno s številčnimi kodami in spletnimi polji) in jih noče brati.
- To dovoljenje **ne omogoča nikakršnega zajema slike** vašega zaslona.
- Plume **nikoli ne pritiska namesto vas** v drugi aplikaciji: zamenja besedilo v polju in nič drugega.

Dve funkciji, ki ju vklopite sami — **Asistirano branje v besedilnem načinu** in **prevajanje prejetih sporočil** — bereta prikazano besedilo neprekinjeno, dokler tečeta, in se ustavita takoj, ko ju izklopite.

Če storitev za dostopnost zavrnete, Plume ostane uporaben: besedilo lahko izberete in uporabite meni »Plume« ob izbiri besedila v Androidu ali pa besedilo delite s Plumeom.

### 1.2 Zajem zaslona (Asistirano branje)

Asistirano branje prekrije prikazano besedilo s prevodom — na primer oblačke v stripu. Za to mora videti sliko zaslona.

- Privzeto je **izklopljeno** in deluje samo v aplikacijah, ki ste jih izrecno dovolili, eno za drugo.
- **Android ob vsakem zagonu seje zahteva svojo privolitev.** To ni dovoljenje, dano enkrat za vselej: vsaka seja zahteva novo soglasje. Plume tega soglasja nikoli ne poskuša znova uporabiti ali zaobiti.
- Ves čas seje **ostaneta vidna trajno obvestilo in sistemski kazalnik**. Plume vašega zaslona ne more zajemati na skrivaj.
- Seja se **samodejno ustavi ob zaklepu zaslona** in takoj, ko jo ustavite sami.
- Aplikacije, ki varujejo svoj prikaz (bančne aplikacije, upravitelji gesel), **zatemni Android sam**, preden Plume karkoli prejme. To je zaščita sistema, resnična, a delna: vklopijo je ne vse občutljive aplikacije. Zato je ne predstavljamo kot absolutno jamstvo.
- **Zajete slike se nikoli ne shranjujejo in ne pošiljajo.** Vsaka slika se analizira v pomnilniku, da se iz nje izlušči besedilo, nato pa se opusti. Nobena slika nikoli ne zapusti vašega telefona, ne glede na izbrani pogon.

---

## 2. Kaj ostane na vašem telefonu in kaj ga zapusti

To je najpomembnejše razlikovanje v tej politiki in nadzirate ga vi.

### 2.1 Pogona, ki ne izneseta ničesar

- **Lokalni komplet** (prepoznavanje in prevajanje besedila brez povezave) deluje v celoti na napravi.
- **Lokalna umetna inteligenca** je model umetne inteligence, ki se enkrat prenese in nato shrani na vaš telefon (približno 720 MB). Izvaja se na vaši napravi.

S tema dvema pogonoma **prebrano ali preoblikovano besedilo ne zapusti vašega telefona.** Ni nobenega omrežnega klica, povezanega z vsebino vašega besedila.

### 2.2 Pogon Umetna inteligenca v oblaku

Ko izberete Umetno inteligenco v oblaku ali ko vaša naprava ni dovolj zmogljiva za Lokalno umetno inteligenco, se zadevno besedilo prenese na naše strežnike, nato pa storitvi umetne inteligence tretje osebe.

**Glede dejanske poti je treba biti jasen:**

- Besedilo gre skozi našo infrastrukturo (Supabase), ki gostuje v **Evropski uniji** (regija Srednja Evropa, Frankfurt).
- Nato se prenese na **openrouter.ai**, posrednika za usmerjanje, ki je **zunaj Evropske unije** in ga da v obdelavo modelu **Mistral Small**.
- **Gre torej za prenos podatkov zunaj Evropske unije.** Ne trdimo nasprotnega in za ta korak ne prikazujemo nobene obljube o evropskem gostovanju.
- **Plume vašega besedila ne hrani.** Nobena naša strežniška funkcija ne zapisuje vsebine vašega besedila: zabeležimo le tehnični identifikator zahteve in identifikator vaše naprave, da preštejemo vašo kvoto in zaznamo zlorabe.
- **Kaj ti ponudniki počnejo na svoji strani, ne moremo jamčiti.** Raje vam to povemo, kot da vam obljubljamo ničelno hrambo, ki je ne moremo preveriti.

**Umetna inteligenca v oblaku se nikoli ne vklopi sama.** Poseben zaslon za privolitev vam te točke pojasni pred prvim pošiljanjem in nič ne odide, dokler ne sprejmete. Če Lokalna umetna inteligenca odpove, Plume ne preklopi v oblak potiho: to vam sporoči in počaka na vašo odločitev. To privolitev lahko kadar koli prekličete v nastavitvah.

Poslano besedilo je omejeno: 1.200 znakov za preoblikovanje in 4.000 znakov za analizo zaslona.

---

## 3. Podatki, ki jih hranimo

Ne uporabljamo **nobenega orodja za analitiko obiskanosti, nobenega oglaševalskega sledilnika tretjih oseb, nobenega orodja za poročanje o sesutjih**. Aplikacija ne vsebuje merilnega SDK.

Tukaj je vse, kar je shranjeno na naših strežnikih:

| Podatek | Zakaj | Trajanje |
|---|---|---|
| **Identifikator naprave** (naključna številka, ki jo ustvari Plume, brez povezave z vašo identiteto ali z oglaševalskim identifikatorjem) | Povezava naprave z računom, uveljavljanje kvot, blokiranje zlorab | Do izbrisa vašega računa |
| **E-poštni naslov računa** (če ustvarite račun z e-pošto ali prek Googla) | Vaše preverjanje pristnosti, povezava vaše naročnine | Do izbrisa vašega računa |
| **Števci uporabe** (število preoblikovanj na dan in na mesec — številke, ne besedila) | Uveljavljanje kvot | Do izbrisa vašega računa |
| **Zgodovina nakupov** (identifikator transakcije Google Play, datumi, stanje naročnine) | Da vam omogočimo dostop do tega, kar ste plačali, upravljamo podaljšanja in izpolnjujemo računovodske obveznosti | Hrani se tudi po izbrisu računa, vendar **ločena od vaše identitete** (glejte §6) |
| **Prostovoljno poslani predlogi** (če nam iz aplikacije pošljete predlog persone) | Izboljšanje kataloga. Ti predlogi se nikoli ne objavijo. | Do izbrisa vašega računa |
| **Tehnični signali zlorabe** (ponavljajoče se prekoračitve, neuspešno preverjanje celovitosti — brez vsakršnega besedila) | Varnost, boj proti goljufijam | Ob izbrisu računa se ločijo od vaše identitete |
| **Jezik in različica aplikacije** | Dostava ustrezne vsebine | Do izbrisa vašega računa |

**Česa ne zbiramo:** vašega imena, vaših stikov, vaše lokacije, vašega imenika, vaših fotografij, vašega koledarja, zgodovine vaših aplikacij. Plume ne zahteva nobenega od teh dovoljenj.

**Kaj ostane izključno na vašem telefonu:** vaše prilagojene persone in njihovi avatarji, vaše nastavitve, vaša pravila po aplikaciji, predpomnilnik prevodov Asistiranega branja (izbrisan ob koncu vsake seje). Nič od tega se ne pošilja na naše strežnike.

---

## 4. Glasovno narekovanje

Gumb z mikrofonom vam omogoča, da narekujete, namesto da tipkate. Dovoljenje za dostop do mikrofona se zahteva **prav v trenutku, ko pritisnete ta gumb**, nikoli ob zagonu, in mikrofon se odpre le v tistem trenutku. Plume nikoli ne posluša v ozadju.

**Plume ne prejema, ne shranjuje in ne prenaša nobenega zvočnega posnetka.** Narekovanje je zaupano sistemu za prepoznavanje govora, vgrajenemu v vaš telefon (Androidovemu). Plume prevzame le prepisano besedilo.

**Pomembno in pošteno pojasnilo:** ta sistemski pogon pripada vašemu telefonu, praviloma Googlu. Odvisno od vaše naprave, njenih nastavitev in nameščenih jezikovnih modulov **lahko zvok prenese na strežnike svojega izdajatelja**, da ga prepiše. Ta obdelava je zunaj dosega Plumea in je urejena s politiko zasebnosti izdajatelja vašega sistema. Zato ne moremo trditi, da vaš glas ostane na napravi — to je odvisno od vašega telefona, ne od nas.

Če dovoljenje za mikrofon zavrnete, vnos s tipkovnico seveda ostane na voljo.

---

## 5. Oglaševanje

Storitev je brezplačna v okviru določene dnevne omejitve uporabe. Nad njo lahko **izberete**, da si ogledate nagrajeni oglas in tako odklenete dodatne uporabe. To ni nikoli vsiljeno: če oglasa ne gledate, preprosto obdržite tisto, do česar ste upravičeni.

- Oglase zagotavlja **Google AdMob**.
- Pojavljajo se **izključno v sami aplikaciji Plume**, nikoli v lebdeči kapsuli in nikoli čez drugo aplikacijo.
- **Naročniki ne vidijo nobenega oglasa.**
- V Evropskem gospodarskem prostoru, Združenem kraljestvu in Švici se vam **pred prvim oglasom** prikaže obrazec za privolitev, ki ga zagotavlja platforma s certifikatom Googla. Dokler vaša izbira ni pridobljena, se ne zahteva noben oglas. Če zavrnete, oglasi ostanejo **neprilagojeni** in **nobena funkcionalnost vam ni odvzeta**. To izbiro lahko kadar koli spremenite v nastavitvah.
- Da se vam nagrada zanesljivo pripiše, se identifikator vaše naprave v Plumeu prenese AdMobu. Google lahko poleg tega zbira svoje podatke v skladu s svojo politiko zasebnosti.

*Na dan pisanja tega dokumenta je prikazovanje oglasov izklopljeno na strežniku. Ta razdelek opisuje delovanje od trenutka, ko bo vklopljeno.*

---

## 6. Naročnine in nakupi

Naročnine in paketi se prodajajo **prek Google Play**. Vaših bančnih podatkov nikoli ne vidimo: obdeluje jih Google, ki je prodajalec v smislu zaračunavanja.

Od Googla prejmemo dokazilo o nakupu, ki ga naš strežnik preveri, in o njem hranimo sled (identifikator transakcije, datumi, stanje). Ta sled se hrani iz računovodskih razlogov in zato, da isti nakup ne bi bil uporabljen dvakrat — vendar se **loči od vaše identitete**, ko izbrišete svoj račun.

---

## 7. Vaše pravice

Imate pravice do dostopa, popravka, izbrisa, omejitve obdelave, ugovora in prenosljivosti podatkov, ki jih določa Splošna uredba o varstvu podatkov (GDPR).

**Najpreprosteje in najhitreje: izbris je vgrajen v aplikacijo.**
Nastavitve → Zasebnost → Izbriši moje podatke. Izvede se **takoj**, ne uvrsti se v čakalno vrsto. Podrobnosti o tem, kaj se izbriše in kaj se ohrani, so na naši posebni strani: `https://readit0.github.io/plume-legal/suppression-compte`.

Račun lahko izbrišete tudi **brez namestitve aplikacije**, tako da pišete na sogacmoi7@gmail.com.

Za vsako drugo zahtevo pišite na **sogacmoi7@gmail.com**. Odgovorimo v enem mesecu.

**Pravne podlage:** izvajanje pogodbe (zagotavljanje storitve, ki jo zahtevate, upravljanje vaše naročnine), vaša privolitev (storitev za dostopnost, zajem zaslona, pošiljanje Umetni inteligenci v oblaku, prilagojeno oglaševanje), naš zakoniti interes (varnost, boj proti goljufijam) in naše zakonske obveznosti (računovodstvo).

Pritožbo lahko vložite pri organu **CNIL** (www.cnil.fr), nadzornem organu izdajatelja, ali, **če prebivate v Evropski uniji**, pri nadzornem organu svoje države prebivališča — člen 77 Splošne uredbe o varstvu podatkov vam pušča izbiro.

---

## 8. Mladoletniki

Plume je orodje za pomoč pri pisanju, namenjeno občinstvu, **staremu 16 let in več**. Zavestno ne zbiramo podatkov otrok, mlajših od 16 let, in aplikacija zanje ni niti zasnovana niti oglaševana. Če imate roditeljsko pravico in menite, da nam je vaš otrok posredoval podatke, pišite na sogacmoi7@gmail.com: račun bomo izbrisali.

Ker aplikacija omogoča preoblikovanje prostega besedila in prikazuje oglase, ni upravičena do programov Google Play, namenjenih družinam.

---

## 9. Obdelovalci in prejemniki

| Ponudnik | Vloga | Kje |
|---|---|---|
| **Supabase** | Gostovanje podatkovne baze, preverjanje pristnosti, strežniške funkcije | Evropska unija (Frankfurt) |
| **OpenRouter** | Usmerjanje zahtev do modela umetne inteligence | **Zunaj Evropske unije** |
| **Mistral AI** (prek OpenRouterja) | Model, ki obdela besedilo (Mistral Small) | Obdelava prek zgoraj navedenega posrednika |
| **Google Play / Google Billing** | Plačilo, naročnine | Google Ireland / Združene države |
| **Google AdMob** | Nagrajeno oglaševanje | Google Ireland / Združene države |
| **Google (sistemske storitve telefona)** | Prepoznavanje govora, moduli za prevajanje brez povezave | Odvisno od vaše naprave |

**Nobenih podatkov ne prodajamo in jih ne odstopamo posrednikom s podatki.**

**Prenosi zunaj Evropske unije:** uporaba OpenRouterja, Google Play in AdMoba pomeni prenos podatkov zunaj Evropske unije. Pravni okvir teh prenosov (standardne pogodbene klavzule, sklep o ustreznosti) **mora pred objavo preveriti in dokumentirati strokovnjak** — glejte opombo na koncu dokumenta.

---

## 10. Varnost

Izmenjava med aplikacijo in našimi strežniki je šifrirana (HTTPS/TLS). Dostop do podatkov v bazi je omejen s strežniškimi pravili: občutljive funkcije iz aplikacije niso dosegljive. Noben sistem ni popolnoma varen, vendar se nobeno besedilo, ki ga preoblikujete, pri nas ne shrani — kar mehansko omejuje to, kar bi vdor lahko razkril.

---

## 11. Spremembe

Vsaka sprememba te politike bo objavljena na naslovu `https://readit0.github.io/plume-legal` z novim datumom. Ob pomembni spremembi glede kroženja vaših podatkov vas bomo o tem obvestili v aplikaciji.

---

## Splošni pogoji

Pogoji uporabe storitve (kvote, naročnine, odpoved) so v ločenem dokumentu: `https://readit0.github.io/plume-legal/conditions-generales`.

---

> ### V pregled strokovnjaku
>
> Ta dokument je bil napisan z merjenjem dejanskega vedenja aplikacije, vendar **ga ni napisal pravnik**. Štiri točke prednostno zaslužijo strokovno mnenje:
>
> 1. **Prenos podatkov zunaj Evropske unije** k OpenRouterju. To je najobčutljivejša točka: treba je določiti veljavni mehanizem prenosa, preveriti, ali s tem ponudnikom obstaja pogodba o obdelavi, in to zapisati sem. Dokler to ni storjeno, ta dokument prenos opisuje, ne da bi trdil, da je pravno urejen.
> 2. **Pravne podlage**, navedene v §7, zlasti razdelitev med privolitvijo in zakonitim interesom za storitev za dostopnost.
> 3. **Najnižja starost** (16 let) in njena skladnost z vprašalnikom za razvrstitev vsebine v Google Play.
> 4. **Navedba glede umetne inteligence** na podlagi evropske uredbe o umetni inteligenci (obveznost preglednosti za sistem z omejenim tveganjem).

---

Ta dokument je prevod francoske različice, ki je na voljo na naslovu https://readit0.github.io/plume-legal/. Na voljo je za vašo informacijo. V primeru odstopanj nam pišite na sogacmoi7@gmail.com.
