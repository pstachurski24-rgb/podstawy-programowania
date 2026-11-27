import json
from pathlib import Path
path = Path(__file__).resolve().parent/'cities.json'
with open(path,encoding='utf-8') as file: data=json.load(file)
for city in data:
    for key,value in city.items():
        print(key, ':',value)
    print()
