import json
from pathlib import Path
path = Path(__file__).resolve().parent/'dogs.json'
with open(path,encoding='utf-8') as file: dogs=json.load(file)
for dog in dogs:
    if dog['age']<5:
        print(dog)
