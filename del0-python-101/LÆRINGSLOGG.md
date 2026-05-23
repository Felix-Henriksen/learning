# Læringslogg: Delprosjekt 0 – Bli kjent med koding og Python

## Hva jeg skulle lære

- Installere Python og kjøre scripts på Windows
- Bruke terminalen for grunnleggende navigasjon
- Forstå variabler, f-strings, og print()
- (Resten av målene fra tutor-planen)

## Hva jeg faktisk gjorde

- 2026-05-23: Verifiserte at Python 3.12 fungerer via `py`-launcheren. Hadde gammel Python 3.8 liggende fra før som forstyrret PATH. Valgte å bruke `py` i terminalen istedenfor å rote med PATH.
- 2026-05-23: Lagde mappestruktur for prosjektet i Dokumenter.
- 2026-05-23: Skrev og kjørte mitt første Python-script `hei.py`.

## Nye konsepter jeg lærte

- **`py`-launcher:** Et verktøy på Windows som kan kjøre flere Python-versjoner. Jeg bruker `py` istedenfor `python`-kommandoen for å sikre at jeg treffer 3.12.
- **PATH:** En liste Windows har over mapper den leter i når jeg skriver kommandoer i terminalen.
- **`mkdir`:** Kommando som lager en ny mappe.
- **`cd`, `dir`/`ls` og `pwd`:** Kommandoer for å bevege seg mellom mapper og se hva som ligger i dem.
- **Variabel:** Et navngitt "rom" som lagrer en verdi.
- **f-string:** En tekst-string i Python som lar meg sette inn verdier fra variabler med `{}`.
- **print-funksjon:** print() - en funksjon som skriver ut informasjon i terminalen.
- **Kjøring av skriptet:** Kjørte skriptet både i PowerShell og i innebygd Terminal på VSCode.
- **.gitignore:** En fil som bestemmer hvilke filer som inneholder hemmeligheter ikke skal vises i github
- **git status, git add ., git commit -m, git push:** Git kommandoer som sender over nye oppdateringer til github repo.

## Det jeg slet med

- Forstod ikke at jeg måtte stå i riktig mappe i terminalen for å kjøre filen.
  - Løsning: Brukte `cd` for å navigere til mappa, eller brukte den innebygde terminalen i VS Code som starter i riktig mappe automatisk.
  - Hvorfor jeg slet: Konseptet "current directory" var nytt for meg.

## Spørsmål jeg fortsatt har

- Ingen!

## Kode-snutter jeg vil huske

\`\`\`python
navn = "Felix"
print(f"Hei, {navn}!")
\`\`\`
