---
name: tatbestand
description: Prüft einen polizeilichen Sachverhalt aus Berlin auf Straftaten und Ordnungswidrigkeiten, je Beteiligtem, mit Norm, Merkmalen und bei Verkehrsverstößen TBNR und Regelsatz. Verwenden bei "tatbestand" oder wenn der Nutzer einen Sachverhalt schildert und wissen will, was vorliegt.
---

# Tatbestand

Beantworte: **Welche Straftaten und Ordnungswidrigkeiten liegen nach diesem Sachverhalt vor, bei wem, und warum?**

Der Nutzer ist Polizeibeamter in Berlin und nutzt das Ergebnis als Arbeitshilfe für Anzeige und Bericht. Ein falscher Paragraf oder ein erfundener Betrag landet in einem Vorgang gegen einen echten Menschen. Deshalb gilt: lieber "konnte ich nicht verifizieren" als eine plausibel klingende Angabe.

## Zwei feste Regeln

**Nichts aus dem Gedächtnis.** Jede Norm, jede Tatbestandsnummer, jeder Betrag, jeder Strafrahmen und jede Entscheidung, die im Ergebnis steht, wurde in dieser Sitzung in der Quelle nachgelesen. Dein Wissen dient nur dazu, Kandidaten zu finden. Gesetze ändern sich (Beispiele der letzten Jahre: Cannabis, Messerverbote, Bußgeldkatalog), und Paragrafen, Absätze und Nummern verrutschen dabei. Was sich nicht nachlesen ließ, wird als **nicht verifiziert** gekennzeichnet oder weggelassen.

**Keine Personendaten.** Enthält der Sachverhalt Klarnamen, Geburtsdaten, Anschriften, Kennzeichen oder Vorgangsnummern, übernimm sie nicht in Suchanfragen, Subagenten-Aufträge oder die Ausgabe. Ersetze sie durch T1, T2 (Tatverdächtige), G1 (Geschädigte), Z1 (Zeugen) und weise den Nutzer einmal kurz darauf hin, Sachverhalte künftig anonymisiert einzugeben, als erste Zeile deiner ersten Antwort. Alter und Tatort (Straße, Platz, Park) sind keine Personendaten in diesem Sinn: Du brauchst sie für die Einordnung und behältst sie.

## 1. Sachverhalt aufnehmen

Zerlege den Sachverhalt in Beteiligte und einzelne Handlungen in zeitlicher Reihenfolge. Halte fest, was für die rechtliche Einordnung zählt: Ort (öffentlicher Verkehrsraum, Wohnung, Grünanlage, Verbotszone), Zeit, Alter der Beteiligten, Tatmittel, Folgen (Verletzung, Schadenshöhe), Alkohol- und Drogenwerte, Fahrzeugart, vorhandene Erlaubnisse. Rechne relative Zeitangaben ("gestern") in ein Datum um.

Arbeite nur mit dem, was geschildert ist. Unterstelle keine Tatsachen, auch keine naheliegenden.

## 2. Rückfragen

Rückfragen sind das Mittel, um Verstöße sicher in A (vorliegend) oder C (nicht) einzuordnen, statt sie in B (fraglich) stehen zu lassen. Frage deshalb, sobald eine Tatsache, die der Nutzer vermutlich kennt, einen Kandidaten entscheidet. Ist nach dem Sachverhalt alles klar, frage nichts.

Eine Runde, höchstens fünf Fragen, jede in einer Zeile und mit wenigen Worten zu beantworten ("Uhrzeit?", "Verletzung sichtbar, ja/nein?"). Zuerst die Fragen, an denen mehrere Einträge oder ein Verbrechen hängen (etwa: Höchstgeschwindigkeit des Fahrzeugs, Fahrerlaubnis vorhanden, Schlag vor oder wegen der Wegnahme). Stelle die Fragen, sobald du weißt, woran es hängt: nach Schritt 3, spätestens wenn der gelesene Wortlaut zeigt, welche Ausnahme oder Ortstatsache entscheidet (Messer zugriffsbereit, Fläche als Grillplatz oder Hundeauslauf ausgewiesen). Dann warte auf die Antwort: Die Ausgabe kommt erst danach. Antwortet der Nutzer nicht oder nur teilweise, frage kein zweites Mal: Was offen bleibt, kommt in B.

## 3. Kandidaten sammeln

Sammle breit, bevor du prüfst. Gehe für jede Handlung jedes Beteiligten durch:

- **StGB**, einschließlich Versuch, Qualifikationen, Regelbeispiele, Beteiligung (Mittäterschaft, Anstiftung, Beihilfe), Unterlassen.
- **Nebenstrafrecht**: etwa StVG, PflVG, BtMG, KCanG, WaffG, SprengG, AufenthG, AsylG, TierSchG, GewSchG, VersFG BE, AO, UrhG, KunstUrhG.
- **Ordnungswidrigkeiten nach Bundesrecht**: OWiG (§§ 111 ff.), StVO, StVZO, FeV, FZV, eKFV, WaffG, KCanG, JuSchG, GewO, GastG.
- **Berliner Landesrecht**, mit den Abkürzungen, die `berlin` versteht: ASOG Bln, LImSchG Bln, StrReinG, GrünanlG, BerlStrG, HundeG, NRSG, VersFG BE, WaffFVerbotV BE 2025 (Waffen- und Messerverbotszonen), WaffÖPNVVerbotV BE (Bahnen, Busse, Bahnhöfe). Berlin weicht hier oft von anderen Ländern ab, deshalb nie Regelungen anderer Länder übertragen.

Die Listen sind Gedankenstützen, nicht abschließend. Nimm auch Tatbestände auf, an die man bei diesem Sachverhalt sofort denkt, die aber wahrscheinlich nicht erfüllt sind. Sie werden für Block C gebraucht.

## 4. Nachlesen

Lies jeden Kandidaten im geltenden Wortlaut nach, bevor du subsumierst. Maßgeblich ist das Recht zur Tatzeit; nennt der Sachverhalt keine, gilt heute.

Die Skripte `norm`, `berlin` und `tbnr` liegen im Ordner `scripts/` neben dieser Datei. Rufe sie immer mit absolutem Pfad auf, gebildet aus dem Verzeichnis dieses Skills. Die Beispiele unten kürzen den Pfad ab.

### Bundesrecht

Nutze `norm`. Es holt Wortlaut und Stand von gesetze-im-internet.de:

```
scripts/norm StGB 223 224      Stand und Wortlaut der Paragrafen
scripts/norm StVO              Stand und Inhaltsverzeichnis
scripts/norm StVO anlage_2 --finde Gehweg    nur die Stellen mit diesem Wort
scripts/norm --suche cannabis  Gesetz finden, wenn die Abkürzung unklar ist
scripts/norm --bgbl 2026 321 7  Artikel 7 aus BGBl. 2026 I Nr. 321, samt Inkrafttreten
```

Lies ein Gesetz in einem Aufruf mit allen Paragrafen, die du brauchst. Bei langen Paragrafen und Anlagen grenzt `--finde WORT` auf die Fundstellen ein; mehrere Wörter müssen alle in derselben Zeile stehen.

Lies die Stand-Zeilen mit. Zwei Hinweise sehen ähnlich aus und bedeuten Verschiedenes:

- **"textlich nachgewiesen, dokumentarisch noch nicht abschließend bearbeitet"** oder **"ist berücksichtigt"**: Die Änderung steht schon im Text. Nichts weiter zu tun, keine Kennzeichnung.
- **"noch nicht berücksichtigt"**: Die Änderung fehlt im Text. Lies den genannten Artikel im Bundesgesetzblatt nach, etwa bei "Art. 7 G v. 22.10.2026 I Nr. 321" mit `norm --bgbl 2026 321 7`. Fasst der Artikel keinen der Paragrafen an, die du verwendest, ist die Sache erledigt und es gibt keine Kennzeichnung. Ändert er einen davon, gilt ab dem Inkrafttreten der Wortlaut aus dem Bundesgesetzblatt. Lässt sich die Fundstelle nicht abrufen (vor 2023), bekommt die Norm ein ⚠.

Drei Meldungen des Skripts:

- **NICHT GEFUNDEN**: Der Paragraf wurde aufgehoben oder umnummeriert. Suche im Inhaltsverzeichnis, statt die alte Nummer zu verwenden.
- Der Paragraf existiert, regelt aber etwas anderes als erwartet: Auch dann ist umnummeriert worden. Suche Straf- und Bußgeldvorschriften eines Nebengesetzes immer über das Inhaltsverzeichnis.
- **ABRUF FEHLGESCHLAGEN**: Die Seite antwortet nicht. Einmal später wiederholen; bleibt es dabei, gilt die Norm als nicht gelesen.

### Verkehrsordnungswidrigkeiten

| Was | Quelle |
|---|---|
| Regelsatz, Fahrverbot | `scripts/norm BKatV anlage --finde Wechsellicht` (Wort aus dem Tatvorwurf) oder `--finde 132` (laufende Nummer) |
| Punkte | `scripts/norm FeV anlage_13 --finde 132` (maßgeblich ist die Zeile, die genau deine BKat-Nummer nennt; steht sie nirgends, gibt es keinen Punkt. Bei Geschwindigkeit und Abstand nennt die Anlage Bereiche wie "11.1.6 bis 11.1.10": dort mit `--finde Geschwindigkeit` suchen) |
| Tatbestandsnummer | `scripts/tbnr bkat:132.3 bkat:241 "Gurt nicht angelegt"` |

Der Bußgeldkatalog ist zu groß, um ihn ganz zu lesen; `--finde` liefert den Nummernblock mit allen Unterfällen (mit Gefährdung, mit Sachbeschädigung, Überschreitungsstufe). Nimm den Unterfall, dessen Text den Sachverhalt genau trifft. Passen mehrere oder keiner genau, nenne die Kandidaten und den Unterschied, statt zu raten.

Vier Tabellen stehen nicht in der Anlage, sondern je auf einer eigenen Seite:

| Seite | Inhalt |
|---|---|
| `norm BKatV anhang` | Tabelle 1: Geschwindigkeit (`--finde 11.3.6`) |
| `norm BKatV anhang_1` | Tabelle 2: Abstand |
| `norm BKatV anhang_2` | Tabelle 3: Achslast und Gesamtgewicht |
| `norm BKatV anhang_3` | Tabelle 4: Erhöhung bei Gefährdung oder Sachbeschädigung |

Tabelle 4 brauchst du, sobald zu einem Verstoß mit Regelsatz über 55 € eine Gefährdung oder Sachbeschädigung hinzutritt, die der Katalog nicht als eigenen Unterfall führt (§ 3 Abs. 3 BKatV): Suche dort die Zeile mit dem Regelsatz (`--finde 80`) und nimm den erhöhten Betrag. `tbnr` zeigt in solchen Fällen schon den erhöhten Betrag; das ist dann keine Abweichung.

Die Regelsätze in Abschnitt I gelten für fahrlässige Begehung und gewöhnliche Umstände. Ohne Anhaltspunkt für Vorsatz gibst du diesen Satz aus. Liegt Vorsatz nahe (bewusst missachtetes Haltgebot), lies § 3 BKatV nach und nenne den erhöhten Satz als Zusatzzeile. Abschnitt II des Katalogs (etwa Handy) ist schon für Vorsatz bemessen und wird nicht erhöht.

`tbnr` lädt bei jedem Aufruf die aktuelle Datenbank zum Tatbestandskatalog von kba.de und gibt deren Stand aus. Lege alle Suchen eines Sachverhalts in einen einzigen Aufruf: kba.de sperrt Adressen, die zu oft abrufen, und rufe kba.de nie auf anderem Weg ab. Suche zuerst über die BKat-Nummer (`bkat:132.3`); Verstöße ohne Eintrag im Bußgeldkatalog findest du über Wörter aus dem Tatvorwurf. Liefert eine Nummer viele Einträge (Geschwindigkeit), nimm den, dessen Text den Sachverhalt trifft; passen zwei, nenne beide mit dem Unterschied. Liegt die Tatzeit zurück, setze `--datum TT.MM.JJJJ` davor.

Betrag, Punkte und Fahrverbot kommen aus `norm`; `tbnr` zeigt sie nur zum Abgleich. Weichen sie ab, ist die Datenbank älter als die Verordnung: Die TBNR bekommt ein ⚠. Einzige Ausnahme: Hat der Verstoß keinen Eintrag im Bußgeldkatalog (`tbnr` zeigt "BKat --"), nenne den Betrag aus der Datenbank mit dem Zusatz "laut TBKat".

Meldet `tbnr` "ABRUF FEHLGESCHLAGEN", wiederhole nicht. Die laufende Nummer des Bußgeldkatalogs steht ohnehin in der Ausgabe. Die TBNR suchst du dann per Websuche (BKat-Nummer oder Tatvorwurf plus "Tatbestandsnummer") und übernimmst sie nur, wenn die Seite denselben Tatvorwurf und denselben Regelsatz nennt wie der Bußgeldkatalog, mit ⚠ samt Quelle und Datum. Sonst steht dort "TBNR ⚠ nicht gefunden".

### Berliner Landesrecht

Nutze `berlin`. Es holt die heute gültige Fassung mit Stand von gesetze.berlin.de, der amtlichen Sammlung:

```
scripts/berlin --suche Hund Leine     Vorschriften und Paragrafen, in denen die Wörter stehen
scripts/berlin "LImSchG Bln"          Stand und Inhaltsverzeichnis
scripts/berlin "LImSchG Bln" 3 20     Stand und Wortlaut der Paragrafen
scripts/berlin HundeG 33 --finde Leine   nur die Zeilen mit diesem Wort (lange Bußgeldparagrafen)
scripts/berlin "WaffFVerbotV BE 2025" "Anlage 1"    Anlage, etwa die Gebiete einer Verbotszone
```

Das funktioniert für Gesetze und Verordnungen des Landes gleichermaßen. `--suche` ist eine Volltextsuche im geltenden Landesrecht: Suche mit einzelnen Wörtern, wie sie im Normtext stehen ("Messer", nicht "Messerverbotszone"). Achte in der Ausgabe auf:

- **Stand** der Vorschrift ("letzte berücksichtigte Änderung").
- **Gültig bis** und **Weitere Fassungen dieser Norm** beim einzelnen Paragrafen: Dort steht, ob eine geänderte Fassung schon verkündet ist und ab wann sie gilt. Liegt die Tatzeit nach diesem Datum, gilt die neue Fassung. Das Inhaltsverzeichnis zeigt die heutige Fassung, auch wenn die Stand-Zeile schon eine künftige Änderung nennt. Liegt die Tatzeit vor "Gültig ab", galt eine ältere Fassung, die das Skript nicht holt: Der Eintrag bekommt ein ⚠.
- **NICHT GEFUNDEN**: Der Paragraf ist aufgehoben, umnummeriert oder noch nicht in Kraft. Rufe das Inhaltsverzeichnis auf, statt die alte Nummer zu verwenden.
- **Hinweis auf fehlende Karten**: Ob ein Ort in einer Zone liegt, entscheidest du nach der Textbeschreibung der Anlage. Trägt sie das nicht eindeutig, ist die Zone eine offene Tatsache (Rückfrage oder B). Dasselbe gilt für alles, was nur vor Ort feststeht und in keinem Gesetz steht: Widmung als Grünanlage, ausgewiesene Flächen, Beschilderung.

Verbotszonen können auch außerhalb dieser Sammlung angeordnet sein (Allgemeinverfügungen, etwa der Bundespolizei für Bahnhöfe). Findest du keine Verordnung, heißt das nur, dass keine Landesverordnung den Ort erfasst.

Rufe nur ab, was der Sachverhalt braucht, und jeden Paragrafen nur einmal. Die Seite ist kein Massenabruf-Dienst. Bußgeldhöhen nach Landesrecht stehen in Verwaltungskatalogen außerhalb der Sammlung; suche sie nur auf Nachfrage.

Meldet das Skript "ABRUF FEHLGESCHLAGEN", versuche es nicht weiter und nimm den Ausweichweg:

1. **Gesetz- und Verordnungsblatt (GVBl.)** im Archiv des Abgeordnetenhauses, pardok.parlament-berlin.de, per Websuche ("GVBl Berlin" + Gesetzesname). Amtlicher Wortlaut, aber nur zum Tag der Verkündung.
2. **Behördenseiten auf berlin.de**: Lesefassungen, Ausführungsvorschriften, Bußgeldkataloge, nur mit erkennbarem Stand-Datum.
3. Suche gezielt nach späteren Änderungen. Bleibt die Aktualität offen, kennzeichne die Norm (siehe Abschnitt 5) und bitte den Nutzer, den Paragrafen auf gesetze.berlin.de selbst aufzurufen und einzufügen.

Frei zugängliche Kopien anderer Anbieter (etwa lexaris.de) sind teils seit Jahren nicht gepflegt und zeigen aufgehobene Fassungen. Verwende sie nicht als Beleg.

### Auslegung und Rechtsprechung

Quellen sind dejure.org, openjur.de und die Seiten der Gerichte (BGH, KG Berlin, BVerfG). Zitiere eine Entscheidung nur mit Gericht, Datum und Aktenzeichen und nur, wenn du sie selbst aufgerufen hast.

Kommentare (Fischer, MüKo, Schönke/Schröder, Hentschel) liegen hinter Bezahlschranken und sind nicht abrufbar. Zitiere sie deshalb nicht.

### Welche Quelle als Beleg zählt

- **Beleg**: Gesetzestext aus den Quellen oben, amtliche Kataloge, selbst gelesene Entscheidungen.
- **Notbehelf mit Kennzeichnung**: Seiten von Behörden, die eine Norm wiedergeben oder erläutern (Senatsverwaltung, Bezirksamt, Polizei Berlin). Gib an, dass es eine Sekundärquelle ist, und nenne ihr Datum.
- **Nur zum Finden**: Anwaltsseiten, Bußgeldrechner, Verlagsseiten, Foren.

### Subagenten

Gesetzestext liest du selbst nach: Die Skripte antworten in Sekunden, und ein Subagent, der Wortlaut zurückreicht, kostet nur doppelt. Starte Subagenten für Recherche, die viele Schritte braucht, und zwar gleichzeitig: Rechtsprechung zu einer tragenden Streitfrage, die Suche nach einer Berliner Verordnung, die `--suche` nicht findet, Ausweichquellen. Der Auftrag enthält die konkrete Frage ohne Personendaten, die Quellenregeln aus diesem Abschnitt und die Anweisung, nur selbst Gelesenes mit URL und Datum zurückzugeben.

Ab etwa fünf Einträgen in A lass am Ende einen frischen Subagenten gegenprüfen und warte auf sein Ergebnis, bevor du ausgibst. Er bekommt den anonymisierten Sachverhalt mit Tatzeit, deine fertige Ausgabe, die absoluten Pfade von `norm` und `berlin` mit je einem Beispielaufruf (auch `norm --bgbl`) und die Ausgabe deines `tbnr`-Aufrufs im Wortlaut; `tbnr` ruft er nicht selbst auf. Er prüft jede Paragrafenangabe (Absatz, Nummer), jede Verweiskette zwischen Normen, jede TBNR und jede Zahl gegen die Quelle und meldet nur Abweichungen. Die Kürze der Merkmalszeilen ist gewollt und kein Befund.

## 5. Prüfen

Prüfe jeden Kandidaten je Beteiligtem getrennt, Merkmal für Merkmal am Gesetzestext:

- Objektiver Tatbestand: jedes Merkmal mit der Tatsache aus dem Sachverhalt, die es erfüllt.
- Subjektiver Tatbestand: Vorsatz, besondere Absichten, bei Fahrlässigkeitsdelikten die Sorgfaltspflichtverletzung. Benenne, woraus sich der Vorsatz ergibt.
- Rechtswidrigkeit und Schuld nur, wenn der Sachverhalt Anlass gibt (Notwehrlage, Einwilligung, Alter unter 14 oder unter 18/21, erhebliche Alkoholisierung).
- Beteiligungsform und Zurechnung bei mehreren Tätern, einschließlich Exzess eines Einzelnen.
- Versuch, Rücktritt, Qualifikation, Regelbeispiel, minder schwerer Fall.
- Konkurrenzen: was verdrängt wird, was nebeneinander steht. Trifft eine Straftat mit einer Ordnungswidrigkeit in derselben Handlung zusammen, gilt § 21 OWiG; bei mehreren Ordnungswidrigkeiten §§ 19, 20 OWiG und im Verkehr § 3 Abs. 5 BKatV. Lies diese Normen nach, wenn du sie anwendest.

Ordne jedes Ergebnis ein:

- **A – Vorliegend**: Jedes Merkmal ist durch eine geschilderte Tatsache belegt.
- **B – Fraglich**: Der Sachverhalt legt den Tatbestand nahe, aber er hängt an einer Tatsache, die nicht geschildert ist und sich durch Rückfragen nicht klären ließ, oder an einer echten Streitfrage. Hierher gehört auch der schwerere Tatbestand, der an einer offenen Tatsache hängt (Raub statt Diebstahl, Straftat statt Ordnungswidrigkeit), selbst wenn er eher nicht vorliegt.
- **C – Nicht**: Ein Tatbestand, an den man bei diesem Sachverhalt sofort denkt, für den aber ein Merkmal fehlt: Es ist widerlegt, oder nichts im Sachverhalt spricht dafür.

Alles andere fällt weg: Fernliegendes erscheint nirgends. C ist keine Liste alles Geprüften, sondern nur für das, was der Nutzer sonst vermissen würde.

Vier Fälle, die immer wieder vorkommen:

- **Ausnahmen und Rechtfertigungen**, für die der Sachverhalt nichts hergibt (berechtigtes Interesse beim Messer, Erlaubnis, Notwehr), hindern A nicht.
- **Grenzwerte und Begriffe aus der Rechtsprechung** (Promillegrenzen, gefährliches Werkzeug, bedeutender Wert): Bei gefestigter Linie bleibt der Verstoß in A. B ist es nur, wenn die Gerichte die Frage für genau diese Konstellation offen gelassen haben oder verschieden entscheiden; dann lies eine Entscheidung dazu oder schreibe "Rspr. nicht gelesen" in die Zeile.
- **Offene Einordnung bei sicherem Verstoß**: Steht fest, dass ein Verstoß vorliegt, aber nicht, nach welcher Norm (E-Scooter oder Kleinkraftrad, je nach Höchstgeschwindigkeit), ist das zuerst eine Rückfrage. Bleibt sie offen, steht der Verstoß einmal in A mit beiden Varianten.
- **Nur behauptete Dritte** (der Halter, "ein Kumpel"): kein eigener A/B/C-Block, sondern eine Zeile, was bei Bestätigung in Betracht kommt.

Die Stufen beschreiben allein die Tatsachenlage. Ob du den Wortlaut gelesen hast, ist eine zweite, getrennte Angabe:

- **Wortlaut gelesen**: Normalfall, keine Kennzeichnung.
- **⚠ Aktualität nicht bestätigt**: Wortlaut gelesen, aber aus einer Quelle mit älterem Stand oder aus einer Sekundärquelle. Der Eintrag bekommt ein ⚠ und am Ende der Ausgabe eine Zeile mit Quelle und Datum.
- **⚠ Wortlaut nicht gelesen**: Die Norm kann nicht in A stehen, höchstens in B, mit ⚠ und einer Zeile am Ende, wo der Nutzer nachlesen kann.

In Block C steht ein ⚠ nur, wenn gerade das fehlende Merkmal von der ungeprüften Fassung abhängen könnte. Sonst bleibt C ohne Kennzeichnung.

## Ausgabe

Auf Deutsch, im Chat. Kurz und knackig: Der Nutzer liest das im Dienst und will das Ergebnis auf einen Blick. Alles Weitere liefert er sich per Nachfrage. Keine Einleitung, keine Zusammenfassung, kein Schlusssatz.

```
T1 (17, Jugendlicher)

A: VORLIEGEND
- Gefährliche Körperverletzung z. N. G1, § 224 Abs. 1 Nr. 2 StGB (Vergehen)
  · körperliche Misshandlung: Schlag ins Gesicht
  · gefährliches Werkzeug: Bierflasche
  · Vorsatz: gezielter Schlag
  + fraglich § 224 Abs. 1 Nr. 4: offen, ob T2 mitwirkte
- Rotlichtverstoß, § 37 Abs. 2, § 49 Abs. 3 Nr. 2 StVO, § 24 StVG
  TBNR … · BKat … · … € · … Punkt(e) · Fahrverbot …
  "Sie missachteten das Rotlicht der Lichtzeichenanlage."
  · Rotlicht missachtet: Haltlinie bei Rot überfahren
- Führen eines Einhandmessers, § 42a Abs. 1 Nr. 3, § 53 Abs. 1 Nr. … WaffG (OWi)
  · geführt: in der Jackentasche, öffentliche Straße

B: FRAGLICH
- Raub, § 249 Abs. 1 StGB (Verbrechen), statt Diebstahl: offen, ob der Schlag der Wegnahme diente

C: NICHT
- Vollrausch, § 323a StGB: kein Anhalt für Schuldunfähigkeit

Tateinheit: Rotlicht und Handy in einer Fahrt, eine Geldbuße nach dem höchsten Regelsatz (§ 19 OWiG, § 3 Abs. 5 BKatV)

T2: nichts
Halter (unbekannt): bei Überlassung § 21 Abs. 1 Nr. 2 StVG

D: REIBUNG
- norm BKatV anhang_1 --finde 12.5: kein Treffer, obwohl die Zeile in der Tabelle steht
```

Das Beispiel zeigt nur die Form. Übernimm daraus keine Normen oder Zahlen.

Regeln für die Form:

- **Ein Eintrag je Verstoß.** Verletzt eine Handlung zwei Vorschriften mit verschiedenen Merkmalen (Hund ohne Leine nach HundeG und nach GrünanlG), sind das zwei Einträge. Kopfzeile mit Bezeichnung und genauer Norm (Absatz, Nummer). Bei Straftaten in Klammern nur, was für die Anzeige zählt: Verbrechen oder Vergehen, Antragsdelikt mit Norm, Versuch. Ordnungswidrigkeiten außerhalb des Verkehrs bekommen "(OWi)". Bei mehreren Geschädigten "z. N. G1".
- **Tatbestandsmerkmale nur in A**, je Merkmal eine Zeile mit wenigen Worten: Merkmal, Doppelpunkt, die Tatsache. Selbstverständliches (etwa "Mensch", "Sache") weglassen.
- **Qualifikation, Regelbeispiel oder weitere Variante desselben Delikts, die offen ist**: kein eigener B-Eintrag, sondern eine Zeile "+ fraglich § …: offen, ob …" am Eintrag in A. Dasselbe für erhöhte Regelsätze (Voreintragung, Vorsatz).
- **B und C: eine Zeile je Eintrag**, bei B die offene Tatsache, bei C das fehlende Merkmal. Keine Merkmalsliste. Eine Verkehrsordnungswidrigkeit in B nennt TBNR, BKat-Nummer und Regelsatz in Klammern, damit der Nutzer sie bei Bestätigung übernehmen kann. Würde ein B-Eintrag einen aus A ersetzen, steht das dabei ("statt Diebstahl").
- **Verkehrsordnungswidrigkeit**: Normenkette, dann in einer Zeile TBNR, BKat-Nummer und Regelsatz, dazu Punkte und Fahrverbot, soweit vorgesehen. Darunter immer der Tatvorwurf aus dem Tatbestandskatalog als Zitat in Anführungszeichen, wortgleich aus der Ausgabe von `tbnr`, etwa "Sie fuhren infolge zu geringen Abstands auf das abbremsende Fahrzeug auf. Es kam zum Unfall." Platzhalter (`#D#`, `*)`) ersetzt du durch die Werte aus dem Sachverhalt, bei Auswahlklammern (`<dem Gehweg/der Fahrbahn>`) nimmst du die zutreffende Variante; sonst änderst du nichts und formulierst nicht selbst. Ohne TBNR entfällt das Zitat. Bei offener Einordnung je Variante TBNR-Zeile und Zitat.
- **Mehrere Verkehrsverstöße in einer Fahrt**: eine Zeile "Tateinheit" nach den Blöcken, damit niemand die Regelsätze addiert. Was in Tatmehrheit steht, nennst du dort ebenfalls.
- **Ordnungswidrigkeit neben Straftat in derselben Handlung**: Die OWi bleibt in A, weil sie in die Anzeige gehört, ohne Regelsatz und ohne Merkmalszeilen. Darunter einmal für alle: "OWi treten hinter § … zurück (§ 21 OWiG)". Ist nicht klar, ob es dieselbe Handlung ist (Messer in der Tasche während einer Bedrohung), bleibt die OWi ein gewöhnlicher Eintrag ohne diese Zeile.
- **Sonstige Konkurrenzen** nur, wenn ein Verstoß aus A verdrängt wird, dann als Zusatz am Eintrag ("tritt hinter § … zurück").
- **Mehrere Beteiligte**: A, B und C je Person, Überschrift "T1", bei unter 21-Jährigen mit Alter und "Jugendlicher" oder "Heranwachsender", bei unter 14-Jährigen "Kind, strafunmündig". Hat jemand nichts verwirklicht, eine Zeile: "T2: nichts".
- **Leere Blöcke weglassen.**
- **⚠-Einträge**: am Ende eine Zeile je Quelle mit Datum oder dem Ort zum Nachlesen. Mehrere Einträge mit derselben Quelle teilen sich die Zeile.
- **Unbeantwortete Rückfragen** stehen nicht noch einmal in der Ausgabe; die offene Tatsache steht in der B-Zeile.

Nicht in die Ausgabe gehören: Strafrahmen, Quellen und Stand, Rechtsprechung, Herleitungen, Hinweise auf weitere Ermittlungen. Du hast das alles geprüft und hältst es bereit.

### D: Reibung

Der Block dient dazu, diesen Skill im Betrieb zu verbessern. Er steht ganz am Ende und nur, wenn in diesem Durchlauf etwas am Skill selbst gehakt hat und sich dort beheben lässt:

- ein Skript stürzte ab, fand etwas Vorhandenes nicht, lieferte Unbrauchbares oder viel zu viel,
- eine Regel in dieser Datei fehlte, widersprach einer anderen oder zwang dich zu raten,
- eine Quelle, auf die der Skill verweist, war nicht erreichbar.

Je Punkt eine Zeile: was genau (bei Skripten der Aufruf), und was daran falsch war. Höchstens fünf Zeilen, das Wichtigste zuerst.

Nicht hierher gehört, was am Sachverhalt liegt oder sich am Skill nicht ändern lässt: offene Tatsachen, unbeantwortete Rückfragen, Streitfragen der Rechtsprechung, Bezahlschranken, eigene Tippfehler, allgemeine Wünsche. Lief alles glatt, entfällt der Block ersatzlos; schreibe dann nicht "keine Reibung".

### Auf Nachfrage

Fragt der Nutzer nach, liefere genau das Gefragte, ebenfalls knapp: Merkmale eines Eintrags aus B oder C, Strafrahmen, Quelle mit Stand, Rechtsprechung, Konkurrenzen, Begründung einer Einordnung. Lies nach, was du dafür noch nicht gelesen hast.
