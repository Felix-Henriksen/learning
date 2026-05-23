# Skript som leser inn brukerinput og gjør enkle utregninger 

tall1 = int(input("Skriv inn det første tallet: "))
tall2 = int(input("Skriv inn det andre tallet: "))

addisjon = tall1 + tall2
subtraksjon = tall1 - tall2
multiplikasjon = tall1 * tall2
divisjon = tall1 / tall2

print(f"{tall1} + {tall2} = {addisjon}")
print(f"{tall1} - {tall2} = {subtraksjon}")
print(f"{tall1} * {tall2} = {multiplikasjon}")
print(f"{tall1} / {tall2} = {divisjon}")