# Personvernerklæringa til Plume

**Sist oppdatert: 12. september 2026** — Versjon 2.0

> *Kva som har endra seg sidan versjon 1.0, og kvifor du kanskje ser samtykkeskjermen igjen i appen:* Vi rettar no to påstandar som ikkje lenger stemte. For det første: funksjonen **eigne språk** lagrar innhaldet du lagar (namn, alfabet, ordliste) på serverane våre — versjon 1.0 hevda feilaktig at ingen tekst vart lagra. For det andre bruker vi no eit verktøy for **teknisk feilrapportering** — versjon 1.0 hevda at det ikkje fanst noko slikt verktøy. Detaljane om desse to punkta finn du under «På eitt minutt» nedanfor, og i §3 og §9. Dette er nøyaktig dei to typane endringar som i appen utløyser eit nytt samtykke (sjå §11).

---

## Kven som er ansvarleg for dataa dine

**SASU RedLine Music**
SIREN 938 277 100 — SIRET `938 277 100 00013`
Abbaye 208-1, 208 Résidence Lavoisier, 18100 Vierzon, France
Kontakt: sogacmoi7@gmail.com

Appen blir publisert på Google Play under utviklarnamnet **openfunworld**.

Denne erklæringa skildrar kva appen Plume gjer i den noverande versjonen. Ho er skriven ved å lese koden til appen, ikkje etter ein generisk mal.

---

## På eitt minutt

Plume hjelper deg å skrive: appen skriv om teksten din direkte i appen der du skriv, og han kan omsetje tekst som blir vist på skjermen.

Tre ting å hugse:

1. **Plume lagrar verken teksten du omformulerer, eller teksten som blir lesen på skjermen.** Vi tek verken vare på ein kopi eller ein logg. **Eit medvite og friviljug unntak:** Om du lagar eit **eige språk** (ditt eige konstruerte språk, med ei ordliste med ord og definisjonar), blir innhaldet i dette språket derimot **lagra** på serverane våre — det er den einaste måten å la deg finne det att på ein annan eining, vidareutvikle det og dele det. Detaljane finn du i §3.
2. **Alt etter kva motor du vel, forlèt teksten din telefonen din eller ikkje.** To motorar (Lokal-kit og Lokal AI) arbeider heilt på eininga. Den tredje (Sky-AI) sender teksten til ei teneste for kunstig intelligens **som ligg utanfor EU**. Du vel sjølv, og Sky-AI blir aldri aktivert utan uttrykkjeleg samtykke frå deg.
3. **Plume treng kraftige løyve** (å lese innhald som blir vist i andre appar, ta skjermbilete). Nedanfor forklarar vi nøyaktig kva dei blir brukte til, og kva dei ikkje blir brukte til.

---

## 1. Kva Plume les på skjermen din, og når

### 1.1 Tilgjengelegheitstenesta

For å skrive om teksten din der du skriv han, brukar Plume tilgjengelegheitstenesta i Android. Dette er eit løyve du sjølv aktiverer i innstillingane på telefonen, etter ein forklaringsskjerm som Plume viser deg **før** han blir spurd om.

Konkret:

- **I kvile** veit Plume berre kva app som er open og når du plasserer markøren i eit innskrivingsfelt. Det er dette som gjer at den flytande kapselen dukkar opp — og berre i appane du sjølv har sett opp.
- **Innhaldet i feltet blir berre lese i det nøyaktige augneblinken du trykkjer på kapselen**, for å bli omskrive og deretter bytt ut på staden.
- **Passordfelt er utelatne.** Appen oppdagar felt av typen passord (medrekna talkodar og webfelt) og nektar å lese dei.
- Dette løyvet gjev **ikkje høve til å ta bilete** av skjermen din.
- Plume **trykkjer aldri på dine vegner** i ein annan app: han byter berre ut teksten i eit felt, ikkje anna.

To funksjonar du sjølv aktiverer — **Assistert lesing i tekstmodus** og **omsetjing av mottekne meldingar** — les teksten som blir vist, kontinuerleg så lenge dei køyrer, og stoggar med det same du slår dei av.

Om du avslår tilgjengelegheitstenesta, kan Plume framleis brukast: du kan velje ut tekst og bruke «Plume»-menyen i Android sitt utvalsmeny, eller dele ein tekst til Plume.

### 1.2 Skjermbilete (Assistert lesing)

Assistert lesing legg ei omsetjing over teksten som blir vist — til dømes replikkboblene i ein teikneserie. Funksjonen treng å sjå biletet av skjermen.

- Han er **slått av som standard** og verkar berre i appar du uttrykkjeleg har godkjent, éin om gongen.
- **Android ber om sitt eige samtykke kvar gong ei økt startar.** Dette er ikkje eit løyve du gjev éin gong for alle: kvar økt krev eit nytt samtykke. Plume prøver aldri å gjenbruke eller omgå dette samtykket.
- Gjennom heile økta **held eit permanent varsel og ein systemindikator fram med å vere synlege.** Plume kan ikkje ta skjermbilete i det skjulte.
- Økta **stoggar automatisk når skjermen blir låst**, og med det same du sjølv stoggar han.
- Appar som vernar visinga si (bankappar, passordhandsamarar) blir **skjulte av Android sjølv** før Plume mottek noko som helst. Dette er eit systemvern, verkeleg men delvis: ikkje alle sensitive appar aktiverer det. Vi presenterer det difor ikkje som ein absolutt garanti.
- **Bileta som blir tekne, blir aldri lagra eller sende.** Kvart bilete blir analysert i minnet for å hente ut teksten, og deretter forkasta. Ingen bilete forlèt telefonen din, uansett kva motor du vel.

---

## 2. Kva som blir verande på telefonen din, og kva som forlèt han

Dette er det viktigaste skiljet i denne erklæringa, og det er du som kontrollerer det.

### 2.1 Motorane som ikkje sender noko ut

- **Lokal-kit** (offline tekstattkjenning og -omsetjing) verkar heilt på eininga.
- **Lokal AI** er ein kunstig intelligens-modell som blir lasta ned éin gong og deretter lagra på telefonen din (omtrent 720 MB). Han køyrer på eininga di.

Med desse to motorane **forlèt ikkje teksten som blir lesen eller omforma, telefonen din.** Det finst ingen nettverkskall knytt til innhaldet i teksten din.

### 2.2 Sky-AI-motoren

Når du vel Sky-AI, eller når eininga di ikkje er kraftig nok for Lokal AI, blir den aktuelle teksten sendt til serverane våre, og deretter til ei tredjeparts teneste for kunstig intelligens.

**Det er naudsynt å vere klar på den verkelege ferda:**

- Teksten går gjennom serverinfrastrukturen vår, som er verta i **EU** (regionen Sentral-Europa, Frankfurt).
- Han blir deretter sendt til ein rutingsformidlar **som ligg utanfor EU**, som let ein kunstig intelligens-modell frå ein tredjepart handsame han.
- **Det er difor snakk om ein overføring av data ut av EU.** Vi hevdar ikkje det motsette, og vi lovar ikkje europeisk vertskap for dette steget.
- **Plume lagrar ikkje teksten din.** Ingen av serverfunksjonane våre skriv innhaldet i teksten din: vi registrerer berre ein teknisk identifikator for førespurnaden og identifikatoren til eininga di, for å telje kvoten din og oppdage misbruk.
- **Kva desse leverandørane gjer på si side, kan vi ikkje garantere.** Vi føretrekkjer å fortelje deg dette framfor å love ein null-lagring vi ikkje er i stand til å kontrollere.

**Sky-AI blir aldri aktivert av seg sjølv.** Ein eigen samtykkeskjerm forklarar deg desse punkta før den første sendinga, og ingenting forlèt eininga før du har godteke. Om Lokal AI feilar, byter ikkje Plume stilt til skya: han varslar deg og ventar på avgjerda di. Du kan trekkje tilbake dette samtykket når som helst i innstillingane.

Teksten som blir sendt, er avgrensa: 1 200 teikn for ei omformulering, 4 000 teikn for ei skjermanalyse.

---

## 3. Dataa vi tek vare på

Vi bruker **ingen verktøy for publikumsanalyse og ingen tredjeparts annonsesporar** utanom annonseringa som er skildra i §5. **Vi bruker eit verktøy for teknisk feilrapportering**: det ser berre programfeil (type feil, teknisk kallstakk, appversjon, operativsystem), aldri korleis du brukar appen eller kva du gjer i han, og aldri teksten du skriv — eit eige filter hindrar det i å sende dette i det heile. Detaljane finn du i §9.

Her er alt som blir lagra på serverane våre:

| Data | Kvifor | Varigheit |
|---|---|---|
| **Einingsidentifikator** (eit tilfeldig nummer generert av Plume, utan samband til identiteten din eller ein annonseidentifikator) | Knyte ei eining til ein konto, handheve kvotar, blokkere misbruk | Til kontoen din blir sletta |
| **E-postadressa til kontoen** (om du lagar ein konto med e-post eller via Google) | Autentisere deg, knyte abonnementet ditt | Til kontoen din blir sletta |
| **Bruksteljarar** (talet på omformuleringar per dag og per månad — tal, ikkje tekst) | Handheve kvotar | Til kontoen din blir sletta |
| **Kjøpshistorikk** (transaksjonsidentifikator frå Google Play, datoar, status på abonnementet) | Gje deg tilgang til det du har betalt for, handtere fornyingar, oppfylle rekneskapsplikta vår | Blir teken vare på òg etter sletting av kontoen, men **fråkopla identiteten din** (sjå §6) |
| **Forslag sende friviljug** (om du skriv oss eit persona-forslag frå appen) | Betre katalogen. Desse forslaga blir aldri publiserte. | Til kontoen din blir sletta |
| **Tekniske signal om misbruk** (gjentekne overskridingar, feila integritetskontroll — utan nokon tekst) | Tryggleik, kamp mot svindel | Fråkopla identiteten din når kontoen blir sletta |
| **Språk og versjon av appen** | Levere rett innhald | Til kontoen din blir sletta |
| **Innhaldet i dei eigne språka du lagar** (namnet, alfabetet, og ordlista — orda og definisjonane du, eller andre, har skrive der) | La deg finne att språket ditt på ei anna eining, vidareutvikle det, og dele det med andre brukarar | Så lenge språket eksisterer. Om du slettar det, forsvinn kortet — men ein kopi som **allereie er importert av ein annan person**, høyrer no til han, og **held fram å eksistere**, som ei melding nokon andre allereie har motteke, som vi ikkje kan gå og slette hjå dei |
| **Tekniske feilrapportar** (type feil, avkorta teknisk kallstakk, appversjon, operativsystem — aldri innhald frå ein tekst) | Diagnostisere og rette feil i appen | Styrt av feilrapporteringsleverandøren vår (sjå §9). Denne innsamlinga krev samtykket ditt og ein brytar vi kan slå av når som helst, utan appoppdatering |

**Det vi ikkje samlar inn:** namnet ditt, kontaktane dine, plasseringa di, adresseboka di, bileta dine, kalenderen din, historikken til appane dine. Plume ber ikkje om nokon av desse løyva.

**Det som berre blir verande på telefonen din:** dei tilpassa personaane dine og avatarane deira, innstillingane dine, reglane dine per app, omsetjingsmellomlageret til Assistert lesing (blir sletta ved slutten av kvar økt). Ingenting av dette blir sendt til serverane våre.

---

## 4. Taleinnskriving

Ein mikrofonknapp lèt deg tale inn i staden for å skrive. Løyvet til mikrofontilgang blir spurt om **i det nøyaktige augneblinken du trykkjer på denne knappen**, aldri ved oppstart, og mikrofonen opnar seg berre i dette augneblinken. Plume lyttar aldri i bakgrunnen.

**Plume mottek, lagrar og sender aldri nokon lydopptak.** Taleinnskrivinga blir overlaten til talegjenkjenningsmotoren som er integrert i telefonen din (Android sin). Plume hentar berre den transkriberte teksten.

**Eit viktig og ærleg poeng:** denne systemmotoren høyrer til telefonen din, som regel Google. Alt etter eininga di, innstillingane hennar, og dei installerte språkmodulane, **kan han sende lyden til serverane til utgjevaren sin** for å transkribere han. Denne handsaminga går utanom Plume og fell inn under personvernerklæringa til utgjevaren av systemet ditt. Vi kan difor ikkje seie at stemma di blir verande på eininga — det kjem an på telefonen din, ikkje på oss.

Om du avslår løyvet til mikrofonen, er tastaturinnskriving sjølvsagt framleis tilgjengeleg.

---

## 5. Annonsering

Tenesta er gratis innanfor ei viss grense for bruk per dag. Utover det kan du **velje** å sjå ein premiert annonse for å låse opp fleire bruk. Dette er aldri påtvinga: om du ikkje ser ein annonse, held du berre fram med det du har rett til.

- Annonsane blir leverte av **Google AdMob**.
- Dei dukkar berre opp **inne i sjølve Plume-appen**, aldri i den flytande kapselen og aldri oppå ein annan app.
- **Abonnentar ser ingen annonsar.**
- I Det europeiske økonomiske samarbeidsområdet, i Storbritannia og i Sveits blir det vist deg eit samtykkeskjema frå ein Google-sertifisert plattform **før den første annonsen**. Så lenge valet ditt ikkje er registrert, blir det ikkje spurt etter nokon annonse. Om du avslår, held annonsane fram med å vere **ikkje-personaliserte**, og **ingen funksjon blir teken frå deg**. Du kan endre dette valet når som helst frå innstillingane.
- For å godskrive premien din på ein påliteleg måte blir Plume-einingsidentifikatoren din send til AdMob. Google kan elles samle inn sine eigne data i tråd med si eiga personvernerklæring.

*På skrivetidspunktet er annonsevisinga slått av på serversida. Denne delen skildrar korleis han verkar frå han blir slått på.*

---

## 6. Abonnement og kjøp

Abonnement og pakkar blir selde **via Google Play**. Vi ser aldri betalingsopplysningane dine: dei blir handsama av Google, som er seljaren i faktureringssamanheng.

Vi mottek frå Google eit kjøpsbevis som serveren vår kontrollerer, og vi tek vare på spora etter det (transaksjonsidentifikator, datoar, status). Desse spora blir tekne vare på av rekneskapsgrunnar og for å hindre at det same kjøpet blir brukt to gonger — men det blir **fråkopla identiteten din** når du slettar kontoen din.

---

## 7. Rettane dine

Du har rett til innsyn, retting, sletting, avgrensing, motsegn og dataportabilitet i tråd med GDPR.

**Det enklaste, og det raskaste: slettinga er integrert i appen.**
Innstillingar → Personvern → Slett dataa mine. Ho blir **utført med det same**, ikkje sett i kø. Detaljane om kva som blir sletta og kva som blir teke vare på, finn du på den eigne sida vår: `https://readit0.github.io/plume-legal/suppression-compte`.

Du kan òg slette kontoen din **utan å installere appen**, ved å skrive til sogacmoi7@gmail.com.

For alle andre førespurnadar, skriv til **sogacmoi7@gmail.com**. Vi svarar innan ein månad.

**Rettsleg grunnlag:** oppfylling av avtalen (levere tenesta du spør om, handtere abonnementet ditt), samtykket ditt (tilgjengelegheitsteneste, skjermbilete, sending til Sky-AI, personalisert annonsering), den rettkomne interessa vår (tryggleik, kamp mot svindel), og dei rettslege pliktene våre (rekneskap).

Du kan klage til **CNIL** (www.cnil.fr), tilsynsstyresmakta til utgjevaren, eller, **om du bur i EU**, til tilsynsstyresmakta i bustadlandet ditt — artikkel 77 i GDPR gjev deg dette valet.

---

## 8. Mindreårige

Plume er eit skriveverktøy meint for eit publikum **på 16 år og eldre**. Vi samlar ikkje medvite inn data frå mindreårige under 16 år, og appen er verken utforma eller marknadsført for dei. Om du har foreldreansvar og trur at barnet ditt har sendt oss data, skriv til sogacmoi7@gmail.com: vi vil slette kontoen.

Sidan appen let deg omformulere fri tekst og viser annonsar, er ho ikkje kvalifisert for familieprogramma til Google Play.

---

## 9. Underleverandørar og mottakarar

| Leverandør | Rolle | Kvar |
|---|---|---|
| **Vertsleverandøren vår** | Vertskap for databasen, autentisering, serverfunksjonar | EU (Frankfurt) |
| **AI-handsamingsleverandøren vår** | Ruting av førespurnadar og handsaming av teksten med ein kunstig intelligens-modell frå ein tredjepart | **Utanfor EU** |
| **Google Play / Google Billing** | Betaling, abonnement | Google Ireland / USA |
| **Google AdMob** | Premiert annonsering | Google Ireland / USA |
| **Google (systemtenester på telefonen)** | Talegjenkjenning, offline-omsetjingsmodular | Alt etter eininga di |
| **Feilrapporteringsleverandøren vår** | Teknisk feilrapportering — berre programfeil, filtrerte før sending: aldri teksten din | USA |

**Vi sel ingen data og gjev ingen data vidare til datameklarar.**

**Overføringar utanfor EU:** bruken av AI-handsamingsleverandøren vår, Google Play, AdMob og feilrapporteringsleverandøren vår inneber ein overføring av data ut av EU.

---

## 10. Tryggleik

Utvekslingane mellom appen og serverane våre er krypterte (HTTPS/TLS). Tilgangen til dataa i databasen er avgrensa av serverreglar: sensitive funksjonar er ikkje tilgjengelege frå appen. Ikkje noko system er fullstendig trygt. Teksten du omformulerer, og teksten som Assistert lesing viser på skjermen, blir ikkje lagra hjå oss, noko som strukturelt avgrensar kva eit innbrot kan avsløre om dei. **Dette gjeld ikkje alt:** ordlista til dei eigne språka du lagar, blir derimot **lagra** (sjå §3), og ville blitt eksponert som all anna data i denne erklæringa ved eit verkeleg innbrot — vi vernar henne med dei same serverreglane for tilgang som resten.

---

## 11. Endringar

Alle endringar i denne erklæringa blir publiserte på `https://readit0.github.io/plume-legal` med ny dato. Ved ei viktig endring i korleis dataa dine blir handsama, vil vi informere deg om det i appen.

**Sidan versjon 2.0 har dette løftet ein konkret mekanisme bak seg.** Ei enkel formell retting (ein dato, ei adresse, ei presisering) krev ingenting meir av deg. Men ei VESENTLEG endring — ein ny mottakar av dataa dine, ein ny kategori av data som blir samla inn, eit nytt føremål, eller ei endring av rettane dine eller prisen — får samtykkeskjermen til å dukke opp igjen éin gong i appen, med eit samandrag av kva som endrar seg, og dei to oppdaterte dokumenta. Det er nøyaktig det som har skjedd for denne versjon 2.0 (sjå boksen øvst i dette dokumentet).

---

## Bruksvilkår

Vilkåra for bruk av tenesta (kvotar, abonnement, oppseiing) finn du i eit eige dokument: `https://readit0.github.io/plume-legal/conditions-generales`.

---
