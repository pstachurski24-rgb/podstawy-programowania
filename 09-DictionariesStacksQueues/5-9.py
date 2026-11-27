import csv
from pathlib import Path
base = Path(__file__).resolve().parent
provinces = {}
with open(base/'province.csv', encoding='utf-8',newline='') as file:
    for row in csv.DictReader(file):
        for prefix in row['Prefixes'].split(';'):
            provinces[prefix.strip().upper()] = row['Province']
counts = {name:0 for name in set(provinces.values())}
unknown = 0
with open(base/'vehicle.txt',encoding='utf-8') as file:
    for line in file:
        plate = line.strip().upper().replace(' ','')
        if not plate: continue
        province = provinces.get(plate[0])
        if province: counts[province]+=1
        else: unknown+=1
for province,count in sorted(counts.items()):
    print(f'{province}: {count}')
print('Unknown:',unknown)
