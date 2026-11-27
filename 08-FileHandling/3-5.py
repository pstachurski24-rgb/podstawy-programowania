# Section 3, item 5: regex validation.
import re
username = input('Username: ')
password = input('Password: ')
username_pattern = r'[a-z]{6,}'
password_pattern = r'[A-Za-z0-9_]{8,}'
username_match = re.fullmatch(username_pattern, username)
password_match = re.fullmatch(password_pattern, password)
if username_match and password_match:
    print('Username and password meet the requirements.')
else:
    print('Invalid username or password.')
