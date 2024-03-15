# Opdracht 2 tekstbestanden
# Naam student:
# Groep:

import random
prompt = "Raad mijn geheime getal \n"
geheim_getal = random.randint(1, 100)
getal = 0
aantal_beurten = 0
# De rest moet jij doen.....
while getal != geheim_getal:
    getal = int(input("raad mijn geheime getal: "))
    aantal_beurten += 1
    if geheim_getal < getal:
            print(f"Lager, dit is beurt {aantal_beurten}")
    elif geheim_getal > getal:
            print(f"Hoger, Dit is beurt {aantal_beurten}")
print("Gefeliciteerd!! Ga door voor de wasmachine!!")
