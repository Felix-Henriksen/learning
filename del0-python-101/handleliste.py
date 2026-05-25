# Tema: Lister
# Skript som utfører diverse liste-funksjoner

handleliste = ['melk', 'brød', 'juice', 'eple', 'skinke']
sjekk = input("Dobbelsjekk om produktet er med i listen: ")

if sjekk in handleliste:
    print("Ja, den er i listen!")
else:
    print("Nei, den er ikke i listen.")

# Skriver ut hvor mange ting det er
#print(f"Det er {len(handleliste)} produkter")

# Skriv ut det første og siste produktet
#print(f"Det første produktet er {handleliste[0]}")
#print(f"Det siste produktet er {handleliste[4]}")

# Legg til et produkt 
#handleliste.append("ost")
#print(handleliste)

# Fjern et produkt
#handleliste.remove(handleliste[2])
#print(handleliste)

