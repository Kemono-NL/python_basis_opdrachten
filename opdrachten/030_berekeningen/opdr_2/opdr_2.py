# Opdracht 2 berekeningen
# Naam student:
# Groep:

# Hier komt je code...

def celsius_to_fahrenheit(celsius):
    return (celsius * 9/5) + 32

def fahrenheit_to_celsius(fahrenheit):
    return (fahrenheit - 32) * 5/9

# Eerste set waarden
c1 = -12
f1 = 102

# Conversie en output
converted_f1 = celsius_to_fahrenheit(c1)
print(f"{c1} graden Celsius is gelijk aan {converted_f1:.1f} graden Fahrenheit.")

converted_c1 = fahrenheit_to_celsius(f1)
print(f"{f1} graden Fahrenheit is gelijk aan {converted_c1:.1f} graden Celsius.")

print()

# Tweede set waarden
c2 = 62.2
f2 = 96

# Conversie en output
converted_f2 = celsius_to_fahrenheit(c2)
print(f"{c2} graden Celsius is gelijk aan {converted_f2:.1f} graden Fahrenheit.")

converted_c2 = fahrenheit_to_celsius(f2)
print(f"{f2} graden Fahrenheit is gelijk aan {converted_c2:.1f} graden Celsius.")
