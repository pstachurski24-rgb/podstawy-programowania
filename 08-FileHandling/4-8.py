# Section 4, item 8: vowels counted using regex.
import re
text = input('Enter text: ')
vowels = re.findall(r'[aeiouAEIOU]', text)
print('Number of vowels:', len(vowels))
