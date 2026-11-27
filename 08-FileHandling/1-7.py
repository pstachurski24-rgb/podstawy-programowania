from pathlib import Path
BASE = Path(__file__).resolve().parent

# Section 1, item 7: total parked cars.
def read_from_file(name):
    with (BASE / name).open('r', encoding='utf-8') as file:
        return file.read()

file_lines = read_from_file('car_park.txt').splitlines()
total = 0
for line in file_lines:
    if line.strip():
        total += int(line)
print('Total cars parked:', total)
