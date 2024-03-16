# Opdracht 1 functies
# Naam student:
# Groep:

import math
#volume = l x b x h
def kubus_vol(m):
    m = zijde ** 3
    return m
   
#pi = 3.141592653589793
def bol_vol(r):
    B = (4/3) * math.pi * r ** 3
    return B
    
zijde = 5
radius = 4

print("De inhoud van deze kubus is:",kubus_vol(5))
print("De inhoud ven deze bol is:",bol_vol(4))