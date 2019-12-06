import json

data = json.loads("./desrouleaux/incidents.json")

for item in data:
    print(item)
