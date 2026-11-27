import json
from pathlib import Path
name = input('Product name: ').strip()
while True:
    try:
        price = round(float(input('Price: ').replace(',','.')),2)
        if price<0: raise ValueError('Price cannot be negative')
        break
    except ValueError: print('Enter a nonnegative number')
while True:
    paid_input = input('Paid (yes/no): ').strip().lower()
    if paid_input in ('yes','no'): break
    print('Enter yes or no')
product = {'name':name,'price':price,'paid':paid_input=='yes'}
path = Path(__file__).resolve().parent/'product.json'
with open(path,'w',encoding='utf-8') as file:
    json.dump(product,file,ensure_ascii=False,indent=4)
print('Saved:',path.name)
