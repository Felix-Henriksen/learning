# Tema: BrukerInput
# Skript som leser inn brukerinput og gjør enkle utregninger 

tall1 = int(input("Skriv inn det første tallet: "))
tall2 = int(input("Skriv inn det andre tallet: "))

addisjon = tall1 + tall2
subtraksjon = tall1 - tall2
multiplikasjon = tall1 * tall2

print(f"{tall1} + {tall2} = {addisjon}")
print(f"{tall1} - {tall2} = {subtraksjon}")
print(f"{tall1} * {tall2} = {multiplikasjon}")

# if/else sjekk - gir feilmelding hvis man prøver å dele på 0
if tall2 == 0:
    print("Kan ikke deles på 0")
else:
    divisjon = tall1 / tall2 # Må bli definert inne i else
    print(f"{tall1} / {tall2} = {divisjon}")