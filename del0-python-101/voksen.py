# Tema: if/else og elif
# Enkelt skript som sjekker om man er voksen eller mindreårig

alder = int(input("Hvor gammel er du? "))

# Oppgave 1:
# if alder >= 18:
#     print("Du er voksen.")
# else:
#     print("Du er mindreårig.")


# Oppgave 2:
if alder < 13:
    print("Du er et barn.")
elif alder < 20:
    print("Du er tenåring.")
elif alder < 65:
    print("Du er voksen.")
else:
    print("Du er pensjonist")
