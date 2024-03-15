# Opdracht 1 functies
# Naam student:
# Groep:


def kilometers_naar_miles(km):
    # je code komt hier
    # het woordje pass hieronder kun je weghalen
    miles = km * 0.621371
    return miles

def miles_naar_kilometers(miles):
    # je code komt hier
    # het woordje pass hieronder kun je weghalen
    km = miles * 1.60934
    return km


kilometers = 1223
miles = 867
afstand_in_mijlen = kilometers_naar_miles(kilometers)
afstand_in_kilometers = miles_naar_kilometers(miles)
print(f"{kilometers} kilometers = {afstand_in_mijlen} mijlen")
print(f"{miles} mijlen = {afstand_in_kilometers} kilometers")