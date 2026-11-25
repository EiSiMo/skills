# Musterfälle: Unfallart, Unfalltyp, Ursachen, Tatbestandsnummer

208 Standardsituationen aus Anlage 3 der GA PPr St 5/2008 (Dienstkunde der Polizei Berlin), geordnet nach Unfallart.
Nutzung: die Situation suchen, die dem geschilderten Unfall am nächsten kommt, und Typ und Ursachen von dort übernehmen.
Durch Drehen oder Spiegeln einer Situation ergeben sich weitere; rechts und links dann sinngemäß tauschen.

- **Typ** ist der Unfalltyp (1 bis 7), **Ursachen** sind Nummern des Ursachenverzeichnisses in `statistik.md`.
  Sie sind auf das heutige Verzeichnis umgestellt: Wo die Richtung offen ist, steht `34/35` (34 Abbiegen nach rechts,
  35 nach links) oder `08/09/10` (falsche Fahrbahn; siehe Verzeichnis). "72 oder 73" heißt: je nach Wetter.
- **TBNR** sind Kandidaten, geprüft gegen den Tatbestandskatalog vom 08.10.2026. Wortlaut und Regelsatz immer in
  `recht/tbkat.txt` nachlesen (`grep "^104106" recht/tbkat.txt`) und dort auch nach treffenderen Varianten suchen.
  "–" heißt: kein Verstoß vorgesehen oder nichts Passendes im Katalog.
- **Lage** beschreibt die Zeichnung der Anlage in Stichworten. Fz = Fahrzeug, R = Radfahrer, F = Fußgänger, K = Krad,
  M = Moped, LA = Lkw mit Anhänger; 01 und 02 sind Ordnungsnummern.
- Sind zwei Beteiligte genannt (01 und 02), haben beide eine Ursache gesetzt; die Angaben stehen dann in dieser Reihenfolge.

## Unfallart 1: Zusammenstoß mit Fahrzeug, das steht, anfährt oder anhält (ruhender Verkehr)

| Fall | Lage in der Skizze | Typ | Ursachen | TBNR |
|---|---|---|---|---|
| nicht angepasste Geschwindigkeit (besondere Verhältnisse), Kollision mit geparktem Fahrzeug | Fz (Verursacher, schleudert) auf Fz (steht) am rechten Rand | 1 | 13, 72 oder 73 | 101006 |
| nicht angepasste Geschwindigkeit (besondere Verhältnisse), Kollision mit geparktem Fahrzeug, Schleudern | Fz (Verursacher, schleudert) auf Fz (steht) am rechten Rand | 1 | 13, 72 oder 73 | 103602, 103620, 101006 |
| nicht angepasste Geschwindigkeit (Abbiegen, Schleudern), Kollision mit geparktem Fahrzeug | Rechtsabbieger (Verursacher, schleudert) trifft Fz (steht) | 1 | 13, 34, 72 oder 73 | 103620, 101006 |
| Benutzung der falschen Fahrbahn, Kollision mit geparktem Fahrzeug | Fz links auf Gegenfahrbahn gegen Fz (steht) | 5 | 08/09/10 | 101118 |
| Kollision mit einem parkenden Fahrzeug in Folge Nichteinhaltung des seitlichen Abstandes | streift Fz (steht) rechts | 5 | 14 | 101012 |
| unzureichender Sicherheitsabstand, Kollision mit parkendem Fahrzeug, linke Fahrbahnseite | frontal gegen Fz (steht) links | 5 | 14 | 102668 |
| Kollision mit einem parkenden Fahrzeug in Folge Nichteinhaltung des seitlichen Abstandes beim Einbiegen (Grundstücksausfahrt) | aus Grundstück, trifft Fz (steht) | 5 | 14 | 101012 |
| Kollision mit einem parkenden Fahrzeug in Folge Nichteinhaltung des seitlichen Abstandes beim Wenden | Wenden, trifft Fz (steht) | 5 | 14, 36 | 101012 |
| Kollision mit einem parkenden Fahrzeug in Folge Nichteinhaltung des seitlichen Abstandes beim Abbiegen | Linksabbieger trifft Fz (steht) | 5 | 14, 35 | 101012 |
| Kollision mit einem parkenden Fahrzeug in Folge Nichteinhaltung des seitlichen Abstandes beim Abbiegen | Rechtsabbieger trifft Fz (steht) (2×) | 5 | 14, 34 | 101012 |
| Einfahren vom Fahrbahnrand in den Fließverkehr, mit Kollision (2×) | Einfahren vom Rand | 5 | 37 | 110131 |
| Einfahren in den Fließverkehr nach links, bei rechts vor links | Anfahren und links einbiegen | 5 | 37 | 110131 |
| Kollision mit einem anderen Fahrzeug beim unachtsamen Türöffnen durch Fahrerin oder Fahrer oder Insassin und/oder Insasse | Tür, Nachfolger trifft | 5 | 45 | 114106 |
| Verkehrswidriges Verhalten beim Ein- und Aussteigen/Be- u. Entladen (ungesicherte Ladeeinrichtung) | stehendes Fz (Verursacher, steht) | 5 | 45 | 122609, 122603 |
| Kollision mit Fließverkehr beim Einparken | Einparken (rückwärts) | 5 | 36 | 109649 |
| Abfahren von der Haltestelle (Z 224) nicht ermöglicht | Haltestelle Z 224, Bus fährt aus | 5 | 49 | 120192 |
| Kollision beim Vorrang an der Parklücke | zwei Fz an einer Parklücke | 5 | 49 | 112446, 101118 |
| Nichtbeachten der Beleuchtungsvorschriften (Z 630 Park- und Warntafel) | stehendes Fz (Verursacher, steht) | 5 | 46 | 117173, 117179, 117167 |
| Kollision mit einem parkenden Fahrzeug in Folge Nichteinhaltung des Abstandes beim Einparken | vorwärts einparken | 7 | 14 | 101136 |
| Kollision mit einem parkenden Fahrzeug in Folge Nichteinhaltung des Abstandes beim Ausparken | ausparken | 7 | 14 | 101136 |
| Kollision mit einem parkenden Fahrzeug in Folge Nichteinhaltung des Abstandes beim Anfahren, auch Starten mit eingelegtem Gang | Anfahren auf Vorderfz | 7 | 14 | 101118 |
| Sicherungspflicht nach einem VU | Fz (Verursacher, steht) auf Kreuzung | 7 | 49 | 134101, 134107 |
| Fehler beim Rückwärtsfahren, Kollision mit einem geparkten Fahrzeug | rückwärts aus Grundstück | 7 | 36 | 109649, 101012 |
| Fehler beim Rückwärtsfahren, Kollision mit einem geparkten Fahrzeug | rückwärts auf Fz (steht) | 7 | 36 | 101136, 109649 |
| Unzulässiges Halten und Parken auf der BAB oder Kraftfahrstraße | BAB, Fz (Verursacher, steht) | 7 | 43 | 118706 |
| Verkehrswidriges Verhalten beim Ein- und Aussteigen bei geparkten Fahrzeugen (eigenständiges Rollen in den Fließverkehr) | Fz rollt aus Parkstreifen | 7 | 45 | 114118 |
| Mangelnde Sicherung eines liegengebliebenen Fahrzeuges - Lkw, Anhänger 2,8 t ohne Beleuchtung oder reflekt. Tafel (01) - Abstand (02) | 01 (Verursacher, steht) vorn, 02 (Verursacher) dahinter | 7 | 14, 44, 46 | 115601, 115607, 101130 |

## Unfallart 2: Zusammenstoß mit Fahrzeug, das vorausfährt oder wartet

| Fall | Lage in der Skizze | Typ | Ursachen | TBNR |
|---|---|---|---|---|
| nicht angepasste Geschwindigkeit (Abbiegen, Schleudern), Kollision mit verkehrsbedingt haltendem Fahrzeug | Rechtsabbieger (Verursacher, schleudert) trifft Fz (steht) | 1 | 13, 34, 72 oder 73 | 103620, 101006 |
| Kollision mit einem haltenden Fahrzeug in Folge Nichteinhaltung des seitlichen Abstandes beim Abbiegen | Abbieger trifft Fz (steht) | 2 | 14, 34/35 | 101012 |
| Kollision mit einem haltenden Fahrzeug in Folge Nichteinhaltung des seitlichen Abstandes beim Abbiegen | Varianten Abbiegen (3×) | 2 | 14, 34/35 | 101012 |
| Abstand beim Abbiegen (Streifen) | zwei Abbieger nebeneinander | 2 | 14, 34/35 | 101012 |
| Bremsen ohne zwingenden Grund beim Abbiegen | Abbieger bremst, Nachfolger fährt auf | 2 | 15 | 104119 |
| Falsche Fahrbahnbenutzung, Kollision mit einem verkehrsbedingt haltenden Fahrzeug | R auf Radweg (Verursacher), Fz (steht) biegt ein | 2 | 10 | 102738, 101118 |
| Kollision mit einem stehenden Fahrzeug durch Abkommen auf die linke Fahrbahnseite | Abkommen nach links gegen Fz (steht) | 6 | 14 | 102668 |
| ungenügender Sicherheitsabstand zum vorausfahrenden Fahrzeug | Auffahren | 6 | 14 | 101124, 104106 |
| Kollision mit voraus verkehrsbedingt haltendem Fahrzeug durch nichtausreichenden Sicherheitsabstand | Auffahren auf Fz (steht) | 6 | 14 | 101130, 104106 |
| Kollision mit voraus verkehrsbedingt haltendem Fahrzeug durch nicht ausreichenden Sicherheitsabstand, besondere Verhältnisse | Auffahren auf Fz (steht), mit S | 6 | 13, 14, 72 oder 73 | 103620, 103602 |
| Kollision mit Vorausfahrendem durch nicht angepasste Geschwindigkeit, besondere Verhältnisse | Auffahren | 6 | 13, 14, 72 oder 73 | 103620, 103602 |
| Bremsen ohne zwingenden Grund, im Längsverkehr | Vorderer bremst (Verursacher) | 6 | 15 | 104119 |
| Auffahren im Längsverkehr (Kradfahrerin oder Kradfahrer zwischen zwei Fahrzeugen) | Krad zwischen zwei Fz („R,M,K“) | 6 | 14 | 101012 |
| Kollision mit einem haltenden Fahrzeug … beim Wenden | Wenden, trifft Fz (steht) | 7 | 14, 36 | 101012 |
| Fehler beim Rückwärtsfahren im Längsverkehr | rückwärts | 7 | 36 | 109649 |
| Fehler beim Rückwärtsfahren im Längsverkehr auf BAB oder Kraftfahrstraße | rückwärts, BAB | 7 | 36 | 118698, 118686, 118674 |

## Unfallart 3: Zusammenstoß mit Fahrzeug, das seitlich in gleicher Richtung fährt

| Fall | Lage in der Skizze | Typ | Ursachen | TBNR |
|---|---|---|---|---|
| nicht angepasste Geschwindigkeit (Abbiegen, Schleudern- besondere Witterungsverhältnisse) | zwei Abbieger nebeneinander, einer (Verursacher, schleudert) | 1 | 13, 34/35, 72 oder 73 | 103620, 101006 |
| Fehler beim paarweisen Abbiegen nach links, keine Einzelursache, äußerer Beteiligter hat Ursache gesetzt | paarweise links, äußerer (Verursacher) | 2 | 26, 35 | 107101 |
| Fehler beim paarweisen Abbiegen, nicht den Pfeilen Z 297 gefolgt | paarweise rechts, Z 297 | 2 | 26, 34/35, 49 | 141252 |
| als auf der Fahrbahn abbiergende Radfahrerin oder abbiegender Radfahrer nicht an der rechten Seite eines in gleicher Richtung abbiegenden Fahrzeuges geblieben | R und Fz biegen nebeneinander links ab | 2 | 34/35 | 101118 |
| Nichtbeachten des Nachfolgenden beim Vorbeifahren an Hindernissen | Hindernis, rechter schert aus | 5 | 25 | 101118, 106106 |
| Falsche Fahrbahnbenutzung -Lichtzeichen bzw. Dauerlichtzeichen, Fahrstreifenwechsel | Dauerlichtzeichen, Streifenwechsel | 6 | 10, 26 | 101118, 137650 |
| Verstoß gegen das Rechtsfahrgebot beim Überholen | zwei parallel | 6 | 11 | 102631 |
| Unzulässiges Rechtsüberholen | Rechtsüberholer schert ein | 6 | 16 | 105101 |
| Überholen trotz unklarer Verkehrslage, Überholverbot | zwei parallel, linker (Verursacher) | 6 | 18 | 105611, 105626, 105638 |
| Überholverbot (Z 276/277) | zwei parallel, linker (Verursacher), mit Z 276/277 | 6 | 49 | 141629 |
| Überholen ohne Beachtung des nachfolgenden Verkehrs, Wiedereinordnen, Ausscheren | linker zieht vor rechten | 6 | 20 | 105673, 105132 |
| Fehler beim Wiedereinordnen nach rechts, Schneiden, mit Kollision | linker zieht vor rechten | 6 | 21 | 105126 |
| Sonstige Fehler beim Überholen, Seitenabstand | parallel, linker (Verursacher) | 6 | 22 | 105113 |
| Fehler beim Überholt werden, Geschwindigkeit erhöhen | parallel, rechter (Verursacher) | 6 | 23 | 105142 |
| Normalfall des Fahrstreifenwechsels | S-Bogen-Wechsel | 6 | 26 | 107101 |
| Nichtbeachten des Nachfolgenden beim Vorbeifahren an Hindernissen, wie Baustelle usw. | Hindernis, Ausscheren | 6 | 26 | 107101 |
| Nichtbeachten des Nachfolgenden beim Vorbeifahren an Hindernisse, Ausscheren an einer dauernden Verengung | dauernde Verengung | 6 | 26 | 107101 |
| Nicht den Pfeilen Z 297 gefolgt | Z 297, geradeaus aus Abbiegestreifen | 6 | 49 | 141252 |

## Unfallart 4: Zusammenstoß mit Fahrzeug, das entgegenkommt

| Fall | Lage in der Skizze | Typ | Ursachen | TBNR |
|---|---|---|---|---|
| Geschwindigkeit - Gegenverkehr | frontal | 1 | 13; 12 (nur wenn Beweismittel vorhanden sind) | 103854 |
| Geschwindigkeit - besondere Verhältnisse Schleudern/Gegenverkehr | einer schleudert | 1 | 13, 72 oder 73 | 103620, 101006 |
| Geschwindigkeit - falsche Fahrbahn Abbiegen, Begegnung | Einmündung mit Insel | 1 | 13, 34/35 | 103602, 103620 |
| Rechtsfahrgebot - Kurve, Kuppe | Kurve | 1 | 11 | 102649, 102637 |
| falsche Fahrbahn beim Abbiegen, Begegnung | Insel | 2 | 08/09/10, 34/35 | 102603 |
| Rechtsfahrgebot beim Abbiegen - Begegnung | ohne Insel | 2 | 11, 34/35 | 102661 |
| Abbiegen nach rechts bei Grünpfeil aus 2. Fahrstreifen, Rechtsfahrgebot beim Abbiegen | Grünpfeil, 2. Streifen | 2 | 11, 34, 49 | 137632, 137106, 102661 |
| Abbiegen nach rechts bei Grünpfeil aus 2. Fahrstreifen, falsche Fahrbahn beim Abbiegen | Grünpfeil, 2. Streifen, mit Insel | 2 | 08/09/10, 34, 49 | 137632, 137106, 102603 |
| Abbiegen nach rechts bei Grünpfeil, Rechtsfahrgebot beim Abbiegen | Grünpfeil, 1 Streifen | 2 | 11, 34, 49 | 137632, 102661 |
| Abbiegen nach rechts bei Grünpfeil, falsche Fahrbahn beim Abbiegen | Grünpfeil, 1 Streifen, mit Insel | 2 | 08/09/10, 34, 49 | 137632, 102603 |
| Vorbeifahren an vorübergehenden Hindernissen, Gegenverkehr | Hindernis, Ausweichen | 5 | 24 | 106102 |
| falsche Fahrbahnbenutzung, Gegenverkehr | mehrstreifig frontal | 6 | 08/09/10 | 101118, 141148, 141152 |
| „Geisterfahrerin" oder „Geisterfahrer" auf der BAB oder Kraftfahrstraße | Doppellinie | 6 | 08 | 102620, 102614, 102608 |
| falsche Fahrbahnbenutzung, entgegen Z 267 | Z 267 | 6 | 09 | 141512, 141190 |
| falsche Fahrbahnbenutzung - Lichtzeichen, Gegenverkehr | Dauerlichtzeichen | 6 | 10 | 137650 |
| Rechtsfahrtgebot, Gegenverkehr - mit Kollision | frontal | 6 | 11 | 102625, 102667 |
| Überholen trotz Gegenverkehrs | Überholer gegen Gegenverkehr | 6 | 17 | 105608, 105620, 105632 |
| Verständigung an Engstellen | Engstelle, beide (Verursacher) | 6 | 49 | 101030 |
| Vorrang bei Z 208 - verengte Fahrbahn, Gegenverkehr | Z 208 | 6 | 32 | 141141 |
| Schrittgeschwindigkeit - Z 325 | Z 325 | 7 | 49 | 142109 |
| Beleuchtungsbetriebsvorschriften | frontal | 7 | 46 | 117102, 117114, 117126 |

## Unfallart 5: Zusammenstoß mit Fahrzeug, das einbiegt oder kreuzt

| Fall | Lage in der Skizze | Typ | Ursachen | TBNR |
|---|---|---|---|---|
| Nichtangepasste Geschwindigkeit - falsche Fahrbahn, Abbiegen | Insel, Rechtsabbieger | 1 | 13, 34 | 103602, 103620 |
| falsche Fahrbahnbenutzung beim Abbiegen | Insel, Rechtsabbieger | 2 | 08/09/10, 34 | 102603 |
| Rechtsfahrgebot beim Abbiegen, wo tangentiales Abbiegen nicht möglich ist | zwei Linksabbieger begegnen sich | 2 | 11, 35 | 102655 |
| ungenügender Seitenabstand beim tangentialen Abbiegen | zwei Linksabbieger begegnen sich, , beide (Verursacher) | 2 | 35, 49 | 101118 |
| tangentiales Abbiegen nicht befolgt | zwei Linksabbieger begegnen sich | 2 | 35, 49 | 109631 |
| Abbiegen - Nichtbeachten Nachfolgeverkehr 01 - Überholen, unklare Verkehrslage 02 | 01 biegt ab, 02 überholt | 2 | 18, 34/35 | 109114, 105611 |
| Abbiegen - Nichtbeachten Nachfolgeverkehr 01 - Überholen, unklare Verkehrslage 02 | 01 biegt ab, 02 überholt, an Grundstück | 2 | 18, 34/35 | 109637, 109114, 105611 |
| Rechtsfahrgebot beim Abbiegen | Rechtsabbieger, Querverkehr | 2 | 11, 34 | 102661 |
| Vorschriftswidriges Linksüberholen | Linksüberholen eines Linksabbiegers | 2 | 22 | 105155 |
| Fehler beim Abbiegen - Nichteinordnen | Abbiegen aus falschem Streifen | 2 | 34/35 | 109108, 101118 |
| Fehler beim Linksabbiegen - Gegenverkehr | Linksabbieger, Gegenverkehr | 2 | 35 | 109601 |
| Fehler beim Linksabbiegen - abknickende Vorfahrt, Gegenverkehr | abknickende Vorfahrt | 2 | 35 | 109601 |
| Fehler beim Abbiegen - aus 2. Fahrstreifen - ohne Ankündigung - Nichteinordnen | Rechtsabbieger aus 2. Streifen | 2 | 34 | 109108, 109102, 109114 |
| Fehler beim Abbiegen - ohne Ankündigung - Nichteinordnen | Linksabbieger aus rechtem Streifen | 2 | 35 | 109108, 109102, 109114 |
| Fehler beim Linksabbiegen - Gegenverkehr nach rechts | Linksabbieger | 2 | 35 | 109655 |
| Fehler beim Abbiegen in ein Grundstück, auch nach links | in Grundstück | 2 | 35 | 109637 |
| Nicht den Pfeilen Z 297 gefolgt | Z 297 | 2 | 49 | 141252 |
| Fehler beim Abbiegen in ein Grundstück, Nichtbeachten Z 295 | über Z 295 ins Grundstück | 2 | 34/35, 49 | 109637, 141500, 141254 |
| Fehler beim Abbiegen (01) Radfahrerin oder Radfahrer über 10 Jahre auf Fußgängerfurt (02) | Furt grün, 01 biegt ab, 02 Rad | 2 | 34/35 und 10 | 109613, 101118, 109114 |
| Missachtung des Rotlichts der LZA, als Radfahrerin oder Radfahrer | Rechtsabbieger bei Grün, R (Verursacher) fährt bei Rot geradeaus | 2 | 31 | 137614, 137626 |
| Nichtbeachten der oder des in gleicher Richtung fahrenden Verkehrsteilnehmers beim Abbiegen nach rechts (links) | Rechtsabbieger, Geradeausfahrer | 2 | 34 | 109613, 109601 |
| Sonderfahrstreifen - Z 245 | Busspur | 2 | 34/35 | 109607 |
| Sonderfahrstreifen - Z 245 | Busspur, beide (Verursacher) | 2 | 10 und 34/35 | 141202, 109114 |
| Nichtbenutzung des vorhandenen Radfahrstreifens beim Abbiegen nach links | Radfahrstreifen | 2 | 35 | 109114, 141449 |
| Abbiegen nach links, ohne auf den nachfolgenden Verkehr zu achten, Wartepflicht | R biegt links ab | 2 | 35 | 109114 |
| Abbiegen nach rechts bei Grünpfeil aus 2. Fahrstreifen, Rechtsfahrgebot beim Abbiegen | Grünpfeil, 2. Streifen | 2 | 11, 34, 49 | 137632, 137106 |
| Abbiegen nach rechts bei Grünpfeil aus 2. Fahrstreifen, falsche Fahrbahn beim Abbiegen | Grünpfeil, 2. Streifen, Insel | 2 | 08/09/10, 34, 49 | 137632, 137106 |
| Abbiegen nach rechts bei Grünpfeil, Rechtsfahrgebot beim Abbiegen | Grünpfeil | 2 | 11, 34, 49 | 137632 |
| Abbiegen nach rechts bei Grünpfeil, falsche Fahrbahn beim Abbiegen | Grünpfeil, Insel | 2 | 08/09/10, 34, 49 | 137106 |
| Vorfahrt - rechts vor links | rechts vor links | 3 | 27 | 108601 |
| Vorfahrt - rechts vor links - zu weit vorgefahren | rechts vor links, vorgefahren | 3 | 27 | 108601 |
| Vorfahrt - Z 206 | STOP | 3 | 28 | 141601 |
| Vorfahrt - Z 205/Z 206 | Z 205/206 | 3 | 28 | 108607 |
| Vorfahrt - Z 205/Z 206 - zu weit vorgefahren | Z 205/206, vorgefahren | 3 | 28 | 108607 |
| Vorfahrt - BAB - Kraftfahrstraße | Einfädeln | 3 | 29 | 118626 |
| Vorfahrt - Feld- , Waldweg | Waldweg | 3 | 30 | 108613 |
| Nichtankündigung beim Folgen des Verlaufes der abknickenden Vorfahrtstraße | abknickende Vorfahrt | 3 | 49 | 142101 |
| Vorrang - LZA | LZA | 3 | 31 | 137602 |
| Haltezeichen eines Eingreifpostens | Kreuzung | 3 | 49 | 136607 |
| Vorrang - VP Regelung | Kreuzung | 3 | 31 | 136106 |
| Räumen nicht ermöglicht, mit LZA | Räumer | 3 | 49 | 101043 |
| Zu spätes Räumen, mit LZA - schon ein oder zwei Fahrzeuge durchgefahren | Räumer bei Rot | 3 | 49 | 101118 |
| Missachtung Sonderrechte (01) Gebührende Rücksichtnahme (02) - immer beide Verursacherinnen und/oder Verursacher | 02 von links, 01 von unten | 3 | 49 | 138602, 135000 |
| stockender Verkehr, **ohne** LZA | Querverkehr | 3 | 49 | 111101 |
| Vorrang - Z 201 | Gleise | 3 | 33 | 119608 |
| Vorrang - Lichtzeichen, Schranken | Gleise | 3 | 33 | 119608 |
| Einfahren - Grundstück, Fließverkehr | aus Grundstück | 3 | 37 | 110101 |
| Einfahren - anderer Straßenteil, Radweg, Fließverkehr | R vom Radweg | 3 | 37 | 110119 |
| Einfahren - anderer Straßenteil Fußgängerfurt/-symbol, Fließverkehr | über Furt | 3 | 37 | 110119 |
| Einfahren - anderer Straßenteil Fließverkehr | anderer Straßenteil | 3 | 37 | 110119 |
| Einfahren - verkehrsberuhigter Bereich Z 326 - Fußgängerbereich Z 243 - Absenkung, Fließverkehr | Einmündung | 3 | 37 | 110113, 110107, 110125 |
| Abbiegen nach rechts bei Grünpfeil | Grünpfeil, R | 3 | 49 | 137638 |
| Abbiegen nach rechts bei Grünpfeil (01) R falschen Radweg benutzt (02) | Grünpfeil, R 02 falscher Radweg | 3 | 49 und 10 | 137638, 102176 |
| Abbiegen nach rechts bei Grünpfeil aus 2. Fahrstreifen | Grünpfeil 2. Streifen, R | 3 | 49 | 137638, 137106 |
| Abbiegen nach rechts bei Grünpfeil aus 2. Fahrstreifen (01), R falschen Radweg benutzt (02) | Grünpfeil 2. Streifen, R, R 02 | 3 | 49 und 10 | 137638, 137106, 102176 |
| Abbiegen nach rechts bei Grünpfeil aus 2. Fahrstreifen | Grünpfeil 2. Streifen, R, Fz | 3 | 49 | 137632, 137106 |
| Abbiegen nach rechts bei Grünpfeil | Grünpfeil | 3 | 49 | 137632 |
| Einfahren aus ruhendem Verkehr - Abbiegen | vom Rand einfahren und abbiegen | 5 | 34/35, 37 | 110131, 109114 |
| Einfahren aus ruhendem Verkehr - Wenden | vom Rand wenden | 5 | 36, 37 | 110131, 109643 |
| Fahrzeug verlassen, Weiterrollen | Parkhafen, rollt | 5 | 45 | 114118 |
| Rückwärtsfahren - Einfahren in den Fließverkehr aus Parkhafen | Parkhafen rückwärts | 5 | 36, 37 | 109649 |
| Abbiegen - Parkhafen | in Parkhafen | 5 | 34/35 | 109114 |
| Wendeverbot Z 272 | Z 272 | 7 | 36, 49 | 141207 |
| Rückwärtsfahren - Fließverkehr | rückwärts | 7 | 36 | 109649 |
| Rückwärtsfahren - Einfahren in den Fließverkehr vom Grundstück | rückwärts aus Grundstück | 7 | 36, 37 | 109649, 110101 |
| Rückwärtsfahren - Einfahren in den Fließverkehr vom anderen Straßenteil | rückwärts von anderem Straßenteil | 7 | 36, 37 | 109649, 110119 |
| Wenden - aus Fließverkehr | Wenden | 7 | 36 | 109643 |
| Wenden - BAB - Kraftfahrstraße | Wenden BAB | 7 | 36 | 118692, 118680, 118668 |
| Verständigung auf Parkplätzen nach § 1 StVO | Parkplatz | 7 | 49 | 101118 |

## Unfallart 6: Zusammenstoß zwischen Fahrzeug und Fußgänger

| Fall | Lage in der Skizze | Typ | Ursachen | TBNR |
|---|---|---|---|---|
| Fußgängerfurt - Abbiegen, LZA in Betrieb | Rot, Furt, Abbieger, F | 2 | 60 | 137101 |
| Abbiegen | ohne LZA | 2 | 40 | 109625 |
| Fußgängerfurt - Abbiegen, LZA in Betrieb | Grün, Furt | 2 | 39, 40 | 109625 |
| Ausfahren - Grundstück Fußgängerin oder Fußgänger auf Gehweg | Ausfahrt Grundstück, F auf Gehweg | 3 | 37, 42 | 110101 |
| Fußgängerüberweg Z 293, Z 350 | Zebrastreifen | 4 | 38 | 126608 |
| Fußgängerfurt - LZA in Betrieb | Furt Rot | 4 | 39 | 137602 |
| Fußgängerüberweg Z 293, Z 350 | Zebrastreifen, F (Verursacher) | 4 | 61 | 101118 |
| Fußgängerfurt - LZA in Betrieb, - VP-Regelung | Furt Rot, F | 4 | 60 | 137101 |
| Benutzungspflicht (§ 25 Abs. 3 StVO) - Fußgängerfurt, - Fußgängerüberweg, - Fußgängertunnel | Kreuzung | 4 | 62 | 125113 |
| falsches Verhalten gegenüber Fußgängerinnen oder Fußgängern an anderen Stellen | F von links | 4 | 42 | 101118 |
| Schulbus mit Warnblinklicht | F, Fz (Verursacher); Bus nicht gezeichnet | 4 | 41 | 120750, 120702 |
| Haltestelle Z 224 | Haltestelle Z 224 | 4 | 41 | 120613 |
| mangelnde Bremsbereitschaft gegenüber Fußgängerinnen oder Fußgängern - Kind, hilfsbedürftigen, älteren Menschen | F, Fz (Verursacher) | 4 | 13, 42 | 103709 |
| Nichtbeachten Fahrzeugverkehr, Hervortreten hinter Sichthindernis | F (Verursacher), Fz | 4 | 64, (63) | 125113 |
| Nichtbeachten Fahrzeugverkehr (01) falsches Verhalten gegenüber Fußgängerinnen oder Fußgängern (02) | F01 (Verursacher), 02 Fz (Verursacher) | 4 | 64, (65), 42 | 125113, 101118 |
| Abbiegen nach rechts bei Grünpfeil | Grünpfeil, Furt | 4 | 39, 49 | 137638 |
| Abbiegen nach rechts bei Grünpfeil | Grünpfeil, Furt, F von links | 4 | 39, 49 | 137638 |
| Abbiegen nach rechts bei Grünpfeil aus 2. Fahrstreifen (2×) | Grünpfeil, Furt, 2 Streifen | 4 | 39, 49 | 137638, 137106 |
| falsches Verhalten gegenüber Fußgängern an anderen Stellen - Rückwärtsfahren | rückwärts gegen F | 7 | 36, 42 | 109649, 101118 |
| Ausfahren, rückwärts - Grundstück, Fußgänger auf Gehweg | rückwärts aus Grundstück | 7 | 37, 42 | 110101, 109649 |
| verbotswidriges Betreten - BAB - Kraftfahrstraße | BAB, F (Verursacher) | 7 | 69 | 118184, 118190 |

## Unfallart 7: Aufprall auf Hindernis auf der Fahrbahn

| Fall | Lage in der Skizze | Typ | Ursachen | TBNR |
|---|---|---|---|---|
| Nicht gesicherte Baustelle |  | 7 | 85 | – |
| Wild auf Fahrbahn |  | 7 | 86 | – |
| anderes Tier auf der Fahrbahn - z. B. nicht angeleinte und frei herumlaufende Hunde |  | 7 | 87 | 128001 |

## Unfallart 8 und 9: Abkommen von der Fahrbahn nach rechts (8) oder links (9)

| Fall | Lage in der Skizze | Typ | Ursachen | TBNR |
|---|---|---|---|---|
| Geschwindigkeit (Baustelle) |  | 1 | 13; (12) nur wenn Beweismittel vorhanden | 103602, 101000 |
| Geschwindigkeit (Baustelle) |  | 1 | 13; (12) nur wenn Beweismittel vorhanden | 103620, 101000 |
| Geschwindigkeit - besondere Verhältnisse, Schleudern |  | 1 | 13, 72 oder 73 | 103620, 101006 |
| Geschwindigkeit - Abbiegen, besondere Verhältnisse, Schleudern |  | 1 | 13, 34/35, 72 oder 73 | 103620, 101006 |
| Geschwindigkeit - Abbiegen |  | 1 | 13, 34/35 | 103620, 101000 |
| Geschwindigkeit - Wenden |  | 1 | 13, 36 | 101000, 101006 |
| Geschwindigkeit - auch Radio einstellen, Zigarette anzünden usw. |  | 7 | 13; (12) nur wenn Beweismittel vorhanden | 101000, 101006 |

## Unfallart 0: Unfall anderer Art

| Fall | Lage in der Skizze | Typ | Ursachen | TBNR |
|---|---|---|---|---|
| Geschwindigkeit - Sturz ohne Fremdeinwirkung | R, K, M | 1 | 13, 72 oder 73 | 101006 |
| Geschwindigkeit - Sturz auf schienengleichen Wegübergang | Gleise | 1 | 13, 72 oder 73 | 101006 |
| Vorfahrt - ohne Berührung mit Abkommen von der Fahrbahn | Z 205 | 3 | 28 | 108607 |
| - Vorbeifahren (01) - Fahrerin oder Fahrer steht an Fz-Tür und wird angefahren (02) | 1/2 | 5 | 14 und 45 | 101012, 114106 |
| falsche Fahrbahnseite - Rechtsfahrgebot, Gegenverkehr von der Fahrbahn abgekommen, ohne Kollision | Ausweichen | 6 | 11 | 102625 |
| Fahrstreifenwechsel - ohne Berührung mit Abkommen von der Fahrbahn | Streifenwechsel | 6 | 26 | 107101 |
| anderer Straßenteil - Sturz ohne Fremdeinwirkung auf Gehweg | Gehweg, R, K, M | 7 | 10 | 102714, 141172 |
| Abstand, Hindernis beim Rangieren | Tafel | 7 | 14 | 101000 |
| Überbesetzung | R | 7 | 47 | 121160 |
| Rückwärtsfahren - Hindernis beim Rangieren | rückwärts gegen Tafel | 7 | 36 | 109649, 101000 |
| ungesicherte Ladung, fallend - direkt auf Fahrzeug | Ladung | 7 | 48 | 122609 |
| ungesicherte Ladung fallend - Mauerstein von Lkw auf Fahrbahn | Ladung | 7 | 48, 88 | 122603, 122609 |
| ungesicherter Ausleger | Ladung | 7 | 48 | 122609 |
| ungesicherte Ladung - allgemein | Ladung | 7 | 48 | 123607 |
| Nichtbeachten Z Z 265 (Durchfahrtshöhe) | Z 265 3,8 m | 7 | 49 | 141181 |
| Beifahrerin oder Beifahrer greift ins Lenkrad (§23 StVO) | Abkommen | 7 | 49 | 101000, 101006 |
| körperliche oder geistige Mängel - z. B. Schwächeanfall, Zuckerschock | Abkommen | 7 | 04, 49 | – |
| Öl auf der Fahrbahn, Verursacherin oder Verursacher unbekannt - nur 1 Beteiligter |  | 7 | 70 | – |
| schlechter Straßenzustand - Löcher in der Fahrbahn |  | 7 | 76 | – |
| Gegenstand, z. B. Stein, auch Taube, Ente fliegt gegen die Windschutzscheibe |  | 7 | 89 | – |
| ungenügendes Lichtraumprofil | Baum/Ast | 7 | 89 | – |
| Mängel allgemein - Verantwortlichkeit | gemeinsame Skizze | 7 | 50 - 55 | 123601 |
| Mängel - Bereifung |  | 7 | 51 | 336608, 336620 |
| Mängel - Bremsen |  | 7 | 52 | 341614, 341617, 365000 |
| Mängel - Lenkung |  | 7 | 53 | 338614, 338617 |
| Mängel - Zugvorrichtung |  | 7 | 54 | 343620, 343623 |
