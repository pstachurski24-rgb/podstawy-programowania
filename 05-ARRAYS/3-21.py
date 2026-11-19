
arr = [2.5, 7.8, 3.1, 9.4, 5.6, 12.3]

value = float(input("Enter value: "))

count = 0

for number in arr:
    if number > value:
        count += 1

print("Array:", arr)
print("Numbers greater than", value, ":", count)
