# Opdracht 2 berekeningen
# Naam student: johnny
# Groep:

# Hier komt je code...

#ik heb dit zo gedaan wat ik vind een lijst zonder leestekens en onder elkaar netter.
gasten = ["Johnny", "Paul", "Kees", "Marie", "Hilda"]

print("Oorspronkelijke lijst:")
for gast in gasten:
    print(gast)

gasten.remove("Marie")
print("\nLijst zonder Marie:")
for gast in gasten:
    print(gast)

kees_index = gasten.index("Kees")
gasten.insert(kees_index + 1, "George")
print("\nUiteindelijke lijst met George naast Kees:")
for gast in gasten:
    print(gast)
