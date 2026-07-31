# Pravila o privatnosti aplikacije Plume

**Posljednje ažuriranje: 31. srpnja 2026.** — Verzija 1.0

---

## Tko je voditelj obrade vaših podataka

**SASU RedLine Music**
SIREN 938 277 100 — SIRET `938 277 100 00013`
Abbaye 208-1, 208 Résidence Lavoisier, 18100 Vierzon, France
Kontakt: sogacmoi7@gmail.com

Aplikacija se objavljuje na Google Playu pod imenom izdavača **openfunword**.

Ova pravila opisuju što aplikacija Plume radi u svojoj trenutačnoj verziji. Napisana su čitanjem koda aplikacije, a ne prema općenitom predlošku.

---

## U jednoj minuti

Plume vam pomaže pisati: preoblikuje vaš tekst izravno u aplikaciji u kojoj upravo tipkate i može prevoditi tekst prikazan na zaslonu.

Tri stvari koje treba zapamtiti:

1. **Plume ne pohranjuje nijedan vaš tekst na svojim poslužiteljima.** Ni vaše preoblikovane tekstove ni tekst pročitan sa zaslona. Ne čuvamo ni kopiju ni zapisnik.
2. **Ovisno o pogonu koji odaberete, vaš tekst napušta ili ne napušta vaš telefon.** Dva pogona (Lokalni komplet i Lokalna umjetna inteligencija) rade u cijelosti na uređaju. Treći (Umjetna inteligencija u oblaku) šalje tekst usluzi umjetne inteligencije **smještenoj izvan Europske unije**. Vi birate, a Umjetna inteligencija u oblaku nikada se ne aktivira bez vaše izričite privole.
3. **Plumeu su potrebna snažna dopuštenja** (čitanje sadržaja prikazanog u drugim aplikacijama, snimanje zaslona). U nastavku objašnjavamo točno čemu služe i čemu ne služe.

---

## 1. Što Plume čita na vašem zaslonu i kada

### 1.1 Usluga pristupačnosti

Da bi vaš tekst prepisao upravo ondje gdje ga pišete, Plume koristi Androidovu uslugu pristupačnosti. To je dopuštenje koje sami uključujete u postavkama telefona, nakon zaslona s objašnjenjem koji vam Plume prikazuje **prije** nego što ga zatraži.

Konkretno:

- **U mirovanju** Plume zna samo koja je aplikacija otvorena i u kojem trenutku postavljate pokazivač u polje za unos. Upravo se time pojavljuje plutajuća kapsula — i to isključivo u aplikacijama koje ste sami postavili.
- **Sadržaj polja čita se samo u točnom trenutku kada dodirnete kapsulu**, kako bi bio prepisan i potom zamijenjen na mjestu.
- **Polja za lozinku su isključena.** Aplikacija prepoznaje polja vrste lozinka (uključujući brojčane kodove i web-polja) i odbija ih čitati.
- To dopuštenje **ne omogućuje nikakvo snimanje slike** vašeg zaslona.
- Plume **nikada ne pritišće umjesto vas** u drugoj aplikaciji: ono zamjenjuje tekst u polju i ništa više.

Dvije funkcije koje sami uključujete — **Potpomognuto čitanje u tekstualnom načinu rada** i **prijevod primljenih poruka** — čitaju prikazani tekst neprekidno dok su uključene i zaustavljaju se čim ih isključite.

Ako odbijete uslugu pristupačnosti, Plume ostaje upotrebljiv: možete odabrati tekst i upotrijebiti izbornik „Plume“ pri odabiru teksta u Androidu ili podijeliti tekst s Plumeom.

### 1.2 Snimanje zaslona (Potpomognuto čitanje)

Potpomognuto čitanje prekriva prikazani tekst prijevodom — na primjer oblačiće u stripu. Za to mora vidjeti sliku zaslona.

- Ono je **isključeno prema zadanim postavkama** i radi samo u aplikacijama koje ste izričito odobrili, jednu po jednu.
- **Android traži vlastitu privolu pri svakom pokretanju sesije.** To nije dopuštenje dano jednom zauvijek: svaka sesija zahtijeva novu suglasnost. Plume nikada ne pokušava tu suglasnost ponovno upotrijebiti ni zaobići.
- Tijekom cijele sesije **ostaju vidljivi trajna obavijest i sustavni pokazatelj**. Plume ne može snimati vaš zaslon potajno.
- Sesija se **automatski zaustavlja pri zaključavanju zaslona** te odmah kada je sami zaustavite.
- Aplikacije koje štite svoj prikaz (bankovne aplikacije, upravitelji lozinki) **zacrnjuje sam Android** prije nego što Plume išta zaprimi. To je zaštita sustava, stvarna, ali djelomična: ne uključuju je sve osjetljive aplikacije. Zato je ne predstavljamo kao apsolutno jamstvo.
- **Snimljene slike nikada se ne spremaju ni ne šalju.** Svaka se slika analizira u memoriji radi izdvajanja teksta, a zatim se odbacuje. Nijedna slika nikada ne napušta vaš telefon, bez obzira na odabrani pogon.

---

## 2. Što ostaje na vašem telefonu, a što odlazi

To je najvažnija razlika u ovim pravilima i nju nadzirete vi.

### 2.1 Pogoni koji ništa ne iznose

- **Lokalni komplet** (izvanmrežno prepoznavanje i prevođenje teksta) radi u cijelosti na uređaju.
- **Lokalna umjetna inteligencija** model je umjetne inteligencije koji se jednom preuzme i zatim pohrani na vaš telefon (otprilike 720 MB). Izvodi se na vašem uređaju.

S ta dva pogona **pročitani ili preoblikovani tekst ne napušta vaš telefon.** Nema nijednog mrežnog zahtjeva povezanog sa sadržajem vašeg teksta.

### 2.2 Pogon Umjetna inteligencija u oblaku

Kada odaberete Umjetnu inteligenciju u oblaku ili kada vaš uređaj nije dovoljno snažan za Lokalnu umjetnu inteligenciju, predmetni se tekst prenosi na naše poslužitelje, a zatim usluzi umjetne inteligencije treće strane.

**Treba biti jasan oko stvarnog puta:**

- Tekst prolazi kroz našu infrastrukturu (Supabase), smještenu u **Europskoj uniji** (regija Srednja Europa, Frankfurt).
- Zatim se prenosi na **openrouter.ai**, posrednika za usmjeravanje **smještenog izvan Europske unije**, koji ga daje na obradu modelu **Mistral Small**.
- **Riječ je dakle o prijenosu podataka izvan Europske unije.** Ne tvrdimo suprotno i za taj korak ne prikazujemo nikakvo obećanje o europskom smještaju.
- **Plume ne pohranjuje vaš tekst.** Nijedna naša poslužiteljska funkcija ne zapisuje sadržaj vašeg teksta: bilježimo samo tehnički identifikator zahtjeva i identifikator vašeg uređaja, radi obračuna vaše kvote i otkrivanja zlouporaba.
- **Što ti pružatelji usluga rade sa svoje strane, ne možemo jamčiti.** Radije vam to kažemo nego da vam obećavamo nulto zadržavanje koje nismo u mogućnosti provjeriti.

**Umjetna inteligencija u oblaku nikada se ne aktivira sama od sebe.** Poseban zaslon za privolu objašnjava vam te točke prije prvog slanja i ništa se ne šalje dok ne prihvatite. Ako Lokalna umjetna inteligencija zakaže, Plume ne prelazi u oblak potiho: obavijestit će vas o tome i pričekati vašu odluku. Tu privolu možete povući u svakom trenutku u postavkama.

Poslani tekst je ograničen: 1.200 znakova za preoblikovanje i 4.000 znakova za analizu zaslona.

---

## 3. Podaci koje pohranjujemo

Ne upotrebljavamo **nijedan alat za analitiku posjećenosti, nijedan oglašivački pratitelj treće strane, nijedan alat za prijavu rušenja**. Aplikacija ne sadrži SDK za mjerenje.

Evo svega što se pohranjuje na našim poslužiteljima:

| Podatak | Zašto | Trajanje |
|---|---|---|
| **Identifikator uređaja** (nasumičan broj koji generira Plume, bez veze s vašim identitetom ni s oglašivačkim identifikatorom) | Povezivanje uređaja s računom, primjena kvota, blokiranje zlouporaba | Do brisanja vašeg računa |
| **Adresa e-pošte računa** (ako otvorite račun e-poštom ili putem Googlea) | Vaša autentifikacija, povezivanje vaše pretplate | Do brisanja vašeg računa |
| **Brojači korištenja** (broj preoblikovanja po danu i po mjesecu — brojevi, ne tekstovi) | Primjena kvota | Do brisanja vašeg računa |
| **Povijest kupnji** (identifikator transakcije Google Play, datumi, stanje pretplate) | Omogućiti vam pristup onome što ste platili, upravljati obnovama, poštovati naše računovodstvene obveze | Čuva se i nakon brisanja računa, ali **odvojena od vašeg identiteta** (vidjeti §6) |
| **Dobrovoljno poslani prijedlozi** (ako nam iz aplikacije pošaljete prijedlog persone) | Poboljšanje kataloga. Ti se prijedlozi nikada ne objavljuju. | Do brisanja vašeg računa |
| **Tehnički signali zlouporabe** (ponovljena prekoračenja, neuspjela provjera cjelovitosti — bez ikakvog teksta) | Sigurnost, borba protiv prijevara | Odvajaju se od vašeg identiteta pri brisanju računa |
| **Jezik i verzija aplikacije** | Isporuka ispravnog sadržaja | Do brisanja vašeg računa |

**Što ne prikupljamo:** vaše ime, vaše kontakte, vašu lokaciju, vaš adresar, vaše fotografije, vaš kalendar, povijest vaših aplikacija. Plume ne traži nijedno od tih dopuštenja.

**Što ostaje isključivo na vašem telefonu:** vaše prilagođene persone i njihovi avatari, vaše postavke, vaša pravila po aplikaciji, međuspremnik prijevoda Potpomognutog čitanja (briše se na kraju svake sesije). Ništa od toga ne šalje se na naše poslužitelje.

---

## 4. Glasovni diktat

Tipka s mikrofonom omogućuje vam da diktirate umjesto da tipkate. Dopuštenje za pristup mikrofonu traži se **u točnom trenutku kada pritisnete tu tipku**, nikada pri pokretanju, i mikrofon se otvara samo u tom trenutku. Plume nikada ne sluša u pozadini.

**Plume ne prima, ne pohranjuje i ne prenosi nikakav zvučni zapis.** Diktat se povjerava sustavu za prepoznavanje govora ugrađenom u vaš telefon (Androidovom). Plume preuzima samo prepisani tekst.

**Važna i poštena napomena:** taj sustavni pogon pripada vašem telefonu, u pravilu Googleu. Ovisno o vašem uređaju, njegovim postavkama i instaliranim jezičnim modulima, **on može prenositi zvuk na poslužitelje svojeg izdavača** radi prepisivanja. Ta je obrada izvan dosega Plumea i uređena je pravilima o privatnosti izdavača vašeg sustava. Stoga ne možemo tvrditi da vaš glas ostaje na uređaju — to ovisi o vašem telefonu, a ne o nama.

Ako odbijete dopuštenje za mikrofon, unos tipkovnicom naravno ostaje dostupan.

---

## 5. Oglašavanje

Usluga je besplatna u okviru određenog dnevnog ograničenja korištenja. Iznad njega **možete odabrati** gledanje nagrađivanog oglasa kako biste otključali dodatna korištenja. To se nikada ne nameće: ako ne gledate oglas, jednostavno zadržavate ono na što imate pravo.

- Oglase isporučuje **Google AdMob**.
- Pojavljuju se **isključivo u samoj aplikaciji Plume**, nikada u plutajućoj kapsuli i nikada preko druge aplikacije.
- **Pretplatnici ne vide nijedan oglas.**
- U Europskom gospodarskom prostoru, Ujedinjenoj Kraljevini i Švicarskoj prikazuje vam se obrazac za privolu koji pruža platforma certificirana od Googlea, **prije prvog oglasa**. Dok vaš odabir nije prikupljen, ne traži se nijedan oglas. Ako odbijete, oglasi ostaju **neprilagođeni** i **ne oduzima vam se nijedna funkcionalnost**. Taj odabir možete promijeniti u svakom trenutku u postavkama.
- Kako bi vam se nagrada pouzdano pripisala, vaš identifikator uređaja u Plumeu prenosi se AdMobu. Google usto može prikupljati vlastite podatke u skladu sa svojim pravilima o privatnosti.

*Na dan pisanja ovog dokumenta prikazivanje oglasa isključeno je na poslužitelju. Ovaj odjeljak opisuje način rada od trenutka kada bude uključeno.*

---

## 6. Pretplate i kupnje

Pretplate i paketi prodaju se **putem Google Playa**. Nikada ne vidimo vaše bankovne podatke: njih obrađuje Google, koji je prodavatelj u smislu naplate.

Od Googlea primamo dokaz o kupnji koji naš poslužitelj provjerava i o njemu čuvamo trag (identifikator transakcije, datumi, stanje). Taj se trag čuva iz računovodstvenih razloga i kako bi se spriječilo da ista kupnja posluži dvaput — ali se **odvaja od vašeg identiteta** kada izbrišete svoj račun.

---

## 7. Vaša prava

Imate prava na pristup, ispravak, brisanje, ograničenje obrade, prigovor i prenosivost podataka predviđena Općom uredbom o zaštiti podataka (OUZP / GDPR).

**Najjednostavnije i najbrže: brisanje je ugrađeno u aplikaciju.**
Postavke → Privatnost → Izbriši moje podatke. Ono se **izvršava odmah**, a ne stavlja u red čekanja. Pojedinosti o tome što se briše, a što se čuva nalaze se na našoj posebnoj stranici: `https://readit0.github.io/plume-legal/suppression-compte`.

Račun možete izbrisati i **bez instaliranja aplikacije**, pisanjem na sogacmoi7@gmail.com.

Za svaki drugi zahtjev pišite na **sogacmoi7@gmail.com**. Odgovaramo u roku od mjesec dana.

**Pravne osnove:** izvršavanje ugovora (pružanje usluge koju tražite, upravljanje vašom pretplatom), vaša privola (usluga pristupačnosti, snimanje zaslona, slanje Umjetnoj inteligenciji u oblaku, personalizirano oglašavanje), naš legitimni interes (sigurnost, borba protiv prijevara) i naše zakonske obveze (računovodstvo).

Pritužbu možete podnijeti tijelu **CNIL** (www.cnil.fr), nadzornom tijelu izdavača, ili, **ako imate boravište u Europskoj uniji**, nadzornom tijelu svoje zemlje boravišta — članak 77. OUZP-a ostavlja vam izbor.

---

## 8. Maloljetnici

Plume je alat za pomoć pri pisanju namijenjen publici **od 16 godina naviše**. Ne prikupljamo svjesno podatke djece mlađe od 16 godina i aplikacija nije ni osmišljena ni promovirana za njih. Ako imate roditeljsku skrb i smatrate da nam je vaše dijete proslijedilo podatke, pišite na sogacmoi7@gmail.com: izbrisat ćemo račun.

Budući da aplikacija omogućuje preoblikovanje slobodnog teksta i prikazuje oglase, ne ispunjava uvjete za Google Playeve programe namijenjene obiteljima.

---

## 9. Izvršitelji obrade i primatelji

| Pružatelj usluge | Uloga | Gdje |
|---|---|---|
| **Supabase** | Smještaj baze podataka, autentifikacija, poslužiteljske funkcije | Europska unija (Frankfurt) |
| **OpenRouter** | Usmjeravanje zahtjeva prema modelu umjetne inteligencije | **Izvan Europske unije** |
| **Mistral AI** (putem OpenRoutera) | Model koji obrađuje tekst (Mistral Small) | Obrada putem gore navedenog posrednika |
| **Google Play / Google Billing** | Plaćanje, pretplate | Google Ireland / Sjedinjene Američke Države |
| **Google AdMob** | Nagrađivano oglašavanje | Google Ireland / Sjedinjene Američke Države |
| **Google (sustavne usluge telefona)** | Prepoznavanje govora, moduli za izvanmrežno prevođenje | Ovisno o vašem uređaju |

**Ne prodajemo nikakve podatke niti ih ustupamo posrednicima u trgovini podacima.**

**Prijenosi izvan Europske unije:** korištenje OpenRoutera, Google Playa i AdMoba podrazumijeva prijenos podataka izvan Europske unije. Pravni okvir tih prijenosa (standardne ugovorne klauzule, odluka o primjerenosti) **mora prije objave provjeriti i dokumentirati stručnjak** — vidjeti napomenu na kraju dokumenta.

---

## 10. Sigurnost

Razmjena između aplikacije i naših poslužitelja je šifrirana (HTTPS/TLS). Pristup podacima u bazi ograničen je poslužiteljskim pravilima: osjetljive funkcije nisu dostupne iz aplikacije. Nijedan sustav nije savršeno siguran, ali nijedan tekst koji preoblikujete ne pohranjuje se kod nas — što mehanički ograničava ono što bi upad mogao otkriti.

---

## 11. Izmjene

Svaka izmjena ovih pravila bit će objavljena na adresi `https://readit0.github.io/plume-legal` s novim datumom. U slučaju važne promjene u kretanju vaših podataka, obavijestit ćemo vas o tome u aplikaciji.

---

## Opći uvjeti

Uvjeti korištenja usluge (kvote, pretplate, raskid) nalaze se u zasebnom dokumentu: `https://readit0.github.io/plume-legal/conditions-generales`.

---

> ### Za pregled od strane stručnjaka
>
> Ovaj je dokument napisan mjerenjem stvarnog ponašanja aplikacije, ali **nije ga napisao pravnik**. Četiri točke prvenstveno zaslužuju stručno mišljenje:
>
> 1. **Prijenos podataka izvan Europske unije** prema OpenRouteru. To je najosjetljivija točka: treba utvrditi primjenjiv mehanizam prijenosa, provjeriti postoji li ugovor o obradi s tim pružateljem usluge i to ovdje zapisati. Dok to nije učinjeno, ovaj dokument opisuje prijenos, a da ne tvrdi da je pravno uređen.
> 2. **Pravne osnove** navedene u §7, osobito podjela između privole i legitimnog interesa za uslugu pristupačnosti.
> 3. **Najniža dob** (16 godina) i njezina usklađenost s upitnikom za klasifikaciju sadržaja Google Playa.
> 4. **Napomena o umjetnoj inteligenciji** na temelju europske uredbe o umjetnoj inteligenciji (obveza transparentnosti za sustav ograničenog rizika).

---

Ovaj je dokument prijevod francuske verzije, dostupne na adresi https://readit0.github.io/plume-legal/. Pružen je radi vaše obavijesti. U slučaju odstupanja obratite nam se na sogacmoi7@gmail.com.
