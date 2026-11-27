from pathlib import Path
BASE = Path(__file__).resolve().parent

# Section 1, item 6: sort country lines alphabetically.
def read_from_file(name):
    with (BASE / name).open('r', encoding='utf-8') as file:
        return file.read()

file_content = read_from_file('countries.txt')
file_lines = file_content.splitlines()
for line in sorted(file_lines):
    print(line)
