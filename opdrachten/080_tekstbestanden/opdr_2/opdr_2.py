# Opdracht 2 tekstbestanden
# Naam student:
# Groep:

import random
prompt = "Raad mijn geheime getal \n"
geheim_getal = random.randint(1, 100)
getal = 0
# De rest moet jij doen.....
while getal != geheim_getal:
    getal = int(input("raad mijn geheime getal: "))
    if geheim_getal < getal:
            print(f"Lager")
    elif geheim_getal > getal:
            print(f"Hoger")
print("Gefeliciteerd!! Ga door voor de wasmaschine!!")
