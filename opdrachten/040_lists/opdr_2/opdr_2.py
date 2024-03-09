# Opdracht 2 lists
# Naam student:
# Groep:


rivier_info = {
    "rijn": ["nederland", "duitsland", "Frankrijk"],
    "maas": ["nederland", "belgië", "duitsland"],
    "nijl": ["egypte", "soedan", "oeganda"]
}

rivieren = list(rivier_info.keys())
# rivieren is nu een list met alleen de riviernamen: ['rijn', 'maas', 'nijl']

# Hier jouw code.....

eerste_rivier_naam = rivieren[0]
eerste_rivier_land_2 = rivier_info[eerste_rivier_naam][1]


print(f"De rivier {eerste_rivier_naam.capitalize()} stroomt onder andere door {eerste_rivier_land_2.capitalize()}")


tweede_rivier_naam = rivieren[1]
eerste_rivier_land_1 = rivier_info[eerste_rivier_naam][0]


print(f"De rivier {tweede_rivier_naam.capitalize()} stroomt onder andere door {eerste_rivier_land_1.capitalize()}")


derde_rivier_naam = rivieren[2]
derde_rivier_land_3 = rivier_info[derde_rivier_naam][2]


print(f"De rivier {derde_rivier_naam.capitalize()} stroomt onder andere door {derde_rivier_land_3.capitalize()}")
