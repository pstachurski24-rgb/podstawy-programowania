import json
from pathlib import Path
path = Path(__file__).resolve().parent/'euro.json'
with open(path,encoding='utf-8') as file: data=json.load(file)
print(f"{'Date':<16}{'Buying Rate':<16}{'Selling Rate':<16}")
print('='*48)
for rate in data['rates']:
    print(f"{rate['effectiveDate']:<16}{rate['bid']:<16.4f}{rate['ask']:<16.4f}")
