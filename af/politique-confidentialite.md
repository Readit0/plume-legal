# Plume se privaatheidsbeleid

**Laas bygewerk: 31 Julie 2026** — Weergawe 1.0

---

## Wie is die verantwoordelike party vir jou inligting

**SASU RedLine Music**
SIREN 938 277 100 — SIRET `938 277 100 00013`
Abbaye 208-1, 208 Résidence Lavoisier, 18100 Vierzon, France
Kontak: sogacmoi7@gmail.com

Die app word op Google Play uitgegee onder die uitgewersnaam **openfunword**.

Hierdie beleid beskryf wat die Plume-app in sy huidige weergawe doen. Dit is geskryf deur die app se kode te lees, nie uit 'n generiese sjabloon nie.

---

## In een minuut

Plume help jou om te skryf: dit herformuleer jou teks direk in die app waarin jy besig is om te tik, en dit kan teks vertaal wat op die skerm vertoon word.

Drie dinge om te onthou:

1. **Plume bewaar geen van jou tekste op sy bedieners nie.** Nie jou herformuleerde tekste nie, en ook nie die teks wat van die skerm gelees word nie. Ons hou nóg 'n kopie nóg 'n logboek daarvan.
2. **Na gelang van die enjin wat jy kies, verlaat jou teks jou foon — of nie.** Twee enjins (die plaaslike stel en die plaaslike KI) werk heeltemal op die toestel. Die derde (die wolk-KI) stuur die teks na 'n diens vir kunsmatige intelligensie **wat buite die Europese Unie geleë is**. Jy kies, en die wolk-KI word nooit sonder jou uitdruklike toestemming geaktiveer nie.
3. **Plume het kragtige toestemmings nodig** (om die inhoud te lees wat in ander programme vertoon word, en om die skerm op te neem). Hieronder verduidelik ons presies waarvoor hulle dien en waarvoor hulle nie dien nie.

---

## 1. Wat Plume op jou skerm lees, en wanneer

### 1.1 Die toeganklikheidsdiens

Om jou teks te herskryf op die plek waar jy dit skryf, gebruik Plume Android se toeganklikheidsdiens. Dit is 'n toestemming wat jy self aanskakel, in die foon se instellings, ná 'n verduidelikingskerm wat Plume jou wys **voordat** dit daarvoor vra.

Konkreet:

- **In rus** weet Plume slegs watter app oop is en op watter oomblik jy die wyser in 'n invoerveld plaas. Dit is wat die swewende kapsule laat verskyn — en slegs in die programme wat jy self opgestel het.
- **Die inhoud van die veld word eers gelees op die presiese oomblik wanneer jy die kapsule raak**, om herskryf en dan ter plaatse vervang te word.
- **Wagwoordvelde word uitgesluit.** Die app bespeur velde van die wagwoordtipe (ook syferkodes en webvelde) en weier om hulle te lees.
- Hierdie toestemming **maak geen beeldopname van jou skerm moontlik nie**.
- Plume **druk nooit in jou plek** in 'n ander app nie: dit vervang die teks van 'n veld, niks anders nie.

Twee funksies wat jy self aanskakel — **Ondersteunde Lees in Teksmodus** en die **vertaling van ontvangde boodskappe** — lees die vertoonde teks deurlopend solank hulle loop, en hou op sodra jy hulle afskakel.

As jy die toeganklikheidsdiens weier, bly Plume bruikbaar: jy kan 'n teks merk en deur die “Plume”-item in Android se seleksiekieslys gaan, of 'n teks na Plume deel.

### 1.2 Die skermopname (Ondersteunde Lees)

Ondersteunde Lees plaas 'n vertaling bo-oor die vertoonde teks — byvoorbeeld die spraakborrels van 'n strokiesprent. Dit moet die beeld van die skerm kan sien.

- Dit is **by verstek afgeskakel** en werk slegs in die programme wat jy uitdruklik toegelaat het, een vir een.
- **Android vra sy eie toestemming elke keer wanneer 'n sessie begin.** Dit is nie 'n toestemming wat een keer vir altyd gegee word nie: elke sessie vereis 'n nuwe toestemming. Plume probeer nooit om hierdie toestemming te hergebruik of te omseil nie.
- Deur die hele sessie **bly 'n permanente kennisgewing en 'n stelselaanwyser sigbaar**. Plume kan nie jou skerm stilweg opneem nie.
- Die sessie **stop outomaties wanneer die skerm sluit**, en onmiddellik wanneer jy dit self stop.
- Programme wat hulle vertoning beskerm (bankprogramme, wagwoordbestuurders) word **deur Android self verduister** voordat Plume enigiets ontvang. Dit is 'n beskerming van die stelsel, werklik maar gedeeltelik: nie alle sensitiewe programme skakel dit aan nie. Ons stel dit dus nie as 'n absolute waarborg voor nie.
- **Die vasgelegde beelde word nooit gestoor of gestuur nie.** Elke beeld word in die geheue ontleed om die teks daaruit te haal, en word dan laat vaar. Geen beeld verlaat jou foon nie, nooit nie, ongeag die enjin wat gekies is.

---

## 2. Wat op jou foon bly en wat weggaan

Dit is die belangrikste onderskeid in hierdie beleid, en dit is jy wat dit beheer.

### 2.1 Die enjins wat niks uitstuur nie

- **Die plaaslike stel** (herkenning en vertaling van teks vanlyn) werk heeltemal op die toestel.
- **Die plaaslike KI** is 'n model vir kunsmatige intelligensie wat een keer afgelaai en daarna op jou foon gestoor word (ongeveer 720 MB). Dit loop op jou toestel.

Met hierdie twee enjins **verlaat die teks wat gelees of herformuleer word, nie jou foon nie.** Daar is geen netwerkoproep wat met die inhoud van jou teks verband hou nie.

### 2.2 Die wolk-KI-enjin

Wanneer jy die wolk-KI kies, of wanneer jou toestel nie kragtig genoeg is vir die plaaslike KI nie, word die betrokke teks na ons bedieners gestuur, en daarna na 'n derdeparty-diens vir kunsmatige intelligensie.

**Ons moet duidelik wees oor die werklike roete:**

- Die teks gaan deur ons infrastruktuur (Supabase), wat in die **Europese Unie** gehuisves word (die streek Sentraal-Europa, Frankfort).
- Dit word daarna na **openrouter.ai** gestuur, 'n roeteringstussenganger **wat buite die Europese Unie geleë is**, wat dit deur die model **Mistral Small** laat verwerk.
- **Dit gaan dus om 'n oordrag van data buite die Europese Unie.** Ons beweer nie die teendeel nie, en ons maak geen belofte van Europese huisvesting vir hierdie stap nie.
- **Plume bewaar nie jou teks nie.** Geen van ons bedienerfunksies skryf die inhoud van jou teks neer nie: ons teken slegs 'n tegniese versoekidentifiseerder en die identifiseerder van jou toestel aan, om jou kwota te tel en misbruik op te spoor.
- **Wat hierdie diensverskaffers aan hulle kant doen, kan ons nie waarborg nie.** Ons verkies om dit vir jou te sê eerder as om jou 'n nulbewaring te belowe wat ons nie in staat is om na te gaan nie.

**Die wolk-KI skakel nooit vanself aan nie.** 'n Toegewyde toestemmingskerm verduidelik hierdie punte aan jou voor die eerste versending, en niks gaan weg voordat jy aanvaar het nie. As die plaaslike KI misluk, skakel Plume nie stilweg oor na die wolk nie: dit laat jou weet en wag op jou besluit. Jy kan hierdie toestemming enige tyd in die instellings herroep.

Die teks wat gestuur word, het 'n boonste grens: 1 200 karakters vir 'n herformulering, 4 000 karakters vir 'n skermontleding.

---

## 3. Die data wat ons bewaar

Ons gebruik **geen hulpmiddel vir gehoorontleding, geen advertensiespoorder van 'n derde party en geen hulpmiddel vir ineenstortingsverslae nie**. Die app bevat geen meet-SDK nie.

Hier is alles wat op ons bedieners gestoor word:

| Data | Waarvoor | Hoe lank |
|---|---|---|
| **Toestelidentifiseerder** ('n ewekansige nommer wat Plume genereer, sonder verband met jou identiteit of met 'n advertensie-ID) | Om 'n toestel aan 'n rekening te koppel, die kwotas toe te pas, misbruik te blokkeer | Tot jou rekening geskrap word |
| **Die rekening se e-posadres** (as jy 'n rekening met e-pos of via Google skep) | Om jou te verifieer, om jou intekening te koppel | Tot jou rekening geskrap word |
| **Gebruikstellers** (die aantal herformulerings per dag en per maand — getalle, nie tekste nie) | Om die kwotas toe te pas | Tot jou rekening geskrap word |
| **Aankoopgeskiedenis** (Google Play-transaksie-identifiseerder, datums, die intekening se status) | Om jou toegang te gee tot dit waarvoor jy betaal het, om hernuwings te bestuur, om ons rekeningkundige verpligtinge na te kom | Word ook ná die skrapping van die rekening bewaar, maar **losgemaak van jou identiteit** (sien §6) |
| **Voorstelle wat vrywillig gestuur is** (as jy vir ons 'n persona-voorstel uit die app skryf) | Om die katalogus te verbeter. Hierdie voorstelle word nooit gepubliseer nie. | Tot jou rekening geskrap word |
| **Tegniese seine van misbruik** (herhaalde oorskrydings, mislukte integriteitskontrole — sonder enige teks) | Sekuriteit, bestryding van bedrog | Word van jou identiteit losgemaak wanneer die rekening geskrap word |
| **Taal en weergawe van die app** | Om die regte inhoud te lewer | Tot jou rekening geskrap word |

**Wat ons nie insamel nie:** jou naam, jou kontakte, jou ligging, jou adresboek, jou foto's, jou kalender, die geskiedenis van jou programme. Plume vra geen van hierdie toestemmings nie.

**Wat slegs op jou foon bly:** jou eie personas en hulle avatars, jou instellings, jou reëls per app, die vertaalkasgeheue van Ondersteunde Lees (wat aan die einde van elke sessie uitgevee word). Niks hiervan word na ons bedieners gestuur nie.

---

## 4. Stemdiktering

'n Mikrofoonknoppie laat jou toe om te dikteer in plaas van te tik. Die toestemming vir toegang tot die mikrofoon word gevra **op die presiese oomblik wanneer jy hierdie knoppie druk**, nooit met die begin nie, en die mikrofoon gaan slegs op daardie oomblik oop. Plume luister nooit in die agtergrond nie.

**Plume ontvang, stoor en stuur geen klankopname nie.** Die diktering word oorgelaat aan die spraakherkenningsenjin wat in jou foon ingebou is (dié van Android). Plume haal slegs die getranskribeerde teks.

**'n Belangrike en eerlike punt:** hierdie stelselenjin behoort aan jou foon, gewoonlik aan Google. Na gelang van jou toestel, sy instellings en die taalmodules wat geïnstalleer is, **kan dit die klank na sy uitgewer se bedieners stuur** om dit te transkribeer. Hierdie verwerking val buite Plume en val onder die privaatheidsbeleid van die uitgewer van jou stelsel. Ons kan dus nie beweer dat jou stem op die toestel bly nie — dit hang van jou foon af, nie van ons nie.

As jy die mikrofoon se toestemming weier, bly invoer met die sleutelbord vanselfsprekend beskikbaar.

---

## 5. Advertensies

Die diens is gratis binne 'n sekere gebruiksperk per dag. Daarbo kan jy **kies** om 'n beloningsadvertensie te kyk om bykomende gebruike te ontsluit. Dit word nooit afgedwing nie: as jy nie 'n advertensie kyk nie, behou jy eenvoudig dit waarop jy geregtig is.

- Die advertensies word deur **Google AdMob** verskaf.
- Hulle verskyn **slegs in die Plume-app self**, nooit in die swewende kapsule nie en nooit bo-oor 'n ander app nie.
- **Intekenaars sien geen advertensies nie.**
- In die Europese Ekonomiese Ruimte, die Verenigde Koninkryk en Switserland word 'n toestemmingsvorm van 'n platform wat deur Google gesertifiseer is aan jou voorgelê **voor die eerste advertensie**. Solank jou keuse nie ingewin is nie, word geen advertensie aangevra nie. As jy weier, bly die advertensies **niegepersonaliseerd** en **word geen funksie van jou weggeneem nie**. Jy kan enige tyd in die instellings op hierdie keuse terugkom.
- Om jou beloning betroubaar te krediteer, word jou Plume-toestelidentifiseerder na AdMob gestuur. Google kan boonop sy eie data insamel ooreenkomstig sy privaatheidsbeleid.

*Op die datum van skryf is die vertoning van advertensies aan die bedienerkant afgeskakel. Hierdie afdeling beskryf hoe dit werk sodra dit aangeskakel word.*

---

## 6. Intekeninge en aankope

Die intekeninge en die pakkette word **via Google Play** verkoop. Ons sien nooit jou bankbesonderhede nie: hulle word deur Google verwerk, wat die verkoper is in die sin van fakturering.

Ons ontvang van Google 'n aankoopbewys wat ons bediener verifieer, en ons bewaar 'n spoor daarvan (transaksie-identifiseerder, datums, status). Hierdie spoor word om rekeningkundige redes bewaar en om te verhoed dat dieselfde aankoop twee keer gebruik word — maar dit word **van jou identiteit losgemaak** wanneer jy jou rekening skrap.

---

## 7. Jou regte

Jy beskik oor die regte op toegang, regstelling, uitwissing, beperking van verwerking, beswaar en data-oordraagbaarheid wat deur die Algemene Databeskermingsregulasie (GDPR) voorsien word.

**Die eenvoudigste en die vinnigste: die skrapping is in die app ingebou.**
Instellings → Privaatheid → Skrap my data. Dit word **onmiddellik uitgevoer**, nie in 'n wagry geplaas nie. Die besonderhede van wat uitgevee word en wat bewaar word, verskyn op ons toegewyde bladsy: `https://readit0.github.io/plume-legal/suppression-compte`.

Jy kan ook jou rekening skrap **sonder om die app te installeer**, deur aan sogacmoi7@gmail.com te skryf.

Vir enige ander versoek, skryf aan **sogacmoi7@gmail.com**. Ons antwoord binne 'n maand.

**Regsgronde:** die uitvoering van die kontrak (om die diens te lewer wat jy vra, om jou intekening te bestuur), jou toestemming (die toeganklikheidsdiens, die skermopname, die versending na die wolk-KI, gepersonaliseerde advertensies), ons regmatige belang (sekuriteit, bestryding van bedrog) en ons wetlike verpligtinge (rekeningkunde).

Jy kan 'n klag by die **CNIL** (www.cnil.fr) indien, die toesighoudende owerheid van die uitgewer, of, **as jy in die Europese Unie woon**, by die toesighoudende owerheid van jou land van verblyf — artikel 77 van die GDPR laat die keuse aan jou.

---

## 8. Minderjariges

Plume is 'n hulpmiddel vir skryfwerk, bedoel vir 'n publiek van **16 jaar en ouer**. Ons samel nie wetend data van kinders onder 16 jaar in nie, en die app is nie vir hulle ontwerp of bemark nie. As jy die ouerlike gesag het en meen dat jou kind data aan ons gestuur het, skryf aan sogacmoi7@gmail.com: ons sal die rekening skrap.

Aangesien die app dit moontlik maak om vrye teks te herformuleer en advertensies vertoon, kom dit nie in aanmerking vir Google Play se programme vir gesinne nie.

---

## 9. Operateurs en ontvangers

| Diensverskaffer | Rol | Waar |
|---|---|---|
| **Supabase** | Huisvesting van die databasis, verifikasie, bedienerfunksies | Europese Unie (Frankfort) |
| **OpenRouter** | Roetering van die versoeke na die KI-model | **Buite die Europese Unie** |
| **Mistral AI** (via OpenRouter) | Model wat die teks verwerk (Mistral Small) | Verwerking via die tussenganger hierbo |
| **Google Play / Google Billing** | Betaling, intekeninge | Google Ireland / Verenigde State |
| **Google AdMob** | Beloningsadvertensies | Google Ireland / Verenigde State |
| **Google (die foon se stelseldienste)** | Spraakherkenning, vanlyn vertaalmodules | Na gelang van jou toestel |

**Ons verkoop geen data nie en dra geen data aan datamakelaars oor nie.**

**Oordragte buite die Europese Unie:** die gebruik van OpenRouter, Google Play en AdMob behels 'n oordrag van data buite die Europese Unie. Die regsraamwerk van hierdie oordragte (standaardkontrakbepalings, toereikendheidsbesluit) **moet deur 'n professionele persoon nagegaan en gedokumenteer word voor publikasie** — sien die nota aan die einde van die dokument.

---

## 10. Sekuriteit

Die uitruilings tussen die app en ons bedieners is geïnkripteer (HTTPS/TLS). Toegang tot die data in die databasis word deur bedienerreëls beperk: die sensitiewe funksies is nie vanuit die app toeganklik nie. Geen stelsel is volmaak veilig nie, maar geen teks wat jy herformuleer, word by ons gestoor nie — wat meganies beperk wat 'n inbraak sou kon onthul.

---

## 11. Wysigings

Enige wysiging van hierdie beleid sal by die adres `https://readit0.github.io/plume-legal` met 'n nuwe datum gepubliseer word. In die geval van 'n belangrike verandering aan die beweging van jou data, sal ons jou daarvan in die app in kennis stel.

---

## Algemene voorwaardes

Die voorwaardes vir die gebruik van die diens (kwotas, intekeninge, kansellasie) verskyn in 'n aparte dokument: `https://readit0.github.io/plume-legal/conditions-generales`.

---

> ### Om deur 'n professionele persoon nagegaan te word
>
> Hierdie dokument is geskryf deur die werklike gedrag van die app te meet, maar **dit is nie deur 'n regspraktisyn geskryf nie**. Vier punte verdien by voorkeur 'n professionele mening:
>
> 1. **Die oordrag van data buite die Europese Unie** na OpenRouter. Dit is die sensitiefste punt: die toepaslike oordragmeganisme moet bepaal word, daar moet nagegaan word of 'n verwerkingsooreenkoms met hierdie diensverskaffer bestaan, en dit moet hier geskryf word. Solank dit nie gedoen is nie, beskryf hierdie dokument die oordrag sonder om te beweer dat dit gereguleer is.
> 2. **Die regsgronde** wat in §7 gekies is, veral die verdeling tussen toestemming en regmatige belang vir die toeganklikheidsdiens.
> 3. **Die minimum ouderdom** (16 jaar) en die ooreenstemming daarvan met Google Play se vraelys vir inhoudsgradering.
> 4. **Die vermelding oor KI** ingevolge die Europese Unie se regulasie oor kunsmatige intelligensie (deursigtigheidsverpligting vir 'n stelsel met beperkte risiko).

---

Hierdie dokument is 'n vertaling van die Franse weergawe, wat by https://readit0.github.io/plume-legal/ beskikbaar is. Dit word vir jou inligting verskaf. Kontak ons by sogacmoi7@gmail.com indien jy 'n afwyking vind.
