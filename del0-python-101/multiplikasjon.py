# Tema: for-loop, range-metode
# Skript som går gjennom gangetabell fra tallet skrevet som brukerinput. 

tall = int(input("Hvilket tall vil du se gangetabellen til? "))

for i in range(1, 11): # mellom 1 - 10
    resultat = tall * i # input ganger range (1-10)
    print(f"{tall} * {i} = {resultat}") 