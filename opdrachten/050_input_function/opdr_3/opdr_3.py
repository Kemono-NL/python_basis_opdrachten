# Opdracht 3 input functie
# Naam student:
# Groep:

# Hier komt je code...

steden = []

while len(steden) < 5:
    nieuwe_stad = input("Voer een stad in (druk op Enter om te stoppen): ").strip()

    if not nieuwe_stad:
        break

    steden.append(nieuwe_stad)

    steden = steden[:5]

    steden.sort(reverse=True)

print(steden)

