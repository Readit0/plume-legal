# Personvernerklæring for Plume

**Sist oppdatert: 12. september 2026** — Versjon 2.0

> *Hva som er endret siden versjon 1.0, og hvorfor du kanskje ser samtykkeskjermen på nytt i appen:* vi retter to påstander som ikke lenger stemte. For det første beholder funksjonen **personlige språk** innholdet du oppretter (navn, alfabet, ordforråd) på serverne våre — versjon 1.0 hevdet feilaktig at ingen tekst ble lagret. For det andre bruker vi nå et verktøy for **teknisk krasjrapportering** — versjon 1.0 hevdet at det ikke fantes noe slikt verktøy. Detaljene om disse to punktene finner du under «På ett minutt» nedenfor, samt i §3 og §9. Dette er nøyaktig de to kategoriene endringer som i appen utløser en ny samtykkeforespørsel (se §11).

---

## Hvem er behandlingsansvarlig for opplysningene dine

**SASU RedLine Music**
SIREN 938 277 100 — SIRET `938 277 100 00013`
Abbaye 208-1, 208 Résidence Lavoisier, 18100 Vierzon, France
Kontakt: sogacmoi7@gmail.com

Appen utgis på Google Play under utgivernavnet **openfunworld**.

Denne erklæringen beskriver hva appen Plume gjør i sin nåværende versjon. Den er skrevet ved å lese koden til appen, ikke ut fra en generisk mal.

---

## På ett minutt

Plume hjelper deg med å skrive: den omformulerer teksten din direkte i appen der du holder på å skrive, og den kan oversette tekst som vises på skjermen.

Tre ting å huske:

1. **Plume lagrer verken tekstene du omformulerer, eller teksten som leses på skjermen.** Vi beholder verken kopi eller logg av dem. **Et bevisst, og frivillig, unntak:** hvis du oppretter et **personlig språk** (ditt eget konstruerte språk, med et ordforråd av ord og deres definisjoner), blir innholdet i dette språket derimot lagret på serverne våre — det er den eneste måten å la deg finne det igjen på en annen enhet, videreutvikle det og dele det. Detaljene står i §3.
2. **Avhengig av motoren du velger, forlater teksten din telefonen — eller den gjør det ikke.** To motorer (det lokale settet og den lokale KI-en) arbeider utelukkende på enheten. Den tredje (sky-KI-en) sender teksten til en tjeneste for kunstig intelligens **som ligger utenfor Den europeiske union**. Du velger, og sky-KI-en slås aldri på uten ditt uttrykkelige samtykke.
3. **Plume trenger vidtrekkende tillatelser** (å lese innholdet som vises i andre apper, og å ta opp skjermen). Nedenfor forklarer vi nøyaktig hva de brukes til, og hva de ikke brukes til.

---

## 1. Hva Plume leser på skjermen din, og når

### 1.1 Tilgjengelighetstjenesten

For å skrive om teksten din der du skriver den, bruker Plume tilgjengelighetstjenesten i Android. Det er en tillatelse du selv slår på i innstillingene på telefonen, etter et forklaringsbilde som Plume viser deg **før** den ber om den.

Konkret:

- **I hvilemodus** vet Plume bare hvilken app som er åpen, og i hvilket øyeblikk du plasserer markøren i et skrivefelt. Det er dette som får den flytende kapselen til å dukke opp — og bare i de appene du selv har satt opp.
- **Innholdet i feltet leses først i det nøyaktige øyeblikket du trykker på kapselen**, for å bli skrevet om og deretter erstattet på stedet.
- **Passordfelt er utelukket.** Appen oppdager felt av passordtypen (også tallkoder og felt på nettsider) og nekter å lese dem.
- Denne tillatelsen **gir ingen mulighet til å ta bilde** av skjermen din.
- Plume **trykker aldri på dine vegne** i en annen app: den erstatter teksten i et felt, ingenting annet.

To funksjoner som du selv slår på — **Assistert lesing i tekstmodus** og **oversettelse av mottatte meldinger** — leser teksten som vises, fortløpende så lenge de kjører, og stopper straks du slår dem av.

Hvis du avslår tilgjengelighetstjenesten, kan Plume fortsatt brukes: du kan merke en tekst og gå via «Plume»-valget i utvalgsmenyen i Android, eller dele en tekst med Plume.

### 1.2 Skjermopptaket (Assistert lesing)

Assistert lesing legger en oversettelse oppå teksten som vises — for eksempel snakkeboblene i en tegneserie. Den må kunne se bildet av skjermen.

- Den er **slått av som standard** og virker bare i de appene du uttrykkelig har gitt tillatelse til, én for én.
- **Android ber om sitt eget samtykke hver gang en økt starter.** Dette er ikke en tillatelse som gis én gang for alle: hver økt krever et nytt samtykke. Plume forsøker aldri å gjenbruke eller omgå dette samtykket.
- Gjennom hele økten **er et fast varsel og en systemindikator synlige**. Plume kan ikke ta opp skjermen din i det skjulte.
- Økten **stopper automatisk når skjermen låses**, og umiddelbart når du selv stopper den.
- Apper som beskytter det de viser (bankapper, passordbehandlere), **skjules av Android selv** før Plume mottar noe som helst. Det er en beskyttelse i systemet, reell, men delvis: ikke alle følsomme apper slår den på. Vi fremstiller den derfor ikke som en absolutt garanti.
- **Bildene som tas opp, lagres aldri og sendes aldri.** Hvert bilde analyseres i minnet for å hente ut teksten, og forkastes deretter. Ikke ett bilde forlater telefonen din, aldri, uansett hvilken motor du har valgt.

---

## 2. Hva som blir igjen på telefonen din, og hva som går ut

Dette er det viktigste skillet i denne erklæringen, og det er du som styrer det.

### 2.1 Motorene som ikke sender noe ut

- **Det lokale settet** (gjenkjenning og oversettelse av tekst uten nett) fungerer utelukkende på enheten.
- **Den lokale KI-en** er en modell for kunstig intelligens som lastes ned én gang og deretter lagres på telefonen din (omtrent 720 MB). Den kjører på enheten din.

Med disse to motorene **forlater ikke teksten som leses eller omformuleres, telefonen din.** Det gjøres ingen nettverkskall knyttet til innholdet i teksten din.

### 2.2 Motoren sky-KI

Når du velger sky-KI-en, eller når enheten din ikke er kraftig nok til den lokale KI-en, sendes den aktuelle teksten til serverne våre og deretter til en tredjeparts tjeneste for kunstig intelligens.

**Vi må være tydelige på den faktiske ruten:**

- Teksten går gjennom serverinfrastrukturen vår, som driftes i **Den europeiske union** (regionen Sentral-Europa, Frankfurt).
- Den sendes deretter til et rutingmellomledd **som ligger utenfor Den europeiske union**, og som lar en kunstig intelligens-modell fra en tredjepart behandle den.
- **Det dreier seg altså om en overføring av opplysninger ut av Den europeiske union.** Vi hevder ikke noe annet, og vi gir ingen lovnad om europeisk drift for dette trinnet.
- **Plume lagrer ikke teksten din.** Ingen av serverfunksjonene våre skriver ned innholdet i teksten din: vi registrerer bare en teknisk forespørselsidentifikator og identifikatoren til enheten din, for å telle kvoten din og oppdage misbruk.
- **Hva disse leverandørene gjør på sin side, kan vi ikke garantere.** Vi sier det heller rett ut enn å love deg null lagring som vi ikke er i stand til å kontrollere.

**Sky-KI-en slår seg aldri på av seg selv.** Et eget samtykkebilde forklarer deg disse punktene før første sending, og ingenting går ut før du har godtatt. Hvis den lokale KI-en mislykkes, går ikke Plume over til skyen i stillhet: den gjør deg oppmerksom på det og venter på avgjørelsen din. Du kan når som helst trekke tilbake dette samtykket i innstillingene.

Teksten som sendes, har en øvre grense: 1 200 tegn for en omformulering, 4 000 tegn for en skjermanalyse.

---

## 3. Opplysningene vi lagrer

Vi bruker **ingen verktøy for publikumsanalyse og ingen tredjeparts annonsesporing**, bortsett fra reklamen som er beskrevet i §5. **Vi bruker et verktøy for teknisk krasjrapportering**: det ser bare programfeil (feiltype, teknisk kallstabel, appversjon, operativsystem), aldri hvordan du bruker appen eller hva du gjør i den, og aldri teksten du skriver — et eget filter forbyr dette før enhver sending. Detaljene står i §9.

Her er alt som lagres på serverne våre:

| Opplysning | Hvorfor | Hvor lenge |
|---|---|---|
| **Enhetsidentifikator** (et tilfeldig tall som Plume genererer, uten forbindelse til identiteten din eller til en annonse-ID) | Knytte en enhet til en konto, håndheve kvotene, blokkere misbruk | Til kontoen din slettes |
| **E-postadressen til kontoen** (hvis du oppretter en konto med e-post eller via Google) | Autentisere deg, knytte abonnementet ditt til kontoen | Til kontoen din slettes |
| **Brukstellere** (antall omformuleringer per dag og per måned — tall, ikke tekster) | Håndheve kvotene | Til kontoen din slettes |
| **Kjøpshistorikk** (transaksjonsidentifikator fra Google Play, datoer, status for abonnementet) | Gi deg tilgang til det du har betalt for, håndtere fornyelsene, oppfylle regnskapspliktene våre | Beholdes også etter at kontoen er slettet, men **løsrevet fra identiteten din** (se §6) |
| **Forslag du sender frivillig** (hvis du sender oss et forslag til en persona fra appen) | Forbedre katalogen. Disse forslagene offentliggjøres aldri. | Til kontoen din slettes |
| **Tekniske misbrukssignaler** (gjentatte overskridelser, mislykket integritetskontroll — uten noen tekst) | Sikkerhet, bekjempelse av svindel | Løsrives fra identiteten din når kontoen slettes |
| **Appens språk og versjon** | Levere riktig innhold | Til kontoen din slettes |
| **Innholdet i de personlige språkene du oppretter** (navnet, alfabetet og ordforrådet — ordene og definisjonene som du, eller andre personer, har skrevet inn i det) | La deg finne igjen språket ditt på en annen enhet, videreutvikle det, og dele det med andre brukere | Så lenge språket finnes. Hvis du sletter det, forsvinner oppføringen dets — men en kopi som allerede er **importert av en annen person**, tilhører da den personen og **overlever**, som en melding som allerede er mottatt av en tredjepart, og som vi ikke kan slette hos vedkommende |
| **Tekniske krasjrapporter** (feiltype, forkortet teknisk kallstabel, appversjon, operativsystem — aldri tekstinnhold) | Diagnostisere og rette krasj i appen | Reguleres av krasjrapporteringsleverandøren vår (se §9). Denne innsamlingen krever ditt samtykke og har en bryter vi når som helst kan slå av, uten en appoppdatering |

**Det vi ikke samler inn:** navnet ditt, kontaktene dine, posisjonen din, adresseboken din, bildene dine, kalenderen din, historikken over appene dine. Plume ber ikke om noen av disse tillatelsene.

**Det som blir igjen bare på telefonen din:** dine egne personaer og avatarene deres, innstillingene dine, reglene dine per app, oversettelsesmellomlageret til Assistert lesing (som tømmes ved slutten av hver økt). Ingenting av dette sendes til serverne våre.

---

## 4. Talediktering

En mikrofonknapp lar deg diktere i stedet for å skrive. Tillatelsen til mikrofonen blir bedt om **i det nøyaktige øyeblikket du trykker på denne knappen**, aldri ved oppstart, og mikrofonen åpnes bare i det øyeblikket. Plume lytter aldri i bakgrunnen.

**Plume mottar, lagrer og overfører ingen lydopptak.** Dikteringen overlates til talegjenkjenningsmotoren som er innebygd i telefonen din (Androids motor). Plume henter bare den transkriberte teksten.

**Et viktig og ærlig punkt:** denne systemmotoren tilhører telefonen din, som regel Google. Avhengig av enheten din, innstillingene dens og språkmodulene som er installert, **kan den sende lyden til serverne til utgiveren sin** for å transkribere den. Denne behandlingen ligger utenfor Plume og hører inn under personvernerklæringen til utgiveren av systemet ditt. Vi kan derfor ikke slå fast at stemmen din blir igjen på enheten — det avhenger av telefonen din, ikke av oss.

Hvis du avslår tillatelsen til mikrofonen, er det selvsagt fortsatt mulig å skrive på tastaturet.

---

## 5. Reklame

Tjenesten er gratis innenfor en viss bruksgrense per dag. Ut over dette kan du **velge** å se en belønnet annonse for å låse opp flere bruk. Det er aldri påtvunget: hvis du ikke ser en annonse, beholder du rett og slett det du har krav på.

- Annonsene leveres av **Google AdMob**.
- De vises **bare i selve Plume-appen**, aldri i den flytende kapselen og aldri oppå en annen app.
- **Abonnenter ser ingen reklame.**
- I Det europeiske økonomiske samarbeidsområdet, i Storbritannia og i Sveits får du presentert et samtykkeskjema fra en plattform som er sertifisert av Google, **før den første annonsen**. Så lenge valget ditt ikke er innhentet, blir det ikke bedt om noen annonse. Hvis du avslår, forblir annonsene **ikke-personaliserte**, og **ingen funksjon tas fra deg**. Du kan når som helst gjøre om dette valget i innstillingene.
- For å kunne godskrive belønningen din på en pålitelig måte, sendes Plume-enhetsidentifikatoren din til AdMob. Google kan for øvrig samle inn sine egne opplysninger i samsvar med sin personvernerklæring.

*På tidspunktet for skrivingen er annonsevisningen slått av på serversiden. Dette avsnittet beskriver hvordan det virker så snart den slås på.*

---

## 6. Abonnementer og kjøp

Abonnementene og pakkene selges **via Google Play**. Vi ser aldri betalingsopplysningene dine: de behandles av Google, som er selger i faktureringssammenheng.

Vi mottar fra Google et kjøpsbevis som serveren vår kontrollerer, og vi beholder et spor av det (transaksjonsidentifikator, datoer, status). Dette sporet beholdes av regnskapsmessige grunner og for å hindre at det samme kjøpet brukes to ganger — men det blir **løsrevet fra identiteten din** når du sletter kontoen din.

---

## 7. Rettighetene dine

Du har rett til innsyn, retting, sletting, begrensning av behandlingen, samt rett til å protestere og rett til dataportabilitet etter personvernforordningen (GDPR).

**Det enkleste og raskeste: slettingen er innebygd i appen.**
Innstillinger → Personvern → Slett dataene mine. Den **utføres umiddelbart**, den settes ikke i kø. Detaljene om hva som slettes og hva som beholdes, står på vår egen side: `https://readit0.github.io/plume-legal/suppression-compte`.

Du kan også slette kontoen din **uten å installere appen**, ved å skrive til sogacmoi7@gmail.com.

For enhver annen henvendelse, skriv til **sogacmoi7@gmail.com**. Vi svarer innen én måned.

**Behandlingsgrunnlag:** oppfyllelse av avtalen (å levere tjenesten du ber om, og å håndtere abonnementet ditt), samtykket ditt (tilgjengelighetstjenesten, skjermopptaket, sendingen til sky-KI-en, personalisert reklame), vår berettigede interesse (sikkerhet, bekjempelse av svindel) og våre rettslige forpliktelser (regnskap).

Du kan klage til **CNIL** (www.cnil.fr), som er tilsynsmyndigheten for utgiveren, eller, **hvis du bor i Den europeiske union**, til tilsynsmyndigheten i landet der du bor — artikkel 77 i personvernforordningen gir deg valget.

---

## 8. Mindreårige

Plume er et hjelpeverktøy for skriving, beregnet på et publikum **fra 16 år og oppover**. Vi samler ikke bevisst inn opplysninger om barn under 16 år, og appen er verken utformet eller markedsført for dem. Hvis du har foreldreansvar og tror at barnet ditt har gitt oss opplysninger, skriv til sogacmoi7@gmail.com: vi sletter kontoen.

Siden appen gjør det mulig å omformulere fri tekst og viser reklame, er den ikke kvalifisert for familieprogrammene i Google Play.

---

## 9. Databehandlere og mottakere

| Leverandør | Rolle | Hvor |
|---|---|---|
| **Hostingleverandøren vår** | Drift av databasen, autentisering, serverfunksjoner | Den europeiske union (Frankfurt) |
| **KI-behandlingsleverandøren vår** | Ruting av forespørslene og behandling av teksten med en kunstig intelligens-modell fra en tredjepart | **Utenfor Den europeiske union** |
| **Google Play / Google Billing** | Betaling, abonnementer | Google Ireland / USA |
| **Google AdMob** | Belønnet reklame | Google Ireland / USA |
| **Google (systemtjenestene på telefonen)** | Talegjenkjenning, oversettelsesmoduler uten nett | Avhengig av enheten din |
| **Krasjrapporteringsleverandøren vår** | Teknisk krasjrapportering — kun programfeil, filtrert før sending: aldri teksten din | USA |

**Vi selger ingen opplysninger og gir ingen opplysninger videre til datameglere.**

**Overføringer ut av Den europeiske union:** bruken av KI-behandlingsleverandøren vår, Google Play, AdMob og krasjrapporteringsleverandøren vår innebærer en overføring av opplysninger ut av Den europeiske union. De juridiske rammene for disse overføringene (standard personvernbestemmelser, beslutning om tilstrekkelig beskyttelsesnivå) **må kontrolleres og dokumenteres av en fagperson før publisering** — se merknaden sist i dokumentet.

---

## 10. Sikkerhet

Utvekslingene mellom appen og serverne våre er kryptert (HTTPS/TLS). Tilgangen til opplysningene i databasen er begrenset av serverregler: de følsomme funksjonene er ikke tilgjengelige fra appen. Ingen systemer er fullkomment sikre. Teksten du omformulerer, og teksten som Assistert lesing viser på skjermen, lagres ikke hos oss, noe som rent mekanisk begrenser hva et innbrudd kunne avsløre om dem. **Det gjelder ikke alt:** ordforrådet i de personlige språkene du oppretter, blir derimot lagret (se §3), og ville blitt eksponert som enhver annen opplysning i denne erklæringen ved et faktisk innbrudd — vi beskytter det med de samme serverreglene for tilgang som resten.

---

## 11. Endringer

Enhver endring av denne erklæringen vil bli publisert på adressen `https://readit0.github.io/plume-legal` med en ny dato. Ved en viktig endring i hvordan opplysningene dine beveger seg, informerer vi deg i appen.

**Siden versjon 2.0 har dette løftet en konkret mekanisme bak seg.** En enkel formrettelse (en dato, en adresse, en presisering) krever ikke noe mer av deg. Men en VESENTLIG endring — en ny mottaker av opplysningene dine, en ny kategori innsamlede opplysninger, et nytt formål, eller en endring av rettighetene dine eller av prisen — gjør at samtykkeskjermen i appen dukker opp på nytt, én gang, med et sammendrag av hva som endres og de to oppdaterte dokumentene. Det er nøyaktig det som har skjedd med denne versjon 2.0 (se boksen øverst i dette dokumentet).

---

## Generelle vilkår

Vilkårene for bruk av tjenesten (kvoter, abonnementer, oppsigelse) står i et eget dokument: `https://readit0.github.io/plume-legal/conditions-generales`.

---

---

Dette dokumentet er en oversettelse av den franske versjonen, som finnes på adressen https://readit0.github.io/plume-legal/. Den stilles til rådighet for din informasjon. Kontakt oss på sogacmoi7@gmail.com hvis du oppdager et avvik.
