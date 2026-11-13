# Print 20 random integers from 5 to 10

import random

for i in range(20):
    number = random.randint(5, 10)
    print(number, end=" ")