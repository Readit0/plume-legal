# Zásady ochrany osobních údajů aplikace Plume

**Poslední aktualizace: 31. července 2026** — Verze 1.0

---

## Kdo je správcem vašich údajů

**SASU RedLine Music**
SIREN 938 277 100 — SIRET `938 277 100 00013`
Abbaye 208-1, 208 Résidence Lavoisier, 18100 Vierzon, France
Kontakt: sogacmoi7@gmail.com

Aplikace je v Google Play zveřejněna pod jménem vydavatele **openfunworld**.

Tyto zásady popisují, co aplikace Plume dělá ve své současné verzi. Byly sepsány na základě čtení kódu aplikace, nikoli podle obecné šablony.

---

## V jedné minutě

Plume vám pomáhá psát: přeformuluje váš text přímo v aplikaci, ve které právě píšete, a umí přeložit text zobrazený na obrazovce.

Tři věci, které je třeba si zapamatovat:

1. **Plume neuchovává žádný z vašich textů na svých serverech.** Ani vaše přeformulované texty, ani text přečtený z obrazovky. Neuchováváme o nich ani kopii, ani záznam v protokolech.
2. **Podle toho, který engine zvolíte, váš text opustí, nebo neopustí váš telefon.** Dva enginy (Místní sada a Místní AI) pracují výhradně v zařízení. Třetí (Cloudová AI) odesílá text službě umělé inteligence **umístěné mimo Evropskou unii**. Volba je na vás a Cloudová AI se nikdy neaktivuje bez vašeho výslovného souhlasu.
3. **Plume potřebuje silná oprávnění** (číst obsah zobrazený v jiných aplikacích, snímat obrazovku). Níže přesně vysvětlujeme, k čemu slouží a k čemu neslouží.

---

## 1. Co Plume čte na vaší obrazovce a kdy

### 1.1 Služba přístupnosti

Aby Plume mohla přepsat váš text tam, kde jej píšete, používá službu přístupnosti systému Android. Toto oprávnění zapínáte sami, v nastavení telefonu, po vysvětlující obrazovce, kterou vám Plume ukáže **předtím**, než o ně požádá.

Konkrétně:

- **V klidovém stavu** Plume ví pouze to, která aplikace je otevřená a ve kterém okamžiku umístíte kurzor do textového pole. Právě to způsobí, že se objeví plovoucí kapsle — a to výhradně v aplikacích, které jste si sami nastavili.
- **Obsah pole se čte pouze v tom přesném okamžiku, kdy se dotknete kapsle**, aby byl text přepsán a poté na místě nahrazen.
- **Pole s hesly jsou vyloučena.** Aplikace rozpozná pole typu heslo (včetně číselných kódů a webových polí) a odmítne je číst.
- Toto oprávnění **neumožňuje žádné snímání obrazu** vaší obrazovky.
- Plume **za vás nikdy na nic neklikne** v jiné aplikaci: nahradí text v poli, nic víc.

Dvě funkce, které si zapínáte sami — **Asistované čtení v textovém režimu** a **překlad přijatých zpráv** — čtou zobrazený text nepřetržitě po celou dobu svého běhu a zastaví se, jakmile je vypnete.

Pokud službu přístupnosti odmítnete, Plume zůstává použitelná: můžete vybrat text a použít položku „Plume“ v nabídce výběru systému Android, nebo text do aplikace Plume sdílet.

### 1.2 Snímání obrazovky (Asistované čtení)

Asistované čtení překrývá zobrazený text překladem — například bubliny komiksu. Potřebuje k tomu vidět obraz obrazovky.

- Je **ve výchozím stavu vypnuté** a funguje pouze v aplikacích, které jste výslovně povolili, jednu po druhé.
- **Android si při každém spuštění relace vyžádá vlastní souhlas.** Nejde o oprávnění udělené jednou provždy: každá relace vyžaduje nový souhlas. Plume se nikdy nesnaží tento souhlas znovu použít ani jej obejít.
- Po celou dobu relace **zůstávají viditelné trvalé oznámení a systémový indikátor**. Plume nemůže vaši obrazovku snímat nenápadně.
- Relace **se automaticky ukončí při uzamčení obrazovky** a okamžitě tehdy, když ji zastavíte sami.
- Aplikace, které chrání své zobrazení (bankovní aplikace, správci hesel), jsou **zakryty samotným Androidem** dříve, než Plume cokoli obdrží. Jde o ochranu systému, skutečnou, ale částečnou: neaktivují ji všechny citlivé aplikace. Nepředstavujeme ji proto jako absolutní záruku.
- **Snímané obrazy se nikdy neukládají ani neodesílají.** Každý obraz je analyzován v paměti, aby z něj byl získán text, a poté zahozen. Žádný obraz nikdy neopustí váš telefon, ať zvolíte kterýkoli engine.

---

## 2. Co zůstává ve vašem telefonu a co jej opouští

To je nejdůležitější rozlišení těchto zásad a ovládáte je vy.

### 2.1 Enginy, které nic neodesílají ven

- **Místní sada** (rozpoznávání a překlad textu offline) funguje výhradně v zařízení.
- **Místní AI** je model umělé inteligence stažený jednou a poté uložený ve vašem telefonu (přibližně 720 MB). Běží ve vašem zařízení.

U těchto dvou enginů **přečtený nebo přeformulovaný text neopouští váš telefon.** Neprobíhá žádné síťové volání související s obsahem vašeho textu.

### 2.2 Engine Cloudová AI

Když zvolíte Cloudovou AI nebo když vaše zařízení není dostatečně výkonné pro Místní AI, je dotčený text předán na naše servery a poté třetí službě umělé inteligence.

**Je třeba jasně říci, jaká je skutečná trasa:**

- Text prochází naší infrastrukturou (Supabase), umístěnou v **Evropské unii** (region střední Evropa, Frankfurt).
- Poté je předán službě **openrouter.ai**, směrovacímu prostředníkovi **umístěnému mimo Evropskou unii**, který jej nechá zpracovat modelem **Mistral Small**.
- **Jde tedy o předání údajů mimo Evropskou unii.** Netvrdíme opak a pro tento krok neuvádíme žádný příslib evropského hostingu.
- **Plume váš text neuchovává.** Žádná z našich serverových funkcí obsah vašeho textu nezapisuje: zaznamenáváme pouze technický identifikátor požadavku a identifikátor vašeho zařízení, abychom počítali váš limit a odhalovali zneužití.
- **To, co tito poskytovatelé dělají na své straně, zaručit nemůžeme.** Raději vám to řekneme, než abychom vám slibovali nulové uchovávání, které nejsme schopni ověřit.

**Cloudová AI se nikdy neaktivuje sama od sebe.** Vyhrazená obrazovka souhlasu vám tyto body vysvětlí před prvním odesláním a nic neodejde, dokud souhlas neudělíte. Pokud Místní AI selže, Plume nepřepne mlčky do cloudu: oznámí vám to a počká na vaše rozhodnutí. Tento souhlas můžete kdykoli odvolat v nastavení.

Odesílaný text je omezen: 1 200 znaků pro přeformulování, 4 000 znaků pro analýzu obrazovky.

---

## 3. Údaje, které uchováváme

Nepoužíváme **žádný nástroj pro analýzu návštěvnosti, žádný reklamní tracker třetí strany, žádný nástroj pro hlášení pádů**. Aplikace neobsahuje žádnou měřicí sadu SDK.

Zde je vše, co je uloženo na našich serverech:

| Údaj | Proč | Doba |
|---|---|---|
| **Identifikátor zařízení** (náhodné číslo generované aplikací Plume, bez vazby na vaši totožnost a bez vazby na reklamní identifikátor) | Přiřadit zařízení k účtu, uplatňovat limity, blokovat zneužití | Do smazání vašeho účtu |
| **E-mailová adresa účtu** (pokud si vytvoříte účet e-mailem nebo přes Google) | Ověřit vaši totožnost, přiřadit vaše předplatné | Do smazání vašeho účtu |
| **Počítadla využití** (počet přeformulování za den a za měsíc — čísla, nikoli texty) | Uplatňovat limity | Do smazání vašeho účtu |
| **Historie nákupů** (identifikátor transakce Google Play, data, stav předplatného) | Zpřístupnit vám to, co jste zaplatili, spravovat obnovení, plnit naše účetní povinnosti | Uchovávána i po smazání účtu, ale **oddělená od vaší totožnosti** (viz §6) |
| **Dobrovolně zaslané návrhy** (pokud nám z aplikace napíšete návrh persony) | Vylepšovat katalog. Tyto návrhy nejsou nikdy zveřejňovány. | Do smazání vašeho účtu |
| **Technické signály zneužití** (opakovaná překročení, selhání kontroly integrity — bez jakéhokoli textu) | Bezpečnost, boj proti podvodům | Odděleny od vaší totožnosti při smazání účtu |
| **Jazyk a verze aplikace** | Doručovat správný obsah | Do smazání vašeho účtu |

**Co neshromažďujeme:** vaše jméno, vaše kontakty, vaši polohu, váš adresář, vaše fotografie, váš kalendář, historii vašich aplikací. Plume o žádné z těchto oprávnění nežádá.

**Co zůstává výhradně ve vašem telefonu:** vaše vlastní persony a jejich avataři, vaše nastavení, vaše pravidla pro jednotlivé aplikace, mezipaměť překladů Asistovaného čtení (mazaná na konci každé relace). Nic z toho se na naše servery neodesílá.

---

## 4. Hlasové diktování

Tlačítko mikrofonu vám umožňuje diktovat namísto psaní. O oprávnění k přístupu k mikrofonu žádáme **přesně ve chvíli, kdy toto tlačítko stisknete**, nikdy při spuštění, a mikrofon se otevře až v tom okamžiku. Plume nikdy neposlouchá na pozadí.

**Plume nepřijímá, neukládá ani nepředává žádnou zvukovou nahrávku.** Diktování je svěřeno enginu rozpoznávání řeči vestavěnému ve vašem telefonu (tomu od Androidu). Plume přebírá pouze přepsaný text.

**Důležitá a poctivá poznámka:** tento systémový engine patří vašemu telefonu, zpravidla společnosti Google. Podle vašeho zařízení, jeho nastavení a nainstalovaných jazykových modulů **může zvuk pro přepis předávat na servery svého vydavatele**. Toto zpracování je mimo dosah aplikace Plume a řídí se zásadami ochrany osobních údajů vydavatele vašeho systému. Nemůžeme tedy tvrdit, že váš hlas zůstává v zařízení — závisí to na vašem telefonu, nikoli na nás.

Pokud oprávnění k mikrofonu odmítnete, psaní na klávesnici samozřejmě zůstává k dispozici.

---

## 5. Reklama

Služba je zdarma v rámci určitého denního limitu využití. Nad jeho rámec si **můžete zvolit**, že zhlédnete odměňovanou reklamu a odemknete si další použití. Nikdy to není vynucené: pokud reklamu nezhlédnete, prostě si ponecháte to, na co máte nárok.

- Reklamy dodává **Google AdMob**.
- Objevují se **výhradně v samotné aplikaci Plume**, nikdy v plovoucí kapsli a nikdy přes jinou aplikaci.
- **Předplatitelé nevidí žádnou reklamu.**
- V Evropském hospodářském prostoru, ve Spojeném království a ve Švýcarsku je vám **před první reklamou** předložen formulář souhlasu poskytovaný platformou certifikovanou společností Google. Dokud není vaše volba získána, není vyžádána žádná reklama. Pokud odmítnete, zůstávají reklamy **nepersonalizované** a **není vám odebrána žádná funkce**. Ke své volbě se můžete kdykoli vrátit v nastavení.
- Aby vám mohla být odměna spolehlivě připsána, je identifikátor vašeho zařízení Plume předán službě AdMob. Google může kromě toho shromažďovat vlastní údaje v souladu se svými zásadami ochrany osobních údajů.

*Ke dni sepsání tohoto dokumentu je zobrazování reklam na straně serveru vypnuto. Tato část popisuje fungování od okamžiku, kdy bude zapnuto.*

---

## 6. Předplatné a nákupy

Předplatné a balíčky se prodávají **prostřednictvím Google Play**. Vaše bankovní údaje nikdy nevidíme: zpracovává je Google, který je z hlediska fakturace prodávajícím.

Od Googlu obdržíme doklad o nákupu, který náš server ověří, a uchováváme o něm záznam (identifikátor transakce, data, stav). Tento záznam je uchováván z účetních důvodů a proto, aby tentýž nákup nebyl použit dvakrát — při smazání vašeho účtu je však **oddělen od vaší totožnosti**.

---

## 7. Vaše práva

Máte práva na přístup, opravu, výmaz, omezení zpracování, vznesení námitky a přenositelnost údajů, která stanoví GDPR.

**Nejjednodušší a nejrychlejší cesta: mazání je zabudováno v aplikaci.**
Nastavení → Soukromí → Smazat moje data. Provede se **okamžitě**, nikoli ve frontě. Podrobnosti o tom, co se maže a co se uchovává, jsou uvedeny na naší vyhrazené stránce: `https://readit0.github.io/plume-legal/suppression-compte`.

Svůj účet můžete smazat i **bez instalace aplikace**, a to zasláním e-mailu na sogacmoi7@gmail.com.

S jakoukoli jinou žádostí se obraťte na **sogacmoi7@gmail.com**. Odpovídáme do jednoho měsíce.

**Právní základy:** splnění smlouvy (poskytnutí služby, o kterou žádáte, správa vašeho předplatného), váš souhlas (služba přístupnosti, snímání obrazovky, odeslání do Cloudové AI, personalizovaná reklama), náš oprávněný zájem (bezpečnost, boj proti podvodům) a naše právní povinnosti (účetnictví).

Můžete podat stížnost u **CNIL** (www.cnil.fr), dozorového úřadu vydavatele, nebo, **máte-li bydliště v Evropské unii**, u dozorového úřadu země svého bydliště — článek 77 GDPR vám ponechává volbu.

---

## 8. Nezletilí

Plume je nástroj pro pomoc s psaním určený publiku **od 16 let výše**. Vědomě neshromažďujeme údaje dětí mladších 16 let a aplikace pro ně není ani navržena, ani propagována. Pokud jste nositelem rodičovské odpovědnosti a domníváte se, že nám vaše dítě předalo údaje, napište na sogacmoi7@gmail.com: účet smažeme.

Protože aplikace umožňuje přeformulovat volný text a zobrazuje reklamu, není způsobilá pro programy Google Play určené rodinám.

---

## 9. Zpracovatelé a příjemci

| Poskytovatel | Role | Kde |
|---|---|---|
| **Supabase** | Hosting databáze, ověřování, serverové funkce | Evropská unie (Frankfurt) |
| **OpenRouter** | Směrování požadavků k modelu AI | **Mimo Evropskou unii** |
| **Mistral AI** (přes OpenRouter) | Model, který text zpracovává (Mistral Small) | Zpracování prostřednictvím výše uvedeného prostředníka |
| **Google Play / Google Billing** | Platba, předplatné | Google Ireland / Spojené státy |
| **Google AdMob** | Odměňovaná reklama | Google Ireland / Spojené státy |
| **Google (systémové služby telefonu)** | Rozpoznávání řeči, moduly offline překladu | Podle vašeho zařízení |

**Žádné údaje neprodáváme a žádné nepostupujeme datovým brokerům.**

**Předávání mimo Evropskou unii:** využití služeb OpenRouter, Google Play a AdMob zahrnuje předání údajů mimo Evropskou unii. Právní rámec těchto předání (standardní smluvní doložky, rozhodnutí o odpovídající ochraně) **musí být před zveřejněním ověřen a zdokumentován odborníkem** — viz poznámku na konci dokumentu.

---

## 10. Bezpečnost

Komunikace mezi aplikací a našimi servery je šifrovaná (HTTPS/TLS). Přístup k údajům v databázi je omezen pravidly na straně serveru: citlivé funkce nejsou z aplikace dostupné. Žádný systém není dokonale bezpečný, ale žádný text, který přeformulujete, u nás není uložen — což mechanicky omezuje to, co by mohlo vniknutí do systému odhalit.

---

## 11. Změny

Každá změna těchto zásad bude zveřejněna na adrese `https://readit0.github.io/plume-legal` s novým datem. V případě podstatné změny v pohybu vašich údajů vás o tom uvědomíme v aplikaci.

---

## Všeobecné podmínky

Podmínky užívání služby (limity, předplatné, ukončení) jsou uvedeny v samostatném dokumentu: `https://readit0.github.io/plume-legal/conditions-generales`.

---

> ### K posouzení odborníkem
>
> Tento dokument byl sepsán měřením skutečného chování aplikace, **nebyl však sepsán právníkem**. Čtyři body si přednostně zaslouží odborné stanovisko:
>
> 1. **Předání údajů mimo Evropskou unii** službě OpenRouter. Jde o nejcitlivější bod: je třeba určit použitelný mechanismus předání, ověřit, že s tímto poskytovatelem existuje smlouva o zpracování osobních údajů, a uvést to zde. Dokud se tak nestane, tento dokument předání popisuje, aniž by tvrdil, že je právně ošetřeno.
> 2. **Právní základy** zvolené v §7, zejména rozdělení mezi souhlas a oprávněný zájem u služby přístupnosti.
> 3. **Minimální věk** (16 let) a jeho soulad s dotazníkem klasifikace obsahu Google Play.
> 4. **Zmínka o umělé inteligenci** podle evropského nařízení o umělé inteligenci (povinnost transparentnosti u systému s omezeným rizikem).

---

Tento dokument je překladem francouzské verze, dostupné na adrese https://readit0.github.io/plume-legal/. Překlad poskytujeme pro vaši informaci. V případě rozporu nás kontaktujte na adrese sogacmoi7@gmail.com.
