from pathlib import Path
BASE = Path(__file__).resolve().parent

# Section 4, item 9: extensions of exactly 4 characters.
import re
with (BASE / 'files.txt').open('r', encoding='utf-8') as file:
    for line in file:
        name = line.strip()
        if re.search(r'\.[A-Za-z0-9]{4}$', name):
            print(name)
