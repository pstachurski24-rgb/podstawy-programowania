from pathlib import Path
BASE = Path(__file__).resolve().parent

# Section 4, item 11: price below 60 AND stock below 40.
import csv
with (BASE / 'clothing.csv').open('r', encoding='utf-8', newline='') as file:
    reader = csv.DictReader(file)
    for row in reader:
        if float(row['Price']) < 60 and int(row['Stock']) < 40:
            print(f"{row['Product']}: price={row['Price']}, stock={row['Stock']}")
