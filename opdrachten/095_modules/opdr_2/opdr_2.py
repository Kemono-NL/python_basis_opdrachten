# Opdracht 1 modules
# Naam student:
# Groep:

from my_modules import csv

persons = []
for line in open("test.csv", 'rt'):
    lst = csv.sanitize(line)
    person = csv.create_person(lst)
    person = csv.add_fullname(person)
    persons.append(person)

csv.print_persons(persons)

