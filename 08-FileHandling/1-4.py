from pathlib import Path
BASE = Path(__file__).resolve().parent

# Section 1, item 4: read countries line by line.
with (BASE / 'countries.txt').open('r', encoding='utf-8') as file:
    for line in file:
        print(line, end='')
