# Izbris vašega računa in vaših podatkov — Plume

**Zadnja posodobitev: 31. julij 2026** — Različica 1.0

Zadevna aplikacija: **Plume** (`com.plume.plume`), ki jo izdaja **SASU RedLine Music**, Abbaye 208-1, 208 Résidence Lavoisier, 18100 Vierzon, France — objavljena v Google Play pod imenom **openfunworld**.

---

## Dva načina za izbris računa

### 1. Iz aplikacije (najhitreje)

**Nastavitve → Zasebnost → Izbriši moje podatke**

Izbris se **izvede takoj**. Ne uvrsti se v čakalno vrsto in ne čaka na nobeno odloženo obdelavo: ko vam aplikacija izbris potrdi, se je ta že zgodil in ga je strežnik preveril.

### 2. Brez namestitve aplikacije

Če ste Plume že odstranili ali če do svojega telefona nimate več dostopa, pišite na:

**sogacmoi7@gmail.com**

- Zadeva: **Izbris računa Plume**
- Navedite **e-poštni naslov svojega računa Plume** (tistega, s katerim ste se registrirali, ali svoj Googlov naslov, če ste se prijavili prek Googla).

Preverimo, ali zahteva res prihaja od imetnika računa, nato pa izvedemo izbris. **Te zahteve obravnavamo najpozneje v 30 dneh**, praviloma pa v nekaj dneh. Po opravljenem izbrisu prejmete potrdilo po e-pošti.

---

## Kaj se izbriše

Izbris **dokončno** odstrani:

- **vaš račun** (e-poštni naslov, geslo, sejo);
- **vaše števce uporabe** — število preoblikovanj, porabljenih na dan in na mesec;
- **vaše predloge** — predloge, ki ste nam jih poslali iz aplikacije. To je edino prosto besedilo, ki smo ga hranili;
- **vaše identifikatorje zahtev** — tehnične reference zahtevanih preoblikovanj;
- **vaše dobropise in odklepe kvote** — kupljene neporabljene dobropise, odklepe, pridobljene z oglasom, prilagojene zgornje meje;
- **povezanost vaših naprav z vašim računom** — vaši drugi telefoni ali tablice se odvežejo in spet postanejo navadne anonimne naprave.

Naprava, s katere zahtevate izbris, se **nevtralizira**: njena povezanost z vašim računom se izbriše, njen identifikacijski ključ se uniči in nadomesti z mrtvo vrednostjo, njen jezik in različica aplikacije se izbrišeta. Ostane le neprozorna številka, ki ne omogoča več niti vaše identifikacije niti najdbe naprave.

**Vaših besedil nismo nikoli hranili.** Ne besedil, ki ste jih preoblikovali, ne besedila, ki ga je Asistirano branje prebralo z zaslona: nikjer na naših strežnikih se niso hranila, zato od njih ni ničesar za izbrisati.

**Na vašem telefonu** so vaše persone, vaši avatarji, vaše nastavitve in vaša pravila po aplikaciji shranjeni lokalno. Izbriše jih izbris, sprožen iz aplikacije, v vsakem primeru pa **izginejo, ko odstranite Plume**.

---

## Kaj se ohrani in zakaj

Ostanejo tri kategorije sledi, vendar je **povezava z vašo identiteto prekinjena**: identifikator vašega računa in identifikator vaše naprave sta iz njih odstranjena. Ti zapisi ne omogočajo več, da bi prišli do vas.

| Kaj ostane | Zakaj tega ne moremo uničiti |
|---|---|
| **Zgodovina vaših nakupov** (identifikator transakcije Google Play, znesek, datumi, stanje naročnine) | Računovodska obveznost: dokazila o plačilu se ne uniči. Hrani se **ločeno od vaše identitete**. |
| **Pravice, pridobljene z nakupom** (naročnina, paketi) | Isti računovodski razlog in dokaz o plačilu v primeru spora. Hranijo se **brez uporabniškega identifikatorja**. |
| **Oglaševalske nagrade in že dodeljeni dobropisi** | Preprečuje, da bi bil isti oglas ali isti nakup unovčen dvakrat. Hrani se le enolična referenca transakcije, **brez identifikatorja naprave**. |
| **Tehnični varnostni signali** (ponavljajoče se prekoračitve, neuspešna preverjanja celovitosti) | Boj proti goljufijam. Ti zapisi ne vsebujejo **nobenega besedila** in se hranijo **brez identifikatorja naprave**. |

Ti anonimizirani podatki se hranijo toliko časa, kolikor zahtevajo naše zakonske, zlasti računovodske obveznosti, nato pa se izbrišejo ali združijo.

---

## Česa izbris ne stori

**Ne odpove vaše naročnine.** Naročnino upravlja Google Play, ne mi: izbris vašega računa Plume je ne ustavi in **obremenitve bi se nadaljevale**.

**Najprej odpovejte naročnino**, nato izbrišite račun:
Play Store → Meni → Plačila in naročnine → Naročnine → Plume → Prekliči naročnino.

**Ne izbriše podatkov, ki jih hrani Google** (nakupi, oglaševanje, prepoznavanje govora v telefonu). Ti podatki spadajo pod vaš Googlov račun in se urejajo v nastavitvah vašega Googlovega računa.

---

## Po izbrisu

Izbris je **dokončen in nepovraten**. Izbrisanega računa ne moremo obnoviti, prav tako ne vaših person ne vaših nakupov, vezanih na ta račun.

Pozneje lahko znova ustvarite račun z istim e-poštnim naslovom: to bo **povsem nov** račun, brez zgodovine. Vaših prejšnjih nakupov, ker so bili ločeni od vsakršne identitete, **ne bo mogoče obnoviti** na tem novem računu. Če želite ohraniti tekočo naročnino, računa ne brišite.

---

## Vaše druge pravice

Poleg izbrisa imate pravice do dostopa, popravka, omejitve obdelave, ugovora in prenosljivosti podatkov, ki jih določa Splošna uredba o varstvu podatkov (GDPR). Pišite na **sogacmoi7@gmail.com**.

Podrobnosti o obdelanih podatkih so v naši politiki zasebnosti: `https://readit0.github.io/plume-legal/politique-confidentialite`.

Pritožbo lahko vložite pri organu **CNIL** (www.cnil.fr).

---

> ### V pregled strokovnjaku
>
> Ta stran natančno opisuje vedenje kode za izbris, preverjene vrstico za vrstico. Tri točke zahtevajo strokovno mnenje ali odločitev pred objavo:
>
> 1. **Rok hrambe anonimiziranih računovodskih podatkov** tukaj ni izražen s številko. To mora biti: zakonski rok hrambe računovodskih listin v Franciji je deset let, tehnična dokumentacija projekta pa omenja strnjevanje nakupnih dogodkov na 24 mesecev. **Ta roka je treba uskladiti**, nato pa ju vpisati na to stran in v politiko zasebnosti.
> 2. **Postopek preverjanja istovetnosti** za zahteve po e-pošti je treba določiti in dokumentirati: sprejeti izbris na podlagi zgolj izjave izpostavlja tveganju zlonamernega izbrisa; zahtevati preveč pomeni oviro, ki je v nasprotju s Splošno uredbo o varstvu podatkov.
> 3. **Opozorilo o nakupih, ki jih po izbrisu ni mogoče obnoviti**, je vredno potrditi: izhaja iz dejstva, da so pravice iz nakupov anonimizirane, in mora biti prikazano **v aplikaciji ob potrditvi**, ne le na tej strani.

---

Ta dokument je prevod francoske različice, ki je na voljo na naslovu https://readit0.github.io/plume-legal/. Na voljo je za vašo informacijo. V primeru odstopanj nam pišite na sogacmoi7@gmail.com.
