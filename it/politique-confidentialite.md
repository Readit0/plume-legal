# Informativa sulla privacy di Plume

**Ultimo aggiornamento: 31 luglio 2026** — Versione 1.0

---

## Chi è il titolare del trattamento dei suoi dati

**SASU RedLine Music**
SIREN 938 277 100 — SIRET `938 277 100 00013`
Abbaye 208-1, 208 Résidence Lavoisier, 18100 Vierzon, France
Contatto: sogacmoi7@gmail.com

L'applicazione è pubblicata su Google Play con il nome di editore **openfunworld**.

La presente informativa descrive ciò che fa l'applicazione Plume nella sua versione attuale. È stata redatta leggendo il codice dell'applicazione, non a partire da un modello generico.

---

## In un minuto

Plume la aiuta a scrivere: riformula il suo testo direttamente nell'applicazione in cui sta digitando, e può tradurre il testo visualizzato sullo schermo.

Tre cose da ricordare:

1. **Plume non conserva nessuno dei suoi testi sui propri server.** Né i testi riformulati, né il testo letto sullo schermo. Non ne conserviamo né copia né registrazione.
2. **A seconda del motore che sceglie, il suo testo lascia o non lascia il suo telefono.** Due motori (il Kit locale e l'IA locale) lavorano interamente sul dispositivo. Il terzo (l'IA cloud) invia il testo a un servizio di intelligenza artificiale **situato al di fuori dell'Unione europea**. La scelta è sua, e l'IA cloud non si attiva mai senza il suo consenso esplicito.
3. **Plume ha bisogno di autorizzazioni potenti** (leggere il contenuto visualizzato nelle altre applicazioni, catturare lo schermo). Qui di seguito spieghiamo con precisione a cosa servono e a cosa non servono.

---

## 1. Ciò che Plume legge sul suo schermo, e quando

### 1.1 Il servizio di accessibilità

Per riscrivere il suo testo là dove lo scrive, Plume utilizza il servizio di accessibilità di Android. È un'autorizzazione che lei attiva personalmente, nelle impostazioni del telefono, dopo una schermata esplicativa che Plume le mostra **prima** di richiedergliela.

In concreto:

- **A riposo**, Plume sa soltanto quale applicazione è aperta e in quale momento lei posiziona il cursore in un campo di scrittura. È questo che fa comparire la capsula fluttuante, e unicamente nelle applicazioni che lei stessa ha configurato.
- **Il contenuto del campo viene letto solo nell'istante preciso in cui tocca la capsula**, per essere riscritto e poi sostituito sul posto.
- **I campi delle password sono esclusi.** L'applicazione rileva i campi di tipo password (compresi i codici numerici e i campi web) e rifiuta di leggerli.
- Questa autorizzazione **non consente alcuna cattura di immagine** del suo schermo.
- Plume **non tocca mai al posto suo** all'interno di un'altra applicazione: sostituisce il testo di un campo, nient'altro.

Due funzioni che lei attiva personalmente — la **Lettura Assistita in modalità Testo** e la **traduzione dei messaggi ricevuti** — leggono il testo visualizzato in modo continuo finché sono in funzione, e si fermano non appena lei le disattiva.

Se rifiuta il servizio di accessibilità, Plume resta utilizzabile: può selezionare un testo e passare dal menu «Plume» della selezione di Android, oppure condividere un testo con Plume.

### 1.2 La cattura dello schermo (Lettura Assistita)

La Lettura Assistita sovrappone una traduzione al testo visualizzato — per esempio le nuvolette di un fumetto. Ha bisogno di vedere l'immagine dello schermo.

- È **disattivata per impostazione predefinita** e funziona solo nelle applicazioni che lei ha esplicitamente autorizzato, una per una.
- **Android le chiede il proprio consenso a ogni avvio di sessione.** Non è un'autorizzazione concessa una volta per tutte: ogni sessione richiede un nuovo accordo. Plume non cerca mai di riutilizzare o di aggirare tale accordo.
- Per tutta la durata della sessione, **una notifica permanente e un indicatore di sistema restano visibili**. Plume non può catturare il suo schermo di nascosto.
- La sessione **si interrompe automaticamente al blocco dello schermo**, e immediatamente quando è lei stessa a interromperla.
- Le applicazioni che proteggono la propria visualizzazione (applicazioni bancarie, gestori di password) vengono **oscurate da Android stesso** prima che Plume riceva alcunché. È una protezione del sistema, reale ma parziale: non tutte le applicazioni sensibili la attivano. Per questo non la presentiamo come una garanzia assoluta.
- **Le immagini catturate non vengono mai salvate né inviate.** Ogni immagine è analizzata in memoria per estrarne il testo, poi abbandonata. Nessuna immagine lascia il suo telefono, mai, qualunque sia il motore scelto.

---

## 2. Ciò che resta sul suo telefono e ciò che esce

È la distinzione più importante della presente informativa, ed è lei a controllarla.

### 2.1 I motori che non fanno uscire nulla

- **Il Kit locale** (riconoscimento e traduzione di testo offline) funziona interamente sul dispositivo.
- **L'IA locale** è un modello di intelligenza artificiale scaricato una volta e poi memorizzato sul suo telefono (circa 720 MB). Viene eseguito sul suo dispositivo.

Con questi due motori, **il testo letto o riformulato non lascia il suo telefono.** Non vi è alcuna chiamata di rete legata al contenuto del suo testo.

### 2.2 Il motore IA cloud

Quando sceglie l'IA cloud, o quando il suo dispositivo non è abbastanza potente per l'IA locale, il testo interessato viene trasmesso ai nostri server e poi a un servizio di intelligenza artificiale di terzi.

**Occorre essere chiari sul percorso reale:**

- Il testo transita dalla nostra infrastruttura (Supabase), ospitata nell'**Unione europea** (regione Europa centrale, Francoforte).
- Viene poi trasmesso a **openrouter.ai**, un intermediario di instradamento **situato al di fuori dell'Unione europea**, che lo fa trattare dal modello **Mistral Small**.
- **Si tratta quindi di un trasferimento di dati al di fuori dell'Unione europea.** Non pretendiamo il contrario, e non mostriamo alcuna promessa di hosting europeo per questa fase.
- **Plume non conserva il suo testo.** Nessuna delle nostre funzioni server scrive il contenuto del suo testo: registriamo soltanto un identificativo tecnico di richiesta e l'identificativo del suo dispositivo, per conteggiare la sua quota e rilevare gli abusi.
- **Ciò che questi fornitori fanno dal canto loro, non possiamo garantirlo.** Preferiamo dirglielo piuttosto che prometterle una conservazione nulla che non siamo in grado di verificare.

**L'IA cloud non si attiva mai da sola.** Una schermata di consenso dedicata le illustra questi punti prima del primo invio, e nulla parte finché lei non ha accettato. Se l'IA locale non riesce, Plume non passa al cloud in silenzio: glielo segnala e attende la sua decisione. Può revocare questo consenso in qualsiasi momento nelle impostazioni.

Il testo inviato ha un limite massimo: 1.200 caratteri per una riformulazione, 4.000 caratteri per un'analisi dello schermo.

---

## 3. I dati che conserviamo

Non utilizziamo **alcuno strumento di analisi del pubblico, alcun tracciatore pubblicitario di terzi, alcuno strumento di segnalazione dei crash**. L'applicazione non contiene alcun SDK di misurazione.

Ecco la totalità di ciò che è memorizzato sui nostri server:

| Dato | Perché | Durata |
|---|---|---|
| **Identificativo del dispositivo** (un numero casuale generato da Plume, senza alcun legame con la sua identità né con un identificativo pubblicitario) | Collegare un dispositivo a un account, applicare le quote, bloccare gli abusi | Fino alla cancellazione del suo account |
| **Indirizzo e-mail dell'account** (se crea un account tramite e-mail o tramite Google) | Autenticarla, collegare il suo abbonamento | Fino alla cancellazione del suo account |
| **Contatori di utilizzo** (numero di riformulazioni al giorno e al mese — numeri, non testi) | Applicare le quote | Fino alla cancellazione del suo account |
| **Cronologia degli acquisti** (identificativo della transazione Google Play, date, stato dell'abbonamento) | Darle accesso a ciò che ha pagato, gestire i rinnovi, rispettare i nostri obblighi contabili | Conservata anche dopo la cancellazione dell'account, ma **separata dalla sua identità** (vedere il §6) |
| **Suggerimenti inviati volontariamente** (se ci scrive un suggerimento di persona dall'applicazione) | Migliorare il catalogo. Questi suggerimenti non vengono mai pubblicati. | Fino alla cancellazione del suo account |
| **Segnali tecnici di abuso** (superamenti ripetuti, esito negativo del controllo di integrità — senza alcun testo) | Sicurezza, lotta contro le frodi | Separati dalla sua identità al momento della cancellazione dell'account |
| **Lingua e versione dell'applicazione** | Fornire il contenuto corretto | Fino alla cancellazione del suo account |

**Ciò che non raccogliamo:** il suo nome, i suoi contatti, la sua posizione, la sua rubrica, le sue foto, il suo calendario, la cronologia delle sue applicazioni. Plume non richiede nessuna di queste autorizzazioni.

**Ciò che resta unicamente sul suo telefono:** i suoi persona personalizzati e i loro avatar, le sue impostazioni, le sue regole per applicazione, la cache di traduzione della Lettura Assistita (cancellata al termine di ogni sessione). Nulla di tutto questo viene inviato ai nostri server.

---

## 4. La dettatura vocale

Un pulsante con il microfono le consente di dettare invece di digitare. L'autorizzazione di accesso al microfono viene richiesta **nel momento preciso in cui preme tale pulsante**, mai all'avvio, e il microfono si apre soltanto in quell'istante. Plume non ascolta mai in secondo piano.

**Plume non riceve, non memorizza e non trasmette alcuna registrazione audio.** La dettatura è affidata al motore di riconoscimento vocale integrato nel suo telefono (quello di Android). Plume recupera soltanto il testo trascritto.

**Punto importante e onesto:** questo motore di sistema appartiene al suo telefono, in genere a Google. A seconda del suo dispositivo, delle sue impostazioni e dei moduli linguistici installati, **esso può trasmettere l'audio ai server del proprio editore** per trascriverlo. Tale trattamento sfugge a Plume e rientra nell'informativa sulla privacy dell'editore del suo sistema. Non possiamo quindi affermare che la sua voce resti sul dispositivo: dipende dal suo telefono, non da noi.

Se rifiuta l'autorizzazione del microfono, la digitazione da tastiera resta ovviamente disponibile.

---

## 5. Pubblicità

Il servizio è gratuito entro un certo limite di utilizzo giornaliero. Oltre tale limite, può **scegliere** di guardare un annuncio con premio per sbloccare utilizzi supplementari. Non è mai imposto: se non guarda alcun annuncio, conserva semplicemente ciò a cui ha diritto.

- Gli annunci sono forniti da **Google AdMob**.
- Compaiono **unicamente all'interno dell'applicazione Plume stessa**, mai nella capsula fluttuante e mai al di sopra di un'altra applicazione.
- **Gli abbonati non vedono alcun annuncio.**
- Nello Spazio economico europeo, nel Regno Unito e in Svizzera, le viene presentato un modulo di consenso fornito da una piattaforma certificata da Google **prima del primo annuncio**. Finché la sua scelta non è stata raccolta, non viene richiesto alcun annuncio. Se rifiuta, gli annunci restano **non personalizzati** e **non le viene tolta alcuna funzionalità**. Può tornare su questa scelta in qualsiasi momento dalle impostazioni.
- Per accreditarle il premio in modo affidabile, il suo identificativo di dispositivo Plume viene trasmesso ad AdMob. Google può inoltre raccogliere propri dati conformemente alla propria informativa sulla privacy.

*Alla data di redazione, la diffusione pubblicitaria è disattivata lato server. La presente sezione descrive il funzionamento a partire dal momento in cui sarà attivata.*

---

## 6. Abbonamenti e acquisti

Gli abbonamenti e i pacchetti sono venduti **tramite Google Play**. Non vediamo mai le sue coordinate bancarie: sono trattate da Google, che è il venditore ai fini della fatturazione.

Riceviamo da Google una prova d'acquisto che il nostro server verifica, e ne conserviamo traccia (identificativo della transazione, date, stato). Tale traccia è conservata per ragioni contabili e per impedire che uno stesso acquisto venga utilizzato due volte, ma viene **separata dalla sua identità** quando lei cancella il suo account.

---

## 7. I suoi diritti

Lei dispone dei diritti di accesso, rettifica, cancellazione, limitazione, opposizione e portabilità previsti dal GDPR.

**Il modo più semplice e più rapido: la cancellazione è integrata nell'applicazione.**
Impostazioni → Privacy → Elimina i miei dati. Viene **eseguita immediatamente**, non messa in coda d'attesa. Il dettaglio di ciò che viene cancellato e di ciò che viene conservato figura nella nostra pagina dedicata: `https://readit0.github.io/plume-legal/suppression-compte`.

Può anche cancellare il suo account **senza installare l'applicazione**, scrivendo a sogacmoi7@gmail.com.

Per qualsiasi altra richiesta, scriva a **sogacmoi7@gmail.com**. Rispondiamo entro un mese.

**Basi giuridiche:** l'esecuzione del contratto (fornire il servizio che lei richiede, gestire il suo abbonamento), il suo consenso (servizio di accessibilità, cattura dello schermo, invio verso l'IA cloud, pubblicità personalizzata), il nostro legittimo interesse (sicurezza, lotta contro le frodi) e i nostri obblighi legali (contabilità).

Può proporre reclamo presso la **CNIL** (www.cnil.fr), autorità di controllo dell'editore, oppure, **se risiede nell'Unione europea**, presso l'autorità di controllo del suo Paese di residenza — l'articolo 77 del GDPR le lascia la scelta.

---

## 8. I minori

Plume è uno strumento di ausilio alla scrittura, destinato a un pubblico **dai 16 anni in su**. Non raccogliamo consapevolmente dati di minori di 16 anni e l'applicazione non è né concepita né promossa per loro. Se lei esercita la responsabilità genitoriale e ritiene che suo figlio ci abbia trasmesso dei dati, scriva a sogacmoi7@gmail.com: cancelleremo l'account.

Poiché l'applicazione consente di riformulare un testo libero e mostra pubblicità, non è ammissibile ai programmi destinati alle famiglie di Google Play.

---

## 9. Responsabili del trattamento e destinatari

| Fornitore | Ruolo | Dove |
|---|---|---|
| **Supabase** | Hosting della banca dati, autenticazione, funzioni server | Unione europea (Francoforte) |
| **OpenRouter** | Instradamento delle richieste verso il modello di IA | **Al di fuori dell'Unione europea** |
| **Mistral AI** (tramite OpenRouter) | Modello che tratta il testo (Mistral Small) | Trattamento tramite l'intermediario di cui sopra |
| **Google Play / Google Billing** | Pagamento, abbonamenti | Google Ireland / Stati Uniti |
| **Google AdMob** | Pubblicità con premio | Google Ireland / Stati Uniti |
| **Google (servizi di sistema del telefono)** | Riconoscimento vocale, moduli di traduzione offline | A seconda del suo dispositivo |

**Non vendiamo alcun dato e non ne cediamo alcuno a intermediari di dati.**

**Trasferimenti al di fuori dell'Unione europea:** il ricorso a OpenRouter, a Google Play e ad AdMob comporta un trasferimento di dati al di fuori dell'Unione europea. Il quadro giuridico di tali trasferimenti (clausole contrattuali tipo, decisione di adeguatezza) **deve essere verificato e documentato da un professionista prima della pubblicazione** — vedere la nota in calce al documento.

---

## 10. Sicurezza

Gli scambi tra l'applicazione e i nostri server sono cifrati (HTTPS/TLS). L'accesso ai dati nella banca dati è limitato da regole lato server: le funzioni sensibili non sono accessibili dall'applicazione. Nessun sistema è perfettamente sicuro, ma nessun testo che lei riformula è memorizzato presso di noi, il che limita meccanicamente ciò che un'intrusione potrebbe rivelare.

---

## 11. Modifiche

Ogni modifica della presente informativa sarà pubblicata all'indirizzo `https://readit0.github.io/plume-legal` con una nuova data. In caso di cambiamento importante nella circolazione dei suoi dati, la informeremo nell'applicazione.

---

## Condizioni generali

Le condizioni di utilizzo del servizio (quote, abbonamenti, disdetta) figurano in un documento distinto: `https://readit0.github.io/plume-legal/conditions-generales`.

---

> ### Da far rileggere a un professionista
>
> Il presente documento è stato redatto misurando il comportamento reale dell'applicazione, ma **non è stato redatto da un giurista**. Quattro punti meritano in via prioritaria un parere professionale:
>
> 1. **Il trasferimento di dati al di fuori dell'Unione europea** verso OpenRouter. È il punto più delicato: occorre determinare il meccanismo di trasferimento applicabile, verificare che esista un accordo sul trattamento dei dati con questo fornitore, e scriverlo qui. Finché ciò non sarà fatto, il presente documento descrive il trasferimento senza affermare che sia giuridicamente inquadrato.
> 2. **Le basi giuridiche** indicate al §7, in particolare la ripartizione tra consenso e legittimo interesse per il servizio di accessibilità.
> 3. **L'età minima** (16 anni) e la sua coerenza con il questionario di classificazione dei contenuti di Google Play.
> 4. **La menzione relativa all'IA** ai sensi del regolamento europeo sull'intelligenza artificiale (obbligo di trasparenza per un sistema a rischio limitato).

---

Il presente documento è una traduzione della versione francese, disponibile all'indirizzo https://readit0.github.io/plume-legal/. È fornita a titolo informativo. In caso di divergenza, ci contatti all'indirizzo sogacmoi7@gmail.com.
