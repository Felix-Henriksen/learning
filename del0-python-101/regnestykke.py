# Tema: Operatorer (matematiske operasjoner)
# Et skript som gjør utregninger av a og b

# Variabler
a = 10 
b = 3

Addisjon = a + b
Subtraksjon = a - b
Multiplikasjon = a * b
Divisjon = a / b

Modulo = a % b # resterende etter en heltallsdivisjon
Potens = a ** b # ganger med seg selv
HeltallsDivisjon = a // b # eks. 10/3 = 3.333 - 10//3 = 3 (1 blir kastet vekk)


print(f"{a}+{b} = {Addisjon}")
print(f"{a}-{b} = {Subtraksjon}")
print(f"{a}*{b} = {Multiplikasjon}")
print(f"{a}/{b} = {Divisjon}")

print(f"{a}%{b} = {Modulo}")
print(f"{a}**{b} = {Potens}")
print(f"{a}//{b} = {HeltallsDivisjon}")


# Ekstraoppgave
# Partall/oddetall sjekk
tall = 20 # eksempeltall
if tall % 2 == 0: # hvis tallet ikke har noe rest etter delt på 2 = partall
    print(f"{tall} er et partall")
else: # hvis tallet har rest = oddetall
    print(f"{tall} er et oddetall")