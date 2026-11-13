a = 0
b = 1

count = 0

while count < 20:
    print(a, end=" ")

    next_number = a + b
    a = b
    b = next_number

    count += 1