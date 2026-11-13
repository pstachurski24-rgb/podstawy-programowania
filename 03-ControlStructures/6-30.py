# Lottery coupon 1-49

for row in range(1, 8):
    number = row

    while number <= 49:
        print(number, end="\t")
        number += 7

    print()