# Privacybeleid van Plume

**Laatst bijgewerkt: 12 september 2026** — Versie 2.0

> *Wat er is veranderd sinds versie 1.0, en waarom u mogelijk het toestemmingsscherm opnieuw ziet in de app:* wij corrigeren twee beweringen die niet langer juist waren. Ten eerste bewaart de functie **persoonlijke talen** op onze servers de inhoud die u aanmaakt (naam, alfabet, lexicon) — versie 1.0 beweerde ten onrechte dat er geen enkele tekst werd opgeslagen. Ten tweede gebruiken wij nu een hulpmiddel voor **technische crashrapportage** — versie 1.0 beweerde dat er geen enkel hulpmiddel van dit type bestond. De details van deze twee punten vindt u hieronder bij "In één minuut", en in §3 en §9. Dit zijn precies de twee categorieën wijzigingen die in de app een nieuwe toestemmingsvraag doen verschijnen (zie §11).

---

## Wie verantwoordelijk is voor uw gegevens

**SASU RedLine Music**
SIREN 938 277 100 — SIRET `938 277 100 00013`
Abbaye 208-1, 208 Résidence Lavoisier, 18100 Vierzon, France
Contact: sogacmoi7@gmail.com

De app wordt op Google Play gepubliceerd onder de ontwikkelaarsnaam **openfunworld**.

Dit beleid beschrijft wat de app Plume in de huidige versie doet. Het is geschreven op basis van de programmacode van de app, niet op basis van een algemeen sjabloon.

---

## In één minuut

Plume helpt u bij het schrijven: de app herschrijft uw tekst rechtstreeks in de toepassing waarin u aan het typen bent, en kan tekst vertalen die op het scherm wordt weergegeven.

Drie dingen om te onthouden:

1. **Plume bewaart noch de teksten die u herschrijft, noch de tekst die op het scherm wordt gelezen.** Wij bewaren daarvan geen kopie en geen logboek. **Een bewuste, en vrijwillige, uitzondering:** als u een **persoonlijke taal** aanmaakt (uw eigen zelfbedachte taal, met een lexicon van woorden en hun betekenissen), dan wordt de inhoud van die taal wél op onze servers bewaard — dat is de enige manier om u in staat te stellen haar op een ander apparaat terug te vinden, haar verder te ontwikkelen en haar te delen. De details staan in §3.
2. **Afhankelijk van de motor die u kiest, verlaat uw tekst uw telefoon of niet.** Twee motoren (de Lokale kit en de Lokale AI) werken volledig op het apparaat. De derde (de Cloud-AI) stuurt de tekst naar een dienst voor kunstmatige intelligentie **buiten de Europese Unie**. U kiest, en de Cloud-AI wordt nooit ingeschakeld zonder uw uitdrukkelijke toestemming.
3. **Plume heeft ingrijpende machtigingen nodig** (de inhoud lezen die in andere apps wordt weergegeven, het scherm vastleggen). Hieronder leggen wij precies uit waarvoor ze dienen en waarvoor niet.

---

## 1. Wat Plume op uw scherm leest, en wanneer

### 1.1 De toegankelijkheidsservice

Om uw tekst te herschrijven op de plek waar u hem schrijft, gebruikt Plume de toegankelijkheidsservice van Android. Dat is een machtiging die u zelf inschakelt in de instellingen van uw telefoon, na een uitlegscherm dat Plume u **vooraf** laat zien.

Concreet:

- **In rust** weet Plume alleen welke app geopend is en wanneer u de cursor in een invoerveld plaatst. Daardoor verschijnt de zwevende capsule — en uitsluitend in de apps die u zelf hebt ingesteld.
- **De inhoud van het veld wordt pas gelezen op het precieze moment waarop u de capsule aanraakt**, om te worden herschreven en vervolgens ter plaatse te worden vervangen.
- **Wachtwoordvelden zijn uitgesloten.** De app herkent velden van het type wachtwoord (met inbegrip van cijfercodes en webvelden) en weigert die te lezen.
- Deze machtiging **maakt geen enkele beeldopname** van uw scherm mogelijk.
- Plume **tikt nooit in uw plaats** in een andere app: de app vervangt de tekst van een veld, meer niet.

Twee functies die u zelf inschakelt — de **Leeshulp in de tekstmodus** en de **vertaling van ontvangen berichten** — lezen de weergegeven tekst doorlopend zolang ze draaien, en stoppen zodra u ze uitschakelt.

Als u de toegankelijkheidsservice weigert, blijft Plume bruikbaar: u kunt een tekst selecteren en de optie "Plume" in het selectiemenu van Android gebruiken, of een tekst met Plume delen.

### 1.2 De schermopname (Leeshulp)

De Leeshulp legt een vertaling over de weergegeven tekst — bijvoorbeeld over de tekstballonnen van een strip. Daarvoor moet de app het beeld van het scherm zien.

- De functie is **standaard uitgeschakeld** en werkt alleen in de apps die u stuk voor stuk uitdrukkelijk hebt toegestaan.
- **Android vraagt bij het begin van elke sessie zijn eigen toestemming.** Dit is geen machtiging die eens en voor altijd wordt verleend: elke sessie vereist een nieuwe toestemming. Plume probeert die toestemming nooit opnieuw te gebruiken of te omzeilen.
- Gedurende de hele sessie **blijven een permanente melding en een systeemindicator zichtbaar**. Plume kan uw scherm niet ongemerkt vastleggen.
- De sessie **stopt automatisch wanneer het scherm wordt vergrendeld**, en onmiddellijk wanneer u de sessie zelf stopt.
- Apps die hun weergave beschermen (bankapps, wachtwoordbeheerders) worden **door Android zelf zwart gemaakt** voordat Plume ook maar iets ontvangt. Dat is een bescherming van het systeem: echt, maar gedeeltelijk, want niet alle gevoelige apps schakelen die in. Wij presenteren die bescherming daarom niet als een absolute garantie.
- **Vastgelegde beelden worden nooit opgeslagen of verzonden.** Elk beeld wordt in het geheugen geanalyseerd om er de tekst uit te halen en wordt daarna weggegooid. Er verlaat nooit een beeld uw telefoon, welke motor u ook kiest.

---

## 2. Wat op uw telefoon blijft en wat vertrekt

Dit is het belangrijkste onderscheid van dit privacybeleid, en u bent degene die het bepaalt.

### 2.1 De motoren die niets naar buiten sturen

- **De Lokale kit** (tekstherkenning en vertaling offline) werkt volledig op het apparaat.
- **De Lokale AI** is een model voor kunstmatige intelligentie dat eenmalig wordt gedownload en daarna op uw telefoon wordt opgeslagen (ongeveer 720 MB). Het draait op uw apparaat.

Met deze twee motoren **verlaat de gelezen of herschreven tekst uw telefoon niet.** Er is geen enkele netwerkoproep die met de inhoud van uw tekst te maken heeft.

### 2.2 De motor Cloud-AI

Wanneer u de Cloud-AI kiest, of wanneer uw apparaat niet krachtig genoeg is voor de Lokale AI, wordt de betrokken tekst doorgestuurd naar onze servers en vervolgens naar een dienst voor kunstmatige intelligentie van een derde partij.

**Over de werkelijke route moeten wij duidelijk zijn:**

- De tekst loopt via onze serverinfrastructuur, gehost in de **Europese Unie** (regio Centraal-Europa, Frankfurt).
- Hij wordt daarna doorgestuurd naar een routeringstussenpersoon **buiten de Europese Unie**, die de tekst laat verwerken door een AI-model van een derde partij.
- **Het gaat hier dus om een doorgifte van gegevens buiten de Europese Unie.** Wij beweren niet het tegendeel en wij doen voor deze stap geen enkele belofte over Europese hosting.
- **Plume bewaart uw tekst niet.** Geen van onze serverfuncties schrijft de inhoud van uw tekst weg: wij registreren alleen een technische aanvraagidentificatie en de identificatie van uw apparaat, om uw quotum te tellen en misbruik op te sporen.
- **Wat deze dienstverleners aan hun kant doen, kunnen wij niet garanderen.** Wij zeggen u dat liever dan u een nulbewaring te beloven die wij niet kunnen controleren.

**De Cloud-AI wordt nooit vanzelf ingeschakeld.** Een apart toestemmingsscherm legt u deze punten uit vóór de eerste verzending, en er vertrekt niets zolang u niet hebt aanvaard. Als de Lokale AI faalt, schakelt Plume niet stilzwijgend over naar de cloud: de app meldt het u en wacht uw beslissing af. U kunt die toestemming op elk moment intrekken in de instellingen.

De verzonden tekst is begrensd: 1.200 tekens voor een herschrijving, 4.000 tekens voor een schermanalyse.

---

## 3. De gegevens die wij bewaren

Wij gebruiken **geen enkel hulpmiddel voor publieksmeting en geen enkele advertentietracker van derden**, afgezien van de advertenties die in §5 worden beschreven. **Wij gebruiken wel een hulpmiddel voor technische crashrapportage**: dat ziet alleen programmafouten (type fout, technische call stack, versie van de app, besturingssysteem), nooit uw gebruik of uw traject, en nooit de tekst die u schrijft — een speciaal filter verbiedt dat vóór elke verzending. De details staan in §9.

Hier is alles wat op onze servers wordt opgeslagen:

| Gegeven | Waarvoor | Bewaartermijn |
|---|---|---|
| **Apparaatidentificatie** (een willekeurig nummer dat door Plume wordt gegenereerd, zonder verband met uw identiteit of met een advertentie-identificatie) | Een apparaat aan een account koppelen, quota toepassen, misbruik blokkeren | Tot uw account wordt verwijderd |
| **E-mailadres van het account** (als u een account aanmaakt via e-mail of via Google) | U authenticeren, uw abonnement koppelen | Tot uw account wordt verwijderd |
| **Gebruiksteller** (aantal herschrijvingen per dag en per maand — getallen, geen teksten) | Quota toepassen | Tot uw account wordt verwijderd |
| **Aankoopgeschiedenis** (transactie-identificatie van Google Play, data, status van het abonnement) | U toegang geven tot wat u hebt betaald, verlengingen beheren, onze boekhoudkundige verplichtingen nakomen | Wordt ook na verwijdering van het account bewaard, maar **losgekoppeld van uw identiteit** (zie § 6) |
| **Vrijwillig verzonden suggesties** (als u ons vanuit de app een persona-suggestie stuurt) | De catalogus verbeteren. Deze suggesties worden nooit gepubliceerd. | Tot uw account wordt verwijderd |
| **Technische misbruiksignalen** (herhaalde overschrijdingen, mislukte integriteitscontrole — zonder enige tekst) | Beveiliging, fraudebestrijding | Losgekoppeld van uw identiteit bij verwijdering van het account |
| **Taal en versie van de app** | De juiste inhoud aanbieden | Tot uw account wordt verwijderd |
| **De inhoud van de persoonlijke talen die u aanmaakt** (de naam ervan, het alfabet ervan, en het lexicon ervan — de woorden en de definities die u, of andere personen, erin hebben geschreven) | U in staat stellen uw taal op een ander apparaat terug te vinden, haar verder te ontwikkelen, en haar met andere gebruikers te delen | Zolang de taal bestaat. Als u haar verwijdert, verdwijnt haar eigen kaart — maar een kopie die al **door iemand anders is geïmporteerd**, behoort dan aan die persoon toe en **blijft bestaan**, zoals een bericht dat al door een derde is ontvangen en dat wij niet bij hem kunnen gaan wissen |
| **Technische crashrapporten** (type fout, ingekorte technische call stack, versie van de app, besturingssysteem — nooit tekstuele inhoud) | Crashes van de app diagnosticeren en verhelpen | Geregeld door onze dienstverlener voor crashrapportage (zie §9). Deze verzameling is onderworpen aan uw toestemming en aan een schakelaar die wij op elk moment kunnen uitzetten, zonder app-update |

**Wat wij niet verzamelen:** uw naam, uw contacten, uw locatie, uw adresboek, uw foto's, uw agenda, de geschiedenis van uw apps. Plume vraagt geen enkele van deze machtigingen.

**Wat uitsluitend op uw telefoon blijft:** uw eigen persona's en hun avatars, uw instellingen, uw regels per app, de vertaalcache van de Leeshulp (gewist aan het einde van elke sessie). Niets daarvan wordt naar onze servers gestuurd.

---

## 4. Dicteren met spraak

Met een microfoonknop kunt u dicteren in plaats van typen. De machtiging voor toegang tot de microfoon wordt gevraagd **op het precieze moment waarop u die knop indrukt**, nooit bij het opstarten, en de microfoon gaat alleen op dat ogenblik open. Plume luistert nooit op de achtergrond mee.

**Plume ontvangt, bewaart en verzendt geen enkele geluidsopname.** Het dicteren wordt overgelaten aan de spraakherkenning die in uw telefoon is ingebouwd (die van Android). Plume krijgt alleen de getranscribeerde tekst.

**Een belangrijk en eerlijk punt:** die systeemvoorziening hoort bij uw telefoon, meestal bij Google. Afhankelijk van uw apparaat, de instellingen daarvan en de geïnstalleerde taalmodules **kan die voorziening de audio naar de servers van haar leverancier sturen** om die te transcriberen. Die verwerking valt buiten Plume en valt onder het privacybeleid van de leverancier van uw besturingssysteem. Wij kunnen dus niet stellen dat uw stem op het apparaat blijft — dat hangt af van uw telefoon, niet van ons.

Als u de microfoonmachtiging weigert, blijft invoer via het toetsenbord uiteraard beschikbaar.

---

## 5. Advertenties

De dienst is gratis binnen een bepaalde gebruikslimiet per dag. Daarboven kunt u ervoor **kiezen** om een beloonde advertentie te bekijken om extra gebruik vrij te spelen. Dat wordt nooit opgelegd: als u geen advertentie bekijkt, behoudt u eenvoudigweg waar u recht op hebt.

- De advertenties worden geleverd door **Google AdMob**.
- Zij verschijnen **uitsluitend in de app Plume zelf**, nooit in de zwevende capsule en nooit boven op een andere app.
- **Abonnees zien geen enkele advertentie.**
- In de Europese Economische Ruimte, het Verenigd Koninkrijk en Zwitserland wordt u **vóór de eerste advertentie** een toestemmingsformulier getoond dat wordt geleverd door een door Google gecertificeerd platform. Zolang uw keuze niet is opgehaald, wordt er geen advertentie aangevraagd. Als u weigert, blijven de advertenties **niet-gepersonaliseerd** en **wordt u geen enkele functie ontnomen**. U kunt op die keuze op elk moment terugkomen via de instellingen.
- Om uw beloning betrouwbaar toe te kennen, wordt uw Plume-apparaatidentificatie doorgegeven aan AdMob. Google kan daarnaast eigen gegevens verzamelen overeenkomstig zijn privacybeleid.

*Op het moment van schrijven staat de advertentievertoning uit aan de serverzijde. Deze paragraaf beschrijft de werking zodra die wordt ingeschakeld.*

---

## 6. Abonnementen en aankopen

Abonnementen en pakketten worden verkocht **via Google Play**. Wij zien uw bankgegevens nooit: die worden verwerkt door Google, dat voor de facturering de verkoper is.

Wij ontvangen van Google een aankoopbewijs dat onze server verifieert, en wij bewaren daarvan een spoor (transactie-identificatie, data, status). Dat spoor wordt bewaard om boekhoudkundige redenen en om te voorkomen dat dezelfde aankoop twee keer wordt gebruikt — maar het wordt **losgekoppeld van uw identiteit** wanneer u uw account verwijdert.

---

## 7. Uw rechten

U beschikt over de rechten van inzage, rectificatie, gegevenswissing, beperking van de verwerking, bezwaar en gegevensoverdraagbaarheid waarin de AVG voorziet.

**Het eenvoudigst en het snelst: de verwijdering is in de app ingebouwd.**
Instellingen → Privacy → Mijn gegevens verwijderen. Zij wordt **onmiddellijk uitgevoerd**, niet in een wachtrij geplaatst. Wat er precies wordt gewist en wat er wordt bewaard, staat op onze aparte pagina: `https://readit0.github.io/plume-legal/suppression-compte`.

U kunt uw account ook **zonder de app te installeren** laten verwijderen, door te schrijven naar sogacmoi7@gmail.com.

Voor elk ander verzoek schrijft u naar **sogacmoi7@gmail.com**. Wij antwoorden binnen een maand.

**Rechtsgronden:** de uitvoering van de overeenkomst (het leveren van de dienst die u vraagt, het beheer van uw abonnement), uw toestemming (toegankelijkheidsservice, schermopname, verzending naar de Cloud-AI, gepersonaliseerde advertenties), ons gerechtvaardigd belang (beveiliging, fraudebestrijding) en onze wettelijke verplichtingen (boekhouding).

U kunt een klacht indienen bij de **CNIL** (www.cnil.fr), de toezichthoudende autoriteit van de uitgever, of, **als u in de Europese Unie woont**, bij de toezichthoudende autoriteit van uw land van verblijf — artikel 77 AVG laat u de keuze.

---

## 8. Minderjarigen

Plume is een hulpmiddel bij het schrijven, bestemd voor een publiek **van 16 jaar en ouder**. Wij verzamelen niet bewust gegevens van kinderen jonger dan 16 jaar en de app is niet voor hen ontworpen en wordt niet voor hen gepromoot. Als u het ouderlijk gezag hebt en denkt dat uw kind ons gegevens heeft doorgegeven, schrijf dan naar sogacmoi7@gmail.com: wij verwijderen het account.

Omdat de app het herschrijven van vrije tekst mogelijk maakt en advertenties toont, komt zij niet in aanmerking voor de gezinsprogramma's van Google Play.

---

## 9. Verwerkers en ontvangers

| Dienstverlener | Rol | Waar |
|---|---|---|
| **Onze hostingdienstverlener** | Hosting van de database, authenticatie, serverfuncties | Europese Unie (Frankfurt) |
| **Onze dienstverlener voor AI-verwerking** | Doorsturen van de aanvragen en verwerking van de tekst door een AI-model van een derde partij | **Buiten de Europese Unie** |
| **Google Play / Google Billing** | Betaling, abonnementen | Google Ireland / Verenigde Staten |
| **Google AdMob** | Beloonde advertenties | Google Ireland / Verenigde Staten |
| **Google (systeemdiensten van de telefoon)** | Spraakherkenning, offline vertaalmodules | Afhankelijk van uw apparaat |
| **Onze dienstverlener voor crashrapportage** | Technische crashrapportage — uitsluitend programmafouten, gefilterd vóór verzending: nooit uw tekst | Verenigde Staten |

**Wij verkopen geen enkel gegeven en dragen er geen enkel over aan datahandelaren.**

**Doorgiften buiten de Europese Unie:** het gebruik van onze dienstverlener voor AI-verwerking, Google Play, AdMob en onze dienstverlener voor crashrapportage houdt een doorgifte van gegevens buiten de Europese Unie in. Het juridische kader van die doorgiften (modelcontractbepalingen, adequaatheidsbesluit) **moet vóór publicatie door een professional worden geverifieerd en gedocumenteerd** — zie de noot aan het einde van dit document.

---

## 10. Beveiliging

Het verkeer tussen de app en onze servers is versleuteld (HTTPS/TLS). De toegang tot de gegevens in de database is beperkt door regels aan de serverzijde: gevoelige functies zijn niet bereikbaar vanuit de app. Geen enkel systeem is volmaakt veilig. De tekst die u herschrijft en de tekst die de Leeshulp op het scherm weergeeft, worden niet bij ons opgeslagen, wat als vanzelf beperkt wat een inbraak daarover zou kunnen onthullen. **Dat geldt niet voor alles:** het lexicon van de persoonlijke talen die u aanmaakt, wordt namelijk wél opgeslagen (zie §3), en zou bij een daadwerkelijke inbraak net als elk ander gegeven uit dit beleid blootgesteld kunnen worden — wij beschermen het met dezelfde serverregels als de rest.

---

## 11. Wijzigingen

Elke wijziging van dit beleid wordt gepubliceerd op `https://readit0.github.io/plume-legal` met een nieuwe datum. Bij een belangrijke wijziging in de route van uw gegevens brengen wij u daarvan in de app op de hoogte.

**Sinds versie 2.0 zit er een concreet mechanisme achter deze belofte.** Een eenvoudige vormcorrectie (een datum, een adres, een precisering) vraagt niets extra's van u. Maar een MATERIËLE wijziging — een nieuwe ontvanger van uw gegevens, een nieuwe categorie verzamelde gegevens, een nieuw doel, of een wijziging van uw rechten of van de prijs — laat het toestemmingsscherm in de app eenmalig opnieuw verschijnen, met een samenvatting van wat er verandert en de twee bijgewerkte documenten. Dat is precies wat er is gebeurd voor deze versie 2.0 (zie het kader bovenaan dit document).

---

## Algemene voorwaarden

De gebruiksvoorwaarden van de dienst (quota, abonnementen, opzegging) staan in een afzonderlijk document: `https://readit0.github.io/plume-legal/conditions-generales`.

---

---

Dit document is een vertaling van de Franse versie, die beschikbaar is op https://readit0.github.io/plume-legal/. Zij wordt u ter informatie aangeboden. Neem bij afwijkingen contact met ons op via sogacmoi7@gmail.com.
