# Opdracht 4 condities
# Naam student:
# Groep:



toppings = [("olijven", 4.50), ("kaas", 3.50), ("salami", 3.00), ("pepperoni", 2.00), ("ansjovis", 2.50)]
beschikbare_toppings = [topping[0] for topping in toppings]

keuze = input(f"Maak een keuze uit onze toppings: {beschikbare_toppings} \n")

# Hier de rest van jouw code...
if keuze in beschikbare_toppings:
    prijs_topping = [topping[1] for topping in toppings if topping[0] == keuze][0]
    print(f"U heeft {keuze} besteld. Dat kost {prijs_topping} euro.")
else:
    print("Uw keuze zit niet in ons assortiment.")
