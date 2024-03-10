# Opdracht 1 input function
# Naam student:
# Groep:

# Hier komt je code, maak gebruik van de input functie om de lengte van de rechthoekzijden van de driehoek op te vragen.

#a*a + b*b = c*c

for i in range(3):  

    print("Geef de lengte van de eerste zijde:")
    pyth_berekening_str = input()
    invoer_eerste_str = float(pyth_berekening_str)
    resultaatA = int(invoer_eerste_str ** 2)
    
    print("Geef de lengte van de tweede zijde:")
    pyth2_berekening_str = input()
    invoer_tweede_str = float(pyth2_berekening_str)
    resultaatB = int(invoer_tweede_str ** 2)

    resultaatC = resultaatA+resultaatB 
    resultaatD = int(resultaatC ** 0.5)

    if i == 2:  
        resultaatD = round(resultaatC ** 0.5, 14)
        print()
        print(f"De lengte van de schuine zijde is: {resultaatD}")
        print()
    else:
        resultaatD = int(resultaatC ** 0.5)
        print()
        print(f"De lengte van de schuine zijde is: {resultaatD}")
        print()
 