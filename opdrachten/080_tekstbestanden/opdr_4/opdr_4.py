# Opdracht 4 Tekst opslaan
# Naam student:
# Groep:


# Party enquete
# Definieer de vragen in een lijst
# Definieer de vragen in een lijst
vragen = [
    "Wat is je voornaam? ",
    "Wat is je achternaam? ",
    "Wat neem je mee aan drank? ",
    "Wat neem je mee om te eten? "
]

# Maak een lege lijst om de antwoorden van de feestgangers op te slaan
feestgangers = []

# Loop door elke vraag in de lijst
for vraag in vragen:
    # Vraag de gebruiker om input en sla het antwoord op in de lijst van feestgangers
    antwoord = input(vraag)
    feestgangers.append(antwoord)

# Maak een dictionary voor de huidige feestganger
feestganger = {
    "voornaam": feestgangers[0],
    "achternaam": feestgangers[1],
    "drank": feestgangers[2],
    "eten": feestgangers[3]
}

# Druk de vragen en antwoorden af
print("Uitvoer op het scherm:")
for i, vraag in enumerate(vragen):
    print(f"{i+1}. {vraag}")
    print(feestgangers[i])
print("\nBedankt voor het invullen!\nSee you at the party.")

# Sla de antwoorden op in een tekstbestand
with open("feestgangers.txt", "a") as f:
    f.write("----\n")
    for key, value in feestganger.items():
        f.write(f"{key}: {value}\n")
    f.write("\n")


    # Open het tekstbestand in leesmodus
with open("feestgangers.txt", "r") as f:
    # Lees en print de inhoud van het tekstbestand regel voor regel
    for line in f:
        print(line.strip())  # strip() wordt gebruikt om het extra regeleinde te verwijderen
