lis=[{'name': 'Blah1', 'age': 'x'}, {'name': 'Blah2', 'age': 'y'}, {'name': None, 'age': None}]

for person_dict in lis:
    if person_dict['name'] == None:
        lis.remove(person_dict)

print lis

