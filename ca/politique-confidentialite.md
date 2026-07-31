# Política de privadesa de Plume

**Última actualització: 31 de juliol de 2026** — Versió 1.0


---

## Qui és el responsable de les seves dades

**SASU RedLine Music**
SIREN 938 277 100 — SIRET `938 277 100 00013`
Abbaye 208-1, 208 Résidence Lavoisier, 18100 Vierzon, France
Contacte: sogacmoi7@gmail.com

L'aplicació es publica a Google Play amb el nom d'editor **openfunworld**.

Aquesta política descriu el que fa l'aplicació Plume en la seva versió actual. S'ha redactat llegint el codi de l'aplicació, no a partir d'un model genèric.

---

## En un minut

Plume l'ajuda a escriure: reformula el seu text directament a l'aplicació on està escrivint, i pot traduir el text que es mostra a la pantalla.

Tres coses que cal recordar:

1. **Plume no conserva cap dels seus textos als seus servidors.** Ni els textos reformulats, ni el text llegit a la pantalla. No en guardem ni còpia ni registre.
2. **Segons el motor que triï, el seu text surt o no surt del seu telèfon.** Dos motors (el Kit local i la IA local) treballen íntegrament al dispositiu. El tercer (la IA Cloud) envia el text a un servei d'intel·ligència artificial **situat fora de la Unió Europea**. Vostè tria, i la IA Cloud no s'activa mai sense el seu acord explícit.
3. **Plume necessita permisos potents** (llegir el contingut que es mostra a les altres aplicacions, capturar la pantalla). Més avall expliquem amb precisió per a què serveixen i per a què no serveixen.

---

## 1. Què llegeix Plume a la seva pantalla, i quan

### 1.1 El servei d'accessibilitat

Per reescriure el seu text allà on l'escriu, Plume utilitza el servei d'accessibilitat d'Android. És un permís que vostè mateix activa, als paràmetres del telèfon, després d'una pantalla explicativa que Plume li mostra **abans** de sol·licitar-lo.

Concretament:

- **En repòs**, Plume només sap quina aplicació està oberta i en quin moment situa el cursor en un camp de text. És això el que fa aparèixer la càpsula flotant, i únicament a les aplicacions que vostè mateix ha configurat.
- **El contingut del camp només es llegeix en l'instant precís en què toca la càpsula**, per ser reescrit i després substituït al mateix lloc.
- **Els camps de contrasenya queden exclosos.** L'aplicació detecta els camps de tipus contrasenya (inclosos els codis numèrics i els camps web) i es nega a llegir-los.
- Aquest permís **no permet cap captura d'imatge** de la seva pantalla.
- Plume **no prem mai res en lloc seu** dins d'una altra aplicació: substitueix el text d'un camp, res més.

Dues funcions que vostè mateix activa —la **Lectura Assistida en mode Text** i la **traducció dels missatges rebuts**— llegeixen el text que es mostra de manera contínua mentre estan en marxa, i s'aturen tan bon punt les desactiva.

Si rebutja el servei d'accessibilitat, Plume continua sent utilitzable: pot seleccionar un text i passar pel menú «Plume» de la selecció d'Android, o compartir un text amb Plume.

### 1.2 La captura de pantalla (Lectura Assistida)

La Lectura Assistida superposa una traducció damunt del text que es mostra, per exemple les bafarades d'un còmic. Necessita veure la imatge de la pantalla.

- Està **desactivada per defecte** i només funciona a les aplicacions que vostè ha autoritzat explícitament, una per una.
- **Android li demana el seu propi consentiment cada vegada que s'inicia una sessió.** No és un permís concedit d'una vegada per sempre: cada sessió exigeix un acord nou. Plume no intenta mai reutilitzar ni eludir aquest acord.
- Durant tota la sessió, **una notificació permanent i un indicador del sistema es mantenen visibles**. Plume no pot capturar la seva pantalla d'amagat.
- La sessió **s'atura automàticament quan la pantalla es bloqueja**, i immediatament quan vostè mateix l'atura.
- Les aplicacions que protegeixen la seva visualització (aplicacions bancàries, gestors de contrasenyes) queden **ocultades pel mateix Android** abans que Plume rebi res. És una protecció del sistema, real però parcial: no totes les aplicacions sensibles l'activen. Per això no la presentem com una garantia absoluta.
- **Les imatges capturades no es desen ni s'envien mai.** Cada imatge s'analitza en memòria per extreure'n el text i tot seguit es descarta. Cap imatge no surt del seu telèfon, mai, sigui quin sigui el motor triat.

---

## 2. El que es queda al seu telèfon i el que en surt

És la distinció més important d'aquesta política, i és vostè qui la controla.

### 2.1 Els motors que no fan sortir res

- **El Kit local** (reconeixement i traducció de text fora de línia) funciona íntegrament al dispositiu.
- **La IA local** és un model d'intel·ligència artificial que es baixa una sola vegada i després es guarda al seu telèfon (uns 720 MB). S'executa al seu dispositiu.

Amb aquests dos motors, **el text llegit o reformulat no surt del seu telèfon.** No hi ha cap petició de xarxa lligada al contingut del seu text.

### 2.2 El motor IA Cloud

Quan tria la IA Cloud, o quan el seu dispositiu no és prou potent per a la IA local, el text corresponent es transmet als nostres servidors i, després, a un servei d'intel·ligència artificial de tercers.

**Cal ser clars sobre el trajecte real:**

- El text passa per la nostra infraestructura (Supabase), allotjada a la **Unió Europea** (regió d'Europa central, Frankfurt).
- Tot seguit es transmet a **openrouter.ai**, un intermediari d'encaminament **situat fora de la Unió Europea**, que el fa processar pel model **Mistral Small**.
- **Es tracta, doncs, d'una transferència de dades fora de la Unió Europea.** No pretenem el contrari, i no mostrem cap promesa d'allotjament europeu per a aquesta etapa.
- **Plume no conserva el seu text.** Cap de les nostres funcions de servidor no escriu el contingut del seu text: només registrem un identificador tècnic de sol·licitud i l'identificador del seu dispositiu, per comptar la seva quota i detectar els abusos.
- **El que aquests proveïdors facin pel seu compte, no ho podem garantir.** Preferim dir-ho clarament abans que prometre-li una retenció nul·la que no estem en condicions de verificar.

**La IA Cloud no s'activa mai tota sola.** Una pantalla de consentiment dedicada li explica aquests punts abans del primer enviament, i no s'envia res mentre no ho hagi acceptat. Si la IA local falla, Plume no passa al núvol en silenci: li ho indica i espera la seva decisió. Pot revocar aquest acord en qualsevol moment als paràmetres.

El text enviat té un límit: 1.200 caràcters per a una reformulació, 4.000 caràcters per a una anàlisi de pantalla.

---

## 3. Les dades que conservem

No utilitzem **cap eina d'analítica d'audiència, cap rastrejador publicitari de tercers, cap eina d'informe d'errors**. L'aplicació no conté cap SDK de mesurament.

Això és tot el que s'emmagatzema als nostres servidors:

| Dada | Per què | Durada |
|---|---|---|
| **Identificador de dispositiu** (un número aleatori generat per Plume, sense relació amb la seva identitat ni amb cap identificador publicitari) | Vincular un dispositiu a un compte, aplicar les quotes, bloquejar els abusos | Fins a la supressió del seu compte |
| **Adreça electrònica del compte** (si crea un compte per correu electrònic o mitjançant Google) | Autenticar-lo, vincular la seva subscripció | Fins a la supressió del seu compte |
| **Comptadors d'ús** (nombre de reformulacions per dia i per mes: xifres, no textos) | Aplicar les quotes | Fins a la supressió del seu compte |
| **Historial de compres** (identificador de transacció de Google Play, dates, estat de la subscripció) | Donar-li accés a allò que ha pagat, gestionar les renovacions, complir les nostres obligacions comptables | Conservat fins i tot després de la supressió del compte, però **desvinculat de la seva identitat** (vegeu §6) |
| **Suggeriments enviats voluntàriament** (si ens escriu un suggeriment de persona des de l'aplicació) | Millorar el catàleg. Aquests suggeriments no es publiquen mai. | Fins a la supressió del seu compte |
| **Senyals tècnics d'abús** (excessos repetits, fallada del control d'integritat, sense cap text) | Seguretat, lluita contra el frau | Desvinculats de la seva identitat en suprimir el compte |
| **Idioma i versió de l'aplicació** | Servir el contingut correcte | Fins a la supressió del seu compte |

**El que no recollim:** el seu nom, els seus contactes, la seva ubicació, la seva llibreta d'adreces, les seves fotos, la seva agenda, l'historial de les seves aplicacions. Plume no demana cap d'aquests permisos.

**El que es queda únicament al seu telèfon:** les seves personas personalitzades i els seus avatars, els seus paràmetres, les seves regles per aplicació, la memòria cau de traducció de la Lectura Assistida (esborrada al final de cada sessió). Res de tot això no s'envia als nostres servidors.

---

## 4. El dictat per veu

Un botó de micròfon li permet dictar en lloc d'escriure. El permís d'accés al micròfon es demana **en el moment precís en què prem aquest botó**, mai en iniciar l'aplicació, i el micròfon només s'obre en aquell instant. Plume no escolta mai en segon pla.

**Plume no rep, no emmagatzema ni transmet cap enregistrament d'àudio.** El dictat es confia al motor de reconeixement de veu integrat al seu telèfon (el d'Android). Plume només recupera el text transcrit.

**Un punt important i honest:** aquest motor del sistema pertany al seu telèfon, generalment a Google. Segons el seu dispositiu, els seus paràmetres i els mòduls d'idioma instal·lats, **pot transmetre l'àudio als servidors del seu editor** per transcriure'l. Aquest tractament escapa a Plume i depèn de la política de privadesa de l'editor del seu sistema. Per tant, no podem afirmar que la seva veu es quedi al dispositiu: això depèn del seu telèfon, no de nosaltres.

Si rebutja el permís del micròfon, l'escriptura amb el teclat continua evidentment disponible.

---

## 5. Publicitat

El servei és gratuït dins d'un cert límit d'ús diari. Més enllà d'aquest límit, pot **triar** de mirar un anunci amb recompensa per desbloquejar usos addicionals. No s'imposa mai: si no mira cap anunci, simplement conserva allò a què té dret.

- Els anuncis els proporciona **Google AdMob**.
- Apareixen **únicament dins de la mateixa aplicació Plume**, mai a la càpsula flotant i mai per damunt d'una altra aplicació.
- **Els subscriptors no veuen cap anunci.**
- A l'Espai Econòmic Europeu, al Regne Unit i a Suïssa, se li presenta un formulari de consentiment proporcionat per una plataforma certificada per Google **abans del primer anunci**. Mentre no s'hagi recollit la seva elecció, no se sol·licita cap anunci. Si el rebutja, els anuncis segueixen sent **no personalitzats** i **no se li retira cap funcionalitat**. Pot canviar aquesta elecció en qualsevol moment des dels paràmetres.
- Per acreditar-li la recompensa de manera fiable, l'identificador del seu dispositiu Plume es transmet a AdMob. Google pot, a més, recollir les seves pròpies dades d'acord amb la seva política de privadesa.

*En la data de redacció, la difusió publicitària està desactivada al servidor. Aquesta secció descriu el funcionament a partir del moment en què s'activi.*

---

## 6. Subscripcions i compres

Les subscripcions i els paquets es venen **a través de Google Play**. No veiem mai les seves dades bancàries: les tracta Google, que és el venedor als efectes de la facturació.

Rebem de Google un justificant de compra que el nostre servidor verifica, i en conservem el rastre (identificador de transacció, dates, estat). Aquest rastre es conserva per raons comptables i per impedir que una mateixa compra serveixi dues vegades, però queda **desvinculat de la seva identitat** quan suprimeix el seu compte.

---

## 7. Els seus drets

Disposa dels drets d'accés, de rectificació, de supressió, de limitació, d'oposició i de portabilitat que preveu el RGPD.

**El més senzill i el més ràpid: la supressió està integrada a l'aplicació.**
Configuració → Privadesa → Suprimeix les meves dades. S'executa **immediatament**, no es posa en cap cua d'espera. El detall del que s'esborra i del que es conserva figura a la nostra pàgina dedicada: `https://readit0.github.io/plume-legal/suppression-compte`.

També pot suprimir el seu compte **sense instal·lar l'aplicació**, escrivint a sogacmoi7@gmail.com.

Per a qualsevol altra sol·licitud, escrigui a **sogacmoi7@gmail.com**. Responem en el termini d'un mes.

**Bases jurídiques:** l'execució del contracte (prestar el servei que ens demana, gestionar la seva subscripció), el seu consentiment (servei d'accessibilitat, captura de pantalla, enviament a la IA Cloud, publicitat personalitzada), el nostre interès legítim (seguretat, lluita contra el frau) i les nostres obligacions legals (comptabilitat).

Pot presentar una reclamació davant la **CNIL** (www.cnil.fr), autoritat de control de l'editor, o, **si resideix a la Unió Europea**, davant l'autoritat de control del seu país de residència: l'article 77 del RGPD li deixa l'elecció.

---

## 8. Els menors

Plume és una eina d'ajuda a la redacció, destinada a un públic **de 16 anys o més**. No recollim conscientment dades d'infants de menys de 16 anys i l'aplicació no està dissenyada ni promoguda per a ells. Si vostè és titular de la potestat parental i creu que el seu fill o filla ens ha transmès dades, escrigui a sogacmoi7@gmail.com: suprimirem el compte.

Com que l'aplicació permet reformular un text lliure i mostra publicitat, no és elegible per als programes de Google Play destinats a les famílies.

---

## 9. Encarregats del tractament i destinataris

| Proveïdor | Funció | On |
|---|---|---|
| **Supabase** | Allotjament de la base de dades, autenticació, funcions de servidor | Unió Europea (Frankfurt) |
| **OpenRouter** | Encaminament de les sol·licituds cap al model d'IA | **Fora de la Unió Europea** |
| **Mistral AI** (mitjançant OpenRouter) | Model que processa el text (Mistral Small) | Tractament a través de l'intermediari anterior |
| **Google Play / Google Billing** | Pagament, subscripcions | Google Ireland / Estats Units |
| **Google AdMob** | Publicitat amb recompensa | Google Ireland / Estats Units |
| **Google (serveis de sistema del telèfon)** | Reconeixement de veu, mòduls de traducció fora de línia | Segons el seu dispositiu |

**No venem cap dada ni en cedim cap a corredors de dades.**

**Transferències fora de la Unió Europea:** el recurs a OpenRouter, a Google Play i a AdMob implica una transferència de dades fora de la Unió Europea. L'enquadrament jurídic d'aquestes transferències (clàusules contractuals tipus, decisió d'adequació) **ha de ser verificat i documentat per un professional abans de la publicació**: vegeu la nota al final del document.

---

## 10. Seguretat

Els intercanvis entre l'aplicació i els nostres servidors estan xifrats (HTTPS/TLS). L'accés a les dades de la base està restringit per regles de servidor: les funcions sensibles no són accessibles des de l'aplicació. Cap sistema no és perfectament segur, però cap text que vostè reformula no s'emmagatzema a casa nostra, cosa que limita mecànicament el que una intrusió podria revelar.

---

## 11. Modificacions

Qualsevol modificació d'aquesta política es publicarà a l'adreça `https://readit0.github.io/plume-legal` amb una data nova. En cas de canvi important en la circulació de les seves dades, l'informarem dins de l'aplicació.

---

## Condicions generals

Les condicions d'ús del servei (quotes, subscripcions, cancel·lació) figuren en un document separat: `https://readit0.github.io/plume-legal/conditions-generales`.

---

> ### Pendent de revisió per un professional
>
> Aquest document s'ha redactat mesurant el comportament real de l'aplicació, però **no l'ha redactat cap jurista**. Quatre punts mereixen prioritàriament un dictamen professional:
>
> 1. **La transferència de dades fora de la Unió Europea** cap a OpenRouter. És el punt més sensible: cal determinar el mecanisme de transferència aplicable, verificar que existeix un acord de tractament amb aquest proveïdor i escriure-ho aquí. Mentre això no s'hagi fet, aquest document descriu la transferència sense afirmar que estigui degudament emparada.
> 2. **Les bases jurídiques** adoptades al §7, en particular el repartiment entre consentiment i interès legítim per al servei d'accessibilitat.
> 3. **L'edat mínima** (16 anys) i la seva coherència amb el qüestionari de classificació de contingut de Google Play.
> 4. **La menció relativa a la IA** en virtut del reglament europeu sobre la intel·ligència artificial (obligació de transparència per a un sistema de risc limitat).

---

Aquest document és una traducció de la versió francesa, disponible a l'adreça https://readit0.github.io/plume-legal/. Es facilita a títol informatiu. En cas de divergència, contacti amb nosaltres a sogacmoi7@gmail.com.
