# Opdracht 3 input functie
# Naam student:
# Groep:

# Hier komt je code...

steden = []

steden.insert(0, input("Vul een stad in: "))
steden.insert(1, input("Vul een stad in: "))
steden.insert(2, input("Vul een stad in: "))
steden.insert(3, input("Vul een stad in: "))
steden.insert(4, input("Vul een stad in: "))

output = ', '.join([f'"{stad}"' for stad in steden])
output = '[' + output + ']'
print(output)