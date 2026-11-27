from pathlib import Path
BASE = Path(__file__).resolve().parent

# Section 1, item 8: display text and count words.
word_count = 0
with (BASE / 'pets.txt').open('r', encoding='utf-8') as file:
    for line in file:
        print(line, end='')
        word_count += len(line.split())
print('\nNumber of words:', word_count)
