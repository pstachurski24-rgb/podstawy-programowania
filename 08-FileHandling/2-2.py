from pathlib import Path
BASE = Path(__file__).resolve().parent

# Section 2, item 2: alphabetical wonders.
seven_wonders = [
    'Great Wall of China', 'Petra', 'Christ the Redeemer',
    'Machu Picchu', 'Chichen Itza', 'Roman Colosseum', 'Taj Mahal'
]
file_name = BASE / 'seven_wonders.txt'
with file_name.open('w', encoding='utf-8') as file:
    for item in sorted(seven_wonders):
        file.write(item + '\n')
print('Saved:', file_name.name)
