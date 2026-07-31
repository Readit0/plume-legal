# Plumes integritetspolicy

**Senast uppdaterad: 31 juli 2026** — Version 1.0

---

## Vem som är personuppgiftsansvarig för dina uppgifter

**SASU RedLine Music**
SIREN 938 277 100 — SIRET `938 277 100 00013`
Abbaye 208-1, 208 Résidence Lavoisier, 18100 Vierzon, France
Kontakt: sogacmoi7@gmail.com

Appen ges ut på Google Play under utgivarnamnet **openfunword**.

Den här policyn beskriver vad appen Plume gör i sin nuvarande version. Den har skrivits genom att läsa appens kod, inte utifrån en generisk mall.

---

## På en minut

Plume hjälper dig att skriva: den formulerar om din text direkt i den app där du håller på att skriva, och den kan översätta text som visas på skärmen.

Tre saker att komma ihåg:

1. **Plume sparar ingen av dina texter på sina servrar.** Varken dina omformulerade texter eller den text som läses av på skärmen. Vi behåller varken kopia eller logg.
2. **Beroende på vilken motor du väljer lämnar din text telefonen — eller inte.** Två motorer (det lokala kitet och den lokala AI:n) arbetar helt och hållet på enheten. Den tredje (Moln-AI) skickar texten till en tjänst för artificiell intelligens **som ligger utanför Europeiska unionen**. Du väljer, och Moln-AI aktiveras aldrig utan ditt uttryckliga samtycke.
3. **Plume behöver kraftfulla behörigheter** (läsa innehåll som visas i andra appar, spela in skärmen). Vi förklarar nedan exakt vad de används till och vad de inte används till.

---

## 1. Vad Plume läser på din skärm, och när

### 1.1 Tillgänglighetstjänsten

För att kunna skriva om din text på den plats där du skriver den använder Plume Androids tillgänglighetstjänst. Det är en behörighet som du själv aktiverar i telefonens inställningar, efter en förklaringsskärm som Plume visar dig **innan** den ber om den.

Konkret:

- **I viloläge** vet Plume bara vilken app som är öppen och i vilket ögonblick du placerar markören i ett inmatningsfält. Det är det som får den flytande kapseln att dyka upp — och bara i de appar som du själv har ställt in.
- **Innehållet i fältet läses av först i det exakta ögonblick då du trycker på kapseln**, för att skrivas om och sedan ersättas på plats.
- **Lösenordsfält är uteslutna.** Appen upptäcker fält av lösenordstyp (även numeriska koder och webbfält) och vägrar att läsa dem.
- Den här behörigheten **gör det inte möjligt att ta någon bild** av din skärm.
- Plume **trycker aldrig i ditt ställe** i en annan app: den ersätter texten i ett fält, ingenting annat.

Två funktioner som du själv aktiverar — **Assisterad läsning i textläge** och **översättning av mottagna meddelanden** — läser den text som visas löpande så länge de är igång, och stannar så snart du stänger av dem.

Om du nekar tillgänglighetstjänsten går Plume fortfarande att använda: du kan markera en text och gå via menyvalet ”Plume” i Androids markeringsmeny, eller dela en text till Plume.

### 1.2 Skärminspelningen (Assisterad läsning)

Assisterad läsning lägger en översättning ovanpå den text som visas — till exempel pratbubblorna i en serie. Den behöver se bilden av skärmen.

- Den är **avstängd som standard** och fungerar bara i de appar som du uttryckligen har tillåtit, en och en.
- **Android ber om sitt eget samtycke varje gång en session startar.** Det är inte en behörighet som ges en gång för alla: varje session kräver ett nytt godkännande. Plume försöker aldrig återanvända eller kringgå det godkännandet.
- Under hela sessionen **syns en permanent avisering och en systemindikator**. Plume kan inte spela in din skärm i smyg.
- Sessionen **avbryts automatiskt när skärmen låses**, och omedelbart när du själv stoppar den.
- Appar som skyddar sin visning (bankappar, lösenordshanterare) **döljs av Android självt** innan Plume tar emot någonting alls. Det är ett skydd i systemet, verkligt men ofullständigt: alla känsliga appar aktiverar det inte. Vi framställer det därför inte som en absolut garanti.
- **De inspelade bilderna sparas aldrig och skickas aldrig.** Varje bild analyseras i minnet för att texten ska kunna hämtas ur den, och överges sedan. Ingen bild lämnar din telefon, aldrig, oavsett vilken motor du har valt.

---

## 2. Vad som stannar i din telefon och vad som lämnar den

Det är den viktigaste skillnaden i den här policyn, och det är du som styr den.

### 2.1 Motorerna som inte skickar ut någonting

- **Det lokala kitet** (igenkänning och översättning av text offline) fungerar helt och hållet på enheten.
- **Den lokala AI:n** är en modell för artificiell intelligens som laddas ned en gång och sedan lagras i din telefon (cirka 720 MB). Den körs på din enhet.

Med de här två motorerna **lämnar den text som läses av eller skrivs om inte din telefon.** Det görs inget nätverksanrop som rör innehållet i din text.

### 2.2 Motorn Moln-AI

När du väljer Moln-AI, eller när din enhet inte är tillräckligt kraftfull för den lokala AI:n, skickas den berörda texten till våra servrar och därefter till en tredje parts tjänst för artificiell intelligens.

**Det gäller att vara tydlig med den verkliga färdvägen:**

- Texten passerar vår infrastruktur (Supabase), som ligger i **Europeiska unionen** (regionen Centraleuropa, Frankfurt).
- Den skickas därefter till **openrouter.ai**, en routningsförmedlare **som ligger utanför Europeiska unionen**, som låter modellen **Mistral Small** behandla den.
- **Det rör sig alltså om en överföring av uppgifter till ett land utanför Europeiska unionen.** Vi påstår inte motsatsen, och vi visar inget löfte om europeisk lagring för det steget.
- **Plume sparar inte din text.** Ingen av våra serverfunktioner skriver ned innehållet i din text: vi registrerar bara en teknisk identifierare för förfrågan och identifieraren för din enhet, för att räkna din kvot och upptäcka missbruk.
- **Vad de här leverantörerna gör på sin sida kan vi inte garantera.** Vi föredrar att säga det rakt ut i stället för att lova dig en nollagring som vi inte har möjlighet att kontrollera.

**Moln-AI aktiveras aldrig av sig själv.** En särskild samtyckesskärm förklarar de här punkterna för dig före den första sändningen, och ingenting skickas i väg förrän du har godkänt. Om den lokala AI:n misslyckas växlar Plume inte över till molnet i tysthet: den talar om det för dig och väntar på ditt beslut. Du kan när som helst återkalla det godkännandet i inställningarna.

Den text som skickas har ett tak: 1 200 tecken för en omformulering, 4 000 tecken för en skärmanalys.

---

## 3. De uppgifter vi sparar

Vi använder **inget verktyg för besöksanalys, ingen tredjepartsspårare för reklam och inget verktyg för kraschrapportering**. Appen innehåller inget mät-SDK.

Här är allt som lagras på våra servrar:

| Uppgift | Varför | Hur länge |
|---|---|---|
| **Enhetsidentifierare** (ett slumpmässigt nummer som Plume genererar, utan koppling till din identitet eller till något annons-ID) | Koppla en enhet till ett konto, tillämpa kvoterna, blockera missbruk | Till dess att ditt konto raderas |
| **Kontots e-postadress** (om du skapar ett konto med e-post eller via Google) | Autentisera dig, koppla din prenumeration | Till dess att ditt konto raderas |
| **Användningsräknare** (antal omformuleringar per dag och per månad — siffror, inte texter) | Tillämpa kvoterna | Till dess att ditt konto raderas |
| **Köphistorik** (transaktionsidentifierare från Google Play, datum, prenumerationens status) | Ge dig tillgång till det du har betalat för, hantera förnyelserna, uppfylla våra bokföringsskyldigheter | Sparas även efter att kontot raderats, men **frikopplad från din identitet** (se §6) |
| **Förslag som skickats frivilligt** (om du skickar oss ett förslag på en persona från appen) | Förbättra katalogen. De här förslagen publiceras aldrig. | Till dess att ditt konto raderas |
| **Tekniska signaler om missbruk** (upprepade överskridanden, misslyckad äkthetskontroll av appen — utan någon text alls) | Säkerhet, bedrägeribekämpning | Frikopplas från din identitet när kontot raderas |
| **Appens språk och version** | Leverera rätt innehåll | Till dess att ditt konto raderas |

**Vad vi inte samlar in:** ditt namn, dina kontakter, din position, din adressbok, dina foton, din kalender, historiken över dina appar. Plume begär ingen av de behörigheterna.

**Vad som bara stannar i din telefon:** dina egna personas och deras avatarer, dina inställningar, dina regler per app, översättningscachen för Assisterad läsning (som töms i slutet av varje session). Ingenting av detta skickas till våra servrar.

---

## 4. Röstdikteringen

En mikrofonknapp låter dig diktera i stället för att skriva. Behörigheten till mikrofonen begärs **i det exakta ögonblick då du trycker på den knappen**, aldrig vid start, och mikrofonen öppnas bara i det ögonblicket. Plume lyssnar aldrig i bakgrunden.

**Plume tar aldrig emot, lagrar eller överför någon ljudinspelning.** Dikteringen anförtros åt den taligenkänningsmotor som är inbyggd i din telefon (Androids). Plume hämtar bara den transkriberade texten.

**En viktig och ärlig punkt:** den systemmotorn tillhör din telefon, i allmänhet Google. Beroende på din enhet, dess inställningar och de språkmoduler som är installerade **kan den skicka ljudet till sin utgivares servrar** för att transkribera det. Den behandlingen ligger utanför Plume och omfattas av integritetspolicyn hos utgivaren av ditt system. Vi kan därför inte påstå att din röst stannar på enheten — det beror på din telefon, inte på oss.

Om du nekar mikrofonbehörigheten är det förstås fortfarande möjligt att skriva på tangentbordet.

---

## 5. Reklam

Tjänsten är gratis inom en viss användningsgräns per dag. Därutöver kan du **välja** att titta på en belönad annons för att låsa upp fler användningar. Det är aldrig påtvingat: om du inte tittar på någon annons behåller du helt enkelt det du har rätt till.

- Annonserna levereras av **Google AdMob**.
- De visas **bara i själva appen Plume**, aldrig i den flytande kapseln och aldrig ovanpå en annan app.
- **Prenumeranter ser ingen reklam.**
- Inom Europeiska ekonomiska samarbetsområdet, i Förenade kungariket och i Schweiz visas ett samtyckesformulär från en plattform som är certifierad av Google **före den första annonsen**. Så länge ditt val inte har inhämtats begärs ingen annons. Om du säger nej förblir annonserna **icke personanpassade** och **ingen funktion tas ifrån dig**. Du kan när som helst ändra det valet i inställningarna.
- För att din belöning ska kunna krediteras på ett tillförlitligt sätt skickas din Plume-enhetsidentifierare till AdMob. Google kan dessutom samla in egna uppgifter i enlighet med sin integritetspolicy.

*Vid tidpunkten för den här texten är annonsvisningen avstängd på serversidan. Det här avsnittet beskriver hur det fungerar så snart den slås på.*

---

## 6. Prenumerationer och köp

Prenumerationerna och paketen säljs **via Google Play**. Vi ser aldrig dina bankuppgifter: de behandlas av Google, som är säljare i faktureringshänseende.

Vi får ett köpbevis av Google som vår server kontrollerar, och vi behåller ett spår av det (transaktionsidentifierare, datum, status). Det spåret sparas av bokföringsskäl och för att hindra att ett och samma köp används två gånger — men det **frikopplas från din identitet** när du raderar ditt konto.

---

## 7. Dina rättigheter

Du har rätt till tillgång, rättelse, radering och begränsning av behandling, rätt att göra invändningar och rätt till dataportabilitet enligt GDPR.

**Det enklaste och snabbaste: raderingen är inbyggd i appen.**
Inställningar → Integritet → Radera mina data. Den **utförs omedelbart**, den läggs inte i kö. Vad som raderas och vad som sparas beskrivs i detalj på vår särskilda sida: `https://readit0.github.io/plume-legal/suppression-compte`.

Du kan också radera ditt konto **utan att installera appen**, genom att skriva till sogacmoi7@gmail.com.

För alla andra önskemål, skriv till **sogacmoi7@gmail.com**. Vi svarar inom en månad.

**Rättsliga grunder:** fullgörandet av avtalet (att leverera den tjänst du efterfrågar, att hantera din prenumeration), ditt samtycke (tillgänglighetstjänsten, skärminspelningen, sändningen till Moln-AI, personanpassad reklam), vårt berättigade intresse (säkerhet, bedrägeribekämpning) och våra rättsliga förpliktelser (bokföring).

Du kan lämna in ett klagomål till **CNIL** (www.cnil.fr), som är utgivarens tillsynsmyndighet, eller, **om du är bosatt i Europeiska unionen**, till tillsynsmyndigheten i ditt hemvistland — artikel 77 i GDPR ger dig valet.

---

## 8. Minderåriga

Plume är ett hjälpmedel för att skriva, avsett för en publik **från 16 år och uppåt**. Vi samlar inte medvetet in uppgifter om barn under 16 år, och appen är varken utformad eller marknadsförd för dem. Om du har vårdnaden om ett barn och tror att ditt barn har lämnat uppgifter till oss, skriv till sogacmoi7@gmail.com: vi raderar kontot.

Eftersom appen gör det möjligt att formulera om fri text och visar reklam är den inte behörig för Google Plays familjeprogram.

---

## 9. Personuppgiftsbiträden och mottagare

| Leverantör | Roll | Var |
|---|---|---|
| **Supabase** | Databashotell, autentisering, serverfunktioner | Europeiska unionen (Frankfurt) |
| **OpenRouter** | Vidarebefordran av förfrågningarna till AI-modellen | **Utanför Europeiska unionen** |
| **Mistral AI** (via OpenRouter) | Modell som behandlar texten (Mistral Small) | Behandling via förmedlaren ovan |
| **Google Play / Google Billing** | Betalning, prenumerationer | Google Ireland / USA |
| **Google AdMob** | Belönad reklam | Google Ireland / USA |
| **Google (telefonens systemtjänster)** | Taligenkänning, offlinemoduler för översättning | Beroende på din enhet |

**Vi säljer inga uppgifter och lämnar inga uppgifter vidare till datamäklare.**

**Överföringar till länder utanför Europeiska unionen:** användningen av OpenRouter, Google Play och AdMob innebär en överföring av uppgifter till ett land utanför Europeiska unionen. Den rättsliga ramen för dessa överföringar (standardavtalsklausuler, beslut om adekvat skyddsnivå) **måste kontrolleras och dokumenteras av en yrkesperson före publicering** — se noten i slutet av dokumentet.

---

## 10. Säkerhet

Utbytet mellan appen och våra servrar är krypterat (HTTPS/TLS). Åtkomsten till uppgifterna i databasen är begränsad av serverregler: de känsliga funktionerna går inte att nå från appen. Inget system är fullkomligt säkert, men ingen text som du formulerar om lagras hos oss — vilket rent mekaniskt begränsar vad ett intrång skulle kunna avslöja.

---

## 11. Ändringar

Varje ändring av den här policyn kommer att publiceras på `https://readit0.github.io/plume-legal` med ett nytt datum. Vid en viktig förändring av hur dina uppgifter cirkulerar informerar vi dig i appen.

---

## Allmänna villkor

Villkoren för att använda tjänsten (kvoter, prenumerationer, uppsägning) finns i ett separat dokument: `https://readit0.github.io/plume-legal/conditions-generales`.

---

> ### Bör granskas av en yrkesperson
>
> Det här dokumentet har skrivits genom att appens faktiska beteende har mätts, men **det har inte skrivits av en jurist**. Fyra punkter förtjänar i första hand ett professionellt utlåtande:
>
> 1. **Överföringen av uppgifter till ett land utanför Europeiska unionen** till OpenRouter. Det är den känsligaste punkten: man måste fastställa vilken överföringsmekanism som är tillämplig, kontrollera att det finns ett personuppgiftsbiträdesavtal med den leverantören, och skriva in det här. Så länge det inte är gjort beskriver det här dokumentet överföringen utan att påstå att den är rättsligt reglerad.
> 2. **De rättsliga grunder** som valts i §7, särskilt fördelningen mellan samtycke och berättigat intresse för tillgänglighetstjänsten.
> 3. **Åldersgränsen** (16 år) och dess överensstämmelse med Google Plays frågeformulär för innehållsklassificering.
> 4. **Uppgiften om AI** enligt Europeiska unionens förordning om artificiell intelligens (öppenhetskrav för ett system med begränsad risk).

---

Det här dokumentet är en översättning av den franska versionen, som finns på adressen https://readit0.github.io/plume-legal/. Den tillhandahålls för din information. Kontakta oss på sogacmoi7@gmail.com om du upptäcker en avvikelse.
