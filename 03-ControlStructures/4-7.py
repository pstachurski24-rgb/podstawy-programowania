total = 0

for i in range(1, 11):
    if i % 2 != 0:
        continue

    total += i

print("Sum of even numbers in range 1-10:", total)