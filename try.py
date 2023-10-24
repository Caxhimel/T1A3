import json

with open('docs/types.json') as f:
    types = json.load(f)
    print(types)

ex_list = []

for keys in types.keys():
    ex_list.append(keys)

print(ex_list)

    