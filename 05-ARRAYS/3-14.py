
arr = [2, 3, 2, 5, 8, 1, 9, 8]

unique_elements = []

for number in arr:
    if arr.count(number) == 1:
        unique_elements.append(number)

print("Array:", *arr)
print("Unique elements:", *unique_elements)
