number = int(input("Enter decimal number: "))

original = number
binary = ""

if number == 0:
    binary = "0"
else:
    while number > 0:
        remainder = number % 2
        binary = str(remainder) + binary
        number //= 2

print(f"{original}(10) = {binary}(2)")