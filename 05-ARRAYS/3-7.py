
arr = [15, 8, 31, 47, 2, 19]

total = 0

for number in arr:
    total += number

average = total / len(arr)

print("Array:", *arr)
print("Arithmetic mean:", average)
