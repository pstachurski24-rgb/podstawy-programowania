from pathlib import Path
BASE = Path(__file__).resolve().parent

# Section 1, item 5: numbered countries.
with (BASE / 'countries.txt').open('r', encoding='utf-8') as file:
    for number, line in enumerate(file, start=1):
        print(f'{number}. {line}', end='')
