import csv
import json


with open('ascii.csv') as csv_file:
    reader = csv.reader(csv_file, delimiter='\t', escapechar='\\')
    
    # strip header
    next(reader)

    characters = []
    for n, line in enumerate(reader):
        c = line[4]
        name = line[5]
        if n < 65 or n > 90:
            print(f"{n}")
            name = name.lower()
            name = name.capitalize()
            
        characters.append({
            #"int": int(line[0]),
            "char": c,
            "name": name,
        })



with open('ascii.json', 'w') as fp:
    json.dump(characters, fp)

