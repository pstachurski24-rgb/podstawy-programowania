from pathlib import Path
BASE = Path(__file__).resolve().parent

# Section 3, item 4: sum Euro amounts extracted from report.
# Matches forms like €12.50, 7,40 € and 3 € in the example data.
import re
from decimal import Decimal

with (BASE / 'report.txt').open('r', encoding='utf-8') as file:
    email = file.read()
pattern = r'(?:€\s*(\d+(?:[.,]\d{1,2})?)|(\d+(?:[.,]\d{1,2})?)\s*€)'
amounts = re.findall(pattern, email)
total = Decimal('0')
for before, after in amounts:
    amount = before or after
    total += Decimal(amount.replace(',', '.'))
print('Total money spent:', f'{total:.2f} €')
