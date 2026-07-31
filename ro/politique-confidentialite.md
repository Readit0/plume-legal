# Politica de confidențialitate a Plume

**Ultima actualizare: 31 iulie 2026** — Versiunea 1.0

---

## Cine este operatorul datelor dumneavoastră

**SASU RedLine Music**
SIREN 938 277 100 — SIRET `938 277 100 00013`
Abbaye 208-1, 208 Résidence Lavoisier, 18100 Vierzon, France
Contact: sogacmoi7@gmail.com

Aplicația este publicată pe Google Play sub numele de editor **openfunword**.

Prezenta politică descrie ce face aplicația Plume în versiunea sa actuală. A fost redactată prin citirea codului aplicației, nu pornind de la un model generic.

---

## Într-un minut

Plume vă ajută să scrieți: reformulează textul dumneavoastră direct în aplicația în care tastați și poate traduce textul afișat pe ecran.

Trei lucruri de reținut:

1. **Plume nu păstrează niciunul dintre textele dumneavoastră pe serverele sale.** Nici textele reformulate, nici textul citit de pe ecran. Nu păstrăm nici copie, nici jurnal.
2. **În funcție de motorul pe care îl alegeți, textul dumneavoastră iese sau nu iese din telefon.** Două motoare (Kitul local și IA locală) lucrează în întregime pe dispozitiv. Al treilea (IA Cloud) trimite textul către un serviciu de inteligență artificială **situat în afara Uniunii Europene**. Dumneavoastră alegeți, iar IA Cloud nu se activează niciodată fără acordul dumneavoastră explicit.
3. **Plume are nevoie de permisiuni puternice** (citirea conținutului afișat în celelalte aplicații, capturarea ecranului). Explicăm mai jos exact la ce servesc și la ce nu servesc.

---

## 1. Ce citește Plume pe ecranul dumneavoastră și când

### 1.1 Serviciul de accesibilitate

Pentru a rescrie textul dumneavoastră chiar acolo unde îl scrieți, Plume folosește serviciul de accesibilitate al Android. Este o permisiune pe care o activați dumneavoastră înșivă, în setările telefonului, după un ecran explicativ pe care Plume vi-l arată **înainte** de a v-o cere.

Concret:

- **În repaus**, Plume știe doar ce aplicație este deschisă și în ce moment plasați cursorul într-un câmp de introducere a textului. Acest lucru face să apară capsula flotantă — și numai în aplicațiile pe care le-ați configurat dumneavoastră.
- **Conținutul câmpului este citit numai în momentul exact în care atingeți capsula**, pentru a fi rescris și apoi înlocuit pe loc.
- **Câmpurile de parolă sunt excluse.** Aplicația detectează câmpurile de tip parolă (inclusiv codurile numerice și câmpurile web) și refuză să le citească.
- Această permisiune **nu permite nicio capturare de imagine** a ecranului dumneavoastră.
- Plume **nu apasă niciodată în locul dumneavoastră** într-o altă aplicație: înlocuiește textul dintr-un câmp, nimic altceva.

Două funcții pe care le activați dumneavoastră înșivă — **Citirea Asistată în modul Text** și **traducerea mesajelor primite** — citesc textul afișat în mod continuu atât timp cât rulează și se opresc de îndată ce le opriți.

Dacă refuzați serviciul de accesibilitate, Plume rămâne utilizabilă: puteți selecta un text și folosi meniul „Plume” al selecției Android sau puteți partaja un text către Plume.

### 1.2 Capturarea ecranului (Citirea Asistată)

Citirea Asistată suprapune o traducere peste textul afișat — de exemplu peste bulele unei benzi desenate. Are nevoie să vadă imaginea ecranului.

- Este **dezactivată în mod implicit** și funcționează numai în aplicațiile pe care le-ați autorizat explicit, una câte una.
- **Android vă cere propriul său consimțământ la fiecare pornire de sesiune.** Nu este o permisiune acordată o dată pentru totdeauna: fiecare sesiune necesită un nou acord. Plume nu încearcă niciodată să reutilizeze sau să eludeze acest acord.
- Pe toată durata sesiunii, **o notificare permanentă și un indicator de sistem rămân vizibile**. Plume nu poate captura ecranul dumneavoastră pe ascuns.
- Sesiunea **se oprește automat la blocarea ecranului** și imediat atunci când o opriți dumneavoastră.
- Aplicațiile care își protejează afișajul (aplicații bancare, gestionare de parole) sunt **mascate de Android însuși** înainte ca Plume să primească ceva. Este o protecție a sistemului, reală, dar parțială: nu toate aplicațiile sensibile o activează. De aceea nu o prezentăm ca pe o garanție absolută.
- **Imaginile capturate nu sunt niciodată salvate și nici trimise.** Fiecare imagine este analizată în memorie pentru a extrage textul, apoi este abandonată. Nicio imagine nu pleacă din telefonul dumneavoastră, niciodată, indiferent de motorul ales.

---

## 2. Ce rămâne pe telefonul dumneavoastră și ce pleacă

Este distincția cea mai importantă din prezenta politică, iar dumneavoastră sunteți cel care o controlează.

### 2.1 Motoarele care nu scot nimic din telefon

- **Kitul local** (recunoașterea și traducerea textului offline) funcționează în întregime pe dispozitiv.
- **IA locală** este un model de inteligență artificială descărcat o singură dată și apoi stocat pe telefonul dumneavoastră (aproximativ 720 Mo). Se execută pe dispozitivul dumneavoastră.

Cu aceste două motoare, **textul citit sau reformulat nu iese din telefonul dumneavoastră.** Nu există niciun apel de rețea legat de conținutul textului dumneavoastră.

### 2.2 Motorul IA Cloud

Când alegeți IA Cloud sau când dispozitivul dumneavoastră nu este suficient de puternic pentru IA locală, textul în cauză este transmis serverelor noastre, apoi unui serviciu terț de inteligență artificială.

**Trebuie să fim clari cu privire la traseul real:**

- Textul tranzitează infrastructura noastră (Supabase), găzduită în **Uniunea Europeană** (regiunea Europa Centrală, Frankfurt).
- Este apoi transmis către **openrouter.ai**, un intermediar de rutare **situat în afara Uniunii Europene**, care îl dă spre prelucrare modelului **Mistral Small**.
- **Este vorba, prin urmare, despre un transfer de date în afara Uniunii Europene.** Nu pretindem contrariul și nu afișăm nicio promisiune de găzduire europeană pentru această etapă.
- **Plume nu păstrează textul dumneavoastră.** Niciuna dintre funcțiile noastre de server nu scrie conținutul textului dumneavoastră: înregistrăm doar un identificator tehnic al cererii și identificatorul dispozitivului dumneavoastră, pentru a vă contoriza cota și pentru a detecta abuzurile.
- **Ceea ce fac acești furnizori la rândul lor nu putem garanta.** Preferăm să vă spunem acest lucru decât să vă promitem o păstrare zero pe care nu suntem în măsură să o verificăm.

**IA Cloud nu se activează niciodată singură.** Un ecran de consimțământ dedicat vă explică aceste aspecte înainte de prima trimitere și nu pleacă nimic atât timp cât nu ați acceptat. Dacă IA locală eșuează, Plume nu trece la cloud în tăcere: vă semnalează acest lucru și așteaptă decizia dumneavoastră. Puteți retrage acest acord în orice moment din setări.

Textul trimis este plafonat: 1 200 de caractere pentru o reformulare, 4 000 de caractere pentru o analiză de ecran.

---

## 3. Datele pe care le păstrăm

Nu folosim **niciun instrument de analiză a audienței, niciun tracker publicitar terț, niciun instrument de raportare a erorilor**. Aplicația nu conține niciun SDK de măsurare.

Iată tot ceea ce este stocat pe serverele noastre:

| Date | De ce | Durată |
|---|---|---|
| **Identificatorul dispozitivului** (un număr aleatoriu generat de Plume, fără legătură cu identitatea dumneavoastră și fără legătură cu un identificator publicitar) | Asocierea unui dispozitiv cu un cont, aplicarea cotelor, blocarea abuzurilor | Până la ștergerea contului dumneavoastră |
| **Adresa de e-mail a contului** (dacă vă creați un cont prin e-mail sau prin Google) | Autentificarea dumneavoastră, asocierea abonamentului dumneavoastră | Până la ștergerea contului dumneavoastră |
| **Contoare de utilizare** (numărul de reformulări pe zi și pe lună — numere, nu texte) | Aplicarea cotelor | Până la ștergerea contului dumneavoastră |
| **Istoricul achizițiilor** (identificatorul tranzacției Google Play, date, starea abonamentului) | Acordarea accesului la ceea ce ați plătit, gestionarea reînnoirilor, respectarea obligațiilor noastre contabile | Păstrat chiar și după ștergerea contului, dar **detașat de identitatea dumneavoastră** (a se vedea §6) |
| **Sugestii trimise în mod voluntar** (dacă ne scrieți o sugestie de persona din aplicație) | Îmbunătățirea catalogului. Aceste sugestii nu sunt niciodată publicate. | Până la ștergerea contului dumneavoastră |
| **Semnale tehnice de abuz** (depășiri repetate, eșec al controlului de integritate — fără niciun text) | Securitate, combaterea fraudei | Detașate de identitatea dumneavoastră la ștergerea contului |
| **Limba și versiunea aplicației** | Livrarea conținutului potrivit | Până la ștergerea contului dumneavoastră |

**Ce nu colectăm:** numele dumneavoastră, contactele dumneavoastră, localizarea dumneavoastră, agenda dumneavoastră de adrese, fotografiile dumneavoastră, calendarul dumneavoastră, istoricul aplicațiilor dumneavoastră. Plume nu solicită niciuna dintre aceste permisiuni.

**Ce rămâne exclusiv pe telefonul dumneavoastră:** personele dumneavoastră personalizate și avatarurile lor, setările dumneavoastră, regulile dumneavoastră per aplicație, memoria cache de traducere a Citirii Asistate (ștearsă la sfârșitul fiecărei sesiuni). Nimic din toate acestea nu este trimis către serverele noastre.

---

## 4. Dictarea vocală

Un buton de microfon vă permite să dictați în loc să tastați. Permisiunea de acces la microfon este solicitată **exact în momentul în care apăsați acest buton**, niciodată la pornire, iar microfonul se deschide doar în acel moment. Plume nu ascultă niciodată în fundal.

**Plume nu primește, nu stochează și nu transmite nicio înregistrare audio.** Dictarea este încredințată motorului de recunoaștere vocală integrat în telefonul dumneavoastră (cel al Android). Plume preia doar textul transcris.

**Un aspect important, spus cinstit:** acest motor de sistem aparține telefonului dumneavoastră, în general Google. În funcție de dispozitivul dumneavoastră, de setările acestuia și de modulele de limbă instalate, **el poate transmite conținutul audio către serverele editorului său** pentru a-l transcrie. Această prelucrare nu se află sub controlul Plume și ține de politica de confidențialitate a editorului sistemului dumneavoastră. Prin urmare, nu putem afirma că vocea dumneavoastră rămâne pe dispozitiv — acest lucru depinde de telefonul dumneavoastră, nu de noi.

Dacă refuzați permisiunea pentru microfon, introducerea de la tastatură rămâne, bineînțeles, disponibilă.

---

## 5. Publicitatea

Serviciul este gratuit în limita unui anumit număr de utilizări pe zi. Peste această limită, puteți **alege** să vizionați o reclamă cu recompensă pentru a debloca utilizări suplimentare. Acest lucru nu este niciodată impus: dacă nu vizionați nicio reclamă, păstrați pur și simplu ceea ce vi se cuvine.

- Reclamele sunt furnizate de **Google AdMob**.
- Ele apar **numai în aplicația Plume propriu-zisă**, niciodată în capsula flotantă și niciodată peste o altă aplicație.
- **Abonații nu văd nicio reclamă.**
- În Spațiul Economic European, în Regatul Unit și în Elveția, vi se prezintă **înainte de prima reclamă** un formular de consimțământ furnizat de o platformă certificată de Google. Atât timp cât alegerea dumneavoastră nu a fost colectată, nu se solicită nicio reclamă. Dacă refuzați, reclamele rămân **nepersonalizate** și **nu vi se retrage nicio funcționalitate**. Puteți reveni asupra acestei alegeri în orice moment din setări.
- Pentru a vă credita recompensa în mod fiabil, identificatorul dispozitivului dumneavoastră Plume este transmis către AdMob. De altfel, Google poate colecta propriile sale date în conformitate cu politica sa de confidențialitate.

*La data redactării, difuzarea publicitară este dezactivată pe partea de server. Prezenta secțiune descrie funcționarea de îndată ce aceasta va fi activată.*

---

## 6. Abonamente și achiziții

Abonamentele și pachetele sunt vândute **prin Google Play**. Nu vedem niciodată datele dumneavoastră bancare: acestea sunt prelucrate de Google, care este vânzătorul în sensul facturării.

Primim de la Google o dovadă de achiziție pe care serverul nostru o verifică și păstrăm urma acesteia (identificatorul tranzacției, date, stare). Această urmă este păstrată din motive contabile și pentru a împiedica folosirea de două ori a aceleiași achiziții — dar este **detașată de identitatea dumneavoastră** atunci când vă ștergeți contul.

---

## 7. Drepturile dumneavoastră

Beneficiați de drepturile de acces, de rectificare, de ștergere, de restricționare a prelucrării, de opoziție și de portabilitate a datelor, prevăzute de GDPR.

**Cel mai simplu și cel mai rapid: ștergerea este integrată în aplicație.**
Setări → Confidențialitate → Ștergeți datele mele. Ea este **executată imediat**, nu este pusă într-o coadă de așteptare. Detaliile privind ceea ce este șters și ceea ce este păstrat figurează în pagina noastră dedicată: `https://readit0.github.io/plume-legal/suppression-compte`.

Vă puteți șterge contul și **fără a instala aplicația**, scriind la sogacmoi7@gmail.com.

Pentru orice altă cerere, scrieți la **sogacmoi7@gmail.com**. Răspundem în termen de o lună.

**Temeiuri juridice:** executarea contractului (furnizarea serviciului pe care îl solicitați, gestionarea abonamentului dumneavoastră), consimțământul dumneavoastră (serviciul de accesibilitate, capturarea ecranului, trimiterea către IA Cloud, publicitatea personalizată), interesul nostru legitim (securitate, combaterea fraudei) și obligațiile noastre legale (contabilitate).

Puteți depune o plângere la **CNIL** (www.cnil.fr), autoritatea de supraveghere a editorului, sau, **dacă aveți reședința în Uniunea Europeană**, la autoritatea de supraveghere din țara dumneavoastră de reședință — articolul 77 din GDPR vă lasă alegerea.

---

## 8. Minorii

Plume este un instrument de asistență la redactare, destinat unui public **de 16 ani și peste**. Nu colectăm cu bună știință date ale copiilor sub 16 ani, iar aplicația nu este concepută și nici promovată pentru ei. Dacă sunteți titularul autorității părintești și considerați că un copil al dumneavoastră ne-a transmis date, scrieți la sogacmoi7@gmail.com: vom șterge contul.

Întrucât aplicația permite reformularea unui text liber și afișează publicitate, ea nu este eligibilă pentru programele Google Play destinate familiilor.

---

## 9. Persoane împuternicite de operator și destinatari

| Furnizor | Rol | Unde |
|---|---|---|
| **Supabase** | Găzduirea bazei de date, autentificare, funcții de server | Uniunea Europeană (Frankfurt) |
| **OpenRouter** | Direcționarea cererilor către modelul de IA | **În afara Uniunii Europene** |
| **Mistral AI** (prin OpenRouter) | Modelul care prelucrează textul (Mistral Small) | Prelucrare prin intermediarul de mai sus |
| **Google Play / Google Billing** | Plată, abonamente | Google Ireland / Statele Unite |
| **Google AdMob** | Publicitate cu recompensă | Google Ireland / Statele Unite |
| **Google (serviciile de sistem ale telefonului)** | Recunoaștere vocală, module de traducere offline | În funcție de dispozitivul dumneavoastră |

**Nu vindem niciun fel de date și nu cedăm date către brokeri de date.**

**Transferuri în afara Uniunii Europene:** recurgerea la OpenRouter, la Google Play și la AdMob implică un transfer de date în afara Uniunii Europene. Cadrul juridic al acestor transferuri (clauze contractuale standard, decizie privind caracterul adecvat al nivelului de protecție) **trebuie verificat și documentat de un profesionist înainte de publicare** — a se vedea nota de la sfârșitul documentului.

---

## 10. Securitatea

Schimburile dintre aplicație și serverele noastre sunt criptate (HTTPS/TLS). Accesul la datele din baza de date este restricționat prin reguli de server: funcțiile sensibile nu sunt accesibile din aplicație. Niciun sistem nu este perfect sigur, dar niciun text pe care îl reformulați nu este stocat la noi — ceea ce limitează în mod mecanic ceea ce ar putea dezvălui o intruziune.

---

## 11. Modificări

Orice modificare a prezentei politici va fi publicată la adresa `https://readit0.github.io/plume-legal`, cu o dată nouă. În cazul unei schimbări importante privind circulația datelor dumneavoastră, vă vom informa în aplicație.

---

## Termeni și condiții

Condițiile de utilizare a serviciului (cote, abonamente, reziliere) figurează într-un document distinct: `https://readit0.github.io/plume-legal/conditions-generales`.

---

> ### De dat spre verificare unui profesionist
>
> Prezentul document a fost redactat prin măsurarea comportamentului real al aplicației, dar **nu a fost redactat de un jurist**. Patru aspecte necesită cu prioritate un aviz profesional:
>
> 1. **Transferul de date în afara Uniunii Europene** către OpenRouter. Este aspectul cel mai sensibil: trebuie stabilit mecanismul de transfer aplicabil, trebuie verificat că există un acord de prelucrare a datelor cu acest furnizor și trebuie consemnat acest lucru aici. Atât timp cât acest lucru nu este făcut, prezentul document descrie transferul fără a afirma că este încadrat juridic.
> 2. **Temeiurile juridice** reținute la §7, în special repartizarea între consimțământ și interes legitim pentru serviciul de accesibilitate.
> 3. **Vârsta minimă** (16 ani) și coerența acesteia cu chestionarul de clasificare a conținutului din Google Play.
> 4. **Mențiunea referitoare la IA** în temeiul regulamentului european privind inteligența artificială (obligația de transparență pentru un sistem cu risc limitat).

---

Prezentul document este o traducere a versiunii în limba franceză, disponibilă la adresa https://readit0.github.io/plume-legal/. Este furnizată cu titlu informativ. În caz de neconcordanță, contactați-ne la sogacmoi7@gmail.com.
