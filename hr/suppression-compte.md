# Brisanje vašeg računa i vaših podataka — Plume

**Posljednje ažuriranje: 31. srpnja 2026.** — Verzija 1.0

Obuhvaćena aplikacija: **Plume** (`com.plume.plume`), koju izdaje **SASU RedLine Music**, Abbaye 208-1, 208 Résidence Lavoisier, 18100 Vierzon, France — objavljena na Google Playu pod imenom **openfunworld**.

---

## Dva načina za brisanje računa

### 1. Iz aplikacije (najbrže)

**Postavke → Privatnost → Izbriši moje podatke**

Brisanje se **izvršava odmah**. Ne stavlja se u red čekanja i ne ovisi ni o kakvoj odgođenoj obradi: kada vam aplikacija potvrdi brisanje, ono se već dogodilo i poslužitelj ga je provjerio.

### 2. Bez instaliranja aplikacije

Ako ste Plume već deinstalirali ili više nemate pristup svojem telefonu, pišite na:

**sogacmoi7@gmail.com**

- Predmet: **Brisanje računa Plume**
- Navedite **adresu e-pošte svojeg računa Plume** (onu kojom ste se registrirali ili svoju Google adresu ako ste se prijavili putem Googlea).

Provjeravamo dolazi li zahtjev doista od nositelja računa, a zatim provodimo brisanje. **Te zahtjeve obrađujemo u roku od najviše 30 dana**, a u pravilu u roku od nekoliko dana. Nakon provedenog brisanja primate potvrdu e-poštom.

---

## Što se briše

Brisanje **trajno** uklanja:

- **vaš račun** (adresa e-pošte, lozinka, sesija);
- **vaše brojače korištenja** — broj preoblikovanja potrošenih po danu i po mjesecu;
- **vaše prijedloge** — prijedloge koje ste nam poslali iz aplikacije. To je jedini slobodni tekst koji smo pohranjivali;
- **vaše identifikatore zahtjeva** — tehničke reference zatraženih preoblikovanja;
- **vaše kredite i otključavanja kvote** — kupljene neiskorištene kredite, otključavanja dobivena oglasom, prilagođene gornje granice;
- **povezanost vaših uređaja s vašim računom** — vaši drugi telefoni ili tableti odvezuju se i ponovno postaju obični anonimni uređaji.

Uređaj s kojeg tražite brisanje **neutralizira se**: njegova povezanost s vašim računom briše se, njegov identifikacijski ključ uništava se i zamjenjuje mrtvom vrijednošću, njegov jezik i verzija aplikacije brišu se. Ostaje samo neproziran broj, koji više ne omogućuje ni da se vas identificira ni da se pronađe uređaj.

**Nikada nismo pohranjivali vaše tekstove.** Ni tekstove koje ste preoblikovali ni tekst koji je Potpomognuto čitanje pročitalo sa zaslona: nisu se čuvali nigdje na našim poslužiteljima, pa od njih nema ništa za izbrisati.

**Na vašem telefonu** vaše persone, vaši avatari, vaše postavke i vaša pravila po aplikaciji pohranjeni su lokalno. Briše ih brisanje pokrenuto iz aplikacije, a u svakom slučaju **nestaju kada deinstalirate Plume**.

---

## Što se čuva i zašto

Tri kategorije tragova ostaju, ali je **veza s vašim identitetom prekinuta**: identifikator vašeg računa i identifikator vašeg uređaja iz njih su uklonjeni. Ti zapisi više ne omogućuju da se dođe do vas.

| Što ostaje | Zašto to ne možemo uništiti |
|---|---|
| **Povijest vaših kupnji** (identifikator transakcije Google Play, iznos, datumi, stanje pretplate) | Računovodstvena obveza: dokaz o plaćanju ne uništava se. Čuva se **odvojen od vašeg identiteta**. |
| **Prava stečena kupnjom** (pretplata, paketi) | Isti računovodstveni razlog te dokaz plaćanja u slučaju spora. Čuvaju se **bez korisničkog identifikatora**. |
| **Oglašivačke nagrade i već dodijeljeni krediti** | Sprječava da se isti oglas ili ista kupnja naplate dvaput. Čuva se samo jedinstvena referenca transakcije, **bez identifikatora uređaja**. |
| **Tehnički sigurnosni signali** (ponovljena prekoračenja, neuspjele provjere cjelovitosti) | Borba protiv prijevara. Ti zapisi ne sadrže **nikakav tekst** i čuvaju se **bez identifikatora uređaja**. |

Ti se anonimizirani podaci čuvaju onoliko dugo koliko zahtijevaju naše zakonske, osobito računovodstvene obveze, a zatim se brišu ili agregiraju.

---

## Što brisanje ne čini

**Ono ne raskida vašu pretplatu.** Pretplatom upravlja Google Play, a ne mi: brisanje vašeg računa Plume ne zaustavlja je i **naplata bi vam se nastavila**.

**Najprije raskinite pretplatu**, a zatim izbrišite račun:
Play Store → Izbornik → Plaćanja i pretplate → Pretplate → Plume → Otkaži pretplatu.

**Ono ne briše podatke koje drži Google** (kupnje, oglašavanje, prepoznavanje govora na telefonu). Ti se podaci odnose na vaš Google račun i njima se upravlja iz postavki vašeg Google računa.

---

## Nakon brisanja

Brisanje je **konačno i nepovratno**. Ne možemo obnoviti izbrisani račun, ni vaše persone, ni vaše kupnje vezane uz taj račun.

Kasnije možete ponovno otvoriti račun s istom adresom e-pošte: bit će to **potpuno nov** račun, bez povijesti. Vaše prethodne kupnje, budući da su odvojene od svakog identiteta, **neće se moći vratiti** na taj novi račun. Ako želite zadržati pretplatu koja je u tijeku, nemojte brisati svoj račun.

---

## Vaša ostala prava

Osim brisanja, imate prava na pristup, ispravak, ograničenje obrade, prigovor i prenosivost podataka predviđena Općom uredbom o zaštiti podataka (OUZP / GDPR). Pišite na **sogacmoi7@gmail.com**.

Pojedinosti o obrađivanim podacima nalaze se u našim pravilima o privatnosti: `https://readit0.github.io/plume-legal/politique-confidentialite`.

Pritužbu možete podnijeti tijelu **CNIL** (www.cnil.fr).

---

> ### Za pregled od strane stručnjaka
>
> Ova stranica točno opisuje ponašanje koda za brisanje, provjereno redak po redak. Tri točke traže stručno mišljenje ili odluku prije objave:
>
> 1. **Rok čuvanja anonimiziranih računovodstvenih podataka** ovdje nije izražen brojkom. To mora biti: zakonski rok čuvanja računovodstvenih isprava u Francuskoj iznosi deset godina, no tehnička dokumentacija projekta spominje sažimanje događaja kupnje na 24 mjeseca. **Ta dva roka moraju se uskladiti**, a zatim upisati na ovu stranicu i u pravila o privatnosti.
> 2. **Postupak provjere identiteta** za zahtjeve e-poštom mora se odrediti i dokumentirati: prihvaćanje brisanja na temelju puke izjave izlaže riziku zlonamjernog brisanja; prevelik zahtjev stvara prepreku protivnu Općoj uredbi o zaštiti podataka.
> 3. **Upozorenje o kupnjama koje se ne mogu vratiti** nakon brisanja zaslužuje potvrdu: proizlazi iz činjenice da su prava iz kupnji anonimizirana i mora biti prikazano **u aplikaciji u trenutku potvrde**, a ne samo na ovoj stranici.

---

Ovaj je dokument prijevod francuske verzije, dostupne na adresi https://readit0.github.io/plume-legal/. Pružen je radi vaše obavijesti. U slučaju odstupanja obratite nam se na sogacmoi7@gmail.com.
