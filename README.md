# Pirmais-modelis-no-nulles

## Projekta apraksts

Šajā projektā tiek izveidots mašīnmācīšanās modelis, kas prognozē pingvīna sugu pēc tā ķermeņa īpašībām.

Projektā tiek izmantota Palmer Penguins datu kopa, kurā ir informācija par 344 pingvīniem un trīs to sugām: Adelie, Gentoo un Chinstrap.

Modelis izmanto četras pazīmes:
- Knābja garums (`bill_length_mm`)
- Knābja dziļums (`bill_depth_mm`)
- Pleznas garums (`flipper_length_mm`)
- Ķermeņa masa (`body_mass_g`)

## Izmantotās tehnoloģijas

- Python - programmēšanas valoda
- pandas - datu nolasīšanai un apstrādei
- scikit-learn - modeļa izveidei un testēšanai

## Projekta faili

- `dati/penguins.csv` - sākotnējie dati
- `dati/AVOTS.txt` - datu avots un lejupielādes datums
- `01_tirisana.py` - datu tīrīšanas skripts
- `02_modelis.py` - modeļa apmācība un testēšana
- `tirs.csv` - attīrītie dati
- `rezultati.md` - rezultātu analīze un secinājumi

## Projekta palaišana

1. Lejupielādēt projektu no GitHub.
2. Atvērt projekta mapi VS Code.
3. Instalēt nepieciešamās bibliotēkas:

python -m pip install pandas scikit-learn

4. Palaist datu tīrīšanas skriptu:

python 01_tirisana.py

5. Palaist modeļa apmācības skriptu:

python 02_modelis.py

## Rezultāti

Pēc datu tīrīšanas no 344 rindām palika 333 rindas.

Modeļa testēšanas rezultāti:
- Modeļa precizitāte: 94.03%
- Bāzes līnijas precizitāte: 43.28%

Divas svarīgākās pazīmes:
1. Pleznas garums (`flipper_length_mm`) - 52.70%
2. Knābja garums (`bill_length_mm`) - 36.97%

Modelis sasniedza par 50.75 procentpunktiem augstāku precizitāti nekā bāzes līnija.

Detalizētāka rezultātu analīze ir pieejama failā `rezultati.md`.