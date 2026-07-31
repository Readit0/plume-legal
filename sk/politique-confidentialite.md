# Zásady ochrany osobných údajov aplikácie Plume

**Posledná aktualizácia: 31. júla 2026** — Verzia 1.0

---

## Kto je prevádzkovateľom vašich údajov

**SASU RedLine Music**
SIREN 938 277 100 — SIRET `938 277 100 00013`
Abbaye 208-1, 208 Résidence Lavoisier, 18100 Vierzon, France
Kontakt: sogacmoi7@gmail.com

Aplikácia je v Google Play zverejnená pod menom vydavateľa **openfunworld**.

Tieto zásady opisujú, čo aplikácia Plume robí vo svojej súčasnej verzii. Boli napísané na základe čítania kódu aplikácie, nie podľa všeobecnej šablóny.

---

## V jednej minúte

Plume vám pomáha písať: preformuluje váš text priamo v aplikácii, v ktorej práve píšete, a dokáže preložiť text zobrazený na obrazovke.

Tri veci, ktoré si treba zapamätať:

1. **Plume neuchováva žiadny z vašich textov na svojich serveroch.** Ani vaše preformulované texty, ani text prečítaný z obrazovky. Neuchovávame o nich ani kópiu, ani záznam v protokoloch.
2. **Podľa toho, ktorý engine si zvolíte, váš text opustí alebo neopustí váš telefón.** Dva enginy (Lokálna súprava a Lokálna AI) pracujú výhradne v zariadení. Tretí (Cloudová AI) odosiela text službe umelej inteligencie **nachádzajúcej sa mimo Európskej únie**. Voľba je na vás a Cloudová AI sa nikdy neaktivuje bez vášho výslovného súhlasu.
3. **Plume potrebuje silné oprávnenia** (čítať obsah zobrazený v iných aplikáciách, snímať obrazovku). Nižšie presne vysvetľujeme, na čo slúžia a na čo neslúžia.

---

## 1. Čo Plume číta na vašej obrazovke a kedy

### 1.1 Služba prístupnosti

Aby Plume mohla prepísať váš text tam, kde ho píšete, používa službu prístupnosti systému Android. Toto oprávnenie zapínate sami, v nastaveniach telefónu, po vysvetľujúcej obrazovke, ktorú vám Plume ukáže **skôr**, ako oň požiada.

Konkrétne:

- **V pokojovom stave** Plume vie iba to, ktorá aplikácia je otvorená a v ktorom okamihu umiestnite kurzor do textového poľa. Práve to spôsobí, že sa objaví plávajúca kapsula — a to výhradne v aplikáciách, ktoré ste si sami nastavili.
- **Obsah poľa sa číta iba v tom presnom okamihu, keď sa dotknete kapsuly**, aby bol text prepísaný a potom na mieste nahradený.
- **Polia s heslami sú vylúčené.** Aplikácia rozpozná polia typu heslo (vrátane číselných kódov a webových polí) a odmietne ich čítať.
- Toto oprávnenie **neumožňuje žiadne snímanie obrazu** vašej obrazovky.
- Plume **za vás nikdy na nič neklikne** v inej aplikácii: nahradí text v poli, nič viac.

Dve funkcie, ktoré si zapínate sami — **Asistované čítanie v textovom režime** a **preklad prijatých správ** — čítajú zobrazený text nepretržite po celý čas svojho behu a zastavia sa hneď, ako ich vypnete.

Ak službu prístupnosti odmietnete, Plume zostáva použiteľná: môžete vybrať text a použiť položku „Plume“ v ponuke výberu systému Android alebo text zdieľať do aplikácie Plume.

### 1.2 Snímanie obrazovky (Asistované čítanie)

Asistované čítanie prekrýva zobrazený text prekladom — napríklad bubliny komiksu. Potrebuje na to vidieť obraz obrazovky.

- Je **predvolene vypnuté** a funguje iba v aplikáciách, ktoré ste výslovne povolili, jednu po druhej.
- **Android si pri každom spustení relácie vyžiada vlastný súhlas.** Nejde o oprávnenie udelené raz navždy: každá relácia vyžaduje nový súhlas. Plume sa nikdy nesnaží tento súhlas znova použiť ani ho obísť.
- Počas celej relácie **zostávajú viditeľné trvalé upozornenie a systémový indikátor**. Plume nemôže vašu obrazovku snímať nenápadne.
- Relácia **sa automaticky ukončí pri uzamknutí obrazovky** a okamžite vtedy, keď ju zastavíte sami.
- Aplikácie, ktoré chránia svoje zobrazenie (bankové aplikácie, správcovia hesiel), sú **prekryté samotným Androidom** skôr, než Plume čokoľvek dostane. Ide o ochranu systému, skutočnú, ale čiastočnú: neaktivujú ju všetky citlivé aplikácie. Nepredstavujeme ju preto ako absolútnu záruku.
- **Snímané obrazy sa nikdy neukladajú ani neodosielajú.** Každý obraz sa analyzuje v pamäti, aby sa z neho získal text, a potom sa zahodí. Žiadny obraz nikdy neopustí váš telefón, nech si zvolíte ktorýkoľvek engine.

---

## 2. Čo zostáva vo vašom telefóne a čo ho opúšťa

Toto je najdôležitejšie rozlíšenie týchto zásad a ovládate ho vy.

### 2.1 Enginy, ktoré nič neodosielajú von

- **Lokálna súprava** (rozpoznávanie a preklad textu offline) funguje výhradne v zariadení.
- **Lokálna AI** je model umelej inteligencie stiahnutý raz a potom uložený vo vašom telefóne (približne 720 MB). Beží vo vašom zariadení.

Pri týchto dvoch enginoch **prečítaný alebo preformulovaný text neopúšťa váš telefón.** Neprebieha žiadne sieťové volanie súvisiace s obsahom vášho textu.

### 2.2 Engine Cloudová AI

Keď si zvolíte Cloudovú AI alebo keď vaše zariadenie nie je dosť výkonné pre Lokálnu AI, dotknutý text sa prenesie na naše servery a následne do služby umelej inteligencie tretej strany.

**Treba jasne povedať, aká je skutočná trasa:**

- Text prechádza našou infraštruktúrou (Supabase), umiestnenou v **Európskej únii** (región stredná Európa, Frankfurt).
- Následne je odovzdaný službe **openrouter.ai**, smerovaciemu sprostredkovateľovi **nachádzajúcemu sa mimo Európskej únie**, ktorý ho dá spracovať modelu **Mistral Small**.
- **Ide teda o prenos údajov mimo Európskej únie.** Netvrdíme opak a pre tento krok neuvádzame žiadny prísľub európskeho hostingu.
- **Plume váš text neuchováva.** Žiadna z našich serverových funkcií obsah vášho textu nezapisuje: zaznamenávame iba technický identifikátor požiadavky a identifikátor vášho zariadenia, aby sme počítali váš limit a odhaľovali zneužitia.
- **To, čo títo poskytovatelia robia na svojej strane, zaručiť nevieme.** Radšej vám to povieme, než by sme vám sľubovali nulové uchovávanie, ktoré nie sme schopní overiť.

**Cloudová AI sa nikdy neaktivuje sama od seba.** Vyhradená obrazovka súhlasu vám tieto body vysvetlí pred prvým odoslaním a nič neodíde, kým súhlas neudelíte. Ak Lokálna AI zlyhá, Plume neprepne potichu do cloudu: oznámi vám to a počká na vaše rozhodnutie. Tento súhlas môžete kedykoľvek odvolať v nastaveniach.

Odosielaný text je obmedzený: 1 200 znakov pre preformulovanie, 4 000 znakov pre analýzu obrazovky.

---

## 3. Údaje, ktoré uchovávame

Nepoužívame **žiadny nástroj na analýzu návštevnosti, žiadny reklamný tracker tretej strany, žiadny nástroj na hlásenie pádov**. Aplikácia neobsahuje žiadnu meraciu súpravu SDK.

Tu je všetko, čo je uložené na našich serveroch:

| Údaj | Prečo | Doba |
|---|---|---|
| **Identifikátor zariadenia** (náhodné číslo generované aplikáciou Plume, bez väzby na vašu totožnosť a bez väzby na reklamný identifikátor) | Priradiť zariadenie k účtu, uplatňovať limity, blokovať zneužitia | Do vymazania vášho účtu |
| **E-mailová adresa účtu** (ak si vytvoríte účet e-mailom alebo cez Google) | Overiť vašu totožnosť, priradiť vaše predplatné | Do vymazania vášho účtu |
| **Počítadlá používania** (počet preformulovaní za deň a za mesiac — čísla, nie texty) | Uplatňovať limity | Do vymazania vášho účtu |
| **História nákupov** (identifikátor transakcie Google Play, dátumy, stav predplatného) | Sprístupniť vám to, čo ste zaplatili, spravovať obnovenia, plniť naše účtovné povinnosti | Uchovávaná aj po vymazaní účtu, ale **oddelená od vašej totožnosti** (pozri §6) |
| **Dobrovoľne zaslané návrhy** (ak nám z aplikácie napíšete návrh persony) | Vylepšovať katalóg. Tieto návrhy sa nikdy nezverejňujú. | Do vymazania vášho účtu |
| **Technické signály zneužitia** (opakované prekročenia, zlyhanie kontroly integrity — bez akéhokoľvek textu) | Bezpečnosť, boj proti podvodom | Oddelené od vašej totožnosti pri vymazaní účtu |
| **Jazyk a verzia aplikácie** | Doručovať správny obsah | Do vymazania vášho účtu |

**Čo nezhromažďujeme:** vaše meno, vaše kontakty, vašu polohu, váš adresár, vaše fotografie, váš kalendár, históriu vašich aplikácií. Plume o žiadne z týchto oprávnení nežiada.

**Čo zostáva výhradne vo vašom telefóne:** vaše vlastné persony a ich avatari, vaše nastavenia, vaše pravidlá pre jednotlivé aplikácie, vyrovnávacia pamäť prekladov Asistovaného čítania (mazaná na konci každej relácie). Nič z toho sa na naše servery neodosiela.

---

## 4. Hlasové diktovanie

Tlačidlo mikrofónu vám umožňuje diktovať namiesto písania. O oprávnenie na prístup k mikrofónu žiadame **presne vo chvíli, keď toto tlačidlo stlačíte**, nikdy pri spustení, a mikrofón sa otvorí až v tom okamihu. Plume nikdy nepočúva na pozadí.

**Plume neprijíma, neukladá ani neprenáša žiadnu zvukovú nahrávku.** Diktovanie je zverené enginu rozpoznávania reči zabudovanému vo vašom telefóne (tomu od Androidu). Plume preberá iba prepísaný text.

**Dôležitá a poctivá poznámka:** tento systémový engine patrí vášmu telefónu, spravidla spoločnosti Google. Podľa vášho zariadenia, jeho nastavení a nainštalovaných jazykových modulov **môže zvuk na prepis odosielať na servery svojho vydavateľa**. Toto spracúvanie je mimo dosahu aplikácie Plume a riadi sa zásadami ochrany osobných údajov vydavateľa vášho systému. Nemôžeme teda tvrdiť, že váš hlas zostáva v zariadení — závisí to od vášho telefónu, nie od nás.

Ak oprávnenie na mikrofón odmietnete, písanie na klávesnici samozrejme zostáva k dispozícii.

---

## 5. Reklama

Služba je bezplatná v rámci určitého denného limitu používania. Nad jeho rámec si **môžete zvoliť**, že si pozriete reklamu s odmenou a odomknete si ďalšie použitia. Nikdy to nie je vynútené: ak si reklamu nepozriete, jednoducho si ponecháte to, na čo máte nárok.

- Reklamy dodáva **Google AdMob**.
- Objavujú sa **výhradne v samotnej aplikácii Plume**, nikdy v plávajúcej kapsule a nikdy cez inú aplikáciu.
- **Predplatitelia nevidia žiadnu reklamu.**
- V Európskom hospodárskom priestore, v Spojenom kráľovstve a vo Švajčiarsku sa vám **pred prvou reklamou** predloží formulár súhlasu poskytovaný platformou certifikovanou spoločnosťou Google. Kým sa vaša voľba nezíska, nevyžiada sa žiadna reklama. Ak odmietnete, reklamy zostávajú **nepersonalizované** a **neodoberie sa vám žiadna funkcia**. K svojej voľbe sa môžete kedykoľvek vrátiť v nastaveniach.
- Aby vám mohla byť odmena spoľahlivo pripísaná, identifikátor vášho zariadenia Plume sa odovzdáva službe AdMob. Google môže okrem toho zhromažďovať vlastné údaje v súlade so svojimi zásadami ochrany osobných údajov.

*Ku dňu napísania tohto dokumentu je zobrazovanie reklám na strane servera vypnuté. Táto časť opisuje fungovanie od okamihu, keď bude zapnuté.*

---

## 6. Predplatné a nákupy

Predplatné a balíky sa predávajú **prostredníctvom Google Play**. Vaše bankové údaje nikdy nevidíme: spracúva ich Google, ktorý je z hľadiska fakturácie predávajúcim.

Od Googlu dostaneme doklad o nákupe, ktorý náš server overí, a uchovávame o ňom záznam (identifikátor transakcie, dátumy, stav). Tento záznam sa uchováva z účtovných dôvodov a preto, aby ten istý nákup neposlúžil dvakrát — pri vymazaní vášho účtu je však **oddelený od vašej totožnosti**.

---

## 7. Vaše práva

Máte práva na prístup, opravu, vymazanie, obmedzenie spracúvania, namietanie a prenosnosť údajov, ktoré stanovuje GDPR.

**Najjednoduchšia a najrýchlejšia cesta: mazanie je zabudované v aplikácii.**
Nastavenia → Súkromie → Vymazať moje údaje. Vykoná sa **okamžite**, nezaraďuje sa do frontu. Podrobnosti o tom, čo sa maže a čo sa uchováva, sú uvedené na našej vyhradenej stránke: `https://readit0.github.io/plume-legal/suppression-compte`.

Svoj účet môžete vymazať aj **bez inštalácie aplikácie**, a to napísaním na sogacmoi7@gmail.com.

S akoukoľvek inou žiadosťou píšte na **sogacmoi7@gmail.com**. Odpovedáme do jedného mesiaca.

**Právne základy:** plnenie zmluvy (poskytnutie služby, o ktorú žiadate, správa vášho predplatného), váš súhlas (služba prístupnosti, snímanie obrazovky, odoslanie do Cloudovej AI, personalizovaná reklama), náš oprávnený záujem (bezpečnosť, boj proti podvodom) a naše zákonné povinnosti (účtovníctvo).

Môžete podať sťažnosť na **CNIL** (www.cnil.fr), dozorný orgán vydavateľa, alebo, **ak máte bydlisko v Európskej únii**, na dozorný orgán krajiny svojho bydliska — článok 77 GDPR vám ponecháva voľbu.

---

## 8. Maloletí

Plume je nástroj na pomoc s písaním určený publiku **od 16 rokov vyššie**. Vedome nezhromažďujeme údaje detí mladších ako 16 rokov a aplikácia nie je pre ne ani navrhnutá, ani propagovaná. Ak ste nositeľom rodičovských práv a povinností a domnievate sa, že nám vaše dieťa poskytlo údaje, napíšte na sogacmoi7@gmail.com: účet vymažeme.

Keďže aplikácia umožňuje preformulovať voľný text a zobrazuje reklamu, nie je spôsobilá pre programy Google Play určené rodinám.

---

## 9. Sprostredkovatelia a príjemcovia

| Poskytovateľ | Úloha | Kde |
|---|---|---|
| **Supabase** | Hosting databázy, overovanie, serverové funkcie | Európska únia (Frankfurt) |
| **OpenRouter** | Smerovanie požiadaviek k modelu AI | **Mimo Európskej únie** |
| **Mistral AI** (cez OpenRouter) | Model, ktorý text spracúva (Mistral Small) | Spracúvanie prostredníctvom vyššie uvedeného sprostredkovateľa |
| **Google Play / Google Billing** | Platba, predplatné | Google Ireland / Spojené štáty |
| **Google AdMob** | Reklama s odmenou | Google Ireland / Spojené štáty |
| **Google (systémové služby telefónu)** | Rozpoznávanie reči, moduly offline prekladu | Podľa vášho zariadenia |

**Žiadne údaje nepredávame a žiadne nepostupujeme dátovým brokerom.**

**Prenosy mimo Európskej únie:** využitie služieb OpenRouter, Google Play a AdMob zahŕňa prenos údajov mimo Európskej únie. Právny rámec týchto prenosov (štandardné zmluvné doložky, rozhodnutie o primeranosti) **musí byť pred zverejnením overený a zdokumentovaný odborníkom** — pozri poznámku na konci dokumentu.

---

## 10. Bezpečnosť

Komunikácia medzi aplikáciou a našimi servermi je šifrovaná (HTTPS/TLS). Prístup k údajom v databáze je obmedzený pravidlami na strane servera: citlivé funkcie nie sú z aplikácie dostupné. Žiadny systém nie je dokonale bezpečný, ale žiadny text, ktorý preformulujete, nie je u nás uložený — čo mechanicky obmedzuje to, čo by mohlo vniknutie do systému odhaliť.

---

## 11. Zmeny

Každá zmena týchto zásad bude zverejnená na adrese `https://readit0.github.io/plume-legal` s novým dátumom. V prípade podstatnej zmeny v pohybe vašich údajov vás o tom upovedomíme v aplikácii.

---

## Všeobecné podmienky

Podmienky používania služby (limity, predplatné, ukončenie) sú uvedené v samostatnom dokumente: `https://readit0.github.io/plume-legal/conditions-generales`.

---

> ### Na posúdenie odborníkom
>
> Tento dokument bol napísaný meraním skutočného správania aplikácie, **nebol však napísaný právnikom**. Štyri body si prednostne zaslúžia odborné stanovisko:
>
> 1. **Prenos údajov mimo Európskej únie** službe OpenRouter. Ide o najcitlivejší bod: treba určiť použiteľný mechanizmus prenosu, overiť, že s týmto poskytovateľom existuje zmluva o spracúvaní osobných údajov, a uviesť to tu. Kým sa tak nestane, tento dokument prenos opisuje bez toho, aby tvrdil, že je právne ošetrený.
> 2. **Právne základy** zvolené v §7, najmä rozdelenie medzi súhlas a oprávnený záujem pri službe prístupnosti.
> 3. **Minimálny vek** (16 rokov) a jeho súlad s dotazníkom klasifikácie obsahu Google Play.
> 4. **Zmienka o umelej inteligencii** podľa európskeho nariadenia o umelej inteligencii (povinnosť transparentnosti pre systém s obmedzeným rizikom).

---

Tento dokument je prekladom francúzskej verzie, dostupnej na adrese https://readit0.github.io/plume-legal/. Preklad poskytujeme pre vašu informáciu. V prípade rozporu nás kontaktujte na adrese sogacmoi7@gmail.com.
