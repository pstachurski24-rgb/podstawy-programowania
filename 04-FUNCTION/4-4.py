
def sum_digits(number):
    total = 0

    for digit in str(abs(number)):
        total += int(digit)

    return total

number = int(input("Enter integer: "))
print("Sum of digits:", sum_digits(number))
