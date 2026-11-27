from pathlib import Path
BASE = Path(__file__).resolve().parent

# Section 4, item 7: analyze a user-selected text file.
file_name = input('File name: ').strip()
try:
    with (BASE / file_name).open('r', encoding='utf-8') as file:
        content = file.read()
    print('Number of lines:', len(content.splitlines()))
    print('Number of characters:', len(content))
    print('Number of words:', len(content.split()))
except FileNotFoundError:
    print('File not found.')
except (OSError, UnicodeError) as error:
    print('Cannot read the file:', error)
