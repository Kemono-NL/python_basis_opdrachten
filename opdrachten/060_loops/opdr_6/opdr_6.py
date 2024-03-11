# Opdracht 3 input functie
# Naam student:
# Groep:

# Hier komt je code...

# Hier start de for-loop

# Lijst met pizza's
My_list = ['margharita', 'calzone', 'verdi', 'olivio', 'quattro stagioni']
My_list.sort()
print("Mijn lijst gesorteerd:", My_list)
#smaak toegevoegd   
My_list.append('yo-favorito')
print("Smaak toegevoegd: ", My_list)
#verwijder een pizza
del My_list[2]
print("Verwijder een pizza:", My_list)
#de eerste 3 pizza's
print("De eerste 3 pizza's", My_list[:3])
#print alleen de middelste uit het gesorteerde lijst
print("De middelste:", f"['{My_list[2]}']")
#print de laatste 3 
print("De laatste 3:", My_list[-3:])

