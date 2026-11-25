import re, sys, json
S, V = sys.argv[1:3]
kat = {z[:6] for z in open(f'{V}/recht/tbkat.txt', encoding='utf-8') if re.match(r'\d{6} \|', z)}
rows = json.load(open(f'{S}/beispiele.json'))
tb = {}
for f in ('a', 'b'):
    for z in open(f'{S}/beispiele_tbnr_{f}.tsv', encoding='utf-8'):
        t = z.rstrip('\n').split('\t')
        if t[0].strip().isdigit():
            tb[int(t[0])] = ([x.strip() for x in t[1].split(',') if x.strip()] if len(t) > 1 else [], t[2] if len(t) > 2 else '')
assert sorted(tb) == list(range(1, len(rows) + 1)), (len(tb), len(rows))
tb[25] = (['101136', '109649'], 'Parkrempler rückwärts: Dienstkunde nennt die Parklücken-Nummer')
bad = [n for v in tb.values() for n in v[0] if n not in kat]
assert not bad, bad
UA = {'1': 'Zusammenstoß mit Fahrzeug, das steht, anfährt oder anhält (ruhender Verkehr)',
      '2': 'Zusammenstoß mit Fahrzeug, das vorausfährt oder wartet',
      '3': 'Zusammenstoß mit Fahrzeug, das seitlich in gleicher Richtung fährt',
      '4': 'Zusammenstoß mit Fahrzeug, das entgegenkommt',
      '5': 'Zusammenstoß mit Fahrzeug, das einbiegt oder kreuzt',
      '6': 'Zusammenstoß zwischen Fahrzeug und Fußgänger',
      '7': 'Aufprall auf Hindernis auf der Fahrbahn',
      '8/9': 'Abkommen von der Fahrbahn nach rechts (8) oder links (9)',
      '0': 'Unfall anderer Art'}
def lage(s):
    s = s.replace('(Q, S)', '(Verursacher, schleudert)').replace('(Q, T)', '(Verursacher, steht)')
    s = s.replace('(Q)', '(Verursacher)').replace('(T)', '(steht)').replace('(S)', '(schleudert)').replace('(hohl)', '(rückwärts)')
    s = re.sub(r'\s*\[\?\]', '', s).replace('schleudert (schleudert)', 'schleudert')
    return s.strip()
def urs(u, text):
    t = text.lower()
    rechts = bool(re.search(r'nach rechts|rechtsabbieg|grünpfeil', t)); links = bool(re.search(r'nach links|linksabbieg|linksüberhol', t))
    ab = '35' if 'linksabbieg' in t else '34' if rechts and not links else '35' if links and not rechts else '34/35'
    u = re.sub(r'(?<![\d/])35(?!\d)', ab, u)
    zehn = '10' if re.search(r'radweg|gehweg|furt|sonderfahrstreifen|busspur|lichtzeichen|straßenteil|radfahrstreifen', t) else '08' if 'geisterfahrer' in t else '09' if 'z 267' in t else '08/09/10'
    u = re.sub(r'(?<![\d/])10(?!\d)', zehn, u)
    return u.replace(' u. ', ' und ')
out, cur, prev, kept, prev_u = [], None, '', 0, ''
for i, r in enumerate(rows, 1):
    sk = r.get('Skizze') or r.get('Skizze (kurz)') or ''
    if sk.strip().lower().startswith('dto'):
        rest = sk.strip()[4:].strip(' .')
        sk = prev + (', ' + rest if rest else '')
    elif sk.strip() not in ('–', '-', ''):
        prev = sk
    if i == 191:
        continue  # Lkw-Benutzungsverbot bei Nebel: alte TBNR entfallen, heutige Entsprechung unklar
    if r['Typ'].strip() in ('–', '-') or r['Typ'].startswith('('):
        continue
    if r['ua'] != cur:
        cur = r['ua']
        out += ['', f"## Unfallart {cur.replace('/', ' und ')}: {UA[cur]}", '', '| Fall | Lage in der Skizze | Typ | Ursachen | TBNR |', '|---|---|---|---|---|']
    fall = re.sub(r'\s+', ' ', r['Beschreibung']).replace('|', '/').strip()
    fall = re.sub(r'^… ', '', fall)
    l = lage(sk) if sk.strip() not in ('–', '-') else ''
    typ = re.sub(r'\s*\(rot\)', '', r['Typ'])
    u = r['Urs'].strip()
    u = prev_u if u.lower().startswith('dto') else u
    prev_u = u
    out.append(f"| {fall} | {l} | {typ} | {urs(u, fall + ' ' + l)} | {', '.join(tb[i][0]) or '–'} |")
    kept += 1
kopf = f"""# Musterfälle: Unfallart, Unfalltyp, Ursachen, Tatbestandsnummer

{kept} Standardsituationen aus Anlage 3 der GA PPr St 5/2008 (Dienstkunde der Polizei Berlin), geordnet nach Unfallart.
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
"""
open(f'{V}/ref/beispiele.md', 'w', encoding='utf-8').write(kopf + '\n'.join(out) + '\n')
print(kept, 'Fälle;', len(out), 'Zeilen')
print('Bemerkungen:'); [print(' ', k, v[1]) for k, v in sorted(tb.items()) if v[1] and not re.search(r'ersetzt|gestrichen|Reihenfolge', v[1])]
