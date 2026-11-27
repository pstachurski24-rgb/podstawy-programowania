from pathlib import Path
BASE = Path(__file__).resolve().parent

# Section 2, item 3: copy a text file.
original_file = BASE / 'healthy_lifestyle.txt'
target_file = BASE / 'copy_healthy_lifestyle.txt'
with original_file.open('r', encoding='utf-8') as file:
    content = file.read()
with target_file.open('w', encoding='utf-8') as file:
    file.write(content)
print('Copied to:', target_file.name)
