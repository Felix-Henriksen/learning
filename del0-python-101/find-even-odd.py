# Tema: for-loop med if-else
# Skript som finner hvilket tall som er partall og oddetall i en liste

tall_liste = [2, 7, 4, 50, 15, 45, 30]

for tall in tall_liste: # sjekker gjennom listen
    if tall % 2 == 0: # betingelsen for partall
        print(f"{tall} er et partall!")
    else: # hvis den ikke er partall = oddetall
        print(f"{tall} er et oddetall!")