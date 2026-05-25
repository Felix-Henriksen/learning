# Tema: for-loop 
# Skript som regner: 
# totalsummen av verdien i en liste.
# finner det største og minste tallet i listen
# regner gjennomsnittet av listen

liste = [5, 10, 15, 20, 25]

# Regner totalsummen av elementene i listen
sum_total = 0
for tall in liste:
    sum_total += tall # ta gammel verdi sum_total, legg til tall, lagre tilbake i sum_total

print(f"Totalt er summen: {sum_total}") # Utenfor løkka - printer bare totalsummen

# Henter ut det største tallet i listen
biggest = liste[0]
for tall in liste:
    if tall > biggest:
        biggest = tall

print(f"Det største tallet i listen er: {biggest}")

# Henter ut det minste tallet i listen
smallest = liste[0]
for tall in liste:
    if tall < smallest:
        smallest = tall

print(f"Det minste tallet i listen er: {smallest}")

# Finner gjennomsnittet av elementene i listen
avg =  sum_total / len(liste)
print(f"Gjennomsnittet er: {avg}")