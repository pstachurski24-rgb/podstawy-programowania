from pathlib import Path
BASE = Path(__file__).resolve().parent

# Section 4, item 12: numbers and their squares/cubes.
file_name = BASE / 'powers.txt'
with file_name.open('w', encoding='utf-8') as file:
    for number in range(1, 101):
        line = f'{number},{number ** 2},{number ** 3}'
        print(line)
        file.write(line + '\n')
