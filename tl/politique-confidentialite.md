# Patakaran sa Privacy ng Plume

**Huling na-update: 31 Hulyo 2026** — Bersyon 1.0

---

## Sino ang may pananagutan sa inyong data

**SASU RedLine Music**
SIREN 938 277 100 — SIRET `938 277 100 00013`
Abbaye 208-1, 208 Résidence Lavoisier, 18100 Vierzon, France
Contact: sogacmoi7@gmail.com

Ang application ay inilalathala sa Google Play sa ilalim ng pangalan ng publisher na **openfunword**.

Inilalarawan ng patakarang ito kung ano ang ginagawa ng application na Plume sa kasalukuyang bersyon nito. Isinulat ito sa pamamagitan ng pagbabasa sa mismong code ng application, hindi mula sa isang pangkalahatang template.

---

## Sa loob ng isang minuto

Tinutulungan kayo ng Plume na magsulat: ni-re-rephrase nito ang inyong teksto diretso sa loob ng application kung saan kayo nagta-type, at kaya nitong isalin ang tekstong nakikita sa screen.

Tatlong bagay na dapat tandaan:

1. **Walang anumang teksto ninyo ang iniimbak ng Plume sa mga server nito.** Hindi ang mga tekstong ni-rephrase ninyo, hindi rin ang tekstong binasa sa screen. Wala kaming itinatagong kopya, wala rin kaming log nito.
2. **Depende sa engine na pipiliin ninyo, lumalabas o hindi lumalabas ang inyong teksto sa inyong telepono.** Dalawang engine (ang Local Kit at ang Local AI) ang gumagana nang buo sa loob mismo ng device. Ang pangatlo (ang Cloud AI) ay nagpapadala ng teksto sa isang serbisyo ng artificial intelligence na **nasa labas ng European Union**. Kayo ang pumipili, at hindi kailanman gumagana ang Cloud AI nang wala ang inyong tahasang pahintulot.
3. **Kailangan ng Plume ang mga makapangyarihang permission** (pagbasa sa nilalamang ipinapakita sa ibang application, pagkuha ng screen). Ipinapaliwanag namin sa ibaba nang eksakto kung para saan ang mga ito at kung para saan hindi.

---

## 1. Ano ang binabasa ng Plume sa inyong screen, at kailan

### 1.1 Ang accessibility service

Upang muling maisulat ang inyong teksto sa mismong lugar kung saan ninyo ito isinusulat, ginagamit ng Plume ang accessibility service ng Android. Isa itong permission na kayo mismo ang nagbubukas, sa settings ng telepono, matapos ang isang paliwanag na ipinapakita ng Plume **bago** ito hingin sa inyo.

Sa konkretong salita:

- **Kapag walang ginagawa**, alam lamang ng Plume kung aling application ang bukas at kung kailan ninyo inilalagay ang cursor sa isang input field. Iyon ang nagpapalabas sa lumulutang na capsule — at sa mga application lamang na kayo mismo ang nag-configure.
- **Ang laman ng field ay binabasa lamang sa mismong sandaling hipuin ninyo ang capsule**, upang muling isulat at pagkatapos ay palitan sa mismong kinaroroonan nito.
- **Hindi kasama ang mga password field.** Natutukoy ng application ang mga field na uri ng password (pati na ang mga numerikong code at ang mga web field) at tumatangging basahin ang mga ito.
- Ang permission na ito ay **hindi nagpapahintulot ng anumang pagkuha ng larawan** ng inyong screen.
- **Hindi kailanman pumipindot ang Plume para sa inyo** sa loob ng ibang application: pinapalitan lamang nito ang teksto ng isang field, wala nang iba.

Dalawang function na kayo mismo ang nagbubukas — ang **Assisted Reading sa Text mode** at ang **pagsasalin ng mga natanggap na mensahe** — ay tuloy-tuloy na bumabasa ng tekstong ipinapakita habang tumatakbo ang mga ito, at humihinto sa sandaling patayin ninyo ang mga ito.

Kung tatanggihan ninyo ang accessibility service, magagamit pa rin ang Plume: puwede kayong pumili ng isang teksto at dumaan sa menu na "Plume" ng selection menu ng Android, o mag-share ng teksto papunta sa Plume.

### 1.2 Ang screen capture (Assisted Reading)

Ang Assisted Reading ay naglalagay ng salin sa ibabaw ng tekstong ipinapakita — halimbawa ang mga speech bubble ng isang komiks. Kailangan nitong makita ang imahe ng screen.

- **Nakapatay ito bilang default** at gumagana lamang sa mga application na tahasan ninyong pinahintulutan, isa-isa.
- **Ang Android mismo ang humihingi ng sarili nitong pahintulot sa inyo sa tuwing magsisimula ang isang session.** Hindi ito isang permission na ibinibigay nang minsanan para sa habambuhay: bawat session ay nangangailangan ng bagong pahintulot. Hindi kailanman sinusubukan ng Plume na gamitin muli o iwasan ang pahintulot na ito.
- Sa buong session, **may nananatiling notification at isang system indicator na nakikita**. Hindi kayang kunan ng Plume ang inyong screen nang palihim.
- Ang session ay **awtomatikong humihinto kapag na-lock ang screen**, at agad kapag kayo mismo ang huminto.
- Ang mga application na pinoprotektahan ang kanilang display (mga banking app, mga password manager) ay **tinatakpan ng Android mismo** bago pa may matanggap ang Plume. Isa itong proteksyon ng sistema, totoo ngunit bahagya lamang: hindi lahat ng sensitibong application ay nagbubukas nito. Kaya hindi namin ito ipinapakilala bilang isang lubos na garantiya.
- **Ang mga nakuhang imahe ay hindi kailanman iniimbak ni ipinapadala.** Ang bawat imahe ay sinusuri sa memory upang makuha ang teksto nito, at pagkatapos ay itinatapon. Walang imaheng lumalabas sa inyong telepono, kailanman, anuman ang engine na napili.

---

## 2. Ano ang nananatili sa inyong telepono at ano ang lumalabas

Ito ang pinakamahalagang pagkakaiba sa patakarang ito, at kayo ang may kontrol dito.

### 2.1 Ang mga engine na walang ipinapalabas

- Ang **Local Kit** (offline na pagkilala at pagsasalin ng teksto) ay gumagana nang buo sa loob ng device.
- Ang **Local AI** ay isang modelo ng artificial intelligence na minsan lamang na-download at pagkatapos ay nakaimbak na sa inyong telepono (mga 720 MB). Tumatakbo ito sa inyong device.

Sa dalawang engine na ito, **ang tekstong binabasa o ni-rephrase ay hindi lumalabas sa inyong telepono.** Walang anumang network call na may kinalaman sa laman ng inyong teksto.

### 2.2 Ang Cloud AI engine

Kapag pinili ninyo ang Cloud AI, o kapag hindi sapat ang lakas ng inyong device para sa Local AI, ang kaukulang teksto ay ipinapadala sa aming mga server, at pagkatapos ay sa isang third-party na serbisyo ng artificial intelligence.

**Kailangang maging malinaw tungkol sa tunay na dinaraanan nito:**

- Dumaraan ang teksto sa aming infrastructure (Supabase), na naka-host sa **European Union** (rehiyon ng Central Europe, Frankfurt).
- Pagkatapos ay ipinapadala ito sa **openrouter.ai**, isang routing intermediary na **nasa labas ng European Union**, na siyang nagpapaproseso nito sa modelong **Mistral Small**.
- **Kaya isa itong paglilipat ng data sa labas ng European Union.** Hindi namin sinasabi ang kabaligtaran, at wala kaming ipinapakitang pangako ng European hosting para sa hakbang na ito.
- **Hindi iniimbak ng Plume ang inyong teksto.** Wala ni isa sa aming mga server function ang nagsusulat ng laman ng inyong teksto: isang teknikal na identifier lamang ng request at ang identifier ng inyong device ang aming itinatala, upang mabilang ang inyong quota at matukoy ang mga pang-aabuso.
- **Ang ginagawa ng mga provider na ito sa kanilang panig ay hindi namin magagarantiya.** Mas gusto naming sabihin ito sa inyo kaysa mangako ng zero retention na hindi naman namin kayang beripikahin.

**Hindi kailanman kusang bumubukas ang Cloud AI.** May isang natatanging consent screen na nagpapaliwanag sa inyo ng mga puntong ito bago ang unang pagpapadala, at walang lumalabas hangga't hindi kayo tumatanggap. Kung mabigo ang Local AI, hindi tahimik na lilipat ang Plume sa cloud: sinasabi nito sa inyo at hinihintay ang inyong pasya. Puwede ninyong bawiin ang pahintulot na ito anumang oras sa settings.

May takda ang tekstong ipinapadala: 1,200 karakter para sa isang pag-rephrase, 4,000 karakter para sa isang pagsusuri ng screen.

---

## 3. Ang datos na aming itinatago

**Wala kaming ginagamit na anumang analytics tool, anumang third-party advertising tracker, ni anumang crash reporting tool.** Walang measurement SDK ang application.

Ito ang kabuuan ng nakaimbak sa aming mga server:

| Datos | Bakit | Tagal |
|---|---|---|
| **Device identifier** (isang random na numero na binubuo ng Plume, walang kaugnayan sa inyong pagkakakilanlan ni sa anumang advertising identifier) | Iugnay ang isang device sa isang account, ipatupad ang mga quota, harangin ang pang-aabuso | Hanggang sa mabura ang inyong account |
| **Email address ng account** (kung gumawa kayo ng account sa pamamagitan ng email o sa pamamagitan ng Google) | Patunayan ang inyong pagkakakilanlan, iugnay ang inyong subscription | Hanggang sa mabura ang inyong account |
| **Mga usage counter** (bilang ng pag-rephrase kada araw at kada buwan — mga numero, hindi mga teksto) | Ipatupad ang mga quota | Hanggang sa mabura ang inyong account |
| **Kasaysayan ng pagbili** (transaction identifier ng Google Play, mga petsa, katayuan ng subscription) | Bigyan kayo ng access sa binayaran ninyo, pamahalaan ang mga pag-renew, tuparin ang aming mga obligasyon sa accounting | Itinatago kahit matapos burahin ang account, ngunit **inihihiwalay sa inyong pagkakakilanlan** (tingnan ang §6) |
| **Mga mungkahing kusang ipinadala** (kung susulat kayo sa amin ng mungkahing persona mula sa application) | Pagandahin ang katalogo. Hindi kailanman inilalathala ang mga mungkahing ito. | Hanggang sa mabura ang inyong account |
| **Mga teknikal na senyales ng pang-aabuso** (paulit-ulit na paglagpas sa takda, palya sa integrity check — walang anumang teksto) | Seguridad, laban sa pandaraya | Inihihiwalay sa inyong pagkakakilanlan kapag binura ang account |
| **Wika at bersyon ng application** | Ihatid ang tamang nilalaman | Hanggang sa mabura ang inyong account |

**Ang hindi namin kinokolekta:** ang inyong pangalan, ang inyong mga contact, ang inyong lokasyon, ang inyong address book, ang inyong mga larawan, ang inyong kalendaryo, ang kasaysayan ng inyong mga application. Wala ni isa sa mga permission na iyan ang hinihingi ng Plume.

**Ang nananatili lamang sa inyong telepono:** ang inyong mga custom na persona at ang kanilang mga avatar, ang inyong mga setting, ang inyong mga panuntunan kada application, ang translation cache ng Assisted Reading (binubura sa katapusan ng bawat session). Wala ni isa sa mga ito ang ipinapadala sa aming mga server.

---

## 4. Ang voice dictation

May isang microphone button na nagbibigay-daan sa inyong magdikta sa halip na mag-type. Ang permission para sa mikropono ay hinihingi **sa mismong sandaling pindutin ninyo ang button na ito**, hindi kailanman sa pagbubukas ng application, at doon lamang bumubukas ang mikropono. Hindi kailanman nakikinig ang Plume sa background.

**Walang anumang audio recording ang natatanggap, iniimbak o ipinapadala ng Plume.** Ang diktasyon ay ipinauubaya sa speech recognition engine na nakapaloob sa inyong telepono (ang sa Android). Ang teksto lamang na na-transcribe ang kinukuha ng Plume.

**Mahalaga at tapat na punto:** ang system engine na iyon ay pag-aari ng inyong telepono, kadalasan ay ng Google. Depende sa inyong device, sa mga setting nito at sa mga naka-install na language module, **maaari nitong ipadala ang audio sa mga server ng may-ari nito** upang i-transcribe. Ang pagproseso na iyon ay wala sa kontrol ng Plume at nasasaklaw ng patakaran sa privacy ng may-ari ng inyong sistema. Kaya hindi namin masasabi na nananatili sa device ang inyong boses — nakadepende iyon sa inyong telepono, hindi sa amin.

Kung tatanggihan ninyo ang permission ng mikropono, nananatiling magagamit siyempre ang pag-type sa keyboard.

---

## 5. Advertising

Libre ang serbisyo hanggang sa isang tiyak na hangganan ng paggamit kada araw. Lampas doon, **puwede ninyong piliin** na manood ng isang rewarded ad upang makakuha ng dagdag na paggamit. Hindi ito kailanman ipinipilit: kung hindi kayo manonood ng ad, mananatili lamang sa inyo ang nararapat sa inyo.

- Ang mga ad ay ibinibigay ng **Google AdMob**.
- Lumalabas ang mga ito **sa loob lamang ng mismong application na Plume**, hindi kailanman sa lumulutang na capsule at hindi kailanman sa ibabaw ng ibang application.
- **Walang nakikitang ad ang mga subscriber.**
- Sa European Economic Area, sa United Kingdom at sa Switzerland, may ipinapakita sa inyong consent form na ibinibigay ng isang platform na sertipikado ng Google **bago ang unang ad**. Hangga't hindi nakukuha ang inyong pili, walang ad na hinihingi. Kung tatanggi kayo, mananatiling **hindi personalized** ang mga ad at **walang function na inaalis sa inyo**. Puwede ninyong baguhin ang piling ito anumang oras mula sa settings.
- Upang maikredito nang maaasahan ang inyong reward, ipinapadala sa AdMob ang device identifier ninyo sa Plume. Maaari ring mangolekta ang Google ng sarili nitong datos alinsunod sa patakaran nito sa privacy.

*Sa petsa ng pagsulat nito, nakapatay sa panig ng server ang paglalabas ng mga ad. Inilalarawan ng bahaging ito kung paano ito gagana sa sandaling buksan ito.*

---

## 6. Mga subscription at pagbili

Ang mga subscription at pack ay ibinebenta **sa pamamagitan ng Google Play**. Hindi namin kailanman nakikita ang inyong mga detalye sa pagbabayad: ang Google ang nagpoproseso ng mga ito, at ito ang nagbebenta sa usapin ng billing.

Tumatanggap kami mula sa Google ng isang patunay ng pagbili na bineberipika ng aming server, at itinatago namin ang bakas nito (transaction identifier, mga petsa, katayuan). Itinatago ang bakas na ito para sa mga dahilan ng accounting at upang mapigilang magamit nang dalawang beses ang iisang pagbili — ngunit **inihihiwalay ito sa inyong pagkakakilanlan** kapag binura ninyo ang inyong account.

---

## 7. Ang inyong mga karapatan

Mayroon kayong karapatan sa access, pagwawasto, pagbura, paghihigpit, pagtutol at portability ng data na itinatakda ng GDPR (ang General Data Protection Regulation ng European Union).

**Ang pinakasimple at pinakamabilis: nakapaloob na sa application ang pagbura.**
Settings → Privacy → Burahin ang aking data. **Isinasagawa ito agad**, hindi ipinipila. Ang detalye ng kung ano ang binubura at kung ano ang itinatago ay makikita sa aming natatanging pahina: `https://readit0.github.io/plume-legal/suppression-compte`.

Puwede rin ninyong burahin ang inyong account **nang hindi ini-install ang application**, sa pamamagitan ng pagsulat sa sogacmoi7@gmail.com.

Para sa anumang ibang kahilingan, sumulat sa **sogacmoi7@gmail.com**. Sumasagot kami sa loob ng isang buwan.

**Mga legal na batayan:** ang pagtupad sa kontrata (pagbibigay ng serbisyong hinihingi ninyo, pamamahala sa inyong subscription), ang inyong pahintulot (accessibility service, screen capture, pagpapadala sa Cloud AI, personalized na advertising), ang aming lehitimong interes (seguridad, laban sa pandaraya) at ang aming mga obligasyong legal (accounting).

Puwede kayong maghain ng reklamo sa **CNIL** (www.cnil.fr), ang supervisory authority ng publisher, o, **kung kayo ay naninirahan sa European Union**, sa supervisory authority ng bansang tinitirhan ninyo — binibigyan kayo ng Artikulo 77 ng GDPR ng ganitong pagpipilian.

---

## 8. Ang mga menor de edad

Ang Plume ay isang kasangkapang pantulong sa pagsulat, nakalaan sa mga gumagamit na **16 taong gulang pataas**. Hindi kami sadyang nangongolekta ng datos ng mga batang wala pang 16 taong gulang at hindi idinisenyo ni itinataguyod ang application para sa kanila. Kung kayo ay may hawak ng awtoridad ng magulang at naniniwala kayong may naipadalang datos sa amin ang inyong anak, sumulat sa sogacmoi7@gmail.com: buburahin namin ang account.

Dahil pinapayagan ng application ang pag-rephrase ng malayang teksto at nagpapakita ito ng advertising, hindi ito kwalipikado sa mga programa ng Google Play na nakalaan para sa mga pamilya.

---

## 9. Mga processor at tatanggap ng data

| Provider | Papel | Saan |
|---|---|---|
| **Supabase** | Hosting ng database, authentication, mga server function | European Union (Frankfurt) |
| **OpenRouter** | Pagruruta ng mga request patungo sa AI model | **Labas ng European Union** |
| **Mistral AI** (sa pamamagitan ng OpenRouter) | Modelong nagpoproseso ng teksto (Mistral Small) | Pagproseso sa pamamagitan ng nabanggit na intermediary |
| **Google Play / Google Billing** | Bayad, mga subscription | Google Ireland / Estados Unidos |
| **Google AdMob** | Rewarded advertising | Google Ireland / Estados Unidos |
| **Google (mga system service ng telepono)** | Speech recognition, mga offline na translation module | Depende sa inyong device |

**Wala kaming ibinebentang anumang datos at wala kaming ibinibigay na anuman sa mga data broker.**

**Paglilipat sa labas ng European Union:** ang paggamit sa OpenRouter, sa Google Play at sa AdMob ay nagsasangkot ng paglilipat ng datos sa labas ng European Union. Ang legal na balangkas ng mga paglilipat na ito (standard contractual clauses, adequacy decision) ay **kailangang beripikahin at idokumento ng isang propesyonal bago ilathala** — tingnan ang paalala sa dulo ng dokumento.

---

## 10. Seguridad

Ang palitan sa pagitan ng application at ng aming mga server ay naka-encrypt (HTTPS/TLS). Ang access sa datos sa database ay pinaghihigpitan ng mga panuntunan sa server: ang mga sensitibong function ay hindi maaabot mula sa application. Walang sistemang ganap na ligtas, ngunit wala ni isang tekstong ni-rephrase ninyo ang nakaimbak sa amin — na mekanikal na naglilimita sa kung ano ang maibubunyag ng isang panghihimasok.

---

## 11. Mga pagbabago

Anumang pagbabago sa patakarang ito ay ilalathala sa `https://readit0.github.io/plume-legal` na may bagong petsa. Kung may mahalagang pagbabago sa daloy ng inyong datos, ipapaalam namin ito sa inyo sa loob ng application.

---

## Mga tuntunin at kundisyon

Ang mga kundisyon sa paggamit ng serbisyo (mga quota, subscription, pagtatapos) ay nasa hiwalay na dokumento: `https://readit0.github.io/plume-legal/conditions-generales`.

---

> ### Dapat suriin ng isang propesyonal
>
> Ang dokumentong ito ay isinulat sa pamamagitan ng pagsukat sa tunay na kilos ng application, ngunit **hindi ito isinulat ng isang abogado**. Apat na punto ang unang-unang nangangailangan ng propesyonal na payo:
>
> 1. **Ang paglilipat ng datos sa labas ng European Union** patungo sa OpenRouter. Ito ang pinakasensitibong punto: kailangang matukoy ang naaangkop na mekanismo ng paglilipat, maberipika na may umiiral na data processing agreement sa provider na iyon, at maisulat ito rito. Hangga't hindi pa ito nagagawa, inilalarawan ng dokumentong ito ang paglilipat nang hindi iginigiit na ito ay may wastong balangkas.
> 2. **Ang mga legal na batayan** na pinili sa §7, lalo na ang paghahati sa pagitan ng pahintulot at lehitimong interes para sa accessibility service.
> 3. **Ang pinakamababang edad** (16 taon) at ang pagkakatugma nito sa content rating questionnaire ng Google Play.
> 4. **Ang pahayag hinggil sa AI** sa ilalim ng regulasyong Europeo tungkol sa artificial intelligence (obligasyon sa transparency para sa isang limited-risk na sistema).

---

Ang dokumentong ito ay isang salin ng bersyong Pranses, na makikita sa https://readit0.github.io/plume-legal/. Ibinibigay ito para sa inyong kaalaman. Kung may pagkakaiba, makipag-ugnayan sa amin sa sogacmoi7@gmail.com.
