def sanitize(line):
   new_lst = []
   lst = t.split(',')
   for item in lst:
       new_lst.append(item.lower().rstrip().strip())
   return new_lst

def create_person(lst):
    person = {"voornaam": "", "tussenvoegsel": "", "achternaam": ""}
    person["voornaam"] = lst[0]
    person["tussenvoegsel"] = lst[1]
    person["achternaam"] = lst[2]
    return person

def add_fullname(person):
    if person["tussenvoegsel"] == "":
        person['full_name'] = f"{person['voornaam'].title()} {person['achternaam'].title()}"
    else:
        person['full_name'] = f"{person['voornaam'].title()} {person['tussenvoegsel']} {person['achternaam'].title()}"
    return person

def print_persons(persons, filter=["full_name"]):
    counter = 0
    for person in persons:
        counter += 1
        for attr in filter:
            print(person[attr].title(), end=" ")
        print(end="\n")
    print(f"Er zijn in totaal {counter} personen")