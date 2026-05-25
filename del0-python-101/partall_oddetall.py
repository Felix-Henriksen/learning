# Tema: if/else
# Skript som sjekker om brukerinput er partall eller oddetall

tall = int(input("Skriv inn tallet her: "))

if tall % 2 == 0:
    print(f"{tall} er partall")
else:
    print(f"{tall} er oddetall")
