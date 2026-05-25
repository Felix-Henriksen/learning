# Læringslogg: Delprosjekt 0 – Bli kjent med koding og Python

## Hva jeg skulle lære

- Installere Python og kjøre scripts på Windows
- Bruke terminalen for grunnleggende navigasjon
- Forstå variabler, f-strings, og print()
- Aritmetiske operasjoner
- BrukerInput og typekonvertering
- if/else conditionals og sammenligningsoperatorer
- Lister
- Truthy og falsy-verdier
- for-loop

## Hva jeg faktisk gjorde

[Tidslinje med hva som skjedde – kort versjon]

- 23-05-2026: Installerte Python, satte opp prosjektet, lærte variabler, f-strings, print(), aritmetiske operasjoner, brukerinput og typekonvertering.
- 24-05-2026: Lærte if/else og lister.
- 24-05-2026: for-loop og startet på funksjoner

## Filer jeg har laget

- `hei.py` – mitt aller første script
- `datatyper.py` – eksperimenterte med int, str, float, bool
- `regnestykke.py` – grunnleggende operatorer
- `hilsen.py` – brukerinput med input()
- `kalkulator.py` – brukerinput + utregning + if/else for å unngå null-divisjon
- `partall_oddetall.py` – modulo + if/else
- `lister.py` - lister basics
- `handleliste.py` – lister med `in`-operatoren


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
- **Aritmetiske operatorer:** Matematiske operasjoner `+` `-` `*` `/` og `//` `**` `%`
- **Python-konvensjoner:**
  - **PEP 8:** Pythons ofisielle stilguide
  - **snake_case:** Variabler og funksjoner med små bokstaver, understrek mellom ord (`antall_studenter`).
  - **PascalCase:** Klassenavn med stor forbokstav (`Person`).
  - **STORE BOKSTAVER:** Konstanter (verdier som ikke endres).
- **Typekonvertering:** Eks. gjør int(input(skriv tall her:)) om fra en str til en int.
- **`if`/ `else` / `elif`:** Betingelser for en handling.
  - Hvis (`if`) en viss betingelse er sann, gjør handling A
  - `elif` lar deg sjekke en alternativ betingelse - gjør handling B.
  - Hvis ikke (`else`), gjør handling C.
- **Sammenligningsoperatorer:**
  - `==` er lik
  - `!=` er ikke lik
  - `<` og `>` mindre/større enn
  - `<=` og `>=` mindre/større enn eller lik
- **Lister:**
  - Syntaks `[1, 'brød', False, 1.5]`
  - **Metoder**
    - `.append` legger til nytt element på slutten av listen
    - `.remove`sletter et valgt element fra listen
  - `in`-operator sjekker om noe finnes i en liste
- **Truthy og falsy verdier:**
  - 0, 0.0, " ", [], None er "falsy" i python. Falsy-verdier er alt som regner som "tomt", "null" eller "ingenting" i python, og som derfor automatisk oppfører seg som False i en if-setning
  - Alle andre verdier er truthy, og er da True i en if-setning
  - Operatoren `or` returnerer ikke True/False, men det første truthy-elementet
- **for-loop:** Brukes til å gjenta en kodeblokk for hvert element i en samling  (f.eks. listem tekstreng eller en rekke med tall)


## Det jeg slet med

- Forstod ikke at jeg måtte stå i riktig mappe i terminalen for å kjøre filen.
  - Løsning: Brukte `cd` for å navigere til mappa, eller brukte den innebygde terminalen i VS Code som starter i riktig mappe automatisk.
  - Hvorfor jeg slet: Konseptet "current directory" var nytt for meg.
- Programmet `regnestykke.py` sa at 14 var oddetall og 13 var partall.
  - Løsning: Jeg hadde skrevet `&` istedenfor `%`. De ser like ut, men gjør forskjellige ting.
  - Hvorfor jeg slet: `&` er en gyldig operator (bitvis AND), så python ga ingen feilmelding - den bare gjorde noe annet det jeg ville.
- Programmet ga 0.066 som gjennomsnitt av tall mellom 5 og 25 - åpenbart umulig. 
  - Løsning: Oppdaget at jeg hadde snudd divisjonen: `len(liste) / sum_total` istdenfor `sumt_total / len(liste)`

## Spørsmål jeg fortsatt har

- Ingen!

## Kode-snutter jeg vil huske

### variabel, print() og f-string

\`\`\`python
navn = "Felix"
print(f"Hei, {navn}!")
\`\`\`

### noen operatorer

\`\`\`python
modulo = a % b
potens = a ** b
heltallsDivisjon = a // b
\`\`\`

### typekonvertering eksempel

\`\`\`python
tall1 = int(input("Skriv inn det første tallet: "))
\`\`\`

### if/else og sammenligningsoperatorer

\`\`\`python
if tall % 2 == 0:
    print("partall")
else:
    print("oddetall")
\`\`\`

### lister og in-operator

\`\`\`python
handleliste = ['melk', 'brød', 'juice', 'eple', 'skinke']
sjekk = input("Dobbelsjekk om produktet er med i listen: ")

if sjekk in handleliste:
    print("Ja, den er i listen!")
else:
    print("Nei, den er ikke i listen.")
\`\`\`

### for-loop med iterering med range-metoden

\`\`\`python
tall = int(input("Hvilket tall vil du se gangetabellen til? "))

for i in range(1, 11): # mellom 1 - 10
    resultat = tall * i # input ganger range (1-10)
    print(f"{tall} * {i} = {resultat}") 
\`\`\`

### for-loop med if-else
\`\`\`python
liste = [5, 10, 15, 20, 25]

biggest = liste[0]
for tall in liste:
    if tall > biggest:
        biggest = tall

print(f"Det største tallet: {biggest}")
\`\`\`