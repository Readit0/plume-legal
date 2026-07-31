# Datenschutzerklärung von Plume

**Letzte Aktualisierung: 31. Juli 2026** — Version 1.0

---

## Wer für Ihre Daten verantwortlich ist

**SASU RedLine Music**
SIREN 938 277 100 — SIRET `938 277 100 00013`
Abbaye 208-1, 208 Résidence Lavoisier, 18100 Vierzon, France
Kontakt: sogacmoi7@gmail.com

Die App wird auf Google Play unter dem Entwicklernamen **openfunworld** veröffentlicht.

Diese Datenschutzerklärung beschreibt, was die App Plume in ihrer aktuellen Version tut. Sie wurde beim Lesen des Programmcodes der App verfasst und nicht anhand einer allgemeinen Vorlage.

---

## In einer Minute

Plume hilft Ihnen beim Schreiben: Die App schreibt Ihren Text direkt in der Anwendung um, in der Sie gerade tippen, und sie kann auf dem Bildschirm angezeigten Text übersetzen.

Drei Dinge, die Sie sich merken sollten:

1. **Plume speichert keinen Ihrer Texte auf seinen Servern.** Weder Ihre umgeschriebenen Texte noch den vom Bildschirm gelesenen Text. Wir bewahren davon weder eine Kopie noch ein Protokoll auf.
2. **Je nachdem, welche Engine Sie wählen, verlässt Ihr Text Ihr Handy oder nicht.** Zwei Engines (das Lokale Kit und die Lokale KI) arbeiten vollständig auf dem Gerät. Die dritte (die Cloud-KI) sendet den Text an einen Dienst für künstliche Intelligenz **außerhalb der Europäischen Union**. Sie entscheiden, und die Cloud-KI wird niemals ohne Ihre ausdrückliche Zustimmung aktiviert.
3. **Plume benötigt weitreichende Berechtigungen** (Lesen der in anderen Apps angezeigten Inhalte, Aufnahme des Bildschirms). Nachfolgend erklären wir genau, wozu sie dienen und wozu nicht.

---

## 1. Was Plume auf Ihrem Bildschirm liest und wann

### 1.1 Der Bedienungshilfen-Dienst

Um Ihren Text dort umzuschreiben, wo Sie ihn schreiben, nutzt Plume den Bedienungshilfen-Dienst von Android. Das ist eine Berechtigung, die Sie selbst in den Einstellungen Ihres Handys aktivieren, nachdem Plume Ihnen **vorher** einen Erklärungsbildschirm gezeigt hat.

Konkret:

- **Im Ruhezustand** weiß Plume nur, welche App geöffnet ist und wann Sie den Cursor in ein Eingabefeld setzen. Das lässt die schwebende Kapsel erscheinen — und zwar nur in den Apps, die Sie selbst konfiguriert haben.
- **Der Inhalt des Feldes wird erst in dem Moment gelesen, in dem Sie die Kapsel berühren**, um umgeschrieben und anschließend an Ort und Stelle ersetzt zu werden.
- **Passwortfelder sind ausgeschlossen.** Die App erkennt Felder vom Typ Passwort (einschließlich Zahlencodes und Webfeldern) und weigert sich, sie zu lesen.
- Diese Berechtigung **erlaubt keinerlei Bildaufnahme** Ihres Bildschirms.
- Plume **tippt niemals an Ihrer Stelle** in einer anderen App: Es ersetzt den Text eines Feldes, nichts weiter.

Zwei Funktionen, die Sie selbst aktivieren — das **Assistierte Lesen im Textmodus** und die **Übersetzung empfangener Nachrichten** —, lesen den angezeigten Text fortlaufend, solange sie laufen, und hören auf, sobald Sie sie abschalten.

Wenn Sie den Bedienungshilfen-Dienst ablehnen, bleibt Plume nutzbar: Sie können einen Text markieren und den Eintrag „Plume“ im Android-Auswahlmenü verwenden oder einen Text an Plume teilen.

### 1.2 Die Bildschirmaufnahme (Assistiertes Lesen)

Das Assistierte Lesen legt eine Übersetzung über den angezeigten Text — zum Beispiel über die Sprechblasen eines Comics. Dafür muss es das Bild des Bildschirms sehen.

- Es ist **standardmäßig deaktiviert** und funktioniert nur in den Apps, die Sie einzeln ausdrücklich freigegeben haben.
- **Android fragt bei jedem Sitzungsstart seine eigene Zustimmung ab.** Das ist keine ein für alle Mal erteilte Berechtigung: Jede Sitzung erfordert eine neue Zustimmung. Plume versucht niemals, diese Zustimmung wiederzuverwenden oder zu umgehen.
- Während der gesamten Sitzung **bleiben eine dauerhafte Benachrichtigung und eine Systemanzeige sichtbar**. Plume kann Ihren Bildschirm nicht unbemerkt aufnehmen.
- Die Sitzung **endet automatisch, wenn der Bildschirm gesperrt wird**, und sofort, wenn Sie sie selbst beenden.
- Apps, die ihre Anzeige schützen (Banking-Apps, Passwortmanager), werden **von Android selbst geschwärzt**, bevor Plume überhaupt etwas erhält. Das ist ein Schutz des Systems, real, aber unvollständig: Nicht alle sensiblen Apps aktivieren ihn. Wir stellen ihn deshalb nicht als absolute Garantie dar.
- **Aufgenommene Bilder werden niemals gespeichert oder gesendet.** Jedes Bild wird im Arbeitsspeicher ausgewertet, um den Text daraus zu gewinnen, und dann verworfen. Kein Bild verlässt jemals Ihr Handy, unabhängig von der gewählten Engine.

---

## 2. Was auf Ihrem Handy bleibt und was es verlässt

Das ist die wichtigste Unterscheidung dieser Datenschutzerklärung, und Sie sind es, der sie steuert.

### 2.1 Die Engines, die nichts nach außen geben

- **Das Lokale Kit** (Texterkennung und Übersetzung offline) arbeitet vollständig auf dem Gerät.
- **Die Lokale KI** ist ein Modell künstlicher Intelligenz, das einmal heruntergeladen und dann auf Ihrem Handy gespeichert wird (rund 720 MB). Es läuft auf Ihrem Gerät.

Mit diesen beiden Engines **verlässt der gelesene oder umgeschriebene Text Ihr Handy nicht.** Es gibt keinen Netzwerkaufruf, der mit dem Inhalt Ihres Textes zusammenhängt.

### 2.2 Die Engine Cloud-KI

Wenn Sie die Cloud-KI wählen oder wenn Ihr Gerät für die Lokale KI nicht leistungsfähig genug ist, wird der betreffende Text an unsere Server und anschließend an einen Dienst für künstliche Intelligenz eines Dritten übermittelt.

**Der tatsächliche Weg muss klar benannt werden:**

- Der Text läuft über unsere Infrastruktur (Supabase), die in der **Europäischen Union** gehostet wird (Region Mitteleuropa, Frankfurt).
- Er wird danach an **openrouter.ai** übermittelt, einen Routing-Vermittler **außerhalb der Europäischen Union**, der ihn durch das Modell **Mistral Small** verarbeiten lässt.
- **Es handelt sich somit um eine Datenübermittlung außerhalb der Europäischen Union.** Wir behaupten nicht das Gegenteil, und wir stellen für diesen Schritt kein europäisches Hosting in Aussicht.
- **Plume speichert Ihren Text nicht.** Keine unserer Serverfunktionen schreibt den Inhalt Ihres Textes: Wir zeichnen nur eine technische Anfragekennung und die Kennung Ihres Geräts auf, um Ihr Kontingent zu zählen und Missbrauch zu erkennen.
- **Was diese Dienstleister ihrerseits tun, können wir nicht garantieren.** Wir sagen Ihnen das lieber, als Ihnen eine Nichtspeicherung zu versprechen, die wir nicht überprüfen können.

**Die Cloud-KI aktiviert sich niemals von selbst.** Ein eigener Einwilligungsbildschirm erklärt Ihnen diese Punkte vor der ersten Übermittlung, und es wird nichts gesendet, solange Sie nicht zugestimmt haben. Wenn die Lokale KI scheitert, wechselt Plume nicht stillschweigend in die Cloud: Die App weist Sie darauf hin und wartet Ihre Entscheidung ab. Sie können diese Zustimmung jederzeit in den Einstellungen widerrufen.

Der gesendete Text ist begrenzt: 1.200 Zeichen für eine Umschreibung, 4.000 Zeichen für eine Bildschirmanalyse.

---

## 3. Die Daten, die wir speichern

Wir verwenden **kein Tool zur Reichweitenmessung, keinen Werbetracker Dritter und kein Tool für Absturzberichte**. Die App enthält kein Mess-SDK.

Hier ist alles, was auf unseren Servern gespeichert wird:

| Daten | Wozu | Speicherdauer |
|---|---|---|
| **Gerätekennung** (eine von Plume erzeugte Zufallszahl, ohne Bezug zu Ihrer Identität und ohne Bezug zu einer Werbe-ID) | Ein Gerät einem Konto zuordnen, Kontingente anwenden, Missbrauch blockieren | Bis zur Löschung Ihres Kontos |
| **E-Mail-Adresse des Kontos** (wenn Sie ein Konto per E-Mail oder über Google erstellen) | Sie authentifizieren, Ihr Abonnement zuordnen | Bis zur Löschung Ihres Kontos |
| **Nutzungszähler** (Anzahl der Umschreibungen pro Tag und pro Monat — Zahlen, keine Texte) | Kontingente anwenden | Bis zur Löschung Ihres Kontos |
| **Kaufhistorie** (Transaktionskennung von Google Play, Daten, Status des Abonnements) | Ihnen Zugang zu dem geben, was Sie bezahlt haben, Verlängerungen verwalten, unsere buchhalterischen Pflichten erfüllen | Wird auch nach der Löschung des Kontos aufbewahrt, jedoch **von Ihrer Identität getrennt** (siehe Abschnitt 6) |
| **Freiwillig gesendete Vorschläge** (wenn Sie uns aus der App einen Persona-Vorschlag schicken) | Den Katalog verbessern. Diese Vorschläge werden niemals veröffentlicht. | Bis zur Löschung Ihres Kontos |
| **Technische Missbrauchssignale** (wiederholte Überschreitungen, fehlgeschlagene Integritätsprüfung — ohne jeglichen Text) | Sicherheit, Betrugsbekämpfung | Werden bei der Löschung des Kontos von Ihrer Identität getrennt |
| **Sprache und Version der App** | Die richtigen Inhalte ausliefern | Bis zur Löschung Ihres Kontos |

**Was wir nicht erheben:** Ihren Namen, Ihre Kontakte, Ihren Standort, Ihr Adressbuch, Ihre Fotos, Ihren Kalender, den Verlauf Ihrer Apps. Plume fordert keine dieser Berechtigungen an.

**Was ausschließlich auf Ihrem Handy bleibt:** Ihre eigenen Personas und deren Avatare, Ihre Einstellungen, Ihre Regeln pro App, der Übersetzungs-Cache des Assistierten Lesens (am Ende jeder Sitzung gelöscht). Nichts davon wird an unsere Server gesendet.

---

## 4. Das Sprachdiktat

Über eine Mikrofontaste können Sie diktieren, statt zu tippen. Die Berechtigung für den Zugriff auf das Mikrofon wird **genau in dem Moment abgefragt, in dem Sie diese Taste drücken**, niemals beim Start, und das Mikrofon wird nur in diesem Augenblick geöffnet. Plume hört niemals im Hintergrund mit.

**Plume empfängt, speichert und übermittelt keinerlei Audioaufnahme.** Das Diktat wird der in Ihrem Handy eingebauten Spracherkennung (der von Android) überlassen. Plume erhält nur den transkribierten Text.

**Ein wichtiger und ehrlicher Punkt:** Diese Systemkomponente gehört zu Ihrem Handy, in der Regel zu Google. Je nach Gerät, dessen Einstellungen und den installierten Sprachmodulen **kann sie das Audio zur Transkription an die Server ihres Anbieters übermitteln.** Diese Verarbeitung entzieht sich Plume und richtet sich nach der Datenschutzerklärung des Anbieters Ihres Betriebssystems. Wir können daher nicht behaupten, dass Ihre Stimme auf dem Gerät bleibt — das hängt von Ihrem Handy ab, nicht von uns.

Wenn Sie die Mikrofonberechtigung ablehnen, bleibt selbstverständlich die Eingabe über die Tastatur verfügbar.

---

## 5. Werbung

Der Dienst ist innerhalb einer bestimmten täglichen Nutzungsgrenze kostenlos. Darüber hinaus können Sie **wählen**, ob Sie eine Werbung mit Belohnung ansehen möchten, um zusätzliche Nutzungen freizuschalten. Das wird niemals verlangt: Wenn Sie keine Werbung ansehen, behalten Sie einfach das, worauf Sie Anspruch haben.

- Die Werbung wird von **Google AdMob** bereitgestellt.
- Sie erscheint **ausschließlich in der App Plume selbst**, niemals in der schwebenden Kapsel und niemals über einer anderen App.
- **Abonnenten sehen keine Werbung.**
- Im Europäischen Wirtschaftsraum, im Vereinigten Königreich und in der Schweiz wird Ihnen **vor der ersten Werbung** ein Einwilligungsformular angezeigt, das von einer von Google zertifizierten Plattform bereitgestellt wird. Solange Ihre Entscheidung nicht eingeholt wurde, wird keine Werbung angefordert. Wenn Sie ablehnen, bleibt die Werbung **nicht personalisiert** und **es wird Ihnen keine Funktion entzogen**. Sie können diese Entscheidung jederzeit in den Einstellungen ändern.
- Um Ihre Belohnung zuverlässig gutzuschreiben, wird Ihre Plume-Gerätekennung an AdMob übermittelt. Google kann darüber hinaus eigene Daten gemäß seiner Datenschutzerklärung erheben.

*Zum Zeitpunkt der Abfassung ist die Werbeauslieferung serverseitig deaktiviert. Dieser Abschnitt beschreibt die Funktionsweise, sobald sie aktiviert ist.*

---

## 6. Abonnements und Käufe

Abonnements und Pakete werden **über Google Play** verkauft. Wir sehen Ihre Bankdaten niemals: Sie werden von Google verarbeitet, das für die Abrechnung der Verkäufer ist.

Wir erhalten von Google einen Kaufbeleg, den unser Server prüft, und wir bewahren dessen Spur auf (Transaktionskennung, Daten, Status). Diese Spur wird aus buchhalterischen Gründen aufbewahrt und um zu verhindern, dass derselbe Kauf zweimal verwendet wird — sie wird jedoch **von Ihrer Identität getrennt**, wenn Sie Ihr Konto löschen.

---

## 7. Ihre Rechte

Ihnen stehen die in der DSGVO vorgesehenen Rechte auf Auskunft, Berichtigung, Löschung, Einschränkung der Verarbeitung, Widerspruch und Datenübertragbarkeit zu.

**Am einfachsten und schnellsten: Die Löschung ist in die App eingebaut.**
Einstellungen → Datenschutz → Meine Daten löschen. Sie wird **sofort ausgeführt** und nicht in eine Warteschlange gestellt. Was genau gelöscht und was aufbewahrt wird, steht auf unserer eigenen Seite: `https://readit0.github.io/plume-legal/suppression-compte`.

Sie können Ihr Konto auch **ohne Installation der App** löschen lassen, indem Sie an sogacmoi7@gmail.com schreiben.

Für jede andere Anfrage schreiben Sie an **sogacmoi7@gmail.com**. Wir antworten innerhalb eines Monats.

**Rechtsgrundlagen:** die Erfüllung des Vertrags (Bereitstellung des von Ihnen gewünschten Dienstes, Verwaltung Ihres Abonnements), Ihre Einwilligung (Bedienungshilfen-Dienst, Bildschirmaufnahme, Übermittlung an die Cloud-KI, personalisierte Werbung), unser berechtigtes Interesse (Sicherheit, Betrugsbekämpfung) und unsere rechtlichen Verpflichtungen (Buchhaltung).

Sie können eine Beschwerde bei der **CNIL** (www.cnil.fr), der Aufsichtsbehörde des Herausgebers, einreichen oder, **wenn Sie in der Europäischen Union wohnen**, bei der Aufsichtsbehörde Ihres Wohnsitzlandes — Artikel 77 DSGVO lässt Ihnen die Wahl.

---

## 8. Minderjährige

Plume ist ein Werkzeug zur Unterstützung beim Schreiben und richtet sich an ein Publikum **ab 16 Jahren**. Wir erheben wissentlich keine Daten von Kindern unter 16 Jahren, und die App ist weder für sie gestaltet noch für sie beworben. Wenn Sie sorgeberechtigt sind und glauben, dass Ihr Kind uns Daten übermittelt hat, schreiben Sie an sogacmoi7@gmail.com: Wir löschen das Konto.

Da die App das Umschreiben freier Texte erlaubt und Werbung anzeigt, ist sie für die Familienprogramme von Google Play nicht zugelassen.

---

## 9. Auftragsverarbeiter und Empfänger

| Dienstleister | Rolle | Wo |
|---|---|---|
| **Supabase** | Hosting der Datenbank, Authentifizierung, Serverfunktionen | Europäische Union (Frankfurt) |
| **OpenRouter** | Weiterleitung der Anfragen an das KI-Modell | **Außerhalb der Europäischen Union** |
| **Mistral AI** (über OpenRouter) | Modell, das den Text verarbeitet (Mistral Small) | Verarbeitung über den vorstehenden Vermittler |
| **Google Play / Google Billing** | Zahlung, Abonnements | Google Ireland / Vereinigte Staaten |
| **Google AdMob** | Werbung mit Belohnung | Google Ireland / Vereinigte Staaten |
| **Google (Systemdienste des Handys)** | Spracherkennung, Offline-Übersetzungsmodule | Je nach Ihrem Gerät |

**Wir verkaufen keine Daten und geben keine an Datenhändler weiter.**

**Übermittlungen außerhalb der Europäischen Union:** Die Nutzung von OpenRouter, Google Play und AdMob bedeutet eine Übermittlung von Daten außerhalb der Europäischen Union. Der rechtliche Rahmen dieser Übermittlungen (Standardvertragsklauseln, Angemessenheitsbeschluss) **muss vor der Veröffentlichung von einer fachkundigen Person geprüft und dokumentiert werden** — siehe die Anmerkung am Ende des Dokuments.

---

## 10. Sicherheit

Der Austausch zwischen der App und unseren Servern ist verschlüsselt (HTTPS/TLS). Der Zugriff auf die Daten in der Datenbank ist durch serverseitige Regeln beschränkt: Sensible Funktionen sind aus der App heraus nicht erreichbar. Kein System ist vollkommen sicher, aber keiner der von Ihnen umgeschriebenen Texte wird bei uns gespeichert — was schon rein mechanisch begrenzt, was ein Eindringen offenlegen könnte.

---

## 11. Änderungen

Jede Änderung dieser Datenschutzerklärung wird unter `https://readit0.github.io/plume-legal` mit einem neuen Datum veröffentlicht. Bei einer wesentlichen Änderung des Wegs Ihrer Daten informieren wir Sie in der App.

---

## Allgemeine Geschäftsbedingungen

Die Nutzungsbedingungen des Dienstes (Kontingente, Abonnements, Kündigung) stehen in einem gesonderten Dokument: `https://readit0.github.io/plume-legal/conditions-generales`.

---

> ### Von einer fachkundigen Person zu prüfen
>
> Dieses Dokument wurde durch Messung des tatsächlichen Verhaltens der App verfasst, **aber nicht von einer Juristin oder einem Juristen**. Vier Punkte bedürfen vorrangig einer fachkundigen Beurteilung:
>
> 1. **Die Datenübermittlung außerhalb der Europäischen Union** an OpenRouter. Das ist der heikelste Punkt: Es muss bestimmt werden, welcher Übermittlungsmechanismus gilt, es muss geprüft werden, ob mit diesem Dienstleister ein Auftragsverarbeitungsvertrag besteht, und beides muss hier festgehalten werden. Solange das nicht geschehen ist, beschreibt dieses Dokument die Übermittlung, ohne zu behaupten, dass sie abgesichert ist.
> 2. **Die Rechtsgrundlagen** in Abschnitt 7, insbesondere die Aufteilung zwischen Einwilligung und berechtigtem Interesse für den Bedienungshilfen-Dienst.
> 3. **Das Mindestalter** (16 Jahre) und dessen Übereinstimmung mit dem Fragebogen zur Altersfreigabe von Google Play.
> 4. **Der Hinweis zur KI** nach der europäischen Verordnung über künstliche Intelligenz (Transparenzpflicht für ein System mit begrenztem Risiko).

---

Dieses Dokument ist eine Übersetzung der französischen Fassung, die unter https://readit0.github.io/plume-legal/ verfügbar ist. Sie wird Ihnen zu Ihrer Information bereitgestellt. Bei Abweichungen wenden Sie sich bitte an sogacmoi7@gmail.com.
