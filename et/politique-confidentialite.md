# Plume'i privaatsuspoliitika

**Viimati uuendatud: 31. juuli 2026** — Versioon 1.0

---

## Kes vastutab teie andmete eest

**SASU RedLine Music**
SIREN 938 277 100 — SIRET `938 277 100 00013`
Abbaye 208-1, 208 Résidence Lavoisier, 18100 Vierzon, France
Kontakt: sogacmoi7@gmail.com

Rakendus on avaldatud Google Play poes väljaandja nime **openfunword** all.

Käesolev poliitika kirjeldab, mida rakendus Plume oma praeguses versioonis teeb. See on koostatud rakenduse koodi lugedes, mitte üldise näidise põhjal.

---

## Ühe minutiga

Plume aitab teil kirjutada: see sõnastab teie teksti ümber otse selles rakenduses, kuhu te parajasti kirjutate, ja oskab tõlkida ekraanil kuvatavat teksti.

Kolm asja, mida meeles pidada:

1. **Plume ei säilita ühtegi teie teksti oma serverites.** Ei teie ümbersõnastatud tekste ega ekraanilt loetud teksti. Me ei hoia neist ei koopiat ega logi.
2. **Sõltuvalt sellest, millise mootori te valite, kas teie tekst lahkub teie telefonist või mitte.** Kaks mootorit (kohalik komplekt ja kohalik tehisintellekt) töötavad täielikult seadmes. Kolmas (pilve-tehisintellekt) saadab teksti tehisintellekti teenusele, mis **asub väljaspool Euroopa Liitu**. Valiku teete teie ja pilve-tehisintellekt ei lülitu kunagi sisse ilma teie selgesõnalise nõusolekuta.
3. **Plume vajab võimsaid lubasid** (lugeda teistes rakendustes kuvatavat sisu, jäädvustada ekraani). Allpool selgitame täpselt, milleks need on ja milleks need ei ole.

---

## 1. Mida Plume teie ekraanilt loeb ja millal

### 1.1 Juurdepääsetavuse teenus

Selleks et teie teksti ümber kirjutada seal, kus te seda kirjutate, kasutab Plume Androidi juurdepääsetavuse teenust. Selle loa lubate te ise telefoni seadetes, pärast selgitavat ekraani, mille Plume teile näitab **enne** loa küsimist.

Konkreetselt:

- **Puhkeolekus** teab Plume ainult seda, milline rakendus on avatud ja millal te asetate kursori sisestusväljale. Just see toob nähtavale hõljuva kapsli — ja üksnes neis rakendustes, mille olete ise seadistanud.
- **Välja sisu loetakse ainult sel täpsel hetkel, kui te kapslit puudutate**, et see ümber kirjutada ja kohapeal asendada.
- **Paroolid on välistatud.** Rakendus tuvastab paroolitüüpi väljad (sealhulgas numbrilised koodid ja veebiväljad) ning keeldub neid lugemast.
- See luba **ei võimalda teie ekraanilt ühtki pilti jäädvustada**.
- Plume **ei vajuta kunagi teie eest** teises rakenduses: ta asendab välja teksti, ei midagi muud.

Kaks funktsiooni, mille lülitate ise sisse — **abistatud lugemine tekstirežiimis** ja **saabunud sõnumite tõlkimine** — loevad kuvatavat teksti pidevalt seni, kuni need töötavad, ja peatuvad kohe, kui te need välja lülitate.

Kui te juurdepääsetavuse teenusest keeldute, jääb Plume kasutatavaks: võite teksti valida ja kasutada Androidi valikumenüü käsku „Plume“ või jagada teksti Plume'ile.

### 1.2 Ekraani jäädvustamine (abistatud lugemine)

Abistatud lugemine kuvab tõlke kuvatava teksti peale — näiteks koomiksi kõnemullide kohale. Selleks peab ta nägema ekraani kujutist.

- See on **vaikimisi välja lülitatud** ja töötab ainult neis rakendustes, mille olete ükshaaval selgesõnaliselt lubanud.
- **Android küsib iga seansi alustamisel oma nõusolekut.** See ei ole üks kord ja lõplikult antud luba: iga seanss nõuab uut nõusolekut. Plume ei püüa kunagi seda nõusolekut taaskasutada ega sellest mööda minna.
- Kogu seansi vältel **jäävad nähtavaks püsiv teavitus ja süsteemi indikaator**. Plume ei saa teie ekraani märkamatult jäädvustada.
- Seanss **lõpeb automaatselt ekraani lukustamisel** ja kohe, kui te selle ise peatate.
- Rakendused, mis kaitsevad oma kuva (pangarakendused, paroolihaldurid), **varjab Android ise** enne, kui Plume midagi kätte saab. See on süsteemi kaitse, päris, kuid osaline: kõik tundlikud rakendused ei lülita seda sisse. Seetõttu ei esitle me seda absoluutse garantiina.
- **Jäädvustatud pilte ei salvestata ega saadeta kunagi.** Iga pilti analüüsitakse mälus, et sellest tekst välja lugeda, ja seejärel see hüljatakse. Ükski pilt ei lahku teie telefonist, mitte kunagi, olenemata valitud mootorist.

---

## 2. Mis jääb teie telefoni ja mis lahkub

See on käesoleva poliitika kõige olulisem eristus ja seda kontrollite teie.

### 2.1 Mootorid, mis midagi välja ei saada

- **Kohalik komplekt** (teksti tuvastamine ja tõlkimine võrguühenduseta) töötab täielikult seadmes.
- **Kohalik tehisintellekt** on tehisintellekti mudel, mis laaditakse ühe korra alla ja salvestatakse seejärel teie telefoni (umbes 720 MB). See töötab teie seadmes.

Nende kahe mootoriga **ei lahku loetud ega ümbersõnastatud tekst teie telefonist.** Teie teksti sisuga seotud võrgupäringuid ei tehta.

### 2.2 Pilve-tehisintellekti mootor

Kui valite pilve-tehisintellekti või kui teie seade ei ole kohaliku tehisintellekti jaoks piisavalt võimas, edastatakse asjaomane tekst meie serveritesse ja seejärel kolmanda isiku tehisintellekti teenusele.

**Tegeliku teekonna kohta tuleb olla selge:**

- Tekst liigub läbi meie taristu (Supabase), mida hostitakse **Euroopa Liidus** (Kesk-Euroopa piirkond, Frankfurt).
- Seejärel edastatakse see teenusele **openrouter.ai**, mis on marsruutimise vahendaja ja **asub väljaspool Euroopa Liitu** ning laseb teksti töödelda mudelil **Mistral Small**.
- **Tegemist on seega andmete edastamisega väljapoole Euroopa Liitu.** Me ei väida vastupidist ega esita selle etapi kohta ühtki lubadust Euroopas hostimise kohta.
- **Plume ei säilita teie teksti.** Ükski meie serverifunktsioon ei kirjuta teie teksti sisu: me salvestame ainult päringu tehnilise identifikaatori ja teie seadme identifikaatori, et lugeda teie kvooti ja tuvastada kuritarvitusi.
- **Mida need teenusepakkujad omalt poolt teevad, seda me ei saa tagada.** Eelistame seda teile öelda, selle asemel et lubada teile säilitamise puudumist, mida me ei ole võimelised kontrollima.

**Pilve-tehisintellekt ei lülitu kunagi ise sisse.** Eraldi nõusolekuekraan selgitab teile neid punkte enne esimest saatmist ja midagi ei lahku enne, kui olete nõustunud. Kui kohalik tehisintellekt ebaõnnestub, ei lülitu Plume vaikselt pilve peale: ta annab teile sellest märku ja ootab teie otsust. Võite selle nõusoleku igal ajal seadetes tagasi võtta.

Saadetaval tekstil on ülempiir: 1 200 tähemärki ümbersõnastuse puhul ja 4 000 tähemärki ekraanianalüüsi puhul.

---

## 3. Andmed, mida me säilitame

Me ei kasuta **ühtegi külastatavuse analüüsi tööriista, ühtegi kolmanda isiku reklaamijälgijat ega ühtegi tõrketeadete tööriista**. Rakendus ei sisalda mõõtmis-SDK-d.

Siin on kõik, mis meie serverites talletatakse:

| Andmed | Milleks | Kestus |
|---|---|---|
| **Seadme identifikaator** (Plume'i loodud juhuslik number, millel puudub seos teie isikuga ega reklaamiidentifikaatoriga) | Siduda seade kontoga, rakendada kvoote, blokeerida kuritarvitusi | Kuni teie konto kustutamiseni |
| **Konto e-posti aadress** (kui loote konto e-posti teel või Google'i kaudu) | Teid autentida, siduda teie tellimus | Kuni teie konto kustutamiseni |
| **Kasutusloendurid** (ümbersõnastuste arv päevas ja kuus — numbrid, mitte tekstid) | Rakendada kvoote | Kuni teie konto kustutamiseni |
| **Ostuajalugu** (Google Play tehingu identifikaator, kuupäevad, tellimuse olek) | Anda teile juurdepääs sellele, mille eest olete maksnud, hallata pikendamisi, täita meie raamatupidamiskohustusi | Säilitatakse ka pärast konto kustutamist, kuid **teie isikust lahutatuna** (vt § 6) |
| **Vabatahtlikult saadetud ettepanekud** (kui saadate meile rakendusest persona ettepaneku) | Kataloogi täiendamiseks. Neid ettepanekuid ei avaldata kunagi. | Kuni teie konto kustutamiseni |
| **Kuritarvituse tehnilised signaalid** (korduvad ületamised, terviklikkuse kontrolli ebaõnnestumine — ilma ühegi tekstita) | Turvalisus, pettusevastane võitlus | Konto kustutamisel teie isikust lahutatud |
| **Rakenduse keel ja versioon** | Õige sisu edastamiseks | Kuni teie konto kustutamiseni |

**Mida me ei kogu:** teie nime, teie kontakte, teie asukohta, teie aadressiraamatut, teie fotosid, teie kalendrit, teie rakenduste ajalugu. Plume ei küsi ühtegi neist lubadest.

**Mis jääb üksnes teie telefoni:** teie kohandatud personad ja nende avatarid, teie seaded, teie rakendusepõhised reeglid, abistatud lugemise tõlkevahemälu (kustutatakse iga seansi lõpus). Midagi sellest ei saadeta meie serveritesse.

---

## 4. Häälsisestus

Mikrofoninupp võimaldab teil tippimise asemel dikteerida. Mikrofoni kasutamise luba küsitakse **täpselt sel hetkel, kui te seda nuppu vajutate**, mitte kunagi käivitamisel, ja mikrofon avaneb ainult sel hetkel. Plume ei kuula kunagi taustal.

**Plume ei võta vastu, ei salvesta ega edasta ühtegi helisalvestist.** Dikteerimine antakse üle teie telefoni sisseehitatud kõnetuvastusmootorile (Androidi omale). Plume saab kätte ainult transkribeeritud teksti.

**Oluline ja aus märkus:** see süsteemimootor kuulub teie telefonile, tavaliselt Google'ile. Sõltuvalt teie seadmest, selle seadetest ja paigaldatud keelemoodulitest **võib see saata heli oma väljaandja serveritesse**, et see transkribeerida. See töötlemine ei ole Plume'i kontrolli all ja sellele kohaldub teie süsteemi väljaandja privaatsuspoliitika. Seetõttu ei saa me kinnitada, et teie hääl jääb seadmesse — see sõltub teie telefonist, mitte meist.

Kui te mikrofoni luba ei anna, jääb klaviatuuriga sisestamine muidugi alles.

---

## 5. Reklaam

Teenus on tasuta teatava päevase kasutuspiirini. Selle ületamisel võite **valida**, kas vaadata preemiareklaami, et avada lisakasutuskordi. Seda ei suruta kunagi peale: kui te reklaami ei vaata, säilitate lihtsalt selle, millele teil on õigus.

- Reklaame pakub **Google AdMob**.
- Need ilmuvad **üksnes Plume'i rakenduses endas**, mitte kunagi hõljuvas kapslis ega teise rakenduse peal.
- **Tellijad ei näe ühtegi reklaami.**
- Euroopa Majanduspiirkonnas, Ühendkuningriigis ja Šveitsis kuvatakse teile **enne esimest reklaami** Google'i sertifitseeritud platvormi pakutav nõusolekuvorm. Kuni teie valikut ei ole saadud, ei küsita ühtegi reklaami. Kui te keeldute, jäävad reklaamid **isikupärastamata** ja **teilt ei võeta ära ühtegi funktsiooni**. Võite selle valiku igal ajal seadetes ümber teha.
- Selleks et teie preemia usaldusväärselt krediteerida, edastatakse teie Plume'i seadme identifikaator AdMobile. Google võib lisaks koguda oma andmeid vastavalt oma privaatsuspoliitikale.

*Käesoleva dokumendi koostamise kuupäeval on reklaamide näitamine serveri poolelt välja lülitatud. Käesolev jaotis kirjeldab, kuidas see toimib, niipea kui see sisse lülitatakse.*

---

## 6. Tellimused ja ostud

Tellimusi ja pakette müüakse **Google Play kaudu**. Me ei näe kunagi teie pangaandmeid: neid töötleb Google, kes on arveldamise mõttes müüja.

Google'ilt saame ostutõendi, mida meie server kontrollib, ja säilitame sellest jälje (tehingu identifikaator, kuupäevad, olek). Seda jälge säilitatakse raamatupidamislikel põhjustel ja selleks, et sama ost ei saaks kaks korda kasutatud — kuid teie konto kustutamisel **lahutatakse see teie isikust**.

---

## 7. Teie õigused

Teil on isikuandmete kaitse üldmäärusega ette nähtud õigus tutvuda andmetega ning õigus nõuda andmete parandamist, kustutamist ja töötlemise piiramist, samuti õigus esitada vastuväiteid ja õigus andmete ülekandmisele.

**Kõige lihtsam ja kiirem: kustutamine on rakendusse sisse ehitatud.**
Seaded → Privaatsus → Kustuta minu andmed. See **käivitatakse kohe**, mitte ei panda ootejärjekorda. Üksikasjad selle kohta, mis kustutatakse ja mis säilitatakse, on meie eraldi lehel: `https://readit0.github.io/plume-legal/suppression-compte`.

Võite oma konto kustutada ka **ilma rakendust paigaldamata**, kirjutades aadressile sogacmoi7@gmail.com.

Kõigi muude taotluste puhul kirjutage aadressile **sogacmoi7@gmail.com**. Vastame ühe kuu jooksul.

**Õiguslikud alused:** lepingu täitmine (teie soovitud teenuse osutamine, teie tellimuse haldamine), teie nõusolek (juurdepääsetavuse teenus, ekraani jäädvustamine, saatmine pilve-tehisintellektile, isikupärastatud reklaam), meie õigustatud huvi (turvalisus, pettusevastane võitlus) ja meie juriidilised kohustused (raamatupidamine).

Teil on õigus esitada kaebus **CNIL-ile** (www.cnil.fr), kes on väljaandja järelevalveasutus, või, **kui te elate Euroopa Liidus**, oma elukohariigi järelevalveasutusele — isikuandmete kaitse üldmääruse artikkel 77 jätab valiku teile.

---

## 8. Alaealised

Plume on kirjutamise abivahend, mis on mõeldud **16-aastasele ja vanemale** kasutajale. Me ei kogu teadlikult alla 16-aastaste laste andmeid ning rakendust ei ole neile mõeldud ega neile ei turundata. Kui olete vanemliku vastutuse kandja ja arvate, et teie laps on meile andmeid edastanud, kirjutage aadressile sogacmoi7@gmail.com: kustutame konto.

Kuna rakendus võimaldab vaba teksti ümber sõnastada ja kuvab reklaami, ei sobi see Google Play peredele mõeldud programmidesse.

---

## 9. Volitatud töötlejad ja vastuvõtjad

| Teenusepakkuja | Roll | Kus |
|---|---|---|
| **Supabase** | Andmebaasi hostimine, autentimine, serverifunktsioonid | Euroopa Liit (Frankfurt) |
| **OpenRouter** | Päringute suunamine tehisintellekti mudelile | **Väljaspool Euroopa Liitu** |
| **Mistral AI** (OpenRouteri kaudu) | Mudel, mis teksti töötleb (Mistral Small) | Töötlemine ülalnimetatud vahendaja kaudu |
| **Google Play / Google Billing** | Makse, tellimused | Google Ireland / Ameerika Ühendriigid |
| **Google AdMob** | Preemiareklaam | Google Ireland / Ameerika Ühendriigid |
| **Google (telefoni süsteemiteenused)** | Kõnetuvastus, võrguühenduseta tõlkemoodulid | Sõltub teie seadmest |

**Me ei müü ühtegi andmet ega loovuta neid andmemaakleritele.**

**Edastamine väljapoole Euroopa Liitu:** OpenRouteri, Google Play ja AdMobi kasutamine tähendab andmete edastamist väljapoole Euroopa Liitu. Nende edastamiste õiguslik raamistik (lepingu tüüptingimused, kaitse piisavuse otsus) **tuleb enne avaldamist spetsialistil kontrollida ja dokumenteerida** — vt märkust dokumendi lõpus.

---

## 10. Turvalisus

Rakenduse ja meie serverite vaheline andmevahetus on krüpteeritud (HTTPS/TLS). Juurdepääsu andmebaasis olevatele andmetele piiravad serveripoolsed reeglid: tundlikud funktsioonid ei ole rakendusest ligipääsetavad. Ükski süsteem ei ole täiuslikult turvaline, kuid ühtegi teie ümbersõnastatud teksti meil ei säilitata — see piirab paratamatult seda, mida sissetung võiks paljastada.

---

## 11. Muudatused

Igast käesoleva poliitika muudatusest teatatakse aadressil `https://readit0.github.io/plume-legal` koos uue kuupäevaga. Kui teie andmete liikumises toimub oluline muudatus, teavitame teid sellest rakenduses.

---

## Üldtingimused

Teenuse kasutustingimused (kvoodid, tellimused, tühistamine) on esitatud eraldi dokumendis: `https://readit0.github.io/plume-legal/conditions-generales`.

---

> ### Spetsialistil üle vaadata
>
> Käesolev dokument on koostatud rakenduse tegelikku käitumist mõõtes, kuid **seda ei ole koostanud jurist**. Neli punkti vajavad eelisjärjekorras spetsialisti arvamust:
>
> 1. **Andmete edastamine väljapoole Euroopa Liitu** OpenRouterile. See on kõige tundlikum punkt: tuleb kindlaks määrata kohaldatav edastamismehhanism, kontrollida, kas selle teenusepakkujaga on sõlmitud andmetöötlusleping, ja see siia kirja panna. Kuni seda tehtud ei ole, kirjeldab käesolev dokument edastamist, väitmata, et see on õiguslikult reguleeritud.
> 2. **Õiguslikud alused**, mis on valitud § 7-s, eelkõige nõusoleku ja õigustatud huvi jaotus juurdepääsetavuse teenuse puhul.
> 3. **Vanuse alampiir** (16 aastat) ja selle kooskõla Google Play sisu klassifitseerimise küsimustikuga.
> 4. **Tehisintellekti käsitlev märge** Euroopa tehisintellekti määruse alusel (läbipaistvuskohustus piiratud riskiga süsteemi puhul).

---

Käesolev dokument on tõlge prantsuskeelsest versioonist, mis on kättesaadav aadressil https://readit0.github.io/plume-legal/. Tõlge on esitatud teile teadmiseks. Lahknevuste korral võtke meiega ühendust aadressil sogacmoi7@gmail.com.
