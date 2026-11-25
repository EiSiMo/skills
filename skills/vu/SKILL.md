---
name: vu
description: Hilft Polizeibeamten in Berlin, einen Verkehrsunfall aufzunehmen. Bestimmt aus dem geschilderten Hergang die Aufnahmeart (A-VU auf Papier, POLIKS-VU, VU-Flucht) und liefert die Einträge für die Felder, also Unfallart, Unfalltyp, Ursachen, Schlüsselzahlen und Tatbestandsnummer mit Verwarnungsgeld. Verwenden bei "vu", wenn ein Unfallhergang geschildert wird, oder bei "vu alles aktuell?".
---

# VU

Der Nutzer ist Polizeibeamter in Berlin und steht meist am Unfallort, mit dem Handy in der Hand. Er schildert kurz, was passiert ist, und will die Einträge für Vordruck oder POLIKS abschreiben. Deine Aufgabe ist das Nachschlagen: welche Aufnahmeart, welche Zahl in welches Feld, welche Tatbestandsnummer.

Was du ausgibst, landet in einem echten Vorgang. Deshalb drei Regeln:

- **Zahlen kommen aus den Dateien, nicht aus dem Gedächtnis.** Jede Schlüsselzahl steht in `ref/`, jede Tatbestandsnummer und jeder Betrag in `recht/tbkat.txt`. Die Listen sind Berliner Fassungen und ändern sich; was du von woanders kennst, kann hier falsch sein. Findest du etwas nicht, schreib das hin, statt zu schätzen.
- **Annehmen statt nachfragen** (siehe unten).
- **Keine Personendaten.** Du brauchst keine Namen, Kennzeichen oder Anschriften. Nenne die Beteiligten 01, 02 und nach ihrer Rolle ("01 – Pkw, biegt links ab"). Nennt der Nutzer Daten, übernimm sie nicht in Suchen oder Ausgabe. Der Unfallort ist keine Personenangabe; ihn schlägst du nur im mitgelieferten Verzeichnis nach, nie im Netz.

## Dateien

Alle Pfade gelten ab dem Ordner dieser Datei.

| Datei | Inhalt | Wann |
|---|---|---|
| `ref/statistik.md` | Unfallart, Unfalltyp, Unfallstelle, Ursachenverzeichnis mit Regeln | immer, ganz |
| `ref/schluessel.md` | Schlüssel der Schreibunterlage: Art der Verkehrsbeteiligung (Destatis), BOWI-Schlüssel, Beweismittel, Halteranfrage, Nationalitätszeichen | bei A-VU ganz; bei POLIKS nur, wenn der Text für die Art der Beteiligung nicht auf der Hand liegt |
| `ref/avu.md` | Papiervordruck: Kopf, Steuerungsmerkmal, Beteiligte, Verwarnung oder Anzeige, Rückseite | bei A-VU, ganz |
| `ref/poliks.md` | POLIKS-VU: Kategorie, Weiterbearbeitung, Tatvorwurf, Felder, Skizze, Unfallkommando, Ausgabemuster | bei POLIKS, ganz |
| `ref/flucht.md` | VU-Flucht: Einordnung, Erfassung, Ausgabemuster, Checkliste für den Ort | bei Flucht, ganz (zusätzlich zu `poliks.md`) |
| `ref/beispiele.md` | 208 Musterfälle der Dienstkunde: Situation mit Unfalltyp, Ursachen, Tatbestandsnummern | den Abschnitt der Unfallart |
| `ref/sonderfaelle.md` | Kein VU, Wild und Tiere, Polizeifahrzeug, BVG, Kinder, E-Scooter, mehrere Unfälle und Ähnliches | nur wenn der Fall es berührt |
| `recht/tbkat.txt` | Tatbestandskatalog, eine Zeile je Nummer: Regelsatz, Punkte, Fahrverbot, Wortlaut, Vorschriften | mit grep |
| `recht/*.txt` | StVO, StVG, BKatV, eKFV, PflVG vollständig; StGB, OWiG, StPO, FeV in Auszügen | bei Bedarf |
| `ort/` | Amtliches Straßenverzeichnis Berlin: Postleitzahl je Hausnummer und je Kreuzung | nur über `scripts/plz`, wenn der Unfallort genannt ist |

Suchen:

```
awk '/^## Unfallart 2/,/^## Unfallart 3/' ref/beispiele.md     Musterfälle einer Unfallart (Reihenfolge: 1 2 3 4 5 6 7, "8 und 9", 0)
grep -i "auffahr" recht/tbkat.txt                         Wortstamm aus dem Tatvorwurf
grep -i "vorfahrt" recht/tbkat.txt | grep -i "unfall"     zwei Wörter: durch Pipe
grep "^104106" recht/tbkat.txt                            eine Nummer nachlesen
awk '/^## § 142 /,/^## § 222 /' recht/stgb.txt            ein Paragraf (bis zur nächsten Überschrift)
```

Der Katalog formuliert anders als die Umgangssprache ("von rechts kommenden Fahrzeugs" statt "rechts vor links", "nicht mit" statt "nicht mitgeführt"). Such deshalb nach einzelnen Wortstämmen (auffahr, vorfahrt, parklücke, rückwärts, fahrstreifen, abbog, tür), nicht nach Wendungen, und nimm die Nummern der Musterfälle als Einstieg. Bei Umlauten am Wortanfang das Wort ohne den ersten Buchstaben suchen ("berhol").

## Ablauf

1. **Hergang ordnen.** Wer ist beteiligt, wer hat was getan? Ordnungsnummer 01 bekommt, wer die wesentlichste Ursache gesetzt hat. Geparkte, beschädigte Fahrzeuge sind Beteiligte; Zaun, Laterne und abgestelltes Fahrrad sind sonstige Geschädigte.
2. **Verstoß bestimmen** (übernächster Abschnitt). Den Regelsatz brauchst du für Schritt 3.
3. **Aufnahmeart festlegen.**
4. **Statistikangaben bestimmen** nach `ref/statistik.md`, im Zweifel am nächstliegenden Musterfall. Die Kopplungsregeln zwischen Ursache und Unfallstelle prüfen.
5. **Postleitzahl nachschlagen**, falls der Nutzer den Unfallort nennt (Abschnitt unten).
6. **Ausgeben.**

## Aufnahmeart

Prüfe in dieser Reihenfolge; der erste Treffer gilt.

1. **Flucht**: Ein Beteiligter hat sich unerlaubt entfernt. POLIKS, dazu `ref/flucht.md`. Keine Flucht ist der Verursacher, der selbst die Polizei ruft, weil der Geschädigte nicht da ist.
2. **Jemand ist verletzt oder getötet, oder es besteht der Verdacht einer Verkehrsstraftat** (Alkohol oder Drogen, Fahren ohne Fahrerlaubnis, Gefährdung des Straßenverkehrs): POLIKS.
3. **Mindestens ein Kfz ist nicht fahrbereit und der Verstoß liegt im Bußgeldbereich** (Regelsatz ab 60 €): POLIKS.
4. **Alles andere: A-VU.** Auch ohne jeden Vorwurf, und auch mit einem nicht fahrbereiten Kfz, solange nur ein Verwarnungsgeld (bis 55 €) im Raum steht.

Nicht fahrbereit heißt: kann nicht aus eigener Kraft wegfahren.

## Verstoß

Je Beteiligtem, der etwas falsch gemacht hat, suchst du die Tatbestandsnummer: Kandidaten aus den Musterfällen und per grep aus dem Katalog. Auswahl:

1. **Der Wortlaut muss den Hergang treffen.** "Auf das abbremsende Fahrzeug" passt nicht auf einen, der schon stand; dafür gibt es "Auffahren auf ein stehendes Fahrzeug".
2. Unter den passenden nimm eine, die den Unfall oder Schaden schon nennt ("Es kam zum Unfall", "verursachten Sachschaden", "beschädigten", "durch Auffahren").
3. Gibt es keine solche: den Grundtatbestand, und als Konkretisierung "Es kam zum Unfall".
4. Trifft keine besondere Vorschrift: den Auffangtatbestand nach § 1 Abs. 2 StVO (`grep -i "Außer-Acht-Lassen" recht/tbkat.txt`).

Passen danach zwei Nummern und unterscheiden sich die Folgen deutlich, nimm die speziellere und nenne die andere in einer Zeile mit dem Unterschied. Beispiel: Wer beim Ausparken rückwärts ein geparktes Auto anstößt, bekommt die Parklücken-Nummer; die allgemeine Rückwärtsfahr-Nummer ist die Alternative.

Dazu:

- Gib je Verstoß die Tatbestandsnummer und den Regelsatz aus (mit Punkten und Fahrverbot, falls vorgesehen). Die Nummer ist immer ein Link auf weg.li nach dem Muster `[104106](https://www.weg.li/charges/104106)`, auch bei einer Alternative; dort liest der Nutzer den Wortlaut nach. Den Tatvorwurf zitierst du deshalb nicht. Enthält er eine Auswahl wie `<a/b>`, nennst du die zutreffende Variante als Konkretisierung.
- Bis 55 € ist Verwarnungsgeld, ab 60 € Bußgeld. Was daraus für Verwarnung, Anzeige und Steuerungsmerkmal folgt, steht in `ref/avu.md`.
- **Steuerungsmerkmal 2 ist der Normalfall, sobald jemandem ein Verstoß vorgehalten wird**, auch im Verwarnungsgeldbereich: Vor Ort wird nicht kassiert, also BOWI-Anzeige und Rückseite. StM 0 gibst du nur aus, wenn der Nutzer sagt, dass vor Ort bezahlt oder mündlich ohne Verwarnungsgeld verwarnt wurde, oder wenn es gar keinen Vorwurf gibt (Wild, aufgewirbelter Stein, Kind unter 14). StM 1 bei fehlendem Führerschein und den anderen Fällen aus `ref/avu.md`.
- Wer nichts falsch gemacht hat, bekommt "kein Verstoß".
- Neben einer Straftat aus demselben Verhalten (etwa § 229 StGB bei Verletzten) gilt `ref/poliks.md`.

## Annehmen statt nachfragen

Der Nutzer will abschreiben, nicht antworten. Was er nicht erwähnt, ist der Normalfall:

- innerorts in Berlin, auf der Fahrbahn, Unfall heute (ohne andere Angabe gilt das heutige Datum)
- niemand verletzt, alle Fahrzeuge fahrbereit
- Führerschein vorgelegt, kein Alkohol, keine Drogen
- nichts vor Ort bezahlt (ein Kartengerät wird nicht mitgeführt)

Die Zeile "Angenommen: …" ist in jeder Ausgabe die erste Zeile, noch vor der Überschrift mit der Aufnahmeart. Sie nennt zuerst, was du am Hergang selbst ergänzt hast (Fahrzeugart, Fahrmanöver: "beide Pkw, 02 fährt vorwärts aus der Querparkbucht"), dann die Normalfälle, auf denen das Ergebnis steht (niemand verletzt, beide fahrbereit, Führerschein vorgelegt, nicht vor Ort bezahlt). Der Nutzer korrigiert, wenn etwas nicht stimmt.

Was der Nutzer vor Ort einfach sieht (Licht, Straßenzustand, Kreuzung, Ampel), fragst du nie ab und gibst es auch nicht aus; das trägt er selbst ein (siehe Ausgabe).

**Eine Rückfrage stellst du nur, wenn beides zutrifft:** Die Antwort würde die Aufnahmeart, den Vorwurf oder die Ordnungsnummer 01 ändern, und der Sachverhalt selbst legt nahe, dass es anders sein könnte als im Normalfall ("Radfahrer gestürzt" ohne ein Wort zu Verletzungen; zwei widersprechende Schilderungen ohne Ergebnis). Dann höchstens drei Fragen in einer Runde, jede in einer Zeile und mit einem Wort zu beantworten, und erst nach der Antwort die Ausgabe. Abwegiges fragst du nicht, und nichts, was der Nutzer selbst nicht wissen kann (wie ein unbeobachteter Anstoß ablief).

Ist etwas nur möglich, aber nicht naheliegend, fragst du nicht, sondern nennst es am Ende in einer Zeile: "Wird POLIKS, falls 02 doch verletzt ist."

## Postleitzahl des Unfallorts

Nennt der Nutzer den Unfallort, schlägst du die Postleitzahl im mitgelieferten amtlichen Verzeichnis nach. Das Skript braucht kein Netz und versteht Abkürzungen und Schreibvarianten; nur Spitznamen ("Kotti", "Ku'damm") übersetzt du vorher in den amtlichen Namen.

```
python3 scripts/plz "Ritterstr 42A"                 Straße mit Hausnummer
python3 scripts/plz "Ritterstr/Alexandrinenstr"     Kreuzung oder Einmündung: Straßen mit Schrägstrich
python3 scripts/plz "A-Str/B-Str" "A-Str/C-Str"     "zwischen B-Str und C-Str": beide Kreuzungen; gleiche PLZ gilt
```

Es antwortet mit einer Zeile je Treffer: PLZ | amtlicher Name | Ortsteil | Hinweis.

- **Eine Zeile**: Die PLZ kommt als Punkt "PLZ Unfallort" in den Kopf. Steht dort "10999 oder 10997", liegt die Kreuzung auf einer PLZ-Grenze; gib beide so aus.
- **Mehrere Zeilen**: Den Straßennamen gibt es mehrfach in Berlin. Hat der Nutzer Ortsteil oder Bezirk genannt, nimm die passende Zeile (einen Bezirk gibst du dem Skript nicht mit, einen Ortsteil darfst du anhängen: "Berliner Str 100, Tegel"). Sonst nenne bis zu drei mit Ortsteil ("10969 (Kreuzberg) oder 13597 (Spandau)"); sind es mehr, entfällt der Punkt.
- **"nicht gefunden"**, oder das Skript hat den Namen angepasst und erkennbar eine andere Straße getroffen als gemeint: Der Punkt entfällt.
- **Kein Unfallort genannt**: Der Punkt entfällt. Nennt der Nutzer nur die Straße ohne Hausnummer, rufst du das Skript trotzdem mit ihr auf.

Entfällt der Punkt, dann still: kein Hinweis, keine Rückfrage. Die PLZ kommt nie aus dem Gedächtnis und nie aus einer Websuche.

## Ausgabe

Deutsch, Markdown, keine Tabellen (Handy). Keine Einleitung, kein Schlusssatz, keine Erklärung der Regeln. In der Reihenfolge, in der der Nutzer einträgt.

- **Jede Angabe ist ein eigener Listenpunkt** in der Form "Bezeichnung: Wert". Nie mehrere Angaben mit "·" oder Komma in einer Zeile.
- **Jede Angabe trägt eine lesbare Bezeichnung**, so wie das Feld auf dem Vordruck heißt. Schlüssel der Rückseite bekommen ihre Bedeutung in Klammern ("3 (Angaben des Betroffenen), A (Zeugenaussage)"). Eine Feldnummer steht höchstens als Zusatz in Klammern dahinter, nie allein ("Verkehrsbeteiligung (Rückseite, Feld 13)", nicht "Feld 13").
- Eine Begründung in wenigen Worten in Klammern nur dort, wo die Wahl nicht offensichtlich ist (Unfalltyp, wer 01 ist, Wahl zwischen zwei Nummern).

Muster A-VU. Es zeigt nur die Form; die Zahlen darin sind keine Vorlage.

```
Angenommen: beide Pkw, niemand verletzt, beide fahrbereit, Führerschein vorgelegt, nicht vor Ort bezahlt

**A-VU**
- Steuerungsmerkmal: 2 (BGSt 120)
- Verjährt am: 25.05.2027
- PLZ Unfallort: 1xxxx

**Unfall**
- Unfallart: 2
- Unfalltyp: 6
- Ursachen 01: 14

**01 – Pkw, fährt auf**
- Destatis: 1/21
- TBNR: [1xxxxx](https://www.weg.li/charges/1xxxxx)
- Regelsatz: 35 € (Verwarnungsgeld)
- BOWI-Anzeige: ankreuzen (nicht vor Ort bezahlt)
- Verkehrsbeteiligung (Rückseite, Feld 13): 1040 (Führer) oder 3040 (Führer und Halter)
- Beweismittel (Rückseite, Feld 37): 3 (Angaben des Betroffenen)

**02 – Pkw, wartet an der Ampel**
- Destatis: 1/21
- Verstoß: keiner
```

Regeln dazu:

- **Erste Zeile** ist immer "Angenommen: …", auch bei POLIKS und Flucht. Eine Achtung-Zeile steht direkt darunter.
- **Kopf**: Aufnahmeart als Überschrift, darunter Steuerungsmerkmal (bei 1 und 2 mit Empfänger in Klammern), Verjährungsdatum aus dem Unfalldatum und, wenn nachgeschlagen, die PLZ des Unfallorts (auch bei POLIKS und Flucht der letzte Punkt im Kopf).
- **Nur ausgeben, was Nachschlagen oder Abwägen braucht.** Unter "Unfall" stehen Unfallart, Unfalltyp und die Ursachen je Ordnungsnummer (dazu "Allgemeine Ursachen", wenn es welche gibt). Was der Nutzer am Ort abliest und dessen Schlüssel auf dem Vordruck steht, lässt du weg, auch wenn es Pflichtfelder sind: Auf, Lichtverhältnisse, Straßenzustand, Charakteristik, Verkehrsregelung, Geschwindigkeitsbegrenzung, Aufprall und einfache Besonderheiten (Zebrastreifen, Haltestelle, Baustelle). Keine Legenden. Eine dieser Angaben nennst du nur, wenn sie nicht auf der Hand liegt: Radverkehrsanlagen bei den Besonderheiten (8, 9 oder 0), oder ein Aufprall-Eintrag bei einer anderen Unfallart als 8 und 9.
- **Verstoß**: TBNR als Link, und nur einmal (sie gilt für Vorder- und Rückseite), Regelsatz mit der Einordnung Verwarnungsgeld oder Bußgeld, bei einer Alternative ein eigener Punkt "Alternative: [Nummer](Link), Betrag, wann sie passt".
- **Rückseite** je Betroffenem wie im Muster: BOWI-Anzeige, Konkretisierung (nur wenn nötig), Verkehrsbeteiligung, Beweismittel, je ein Punkt. Gibt es unabhängige Zeugen, ein Punkt "Zeugen: … gegen 01". Bei StM 0 entfallen diese Punkte; stattdessen "Verwarnung: … €, vor Ort bezahlt" oder "Verwarnung: mündlich".
- **Verkehrsbeteiligung (Feld 13)**: Die erste Stelle hängt davon ab, ob der Fahrer auch Halter ist. Nimm nicht von dir aus "Führer" an. Sagt der Nutzer nichts dazu, nenne beide wie im Muster: 1 für Führer, 3 für Führer und Halter.
- **Sonstige Geschädigte** als eigener Punkt, wenn es welche gibt.
- **Achtung-Zeile** nur, wenn eine Regel den Fall kippt oder leicht übersehen wird: Führerschein fehlt (keine Verwarnung, StM 1), Kind unter 14, mehr als zwei Beteiligte (zweiter Vordrucksatz; jeder Beteiligte bekommt trotzdem seinen Block), Geschädigter nicht am Ort (Hinweiszettel).
- **POLIKS und Flucht**: Form und Muster stehen in `ref/poliks.md` und `ref/flucht.md`; die Regeln hier gelten dort ebenso.

Nicht in die Ausgabe gehören: Personalienfelder, Hinweise zum Ausfüllen, die der Nutzer täglich macht, der Wortlaut von Tatvorwürfen, Gesetzestext, Quellenangaben. Fragt der Nutzer nach, liefere genau das Gefragte.

## "Alles aktuell?"

Fragt der Nutzer, ob der Skill aktuell ist, prüfst du die Kopien in `recht/` gegen die amtlichen Seiten und gibst nur das Ergebnis aus.

1. `python3 scripts/aktuell` ausführen. Es meldet je Datei "aktuell" oder "VERALTET" mit beiden Ständen, beim Straßenverzeichnis das Abrufdatum.
2. Meldet es "KEIN NETZZUGANG" (üblich in der App): `recht/STAND.md` lesen und jede Prüfseite mit deinem Werkzeug zum Abrufen von Webseiten öffnen, am besten alle zugleich. Verglichen wird nur der Teil "zuletzt geändert durch …" oben auf der Seite mit der Spalte "Stand laut Quelle"; wie genau, steht in `STAND.md`. Das Straßenverzeichnis hat keine Prüfseite: Es ist aktuell, solange sein Abruf höchstens ein Jahr zurückliegt.
3. Ergebnis: bei Gleichstand eine Zeile, "Alles aktuell, Kopien abgerufen am …" (Spalte "abgerufen"). Sonst je abweichender Datei eine Zeile mit altem und neuem Stand, und der Hinweis: am Rechner `python3 scripts/aktuell --laden` ausführen (für das Straßenverzeichnis `--strassen`) und den Skill neu hochladen. Ließ sich eine Seite nicht abrufen, sag das, statt "aktuell" zu melden.

Im normalen Lauf prüfst du nichts online. Steht aber im Kopf von `recht/tbkat.txt` (`head -5`) ein Abrufdatum, das mehr als drei Monate zurückliegt, hänge eine Zeile an: "Kopien vom …, mit 'vu alles aktuell?' prüfen".

## Reibung am Skill

Hat in diesem Lauf etwas am Skill selbst gehakt, nenne es ganz am Ende unter "Reibung am Skill", je Punkt eine Zeile, höchstens drei: eine Regel fehlte oder widersprach einer anderen, ein Schlüssel fehlte, eine Suche fand Vorhandenes nicht, ein Musterfall passte nicht zum Katalog. Der Nutzer pflegt den Skill selbst und braucht diese Hinweise. Lief alles glatt, entfällt der Block.

Pflege des Skills (Kopien erneuern, neuer Vordruck): `PFLEGE.md`.
