# Plumes privatlivspolitik

**Sidst opdateret: 31. juli 2026** — Version 1.0

---

## Hvem er dataansvarlig for dine oplysninger

**SASU RedLine Music**
SIREN 938 277 100 — SIRET `938 277 100 00013`
Abbaye 208-1, 208 Résidence Lavoisier, 18100 Vierzon, France
Kontakt: sogacmoi7@gmail.com

Appen udgives på Google Play under udgivernavnet **openfunworld**.

Denne politik beskriver, hvad appen Plume gør i sin nuværende version. Den er skrevet ved at læse appens kode, ikke ud fra en generisk skabelon.

---

## På et minut

Plume hjælper dig med at skrive: den omformulerer din tekst direkte i den app, hvor du er i gang med at skrive, og den kan oversætte tekst, der vises på skærmen.

Tre ting, du skal huske:

1. **Plume gemmer ingen af dine tekster på sine servere.** Hverken dine omformulerede tekster eller den tekst, der læses på skærmen. Vi beholder hverken kopi eller log.
2. **Afhængigt af den motor, du vælger, forlader din tekst din telefon — eller gør det ikke.** To motorer (det lokale kit og den lokale AI) arbejder udelukkende på enheden. Den tredje (Cloud-AI) sender teksten til en tjeneste for kunstig intelligens, **der ligger uden for Den Europæiske Union**. Du vælger, og Cloud-AI aktiveres aldrig uden dit udtrykkelige samtykke.
3. **Plume har brug for vidtgående tilladelser** (at læse det indhold, der vises i andre apps, og at optage skærmen). Vi forklarer nedenfor præcist, hvad de bruges til, og hvad de ikke bruges til.

---

## 1. Hvad Plume læser på din skærm, og hvornår

### 1.1 Tilgængelighedstjenesten

For at kunne omskrive din tekst dér, hvor du skriver den, bruger Plume Androids tilgængelighedstjeneste. Det er en tilladelse, du selv slår til i telefonens indstillinger, efter en forklaringsskærm, som Plume viser dig, **inden** den beder om den.

Konkret:

- **I hviletilstand** ved Plume kun, hvilken app der er åben, og på hvilket tidspunkt du placerer markøren i et indtastningsfelt. Det er dét, der får den flydende kapsel til at dukke op — og kun i de apps, du selv har konfigureret.
- **Indholdet i feltet læses først i det præcise øjeblik, hvor du rører kapslen**, for at blive omskrevet og derefter erstattet på stedet.
- **Adgangskodefelter er udelukket.** Appen registrerer felter af adgangskodetypen (også numeriske koder og webfelter) og nægter at læse dem.
- Denne tilladelse **giver ikke mulighed for at tage noget billede** af din skærm.
- Plume **trykker aldrig i dit sted** i en anden app: den erstatter teksten i et felt, intet andet.

To funktioner, som du selv slår til — **Assisteret læsning i teksttilstand** og **oversættelse af modtagne beskeder** — læser den viste tekst løbende, så længe de kører, og stopper, så snart du slår dem fra.

Hvis du afviser tilgængelighedstjenesten, kan Plume stadig bruges: du kan markere en tekst og gå via menupunktet »Plume« i Androids markeringsmenu, eller dele en tekst med Plume.

### 1.2 Skærmoptagelsen (Assisteret læsning)

Assisteret læsning lægger en oversættelse oven på den viste tekst — for eksempel talebobler i en tegneserie. Den har brug for at se billedet af skærmen.

- Den er **slået fra som standard** og virker kun i de apps, du udtrykkeligt har givet tilladelse til, én ad gangen.
- **Android beder om sit eget samtykke, hver gang en session startes.** Det er ikke en tilladelse, der gives én gang for alle: hver session kræver et nyt samtykke. Plume forsøger aldrig at genbruge eller omgå dette samtykke.
- Under hele sessionen **forbliver en permanent notifikation og en systemindikator synlige**. Plume kan ikke optage din skærm i det skjulte.
- Sessionen **stopper automatisk, når skærmen låses**, og øjeblikkeligt, når du selv stopper den.
- Apps, der beskytter deres visning (bankapps, adgangskodeadministratorer), **skjules af Android selv**, før Plume modtager noget som helst. Det er en beskyttelse i systemet, reel men delvis: ikke alle følsomme apps slår den til. Vi fremstiller den derfor ikke som en absolut garanti.
- **De optagne billeder gemmes aldrig og sendes aldrig.** Hvert billede analyseres i hukommelsen for at udtrække teksten og opgives derefter. Intet billede forlader din telefon, aldrig, uanset hvilken motor du har valgt.

---

## 2. Hvad der bliver på din telefon, og hvad der forlader den

Det er den vigtigste sondring i denne politik, og det er dig, der styrer den.

### 2.1 De motorer, der ikke sender noget ud

- **Det lokale kit** (genkendelse og oversættelse af tekst offline) fungerer udelukkende på enheden.
- **Den lokale AI** er en model for kunstig intelligens, der downloades én gang og derefter gemmes på din telefon (cirka 720 MB). Den kører på din enhed.

Med disse to motorer **forlader den tekst, der læses eller omformuleres, ikke din telefon.** Der foretages ingen netværkskald, der vedrører indholdet af din tekst.

### 2.2 Motoren Cloud-AI

Når du vælger Cloud-AI, eller når din enhed ikke er kraftig nok til den lokale AI, sendes den pågældende tekst til vores servere og derefter til en tredjeparts tjeneste for kunstig intelligens.

**Man skal være klar om den reelle vej:**

- Teksten passerer gennem vores infrastruktur (Supabase), der hostes i **Den Europæiske Union** (regionen Centraleuropa, Frankfurt).
- Den sendes derefter til **openrouter.ai**, en routingformidler, **der ligger uden for Den Europæiske Union**, som lader modellen **Mistral Small** behandle den.
- **Der er altså tale om en overførsel af oplysninger til et land uden for Den Europæiske Union.** Vi påstår ikke det modsatte, og vi giver ingen løfter om europæisk hosting for dette trin.
- **Plume gemmer ikke din tekst.** Ingen af vores serverfunktioner skriver indholdet af din tekst ned: vi registrerer kun en teknisk identifikator for anmodningen og identifikatoren for din enhed for at tælle din kvote og opdage misbrug.
- **Hvad disse leverandører gør på deres side, kan vi ikke garantere.** Vi foretrækker at sige det ligeud frem for at love dig en nulopbevaring, som vi ikke er i stand til at kontrollere.

**Cloud-AI aktiveres aldrig af sig selv.** En særlig samtykkeskærm forklarer dig disse punkter inden den første afsendelse, og intet sendes, før du har accepteret. Hvis den lokale AI slår fejl, skifter Plume ikke til skyen i stilhed: den gør dig opmærksom på det og venter på din beslutning. Du kan til enhver tid tilbagekalde dette samtykke i indstillingerne.

Den tekst, der sendes, har et loft: 1.200 tegn for en omformulering, 4.000 tegn for en skærmanalyse.

---

## 3. De oplysninger, vi gemmer

Vi bruger **intet værktøj til publikumsanalyse, ingen tredjeparts reklamesporing og intet værktøj til nedbrudsrapportering**. Appen indeholder intet måle-SDK.

Her er alt, hvad der gemmes på vores servere:

| Oplysning | Hvorfor | Hvor længe |
|---|---|---|
| **Enhedsidentifikator** (et tilfældigt tal, som Plume genererer, uden forbindelse til din identitet eller til et annonce-id) | Knytte en enhed til en konto, anvende kvoterne, blokere misbrug | Indtil din konto slettes |
| **Kontoens e-mailadresse** (hvis du opretter en konto med e-mail eller via Google) | Godkende dig, knytte dit abonnement | Indtil din konto slettes |
| **Forbrugstællere** (antal omformuleringer pr. dag og pr. måned — tal, ikke tekster) | Anvende kvoterne | Indtil din konto slettes |
| **Købshistorik** (transaktionsidentifikator fra Google Play, datoer, abonnementets status) | Give dig adgang til det, du har betalt for, håndtere fornyelserne, overholde vores bogføringsforpligtelser | Gemmes også efter kontoens sletning, men **løsrevet fra din identitet** (se §6) |
| **Forslag sendt frivilligt** (hvis du sender os et forslag til en persona fra appen) | Forbedre kataloget. Disse forslag offentliggøres aldrig. | Indtil din konto slettes |
| **Tekniske signaler om misbrug** (gentagne overskridelser, mislykket integritetskontrol af appen — uden nogen tekst) | Sikkerhed, bekæmpelse af svindel | Løsrives fra din identitet, når kontoen slettes |
| **Appens sprog og version** | Levere det rigtige indhold | Indtil din konto slettes |

**Hvad vi ikke indsamler:** dit navn, dine kontakter, din placering, din adressebog, dine billeder, din kalender, historikken over dine apps. Plume beder ikke om nogen af disse tilladelser.

**Hvad der udelukkende bliver på din telefon:** dine egne personaer og deres avatarer, dine indstillinger, dine regler pr. app, oversættelsescachen for Assisteret læsning (som ryddes ved afslutningen af hver session). Intet af dette sendes til vores servere.

---

## 4. Diktering med stemmen

En mikrofonknap giver dig mulighed for at diktere i stedet for at skrive. Tilladelsen til mikrofonen bliver bedt om **i det præcise øjeblik, hvor du trykker på denne knap**, aldrig ved opstart, og mikrofonen åbner kun i det øjeblik. Plume lytter aldrig i baggrunden.

**Plume modtager, gemmer og overfører aldrig nogen lydoptagelse.** Dikteringen overlades til den talegenkendelsesmotor, der er indbygget i din telefon (Androids). Plume henter kun den transskriberede tekst.

**Et vigtigt og ærligt punkt:** denne systemmotor tilhører din telefon, i almindelighed Google. Afhængigt af din enhed, dens indstillinger og de installerede sprogmoduler **kan den sende lyden til udgiverens servere** for at transskribere den. Denne behandling ligger uden for Plume og hører under privatlivspolitikken hos udgiveren af dit system. Vi kan derfor ikke hævde, at din stemme bliver på enheden — det afhænger af din telefon, ikke af os.

Hvis du afviser tilladelsen til mikrofonen, er indtastning på tastaturet naturligvis fortsat mulig.

---

## 5. Reklame

Tjenesten er gratis inden for en vis brugsgrænse pr. dag. Derudover kan du **vælge** at se en belønnet annonce for at låse op for yderligere anvendelser. Det er aldrig påtvunget: hvis du ikke ser en annonce, beholder du blot det, du har ret til.

- Annoncerne leveres af **Google AdMob**.
- De vises **kun i selve appen Plume**, aldrig i den flydende kapsel og aldrig oven på en anden app.
- **Abonnenter ser ingen reklame.**
- I Det Europæiske Økonomiske Samarbejdsområde, i Det Forenede Kongerige og i Schweiz bliver du præsenteret for en samtykkeformular fra en platform, der er certificeret af Google, **inden den første annonce**. Så længe dit valg ikke er indhentet, anmodes der ikke om nogen annonce. Hvis du siger nej, forbliver annoncerne **ikke-personaliserede**, og **ingen funktion tages fra dig**. Du kan til enhver tid ændre dette valg i indstillingerne.
- For at kunne kreditere din belønning pålideligt sendes din Plume-enhedsidentifikator til AdMob. Google kan i øvrigt indsamle sine egne oplysninger i overensstemmelse med sin privatlivspolitik.

*På skrivetidspunktet er visningen af annoncer slået fra på serversiden. Dette afsnit beskriver, hvordan det fungerer, så snart den slås til.*

---

## 6. Abonnementer og køb

Abonnementerne og pakkerne sælges **via Google Play**. Vi ser aldrig dine betalingsoplysninger: de behandles af Google, som er sælger i faktureringsmæssig forstand.

Vi modtager et købsbevis fra Google, som vores server kontrollerer, og vi gemmer et spor af det (transaktionsidentifikator, datoer, status). Dette spor gemmes af bogføringsmæssige grunde og for at forhindre, at det samme køb bruges to gange — men det bliver **løsrevet fra din identitet**, når du sletter din konto.

---

## 7. Dine rettigheder

Du har ret til indsigt, berigtigelse, sletning, begrænsning af behandling, indsigelse og dataportabilitet i henhold til GDPR.

**Det enkleste og hurtigste: sletningen er indbygget i appen.**
Indstillinger → Privatliv → Slet mine data. Den **udføres øjeblikkeligt**, den sættes ikke i kø. Detaljerne om, hvad der slettes, og hvad der gemmes, står på vores særskilte side: `https://readit0.github.io/plume-legal/suppression-compte`.

Du kan også slette din konto **uden at installere appen** ved at skrive til sogacmoi7@gmail.com.

For alle andre anmodninger skal du skrive til **sogacmoi7@gmail.com**. Vi svarer inden for en måned.

**Retsgrundlag:** opfyldelsen af aftalen (at levere den tjeneste, du beder om, og at håndtere dit abonnement), dit samtykke (tilgængelighedstjenesten, skærmoptagelsen, afsendelsen til Cloud-AI, personaliseret reklame), vores legitime interesse (sikkerhed, bekæmpelse af svindel) og vores retlige forpligtelser (bogføring).

Du kan indgive en klage til **CNIL** (www.cnil.fr), som er udgiverens tilsynsmyndighed, eller, **hvis du bor i Den Europæiske Union**, til tilsynsmyndigheden i dit bopælsland — artikel 77 i GDPR giver dig valget.

---

## 8. Mindreårige

Plume er et hjælpeværktøj til at skrive, beregnet til et publikum **fra 16 år og opefter**. Vi indsamler ikke bevidst oplysninger om børn under 16 år, og appen er hverken udformet eller markedsført til dem. Hvis du har forældremyndigheden og mener, at dit barn har givet os oplysninger, så skriv til sogacmoi7@gmail.com: vi sletter kontoen.

Da appen gør det muligt at omformulere fri tekst og viser reklame, er den ikke berettiget til Google Plays familieprogrammer.

---

## 9. Databehandlere og modtagere

| Leverandør | Rolle | Hvor |
|---|---|---|
| **Supabase** | Hosting af databasen, godkendelse, serverfunktioner | Den Europæiske Union (Frankfurt) |
| **OpenRouter** | Videresendelse af anmodningerne til AI-modellen | **Uden for Den Europæiske Union** |
| **Mistral AI** (via OpenRouter) | Model, der behandler teksten (Mistral Small) | Behandling via formidleren ovenfor |
| **Google Play / Google Billing** | Betaling, abonnementer | Google Ireland / USA |
| **Google AdMob** | Belønnet reklame | Google Ireland / USA |
| **Google (telefonens systemtjenester)** | Talegenkendelse, offlinemoduler til oversættelse | Afhængigt af din enhed |

**Vi sælger ingen oplysninger og videregiver ingen oplysninger til databrokere.**

**Overførsler til lande uden for Den Europæiske Union:** brugen af OpenRouter, Google Play og AdMob indebærer en overførsel af oplysninger til et land uden for Den Europæiske Union. De juridiske rammer for disse overførsler (standardkontraktbestemmelser, afgørelse om tilstrækkeligt beskyttelsesniveau) **skal kontrolleres og dokumenteres af en fagperson inden offentliggørelse** — se noten sidst i dokumentet.

---

## 10. Sikkerhed

Udvekslingen mellem appen og vores servere er krypteret (HTTPS/TLS). Adgangen til oplysningerne i databasen er begrænset af serverregler: de følsomme funktioner kan ikke tilgås fra appen. Intet system er fuldkommen sikkert, men ingen tekst, du omformulerer, gemmes hos os — hvilket rent mekanisk begrænser, hvad et indbrud ville kunne afsløre.

---

## 11. Ændringer

Enhver ændring af denne politik vil blive offentliggjort på adressen `https://readit0.github.io/plume-legal` med en ny dato. I tilfælde af en væsentlig ændring af, hvordan dine oplysninger bevæger sig, informerer vi dig i appen.

---

## Almindelige betingelser

Betingelserne for brug af tjenesten (kvoter, abonnementer, opsigelse) står i et særskilt dokument: `https://readit0.github.io/plume-legal/conditions-generales`.

---

> ### Bør gennemlæses af en fagperson
>
> Dette dokument er skrevet ved at måle appens faktiske adfærd, men **det er ikke skrevet af en jurist**. Fire punkter fortjener først og fremmest en professionel vurdering:
>
> 1. **Overførslen af oplysninger til et land uden for Den Europæiske Union** til OpenRouter. Det er det mest følsomme punkt: man skal fastlægge, hvilken overførselsmekanisme der finder anvendelse, kontrollere, at der findes en databehandleraftale med denne leverandør, og skrive det her. Så længe det ikke er gjort, beskriver dette dokument overførslen uden at hævde, at den er juridisk reguleret.
> 2. **De retsgrundlag**, der er valgt i §7, navnlig fordelingen mellem samtykke og legitim interesse for tilgængelighedstjenesten.
> 3. **Aldersgrænsen** (16 år) og dens sammenhæng med Google Plays spørgeskema om indholdsklassificering.
> 4. **Oplysningen om AI** i henhold til Den Europæiske Unions forordning om kunstig intelligens (gennemsigtighedsforpligtelse for et system med begrænset risiko).

---

Dette dokument er en oversættelse af den franske version, der findes på adressen https://readit0.github.io/plume-legal/. Den stilles til rådighed til din information. Kontakt os på sogacmoi7@gmail.com, hvis du finder en uoverensstemmelse.
