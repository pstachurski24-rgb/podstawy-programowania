from pathlib import Path
BASE = Path(__file__).resolve().parent

# Section 4, item 10: Graphic Designer fields using CSV.
import csv
print('GRAPHIC DESIGNERS')
print('=================')
with (BASE / 'it_company.csv').open('r', encoding='utf-8', newline='') as file:
    reader = csv.DictReader(file)
    for row in reader:
        if row['Job Title'] == 'Graphic Designer':
            print(f"{row['First Name']} {row['Last Name']},{row['Email']}")
