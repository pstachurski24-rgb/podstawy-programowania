
def f(number):
    digits = str(number)
    total = 0

    for digit in digits:
        if digits.count(digit) > 1:
            total += int(digit)

    return total


print(f(1027))
print(f(230335))
print(f(513553007))
