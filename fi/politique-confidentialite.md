# Plumen tietosuojaseloste

**Viimeksi päivitetty: 31. heinäkuuta 2026** — Versio 1.0

---

## Kuka on tietojesi rekisterinpitäjä

**SASU RedLine Music**
SIREN 938 277 100 — SIRET `938 277 100 00013`
Abbaye 208-1, 208 Résidence Lavoisier, 18100 Vierzon, France
Yhteydenotot: sogacmoi7@gmail.com

Sovellus julkaistaan Google Playssä julkaisijanimellä **openfunword**.

Tämä seloste kuvaa, mitä Plume-sovellus tekee nykyisessä versiossaan. Se on kirjoitettu lukemalla sovelluksen koodia, ei yleisen mallipohjan perusteella.

---

## Minuutissa

Plume auttaa sinua kirjoittamaan: se kirjoittaa tekstisi uudelleen suoraan siinä sovelluksessa, jossa olet kirjoittamassa, ja se osaa kääntää näytöllä näkyvää tekstiä.

Kolme muistettavaa asiaa:

1. **Plume ei säilytä mitään tekstejäsi palvelimillaan.** Ei uudelleen kirjoitettuja tekstejäsi eikä näytöltä luettua tekstiä. Emme säilytä niistä kopiota emmekä lokia.
2. **Valitsemastasi moottorista riippuu, poistuuko tekstisi puhelimestasi vai ei.** Kaksi moottoria (paikallinen työkalupaketti ja paikallinen tekoäly) toimivat kokonaan laitteessa. Kolmas (Pilvitekoäly) lähettää tekstin tekoälypalveluun, joka **sijaitsee Euroopan unionin ulkopuolella**. Sinä valitset, eikä Pilvitekoäly kytkeydy koskaan päälle ilman nimenomaista suostumustasi.
3. **Plume tarvitsee laajoja käyttöoikeuksia** (muissa sovelluksissa näkyvän sisällön lukeminen, näytön kaappaaminen). Kerromme jäljempänä täsmälleen, mihin niitä käytetään ja mihin ei.

---

## 1. Mitä Plume lukee näytöltäsi ja milloin

### 1.1 Esteettömyyspalvelu

Kirjoittaakseen tekstisi uudelleen siinä paikassa, jossa sen kirjoitat, Plume käyttää Androidin esteettömyyspalvelua. Se on käyttöoikeus, jonka otat itse käyttöön puhelimen asetuksissa sen jälkeen, kun Plume on näyttänyt sinulle selitysnäytön **ennen** kuin se pyytää sitä.

Käytännössä:

- **Lepotilassa** Plume tietää vain, mikä sovellus on auki ja millä hetkellä siirrät kohdistimen tekstikenttään. Juuri se saa kelluvan kapselin ilmestymään näkyviin — ja vain niissä sovelluksissa, jotka olet itse määrittänyt.
- **Kentän sisältö luetaan vasta sillä hetkellä, kun kosketat kapselia**, jotta se voidaan kirjoittaa uudelleen ja korvata paikan päällä.
- **Salasanakentät on rajattu pois.** Sovellus tunnistaa salasanatyyppiset kentät (myös numerokoodit ja verkkosivujen kentät) ja kieltäytyy lukemasta niitä.
- Tämä käyttöoikeus **ei mahdollista minkäänlaisen kuvan ottamista** näytöstäsi.
- Plume **ei koskaan paina mitään puolestasi** toisessa sovelluksessa: se korvaa kentän tekstin, ei mitään muuta.

Kaksi toimintoa, jotka otat itse käyttöön — **Lukuapu tekstitilassa** ja **saapuneiden viestien kääntäminen** — lukevat näytöllä näkyvää tekstiä jatkuvasti niin kauan kuin ne ovat käynnissä, ja pysähtyvät heti, kun kytket ne pois.

Jos kieltäydyt esteettömyyspalvelusta, Plume on yhä käytettävissä: voit valita tekstin ja käyttää Androidin valintavalikon ”Plume”-kohtaa tai jakaa tekstin Plumelle.

### 1.2 Näytön kaappaus (Lukuapu)

Lukuapu asettaa käännöksen näytöllä näkyvän tekstin päälle — esimerkiksi sarjakuvan puhekuplien päälle. Se tarvitsee nähdäkseen näytön kuvan.

- Se on **oletuksena pois käytöstä** ja toimii vain niissä sovelluksissa, jotka olet nimenomaisesti sallinut yksi kerrallaan.
- **Android pyytää oman suostumuksensa jokaisen istunnon alussa.** Kyse ei ole kerran ja lopullisesti annettavasta luvasta: jokainen istunto vaatii uuden hyväksynnän. Plume ei koskaan yritä käyttää tätä hyväksyntää uudelleen eikä kiertää sitä.
- Koko istunnon ajan **pysyvä ilmoitus ja järjestelmän merkkivalo pysyvät näkyvissä**. Plume ei voi kaapata näyttöäsi huomaamatta.
- Istunto **päättyy automaattisesti, kun näyttö lukitaan**, ja välittömästi, kun pysäytät sen itse.
- Sovellukset, jotka suojaavat näkymänsä (pankkisovellukset, salasanojen hallintaohjelmat), **Android peittää itse** ennen kuin Plume vastaanottaa mitään. Kyse on järjestelmän suojauksesta, joka on todellinen mutta osittainen: kaikki arkaluonteiset sovellukset eivät ota sitä käyttöön. Emme siksi esitä sitä ehdottomana takeena.
- **Kaapattuja kuvia ei koskaan tallenneta eikä lähetetä.** Jokainen kuva analysoidaan muistissa tekstin poimimiseksi ja hylätään sen jälkeen. Yksikään kuva ei lähde puhelimestasi, ei koskaan, valitsemastasi moottorista riippumatta.

---

## 2. Mikä jää puhelimeesi ja mikä lähtee sieltä

Tämä on tämän selosteen tärkein erottelu, ja sinä hallitset sitä.

### 2.1 Moottorit, jotka eivät lähetä mitään ulos

- **Paikallinen työkalupaketti** (tekstin tunnistus ja kääntäminen ilman verkkoyhteyttä) toimii kokonaan laitteessa.
- **Paikallinen tekoäly** on tekoälymalli, joka ladataan kerran ja tallennetaan sitten puhelimeesi (noin 720 Mt). Se suoritetaan laitteessasi.

Näillä kahdella moottorilla **luettu tai uudelleen kirjoitettu teksti ei poistu puhelimestasi.** Tekstisi sisältöön ei liity yhtään verkkokutsua.

### 2.2 Pilvitekoäly-moottori

Kun valitset Pilvitekoälyn tai kun laitteesi ei ole riittävän tehokas paikalliselle tekoälylle, kyseinen teksti lähetetään palvelimillemme ja sieltä edelleen kolmannen osapuolen tekoälypalveluun.

**Todellinen reitti on syytä kertoa selvästi:**

- Teksti kulkee infrastruktuurimme (Supabase) kautta, joka sijaitsee **Euroopan unionissa** (Keski-Euroopan alue, Frankfurt).
- Sen jälkeen se välitetään palveluun **openrouter.ai**, joka on **Euroopan unionin ulkopuolella sijaitseva** reitityksen välittäjä ja joka antaa **Mistral Small** -mallin käsitellä sen.
- **Kyse on siis tietojen siirrosta Euroopan unionin ulkopuolelle.** Emme väitä muuta emmekä esitä minkäänlaista lupausta eurooppalaisesta säilytyksestä tämän vaiheen osalta.
- **Plume ei säilytä tekstiäsi.** Yksikään palvelintoiminnoistamme ei kirjoita tekstisi sisältöä talteen: tallennamme vain pyynnön teknisen tunnisteen ja laitteesi tunnisteen, jotta voimme laskea kiintiösi ja havaita väärinkäytökset.
- **Emme voi taata sitä, mitä nämä palveluntarjoajat tekevät omalla puolellaan.** Kerromme sen mieluummin suoraan kuin lupaamme sinulle nollasäilytystä, jota emme pysty tarkistamaan.

**Pilvitekoäly ei kytkeydy koskaan päälle itsestään.** Erillinen suostumusnäyttö selittää sinulle nämä kohdat ennen ensimmäistä lähetystä, eikä mitään lähde ennen kuin olet hyväksynyt sen. Jos paikallinen tekoäly epäonnistuu, Plume ei siirry pilveen vaiti: se ilmoittaa siitä sinulle ja odottaa päätöstäsi. Voit peruuttaa tämän suostumuksen milloin tahansa asetuksista.

Lähetettävällä tekstillä on yläraja: 1 200 merkkiä uudelleenkirjoitusta varten ja 4 000 merkkiä näytön analyysia varten.

---

## 3. Tiedot, joita säilytämme

Emme käytä **mitään kävijäseurannan työkalua, kolmannen osapuolen mainosseurainta emmekä kaatumisraportoinnin työkalua**. Sovellus ei sisällä mittauskirjastoa.

Tässä on kaikki, mitä palvelimillemme tallennetaan:

| Tieto | Miksi | Kuinka kauan |
|---|---|---|
| **Laitetunniste** (Plumen luoma satunnainen numero, jolla ei ole yhteyttä henkilöllisyyteesi eikä mainostunnisteeseen) | Laitteen liittäminen tiliin, kiintiöiden soveltaminen, väärinkäytösten estäminen | Tilisi poistamiseen asti |
| **Tilin sähköpostiosoite** (jos luot tilin sähköpostilla tai Google-tunnuksilla) | Sinun tunnistamisesi, tilauksesi liittäminen | Tilisi poistamiseen asti |
| **Käyttölaskurit** (uudelleenkirjoitusten määrä päivässä ja kuukaudessa — lukuja, ei tekstejä) | Kiintiöiden soveltaminen | Tilisi poistamiseen asti |
| **Ostohistoria** (Google Playn tapahtumatunniste, päivämäärät, tilauksen tila) | Pääsyn antaminen siihen, minkä olet maksanut, uusimisten hallinta, kirjanpitovelvoitteidemme täyttäminen | Säilytetään myös tilin poistamisen jälkeen, mutta **irrotettuna henkilöllisyydestäsi** (ks. §6) |
| **Vapaaehtoisesti lähetetyt ehdotukset** (jos lähetät meille sovelluksesta ehdotuksen persoonasta) | Valikoiman parantaminen. Näitä ehdotuksia ei koskaan julkaista. | Tilisi poistamiseen asti |
| **Väärinkäytösten tekniset merkit** (toistuvat ylitykset, epäonnistunut sovelluksen eheystarkistus — ilman mitään tekstiä) | Turvallisuus, väärinkäytösten torjunta | Irrotetaan henkilöllisyydestäsi tilin poistamisen yhteydessä |
| **Sovelluksen kieli ja versio** | Oikean sisällön tarjoaminen | Tilisi poistamiseen asti |

**Mitä emme kerää:** nimeäsi, yhteystietojasi, sijaintiasi, osoitekirjaasi, valokuviasi, kalenteriasi tai sovellustesi käyttöhistoriaa. Plume ei pyydä mitään näistä käyttöoikeuksista.

**Mikä jää pelkästään puhelimeesi:** omat persoonasi ja niiden avatarit, asetuksesi, sovelluskohtaiset sääntösi ja Lukuavun käännösvälimuisti (joka tyhjennetään jokaisen istunnon päätteeksi). Mitään näistä ei lähetetä palvelimillemme.

---

## 4. Puhesanelu

Mikrofonipainike antaa sinun sanella kirjoittamisen sijaan. Mikrofonin käyttöoikeutta pyydetään **juuri sillä hetkellä, kun painat tätä painiketta**, ei koskaan käynnistyksen yhteydessä, ja mikrofoni avataan vain sillä hetkellä. Plume ei kuuntele koskaan taustalla.

**Plume ei vastaanota, tallenna eikä välitä mitään äänitallennetta.** Sanelu annetaan puhelimeesi sisäänrakennetun puheentunnistusmoottorin (Androidin) tehtäväksi. Plume hakee vain kirjoitetuksi muunnetun tekstin.

**Tärkeä ja rehellinen kohta:** tämä järjestelmän moottori kuuluu puhelimeesi, yleensä Googlelle. Laitteestasi, sen asetuksista ja asennetuista kielipaketeista riippuen **se voi lähettää äänen julkaisijansa palvelimille** kirjoitetuksi muuntamista varten. Tämä käsittely on Plumen ulottumattomissa, ja siihen sovelletaan järjestelmäsi julkaisijan tietosuojaselostetta. Emme siis voi väittää, että äänesi pysyy laitteessa — se riippuu puhelimestasi, ei meistä.

Jos kieltäydyt mikrofonin käyttöoikeudesta, näppäimistöllä kirjoittaminen on tietenkin edelleen käytettävissä.

---

## 5. Mainonta

Palvelu on maksuton tiettyyn päivittäiseen käyttörajaan asti. Sen jälkeen voit **halutessasi** katsoa palkkiomainoksen saadaksesi lisää käyttökertoja. Sitä ei koskaan pakoteta: jos et katso mainosta, säilytät yksinkertaisesti sen, mihin sinulla on oikeus.

- Mainokset toimittaa **Google AdMob**.
- Ne näkyvät **vain itse Plume-sovelluksessa**, ei koskaan kelluvassa kapselissa eikä koskaan toisen sovelluksen päällä.
- **Tilaajat eivät näe lainkaan mainoksia.**
- Euroopan talousalueella, Yhdistyneessä kuningaskunnassa ja Sveitsissä sinulle esitetään **ennen ensimmäistä mainosta** suostumuslomake, jonka tarjoaa Googlen sertifioima alusta. Niin kauan kuin valintaasi ei ole saatu, mainosta ei pyydetä. Jos kieltäydyt, mainokset pysyvät **kohdentamattomina** eikä **sinulta viedä mitään toimintoa**. Voit muuttaa tätä valintaa milloin tahansa asetuksista.
- Jotta palkkiosi voidaan hyvittää luotettavasti, Plumen laitetunnisteesi välitetään AdMobille. Google voi lisäksi kerätä omia tietojaan oman tietosuojaselosteensa mukaisesti.

*Tätä kirjoitettaessa mainosten näyttäminen on kytketty pois päältä palvelimen puolella. Tämä luku kuvaa toimintaa siitä hetkestä, kun se otetaan käyttöön.*

---

## 6. Tilaukset ja ostot

Tilaukset ja paketit myydään **Google Playn kautta**. Emme näe koskaan maksukorttitietojasi: niitä käsittelee Google, joka on laskutuksen kannalta myyjä.

Saamme Googlelta ostotositteen, jonka palvelimemme tarkistaa, ja säilytämme siitä merkinnän (tapahtumatunniste, päivämäärät, tila). Tämä merkintä säilytetään kirjanpidollisista syistä ja sen estämiseksi, että samaa ostoa käytettäisiin kahdesti — mutta se **irrotetaan henkilöllisyydestäsi**, kun poistat tilisi.

---

## 7. Oikeutesi

Sinulla on GDPR:n mukaiset oikeudet saada pääsy tietoihin, oikaista ja poistaa tietoja, rajoittaa käsittelyä, vastustaa käsittelyä sekä siirtää tiedot järjestelmästä toiseen.

**Yksinkertaisin ja nopein tapa: poisto on rakennettu sovellukseen.**
Asetukset → Tietosuoja → Poista tietoni. Se **suoritetaan välittömästi**, sitä ei aseteta jonoon. Yksityiskohdat siitä, mikä poistetaan ja mikä säilytetään, ovat omalla sivullamme: `https://readit0.github.io/plume-legal/suppression-compte`.

Voit myös poistaa tilisi **asentamatta sovellusta** kirjoittamalla osoitteeseen sogacmoi7@gmail.com.

Kaikissa muissa pyynnöissä kirjoita osoitteeseen **sogacmoi7@gmail.com**. Vastaamme kuukauden kuluessa.

**Käsittelyn oikeusperusteet:** sopimuksen täytäntöönpano (pyytämäsi palvelun tuottaminen, tilauksesi hallinnointi), suostumuksesi (esteettömyyspalvelu, näytön kaappaus, lähetys Pilvitekoälylle, kohdennettu mainonta), oikeutettu etumme (turvallisuus, väärinkäytösten torjunta) ja lakisääteiset velvoitteemme (kirjanpito).

Voit tehdä valituksen **CNIL**:lle (www.cnil.fr), joka on julkaisijan valvontaviranomainen, tai, **jos asut Euroopan unionissa**, asuinmaasi valvontaviranomaiselle — GDPR:n 77 artikla jättää valinnan sinulle.

---

## 8. Alaikäiset

Plume on kirjoittamisen apuväline, joka on tarkoitettu **16 vuotta täyttäneille**. Emme kerää tietoisesti alle 16-vuotiaiden lasten tietoja, eikä sovellusta ole suunniteltu eikä markkinoitu heille. Jos olet huoltaja ja epäilet, että lapsesi on luovuttanut meille tietoja, kirjoita osoitteeseen sogacmoi7@gmail.com: poistamme tilin.

Koska sovellus mahdollistaa vapaan tekstin uudelleenkirjoittamisen ja näyttää mainoksia, se ei ole kelvollinen Google Playn perheille suunnattuihin ohjelmiin.

---

## 9. Henkilötietojen käsittelijät ja vastaanottajat

| Palveluntarjoaja | Tehtävä | Missä |
|---|---|---|
| **Supabase** | Tietokannan ylläpito, tunnistautuminen, palvelintoiminnot | Euroopan unioni (Frankfurt) |
| **OpenRouter** | Pyyntöjen välittäminen tekoälymallille | **Euroopan unionin ulkopuolella** |
| **Mistral AI** (OpenRouterin kautta) | Malli, joka käsittelee tekstin (Mistral Small) | Käsittely edellä mainitun välittäjän kautta |
| **Google Play / Google Billing** | Maksaminen, tilaukset | Google Ireland / Yhdysvallat |
| **Google AdMob** | Palkkiomainonta | Google Ireland / Yhdysvallat |
| **Google (puhelimen järjestelmäpalvelut)** | Puheentunnistus, verkottomat käännöspaketit | Laitteestasi riippuen |

**Emme myy mitään tietoja emmekä luovuta niitä tietovälittäjille.**

**Siirrot Euroopan unionin ulkopuolelle:** OpenRouterin, Google Playn ja AdMobin käyttö merkitsee tietojen siirtoa Euroopan unionin ulkopuolelle. Näiden siirtojen oikeudellinen perusta (vakiosopimuslausekkeet, tietosuojan riittävyyttä koskeva päätös) **on ammattilaisen tarkistettava ja dokumentoitava ennen julkaisua** — ks. asiakirjan lopussa oleva huomautus.

---

## 10. Tietoturva

Sovelluksen ja palvelimiemme välinen liikenne on salattu (HTTPS/TLS). Pääsyä tietokannan tietoihin rajoitetaan palvelimen säännöillä: arkaluonteisiin toimintoihin ei pääse sovelluksesta käsin. Mikään järjestelmä ei ole täydellisen turvallinen, mutta yhtäkään uudelleen kirjoittamaasi tekstiä ei tallenneta meille — mikä rajoittaa mekaanisesti sitä, mitä tunkeutuminen voisi paljastaa.

---

## 11. Muutokset

Jokainen tähän selosteeseen tehtävä muutos julkaistaan osoitteessa `https://readit0.github.io/plume-legal` uudella päivämäärällä. Jos tietojesi kulussa tapahtuu merkittävä muutos, ilmoitamme siitä sinulle sovelluksessa.

---

## Käyttöehdot

Palvelun käyttöehdot (kiintiöt, tilaukset, irtisanominen) ovat erillisessä asiakirjassa: `https://readit0.github.io/plume-legal/conditions-generales`.

---

> ### Luetutettava ammattilaisella
>
> Tämä asiakirja on kirjoitettu mittaamalla sovelluksen todellista toimintaa, mutta **sitä ei ole kirjoittanut lakimies**. Neljä kohtaa ansaitsee ensisijaisesti ammattilaisen arvion:
>
> 1. **Tietojen siirto Euroopan unionin ulkopuolelle** OpenRouterille. Se on kaikkein herkin kohta: on määritettävä, mitä siirtomekanismia sovelletaan, tarkistettava, että tämän palveluntarjoajan kanssa on henkilötietojen käsittelyä koskeva sopimus, ja kirjattava se tähän. Niin kauan kuin sitä ei ole tehty, tämä asiakirja kuvaa siirron väittämättä sitä oikeudellisesti järjestetyksi.
> 2. **Käsittelyn oikeusperusteet**, jotka on valittu §7:ssä, erityisesti suostumuksen ja oikeutetun edun jako esteettömyyspalvelun osalta.
> 3. **Ikäraja** (16 vuotta) ja sen yhdenmukaisuus Google Playn sisällön ikäluokitusta koskevan kyselyn kanssa.
> 4. **Tekoälyä koskeva maininta** Euroopan unionin tekoälyasetuksen nojalla (rajoitetun riskin järjestelmän avoimuusvelvoite).

---

Tämä asiakirja on käännös ranskankielisestä versiosta, joka on saatavilla osoitteessa https://readit0.github.io/plume-legal/. Se toimitetaan sinulle tiedoksi. Jos huomaat eroavaisuuden, ota meihin yhteyttä osoitteessa sogacmoi7@gmail.com.
