# Pravila o privatnosti aplikacije Plume

**Zadnje ažurirano: 12. septembar 2026.** — Verzija 2.0

> *Šta se promijenilo od verzije 1.0, i zašto možda ponovo vidite ekran za prihvatanje u aplikaciji:* ispravljamo dvije tvrdnje koje više nisu bile tačne. Prvo, funkcija **lični jezici** čuva na našim serverima sadržaj koji kreirate (naziv, alfabet, rječnik) — verzija 1.0 je pogrešno tvrdila da se nikakav tekst ne pohranjuje. Drugo, sada koristimo alat za **tehnički izvještaj o padu aplikacije** — verzija 1.0 je tvrdila da takav alat ne postoji. Detalji o ove dvije tačke nalaze se u odjeljku „Za jedan minut" ispod, kao i u §3 i §9. To su tačno dvije kategorije promjena koje, u aplikaciji, pokreću novi zahtjev za saglasnost (vidi §11).

---

## Ko je odgovoran za vaše podatke

**SASU RedLine Music**
SIREN 938 277 100 — SIRET `938 277 100 00013`
Abbaye 208-1, 208 Résidence Lavoisier, 18100 Vierzon, France
Kontakt: sogacmoi7@gmail.com

Aplikacija je objavljena na Google Play-u pod imenom izdavača **openfunworld**.

Ova pravila opisuju šta aplikacija Plume radi u svojoj trenutnoj verziji. Napisana su na osnovu čitanja koda aplikacije, a ne prema generičkom obrascu.

---

## Za jedan minut

Plume vam pomaže da pišete: preformuliše vaš tekst direktno u aplikaciji u kojoj kucate, i može prevesti tekst prikazan na ekranu.

Tri stvari koje treba zapamtiti:

1. **Plume ne čuva ni tekstove koje preformulišete, ni tekst pročitan na ekranu.** Ne čuvamo ni kopiju, ni zapisnik. **Svjesan i namjeran izuzetak:** ako kreirate **lični jezik** (vaš vlastiti izmišljeni jezik, sa rječnikom riječi i njihovih definicija), sadržaj tog jezika **se** čuva na našim serverima — to je jedini način da vam omogućimo da ga pronađete na drugom uređaju, da ga razvijate i da ga dijelite. Detalji su u §3.
2. **U zavisnosti od motora koji odaberete, vaš tekst napušta ili ne napušta vaš telefon.** Dva motora (lokalni Kit i lokalna VI) rade u potpunosti na uređaju. Treći (Cloud VI) šalje tekst servisu vještačke inteligencije koji se **nalazi izvan Evropske unije**. Vi birate, a Cloud VI se nikada ne aktivira bez vaše izričite saglasnosti.
3. **Plume-u su potrebne moćne dozvole** (čitanje sadržaja prikazanog u drugim aplikacijama, snimanje ekrana). U nastavku precizno objašnjavamo čemu služe, a čemu ne.

---

## 1. Šta Plume čita na vašem ekranu, i kada

### 1.1 Usluga pristupačnosti

Da bi prepisao vaš tekst na mjestu gdje ga pišete, Plume koristi Android-ovu uslugu pristupačnosti. To je dozvola koju sami aktivirate, u podešavanjima telefona, nakon ekrana sa objašnjenjem koji vam Plume prikazuje prije nego što je zatraži.

Konkretno:

- **U mirovanju**, Plume zna samo koja je aplikacija otvorena i u kom trenutku postavljate kursor u polje za unos. To je ono što izaziva pojavljivanje plutajuće kapsule — i to samo u aplikacijama koje ste sami podesili.
- **Sadržaj polja se čita samo u tačnom trenutku kada dodirnete kapsulu**, da bi bio prepisan i zatim zamijenjen na mjestu.
- **Polja za lozinku su isključena.** Aplikacija detektuje polja tipa lozinke (uključujući numeričke kodove i web polja) i odbija da ih čita.
- Ova dozvola **ne omogućava nikakvo snimanje slike** vašeg ekrana.
- Plume **nikada ne pritiska umjesto vas** u drugoj aplikaciji: zamjenjuje tekst u polju, ništa drugo.

Dvije funkcije koje sami aktivirate — Asistirano čitanje u tekstualnom režimu i prevod primljenih poruka — kontinuirano čitaju prikazani tekst dok rade, i prestaju čim ih isključite.

Ako odbijete uslugu pristupačnosti, Plume ostaje upotrebljiv: možete odabrati tekst i koristiti Android-ov meni za odabir „Plume", ili podijeliti tekst sa Plume-om.

### 1.2 Snimanje ekrana (Asistirano čitanje)

Asistirano čitanje postavlja prevod preko prikazanog teksta — na primjer, oblačiće u stripu. Potrebno mu je da vidi sliku ekrana.

- **Podrazumijevano je isključena** i radi samo u aplikacijama koje ste izričito odobrili, jednu po jednu.
- **Android traži svoju vlastitu saglasnost pri svakom pokretanju sesije.** To nije dozvola data jednom zauvijek: svaka sesija zahtijeva novu saglasnost. Plume nikada ne pokušava ponovo iskoristiti ili zaobići tu saglasnost.
- Tokom cijele sesije, **trajno obavještenje i sistemski indikator ostaju vidljivi**. Plume ne može diskretno snimati vaš ekran.
- Sesija se automatski zaustavlja pri zaključavanju ekrana, i odmah kada je sami zaustavite.
- Aplikacije koje štite svoj prikaz (bankovne aplikacije, upravljači lozinkama) sam Android sakriva prije nego što Plume bilo šta primi. To je stvarna, ali djelimična zaštita sistema: sve osjetljive aplikacije je ne aktiviraju. Zato je ne predstavljamo kao apsolutnu garanciju.
- Snimljene slike se nikada ne čuvaju niti šalju. Svaka slika se analizira u memoriji radi izdvajanja teksta, a zatim se odbacuje. Nijedna slika nikada ne napušta vaš telefon, bez obzira koji je motor odabran.

---

## 2. Šta ostaje na vašem telefonu, a šta odlazi

Ovo je najvažnija razlika u ovim pravilima, i vi je kontrolišete.

### 2.1 Motori koji ništa ne šalju napolje

- **Lokalni Kit** (prepoznavanje i prevod teksta van mreže) radi u potpunosti na uređaju.
- **Lokalna VI** je model vještačke inteligencije koji se preuzima jednom, a zatim čuva na vašem telefonu (oko 720 MB). Izvršava se na vašem uređaju.

Sa ova dva motora, pročitani ili preformulisani tekst ne napušta vaš telefon. Ne postoji nikakav mrežni poziv povezan sa sadržajem vašeg teksta.

### 2.2 Cloud VI motor

Kada odaberete Cloud VI, ili kada vaš uređaj nije dovoljno snažan za lokalnu VI, odgovarajući tekst se prenosi na naše servere, a zatim na servis vještačke inteligencije treće strane.

Potrebno je biti jasan u vezi sa stvarnim putem:

- Tekst prolazi kroz našu serversku infrastrukturu, smještenu u Evropskoj uniji (region Centralna Evropa, Frankfurt).
- Zatim se prenosi na posrednika za usmjeravanje koji se nalazi izvan Evropske unije, koji ga obrađuje putem modela vještačke inteligencije treće strane.
- Riječ je, dakle, o prenosu podataka izvan Evropske unije. Ne tvrdimo suprotno, i ne dajemo nikakvo obećanje o evropskom smještaju za ovaj korak.
- Plume ne čuva vaš tekst. Nijedna od naših serverskih funkcija ne zapisuje sadržaj vašeg teksta: bilježimo samo tehnički identifikator zahtjeva i identifikator vašeg uređaja, radi brojanja vaše kvote i otkrivanja zloupotreba.
- Ne možemo garantovati šta ovi pružaoci usluga rade sa svoje strane. Radije vam to kažemo nego da vam obećavamo nulto zadržavanje podataka koje nismo u mogućnosti provjeriti.

Cloud VI se nikada ne aktivira sama od sebe. Poseban ekran za saglasnost objašnjava vam ove tačke prije prvog slanja, i ništa ne odlazi dok ne prihvatite. Ako lokalna VI ne uspije, Plume ne prebacuje na cloud u tišini: obavještava vas i čeka vašu odluku. Ovu saglasnost možete opozvati u bilo kom trenutku u podešavanjima.

Poslati tekst je ograničen: 1.200 znakova za preformulaciju, 4.000 znakova za analizu ekrana.

---

## 3. Podaci koje čuvamo

Ne koristimo nikakav alat za analizu publike niti bilo kakav reklamni tragač treće strane, osim reklama opisanih u §5. Koristimo alat za tehnički izvještaj o padu aplikacije: on vidi samo greške u programu (tip greške, tehnički stek poziva, verziju aplikacije, operativni sistem), nikada vašu upotrebu niti vaš put kroz aplikaciju, i nikada tekst koji pišete — poseban filter mu to zabranjuje prije bilo kakvog slanja. Detalji su u §9.

Evo cjelokupnog sadržaja koji se čuva na našim serverima:

| Podatak | Zašto | Trajanje |
|---|---|---|
| **Identifikator uređaja** (nasumični broj koji generiše Plume, bez veze sa vašim identitetom ili reklamnim identifikatorom) | Povezivanje uređaja sa računom, primjena kvota, blokiranje zloupotreba | Do brisanja vašeg računa |
| **E-mail adresa računa** (ako kreirate račun putem e-maila ili preko Google-a) | vaša autentifikacija, povezivanje vaše pretplate | Do brisanja vašeg računa |
| **Brojači upotrebe** (broj preformulacija dnevno i mjesečno — brojevi, ne tekstovi) | Primjena kvota | Do brisanja vašeg računa |
| **Historija kupovine** (identifikator Google Play transakcije, datumi, status pretplate) | Omogućavanje pristupa onome što ste platili, upravljanje obnovama, poštovanje naših računovodstvenih obaveza | Čuva se i nakon brisanja računa, ali **odvojeno od vašeg identiteta** (vidi §6) |
| **Prijedlozi poslani dobrovoljno** (ako nam pišete prijedlog persone iz aplikacije) | Poboljšanje kataloga. Ovi prijedlozi se nikada ne objavljuju. | Do brisanja vašeg računa |
| **Tehnički signali zloupotrebe** (ponovljena prekoračenja, neuspjeh provjere integriteta — bez ikakvog teksta) | Sigurnost, borba protiv prevare | Odvojeni od vašeg identiteta pri brisanju računa |
| **Jezik i verzija aplikacije** | Pružanje odgovarajućeg sadržaja | Do brisanja vašeg računa |
| **Sadržaj ličnih jezika koje kreirate** (njegov naziv, alfabet i rječnik — riječi i definicije koje ste vi, ili druge osobe, tu napisali) | Omogućavanje da pronađete svoj jezik na drugom uređaju, da ga razvijate, i da ga dijelite sa drugim korisnicima | Sve dok jezik postoji. Ako ga obrišete, njegov zapis nestaje — ali kopija koju je već **uvezla druga osoba** sada pripada njoj i **opstaje**, poput poruke koju je treća strana već primila, a koju ne možemo obrisati kod nje |
| **Tehnički izvještaji o padu aplikacije** (tip greške, skraćeni tehnički stek poziva, verzija aplikacije, operativni sistem — nikada sadržaj teksta) | Dijagnostika i ispravka padova aplikacije | Uređuje naš pružalac usluga izvještavanja o padovima (vidi §9). Ovo prikupljanje podliježe vašoj saglasnosti i prekidaču koji možemo isključiti u bilo kom trenutku, bez ažuriranja aplikacije |

Šta ne prikupljamo: vaše ime, vaše kontakte, vašu lokaciju, vaš adresar, vaše fotografije, vaš kalendar, historiju vaših aplikacija. Plume ne traži nijednu od ovih dozvola.

Šta ostaje isključivo na vašem telefonu: vaše prilagođene persone i njihovi avatari, vaša podešavanja, vaša pravila po aplikaciji, keš prevoda Asistiranog čitanja (briše se na kraju svake sesije). Ništa od ovoga se ne šalje na naše servere.

---

## 4. Glasovno diktiranje

Dugme mikrofona vam omogućava da diktirate umjesto da kucate. Dozvola za pristup mikrofonu se traži u tačnom trenutku kada pritisnete to dugme, nikada pri pokretanju, a mikrofon se otvara samo u tom trenutku. Plume nikada ne sluša u pozadini.

Plume ne prima, ne čuva niti prenosi nikakav audio zapis. Diktiranje se povjerava motoru za prepoznavanje glasa ugrađenom u vaš telefon (Android-ovom). Plume dobija samo transkribovani tekst.

Važna i iskrena napomena: ovaj sistemski motor pripada vašem telefonu, obično Google-u. U zavisnosti od vašeg uređaja, njegovih podešavanja i instaliranih jezičkih modula, on može prenijeti audio zapis na servere svog izdavača radi transkripcije. Ova obrada je van dosega Plume-a i podliježe pravilima o privatnosti izdavača vašeg sistema. Zato ne možemo tvrditi da vaš glas ostaje na uređaju — to zavisi od vašeg telefona, a ne od nas.

Ako odbijete dozvolu za mikrofon, unos putem tastature naravno ostaje dostupan.

---

## 5. Reklame

Usluga je besplatna do određenog dnevnog ograničenja upotrebe. Nakon toga, možete odabrati da pogledate nagradnu reklamu kako biste otključali dodatne upotrebe. To nikada nije obavezno: ako ne pogledate reklamu, jednostavno zadržavate ono na šta imate pravo.

- Reklame pruža Google AdMob.
- Pojavljuju se isključivo unutar same aplikacije Plume, nikada u plutajućoj kapsuli i nikada preko druge aplikacije.
- Pretplatnici ne vide nikakve reklame.
- U Evropskom ekonomskom prostoru, Ujedinjenom Kraljevstvu i Švicarskoj, prije prve reklame vam se prikazuje obrazac za saglasnost koji pruža platforma certifikovana od strane Google-a. Dok se vaš izbor ne prikupi, nijedna reklama se ne prikazuje. Ako odbijete, reklame ostaju nepersonalizovane i nijedna funkcija vam se ne oduzima. Ovaj izbor možete promijeniti u bilo kom trenutku iz podešavanja.
- Kako bi se vaša nagrada pouzdano dodijelila, vaš Plume identifikator uređaja se prenosi AdMob-u. Google može, osim toga, prikupljati vlastite podatke u skladu sa svojim pravilima o privatnosti.

*Na dan pisanja, prikazivanje reklama je isključeno na strani servera. Ovaj odjeljak opisuje funkcionisanje čim bude aktivirano.*

---

## 6. Pretplate i kupovine

Pretplate i paketi se prodaju putem Google Play-a. Nikada ne vidimo vaše bankovne podatke: njima upravlja Google, koji je prodavac u smislu fakturisanja.

Od Google-a dobijamo dokaz o kupovini koji naš server provjerava, i čuvamo njegov trag (identifikator transakcije, datumi, status). Ovaj trag se čuva iz računovodstvenih razloga i kako bi se spriječilo da ista kupovina posluži dva puta — ali se odvaja od vašeg identiteta kada obrišete svoj račun.

---

## 7. vaša prava

Imate pravo na pristup, ispravku, brisanje, ograničenje, prigovor i prenosivost podataka, predviđeno Opštom uredbom o zaštiti podataka (GDPR).

**Najjednostavnije i najbrže: brisanje je ugrađeno u aplikaciju.**
Postavke → Privatnost → Obriši moje podatke. Izvršava se odmah, ne stavlja se u red čekanja. Detalji o tome šta se briše, a šta čuva, nalaze se na našoj posvećenoj stranici: `https://readit0.github.io/plume-legal/suppression-compte`.

Svoj račun možete obrisati i bez instaliranja aplikacije, pisanjem na sogacmoi7@gmail.com.

Za bilo koji drugi zahtjev, pišite na sogacmoi7@gmail.com. Odgovaramo u roku od mjesec dana.

**Pravni osnovi:** izvršenje ugovora (pružanje usluge koju tražite, upravljanje vašom pretplatom), vaša saglasnost (usluga pristupačnosti, snimanje ekrana, slanje ka Cloud VI, personalizovane reklame), naš legitimni interes (sigurnost, borba protiv prevare) i naše zakonske obaveze (računovodstvo).

Možete podnijeti žalbu francuskom regulatornom tijelu CNIL (www.cnil.fr), nadzornom tijelu izdavača, ili, **ako živite u Evropskoj uniji**, nadzornom tijelu vaše zemlje prebivališta — član 77. GDPR-a vam ostavlja taj izbor.

---

## 8. Maloljetnici

Plume je alat za pomoć pri pisanju, namijenjen korisnicima od 16 godina naviše. Svjesno ne prikupljamo podatke maloljetnika mlađih od 16 godina, a aplikacija nije osmišljena niti promovisana za njih. Ako ste nosilac roditeljskog prava i mislite da nam je vaše dijete proslijedilo podatke, pišite na sogacmoi7@gmail.com: obrisaćemo račun.

Pošto aplikacija omogućava preformulisanje slobodnog teksta i prikazuje reklame, nije podobna za programe namijenjene porodicama na Google Play-u.

---

## 9. Podizvođači i primaoci podataka

| Pružalac usluga | Uloga | Gdje |
|---|---|---|
| **Naš pružalac usluga hostinga** | Hosting baze podataka, autentifikacija, serverske funkcije | Evropska unija (Frankfurt) |
| **Naš pružalac usluga obrade VI** | Usmjeravanje zahtjeva i obrada teksta modelom vještačke inteligencije treće strane | **Izvan Evropske unije** |
| **Google Play / Google Billing** | Plaćanje, pretplate | Google Ireland / Sjedinjene Američke Države |
| **Google AdMob** | Nagradne reklame | Google Ireland / Sjedinjene Američke Države |
| **Google** (sistemske usluge telefona) | Prepoznavanje glasa, moduli za prevod van mreže | Zavisno od vašeg uređaja |
| **Naš pružalac usluga izvještavanja o padovima** | Tehnički izvještaj o padu aplikacije — samo greške u programu, filtrirane prije slanja: nikada vaš tekst | Sjedinjene Američke Države |

Ne prodajemo nikakve podatke i ne ustupamo ih posrednicima za podatke.

Prenosi izvan Evropske unije: korištenje našeg pružaoca usluga obrade VI, Google Play-a, AdMob-a i našeg pružaoca usluga izvještavanja o padovima podrazumijeva prenos podataka izvan Evropske unije.

---

## 10. Sigurnost

Razmjena podataka između aplikacije i naših servera je šifrirana (HTTPS/TLS). Pristup podacima u bazi je ograničen serverskim pravilima: osjetljive funkcije nisu dostupne iz aplikacije. Nijedan sistem nije potpuno siguran. Tekst koji preformulišete i onaj koji Asistirano čitanje prikazuje na ekranu ne čuvaju se kod nas, što mehanički ograničava ono što bi upad mogao otkriti o njima. **Ovo nije tačno za sve:** rječnik ličnih jezika koje kreirate se, naprotiv, **čuva** (vidi §3), i bio bi izložen kao bilo koji drugi podatak iz ovih pravila u slučaju stvarnog upada — štitimo ga istim serverskim pravilima pristupa kao i ostalo.

---

## 11. Izmjene

Svaka izmjena ovih pravila biće objavljena na adresi `https://readit0.github.io/plume-legal` sa novim datumom. U slučaju važne promjene u vezi sa kretanjem vaših podataka, obavijestićemo vas o tome u aplikaciji.

**Od verzije 2.0, ovo obećanje ima konkretan mehanizam iza sebe.** Jednostavna formalna ispravka (datum, adresa, preciziranje) od vas ne traži ništa dodatno. Ali SUŠTINSKA promjena — novi primalac vaših podataka, nova kategorija prikupljenih podataka, nova svrha, ili promjena vaših prava ili cijene — ponovo prikazuje, jednom, ekran za prihvatanje u aplikaciji, sa sažetkom onoga što se mijenja i oba ažurirana dokumenta. Upravo se to dogodilo za ovu verziju 2.0 (vidi okvir na početku ovog dokumenta).

---

## Uslovi korištenja

Uslovi korištenja usluge (kvote, pretplate, otkazivanje) nalaze se u zasebnom dokumentu: `https://readit0.github.io/plume-legal/conditions-generales`.

---
