# POLIKS-VU (Anwendungsfall VU-Anzeige)

Die Statistikangaben (Unfallart, Unfalltyp, Unfallstelle, Ursachen) stehen in `statistik.md` und gelten hier unverändert. POLIKS zeigt Katalogtexte statt Schlüsselzahlen: Gib deshalb immer Zahl und Text aus. Die Texte für die Art der Beteiligung stehen in `schluessel.md`.

Quellen: GA PPr St 5/2008 mit Anlage 2.1 (Ausfüllanleitung POLIKS) und Fachnachricht vom 15.12.2014, Checkliste VU-Flucht/VUK (06.2026). **Die Ausfüllanleitung ist von 2008. Feldnamen und Reiter können in der heutigen Maske anders heißen;** die Regeln dahinter gelten weiter.

## Unfallkategorie

| Kat. | Bedeutung |
|---|---|
| 1 | Unfall mit Getöteten (am Unfallort oder innerhalb von 30 Tagen verstorben) |
| 2 | Unfall mit Schwerverletzten (mindestens 24 Stunden stationär im Krankenhaus), keine Getöteten |
| 3 | Unfall mit Leichtverletzten (alle übrigen Verletzten) |
| 4 | Schwerwiegender Unfall mit Sachschaden: Straftat oder Ordnungswidrigkeit im Bußgeldbereich, **und** mindestens ein Kfz nicht fahrbereit. Auch mit Alkohol |
| 5 | Sonstiger Sachschadenunfall ohne Alkohol: alle Kfz fahrbereit, oder gar kein Straf- oder Bußgeldvorwurf. Auch eine Flucht, wenn die Fahrzeuge fahrbereit sind |
| 6 | Sonstiger Sachschadenunfall unter Alkoholeinwirkung, alle Kfz fahrbereit |

Die Abgrenzung schwer/leicht folgt der amtlichen Unfallstatistik; die GA definiert sie nicht.

## Wer bearbeitet weiter

In die Kopfzeile der Ausgabe gehört einer dieser Einträge:

- **"Weiterbearbeitung Dir K 23"** (Verkehrsermittlungsdienst): der Regelfall bei POLIKS, also bei Verletzten, Straftatverdacht und Flucht.
- **"Weiterbearbeitung nach StM …"** nur in zwei Fällen:
  - **Sachschaden mit Bußgeld**: mindestens ein Kfz nicht fahrbereit, Verstoß im Bußgeldbereich, niemand verletzt, kein Straftatverdacht. In der Regel StM 2 (Bußgeldstelle, BGSt 120); StM 1, wenn noch ermittelt werden muss.
  - **Alleinunfall**: Nur der Fahrer selbst ist verletzt (nicht getötet), kein anderer Verkehrsteilnehmer war beteiligt, kein Verdacht einer Verkehrsstraftat, kein Alkohol. Wer nur einen Sachschaden hat (Zaun, geparktes Auto), zählt dabei nicht als beteiligt. Steuerungsmerkmal wie beim A-VU (`avu.md`): 2, sobald ihm ein Verstoß vorgehalten wird; 0 ohne Vorwurf.

## Vorgang und Tatvorwurf

- **Ereignisbezeichnung** genau aus dem Untermenü wählen ("Verkehrsunfall mit schwerverletzter Person"). Unter **Zusatzbezeichnung** weitere Tatbestände, die nicht im Erfassungsgrund stecken (Fahren ohne Fahrerlaubnis, Unerlaubtes Entfernen vom Unfallort).
- **Tatvorwurf**: Jeder strafrechtlich handelnden Person alle verwirklichten Straftatbestände zuordnen, je Norm eine Zeile, auch bei Unbekannten und bei Kindern. Einzutragen ist die verletzte Norm, nicht der statistische Begriff: nicht "VU mit leichtverletzter Person", sondern "Fahrlässige Körperverletzung, § 229 StGB".
- **Verletzte**: Ist ein anderer verletzt und hat ein Beteiligter dafür eine Ursache gesetzt, lautet der Vorwurf gegen ihn fahrlässige Körperverletzung, § 229 StGB. Das ist ein Antragsdelikt (§ 230): Strafantrag des Verletzten aufnehmen oder vermerken, dass er ihn sich vorbehält.
- **Ordnungswidrigkeiten** können in einer Zeile zusammengefasst werden: Tatvorwurf "Ordnungswidrigkeit", Zusatzbezeichnung "VK-Owi", Rechtsnorm aus der Spalte Vorschriften des Katalogs, etwa "§ 9 Abs. 3, § 1 Abs. 2, § 49 StVO i. V. m. § 24 StVG".
- **Tatbestandsnummer neben einer Straftat**: Das Feld bleibt bei der Person leer, wenn sie wegen desselben Verhaltens einer Straftat beschuldigt ist. Nenne die Nummer des Verkehrsverstoßes trotzdem in einer Zeile ("OWi dahinter"): Ihre Normen gehören als VK-Owi in den Tatvorwurf, und sie gilt, falls die Straftat entfällt.
- **Unfallflucht**: eigener Weg, siehe `flucht.md`.
- Was der Katalog nicht kennt (etwa Anstiftung), als "Sonstiges Delikt" mit Zusatzbezeichnung und Rechtsnorm.
- **Mehrere Beschuldigte**: Die Strafermittlung gegen die erste Person läuft im VU-Vorgang. Für jede weitere beschuldigte Person ein gesonderter Vorgang mit deliktischem Erfassungsgrund und Anwendungsfall Strafanzeige, mit Verweis auf den Parallelvorgang. Die Statistikdaten stehen nur im VU. Eine Verkehrs-OWi gegen eine andere Person wird aus dem VU-Vorgang verfolgt, Kopie an die Bußgeldstelle.
- Kleinere Straftaten im Zusammenhang mit dem Unfall (Beleidigung, einfache Körperverletzung) werden beim VU mitbearbeitet, mit eigenem Vorgang Strafanzeige.

Häufige Normen (Wortlaut in `recht/`): § 229 StGB fahrlässige Körperverletzung · § 222 StGB fahrlässige Tötung · § 142 StGB unerlaubtes Entfernen · § 315c StGB Gefährdung des Straßenverkehrs · § 316 StGB Trunkenheit im Verkehr · § 315b StGB gefährlicher Eingriff · § 315d StGB verbotenes Rennen · § 21 StVG Fahren ohne Fahrerlaubnis · § 6 PflVG ohne Haftpflichtversicherung · § 24a StVG 0,5 Promille, THC (OWi) · § 24c StVG Fahranfänger (OWi).

## Ereignis- und Statistikdaten

| Feld | Regel |
|---|---|
| Unfallart, Unfalltyp, Unfallkategorie | Je ein Eintrag |
| Charakteristik, Besonderheiten der Unfallstelle | Je höchstens drei |
| Verkehrsregelung | Höchstens ein Eintrag; keine Ampel = kein Eintrag |
| Geschwindigkeitsbegrenzung | Nur wenn durch Zeichen angeordnet |
| Lichtverhältnisse | Pflicht, ein Eintrag |
| Straßenzustand | Pflicht, höchstens zwei |
| Aufprall auf Hindernis neben der Fahrbahn | Offen lassen, wenn kein Katalogbegriff zutrifft |
| Allgemeine Unfallursache | Die Ursachen 70 bis 90, die zu keiner Person gehören |
| Konkretisierung der Unfallursache | Kurze Beschreibung bei 89, oder Klarstellung, wenn die Nummer mehreres umfasst (72: "Eis") |
| Regelbetrag | Bei Ordnungswidrigkeit "Verwarnungsgeld" oder "Bußgeld"; bei Straftaten leer |
| VU-Merkmal | Etwa "präventionsrelevanter Verkehrsunfall"; bei polizeilichem Betriebsunfall "Betriebsunfall" |

## Beteiligte

- Ordnungsnummern ab 1 in aufsteigender Reihenfolge; 01 hat die wesentlichste Ursache gesetzt. Geparkte, beschädigte Fahrzeuge sind Beteiligte.
- **Sonstige Geschädigte** bekommen in POLIKS eigene Ordnungsnummern im Anschluss an die Beteiligten. Geschädigte Mitfahrer bekommen die Nummer ihres Fahrzeugs. Beschädigte Sachen stehen unter "Sonstige Sache", nicht unter "Natürliche Person".
- Niemand wird doppelt erfasst (als Beteiligter und Zeuge).
- Erst abgleichen, dann dem Titel die Ordnungsnummer voranstellen.

| Feld je Fahrzeugführer | Regel |
|---|---|
| § 142 StGB (unerlaubtes Entfernen) | Pflicht, ja oder nein |
| Alkohol, AAK-Wert | Eintragen, was festgestellt ist. Den BAK-Wert trägt der Ermittlungsdienst nach |
| Drogen-/Medikamenteneinwirkung | Nur bei Hinweisen, sonst leer |
| Sicherheitsgurt angelegt, Schutzhelm getragen | Pflicht, wenn für das Fahrzeug vorgeschrieben |
| Fahrerlaubnis vorhanden; Führerschein | Daten der Klasse, die für das geführte Fahrzeug gilt |
| Vorläufig festgestellte Ursachen | Ursachen 01 bis 69 dieser Person; "Konkretisierung zur Ursache" bei Restpositionen (49, 69) |
| Tatbestandsnr., Konkretisierung | Aus `recht/tbkat.txt` wie beim A-VU; leer neben einer Straftat (siehe oben) |
| Art der Beteiligung | Als Text nach dem BOWI-Schlüssel in `schluessel.md`: Rolle und Fahrzeug, bei schweren Fahrzeugen das Gewicht ("Führer Pkw", "Führer Lkw über 7,5 t", "Radfahrende"); geführt oder geparkt. "Konkretisierung der Verkehrsbeteiligung" nur bei "sonstiges" |

| Feld je Kfz | Regel |
|---|---|
| Beschädigte Sektoren | Nur Zahlen nach dem Schema der Maske (1, 2), kein Text |
| Schadensbeschreibung | Text mit Verlauf; zurückgebliebene oder aufgefundene Teile nennen. Bei Flucht besonders genau |
| Schadenshöhe | Geschätzt oder bekannt |
| Insassen | Gesamtzahl zur Unfallzeit; geparkt "00"; unbekanntes Fahrzeug: leer |
| Gefahrgut | Ja oder nein; unbekannt (Flucht): offen lassen |

## Maßnahmen (HEM)

Blutentnahme, Sicherstellung oder Beschlagnahme von Führerschein oder Fahrzeug über die Registerkarten als HEM eintragen, nicht als eigenen Anwendungsfall. "Ausdrücklicher Widerspruch" immer mit ja oder nein angeben. Vor Ort erstellte Protokolle zum Vorgang scannen.

## Sachverhalt

- Kurz, mit den verkehrsrechtlichen Begriffen, in der üblichen Anrede: "Herr M. (01) befuhr die A-Straße in Richtung B-Straße …". Keine Himmelsrichtungen. Kein Verweis auf andere Vorgangsteile.
- Zusätzlich hinein: Angaben zur Fahrerlaubnis, wenn der Führerschein fehlt; Ausfallerscheinungen bei Alkohol, Drogen, Medikamenten; körperliche oder geistige Mängel; Hinweis auf Verjährung.

## Skizze und Fotos

Eine Symbolskizze (POLIKS-Graf, Symbol der ersten Kollision) gehört zu jedem Unfall. Darüber hinaus gilt die erste zutreffende Zeile von oben:

| Lage | Dokumentation |
|---|---|
| Verkehrsstraftat, Person getötet oder ärztliche Behandlung gewünscht oder nötig | Maßstabsgerechte Skizze, Fotos |
| Verkehrsstraftat, Person verletzt, keine ärztliche Behandlung | Verhältnisgerechte Skizze, gegebenenfalls Fotos |
| Verkehrsstraftat, Verursachung ungeklärt, oder Unfallflucht | Verhältnisgerechte Skizze, gegebenenfalls Fotos. Flucht mit Verletzten: maßstabsgerecht und Fotos |
| Verkehrsstraftat, Verursachung geklärt und Rechtslage eindeutig | Grundsätzlich keine Skizze |
| Ordnungswidrigkeit, geklärt und eindeutig | Grundsätzlich keine Skizze |
| Ordnungswidrigkeit, ungeklärt | Verhältnisgerechte Skizze |

## Unfallkommando (Dir K 24) anfordern

Immer über den Lagedienst der örtlichen Direktion. Kriterien:

- mindestens eine Person getötet, oder mit dem Ableben ist zu rechnen
- mindestens eine Person schwer verletzt und Notarzt oder Rettungshubschrauber am Ort
- besonderes Schadens- oder Spurenbild ("Spinne" in der Windschutzscheibe), Verletzungen lassen erhebliche Folgeschäden erwarten
- Unfall bei Sonder- oder Wegerechtsfahrt (gleich welcher Behörde) mit mindestens einer schwer verletzten Person
- Gefahrguttransport mit Freisetzung von Gefahrgut
- Unfallflucht mit schwer verletzter Person
- besondere Komplexität oder erschwerte Beweisführung (weiträumiges Trümmerfeld)
- frische Unfallspuren an einem nach Diebstahl oder unbefugter Benutzung aufgefundenen Kfz

Rücksprache zur Unterstützung: besonderes Medieninteresse, Verdacht auf gestellten Unfall (Zuständigkeit LKA 223), fehlende technische Ausstattung für die Aufnahme.

Ein Unfallort mit Schwerverletzten oder Getöteten ist ein Tatort: Veränderungsverbot, Veränderungen durch Feuerwehr oder Polizei dokumentieren.

## Ausgabe bei POLIKS

Es gelten die Regeln aus `SKILL.md`: jede Angabe ein eigener Listenpunkt mit lesbarer Bezeichnung, Tatbestandsnummern als Link ohne Zitat, nichts, was der Beamte am Ort einfach abliest. Das Muster zeigt nur die Form; keine Zahl daraus übernehmen.

```
Angenommen: Pkw fahrbereit, Führerschein vorgelegt, kein Alkohol

**POLIKS-VU**
- Unfallkategorie: 3 Leichtverletzte
- Weiterbearbeitung: Dir K 23
- PLZ Unfallort: 1xxxx

**Unfall**
- Unfallart: 5 Zusammenstoß mit anderem Fahrzeug, das einbiegt oder kreuzt
- Unfalltyp: 2 Abbiege-Unfall

**01 – Pkw, biegt rechts ab**
- Art der Beteiligung: Führer Pkw (oder Führer und Halter)
- § 142 StGB: nein
- Ursachen: 34 Fehler beim Abbiegen nach rechts
- Tatvorwurf: Fahrlässige Körperverletzung, § 229 StGB
- Strafantrag: von 02 aufnehmen
- Tatvorwurf: Ordnungswidrigkeit, VK-Owi, § 9 Abs. 3, § 1 Abs. 2, § 49 StVO i. V. m. § 24 StVG
- Tatbestandsnr.: leer wegen der Straftat
- OWi dahinter: [1xxxxx](https://www.weg.li/charges/1xxxxx)

**02 – Radfahrerin, fährt geradeaus**
- Art der Beteiligung: Radfahrende
- § 142 StGB: nein
- Verletzung: leicht
- Verstoß: keiner

**Dokumentation**
- Skizze: maßstabsgerecht, mit Fotos (ärztliche Behandlung)
- Zeugen: Fußgänger am Ort

Wird Kategorie 2, falls 02 mindestens 24 Stunden stationär bleibt.
```

- Kopf: Unfallkategorie mit Text, Weiterbearbeitung und, wenn nachgeschlagen, die PLZ des Unfallorts. Kein Verjährungsdatum. Warum POLIKS, nur wenn es nicht offensichtlich ist (eigener Punkt "Grund: nicht fahrbereit und Bußgeld").
- Liegt nur eine Ordnungswidrigkeit vor: je Person "Tatbestandsnr.: [1xxxxx](https://www.weg.li/charges/1xxxxx)", ohne Betrag.
- Unter "Unfall" stehen nur Unfallart und Unfalltyp, dazu "Allgemeine Unfallursache: …", wenn es eine gibt. Die Ursachen 01 bis 69 stehen bei der Person, weil die Maske sie dort führt.
- Art der Beteiligung: Ob der Fahrer auch Halter ist, nicht annehmen; ist es offen, beides nennen.
- Verletzungen stehen als Punkt "Verletzung: …" bei der Person. Wer nur sich selbst verletzt hat, begründet keinen § 229 StGB.
- Löst der Fall Maßnahmen aus (Blutentnahme, Führerschein, Fahrzeug), ein Punkt "Maßnahmen (HEM): …" bei der Person.
- Unter "Dokumentation" die Skizze nach der Tabelle oben, "Zeugen: …", wenn der Sachverhalt welche nennt, und "Unfallkommando: anfordern", wenn ein Kriterium erfüllt ist.
- Nicht ausgeben, was nur der Beamte vor Ort weiß und selbst einträgt: Gurt, Helm, Alkoholwerte, Führerscheindaten, Insassenzahl, Schadenssektoren.
