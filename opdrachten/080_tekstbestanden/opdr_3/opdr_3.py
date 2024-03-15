# Opdracht 3 Tekst opslaan
# Naam student:
# Groep:

zin = "Deze zin wil ik gaan encrypten, dat lijkt me leuk"
verschoven_zin = ""

# Loop door elk karakter in de zin
for karakter in zin:
    # Verschuif alleen letters
    if karakter.isalpha():
        verschoven_karakter = chr(ord(karakter) + 5)
        if verschoven_karakter > 'z' or (karakter.isupper() and verschoven_karakter > 'Z'):
            verschoven_karakter = chr(ord(karakter) - 21)
    else:
        verschoven_karakter = karakter  # Behoud spaties en leestekens ongewijzigd
    verschoven_zin += verschoven_karakter  # Voeg het verschoven karakter toe aan de zin

# Druk de verschoven zin af
print("Verschoven zin:", verschoven_zin)


