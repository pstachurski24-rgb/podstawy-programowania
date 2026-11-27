from pathlib import Path
BASE = Path(__file__).resolve().parent

# Section 2, item 5: append shopping items until 0.
shopping_list = BASE / 'shopping_list.txt'

def add_product(file_name, product_name):
    with file_name.open('a', encoding='utf-8') as file:
        file.write(product_name + '\n')

while True:
    product = input('Enter product name (0 stops): ')
    if product == '0':
        break
    add_product(shopping_list, product)
print('Shopping list updated.')
