from pathlib import Path
BASE = Path(__file__).resolve().parent

# Section 4, item 4: handles missing file safely.
try:
    with (BASE / 'missing_file.txt').open('r', encoding='utf-8') as file:
        print(file.read())
except FileNotFoundError:
    print('The file does not exist.')
print('Program continues.')
