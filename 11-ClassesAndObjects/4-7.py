# 4-7: Statistics (optional keyboard input; default UEK values)
from statistics import median

class Statistics:
    def __init__(self):
        self.numbers = []

    def add_number(self, value):
        self.numbers.append(float(value))

    def display_numbers(self):
        print('Numbers:', ' '.join(f'{v:g}' for v in self.numbers))

    def report(self):
        if not self.numbers:
            print('No numbers provided')
            return
        self.display_numbers()
        print('Minimum:', min(self.numbers))
        print('Maximum:', max(self.numbers))
        print('Mean:', sum(self.numbers)/len(self.numbers))
        print('Median:', median(self.numbers))

values = input('Numbers separated by spaces (Enter = 12 37 6 9 17): ').strip()
values = values or '12 37 6 9 17'
stats = Statistics()
for number in values.split():
    stats.add_number(number)
stats.report()
