# Læringslogg: Linux 101 – Grunnleggende Linux

## Hva jeg skulle lære

- Linux-filsystemet og hvordan det henger sammen under én rot (`/`)
- Navigasjon i terminalen
- Lage og slette mapper og filer
- Forskjellen på mappe og fil
- Tab-fullføring og effektiv terminalbruk

## Hva jeg faktisk gjorde

- 07-06-2026: Satte opp Git på MSI-laptopen (homelab), klonet `learning`-repoet, og opprettet `linux-101`-mappa for Linux-læring.
- 07-06-2026: Lærte navigasjon (`pwd`, `ls`, `cd`), oppretting/sletting av mapper, og forskjellen på `mkdir` og `touch`.

## Filer og struktur jeg har laget

- `linux-101/` – mappe for Linux-grunnleggende
- `LAERINGSLOGG.md` – denne loggen

## Nye konsepter jeg lærte

- **Linux-filsystemet:** Alt henger under én rot `/`. Min hjemmemappe er `/home/hauscat/`, og `~` er en snarvei dit.
- **Navigasjonskommandoer:**
  - `pwd` – vis hvor jeg står (print working directory)
  - `ls` / `ls -l` / `ls -la` – list innhold (`-l` lang format, `-a` viser skjulte filer)
  - `cd <mappe>` – gå inn i en mappe
  - `cd ..` – gå ett nivå opp
  - `cd ~` eller `cd` – gå til hjemmemappa
  - `cd -` – gå tilbake til forrige mappe jeg var i
- **Spesialmapper:** `.` betyr "denne mappa", `..` betyr "mappa over".
- **Skjulte filer:** Filer/mapper som starter med `.` (f.eks. `.bashrc`, `.config`) vises ikke med vanlig `ls`, kun med `ls -a`.
- **`mkdir` vs `touch`:**
  - `mkdir <navn>` lager en MAPPE
  - `touch <navn>` lager en (tom) FIL
  - Endelsen (`.md`, `.txt`) betyr ingenting for Linux – det er bare en del av navnet. En mappe kan hete "noe.md" og er fortsatt en mappe.
- **Slette:**
  - `rmdir <mappe>` – sletter TOMME mapper (nekter hvis det er innhold – en sikkerhet)
  - `rm -r` / `rm -rf` – sletter mapper MED innhold. FARLIG, ingen angre, ingen papirkurv.
- **Tab-fullføring:** Trykk Tab for å autofullføre fil-/mappenavn. Sparer tid og hindrer skrivefeil med rare tegn.
- **Git på ny maskin:** Klonet repo med `git clone <url>`. Offentlige repoer krever ikke token for å klone (lese), men push (skrive) krever Personal Access Token.

## Det jeg slet med

- Lagde `test1,` med komma ved en feil fordi jeg skrev `mkdir test1, test2, test3`.
  - Løsning: Slettet med `rmdir "test1,"` (anførselstegn rundt navn med spesialtegn), og lærte at riktig syntaks er `mkdir test1 test2 test3` med MELLOMROM.
  - Hvorfor jeg slet: I Linux skiller mellomrom argumenter. Komma blir en del av navnet.
- Brukte `mkdir LAERINGSLOGG.md` og fikk en mappe istedenfor en fil.
  - Løsning: Slettet mappa med `rmdir`, og lagde fila med `touch` (eller via VS Code).
  - Hvorfor jeg slet: Trodde `.md`-endelsen gjorde det til en fil, men endelsen betyr ingenting for Linux.

## Spørsmål jeg fortsatt har



## Kommandoer jeg vil huske

\`\`\`bash
pwd                    # hvor er jeg
ls -la                 # list alt, inkludert skjulte filer
cd ~                   # hjem
cd -                   # forrige mappe
mkdir prosjekt         # lag mappe
touch notater.md       # lag fil
rmdir tom-mappe        # slett tom mappe
\`\`\`