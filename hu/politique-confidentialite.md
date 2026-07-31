# A Plume adatkezelési tájékoztatója

**Utolsó frissítés: 2026. július 31.** — 1.0-s verzió

---

## Ki kezeli az Ön adatait

**SASU RedLine Music**
SIREN 938 277 100 — SIRET `938 277 100 00013`
Abbaye 208-1, 208 Résidence Lavoisier, 18100 Vierzon, France
Kapcsolat: sogacmoi7@gmail.com

Az alkalmazást a Google Play áruházban az **openfunworld** kiadói néven tesszük közzé.

Ez a tájékoztató azt írja le, mit tesz a Plume alkalmazás a jelenlegi verziójában. Az alkalmazás kódjának elolvasásával készült, nem pedig egy általános minta alapján.

---

## Egy percben

A Plume az írásban segíti Önt: átfogalmazza a szövegét közvetlenül abban az alkalmazásban, amelyben éppen gépel, és le tudja fordítani a képernyőn megjelenő szöveget.

Három dolgot érdemes megjegyezni:

1. **A Plume egyetlen szövegét sem őrzi meg a szerverein.** Sem az átfogalmazott szövegeit, sem a képernyőről beolvasott szöveget. Nem tartunk meg róluk sem másolatot, sem naplóbejegyzést.
2. **Attól függően, hogy melyik motort választja, a szövege elhagyja a telefonját, vagy nem.** Két motor (a Helyi Kit és a Helyi MI) teljes egészében a készüléken dolgozik. A harmadik (a Felhő MI) elküldi a szöveget egy **az Európai Unión kívül található** mesterségesintelligencia-szolgáltatásnak. A választás az Öné, és a Felhő MI soha nem aktiválódik az Ön kifejezett hozzájárulása nélkül.
3. **A Plume erős engedélyeket igényel** (a más alkalmazásokban megjelenő tartalom olvasása, a képernyő rögzítése). Az alábbiakban pontosan elmagyarázzuk, mire szolgálnak, és mire nem.

---

## 1. Mit olvas a Plume az Ön képernyőjén, és mikor

### 1.1 A kisegítő lehetőségek szolgáltatása

Ahhoz, hogy a szövegét ott írja át, ahol Ön írja, a Plume az Android kisegítő lehetőségek szolgáltatását használja. Ezt az engedélyt Ön maga kapcsolja be a telefon beállításaiban, egy magyarázó képernyő után, amelyet a Plume **azelőtt** mutat meg Önnek, hogy kérné.

Konkrétan:

- **Nyugalmi állapotban** a Plume csak azt tudja, melyik alkalmazás van megnyitva, és mikor helyezi a kurzort egy beviteli mezőbe. Ettől jelenik meg a lebegő kapszula — és kizárólag azokban az alkalmazásokban, amelyeket Ön maga állított be.
- **A mező tartalmát csak abban a pillanatban olvassa be, amikor Ön megérinti a kapszulát**, hogy átírja, majd helyben lecserélje.
- **A jelszómezők ki vannak zárva.** Az alkalmazás felismeri a jelszó típusú mezőket (beleértve a számkódokat és a webes mezőket is), és nem hajlandó beolvasni őket.
- Ez az engedély **semmilyen képfelvételt nem tesz lehetővé** az Ön képernyőjéről.
- A Plume **soha nem nyom meg semmit Ön helyett** egy másik alkalmazásban: lecseréli egy mező szövegét, semmi mást.

Két olyan funkció, amelyet Ön maga kapcsol be — a **Segített Olvasás Szöveg módban** és a **beérkező üzenetek fordítása** —, folyamatosan olvassa a megjelenített szöveget, amíg fut, és leáll, amint Ön kikapcsolja.

Ha elutasítja a kisegítő lehetőségek szolgáltatását, a Plume továbbra is használható: kijelölhet egy szöveget, és használhatja az Android kijelölési menüjének „Plume” pontját, vagy megoszthat egy szöveget a Plume-mal.

### 1.2 A képernyő rögzítése (Segített Olvasás)

A Segített Olvasás egy fordítást helyez a megjelenített szöveg fölé — például egy képregény szövegbuborékjai fölé. Ehhez látnia kell a képernyő képét.

- **Alapértelmezés szerint ki van kapcsolva**, és csak azokban az alkalmazásokban működik, amelyeket Ön kifejezetten, egyenként engedélyezett.
- **Az Android minden munkamenet indításakor kéri a saját hozzájárulását.** Ez nem egyszer s mindenkorra megadott engedély: minden munkamenet új hozzájárulást igényel. A Plume soha nem próbálja újrafelhasználni vagy megkerülni ezt a hozzájárulást.
- A munkamenet teljes ideje alatt **egy állandó értesítés és egy rendszerjelzés marad látható**. A Plume nem tudja észrevétlenül rögzíteni az Ön képernyőjét.
- A munkamenet **a képernyő zárolásakor automatikusan leáll**, és azonnal leáll akkor is, ha Ön maga állítja le.
- Azokat az alkalmazásokat, amelyek védik a megjelenítésüket (banki alkalmazások, jelszókezelők), **maga az Android takarja ki**, mielőtt a Plume bármit is megkapna. Ez a rendszer védelme, valós, de részleges: nem minden érzékeny alkalmazás kapcsolja be. Ezért nem mutatjuk be abszolút garanciaként.
- **A rögzített képeket soha nem mentjük el és nem küldjük el.** Minden képet a memóriában elemzünk a szöveg kinyeréséhez, majd elvetjük. Egyetlen kép sem hagyja el a telefonját, soha, bármelyik motort is választotta.

---

## 2. Mi marad a telefonján, és mi távozik

Ez a tájékoztató legfontosabb megkülönböztetése, és Ön az, aki ellenőrzése alatt tartja.

### 2.1 Azok a motorok, amelyek semmit nem küldenek ki

- **A Helyi Kit** (offline szövegfelismerés és -fordítás) teljes egészében a készüléken működik.
- **A Helyi MI** egy mesterségesintelligencia-modell, amelyet egyszer tölt le, majd a telefonján tárol (körülbelül 720 MB). A készülékén fut.

Ezzel a két motorral **a beolvasott vagy átfogalmazott szöveg nem hagyja el a telefonját.** A szövege tartalmához nem kapcsolódik semmilyen hálózati hívás.

### 2.2 A Felhő MI motor

Amikor a Felhő MI-t választja, vagy amikor a készüléke nem elég erős a Helyi MI-hez, az érintett szöveget továbbítjuk a szervereinkre, majd egy harmadik fél mesterségesintelligencia-szolgáltatásának.

**A valódi útvonalról világosan kell beszélni:**

- A szöveg áthalad az infrastruktúránkon (Supabase), amely az **Európai Unióban** (közép-európai régió, Frankfurt) található.
- Ezután továbbítjuk az **openrouter.ai** részére, amely egy **az Európai Unión kívül található** útválasztó közvetítő, és amely a **Mistral Small** modellel dolgoztatja fel.
- **Ez tehát adattovábbítás az Európai Unión kívülre.** Nem állítjuk az ellenkezőjét, és erre a lépésre nem hirdetünk semmiféle európai tárhelyre vonatkozó ígéretet.
- **A Plume nem őrzi meg az Ön szövegét.** Egyik szerverfüggvényünk sem írja ki a szövege tartalmát: kizárólag egy technikai kérésazonosítót és a készüléke azonosítóját rögzítjük, hogy számon tartsuk a kvótáját, és felderítsük a visszaéléseket.
- **Azt, hogy ezek a szolgáltatók a maguk részéről mit tesznek, nem tudjuk garantálni.** Inkább megmondjuk Önnek, mintsem hogy nulla adatmegőrzést ígérjünk, amelyet nem áll módunkban ellenőrizni.

**A Felhő MI soha nem kapcsol be magától.** Egy külön hozzájárulási képernyő elmagyarázza Önnek ezeket a pontokat az első küldés előtt, és semmi nem indul el mindaddig, amíg Ön nem fogadta el. Ha a Helyi MI nem jár sikerrel, a Plume nem vált át csendben a felhőre: jelzi Önnek, és megvárja a döntését. Ezt a hozzájárulást bármikor visszavonhatja a beállításokban.

Az elküldött szöveg felső korláthoz kötött: 1 200 karakter egy átfogalmazásnál, 4 000 karakter egy képernyőelemzésnél.

---

## 3. Az általunk megőrzött adatok

**Semmilyen látogatottságelemző eszközt, semmilyen harmadik féltől származó hirdetési nyomkövetőt, semmilyen összeomlás-jelentő eszközt nem használunk.** Az alkalmazás nem tartalmaz mérési SDK-t.

Íme mindaz, amit a szervereinken tárolunk:

| Adat | Miért | Időtartam |
|---|---|---|
| **Készülékazonosító** (a Plume által generált véletlenszerű szám, amely nem áll kapcsolatban sem az Ön személyazonosságával, sem hirdetési azonosítóval) | Készülék fiókhoz rendelése, a kvóták alkalmazása, a visszaélések blokkolása | A fiókja törléséig |
| **A fiók e-mail-címe** (ha e-mailben vagy Google-fiókkal hoz létre fiókot) | Az Ön hitelesítése, az előfizetése hozzárendelése | A fiókja törléséig |
| **Használati számlálók** (az átfogalmazások napi és havi száma — számok, nem szövegek) | A kvóták alkalmazása | A fiókja törléséig |
| **Vásárlási előzmények** (Google Play tranzakcióazonosító, dátumok, az előfizetés állapota) | Hozzáférés biztosítása ahhoz, amiért fizetett, a megújítások kezelése, számviteli kötelezettségeink teljesítése | A fiók törlése után is megőrizzük, de **az Ön személyazonosságától elválasztva** (lásd a 6. pontot) |
| **Önként elküldött javaslatok** (ha az alkalmazásból persona-javaslatot ír nekünk) | A katalógus fejlesztése. Ezeket a javaslatokat soha nem tesszük közzé. | A fiókja törléséig |
| **Visszaélésre utaló technikai jelzések** (ismételt túllépések, sikertelen integritás-ellenőrzés — mindenféle szöveg nélkül) | Biztonság, csalás elleni küzdelem | A fiók törlésekor elválasztjuk őket az Ön személyazonosságától |
| **Az alkalmazás nyelve és verziója** | A megfelelő tartalom kiszolgálása | A fiókja törléséig |

**Amit nem gyűjtünk:** az Ön nevét, a névjegyeit, a tartózkodási helyét, a címjegyzékét, a fényképeit, a naptárát, az alkalmazásai előzményeit. A Plume egyik ilyen engedélyt sem kéri.

**Ami kizárólag a telefonján marad:** az egyéni personái és azok avatarjai, a beállításai, az alkalmazásonkénti szabályai, a Segített Olvasás fordítási gyorsítótára (amely minden munkamenet végén törlődik). Ezek közül semmit nem küldünk el a szervereinkre.

---

## 4. A hangdiktálás

Egy mikrofongomb lehetővé teszi, hogy gépelés helyett diktáljon. A mikrofonhoz való hozzáférés engedélyét **pontosan abban a pillanatban kérjük, amikor Ön megnyomja ezt a gombot**, soha nem indításkor, és a mikrofon is csak ekkor nyílik meg. A Plume soha nem hallgatózik a háttérben.

**A Plume semmilyen hangfelvételt nem kap, nem tárol és nem továbbít.** A diktálást a telefonjába épített beszédfelismerő motorra (az Android motorjára) bízza. A Plume csak az átírt szöveget veszi át.

**Fontos és őszinte megjegyzés:** ez a rendszermotor az Ön telefonjához tartozik, általában a Google-hoz. A készülékétől, annak beállításaitól és a telepített nyelvi moduloktól függően **továbbíthatja a hangot a gyártója szervereinek** az átíráshoz. Ez az adatkezelés kívül esik a Plume hatáskörén, és a rendszere gyártójának adatkezelési tájékoztatója alá tartozik. Ezért nem állíthatjuk, hogy a hangja a készüléken marad — ez a telefonjától függ, nem tőlünk.

Ha elutasítja a mikrofonengedélyt, a billentyűzetes bevitel természetesen továbbra is elérhető marad.

---

## 5. Hirdetések

A szolgáltatás egy bizonyos napi használati korlátig ingyenes. Ezen felül **választhatja** azt, hogy megnéz egy jutalmazott hirdetést további használatok feloldásáért. Ezt soha nem írjuk elő: ha nem néz hirdetést, egyszerűen megtartja azt, ami jár Önnek.

- A hirdetéseket a **Google AdMob** szolgáltatja.
- **Kizárólag magában a Plume alkalmazásban** jelennek meg, soha nem a lebegő kapszulában és soha nem egy másik alkalmazás fölött.
- **Az előfizetők egyetlen hirdetést sem látnak.**
- Az Európai Gazdasági Térségben, az Egyesült Királyságban és Svájcban **az első hirdetés előtt** egy Google által tanúsított platform által biztosított hozzájárulási űrlapot jelenítünk meg Önnek. Amíg az Ön választását nem gyűjtöttük be, egyetlen hirdetést sem kérünk le. Ha elutasítja, a hirdetések **nem személyre szabottak** maradnak, és **semmilyen funkciót nem vonunk meg Öntől**. Ezt a választását bármikor módosíthatja a beállításokból.
- Ahhoz, hogy a jutalmát megbízhatóan jóváírjuk, a Plume készülékazonosítóját továbbítjuk az AdMobnak. A Google egyebekben a saját adatkezelési tájékoztatójának megfelelően gyűjtheti a saját adatait.

*A szöveg írásának időpontjában a hirdetések megjelenítése a szerveroldalon ki van kapcsolva. Ez a szakasz azt írja le, hogyan fog működni, amint bekapcsoljuk.*

---

## 6. Előfizetések és vásárlások

Az előfizetéseket és a csomagokat **a Google Play útján** értékesítjük. Soha nem látjuk a bankkártyaadatait: azokat a Google kezeli, amely a számlázás értelmében az eladó.

A Google-tól vásárlási igazolást kapunk, amelyet a szerverünk ellenőriz, és amelyről nyomot őrzünk meg (tranzakcióazonosító, dátumok, állapot). Ezt a nyomot számviteli okokból őrizzük meg, valamint azért, hogy megakadályozzuk ugyanannak a vásárlásnak a kétszeri felhasználását — de **elválasztjuk az Ön személyazonosságától**, amikor törli a fiókját.

---

## 7. Az Ön jogai

Önt megilleti a GDPR szerinti hozzáférés joga, a helyesbítéshez, a törléshez, az adatkezelés korlátozásához, a tiltakozáshoz és az adathordozhatósághoz való jog.

**A legegyszerűbb és a leggyorsabb: a törlés be van építve az alkalmazásba.**
Beállítások → Adatvédelem → Adataim törlése. A törlés **azonnal végrehajtódik**, nem kerül várólistára. Annak részletezését, hogy mi törlődik és mi marad meg, külön oldalunk tartalmazza: `https://readit0.github.io/plume-legal/suppression-compte`.

A fiókját **az alkalmazás telepítése nélkül** is törölheti, ha ír a sogacmoi7@gmail.com címre.

Minden egyéb kérés esetén írjon a **sogacmoi7@gmail.com** címre. Egy hónapon belül válaszolunk.

**Jogalapok:** a szerződés teljesítése (az Ön által kért szolgáltatás nyújtása, az előfizetése kezelése), az Ön hozzájárulása (kisegítő lehetőségek szolgáltatása, képernyőrögzítés, a Felhő MI-nek való elküldés, személyre szabott hirdetések), a jogos érdekünk (biztonság, csalás elleni küzdelem) és a jogi kötelezettségeink (számvitel).

Panasszal fordulhat a **CNIL**-hez (www.cnil.fr), amely a kiadó felügyeleti hatósága, vagy, **ha az Európai Unióban rendelkezik lakóhellyel**, a lakóhelye szerinti ország felügyeleti hatóságához — a GDPR 77. cikke Önre bízza a választást.

---

## 8. A kiskorúak

A Plume fogalmazást segítő eszköz, amely **16 éves és idősebb** közönségnek szól. Tudatosan nem gyűjtünk 16 év alatti gyermekektől származó adatokat, és az alkalmazást nem nekik terveztük, illetve nem nekik hirdetjük. Ha Ön szülői felügyeletet gyakorol, és úgy véli, hogy a gyermeke adatokat továbbított nekünk, írjon a sogacmoi7@gmail.com címre: töröljük a fiókot.

Mivel az alkalmazás lehetővé teszi szabad szöveg átfogalmazását és hirdetéseket jelenít meg, nem felel meg a Google Play családoknak szóló programjai feltételeinek.

---

## 9. Adatfeldolgozók és címzettek

| Szolgáltató | Szerep | Hol |
|---|---|---|
| **Supabase** | Az adatbázis tárhelye, hitelesítés, szerverfüggvények | Európai Unió (Frankfurt) |
| **OpenRouter** | A kérések továbbítása az MI-modell felé | **Az Európai Unión kívül** |
| **Mistral AI** (az OpenRouteren keresztül) | A szöveget feldolgozó modell (Mistral Small) | Feldolgozás a fenti közvetítőn keresztül |
| **Google Play / Google Billing** | Fizetés, előfizetések | Google Ireland / Egyesült Államok |
| **Google AdMob** | Jutalmazott hirdetések | Google Ireland / Egyesült Államok |
| **Google (a telefon rendszerszolgáltatásai)** | Beszédfelismerés, offline fordítási modulok | A készülékétől függően |

**Semmilyen adatot nem adunk el, és semmilyen adatot nem adunk át adatkereskedőknek.**

**Adattovábbítás az Európai Unión kívülre:** az OpenRouter, a Google Play és az AdMob igénybevétele adattovábbítással jár az Európai Unión kívülre. Ezen adattovábbítások jogi kereteit (általános adatvédelmi kikötések, megfelelőségi határozat) **a közzététel előtt szakembernek kell ellenőriznie és dokumentálnia** — lásd a dokumentum végén lévő megjegyzést.

---

## 10. Biztonság

Az alkalmazás és a szervereink közötti adatcserét titkosítjuk (HTTPS/TLS). Az adatbázisban tárolt adatokhoz való hozzáférést szerveroldali szabályok korlátozzák: az érzékeny funkciók az alkalmazásból nem érhetők el. Egyetlen rendszer sem tökéletesen biztonságos, de az Ön által átfogalmazott szövegek egyikét sem tároljuk nálunk — ez pedig eleve korlátozza azt, amit egy behatolás felfedhetne.

---

## 11. Módosítások

A jelen tájékoztató minden módosítását a `https://readit0.github.io/plume-legal` címen tesszük közzé, új dátummal. Ha lényegesen változik az adatai áramlása, arról az alkalmazásban tájékoztatjuk Önt.

---

## Általános feltételek

A szolgáltatás használati feltételeit (kvóták, előfizetések, felmondás) külön dokumentum tartalmazza: `https://readit0.github.io/plume-legal/conditions-generales`.

---

> ### Szakemberrel átnézendő
>
> Ez a dokumentum az alkalmazás tényleges viselkedésének megmérésével készült, de **nem jogász írta**. Négy pont igényel elsősorban szakmai véleményt:
>
> 1. **Az Európai Unión kívülre irányuló adattovábbítás** az OpenRouter felé. Ez a legérzékenyebb pont: meg kell határozni az alkalmazandó adattovábbítási mechanizmust, ellenőrizni kell, hogy létezik-e adatfeldolgozási szerződés ezzel a szolgáltatóval, és ezt itt le kell írni. Amíg ez nem történik meg, ez a dokumentum leírja az adattovábbítást anélkül, hogy azt állítaná, hogy az jogilag keretezett.
> 2. **A 7. pontban** kiválasztott **jogalapok**, különösen a hozzájárulás és a jogos érdek közötti megosztás a kisegítő lehetőségek szolgáltatása esetében.
> 3. **A korhatár** (16 év) és annak összhangja a Google Play tartalombesorolási kérdőívével.
> 4. **Az MI-re vonatkozó tájékoztatás** a mesterséges intelligenciáról szóló európai rendelet alapján (átláthatósági kötelezettség korlátozott kockázatú rendszer esetén).

---

Ez a dokumentum a francia változat fordítása, amely a https://readit0.github.io/plume-legal/ címen érhető el. Tájékoztatásul szolgál. Eltérés esetén vegye fel velünk a kapcsolatot a sogacmoi7@gmail.com címen.
