# Opdracht 1 input function
# Naam student:
# Groep:

# Hier komt je code, maak gebruik van de input functie om de lengte van de rechthoekzijden van de driehoek op te vragen.

#a*a + b*b = c*c
import math

a = float(input("Geef de lengte van de eerste zijde: "))
b = float(input("Geef de lengte van de tweede zijde: "))

c = round(math.sqrt(pow(a,2) + pow(b,2)),2)

print("De lengte van de schuine zijde is:", c)

 