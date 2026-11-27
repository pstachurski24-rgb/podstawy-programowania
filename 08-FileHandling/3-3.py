# Section 3, item 3: regex101.com practice (test each pattern there too).
import re

text = ("Alice was born on March 12, 1992. Her brother, John, was born on "
        "June 5, 1988. They have a mutual friend named Mike, whose phone number "
        "is 555-123-4567. In their hometown, which has a population of 1,234 "
        "or 1,235 people, a holiday festival is held every year on December 25. "
        "Alice works in an office with 30 employees. Her phone number is "
        "555-765-4321.")

patterns = {
    'Dates with year': r'\b[A-Z][a-z]+\s+\d{1,2},\s+\d{4}\b',
    'Phone numbers': r'\b\d{3}-\d{3}-\d{4}\b',
    'Thousands': r'\b\d{1,3}(?:,\d{3})+\b',
    'Capitalized names': r'\b[A-Z][a-z]+\b',
    # Standalone digits, not fragments of dates, phones or comma-separated values:
    'Whole numbers': r'(?<![\w,\-])\d+(?![\w,\-])',
}
for label, pattern in patterns.items():
    print(label, '=>', re.findall(pattern, text))
