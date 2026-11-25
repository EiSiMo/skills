# A-VU: Vordruck Pol V100 "Sonstiger Sachschadenunfall"

Stand des Vordrucks: 05.23. Die Felder Unfallart bis Ursachen stehen in `statistik.md`, die Schlüsselzahlen der Schreibunterlage (Destatis, BOWI, Beweismittel, Halteranfrage, Nationalitätszeichen) in `schluessel.md`. Hier steht, wie der Vordruck auszufüllen ist.
Quellen: Vordruck und Schreibunterlage (05.23), Ausfüllhilfe PA 06.26, GA PPr St 5/2008 mit Anlage 2.2 (Stand 06.2026).

Ein Vordrucksatz fasst zwei Beteiligte. Bei mehr Beteiligten weitere Sätze nehmen; die Statistikfelder nur auf dem ersten ausfüllen.

## Kopf

| Feld | Eintrag |
|---|---|
| Sammelanzeige | Nur ankreuzen bei mehreren Unfällen desselben Verursachers (etwa ein zweiter Unfall beim Räumen der Unfallstelle) |
| Tatbestandsaufnahme / Protokollaufnahme | Tatbestandsaufnahme: am Unfallort aufgenommen. Protokollaufnahme: nachträglich auf der Dienststelle angezeigt. (Die GA erklärt die Begriffe nicht ausdrücklich; so ergibt es sich aus ihrer Ziffer 11.) |
| An | Folgt dem Steuerungsmerkmal: 2 = BGSt 120, 1 = Dir K 23, 0 = Dir A (Ablage beim Abschnitt). (Zuordnung aus den Ausfertigungshinweisen der Schreibunterlage abgeleitet.) |
| Aktenzeichen BGSt | Bleibt leer |
| Unfallvorgangsnummer | Abschnitt des Unfallortes (2 Stellen) · Unfalldatum TTMMJJ · Unfallzeit HHMM · A (vorgedruckt) · Steuerungsmerkmal |
| Verjährt am | Unfalldatum plus sechs Monate (§ 26 Abs. 3 StVG, in `recht/stvg.txt`) |
| Dienststellenkennung | Schlüsselzahl der aufnehmenden Dienststelle, sechs Stellen, ohne Dienstgruppe (A 22 = 002200) |
| Unfalldatum, Unfallzeit | TTMMJJ und HHMM. Unbekannt: Zeitpunkt der Feststellung |
| Anzahl der Beteiligten | Zweistellig (02) |
| Unfallort | Postleitzahl, Bezirk (Kürzel mit vier Buchstaben), Straße und Hausnummer, Namen ausgeschrieben. Ohne Hausnummer umschreiben ("zwischen A-Str. und B-Str.", "ca. 100 m vor A-Str."). An Kreuzung oder Einmündung alle Straßen mit Schrägstrich, die vorfahrtrechtlich übergeordnete zuerst, auch wenn eine Ampel regelt. Keine Baum- oder Lichtmastnummern (Ausnahme Autobahn). Höchstens 155 Zeichen |
| Unfallkategorie (Feld 61) | 5 ist vorgedruckt |
| Sondererhebung, Felder 68–78 | Bleiben leer (nur auf besondere Weisung) |

### Steuerungsmerkmal

| StM | Wann | Wohin |
|---|---|---|
| 2 | **Normalfall, sobald jemandem ein Verstoß vorgehalten wird.** Ermittlungen abgeschlossen, die Bußgeldstelle verfolgt: Verstoß im Bußgeldbereich, oder Verwarnungsgeld nicht vor Ort bezahlt (abgelehnt, nicht zahlungsfähig, oder schlicht kein Kartengerät dabei) | BGSt 120 |
| 1 | Weitere Ermittlungen nötig: Führerschein nicht mitgeführt, behaupteter oder festgestellter technischer Mangel, der zum Unfall beitrug. Hergang oder Verursacher unklar nur im Ausnahmefall | Dir K 23 (Verkehrsermittlungsdienst) |
| 0 | Am Ort abgeschlossen. Nur wenn der Nutzer es sagt (Verwarnungsgeld vor Ort bezahlt, oder mündlich ohne Verwarnungsgeld verwarnt), oder wenn es keinen Vorwurf gibt: Wildunfall, unabwendbares Ereignis (aufgewirbelter Stein oder Splitt; nicht bei verlorener Ladung), Kind unter 14 | Ablage beim Tatortabschnitt |

In der Praxis wird kein Kartengerät (ZVT) mitgeführt. Deshalb nie von dir aus StM 0 annehmen, wenn ein Verstoß im Raum steht.

## Beteiligte und Geschädigte

- **Beteiligter** ist jeder, dessen Verhalten zum Unfall beigetragen haben kann. Zusätzlich zählt jedes geparkte Fahrzeug, das beschädigt wurde, als Beteiligter mit eigener Ordnungsnummer.
- **Sonstige Geschädigte** (eigenes Feld, keine Ordnungsnummer): abgestellte Fahrräder und Eigentümer beschädigter Sachen wie Zaun, Ampelmast, Lichtmast, Baum. Name oder Firma, Anschrift, Art und Höhe des Schadens. Tiere sind keine Beteiligten.
- **Ordnungsnummer 01** bekommt, wer nach dem ersten Anschein die wesentlichste Ursache gesetzt hat. Die übrigen folgen aufsteigend.

| Feld je Beteiligtem | Eintrag |
|---|---|
| Personalien | Familienname in GROSSBUCHSTABEN, Rufname unterstrichen, je Zeile höchstens 30 Zeichen (Wohnort 25) |
| Staatsangehörigkeit | Immer, als Nationalitätszeichen wie am Kfz, auch D |
| Erteilungsdatum FE | Datum der Klasse, die für das geführte Fahrzeug nötig ist (Rückseite des Führerscheins) |
| Geschlecht | m, w oder d ankreuzen |
| Destatis-Schlüssel | Art der Verkehrsbeteiligung aus `schluessel.md`. Form: eine Stelle / zwei Stellen (Pkw geführt: 1/21) |
| Rechtswirksam verwarnt | Nur bei StM 0. Vor Ort bezahlt: Betrag eintragen und "bezahlt ZVT" ankreuzen. Mündlich ohne Verwarnungsgeld: kein Betrag, "mdl." ankreuzen |
| BOWI-Anzeige | Ankreuzen, wenn ein Bußgeldverfahren eingeleitet wird; dann Rückseite ausfüllen |
| BOWI-TBNR | Immer eintragen, sobald dem Beteiligten ein Verstoß vorgehalten wurde, gleich ob verwarnt oder angezeigt. Eine nötige Konkretisierung dahinter |
| Halter | Wie Fahrer: "w. o.". Sonst Anschrift aus der Zulassungsbescheinigung Teil I |
| Kennzeichen | Mit Bindestrich nach dem Zulassungsbezirk (B-AB 1234). Anhängerkennzeichen auf die Rückseite |
| Sachschaden | Schätzwert in Euro |
| Hauptanstoßstelle | Im Fahrzeugschema ankreuzen, höchstens drei Kreuze, nur die erste Anstoßstelle |
| Kfz nicht fahrbereit | Ankreuzen, wenn es nicht mehr aus eigener Kraft wegfahren kann. Reifenwechsel oder bloße Verkehrsunsicherheit zählen nicht. Achtung: nicht fahrbereit und Verstoß im Bußgeldbereich heißt POLIKS statt A-VU |
| Gefahrguttransport | Ankreuzen, wenn zutreffend |

Ist ein Beteiligter oder Geschädigter nicht am Ort (geparktes Auto, Halter fehlt): Hinweiszettel mit dem Unfallaktenzeichen am Fahrzeug hinterlassen.

**Symbolskizze**: Nordpfeil nach oben. Jeder Beteiligte als Pfeil in Fahrtrichtung mit Kennbuchstabe und Ordnungsnummer (P1, R2). Verursacher mit Querstrich auf dem Pfeil, Stehende oder Wartende mit Standstrich am Pfeilende. Straßennamen dazu. Kennbuchstaben: P Pkw · L Lkw, Zugmaschine · LA Lkw mit Anhänger, Sattelzug · B Bus · K Krad · M Moped · R Radfahrer · F Fußgänger · A Anhänger · Strab Straßenbahn · S Sonstige · X Unbekannt.

## Verwarnung oder Anzeige

Die Tatbestandsnummer wählst du nach den Regeln in `SKILL.md`. Was daraus folgt, bestimmt der Regelsatz:

| Lage | Folge | StM |
|---|---|---|
| bis 55 € (Verwarnungsgeld), nicht vor Ort bezahlt: **der Normalfall** | BOWI-Anzeige ankreuzen, Rückseite ausfüllen. Ist der Betroffene einverstanden, dort "zahlungswillig, aber -unfähig" ankreuzen; er bekommt das Verwarnungsangebot dann schriftlich von der Bußgeldstelle. Lehnt er ab, die Ablehnung in der Anhörung vermerken | 2 |
| ab 60 € (Bußgeld) | BOWI-Anzeige ankreuzen, Rückseite ausfüllen. Ist zugleich ein Kfz nicht fahrbereit: POLIKS statt A-VU | 2 |
| Nutzer sagt: Verwarnungsgeld vor Ort bezahlt | "Rechtswirksam verwarnt": Betrag eintragen, "bezahlt ZVT" ankreuzen. Keine Rückseite | 0 |
| Nutzer sagt: mündlich verwarnt, ohne Verwarnungsgeld | "mdl." ankreuzen, kein Betrag. Keine Rückseite | 0 |
| kein Vorwurf gegen irgendwen (Wild, aufgewirbelter Stein, Kind unter 14) | kein Eintrag | 0 |

Eine Verwarnung ohne Verwarnungsgeld ist bei unbedeutenden Verstößen zulässig; es zählt das Gewicht des Verstoßes, nicht die Schadenshöhe (positiv etwa, wenn der Verursacher eines Parkremplers selbst die Polizei ruft). Ob er so verfährt, entscheidet der Beamte; von dir aus schlägst du es nicht vor.

**Mehrere Verstöße derselben Person.** Durch dieselbe Handlung (Tateinheit): die Nummer mit dem höchsten Regelsatz eintragen, die übrigen nur im Feld Unfallhergang nennen. Durch verschiedene Handlungen (Tatmehrheit): die Nummer eintragen, aus der der Unfall folgt; für die übrigen je eine eigene BOWI-Anzeige.

**Führerschein nicht mitgeführt:** dieser Person keine Verwarnung anbieten, weder mit noch ohne Verwarnungsgeld (sonst Strafklageverbrauch, falls gar keine Fahrerlaubnis besteht). StM 1. Die BOWI-TBNR des Unfallverstoßes trotzdem eintragen. Im Feld Führerscheindaten nur ein Stern, die erfragten Daten unter Unfallhergang ("* 02 FS nicht mitgeführt. Eigene Angaben stimmen mit ZEVIS-Eintrag überein (Kl. B, 2003 in München erworben)"). Das Nichtmitführen ist ein eigener Verstoß (Katalogsuche: `grep -i "Führerschein nicht mit" recht/tbkat.txt`); auch dessen Nummer unter Unfallhergang nennen. Weiterfahrt grundsätzlich untersagen.

## Rückseite

Nur auszufüllen bei BOWI-Anzeige (StM 2) oder Weiterermittlung (StM 1). Bei StM 1 gehören Hergang, Führerscheindaten und Zeugen hinein, dazu die Felder 08 bis 37, soweit der Verstoß schon feststeht.

| Feld | Eintrag |
|---|---|
| BOWI-Verfahren gegen | Ordnungsnummer des Betroffenen |
| 08 Tatbestands-Nr. | Sechs Stellen aus dem Katalog |
| 09 Konkretisierung | Pflicht, wenn der Tatvorwurf im Katalog eine Auswahl `<a/b>`, einen Platzhalter `#…#` oder `*)` enthält: die zutreffende Variante oder den Wert nennen (bei "<entgegenkommender/gleicher> Richtung": "gleicher"). Bei `+)`: worin die Behinderung oder Gefährdung bestand. Hier auch der Hinweis auf Tateinheit oder Tatmehrheit. Der Text geht wörtlich in den Bescheid |
| 13 Verkehrsbeteiligung | BOWI-Schlüssel aus `schluessel.md`, vier Stellen. Führer eines Pkw: 1040; ist er zugleich Halter: 3040. Ist das nicht bekannt, beide nennen |
| 14 Sonst. Verkehrsbeteiligung | Text nur, wenn der Schlüssel "sonstiges" lautet (Feld 13: 1990, Feld 14: "Trike") |
| 37 Beweismittel | Schlüssel aus `schluessel.md`, höchstens drei. Beim Unfall üblich: 3 (Angaben des Betroffenen); dazu A bei unabhängigem Zeugen, 4 wenn Fotos gefertigt wurden, Z nur wenn der Beamte den Hergang selbst gesehen hat |
| 38 Sonst. Beweismittel | Nur wenn kein Schlüssel passt ("Dashcam"), höchstens 60 Zeichen |
| 50 abw. EUR-Betrag | Bleibt leer (nur Bußgeldstelle). Einen Vorschlag zur Erhöhung kurz unter Unfallhergang begründen |
| Fabrikat | Hersteller (VW, Ford) |
| 16 Halteranfrage | Leer bei gewöhnlichem deutschem Kennzeichen, sonst Schlüssel aus `schluessel.md` |
| Hinweis auf Aussagefreiheit | Pflicht, in der Regel "ja" |
| Verstoß zugegeben; zahlungswillig, aber -unfähig | Zutreffendes ankreuzen |
| Führerscheindaten | Klasse, Ausstellungsdatum (Vorderseite, Nr. 4a), Behörde ("C1E 21.05.99 LEA Berlin"). Ohne BOWI-Verfahren nur "lag vor". Bei ausländischem Führerschein Ersteinreise und Meldeverhältnisse prüfen |
| Versicherungskarten-Nr. | Nur bei außerhalb der EU zugelassenem Kfz |
| Unfallhergang | Bei ungeklärtem Hergang (StM 1) die Schilderung. Außerdem: weitere Tatbestandsnummern bei Tateinheit, Führerscheindaten bei Nichtmitführen, Anhängerdaten |
| Zeugen | Nur Personen, die nicht schon Beteiligte sind; Mitfahrer zählen. Erste Spalte: Ordnungsnummer, gegen die der Zeuge aussagt |
| Anhörung | Äußerung nach Belehrung (§ 55 OWiG, §§ 163a, 136 StPO), knapp; Spontanäußerungen als solche kennzeichnen |

## Ausfertigungen

1. Ausfertigung (weiß/rot): bei StM 0 Ablage beim Tatortabschnitt, bei StM 1 sofort an die sachbearbeitende Dienststelle, bei StM 2 sofort an BGSt 120.
2. Ausfertigung (weiß/grün): Dir E/V Abt. Verkehr VSD 3.
3. Ausfertigung (weiß): bei StM 1 mit der ersten an die sachbearbeitende Dienststelle, sonst an den Tatortabschnitt.
4. Ausfertigung (weiß): Tatortabschnitt.
