# Sonderfälle

Nur lesen, wenn der Sachverhalt einen dieser Punkte berührt. Quelle: GA PPr St 5/2008 (Dienststellenbezeichnungen dort teils überholt), Checkliste VUK (06.2026).

## Ist das überhaupt ein Verkehrsunfall?

Ein VU ist ein plötzliches, von mindestens einem Beteiligten nicht gewolltes Ereignis im öffentlichen Verkehrsraum, das mit den typischen Gefahren des Straßenverkehrs zusammenhängt und zu Personenschaden oder nicht ganz belanglosem Sachschaden führt. Eine Wertgrenze gibt es nicht.

| Lage | Einordnung |
|---|---|
| Körperverletzung oder Sachbeschädigung nach Streit, Verfolgung oder Aussteigen (Aggressionstat) | Kein VU, sondern allgemeine Straftat. Probe: Wäre der Hergang auch fahrlässig denkbar? |
| Fahrgast stürzt im Bus oder in der Bahn bei gewöhnlichem Bremsen oder Abbiegen | Kein VU |
| Fahrgast stürzt, weil der Fahrer scharf bremsen musste, um einen Zusammenstoß zu verhindern | VU (Unfallart 0). Im Zweifel VU aufnehmen |
| Ereignis auf besonderem Bahnkörper (Gleise abseits der Fahrbahn) | Kein VU; gegebenenfalls Strafanzeige. Straßenbündige Gleise: VU |
| Aufgewirbelter Stein oder Splitt beschädigt ein Fahrzeug | VU, unabwendbares Ereignis: kein Vorwurf, am Ort abgeschlossen, StM 0. Gilt nicht für verlorene Ladung |
| Grunddaten fehlen, nur Verdacht auf einen Unfall | "Ereignis im Straßenverkehr", siehe `flucht.md` |
| Unfallort außerhalb Berlins, Anzeige in Berlin | A-VU erhält kein Berliner Aktenzeichen, Weiterleitung an die örtliche Dienststelle. Auslandsunfälle nur bei Verdacht einer Straftat |

## Tiere

- **Wildunfall**: VU. Unfallart 7, Unfalltyp 7, allgemeine Ursache 86, kein Vorwurf, StM 0. Jagdausübungsberechtigten, Forstamt oder Stadtjäger unverzüglich benachrichtigen.
- **Frei laufendes Haustier**: Unfallart 7, Unfalltyp 7, allgemeine Ursache 87. Vorwurf gegen den Verantwortlichen (Suche im Katalog: `grep -i "Tiere" recht/tbkat.txt`).
- **Geführtes Tier, Reiter**: Unfallart 0.
- Tiere sind nie Beteiligte.

## Polizei und Sonderrechte

- Unfälle mit Polizeifahrzeugen nimmt eine nicht betroffene Dienststelle auf.
- Bei zivilen Dienstfahrzeugen das Behördenkennzeichen eintragen, nicht das Tarnkennzeichen. Schadenersatz: Verweis an die Selbstversicherung des Landes Berlin.
- Sonder- oder Wegerechtsfahrt gegen Querverkehr: in der Regel haben beide eine Ursache gesetzt (Unfalltyp 3, je Ursache 49). Unfallkommando bei Sonder- oder Wegerechtsfahrt mit Schwerverletzten (Kriterien in `poliks.md`); nach der GA auch sonst bei Sonderrechtsfahrten der Polizei, außer bei Park- und Rangierschäden.
- Verfolgungsfahrt: Polizeikräfte auch ohne Berührung als Beteiligte erfassen, wenn ihr Verhalten und der Unfall unmittelbar zusammenhängen.

## Besondere Beteiligte

- **BVG-Personal** als Anzeigende oder Zeugen: Name und Dienstnummer genügen. Ist eine Straßenbahn beteiligt, den Ermittlungsdienst informieren.
- **Bundeswehr** (Dienstfahrzeug oder verletzter Soldat) und **NATO-Truppen**: Aufnahme und Verfolgung wie bei jedem anderen; Feldjäger über das Lagezentrum benachrichtigen.
- **Diplomaten und andere Bevorrechtigte**: regelt die GA über Verkehrsstraftaten, nicht diese. Halteranfrage-Schlüssel 12.
- **Wohnsitz im Ausland**: sofort anhören oder vernehmen, nach einer Zustelladresse in Berlin fragen. Bei Tod oder schweren Fällen das Konsulat benachrichtigen.
- **Kinder unter 14** handeln nicht vorwerfbar (§ 12 OWiG, in `recht/owig.txt`): keine Verwarnung, keine Anzeige; auf dem A-VU bleibt die BOWI-TBNR leer. Ordnungsnummer und Ursachen werden trotzdem eingetragen, in POLIKS auch der Tatvorwurf. Mit dem Fahrrad müssen Kinder bis acht und dürfen Kinder bis zehn Jahre den Gehweg benutzen (§ 2 Abs. 5 StVO): das ist dann kein Fehler.
- **E-Scooter** sind Kraftfahrzeuge (eKFV in `recht/ekfv.txt`). Destatis-Schlüssel 05, BOWI-Fahrzeug 16. Katalogsuche: `grep -i "Elektrokleinst" recht/tbkat.txt`.

## Besondere Abläufe

- **Mehrere Unfälle derselben Person** an verschiedenen Orten: je Unfallort eine eigene Anzeige, als Sammelanzeige gekennzeichnet; zuständig ist der Abschnitt des ersten Unfallorts. Nur eine Anzeige, wenn die weiteren Zusammenstöße Folge desselben Ablaufs sind (Fahrer verliert die Kontrolle und streift mehrere Autos); die weiteren Orte dann im Hergang nennen.
- **Falschparker wird beschädigt**, hat aber keine Ursache gesetzt und ist nicht am Ort: Die Anzeige wegen des Parkverstoßes wird im VU miterfasst. Keine Abgabe an den Ermittlungsdienst nötig, wenn die Lage sonst klar ist.
- **Verlorene Ladung oder Fahrzeugteile überfahren**, Verantwortlicher unbekannt: ungeklärter VU, Abgabe an den Ermittlungsdienst.
- **Gefahrgut beteiligt**: Ermittlungsdienst informieren; Unfallkommando bei Freisetzung.
- **Verdacht auf gestellten Unfall**: besonders gründlich aufnehmen, Rücksprache Unfallkommando; zuständig ist LKA 223.
- **Führerschein**: Verwahrung oder Beschlagnahme, wenn dringende Gründe für eine Entziehung sprechen (§ 69 StGB, §§ 94, 98, 111a StPO, alle in `recht/`).
- **Fahrzeug mit behauptetem oder vermutetem technischen Mangel als Unfallursache**: verwahren oder beschlagnahmen, Ermittlungsdienst vorab anrufen. Schäden, die erst durch den Unfall entstanden sind: kein Mängelbericht, nur Hinweis auf die Beseitigung.
- **Öffentliches Eigentum beschädigt** (Ampel, Lichtmast, Schutzplanke): zuständige Stelle unterrichten, Ampelschäden sofort melden. Der Eigentümer ist sonstiger Geschädigter.
- **Abwesende Geschädigte**: Unfallaktenzeichen per Hinweiszettel am Fahrzeug hinterlassen und Benachrichtigung anstreben.
- **Verjährte Verstöße** bei später Anzeige: trotzdem als VU erfassen und die Verjährung vermerken.
