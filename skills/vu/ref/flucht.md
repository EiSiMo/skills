# VU-Flucht (§ 142 StGB)

Quellen: Checkliste VU-Flucht der PA (06.2026), GA PPr St 5/2008 mit Anlage 2.1 (POLIKS-Anleitung von 2008; Feldnamen können heute abweichen). Wortlaut des § 142 in `recht/stgb.txt`.

## Einordnen

- Eine Flucht ist der Verdacht einer Verkehrsstraftat und läuft deshalb **immer über POLIKS**, nie als A-VU. Alles aus `poliks.md` gilt zusätzlich. Weiterbearbeitung: Dir K 23. Kategorie nach den Folgen: ohne Verletzte und mit fahrbereiten Fahrzeugen 5, mit einem nicht fahrbereiten Kfz 4, mit Verletzten 1 bis 3.
- **Kein Fluchtfall** ist der Verursacher, der nach einem Parkrempler selbst die Polizei ruft, weil der Geschädigte nicht da ist: gewöhnlicher Unfall, in der Regel A-VU, Verwarnung ohne Verwarnungsgeld möglich. Am beschädigten Fahrzeug den Hinweiszettel hinterlassen.
- **"Ereignis im Straßenverkehr" statt VU**, wenn Grunddaten fehlen oder nur ein Anfangsverdacht auf einen Unfall besteht:
  - Der Geschädigte ist unbekannt und nicht ohne Weiteres zu ermitteln (Verursacher meldet sich, das beschädigte parkende Fahrzeug ist inzwischen weg).
  - Unfallort und Unfallzeit sind unbekannt: Der Geschädigte stellt den Schaden irgendwann fest und weiß nicht, wo und wann er entstanden ist. Steht der Abstellort fest und gibt es ein Zeitfenster (abgestellt gestern Abend, bemerkt heute früh), ist es ein VU mit Flucht.
  - Nach Diebstahl aufgefundenes Fahrzeug mit Unfallspuren (Unfallkommando anfordern).
  - Frische Unfallspuren bei einer Kontrolle, der Fahrer macht keine Angaben.

  Erfassung dann: Erfassungsgrund "Ereignis im Straßenverkehr", Ereignisbezeichnung "Besichtigung eines Fahrzeuges", Vorgangstyp Verkehrsunfall, Anwendungsfall VU-Anzeige. Keine HEM, zählt nicht als VU. Im Zweifel ein Tätigkeitsbericht "Ereignis mit Bezug zum Straßenverkehr".

## Erfassung in POLIKS

| Feld | Eintrag |
|---|---|
| Dringlichkeit | "VU-Flucht". Geht anderen Vermerken vor; es ist nur eine Angabe möglich |
| Tatvorwurf gegen den Geflüchteten | Tatvorwurf "Sonstige Ermittlungen", Zusatzbezeichnung "Unfallflucht", Rechtsnorm "§ 142 StGB". (Über die Erfassungsgründe des VU oder den Katalog der Verkehrsstraftaten lässt sich die Flucht nicht eintragen.) Daneben die übrigen Vorwürfe: etwa § 229 StGB bei Verletzten, und der Verkehrsverstoß, der zum Unfall führte |
| Geflüchteter Beteiligter | Als "Unbekannter mit Beschreibung" anlegen. Er ist in der Regel Ordnungsnummer 01, der Geschädigte 02 |
| § 142 StGB (unerlaubtes Entfernen) | "Ja" beim Geflüchteten. Bleibt stehen, auch wenn sich später ergibt, dass keine Flucht vorlag |
| Fluchtfahrzeug | So genau wie bekannt. Insassenzahl leer, Gefahrgut offen lassen |
| Schaden am geschädigten Fahrzeug | Genau beschreiben, mit Verlauf und Höhe über dem Boden; zurückgebliebene Fremdteile nennen |
| Sachverhalt | Abstellzeit des beschädigten Fahrzeugs und Zeitpunkt der Schadensfeststellung immer angeben. Tatvorwurf und Belehrung vermerken, wenn der Fahrer angetroffen wurde. Wer wann welche Ermittlung veranlasst hat |
| Zusatzbezeichnung | "Videosicherung erforderlich", wenn ein Video nicht am selben Tag abgeholt werden kann |
| Statistikangaben | Wie bei jedem Unfall. Ist auch die Art des Fluchtfahrzeugs unbekannt: Verkehrsbeteiligung 92, in der Ausgabe "Führer, Fahrzeugart unbekannt" |
| HEM "Unfallflucht geklärt/ungeklärt" | Legt der Sachbearbeiter des Ermittlungsdienstes an, nicht die aufnehmende Kraft |

Skizze: verhältnisgerecht, gegebenenfalls Fotos; bei Flucht mit Verletzten maßstabsgerecht mit Fotos. Flucht mit schwer verletzter Person: Unfallkommando anfordern (Kriterien in `poliks.md`).

**Hergang unbekannt.** Meist hat niemand den Anstoß gesehen; dann weiß auch der Beamte nicht mehr als das Schadensbild, und eine Rückfrage hilft nicht. Wähle Unfalltyp, Ursache und Tatbestandsnummer nach der naheliegendsten Lage und sag in einer Zeile, wovon du ausgehst und was sich bei der anderen Lage ändert:

- Anstoß an Front oder Heck eines längs geparkten Fahrzeugs spricht für Rangieren beim Ein- oder Ausparken: Unfallart 1, Unfalltyp 7.
- Streifschaden an der Seite zur Fahrbahn spricht für Vorbeifahren: Unfallart 1, Unfalltyp 5.

## Ausgabe bei Flucht

Wie bei POLIKS (`poliks.md`), mit diesen Zusätzen. Das Muster zeigt nur die Form.

```
Angenommen: …

**POLIKS-VU, Flucht**
- Dringlichkeit: VU-Flucht
- Unfallkategorie: 5 Sonstiger Sachschadenunfall
- Weiterbearbeitung: Dir K 23
- Unfallzeit: zwischen … (abgestellt) und … (bemerkt), beide Zeiten in den Sachverhalt
- PLZ Unfallort: 1xxxx

**Unfall**
- Unfallart: 1 Zusammenstoß mit anderem Fahrzeug, das steht, anfährt oder anhält
- Unfalltyp: 7 Sonstiger Unfall (Rangieren, nach dem Schadensbild)

**01 – Unbekannter mit Beschreibung, Fahrer weißer Transporter**
- Art der Beteiligung: Führer Kleintransporter (ob auch Halter, ist offen)
- § 142 StGB: ja
- Ursachen: …
- Tatvorwurf: Sonstige Ermittlungen, Zusatzbezeichnung "Unfallflucht", § 142 StGB
- Tatvorwurf: Ordnungswidrigkeit, VK-Owi, § …
- Tatbestandsnr.: leer wegen der Straftat
- OWi dahinter: [1xxxxx](https://www.weg.li/charges/1xxxxx)
- Fahrzeug: Farbe und Art, soweit bekannt (das Kennzeichen trägt der Nutzer selbst ein)
- Insassen: leer
- Gefahrgut: offen

**02 – Pkw, geparkt**
- Art der Beteiligung: Pkw, geparkt
- § 142 StGB: nein
- Insassen: 00
- Verstoß: keiner
- Schaden: genau beschreiben (Stelle, Verlauf, Höhe über dem Boden, Fremdteile)

**Dokumentation**
- Skizze: verhältnisgerecht, Fotos vom Schaden
- Zeugen: Hinweisgeber vom Zettel

**Jetzt am Ort**
- (nur die Punkte der Checkliste unten, die nach dem Sachverhalt anstehen, höchstens acht)
```

## Ermittlungen am Ort (Checkliste)

**Kennzeichen bekannt oder ermittelbar**
- Zettel eines Zeugen oder ein Foto davon zum Vorgang nehmen. Zeugen anrufen: Personalien, Erreichbarkeit, Sachverhalt.
- Teilkennzeichen: in ZEVIS selbst variieren (Kombination ändern, Anfrage mit einem "?" ist zulässig). Sonst Rücksprache Dir X K 24 für die Anfrage beim KBA.

**Vorermittlungen**
- Kennzeichen in ZEVIS/POLIKS abfragen, Halteranschrift ermitteln.
- Halter im Einwohnerwesen abfragen (ZEVIS-Anschrift oft veraltet). Lichtbild vorhanden: passt es zur Beschreibung der Zeugen?
- Halteranschrift selbst aufsuchen oder den Wohnabschnitt oder Fremdkräfte beauftragen.

**An der Halteranschrift**
- Fahrzeug da: Motorhaube warm? Schäden? Schriftlich festhalten.
- Halter aufsuchen. Passt die Personenbeschreibung auf ihn: Tatvorwurf und Belehrung (im Sachverhalt notieren). Passt sie nicht: nach dem Nutzer zur Tatzeit fragen; Zeugnisverweigerungsrecht von Angehörigen beachten.
- Auf Alkohol und Drogen achten (Vortest, Blutentnahme).
- Zugriff auf den Fahrzeugschlüssel klären (noch in der Tasche? Durchsuchung).

**Spurensicherung am Fahrzeug**
- Fotos mit festem Maßstab (Zollstock), Höhe der Anstoßstelle von unten bis oben, planparallel fotografieren (in die Knie gehen).
- Fremdlack (Farbaufrieb) immer sichern, mit Klebeband abnehmen. Wenn möglich auch Eigenlack; bei auswärtigen Fahrzeugen immer.
- Die Fahrzeuge sind Beweismittel. Verweigert jemand die Spurensicherung (Sorge um den Lack): richterliche Entscheidung über die Rufbereitschaft der Staatsanwaltschaft, Tel. 0172-3851354. In der Regel wird das Fahrzeug für die Dauer der Spurensicherung beschlagnahmt.

**Fahrzeug nicht an der Halteranschrift**
- Halter nach dem Standort fragen.
- Ausländisches Kennzeichen: POLIKS/EUCARIS. Hat der Halter eine Berliner Meldeanschrift, dort weiter wie oben.
- Keine Berliner Anschrift oder ausländisches Kennzeichen: Sachfahndung prüfen, nach Rücksprache mit Dir X K 24 oder K 23. Ausschreibungsgrund: Spurensicherung, Insassenfeststellung.
- Wird das Fahrzeug bald repariert, ist der Lackvergleich als Beweis verloren.

**Video und Fotos** (Zeitfenster 24 bis 48 Stunden)
- Parkhaus: Videoüberwachung, Sicherheitsdienst.
- Autobahntunnel: Tunnelleitzentrale, Tel. 03303-5804000, tlz-berlin@autobahn.de.
- Einkaufsstraße: Kameras von Geschäften.
- Dashcams von Zeugen und Beteiligten; bei Tesla immer. Ein unbeteiligter Tesla in der Nähe: Wächtermodus, Halter zur Beweissicherung ermitteln.
- Sicherung veranlassen und im Vorgang vermerken, bei wem das Video abzuholen ist (Name, Telefon, E-Mail). Zeugenfotos an die dienstliche E-Mail senden lassen, eigene Bilder über die PolCloud speichern.
- Abholung am selben Tag nicht möglich: Information an W1 oder K 24 der Direktion, in POLIKS Zusatzbezeichnung "Videosicherung erforderlich".

**Geschädigter am Ort**
- Zum Hergang befragen, Handynummer notieren.
- Spurensicherung wie oben. Die Sicherung des Fahrzeugs ist danach Sache des Halters.

**Geschädigter nicht am Ort**
- Spurensicherung wie oben.
- Halter informieren, vor allem wenn Wertsachen im Auto liegen; notfalls Sicherstellung zur Eigentumssicherung.
- Hinweiszettel (Pol V510) am Fahrzeug hinterlassen oder an der Halteranschrift einwerfen.
- Nachts muss der Halter bei geringem Schaden nicht herausgeklingelt werden; der Zettel reicht. Ausnahme: Das Fahrzeug lässt sich nicht mehr verschließen oder es liegen Wertsachen darin.

**Dokumentation**
- Halteranschrift selbst aufgesucht: Ergebnis im Hauptvorgang vermerken (wer hat wann was veranlasst).
- Durch Fremdkräfte aufgesucht: Zuarbeit zum Hauptvorgang, Tätigkeitsbericht mit der Überschrift "Ermittlungen an Halteranschrift".

**Rückfragen** (X = Ziffer der Direktion): Verkehrsermittlungsdienst Dir X K 23, Tel. X 72300 · Unfallkommando Dir X K 24, Tel. X 72400, außerhalb der Bürozeiten X 72800 · Lagedienst X 01700.
