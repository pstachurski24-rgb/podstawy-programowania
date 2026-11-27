from pathlib import Path
BASE = Path(__file__).resolve().parent

# Section 4, item 4: intentionally fails on a missing file.
with (BASE / 'missing_file.txt').open('r', encoding='utf-8') as file:
    print(file.read())
