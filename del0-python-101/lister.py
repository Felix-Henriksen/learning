# Tema: Lister


#Min første liste
spillere = ["Alice", "Bob", "Carol", "Dave"]
print(spillere)
print(f"Det er {len(spillere)} spillere.")

# Hent enkeltelementer
print(f"Spiller 1 er: {spillere[0]}")
print(f"Spiller 2 er: {spillere[1]}")


# Endre en spiller
spillere[1] = "Bobby"
print(spillere)

# Legg til en ny spiller
spillere.append("Eve")
print(spillere)

# Fjern en spiller
spillere.remove("Eve")
print(spillere)

# Sjekk om noen er med
if 'Alice' in spillere:
    print("Alice er med!")