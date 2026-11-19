
arr = [8, 2, 5, 1, 9]

squares = []

for number in arr:
    squares.append(number ** 2)

print("Array:", *arr)
print("2nd power:", *squares)
