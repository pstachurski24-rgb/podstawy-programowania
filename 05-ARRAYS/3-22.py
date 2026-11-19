
arr = [7, 9, 2, 4, 5, 6]

even = []
odd = []

for number in arr:
    if number % 2 == 0:
        even.append(number)
    else:
        odd.append(number)

arr = even + odd

print(arr)
