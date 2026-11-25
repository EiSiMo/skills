# Pflege des Skills vu

Für den, der den Skill aktuell hält. Im laufenden Fall wird diese Datei nicht gebraucht.

## Was wo liegt

| Ordner | Inhalt | Entsteht wie |
|---|---|---|
| `SKILL.md` | Ablauf, Aufnahmeart, Rückfrage-Regel, Ausgabeform | von Hand |
| `ref/` | Schlüssel und Regeln aus den Dienstunterlagen | von Hand, aus `base/` |
| `recht/` | Gesetzestexte und Tatbestandskatalog als Text, `STAND.md` | erzeugt von `scripts/aktuell --laden`, nie von Hand ändern |
| `ort/` | Straßenverzeichnis Berlin mit Postleitzahlen: `strassen.txt` (Hausnummern), `kreuzungen.txt` | erzeugt von `scripts/aktuell --strassen`, nie von Hand ändern |
| `scripts/aktuell` | prüft und erneuert `recht/` und `ort/` | |
| `scripts/plz` | schlägt die Postleitzahl eines Unfallorts in `ort/` nach, ohne Netz | |
| `base/` | Quellunterlagen (Vordruck-Fotos, Ausfüllhilfe, GA mit Anlagen, Checkliste, Unfalltypen-Katalog). In `base/aufbereitung/` liegen die Abschrift der Fotos (`fotos.md`), die Auswertungen von GA und Ausfüllhilfe und das Skript, das `ref/beispiele.md` erzeugt hat | gehört nicht in das hochgeladene Paket |

## Gesetze und Katalog erneuern

```
python3 scripts/aktuell            prüft die Stände gegen gesetze-im-internet.de und kba.de
python3 scripts/aktuell --laden    lädt alles neu und schreibt recht/ samt STAND.md
```

Nach `--laden` auf zwei Meldungen achten:

- `FEHLER … § … steht nicht mehr im Gesetz`: Der Paragraf wurde aufgehoben oder umnummeriert. In der Liste `GESETZE` oben im Skript anpassen.
- `HINWEIS ref/beispiele.md nennt Tatbestandsnummern, die es im Katalog nicht mehr gibt`: Die Nummern dort ersetzen (im neuen `recht/tbkat.txt` nach dem Wortlaut suchen) oder streichen.

Ein weiteres Gesetz oder weitere Paragrafen: Zeile in `GESETZE` ergänzen (Dateiname, Kürzel, Pfadname der Seite auf gesetze-im-internet.de, Paragrafenliste oder `None` für alles), dann `--laden`. In `SKILL.md` die Zeile zu `recht/*.txt` anpassen.

Die Grenze zwischen Verwarnungsgeld und Bußgeld (55 €) steht in `SKILL.md` und `ref/avu.md`; sie folgt § 56 OWiG.

## Straßenverzeichnis erneuern

```
python3 scripts/aktuell --strassen    lädt rund 150 MB von gdi.berlin.de und baut ort/ neu (etwa eine Minute)
```

Einmal im Jahr genügt; `scripts/aktuell` meldet es, wenn der Abruf älter ist. Quelle sind drei amtliche Datensätze des Geoportals Berlin: "Adressen Berlin" (jede Adresse mit Postleitzahl), "Detailnetz Berlin" (Straßenabschnitte und Knoten) und "Postleitzahlen" (Flächen). Daraus rechnet das Skript:

- `ort/strassen.txt`: je Straße und Postleitzahl die Hausnummern. Geprüft am 25.11.2026: Für alle 403.006 Adressen mit Hausnummer liefert `scripts/plz` die amtliche PLZ.
- `ort/kreuzungen.txt`: je Straßenpaar, das sich an einem Knoten trifft, die PLZ der Fläche, in der der Knoten liegt. Liegt ein Nachbargebiet höchstens 15 m entfernt (20 m an Straßen der Klassen III und IV, 30 m an Hauptstraßen), steht dessen PLZ dahinter: Die Kreuzung liegt auf der Grenze. Das trifft etwa jede achte Kreuzung.

Meldet `--strassen` "Dienst geändert?" oder "Feld … fehlt", hat das Geoportal Namen von Schichten oder Feldern geändert; die stehen in `strassen_laden()`, `strassenzeilen()` und `kreuzungszeilen()` im Skript. Bis das behoben ist, bleibt das alte Verzeichnis gültig.

## Auf das Handy bringen

Die App nutzt eine hochgeladene Kopie. Nach jeder Änderung neu packen und in claude.ai unter den Skills ersetzen:

```
cd ~/Repositories/skills/skills && rm -f /tmp/vu.zip && zip -r /tmp/vu.zip vu -x 'vu/base/*' -x '*/__pycache__/*'
```

## Neuer Vordruck oder neue Unterlagen

1. Fotos oder PDF nach `base/` legen.
2. Abgleichen, was sich geändert hat, und die betroffene Datei anpassen:

| Datei | Stammt aus |
|---|---|
| `ref/statistik.md` Unfallart, Unfallstelle | Vordruck Vorderseite (linke Spalte), Ausfüllhilfe S. 5–9 |
| `ref/statistik.md` Unfalltyp | GA Anlage 3 S. 1–2, Unfalltypen-Katalog (Textseiten) |
| `ref/statistik.md` Ursachen | Schreibunterlage Rückseite (Verzeichnis), GA Anlage 2.2 S. 10–13 (Kopplungsregeln) |
| `ref/schluessel.md` | Schreibunterlage: Schlüsselseite (Destatis, BOWI 21, Felder 16 und 37) und Nationalitätszeichen der Hinweisseite |
| `ref/avu.md` | Vordruck beide Seiten, Hinweisseite der Schreibunterlage, Ausfüllhilfe, GA Ziffern 4, 5, 16, 22 |
| `ref/beispiele.md` | GA Anlage 3 S. 4–48; Ursachen und Tatbestandsnummern auf heutigen Stand umgestellt |
| `ref/poliks.md` | GA Ziffern 6, 15, Anlage 2.1, Fachnachricht 15.12.2014, Checkliste S. 4 (Unfallkommando) |
| `ref/flucht.md` | Checkliste VU-Flucht, GA Ziffern 10, 21.6, 22.2, Anlage 2.1 |
| `ref/sonderfaelle.md` | GA Ziffern 1.3, 3, 9, 11, 13, 14, 17–23 |
| `ort/` | Geoportal Berlin, siehe "Straßenverzeichnis erneuern" |

## Offene Punkte

Stellen, an denen die Unterlagen nichts Eindeutiges hergeben und der Skill eine begründete Annahme trifft. Beim Testen bestätigen oder korrigieren, dann hier streichen.

- **Ankreuzfelder "An" im Kopf**: Zuordnung StM 2 = BGSt 120, StM 1 = Dir K 23, StM 0 = Dir A ist aus den Ausfertigungshinweisen abgeleitet.
- **Tatbestandsaufnahme / Protokollaufnahme**: Bedeutung (am Ort / nachträglich auf der Dienststelle) ist erschlossen, nirgends definiert.
- **Ursachen 03 und 04**: Auf der Schreibunterlage stehen die Nummern versetzt gedruckt. Der Skill nimmt 03 = Übermüdung, 04 = sonstige körperliche oder geistige Mängel, wie in der GA.
- **BOWI-Schlüssel für Radfahrer und Fußgänger** (9950, 9940): aus dem Aufbau des Schlüssels abgeleitet, die Schreibunterlage nennt dafür kein Beispiel.
- **Besonderheit 1 "Radverkehrsführung"** neben 8 und 9, und das Feld "Auf" bei einem Zusammenstoß auf der Radfurt in der Kreuzung: Die Unterlagen grenzen das nicht ab; der Skill nennt im Zweifel beide Möglichkeiten.
- **Hauptanstoßstelle**: Der Skill nennt die Stelle in Worten, nicht als Sektorzahl; die Lage der Sektoren 1 bis 12 ist auf dem Foto nicht sicher zuzuordnen.
- **POLIKS**: Feldnamen und Reiter stammen aus der Anleitung von 2008. Aktuelle Bildschirmfotos der Masken (VU-Anzeige, Flucht) würden `ref/poliks.md` und `ref/flucht.md` deutlich verbessern.
- **Tatbestandsnummer neben einer Straftat**: Nach der Anleitung von 2008 bleibt das Feld bei Straftaten leer.
- **Vordruck**: Grundlage ist Pol V100 Stand 05.23. Die Ausfüllhilfe beschreibt schon 05/25 mit dem neuen Feld 91 (Nationalitätszeichen des Fahrzeugs).
- **Vollständige Schlüssellisten** für Beweismittel und Halteranfrage stehen laut Schreibunterlage im Intranet; der Skill kennt nur den Auszug.
- **Musterfälle**: Die Unfalltypen und Ursachen sind amtlich (2008), die Tatbestandsnummern wurden am 25.11.2026 gegen den Katalog vom 08.10.2026 neu zugeordnet. Zwei Fälle blieben unsicher: "falsche Fahrbahnbenutzung, Gegenverkehr" (Unfallart 4) und "Beifahrer greift ins Lenkrad" (Unfallart 0).
