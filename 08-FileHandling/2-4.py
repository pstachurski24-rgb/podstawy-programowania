from pathlib import Path
BASE = Path(__file__).resolve().parent

# Section 2, item 4: save Software Engineers to another file.
employees_file = BASE / 'it_company.csv'
position_file = BASE / 'software_engineer.txt'
job_title = 'Software Engineer'
with employees_file.open('r', encoding='utf-8') as input_file:
    with position_file.open('w', encoding='utf-8') as output_file:
        for line in input_file:
            if job_title in line:
                output_file.write(line)
print('Saved:', position_file.name)
