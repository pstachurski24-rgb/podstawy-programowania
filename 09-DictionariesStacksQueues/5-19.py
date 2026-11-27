import json
from pathlib import Path
path = Path(__file__).resolve().parent/'reservations.json'
def load_reservations(path):
    with open(path,encoding='utf-8') as file: return json.load(file)
def summary(reservations):
    return {'rooms':len({r['room'] for r in reservations}),
            'paid_count':sum(r['paid'] for r in reservations),
            'unpaid_count':sum(not r['paid'] for r in reservations),
            'paid_total':round(sum(r['amount'] for r in reservations if r['paid']),2),
            'unpaid_total':round(sum(r['amount'] for r in reservations if not r['paid']),2)}
for key,value in summary(load_reservations(path)).items():
    print(key, ':',value)
