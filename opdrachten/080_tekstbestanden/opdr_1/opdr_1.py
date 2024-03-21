# Opdracht 1 while-loops
# Naam student:
# Groep:

# Jouw code komt hier
Lijst = []

vragen = [
    "Wat is jouw naam?: ",
    "Wat vind je van de huidige regering?: ",
    "Wat vind je van de Python-lessen tot nu toe?: ",
    "Wat vind jij de mooiste stad van Nederland?: "
]
for vraag in vragen:
    antwoord = input(vraag)
    Lijst.append((vraag, antwoord))


print(Lijst)

# Open een bestand om de antwoorden in te schrijven ('a' staat voor append mode, dit zorgt ervoor dat de antwoorden aan het einde van het bestand worden toegevoegd)
with open("antwoorden.txt", "a") as bestand:
    # Loop door elke vraag en antwoord in de lijst en schrijf deze naar het bestand
    for vraag, antwoord in Lijst:
        bestand.write(vraag + antwoord + "\n")
    # Voeg een lege regel toe na alle antwoorden
    bestand.write("\n")

    
