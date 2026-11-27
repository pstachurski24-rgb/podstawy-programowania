import json
from pathlib import Path
path = Path(__file__).resolve().parent/'computer.json'
with open(path,encoding='utf-8') as file: data=json.load(file)
for key,value in data.items():
    print(key, ':', value)
