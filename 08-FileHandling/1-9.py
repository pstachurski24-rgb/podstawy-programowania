from pathlib import Path
BASE = Path(__file__).resolve().parent

# Section 1, item 9: numbered Software Engineers.
# Source exercise mentions .csv, although starter snippet says .txt.
job_title = 'Software Engineer'
counter = 1
with (BASE / 'it_company.csv').open('r', encoding='utf-8') as file:
    for line in file:
        if job_title in line:
            print(f'{counter}. {line}', end='')
            counter += 1
