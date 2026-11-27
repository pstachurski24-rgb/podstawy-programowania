from pathlib import Path
BASE = Path(__file__).resolve().parent

# Section 4, item 5: show five lines per page.
with (BASE / 'it_company.csv').open('r', encoding='utf-8') as file:
    while True:
        batch = [file.readline() for _ in range(5)]
        batch = [line for line in batch if line]
        if not batch:
            break
        for line in batch:
            print(line, end='')
        print()  # Leave a line before the prompt.
        input('Press Enter key...')
